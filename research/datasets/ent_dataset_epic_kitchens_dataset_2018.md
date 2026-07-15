---
$id: ent_dataset_epic_kitchens_dataset_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: Epic-Kitchens Dataset
  zh: Epic-Kitchens 数据集
  ko: Epic-Kitchens 데이터셋
summary:
  en: Egocentric kitchen-interaction video dataset widely used for manipulation and activity understanding.
  zh: '核心内容 ### Epic-Kitchens 数据集的定义与定位 Epic-Kitchens 数据集属于 **dataset** 类型。 所属领域包括：09_data_datasets, 07_ai_models_algorithms。
    价值链层级：intelligence。 第一视角厨房交互视频数据集，广泛用于操作与活动理解。 英文名称为 *Epic-Kitchens Dataset*。 韩文名称为 *Epic-Kitchens 데이터셋*。'
  ko: 조작 및 활동 이해에 널리 사용되는 자아중심 주방 상호작용 비디오 데이터셋.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dataset
- egocentric
- epic_kitchens
- kitchen
- video
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-02'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: Epic-Kitchens Dataset
  url: https://epic-kitchens.github.io/
  date: '2018'
  accessed_at: '2026-07-02'
---

## 概述
第一视角厨房交互视频数据集，广泛用于操作与活动理解。

## 核心内容
### Epic-Kitchens 数据集的定义与定位
Epic-Kitchens 数据集属于 **dataset** 类型。 所属领域包括：09_data_datasets, 07_ai_models_algorithms。 价值链层级：intelligence。 第一视角厨房交互视频数据集，广泛用于操作与活动理解。 英文名称为 *Epic-Kitchens Dataset*。 韩文名称为 *Epic-Kitchens 데이터셋*。

### Epic-Kitchens 数据集的任务设置与数据构成
Epic-Kitchens 数据集通过标准化的任务或数据格式，为不同方法提供可比较的评估基础。理解其覆盖范围与标注方式，有助于正确解读实验结果。
数据或任务的多样性、真实性与可扩展性，是衡量其价值的重要维度。

### 使用方法与评价指标
使用该dataset时，应关注基线方法、评估协议、误差来源以及结果的可复现性，以避免片面或误导性的结论。
同时，需要注意训练集与测试集的划分、分布外泛化能力以及仿真到真实的迁移差距。

### 典型结果与研究价值
Epic-Kitchens 数据集为学术界与工业界提供了统一的比较基准，推动了相关算法的快速发展。
通过分析排行榜结果与失败案例，可以识别当前方法的优势与短板，指导后续研究方向。

### 相关标签
- dataset
- egocentric
- epic_kitchens
- kitchen
- video

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键dataset之一，Epic-Kitchens 数据集在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Epic-Kitchens Dataset](https://epic-kitchens.github.io/)


