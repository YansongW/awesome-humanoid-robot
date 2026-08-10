---
$id: ent_paper_huang_hyperparameter_auto_tuning_in_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hyperparameter Auto-tuning in Self-Supervised Robotic Learning
  zh: 自监督机器人学习中的超参数自动调优
  ko: 자기지도 로봇 학습의 하이퍼파라미터 자동 튜닝
summary:
  en: Proposes an online ELBO-based auto-tuning technique for self-supervised reinforcement learning (RIG+SAC) that dynamically
    adjusts the replay buffer size, the number of policy gradient updates per epoch, and the number of exploration steps per
    epoch to reduce manual tuning and sample/compute cost.
  zh: 本文提出一种基于证据下界（ELBO）的在线自动调参技术，用于自监督强化学习（RIG+SAC）框架。该方法能动态调整回放缓冲区大小、每轮策略梯度更新次数和每轮探索步数三个超参数，显著减少人工调参成本并降低样本与计算开销。
  ko: 자기지도 강화학습(RIG+SAC)을 위해 VAE ELBO에 기반한 온라인 하이퍼파라미터 자동 튜닝 기법을 제안하며, 재생 버퍼 크기·에폭당 정책 그래디언트 업데이트 횟수·탐색 스텝 수를 동적으로 조정하여 수동
    튜닝과 샘플/계산 비용을 줄인다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- self_supervised_rl
