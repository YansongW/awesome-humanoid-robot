# M11 · 仿真环境与模型转换：在数字世界先摔一万次

**全局位置**：紧接 [M10 的 URDF 模型包](m10-urdf-modeling.md)之后，是 Stage 2 仿真的第一棒。输入是 M10 交付的模型包，输出是一个**跑通的仿真工程**——模型加载无警告、接触行为合理、执行器/传感器建模完成、基线体检全过。[M12](m12-sim-walking.md) 用它站立行走，[M13](m13-rl-training.md) 用它训练策略。

**前置条件**：M10 验收全过（模型包入库、惯性参数已核）；[Stage 0](../stage-0-foundations.md) 步骤 4 的 PD 站立手感还在。

理论背景：[第 23 章 仿真与物理引擎](/wiki/chapters/chapter-23/)、[第 22 章 软件中间件](/wiki/chapters/chapter-22/)、[附录 C 软件与仿真平台清单](/wiki/appendices/appendix-c/)；引擎选型总表见[仿真环境搭建手册](../playbooks/sim-setup.md)第一步。

## 步骤 1：引擎安装与官方基线验证

【做什么】两条主线二选一（或都装）：

- **[MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/)**：`pip install mujoco`，纯 CPU 可跑；
- **[Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/)**（跑在 [Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/) 之上）：需 NVIDIA GPU，conda 环境，Isaac Lab 与 Isaac Sim 版本严格匹配——组合随 release 变化，以官方安装文档为准，按你所选版本自行核对。

装完先跑官方示例（MuJoCo 自带 humanoid 模型 / Isaac Lab 的 H1 人形示例），再碰自己的模型：

```bash
# MuJoCo：CPU 即可；加载官方自带人形模型验证（模型路径随版本变化，按你所选版本核对）
pip install mujoco
python -m mujoco.viewer --mjcf=$(python -c "import mujoco, os; print(os.path.join(os.path.dirname(mujoco.__file__), 'model', 'humanoid', 'humanoid.xml'))")
# Isaac Lab：conda 环境 + 官方 H1 示例（安装步骤与任务名以官方文档为准）
conda create -n isaaclab python=3.10 -y && conda activate isaaclab
git clone https://github.com/isaac-sim/IsaacLab.git
```

【为什么】官方示例帮你隔离"环境问题"与"模型问题"——示例跑不起来是装错了，示例能跑、你的模型不能跑才是模型错了。选型逻辑（详见[仿真手册](../playbooks/sim-setup.md)）：MuJoCo 接触质量高，是腿足控制研究的事实标准；Isaac Lab GPU 大规模并行，为 RL 训练而生。开源锚点：ToddlerBot 用 MuJoCo/MJX、Berkeley Humanoid Lite 基于 Isaac Lab、OpenLoong 的 MPC+WBC 部署在 MuJoCo（`data/roadmap/research/` 各档案）。

【你的情况怎么分析】无 N 卡：MuJoCo 一条路走到底，控制研究与 CPU 小规模 RL 都够；有 RTX 卡且走 RL 路线：都装，MuJoCo 调模型、Isaac Lab 训策略（Berkeley 即此组合）；要 ROS 全栈集成测试：另加 [Gazebo](/entry/ent_software_gazebo/)，别纠结它的物理精度。

## 步骤 2：URDF → MJCF/USD 转换与复核

【做什么】把你的 [URDF](/entry/ent_technology_urdf_robot_description_format_2024/) 转成目标格式：MuJoCo 可直接编译 URDF 并另存 [MJCF](/entry/ent_technology_mjcf_simulation_format_2024/)，进 Isaac 用官方 URDF Importer 转 USD：

```bash
# MuJoCo Python API 编译 URDF 并导出 MJCF（API 细节按你所选版本核对）
python -c "import mujoco; m = mujoco.MjModel.from_xml_path('robot.urdf'); mujoco.mj_saveLastXML('robot_mjcf.xml', m); print('converted OK')"
```

四类经典转换错误，逐个排查：

| 错误 | 症状 | 修法 |
|---|---|---|
| 惯性张量非正定 | 编译报错/模型抽搐 | 回 M10 步骤 3 用 CAD 重导，检查 ixx/iyy/izz 三角不等式 |
| mesh 单位 mm 当 m | 模型大/小 1000 倍 | 缩放 ×0.001 或在导出时统一为米 |
| mesh 路径大小写 | Linux 下找不到文件 | 路径与文件名全小写规范化 |
| 关节轴向约定差异 | 运动方向全反 | viewer 逐关节驱动核对（M10 已初验，这里做仿真内复核） |

