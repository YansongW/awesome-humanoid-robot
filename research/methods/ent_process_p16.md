---
$id: ent_process_p16
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Pilot & Production Ramp
  zh: 小批量试产与量产准备（Pilot & Production Ramp）
  ko: 小批量试产与量产准备（Pilot & Production Ramp）
summary:
  en: Pilot & Production Ramp-stage 16 of the Android product development process, covering concept design, implementation
    verification, and document delivery.
  zh: 小批量试产与量产准备（Pilot & Production Ramp）是人形机器人产品开发全流程中的第 16 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 小批量试产与量产准备（Pilot & Production Ramp）
domains:
- 05_mass_production
- 11_applications_markets
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
小批量试产与量产准备（Pilot & Production Ramp）是人形机器人产品开发全流程中的第 16 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 可制造性设计

##### DFM/DFA 评审
- **方法 / 工具**：设计可制造性/可装配性分析、装配工时估算
- **设计思考逻辑**：将 3D 打印/CNC 原型转化为压铸、注塑、钣金等量产工艺
- **关键约束**：模具成本、良率、节拍
- **完成标准 / 输出物**：DFM/DFA 报告、工程变更清单、成本影响评估
**三级子任务：**
- **P16.1.1.1 输入梳理与目标量化**：整理「DFM/DFA 评审」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.1.1.2 方案/方法设计**：针对「DFM/DFA 评审」制定实施方法或候选方案，使用「设计可制造性/可装配性分析、装配工时估算」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.1.1.3 实施/原型/样件制作**：根据设计方案执行「DFM/DFA 评审」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.1.1.4 测试执行与结果分析**：按照验收标准执行「DFM/DFA 评审」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.1.1.5 文档输出与下游交付**：输出「DFM/DFA 评审」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 模具与工装设计
- **方法 / 工具**：压铸模、注塑模、冲压模、夹具、治具、检具
- **设计思考逻辑**：保证批量一致性与装配精度
- **关键约束**：模具周期、成本、修改难度
- **完成标准 / 输出物**：模具/工装图纸、FAI 计划、验收标准
**三级子任务：**
- **P16.1.2.1 输入梳理与目标量化**：整理「模具与工装设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.1.2.2 概念与详细设计**：完成「模具与工装设计」的概念设计、详细设计与接口定义，使用「压铸模、注塑模、冲压模、夹具、治具、检具」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.1.2.3 实施/原型/样件制作**：根据设计方案执行「模具与工装设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.1.2.4 验证与问题闭环**：对「模具与工装设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.1.2.5 文档输出与下游交付**：输出「模具与工装设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 装配线规划与 SOP
- **方法 / 工具**：工位设计、工装夹具、标准作业、节拍平衡
- **设计思考逻辑**：从单台手工装配过渡到小批量流水线
- **关键约束**：节拍、人员培训、场地
- **完成标准 / 输出物**：装配流程图、工装清单、SOP、节拍测算
**三级子任务：**
- **P16.1.3.1 输入梳理与目标量化**：整理「装配线规划与 SOP」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.1.3.2 算法/控制方案设计**：基于「工位设计、工装夹具、标准作业、节拍平衡」建立数学模型或算法框架，形成候选方案，评估稳定性、实时性与可扩展性，并冻结实现路径。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.1.3.3 算法实现与仿真验证**：将「装配线规划与 SOP」的算法在仿真环境或离线数据中实现，验证功能正确性、实时性与鲁棒性。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.1.3.4 算法调参与性能验证**：对「装配线规划与 SOP」算法进行参数调优与边界测试，验证在典型/极端工况下的性能是否满足指标。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.1.3.5 文档输出与下游交付**：输出「装配线规划与 SOP」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 供应链与质量管理

