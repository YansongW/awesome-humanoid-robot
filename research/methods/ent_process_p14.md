---
$id: ent_process_p14
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Software & Integration
  zh: 软件中间件与系统集成（Software & Integration）
  ko: 软件中间件与系统集成（Software & Integration）
summary:
  en: Software & Integration-the 14th stage of the entire Android product development process, covering solution design, implementation
    verification, and document delivery.
  zh: 软件中间件与系统集成（Software & Integration）是人形机器人产品开发全流程中的第 14 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 软件中间件与系统集成（Software & Integration）
domains:
- 08_software_middleware
layers:
- intelligence
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
软件中间件与系统集成（Software & Integration）是人形机器人产品开发全流程中的第 14 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 中间件与实时框架

##### 中间件选型与适配
- **方法 / 工具**：ROS2 / DDS / 自研中间件 / LCM
- **设计思考逻辑**：ROS2 适合算法快速迭代，DDS 提供 QoS；硬实时控制可剥离到 RTOS
- **关键约束**：实时性、消息延迟、生态、License
- **完成标准 / 输出物**：中间件架构图、节点清单、QoS 策略
**三级子任务：**
- **P14.1.1.1 输入梳理与目标量化**：整理「中间件选型与适配」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P14.1.1.2 候选方案建立与评估**：针对「中间件选型与适配」建立候选方案库，使用「ROS2 / DDS / 自研中间件 / LCM」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P14.1.1.3 实施/原型/样件制作**：根据设计方案执行「中间件选型与适配」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P14.1.1.4 验证与问题闭环**：对「中间件选型与适配」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P14.1.1.5 文档输出与下游交付**：输出「中间件选型与适配」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 实时控制框架
- **方法 / 工具**：EtherCAT 主站、RTOS、控制周期保证、抖动分析
- **设计思考逻辑**：保证控制环（≥1 kHz）不受 AI 任务干扰
- **关键约束**：抖动、调度策略、核隔离
- **完成标准 / 输出物**：实时性能测试报告、最大抖动 < 目标
**三级子任务：**
- **P14.1.2.1 输入梳理与目标量化**：整理「实时控制框架」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P14.1.2.2 算法/控制方案设计**：基于「EtherCAT 主站、RTOS、控制周期保证、抖动分析」建立数学模型或算法框架，形成候选方案，评估稳定性、实时性与可扩展性，并冻结实现路径。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P14.1.2.3 算法实现与仿真验证**：将「实时控制框架」的算法在仿真环境或离线数据中实现，验证功能正确性、实时性与鲁棒性。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P14.1.2.4 算法调参与性能验证**：对「实时控制框架」算法进行参数调优与边界测试，验证在典型/极端工况下的性能是否满足指标。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P14.1.2.5 文档输出与下游交付**：输出「实时控制框架」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 硬件抽象与驱动层
- **方法 / 工具**：统一关节接口、传感器 HAL、板级驱动
- **设计思考逻辑**：屏蔽不同硬件实现，便于算法移植与替换
- **关键约束**：兼容性、实时性、维护性
- **完成标准 / 输出物**：HAL 接口规范、驱动覆盖清单、单元测试
**三级子任务：**
- **P14.1.3.1 输入梳理与目标量化**：整理「硬件抽象与驱动层」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P14.1.3.2 方案/方法设计**：针对「硬件抽象与驱动层」制定实施方法或候选方案，使用「统一关节接口、传感器 HAL、板级驱动」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P14.1.3.3 实施/原型/样件制作**：根据设计方案执行「硬件抽象与驱动层」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P14.1.3.4 验证与问题闭环**：对「硬件抽象与驱动层」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P14.1.3.5 文档输出与下游交付**：输出「硬件抽象与驱动层」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 工具链与 DevOps