转换后手动修补 MJCF：`<compiler angle="radian" .../>` 统一角度单位、补回转换丢掉的关节限位、确认坐标系约定。

【为什么】URDF 为可视化与 ROS 工具链而生，只支持树状结构、执行器模型弱；MJCF 为仿真与控制而生——编译期自动算惯性，执行器与传感器是一等公民（第 23 章 23.4 节）。每次转换都有信息损耗，小错误会被物理引擎放大成"一跑就飞"。

【你的情况怎么分析】复刻开源平台：直接用官方维护的 MJCF/USD（Berkeley 三格式齐全，档案），本步只做逐关节复核；自研模型：转换产物与修补记录一起进版本管理，M13 改模型时你才知道改了什么。

## 步骤 3：执行器建模——限幅虚高 = sim-to-real 自杀

【做什么】MJCF 里给每个可控关节配执行器：力控用 `motor`，位置控制用 `position`；三条纪律：

1. **力矩限幅** = M01 指标表的峰值扭矩（M10 步骤 4 已写入 effort，转换后核对没丢）；
2. **速度限幅**取 M01 额定转速换算值；
3. **执行器动态**用一阶低通近似真实响应，时间常数先估 5–20 ms（工程建议值，[M14](m14-sim-to-real.md) 用[系统辨识](/entry/ent_method_system_identification/)实测回填）。

```xml
<actuator>
  <!-- ctrlrange 填 M01 指标表峰值扭矩，严禁虚高 -->
  <position joint="l_knee_pitch" kp="40" forcerange="-33 33" ctrllimited="true" ctrlrange="-1.2 1.2"/>
  <!-- 一阶低通近似执行器动态：dynprm 为时间常数（秒），5–20 ms 工程建议值起步 -->
  <general joint="l_hip_pitch" dyntype="filter" dynprm="0.01" gaintype="fixed" gainprm="1" ctrllimited="true" ctrlrange="-20 20"/>
</actuator>
```

【为什么】RL 会学出限幅内的动作：限幅虚高，策略就学出实机执行不了的动作，sim-to-real 直接失败（M10 步骤 4 的规则）。真实执行器不是理想力矩源——电流环响应与通信延迟让它近似一阶惯性环节；不建模这段动态，仿真里能用的增益到实机就是振荡。

【你的情况怎么分析】总线舵机/QDD 准直驱：`position` + 力矩限幅最贴近实机工作方式；计划纯力控：`motor` + 低通。时间常数拿不准先取 10 ms 量级起步，M14 回来校。PD 增益写在模型里（kp/kv）还是写在控制器代码里：写模型里换控制器不用重调，写代码里便于在线整定——选一个并全程统一。

## 步骤 4：接触与摩擦——双足的一切发生在脚底

【做什么】四个动作：

1. **足底摩擦系数**：橡胶/PLA 对地板的量级先取 0.6–1.0 区间试（具体取值需按材料自行确认）；
2. **接触求解参数**：`solref`（时间常数、阻尼比）调接触软硬——太软脚陷地，太硬数值抖动；`solimp` 控制约束阻抗曲线，先用默认附近值；
3. **自碰撞对裁剪**：用 `exclude` 只留必要接触对，接触对数量直接决定仿真速度；
4. **地板与扰动接口**：地板 geom 参数化，预留外力扰动入口——M13 的[域随机化](/entry/ent_method_domain_randomization/)要随机摩擦、要推机器人。

```xml
<default>
  <!-- solref=(时间常数, 阻尼比)：典型取 2–10×timestep，越小接触越硬 -->
  <geom solref="0.01 1" solimp="0.9 0.95 0.001" friction="0.8 0.005 0.0001"/>
</default>
<contact><exclude body1="l_thigh" body2="l_shank"/></contact>  <!-- 排除不可能相碰的连杆对 -->
```

【为什么】接触参数是 sim-to-real 差距的大头，必须与"足底材料-地面材料"成对标定并纳入后续域随机化范围（第 23 章 23.4.4 节）。先把标称值调合理，再谈随机化。

【你的情况怎么分析】拿不准摩擦：把足底材料样品放在目标地板上，用弹簧秤拉滑块估算量级。打印 PLA 足底与橡胶鞋底差一截，别抄别人的数。

## 步骤 5：传感器仿真与观测管线

【做什么】按实机 BOM 建观测管线：[IMU](/entry/ent_component_imu_2024/)（姿态/角速度 + 噪声模型）、关节编码器（位置/速度，可加量化）、足底接触力；并定下频率分层：

