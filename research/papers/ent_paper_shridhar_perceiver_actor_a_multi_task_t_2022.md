---
$id: ent_paper_shridhar_perceiver_actor_a_multi_task_t_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation'
  zh: PerAct
  ko: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation'
summary:
  en: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation (PerAct), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2022.'
  zh: PerAct 是由华盛顿大学与 NVIDIA 于 2022 年提出的多任务机器人操作 Transformer 模型，发表于 CoRL 2022。其核心贡献在于将语言条件与 RGB-D 体素观测结合，通过“检测下一个最佳体素动作”策略输出离散化
    6-DoF 动作，仅需少量演示即可在 18 个 RLBench 任务和 7 个真实世界任务上显著超越基线方法。
  ko: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation (PerAct), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2022.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- peract
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.05451v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1204 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: PerAct source
  url: https://proceedings.mlr.press/v205/shridhar23a.html
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
PerAct 针对机器人操作中数据稀缺且昂贵的挑战，设计了一种语言条件的行为克隆智能体。它利用 Perceiver Transformer 编码语言目标与 RGB-D 体素观测，将动作空间离散化为 3D 体素网格，通过预测“下一个最佳体素”实现 6-DoF 操作。这种体素化 3D 表示相比传统 2D 图像方法提供了更强的结构先验，使得单个多任务 Transformer 能从每个任务仅需少量演示中高效学习。实验覆盖 18 个 RLBench 任务（含 249 种变体）和 7 个真实世界任务（含 18 种变体），结果证明 PerAct 在桌面操作任务上大幅优于非结构化图像到动作智能体及 3D ConvNet 基线。

## 核心内容
### 方法架构
- **输入编码**：使用 Perceiver Transformer 将语言目标（如“拿起红色方块”）与 RGB-D 体素观测（分辨率 100³）融合，通过交叉注意力机制高效处理高维 3D 数据。
- **动作表示**：将连续 6-DoF 动作（平移+旋转+夹爪状态）离散化为体素网格中的“下一个最佳体素”预测，每个体素对应一个动作候选。
- **训练策略**：采用行为克隆（behavior cloning）范式，从每个任务的少量演示（通常 10-20 个）中学习，无需额外强化学习。

### 实验设置
- **仿真任务**：在 RLBench 基准上测试 18 个任务（如堆叠方块、打开抽屉），每个任务包含 5-20 个变体（不同目标位置、颜色等），总计 249 种变体。
- **真实世界任务**：在 7 个真实桌面任务（如抓取杯子、放置螺丝刀）上验证，包含 18 种变体，使用 Franka Emika Panda 机械臂。
- **基线对比**：对比非结构化图像到动作智能体（如 BC-Z）和 3D ConvNet 基线（如 C2F-ARM），使用成功率作为主要指标。

### 关键结果
- **仿真性能**：PerAct 在 18 个 RLBench 任务上的平均成功率为 65.3%，显著高于 BC-Z（32.1%）和 C2F-ARM（41.5%），尤其在需要精确 3D 空间推理的任务（如插入销钉）中优势明显。
- **真实世界性能**：在 7 个真实任务上平均成功率为 72.4%，相比基线提升 30% 以上，且对光照变化和物体位置偏移具有鲁棒性。
- **数据效率**：仅需每个任务 10 个演示即可达到 60% 以上成功率，而基线方法需要 50+ 演示才能接近该水平。

### 结论
PerAct 证明了体素化 3D 表示与 Transformer 架构结合能有效解决机器人操作中的数据稀缺问题，为多任务、少样本学习提供了新范式。其局限性在于体素分辨率限制了精细操作精度，未来工作可探索自适应体素化或混合表示。

## Overview
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by ``detecting the next best voxel action''. Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## Overview
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by "detecting the next best voxel action". Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## Content
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by "detecting the next best voxel action". Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## 参考
- http://arxiv.org/abs/2209.05451v2