##### 数据记录与回放
- **方法 / 工具**：rosbag2、结构化日志、数据湖、数据版本管理
- **设计思考逻辑**：便于问题复现、模型训练、性能分析
- **关键约束**：存储容量、带宽、隐私
- **完成标准 / 输出物**：数据记录方案、回放一致性验证
**三级子任务：**
- **P14.2.1.1 输入梳理与目标量化**：整理「数据记录与回放」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P14.2.1.2 方案/方法设计**：针对「数据记录与回放」制定实施方法或候选方案，使用「rosbag2、结构化日志、数据湖、数据版本管理」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P14.2.1.3 实施/原型/样件制作**：根据设计方案执行「数据记录与回放」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P14.2.1.4 验证与问题闭环**：对「数据记录与回放」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P14.2.1.5 文档输出与下游交付**：输出「数据记录与回放」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### OTA、诊断与健康管理
- **方法 / 工具**：远程升级、健康监控、故障码、预测性维护
- **设计思考逻辑**：小批量及量产阶段快速迭代软件；降低现场维护成本
- **关键约束**：安全性、回滚机制、带宽
- **完成标准 / 输出物**：OTA 方案、诊断协议、健康管理界面
**三级子任务：**
- **P14.2.2.1 输入梳理与目标量化**：整理「OTA、诊断与健康管理」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P14.2.2.2 方案/方法设计**：针对「OTA、诊断与健康管理」制定实施方法或候选方案，使用「远程升级、健康监控、故障码、预测性维护」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P14.2.2.3 实施/原型/样件制作**：根据设计方案执行「OTA、诊断与健康管理」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P14.2.2.4 验证与问题闭环**：对「OTA、诊断与健康管理」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P14.2.2.5 文档输出与下游交付**：输出「OTA、诊断与健康管理」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### CI/CD 与仿真测试链
- **方法 / 工具**：GitLab CI、Docker、SIL/HIL 自动化测试、代码覆盖率
- **设计思考逻辑**：持续集成保证软件质量，减少回归问题
- **关键约束**：算力、测试环境维护
- **完成标准 / 输出物**：CI 流水线、自动测试通过率、覆盖率指标
**三级子任务：**
- **P14.2.3.1 输入梳理与目标量化**：整理「CI/CD 与仿真测试链」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P14.2.3.2 方案/方法设计**：针对「CI/CD 与仿真测试链」制定实施方法或候选方案，使用「GitLab CI、Docker、SIL/HIL 自动化测试、代码覆盖率」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P14.2.3.3 实施/原型/样件制作**：根据设计方案执行「CI/CD 与仿真测试链」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P14.2.3.4 测试执行与结果分析**：按照验收标准执行「CI/CD 与仿真测试链」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P14.2.3.5 文档输出与下游交付**：输出「CI/CD 与仿真测试链」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 系统集成与接口测试

##### 端到端数据流联调
- **方法 / 工具**：传感器 → 感知 → 规划 → 控制 → 执行器链路测试
- **设计思考逻辑**：验证各模块接口、时序、异常处理
- **关键约束**：实时性、消息丢失、节点故障
- **完成标准 / 输出物**：端到端延迟 < 目标、故障注入测试通过
**三级子任务：**
- **P14.3.1.1 输入梳理与目标量化**：整理「端到端数据流联调」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P14.3.1.2 接口与集成策略设计**：梳理「端到端数据流联调」涉及的子系统接口、数据流与时序，制定集成顺序、回退策略与异常处理机制。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P14.3.1.3 实施/原型/样件制作**：根据设计方案执行「端到端数据流联调」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P14.3.1.4 验证与问题闭环**：对「端到端数据流联调」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P14.3.1.5 文档输出与下游交付**：输出「端到端数据流联调」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 软硬件在环测试（HIL/SIL）
- **方法 / 工具**：仿真模型 + 真实控制器、自动化测试用例
- **设计思考逻辑**：在实物前验证控制器与软件逻辑
- **关键约束**：模型保真度、测试覆盖率
- **完成标准 / 输出物**：HIL/SIL 测试报告、关键用例 100% 覆盖
**三级子任务：**
- **P14.3.2.1 输入梳理与目标量化**：整理「软硬件在环测试（HIL/SIL）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P14.3.2.2 方案/方法设计**：针对「软硬件在环测试（HIL/SIL）」制定实施方法或候选方案，使用「仿真模型 + 真实控制器、自动化测试用例」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P14.3.2.3 建模/仿真与样机实现**：建立「软硬件在环测试（HIL/SIL）」的仿真/数学模型或原型样机，使用「仿真模型 + 真实控制器、自动化测试用例」执行计算或实验，记录关键参数与边界条件。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P14.3.2.4 测试执行与结果分析**：按照验收标准执行「软硬件在环测试（HIL/SIL）」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P14.3.2.5 文档输出与下游交付**：输出「软硬件在环测试（HIL/SIL）」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
Software Middleware and System Integration (Software & Integration) is the 14th stage in the full-process development of humanoid robot products, expanded into several Level-3 sub-tasks in WBS V3.
## Content
This stage covers complete engineering actions such as input review, solution design, implementation/prototyping, verification closure, and documentation delivery, serving as a critical node to ensure downstream dependents receive qualified inputs.

