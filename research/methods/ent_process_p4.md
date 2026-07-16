---
$id: ent_process_p4
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Design of Joint Module and Actuator & Drive
  zh: 关节模组与驱动系统设计（Actuator & Drive）
  ko: 关节模组与驱动系统设计（Actuator & Drive）
summary:
  en: Design of Actuator & Drive-phase 4 of the entire product development process for Android, covering conceptual design,
    implementation verification, and document delivery.
  zh: 关节模组与驱动系统设计（Actuator & Drive）是人形机器人产品开发全流程中的第 4 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 关节模组与驱动系统设计（Actuator & Drive）
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
关节模组与驱动系统设计（Actuator & Drive）是人形机器人产品开发全流程中的第 4 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 关节需求与拓扑

##### 关节性能需求精化
- **方法 / 工具**：P3.1.3 输出 + 安全系数、热裕量、带宽需求
- **设计思考逻辑**：峰值扭矩 = 动力学峰值 × 1.5–2.0 安全系数；连续扭矩按持续行走工况
- **关键约束**：电机热时间常数、散热能力、反向驱动透明度
- **完成标准 / 输出物**：各关节最终扭矩/速度/带宽需求表 v2
**三级子任务：**
- **P4.1.1.1 输入梳理与目标量化**：整理「关节性能需求精化」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.1.1.2 方案/方法设计**：针对「关节性能需求精化」制定实施方法或候选方案，使用「P3.1.3 输出 + 安全系数、热裕量、带宽需求」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.1.1.3 实施/原型/样件制作**：根据设计方案执行「关节性能需求精化」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.1.1.4 验证与问题闭环**：对「关节性能需求精化」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.1.1.5 文档输出与下游交付**：输出「关节性能需求精化」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 执行器拓扑选择
- **方法 / 工具**：QDD、谐波减速、行星+无框电机、直驱对比表
- **设计思考逻辑**：高动态关节（髋/踝）倾向 QDD；高扭矩小体积（肩/腕）倾向谐波
- **关键约束**：反驱透明度、刚度、背隙、效率、噪音
- **完成标准 / 输出物**：《执行器拓扑决策矩阵》：每关节选型、理由、备份方案
**三级子任务：**
- **P4.1.2.1 输入梳理与目标量化**：整理「执行器拓扑选择」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.1.2.2 候选方案建立与评估**：针对「执行器拓扑选择」建立候选方案库，使用「QDD、谐波减速、行星+无框电机、直驱对比表」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.1.2.3 实施/原型/样件制作**：根据设计方案执行「执行器拓扑选择」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.1.2.4 验证与问题闭环**：对「执行器拓扑选择」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.1.2.5 文档输出与下游交付**：输出「执行器拓扑选择」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 电机与减速器

