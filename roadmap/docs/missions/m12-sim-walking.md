# M12 · 仿真站立与行走：先站稳，再走路

**全局位置**：紧接 [M11 仿真工程就绪](m11-sim-setup.md)之后。输入是能加载、接触合理的仿真模型；输出是**两个交付物**：①PD 站立 demo（10 分钟不摔 + 抗推恢复）；②一份书面化的行走技术路线决策（经典 MPC/WBC 还是 RL）——[M13](m13-rl-training.md) 沿 RL 线深入训练。

**前置条件**：M11 验收全过（基线体检四项全过）；[Stage 0](../stage-0-foundations.md) 的 PD 站立手感还在——本任务步骤 1 就是它的放大版。

理论背景：[第 14 章 机器人控制基础](/wiki/chapters/chapter-14/)、[第 15 章 运动生成与 Locomotion](/wiki/chapters/chapter-15/)、[第 23 章 仿真与物理引擎](/wiki/chapters/chapter-23/)；平衡理论阶梯的完整版见[阶段 2 总览](../stage-2-biped.md)第 2 节。

## 步骤 1：PD 站立——行走的入场券

【做什么】三件事按序做：

1. **设计零力矩站立姿态**：各关节目标角（踝/膝/髋补偿）让质心投影落在支撑多边形中心附近——用 M11 的 keyframe 起步，微调至不漂；
2. **位置 PD 控制**：接 M11 的频率分层（物理 1 kHz、控制 100 Hz 量级）：

```python
# 位置 PD 主循环：目标角跟踪 + 力矩限幅（限幅与 M11 步骤 3 一致）
tau = kp * (q_des - q) - kd * dq
tau = np.clip(tau, -tau_max, tau_max)
```

3. **判据阶梯逐级验收**：10 s → 60 s → 10 min 无摔倒；然后给躯干一个小冲量扰动，能恢复才算过。增益整定：先 P 后 D——P 加到要抖不抖，再用 D 把抖动压下去；高频抖动先降 P，仍抖就检查仿真步长。

【为什么】站立是行走的子集：站立回路（踝/髋策略）调通，行走只是把平衡点周期性移出支撑域再捕获（[阶段 2](../stage-2-biped.md) 复刻流程 Step 7 的口径）。PD 站立验证的是**模型正确性**——零位、轴向、质量属性（[仿真手册](../playbooks/sim-setup.md)三级火箭第一级），这步过不去，后面全是白费。

【你的情况怎么分析】站不住先别急着调参，按"模型错 → 增益错 → 步长错"顺序排查：零力矩悬挂过了吗（M11 步骤 6）？质心投影算过吗？增益减半现象变吗？

## 步骤 2：平衡理论阶梯——ZMP、LIPM 与分层架构

【做什么】按顺序啃三级（详见[阶段 2](../stage-2-biped.md) 第 2 节）：

1. **[ZMP（零力矩点）](/entry/ent_paper_zero_moment_point_2024/)**：地面反力等效作用点落在支撑多边形内才不倾倒。在仿真里画出/打印 ZMP 轨迹，观察它何时跑出支撑域、机器人何时倒；
2. **LIPM 线性倒立摆**：把全身简化成"质心 + 无质量腿"，质心高度恒定假设下有解析解，平地 ZMP 估算：

```
# 平地 LIPM 近似：x_zmp = x_com - (z_com / g) * x_ddot_com
x_zmp = x_com - (z_com / 9.81) * x_ddot_com
```

3. **[步态规划](/entry/ent_method_gait_planning/)与分层架构**：给定目标速度，决定摆动脚落点与双支撑/摆动相切换时序（入门经典是 LIPM + 捕获点分析：不迈步会摔到哪儿，就踩到哪儿）；并建立分层认知：**落点规划 → 质心轨迹 → WBC 分配 → 关节力矩**。

【为什么】ZMP 是双足稳定性最经典的判据，是排查一切摔倒的第一工具；分层架构让你能定位"走歪了"是落点错（决策层）还是力控没跟上（执行层）。不建这个认知直接上 RL，摔了分不清是模型错还是控制错。系统推导见 [第 14 章](/wiki/chapters/chapter-14/)与[第 15 章](/wiki/chapters/chapter-15/)。

【你的情况怎么分析】走 RL 路线：概念理解即可（策略自己学落点），但 ZMP 观察练习必做；走 MPC 路线：LIPM 推导必须吃透，它是步骤 3 里 MPC 的预测模型。

## 步骤 3：经典路线实操——跑通 OpenLoong MPC+WBC

【做什么】跑通 OpenLoong-Dyn-Control：部署在 [MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/) 上的 MPC+WBC 全身控制框架，自带**行走/跳跃/盲踩障碍**三个示例，已在实物样机实现行走与盲踩障碍，Apache-2.0（`data/roadmap/research/openloong-qinglong.md`）：

```bash
git clone https://github.com/loongOpen/OpenLoong-Dyn-Control.git
# 依赖安装与编译严格按仓库 README（版本随仓库更新变化，按你所选版本核对）
```

跑通后**动手改**并记录：MPC 权重、步频、步长，每改一项记录行走质量变化（稳定性/速度跟踪/抖动）。同时理清分工：[MPC（模型预测控制）](/entry/ent_method_model_predictive_control/)滚动预测一个时间窗、解带约束优化，管"未来几步怎么踩、怎么用力"；[WBC（全身控制）](/entry/ent_method_whole_body_control/)把任务目标按优先级分配到全身关节力矩，管"这一拍各关节出多少力"；[Pinocchio](/entry/ent_software_pinocchio/)是高效刚体动力学库，MPC/WBC 算动力学项几乎必用它。

