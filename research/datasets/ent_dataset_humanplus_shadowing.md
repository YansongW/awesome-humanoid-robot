---
$id: ent_dataset_humanplus_shadowing
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: HumanPlus Shadowing Dataset
  zh: HumanPlus Shadowing数据集
  ko: HumanPlus Shadowing 데이터셋
summary:
  en: A dataset collected by shadowing human motion with a humanoid robot, used to train whole-body imitation and teleoperation
    policies.
  zh: 通过人形机器人跟随人体运动采集的数据集，用于训练全身模仿与遥操作策略。
  ko: 휴로봇으로 인간 동작을 따라 촬영하여 수집한 데이터셋으로, 전신 모방 및 원격 조작 정책 학습에 사용.
domains:
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
tags:
- dataset
- chapter_21
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
通过人形机器人跟随人体运动采集的数据集，用于训练全身模仿与遥操作策略。

## 核心内容
### HumanPlus Shadowing数据集的定义与定位
HumanPlus Shadowing数据集属于 **dataset** 类型。 所属领域包括：09_data_datasets。 价值链层级：intelligence。 通过人形机器人跟随人体运动采集的数据集，用于训练全身模仿与遥操作策略。 英文名称为 *HumanPlus Shadowing Dataset*。 韩文名称为 *HumanPlus Shadowing 데이터셋*。

### HumanPlus Shadowing数据集的任务设置与数据构成
HumanPlus Shadowing数据集通过标准化的任务或数据格式，为不同方法提供可比较的评估基础。理解其覆盖范围与标注方式，有助于正确解读实验结果。
数据或任务的多样性、真实性与可扩展性，是衡量其价值的重要维度。

### 使用方法与评价指标
使用该dataset时，应关注基线方法、评估协议、误差来源以及结果的可复现性，以避免片面或误导性的结论。
同时，需要注意训练集与测试集的划分、分布外泛化能力以及仿真到真实的迁移差距。

### 典型结果与研究价值
HumanPlus Shadowing数据集为学术界与工业界提供了统一的比较基准，推动了相关算法的快速发展。
通过分析排行榜结果与失败案例，可以识别当前方法的优势与短板，指导后续研究方向。

### 相关标签
- dataset
- chapter_21
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键dataset之一，HumanPlus Shadowing数据集在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction

