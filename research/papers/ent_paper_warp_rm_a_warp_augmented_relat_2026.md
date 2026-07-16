---
$id: ent_paper_warp_rm_a_warp_augmented_relat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation'
  zh: 'WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation'
  ko: 'WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation'
summary:
  en: 'arXiv:2606.28320v3 Announce Type: replace Abstract: Scaling imitation learning requires large datasets, yet human teleoperation
    inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward
    models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations
    to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm
    for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame
    progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM
    to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows
    yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to
    upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating
    per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object
    manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data,
    we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As
    the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC''s
    collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world,
    as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance
    tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/'
  zh: 'arXiv:2606.28320v3 Announce Type: replace Abstract: Scaling imitation learning requires large datasets, yet human teleoperation
    inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward
    models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations
    to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm
    for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame
    progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM
    to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows
    yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to
    upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating
    per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object
    manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data,
    we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As
    the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC''s
    collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world,
    as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance
    tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/'
  ko: 'arXiv:2606.28320v3 Announce Type: replace Abstract: Scaling imitation learning requires large datasets, yet human teleoperation
    inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward
    models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations
    to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm
    for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame
    progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM
    to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows
    yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to
    upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating
    per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object
    manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data,
    we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As
    the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC''s
    collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world,
    as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance
    tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- warp_rm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.28320v3.
sources:
- id: src_001
  type: paper
  title: 'WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation (arXiv)'
  url: https://arxiv.org/abs/2606.28320
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data, we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world, as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/

## 核心内容
Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data, we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world, as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/

## 参考
- http://arxiv.org/abs/2606.28320v3

## Overview
Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data, we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world, as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/

## Content
Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data, we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world, as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/

## 개요
모방 학습(imitation learning)의 확장에는 대규모 데이터셋이 필요하지만, 인간의 원격 조작(teleoperation)은 필연적으로 망설임과 회복 동작이 포함된 혼합 품질의 시연(demonstration)을 생성합니다. 기존의 프레임 수준 진행 보상 모델(frame-level progress reward model)은 라벨 노이즈(label noise)가 있는 절대적 시간 진행 프록시(absolute temporal progress proxy)를 사용하여 학습하거나, 하위 작업 경계(subtask boundary)를 정의하기 위해 비용이 많이 드는 인간 주석(human annotation)이 필요합니다. 본 논문에서는 성공적인 시연으로부터 직접 밀집된(dense) 부호 있는 상대적 진행 크기(signed relative progress magnitude)를 학습하는 완전 자가 지도(full self-supervised) 알고리즘인 WARP(Warp-Augmented Relative Progress)를 제안합니다. WARP는 시연의 시간 왜곡 증강(time-warp augmentation, 가변 재생 속도 및 역방향 재생)을 통해 프레임별 진행 목표를 생성하고, 입력 프레임 간의 정규화된 경과 시간(normalized elapsed time)을 예측하도록 WARP-RM을 학습시킵니다. 이러한 예측을 중첩 윈도우(overlapping window)에 걸쳐 집계하면 밀집된 프레임 수준 진행 신호를 얻을 수 있습니다. 그런 다음 WARP-BC를 도입하여, 행동 복제(behavior cloning) 중에 높은 이점(high-advantage)을 가진 행동 청크(action chunk)의 가중치를 높이는 데 이러한 스칼라 보상 추정치를 활용합니다. 여기서 청크 수준 이점은 프레임별 보상을 집계하여 얻습니다. 본 접근법을 무작위로 구겨진 상태에서 티셔츠를 접는 장기간 변형 가능한 물체 조작 작업(long-horizon deformable object manipulation task)을 수행하는 물리적 양팔 로봇 시스템에서 평가합니다. 최적이 아닌 데이터에 대한 정책의 강건성을 평가하기 위해, 에피소드 길이를 원격 조작의 비최적성(proxy for teleoperation sub-optimality)의 프록시로 사용하여 다양한 품질의 훈련 데이터셋을 구성합니다. 데이터셋이 더 많은 비효율성을 포함하도록 확장됨에 따라, WARP-BC는 19/20의 성공률을 유지하는 반면, 기본 BC(vanilla BC)는 2/20으로 성능이 붕괴되어 최대 18배의 처리량(throughput) 향상을 보여줍니다. 또한, 실제 환경에서 병-통(bottle-in-bin) 배치 작업과 재현 가능한 시뮬레이션에서 평가하여 성공률, 속도 및 처리량의 향상이 쌍체 유의성 검정(paired significance test)에서 유의미함을 확인했으며, 모든 시뮬레이션 코드와 평가 산출물을 공개합니다. 프로젝트 페이지: https://uynitsuj.github.io/warp-rm/

## 핵심 내용
모방 학습의 확장에는 대규모 데이터셋이 필요하지만, 인간의 원격 조작은 필연적으로 망설임과 회복 동작이 포함된 혼합 품질의 시연을 생성합니다. 기존의 프레임 수준 진행 보상 모델은 라벨 노이즈가 있는 절대적 시간 진행 프록시를 사용하여 학습하거나, 하위 작업 경계를 정의하기 위해 비용이 많이 드는 인간 주석이 필요합니다. 본 논문에서는 성공적인 시연으로부터 직접 밀집된 부호 있는 상대적 진행 크기를 학습하는 완전 자가 지도 알고리즘인 WARP를 제안합니다. WARP는 시연의 시간 왜곡 증강(가변 재생 속도 및 역방향 재생)을 통해 프레임별 진행 목표를 생성하고, 입력 프레임 간의 정규화된 경과 시간을 예측하도록 WARP-RM을 학습시킵니다. 이러한 예측을 중첩 윈도우에 걸쳐 집계하면 밀집된 프레임 수준 진행 신호를 얻을 수 있습니다. 그런 다음 WARP-BC를 도입하여, 행동 복제 중에 높은 이점을 가진 행동 청크의 가중치를 높이는 데 이러한 스칼라 보상 추정치를 활용합니다. 여기서 청크 수준 이점은 프레임별 보상을 집계하여 얻습니다. 본 접근법을 무작위로 구겨진 상태에서 티셔츠를 접는 장기간 변형 가능한 물체 조작 작업을 수행하는 물리적 양팔 로봇 시스템에서 평가합니다. 최적이 아닌 데이터에 대한 정책의 강건성을 평가하기 위해, 에피소드 길이를 원격 조작의 비최적성의 프록시로 사용하여 다양한 품질의 훈련 데이터셋을 구성합니다. 데이터셋이 더 많은 비효율성을 포함하도록 확장됨에 따라, WARP-BC는 19/20의 성공률을 유지하는 반면, 기본 BC는 2/20으로 성능이 붕괴되어 최대 18배의 처리량 향상을 보여줍니다. 또한, 실제 환경에서 병-통 배치 작업과 재현 가능한 시뮬레이션에서 평가하여 성공률, 속도 및 처리량의 향상이 쌍체 유의성 검정에서 유의미함을 확인했으며, 모든 시뮬레이션 코드와 평가 산출물을 공개합니다. 프로젝트 페이지: https://uynitsuj.github.io/warp-rm/
