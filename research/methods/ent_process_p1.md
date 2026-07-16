---
$id: ent_process_p1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Requirements Definition and System Design (Concept / Pre-A)
  zh: 需求定义与系统方案（Concept / Pre-A）
  ko: 需求定义与系统方案（Concept / Pre-A）
summary:
  en: Requirement Definition and System Architecture (Concept / Pre-A) – the first phase of the full lifecycle for humanoid
    robot product development, encompassing conceptual design, implementation validation, and document delivery.
  zh: 需求定义与系统方案（Concept / Pre-A）是人形机器人产品开发全流程中的第 1 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 需求定义与系统方案（Concept / Pre-A）
domains:
- 06_design_engineering
- 12_policy_regulation_ethics
layers:
- midstream
- validation_markets
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
需求定义与系统方案（Concept / Pre-A）是人形机器人产品开发全流程中的第 1 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 需求工程

##### 利益相关方需求采集
- **方法 / 工具**：访谈、问卷、工作坊、现场跟拍、Kano 模型
- **设计思考逻辑**：识别显性与隐性需求；区分 Must-have / Differentiator / Exciter
- **关键约束**：时间、样本代表性、需求冲突
- **完成标准 / 输出物**：利益相关方清单、需求池、优先级排序
**三级子任务：**
- **P1.1.1.1 输入梳理与目标量化**：整理「利益相关方需求采集」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P1.1.1.2 方案/方法设计**：针对「利益相关方需求采集」制定实施方法或候选方案，使用「访谈、问卷、工作坊、现场跟拍、Kano 模型」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P1.1.1.3 实施/原型/样件制作**：根据设计方案执行「利益相关方需求采集」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P1.1.1.4 验证与问题闭环**：对「利益相关方需求采集」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P1.1.1.5 文档输出与下游交付**：输出「利益相关方需求采集」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 系统需求规格书（SyRS）
- **方法 / 工具**：SysML 用例图、需求树、SMART 原则
- **设计思考逻辑**：将商业语言转化为工程语言：尺寸、重量、DOF、速度、负载、续航、安全等级
- **关键约束**：指标耦合、测试可行性、成本驱动
- **完成标准 / 输出物**：SyRS 基线发布、需求可追溯、验收条件量化
**三级子任务：**
- **P1.1.2.1 输入梳理与目标量化**：整理「系统需求规格书（SyRS）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P1.1.2.2 方案/方法设计**：针对「系统需求规格书（SyRS）」制定实施方法或候选方案，使用「SysML 用例图、需求树、SMART 原则」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P1.1.2.3 实施/原型/样件制作**：根据设计方案执行「系统需求规格书（SyRS）」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P1.1.2.4 验证与问题闭环**：对「系统需求规格书（SyRS）」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P1.1.2.5 文档输出与下游交付**：输出「系统需求规格书（SyRS）」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 法规、标准与安全需求映射
- **方法 / 工具**：ISO 10218-1/2、ISO/TS 15066、IEC 61508、IEC 62368、CE/FCC/UL 差距分析
- **设计思考逻辑**：安全需求必须在设计早期成为硬约束，而非后期补票
- **关键约束**：地区差异、认证周期、测试费用
- **完成标准 / 输出物**：法规需求矩阵、合规路线图、安全目标等级（SIL/PL）
**三级子任务：**
- **P1.1.3.1 输入梳理与目标量化**：整理「法规、标准与安全需求映射」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P1.1.3.2 方案/方法设计**：针对「法规、标准与安全需求映射」制定实施方法或候选方案，使用「ISO 10218-1/2、ISO/TS 15066、IEC 61508、IEC 62368、CE/FCC/UL 差距分析」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P1.1.3.3 实施/原型/样件制作**：根据设计方案执行「法规、标准与安全需求映射」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P1.1.3.4 验证与问题闭环**：对「法规、标准与安全需求映射」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P1.1.3.5 文档输出与下游交付**：输出「法规、标准与安全需求映射」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 人因工程与交互需求
- **方法 / 工具**：人体测量数据库、可达域分析、惊吓反应实验、HMI 原型
- **设计思考逻辑**：机器人与人共融场景的高度、视野、声音、动作必须可接受
- **关键约束**：文化差异、用户群体多样性、心理安全
- **完成标准 / 输出物**：人因需求报告、关键交互姿态包络、HMI 原则
**三级子任务：**
- **P1.1.4.1 输入梳理与目标量化**：整理「人因工程与交互需求」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P1.1.4.2 方案/方法设计**：针对「人因工程与交互需求」制定实施方法或候选方案，使用「人体测量数据库、可达域分析、惊吓反应实验、HMI 原型」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P1.1.4.3 实施/原型/样件制作**：根据设计方案执行「人因工程与交互需求」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P1.1.4.4 验证与问题闭环**：对「人因工程与交互需求」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P1.1.4.5 文档输出与下游交付**：输出「人因工程与交互需求」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 概念设计

