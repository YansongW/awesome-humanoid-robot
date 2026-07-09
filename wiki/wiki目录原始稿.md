# 《人形机器人：从矿山到市场的知识图谱》
## Wiki 目录（精细化版）

> 基于 Awesome Humanoid Robot 知识图谱的 Wiki 架构  
> 设计原则：以实体为节点、关系为线索、来源为证据、跨层链路为叙事主线

---

## 本书导读

### 如何使用本书
- 技术读者：按“零部件 → 设计 → 控制 → AI → 量产”路径阅读
- 产业读者：按“供应链 → 制造 → 应用 → 市场 → 政策”路径阅读
- 研究读者：按“基础 → 方法 → 数据集 → 仿真 → 基准”路径阅读

### 知识图谱映射说明
- 每个章节末尾附“本章知识图谱锚点”，列出对应实体类型、核心关系与关键 case
- 跨层关系以 → 符号标注链路方向

---

# 第一部分：总论 — 为什么需要一张人形机器人的全景地图

## 第 1 章 人形机器人产业化的核心矛盾
### 1.1 能走的机器人 vs 能卖的机器人
- 演示指标与产品指标的鸿沟
- 可靠性、成本、可维护性、合规性四维约束

### 1.2 从 0 到 1 的七个跃迁
- 实验室样机 → 工程样机 → 小批量 → 量产 → 部署 → 运营 → 规模化复制

### 1.3 系统复杂度来源
- 机械、电子、软件、AI、数据、供应链、法规的强耦合

### 1.4 本书的叙事框架
- 物理层 → 感知层 → 决策层 → 执行层 → 系统层 → 产业层

**本章知识图谱锚点**  
实体：`robot_system`、`component`、`technology`、`method`  
关系：`is_part_of`、`implemented_on`、`applies_to`  
链路：`foundation → principle → formalism → method → system`

---

## 第 2 章 知识图谱构建方法论
### 2.1 信息模型
- 实体 schema：id、type、domain、theoretical_depth、source
- 关系 schema：type、direction、verification、reviewed_by

### 2.2 分层体系
- 00 基础学科
- 01 原材料
- 02 零部件
- 03 制造工艺
- 04 组装集成测试
- 05 量产制造
- 06 设计工程
- 07 AI 模型与算法
- 08 软件中间件
- 09 数据与数据集
- 10 评测基准
- 11 应用市场
- 12 政策法规伦理

### 2.3 跨层关系类型
- `uses`：方法使用数据集
- `requires`：方法依赖硬件
- `is_part_of`：零部件组成整机
- `manufactured_by`：零部件由厂商制造
- `implemented_on`：算法部署于机器人
- `tested_with`：系统经过测试验证
- `applies_to`：工艺/标准适用于系统

### 2.4 AI4Sci 流水线与人机协同
- 自动发现、抽取、去重、关系生成
- 人工审阅队列与 staging 机制

**本章知识图谱锚点**  
实体：`concept`、`principle`、`standard`  
关系：`models`、`analyzes`、`validates_on`  
链路：`data → method → software → robot → manufacturing → application`

---

# 第二部分：物理基础层 — 材料、零部件与供应链

## 第 3 章 关键材料科学
### 3.1 永磁材料
- 钕铁硼磁体的磁性能与退磁曲线
- 稀土元素供应链：镨、钕、镝、铽

### 3.2 结构材料
- 铝镁合金、碳纤维复合材料、工程塑料
- 比刚度、比强度与疲劳寿命

### 3.3 能源材料
- 锂离子电池、固态电池、能量密度与功率密度
- 热失控防护与电池管理系统

### 3.4 半导体与传感器材料
- 功率器件：SiC、GaN
- MEMS 传感器材料与工艺

### 3.5 线缆与接插件
- 柔性线缆、高功率线缆、信号完整性

**本章知识图谱锚点**  
实体：`material`、`component`、`company`  
关系：`is_part_of`、`manufactured_by`、`supplies`  
链路：`material → component → supplier → robot_system`

---

## 第 4 章 执行器：人形机器人的“肌肉”
### 4.1 执行器分类与选型
- 线性执行器 vs 旋转执行器
- 力控执行器与位置控制执行器

### 4.2 电机技术
- 无框力矩电机
- 空心杯电机
- 伺服电机与无刷直流电机
- 电机常数、转矩密度、效率曲线

