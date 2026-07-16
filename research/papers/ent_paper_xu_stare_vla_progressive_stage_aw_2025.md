---
$id: ent_paper_xu_stare_vla_progressive_stage_aw_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models'
  zh: STARE-VLA
  ko: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models'
summary:
  en: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (STARE-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Technical University of Munich, Imperial College
    London, Munich Research Center, Huawei Technologies.'
  zh: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (STARE-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Technical University of Munich, Imperial College
    London, Munich Research Center, Huawei Technologies.'
  ko: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (STARE-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Technical University of Munich, Imperial College
    London, Munich Research Center, Huawei Technologies.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- stare_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05107v2.
sources:
- id: src_001
  type: paper
  title: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2512.05107
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: STARE-VLA source
  url: https://doi.org/10.48550/arXiv.2512.05107
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

## 核心内容
Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

## 参考
- http://arxiv.org/abs/2512.05107v2

## Overview
Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

## Content
Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

## 개요
최근 Vision-Language-Action (VLA) 모델은 대규모 언어 모델과 강화 학습 기반 미세 조정을 통해 로봇 조작 분야에서 놀라운 발전을 보여주고 있습니다. 기존 방법들은 장기적인 행동을 언어 시퀀스로 간주하고 Trajectory-wise Preference Optimization (TPO) 또는 Proximal Policy Optimization (PPO)과 같은 궤적 수준 최적화 방법을 적용하여, 거친 신용 할당과 불안정한 훈련을 초래합니다. 그러나 언어가 유연한 문장 순서에도 불구하고 통일된 의미를 유지하는 것과 달리, 행동 궤적은 인과적으로 연결된 단계를 통해 진행되며 각 단계마다 학습 난이도가 다릅니다. 이는 점진적인 단계 최적화를 동기부여합니다. 이에 우리는 장기적인 행동 궤적을 의미적으로 의미 있는 단계로 분해하고, 밀집되고 해석 가능하며 단계에 맞춰진 강화 신호를 제공하는 모듈인 Stage-Aware Reinforcement (STARE)를 제시합니다. STARE를 TPO와 PPO에 통합하여, 오프라인 단계별 선호도와 온라인 단계 내 상호작용을 위한 Stage-Aware TPO (STA-TPO) 및 Stage-Aware PPO (STA-PPO)를 각각 생성합니다. 또한 지도 미세 조정을 초기화로 삼아, VLA 모델의 행동 정확도를 향상시키기 위한 직렬 미세 조정 파이프라인인 Imitation -> Preference -> Interaction (IPI)을 제안합니다. SimplerEnv와 ManiSkill3에서의 실험은 상당한 성능 향상을 입증하며, SimplerEnv에서 98.0%, ManiSkill3 작업에서 96.4%의 최첨단 성공률을 달성했습니다.

## 핵심 내용
최근 Vision-Language-Action (VLA) 모델은 대규모 언어 모델과 강화 학습 기반 미세 조정을 통해 로봇 조작 분야에서 놀라운 발전을 보여주고 있습니다. 기존 방법들은 장기적인 행동을 언어 시퀀스로 간주하고 Trajectory-wise Preference Optimization (TPO) 또는 Proximal Policy Optimization (PPO)과 같은 궤적 수준 최적화 방법을 적용하여, 거친 신용 할당과 불안정한 훈련을 초래합니다. 그러나 언어가 유연한 문장 순서에도 불구하고 통일된 의미를 유지하는 것과 달리, 행동 궤적은 인과적으로 연결된 단계를 통해 진행되며 각 단계마다 학습 난이도가 다릅니다. 이는 점진적인 단계 최적화를 동기부여합니다. 이에 우리는 장기적인 행동 궤적을 의미적으로 의미 있는 단계로 분해하고, 밀집되고 해석 가능하며 단계에 맞춰진 강화 신호를 제공하는 모듈인 Stage-Aware Reinforcement (STARE)를 제시합니다. STARE를 TPO와 PPO에 통합하여, 오프라인 단계별 선호도와 온라인 단계 내 상호작용을 위한 Stage-Aware TPO (STA-TPO) 및 Stage-Aware PPO (STA-PPO)를 각각 생성합니다. 또한 지도 미세 조정을 초기화로 삼아, VLA 모델의 행동 정확도를 향상시키기 위한 직렬 미세 조정 파이프라인인 Imitation -> Preference -> Interaction (IPI)을 제안합니다. SimplerEnv와 ManiSkill3에서의 실험은 상당한 성능 향상을 입증하며, SimplerEnv에서 98.0%, ManiSkill3 작업에서 96.4%의 최첨단 성공률을 달성했습니다.