##### 电机选型
- **方法 / 工具**：转矩密度、热阻、编码器分辨率、峰值电流、效率图对比
- **设计思考逻辑**：优先高转矩密度无框/集成电机；校核绕组温升与退磁
- **关键约束**：驱动器母线电压、电流能力、供货周期
- **完成标准 / 输出物**：电机规格书、选型对比表、热校核
**三级子任务：**
- **P4.2.1.1 输入梳理与目标量化**：整理「电机选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.2.1.2 候选方案建立与评估**：针对「电机选型」建立候选方案库，使用「转矩密度、热阻、编码器分辨率、峰值电流、效率图对比」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.2.1.3 实施/原型/样件制作**：根据设计方案执行「电机选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.2.1.4 验证与问题闭环**：对「电机选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.2.1.5 文档输出与下游交付**：输出「电机选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 减速器与传动选型
- **方法 / 工具**：谐波、行星、摆线、同步带、丝杠对比；背隙/刚度/寿命测试
- **设计思考逻辑**：输出端力矩/位置传感器配置决定控制精度；传动链刚度影响带宽
- **关键约束**：谐波柔轮疲劳、行星磨损、噪音、成本
- **完成标准 / 输出物**：减速器规格、传动链图纸、刚度/背隙预算
**三级子任务：**
- **P4.2.2.1 输入梳理与目标量化**：整理「减速器与传动选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.2.2.2 候选方案建立与评估**：针对「减速器与传动选型」建立候选方案库，使用「谐波、行星、摆线、同步带、丝杠对比；背隙/刚度/寿命测试」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.2.2.3 实施/原型/样件制作**：根据设计方案执行「减速器与传动选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.2.2.4 验证与问题闭环**：对「减速器与传动选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.2.2.5 文档输出与下游交付**：输出「减速器与传动选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 轴承与输出接口设计
- **方法 / 工具**：轴承寿命计算、交叉滚子/角接触组合、配合公差分析
- **设计思考逻辑**：关节输出端承受径向/轴向/力矩复合载荷，轴承布置决定寿命
- **关键约束**：加工精度、装配顺序、维护性
- **完成标准 / 输出物**：轴承选型表、接口图纸、寿命校核
**三级子任务：**
- **P4.2.3.1 输入梳理与目标量化**：整理「轴承与输出接口设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.2.3.2 概念与详细设计**：完成「轴承与输出接口设计」的概念设计、详细设计与接口定义，使用「轴承寿命计算、交叉滚子/角接触组合、配合公差分析」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.2.3.3 实施/原型/样件制作**：根据设计方案执行「轴承与输出接口设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.2.3.4 验证与问题闭环**：对「轴承与输出接口设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.2.3.5 文档输出与下游交付**：输出「轴承与输出接口设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 驱动器与传感器集成

##### 电机驱动器设计/选型
- **方法 / 工具**：FOC 驱动器、SiC/GaN 方案、峰值/连续电流、热设计
- **设计思考逻辑**：关节内部集成驱动器可缩短线缆、降低 EMI；需考虑散热
- **关键约束**：空间、散热、EMI、功能安全
- **完成标准 / 输出物**：驱动器规格、电气原理图、热仿真/测试
**三级子任务：**
- **P4.3.1.1 输入梳理与目标量化**：整理「电机驱动器设计/选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.3.1.2 候选方案建立与评估**：针对「电机驱动器设计/选型」建立候选方案库，使用「FOC 驱动器、SiC/GaN 方案、峰值/连续电流、热设计」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.3.1.3 实施/原型/样件制作**：根据设计方案执行「电机驱动器设计/选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.3.1.4 验证与问题闭环**：对「电机驱动器设计/选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.3.1.5 文档输出与下游交付**：输出「电机驱动器设计/选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 位置/力矩传感器方案
- **方法 / 工具**：绝对/增量编码器、磁编/光编、力矩传感器、双编码器方案
- **设计思考逻辑**：双编码器提升控制精度；力矩传感器实现柔顺控制
- **关键约束**：成本、精度、抗油污振动、布线
- **完成标准 / 输出物**：传感器方案、精度预算、安装图纸
**三级子任务：**
- **P4.3.2.1 输入梳理与目标量化**：整理「位置/力矩传感器方案」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.3.2.2 方案/方法设计**：针对「位置/力矩传感器方案」制定实施方法或候选方案，使用「绝对/增量编码器、磁编/光编、力矩传感器、双编码器方案」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.3.2.3 实施/原型/样件制作**：根据设计方案执行「位置/力矩传感器方案」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.3.2.4 验证与问题闭环**：对「位置/力矩传感器方案」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.3.2.5 文档输出与下游交付**：输出「位置/力矩传感器方案」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 关节模组集成与台架测试
- **方法 / 工具**：扭矩传感器、功率分析仪、温升/刚度/带宽测试
- **设计思考逻辑**：台架验证峰值扭矩、连续扭矩、刚度、效率、温升是否达标
- **关键约束**：测试夹具刚性、测量精度
- **完成标准 / 输出物**：《关节测试报告》：扭矩-电流、效率图、温升曲线、带宽
**三级子任务：**
- **P4.3.3.1 输入梳理与目标量化**：整理「关节模组集成与台架测试」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.3.3.2 接口与集成策略设计**：梳理「关节模组集成与台架测试」涉及的子系统接口、数据流与时序，制定集成顺序、回退策略与异常处理机制。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.3.3.3 实施/原型/样件制作**：根据设计方案执行「关节模组集成与台架测试」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.3.3.4 测试执行与结果分析**：按照验收标准执行「关节模组集成与台架测试」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.3.3.5 文档输出与下游交付**：输出「关节模组集成与台架测试」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 关节可靠性

