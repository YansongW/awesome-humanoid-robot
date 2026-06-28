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
  en: Proposes an online ELBO-based auto-tuning technique for self-supervised reinforcement
    learning (RIG+SAC) that dynamically adjusts the replay buffer size, the number
    of policy gradient updates per epoch, and the number of exploration steps per
    epoch to reduce manual tuning and sample/compute cost.
  zh: 提出一种基于变分自编码器证据下界（ELBO）的在线自动调参方法，用于自监督强化学习（RIG+SAC），动态调整回放缓冲区大小、每轮策略梯度更新次数和每轮探索步数，以减少人工调参及样本/计算开销。
  ko: 자기지도 강화학습(RIG+SAC)을 위해 VAE ELBO에 기반한 온라인 하이퍼파라미터 자동 튜닝 기법을 제안하며, 재생 버퍼 크기·에폭당
    정책 그래디언트 업데이트 횟수·탐색 스텝 수를 동적으로 조정하여 수동 튜닝과 샘플/계산 비용을 줄인다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the abstract and provided metadata; full paper text was
    not consulted. Requires human review before full verification.
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

## Overview

Policy optimization in reinforcement learning depends on many hyperparameters that are usually fixed by hand. Setting them incorrectly can cause insufficient learning (convergence to poor local optima) or redundant learning (wasted samples, time, and computation), and these problems are amplified in multi-task and curriculum settings. This paper observes that the Evidence Lower Bound (ELBO) used in Variational Auto-Encoders correlates with the diversity of generated image samples, and proposes an online auto-tuning method that uses the negative ELBO of the VAE goal generator in RIG+SAC to adapt three hyperparameters: replay buffer size, the number of policy gradient updates per epoch, and the number of exploration steps per epoch. A single scaling factor ξ ties the three hyperparameters together so that the system can increase exploration and updates when goal diversity is high and reduce them when diversity is low.

The authors instantiate their method on Reinforcement Learning with Imagined Goals (RIG) combined with Soft Actor-Critic (SAC). They report experiments on simulated visual manipulation/navigation tasks and a real-robot reaching task, including curriculum learning, showing that the proposed auto-tuning can match or exceed fixed hyperparameter settings while using less time and fewer computational resources.

## Key Contributions

- Identified and theoretically linked the negative ELBO of the VAE goal generator to the empirical entropy/diversity of training samples.
- Proposed an online auto-tuning method that replaces three RIG+SAC hyperparameters with a single scaling factor ξ.
- Demonstrated the method on simulated visual manipulation/navigation tasks and a real-robot visual reaching task, including curriculum learning, while reportedly using fewer resources than fixed Optuna-tuned values.
- Reduced the manual tuning burden for self-supervised visual RL by enabling dynamic, online hyperparameter adjustment.

## Relevance to Humanoid Robotics

Humanoid robots must learn versatile, vision-based behaviors in unstructured environments, which typically requires self-supervised or multi-task reinforcement learning from high-dimensional image observations. Such learning is notoriously sensitive to hyperparameters and expensive in terms of samples, wall-clock time, and compute, making manual tuning a major scalability bottleneck. By using the VAE ELBO as an online diversity signal to auto-tune key hyperparameters, this work directly addresses the sample-efficiency and tuning burden that limit scaling of visual self-supervised RL to complex humanoid platforms.

Although the experiments are performed on a general robot-learning framework rather than a humanoid, the underlying problem—tuning visual multi-task RL with limited samples and compute—is central to humanoid skill acquisition. The method’s emphasis on reducing redundant learning and avoiding local optima is especially relevant for humanoid systems where real-world interaction is costly and curricula are often required to learn whole-body behaviors.
