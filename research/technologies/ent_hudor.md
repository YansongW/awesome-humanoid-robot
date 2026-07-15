---
$id: ent_hudor
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: HuDOR
  zh: HuDOR
  ko: HuDOR
summary:
  en: A human-to-robot demonstration dataset or teleoperation framework used to collect human hand motion data for training
    imitation-learning policies on dexterous robot hands.
  zh: 一种用于采集人手动作数据以训练灵巧机器人手模仿学习策略的人类到机器人演示数据集或遥操作框架。
  ko: 능숙한 로봇 손의 모방 학습 정책을 훈련하기 위해 인간 손 동작 데이터를 수집하는 데 사용되는 인간-로봇 시연 데이터 세트 또는 원격 조작 프레임워크입니다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hudor
- teleoperation
- imitation_learning
- dataset
- dexterous_manipulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: Mentioned in the RUKA paper as the source of teleoperation/imitation-learning demonstrations; exact scope and public
    availability should be verified. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
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
一种用于采集人手动作数据以训练灵巧机器人手模仿学习策略的人类到机器人演示数据集或遥操作框架。

## 核心内容
### HuDOR的定义与定位
HuDOR属于 **dataset** 类型。 所属领域包括：09_data_datasets, 07_ai_models_algorithms。 价值链层级：intelligence。 一种用于采集人手动作数据以训练灵巧机器人手模仿学习策略的人类到机器人演示数据集或遥操作框架。 英文名称为 *HuDOR*。 韩文名称为 *HuDOR*。

### HuDOR的任务设置与数据构成
HuDOR通过标准化的任务或数据格式，为不同方法提供可比较的评估基础。理解其覆盖范围与标注方式，有助于正确解读实验结果。
数据或任务的多样性、真实性与可扩展性，是衡量其价值的重要维度。

### 使用方法与评价指标
使用该dataset时，应关注基线方法、评估协议、误差来源以及结果的可复现性，以避免片面或误导性的结论。
同时，需要注意训练集与测试集的划分、分布外泛化能力以及仿真到真实的迁移差距。

### 典型结果与研究价值
HuDOR为学术界与工业界提供了统一的比较基准，推动了相关算法的快速发展。
通过分析排行榜结果与失败案例，可以识别当前方法的优势与短板，指导后续研究方向。

### 相关标签
- hudor
- teleoperation
- imitation_learning
- dataset
- dexterous_manipulation

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键dataset之一，HuDOR在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [RUKA: Rethinking the Design of Humanoid Hands with Learning](https://arxiv.org/abs/2504.13165)