```xml
<sensor>
  <framequat objtype="site" objname="imu_site" noise="0.001"/>
  <gyro site="imu_site" noise="0.005"/>
  <jointpos joint="l_knee_pitch"/>  <jointvel joint="l_knee_pitch"/>
</sensor>
```

```python
# 物理 1 kHz、控制 100 Hz（工程建议值，按你的控制器带宽与总线速率核对）
model.opt.timestep = 0.001   # 物理步长
decimation = 10              # 每 10 步物理发一次控制 → 100 Hz
```

**铁律：观测接口与实机传感器一一对应——实机拿不到的观测不进策略**（M13/M14 的共同纪律）。控制频率锚点：ToddlerBot 全状态反馈 50 Hz、Berkeley CAN 总线 250 Hz（各调研档案）。

【为什么】观测是 sim-to-real 最容易作弊的地方：仿真里随手可读的真值（基座线速度、质心位置）实机上都不存在。现在按实机传感器清单建管线，M13 训练零返工；加噪声不是折腾自己，是让策略提前适应真实传感器。

【你的情况怎么分析】实机传感器还没定：先回[传感器选型手册](../playbooks/sensor-selection.md)定 BOM，仿真观测跟着实机走，不反过来。

## 步骤 6：基线健康检查——M12 的入场券

【做什么】四项体检：

1. **零力矩释放**：关掉执行器，自由落体/悬挂——模型不散架、关节有阻尼不乱甩；
2. **初始 keyframe**：站立姿态零输入 10 s 不漂，质心投影稳在支撑域内；
3. **接触力量级**：站立时单脚法向力 ≈ 体重一半量级，不大不小；
4. **仿真速度**：记录 real-time factor（RTF），目标 ≥ 1（RL 吞吐另算）。

【为什么】模型级错误（惯性错、轴向反、限位丢）在 PD 站立时会全部暴露，用被动动力学查最便宜；RTF 决定后面 MPC 实时性与 RL 训练吞吐的天花板。

【你的情况怎么分析】悬挂就散架：惯性或关节定义错，回 M10 步骤 3；RTF < 0.5：查接触对数量、碰撞 mesh 复杂度、步长，别硬扛。

## 验收标准

- [ ] 引擎官方示例跑通（MuJoCo humanoid 或 Isaac Lab H1），录屏/日志存档。
- [ ] 模型加载无 warning；逐关节驱动方向与 M10 约定复核一致。
- [ ] 执行器限幅（力矩/速度/位置）与 M01 指标表逐项一致，无虚高。
- [ ] 零力矩悬挂/自由落体测试通过：不散架、阻尼正常；keyframe 站立 10 s 不漂，接触力量级合理。
- [ ] 观测清单成文：每项注明实机来源（哪个传感器、什么速率），实机拿不到的标注"禁入策略"。
- [ ] real-time factor 记录在案，接触对与碰撞体已裁剪。

## 常见坑与排查

| 症状 | 可能原因 | 排查动作 |
|---|---|---|
| MJCF 编译报惯性张量非正定 | 手写惯量矩阵不满足物理约束 | 回 M10 步骤 3 用 CAD 重导；查 ixx/iyy/izz 三角不等式 |
| 脚陷地或像溜冰 | solref 太软 / 摩擦系数过低 | 回步骤 4 调 solref 时间常数与 friction |
| 仿真比实时慢好几倍 | 接触对太多 / 碰撞 mesh 太复杂 | exclude 裁剪接触对；碰撞体回 M10 步骤 5 简化 |
| 关节运动方向全反 | 度/弧度混用 / 轴向约定差异 | 核对 compiler angle；viewer 单关节逐个复核 |
| URDF 转 USD 后限位丢失 | Importer 选项/版本行为差异 | 转换后逐项核对 limit，缺失手动补回（按你所选版本 Importer 文档核对） |

## 配套阅读

- 上一任务：[M10 · URDF 建模与导出](m10-urdf-modeling.md)
- 下一任务：[M12 · 仿真站立与行走](m12-sim-walking.md)
- 理论背景：[第 22 章 软件中间件](/wiki/chapters/chapter-22/)、[第 23 章 仿真与物理引擎](/wiki/chapters/chapter-23/)、[附录 C 软件与仿真平台清单](/wiki/appendices/appendix-c/)
- [仿真环境搭建手册](../playbooks/sim-setup.md) · [阶段 2 总览](../stage-2-biped.md)