##### 概念方案发散与收敛
- **方法 / 工具**：头脑风暴、形态草图、Morphological Matrix、Pugh Matrix
- **设计思考逻辑**：在多种整机布局、驱动方案、传感方案中系统评估
- **关键约束**：技术成熟度、成本、可制造性
- **完成标准 / 输出物**：至少 3 套概念方案、评分矩阵、选定方案理由
**三级子任务：**
- **P1.2.1.1 输入梳理与目标量化**：整理「概念方案发散与收敛」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P1.2.1.2 方案/方法设计**：针对「概念方案发散与收敛」制定实施方法或候选方案，使用「头脑风暴、形态草图、Morphological Matrix、Pugh Matrix」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P1.2.1.3 实施/原型/样件制作**：根据设计方案执行「概念方案发散与收敛」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P1.2.1.4 验证与问题闭环**：对「概念方案发散与收敛」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P1.2.1.5 文档输出与下游交付**：输出「概念方案发散与收敛」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 整机架构与功能分配
- **方法 / 工具**：功能分解、N² 图、接口控制文档（ICD）草案
- **设计思考逻辑**：明确运动、操作、感知、计算、能源、热管理、结构子系统的边界
- **关键约束**：实时性、功耗、线缆数量、可维护性
- **完成标准 / 输出物**：系统架构图、功能分配表、ICD 草案
**三级子任务：**
- **P1.2.2.1 输入梳理与目标量化**：整理「整机架构与功能分配」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P1.2.2.2 方案/方法设计**：针对「整机架构与功能分配」制定实施方法或候选方案，使用「功能分解、N² 图、接口控制文档（ICD）草案」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P1.2.2.3 实施/原型/样件制作**：根据设计方案执行「整机架构与功能分配」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P1.2.2.4 验证与问题闭环**：对「整机架构与功能分配」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P1.2.2.5 文档输出与下游交付**：输出「整机架构与功能分配」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 关键技术指标权衡分析
- **方法 / 工具**：多目标优化、Pareto 前沿、敏感性分析
- **设计思考逻辑**：速度 vs 续航 vs 成本 vs 负载；找到可接受的设计空间
- **关键约束**：物理极限、供应链能力、预算
- **完成标准 / 输出物**：权衡分析表、指标边界、设计空间图
**三级子任务：**
- **P1.2.3.1 输入梳理与目标量化**：整理「关键技术指标权衡分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P1.2.3.2 方案/方法设计**：针对「关键技术指标权衡分析」制定实施方法或候选方案，使用「多目标优化、Pareto 前沿、敏感性分析」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P1.2.3.3 实施/原型/样件制作**：根据设计方案执行「关键技术指标权衡分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P1.2.3.4 验证与问题闭环**：对「关键技术指标权衡分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P1.2.3.5 文档输出与下游交付**：输出「关键技术指标权衡分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 概念验证（Proof of Concept）
- **方法 / 工具**：快速样机、关键子系统台架测试、技术 de-risk
- **设计思考逻辑**：对最高风险项（如关节峰值扭矩、单腿平衡、手指力控）提前验证
- **关键约束**：时间、预算、样机精度
- **完成标准 / 输出物**：POC 报告、风险降级记录、Go/No-Go 决策
**三级子任务：**
- **P1.2.4.1 输入梳理与目标量化**：整理「概念验证（Proof of Concept）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P1.2.4.2 方案/方法设计**：针对「概念验证（Proof of Concept）」制定实施方法或候选方案，使用「快速样机、关键子系统台架测试、技术 de-risk」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P1.2.4.3 实施/原型/样件制作**：根据设计方案执行「概念验证（Proof of Concept）」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P1.2.4.4 测试执行与结果分析**：按照验收标准执行「概念验证（Proof of Concept）」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P1.2.4.5 文档输出与下游交付**：输出「概念验证（Proof of Concept）」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
Requirements Definition and System Concept (Concept / Pre-A) is the first stage in the full lifecycle of humanoid robot product development, expanded into several Level-3 sub-tasks in WBS V3.
## Content
This stage covers complete engineering actions such as input review, concept design, implementation/prototyping, verification closure, and documentation delivery, serving as a critical checkpoint to ensure downstream dependencies receive qualified inputs.