##### 关节寿命与失效分析
- **方法 / 工具**：加速寿命试验、振动试验、磨损分析、FMEA
- **设计思考逻辑**：预估关节在目标寿命内的磨损与失效模式，指导维护策略
- **关键约束**：MTBF 目标、维护周期、测试成本
- **完成标准 / 输出物**：寿命测试计划、失效模式分析、维护周期建议
**三级子任务：**
- **P4.4.1.1 输入梳理与目标量化**：整理「关节寿命与失效分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.4.1.2 方案/方法设计**：针对「关节寿命与失效分析」制定实施方法或候选方案，使用「加速寿命试验、振动试验、磨损分析、FMEA」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.4.1.3 实施/原型/样件制作**：根据设计方案执行「关节寿命与失效分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.4.1.4 验证与问题闭环**：对「关节寿命与失效分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.4.1.5 文档输出与下游交付**：输出「关节寿命与失效分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 关节安全与故障保护
- **方法 / 工具**：过流/过温/过压保护、刹车、limp-home 模式
- **设计思考逻辑**：关节失效不能导致整机失控；需有故障安全状态
- **关键约束**：响应时间、额外重量、成本
- **完成标准 / 输出物**：故障保护策略、FMEA 更新、安全测试
**三级子任务：**
- **P4.4.2.1 输入梳理与目标量化**：整理「关节安全与故障保护」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P4.4.2.2 方案/方法设计**：针对「关节安全与故障保护」制定实施方法或候选方案，使用「过流/过温/过压保护、刹车、limp-home 模式」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P4.4.2.3 实施/原型/样件制作**：根据设计方案执行「关节安全与故障保护」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P4.4.2.4 验证与问题闭环**：对「关节安全与故障保护」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P4.4.2.5 文档输出与下游交付**：输出「关节安全与故障保护」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### NVH 与声学设计

