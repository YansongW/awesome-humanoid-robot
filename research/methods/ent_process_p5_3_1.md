---
$id: ent_process_p5_3_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Wiring design of cable and pipe
  zh: 线缆与管路布线设计
  ko: 线缆与管路布线设计
summary:
  en: '“Wiring design code”: Cable model, fixed point, bending radius, trend'
  zh: '- P5.3.1.1 输入梳理与目标量化 - 整理「线缆与管路布线设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 《布线设计规范》：线缆型号、固定点、弯曲半径、走向
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
- method
---


## 概述
**所属阶段/工作包**：本体结构工程与原型（Mechanical Structure）

## 核心内容
**方法 / 工具**：3D 线束布线、弯曲半径校核、固定点设计

**设计思考逻辑**：动力/信号/冷却管路随关节运动不拉扯、不磨损；预留维护长度

**关键约束**：弯曲寿命、EMC 屏蔽、散热、可更换性

**完成标准 / 输出物**：《布线设计规范》：线缆型号、固定点、弯曲半径、走向

**三级子任务与四级关键动作：**

- P5.3.1.1 输入梳理与目标量化
  - 整理「线缆与管路布线设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P5.3.1.2 概念与详细设计
  - 完成「线缆与管路布线设计」的概念设计、详细设计与接口定义，使用「3D 线束布线、弯曲半径校核、固定点设计」验证可行性，输出图纸/算法/逻辑框架。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P5.3.1.3 实施/原型/样件制作
  - 根据设计方案执行「线缆与管路布线设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P5.3.1.4 验证与问题闭环
  - 对「线缆与管路布线设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P5.3.1.5 文档输出与下游交付
  - 输出「线缆与管路布线设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）