## Key Sub-tasks and Technical Content
#### Requirements Engineering

##### Stakeholder Requirements Elicitation
- **Methods / Tools**: Interviews, questionnaires, workshops, on-site observation, Kano model
- **Design Thinking Logic**: Identify explicit and implicit needs; distinguish Must-have / Differentiator / Exciter
- **Key Constraints**: Time, sample representativeness, requirement conflicts
- **Completion Criteria / Deliverables**: Stakeholder list, requirements pool, priority ranking
**Level-3 Sub-tasks:**
- **P1.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Stakeholder Requirements Elicitation"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P1.1.1.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "Stakeholder Requirements Elicitation"; demonstrate using "Interviews, questionnaires, workshops, on-site observation, Kano model"; clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P1.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Stakeholder Requirements Elicitation" according to the design solution; create prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P1.1.1.4 Verification and Issue Closure**: Verify the output of "Stakeholder Requirements Elicitation"; check if completion criteria are met; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P1.1.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Stakeholder Requirements Elicitation"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### System Requirements Specification (SyRS)
- **Methods / Tools**: SysML use case diagrams, requirements tree, SMART principle
- **Design Thinking Logic**: Translate business language into engineering language: dimensions, weight, DOF, speed, payload, endurance, safety level
- **Key Constraints**: Indicator coupling, test feasibility, cost drivers
- **Completion Criteria / Deliverables**: SyRS baseline release, requirements traceability, quantified acceptance conditions
**Level-3 Sub-tasks:**
- **P1.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "System Requirements Specification (SyRS)"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P1.1.2.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "System Requirements Specification (SyRS)"; demonstrate using "SysML use case diagrams, requirements tree, SMART principle"; clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P1.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "System Requirements Specification (SyRS)" according to the design solution; create prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P1.1.2.4 Verification and Issue Closure**: Verify the output of "System Requirements Specification (SyRS)"; check if completion criteria are met; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P1.1.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "System Requirements Specification (SyRS)"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Regulatory, Standards, and Safety Requirements Mapping
- **Methods / Tools**: ISO 10218-1/2, ISO/TS 15066, IEC 61508, IEC 62368, CE/FCC/UL gap analysis
- **Design Thinking Logic**: Safety requirements must become hard constraints early in design, not retrofitted later
- **Key Constraints**: Regional differences, certification cycles, testing costs
- **Completion Criteria / Deliverables**: Regulatory requirements matrix, compliance roadmap, safety integrity level (SIL/PL)
**Level-3 Sub-tasks:**
- **P1.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Regulatory, Standards, and Safety Requirements Mapping"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P1.1.3.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "Regulatory, Standards, and Safety Requirements Mapping"; demonstrate using "ISO 10218-1/2, ISO/TS 15066, IEC 61508, IEC 62368, CE/FCC/UL gap analysis"; clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P1.1.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Regulatory, Standards, and Safety Requirements Mapping" according to the design solution; create prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P1.1.3.4 Verification and Issue Closure**: Verify the output of "Regulatory, Standards, and Safety Requirements Mapping"; check if completion criteria are met; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P1.1.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Regulatory, Standards, and Safety Requirements Mapping"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Human Factors Engineering and Interaction Requirements
- **Methods / Tools**: Anthropometric databases, reach envelope analysis, startle response experiments, HMI prototypes
- **Design Thinking Logic**: In human-robot coexistence scenarios, height, field of view, sound, and motion must be acceptable
- **Key Constraints**: Cultural differences, user group diversity, psychological safety
- **Completion Criteria / Deliverables**: Human factors requirements report, key interaction posture envelopes, HMI principles
**Level-3 Sub-tasks:**
- **P1.1.4.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Human Factors Engineering and Interaction Requirements"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P1.1.4.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "Human Factors Engineering and Interaction Requirements"; demonstrate using "Anthropometric databases, reach envelope analysis, startle response experiments, HMI prototypes"; clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P1.1.4.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Human Factors Engineering and Interaction Requirements" according to the design solution; create prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P1.1.4.4 Verification and Issue Closure**: Verify the output of "Human Factors Engineering and Interaction Requirements"; check if completion criteria are met; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P1.1.4.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Human Factors Engineering and Interaction Requirements"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