### 4.3 减速器技术
- 谐波减速器：柔轮、刚轮、波发生器
- RV 减速器：针轮、摆线轮
- 行星滚柱丝杠与行星减速器
- 减速比、背隙、刚性、效率

### 4.4 驱动与功率电子
- 伺服驱动器
- FOC 控制、电流环、速度环、位置环
- 安全关断与制动

### 4.5 执行器集成设计
- 电机 + 减速器 + 驱动器 + 编码器 + 力传感的一体化
- 散热、密封、线缆走线

### 4.6 执行器性能指标
-  Human-Level Actuation Score
- 功率质量比、峰值扭矩、带宽

**本章知识图谱锚点**  
实体：`component`、`component_manufacturer`、`technology`  
关系：`is_part_of`、`manufactures`、`supplies`  
链路：`motor + reducer + drive → actuator → joint → robot`

---

## 第 5 章 传感与感知硬件
### 5.1 视觉传感器
- RGB-D 相机：Intel RealSense、Azure Kinect
- 工业相机与镜头选型
- 多相机标定与时间同步

### 5.2 激光雷达
- Livox Mid-360 等固态激光雷达
- 点云密度、视场角、抗干扰

### 5.3 惯性测量
- IMU：加速度计 + 陀螺仪
- 零偏稳定性、噪声密度、温度漂移

### 5.4 力觉与触觉
- 六维力/力矩传感器
- 指尖触觉阵列
- 力控装配中的传感融合

### 5.5 其他传感器
- 编码器、电位计、温度传感器、电流传感器

**本章知识图谱锚点**  
实体：`component`、`technology`、`software_platform`  
关系：`is_part_of`、`used_by`、`fuses_with`  
链路：`sensor → perception algorithm → state estimation → control`

---

## 第 6 章 计算、电源与热管理
### 6.1 边缘计算平台
- NVIDIA Jetson AGX Orin、Jetson Thor
- CPU/GPU/NPU 异构计算
- 算力、功耗、尺寸、散热约束

### 6.2 安全计算
- 安全 MCU
- 功能安全架构
- 冗余设计与看门狗

### 6.3 电源系统
- 电池包与电池管理系统（BMS）
- 配电系统
- 功耗预算与续航优化

### 6.4 热管理
- 主动散热与被动散热
- 热仿真与热测试

**本章知识图谱锚点**  
实体：`component`、`software_platform`、`technology`  
关系：`requires`、`is_part_of`、`manages`  
链路：`compute + power + thermal → robot_system → safety certification`

---

## 第 7 章 供应商地图与供应链治理
### 7.1 全球供应链格局
- 日本：减速器、精密轴承
- 欧美：高端电机、驱动器、软件
- 中国：电机、结构件、代工、成本优势

### 7.2 关键供应商案例
- Nabtesco（RV 减速器）
- Harmonic Drive Systems（谐波减速器）
- Maxon、Kollmorgen（电机）
- 汇川技术、三花智控、拓普集团、绿的谐波、鸣志电器、CubeMars

### 7.3 供应商认证与质量管理
- 供应商准入（Supplier Qualification）
- IQC、PQC、OQC
- 产能爬坡与交付保障

### 7.4 供应链风险
- 地缘政治、单一来源、原材料波动
- BOM 成本分解与替代方案

**本章知识图谱锚点**  
实体：`company`、`component_manufacturer`、`tier1_supplier`、`oem`  
关系：`manufactures`、`supplies`、`sources_from`  
链路：`raw_material → component_maker → tier1_supplier → oem → robot_system`

---

# 第三部分：设计工程层 — 从概念到图纸

## 第 8 章 人形机器人设计原理
### 8.1 形态学与自由度配置
- 双足 vs 轮式 vs 混合
- 全身自由度：髋、膝、踝、躯干、肩、肘、腕、颈、手指

### 8.2 运动学与动力学
- 正运动学、逆运动学
- 质心、零力矩点（ZMP）、动量
- 浮动基动力学

### 8.3 机械设计
- 连杆、关节、轴承、预紧
- 刚度、阻尼与模态分析
- 轻量化与强度平衡

### 8.4 安全设计
- 固有安全：质量、速度、刚度限制
- 主动安全：碰撞检测、柔顺控制
- 紧急停止系统

### 8.5 数字样机与模型定义
- URDF、MJCF、SDFormat
- CAD/CAE 集成
- Model-Based Definition（MBD）
- 有限元分析（FEA）

