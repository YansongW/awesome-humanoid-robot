---
$id: ent_process_p5
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Ontological Structure Engineering and Prototyping (Mechanical Structure)
  zh: 本体结构工程与原型（Mechanical Structure）
  ko: 本体结构工程与原型（Mechanical Structure）
summary:
  en: Mechanical Structure (MED)——The fifth phase of the humanoid robot product development process, covering solution design,
    implementation verification, and documentation delivery.
  zh: 本体结构工程与原型（Mechanical Structure）是人形机器人产品开发全流程中的第 5 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 本体结构工程与原型（Mechanical Structure）
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
  notes: Body populated from docs/humanoid_full_development_workflow_v3.md by scripts/backfill_process_bodies.py. English
    name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.
sources:
- id: wbs_v3_report
  type: report
  title: 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）
  date: '2026-06-27'
theoretical_depth:
- system
---



## 概述
本体结构工程与原型（Mechanical Structure）是人形机器人产品开发全流程中的第 5 个阶段，在 WBS V3 中展开为若干三级子任务。

该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 详细结构设计

##### 中心骨架与四肢连杆设计
- **方法 / 工具**：SolidWorks / NX / CATIA、拓扑优化、尺寸优化
- **设计思考逻辑**：中心骨架承载躯干负载并传递至腿；四肢连杆需高刚度低重量
- **关键约束**：刚度、强度、重量、装配可达性
- **完成标准 / 输出物**：3D 结构模型、关键截面设计、BOM 初稿
**三级子任务：**
- **P5.1.1.1 输入梳理与目标量化**：整理「中心骨架与四肢连杆设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.1.1.2 概念与详细设计**：完成「中心骨架与四肢连杆设计」的概念设计、详细设计与接口定义，使用「SolidWorks / NX / CATIA、拓扑优化、尺寸优化」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.1.1.3 实施/原型/样件制作**：根据设计方案执行「中心骨架与四肢连杆设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.1.1.4 验证与问题闭环**：对「中心骨架与四肢连杆设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P5.1.1.5 文档输出与下游交付**：输出「中心骨架与四肢连杆设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 关节安装接口与壳体设计
- **方法 / 工具**：接口公差分析、定位销/法兰设计、密封设计
- **设计思考逻辑**：关节与结构之间需精确同轴、可重复拆装，并防尘防水
- **关键约束**：加工精度、密封等级、维护空间
- **完成标准 / 输出物**：关节接口图纸、壳体 3D、密封方案
**三级子任务：**
- **P5.1.2.1 输入梳理与目标量化**：整理「关节安装接口与壳体设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.1.2.2 概念与详细设计**：完成「关节安装接口与壳体设计」的概念设计、详细设计与接口定义，使用「接口公差分析、定位销/法兰设计、密封设计」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.1.2.3 实施/原型/样件制作**：根据设计方案执行「关节安装接口与壳体设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.1.2.4 验证与问题闭环**：对「关节安装接口与壳体设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P5.1.2.5 文档输出与下游交付**：输出「关节安装接口与壳体设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 外观覆盖件与分缝设计
- **方法 / 工具**：A 面分缝、卡扣/螺钉隐藏、可拆卸面板
- **设计思考逻辑**：覆盖件需兼顾外观、散热、维护开口、跌落保护
- **关键约束**：ID 冻结、模具/打印工艺、装配顺序
- **完成标准 / 输出物**：覆盖件 3D、分缝方案、维护开口布局
**三级子任务：**
- **P5.1.3.1 输入梳理与目标量化**：整理「外观覆盖件与分缝设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.1.3.2 概念与详细设计**：完成「外观覆盖件与分缝设计」的概念设计、详细设计与接口定义，使用「A 面分缝、卡扣/螺钉隐藏、可拆卸面板」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.1.3.3 实施/原型/样件制作**：根据设计方案执行「外观覆盖件与分缝设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.1.3.4 验证与问题闭环**：对「外观覆盖件与分缝设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P5.1.3.5 文档输出与下游交付**：输出「外观覆盖件与分缝设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 材料与工艺

##### 结构材料选型
- **方法 / 工具**：铝合金 7075/6061、碳纤维、钛合金、工程塑料对比
- **设计思考逻辑**：高载荷连杆用铝合金/CNC，外壳/支架用 SLS/MJF 3D 打印或注塑
- **关键约束**：强度、刚度、密度、成本、批量制造可行性
- **完成标准 / 输出物**：《材料选型表》：各部件材料、工艺、原因
**三级子任务：**
- **P5.2.1.1 输入梳理与目标量化**：整理「结构材料选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.2.1.2 候选方案建立与评估**：针对「结构材料选型」建立候选方案库，使用「铝合金 7075/6061、碳纤维、钛合金、工程塑料对比」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.2.1.3 实施/原型/样件制作**：根据设计方案执行「结构材料选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.2.1.4 验证与问题闭环**：对「结构材料选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P5.2.1.5 文档输出与下游交付**：输出「结构材料选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 面向增材制造的设计（DfAM）
- **方法 / 工具**：SLS/MJF/SLA 设计规范、支撑优化、晶格结构
- **设计思考逻辑**：原型阶段大量结构件采用 3D 打印，需针对打印工艺优化
- **关键约束**：打印材料强度、层间结合、尺寸精度、表面质量
- **完成标准 / 输出物**：DfAM 检查清单、3D 打印件图纸、打印参数
**三级子任务：**
- **P5.2.2.1 输入梳理与目标量化**：整理「面向增材制造的设计（DfAM）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.2.2.2 概念与详细设计**：完成「面向增材制造的设计（DfAM）」的概念设计、详细设计与接口定义，使用「SLS/MJF/SLA 设计规范、支撑优化、晶格结构」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.2.2.3 实施/原型/样件制作**：根据设计方案执行「面向增材制造的设计（DfAM）」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.2.2.4 验证与问题闭环**：对「面向增材制造的设计（DfAM）」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P5.2.2.5 文档输出与下游交付**：输出「面向增材制造的设计（DfAM）」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 面向量产工艺评估
- **方法 / 工具**：压铸、注塑、钣金、CNC、复材成型工艺对比
- **设计思考逻辑**：原型验证后需将 3D 打印件转换为可量产工艺
- **关键约束**：模具成本、最小订单量、良率、周期
- **完成标准 / 输出物**：量产工艺路线图、关键件工艺选择
**三级子任务：**
- **P5.2.3.1 输入梳理与目标量化**：整理「面向量产工艺评估」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.2.3.2 方案/方法设计**：针对「面向量产工艺评估」制定实施方法或候选方案，使用「压铸、注塑、钣金、CNC、复材成型工艺对比」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.2.3.3 实施/原型/样件制作**：根据设计方案执行「面向量产工艺评估」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.2.3.4 验证与问题闭环**：对「面向量产工艺评估」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P5.2.3.5 文档输出与下游交付**：输出「面向量产工艺评估」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 布线、维护与装配

