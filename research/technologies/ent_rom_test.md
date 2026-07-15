---
$id: ent_rom_test
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: benchmark
names:
  en: Range of Motion Test
  zh: 活动范围测试
  ko: 가동 범위 테스트
summary:
  en: A benchmark that measures the reachable joint angles of a robot hand or limb, used to evaluate workspace coverage and
    joint flexibility.
  zh: 一种测量机器人手或肢体可达关节角度的基准，用于评估工作空间覆盖范围和关节灵活性。
  ko: 로봇 손이나 사지의 도달 가능한 관절 각도를 측정하여 작업 공간 커버리지와 관절 유연성을 평가하는 벤치마크입니다.
domains:
- 10_evaluation_benchmarks
- 06_design_engineering
layers:
- validation_markets
- midstream
functional_roles:
- knowledge
- tool_equipment
tags:
- rom
- range_of_motion
- benchmark
- workspace
- dexterous_hand
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard benchmark referenced in the RUKA paper for joint reachability evaluation. Body backfilled from entity metadata
    by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
一种测量机器人手或肢体可达关节角度的基准，用于评估工作空间覆盖范围和关节灵活性。

## 核心内容
### 活动范围测试的定义与定位
活动范围测试属于 **benchmark** 类型。 所属领域包括：10_evaluation_benchmarks, 06_design_engineering。 价值链层级：validation_markets, midstream。 一种测量机器人手或肢体可达关节角度的基准，用于评估工作空间覆盖范围和关节灵活性。 英文名称为 *Range of Motion Test*。 韩文名称为 *가동 범위 테스트*。

### 活动范围测试的任务设置与数据构成
活动范围测试通过标准化的任务或数据格式，为不同方法提供可比较的评估基础。理解其覆盖范围与标注方式，有助于正确解读实验结果。
数据或任务的多样性、真实性与可扩展性，是衡量其价值的重要维度。

### 使用方法与评价指标
使用该benchmark时，应关注基线方法、评估协议、误差来源以及结果的可复现性，以避免片面或误导性的结论。
同时，需要注意训练集与测试集的划分、分布外泛化能力以及仿真到真实的迁移差距。

### 典型结果与研究价值
活动范围测试为学术界与工业界提供了统一的比较基准，推动了相关算法的快速发展。
通过分析排行榜结果与失败案例，可以识别当前方法的优势与短板，指导后续研究方向。

### 相关标签
- rom
- range_of_motion
- benchmark
- workspace
- dexterous_hand

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键benchmark之一，活动范围测试在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [RUKA: Rethinking the Design of Humanoid Hands with Learning](https://arxiv.org/abs/2504.13165)

