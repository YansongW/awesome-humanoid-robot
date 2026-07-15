---
$id: ent_process_p13_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Computing Platform Architecture and Selection
  zh: 计算平台架构与选型
  ko: 计算平台架构与选型
summary:
  en: Computing architecture diagram, compute power/power consumption budget for each node, security zoning
  zh: '- P13.1.1.1 输入梳理与目标量化 - 整理「计算平台架构与选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 计算架构图、各节点算力/功耗预算、安全分区
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
**方法 / 工具**：Jetson / Intel NUC / 自研载板 / FPGA / MCU 分布

**设计思考逻辑**：AI 任务用 GPU，实时控制用 MCU/FPGA，安全监控独立

**关键约束**：功耗、散热、重量、实时性、功能安全

**完成标准 / 输出物**：计算架构图、各节点算力/功耗预算、安全分区

**三级子任务与四级关键动作：**

- P13.1.1.1 输入梳理与目标量化
  - 整理「计算平台架构与选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P13.1.1.2 候选方案建立与评估
  - 针对「计算平台架构与选型」建立候选方案库，使用「Jetson / Intel NUC / 自研载板 / FPGA / MCU 分布」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P13.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「计算平台架构与选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P13.1.1.4 验证与问题闭环
  - 对「计算平台架构与选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P13.1.1.5 文档输出与下游交付
  - 输出「计算平台架构与选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）



