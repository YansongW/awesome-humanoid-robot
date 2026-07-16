---
$id: ent_process_p3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: System Architecture and Electromechanical Master Design (System / Preliminary Design)
  zh: 系统架构与机电总体设计（System / Preliminary Design）
  ko: 系统架构与机电总体设计（System / Preliminary Design）
summary:
  en: System Architecture and Electromechanical Design (System / Preliminary Design) —— Phase 3 of the humanoid robot product
    development process, covering solution design, implementation verification, and documentation delivery.
  zh: 系统架构与机电总体设计（System / Preliminary Design）是人形机器人产品开发全流程中的第 3 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 系统架构与机电总体设计（System / Preliminary Design）
domains:
- 06_design_engineering
- 02_components
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
系统架构与机电总体设计（System / Preliminary Design）是人形机器人产品开发全流程中的第 3 个阶段，在 WBS V3 中展开为若干三级子任务。

该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 机械总体设计

##### DOF 配置与关节布局
- **方法 / 工具**：仿生分析、任务驱动 DOF 分析、冗余度评估
- **设计思考逻辑**：腿部 6×2、手臂 7×2、躯干 1–3、头部 2–3、手部 11–22；在满足任务前提下减少复杂度和重量
- **关键约束**：重量、成本、控制实时性、线束数量
- **完成标准 / 输出物**：DOF 配置表、关节运动范围、关节速度/扭矩需求 v1
**三级子任务：**
- **P3.1.1.1 输入梳理与目标量化**：整理「DOF 配置与关节布局」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.1.1.2 方案/方法设计**：针对「DOF 配置与关节布局」制定实施方法或候选方案，使用「仿生分析、任务驱动 DOF 分析、冗余度评估」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.1.1.3 实施/原型/样件制作**：根据设计方案执行「DOF 配置与关节布局」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.1.1.4 验证与问题闭环**：对「DOF 配置与关节布局」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P3.1.1.5 文档输出与下游交付**：输出「DOF 配置与关节布局」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 整机质量属性预算
- **方法 / 工具**：自顶向下质量分配、 bottoms-up 核算、CoM 与惯量追踪
- **设计思考逻辑**：质量和惯量直接影响能耗、动态响应与稳定性；需在早期锁定
- **关键约束**：总重目标、电池能量密度、结构材料
- **完成标准 / 输出物**：《质量预算表》、整机 CoM 范围、主惯量上限
**三级子任务：**
- **P3.1.2.1 输入梳理与目标量化**：整理「整机质量属性预算」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.1.2.2 方案/方法设计**：针对「整机质量属性预算」制定实施方法或候选方案，使用「自顶向下质量分配、 bottoms-up 核算、CoM 与惯量追踪」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.1.2.3 实施/原型/样件制作**：根据设计方案执行「整机质量属性预算」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.1.2.4 验证与问题闭环**：对「整机质量属性预算」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P3.1.2.5 文档输出与下游交付**：输出「整机质量属性预算」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 运动学与动力学初步分析
- **方法 / 工具**：解析法、Matlab/Python、Pinocchio/RBDL、典型动作仿真
- **设计思考逻辑**：估算站立、蹲起、行走、抓取时各关节峰值扭矩和速度
- **关键约束**：载荷假设保守性、接触模型简化
- **完成标准 / 输出物**：关节需求规格 v1、峰值/连续扭矩表、关键动作反力
**三级子任务：**
- **P3.1.3.1 输入梳理与目标量化**：整理「运动学与动力学初步分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.1.3.2 方案/方法设计**：针对「运动学与动力学初步分析」制定实施方法或候选方案，使用「解析法、Matlab/Python、Pinocchio/RBDL、典型动作仿真」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.1.3.3 建模/仿真与样机实现**：建立「运动学与动力学初步分析」的仿真/数学模型或原型样机，使用「解析法、Matlab/Python、Pinocchio/RBDL、典型动作仿真」执行计算或实验，记录关键参数与边界条件。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.1.3.4 仿真结果校核与优化**：校核「运动学与动力学初步分析」仿真结果与理论/试验数据的一致性，识别薄弱点并迭代优化。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.1.3.5 文档输出与下游交付**：输出「运动学与动力学初步分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 结构拓扑与传力路径设计
- **方法 / 工具**：拓扑优化、受力路径草图、模块化划分
- **设计思考逻辑**：采用中心骨架 + 可拆卸四肢模块，便于装配、维护与升级
- **关键约束**：刚度、强度、重量、可维护性
- **完成标准 / 输出物**：结构拓扑方案、传力路径图、模块接口定义
**三级子任务：**
- **P3.1.4.1 输入梳理与目标量化**：整理「结构拓扑与传力路径设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.1.4.2 概念与详细设计**：完成「结构拓扑与传力路径设计」的概念设计、详细设计与接口定义，使用「拓扑优化、受力路径草图、模块化划分」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.1.4.3 实施/原型/样件制作**：根据设计方案执行「结构拓扑与传力路径设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.1.4.4 验证与问题闭环**：对「结构拓扑与传力路径设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P3.1.4.5 文档输出与下游交付**：输出「结构拓扑与传力路径设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 电气与计算架构

