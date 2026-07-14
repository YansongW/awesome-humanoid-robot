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