**本章知识图谱锚点**  
实体：`technology`、`software_platform`、`method`、`principle`  
关系：`models`、`analyzes`、`applies_to`  
链路：`principle → formalism → CAD/CAE → design → component → robot`

---

## 第 9 章 关键子系统设计
### 9.1 腿部与 locomotion 机构
- 串联 vs 并联腿
- 脚踝柔顺机构
- 足端设计

### 9.2 手臂与操作机构
- 7 自由度机械臂
- 肩部抬高、肘部伸展、腕部灵活度

### 9.3 灵巧手设计
- 自由度、传动、触觉集成
- 抓取策略与手指构型

### 9.4 头部与交互界面
- 显示、语音、表情、 gaze 控制

### 9.5 躯干与电池布局
- 质心集中化
- 维护便利性

**本章知识图谱锚点**  
实体：`component`、`robot_system`、`technology`  
关系：`is_part_of`、`enables`  
链路：`sub_system_design → component_selection → integration → validation`

---

# 第四部分：制造与量产层 — 从图纸到万台

## 第 10 章 制造工艺体系
### 10.1 机加工与精密制造
- CNC、车铣复合、磨削
- 公差与表面粗糙度

### 10.2 电机制造
- 绕线、浸漆、磁钢装配、动平衡

### 10.3 减速器制造
- 柔轮热处理、齿形加工
- 装配精度控制

### 10.4 结构件制造
- 压铸、注塑、3D 打印
- 焊接、粘接、紧固

### 10.5 可制造性设计（DFM）
- 减少零件数
- 标准化紧固件
- 装配可达性

### 10.6 可装配性设计（DFA）
- 自定位、防错、最小工具

**本章知识图谱锚点**  
实体：`technology`、`method`、`component`  
关系：`applies_to`、`produces`、`is_part_of`  
链路：`DFM/DFA → process → component → assembly`

---

## 第 11 章 装配、集成与测试
### 11.1 装配线设计
- 工位划分、节拍平衡
- 人工装配 vs 自动化装配

### 11.2 关节装配
- 电机、减速器、编码器、力传感器的同轴装配
- 预紧力控制

### 11.3 整机集成
- 线缆布置、接插件固定
- 控制器、电池、传感器的安装

### 11.4 系统集成测试台
- 功能测试、性能测试、耐久测试
- 环境测试（温度、振动、跌落）

### 11.5 硬件在环测试（HIL）
- 控制器在环、执行器在环
- 故障注入

### 11.6 标定
- 关节角度标定
- 力传感器标定
- 相机-IMU-激光雷达联合标定

**本章知识图谱锚点**  
实体：`equipment`、`technology`、`robot_system`  
关系：`validates_on`、`tested_with`、`applies_to`  
链路：`assembly → integration → test_bench → HIL → calibration → acceptance`

---

## 第 12 章 认证、合规与质量标准
### 12.1 安全标准
- ISO 13482（个人护理机器人）
- ISO/TS 15066（协作机器人）
- IEC 61508 / ISO 13849（功能安全）

### 12.2 电磁兼容（EMC）
- 辐射发射、传导发射、抗扰度

### 12.3 电气安全
- IEC 62368、IEC 60950

### 12.4 区域准入
- 北美：UL、FCC
- 欧洲：CE、UKCA
- 中国：CR、CCC

### 12.5 认证流程与文档
- 技术文件、测试报告、工厂审查

**本章知识图谱锚点**  
实体：`standard`、`component`、`robot_system`  
关系：`regulates`、`is_regulated_by`、`applies_to`  
链路：`standard → safety_design → component → robot_system → certification`

---

## 第 13 章 量产与规模化
### 13.1 产能爬坡曲线
- 从 NPI 到 MP
- 良率学习曲线

### 13.2 BOM 成本工程
- 成本分解、VA/VE
- 国产化替代与议价能力

### 13.3 工厂设计
- 产线布局、物流、仓储
- 自动化程度选择

### 13.4 质量系统
- SPC、FMEA、8D
- 追溯系统

### 13.5 售后服务与备件
- 维修策略、备件预测
- OTA 升级与远程诊断

### 13.6 机群管理
- Fleet Management Platform
- 数据采集、任务调度、状态监控

**本章知识图谱锚点**  
实体：`technology`、`software_platform`、`robot_system`、`oem`  
关系：`manages`、`applies_to`、`produces`  
链路：`BOM → DFM → assembly → test → certification → ramp → fleet_management`

---