##### 计算架构与节点分布
- **方法 / 工具**：算力需求估算、集中式 vs 分布式对比、安全分区
- **设计思考逻辑**：AI 任务（GPU）、实时控制（MCU/FPGA）、安全监控分离，降低互相干扰
- **关键约束**：功耗、散热、重量、实时性
- **完成标准 / 输出物**：计算架构图、各节点算力/功耗预算、通信接口
**三级子任务：**
- **P3.2.1.1 输入梳理与目标量化**：整理「计算架构与节点分布」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.2.1.2 方案/方法设计**：针对「计算架构与节点分布」制定实施方法或候选方案，使用「算力需求估算、集中式 vs 分布式对比、安全分区」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.2.1.3 实施/原型/样件制作**：根据设计方案执行「计算架构与节点分布」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.2.1.4 验证与问题闭环**：对「计算架构与节点分布」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P3.2.1.5 文档输出与下游交付**：输出「计算架构与节点分布」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 通信网络架构
- **方法 / 工具**：CAN-FD / EtherCAT / Ethernet / TSN 带宽与时延分析
- **设计思考逻辑**：关节控制需要高实时性，视觉/AI 需要高带宽；必要时双总线
- **关键约束**：线缆数量、EMC、成本、可扩展性
- **完成标准 / 输出物**：通信拓扑图、协议分配表、带宽/延迟预算
**三级子任务：**
- **P3.2.2.1 输入梳理与目标量化**：整理「通信网络架构」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.2.2.2 方案/方法设计**：针对「通信网络架构」制定实施方法或候选方案，使用「CAN-FD / EtherCAT / Ethernet / TSN 带宽与时延分析」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.2.2.3 实施/原型/样件制作**：根据设计方案执行「通信网络架构」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.2.2.4 验证与问题闭环**：对「通信网络架构」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P3.2.2.5 文档输出与下游交付**：输出「通信网络架构」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 电源架构初步设计
- **方法 / 工具**：母线电压选择、功率流分析、安全分区
- **设计思考逻辑**：电机母线（48 V/60 V/72 V）与逻辑电源隔离；故障时安全断电
- **关键约束**：压降、效率、EMI、安全标准
- **完成标准 / 输出物**：电源架构图、母线电压选择理由、功率预算 v1
**三级子任务：**
- **P3.2.3.1 输入梳理与目标量化**：整理「电源架构初步设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.2.3.2 概念与详细设计**：完成「电源架构初步设计」的概念设计、详细设计与接口定义，使用「母线电压选择、功率流分析、安全分区」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.2.3.3 实施/原型/样件制作**：根据设计方案执行「电源架构初步设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.2.3.4 验证与问题闭环**：对「电源架构初步设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P3.2.3.5 文档输出与下游交付**：输出「电源架构初步设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 安全与可靠性架构

##### 功能安全概念设计
- **方法 / 工具**：HARA、STPA、安全目标分解、冗余策略
- **设计思考逻辑**：识别与人接触、跌倒、夹持、电气相关的危害，定义安全功能
- **关键约束**：SIL/PL 等级、成本、复杂度
- **完成标准 / 输出物**：安全概念文档、安全目标、功能安全架构
**三级子任务：**
- **P3.3.1.1 输入梳理与目标量化**：整理「功能安全概念设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.3.1.2 概念与详细设计**：完成「功能安全概念设计」的概念设计、详细设计与接口定义，使用「HARA、STPA、安全目标分解、冗余策略」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.3.1.3 实施/原型/样件制作**：根据设计方案执行「功能安全概念设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.3.1.4 验证与问题闭环**：对「功能安全概念设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P3.3.1.5 文档输出与下游交付**：输出「功能安全概念设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 可靠性目标与分配
- **方法 / 工具**：可靠性框图（RBD）、FMEA、MTBF 分配
- **设计思考逻辑**：整机可靠性目标分解到关节、电池、计算等关键部件
- **关键约束**：测试时间、加速试验能力、数据有限
- **完成标准 / 输出物**：可靠性目标分配表、关键件 MTBF 目标
**三级子任务：**
- **P3.3.2.1 输入梳理与目标量化**：整理「可靠性目标与分配」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P3.3.2.2 方案/方法设计**：针对「可靠性目标与分配」制定实施方法或候选方案，使用「可靠性框图（RBD）、FMEA、MTBF 分配」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P3.3.2.3 实施/原型/样件制作**：根据设计方案执行「可靠性目标与分配」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P3.3.2.4 验证与问题闭环**：对「可靠性目标与分配」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P3.3.2.5 文档输出与下游交付**：输出「可靠性目标与分配」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 系统辨识与校准