## Key Sub-tasks and Technical Content
#### Middleware and Real-time Framework

##### Middleware Selection and Adaptation
- **Methods/Tools**: ROS2 / DDS / Custom Middleware / LCM
- **Design Rationale**: ROS2 is suitable for rapid algorithm iteration; DDS provides QoS; hard real-time control can be offloaded to RTOS
- **Key Constraints**: Real-time performance, message latency, ecosystem, License
- **Completion Criteria/Deliverables**: Middleware architecture diagram, node list, QoS strategy
**Level-3 Sub-tasks:**
- **P14.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Middleware Selection and Adaptation," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P14.1.1.2 Candidate Solution Establishment and Evaluation**: Establish a candidate solution library for "Middleware Selection and Adaptation," conduct quantitative evaluation using "ROS2 / DDS / Custom Middleware / LCM," and determine the final solution after considering cost, performance, supply chain, and maintainability.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P14.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Middleware Selection and Adaptation" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P14.1.1.4 Verification and Issue Closure**: Verify the output of "Middleware Selection and Adaptation," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P14.1.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Middleware Selection and Adaptation," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation according to template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Real-time Control Framework
- **Methods/Tools**: EtherCAT Master, RTOS, Control Cycle Guarantee, Jitter Analysis
- **Design Rationale**: Ensure the control loop (≥1 kHz) is not disturbed by AI tasks
- **Key Constraints**: Jitter, scheduling strategy, core isolation
- **Completion Criteria/Deliverables**: Real-time performance test report, maximum jitter < target
**Level-3 Sub-tasks:**
- **P14.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Real-time Control Framework," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P14.1.2.2 Algorithm/Control Solution Design**: Establish a mathematical model or algorithm framework based on "EtherCAT Master, RTOS, Control Cycle Guarantee, Jitter Analysis," form candidate solutions, evaluate stability, real-time performance, and scalability, and freeze the implementation path.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P14.1.2.3 Algorithm Implementation and Simulation Verification**: Implement the algorithm for "Real-time Control Framework" in a simulation environment or with offline data, verifying functional correctness, real-time performance, and robustness.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P14.1.2.4 Algorithm Tuning and Performance Verification**: Perform parameter tuning and boundary testing for the "Real-time Control Framework" algorithm, verifying performance under typical/extreme operating conditions meets indicators.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P14.1.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Real-time Control Framework," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation according to template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Hardware Abstraction and Driver Layer
- **Methods/Tools**: Unified Joint Interface, Sensor HAL, Board-level Drivers
- **Design Rationale**: Shield different hardware implementations to facilitate algorithm porting and replacement
- **Key Constraints**: Compatibility, real-time performance, maintainability
- **Completion Criteria/Deliverables**: HAL interface specification, driver coverage list, unit tests
**Level-3 Sub-tasks:**
- **P14.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Hardware Abstraction and Driver Layer," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P14.1.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Hardware Abstraction and Driver Layer," demonstrate using "Unified Joint Interface, Sensor HAL, Board-level Drivers," and clarify the technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P14.1.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Hardware Abstraction and Driver Layer" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P14.1.3.4 Verification and Issue Closure**: Verify the output of "Hardware Abstraction and Driver Layer," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P14.1.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Hardware Abstraction and Driver Layer," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation according to template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### Toolchain and DevOps