# 第五部分：控制与运动层 — 让机器人动起来

## 第 14 章 机器人控制基础
### 14.1 刚体动力学
- 欧拉-拉格朗日方程
- 浮动基动力学
- 接触约束

### 14.2 反馈控制
- PID、阻抗控制、导纳控制
- 力位混合控制

### 14.3 全身控制
- 质心-动量控制
- 任务优先级与零空间投影
- QP 优化框架

### 14.4 模型预测控制（MPC）
- 步态优化
- 接触序列规划
- 实时求解器

**本章知识图谱锚点**  
实体：`principle`、`formalism`、`method`、`component`  
关系：`requires`、`implemented_on`  
链路：`dynamics → control_law → MPC → software → compute → actuator`

---

## 第 15 章 运动生成与 Locomotion
### 15.1 步态规划
- 步态周期、支撑相、摆动相
- ZMP 与捕获点

### 15.2 基于优化的运动生成
- 直接配点法、 shooting method
- 非线性规划求解

### 15.3 强化学习 Locomotion
- PPO、SAC、 curriculum learning
-  sim-to-real 迁移

### 15.4 鲁棒性与恢复
- 外部扰动抑制
- 跌倒检测与恢复

**本章知识图谱锚点**  
实体：`method`、`algorithm`、`software_platform`  
关系：`uses`、`implemented_on`  
链路：`method → simulator → sim-to-real → robot_system`

---

## 第 16 章 操作与抓取
### 16.1 抓取模型
- 力闭合、形闭合
- GRASP 分类法

### 16.2 运动规划
- MoveIt、OMPL
- 碰撞检测、轨迹优化

### 16.3 灵巧操作
- 指尖力控
- 滑动、插入、旋转

### 16.4 全身操作
- 移动操作
- 双臂协调

**本章知识图谱锚点**  
实体：`method`、`software_platform`、`technology`  
关系：`uses`、`implemented_on`  
链路：`grasp_planning → motion_planning → whole_body_control → robot`

---

## 第 17 章 遥操作与人机协作
### 17.1 遥操作架构
- 主从控制
- 力反馈
- 双边控制稳定性

### 17.2 典型遥操作系统
- ALOHA
- Mobile ALOHA
- HumanPlus Shadowing System

### 17.3 数据采集
- 遥操作数据的质量与多样性
- 低成本遥操作方案

### 17.4 人机协作安全
- 协作速度、力限
- 意图预测

**本章知识图谱锚点**  
实体：`technology`、`dataset`、`method`  
关系：`uses_data`、`requires`、`implemented_on`  
链路：`teleoperation → dataset → imitation_learning → policy`

---

# 第六部分：AI、模型与数据层

## 第 18 章 模仿学习与策略学习
### 18.1 行为克隆
- 数据集构建、模型架构、训练目标

### 18.2 扩散策略（Diffusion Policy）
- 动作生成建模
- 多模态动作分布

### 18.3 动作分块（Action Chunking）
- ACT 框架
- 时序一致性

### 18.4 强化学习与离线 RL
- 奖励设计
- 样本效率

### 18.5 Sim-to-Real for Policy
- Domain randomization
- Domain adaptation
- System identification

**本章知识图谱锚点**  
实体：`paper`、`method`、`dataset`  
关系：`uses_dataset`、`implemented_on`  
链路：`dataset → diffusion_policy/ACT → robot_system`

---

## 第 19 章 视觉-语言-动作模型（VLA）
### 19.1 从 VLM 到 VLA
- 预训练视觉-语言模型
- 动作空间对齐

### 19.2 代表性模型
- RT-2：VLA 的开山之作
- OpenVLA：开源可微调
- GR00T N1：NVIDIA 通用人形模型
- π0 / π0-FAST：Physical Intelligence

### 19.3 训练数据与规模化
- Open X-Embodiment 数据集联盟
- 数据混合、权重、筛选

### 19.4 推理与部署
- 低延迟推理
- 云端 vs 边缘部署

**本章知识图谱锚点**  
实体：`paper`、`method`、`dataset`、`robot_system`  
关系：`uses_dataset`、`implemented_on`、`requires`  
链路：`open_x_embodiment → VLA → compute → robot_system`

---

## 第 20 章 世界模型与长期推理
### 20.1 世界模型概述
- 状态预测、动作后果预测
- 基于模型的强化学习

### 20.2 视频生成世界模型
- Sora-like 模型在机器人中的应用
- 动作条件视频预测

