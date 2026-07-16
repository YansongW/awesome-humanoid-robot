---
$id: ent_process_p6
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: URDF modeling and Kinematics & URDF
  zh: URDF 建模与运动学校核（Kinematics & URDF）
  ko: URDF 建模与运动学校核（Kinematics & URDF）
summary:
  en: URDF modeling and Kinematics & URDF-phase 6 of the entire Android product development process, covering conceptual design,
    implementation verification, and document delivery.
  zh: URDF 建模与运动学校核（Kinematics & URDF）是人形机器人产品开发全流程中的第 6 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: URDF 建模与运动学校核（Kinematics & URDF）
domains:
- 06_design_engineering
- 08_software_middleware
layers:
- intelligence
- midstream
functional_roles:
- process
- knowledge
tags: []
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py. English name/summary machine-translated
    from Chinese by scripts/backfill_en_translations.py.
sources:
- id: wbs_v3_report
  type: report
  title: 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）
  date: '2026-06-27'
theoretical_depth:
- system
---



## 概述
URDF 建模与运动学校核（Kinematics & URDF）是人形机器人产品开发全流程中的第 6 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### URDF/SDF 模型构建

##### URDF/SDF 文件生成
- **方法 / 工具**：ROS URDF、Xacro、SolidWorks/NX → URDF 插件、惯性参数校核
- **设计思考逻辑**：连杆、关节、惯性、碰撞体、视觉模型需与 CAD 完全一致；质量属性来自 P3.1.2/P3.1.3
- **关键约束**：坐标系一致性、单位统一、碰撞体不能太密
- **完成标准 / 输出物**：可在 RViz/Gazebo/Isaac Sim 中正确加载、无解析错误
**三级子任务：**
- **P6.1.1.1 输入梳理与目标量化**：整理「URDF/SDF 文件生成」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P6.1.1.2 方案/方法设计**：针对「URDF/SDF 文件生成」制定实施方法或候选方案，使用「ROS URDF、Xacro、SolidWorks/NX → URDF 插件、惯性参数校核」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P6.1.1.3 实施/原型/样件制作**：根据设计方案执行「URDF/SDF 文件生成」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P6.1.1.4 验证与问题闭环**：对「URDF/SDF 文件生成」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P6.1.1.5 文档输出与下游交付**：输出「URDF/SDF 文件生成」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### DH / 修改 DH 参数定义
- **方法 / 工具**：解析法、Pinocchio/RBDL、符号计算
- **设计思考逻辑**：为每条运动链建立标准运动学参数，便于逆解与控制器实现
- **关键约束**：坐标系方向约定、关节零点定义
- **完成标准 / 输出物**：《DH 参数表》、正运动学代码与 URDF 对比误差 < 1e-6
**三级子任务：**
- **P6.1.2.1 输入梳理与目标量化**：整理「DH / 修改 DH 参数定义」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P6.1.2.2 方案/方法设计**：针对「DH / 修改 DH 参数定义」制定实施方法或候选方案，使用「解析法、Pinocchio/RBDL、符号计算」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P6.1.2.3 实施/原型/样件制作**：根据设计方案执行「DH / 修改 DH 参数定义」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P6.1.2.4 验证与问题闭环**：对「DH / 修改 DH 参数定义」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P6.1.2.5 文档输出与下游交付**：输出「DH / 修改 DH 参数定义」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 碰撞与自干涉模型
- **方法 / 工具**：凸包/简化网格、FCL/PyBullet、碰撞矩阵
- **设计思考逻辑**：运动过程中肢体与环境、肢体与肢体不得发生碰撞；碰撞体过紧会误报，过松会漏报
- **关键约束**：计算开销、精度、维护性
- **完成标准 / 输出物**：典型动作无自碰撞误报、关键姿态无环境穿透
**三级子任务：**
- **P6.1.3.1 输入梳理与目标量化**：整理「碰撞与自干涉模型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P6.1.3.2 方案/方法设计**：针对「碰撞与自干涉模型」制定实施方法或候选方案，使用「凸包/简化网格、FCL/PyBullet、碰撞矩阵」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P6.1.3.3 实施/原型/样件制作**：根据设计方案执行「碰撞与自干涉模型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P6.1.3.4 验证与问题闭环**：对「碰撞与自干涉模型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P6.1.3.5 文档输出与下游交付**：输出「碰撞与自干涉模型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 运动学验证