##### 关节零点与传感器标定
- **方法 / 工具**：编码器零点标定、IMU 六位置标定、力/力矩传感器加载标定、标定夹具
- **设计思考逻辑**：传感器读数与实际控制输入的准确性直接决定状态估计与力控精度
- **关键约束**：标定精度、温度漂移、重复性、现场可维护性
- **完成标准 / 输出物**：关节零点误差 < 目标、IMU 偏差 < 目标、力传感器线性度达标
**三级子任务：**
- **P3.4.1.1 输入梳理与目标量化**：整理「关节零点与传感器标定」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P3.4.1.2 方案/方法设计**：针对「关节零点与传感器标定」制定实施方法或候选方案，使用「编码器零点标定、IMU 六位置标定、力/力矩传感器加载标定、标定夹具」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P3.4.1.3 实施/建模/实验**：根据方案执行「关节零点与传感器标定」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P3.4.1.4 验证与优化**：对「关节零点与传感器标定」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P3.4.1.5 文档输出与下游交付**：输出「关节零点与传感器标定」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 手眼标定与外部参数标定
- **方法 / 工具**：相机-机器人标定板、ArUco/AprilTag、Eye-in-Hand/Eye-to-Hand 算法
- **设计思考逻辑**：视觉感知结果必须准确映射到机器人基座或工具坐标系
- **关键约束**：标定板精度、相机畸变、遮挡
- **完成标准 / 输出物**：手眼标定重投影误差 < 目标、外参稳定
**三级子任务：**
- **P3.4.2.1 输入梳理与目标量化**：整理「手眼标定与外部参数标定」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P3.4.2.2 方案/方法设计**：针对「手眼标定与外部参数标定」制定实施方法或候选方案，使用「相机-机器人标定板、ArUco/AprilTag、Eye-in-Hand/Eye-to-Hand 算法」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P3.4.2.3 实施/建模/实验**：根据方案执行「手眼标定与外部参数标定」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P3.4.2.4 验证与优化**：对「手眼标定与外部参数标定」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P3.4.2.5 文档输出与下游交付**：输出「手眼标定与外部参数标定」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 质心/惯量参数辨识
- **方法 / 工具**：摆动实验、悬挂法、力台测量、最小二乘/最大似然辨识
- **设计思考逻辑**：URDF 中的质心与惯量参数需与实物一致，才能进行准确动力学控制
- **关键约束**：激励充分性、测量噪声、参数可辨识性
- **完成标准 / 输出物**：辨识后整机质量/CoM/惯量与实测误差 < 5%
**三级子任务：**
- **P3.4.3.1 输入梳理与目标量化**：整理「质心/惯量参数辨识」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P3.4.3.2 方案/方法设计**：针对「质心/惯量参数辨识」制定实施方法或候选方案，使用「摆动实验、悬挂法、力台测量、最小二乘/最大似然辨识」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P3.4.3.3 实施/建模/实验**：根据方案执行「质心/惯量参数辨识」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P3.4.3.4 验证与优化**：对「质心/惯量参数辨识」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P3.4.3.5 文档输出与下游交付**：输出「质心/惯量参数辨识」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 连杆加工误差与DH参数现场修正
- **方法 / 工具**：三坐标测量/激光跟踪仪、运动学误差模型、DH 参数优化
- **设计思考逻辑**：实际连杆长度、关节轴线偏差会导致末端定位误差，需要现场修正
- **关键约束**：测量设备可达性、修正模型不引入奇异
- **完成标准 / 输出物**：末端定位精度提升 > 30%、DH 修正表发布
**三级子任务：**
- **P3.4.4.1 输入梳理与目标量化**：整理「连杆加工误差与DH参数现场修正」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P3.4.4.2 方案/方法设计**：针对「连杆加工误差与DH参数现场修正」制定实施方法或候选方案，使用「三坐标测量/激光跟踪仪、运动学误差模型、DH 参数优化」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P3.4.4.3 实施/建模/实验**：根据方案执行「连杆加工误差与DH参数现场修正」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P3.4.4.4 验证与优化**：对「连杆加工误差与DH参数现场修正」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P3.4.4.5 文档输出与下游交付**：输出「连杆加工误差与DH参数现场修正」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 动力学参数辨识与URDF更新
- **方法 / 工具**：激励轨迹设计、关节力矩/位置数据采集、摩擦/惯量辨识、URDF 回归
- **设计思考逻辑**：将辨识得到的摩擦、惯量、质心参数反馈更新 URDF，提高仿真与实际控制精度
- **关键约束**：安全激励边界、关节速度/扭矩限制
- **完成标准 / 输出物**：辨识 URDF 与实测扭矩误差 < 目标、版本更新
**三级子任务：**
- **P3.4.5.1 输入梳理与目标量化**：整理「动力学参数辨识与URDF更新」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P3.4.5.2 方案/方法设计**：针对「动力学参数辨识与URDF更新」制定实施方法或候选方案，使用「激励轨迹设计、关节力矩/位置数据采集、摩擦/惯量辨识、URDF 回归」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P3.4.5.3 实施/建模/实验**：根据方案执行「动力学参数辨识与URDF更新」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P3.4.5.4 验证与优化**：对「动力学参数辨识与URDF更新」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P3.4.5.5 文档输出与下游交付**：输出「动力学参数辨识与URDF更新」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
System Architecture and Electromechanical Overall Design (System / Preliminary Design) is the third stage in the full process of humanoid robot product development, expanded into several third-level sub-tasks in WBS V3.