##### 线缆与管路布线设计
- **方法 / 工具**：3D 线束布线、弯曲半径校核、固定点设计
- **设计思考逻辑**：动力/信号/冷却管路随关节运动不拉扯、不磨损；预留维护长度
- **关键约束**：弯曲寿命、EMC 屏蔽、散热、可更换性
- **完成标准 / 输出物**：《布线设计规范》：线缆型号、固定点、弯曲半径、走向
**三级子任务：**
- **P5.3.1.1 输入梳理与目标量化**：整理「线缆与管路布线设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.3.1.2 概念与详细设计**：完成「线缆与管路布线设计」的概念设计、详细设计与接口定义，使用「3D 线束布线、弯曲半径校核、固定点设计」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.3.1.3 实施/原型/样件制作**：根据设计方案执行「线缆与管路布线设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.3.1.4 验证与问题闭环**：对「线缆与管路布线设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P5.3.1.5 文档输出与下游交付**：输出「线缆与管路布线设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 装配顺序与工装夹具规划
- **方法 / 工具**：DFA 分析、装配仿真、标准作业指导书（SOP）
- **设计思考逻辑**：模块化解耦：手臂、腿部、躯干可独立拆装；关键件可达性
- **关键约束**：工具空间、紧固件标准化、节拍
- **完成标准 / 输出物**：装配顺序图、工装清单、SOP 草案
**三级子任务：**
- **P5.3.2.1 输入梳理与目标量化**：整理「装配顺序与工装夹具规划」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.3.2.2 算法/控制方案设计**：基于「DFA 分析、装配仿真、标准作业指导书（SOP）」建立数学模型或算法框架，形成候选方案，评估稳定性、实时性与可扩展性，并冻结实现路径。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.3.2.3 建模/仿真与样机实现**：建立「装配顺序与工装夹具规划」的仿真/数学模型或原型样机，使用「DFA 分析、装配仿真、标准作业指导书（SOP）」执行计算或实验，记录关键参数与边界条件。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.3.2.4 仿真结果校核与优化**：校核「装配顺序与工装夹具规划」仿真结果与理论/试验数据的一致性，识别薄弱点并迭代优化。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.3.2.5 文档输出与下游交付**：输出「装配顺序与工装夹具规划」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 可维护性与维修性设计
- **方法 / 工具**：MTTR 分析、易损件识别、快拆结构
- **设计思考逻辑**：关节、电池、计算模块应能在现场快速更换
- **关键约束**：结构强度、密封、成本
- **完成标准 / 输出物**：维护手册草案、MTTR 目标、快拆件清单
**三级子任务：**
- **P5.3.3.1 输入梳理与目标量化**：整理「可维护性与维修性设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P5.3.3.2 概念与详细设计**：完成「可维护性与维修性设计」的概念设计、详细设计与接口定义，使用「MTTR 分析、易损件识别、快拆结构」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P5.3.3.3 实施/原型/样件制作**：根据设计方案执行「可维护性与维修性设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P5.3.3.4 验证与问题闭环**：对「可维护性与维修性设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P5.3.3.5 文档输出与下游交付**：输出「可维护性与维修性设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
Mechanical Structure is the 5th phase in the full-process development of humanoid robot products, expanded into several Level-3 sub-tasks in WBS V3.

This phase covers complete engineering actions including input review, conceptual design, implementation/prototyping, verification closure, and documentation delivery. It is a critical milestone to ensure downstream dependencies receive qualified inputs.

## Content
### Key Sub-tasks and Technical Content
#### Detailed Structural Design

##### Central Skeleton and Limb Link Design
- **Methods / Tools**: SolidWorks / NX / CATIA, topology optimization, size optimization
- **Design Rationale**: The central skeleton carries the torso load and transmits it to the legs; limb links require high stiffness and low weight
- **Key Constraints**: Stiffness, strength, weight, assembly accessibility
- **Completion Criteria / Deliverables**: 3D structural model, critical cross-section design, preliminary BOM
**Level-3 Sub-tasks:**
- **P5.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Central Skeleton and Limb Link Design," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P5.1.1.2 Conceptual and Detailed Design**: Complete the conceptual design, detailed design, and interface definition for "Central Skeleton and Limb Link Design," verify feasibility using "SolidWorks / NX / CATIA, topology optimization, size optimization," and output drawings/algorithms/logical frameworks.
**Level-4 Key Actions:**
1. Generate no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize a review and freeze the solution
- **P5.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Central Skeleton and Limb Link Design" according to the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P5.1.1.4 Verification and Issue Closure**: Verify the outputs of "Central Skeleton and Limb Link Design," check if completion criteria are met, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P5.1.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Central Skeleton and Limb Link Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Joint Mounting Interface and Housing Design
- **Methods / Tools**: Interface tolerance analysis, locating pin/flange design, sealing design
- **Design Rationale**: Joints and structures require precise coaxial alignment, repeatable assembly/disassembly, and dust/water resistance
- **Key Constraints**: Machining precision, sealing level, maintenance space
- **Completion Criteria / Deliverables**: Joint interface drawings, housing 3D model, sealing solution
**Level-3 Sub-tasks:**
- **P5.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Joint Mounting Interface and Housing Design," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P5.1.2.2 Conceptual and Detailed Design**: Complete the conceptual design, detailed design, and interface definition for "Joint Mounting Interface and Housing Design," verify feasibility using "interface tolerance analysis, locating pin/flange design, sealing design," and output drawings/algorithms/logical frameworks.
**Level-4 Key Actions:**
1. Generate no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize a review and freeze the solution
- **P5.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Joint Mounting Interface and Housing Design" according to the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P5.1.2.4 Verification and Issue Closure**: Verify the outputs of "Joint Mounting Interface and Housing Design," check if completion criteria are met, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P5.1.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Joint Mounting Interface and Housing Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Exterior Cover and Seam Design
- **Methods / Tools**: Class-A surface seams, snap-fit/screw concealment, removable panels
- **Design Rationale**: Covers must balance aesthetics, heat dissipation, maintenance access, and drop protection
- **Key Constraints**: Frozen ID, mold/printing process, assembly sequence
- **Completion Criteria / Deliverables**: Cover 3D model, seam solution, maintenance access layout
**Level-3 Sub-tasks:**
- **P5.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Exterior Cover and Seam Design," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P5.1.3.2 Conceptual and Detailed Design**: Complete the conceptual design, detailed design, and interface definition for "Exterior Cover and Seam Design," verify feasibility using "Class-A surface seams, snap-fit/screw concealment, removable panels," and output drawings/algorithms/logical frameworks.
**Level-4 Key Actions:**
1. Generate no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize a review and freeze the solution
- **P5.1.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Exterior Cover and Seam Design" according to the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P5.1.3.4 Verification and Issue Closure**: Verify the outputs of "Exterior Cover and Seam Design," check if completion criteria are met, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P5.1.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Exterior Cover and Seam Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