### 20.3 规划与推理
- 任务规划（Task Planning）
- 符号-神经混合推理

### 20.4 开放世界泛化
- 未见物体、未见环境
- 常识推理

**本章知识图谱锚点**  
实体：`method`、`paper`、`concept`  
关系：`models`、`requires`  
链路：`world_model → planner → policy → robot`

---

## 第 21 章 数据基础设施
### 21.1 数据采集系统
- 遥操作数据采集
- 动作捕捉系统（OptiTrack、Vicon）
- 自监督数据采集

### 21.2 公开数据集
- Open X-Embodiment
- DROID、RH20T、AMASS
- 数据集许可证与使用边界

### 21.3 数据工程
- 数据清洗、去重、标注
- 数据版本管理
- 数据分布与偏差分析

### 21.4 车队数据飞轮
- 部署后数据采集
- 失败案例挖掘
- 持续学习与模型更新

**本章知识图谱锚点**  
实体：`dataset`、`technology`、`software_platform`  
关系：`uses_data`、`used_with`、`used_by`  
链路：`data_collection → dataset → model_training → deployment → fleet_data → retraining`

---

# 第七部分：软件与仿真层

## 第 22 章 软件中间件
### 22.1 ROS 2 生态
- 节点、话题、服务、动作
- DDS 与实时性

### 22.2 实时操作系统
- Linux RT-PREEMPT、QNX、Zephyr
- 调度、确定性、延迟

### 22.3 通信总线
- EtherCAT、CAN Bus、CANopen
- 时间同步、带宽、可靠性

### 22.4 运动规划库
- MoveIt、OMPL、Pinocchio、Drake

### 22.5 数据与监控平台
- 日志、指标、可视化
- Fleet Management

**本章知识图谱锚点**  
实体：`software_platform`、`technology`  
关系：`used_by`、`requires`  
链路：`ROS2 → middleware → planning → control → robot`

---

## 第 23 章 仿真与物理引擎
### 23.1 物理引擎对比
- MuJoCo
- NVIDIA Isaac Sim / Isaac Lab
- Genesis
- Drake
- Gazebo

### 23.2 仿真资产
- URDF、MJCF、USD
- 网格、材质、碰撞体

### 23.3 Sim-to-Real
- Domain randomization
- Domain adaptation
- 系统辨识

### 23.4 数字孪生
- 工厂数字孪生
- 机器人数字孪生
- 虚实同步

**本章知识图谱锚点**  
实体：`software_platform`、`technology`、`robot_system`  
关系：`models`、`used_by`、`tested_with`  
链路：`simulator → policy_training → sim-to-real → robot_system`

---

## 第 24 章 端到端软件栈
### 24.1 感知栈
- 视觉检测、分割、深度估计
- 多传感器融合

### 24.2 决策栈
- 任务规划、动作规划
- VLA/LLM 作为高层控制器

### 24.3 执行栈
- 轨迹跟踪、力控、全身控制

### 24.4 安全与故障处理
- 故障检测、降级模式、紧急停止
- 功能安全架构

### 24.5 人机交互
- 语音、视觉、触觉交互
- 自然语言指令理解

**本章知识图谱锚点**  
实体：`software_platform`、`method`、`component`  
关系：`uses`、`requires`、`is_part_of`  
链路：`perception → planning → control → actuation → safety`

---

# 第八部分：评测、基准与验证

## 第 25 章 机器人评测体系
### 25.1 仿真基准
- ManiSkill、RoboSkills、Isaac Gym Benchmarks

### 25.2 真实世界任务基准
- 操作任务、移动任务、双臂任务

### 25.3 硬件评测
- Human-Level Actuation Score
- 动态性能、效率、寿命

### 25.4 安全性基准
- 碰撞力、紧急停止响应
- 功能安全验证

### 25.5 可重复性与标准化
- 测试协议、环境配置、度量指标

**本章知识图谱锚点**  
实体：`benchmark`、`method`、`robot_system`  
关系：`evaluates`、`tested_with`  
链路：`benchmark → method/robot → metric → comparison`

---

# 第九部分：整机、企业与市场

## 第 26 章 整机系统案例
### 26.1 Tesla Optimus
- 系统架构、执行器、供应链
- 量产策略与进展

### 26.2 Unitree H1 / G1
- 硬件平台、开源生态
- 科研与商业路径

### 26.3 Figure 02
- 面向工业场景的设计
- 与 OpenAI/BMW 的合作

