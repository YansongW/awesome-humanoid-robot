---
$id: ent_process_p11
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Dexterous Hand Selection/Design and Integration
  zh: 灵巧手选型/设计与集成（Dexterous Hand）
  ko: 灵巧手选型/设计与集成（Dexterous Hand）
summary:
  en: Dexterous Hand Selection/Design and Integration — the 11th phase of the full-cycle humanoid robot product development
    process, encompassing conceptual design, implementation and validation, and documentation delivery.
  zh: 灵巧手选型/设计与集成（Dexterous Hand）是人形机器人产品开发全流程中的第 11 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 灵巧手选型/设计与集成（Dexterous Hand）
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
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
灵巧手选型/设计与集成（Dexterous Hand）是人形机器人产品开发全流程中的第 11 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 手部架构与驱动

##### 手部 DOF 与功能定义
- **方法 / 工具**：任务分析、抓取分类、仿生对比
- **设计思考逻辑**：拇指对掌、手指屈曲/外展；根据目标物体决定全自由度或欠驱动
- **关键约束**：重量、体积、线缆数量、成本
- **完成标准 / 输出物**：《手部规格书》：DOF、关节范围、指尖力、抓取类型覆盖
**三级子任务：**
- **P11.1.1.1 输入梳理与目标量化**：整理「手部 DOF 与功能定义」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P11.1.1.2 方案/方法设计**：针对「手部 DOF 与功能定义」制定实施方法或候选方案，使用「任务分析、抓取分类、仿生对比」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P11.1.1.3 实施/原型/样件制作**：根据设计方案执行「手部 DOF 与功能定义」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P11.1.1.4 验证与问题闭环**：对「手部 DOF 与功能定义」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P11.1.1.5 文档输出与下游交付**：输出「手部 DOF 与功能定义」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 驱动与传动方案
- **方法 / 工具**：腱绳传动、微型电机直驱、连杆传动、液压/气动对比
- **设计思考逻辑**：腱绳体积小但复杂；直驱易维护但体积大；欠驱动降低成本
- **关键约束**：可靠性、可维护性、回差、力控精度
- **完成标准 / 输出物**：驱动方案决策报告、传动链图纸
**三级子任务：**
- **P11.1.2.1 输入梳理与目标量化**：整理「驱动与传动方案」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P11.1.2.2 方案/方法设计**：针对「驱动与传动方案」制定实施方法或候选方案，使用「腱绳传动、微型电机直驱、连杆传动、液压/气动对比」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P11.1.2.3 实施/原型/样件制作**：根据设计方案执行「驱动与传动方案」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P11.1.2.4 验证与问题闭环**：对「驱动与传动方案」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P11.1.2.5 文档输出与下游交付**：输出「驱动与传动方案」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 触觉与力觉传感器集成
- **方法 / 工具**：阵列触觉、指尖六维力、关节力矩、滑移检测
- **设计思考逻辑**：精细操作依赖触觉反馈；力控保障安全
- **关键约束**：布线、信号处理、成本、空间
- **完成标准 / 输出物**：传感器布置方案、信号处理链、标定方法
**三级子任务：**
- **P11.1.3.1 输入梳理与目标量化**：整理「触觉与力觉传感器集成」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P11.1.3.2 接口与集成策略设计**：梳理「触觉与力觉传感器集成」涉及的子系统接口、数据流与时序，制定集成顺序、回退策略与异常处理机制。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P11.1.3.3 实施/原型/样件制作**：根据设计方案执行「触觉与力觉传感器集成」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P11.1.3.4 验证与问题闭环**：对「触觉与力觉传感器集成」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P11.1.3.5 文档输出与下游交付**：输出「触觉与力觉传感器集成」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 抓取规划与控制集成