This stage covers complete engineering actions such as input review, scheme design, implementation/prototyping, verification closed-loop, and documentation delivery, serving as a key milestone to ensure downstream dependencies receive qualified inputs.

## Content
### Mechanical Overall Design

##### DOF Configuration and Joint Layout
- **Methods/Tools**: Bionic analysis, task-driven DOF analysis, redundancy assessment
- **Design Rationale**: Legs 6×2, arms 7×2, torso 1–3, head 2–3, hands 11–22; reduce complexity and weight while meeting task requirements
- **Key Constraints**: Weight, cost, real-time control, wiring harness count
- **Completion Criteria/Deliverables**: DOF configuration table, joint range of motion, joint speed/torque requirements v1
**Third-level sub-tasks:**
- **P3.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "DOF Configuration and Joint Layout"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Fourth-level key actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P3.1.1.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "DOF Configuration and Joint Layout"; demonstrate using "bionic analysis, task-driven DOF analysis, redundancy assessment"; clarify technical roadmap and resource requirements.
**Fourth-level key actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P3.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "DOF Configuration and Joint Layout" according to the design scheme; produce prototypes, samples, or complete key steps; record process data.
**Fourth-level key actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P3.1.1.4 Verification and Issue Closure**: Verify outputs of "DOF Configuration and Joint Layout"; check if completion criteria are met; record issues and track until closure.
**Fourth-level key actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P3.1.1.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "DOF Configuration and Joint Layout"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Fourth-level key actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Whole-Machine Mass Property Budget
- **Methods/Tools**: Top-down mass allocation, bottoms-up calculation, CoM and inertia tracking
- **Design Rationale**: Mass and inertia directly affect energy consumption, dynamic response, and stability; must be locked in early
- **Key Constraints**: Total weight target, battery energy density, structural materials
- **Completion Criteria/Deliverables**: "Mass Budget Table", whole-machine CoM range, principal inertia upper limit
**Third-level sub-tasks:**
- **P3.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Whole-Machine Mass Property Budget"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Fourth-level key actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P3.1.2.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Whole-Machine Mass Property Budget"; demonstrate using "top-down mass allocation, bottoms-up calculation, CoM and inertia tracking"; clarify technical roadmap and resource requirements.
**Fourth-level key actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P3.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Whole-Machine Mass Property Budget" according to the design scheme; produce prototypes, samples, or complete key steps; record process data.
**Fourth-level key actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P3.1.2.4 Verification and Issue Closure**: Verify outputs of "Whole-Machine Mass Property Budget"; check if completion criteria are met; record issues and track until closure.
**Fourth-level key actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P3.1.2.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Whole-Machine Mass Property Budget"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Fourth-level key actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Preliminary Kinematics and Dynamics Analysis
- **Methods/Tools**: Analytical methods, Matlab/Python, Pinocchio/RBDL, typical motion simulation
- **Design Rationale**: Estimate peak torque and speed for each joint during standing, squatting, walking, and grasping
- **Key Constraints**: Conservative load assumptions, simplified contact models
- **Completion Criteria/Deliverables**: Joint requirement specification v1, peak/continuous torque table, reaction forces for key motions
**Third-level sub-tasks:**
- **P3.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Preliminary Kinematics and Dynamics Analysis"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Fourth-level key actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P3.1.3.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Preliminary Kinematics and Dynamics Analysis"; demonstrate using "analytical methods, Matlab/Python, Pinocchio/RBDL, typical motion simulation"; clarify technical roadmap and resource requirements.
**Fourth-level key actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P3.1.3.3 Modeling/Simulation and Prototype Implementation**: Establish simulation/mathematical models or prototype samples for "Preliminary Kinematics and Dynamics Analysis"; perform calculations or experiments using "analytical methods, Matlab/Python, Pinocchio/RBDL, typical motion simulation"; record key parameters and boundary conditions.
**Fourth-level key actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P3.1.3.4 Simulation Result Verification and Optimization**: Verify consistency of simulation results for "Preliminary Kinematics and Dynamics Analysis" with theoretical/experimental data; identify weak points and iterate for optimization.
**Fourth-level key actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P3.1.3.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Preliminary Kinematics and Dynamics Analysis"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Fourth-level key actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Structural Topology and Load Path Design
- **Methods/Tools**: Topology optimization, load path sketching, modular partitioning
- **Design Rationale**: Use central skeleton with detachable limb modules for ease of assembly, maintenance, and upgrade
- **Key Constraints**: Stiffness, strength, weight, maintainability
- **Completion Criteria/Deliverables**: Structural topology scheme, load path diagram, module interface definition
**Third-level sub-tasks:**
- **P3.1.4.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Structural Topology and Load Path Design"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Fourth-level key actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P3.1.4.2 Conceptual and Detailed Design**: Complete conceptual design, detailed design, and interface definition for "Structural Topology and Load Path Design"; verify feasibility using "topology optimization, load path sketching, modular partitioning"; output drawings/algorithms/logical frameworks.
**Fourth-level key actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P3.1.4.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Structural Topology and Load Path Design" according to the design scheme; produce prototypes, samples, or complete key steps; record process data.
**Fourth-level key actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P3.1.4.4 Verification and Issue Closure**: Verify outputs of "Structural Topology and Load Path Design"; check if completion criteria are met; record issues and track until closure.
**Fourth-level key actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P3.1.4.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Structural Topology and Load Path Design"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Fourth-level key actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