#### Materials and Processes

##### Structural Material Selection
- **Methods / Tools**: Comparison of aluminum alloys 7075/6061, carbon fiber, titanium alloy, engineering plastics
- **Design Rationale**: High-load links use aluminum alloy/CNC; housings/brackets use SLS/MJF 3D printing or injection molding
- **Key Constraints**: Strength, stiffness, density, cost, batch manufacturing feasibility
- **Completion Criteria / Deliverables**: "Material Selection Table": material, process, and rationale for each component
**Level-3 Sub-tasks:**
- **P5.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Structural Material Selection," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P5.2.1.2 Candidate Solution Establishment and Evaluation**: Build a candidate solution library for "Structural Material Selection," perform quantitative evaluation using "comparison of aluminum alloys 7075/6061, carbon fiber, titanium alloy, engineering plastics," and determine the final solution considering cost, performance, supply chain, and maintainability.
**Level-4 Key Actions:**
1. Generate no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize a review and freeze the solution
- **P5.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Structural Material Selection" according to the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P5.2.1.4 Verification and Issue Closure**: Verify the outputs of "Structural Material Selection," check if completion criteria are met, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P5.2.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Structural Material Selection," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Design for Additive Manufacturing (DfAM)
- **Methods / Tools**: SLS/MJF/SLA design guidelines, support optimization, lattice structures
- **Design Rationale**: Many structural parts in the prototype phase use 3D printing and require optimization for the printing process
- **Key Constraints**: Printed material strength, interlayer bonding, dimensional accuracy, surface quality
- **Completion Criteria / Deliverables**: DfAM checklist, 3D printed part drawings, printing parameters
**Level-3 Sub-tasks:**
- **P5.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Design for Additive Manufacturing (DfAM)," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P5.2.2.2 Conceptual and Detailed Design**: Complete the conceptual design, detailed design, and interface definition for "Design for Additive Manufacturing (DfAM)," verify feasibility using "SLS/MJF/SLA design guidelines, support optimization, lattice structures," and output drawings/algorithms/logical frameworks.
**Level-4 Key Actions:**
1. Generate no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize a review and freeze the solution
- **P5.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Design for Additive Manufacturing (DfAM)" according to the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P5.2.2.4 Verification and Issue Closure**: Verify the outputs of "Design for Additive Manufacturing (DfAM)," check if completion criteria are met, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P5.2.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Design for Additive Manufacturing (DfAM)," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Mass Production Process Assessment
- **Methods / Tools**: Comparison of die casting, injection molding, sheet metal, CNC, composite molding processes
- **Design Rationale**: After prototype verification, 3D printed parts need to be converted to mass-producible processes
- **Key Constraints**: Mold cost, minimum order quantity, yield rate, cycle time
- **Completion Criteria / Deliverables**: Mass production process roadmap, key part process selection
**Level-3 Sub-tasks:**
- **P5.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Mass Production Process Assessment," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P5.2.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Mass Production Process Assessment," conduct feasibility studies using "comparison of die casting, injection molding, sheet metal, CNC, composite molding processes," and clarify the technical roadmap and resource requirements.
**Level-4 Key Actions:**
1. Generate no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize a review and freeze the solution
- **P5.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Mass Production Process Assessment" according to the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P5.2.3.4 Verification and Issue Closure**: Verify the outputs of "Mass Production Process Assessment," check if completion criteria are met, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P5.2.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Mass Production Process Assessment," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

#### Wiring, Maintenance, and Assembly

##### Cable and Hose Routing Design
- **Methods / Tools**: 3D harness routing, bend radius verification, fixing point design
- **Design Rationale**: Power/signal/cooling lines must not pull or wear during joint movement; reserve maintenance length
- **Key Constraints**: Bending fatigue life, EMC shielding, heat dissipation, replaceability
- **Completion Criteria / Deliverables**: "Wiring Design Specification": cable type, fixing points, bend radius, routing path
**Level-3 Sub-tasks:**
- **P5.3.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Cable and Hose Routing Design," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P5.3.1.2 Conceptual and Detailed Design**: Complete the conceptual design, detailed design, and interface definition for "Cable and Hose Routing Design," verify feasibility using "3D harness routing, bend radius verification, fixing point design," and output drawings/algorithms/logical frameworks.
**Level-4 Key Actions:**
1. Generate no fewer than 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize a review and freeze the solution
- **P5.3.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation work for "Cable and Hose Routing Design" according to the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P5.3.1.4 Verification and Issue Closure**: Verify the outputs of "Cable and Hose Routing Design," check if completion criteria are met, record issues, and track them to closure.
**Level-4 Key Actions:**
1. Develop test/review plans and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P5.3.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawings/specifications for "Cable and Hose Routing Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

## 개요
본체 구조 공학과 프로토타입(Mechanical Structure)은 휴머노이드 로봇 제품 개발 전 과정 중 5번째 단계이며, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.

이 단계는 입력 검토, 설계, 구현/프로토타입, 검증 폐쇄 및 문서 인도 등 완전한 엔지니어링 작업을 포함하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 마일스톤입니다.

## 핵심 내용

#### 상세 구조 설계

##### 중앙 골격 및 사지 링크 설계
- **방법 / 도구**: SolidWorks / NX / CATIA, 위상 최적화, 치수 최적화
- **설계 사고 논리**: 중앙 골격은 동체 하중을 지지하고 다리로 전달하며, 사지 링크는 높은 강성과 낮은 중량이 요구됨
- **핵심 제약 조건**: 강성, 강도, 중량, 조립 접근성
- **완료 기준 / 산출물**: 3D 구조 모델, 주요 단면 설계, BOM 초안
**3레벨 하위 작업:**
- **P5.1.1.1 입력 검토 및 목표 정량화**: 「중앙 골격 및 사지 링크 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P5.1.1.2 개념 및 상세 설계**: 「중앙 골격 및 사지 링크 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「SolidWorks / NX / CATIA, 위상 최적화, 치수 최적화」를 사용하여 타당성을 검증하며, 도면/알고리즘/로직 프레임워크를 출력함.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 방안을 마련
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 확정
- **P5.1.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「중앙 골격 및 사지 링크 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품을 구축하고 핵심 파라미터를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P5.1.1.4 검증 및 문제 폐쇄**: 「중앙 골격 및 사지 링크 설계」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P5.1.1.5 문서 출력 및 하위 인도**: 「중앙 골격 및 사지 링크 설계」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 관절 장착 인터페이스 및 하우징 설계
- **방법 / 도구**: 인터페이스 공차 분석, 위치 결정 핀/플랜지 설계, 밀봉 설계
- **설계 사고 논리**: 관절과 구조 사이에는 정밀한 동축성, 반복적인 분해/조립이 가능해야 하며, 방진 및 방수가 필요함
- **핵심 제약 조건**: 가공 정밀도, 밀봉 등급, 유지보수 공간
- **완료 기준 / 산출물**: 관절 인터페이스 도면, 하우징 3D, 밀봉 방안
**3레벨 하위 작업:**
- **P5.1.2.1 입력 검토 및 목표 정량화**: 「관절 장착 인터페이스 및 하우징 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P5.1.2.2 개념 및 상세 설계**: 「관절 장착 인터페이스 및 하우징 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「인터페이스 공차 분석, 위치 결정 핀/플랜지 설계, 밀봉 설계」를 사용하여 타당성을 검증하며, 도면/알고리즘/로직 프레임워크를 출력함.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 방안을 마련
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 확정
- **P5.1.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「관절 장착 인터페이스 및 하우징 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품을 구축하고 핵심 파라미터를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P5.1.2.4 검증 및 문제 폐쇄**: 「관절 장착 인터페이스 및 하우징 설계」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P5.1.2.5 문서 출력 및 하위 인도**: 「관절 장착 인터페이스 및 하우징 설계」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 외관 커버 및 분할선 설계
- **방법 / 도구**: A면 분할선, 스냅/나사 은폐, 분리형 패널
- **설계 사고 논리**: 커버는 외관, 방열, 유지보수 개구부, 낙하 보호를 모두 고려해야 함
- **핵심 제약 조건**: ID 확정, 금형/프린팅 공정, 조립 순서
- **완료 기준 / 산출물**: 커버 3D, 분할선 방안, 유지보수 개구부 배치
**3레벨 하위 작업:**
- **P5.1.3.1 입력 검토 및 목표 정량화**: 「외관 커버 및 분할선 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P5.1.3.2 개념 및 상세 설계**: 「외관 커버 및 분할선 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「A면 분할선, 스냅/나사 은폐, 분리형 패널」을 사용하여 타당성을 검증하며, 도면/알고리즘/로직 프레임워크를 출력함.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 방안을 마련
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 확정
- **P5.1.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「외관 커버 및 분할선 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품을 구축하고 핵심 파라미터를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P5.1.3.4 검증 및 문제 폐쇄**: 「외관 커버 및 분할선 설계」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P5.1.3.5 문서 출력 및 하위 인도**: 「외관 커버 및 분할선 설계」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 재료 및 공정