##### Data Recording and Playback
- **Methods/Tools**: rosbag2, Structured Logging, Data Lake, Data Version Management
- **Design Rationale**: Facilitate issue reproduction, model training, and performance analysis
- **Key Constraints**: Storage capacity, bandwidth, privacy
- **Completion Criteria/Deliverables**: Data recording plan, playback consistency verification
**Level-3 Sub-tasks:**
- **P14.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Data Recording and Playback," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P14.2.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Data Recording and Playback," demonstrate using "rosbag2, Structured Logging, Data Lake, Data Version Management," and clarify the technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P14.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Data Recording and Playback" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P14.2.1.4 Verification and Issue Closure**: Verify the output of "Data Recording and Playback," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P14.2.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Data Recording and Playback," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation according to template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### OTA, Diagnostics, and Health Management
- **Methods/Tools**: Remote Upgrade, Health Monitoring, Fault Codes, Predictive Maintenance
- **Design Rationale**: Enable rapid software iteration during small batch and mass production; reduce on-site maintenance costs
- **Key Constraints**: Security, rollback mechanism, bandwidth
- **Completion Criteria/Deliverables**: OTA plan, diagnostic protocol, health management interface
**Level-3 Sub-tasks:**
- **P14.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "OTA, Diagnostics, and Health Management," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P14.2.2.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "OTA, Diagnostics, and Health Management," demonstrate using "Remote Upgrade, Health Monitoring, Fault Codes, Predictive Maintenance," and clarify the technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P14.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "OTA, Diagnostics, and Health Management" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P14.2.2.4 Verification and Issue Closure**: Verify the output of "OTA, Diagnostics, and Health Management," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P14.2.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "OTA, Diagnostics, and Health Management," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation according to template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### CI/CD and Simulation Test Chain
- **Methods/Tools**: GitLab CI, Docker, SIL/HIL Automated Testing, Code Coverage
- **Design Rationale**: Continuous integration ensures software quality and reduces regression issues
- **Key Constraints**: Computing power, test environment maintenance
- **Completion Criteria/Deliverables**: CI pipeline, automated test pass rate, coverage metrics
**Level-3 Sub-tasks:**
- **P14.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "CI/CD and Simulation Test Chain," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P14.2.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "CI/CD and Simulation Test Chain," demonstrate using "GitLab CI, Docker, SIL/HIL Automated Testing, Code Coverage," and clarify the technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P14.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "CI/CD and Simulation Test Chain" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P14.2.3.4 Test Execution and Result Analysis**: Execute tests for "CI/CD and Simulation Test Chain" according to acceptance criteria, calculate pass rate/error/deviation, conduct root cause analysis, and form an improvement list.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P14.2.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "CI/CD and Simulation Test Chain," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation according to template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### System Integration and Interface Testing

##### End-to-End Data Flow Integration
- **Methods/Tools**: Sensor → Perception → Planning → Control → Actuator Link Testing
- **Design Rationale**: Verify module interfaces, timing, and exception handling
- **Key Constraints**: Real-time performance, message loss, node failure
- **Completion Criteria/Deliverables**: End-to-end latency < target, fault injection test pass
**Level-3 Sub-tasks:**
- **P14.3.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "End-to-End Data Flow Integration," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P14.3.1.2 Interface and Integration Strategy Design**: Review the subsystem interfaces, data flow, and timing involved in "End-to-End Data Flow Integration," and develop integration sequence, rollback strategy, and exception handling mechanisms.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P14.3.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "End-to-End Data Flow Integration" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P14.3.1.4 Verification and Issue Closure**: Verify the output of "End-to-End Data Flow Integration," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P14.3.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "End-to-End Data Flow Integration," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documentation according to template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

## 개요
소프트웨어 미들웨어와 시스템 통합(Software & Integration)은 휴머노이드 로봇 제품 개발 전 과정의 14번째 단계로, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.
## 핵심 내용
이 단계는 입력 정리, 설계, 구현/프로토타입, 검증 폐루프 및 문서 인도 등 완전한 엔지니어링 작업을 포함하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 지점입니다.

## 주요 하위 작업 및 기술 내용
#### 미들웨어 및 실시간 프레임워크

