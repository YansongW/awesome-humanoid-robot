---
$id: ent_process_p8
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Structural FEA and iteration
  zh: 结构强度仿真与迭代（Structural FEA）
  ko: 结构强度仿真与迭代（Structural FEA）
summary:
  en: Structural FEA-the 8th stage of the Android product development process, covering conceptual design, implementation
    verification, and document delivery.
  zh: 结构强度仿真与迭代（Structural FEA）是人形机器人产品开发全流程中的第 8 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 结构强度仿真与迭代（Structural FEA）
domains:
- 06_design_engineering
- 03_manufacturing_processes
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
结构强度仿真与迭代（Structural FEA）是人形机器人产品开发全流程中的第 8 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 载荷与仿真模型

##### 载荷工况定义
- **方法 / 工具**：静力学、动态冲击、跌落、典型运动反力、疲劳载荷谱
- **设计思考逻辑**：最严苛工况决定结构设计；包含单腿支撑、跌倒冲击、抓取最大负载
- **关键约束**：载荷传递路径、安全系数、测试验证
- **完成标准 / 输出物**：《载荷工况表》：载荷大小、方向、作用点、发生概率
**三级子任务：**
- **P8.1.1.1 输入梳理与目标量化**：整理「载荷工况定义」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P8.1.1.2 方案/方法设计**：针对「载荷工况定义」制定实施方法或候选方案，使用「静力学、动态冲击、跌落、典型运动反力、疲劳载荷谱」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P8.1.1.3 实施/原型/样件制作**：根据设计方案执行「载荷工况定义」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P8.1.1.4 验证与问题闭环**：对「载荷工况定义」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P8.1.1.5 文档输出与下游交付**：输出「载荷工况定义」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### FEA 模型准备
- **方法 / 工具**：HyperMesh / ANSA / Abaqus / ANSYS、网格收敛分析
- **设计思考逻辑**：简化非承力特征、合理网格划分、材料属性、接触/绑定设置
- **关键约束**：网格质量、计算时间、资源
- **完成标准 / 输出物**：高质量 FEA 模型、网格质量报告、边界条件清单
**三级子任务：**
- **P8.1.2.1 输入梳理与目标量化**：整理「FEA 模型准备」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P8.1.2.2 方案/方法设计**：针对「FEA 模型准备」制定实施方法或候选方案，使用「HyperMesh / ANSA / Abaqus / ANSYS、网格收敛分析」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P8.1.2.3 实施/原型/样件制作**：根据设计方案执行「FEA 模型准备」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P8.1.2.4 验证与问题闭环**：对「FEA 模型准备」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P8.1.2.5 文档输出与下游交付**：输出「FEA 模型准备」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 非线性分析与稳定性
- **方法 / 工具**：接触非线性、几何非线性、屈曲分析
- **设计思考逻辑**：薄壁结构在冲击下可能发生屈曲；大变形需考虑几何非线性
- **关键约束**：收敛难度、计算成本
- **完成标准 / 输出物**：屈曲模态、大变形下的应力/应变
**三级子任务：**
- **P8.1.3.1 输入梳理与目标量化**：整理「非线性分析与稳定性」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P8.1.3.2 方案/方法设计**：针对「非线性分析与稳定性」制定实施方法或候选方案，使用「接触非线性、几何非线性、屈曲分析」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P8.1.3.3 实施/原型/样件制作**：根据设计方案执行「非线性分析与稳定性」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P8.1.3.4 验证与问题闭环**：对「非线性分析与稳定性」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P8.1.3.5 文档输出与下游交付**：输出「非线性分析与稳定性」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 强度、疲劳与优化