#### Electrical and Computing Architecture

##### Computing Architecture and Node Distribution
- **Methods/Tools**: Computational power estimation, centralized vs distributed comparison, safety partitioning
- **Design Rationale**: Separate AI tasks (GPU), real-time control (MCU/FPGA), and safety monitoring to reduce mutual interference
- **Key Constraints**: Power consumption, heat dissipation, weight, real-time performance
- **Completion Criteria/Deliverables**: Computing architecture diagram, node computational power/power budget, communication interfaces
**Third-level sub-tasks:**
- **P3.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Computing Architecture and Node Distribution"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Fourth-level key actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P3.2.1.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Computing Architecture and Node Distribution"; demonstrate using "computational power estimation, centralized vs distributed comparison, safety partitioning"; clarify technical roadmap and resource requirements.
**Fourth-level key actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P3.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Computing Architecture and Node Distribution" according to the design scheme; produce prototypes, samples, or complete key steps; record process data.
**Fourth-level key actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P3.2.1.4 Verification and Issue Closure**: Verify outputs of "Computing Architecture and Node Distribution"; check if completion criteria are met; record issues and track until closure.
**Fourth-level key actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P3.2.1.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Computing Architecture and Node Distribution"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Fourth-level key actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Communication Network Architecture
- **Methods/Tools**: CAN-FD / EtherCAT / Ethernet / TSN bandwidth and latency analysis
- **Design Rationale**: Joint control requires high real-time performance; vision/AI requires high bandwidth; dual bus if necessary
- **Key Constraints**: Cable count, EMC, cost, scalability
- **Completion Criteria/Deliverables**: Communication topology diagram, protocol allocation table, bandwidth/latency budget
**Third-level sub-tasks:**
- **P3.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Communication Network Architecture"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Fourth-level key actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P3.2.2.2 Scheme/Method Design**: Develop implementation methods or candidate schemes for "Communication Network Architecture"; demonstrate using "CAN-FD / EtherCAT / Ethernet / TSN bandwidth and latency analysis"; clarify technical roadmap and resource requirements.
**Fourth-level key actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P3.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Communication Network Architecture" according to the design scheme; produce prototypes, samples, or complete key steps; record process data.
**Fourth-level key actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P3.2.2.4 Verification and Issue Closure**: Verify outputs of "Communication Network Architecture"; check if completion criteria are met; record issues and track until closure.
**Fourth-level key actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P3.2.2.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Communication Network Architecture"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Fourth-level key actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Preliminary Power Architecture Design
- **Methods/Tools**: Bus voltage selection, power flow analysis, safety partitioning
- **Design Rationale**: Isolate motor bus (48 V/60 V/72 V) from logic power; ensure safe power-off during faults
- **Key Constraints**: Voltage drop, efficiency, EMI, safety standards
- **Completion Criteria/Deliverables**: Power architecture diagram, bus voltage selection rationale, power budget v1
**Third-level sub-tasks:**
- **P3.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Preliminary Power Architecture Design"; convert completion criteria into quantifiable acceptance indicators; define Owner and milestones.
**Fourth-level key actions:**
1. List all upstream inputs and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P3.2.3.2 Conceptual and Detailed Design**: Complete conceptual design, detailed design, and interface definition for "Preliminary Power Architecture Design"; verify feasibility using "bus voltage selection, power flow analysis, safety partitioning"; output drawings/algorithms/logical frameworks.
**Fourth-level key actions:**
1. Generate at least 2 candidate schemes
2. Establish evaluation matrix and quantify scoring
3. Organize review and freeze the scheme
- **P3.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Preliminary Power Architecture Design" according to the design scheme; produce prototypes, samples, or complete key steps; record process data.
**Fourth-level key actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P3.2.3.4 Verification and Issue Closure**: Verify outputs of "Preliminary Power Architecture Design"; check if completion criteria are met; record issues and track until closure.
**Fourth-level key actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P3.2.3.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Preliminary Power Architecture Design"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
**Fourth-level key actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