【为什么】这是零硬件学全尺寸人形经典控制管线的现成教材——青龙整机 185 cm/80 kg+ 个人无法复刻，但控制框架随便学（档案口径）。亲手改参看到行走质量变化，比读十篇论文建立直觉快。

【你的情况怎么分析】编译跑不起来：严格按仓库 README 核对依赖版本，别自行升级。数学跟不上：先当"可调参的黑盒"用，把"参数→现象"对应关系记下来，推导回头补。

## 步骤 4：RL 路线预演——只证明管线通，不开始训练

【做什么】只做一件事：把 M13 要用的官方环境在你机器上跑通——[Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) 人形示例或 [MuJoCo Playground](/entry/ent_paper_202501_mujoco_playground_2025/)，确认 obs/action/reward 数据流能转起来，记录 FPS 与显存/CPU 占用：

```bash
# Isaac Lab 官方人形环境冒烟测试（任务名与脚本路径按你所选版本官方文档核对）
./isaaclab.sh -p <官方 RL 示例脚本> --task=<人形任务名> --num_envs=16 --headless --max_iterations=2
# 记录：FPS、nvidia-smi 显存占用、obs/action 维度
```

**不开始训练**：跑官方基线、换自己模型、调奖励是 [M13](m13-rl-training.md) 步骤 1–3 的事，本步只做管线彩排，证明"到我这台机器上能跑"。

【为什么】RL 栈的环境/依赖/版本问题极其耗时，现在暴露，M13 就能直接开训；FPS 与硬件占用数据决定 M13 的并行环境数怎么设（[PPO](/entry/ent_algorithm_ppo/) 吃吞吐）。

【你的情况怎么分析】无 N 卡：MuJoCo Playground/MJX 或 CPU 小规模环境先验证数据流；有卡：Isaac Lab 官方人形任务空跑两 iter 或加载官方预训练 checkpoint 评测，截图数据流日志存档。

## 步骤 5：路线决策——写下来，别漂移

【做什么】对照下表选定主线，写入建造日志（可以两条都试，但写明主次与理由）：

| 维度 | 经典 MPC/WBC | RL（[PPO](/entry/ent_algorithm_ppo/) + 域随机化） |
|---|---|---|
| 开发量 | 推导实现量大，但有 OpenLoong 现成框架可学 | 训练管线现成，奖励工程是新工作量 |
| 数学门槛 | 高（动力学 + 优化） | 中（概念即可上手，调奖励是实验科学） |
| 硬件需求 | CPU 可跑（MuJoCo） | N 卡训练更顺（Isaac Lab），CPU 也行但慢一个量级 |
| 可解释性 | 高——每个力矩有出处 | 低——策略是黑盒 |
| 实机案例 | BRUCE 可变周期 MPC 实现行走/跑步/跳跃（bruce-westwood.md） | ToddlerBot、Berkeley 均实现零样本 [sim-to-real](/entry/ent_method_sim_to_real/) 行走（各档案） |

【为什么】两条路都通，但你的时间只够主线一条；决策写下来，是为了 M13/[M14](m14-sim-to-real.md) 排查时方向不漂移。[阶段 2](../stage-2-biped.md) 决策树的口径同样适用：第一台的核心 KPI 是"走起来"，不是一步到位。

【你的情况怎么分析】数学强 + 想吃透控制 → MPC/WBC 主线，OpenLoong 就是教材；ML 背景 + 有 GPU → RL 主线直通 M13；都想试 → 主线 RL、辅线读 OpenLoong 代码理解控制结构（或反过来），但日志里必须写清谁是主线。

## 验收标准

- [ ] PD 站立 10 min 仿真时间不摔倒，躯干轻推后能恢复（录屏存档）。
- [ ] ZMP 观察记录成文：站立与推扰下 ZMP 是否留在支撑多边形内，有图有结论。
- [ ] OpenLoong 示例或官方 RL 环境至少一个跑通（录屏 + 改参/数据流记录存档）。
- [ ] 路线决策书面化：主线/辅线、理由、预期风险，写入建造日志。
- [ ] 若主线为 RL：M13 所需官方环境确认可跑，FPS 与硬件占用有记录。

## 常见坑与排查

| 症状 | 可能原因 | 排查动作 |
|---|---|---|
| PD 站立高频抖动、嗡嗡作响 | P 增益过高 / 仿真步长过大 | P 减半复测；减小步长对比；查是否把阻尼写成了刚度 |
| 站立缓慢向一侧倾倒 | 质心投影偏离支撑域中心 / 模型左右不对称 | 打印质心投影；回 M10 查镜像关节轴向 |
| 脚底溜冰站不住 | 摩擦系数过低或接触太软 | 回 M11 步骤 4 调 friction 与 solref |
| 一推就倒、恢复不了 | D 增益不足 / 踝力矩限幅太死 | 加大 D 复测；核对踝执行器限幅（M11 步骤 3） |
| 直接跳 RL，摔倒分不清谁的错 | 跳过平衡理论阶梯 | 回步骤 2 做 ZMP 观察；PD 站立验收后再谈 RL |
| OpenLoong 示例跑不起来 | 依赖版本错配 | 严格按仓库 README 核对版本，不自行升级依赖 |

## 配套阅读

- 上一任务：[M11 · 仿真环境与模型转换](m11-sim-setup.md)
- 下一任务：[M13 · 强化学习训练](m13-rl-training.md)
- 理论背景：[第 14 章 机器人控制基础](/wiki/chapters/chapter-14/)、[第 15 章 运动生成与 Locomotion](/wiki/chapters/chapter-15/)、[第 23 章 仿真与物理引擎](/wiki/chapters/chapter-23/)、[附录 C 软件与仿真平台清单](/wiki/appendices/appendix-c/)
- [仿真环境搭建手册](../playbooks/sim-setup.md) · [阶段 2 总览](../stage-2-biped.md)
