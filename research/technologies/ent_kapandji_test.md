---
$id: ent_kapandji_test
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: benchmark
names:
  en: Kapandji Test
  zh: Kapandji测试
  ko: Kapandji 테스트
summary:
  en: A clinical test of thumb opposability and digital dexterity, adapted in robotics to evaluate thumb range of motion and
    opposition quality in dexterous robot hands.
  zh: 一种临床拇指对掌能力和手指灵活性测试，在机器人学中被改编用于评估灵巧机器人手的拇指活动范围和对掌质量。
  ko: 임상적으로 엄지 대립 능력과 손가락 재주를 측정하는 테스트로, 로봇공학에서 능숙한 로봇 손의 엄지 가동 범위와 대립 품질을 평가하기 위해 채택되었습니다.
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
- kapandji
- thumb
- opposition
- benchmark
- dexterous_hand
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard clinical test referenced in the RUKA paper for thumb opposability evaluation. Body backfilled from entity
    metadata by scripts/backfill_critical_entities.py.
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
一种临床拇指对掌能力和手指灵活性测试，在机器人学中被改编用于评估灵巧机器人手的拇指活动范围和对掌质量。

## 核心内容
### Kapandji测试的定义与定位
Kapandji测试属于 **评测基准** 类型。 所属领域包括：评测基准, 设计工程。 价值链层级：验证与市场层, midstream。 一种临床拇指对掌能力和手指灵活性测试，在机器人学中被改编用于评估灵巧机器人手的拇指活动范围和对掌质量。 英文名称为 *Kapandji Test*。 韩文名称为 *Kapandji 테스트*。

### Kapandji测试的任务设置与数据构成
Kapandji测试通过标准化的任务或数据格式，为不同方法提供可比较的评估基础。理解其覆盖范围与标注方式，有助于正确解读实验结果。
数据或任务的多样性、真实性与可扩展性，是衡量其价值的重要维度。

### 使用方法与评价指标
使用该benchmark时，应关注基线方法、评估协议、误差来源以及结果的可复现性，以避免片面或误导性的结论。
同时，需要注意训练集与测试集的划分、分布外泛化能力以及仿真到真实的迁移差距。

### 典型结果与研究价值
Kapandji测试为学术界与工业界提供了统一的比较基准，推动了相关算法的快速发展。
通过分析排行榜结果与失败案例，可以识别当前方法的优势与短板，指导后续研究方向。

### 相关标签
- kapandji
- thumb
- opposition
- benchmark
- dexterous_hand

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键评测基准之一，Kapandji测试在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [RUKA: Rethinking the Design of Humanoid Hands with Learning](https://arxiv.org/abs/2504.13165)