#### Concept Design

##### Concept Divergence and Convergence
- **Methods / Tools**: Brainstorming, morphological sketches, Morphological Matrix, Pugh Matrix
- **Design Thinking Logic**: Systematically evaluate multiple whole-body layouts, actuation schemes, and sensing schemes
- **Key Constraints**: Technology readiness, cost, manufacturability
- **Completion Criteria / Deliverables**: At least 3 concept solutions, scoring matrix, rationale for selected solution
**Level-3 Sub-tasks:**
- **P1.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Concept Divergence and Convergence"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P1.2.1.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "Concept Divergence and Convergence"; demonstrate using "Brainstorming, morphological sketches, Morphological Matrix, Pugh Matrix"; clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P1.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Concept Divergence and Convergence" according to the design solution; create prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P1.2.1.4 Verification and Issue Closure**: Verify the output of "Concept Divergence and Convergence"; check if completion criteria are met; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P1.2.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Concept Divergence and Convergence"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Whole-Body Architecture and Function Allocation
- **Methods / Tools**: Functional decomposition, N² diagram, Interface Control Document (ICD) draft
- **Design Thinking Logic**: Define boundaries of motion, manipulation, perception, computation, power, thermal management, and structural subsystems
- **Key Constraints**: Real-time performance, power consumption, cable count, maintainability
- **Completion Criteria / Deliverables**: System architecture diagram, function allocation table, ICD draft
**Level-3 Sub-tasks:**
- **P1.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Whole-Body Architecture and Function Allocation"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P1.2.2.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "Whole-Body Architecture and Function Allocation"; demonstrate using "Functional decomposition, N² diagram, Interface Control Document (ICD) draft"; clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P1.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Whole-Body Architecture and Function Allocation" according to the design solution; create prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P1.2.2.4 Verification and Issue Closure**: Verify the output of "Whole-Body Architecture and Function Allocation"; check if completion criteria are met; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P1.2.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Whole-Body Architecture and Function Allocation"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Key Technical Indicator Trade-off Analysis
- **Methods / Tools**: Multi-objective optimization, Pareto frontier, sensitivity analysis
- **Design Thinking Logic**: Speed vs. endurance vs. cost vs. payload; find an acceptable design space
- **Key Constraints**: Physical limits, supply chain capability, budget
- **Completion Criteria / Deliverables**: Trade-off analysis table, indicator boundaries, design space diagram
**Level-3 Sub-tasks:**
- **P1.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Key Technical Indicator Trade-off Analysis"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P1.2.3.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "Key Technical Indicator Trade-off Analysis"; demonstrate using "Multi-objective optimization, Pareto frontier, sensitivity analysis"; clarify technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P1.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Key Technical Indicator Trade-off Analysis" according to the design solution; create prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P1.2.3.4 Verification and Issue Closure**: Verify the output of "Key Technical Indicator Trade-off Analysis"; check if completion criteria are met; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P1.2.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Key Technical Indicator Trade-off Analysis"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

## 개요
요구사항 정의 및 시스템 개념(Concept / Pre-A)은 휴머노이드 로봇 제품 개발 전 과정의 첫 번째 단계로, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.
## 핵심 내용
이 단계는 입력 정리, 설계, 구현/프로토타입, 검증 폐쇄 및 문서 인도 등 완전한 엔지니어링 활동을 포괄하며, 하위 의존 부서가 적격한 입력을 확보하는 핵심 관문입니다.

## 주요 하위 작업 및 기술 내용
#### 요구사항 엔지니어링