- reinforcement_learning
- hyperparameter_auto_tuning
- variational_autoencoder
- soft_actor_critic
- imagined_goals
- visual_rl
- multi_task_learning
- sample_efficiency
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.08252v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (551 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Hyperparameter Auto-tuning in Self-Supervised Robotic Learning
  url: https://arxiv.org/abs/2010.08252
  date: '2021'
  accessed_at: '2026-06-28'
  doi: 10.1109/LRA.2021.3064509
theoretical_depth:
- method
---
## 概述
强化学习中的超参数选择不当会导致学习不足或冗余，尤其在多任务场景中问题加剧。作者观察到变分自编码器中的ELBO与图像样本多样性相关，据此设计自动调参方法。该方法在RIG+SAC自监督机器人学习框架上验证，实验表明其能以更少时间和计算资源达到最优性能。项目页面提供代码、视频及仿真/真实机器人实验附录。

## 核心内容
### 方法核心
- **理论基础**：利用VAE中ELBO值与图像样本多样性的相关性，将ELBO作为超参数调整的在线信号。
- **自动调参对象**：三个关键超参数——回放缓冲区容量、每轮策略梯度更新次数、每轮探索步数。
- **调整机制**：根据ELBO动态变化，在训练过程中实时调整上述参数，避免固定参数导致的局部最优或资源浪费。

### 实验设置
- **基线框架**：采用RIG+SAC（基于想象目标的强化学习+软演员-评论家算法）作为自监督学习基线。
- **验证场景**：包含仿真环境和真实机器人实验，项目页面提供完整代码与视频。

### 关键结果
- **性能提升**：自动调参方法在同等任务下达到最优策略性能，且训练时间与计算资源消耗显著降低。
- **效率优势**：相比手动调参，该方法无需人工干预即可在线适应环境变化，尤其适用于多任务学习场景。

## Overview
Policy optimization in reinforcement learning requires the selection of numerous hyperparameters across different environments. Fixing them incorrectly may negatively impact optimization performance leading notably to insufficient or redundant learning. Insufficient learning (due to convergence to local optima) results in under-performing policies whilst redundant learning wastes time and resources. The effects are further exacerbated when using single policies to solve multi-task learning problems. Observing that the Evidence Lower Bound (ELBO) used in Variational Auto-Encoders correlates with the diversity of image samples, we propose an auto-tuning technique based on the ELBO for self-supervised reinforcement learning. Our approach can auto-tune three hyperparameters: the replay buffer size, the number of policy gradient updates during each epoch, and the number of exploration steps during each epoch. We use a state-of-the-art self-supervised robot learning framework (Reinforcement Learning with Imagined Goals (RIG) using Soft Actor-Critic) as baseline for experimental verification. Experiments show that our method can auto-tune online and yields the best performance at a fraction of the time and computational resources. Code, video, and appendix for simulated and real-robot experiments can be found at the project page \url{www.JuanRojas.net/autotune}.

## Overview
Policy optimization in reinforcement learning requires the selection of numerous hyperparameters across different environments. Fixing them incorrectly may negatively impact optimization performance, leading notably to insufficient or redundant learning. Insufficient learning (due to convergence to local optima) results in under-performing policies, while redundant learning wastes time and resources. The effects are further exacerbated when using single policies to solve multi-task learning problems. Observing that the Evidence Lower Bound (ELBO) used in Variational Auto-Encoders correlates with the diversity of image samples, we propose an auto-tuning technique based on the ELBO for self-supervised reinforcement learning. Our approach can auto-tune three hyperparameters: the replay buffer size, the number of policy gradient updates during each epoch, and the number of exploration steps during each epoch. We use a state-of-the-art self-supervised robot learning framework (Reinforcement Learning with Imagined Goals (RIG) using Soft Actor-Critic) as a baseline for experimental verification. Experiments show that our method can auto-tune online and yields the best performance at a fraction of the time and computational resources. Code, video, and appendix for simulated and real-robot experiments can be found at the project page \url{www.JuanRojas.net/autotune}.

## Content
Policy optimization in reinforcement learning requires the selection of numerous hyperparameters across different environments. Fixing them incorrectly may negatively impact optimization performance, leading notably to insufficient or redundant learning. Insufficient learning (due to convergence to local optima) results in under-performing policies, while redundant learning wastes time and resources. The effects are further exacerbated when using single policies to solve multi-task learning problems. Observing that the Evidence Lower Bound (ELBO) used in Variational Auto-Encoders correlates with the diversity of image samples, we propose an auto-tuning technique based on the ELBO for self-supervised reinforcement learning. Our approach can auto-tune three hyperparameters: the replay buffer size, the number of policy gradient updates during each epoch, and the number of exploration steps during each epoch. We use a state-of-the-art self-supervised robot learning framework (Reinforcement Learning with Imagined Goals (RIG) using Soft Actor-Critic) as a baseline for experimental verification. Experiments show that our method can auto-tune online and yields the best performance at a fraction of the time and computational resources. Code, video, and appendix for simulated and real-robot experiments can be found at the project page \url{www.JuanRojas.net/autotune}.

## 参考
- http://arxiv.org/abs/2010.08252v4

## 개요
강화 학습에서 하이퍼파라미터 선택이 부적절하면 학습 부족이나 중복이 발생할 수 있으며, 특히 다중 작업 시나리오에서 문제가 심화됩니다. 저자는 변분 오토인코더의 ELBO가 이미지 샘플 다양성과 관련이 있음을 관찰하고, 이를 바탕으로 자동 하이퍼파라미터 조정 방법을 설계했습니다. 이 방법은 RIG+SAC 자기 지도 로봇 학습 프레임워크에서 검증되었으며, 실험 결과 더 적은 시간과 계산 자원으로 최적 성능에 도달할 수 있음을 보여줍니다. 프로젝트 페이지에서는 코드, 비디오 및 시뮬레이션/실제 로봇 실험 부록을 제공합니다.

## 핵심 내용
### 방법 핵심
- **이론적 기반**: VAE의 ELBO 값과 이미지 샘플 다양성 간의 상관관계를 활용하여, ELBO를 하이퍼파라미터 조정의 온라인 신호로 사용합니다.
- **자동 조정 대상**: 세 가지 핵심 하이퍼파라미터——리플레이 버퍼 용량, 에피소드당 정책 그라디언트 업데이트 횟수, 에피소드당 탐색 단계 수.
- **조정 메커니즘**: ELBO의 동적 변화에 따라 훈련 과정에서 위 파라미터를 실시간으로 조정하여, 고정 파라미터로 인한 지역 최적해 또는 자원 낭비를 방지합니다.

### 실험 설정
- **기준 프레임워크**: RIG+SAC(상상 기반 목표 강화 학습 + 소프트 액터-크리틱 알고리즘)을 자기 지도 학습 기준으로 채택합니다.
- **검증 시나리오**: 시뮬레이션 환경과 실제 로봇 실험을 포함하며, 프로젝트 페이지에서 전체 코드와 비디오를 제공합니다.

### 주요 결과
- **성능 향상**: 자동 조정 방법은 동일한 작업에서 최적 정책 성능에 도달하며, 훈련 시간과 계산 자원 소비가 크게 감소합니다.
- **효율성 이점**: 수동 조정에 비해 이 방법은 인간의 개입 없이 온라인으로 환경 변화에 적응할 수 있어, 특히 다중 작업 학습 시나리오에 적합합니다.