##### 正逆运动学解算验证
- **方法 / 工具**：解析/数值逆解、随机姿态采样、奇异性分析
- **设计思考逻辑**：验证 URDF 中关节极限、连杆长度与 CAD 一致；IK 解算成功率高
- **关键约束**：奇异位置、多解选择、关节极限
- **完成标准 / 输出物**：随机 1000 组位姿 IK 成功率 > 99%、位置误差 < 1 mm
**三级子任务：**
- **P6.2.1.1 输入梳理与目标量化**：整理「正逆运动学解算验证」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P6.2.1.2 方案/方法设计**：针对「正逆运动学解算验证」制定实施方法或候选方案，使用「解析/数值逆解、随机姿态采样、奇异性分析」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P6.2.1.3 实施/原型/样件制作**：根据设计方案执行「正逆运动学解算验证」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P6.2.1.4 测试执行与结果分析**：按照验收标准执行「正逆运动学解算验证」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P6.2.1.5 文档输出与下游交付**：输出「正逆运动学解算验证」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 工作空间与可达性分析
- **方法 / 工具**：Matlab/Python、RViz、蒙特卡洛采样
- **设计思考逻辑**：生成足端/手末端可达空间云图，验证覆盖 P2.2.1 人机工程需求
- **关键约束**：自碰撞约束、关节极限
- **完成标准 / 输出物**：《工作空间分析报告》：可达域包络、关键姿态覆盖度 > 95%
**三级子任务：**
- **P6.2.2.1 输入梳理与目标量化**：整理「工作空间与可达性分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P6.2.2.2 方案/方法设计**：针对「工作空间与可达性分析」制定实施方法或候选方案，使用「Matlab/Python、RViz、蒙特卡洛采样」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P6.2.2.3 实施/原型/样件制作**：根据设计方案执行「工作空间与可达性分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P6.2.2.4 验证与问题闭环**：对「工作空间与可达性分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P6.2.2.5 文档输出与下游交付**：输出「工作空间与可达性分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 雅可比与速度/力传递分析
- **方法 / 工具**：几何雅可比、可操作度椭球、力椭球
- **设计思考逻辑**：评估机器人在不同姿态下的速度/力操作能力，为控制设计提供依据
- **关键约束**：数值稳定性
- **完成标准 / 输出物**：典型姿态可操作度指标、力传递效率分析
**三级子任务：**
- **P6.2.3.1 输入梳理与目标量化**：整理「雅可比与速度/力传递分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P6.2.3.2 方案/方法设计**：针对「雅可比与速度/力传递分析」制定实施方法或候选方案，使用「几何雅可比、可操作度椭球、力椭球」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P6.2.3.3 实施/原型/样件制作**：根据设计方案执行「雅可比与速度/力传递分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P6.2.3.4 验证与问题闭环**：对「雅可比与速度/力传递分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P6.2.3.5 文档输出与下游交付**：输出「雅可比与速度/力传递分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
URDF modeling and kinematics verification (Kinematics & URDF) is the 6th stage in the full humanoid robot product development workflow, expanded into several Level-3 sub-tasks in WBS V3.
## Content
This stage covers complete engineering actions such as input review, solution design, implementation/prototyping, verification closure, and documentation delivery, serving as a critical checkpoint to ensure downstream dependencies receive qualified inputs.

## Key Sub-tasks and Technical Content
#### URDF/SDF Model Construction