##### 静动态应力与变形分析
- **方法 / 工具**：线弹性/弹塑性分析、von Mises、变形云图
- **设计思考逻辑**：校核关键件应力是否低于材料屈服/疲劳极限，变形是否影响运动
- **关键约束**：局部应力集中、焊缝/螺接模拟
- **完成标准 / 输出物**：《FEA 应力报告》：应力、变形、安全系数
**三级子任务：**
- **P8.2.1.1 输入梳理与目标量化**：整理「静动态应力与变形分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P8.2.1.2 方案/方法设计**：针对「静动态应力与变形分析」制定实施方法或候选方案，使用「线弹性/弹塑性分析、von Mises、变形云图」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P8.2.1.3 实施/原型/样件制作**：根据设计方案执行「静动态应力与变形分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P8.2.1.4 验证与问题闭环**：对「静动态应力与变形分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P8.2.1.5 文档输出与下游交付**：输出「静动态应力与变形分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 疲劳与寿命预估
- **方法 / 工具**：S-N 曲线、Miner 累积损伤、雨流计数
- **设计思考逻辑**：对高周疲劳部位（关节耳片、连杆孔边）进行寿命评估
- **关键约束**：载荷谱不确定性、材料疲劳数据
- **完成标准 / 输出物**：疲劳分析报告、关键件循环寿命 > 目标
**三级子任务：**
- **P8.2.2.1 输入梳理与目标量化**：整理「疲劳与寿命预估」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P8.2.2.2 方案/方法设计**：针对「疲劳与寿命预估」制定实施方法或候选方案，使用「S-N 曲线、Miner 累积损伤、雨流计数」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P8.2.2.3 实施/原型/样件制作**：根据设计方案执行「疲劳与寿命预估」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P8.2.2.4 验证与问题闭环**：对「疲劳与寿命预估」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P8.2.2.5 文档输出与下游交付**：输出「疲劳与寿命预估」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 轻量化与拓扑优化
- **方法 / 工具**：拓扑优化、尺寸优化、筋板/加强筋布置、复合材料替代
- **设计思考逻辑**：在应力裕量足够前提下减重，降低整机惯量与能耗
- **关键约束**：制造工艺限制、成本
- **完成标准 / 输出物**：优化后 CAD、减重比例 > 目标、强度仍满足
**三级子任务：**
- **P8.2.3.1 输入梳理与目标量化**：整理「轻量化与拓扑优化」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P8.2.3.2 方案/方法设计**：针对「轻量化与拓扑优化」制定实施方法或候选方案，使用「拓扑优化、尺寸优化、筋板/加强筋布置、复合材料替代」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P8.2.3.3 实施/原型/样件制作**：根据设计方案执行「轻量化与拓扑优化」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P8.2.3.4 验证与问题闭环**：对「轻量化与拓扑优化」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P8.2.3.5 文档输出与下游交付**：输出「轻量化与拓扑优化」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 仿真-试验闭环迭代
- **方法 / 工具**：原型加载试验、应变片、位移传感器、与 FEA 对比
- **设计思考逻辑**：通过试验修正仿真边界条件与材料参数，形成闭环
- **关键约束**：试验夹具、加载精度
- **完成标准 / 输出物**：仿真与试验误差 < 15%、设计迭代记录
**三级子任务：**
- **P8.2.4.1 输入梳理与目标量化**：整理「仿真-试验闭环迭代」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P8.2.4.2 接口与集成策略设计**：梳理「仿真-试验闭环迭代」涉及的子系统接口、数据流与时序，制定集成顺序、回退策略与异常处理机制。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P8.2.4.3 建模/仿真与样机实现**：建立「仿真-试验闭环迭代」的仿真/数学模型或原型样机，使用「原型加载试验、应变片、位移传感器、与 FEA 对比」执行计算或实验，记录关键参数与边界条件。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P8.2.4.4 测试执行与结果分析**：按照验收标准执行「仿真-试验闭环迭代」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P8.2.4.5 文档输出与下游交付**：输出「仿真-试验闭环迭代」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
Structural FEA (Finite Element Analysis) is the 8th stage in the full-process development of humanoid robot products, expanded into several Level-3 sub-tasks in WBS V3.

## Content
This stage covers complete engineering actions such as input review, scheme design, implementation/prototyping, verification closed-loop, and documentation delivery, serving as a critical milestone to ensure downstream dependents receive qualified inputs.

## Key Sub-tasks and Technical Content
#### Loads and Simulation Models