##### 抓取姿态生成与力闭合分析
- **方法 / 工具**：GraspIt / OpenRAVE、力闭合判据、对抗抓取
- **设计思考逻辑**：基于物体模型或点云生成稳定抓取；支持包络抓取与精确捏取
- **关键约束**：实时性、物体多样性、模型不确定性
- **完成标准 / 输出物**：抓取库/策略、典型物体成功率 > 目标
**三级子任务：**
- **P11.2.1.1 输入梳理与目标量化**：整理「抓取姿态生成与力闭合分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P11.2.1.2 方案/方法设计**：针对「抓取姿态生成与力闭合分析」制定实施方法或候选方案，使用「GraspIt / OpenRAVE、力闭合判据、对抗抓取」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P11.2.1.3 实施/原型/样件制作**：根据设计方案执行「抓取姿态生成与力闭合分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P11.2.1.4 验证与问题闭环**：对「抓取姿态生成与力闭合分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P11.2.1.5 文档输出与下游交付**：输出「抓取姿态生成与力闭合分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 手指阻抗与力控
- **方法 / 工具**：关节/指尖阻抗控制、导纳控制、力位混合
- **设计思考逻辑**：实现柔顺抓取，避免损坏物体或手指
- **关键约束**：带宽、稳定性、传感器噪声
- **完成标准 / 输出物**：力控实验数据、易碎物体抓取视频
**三级子任务：**
- **P11.2.2.1 输入梳理与目标量化**：整理「手指阻抗与力控」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P11.2.2.2 方案/方法设计**：针对「手指阻抗与力控」制定实施方法或候选方案，使用「关节/指尖阻抗控制、导纳控制、力位混合」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P11.2.2.3 实施/原型/样件制作**：根据设计方案执行「手指阻抗与力控」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P11.2.2.4 验证与问题闭环**：对「手指阻抗与力控」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P11.2.2.5 文档输出与下游交付**：输出「手指阻抗与力控」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 与手臂集成与手眼标定
- **方法 / 工具**：腕部接口设计、手眼标定、线缆管理、联合控制
- **设计思考逻辑**：手腕作为手与臂的接口，需考虑载荷、通信、热管理
- **关键约束**：腕部自由度、布线、标定精度
- **完成标准 / 输出物**：集成测试报告、手眼标定误差 < 目标
**三级子任务：**
- **P11.2.3.1 输入梳理与目标量化**：整理「与手臂集成与手眼标定」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P11.2.3.2 接口与集成策略设计**：梳理「与手臂集成与手眼标定」涉及的子系统接口、数据流与时序，制定集成顺序、回退策略与异常处理机制。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P11.2.3.3 实施/原型/样件制作**：根据设计方案执行「与手臂集成与手眼标定」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P11.2.3.4 验证与问题闭环**：对「与手臂集成与手眼标定」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P11.2.3.5 文档输出与下游交付**：输出「与手臂集成与手眼标定」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
Dexterous Hand selection/design and integration is the 11th phase in the full-process development of humanoid robot products, expanded into several third-level sub-tasks in WBS V3.
## Content
This phase covers complete engineering actions such as input review, solution design, implementation/prototyping, verification closed-loop, and documentation delivery, serving as a key milestone to ensure downstream dependents receive qualified inputs.

## Key Sub-tasks and Technical Content
#### Hand Architecture and Actuation

##### Hand DOF and Function Definition
- **Methods/Tools**: Task analysis, grasp classification, bionic comparison
- **Design Logic**: Thumb opposition, finger flexion/abduction; decide full DOF or underactuation based on target objects
- **Key Constraints**: Weight, volume, cable count, cost
- **Completion Criteria/Deliverables**: "Hand Specification": DOF, joint range, fingertip force, grasp type coverage
**Third-level Sub-tasks:**
- **P11.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Hand DOF and Function Definition", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Fourth-level Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P11.1.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Hand DOF and Function Definition", demonstrate using "task analysis, grasp classification, bionic comparison", and clarify technical route and resource requirements.
**Fourth-level Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P11.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Hand DOF and Function Definition" based on the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Fourth-level Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P11.1.1.4 Verification and Issue Closure**: Verify the output of "Hand DOF and Function Definition", check if completion criteria are met, record issues, and track until closure.
**Fourth-level Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P11.1.1.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Hand DOF and Function Definition", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Fourth-level Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Actuation and Transmission Solution
- **Methods/Tools**: Tendon-driven, micro-motor direct drive, linkage transmission, hydraulic/pneumatic comparison
- **Design Logic**: Tendon is compact but complex; direct drive is easy to maintain but bulky; underactuation reduces cost
- **Key Constraints**: Reliability, maintainability, backlash, force control accuracy
- **Completion Criteria/Deliverables**: Actuation solution decision report, transmission chain drawings
**Third-level Sub-tasks:**
- **P11.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Actuation and Transmission Solution", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Fourth-level Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P11.1.2.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Actuation and Transmission Solution", demonstrate using "tendon-driven, micro-motor direct drive, linkage transmission, hydraulic/pneumatic comparison", and clarify technical route and resource requirements.
**Fourth-level Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P11.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Actuation and Transmission Solution" based on the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Fourth-level Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P11.1.2.4 Verification and Issue Closure**: Verify the output of "Actuation and Transmission Solution", check if completion criteria are met, record issues, and track until closure.
**Fourth-level Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P11.1.2.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Actuation and Transmission Solution", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Fourth-level Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Tactile and Force Sensor Integration
- **Methods/Tools**: Array tactile, fingertip 6-axis force, joint torque, slip detection
- **Design Logic**: Fine manipulation relies on tactile feedback; force control ensures safety
- **Key Constraints**: Wiring, signal processing, cost, space
- **Completion Criteria/Deliverables**: Sensor layout plan, signal processing chain, calibration method
**Third-level Sub-tasks:**
- **P11.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Tactile and Force Sensor Integration", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Fourth-level Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P11.1.3.2 Interface and Integration Strategy Design**: Review subsystem interfaces, data flow, and timing involved in "Tactile and Force Sensor Integration", develop integration sequence, rollback strategy, and exception handling mechanism.
**Fourth-level Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P11.1.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Tactile and Force Sensor Integration" based on the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Fourth-level Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P11.1.3.4 Verification and Issue Closure**: Verify the output of "Tactile and Force Sensor Integration", check if completion criteria are met, record issues, and track until closure.
**Fourth-level Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P11.1.3.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Tactile and Force Sensor Integration", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Fourth-level Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### Grasp Planning and Control Integration