#### Safety and Reliability Architecture

## 개요
시스템 아키텍처 및 기계 전반 설계(System / Preliminary Design)는 휴머노이드 로봇 제품 개발 전 과정 중 3번째 단계로, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.

이 단계는 입력 정리, 설계안 수립, 구현/프로토타입, 검증 폐루프 및 문서 인도 등 완전한 엔지니어링 작업을 포함하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 마일스톤입니다.

## 핵심 하위 작업 및 기술 내용
#### 기계 전반 설계

##### DOF 구성 및 관절 배치
- **방법 / 도구**: 생체 모방 분석, 작업 기반 DOF 분석, 여유도 평가
- **설계 사고 논리**: 다리 6×2, 팔 7×2, 몸통 1–3, 머리 2–3, 손 11–22; 작업 조건을 충족하는 범위 내에서 복잡성과 무게 최소화
- **핵심 제약 조건**: 무게, 비용, 제어 실시간성, 케이블 수량
- **완료 기준 / 산출물**: DOF 구성표, 관절 운동 범위, 관절 속도/토크 요구 사항 v1
**3레벨 하위 작업:**
- **P3.1.1.1 입력 정리 및 목표 정량화**: 「DOF 구성 및 관절 배치」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P3.1.1.2 설계안/방법 설계**: 「DOF 구성 및 관절 배치」에 대한 구현 방법 또는 후보 설계안을 수립하고, 「생체 모방 분석, 작업 기반 DOF 분석, 여유도 평가」를 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 설계안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 설계안 확정
- **P3.1.1.3 구현/프로토타입/시제품 제작**: 설계안에 따라 「DOF 구성 및 관절 배치」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P3.1.1.4 검증 및 문제 폐루프**: 「DOF 구성 및 관절 배치」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P3.1.1.5 문서 출력 및 하위 인도**: 「DOF 구성 및 관절 배치」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서 통보

