---
$id: ent_process_p13_3_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: ''
  zh: EMC/EMI 设计与测试
  ko: EMC/EMI 设计与测试
summary:
  en: ''
  zh: EMC 设计规范、预测试报告、整改记录
  ko: EMC 设计规范、预测试报告、整改记录
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



**所属阶段/工作包**：电子电气与能源系统（Electronics & Power）

**方法 / 工具**：屏蔽、滤波、接地、PCB 布局、辐射/传导测试

**设计思考逻辑**：大功率电机驱动与高速计算共存，EMC 风险高

**关键约束**：CE/FCC/UL 标准、重量、成本

**完成标准 / 输出物**：EMC 设计规范、预测试报告、整改记录

**三级子任务与四级关键动作：**

- P13.3.2.1 输入梳理与目标量化
  - 整理「EMC/EMI 设计与测试」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P13.3.2.2 概念与详细设计
  - 完成「EMC/EMI 设计与测试」的概念设计、详细设计与接口定义，使用「屏蔽、滤波、接地、PCB 布局、辐射/传导测试」验证可行性，输出图纸/算法/逻辑框架。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P13.3.2.3 实施/原型/样件制作
  - 根据设计方案执行「EMC/EMI 设计与测试」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P13.3.2.4 测试执行与结果分析
  - 按照验收标准执行「EMC/EMI 设计与测试」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P13.3.2.5 文档输出与下游交付
  - 输出「EMC/EMI 设计与测试」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方