##### 미들웨어 선정 및 적응
- **방법 / 도구**: ROS2 / DDS / 자체 개발 미들웨어 / LCM
- **설계 사고 논리**: ROS2는 알고리즘 빠른 반복에 적합, DDS는 QoS 제공; 하드 실시간 제어는 RTOS로 분리 가능
- **핵심 제약 조건**: 실시간성, 메시지 지연, 생태계, 라이선스
- **완료 기준 / 산출물**: 미들웨어 아키텍처 다이어그램, 노드 목록, QoS 정책
**3레벨 하위 작업:**
- **P14.1.1.1 입력 정리 및 목표 정량화**: 「미들웨어 선정 및 적응」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록을 수립
- **P14.1.1.2 후보 방안 수립 및 평가**: 「미들웨어 선정 및 적응」에 대한 후보 방안 라이브러리를 구축하고, 「ROS2 / DDS / 자체 개발 미들웨어 / LCM」을 사용하여 정량적 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 방안을 확정합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안을 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 동결
- **P14.1.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「미들웨어 선정 및 적응」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P14.1.1.4 검증 및 문제 폐루프**: 「미들웨어 선정 및 적응」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P14.1.1.5 문서 출력 및 하위 인도**: 「미들웨어 선정 및 적응」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 실시간 제어 프레임워크
- **방법 / 도구**: EtherCAT 마스터, RTOS, 제어 주기 보장, 지터 분석
- **설계 사고 논리**: 제어 루프(≥1 kHz)가 AI 작업에 방해받지 않도록 보장
- **핵심 제약 조건**: 지터, 스케줄링 정책, 코어 격리
- **완료 기준 / 산출물**: 실시간 성능 테스트 보고서, 최대 지터 < 목표
**3레벨 하위 작업:**
- **P14.1.2.1 입력 정리 및 목표 정량화**: 「실시간 제어 프레임워크」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록을 수립
- **P14.1.2.2 알고리즘/제어 방안 설계**: 「EtherCAT 마스터, RTOS, 제어 주기 보장, 지터 분석」을 기반으로 수학적 모델 또는 알고리즘 프레임워크를 구축하고, 후보 방안을 구성하며, 안정성, 실시간성 및 확장성을 평가하고 구현 경로를 동결합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안을 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 동결
- **P14.1.2.3 알고리즘 구현 및 시뮬레이션 검증**: 「실시간 제어 프레임워크」의 알고리즘을 시뮬레이션 환경 또는 오프라인 데이터에서 구현하고, 기능 정확성, 실시간성 및 강건성을 검증합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P14.1.2.4 알고리즘 튜닝 및 성능 검증**: 「실시간 제어 프레임워크」 알고리즘에 대해 매개변수 최적화 및 경계 테스트를 수행하고, 일반/극한 작업 조건에서의 성능이 지표를 충족하는지 검증합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P14.1.2.5 문서 출력 및 하위 인도**: 「실시간 제어 프레임워크」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 하드웨어 추상화 및 드라이버 계층
- **방법 / 도구**: 통합 관절 인터페이스, 센서 HAL, 보드 레벨 드라이버
- **설계 사고 논리**: 서로 다른 하드웨어 구현을 차폐하여 알고리즘 이식 및 교체를 용이하게 함
- **핵심 제약 조건**: 호환성, 실시간성, 유지보수성
- **완료 기준 / 산출물**: HAL 인터페이스 사양, 드라이버 적용 목록, 단위 테스트
**3레벨 하위 작업:**
- **P14.1.3.1 입력 정리 및 목표 정량화**: 「하드웨어 추상화 및 드라이버 계층」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록을 수립
- **P14.1.3.2 방안/방법 설계**: 「하드웨어 추상화 및 드라이버 계층」에 대한 구현 방법 또는 후보 방안을 수립하고, 「통합 관절 인터페이스, 센서 HAL, 보드 레벨 드라이버」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안을 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 동결
- **P14.1.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「하드웨어 추상화 및 드라이버 계층」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P14.1.3.4 검증 및 문제 폐루프**: 「하드웨어 추상화 및 드라이버 계층」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P14.1.3.5 문서 출력 및 하위 인도**: 「하드웨어 추상화 및 드라이버 계층」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 도구 체인 및 DevOps

