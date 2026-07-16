---
$id: ent_dataset_rh20t_manipulation_dataset_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: RH20T Manipulation Dataset
  zh: RH20T 操作数据集
  ko: RH20T 조작 데이터셋
summary:
  en: ~110k contact-rich manipulation sequences with visual, force, audio, and human-demo pairs.
  zh: 约11万条接触丰富的操作序列，包含视觉、力觉、音频和人类演示对。
  ko: 시각, 힘, 오디오 및 인간 시연 쌍이 포함된 약 11만 개의 접촉이 풍부한 조작 시퀀스.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- contact_rich
- dataset
- manipulation
- rh20t
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
  title: RH20T Manipulation Dataset
  url: https://rh20t.github.io/
  date: '2023'
  accessed_at: '2026-07-02'
---

## 概述
约11万条接触丰富的操作序列，包含视觉、力觉、音频和人类演示对。

## 核心内容
### RH20T 操作数据集的定义与定位
RH20T 操作数据集属于 **数据集** 类型。 所属领域包括：数据与数据集, AI 模型与算法。 价值链层级：智能层。 约11万条接触丰富的操作序列，包含视觉、力觉、音频和人类演示对。 英文名称为 *RH20T Manipulation Dataset*。 韩文名称为 *RH20T 조작 데이터셋*。

### RH20T 操作数据集的任务设置与数据构成
RH20T 操作数据集通过标准化的任务或数据格式，为不同方法提供可比较的评估基础。理解其覆盖范围与标注方式，有助于正确解读实验结果。
数据或任务的多样性、真实性与可扩展性，是衡量其价值的重要维度。

### 使用方法与评价指标
使用该dataset时，应关注基线方法、评估协议、误差来源以及结果的可复现性，以避免片面或误导性的结论。
同时，需要注意训练集与测试集的划分、分布外泛化能力以及仿真到真实的迁移差距。

### 典型结果与研究价值
RH20T 操作数据集为学术界与工业界提供了统一的比较基准，推动了相关算法的快速发展。
通过分析排行榜结果与失败案例，可以识别当前方法的优势与短板，指导后续研究方向。

### 相关标签
- contact_rich
- dataset
- manipulation
- rh20t

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键数据集之一，RH20T 操作数据集在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [RH20T Manipulation Dataset](https://rh20t.github.io/)