##### 전기계 질량 속성 예산
- **방법 / 도구**: 하향식 질량 할당, 상향식 계산, CoM 및 관성 추적
- **설계 사고 논리**: 질량과 관성은 에너지 소비, 동적 응답 및 안정성에 직접적인 영향을 미치므로, 초기 단계에서 확정해야 함
- **핵심 제약 조건**: 총 중량 목표, 배터리 에너지 밀도, 구조 재료
- **완료 기준 / 산출물**: 《질량 예산표》, 전기계 CoM 범위, 주 관성 상한
**3레벨 하위 작업:**
- **P3.1.2.1 입력 정리 및 목표 정량화**: 「전기계 질량 속성 예산」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P3.1.2.2 설계안/방법 설계**: 「전기계 질량 속성 예산」에 대한 구현 방법 또는 후보 설계안을 수립하고, 「하향식 질량 할당, 상향식 계산, CoM 및 관성 추적」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 설계안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 설계안 확정
- **P3.1.2.3 구현/프로토타입/시제품 제작**: 설계안에 따라 「전기계 질량 속성 예산」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P3.1.2.4 검증 및 문제 폐루프**: 「전기계 질량 속성 예산」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P3.1.2.5 문서 출력 및 하위 인도**: 「전기계 질량 속성 예산」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서 통보

##### 운동학 및 동역학 예비 분석
- **방법 / 도구**: 해석법, Matlab/Python, Pinocchio/RBDL, 대표 동작 시뮬레이션
- **설계 사고 논리**: 서기, 쪼그려 앉기, 걷기, 잡기 시 각 관절의 피크 토크와 속도 추정
- **핵심 제약 조건**: 하중 가정의 보수성, 접촉 모델 단순화
- **완료 기준 / 산출물**: 관절 요구 사양 v1, 피크/연속 토크 표, 대표 동작 반력
**3레벨 하위 작업:**
- **P3.1.3.1 입력 정리 및 목표 정량화**: 「운동학 및 동역학 예비 분석」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P3.1.3.2 설계안/방법 설계**: 「운동학 및 동역학 예비 분석」에 대한 구현 방법 또는 후보 설계안을 수립하고, 「해석법, Matlab/Python, Pinocchio/RBDL, 대표 동작 시뮬레이션」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 설계안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 설계안 확정
- **P3.1.3.3 모델링/시뮬레이션 및 시제품 구현**: 「운동학 및 동역학 예비 분석」의 시뮬레이션/수학적 모델 또는 프로토타입 시제품을 구축하고, 「해석법, Matlab/Python, Pinocchio/RBDL, 대표 동작 시뮬레이션」을 사용하여 계산 또는 실험을 수행하며, 핵심 파라미터와 경계 조건을 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P3.1.3.4 시뮬레이션 결과 검증 및 최적화**: 「운동학 및 동역학 예비 분석」 시뮬레이션 결과와 이론/실험 데이터의 일관성을 검증하고, 취약점을 식별하여 반복 최적화합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P3.1.3.5 문서 출력 및 하위 인도**: 「운동학 및 동역학 예비 분석」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서 통보

##### 구조 토폴로지 및 하중 전달 경로 설계
- **방법 / 도구**: 토폴로지 최적화, 하중 경로 스케치, 모듈식 분할
- **설계 사고 논리**: 중앙 골격 + 분리 가능한 사지 모듈 채택으로 조립, 유지보수 및 업그레이드 용이
- **핵심 제약 조건**: 강성, 강도, 무게, 유지보수성
- **완료 기준 / 산출물**: 구조 토폴로지 설계안, 하중 전달 경로도, 모듈 인터페이스 정의
**3레벨 하위 작업:**
- **P3.1.4.1 입력 정리 및 목표 정량화**: 「구조 토폴로지 및 하중 전달 경로 설계」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P3.1.4.2 개념 및 상세 설계**: 「구조 토폴로지 및 하중 전달 경로 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「토폴로지 최적화, 하중 경로 스케치, 모듈식 분할」을 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 설계안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 설계안 확정
- **P3.1.4.3 구현/프로토타입/시제품 제작**: 설계안에 따라 「구조 토폴로지 및 하중 전달 경로 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P3.1.4.4 검증 및 문제 폐루프**: 「구조 토폴로지 및 하중 전달 경로 설계」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P3.1.4.5 문서 출력 및 하위 인도**: 「구조 토폴로지 및 하중 전달 경로 설계」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서 통보

#### 전기 및 컴퓨팅 아키텍처