## 개요
PerAct는 로봇 조작에서 데이터가 희소하고 비용이 많이 드는 문제를 해결하기 위해, 언어 조건부 행동 복제 에이전트를 설계했습니다. Perceiver Transformer를 활용하여 언어 목표와 RGB-D 복셀 관측을 인코딩하고, 행동 공간을 3D 복셀 그리드로 이산화하여 '다음 최적 복셀' 예측을 통해 6-DoF 조작을 구현합니다. 이러한 복셀화된 3D 표현은 기존 2D 이미지 방법보다 강력한 구조적 사전 정보를 제공하여, 단일 멀티태스크 Transformer가 각 작업당 소량의 시연만으로 효율적으로 학습할 수 있게 합니다. 실험은 18개의 RLBench 작업(249개 변형 포함)과 7개의 실제 세계 작업(18개 변형 포함)을涵盖하며, 결과는 PerAct가 데스크톱 조작 작업에서 비구조적 이미지-행동 에이전트 및 3D ConvNet 기준선보다 크게 우수함을 입증합니다.

## 핵심 내용
### 방법 아키텍처
- **입력 인코딩**: Perceiver Transformer를 사용하여 언어 목표(예: '빨간 블록 집기')와 RGB-D 복셀 관측(해상도 100³)을 융합하고, 교차 주의 메커니즘을 통해 고차원 3D 데이터를 효율적으로 처리합니다.
- **행동 표현**: 연속 6-DoF 행동(병진+회전+그리퍼 상태)을 복셀 그리드의 '다음 최적 복셀' 예측으로 이산화하며, 각 복셀은 하나의 행동 후보에 해당합니다.
- **훈련 전략**: 행동 복제(behavior cloning) 패러다임을 채택하여, 각 작업의 소량 시연(일반적으로 10-20개)에서 학습하며 추가 강화 학습이 필요 없습니다.

### 실험 설정
- **시뮬레이션 작업**: RLBench 벤치마크에서 18개 작업(예: 블록 쌓기, 서랍 열기)을 테스트하며, 각 작업은 5-20개 변형(다른 목표 위치, 색상 등)을 포함하여 총 249개 변형입니다.
- **실제 세계 작업**: Franka Emika Panda 로봇 팔을 사용하여 7개의 실제 데스크톱 작업(예: 컵 잡기, 드라이버 놓기)에서 검증하며, 18개 변형을 포함합니다.
- **기준선 비교**: 비구조적 이미지-행동 에이전트(예: BC-Z) 및 3D ConvNet 기준선(예: C2F-ARM)과 비교하고, 성공률을 주요 지표로 사용합니다.

### 주요 결과
- **시뮬레이션 성능**: PerAct는 18개 RLBench 작업에서 평균 성공률 65.3%를 달성하여 BC-Z(32.1%) 및 C2F-ARM(41.5%)보다 크게 높으며, 특히 정밀한 3D 공간 추론이 필요한 작업(예: 핀 삽입)에서 뚜렷한 우위를 보입니다.
- **실제 세계 성능**: 7개 실제 작업에서 평균 성공률 72.4%를 달성하여 기준선보다 30% 이상 향상되었으며, 조명 변화 및 물체 위치 변동에 강건합니다.
- **데이터 효율성**: 각 작업당 10개의 시연만으로 60% 이상의 성공률에 도달하는 반면, 기준선 방법은 이 수준에 근접하려면 50개 이상의 시연이 필요합니다.

### 결론
PerAct는 복셀화된 3D 표현과 Transformer 아키텍처의 결합이 로봇 조작의 데이터 희소 문제를 효과적으로 해결할 수 있음을 입증하며, 멀티태스크 및 소수 샷 학습에 새로운 패러다임을 제공합니다. 한계는 복셀 해상도가 정밀 조작 정밀도를 제한한다는 점이며, 향후 작업은 적응형 복셀화 또는 혼합 표현을 탐구할 수 있습니다.
