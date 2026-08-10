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
  zh: WARP-RM 是一种全自监督的进度奖励模型，由研究团队提出，用于从成功演示中学习稠密的相对进度信号。其核心贡献在于通过时间扭曲增强生成帧级进度目标，并利用该信号提升行为克隆中高优势动作块的权重，在长时程变形物体操作任务中显著提升策略鲁棒性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.28320v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (722 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation (arXiv)'
  url: https://arxiv.org/abs/2606.28320
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
WARP（Warp-Augmented Relative Progress）算法通过时间扭曲增强（变速播放和倒放）为演示帧生成进度目标，训练 WARP-RM 预测帧间归一化经过时间。将重叠窗口的预测聚合后得到稠密帧级进度信号，进而提出 WARP-BC，在行为克隆中利用这些标量奖励估计提升高优势动作块的权重。在双臂机器人折叠T恤任务中，当数据集包含更多低质量演示时，WARP-BC 保持 19/20 成功率，而标准 BC 降至 2/20，吞吐量提升达 18 倍。

## 核心内容
### 方法
- **WARP 算法**：对成功演示施加时间扭曲增强（变速播放和倒放），生成每帧的进度目标。训练 WARP-RM 预测输入帧之间的归一化经过时间。
- **进度信号聚合**：通过重叠窗口聚合预测结果，得到稠密的帧级进度信号。
- **WARP-BC**：在行为克隆中，将帧级奖励聚合为动作块级优势，并据此提升高优势动作块的权重。

### 实验设置
- **物理系统**：双臂机器人执行长时程变形物体操作任务——从随机揉皱状态折叠T恤。
- **数据集构建**：以回合长度作为遥操作次优性代理，构建不同质量的训练数据集。
- **对比基准**：标准行为克隆（vanilla BC）。

### 关键结果
- **T恤折叠任务**：当数据集扩大以包含更多低效演示时，WARP-BC 维持 19/20 成功率，而 vanilla BC 降至 2/20，吞吐量提升高达 18 倍。
- **瓶入箱放置任务**：在真实世界和可复现仿真中均验证了成功率、速度和吞吐量的提升，并通过配对显著性检验。
- **开源**：发布所有仿真代码和评估工件。

## Overview
Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data, we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world, as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/

## 参考
- http://arxiv.org/abs/2606.28320v3

## 개요
WARP(Warp-Augmented Relative Progress) 알고리즘은 시간 왜곡 증강(배속 재생 및 역방향 재생)을 통해 데모 프레임에 대한 진행 목표를 생성하고, WARP-RM을 훈련하여 프레임 간 정규화된 경과 시간을 예측합니다. 중첩 창의 예측을 집계하여 조밀한 프레임 수준 진행 신호를 얻은 후, WARP-BC를 제안하여 행동 클로닝에서 이러한 스칼라 보상 추정치를 활용해 높은 이점을 가진 행동 블록의 가중치를 높입니다. 이중 로봇 팔 티셔츠 접기 작업에서 데이터셋에 저품질 데모가 더 많이 포함될 때, WARP-BC는 19/20 성공률을 유지하는 반면, 표준 BC는 2/20으로 떨어지며 처리량은 최대 18배 향상됩니다.

## 핵심 내용
### 방법
- **WARP 알고리즘**: 성공적인 데모에 시간 왜곡 증강(배속 재생 및 역방향 재생)을 적용하여 각 프레임의 진행 목표를 생성합니다. WARP-RM을 훈련하여 입력 프레임 간의 정규화된 경과 시간을 예측합니다.
- **진행 신호 집계**: 중첩 창을 통해 예측 결과를 집계하여 조밀한 프레임 수준 진행 신호를 얻습니다.
- **WARP-BC**: 행동 클로닝에서 프레임 수준 보상을 행동 블록 수준 이점으로 집계하고, 이를 기반으로 높은 이점을 가진 행동 블록의 가중치를 높입니다.

### 실험 설정
- **물리 시스템**: 이중 로봇 팔이 장시간 변형 물체 조작 작업(무작위로 구겨진 상태에서 티셔츠 접기)을 수행합니다.
- **데이터셋 구축**: 에피소드 길이를 원격 조작의 비최적성 대리 지표로 사용하여 다양한 품질의 훈련 데이터셋을 구축합니다.
- **비교 기준**: 표준 행동 클로닝(vanilla BC).

### 주요 결과
- **티셔츠 접기 작업**: 데이터셋이 더 많은 비효율적 데모를 포함하도록 확장될 때, WARP-BC는 19/20 성공률을 유지하는 반면, vanilla BC는 2/20으로 떨어지며 처리량은 최대 18배 향상됩니다.
- **병을 상자에 넣는 배치 작업**: 실제 세계와 재현 가능한 시뮬레이션 모두에서 성공률, 속도 및 처리량의 향상이 검증되었으며, 쌍체 유의성 검정을 통해 확인되었습니다.
- **오픈소스**: 모든 시뮬레이션 코드와 평가 아티팩트를 공개합니다.
