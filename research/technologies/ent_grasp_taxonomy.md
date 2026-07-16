---
$id: ent_grasp_taxonomy
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: standard
names:
  en: GRASP Taxonomy
  zh: GRASP抓取分类法
  ko: GRASP 분류법
summary:
  en: A standardized classification system for human and robot hand grasps, used to evaluate grasp diversity and coverage
    in dexterous manipulation research.
  zh: 一种用于人类和机器人手部抓取的标准化分类系统，用于评估灵巧操作研究中的抓取多样性和覆盖范围。
  ko: 인간 및 로봇 손의 그립을 분류하는 표준화된 체계로, 능숙한 조작 연구에서 그립 다양성과 커버리지를 평가하는 데 사용됩니다.
domains:
- 10_evaluation_benchmarks
- 06_design_engineering
layers:
- validation_markets
- midstream
functional_roles:
- knowledge
- policy
tags:
- grasp
- taxonomy
- benchmark
- dexterous_manipulation
- hand
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Well-known grasp taxonomy referenced in the RUKA paper for evaluation. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
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
一种用于人类和机器人手部抓取的标准化分类系统，用于评估灵巧操作研究中的抓取多样性和覆盖范围。

## 核心内容
### GRASP抓取分类法的定义与定位
GRASP抓取分类法属于 **标准** 类型。 所属领域包括：评测基准, 设计工程。 价值链层级：验证与市场层, midstream。 一种用于人类和机器人手部抓取的标准化分类系统，用于评估灵巧操作研究中的抓取多样性和覆盖范围。 英文名称为 *GRASP Taxonomy*。 韩文名称为 *GRASP 분류법*。

### GRASP抓取分类法的关键维度
理解GRASP抓取分类法需要从定义、边界条件、相关实体以及典型应用场景等多个维度展开，以形成系统性的认知。
该实体在人形机器人知识图谱中起到连接基础理论与工程实践的桥梁作用。

### 实践意义
在人形机器人产业化的背景下，GRASP抓取分类法对于技术研究、产品开发、投资决策与生态建设均具有参考价值。
准确把握其内涵与外延，有助于避免概念混淆并推动跨学科协作。

### 研究与发展方向
随着人形机器人技术不断演进，GRASP抓取分类法的相关理论与实践也将持续更新，需要保持跟踪与审校。

### 相关标签
- grasp
- taxonomy
- benchmark
- dexterous_manipulation
- hand

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键标准之一，GRASP抓取分类法在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [RUKA: Rethinking the Design of Humanoid Hands with Learning](https://arxiv.org/abs/2504.13165)