##### 供应商选择与审核
- **方法 / 工具**：供应商审核、样品承认、IQC、第二供应商开发
- **设计思考逻辑**：关键部件（电机、减速器、电池、计算板）需多家备份
- **关键约束**：交付周期、质量一致性、价格
- **完成标准 / 输出物**：供应商清单、样品测试报告、合格供方名录
**三级子任务：**
- **P16.2.1.1 输入梳理与目标量化**：整理「供应商选择与审核」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.2.1.2 候选方案建立与评估**：针对「供应商选择与审核」建立候选方案库，使用「供应商审核、样品承认、IQC、第二供应商开发」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.2.1.3 实施/原型/样件制作**：根据设计方案执行「供应商选择与审核」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.2.1.4 验证与问题闭环**：对「供应商选择与审核」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.2.1.5 文档输出与下游交付**：输出「供应商选择与审核」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 质量控制体系建立
- **方法 / 工具**：SPC、FAI、来料检验、过程检验、出货检验、MSA
- **设计思考逻辑**：建立关键尺寸与性能监控，防止批量不良
- **关键约束**：AQL 标准、检测能力、人员培训
- **完成标准 / 输出物**：质量计划、检验规范、SPC 控制图
**三级子任务：**
- **P16.2.2.1 输入梳理与目标量化**：整理「质量控制体系建立」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.2.2.2 算法/控制方案设计**：基于「SPC、FAI、来料检验、过程检验、出货检验、MSA」建立数学模型或算法框架，形成候选方案，评估稳定性、实时性与可扩展性，并冻结实现路径。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.2.2.3 算法实现与仿真验证**：将「质量控制体系建立」的算法在仿真环境或离线数据中实现，验证功能正确性、实时性与鲁棒性。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.2.2.4 算法调参与性能验证**：对「质量控制体系建立」算法进行参数调优与边界测试，验证在典型/极端工况下的性能是否满足指标。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.2.2.5 文档输出与下游交付**：输出「质量控制体系建立」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 来料与过程异常处理
- **方法 / 工具**：8D、CAPA、供应商质量改进
- **设计思考逻辑**：快速闭环质量问题，避免流入下游
- **关键约束**：响应时间、根因分析能力
- **完成标准 / 输出物**：8D 报告、改善验证、不良率下降
**三级子任务：**
- **P16.2.3.1 输入梳理与目标量化**：整理「来料与过程异常处理」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.2.3.2 方案/方法设计**：针对「来料与过程异常处理」制定实施方法或候选方案，使用「8D、CAPA、供应商质量改进」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.2.3.3 实施/原型/样件制作**：根据设计方案执行「来料与过程异常处理」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.2.3.4 验证与问题闭环**：对「来料与过程异常处理」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.2.3.5 文档输出与下游交付**：输出「来料与过程异常处理」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 试产与量产爬坡

##### 小批量试产（Pilot Run）
- **方法 / 工具**：10–50 台试产、问题追踪、ECN、首件检验
- **设计思考逻辑**：验证供应链、装配、测试、软件全链路
- **关键约束**：时间、资源、样机成本
- **完成标准 / 输出物**：试产总结报告、直通率、问题闭环率
**三级子任务：**
- **P16.3.1.1 输入梳理与目标量化**：整理「小批量试产（Pilot Run）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.3.1.2 方案/方法设计**：针对「小批量试产（Pilot Run）」制定实施方法或候选方案，使用「10–50 台试产、问题追踪、ECN、首件检验」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.3.1.3 实施/原型/样件制作**：根据设计方案执行「小批量试产（Pilot Run）」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.3.1.4 验证与问题闭环**：对「小批量试产（Pilot Run）」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.3.1.5 文档输出与下游交付**：输出「小批量试产（Pilot Run）」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 成本核算与降本
- **方法 / 工具**：实际 BOM、制造成本、良率影响、VA/VE
- **设计思考逻辑**：小批量数据修正早期成本模型，为量产定价提供依据
- **关键约束**：规模经济、供应商议价能力
- **完成标准 / 输出物**：小批量成本分析报告、降本项目清单
**三级子任务：**
- **P16.3.2.1 输入梳理与目标量化**：整理「成本核算与降本」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.3.2.2 方案/方法设计**：针对「成本核算与降本」制定实施方法或候选方案，使用「实际 BOM、制造成本、良率影响、VA/VE」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.3.2.3 实施/原型/样件制作**：根据设计方案执行「成本核算与降本」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.3.2.4 验证与问题闭环**：对「成本核算与降本」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.3.2.5 文档输出与下游交付**：输出「成本核算与降本」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### PPAP / 量产 readiness 评估
- **方法 / 工具**：PPAP 文件包、产能爬坡计划、质量/交付/成本 readiness 检查
- **设计思考逻辑**：确认具备批量交付能力
- **关键约束**：客户/法规要求
- **完成标准 / 输出物**：PPAP 批准、量产 readiness 评估通过
**三级子任务：**
- **P16.3.3.1 输入梳理与目标量化**：整理「PPAP / 量产 readiness 评估」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.3.3.2 方案/方法设计**：针对「PPAP / 量产 readiness 评估」制定实施方法或候选方案，使用「PPAP 文件包、产能爬坡计划、质量/交付/成本 readiness 检查」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.3.3.3 实施/原型/样件制作**：根据设计方案执行「PPAP / 量产 readiness 评估」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P16.3.3.4 验证与问题闭环**：对「PPAP / 量产 readiness 评估」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.3.3.5 文档输出与下游交付**：输出「PPAP / 量产 readiness 评估」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 服务手册与培训
- **方法 / 工具**：维修手册、备件清单、客户培训、现场支持流程
- **设计思考逻辑**：量产不仅是卖出产品，还要建立服务能力
- **关键约束**：文档完整性、培训体系
- **完成标准 / 输出物**：服务手册、备件策略、培训计划
**三级子任务：**
- **P16.3.4.1 输入梳理与目标量化**：整理「服务手册与培训」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P16.3.4.2 方案/方法设计**：针对「服务手册与培训」制定实施方法或候选方案，使用「维修手册、备件清单、客户培训、现场支持流程」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P16.3.4.3 内容编写与内部评审**：按模板完成「服务手册与培训」主体内容编写，引用原始数据与结论，组织评审并修订。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.3.4.4 验证与问题闭环**：对「服务手册与培训」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P16.3.4.5 文档输出与下游交付**：输出「服务手册与培训」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 包装/运输/贮存与现场部署

##### 包装/运输/贮存设计
- **方法 / 工具**：运输冲击仿真、包装箱设计、固定夹具、贮存环境要求
- **设计思考逻辑**：保证机器人在运输和长期贮存过程中不受损伤
- **关键约束**：尺寸、重量、成本、可重复使用
- **完成标准 / 输出物**：运输试验通过、包装规范、贮存手册
**三级子任务：**
- **P16.4.1.1 输入梳理与目标量化**：整理「包装/运输/贮存设计」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P16.4.1.2 方案/方法设计**：针对「包装/运输/贮存设计」制定实施方法或候选方案，使用「运输冲击仿真、包装箱设计、固定夹具、贮存环境要求」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P16.4.1.3 实施/建模/实验**：根据方案执行「包装/运输/贮存设计」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P16.4.1.4 验证与优化**：对「包装/运输/贮存设计」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P16.4.1.5 文档输出与下游交付**：输出「包装/运输/贮存设计」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 现场部署与运维
- **方法 / 工具**：安装调试、客户培训、远程运维、备件物流、现场服务手册
- **设计思考逻辑**：产品交付不仅是硬件，还包括持续服务能力
- **关键约束**：人员培训、服务网络、备件库存
- **完成标准 / 输出物**：部署SOP、培训材料、服务手册、SLA
**三级子任务：**
- **P16.4.2.1 输入梳理与目标量化**：整理「现场部署与运维」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P16.4.2.2 方案/方法设计**：针对「现场部署与运维」制定实施方法或候选方案，使用「安装调试、客户培训、远程运维、备件物流、现场服务手册」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P16.4.2.3 实施/建模/实验**：根据方案执行「现场部署与运维」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P16.4.2.4 验证与优化**：对「现场部署与运维」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P16.4.2.5 文档输出与下游交付**：输出「现场部署与运维」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

#### 可持续性、法务与保险