##### 电机/减速器噪声源分析
- **方法 / 工具**：声功率测量、频谱分析、阶次分析、结构模态测试
- **设计思考逻辑**：识别主要噪声源（齿槽转矩、换向、齿轮啮合）以针对性降噪
- **关键约束**：测试环境本底噪声、传感器布置
- **完成标准 / 输出物**：噪声源频谱图、主要贡献频段识别
**三级子任务：**
- **P4.5.1.1 输入梳理与目标量化**：整理「电机/减速器噪声源分析」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P4.5.1.2 方案/方法设计**：针对「电机/减速器噪声源分析」制定实施方法或候选方案，使用「声功率测量、频谱分析、阶次分析、结构模态测试」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P4.5.1.3 实施/建模/实验**：根据方案执行「电机/减速器噪声源分析」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P4.5.1.4 验证与优化**：对「电机/减速器噪声源分析」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P4.5.1.5 文档输出与下游交付**：输出「电机/减速器噪声源分析」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 整机 NVH 测试
- **方法 / 工具**：半消声室/现场声压测量、振动加速度、声强扫描
- **设计思考逻辑**：评估整机在站立、行走、操作时的噪声与振动水平
- **关键约束**：测试场地、背景噪声、运行工况
- **完成标准 / 输出物**：整机噪音 dB(A) 满足目标、振动幅值满足目标
**三级子任务：**
- **P4.5.2.1 输入梳理与目标量化**：整理「整机 NVH 测试」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P4.5.2.2 方案/方法设计**：针对「整机 NVH 测试」制定实施方法或候选方案，使用「半消声室/现场声压测量、振动加速度、声强扫描」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P4.5.2.3 实施/建模/实验**：根据方案执行「整机 NVH 测试」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P4.5.2.4 验证与优化**：对「整机 NVH 测试」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P4.5.2.5 文档输出与下游交付**：输出「整机 NVH 测试」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 降噪设计与验证
- **方法 / 工具**：阻尼材料、隔振垫、齿形优化、控制降噪（电流谐波抑制）
- **设计思考逻辑**：从结构与控制两方面降低噪声，满足人机共融场景要求
- **关键约束**：重量、散热、成本
- **完成标准 / 输出物**：降噪方案、验证前后对比、满足法规/场景要求
**三级子任务：**
- **P4.5.3.1 输入梳理与目标量化**：整理「降噪设计与验证」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P4.5.3.2 方案/方法设计**：针对「降噪设计与验证」制定实施方法或候选方案，使用「阻尼材料、隔振垫、齿形优化、控制降噪（电流谐波抑制）」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P4.5.3.3 实施/建模/实验**：根据方案执行「降噪设计与验证」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P4.5.3.4 验证与优化**：对「降噪设计与验证」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P4.5.3.5 文档输出与下游交付**：输出「降噪设计与验证」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
The Joint Module and Drive System Design (Actuator & Drive) is the 4th stage in the full-process development of humanoid robot products, expanded into several Level-3 sub-tasks in WBS V3.
## Content
This stage covers complete engineering actions such as input review, concept design, implementation/prototyping, verification closure, and documentation delivery, serving as a critical milestone to ensure downstream dependents receive qualified inputs.

## Key Sub-Tasks and Technical Content
#### Joint Requirements and Topology

##### Joint Performance Requirement Refinement
- **Method / Tool**: P3.1.3 output + safety factor, thermal margin, bandwidth requirement
- **Design Rationale**: Peak torque = dynamic peak × 1.5–2.0 safety factor; continuous torque based on sustained walking conditions
- **Key Constraints**: Motor thermal time constant, heat dissipation capability, back-drive transparency
- **Completion Criteria / Deliverable**: Final torque/speed/bandwidth requirement table v2 for each joint
**Level-3 Sub-Tasks:**
- **P4.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Joint Performance Requirement Refinement," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P4.1.1.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "Joint Performance Requirement Refinement," using "P3.1.3 output + safety factor, thermal margin, bandwidth requirement" for demonstration, and clarify technical route and resource needs.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P4.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Joint Performance Requirement Refinement" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P4.1.1.4 Verification and Issue Closure**: Verify the output of "Joint Performance Requirement Refinement," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P4.1.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Joint Performance Requirement Refinement," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Actuator Topology Selection
- **Method / Tool**: QDD, harmonic drive, planetary + frameless motor, direct drive comparison table
- **Design Rationale**: High-dynamic joints (hip/ankle) favor QDD; high-torque small-volume joints (shoulder/wrist) favor harmonic drive
- **Key Constraints**: Back-drive transparency, stiffness, backlash, efficiency, noise
- **Completion Criteria / Deliverable**: "Actuator Topology Decision Matrix": selection per joint, rationale, backup solution
**Level-3 Sub-Tasks:**
- **P4.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Actuator Topology Selection," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P4.1.2.2 Candidate Solution Establishment and Evaluation**: Build a candidate solution library for "Actuator Topology Selection," use "QDD, harmonic drive, planetary + frameless motor, direct drive comparison table" for quantitative evaluation, and determine the final solution considering cost, performance, supply chain, and maintainability.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P4.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Actuator Topology Selection" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P4.1.2.4 Verification and Issue Closure**: Verify the output of "Actuator Topology Selection," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P4.1.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Actuator Topology Selection," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### Motor and Reducer