##### URDF/SDF File Generation
- **Methods / Tools**: ROS URDF, Xacro, SolidWorks/NX → URDF plugin, inertia parameter verification
- **Design Rationale**: Links, joints, inertia, collision bodies, and visual models must be fully consistent with CAD; mass properties sourced from P3.1.2/P3.1.3
- **Key Constraints**: Coordinate system consistency, unit uniformity, collision bodies must not be too dense
- **Completion Criteria / Deliverables**: Correctly loadable in RViz/Gazebo/Isaac Sim without parsing errors
**Level-3 Sub-tasks:**
- **P6.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "URDF/SDF File Generation," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P6.1.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "URDF/SDF File Generation," justify using "ROS URDF, Xacro, SolidWorks/NX → URDF plugin, inertia parameter verification," and clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P6.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "URDF/SDF File Generation" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P6.1.1.4 Verification and Issue Closure**: Verify the output of "URDF/SDF File Generation," check compliance with completion criteria, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P6.1.1.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "URDF/SDF File Generation," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### DH / Modified DH Parameter Definition
- **Methods / Tools**: Analytical method, Pinocchio/RBDL, symbolic computation
- **Design Rationale**: Establish standard kinematic parameters for each kinematic chain to facilitate inverse kinematics and controller implementation
- **Key Constraints**: Coordinate system orientation conventions, joint zero definitions
- **Completion Criteria / Deliverables**: "DH Parameter Table," forward kinematics code with error < 1e-6 compared to URDF
**Level-3 Sub-tasks:**
- **P6.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "DH / Modified DH Parameter Definition," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P6.1.2.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "DH / Modified DH Parameter Definition," justify using "analytical method, Pinocchio/RBDL, symbolic computation," and clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P6.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "DH / Modified DH Parameter Definition" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P6.1.2.4 Verification and Issue Closure**: Verify the output of "DH / Modified DH Parameter Definition," check compliance with completion criteria, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P6.1.2.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "DH / Modified DH Parameter Definition," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Collision and Self-Interference Model
- **Methods / Tools**: Convex hull/simplified mesh, FCL/PyBullet, collision matrix
- **Design Rationale**: No collisions between limbs and environment or between limbs during motion; overly tight collision bodies cause false positives, overly loose ones cause missed detections
- **Key Constraints**: Computational cost, accuracy, maintainability
- **Completion Criteria / Deliverables**: No false self-collision alarms in typical motions, no environmental penetration in key poses
**Level-3 Sub-tasks:**
- **P6.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Collision and Self-Interference Model," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P6.1.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Collision and Self-Interference Model," justify using "convex hull/simplified mesh, FCL/PyBullet, collision matrix," and clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P6.1.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Collision and Self-Interference Model" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P6.1.3.4 Verification and Issue Closure**: Verify the output of "Collision and Self-Interference Model," check compliance with completion criteria, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P6.1.3.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Collision and Self-Interference Model," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### Kinematics Verification

##### Forward and Inverse Kinematics Solution Verification
- **Methods / Tools**: Analytical/numerical inverse kinematics, random pose sampling, singularity analysis
- **Design Rationale**: Verify that joint limits and link lengths in URDF are consistent with CAD; high IK solution success rate
- **Key Constraints**: Singular positions, multi-solution selection, joint limits
- **Completion Criteria / Deliverables**: IK success rate > 99% for 1000 random poses, position error < 1 mm
**Level-3 Sub-tasks:**
- **P6.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Forward and Inverse Kinematics Solution Verification," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P6.2.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Forward and Inverse Kinematics Solution Verification," justify using "analytical/numerical inverse kinematics, random pose sampling, singularity analysis," and clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P6.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Forward and Inverse Kinematics Solution Verification" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P6.2.1.4 Test Execution and Result Analysis**: Execute tests for "Forward and Inverse Kinematics Solution Verification" according to acceptance criteria, calculate pass rate/error/deviation, perform root cause analysis, and form improvement list.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P6.2.1.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Forward and Inverse Kinematics Solution Verification," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Workspace and Reachability Analysis
- **Methods / Tools**: Matlab/Python, RViz, Monte Carlo sampling
- **Design Rationale**: Generate reachable workspace point clouds for foot/end-effector, verify coverage of P2.2.1 ergonomic requirements
- **Key Constraints**: Self-collision constraints, joint limits
- **Completion Criteria / Deliverables**: "Workspace Analysis Report": reachable envelope, key pose coverage > 95%
**Level-3 Sub-tasks:**
- **P6.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Workspace and Reachability Analysis," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P6.2.2.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Workspace and Reachability Analysis," justify using "Matlab/Python, RViz, Monte Carlo sampling," and clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P6.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Workspace and Reachability Analysis" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P6.2.2.4 Verification and Issue Closure**: Verify the output of "Workspace and Reachability Analysis," check compliance with completion criteria, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P6.2.2.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Workspace and Reachability Analysis," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Jacobian and Velocity/Force Transmission Analysis
- **Methods / Tools**: Geometric Jacobian, manipulability ellipsoid, force ellipsoid
- **Design Rationale**: Evaluate the robot's velocity/force manipulation capability in different poses to inform control design
- **Key Constraints**: Numerical stability
- **Completion Criteria / Deliverables**: Manipulability metrics for typical poses, force transmission efficiency analysis
**Level-3 Sub-tasks:**
- **P6.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Jacobian and Velocity/Force Transmission Analysis," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P6.2.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Jacobian and Velocity/Force Transmission Analysis," justify using "geometric Jacobian, manipulability ellipsoid, force ellipsoid," and clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P6.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Jacobian and Velocity/Force Transmission Analysis" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P6.2.3.4 Verification and Issue Closure**: Verify the output of "Jacobian and Velocity/Force Transmission Analysis," check compliance with completion criteria, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P6.2.3.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Jacobian and Velocity/Force Transmission Analysis," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

