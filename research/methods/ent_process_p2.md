---
$id: ent_process_p2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Industrial Design and Appearance Engineering (ID / A-Surface)
  zh: 工业设计与外观工程（ID / A-Surface）
  ko: 工业设计与外观工程（ID / A-Surface）
summary:
  en: Industrial Design and Appearance Engineering (ID / A-Surface) —— Phase 2 of the humanoid robot product development process,
    covering solution design, implementation verification, and documentation delivery.
  zh: 工业设计与外观工程（ID / A-Surface）是人形机器人产品开发全流程中的第 2 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 工业设计与外观工程（ID / A-Surface）
domains:
- 06_design_engineering
layers:
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
工业设计与外观工程（ID / A-Surface）是人形机器人产品开发全流程中的第 2 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 造型与品牌定义

##### 设计语言与品牌 DNA
- **方法 / 工具**：情绪板、形态趋势研究、品牌符号提取
- **设计思考逻辑**：外观是产品差异化的重要载体，同时必须服务功能
- **关键约束**：内部机构空间、散热开口、维护开口、CMF 成本
- **完成标准 / 输出物**：设计语言指南、3 套造型方向
**三级子任务：**
- **P2.1.1.1 输入梳理与目标量化**：整理「设计语言与品牌 DNA」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P2.1.1.2 概念与详细设计**：完成「设计语言与品牌 DNA」的概念设计、详细设计与接口定义，使用「情绪板、形态趋势研究、品牌符号提取」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P2.1.1.3 实施/原型/样件制作**：根据设计方案执行「设计语言与品牌 DNA」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P2.1.1.4 验证与问题闭环**：对「设计语言与品牌 DNA」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P2.1.1.5 文档输出与下游交付**：输出「设计语言与品牌 DNA」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### A 面 3D 建模与可视化
- **方法 / 工具**：Alias / Rhino / Blender / Cinema 4D、KeyShot 渲染
- **设计思考逻辑**：在外观冻结前充分验证比例、姿态、视觉重心
- **关键约束**：曲面可制造性、喷涂/覆膜工艺、光学传感器窗口
- **完成标准 / 输出物**：高精度 A 面、渲染图、CMF 方案、关键视角评审通过
**三级子任务：**
- **P2.1.2.1 输入梳理与目标量化**：整理「A 面 3D 建模与可视化」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P2.1.2.2 方案/方法设计**：针对「A 面 3D 建模与可视化」制定实施方法或候选方案，使用「Alias / Rhino / Blender / Cinema 4D、KeyShot 渲染」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P2.1.2.3 实施/原型/样件制作**：根据设计方案执行「A 面 3D 建模与可视化」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P2.1.2.4 验证与问题闭环**：对「A 面 3D 建模与可视化」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P2.1.2.5 文档输出与下游交付**：输出「A 面 3D 建模与可视化」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 外观手板与比例模型
- **方法 / 工具**：SLA/SLS 3D 打印、泡沫 CNC、喷漆、覆膜
- **设计思考逻辑**：1:1 物理模型验证视觉比例、装配空间、人机交互
- **关键约束**：手板材料不等于量产材料、强度有限
- **完成标准 / 输出物**：1:1 外观手板、评审纪要、问题清单
**三级子任务：**
- **P2.1.3.1 输入梳理与目标量化**：整理「外观手板与比例模型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P2.1.3.2 方案/方法设计**：针对「外观手板与比例模型」制定实施方法或候选方案，使用「SLA/SLS 3D 打印、泡沫 CNC、喷漆、覆膜」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P2.1.3.3 实施/原型/样件制作**：根据设计方案执行「外观手板与比例模型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P2.1.3.4 验证与问题闭环**：对「外观手板与比例模型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P2.1.3.5 文档输出与下游交付**：输出「外观手板与比例模型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 人机工程与交互设计