##### Motor Selection
- **Method / Tool**: Torque density, thermal resistance, encoder resolution, peak current, efficiency map comparison
- **Design Rationale**: Prioritize high torque density frameless/integrated motors; verify winding temperature rise and demagnetization
- **Key Constraints**: Drive bus voltage, current capability, lead time
- **Completion Criteria / Deliverable**: Motor specification sheet, selection comparison table, thermal verification
**Level-3 Sub-Tasks:**
- **P4.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Motor Selection," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P4.2.1.2 Candidate Solution Establishment and Evaluation**: Build a candidate solution library for "Motor Selection," use "torque density, thermal resistance, encoder resolution, peak current, efficiency map comparison" for quantitative evaluation, and determine the final solution considering cost, performance, supply chain, and maintainability.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P4.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Motor Selection" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P4.2.1.4 Verification and Issue Closure**: Verify the output of "Motor Selection," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P4.2.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Motor Selection," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Reducer and Transmission Selection
- **Method / Tool**: Comparison of harmonic, planetary, cycloidal, timing belt, leadscrew; backlash/stiffness/life testing
- **Design Rationale**: Output torque/position sensor configuration determines control accuracy; transmission chain stiffness affects bandwidth
- **Key Constraints**: Harmonic flexspline fatigue, planetary wear, noise, cost
- **Completion Criteria / Deliverable**: Reducer specification, transmission chain drawing, stiffness/backlash budget
**Level-3 Sub-Tasks:**
- **P4.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Reducer and Transmission Selection," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P4.2.2.2 Candidate Solution Establishment and Evaluation**: Build a candidate solution library for "Reducer and Transmission Selection," use "comparison of harmonic, planetary, cycloidal, timing belt, leadscrew; backlash/stiffness/life testing" for quantitative evaluation, and determine the final solution considering cost, performance, supply chain, and maintainability.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P4.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Reducer and Transmission Selection" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P4.2.2.4 Verification and Issue Closure**: Verify the output of "Reducer and Transmission Selection," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P4.2.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Reducer and Transmission Selection," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Bearing and Output Interface Design
- **Method / Tool**: Bearing life calculation, cross roller/angular contact combination, fit tolerance analysis
- **Design Rationale**: Joint output end bears combined radial/axial/torque loads; bearing arrangement determines life
- **Key Constraints**: Machining accuracy, assembly sequence, maintainability
- **Completion Criteria / Deliverable**: Bearing selection table, interface drawing, life verification
**Level-3 Sub-Tasks:**
- **P4.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Bearing and Output Interface Design," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P4.2.3.2 Concept and Detailed Design**: Complete concept design, detailed design, and interface definition for "Bearing and Output Interface Design," use "bearing life calculation, cross roller/angular contact combination, fit tolerance analysis" to verify feasibility, and output drawings/algorithms/logic frameworks.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P4.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Bearing and Output Interface Design" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P4.2.3.4 Verification and Issue Closure**: Verify the output of "Bearing and Output Interface Design," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P4.2.3.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Bearing and Output Interface Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

#### Driver and Sensor Integration

##### Motor Driver Design/Selection
- **Method / Tool**: FOC driver, SiC/GaN solution, peak/continuous current, thermal design
- **Design Rationale**: Integrating the driver inside the joint shortens cables and reduces EMI; heat dissipation must be considered
- **Key Constraints**: Space, heat dissipation, EMI, functional safety
- **Completion Criteria / Deliverable**: Driver specification, electrical schematic, thermal simulation/test
**Level-3 Sub-Tasks:**
- **P4.3.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Motor Driver Design/Selection," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P4.3.1.2 Candidate Solution Establishment and Evaluation**: Build a candidate solution library for "Motor Driver Design/Selection," use "FOC driver, SiC/GaN solution, peak/continuous current, thermal design" for quantitative evaluation, and determine the final solution considering cost, performance, supply chain, and maintainability.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P4.3.1.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Motor Driver Design/Selection" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P4.3.1.4 Verification and Issue Closure**: Verify the output of "Motor Driver Design/Selection," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P4.3.1.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Motor Driver Design/Selection," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