##### 구조 재료 선정
- **방법 / 도구**: 알루미늄 합금 7075/6061, 탄소 섬유, 티타늄 합금, 엔지니어링 플라스틱 비교
- **설계 사고 논리**: 고하중 링크는 알루미늄 합금/CNC를 사용하고, 외부 케이스/브래킷은 SLS/MJF 3D 프린팅 또는 사출 성형을 사용함
- **핵심 제약 조건**: 강도, 강성, 밀도, 비용, 양산 가능성
- **완료 기준 / 산출물**: 《재료 선정표》: 각 부품의 재료, 공정, 이유
**3레벨 하위 작업:**
- **P5.2.1.1 입력 검토 및 목표 정량화**: 「구조 재료 선정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P5.2.1.2 후보 방안 수립 및 평가**: 「구조 재료 선정」을 위한 후보 방안 라이브러리를 구축하고, 「알루미늄 합금 7075/6061, 탄소 섬유, 티타늄 합금, 엔지니어링 플라스틱 비교」를 사용하여 정량적으로 평가하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 방안을 결정함.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 방안을 마련
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 확정
- **P5.2.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「구조 재료 선정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품을 구축하고 핵심 파라미터를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P5.2.1.4 검증 및 문제 폐쇄**: 「구조 재료 선정」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P5.2.1.5 문서 출력 및 하위 인도**: 「구조 재료 선정」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 적층 제조를 위한 설계 (DfAM)
- **방법 / 도구**: SLS/MJF/SLA 설계 규격, 지지대 최적화, 격자 구조
- **설계 사고 논리**: 프로토타입 단계에서 많은 구조 부품이 3D 프린팅을 사용하므로, 프린팅 공정에 맞게 최적화해야 함
- **핵심 제약 조건**: 프린팅 재료 강도, 층간 결합, 치수 정밀도, 표면 품질
- **완료 기준 / 산출물**: DfAM 체크리스트, 3D 프린팅 부품 도면, 프린팅 파라미터
**3레벨 하위 작업:**
- **P5.2.2.1 입력 검토 및 목표 정량화**: 「적층 제조를 위한 설계 (DfAM)」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P5.2.2.2 개념 및 상세 설계**: 「적층 제조를 위한 설계 (DfAM)」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「SLS/MJF/SLA 설계 규격, 지지대 최적화, 격자 구조」를 사용하여 타당성을 검증하며, 도면/알고리즘/로직 프레임워크를 출력함.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 방안을 마련
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 확정
- **P5.2.2.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「적층 제조를 위한 설계 (DfAM)」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품을 구축하고 핵심 파라미터를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P5.2.2.4 검증 및 문제 폐쇄**: 「적층 제조를 위한 설계 (DfAM)」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P5.2.2.5 문서 출력 및 하위 인도**: 「적층 제조를 위한 설계 (DfAM)」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 양산 공정 평가
- **방법 / 도구**: 다이캐스팅, 사출 성형, 판금, CNC, 복합재 성형 공정 비교
- **설계 사고 논리**: 프로토타입 검증 후 3D 프린팅 부품을 양산 가능한 공정으로 전환해야 함
- **핵심 제약 조건**: 금형 비용, 최소 주문량, 수율, 사이클 타임
- **완료 기준 / 산출물**: 양산 공정 로드맵, 핵심 부품 공정 선택
**3레벨 하위 작업:**
- **P5.2.3.1 입력 검토 및 목표 정량화**: 「양산 공정 평가」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P5.2.3.2 방안/방법 설계**: 「양산 공정 평가」를 위한 구현 방법 또는 후보 방안을 수립하고, 「다이캐스팅, 사출 성형, 판금, CNC, 복합재 성형 공정 비교」를 사용하여 논증하며, 기술 로드맵과 리소스 요구 사항을 명확히 함.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 방안을 마련
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 확정
- **P5.2.3.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「양산 공정 평가」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품을 구축하고 핵심 파라미터를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P5.2.3.4 검증 및 문제 폐쇄**: 「양산 공정 평가」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P5.2.3.5 문서 출력 및 하위 인도**: 「양산 공정 평가」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 배선, 유지보수 및 조립

##### 케이블 및 배관 배선 설계
- **방법 / 도구**: 3D 와이어 하네스 배선, 굽힘 반경 검토, 고정점 설계
- **설계 사고 논리**: 동력/신호/냉각 배관이 관절 운동 시 당겨지거나 마모되지 않도록 하고, 유지보수 여유 길이를 확보함
- **핵심 제약 조건**: 굽힘 수명, EMC 차폐, 방열, 교체 가능성
- **완료 기준 / 산출물**: 《배선 설계 규격》: 케이블 모델, 고정점, 굽힘 반경, 경로
**3레벨 하위 작업:**
- **P5.3.1.1 입력 검토 및 목표 정량화**: 「케이블 및 배관 배선 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P5.3.1.2 개념 및 상세 설계**: 「케이블 및 배관 배선 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「3D 와이어 하네스 배선, 굽힘 반경 검토, 고정점 설계」를 사용하여 타당성을 검증하며, 도면/알고리즘/로직 프레임워크를 출력함.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 방안을 마련
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 방안을 확정
- **P5.3.1.3 구현/프로토타입/시제품 제작**: 설계 방안에 따라 「케이블 및 배관 배선 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
**4레벨 핵심 작업:**
1. 모델/시제품을 구축하고 핵심 파라미터를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P5.3.1.4 검증 및 문제 폐쇄**: 「케이블 및 배관 배선 설계」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적함.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P5.3.1.5 문서 출력 및 하위 인도**: 「케이블 및 배관 배선 설계」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료함.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지