##### 人体尺度与可达域分析
- **方法 / 工具**：人体测量数据库、CATIA / Jack / RAMSIS、可达域云图
- **设计思考逻辑**：验证机器人能完成目标场景所需的操作高度、视野与避障
- **关键约束**：关节运动范围未定、需预留裕量
- **完成标准 / 输出物**：可达域报告、关键操作姿态、干涉检查
**三级子任务：**
- **P2.2.1.1 输入梳理与目标量化**：整理「人体尺度与可达域分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P2.2.1.2 方案/方法设计**：针对「人体尺度与可达域分析」制定实施方法或候选方案，使用「人体测量数据库、CATIA / Jack / RAMSIS、可达域云图」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P2.2.1.3 实施/原型/样件制作**：根据设计方案执行「人体尺度与可达域分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P2.2.1.4 验证与问题闭环**：对「人体尺度与可达域分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P2.2.1.5 文档输出与下游交付**：输出「人体尺度与可达域分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 人机交互（HMI）设计
- **方法 / 工具**：用户旅程图、语音/手势/触屏/灯语原型、可用性测试
- **设计思考逻辑**：降低用户使用门槛，建立信任与可预测性
- **关键约束**：多模态一致性、响应延迟、误触发
- **完成标准 / 输出物**：HMI 规范、交互原型、可用性测试报告
**三级子任务：**
- **P2.2.2.1 输入梳理与目标量化**：整理「人机交互（HMI）设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P2.2.2.2 概念与详细设计**：完成「人机交互（HMI）设计」的概念设计、详细设计与接口定义，使用「用户旅程图、语音/手势/触屏/灯语原型、可用性测试」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P2.2.2.3 实施/原型/样件制作**：根据设计方案执行「人机交互（HMI）设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P2.2.2.4 验证与问题闭环**：对「人机交互（HMI）设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P2.2.2.5 文档输出与下游交付**：输出「人机交互（HMI）设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### ID-结构接口冻结
- **方法 / 工具**：GD&T、安装点布局、分缝/拆卸方案联合评审
- **设计思考逻辑**：外观面与内部骨架的接口必须在详细设计前确定
- **关键约束**：后续修改成本高、模具周期长
- **完成标准 / 输出物**：《ID-结构接口规范》、安装点图、密封等级定义
**三级子任务：**
- **P2.2.3.1 输入梳理与目标量化**：整理「ID-结构接口冻结」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P2.2.3.2 方案/方法设计**：针对「ID-结构接口冻结」制定实施方法或候选方案，使用「GD&T、安装点布局、分缝/拆卸方案联合评审」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P2.2.3.3 实施/原型/样件制作**：根据设计方案执行「ID-结构接口冻结」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P2.2.3.4 验证与问题闭环**：对「ID-结构接口冻结」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P2.2.3.5 文档输出与下游交付**：输出「ID-结构接口冻结」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
Industrial Design / A-Surface Engineering (ID / A-Surface) is the second stage in the full-process development of humanoid robot products, expanded into several Level-3 sub-tasks in WBS V3.
## Content
This stage covers complete engineering actions such as input review, concept design, implementation/prototyping, verification closure, and documentation delivery, serving as a critical node to ensure downstream dependencies receive qualified inputs.

## Key Sub-Tasks and Technical Content
#### Styling and Brand Definition

