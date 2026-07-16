---
$id: ent_dataset_amass_motion_dataset_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: AMASS Motion Dataset
  zh: AMASS 动作数据集
  ko: AMASS 모션 데이터셋
summary:
  en: Large-scale clean motion-capture dataset of human body shapes and poses, widely used for humanoid sim pre-training.
  zh: 大规模干净的动作捕捉数据集，包含人体形状和姿态，广泛用于人形机器人仿真预训练。
  ko: 인체 형태와 자세를 포함한 대규모 클린 모션 캡처 데이터셋, 휨로봇 시뮬레이션 사전 학습에 널리 사용.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- amass
- dataset
- human_motion
- motion_capture
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
  title: AMASS Motion Dataset
  url: https://amass.is.tue.mpg.de/
  date: '2019'
  accessed_at: '2026-07-02'
---

## 概述
大规模干净的动作捕捉数据集，包含人体形状和姿态，广泛用于人形机器人仿真预训练。

## 核心内容
### AMASS 动作数据集的定义与定位
AMASS 动作数据集属于 **数据集** 类型。 所属领域包括：数据与数据集, AI 模型与算法。 价值链层级：智能层。 大规模干净的动作捕捉数据集，包含人体形状和姿态，广泛用于人形机器人仿真预训练。 英文名称为 *AMASS Motion Dataset*。 韩文名称为 *AMASS 모션 데이터셋*。

### AMASS 动作数据集的任务设置与数据构成
AMASS 动作数据集通过标准化的任务或数据格式，为不同方法提供可比较的评估基础。理解其覆盖范围与标注方式，有助于正确解读实验结果。
数据或任务的多样性、真实性与可扩展性，是衡量其价值的重要维度。

### 使用方法与评价指标
使用该dataset时，应关注基线方法、评估协议、误差来源以及结果的可复现性，以避免片面或误导性的结论。
同时，需要注意训练集与测试集的划分、分布外泛化能力以及仿真到真实的迁移差距。

### 典型结果与研究价值
AMASS 动作数据集为学术界与工业界提供了统一的比较基准，推动了相关算法的快速发展。
通过分析排行榜结果与失败案例，可以识别当前方法的优势与短板，指导后续研究方向。

### 相关标签
- amass
- dataset
- human_motion
- motion_capture

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键数据集之一，AMASS 动作数据集在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [AMASS Motion Dataset](https://amass.is.tue.mpg.de/)