##### 可持续性与 EOL 策略
- **方法 / 工具**：LCA、RoHS/REACH 合规、回收拆解设计、EOL 处理方案
- **设计思考逻辑**：满足环保法规并降低企业长期责任风险
- **关键约束**：材料选择、成本、供应链
- **完成标准 / 输出物**：LCA 报告、合规声明、拆解指南
**三级子任务：**
- **P16.5.1.1 输入梳理与目标量化**：整理「可持续性与 EOL 策略」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P16.5.1.2 方案/方法设计**：针对「可持续性与 EOL 策略」制定实施方法或候选方案，使用「LCA、RoHS/REACH 合规、回收拆解设计、EOL 处理方案」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P16.5.1.3 实施/建模/实验**：根据方案执行「可持续性与 EOL 策略」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P16.5.1.4 验证与优化**：对「可持续性与 EOL 策略」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P16.5.1.5 文档输出与下游交付**：输出「可持续性与 EOL 策略」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 法务与保险
- **方法 / 工具**：产品责任险、使用条款、免责声明、事故责任划分、合规审查
- **设计思考逻辑**：降低产品上市后法律与财务风险
- **关键约束**：地区法律差异、保险费率
- **完成标准 / 输出物**：保险合同、用户协议、责任矩阵
**三级子任务：**
- **P16.5.2.1 输入梳理与目标量化**：整理「法务与保险」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P16.5.2.2 方案/方法设计**：针对「法务与保险」制定实施方法或候选方案，使用「产品责任险、使用条款、免责声明、事故责任划分、合规审查」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P16.5.2.3 实施/建模/实验**：根据方案执行「法务与保险」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P16.5.2.4 验证与优化**：对「法务与保险」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P16.5.2.5 文档输出与下游交付**：输出「法务与保险」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

#### 经济性迭代

##### VA/VE 与面向成本设计（DFC）
- **方法 / 工具**：价值工程分析、成本拆解、DFC 评审、二供开发、目标成本达成
- **设计思考逻辑**：在量产前持续降本而不牺牲核心性能与安全
- **关键约束**：质量底线、供应商能力、时间
- **完成标准 / 输出物**：降本项目清单、成本达成率、VA/VE 报告
**三级子任务：**
- **P16.6.1.1 输入梳理与目标量化**：整理「VA/VE 与面向成本设计（DFC）」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P16.6.1.2 方案/方法设计**：针对「VA/VE 与面向成本设计（DFC）」制定实施方法或候选方案，使用「价值工程分析、成本拆解、DFC 评审、二供开发、目标成本达成」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P16.6.1.3 实施/建模/实验**：根据方案执行「VA/VE 与面向成本设计（DFC）」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P16.6.1.4 验证与优化**：对「VA/VE 与面向成本设计（DFC）」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P16.6.1.5 文档输出与下游交付**：输出「VA/VE 与面向成本设计（DFC）」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
Pilot & Production Ramp is the 16th stage in the full-process development of humanoid robot products, expanded into several Level-3 sub-tasks in WBS V3.
## Content
This stage covers complete engineering actions such as input review, solution design, implementation/prototyping, verification closure, and documentation delivery. It is a key node to ensure downstream dependents receive qualified inputs.

## Key Sub-tasks and Technical Content
#### Design for Manufacturing

##### DFM/DFA Review
- **Methods / Tools**: Design for Manufacturing/Assembly analysis, assembly time estimation
- **Design Thinking Logic**: Convert 3D printing/CNC prototypes into mass production processes such as die casting, injection molding, and sheet metal
- **Key Constraints**: Mold cost, yield rate, cycle time
- **Completion Criteria / Deliverables**: DFM/DFA report, engineering change list, cost impact assessment
**Level-3 Sub-tasks:**
- **P16.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "DFM/DFA Review," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, time nodes, and risk register
- **P16.1.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "DFM/DFA Review," use "Design for Manufacturing/Assembly analysis, assembly time estimation" for validation, and clarify the technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and perform quantitative scoring
3. Organize a review and freeze the solution
- **P16.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "DFM/DFA Review" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P16.1.1.4 Test Execution and Result Analysis**: Execute "DFM/DFA Review" tests according to acceptance criteria, calculate pass rate/error/deviation, conduct root cause analysis, and form an improvement list.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P16.1.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "DFM/DFA Review," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents according to templates and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Mold and Tooling Design
- **Methods / Tools**: Die casting mold, injection mold, stamping die, fixture, jig, gauge
- **Design Thinking Logic**: Ensure batch consistency and assembly precision
- **Key Constraints**: Mold lead time, cost, modification difficulty
- **Completion Criteria / Deliverables**: Mold/tooling drawings, FAI plan, acceptance criteria
**Level-3 Sub-tasks:**
- **P16.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Mold and Tooling Design," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, time nodes, and risk register
- **P16.1.2.2 Concept and Detailed Design**: Complete concept design, detailed design, and interface definition for "Mold and Tooling Design," use "Die casting mold, injection mold, stamping die, fixture, jig, gauge" to verify feasibility, and output drawings/algorithms/logical frameworks.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and perform quantitative scoring
3. Organize a review and freeze the solution
- **P16.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Mold and Tooling Design" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P16.1.2.4 Verification and Issue Closure**: Verify the output of "Mold and Tooling Design," check if it meets completion criteria, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P16.1.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Mold and Tooling Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents according to templates and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Assembly Line Planning and SOP
- **Methods / Tools**: Station design, tooling fixtures, standard work, cycle time balancing
- **Design Thinking Logic**: Transition from single-unit manual assembly to small-batch production line
- **Key Constraints**: Cycle time, personnel training, floor space
- **Completion Criteria / Deliverables**: Assembly flow chart, tooling list, SOP, cycle time calculation
**Level-3 Sub-tasks:**
- **P16.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Assembly Line Planning and SOP," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, time nodes, and risk register
- **P16.1.3.2 Algorithm/Control Solution Design**: Based on "Station design, tooling fixtures, standard work, cycle time balancing," establish a mathematical model or algorithm framework, form candidate solutions, evaluate stability, real-time performance, and scalability, and freeze the implementation path.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and perform quantitative scoring
3. Organize a review and freeze the solution
- **P16.1.3.3 Algorithm Implementation and Simulation Verification**: Implement the algorithm for "Assembly Line Planning and SOP" in a simulation environment or with offline data, verifying functional correctness, real-time performance, and robustness.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P16.1.3.4 Algorithm Tuning and Performance Verification**: Perform parameter tuning and boundary testing on the "Assembly Line Planning and SOP" algorithm, verifying whether performance under typical/extreme conditions meets indicators.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P16.1.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Assembly Line Planning and SOP," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents according to templates and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### Supply Chain and Quality Management

##### Supplier Selection and Audit
- **Methods / Tools**: Supplier audit, sample approval, IQC, second supplier development
- **Design Thinking Logic**: Key components (motors, reducers, batteries, computing boards) require multiple backups
- **Key Constraints**: Delivery lead time, quality consistency, price
- **Completion Criteria / Deliverables**: Supplier list, sample test report, approved supplier list
**Level-3 Sub-tasks:**
- **P16.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Supplier Selection and Audit," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, time nodes, and risk register
- **P16.2.1.2 Candidate Solution Establishment and Evaluation**: Establish a candidate solution library for "Supplier Selection and Audit," use "Supplier audit, sample approval, IQC, second supplier development" for quantitative evaluation, consider cost, performance, supply chain, and maintainability to determine the final solution.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and perform quantitative scoring
3. Organize a review and freeze the solution
- **P16.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Supplier Selection and Audit" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P16.2.1.4 Verification and Issue Closure**: Verify the output of "Supplier Selection and Audit," check if it meets completion criteria, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P16.2.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Supplier Selection and Audit," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents according to templates and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Quality Control System Establishment
- **Methods / Tools**: SPC, FAI, incoming inspection, in-process inspection, outgoing inspection, MSA
- **Design Thinking Logic**: Establish monitoring of key dimensions and performance to prevent batch defects
- **Key Constraints**: AQL standards, inspection capability, personnel training
- **Completion Criteria / Deliverables**: Quality plan, inspection specification, SPC control chart
**Level-3 Sub-tasks:**
- **P16.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Quality Control System Establishment," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, time nodes, and risk register
- **P16.2.2.2 Algorithm/Control Solution Design**: Based on "SPC, FAI, incoming inspection, in-process inspection, outgoing inspection, MSA," establish a mathematical model or algorithm framework, form candidate solutions, evaluate stability, real-time performance, and scalability, and freeze the implementation path.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and perform quantitative scoring
3. Organize a review and freeze the solution
- **P16.2.2.3 Algorithm Implementation and Simulation Verification**: Implement the algorithm for "Quality Control System Establishment" in a simulation environment or with offline data, verifying functional correctness, real-time performance, and robustness.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P16.2.2.4 Algorithm Tuning and Performance Verification**: Perform parameter tuning and boundary testing on the "Quality Control System Establishment" algorithm, verifying whether performance under typical/extreme conditions meets indicators.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P16.2.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Quality Control System Establishment," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents according to templates and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Incoming and Process Anomaly Handling
- **Methods / Tools**: 8D, CAPA, supplier quality improvement
- **Design Thinking Logic**: Quickly close quality issues to prevent them from flowing downstream
- **Key Constraints**: Response time, root cause analysis capability
- **Completion Criteria / Deliverables**: 8D report, improvement verification, defect rate reduction
**Level-3 Sub-tasks:**
- **P16.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Incoming and Process Anomaly Handling," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, time nodes, and risk register
- **P16.2.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Incoming and Process Anomaly Handling," use "8D, CAPA, supplier quality improvement" for validation, and clarify the technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and perform quantitative scoring
3. Organize a review and freeze the solution
- **P16.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Incoming and Process Anomaly Handling" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P16.2.3.4 Verification and Issue Closure**: Verify the output of "Incoming and Process Anomaly Handling," check if it meets completion criteria, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P16.2.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Incoming and Process Anomaly Handling," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents according to templates and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### Pilot Run and Production Ramp

##### Small-Batch Pilot Run
- **Methods / Tools**: 10–50 unit pilot run, issue tracking, ECN, first article inspection
- **Design Thinking Logic**: Verify the entire chain of supply chain, assembly, testing, and software
- **Key Constraints**: Time, resources, prototype cost
- **Completion Criteria / Deliverables**: Pilot run summary report, first pass yield, issue closure rate
**Level-3 Sub-tasks:**
- **P16.3.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Small-Batch Pilot Run," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, time nodes, and risk register
- **P16.3.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Small-Batch Pilot Run," use "10–50 unit pilot run, issue tracking, ECN, first article inspection" for validation, and clarify the technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and perform quantitative scoring
3. Organize a review and freeze the solution
- **P16.3.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Small-Batch Pilot Run" according to the design solution, create prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P16.3.1.4 Verification and Issue Closure**: Verify the output of "Small-Batch Pilot Run," check if it meets completion criteria, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P16.3.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Small-Batch Pilot Run," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents according to templates and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

## 개요
소량 시제품 생산 및 양산 준비(Pilot & Production Ramp)는 휴머노이드 로봇 제품 개발 전 과정 중 16번째 단계로, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.
## 핵심 내용
이 단계는 입력 정리,方案 설계, 구현/프로토타입, 검증 폐쇄 및 문서 인도 등 완전한 엔지니어링 작업을 포함하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 노드입니다.

## 주요 하위 작업 및 기술 내용
#### 제조 가능성 설계

##### DFM/DFA 검토
- **방법 / 도구**: 설계 제조 가능성/조립 가능성 분석, 조립 공수 추정
- **설계 사고 논리**: 3D 프린팅/CNC 프로토타입을 다이캐스팅, 사출 성형, 판금 등 양산 공정으로 전환
- **핵심 제약 조건**: 금형 비용, 수율, 택트 타임
- **완료 기준 / 산출물**: DFM/DFA 보고서, 엔지니어링 변경 목록, 비용 영향 평가
**3레벨 하위 작업:**
- **P16.1.1.1 입력 정리 및 목표 정량화**: 「DFM/DFA 검토」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P16.1.1.2方案/방법 설계**: 「DFM/DFA 검토」에 대한 구현 방법 또는 후보方案을 수립하고, 「설계 제조 가능성/조립 가능성 분석, 조립 공수 추정」을 사용하여论证하며, 기술 경로와 자원 요구 사항을 명확히 합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보方案 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및方案 확정
- **P16.1.1.3 구현/프로토타입/시제품 제작**: 설계方案에 따라 「DFM/DFA 검토」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 실행
3. 이상 및 편차 기록
- **P16.1.1.4 테스트 실행 및 결과 분석**: 검수 기준에 따라 「DFM/DFA 검토」 테스트를 실행하고, 통과율/오차/편차를 통계하며, 근본 원인 분석을 수행하고 개선 목록을 작성합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 실행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P16.1.1.5 문서 출력 및 하위 인도**: 「DFM/DFA 검토」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 금형 및 지그 설계
- **방법 / 도구**: 다이캐스팅 금형, 사출 금형, 프레스 금형, 지그,治具, 검사 지그
- **설계 사고 논리**: 배치 일관성 및 조립 정밀도 보장
- **핵심 제약 조건**: 금형周期, 비용, 수정 난이도
- **완료 기준 / 산출물**: 금형/지그 도면, FAI 계획, 검수 기준
**3레벨 하위 작업:**
- **P16.1.2.1 입력 정리 및 목표 정량화**: 「금형 및 지그 설계」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P16.1.2.2 개념 및 상세 설계**: 「금형 및 지그 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「다이캐스팅 금형, 사출 금형, 프레스 금형, 지그,治具, 검사 지그」를 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보方案 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및方案 확정
- **P16.1.2.3 구현/프로토타입/시제품 제작**: 설계方案에 따라 「금형 및 지그 설계」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 실행
3. 이상 및 편차 기록
- **P16.1.2.4 검증 및 문제 폐쇄**: 「금형 및 지그 설계」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 실행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P16.1.2.5 문서 출력 및 하위 인도**: 「금형 및 지그 설계」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 조립 라인 계획 및 SOP
- **방법 / 도구**: 공정 설계, 지그治具, 표준 작업, 택트 타임 밸런싱
- **설계 사고 논리**: 단일 수동 조립에서 소량 라인 생산으로 전환
- **핵심 제약 조건**: 택트 타임, 인력 교육, 공간
- **완료 기준 / 산출물**: 조립 흐름도, 지그 목록, SOP, 택트 타임 산출
**3레벨 하위 작업:**
- **P16.1.3.1 입력 정리 및 목표 정량화**: 「조립 라인 계획 및 SOP」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P16.1.3.2 알고리즘/제어方案 설계**: 「공정 설계, 지그治具, 표준 작업, 택트 타임 밸런싱」을 기반으로 수학적 모델 또는 알고리즘 프레임워크를 구축하고, 후보方案을 도출하며, 안정성, 실시간성 및 확장성을 평가하고 구현 경로를 확정합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보方案 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및方案 확정
- **P16.1.3.3 알고리즘 구현 및 시뮬레이션 검증**: 「조립 라인 계획 및 SOP」의 알고리즘을 시뮬레이션 환경 또는 오프라인 데이터에서 구현하고, 기능 정확성, 실시간성 및 견고성을 검증합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 실행
3. 이상 및 편차 기록
- **P16.1.3.4 알고리즘 튜닝 및 성능 검증**: 「조립 라인 계획 및 SOP」 알고리즘의 파라미터 최적화 및 경계 테스트를 수행하고, 일반/극한 조건에서의 성능이 지표를 충족하는지 검증합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 실행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P16.1.3.5 문서 출력 및 하위 인도**: 「조립 라인 계획 및 SOP」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

#### 공급망 및 품질 관리

##### 공급업체 선정 및 심사
- **방법 / 도구**: 공급업체 심사, 샘플 승인, IQC, 2차 공급업체 개발
- **설계 사고 논리**: 핵심 부품(모터, 감속기, 배터리, 컴퓨팅 보드)은 다중 공급처 확보 필요
- **핵심 제약 조건**: 납기, 품질 일관성, 가격
- **완료 기준 / 산출물**: 공급업체 목록, 샘플 테스트 보고서, 적격 공급업체 명단
**3레벨 하위 작업:**
- **P16.2.1.1 입력 정리 및 목표 정량화**: 「공급업체 선정 및 심사」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P16.2.1.2 후보方案 수립 및 평가**: 「공급업체 선정 및 심사」에 대한 후보方案 라이브러리를 구축하고, 「공급업체 심사, 샘플 승인, IQC, 2차 공급업체 개발」을 사용하여 정량적 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종方案을 결정합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보方案 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및方案 확정
- **P16.2.1.3 구현/프로토타입/시제품 제작**: 설계方案에 따라 「공급업체 선정 및 심사」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 실행
3. 이상 및 편차 기록
- **P16.2.1.4 검증 및 문제 폐쇄**: 「공급업체 선정 및 심사」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 실행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P16.2.1.5 문서 출력 및 하위 인도**: 「공급업체 선정 및 심사」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 품질 관리 체계 구축
- **방법 / 도구**: SPC, FAI, 입고 검사, 공정 검사, 출하 검사, MSA
- **설계 사고 논리**: 핵심 치수 및 성능 모니터링 구축, 배치 불량 방지
- **핵심 제약 조건**: AQL 기준, 검사 능력, 인력 교육
- **완료 기준 / 산출물**: 품질 계획, 검사 규격, SPC 관리도
**3레벨 하위 작업:**
- **P16.2.2.1 입력 정리 및 목표 정량화**: 「품질 관리 체계 구축」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P16.2.2.2 알고리즘/제어方案 설계**: 「SPC, FAI, 입고 검사, 공정 검사, 출하 검사, MSA」를 기반으로 수학적 모델 또는 알고리즘 프레임워크를 구축하고, 후보方案을 도출하며, 안정성, 실시간성 및 확장성을 평가하고 구현 경로를 확정합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보方案 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및方案 확정
- **P16.2.2.3 알고리즘 구현 및 시뮬레이션 검증**: 「품질 관리 체계 구축」의 알고리즘을 시뮬레이션 환경 또는 오프라인 데이터에서 구현하고, 기능 정확성, 실시간성 및 견고성을 검증합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 실행
3. 이상 및 편차 기록
- **P16.2.2.4 알고리즘 튜닝 및 성능 검증**: 「품질 관리 체계 구축」 알고리즘의 파라미터 최적화 및 경계 테스트를 수행하고, 일반/극한 조건에서의 성능이 지표를 충족하는지 검증합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 실행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P16.2.2.5 문서 출력 및 하위 인도**: 「품질 관리 체계 구축」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

