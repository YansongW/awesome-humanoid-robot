---
$id: ent_process_p4_3_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: ''
  zh: 位置/力矩传感器方案
  ko: 位置/力矩传感器方案
summary:
  en: ''
  zh: 传感器方案、精度预算、安装图纸
  ko: 传感器方案、精度预算、安装图纸
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
  reviewed_at: '2026-06-27'
  confidence: high
  notes: Derived from docs/humanoid_full_development_workflow_v3.md
sources:
- id: wbs_v3_report
  type: report
  title: 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）
  date: '2026-06-27'
theoretical_depth:
- method
---



**所属阶段/工作包**：关节模组与驱动系统设计（Actuator & Drive）

**方法 / 工具**：绝对/增量编码器、磁编/光编、力矩传感器、双编码器方案

**设计思考逻辑**：双编码器提升控制精度；力矩传感器实现柔顺控制

**关键约束**：成本、精度、抗油污振动、布线

**完成标准 / 输出物**：传感器方案、精度预算、安装图纸

**三级子任务与四级关键动作：**

- P4.3.2.1 输入梳理与目标量化
  - 整理「位置/力矩传感器方案」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P4.3.2.2 方案/方法设计
  - 针对「位置/力矩传感器方案」制定实施方法或候选方案，使用「绝对/增量编码器、磁编/光编、力矩传感器、双编码器方案」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P4.3.2.3 实施/原型/样件制作
  - 根据设计方案执行「位置/力矩传感器方案」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P4.3.2.4 验证与问题闭环
  - 对「位置/力矩传感器方案」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P4.3.2.5 文档输出与下游交付
  - 输出「位置/力矩传感器方案」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方