##### Grasp Pose Generation and Force Closure Analysis
- **Methods/Tools**: GraspIt / OpenRAVE, force closure criteria, adversarial grasping
- **Design Logic**: Generate stable grasps based on object models or point clouds; support enveloping grasps and precision pinches
- **Key Constraints**: Real-time performance, object diversity, model uncertainty
- **Completion Criteria/Deliverables**: Grasp library/strategy, success rate for typical objects > target
**Third-level Sub-tasks:**
- **P11.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Grasp Pose Generation and Force Closure Analysis", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Fourth-level Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P11.2.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Grasp Pose Generation and Force Closure Analysis", demonstrate using "GraspIt / OpenRAVE, force closure criteria, adversarial grasping", and clarify technical route and resource requirements.
**Fourth-level Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P11.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Grasp Pose Generation and Force Closure Analysis" based on the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Fourth-level Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P11.2.1.4 Verification and Issue Closure**: Verify the output of "Grasp Pose Generation and Force Closure Analysis", check if completion criteria are met, record issues, and track until closure.
**Fourth-level Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P11.2.1.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Grasp Pose Generation and Force Closure Analysis", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Fourth-level Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Finger Impedance and Force Control
- **Methods/Tools**: Joint/fingertip impedance control, admittance control, force-position hybrid
- **Design Logic**: Achieve compliant grasping to avoid damaging objects or fingers
- **Key Constraints**: Bandwidth, stability, sensor noise
- **Completion Criteria/Deliverables**: Force control experimental data, fragile object grasping video
**Third-level Sub-tasks:**
- **P11.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Finger Impedance and Force Control", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Fourth-level Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P11.2.2.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Finger Impedance and Force Control", demonstrate using "joint/fingertip impedance control, admittance control, force-position hybrid", and clarify technical route and resource requirements.
**Fourth-level Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P11.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Finger Impedance and Force Control" based on the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Fourth-level Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P11.2.2.4 Verification and Issue Closure**: Verify the output of "Finger Impedance and Force Control", check if completion criteria are met, record issues, and track until closure.
**Fourth-level Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P11.2.2.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Finger Impedance and Force Control", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Fourth-level Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Arm Integration and Hand-Eye Calibration
- **Methods/Tools**: Wrist interface design, hand-eye calibration, cable management, joint control
- **Design Logic**: The wrist serves as the interface between hand and arm, considering load, communication, and thermal management
- **Key Constraints**: Wrist DOF, wiring, calibration accuracy
- **Completion Criteria/Deliverables**: Integration test report, hand-eye calibration error < target
**Third-level Sub-tasks:**
- **P11.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Arm Integration and Hand-Eye Calibration", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Fourth-level Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P11.2.3.2 Interface and Integration Strategy Design**: Review subsystem interfaces, data flow, and timing involved in "Arm Integration and Hand-Eye Calibration", develop integration sequence, rollback strategy, and exception handling mechanism.
**Fourth-level Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the solution
- **P11.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Arm Integration and Hand-Eye Calibration" based on the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Fourth-level Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P11.2.3.4 Verification and Issue Closure**: Verify the output of "Arm Integration and Hand-Eye Calibration", check if completion criteria are met, record issues, and track until closure.
**Fourth-level Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P11.2.3.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Arm Integration and Hand-Eye Calibration", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Fourth-level Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