##### Design Language and Brand DNA
- **Methods / Tools**: Mood boards, form trend research, brand symbol extraction
- **Design Thinking Logic**: Appearance is an important carrier of product differentiation, while also serving functionality
- **Key Constraints**: Internal mechanism space, heat dissipation openings, maintenance openings, CMF cost
- **Completion Criteria / Deliverables**: Design language guide, 3 styling directions
**Level-3 Sub-Tasks:**
- **P2.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Design Language and Brand DNA"; convert completion criteria into quantifiable acceptance indicators; clarify Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P2.1.1.2 Concept and Detailed Design**: Complete concept design, detailed design, and interface definition for "Design Language and Brand DNA"; verify feasibility using "mood boards, form trend research, brand symbol extraction"; output drawings/algorithms/logical frameworks.
**Level-4 Key Actions:**
1. Develop no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P2.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Design Language and Brand DNA" according to the design plan; fabricate prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P2.1.1.4 Verification and Issue Closure**: Verify the output of "Design Language and Brand DNA" against completion criteria; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P2.1.1.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Design Language and Brand DNA"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Class-A Surface 3D Modeling and Visualization
- **Methods / Tools**: Alias / Rhino / Blender / Cinema 4D, KeyShot rendering
- **Design Thinking Logic**: Fully verify proportions, posture, and visual center of gravity before appearance freeze
- **Key Constraints**: Surface manufacturability, painting/film coating processes, optical sensor windows
- **Completion Criteria / Deliverables**: High-precision Class-A surface, renderings, CMF scheme, key perspective review approval
**Level-3 Sub-Tasks:**
- **P2.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Class-A Surface 3D Modeling and Visualization"; convert completion criteria into quantifiable acceptance indicators; clarify Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P2.1.2.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Class-A Surface 3D Modeling and Visualization"; demonstrate using "Alias / Rhino / Blender / Cinema 4D, KeyShot rendering"; clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Develop no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P2.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Class-A Surface 3D Modeling and Visualization" according to the design plan; fabricate prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P2.1.2.4 Verification and Issue Closure**: Verify the output of "Class-A Surface 3D Modeling and Visualization" against completion criteria; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P2.1.2.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Class-A Surface 3D Modeling and Visualization"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Appearance Mockup and Scale Model
- **Methods / Tools**: SLA/SLS 3D printing, foam CNC, painting, film coating
- **Design Thinking Logic**: 1:1 physical model to verify visual proportions, assembly space, and human-robot interaction
- **Key Constraints**: Mockup materials differ from production materials; limited strength
- **Completion Criteria / Deliverables**: 1:1 appearance mockup, review minutes, issue list
**Level-3 Sub-Tasks:**
- **P2.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Appearance Mockup and Scale Model"; convert completion criteria into quantifiable acceptance indicators; clarify Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P2.1.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Appearance Mockup and Scale Model"; demonstrate using "SLA/SLS 3D printing, foam CNC, painting, film coating"; clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Develop no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P2.1.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Appearance Mockup and Scale Model" according to the design plan; fabricate prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P2.1.3.4 Verification and Issue Closure**: Verify the output of "Appearance Mockup and Scale Model" against completion criteria; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P2.1.3.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Appearance Mockup and Scale Model"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

#### Ergonomics and Interaction Design