## Completion Criteria
All Level-3 sub-tasks in this stage have passed acceptance review, and key deliverables are version-controlled and formally delivered to downstream dependents.

## 개요
URDF 모델링 및 운동학 검증(Kinematics & URDF)은 휴머노이드 로봇 제품 개발 전 과정 중 6번째 단계이며, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.
## 핵심 내용
이 단계는 입력 정리, 설계 방안, 구현/프로토타입, 검증 폐쇄 및 문서 인도 등 완전한 엔지니어링 작업을 포함하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 지점입니다.

## 주요 하위 작업 및 기술 내용
#### URDF/SDF 모델 구축

##### URDF/SDF 파일 생성
- **방법 / 도구**: ROS URDF, Xacro, SolidWorks/NX → URDF 플러그인, 관성 매개변수 검증
- **설계 사고 논리**: 링크, 조인트, 관성, 충돌체, 시각 모델은 CAD와 완전히 일치해야 함; 질량 속성은 P3.1.2/P3.1.3에서 가져옴
- **주요 제약 조건**: 좌표계 일관성, 단위 통일, 충돌체가 너무 조밀하지 않아야 함
- **완료 기준 / 산출물**: RViz/Gazebo/Isaac Sim에서 올바르게 로드 가능, 구문 오류 없음
**3레벨 하위 작업:**
- **P6.1.1.1 입력 정리 및 목표 정량화**: 「URDF/SDF 파일 생성」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록 수립
- **P6.1.1.2 방안/방법 설계**: 「URDF/SDF 파일 생성」에 대한 구현 방법 또는 후보 방안을 수립하고, 「ROS URDF, Xacro, SolidWorks/NX → URDF 플러그인, 관성 매개변수 검증」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
**4레벨 핵심 작업:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 방안 확정
- **P6.1.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「URDF/SDF 파일 생성」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 매개변수 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P6.1.1.4 검증 및 문제 폐쇄**: 「URDF/SDF 파일 생성」의 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P6.1.1.5 문서 출력 및 하위 인도**: 「URDF/SDF 파일 생성」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 참조
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### DH / 수정 DH 매개변수 정의
- **방법 / 도구**: 해석법, Pinocchio/RBDL, 기호 계산
- **설계 사고 논리**: 각 운동 체인에 대해 표준 운동학 매개변수를 설정하여 역운동학 및 컨트롤러 구현을 용이하게 함
- **주요 제약 조건**: 좌표계 방향 약속, 조인트 영점 정의
- **완료 기준 / 산출물**: 《DH 매개변수 표》, 정운동학 코드와 URDF 비교 오차 < 1e-6
**3레벨 하위 작업:**
- **P6.1.2.1 입력 정리 및 목표 정량화**: 「DH / 수정 DH 매개변수 정의」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록 수립
- **P6.1.2.2 방안/방법 설계**: 「DH / 수정 DH 매개변수 정의」에 대한 구현 방법 또는 후보 방안을 수립하고, 「해석법, Pinocchio/RBDL, 기호 계산」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
**4레벨 핵심 작업:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 방안 확정
- **P6.1.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「DH / 수정 DH 매개변수 정의」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 매개변수 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P6.1.2.4 검증 및 문제 폐쇄**: 「DH / 수정 DH 매개변수 정의」의 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P6.1.2.5 문서 출력 및 하위 인도**: 「DH / 수정 DH 매개변수 정의」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 참조
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 충돌 및 자체 간섭 모델
- **방법 / 도구**: 볼록 껍질/단순화된 메쉬, FCL/PyBullet, 충돌 매트릭스
- **설계 사고 논리**: 운동 과정에서 팔다리와 환경, 팔다리와 팔다리 간 충돌이 발생하지 않아야 함; 충돌체가 너무 조밀하면 오경보, 너무 느슨하면 누락 발생
- **주요 제약 조건**: 계산 비용, 정밀도, 유지보수성
- **완료 기준 / 산출물**: 일반 동작에서 자체 충돌 오경보 없음, 주요 자세에서 환경 관통 없음
**3레벨 하위 작업:**
- **P6.1.3.1 입력 정리 및 목표 정량화**: 「충돌 및 자체 간섭 모델」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록 수립
- **P6.1.3.2 방안/방법 설계**: 「충돌 및 자체 간섭 모델」에 대한 구현 방법 또는 후보 방안을 수립하고, 「볼록 껍질/단순화된 메쉬, FCL/PyBullet, 충돌 매트릭스」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
**4레벨 핵심 작업:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 방안 확정
- **P6.1.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「충돌 및 자체 간섭 모델」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 매개변수 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P6.1.3.4 검증 및 문제 폐쇄**: 「충돌 및 자체 간섭 모델」의 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P6.1.3.5 문서 출력 및 하위 인도**: 「충돌 및 자체 간섭 모델」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 참조
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