##### Load Case Definition
- **Methods/Tools**: Statics, dynamic impact, drop, typical motion reaction forces, fatigue load spectrum
- **Design Logic**: The most severe load case determines structural design; includes single-leg support, fall impact, maximum payload grasping
- **Key Constraints**: Load path, safety factor, test verification
- **Completion Criteria/Deliverables**: "Load Case Table": load magnitude, direction, application point, occurrence probability
**Level-3 Sub-tasks:**
- **P8.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Load Case Definition," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P8.1.1.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Load Case Definition," using "Statics, dynamic impact, drop, typical motion reaction forces, fatigue load spectrum" for demonstration, and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P8.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Load Case Definition" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P8.1.1.4 Verification and Issue Closure**: Verify the output of "Load Case Definition," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P8.1.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Load Case Definition," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### FEA Model Preparation
- **Methods/Tools**: HyperMesh / ANSA / Abaqus / ANSYS, mesh convergence analysis
- **Design Logic**: Simplify non-load-bearing features, reasonable mesh division, material properties, contact/tie settings
- **Key Constraints**: Mesh quality, computation time, resources
- **Completion Criteria/Deliverables**: High-quality FEA model, mesh quality report, boundary condition list
**Level-3 Sub-tasks:**
- **P8.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "FEA Model Preparation," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P8.1.2.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "FEA Model Preparation," using "HyperMesh / ANSA / Abaqus / ANSYS, mesh convergence analysis" for demonstration, and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P8.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "FEA Model Preparation" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P8.1.2.4 Verification and Issue Closure**: Verify the output of "FEA Model Preparation," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P8.1.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "FEA Model Preparation," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Nonlinear Analysis and Stability
- **Methods/Tools**: Contact nonlinearity, geometric nonlinearity, buckling analysis
- **Design Logic**: Thin-walled structures may buckle under impact; large deformation requires consideration of geometric nonlinearity
- **Key Constraints**: Convergence difficulty, computational cost
- **Completion Criteria/Deliverables**: Buckling modes, stress/strain under large deformation
**Level-3 Sub-tasks:**
- **P8.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Nonlinear Analysis and Stability," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P8.1.3.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Nonlinear Analysis and Stability," using "Contact nonlinearity, geometric nonlinearity, buckling analysis" for demonstration, and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P8.1.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Nonlinear Analysis and Stability" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P8.1.3.4 Verification and Issue Closure**: Verify the output of "Nonlinear Analysis and Stability," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P8.1.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Nonlinear Analysis and Stability," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### Strength, Fatigue, and Optimization

##### Static and Dynamic Stress and Deformation Analysis
- **Methods/Tools**: Linear elastic/elastoplastic analysis, von Mises, deformation contour
- **Design Logic**: Verify whether stress in critical components is below material yield/fatigue limit, and whether deformation affects motion
- **Key Constraints**: Local stress concentration, weld/bolt simulation
- **Completion Criteria/Deliverables**: "FEA Stress Report": stress, deformation, safety factor
**Level-3 Sub-tasks:**
- **P8.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Static and Dynamic Stress and Deformation Analysis," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P8.2.1.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Static and Dynamic Stress and Deformation Analysis," using "Linear elastic/elastoplastic analysis, von Mises, deformation contour" for demonstration, and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P8.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Static and Dynamic Stress and Deformation Analysis" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P8.2.1.4 Verification and Issue Closure**: Verify the output of "Static and Dynamic Stress and Deformation Analysis," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P8.2.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Static and Dynamic Stress and Deformation Analysis," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Fatigue and Life Prediction
- **Methods/Tools**: S-N curve, Miner cumulative damage, rainflow counting
- **Design Logic**: Evaluate life for high-cycle fatigue locations (joint lugs, link hole edges)
- **Key Constraints**: Load spectrum uncertainty, material fatigue data
- **Completion Criteria/Deliverables**: Fatigue analysis report, critical component cycle life > target
**Level-3 Sub-tasks:**
- **P8.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Fatigue and Life Prediction," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P8.2.2.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Fatigue and Life Prediction," using "S-N curve, Miner cumulative damage, rainflow counting" for demonstration, and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P8.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Fatigue and Life Prediction" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P8.2.2.4 Verification and Issue Closure**: Verify the output of "Fatigue and Life Prediction," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P8.2.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Fatigue and Life Prediction," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Lightweighting and Topology Optimization
- **Methods/Tools**: Topology optimization, size optimization, rib/ribbed plate arrangement, composite material substitution
- **Design Logic**: Reduce weight while maintaining sufficient stress margin, lowering overall inertia and energy consumption
- **Key Constraints**: Manufacturing process limitations, cost
- **Completion Criteria/Deliverables**: Optimized CAD, weight reduction ratio > target, strength still satisfied
**Level-3 Sub-tasks:**
- **P8.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Lightweighting and Topology Optimization," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P8.2.3.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Lightweighting and Topology Optimization," using "Topology optimization, size optimization, rib/ribbed plate arrangement, composite material substitution" for demonstration, and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P8.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Lightweighting and Topology Optimization" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P8.2.3.4 Verification and Issue Closure**: Verify the output of "Lightweighting and Topology Optimization," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P8.2.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Lightweighting and Topology Optimization," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Simulation-Test Closed-Loop Iteration
- **Methods/Tools**: Prototype loading test, strain gauges, displacement sensors, comparison with FEA
- **Design Logic**: Correct simulation boundary conditions and material parameters through testing, forming a closed loop
- **Key Constraints**: Test fixtures, loading accuracy
- **Completion Criteria/Deliverables**: Simulation vs. test error < 15%, design iteration records
**Level-3 Sub-tasks:**
- **P8.2.4.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Simulation-Test Closed-Loop Iteration," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P8.2.4.2 Interface and Integration Strategy Design**: Review subsystem interfaces, data flow, and timing involved in "Simulation-Test Closed-Loop Iteration," define integration sequence, rollback strategy, and exception handling mechanism.
**Level-4 Key Actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P8.2.4.3 Modeling/Simulation and Prototype Implementation**: Build simulation/mathematical models or prototypes for "Simulation-Test Closed-Loop Iteration," using "Prototype loading test, strain gauges, displacement sensors, comparison with FEA" to perform calculations or experiments, and record key parameters and boundary conditions.
**Level-4 Key Actions:**
1. Build model/prototype and record key parameters
2. Execute simulation or prototype verification
3. Record anomalies and deviations
- **P8.2.4.4 Test Execution and Result Analysis**: Execute tests for "Simulation-Test Closed-Loop Iteration" according to acceptance criteria, calculate pass rate/error/deviation, perform root cause analysis, and form improvement list.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P8.2.4.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Simulation-Test Closed-Loop Iteration," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