## Completion Criteria
All third-level sub-tasks in this phase have passed acceptance review, key deliverable versions are under control, and formal delivery has been made to downstream dependents.

## 개요
덱스터러스 핸드(Dexterous Hand) 선정/설계 및 통합은 휴머노이드 로봇 제품 개발 전 과정 중 11번째 단계이며, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.
## 핵심 내용
이 단계는 입력 정리, 설계 방안, 구현/프로토타입, 검증 폐쇄 및 문서 인도 등 완전한 엔지니어링 작업을 포괄하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 지점입니다.

## 주요 하위 작업 및 기술 내용
#### 손 구조 및 구동

##### 손 DOF 및 기능 정의
- **방법 / 도구**: 작업 분석, 파지 분류, 생체 모방 비교
- **설계 사고 논리**: 엄지 맞섬, 손가락 굴곡/외전; 대상 물체에 따라 완전 자유도 또는 저구동 결정
- **핵심 제약 조건**: 무게, 부피, 케이블 수량, 비용
- **완료 기준 / 산출물**: 《손 사양서》: DOF, 관절 범위, 손끝 힘, 파지 유형 범위
**3레벨 하위 작업:**
- **P11.1.1.1 입력 정리 및 목표 정량화**: 「손 DOF 및 기능 정의」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P11.1.1.2 방안/방법 설계**: 「손 DOF 및 기능 정의」에 대한 구현 방법 또는 후보 방안을 수립하고, 「작업 분석, 파지 분류, 생체 모방 비교」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P11.1.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「손 DOF 및 기능 정의」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P11.1.1.4 검증 및 문제 폐쇄**: 「손 DOF 및 기능 정의」 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P11.1.1.5 문서 출력 및 하위 인도**: 「손 DOF 및 기능 정의」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 완료 및 버전 관리
3. 게시 및 하위 의존 부서 통지

##### 구동 및 전동 방안
- **방법 / 도구**: 텐던 구동, 초소형 모터 직접 구동, 링크 구동, 유압/공압 비교
- **설계 사고 논리**: 텐던은 부피가 작지만 복잡함; 직접 구동은 유지보수가 쉽지만 부피가 큼; 저구동은 비용 절감
- **핵심 제약 조건**: 신뢰성, 유지보수성, 백래시, 힘 제어 정밀도
- **완료 기준 / 산출물**: 구동 방안 결정 보고서, 전동 체인 도면
**3레벨 하위 작업:**
- **P11.1.2.1 입력 정리 및 목표 정량화**: 「구동 및 전동 방안」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P11.1.2.2 방안/방법 설계**: 「구동 및 전동 방안」에 대한 구현 방법 또는 후보 방안을 수립하고, 「텐던 구동, 초소형 모터 직접 구동, 링크 구동, 유압/공압 비교」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P11.1.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「구동 및 전동 방안」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P11.1.2.4 검증 및 문제 폐쇄**: 「구동 및 전동 방안」 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P11.1.2.5 문서 출력 및 하위 인도**: 「구동 및 전동 방안」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 완료 및 버전 관리
3. 게시 및 하위 의존 부서 통지

##### 촉각 및 힘 센서 통합
- **방법 / 도구**: 배열 촉각, 손끝 6축 힘, 관절 토크, 미끄러짐 감지
- **설계 사고 논리**: 정밀 조작은 촉각 피드백에 의존; 힘 제어는 안전 보장
- **핵심 제약 조건**: 배선, 신호 처리, 비용, 공간
- **완료 기준 / 산출물**: 센서 배치 방안, 신호 처리 체인, 교정 방법
**3레벨 하위 작업:**
- **P11.1.3.1 입력 정리 및 목표 정량화**: 「촉각 및 힘 센서 통합」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P11.1.3.2 인터페이스 및 통합 전략 설계**: 「촉각 및 힘 센서 통합」과 관련된 하위 시스템 인터페이스, 데이터 흐름 및 타이밍을 정리하고, 통합 순서, 롤백 전략 및 예외 처리 메커니즘을 수립합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P11.1.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「촉각 및 힘 센서 통합」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P11.1.3.4 검증 및 문제 폐쇄**: 「촉각 및 힘 센서 통합」 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P11.1.3.5 문서 출력 및 하위 인도**: 「촉각 및 힘 센서 통합」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 완료 및 버전 관리
3. 게시 및 하위 의존 부서 통지