##### 입고 및 공정 이상 처리
- **방법 / 도구**: 8D, CAPA, 공급업체 품질 개선
- **설계 사고 논리**: 품질 문제 신속 폐쇄, 하위 단계 유입 방지
- **핵심 제약 조건**: 대응 시간, 근본 원인 분석 능력
- **완료 기준 / 산출물**: 8D 보고서, 개선 검증, 불량률 감소
**3레벨 하위 작업:**
- **P16.2.3.1 입력 정리 및 목표 정량화**: 「입고 및 공정 이상 처리」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P16.2.3.2方案/방법 설계**: 「입고 및 공정 이상 처리」에 대한 구현 방법 또는 후보方案을 수립하고, 「8D, CAPA, 공급업체 품질 개선」을 사용하여论证하며, 기술 경로와 자원 요구 사항을 명확히 합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보方案 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및方案 확정
- **P16.2.3.3 구현/프로토타입/시제품 제작**: 설계方案에 따라 「입고 및 공정 이상 처리」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 실행
3. 이상 및 편차 기록
- **P16.2.3.4 검증 및 문제 폐쇄**: 「입고 및 공정 이상 처리」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 실행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P16.2.3.5 문서 출력 및 하위 인도**: 「입고 및 공정 이상 처리」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지

#### 시제품 생산 및 양산 램프업

##### 소량 시제품 생산(Pilot Run)
- **방법 / 도구**: 10–50대 시제품 생산, 문제 추적, ECN, 첫품 검사
- **설계 사고 논리**: 공급망, 조립, 테스트, 소프트웨어 전체 링크 검증
- **핵심 제약 조건**: 시간, 자원, 시제품 비용
- **완료 기준 / 산출물**: 시제품 생산 요약 보고서, 직통율, 문제 폐쇄율
**3레벨 하위 작업:**
- **P16.3.1.1 입력 정리 및 목표 정량화**: 「소량 시제품 생산(Pilot Run)」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전 확인
2. 검수 기준을 정량화 가능한 KPI로 전환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P16.3.1.2方案/방법 설계**: 「소량 시제품 생산(Pilot Run)」에 대한 구현 방법 또는 후보方案을 수립하고, 「10–50대 시제품 생산, 문제 추적, ECN, 첫품 검사」를 사용하여论证하며, 기술 경로와 자원 요구 사항을 명확히 합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보方案 도출
2. 평가 매트릭스 구축 및 정량적 점수 부여
3. 검토 조직 및方案 확정
- **P16.3.1.3 구현/프로토타입/시제품 제작**: 설계方案에 따라 「소량 시제품 생산(Pilot Run)」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 실행
3. 이상 및 편차 기록
- **P16.3.1.4 검증 및 문제 폐쇄**: 「소량 시제품 생산(Pilot Run)」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 실행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P16.3.1.5 문서 출력 및 하위 인도**: 「소량 시제품 생산(Pilot Run)」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서에 통지