##### Position/Torque Sensor Solution
- **Method / Tool**: Absolute/incremental encoder, magnetic/optical encoder, torque sensor, dual-encoder solution
- **Design Rationale**: Dual encoders improve control accuracy; torque sensors enable compliant control
- **Key Constraints**: Cost, accuracy, resistance to oil contamination and vibration, wiring
- **Completion Criteria / Deliverable**: Sensor solution, accuracy budget, installation drawing
**Level-3 Sub-Tasks:**
- **P4.3.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Position/Torque Sensor Solution," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P4.3.2.2 Concept/Method Design**: Develop implementation methods or candidate solutions for "Position/Torque Sensor Solution," using "absolute/incremental encoder, magnetic/optical encoder, torque sensor, dual-encoder solution" for demonstration, and clarify technical route and resource needs.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and assign quantitative scores
3. Organize review and freeze the solution
- **P4.3.2.3 Implementation/Prototype/Sample Fabrication**: Execute the implementation of "Position/Torque Sensor Solution" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P4.3.2.4 Verification and Issue Closure**: Verify the output of "Position/Torque Sensor Solution," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P4.3.2.5 Documentation Output and Downstream Delivery**: Output the final report/drawing/specification for "Position/Torque Sensor Solution," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and cite raw data
2. Complete internal review and version control
3. Release and notify downstream dependents

## 개요
관절 모듈 및 구동 시스템 설계(Actuator & Drive)는 휴머노이드 로봇 제품 개발 전 과정 중 4번째 단계이며, WBS V3에서 여러 3레벨 하위 작업으로 세분화됩니다.
## 핵심 내용
이 단계는 입력 정리, 설계, 구현/프로토타입, 검증 폐쇄 및 문서 인도 등 완전한 엔지니어링 작업을 포함하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 단계입니다.

## 주요 하위 작업 및 기술 내용
#### 관절 요구 사항 및 토폴로지

##### 관절 성능 요구 사항 정밀화
- **방법 / 도구**: P3.1.3 출력 + 안전 계수, 열 여유, 대역폭 요구 사항
- **설계 사고 논리**: 최대 토크 = 동역학 최대값 × 1.5–2.0 안전 계수; 연속 토크는 지속 보행 조건 기준
- **주요 제약 조건**: 모터 열 시상수, 방열 능력, 역구동 투명성
- **완료 기준 / 산출물**: 각 관절 최종 토크/속도/대역폭 요구 사항표 v2
**3레벨 하위 작업:**
- **P4.1.1.1 입력 정리 및 목표 정량화**: 「관절 성능 요구 사항 정밀화」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 수립
- **P4.1.1.2 설계/방법 설계**: 「관절 성능 요구 사항 정밀화」에 대한 구현 방법 또는 후보 설계를 수립하고, 「P3.1.3 출력 + 안전 계수, 열 여유, 대역폭 요구 사항」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 주요 작업:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 수립하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P4.1.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「관절 성능 요구 사항 정밀화」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P4.1.1.4 검증 및 문제 폐쇄**: 「관절 성능 요구 사항 정밀화」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료될 때까지 추적합니다.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P4.1.1.5 문서 출력 및 하위 인도**: 「관절 성능 요구 사항 정밀화」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 액추에이터 토폴로지 선택
- **방법 / 도구**: QDD, 하모닉 감속, 유성+프레임리스 모터, 직접 구동 비교표
- **설계 사고 논리**: 고동적 관절(엉덩이/발목)은 QDD 선호; 고토크 소형(어깨/손목)은 하모닉 선호
- **주요 제약 조건**: 역구동 투명성, 강성, 백래시, 효율, 소음
- **완료 기준 / 산출물**: 《액추에이터 토폴로지 결정 매트릭스》: 관절별 선정, 이유, 백업 설계
**3레벨 하위 작업:**
- **P4.1.2.1 입력 정리 및 목표 정량화**: 「액추에이터 토폴로지 선택」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 수립
- **P4.1.2.2 후보 설계 수립 및 평가**: 「액추에이터 토폴로지 선택」에 대한 후보 설계 라이브러리를 구축하고, 「QDD, 하모닉 감속, 유성+프레임리스 모터, 직접 구동 비교표」를 사용하여 정량적으로 평가하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 설계를 결정합니다.
**4레벨 주요 작업:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 수립하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P4.1.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「액추에이터 토폴로지 선택」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P4.1.2.4 검증 및 문제 폐쇄**: 「액추에이터 토폴로지 선택」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료될 때까지 추적합니다.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P4.1.2.5 문서 출력 및 하위 인도**: 「액추에이터 토폴로지 선택」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 모터 및 감속기

##### 모터 선정
- **방법 / 도구**: 토크 밀도, 열 저항, 엔코더 분해능, 피크 전류, 효율 그래프 비교
- **설계 사고 논리**: 높은 토크 밀도의 프레임리스/통합 모터 우선; 권선 온도 상승 및 감자 검증
- **주요 제약 조건**: 드라이버 모선 전압, 전류 용량, 공급 기간
- **완료 기준 / 산출물**: 모터 규격서, 선정 비교표, 열 검증
**3레벨 하위 작업:**
- **P4.2.1.1 입력 정리 및 목표 정량화**: 「모터 선정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 수립
- **P4.2.1.2 후보 설계 수립 및 평가**: 「모터 선정」에 대한 후보 설계 라이브러리를 구축하고, 「토크 밀도, 열 저항, 엔코더 분해능, 피크 전류, 효율 그래프 비교」를 사용하여 정량적으로 평가하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 설계를 결정합니다.
**4레벨 주요 작업:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 수립하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P4.2.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「모터 선정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P4.2.1.4 검증 및 문제 폐쇄**: 「모터 선정」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료될 때까지 추적합니다.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P4.2.1.5 문서 출력 및 하위 인도**: 「모터 선정」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 감속기 및 전동 선정
- **방법 / 도구**: 하모닉, 유성, 사이클로이드, 타이밍 벨트, 볼스크류 비교; 백래시/강성/수명 테스트
- **설계 사고 논리**: 출력단 토크/위치 센서 구성이 제어 정밀도를 결정; 전동 체인 강성이 대역폭에 영향
- **주요 제약 조건**: 하모닉 플렉스플라인 피로, 유성 마모, 소음, 비용
- **완료 기준 / 산출물**: 감속기 규격, 전동 체인 도면, 강성/백래시 예산
**3레벨 하위 작업:**
- **P4.2.2.1 입력 정리 및 목표 정량화**: 「감속기 및 전동 선정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 수립
- **P4.2.2.2 후보 설계 수립 및 평가**: 「감속기 및 전동 선정」에 대한 후보 설계 라이브러리를 구축하고, 「하모닉, 유성, 사이클로이드, 타이밍 벨트, 볼스크류 비교; 백래시/강성/수명 테스트」를 사용하여 정량적으로 평가하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 설계를 결정합니다.
**4레벨 주요 작업:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 수립하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P4.2.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「감속기 및 전동 선정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P4.2.2.4 검증 및 문제 폐쇄**: 「감속기 및 전동 선정」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료될 때까지 추적합니다.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P4.2.2.5 문서 출력 및 하위 인도**: 「감속기 및 전동 선정」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 베어링 및 출력 인터페이스 설계
- **방법 / 도구**: 베어링 수명 계산, 크로스 롤러/앵귤러 콘택트 조합, 끼워맞춤 공차 분석
- **설계 사고 논리**: 관절 출력단이 반경/축/토크 복합 하중을 받으며, 베어링 배치가 수명을 결정
- **주요 제약 조건**: 가공 정밀도, 조립 순서, 유지보수성
- **완료 기준 / 산출물**: 베어링 선정표, 인터페이스 도면, 수명 검증
**3레벨 하위 작업:**
- **P4.2.3.1 입력 정리 및 목표 정량화**: 「베어링 및 출력 인터페이스 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 수립
- **P4.2.3.2 개념 및 상세 설계**: 「베어링 및 출력 인터페이스 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「베어링 수명 계산, 크로스 롤러/앵귤러 콘택트 조합, 끼워맞춤 공차 분석」을 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력합니다.
**4레벨 주요 작업:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 수립하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P4.2.3.3 구현/프로토타입/시제품 제작**: 설계에 따라 「베어링 및 출력 인터페이스 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P4.2.3.4 검증 및 문제 폐쇄**: 「베어링 및 출력 인터페이스 설계」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료될 때까지 추적합니다.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P4.2.3.5 문서 출력 및 하위 인도**: 「베어링 및 출력 인터페이스 설계」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 드라이버 및 센서 통합