#### 운동학 검증

##### 정/역운동학 해석 검증
- **방법 / 도구**: 해석/수치 역운동학, 무작위 자세 샘플링, 특이점 분석
- **설계 사고 논리**: URDF의 조인트 한계, 링크 길이가 CAD와 일치하는지 검증; IK 해석 성공률 높음
- **주요 제약 조건**: 특이 위치, 다중 해 선택, 조인트 한계
- **완료 기준 / 산출물**: 무작위 1000개 자세 IK 성공률 > 99%, 위치 오차 < 1 mm
**3레벨 하위 작업:**
- **P6.2.1.1 입력 정리 및 목표 정량화**: 「정/역운동학 해석 검증」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록 수립
- **P6.2.1.2 방안/방법 설계**: 「정/역운동학 해석 검증」에 대한 구현 방법 또는 후보 방안을 수립하고, 「해석/수치 역운동학, 무작위 자세 샘플링, 특이점 분석」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
**4레벨 핵심 작업:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 방안 확정
- **P6.2.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「정/역운동학 해석 검증」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 매개변수 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P6.2.1.4 테스트 실행 및 결과 분석**: 검수 기준에 따라 「정/역운동학 해석 검증」 테스트를 수행하고, 통과율/오차/편차를 통계하며, 근본 원인 분석을 수행하고 개선 목록을 작성함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P6.2.1.5 문서 출력 및 하위 인도**: 「정/역운동학 해석 검증」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 참조
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 작업 공간 및 도달 가능성 분석
- **방법 / 도구**: Matlab/Python, RViz, 몬테카를로 샘플링
- **설계 사고 논리**: 발끝/손끝 도달 가능 공간 클라우드 맵을 생성하여 P2.2.1 인간공학 요구 사항 충족 검증
- **주요 제약 조건**: 자체 충돌 제약, 조인트 한계
- **완료 기준 / 산출물**: 《작업 공간 분석 보고서》: 도달 가능 영역 포락선, 주요 자세 커버리지 > 95%
**3레벨 하위 작업:**
- **P6.2.2.1 입력 정리 및 목표 정량화**: 「작업 공간 및 도달 가능성 분석」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록 수립
- **P6.2.2.2 방안/방법 설계**: 「작업 공간 및 도달 가능성 분석」에 대한 구현 방법 또는 후보 방안을 수립하고, 「Matlab/Python, RViz, 몬테카를로 샘플링」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
**4레벨 핵심 작업:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 방안 확정
- **P6.2.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「작업 공간 및 도달 가능성 분석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 매개변수 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P6.2.2.4 검증 및 문제 폐쇄**: 「작업 공간 및 도달 가능성 분석」의 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P6.2.2.5 문서 출력 및 하위 인도**: 「작업 공간 및 도달 가능성 분석」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 참조
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 야코비안 및 속도/힘 전달 분석
- **방법 / 도구**: 기하 야코비안, 조작도 타원체, 힘 타원체
- **설계 사고 논리**: 다양한 자세에서 로봇의 속도/힘 조작 능력을 평가하여 제어 설계에 근거 제공
- **주요 제약 조건**: 수치 안정성
- **완료 기준 / 산출물**: 일반 자세 조작도 지표, 힘 전달 효율 분석
**3레벨 하위 작업:**
- **P6.2.3.1 입력 정리 및 목표 정량화**: 「야코비안 및 속도/힘 전달 분석」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록 수립
- **P6.2.3.2 방안/방법 설계**: 「야코비안 및 속도/힘 전달 분석」에 대한 구현 방법 또는 후보 방안을 수립하고, 「기하 야코비안, 조작도 타원체, 힘 타원체」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
**4레벨 핵심 작업:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 방안 확정
- **P6.2.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「야코비안 및 속도/힘 전달 분석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 매개변수 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P6.2.3.4 검증 및 문제 폐쇄**: 「야코비안 및 속도/힘 전달 분석」의 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P6.2.3.5 문서 출력 및 하위 인도**: 「야코비안 및 속도/힘 전달 분석」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 참조
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

## 완료 기준
본 단계의 모든 3레벨 하위 작업은 검수 심사를 통과하며, 주요 산출물의 버전이 관리되고 하위 의존 부서에 공식적으로 인도됩니다.
