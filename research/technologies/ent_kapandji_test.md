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

## Overview
A clinical test for thumb opposition ability and finger dexterity, adapted in robotics to evaluate the range of motion and opposition quality of the thumb in dexterous robotic hands.

## Content
### Definition and Positioning of the Kapandji Test
The Kapandji test belongs to the **evaluation benchmark** category. Its related fields include: evaluation benchmarks, design engineering. Value chain level: validation and market level, midstream. A clinical test for thumb opposition ability and finger dexterity, adapted in robotics to evaluate the range of motion and opposition quality of the thumb in dexterous robotic hands. Its English name is *Kapandji Test*. Its Korean name is *Kapandji 테스트*.

### Task Setup and Data Composition of the Kapandji Test
The Kapandji test provides a comparable evaluation basis for different methods through standardized tasks or data formats. Understanding its coverage and annotation methods helps in correctly interpreting experimental results.
The diversity, realism, and scalability of data or tasks are important dimensions for measuring its value.

### Usage Methods and Evaluation Metrics
When using this benchmark, attention should be paid to baseline methods, evaluation protocols, sources of error, and reproducibility of results to avoid one-sided or misleading conclusions.
At the same time, it is necessary to consider the division of training and test sets, out-of-distribution generalization ability, and the simulation-to-real transfer gap.

### Typical Results and Research Value
The Kapandji test provides a unified comparison benchmark for academia and industry, driving the rapid development of related algorithms.
By analyzing leaderboard results and failure cases, the strengths and weaknesses of current methods can be identified, guiding future research directions.

### Related Tags
- kapandji
- thumb
- opposition
- benchmark
- dexterous_hand

### Role in Humanoid Robot Systems
As one of the key evaluation benchmarks in the humanoid robot industry chain, the Kapandji test plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, execution, energy, structure, and verification, collectively determining overall machine performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요  
임상에서 엄지 맞섬 능력과 손가락 민첩성을 평가하는 검사로, 로봇공학에서는 기민한 로봇 손의 엄지 가동 범위와 맞섬 품질을 평가하기 위해 변형되어 사용됩니다.

## 핵심 내용  
### Kapandji 테스트의 정의와 위치  
Kapandji 테스트는 **평가 기준** 유형에 속합니다. 관련 분야로는 평가 기준, 설계 공학이 있습니다. 가치 사슬 단계로는 검증 및 시장 단계, 중류(midstream)에 해당합니다. 임상에서 엄지 맞섬 능력과 손가락 민첩성을 평가하는 검사로, 로봇공학에서는 기민한 로봇 손의 엄지 가동 범위와 맞섬 품질을 평가하기 위해 변형되었습니다. 영어 명칭은 *Kapandji Test*이며, 한국어 명칭은 *Kapandji 테스트*입니다.

### Kapandji 테스트의 과제 설정과 데이터 구성  
Kapandji 테스트는 표준화된 과제 또는 데이터 형식을 통해 다양한 방법에 비교 가능한 평가 기반을 제공합니다. 그 적용 범위와 주석 방식을 이해하면 실험 결과를 올바르게 해석하는 데 도움이 됩니다.  
데이터 또는 과제의 다양성, 현실성, 확장 가능성은 그 가치를 측정하는 중요한 차원입니다.

### 사용 방법과 평가 지표  
이 벤치마크를 사용할 때는 기준 방법, 평가 프로토콜, 오차 원인, 결과의 재현 가능성에 주의하여 편향되거나 오해를 불러일으키는 결론을 피해야 합니다.  
동시에 훈련 세트와 테스트 세트의 분할, 분포 외 일반화 능력, 시뮬레이션에서 실제로의 전환 격차에 유의해야 합니다.

### 대표적 결과와 연구 가치  
Kapandji 테스트는 학계와 산업계에 통일된 비교 기준을 제공하여 관련 알고리즘의 빠른 발전을 촉진했습니다.  
리더보드 결과와 실패 사례를 분석함으로써 현재 방법의 장점과 단점을 식별하고, 향후 연구 방향을 안내할 수 있습니다.

### 관련 태그  
- kapandji  
- thumb  
- opposition  
- benchmark  
- dexterous_hand  

### 휴머노이드 로봇 시스템에서의 역할  
휴머노이드 로봇 산업 체인에서 핵심 평가 기준 중 하나로서, Kapandji 테스트는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조, 검증 등 여러 하위 시스템과 상호 연결되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 환경에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
