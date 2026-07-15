---
$id: ent_process_p4_2_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Selection of reducer and transmission
  zh: 减速器与传动选型
  ko: 减速器与传动选型
summary:
  en: Reducer specification, chain drawing, stiffness/backlash budget
  zh: '- P4.2.2.1 输入梳理与目标量化 - 整理「减速器与传动选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 减速器规格、传动链图纸、刚度/背隙预算
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
- method
---


## 概述
**所属阶段/工作包**：关节模组与驱动系统设计（Actuator & Drive）

## 核心内容
**方法 / 工具**：谐波、行星、摆线、同步带、丝杠对比；背隙/刚度/寿命测试

**设计思考逻辑**：输出端力矩/位置传感器配置决定控制精度；传动链刚度影响带宽

**关键约束**：谐波柔轮疲劳、行星磨损、噪音、成本

**完成标准 / 输出物**：减速器规格、传动链图纸、刚度/背隙预算

**三级子任务与四级关键动作：**

- P4.2.2.1 输入梳理与目标量化
  - 整理「减速器与传动选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P4.2.2.2 候选方案建立与评估
  - 针对「减速器与传动选型」建立候选方案库，使用「谐波、行星、摆线、同步带、丝杠对比；背隙/刚度/寿命测试」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P4.2.2.3 实施/原型/样件制作
  - 根据设计方案执行「减速器与传动选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P4.2.2.4 验证与问题闭环
  - 对「减速器与传动选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P4.2.2.5 文档输出与下游交付
  - 输出「减速器与传动选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）