### 26.4 波士顿动力 Atlas
- 液压到电动的转变
- 动态运动能力

### 26.5 其他整机
- Agility Robotics Digit
- Apptronik Apollo
- 1X Technologies NEO
- 傅利叶、宇树、智元、优必选等中国厂商

**本章知识图谱锚点**  
实体：`robot_system`、`company`、`component`  
关系：`is_part_of`、`manufactured_by`、`sources_from`  
链路：`component → supplier → OEM → robot_system → application`

---

## 第 27 章 应用场景
### 27.1 工业制造
- 汽车工厂、3C 制造
- 物料搬运、装配、质检

### 27.2 物流仓储
- 拣选、搬运、分拣
- 与人协作的仓库机器人

### 27.3 商业服务
- 零售、餐饮、导览

### 27.4 医疗健康
- 康复训练、陪护、手术辅助

### 27.5 家庭服务
- 清洁、整理、照护

### 27.6 科研、教育与特种任务
- 科研平台、教学、救援、安防

**本章知识图谱锚点**  
实体：`application`、`robot_system`、`technology`  
关系：`applies_to`、`used_in`  
链路：`robot_system → application → market → customer_value`

---

## 第 28 章 市场、企业与投资
### 28.1 全球市场规模与预测
- 出货量、单价、渗透率
- 工业 vs 服务市场

### 28.2 企业生态
- 整机 OEM
- 核心零部件供应商
- 软件与 AI 公司
- 系统集成商

### 28.3 投融资趋势
- 融资阶段、金额、地域分布
- 独角兽与上市公司

### 28.4 商业模式
- 销售、租赁、服务订阅
- Robot-as-a-Service（RaaS）

**本章知识图谱锚点**  
实体：`company`、`oem`、`market`、`application`  
关系：`operates_in`、`competes_with`、`partners_with`  
链路：`company → product → application → market → revenue_model`

---

# 第十部分：政策、伦理与未来

## 第 29 章 政策、监管与伦理
### 29.1 安全法规
- ISO/IEC/EN 标准体系
- 区域准入差异

### 29.2 责任与保险
- 产品责任、运营责任
- 保险产品设计

### 29.3 隐私与数据安全
- 视觉数据采集与存储
- 生物识别与个人信息保护

### 29.4 劳动力与社会影响
- 就业替代与就业创造
- 人机协作的社会接受度

### 29.5 伦理设计
- 透明度、可解释性、公平性
- 以人为本的设计原则

**本章知识图谱锚点**  
实体：`standard`、`concept`、`application`  
关系：`regulates`、`applies_to`  
链路：`policy → standard → design → application → society`

---

## 第 30 章 未来展望
### 30.1 技术演进趋势
- 硬件成本下降曲线
- AI 模型通用化
- 数据飞轮效应

### 30.2 产业化临界点
- 成本-性能-可靠性三角
- 规模化部署的条件

### 30.3 通用机器人愿景
- 从专用到通用
- 具身智能的终极目标

### 30.4 知识图谱的持续发展
- 社区共建
- 自动更新与人工审核
- 从知识图谱到智能助手

**本章知识图谱锚点**  
实体：`concept`、`technology`、`market`  
关系：`enables`、`drives`  
链路：`technology_progress → cost_reduction → market_expansion → societal_impact`

---

# 附录

## 附录 A 实体类型与关系类型速查表
- A.1 实体类型完整列表
- A.2 关系类型完整列表
- A.3 Domain 编码对照表

## 附录 B 关键数据集清单
- B.1 操作数据集
- B.2 运动数据集
- B.3 仿真数据集
- B.4 数据集许可证说明

## 附录 C 关键软件与仿真平台清单
- C.1 物理引擎
- C.2 仿真平台
- C.3 运动规划库
- C.4 中间件与操作系统

## 附录 D 主要供应商与企业名录
- D.1 减速器厂商
- D.2 电机厂商
- D.3 传感器厂商
- D.4 计算平台厂商
- D.5 整机厂商

## 附录 E 标准、法规与认证清单
- E.1 国际标准
- E.2 区域法规
- E.3 认证机构

## 附录 F 知识图谱查询示例
- F.1 查询某机器人的所有零部件
- F.2 查询某算法的训练数据集
- F.3 查询某零部件的供应商
- F.4 查询跨层关系路径

## 附录 G 术语表（中英对照）

## 附录 H 参考文献与来源索引