##### 컴퓨팅 아키텍처 및 노드 분포
- **방법 / 도구**: 연산 성능 요구 추정, 집중식 vs 분산식 비교, 안전 구역 분할
- **설계 사고 논리**: AI 작업(GPU), 실시간 제어(MCU/FPGA), 안전 모니터링 분리로 상호 간섭 감소
- **핵심 제약 조건**: 전력 소비, 방열, 무게, 실시간성
- **완료 기준 / 산출물**: 컴퓨팅 아키텍처도, 각 노드 연산 성능/전력 소비 예산, 통신 인터페이스
**3레벨 하위 작업:**
- **P3.2.1.1 입력 정리 및 목표 정량화**: 「컴퓨팅 아키텍처 및 노드 분포」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P3.2.1.2 설계안/방법 설계**: 「컴퓨팅 아키텍처 및 노드 분포」에 대한 구현 방법 또는 후보 설계안을 수립하고, 「연산 성능 요구 추정, 집중식 vs 분산식 비교, 안전 구역 분할」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 설계안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 설계안 확정
- **P3.2.1.3 구현/프로토타입/시제품 제작**: 설계안에 따라 「컴퓨팅 아키텍처 및 노드 분포」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P3.2.1.4 검증 및 문제 폐루프**: 「컴퓨팅 아키텍처 및 노드 분포」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P3.2.1.5 문서 출력 및 하위 인도**: 「컴퓨팅 아키텍처 및 노드 분포」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서 통보

##### 통신 네트워크 아키텍처
- **방법 / 도구**: CAN-FD / EtherCAT / Ethernet / TSN 대역폭 및 지연 분석
- **설계 사고 논리**: 관절 제어는 높은 실시간성 필요, 비전/AI는 높은 대역폭 필요; 필요 시 이중 버스
- **핵심 제약 조건**: 케이블 수량, EMC, 비용, 확장성
- **완료 기준 / 산출물**: 통신 토폴로지도, 프로토콜 할당표, 대역폭/지연 예산
**3레벨 하위 작업:**
- **P3.2.2.1 입력 정리 및 목표 정량화**: 「통신 네트워크 아키텍처」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P3.2.2.2 설계안/방법 설계**: 「통신 네트워크 아키텍처」에 대한 구현 방법 또는 후보 설계안을 수립하고, 「CAN-FD / EtherCAT / Ethernet / TSN 대역폭 및 지연 분석」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 설계안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 설계안 확정
- **P3.2.2.3 구현/프로토타입/시제품 제작**: 설계안에 따라 「통신 네트워크 아키텍처」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P3.2.2.4 검증 및 문제 폐루프**: 「통신 네트워크 아키텍처」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P3.2.2.5 문서 출력 및 하위 인도**: 「통신 네트워크 아키텍처」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서 통보

##### 전원 아키텍처 예비 설계
- **방법 / 도구**: 버스 전압 선택, 전력 흐름 분석, 안전 구역 분할
- **설계 사고 논리**: 모터 버스(48 V/60 V/72 V)와 로직 전원 분리; 고장 시 안전 전원 차단
- **핵심 제약 조건**: 전압 강하, 효율, EMI, 안전 표준
- **완료 기준 / 산출물**: 전원 아키텍처도, 버스 전압 선택 이유, 전력 예산 v1
**3레벨 하위 작업:**
- **P3.2.3.1 입력 정리 및 목표 정량화**: 「전원 아키텍처 예비 설계」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 작업:**
1. 모든 상위 입력 목록을 작성하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부 구축
- **P3.2.3.2 개념 및 상세 설계**: 「전원 아키텍처 예비 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「버스 전압 선택, 전력 흐름 분석, 안전 구역 분할」을 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력합니다.
**4레벨 핵심 작업:**
1. 2개 이상의 후보 설계안 도출
2. 평가 매트릭스 구축 및 정량적 점수화
3. 검토 조직 및 설계안 확정
- **P3.2.3.3 구현/프로토타입/시제품 제작**: 설계안에 따라 「전원 아키텍처 예비 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 작업:**
1. 모델/시제품 구축 및 핵심 파라미터 기록
2. 시뮬레이션 또는 프로토타입 검증 수행
3. 이상 및 편차 기록
- **P3.2.3.4 검증 및 문제 폐루프**: 「전원 아키텍처 예비 설계」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적합니다.
**4레벨 핵심 작업:**
1. 테스트/검토 계획 및 통과 기준 수립
2. 테스트 수행 및 원시 데이터 기록
3. 문제 목록 및 개선 조치 출력
- **P3.2.3.5 문서 출력 및 하위 인도**: 「전원 아키텍처 예비 설계」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 인도를 완료합니다.
**4레벨 핵심 작업:**
1. 템플릿에 따라 문서 작성 및 원시 데이터 인용
2. 내부 검토 및 버전 관리 완료
3. 게시 및 하위 의존 부서 통보

#### 안전 및 신뢰성 아키텍처
