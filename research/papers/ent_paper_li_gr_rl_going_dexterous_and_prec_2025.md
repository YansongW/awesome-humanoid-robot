---
$id: ent_paper_li_gr_rl_going_dexterous_and_prec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation'
  zh: GR-RL
  ko: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation'
summary:
  en: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (GR-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ByteDance Seed.'
  zh: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (GR-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ByteDance Seed.'
  ko: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (GR-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ByteDance Seed.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gr_rl
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01801v3.
sources:
- id: src_001
  type: paper
  title: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.01801
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GR-RL source
  url: https://doi.org/10.48550/arXiv.2512.01801
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present GR-RL, a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation. Assuming the optimality of human demonstrations is core to existing VLA policies. However, we claim that in highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. Specifically, we show that by directly applying offline RL with sparse reward, the resulting $Q$-values can be treated as a robust progress function. Next, we introduce morphological symmetry augmentation that greatly improves the generalization and performance of GR-RL. Lastly, to better align the VLA policy with its deployment behaviors for high-precision control, we perform online RL by learning a latent space noise predictor. With this pipeline, GR-RL is, to our knowledge, the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction. We hope GR-RL provides a step toward enabling generalist robot foundation models to specialize into reliable real-world experts.

## 核心内容
We present GR-RL, a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation. Assuming the optimality of human demonstrations is core to existing VLA policies. However, we claim that in highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. Specifically, we show that by directly applying offline RL with sparse reward, the resulting $Q$-values can be treated as a robust progress function. Next, we introduce morphological symmetry augmentation that greatly improves the generalization and performance of GR-RL. Lastly, to better align the VLA policy with its deployment behaviors for high-precision control, we perform online RL by learning a latent space noise predictor. With this pipeline, GR-RL is, to our knowledge, the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction. We hope GR-RL provides a step toward enabling generalist robot foundation models to specialize into reliable real-world experts.

## 参考
- http://arxiv.org/abs/2512.01801v3

## Overview
We present GR-RL, a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation. Assuming the optimality of human demonstrations is core to existing VLA policies. However, we claim that in highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. Specifically, we show that by directly applying offline RL with sparse reward, the resulting $Q$-values can be treated as a robust progress function. Next, we introduce morphological symmetry augmentation that greatly improves the generalization and performance of GR-RL. Lastly, to better align the VLA policy with its deployment behaviors for high-precision control, we perform online RL by learning a latent space noise predictor. With this pipeline, GR-RL is, to our knowledge, the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction. We hope GR-RL provides a step toward enabling generalist robot foundation models to specialize into reliable real-world experts.

## Content
We present GR-RL, a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation. Assuming the optimality of human demonstrations is core to existing VLA policies. However, we claim that in highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. Specifically, we show that by directly applying offline RL with sparse reward, the resulting $Q$-values can be treated as a robust progress function. Next, we introduce morphological symmetry augmentation that greatly improves the generalization and performance of GR-RL. Lastly, to better align the VLA policy with its deployment behaviors for high-precision control, we perform online RL by learning a latent space noise predictor. With this pipeline, GR-RL is, to our knowledge, the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction. We hope GR-RL provides a step toward enabling generalist robot foundation models to specialize into reliable real-world experts.

## 개요
우리는 GR-RL을 제시합니다. 이는 일반적인 시각-언어-행동(VLA) 정책을 장기적인 정밀 조작을 위한 고성능 전문가 정책으로 전환하는 로봇 학습 프레임워크입니다. 기존 VLA 정책의 핵심은 인간 시연의 최적성을 가정하는 데 있습니다. 그러나 우리는 매우 정밀하고 세밀한 조작 작업에서 인간 시연이 노이즈가 많고 최적이 아니라고 주장합니다. GR-RL은 강화 학습을 통해 시연을 필터링, 증강 및 강화하는 다단계 훈련 파이프라인을 제안합니다. 첫째, GR-RL은 시각-언어 조건부 작업 진행도를 학습하고, 시연 궤적을 필터링하여 진행에 긍정적으로 기여하는 전환만 유지합니다. 구체적으로, 희소 보상을 사용한 오프라인 RL을 직접 적용함으로써 결과 $Q$-값이 강건한 진행 함수로 처리될 수 있음을 보여줍니다. 다음으로, 형태적 대칭 증강을 도입하여 GR-RL의 일반화와 성능을 크게 향상시킵니다. 마지막으로, 고정밀 제어를 위해 VLA 정책을 배포 행동과 더 잘 정렬하기 위해 잠재 공간 노이즈 예측기를 학습하여 온라인 RL을 수행합니다. 이 파이프라인을 통해 GR-RL은, 우리가 아는 한, 여러 구멍을 통해 신발끈을 꿰어 신발을 자율적으로 묶을 수 있는 최초의 학습 기반 정책으로, 83.3%의 성공률을 달성합니다. 이 작업은 장기적인 추론, 밀리미터 수준의 정밀도, 그리고 유연한 연체 상호작용을 요구합니다. 우리는 GR-RL이 일반적인 로봇 기초 모델이 신뢰할 수 있는 실제 전문가로 특화되는 데 한 걸음 더 나아가길 바랍니다.

## 핵심 내용
우리는 GR-RL을 제시합니다. 이는 일반적인 시각-언어-행동(VLA) 정책을 장기적인 정밀 조작을 위한 고성능 전문가 정책으로 전환하는 로봇 학습 프레임워크입니다. 기존 VLA 정책의 핵심은 인간 시연의 최적성을 가정하는 데 있습니다. 그러나 우리는 매우 정밀하고 세밀한 조작 작업에서 인간 시연이 노이즈가 많고 최적이 아니라고 주장합니다. GR-RL은 강화 학습을 통해 시연을 필터링, 증강 및 강화하는 다단계 훈련 파이프라인을 제안합니다. 첫째, GR-RL은 시각-언어 조건부 작업 진행도를 학습하고, 시연 궤적을 필터링하여 진행에 긍정적으로 기여하는 전환만 유지합니다. 구체적으로, 희소 보상을 사용한 오프라인 RL을 직접 적용함으로써 결과 $Q$-값이 강건한 진행 함수로 처리될 수 있음을 보여줍니다. 다음으로, 형태적 대칭 증강을 도입하여 GR-RL의 일반화와 성능을 크게 향상시킵니다. 마지막으로, 고정밀 제어를 위해 VLA 정책을 배포 행동과 더 잘 정렬하기 위해 잠재 공간 노이즈 예측기를 학습하여 온라인 RL을 수행합니다. 이 파이프라인을 통해 GR-RL은, 우리가 아는 한, 여러 구멍을 통해 신발끈을 꿰어 신발을 자율적으로 묶을 수 있는 최초의 학습 기반 정책으로, 83.3%의 성공률을 달성합니다. 이 작업은 장기적인 추론, 밀리미터 수준의 정밀도, 그리고 유연한 연체 상호작용을 요구합니다. 우리는 GR-RL이 일반적인 로봇 기초 모델이 신뢰할 수 있는 실제 전문가로 특화되는 데 한 걸음 더 나아가길 바랍니다.