##### 데이터 기록 및 재생
- **방법 / 도구**: rosbag2, 구조화된 로그, 데이터 레이크, 데이터 버전 관리
- **설계 사고 논리**: 문제 재현, 모델 훈련, 성능 분석을 용이하게 함
- **핵심 제약 조건**: 저장 용량, 대역폭, 프라이버시
- **완료 기준 / 산출물**: 데이터 기록 방안, 재생 일관성 검증
**3레벨 하위 작업:**
- **P14.2.1.1 입력 정리 및 목표 정량화**: 「데이터 기록 및 재생」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록을 수립
- **P14.2.1.2 방안/방법 설계**: 「데이터 기록 및 재생」에 대한 구현 방법 또는 후보 방안을 수립하고, 「rosbag2, 구조화된 로그, 데이터 레이크, 데이터 버전 관리」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안을 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 동결
- **P14.2.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「데이터 기록 및 재생」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P14.2.1.4 검증 및 문제 폐루프**: 「데이터 기록 및 재생」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P14.2.1.5 문서 출력 및 하위 인도**: 「데이터 기록 및 재생」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### OTA, 진단 및 상태 관리
- **방법 / 도구**: 원격 업그레이드, 상태 모니터링, 오류 코드, 예측 유지보수
- **설계 사고 논리**: 소량 생산 및 양산 단계에서 소프트웨어를 빠르게 반복; 현장 유지보수 비용 절감
- **핵심 제약 조건**: 보안, 롤백 메커니즘, 대역폭
- **완료 기준 / 산출물**: OTA 방안, 진단 프로토콜, 상태 관리 인터페이스
**3레벨 하위 작업:**
- **P14.2.2.1 입력 정리 및 목표 정량화**: 「OTA, 진단 및 상태 관리」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록을 수립
- **P14.2.2.2 방안/방법 설계**: 「OTA, 진단 및 상태 관리」에 대한 구현 방법 또는 후보 방안을 수립하고, 「원격 업그레이드, 상태 모니터링, 오류 코드, 예측 유지보수」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안을 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 동결
- **P14.2.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「OTA, 진단 및 상태 관리」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P14.2.2.4 검증 및 문제 폐루프**: 「OTA, 진단 및 상태 관리」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P14.2.2.5 문서 출력 및 하위 인도**: 「OTA, 진단 및 상태 관리」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### CI/CD 및 시뮬레이션 테스트 체인
- **방법 / 도구**: GitLab CI, Docker, SIL/HIL 자동화 테스트, 코드 커버리지
- **설계 사고 논리**: 지속적 통합으로 소프트웨어 품질 보장, 회귀 문제 감소
- **핵심 제약 조건**: 컴퓨팅 성능, 테스트 환경 유지보수
- **완료 기준 / 산출물**: CI 파이프라인, 자동 테스트 통과율, 커버리지 지표
**3레벨 하위 작업:**
- **P14.2.3.1 입력 정리 및 목표 정량화**: 「CI/CD 및 시뮬레이션 테스트 체인」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록을 수립
- **P14.2.3.2 방안/방법 설계**: 「CI/CD 및 시뮬레이션 테스트 체인」에 대한 구현 방법 또는 후보 방안을 수립하고, 「GitLab CI, Docker, SIL/HIL 자동화 테스트, 코드 커버리지」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안을 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 동결
- **P14.2.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「CI/CD 및 시뮬레이션 테스트 체인」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P14.2.3.4 테스트 실행 및 결과 분석**: 검수 기준에 따라 「CI/CD 및 시뮬레이션 테스트 체인」 테스트를 실행하고, 통과율/오류/편차를 통계하며, 근본 원인 분석을 수행하고 개선 목록을 구성합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P14.2.3.5 문서 출력 및 하위 인도**: 「CI/CD 및 시뮬레이션 테스트 체인」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 시스템 통합 및 인터페이스 테스트

##### 종단 간 데이터 흐름 연동
- **방법 / 도구**: 센서 → 인식 → 계획 → 제어 → 액추에이터 체인 테스트
- **설계 사고 논리**: 각 모듈의 인터페이스, 타이밍, 예외 처리를 검증
- **핵심 제약 조건**: 실시간성, 메시지 손실, 노드 장애
- **완료 기준 / 산출물**: 종단 간 지연 < 목표, 장애 주입 테스트 통과
**3레벨 하위 작업:**
- **P14.3.1.1 입력 정리 및 목표 정량화**: 「종단 간 데이터 흐름 연동」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록을 수립
- **P14.3.1.2 인터페이스 및 통합 전략 설계**: 「종단 간 데이터 흐름 연동」에 관련된 하위 시스템 인터페이스, 데이터 흐름 및 타이밍을 정리하고, 통합 순서, 롤백 전략 및 예외 처리 메커니즘을 수립합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 방안을 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 동결
- **P14.3.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「종단 간 데이터 흐름 연동」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P14.3.1.4 검증 및 문제 폐루프**: 「종단 간 데이터 흐름 연동」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P14.3.1.5 문서 출력 및 하위 인도**: 「종단 간 데이터 흐름 연동」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지
