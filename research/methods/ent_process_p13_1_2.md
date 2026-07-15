---
$id: ent_process_p13_1_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: In-house/Third-party PCB Design
  zh: 自研/外购 PCB 设计
  ko: 自研/外购 PCB 设计
summary:
  en: Schematic diagram, PCB layout, bill of materials, DFM report
  zh: '- P13.1.2.1 输入梳理与目标量化 - 整理「自研/外购 PCB 设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 原理图、PCB、BOM、DFM 报告
domains:
- 02_components
- 08_software_middleware
layers:
- intelligence
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
- method
---


## 概述
**所属阶段/工作包**：电子电气与能源系统（Electronics & Power）

## 核心内容
**方法 / 工具**：载板、关节驱动板、传感器接口板、安全监控板

**设计思考逻辑**：将计算、通信、电源、安全功能固化到可靠硬件

**关键约束**：EMC、SI/PI、热、空间、可制造性

**完成标准 / 输出物**：原理图、PCB、BOM、DFM 报告

**三级子任务与四级关键动作：**

- P13.1.2.1 输入梳理与目标量化
  - 整理「自研/外购 PCB 设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P13.1.2.2 概念与详细设计
  - 完成「自研/外购 PCB 设计」的概念设计、详细设计与接口定义，使用「载板、关节驱动板、传感器接口板、安全监控板」验证可行性，输出图纸/算法/逻辑框架。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P13.1.2.3 实施/原型/样件制作
  - 根据设计方案执行「自研/外购 PCB 设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P13.1.2.4 验证与问题闭环
  - 对「自研/外购 PCB 设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P13.1.2.5 文档输出与下游交付
  - 输出「自研/外购 PCB 设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）