##### 이해관계자 요구사항 수집
- **방법 / 도구**: 인터뷰, 설문조사, 워크숍, 현장 촬영, Kano 모델
- **설계 사고 논리**: 명시적 및 암묵적 요구사항 식별; Must-have / Differentiator / Exciter 구분
- **주요 제약 조건**: 시간, 표본 대표성, 요구사항 충돌
- **완료 기준 / 산출물**: 이해관계자 목록, 요구사항 풀, 우선순위 정렬
**3레벨 하위 작업:**
- **P1.1.1.1 입력 정리 및 목표 정량화**: 「이해관계자 요구사항 수집」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록부 구축
- **P1.1.1.2 설계/방법 설계**: 「이해관계자 요구사항 수집」에 대한 구현 방법 또는 후보 설계를 수립하고, 「인터뷰, 설문조사, 워크숍, 현장 촬영, Kano 모델」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 최소 2개의 후보 설계 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 설계 확정
- **P1.1.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「이해관계자 요구사항 수집」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P1.1.1.4 검증 및 문제 폐쇄**: 「이해관계자 요구사항 수집」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P1.1.1.5 문서 출력 및 하위 인도**: 「이해관계자 요구사항 수집」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 시스템 요구사항 명세서 (SyRS)
- **방법 / 도구**: SysML 유스케이스 다이어그램, 요구사항 트리, SMART 원칙
- **설계 사고 논리**: 비즈니스 언어를 엔지니어링 언어로 변환: 크기, 무게, DOF, 속도, 부하, 배터리 수명, 안전 등급
- **주요 제약 조건**: 지표 결합, 테스트 가능성, 비용 주도
- **완료 기준 / 산출물**: SyRS 기준선 릴리스, 요구사항 추적 가능, 검수 조건 정량화
**3레벨 하위 작업:**
- **P1.1.2.1 입력 정리 및 목표 정량화**: 「시스템 요구사항 명세서 (SyRS)」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록부 구축
- **P1.1.2.2 설계/방법 설계**: 「시스템 요구사항 명세서 (SyRS)」에 대한 구현 방법 또는 후보 설계를 수립하고, 「SysML 유스케이스 다이어그램, 요구사항 트리, SMART 원칙」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 최소 2개의 후보 설계 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 설계 확정
- **P1.1.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「시스템 요구사항 명세서 (SyRS)」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P1.1.2.4 검증 및 문제 폐쇄**: 「시스템 요구사항 명세서 (SyRS)」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P1.1.2.5 문서 출력 및 하위 인도**: 「시스템 요구사항 명세서 (SyRS)」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 법규, 표준 및 안전 요구사항 매핑
- **방법 / 도구**: ISO 10218-1/2, ISO/TS 15066, IEC 61508, IEC 62368, CE/FCC/UL 차이 분석
- **설계 사고 논리**: 안전 요구사항은 설계 초기에 하드 제약 조건이 되어야 하며, 후반에 추가되어서는 안 됨
- **주요 제약 조건**: 지역 차이, 인증 주기, 테스트 비용
- **완료 기준 / 산출물**: 법규 요구사항 매트릭스, 규정 준수 로드맵, 안전 목표 등급 (SIL/PL)
**3레벨 하위 작업:**
- **P1.1.3.1 입력 정리 및 목표 정량화**: 「법규, 표준 및 안전 요구사항 매핑」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록부 구축
- **P1.1.3.2 설계/방법 설계**: 「법규, 표준 및 안전 요구사항 매핑」에 대한 구현 방법 또는 후보 설계를 수립하고, 「ISO 10218-1/2, ISO/TS 15066, IEC 61508, IEC 62368, CE/FCC/UL 차이 분석」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 최소 2개의 후보 설계 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 설계 확정
- **P1.1.3.3 구현/프로토타입/시제품 제작**: 설계에 따라 「법규, 표준 및 안전 요구사항 매핑」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P1.1.3.4 검증 및 문제 폐쇄**: 「법규, 표준 및 안전 요구사항 매핑」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P1.1.3.5 문서 출력 및 하위 인도**: 「법규, 표준 및 안전 요구사항 매핑」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 인간공학 및 상호작용 요구사항
- **방법 / 도구**: 인체 측정 데이터베이스, 도달 가능 영역 분석, 놀람 반응 실험, HMI 프로토타입
- **설계 사고 논리**: 로봇과 인간이 공존하는 시나리오에서 높이, 시야, 소리, 동작이 수용 가능해야 함
- **주요 제약 조건**: 문화 차이, 사용자 그룹 다양성, 심리적 안전
- **완료 기준 / 산출물**: 인간공학 요구사항 보고서, 주요 상호작용 자세 포락선, HMI 원칙
**3레벨 하위 작업:**
- **P1.1.4.1 입력 정리 및 목표 정량화**: 「인간공학 및 상호작용 요구사항」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록부 구축
- **P1.1.4.2 설계/방법 설계**: 「인간공학 및 상호작용 요구사항」에 대한 구현 방법 또는 후보 설계를 수립하고, 「인체 측정 데이터베이스, 도달 가능 영역 분석, 놀람 반응 실험, HMI 프로토타입」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 최소 2개의 후보 설계 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 설계 확정
- **P1.1.4.3 구현/프로토타입/시제품 제작**: 설계에 따라 「인간공학 및 상호작용 요구사항」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P1.1.4.4 검증 및 문제 폐쇄**: 「인간공학 및 상호작용 요구사항」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P1.1.4.5 문서 출력 및 하위 인도**: 「인간공학 및 상호작용 요구사항」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