#### 파지 계획 및 제어 통합

##### 파지 자세 생성 및 힘 폐쇄 분석
- **방법 / 도구**: GraspIt / OpenRAVE, 힘 폐쇄 판별, 대항 파지
- **설계 사고 논리**: 물체 모델 또는 포인트 클라우드 기반 안정적인 파지 생성; 포위 파지 및 정밀 집게 파지 지원
- **핵심 제약 조건**: 실시간성, 물체 다양성, 모델 불확실성
- **완료 기준 / 산출물**: 파지 라이브러리/전략, 대표 물체 성공률 > 목표
**3레벨 하위 작업:**
- **P11.2.1.1 입력 정리 및 목표 정량화**: 「파지 자세 생성 및 힘 폐쇄 분석」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P11.2.1.2 방안/방법 설계**: 「파지 자세 생성 및 힘 폐쇄 분석」에 대한 구현 방법 또는 후보 방안을 수립하고, 「GraspIt / OpenRAVE, 힘 폐쇄 판별, 대항 파지」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P11.2.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「파지 자세 생성 및 힘 폐쇄 분석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P11.2.1.4 검증 및 문제 폐쇄**: 「파지 자세 생성 및 힘 폐쇄 분석」 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P11.2.1.5 문서 출력 및 하위 인도**: 「파지 자세 생성 및 힘 폐쇄 분석」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 완료 및 버전 관리
3. 게시 및 하위 의존 부서 통지

##### 손가락 임피던스 및 힘 제어
- **방법 / 도구**: 관절/손끝 임피던스 제어, 어드미턴스 제어, 힘-위치 혼합
- **설계 사고 논리**: 유연한 파지 구현, 물체 또는 손가락 손상 방지
- **핵심 제약 조건**: 대역폭, 안정성, 센서 노이즈
- **완료 기준 / 산출물**: 힘 제어 실험 데이터, 취약 물체 파지 영상
**3레벨 하위 작업:**
- **P11.2.2.1 입력 정리 및 목표 정량화**: 「손가락 임피던스 및 힘 제어」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P11.2.2.2 방안/방법 설계**: 「손가락 임피던스 및 힘 제어」에 대한 구현 방법 또는 후보 방안을 수립하고, 「관절/손끝 임피던스 제어, 어드미턴스 제어, 힘-위치 혼합」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P11.2.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「손가락 임피던스 및 힘 제어」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P11.2.2.4 검증 및 문제 폐쇄**: 「손가락 임피던스 및 힘 제어」 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P11.2.2.5 문서 출력 및 하위 인도**: 「손가락 임피던스 및 힘 제어」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 완료 및 버전 관리
3. 게시 및 하위 의존 부서 통지

##### 팔 통합 및 손-눈 보정
- **방법 / 도구**: 손목 인터페이스 설계, 손-눈 보정, 케이블 관리, 공동 제어
- **설계 사고 논리**: 손목은 손과 팔의 인터페이스로서 하중, 통신, 열 관리를 고려해야 함
- **핵심 제약 조건**: 손목 자유도, 배선, 보정 정밀도
- **완료 기준 / 산출물**: 통합 테스트 보고서, 손-눈 보정 오차 < 목표
**3레벨 하위 작업:**
- **P11.2.3.1 입력 정리 및 목표 정량화**: 「팔 통합 및 손-눈 보정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P11.2.3.2 인터페이스 및 통합 전략 설계**: 「팔 통합 및 손-눈 보정」과 관련된 하위 시스템 인터페이스, 데이터 흐름 및 타이밍을 정리하고, 통합 순서, 롤백 전략 및 예외 처리 메커니즘을 수립합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P11.2.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「팔 통합 및 손-눈 보정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P11.2.3.4 검증 및 문제 폐쇄**: 「팔 통합 및 손-눈 보정」 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P11.2.3.5 문서 출력 및 하위 인도**: 「팔 통합 및 손-눈 보정」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 완료 및 버전 관리
3. 게시 및 하위 의존 부서 통지

## 완료 기준
본 단계의 모든 3레벨 하위 작업이 검수 검토를 통과하고, 핵심 산출물 버전이 관리되어 하위 의존 부서에 공식적으로 인도됩니다.