##### 모터 드라이버 설계/선정
- **방법 / 도구**: FOC 드라이버, SiC/GaN 설계, 피크/연속 전류, 열 설계
- **설계 사고 논리**: 관절 내부에 드라이버를 통합하면 케이블을 단축하고 EMI를 낮출 수 있음; 방열 고려 필요
- **주요 제약 조건**: 공간, 방열, EMI, 기능 안전
- **완료 기준 / 산출물**: 드라이버 규격, 전기 회로도, 열 시뮬레이션/테스트
**3레벨 하위 작업:**
- **P4.3.1.1 입력 정리 및 목표 정량화**: 「모터 드라이버 설계/선정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 수립
- **P4.3.1.2 후보 설계 수립 및 평가**: 「모터 드라이버 설계/선정」에 대한 후보 설계 라이브러리를 구축하고, 「FOC 드라이버, SiC/GaN 설계, 피크/연속 전류, 열 설계」를 사용하여 정량적으로 평가하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 설계를 결정합니다.
**4레벨 주요 작업:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 수립하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P4.3.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「모터 드라이버 설계/선정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P4.3.1.4 검증 및 문제 폐쇄**: 「모터 드라이버 설계/선정」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료될 때까지 추적합니다.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P4.3.1.5 문서 출력 및 하위 인도**: 「모터 드라이버 설계/선정」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 위치/토크 센서 설계
- **방법 / 도구**: 절대/증분 엔코더, 자기/광학 엔코더, 토크 센서, 이중 엔코더 설계
- **설계 사고 논리**: 이중 엔코더가 제어 정밀도를 향상; 토크 센서가 순응 제어를 구현
- **주요 제약 조건**: 비용, 정밀도, 오일/진동 저항, 배선
- **완료 기준 / 산출물**: 센서 설계, 정밀도 예산, 설치 도면
**3레벨 하위 작업:**
- **P4.3.2.1 입력 정리 및 목표 정량화**: 「위치/토크 센서 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
**4레벨 주요 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 담당자, 시간 노드 및 위험 등록을 수립
- **P4.3.2.2 설계/방법 설계**: 「위치/토크 센서 설계」에 대한 구현 방법 또는 후보 설계를 수립하고, 「절대/증분 엔코더, 자기/광학 엔코더, 토크 센서, 이중 엔코더 설계」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 주요 작업:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 수립하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P4.3.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「위치/토크 센서 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 주요 작업:**
1. 모델/시제품을 구축하고 주요 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 수행
3. 이상 및 편차를 기록
- **P4.3.2.4 검증 및 문제 폐쇄**: 「위치/토크 센서 설계」 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료될 때까지 추적합니다.
**4레벨 주요 작업:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 수행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P4.3.2.5 문서 출력 및 하위 인도**: 「위치/토크 센서 설계」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 주요 작업:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지
