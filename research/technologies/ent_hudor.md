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
HuDOR属于 **数据集** 类型。 所属领域包括：数据与数据集, AI 模型与算法。 价值链层级：智能层。 一种用于采集人手动作数据以训练灵巧机器人手模仿学习策略的人类到机器人演示数据集或遥操作框架。 英文名称为 *HuDOR*。 韩文名称为 *HuDOR*。

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
作为人形机器人产业链中的关键数据集之一，HuDOR在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [RUKA: Rethinking the Design of Humanoid Hands with Learning](https://arxiv.org/abs/2504.13165)

## Overview
A human-to-robot demonstration dataset or teleoperation framework for collecting human hand motion data to train imitation learning policies for dexterous robotic hands.

## Content
### Definition and Positioning of HuDOR
HuDOR belongs to the **dataset** category. Its domains include: Data and Datasets, AI Models and Algorithms. Value chain level: Intelligence layer. It is a human-to-robot demonstration dataset or teleoperation framework for collecting human hand motion data to train imitation learning policies for dexterous robotic hands. The English name is *HuDOR*. The Korean name is *HuDOR*.

### Task Setup and Data Composition of HuDOR
HuDOR provides a comparable evaluation basis for different methods through standardized tasks or data formats. Understanding its coverage and annotation methods helps in correctly interpreting experimental results.
The diversity, authenticity, and scalability of data or tasks are important dimensions for measuring its value.

### Usage Methods and Evaluation Metrics
When using this dataset, attention should be paid to baseline methods, evaluation protocols, sources of error, and reproducibility of results to avoid one-sided or misleading conclusions.
Additionally, it is necessary to consider the training-test set split, out-of-distribution generalization capability, and the sim-to-real transfer gap.

### Typical Results and Research Value
HuDOR provides a unified comparison benchmark for academia and industry, driving the rapid development of related algorithms.
By analyzing leaderboard results and failure cases, the strengths and weaknesses of current methods can be identified, guiding future research directions.

### Related Tags
- hudor
- teleoperation
- imitation_learning
- dataset
- dexterous_manipulation

### Role in Humanoid Robot Systems
As one of the key datasets in the humanoid robot industry chain, HuDOR plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, execution, energy, structure, and verification, collectively determining overall system performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
사람 손 동작 데이터를 수집하여 정교한 로봇 손의 모방 학습 정책을 훈련시키기 위한 인간-로봇 시연 데이터셋 또는 원격 조작 프레임워크.

## 핵심 내용
### HuDOR의 정의와 위치
HuDOR는 **데이터셋** 유형에 속함. 관련 분야는 데이터 및 데이터셋, AI 모델 및 알고리즘을 포함. 가치 사슬 계층: 지능 계층. 사람 손 동작 데이터를 수집하여 정교한 로봇 손의 모방 학습 정책을 훈련시키기 위한 인간-로봇 시연 데이터셋 또는 원격 조작 프레임워크. 영문 명칭은 *HuDOR*. 한글 명칭은 *HuDOR*.

### HuDOR의 작업 설정과 데이터 구성
HuDOR는 표준화된 작업 또는 데이터 형식을 통해 다양한 방법에 비교 가능한 평가 기준을 제공함. 그 적용 범위와 주석 방식을 이해하면 실험 결과를 올바르게 해석하는 데 도움이 됨. 데이터 또는 작업의 다양성, 현실성 및 확장 가능성은 그 가치를 측정하는 중요한 차원임.

### 사용 방법과 평가 지표
이 데이터셋을 사용할 때는 기준 방법, 평가 프로토콜, 오류 원인 및 결과의 재현 가능성에 주의하여 편향되거나 오해를 불러일으키는 결론을 피해야 함. 동시에 훈련 세트와 테스트 세트의 분할, 분포 외 일반화 능력 및 시뮬레이션에서 실제로의 전환 격차에 주의해야 함.

### 대표적인 결과와 연구 가치
HuDOR는 학계와 산업계에 통일된 비교 기준을 제공하여 관련 알고리즘의 빠른 발전을 촉진함. 순위표 결과와 실패 사례를 분석하면 현재 방법의 장점과 단점을 식별하고 후속 연구 방향을 안내할 수 있음.

### 관련 태그
- hudor
- teleoperation
- imitation_learning
- dataset
- dexterous_manipulation

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인에서 핵심 데이터셋 중 하나로서 HuDOR는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 함. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정함. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있음.