##### Human Body Dimensions and Reachability Analysis
- **Methods / Tools**: Anthropometric databases, CATIA / Jack / RAMSIS, reachability cloud maps
- **Design Thinking Logic**: Verify the robot's ability to achieve required operation heights, field of view, and obstacle avoidance for target scenarios
- **Key Constraints**: Joint range of motion not yet determined; margin must be reserved
- **Completion Criteria / Deliverables**: Reachability report, key operation postures, interference check
**Level-3 Sub-Tasks:**
- **P2.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Human Body Dimensions and Reachability Analysis"; convert completion criteria into quantifiable acceptance indicators; clarify Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P2.2.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Human Body Dimensions and Reachability Analysis"; demonstrate using "anthropometric databases, CATIA / Jack / RAMSIS, reachability cloud maps"; clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Develop no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P2.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Human Body Dimensions and Reachability Analysis" according to the design plan; fabricate prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P2.2.1.4 Verification and Issue Closure**: Verify the output of "Human Body Dimensions and Reachability Analysis" against completion criteria; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P2.2.1.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Human Body Dimensions and Reachability Analysis"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Human-Machine Interaction (HMI) Design
- **Methods / Tools**: User journey maps, voice/gesture/touchscreen/light language prototypes, usability testing
- **Design Thinking Logic**: Lower user adoption barriers, build trust and predictability
- **Key Constraints**: Multimodal consistency, response latency, false triggers
- **Completion Criteria / Deliverables**: HMI specification, interaction prototype, usability test report
**Level-3 Sub-Tasks:**
- **P2.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Human-Machine Interaction (HMI) Design"; convert completion criteria into quantifiable acceptance indicators; clarify Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P2.2.2.2 Concept and Detailed Design**: Complete concept design, detailed design, and interface definition for "Human-Machine Interaction (HMI) Design"; verify feasibility using "user journey maps, voice/gesture/touchscreen/light language prototypes, usability testing"; output drawings/algorithms/logical frameworks.
**Level-4 Key Actions:**
1. Develop no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P2.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Human-Machine Interaction (HMI) Design" according to the design plan; fabricate prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P2.2.2.4 Verification and Issue Closure**: Verify the output of "Human-Machine Interaction (HMI) Design" against completion criteria; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P2.2.2.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "Human-Machine Interaction (HMI) Design"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### ID-Structure Interface Freeze
- **Methods / Tools**: GD&T, mounting point layout, joint review of parting lines/disassembly schemes
- **Design Thinking Logic**: Interfaces between appearance surfaces and internal skeleton must be determined before detailed design
- **Key Constraints**: High cost of subsequent modifications, long mold cycle
- **Completion Criteria / Deliverables**: "ID-Structure Interface Specification", mounting point drawing, sealing level definition
**Level-3 Sub-Tasks:**
- **P2.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "ID-Structure Interface Freeze"; convert completion criteria into quantifiable acceptance indicators; clarify Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P2.2.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "ID-Structure Interface Freeze"; demonstrate using "GD&T, mounting point layout, joint review of parting lines/disassembly schemes"; clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Develop no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P2.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "ID-Structure Interface Freeze" according to the design plan; fabricate prototypes, samples, or complete key steps; record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P2.2.3.4 Verification and Issue Closure**: Verify the output of "ID-Structure Interface Freeze" against completion criteria; record issues and track to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P2.2.3.5 Documentation Output and Downstream Delivery**: Output final report/drawings/specifications for "ID-Structure Interface Freeze"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

## Completion Criteria
All Level-3 sub-tasks in this stage have passed acceptance review; key deliverables are version-controlled and formally delivered to downstream dependencies.

## 개요
산업 디자인 및 외관 엔지니어링(ID / A-Surface)은 휴머노이드 로봇 제품 개발 전 과정 중 두 번째 단계로, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.

## 핵심 내용
이 단계는 입력 정리, 설계 방안, 구현/프로토타입, 검증 폐쇄 및 문서 인도 등 완전한 엔지니어링 활동을 포함하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 단계입니다.

## 주요 하위 작업 및 기술 내용
#### 디자인 및 브랜드 정의

##### 디자인 언어 및 브랜드 DNA
- **방법 / 도구**: 무드보드, 형태 트렌드 연구, 브랜드 심볼 추출
- **디자인 사고 논리**: 외관은 제품 차별화의 중요한 수단이며, 동시에 기능을 지원해야 함
- **주요 제약 조건**: 내부 기구 공간, 방열 개구부, 유지보수 개구부, CMF 비용
- **완료 기준 / 산출물**: 디자인 언어 가이드, 3가지 디자인 방향
**3레벨 하위 작업:**
- **P2.1.1.1 입력 정리 및 목표 정량화**: 「디자인 언어 및 브랜드 DNA」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 주요 활동:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P2.1.1.2 개념 및 상세 설계**: 「디자인 언어 및 브랜드 DNA」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「무드보드, 형태 트렌드 연구, 브랜드 심볼 추출」을 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력함.
**4레벨 주요 활동:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P2.1.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「디자인 언어 및 브랜드 DNA」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 주요 활동:**
1. 모델/시제품 구축 및 주요 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P2.1.1.4 검증 및 문제 폐쇄**: 「디자인 언어 및 브랜드 DNA」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적함.
**4레벨 주요 활동:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P2.1.1.5 문서 출력 및 하위 인도**: 「디자인 언어 및 브랜드 DNA」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 주요 활동:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### A면 3D 모델링 및 시각화
- **방법 / 도구**: Alias / Rhino / Blender / Cinema 4D, KeyShot 렌더링
- **디자인 사고 논리**: 외관 확정 전에 비율, 자세, 시각적 중심을 충분히 검증
- **주요 제약 조건**: 곡면 제조 가능성, 도장/필름 공정, 광학 센서 창
- **완료 기준 / 산출물**: 고정밀 A면, 렌더링 이미지, CMF 방안, 주요 시점 검토 통과
**3레벨 하위 작업:**
- **P2.1.2.1 입력 정리 및 목표 정량화**: 「A면 3D 모델링 및 시각화」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 주요 활동:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P2.1.2.2 방안/방법 설계**: 「A면 3D 모델링 및 시각화」에 대한 구현 방법 또는 후보 방안을 수립하고, 「Alias / Rhino / Blender / Cinema 4D, KeyShot 렌더링」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 함.
**4레벨 주요 활동:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P2.1.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「A면 3D 모델링 및 시각화」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 주요 활동:**
1. 모델/시제품 구축 및 주요 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P2.1.2.4 검증 및 문제 폐쇄**: 「A면 3D 모델링 및 시각화」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적함.
**4레벨 주요 활동:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P2.1.2.5 문서 출력 및 하위 인도**: 「A면 3D 모델링 및 시각화」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 주요 활동:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 외관 핸드메이드 및 축소 모형
- **방법 / 도구**: SLA/SLS 3D 프린팅, 폼 CNC, 도장, 필름
- **디자인 사고 논리**: 1:1 물리적 모형으로 시각적 비율, 조립 공간, 인간-로봇 상호작용 검증
- **주요 제약 조건**: 핸드메이드 재료는 양산 재료와 다르며, 강도가 제한적임
- **완료 기준 / 산출물**: 1:1 외관 핸드메이드, 검토 회의록, 문제 목록
**3레벨 하위 작업:**
- **P2.1.3.1 입력 정리 및 목표 정량화**: 「외관 핸드메이드 및 축소 모형」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 주요 활동:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P2.1.3.2 방안/방법 설계**: 「외관 핸드메이드 및 축소 모형」에 대한 구현 방법 또는 후보 방안을 수립하고, 「SLA/SLS 3D 프린팅, 폼 CNC, 도장, 필름」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 함.
**4레벨 주요 활동:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P2.1.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「외관 핸드메이드 및 축소 모형」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 주요 활동:**
1. 모델/시제품 구축 및 주요 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P2.1.3.4 검증 및 문제 폐쇄**: 「외관 핸드메이드 및 축소 모형」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적함.
**4레벨 주요 활동:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P2.1.3.5 문서 출력 및 하위 인도**: 「외관 핸드메이드 및 축소 모형」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 주요 활동:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

#### 인간공학 및 상호작용 설계

##### 인체 치수 및 도달 범위 분석
- **방법 / 도구**: 인체 측정 데이터베이스, CATIA / Jack / RAMSIS, 도달 범위 클라우드 맵
- **디자인 사고 논리**: 로봇이 목표 시나리오에 필요한 작업 높이, 시야 및 장애물 회피를 수행할 수 있는지 검증
- **주요 제약 조건**: 관절 운동 범위 미확정, 여유분 확보 필요
- **완료 기준 / 산출물**: 도달 범위 보고서, 주요 작업 자세, 간섭 검사
**3레벨 하위 작업:**
- **P2.2.1.1 입력 정리 및 목표 정량화**: 「인체 치수 및 도달 범위 분석」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 주요 활동:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P2.2.1.2 방안/방법 설계**: 「인체 치수 및 도달 범위 분석」에 대한 구현 방법 또는 후보 방안을 수립하고, 「인체 측정 데이터베이스, CATIA / Jack / RAMSIS, 도달 범위 클라우드 맵」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 함.
**4레벨 주요 활동:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P2.2.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「인체 치수 및 도달 범위 분석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 주요 활동:**
1. 모델/시제품 구축 및 주요 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P2.2.1.4 검증 및 문제 폐쇄**: 「인체 치수 및 도달 범위 분석」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적함.
**4레벨 주요 활동:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P2.2.1.5 문서 출력 및 하위 인도**: 「인체 치수 및 도달 범위 분석」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 주요 활동:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 인간-로봇 상호작용(HMI) 설계
- **방법 / 도구**: 사용자 여정 맵, 음성/제스처/터치스크린/라이트 신호 프로토타입, 사용성 테스트
- **디자인 사고 논리**: 사용자 사용 장벽을 낮추고, 신뢰와 예측 가능성 구축
- **주요 제약 조건**: 다중 모드 일관성, 응답 지연, 오작동
- **완료 기준 / 산출물**: HMI 규격, 상호작용 프로토타입, 사용성 테스트 보고서
**3레벨 하위 작업:**
- **P2.2.2.1 입력 정리 및 목표 정량화**: 「인간-로봇 상호작용(HMI) 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 주요 활동:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P2.2.2.2 개념 및 상세 설계**: 「인간-로봇 상호작용(HMI) 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「사용자 여정 맵, 음성/제스처/터치스크린/라이트 신호 프로토타입, 사용성 테스트」를 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력함.
**4레벨 주요 활동:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P2.2.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「인간-로봇 상호작용(HMI) 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 주요 활동:**
1. 모델/시제품 구축 및 주요 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P2.2.2.4 검증 및 문제 폐쇄**: 「인간-로봇 상호작용(HMI) 설계」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적함.
**4레벨 주요 활동:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P2.2.2.5 문서 출력 및 하위 인도**: 「인간-로봇 상호작용(HMI) 설계」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 주요 활동:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### ID-구조 인터페이스 확정
- **방법 / 도구**: GD&T, 장착점 배치, 분할선/분해 방안 공동 검토
- **디자인 사고 논리**: 외관면과 내부 골격의 인터페이스는 상세 설계 전에 결정되어야 함
- **주요 제약 조건**: 이후 수정 비용이 높고, 금형 주기가 길어짐
- **완료 기준 / 산출물**: 《ID-구조 인터페이스 규격》, 장착점 도면, 밀봉 등급 정의
**3레벨 하위 작업:**
- **P2.2.3.1 입력 정리 및 목표 정량화**: 「ID-구조 인터페이스 확정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 주요 활동:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P2.2.3.2 방안/방법 설계**: 「ID-구조 인터페이스 확정」에 대한 구현 방법 또는 후보 방안을 수립하고, 「GD&T, 장착점 배치, 분할선/분해 방안 공동 검토」를 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 함.
**4레벨 주요 활동:**
1. 최소 2개의 후보 방안 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및 방안 확정
- **P2.2.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「ID-구조 인터페이스 확정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 주요 활동:**
1. 모델/시제품 구축 및 주요 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P2.2.3.4 검증 및 문제 폐쇄**: 「ID-구조 인터페이스 확정」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적함.
**4레벨 주요 활동:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P2.2.3.5 문서 출력 및 하위 인도**: 「ID-구조 인터페이스 확정」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 주요 활동:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

## 완료 기준
본 단계의 모든 3레벨 하위 작업이 검수 검토를 통과하고, 주요 산출물의 버전이 관리되어 하위 의존 부서에 공식적으로 인도됩니다.
