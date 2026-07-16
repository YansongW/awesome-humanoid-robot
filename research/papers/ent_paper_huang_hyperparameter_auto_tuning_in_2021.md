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
  zh: 提出一种基于变分自编码器证据下界（ELBO）的在线自动调参方法，用于自监督强化学习（RIG+SAC），动态调整回放缓冲区大小、每轮策略梯度更新次数和每轮探索步数，以减少人工调参及样本/计算开销。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.08252v4.
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
Policy optimization in reinforcement learning requires the selection of numerous hyperparameters across different environments. Fixing them incorrectly may negatively impact optimization performance leading notably to insufficient or redundant learning. Insufficient learning (due to convergence to local optima) results in under-performing policies whilst redundant learning wastes time and resources. The effects are further exacerbated when using single policies to solve multi-task learning problems. Observing that the Evidence Lower Bound (ELBO) used in Variational Auto-Encoders correlates with the diversity of image samples, we propose an auto-tuning technique based on the ELBO for self-supervised reinforcement learning. Our approach can auto-tune three hyperparameters: the replay buffer size, the number of policy gradient updates during each epoch, and the number of exploration steps during each epoch. We use a state-of-the-art self-supervised robot learning framework (Reinforcement Learning with Imagined Goals (RIG) using Soft Actor-Critic) as baseline for experimental verification. Experiments show that our method can auto-tune online and yields the best performance at a fraction of the time and computational resources. Code, video, and appendix for simulated and real-robot experiments can be found at the project page \url{www.JuanRojas.net/autotune}.

## 核心内容
Policy optimization in reinforcement learning requires the selection of numerous hyperparameters across different environments. Fixing them incorrectly may negatively impact optimization performance leading notably to insufficient or redundant learning. Insufficient learning (due to convergence to local optima) results in under-performing policies whilst redundant learning wastes time and resources. The effects are further exacerbated when using single policies to solve multi-task learning problems. Observing that the Evidence Lower Bound (ELBO) used in Variational Auto-Encoders correlates with the diversity of image samples, we propose an auto-tuning technique based on the ELBO for self-supervised reinforcement learning. Our approach can auto-tune three hyperparameters: the replay buffer size, the number of policy gradient updates during each epoch, and the number of exploration steps during each epoch. We use a state-of-the-art self-supervised robot learning framework (Reinforcement Learning with Imagined Goals (RIG) using Soft Actor-Critic) as baseline for experimental verification. Experiments show that our method can auto-tune online and yields the best performance at a fraction of the time and computational resources. Code, video, and appendix for simulated and real-robot experiments can be found at the project page \url{www.JuanRojas.net/autotune}.

## 参考
- http://arxiv.org/abs/2010.08252v4

## Overview
Policy optimization in reinforcement learning requires the selection of numerous hyperparameters across different environments. Fixing them incorrectly may negatively impact optimization performance, leading notably to insufficient or redundant learning. Insufficient learning (due to convergence to local optima) results in under-performing policies, while redundant learning wastes time and resources. The effects are further exacerbated when using single policies to solve multi-task learning problems. Observing that the Evidence Lower Bound (ELBO) used in Variational Auto-Encoders correlates with the diversity of image samples, we propose an auto-tuning technique based on the ELBO for self-supervised reinforcement learning. Our approach can auto-tune three hyperparameters: the replay buffer size, the number of policy gradient updates during each epoch, and the number of exploration steps during each epoch. We use a state-of-the-art self-supervised robot learning framework (Reinforcement Learning with Imagined Goals (RIG) using Soft Actor-Critic) as a baseline for experimental verification. Experiments show that our method can auto-tune online and yields the best performance at a fraction of the time and computational resources. Code, video, and appendix for simulated and real-robot experiments can be found at the project page \url{www.JuanRojas.net/autotune}.

## Content
Policy optimization in reinforcement learning requires the selection of numerous hyperparameters across different environments. Fixing them incorrectly may negatively impact optimization performance, leading notably to insufficient or redundant learning. Insufficient learning (due to convergence to local optima) results in under-performing policies, while redundant learning wastes time and resources. The effects are further exacerbated when using single policies to solve multi-task learning problems. Observing that the Evidence Lower Bound (ELBO) used in Variational Auto-Encoders correlates with the diversity of image samples, we propose an auto-tuning technique based on the ELBO for self-supervised reinforcement learning. Our approach can auto-tune three hyperparameters: the replay buffer size, the number of policy gradient updates during each epoch, and the number of exploration steps during each epoch. We use a state-of-the-art self-supervised robot learning framework (Reinforcement Learning with Imagined Goals (RIG) using Soft Actor-Critic) as a baseline for experimental verification. Experiments show that our method can auto-tune online and yields the best performance at a fraction of the time and computational resources. Code, video, and appendix for simulated and real-robot experiments can be found at the project page \url{www.JuanRojas.net/autotune}.

## 개요
강화 학습에서의 정책 최적화는 다양한 환경에 걸쳐 수많은 하이퍼파라미터를 선택해야 합니다. 이를 잘못 고정하면 최적화 성능에 부정적인 영향을 미쳐, 특히 학습 부족 또는 중복 학습을 초래할 수 있습니다. 학습 부족(국소 최적해로 수렴으로 인해)은 성능이 낮은 정책을 초래하는 반면, 중복 학습은 시간과 자원을 낭비합니다. 이러한 영향은 단일 정책을 사용하여 다중 작업 학습 문제를 해결할 때 더욱 악화됩니다. 변분 오토인코더에서 사용되는 증거 하한(ELBO)이 이미지 샘플의 다양성과 상관관계가 있음을 관찰하여, 우리는 ELBO 기반의 자동 튜닝 기법을 자기 지도 강화 학습에 제안합니다. 우리의 접근 방식은 세 가지 하이퍼파라미터(리플레이 버퍼 크기, 각 에포크 동안의 정책 그래디언트 업데이트 횟수, 각 에포크 동안의 탐색 단계 수)를 자동으로 튜닝할 수 있습니다. 우리는 최신 자기 지도 로봇 학습 프레임워크(Soft Actor-Critic을 사용한 상상 목표 기반 강화 학습(RIG))를 실험 검증의 기준선으로 사용합니다. 실험 결과, 우리의 방법이 온라인으로 자동 튜닝할 수 있으며, 적은 시간과 계산 자원으로 최고의 성능을 달성함을 보여줍니다. 시뮬레이션 및 실제 로봇 실험을 위한 코드, 비디오 및 부록은 프로젝트 페이지 \url{www.JuanRojas.net/autotune}에서 확인할 수 있습니다.

## 핵심 내용
강화 학습에서의 정책 최적화는 다양한 환경에 걸쳐 수많은 하이퍼파라미터를 선택해야 합니다. 이를 잘못 고정하면 최적화 성능에 부정적인 영향을 미쳐, 특히 학습 부족 또는 중복 학습을 초래할 수 있습니다. 학습 부족(국소 최적해로 수렴으로 인해)은 성능이 낮은 정책을 초래하는 반면, 중복 학습은 시간과 자원을 낭비합니다. 이러한 영향은 단일 정책을 사용하여 다중 작업 학습 문제를 해결할 때 더욱 악화됩니다. 변분 오토인코더에서 사용되는 증거 하한(ELBO)이 이미지 샘플의 다양성과 상관관계가 있음을 관찰하여, 우리는 ELBO 기반의 자동 튜닝 기법을 자기 지도 강화 학습에 제안합니다. 우리의 접근 방식은 세 가지 하이퍼파라미터(리플레이 버퍼 크기, 각 에포크 동안의 정책 그래디언트 업데이트 횟수, 각 에포크 동안의 탐색 단계 수)를 자동으로 튜닝할 수 있습니다. 우리는 최신 자기 지도 로봇 학습 프레임워크(Soft Actor-Critic을 사용한 상상 목표 기반 강화 학습(RIG))를 실험 검증의 기준선으로 사용합니다. 실험 결과, 우리의 방법이 온라인으로 자동 튜닝할 수 있으며, 적은 시간과 계산 자원으로 최고의 성능을 달성함을 보여줍니다. 시뮬레이션 및 실제 로봇 실험을 위한 코드, 비디오 및 부록은 프로젝트 페이지 \url{www.JuanRojas.net/autotune}에서 확인할 수 있습니다.