## Completion Criteria
All Level-3 sub-tasks in this stage have passed acceptance review, and key deliverables are version-controlled and formally delivered to downstream dependents.

## 개요
구조 강도 시뮬레이션 및 반복(Structural FEA)은 휴머노이드 로봇 제품 개발 전 과정 중 8번째 단계이며, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.
## 핵심 내용
이 단계는 입력 검토, 설계, 구현/프로토타입, 검증 폐쇄 및 문서 인도 등 완전한 엔지니어링 작업을 포함하며, 하위 의존 부서가 적격한 입력을 확보하는 중요한 지점입니다.

## 주요 하위 작업 및 기술 내용
#### 하중 및 시뮬레이션 모델

##### 하중 조건 정의
- **방법 / 도구**: 정역학, 동적 충격, 낙하, 대표 운동 반력, 피로 하중 스펙트럼
- **설계 사고 논리**: 가장 엄격한 조건이 구조 설계를 결정함; 한쪽 다리 지지, 넘어짐 충격, 최대 하중 파지를 포함
- **주요 제약**: 하중 전달 경로, 안전 계수, 테스트 검증
- **완료 기준 / 산출물**: 《하중 조건표》: 하중 크기, 방향, 작용점, 발생 확률
**3레벨 하위 작업:**
- **P8.1.1.1 입력 검토 및 목표 정량화**: 「하중 조건 정의」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 설정
- **P8.1.1.2 설계/방법 설계**: 「하중 조건 정의」에 대한 구현 방법 또는 후보 설계를 수립하고, 「정역학, 동적 충격, 낙하, 대표 운동 반력, 피로 하중 스펙트럼」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
**4레벨 주요 작업:**
1. 최소 2개의 후보 설계를 도출
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P8.1.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「하중 조건 정의」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P8.1.1.4 검증 및 문제 폐쇄**: 「하중 조건 정의」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료될 때까지 추적.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P8.1.1.5 문서 출력 및 하위 인도**: 「하중 조건 정의」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 참조
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### FEA 모델 준비
- **방법 / 도구**: HyperMesh / ANSA / Abaqus / ANSYS, 메쉬 수렴 분석
- **설계 사고 논리**: 비하중 지지 특징 단순화, 적절한 메쉬 분할, 재료 속성, 접촉/구속 설정
- **주요 제약**: 메쉬 품질, 계산 시간, 자원
- **완료 기준 / 산출물**: 고품질 FEA 모델, 메쉬 품질 보고서, 경계 조건 목록
**3레벨 하위 작업:**
- **P8.1.2.1 입력 검토 및 목표 정량화**: 「FEA 모델 준비」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 설정
- **P8.1.2.2 설계/방법 설계**: 「FEA 모델 준비」에 대한 구현 방법 또는 후보 설계를 수립하고, 「HyperMesh / ANSA / Abaqus / ANSYS, 메쉬 수렴 분석」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
**4레벨 주요 작업:**
1. 최소 2개의 후보 설계를 도출
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P8.1.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「FEA 모델 준비」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P8.1.2.4 검증 및 문제 폐쇄**: 「FEA 모델 준비」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료될 때까지 추적.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P8.1.2.5 문서 출력 및 하위 인도**: 「FEA 모델 준비」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 참조
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 비선형 해석 및 안정성
- **방법 / 도구**: 접촉 비선형, 기하 비선형, 좌굴 해석
- **설계 사고 논리**: 얇은 벽 구조는 충격 시 좌굴이 발생할 수 있음; 큰 변형은 기하 비선형을 고려해야 함
- **주요 제약**: 수렴 난이도, 계산 비용
- **완료 기준 / 산출물**: 좌굴 모드, 큰 변형 하의 응력/변형률
**3레벨 하위 작업:**
- **P8.1.3.1 입력 검토 및 목표 정량화**: 「비선형 해석 및 안정성」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 설정
- **P8.1.3.2 설계/방법 설계**: 「비선형 해석 및 안정성」에 대한 구현 방법 또는 후보 설계를 수립하고, 「접촉 비선형, 기하 비선형, 좌굴 해석」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
**4레벨 주요 작업:**
1. 최소 2개의 후보 설계를 도출
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P8.1.3.3 구현/프로토타입/시제품 제작**: 설계에 따라 「비선형 해석 및 안정성」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P8.1.3.4 검증 및 문제 폐쇄**: 「비선형 해석 및 안정성」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료될 때까지 추적.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P8.1.3.5 문서 출력 및 하위 인도**: 「비선형 해석 및 안정성」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 참조
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 강도, 피로 및 최적화

##### 정적 및 동적 응력과 변형 해석
- **방법 / 도구**: 선형 탄성/탄소성 해석, von Mises, 변형 분포도
- **설계 사고 논리**: 주요 부품의 응력이 재료 항복/피로 한계 미만인지, 변형이 운동에 영향을 미치는지 검증
- **주요 제약**: 국부 응력 집중, 용접/볼트 연결 시뮬레이션
- **완료 기준 / 산출물**: 《FEA 응력 보고서》: 응력, 변형, 안전 계수
**3레벨 하위 작업:**
- **P8.2.1.1 입력 검토 및 목표 정량화**: 「정적 및 동적 응력과 변형 해석」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 설정
- **P8.2.1.2 설계/방법 설계**: 「정적 및 동적 응력과 변형 해석」에 대한 구현 방법 또는 후보 설계를 수립하고, 「선형 탄성/탄소성 해석, von Mises, 변형 분포도」를 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
**4레벨 주요 작업:**
1. 최소 2개의 후보 설계를 도출
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P8.2.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「정적 및 동적 응력과 변형 해석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P8.2.1.4 검증 및 문제 폐쇄**: 「정적 및 동적 응력과 변형 해석」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료될 때까지 추적.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P8.2.1.5 문서 출력 및 하위 인도**: 「정적 및 동적 응력과 변형 해석」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 참조
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 피로 및 수명 예측
- **방법 / 도구**: S-N 곡선, Miner 누적 손상, 레인플로우 카운팅
- **설계 사고 논리**: 고주기 피로 부위(관절 러그, 커넥팅 로드 구멍 가장자리)에 대한 수명 평가 수행
- **주요 제약**: 하중 스펙트럼 불확실성, 재료 피로 데이터
- **완료 기준 / 산출물**: 피로 분석 보고서, 주요 부품의 반복 수명 > 목표
**3레벨 하위 작업:**
- **P8.2.2.1 입력 검토 및 목표 정량화**: 「피로 및 수명 예측」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 설정
- **P8.2.2.2 설계/방법 설계**: 「피로 및 수명 예측」에 대한 구현 방법 또는 후보 설계를 수립하고, 「S-N 곡선, Miner 누적 손상, 레인플로우 카운팅」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
**4레벨 주요 작업:**
1. 최소 2개의 후보 설계를 도출
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P8.2.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「피로 및 수명 예측」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P8.2.2.4 검증 및 문제 폐쇄**: 「피로 및 수명 예측」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료될 때까지 추적.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P8.2.2.5 문서 출력 및 하위 인도**: 「피로 및 수명 예측」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 참조
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 경량화 및 위상 최적화
- **방법 / 도구**: 위상 최적화, 치수 최적화, 리브/보강재 배치, 복합재 대체
- **설계 사고 논리**: 응력 여유가 충분한 조건에서 중량을 줄여, 전체 기계의 관성과 에너지 소비를 낮춤
- **주요 제약**: 제조 공정 제한, 비용
- **완료 기준 / 산출물**: 최적화된 CAD, 중량 감소 비율 > 목표, 강도 여전히 충족
**3레벨 하위 작업:**
- **P8.2.3.1 입력 검토 및 목표 정량화**: 「경량화 및 위상 최적화」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 설정
- **P8.2.3.2 설계/방법 설계**: 「경량화 및 위상 최적화」에 대한 구현 방법 또는 후보 설계를 수립하고, 「위상 최적화, 치수 최적화, 리브/보강재 배치, 복합재 대체」를 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
**4레벨 주요 작업:**
1. 최소 2개의 후보 설계를 도출
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P8.2.3.3 구현/프로토타입/시제품 제작**: 설계에 따라 「경량화 및 위상 최적화」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P8.2.3.4 검증 및 문제 폐쇄**: 「경량화 및 위상 최적화」의 출력을 검증하여 완료 기준을 충족하는지 확인하고, 문제를 기록하여 종료될 때까지 추적.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P8.2.3.5 문서 출력 및 하위 인도**: 「경량화 및 위상 최적화」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 참조
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 시뮬레이션-실험 폐쇄 반복
- **방법 / 도구**: 프로토타입 하중 시험, 스트레인 게이지, 변위 센서, FEA와 비교
- **설계 사고 논리**: 실험을 통해 시뮬레이션 경계 조건과 재료 매개변수를 수정하여 폐쇄 루프 형성
- **주요 제약**: 시험 지그, 하중 정밀도
- **완료 기준 / 산출물**: 시뮬레이션과 실험 오차 < 15%, 설계 반복 기록
**3레벨 하위 작업:**
- **P8.2.4.1 입력 검토 및 목표 정량화**: 「시뮬레이션-실험 폐쇄 반복」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 설정
- **P8.2.4.2 인터페이스 및 통합 전략 설계**: 「시뮬레이션-실험 폐쇄 반복」과 관련된 하위 시스템 인터페이스, 데이터 흐름 및 시퀀스를 정리하고, 통합 순서, 롤백 전략 및 이상 처리 메커니즘을 수립.
**4레벨 주요 작업:**
1. 최소 2개의 후보 설계를 도출
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P8.2.4.3 모델링/시뮬레이션 및 시제품 구현**: 「시뮬레이션-실험 폐쇄 반복」의 시뮬레이션/수학적 모델 또는 프로토타입 시제품을 구축하고, 「프로토타입 하중 시험, 스트레인 게이지, 변위 센서, FEA와 비교」를 사용하여 계산 또는 실험을 수행하며, 주요 매개변수와 경계 조건을 기록.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P8.2.4.4 테스트 수행 및 결과 분석**: 검수 기준에 따라 「시뮬레이션-실험 폐쇄 반복」 테스트를 수행하고, 통과율/오차/편차를 통계하며, 근본 원인 분석을 수행하고 개선 목록을 작성.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P8.2.4.5 문서 출력 및 하위 인도**: 「시뮬레이션-실험 폐쇄 반복」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 참조
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

## 완료 기준
본 단계의 모든 3레벨 하위 작업이 검수 심사를 통과하고, 주요 산출물의 버전이 관리되며 공식적으로 하위 의존 부서에 인도됩니다.