#### 개념 설계

##### 개념 설계 발산 및 수렴
- **방법 / 도구**: 브레인스토밍, 형태 스케치, Morphological Matrix, Pugh Matrix
- **설계 사고 논리**: 다양한 전체 기체 레이아웃, 구동 방식, 센서 방식에서 체계적으로 평가
- **주요 제약 조건**: 기술 성숙도, 비용, 제조 가능성
- **완료 기준 / 산출물**: 최소 3개의 개념 설계, 점수 매트릭스, 선택된 설계 이유
**3레벨 하위 작업:**
- **P1.2.1.1 입력 정리 및 목표 정량화**: 「개념 설계 발산 및 수렴」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록부 구축
- **P1.2.1.2 설계/방법 설계**: 「개념 설계 발산 및 수렴」에 대한 구현 방법 또는 후보 설계를 수립하고, 「브레인스토밍, 형태 스케치, Morphological Matrix, Pugh Matrix」를 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 최소 2개의 후보 설계 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 설계 확정
- **P1.2.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「개념 설계 발산 및 수렴」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P1.2.1.4 검증 및 문제 폐쇄**: 「개념 설계 발산 및 수렴」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P1.2.1.5 문서 출력 및 하위 인도**: 「개념 설계 발산 및 수렴」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 전체 기체 아키텍처 및 기능 할당
- **방법 / 도구**: 기능 분해, N² 다이어그램, 인터페이스 제어 문서 (ICD) 초안
- **설계 사고 논리**: 운동, 조작, 인지, 계산, 에너지, 열 관리, 구조 서브시스템의 경계 명확화
- **주요 제약 조건**: 실시간성, 전력 소비, 케이블 수, 유지보수성
- **완료 기준 / 산출물**: 시스템 아키텍처 다이어그램, 기능 할당표, ICD 초안
**3레벨 하위 작업:**
- **P1.2.2.1 입력 정리 및 목표 정량화**: 「전체 기체 아키텍처 및 기능 할당」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록부 구축
- **P1.2.2.2 설계/방법 설계**: 「전체 기체 아키텍처 및 기능 할당」에 대한 구현 방법 또는 후보 설계를 수립하고, 「기능 분해, N² 다이어그램, 인터페이스 제어 문서 (ICD) 초안」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 최소 2개의 후보 설계 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 설계 확정
- **P1.2.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「전체 기체 아키텍처 및 기능 할당」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P1.2.2.4 검증 및 문제 폐쇄**: 「전체 기체 아키텍처 및 기능 할당」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P1.2.2.5 문서 출력 및 하위 인도**: 「전체 기체 아키텍처 및 기능 할당」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 핵심 기술 지표 트레이드오프 분석
- **방법 / 도구**: 다목적 최적화, Pareto 프론티어, 민감도 분석
- **설계 사고 논리**: 속도 vs 배터리 수명 vs 비용 vs 부하; 수용 가능한 설계 공간 찾기
- **주요 제약 조건**: 물리적 한계, 공급망 역량, 예산
- **완료 기준 / 산출물**: 트레이드오프 분석표, 지표 경계, 설계 공간 도표
**3레벨 하위 작업:**
- **P1.2.3.1 입력 정리 및 목표 정량화**: 「핵심 기술 지표 트레이드오프 분석」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록부 구축
- **P1.2.3.2 설계/방법 설계**: 「핵심 기술 지표 트레이드오프 분석」에 대한 구현 방법 또는 후보 설계를 수립하고, 「다목적 최적화, Pareto 프론티어, 민감도 분석」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 최소 2개의 후보 설계 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 설계 확정
- **P1.2.3.3 구현/프로토타입/시제품 제작**: 설계에 따라 「핵심 기술 지표 트레이드오프 분석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P1.2.3.4 검증 및 문제 폐쇄**: 「핵심 기술 지표 트레이드오프 분석」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P1.2.3.5 문서 출력 및 하위 인도**: 「핵심 기술 지표 트레이드오프 분석」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지
