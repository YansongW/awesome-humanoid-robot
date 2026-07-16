---
$id: ent_paper_jin_dual_actor_fine_tuning_of_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach'
  zh: Dual-Actor Fine-Tuning of VLA Models
  ko: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach'
summary:
  en: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (Dual-Actor Fine-Tuning of VLA Models),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by City University of Hong Kong, Beijing
    Xiaomi Robot Technology Co., Ltd..'
  zh: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (Dual-Actor Fine-Tuning of VLA Models),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by City University of Hong Kong, Beijing
    Xiaomi Robot Technology Co., Ltd..'
  ko: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (Dual-Actor Fine-Tuning of VLA Models),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by City University of Hong Kong, Beijing
    Xiaomi Robot Technology Co., Ltd..'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dual_actor_fine_tuning_of_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13774v1.
sources:
- id: src_001
  type: paper
  title: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (arXiv)'
  url: https://arxiv.org/abs/2509.13774
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Dual-Actor Fine-Tuning of VLA Models source
  url: https://doi.org/10.48550/arXiv.2509.13774
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models demonstrate strong generalization in robotic manipulation but face challenges in complex, real-world tasks. While supervised fine-tuning with demonstrations is constrained by data quality, reinforcement learning (RL) offers a promising alternative. We propose a human-in-the-loop dual-actor fine-tuning framework grounded in RL. The framework integrates a primary actor for robust multi-task performance with a refinement actor for latent-space adaptation. Beyond standard physical interventions, we introduce a lightweight talk-and-tweak scheme that converts human corrections into semantically grounded language commands, thereby generating a new dataset for policy learning. In real-world multi-task experiments, our approach achieves 100% success across three tasks within 101 minutes of online fine-tuning. For long-horizon tasks, it sustains a 50% success rate over 12 consecutive operations. Furthermore, the framework scales effectively to multi-robot training, achieving up to a 2 times improvement in efficiency when using dual robots. The experiment videos are available at https://sites.google.com/view/hil-daft/.

## 核心内容
Vision-language-action (VLA) models demonstrate strong generalization in robotic manipulation but face challenges in complex, real-world tasks. While supervised fine-tuning with demonstrations is constrained by data quality, reinforcement learning (RL) offers a promising alternative. We propose a human-in-the-loop dual-actor fine-tuning framework grounded in RL. The framework integrates a primary actor for robust multi-task performance with a refinement actor for latent-space adaptation. Beyond standard physical interventions, we introduce a lightweight talk-and-tweak scheme that converts human corrections into semantically grounded language commands, thereby generating a new dataset for policy learning. In real-world multi-task experiments, our approach achieves 100% success across three tasks within 101 minutes of online fine-tuning. For long-horizon tasks, it sustains a 50% success rate over 12 consecutive operations. Furthermore, the framework scales effectively to multi-robot training, achieving up to a 2 times improvement in efficiency when using dual robots. The experiment videos are available at https://sites.google.com/view/hil-daft/.

## 参考
- http://arxiv.org/abs/2509.13774v1

## Overview
Vision-language-action (VLA) models demonstrate strong generalization in robotic manipulation but face challenges in complex, real-world tasks. While supervised fine-tuning with demonstrations is constrained by data quality, reinforcement learning (RL) offers a promising alternative. We propose a human-in-the-loop dual-actor fine-tuning framework grounded in RL. The framework integrates a primary actor for robust multi-task performance with a refinement actor for latent-space adaptation. Beyond standard physical interventions, we introduce a lightweight talk-and-tweak scheme that converts human corrections into semantically grounded language commands, thereby generating a new dataset for policy learning. In real-world multi-task experiments, our approach achieves 100% success across three tasks within 101 minutes of online fine-tuning. For long-horizon tasks, it sustains a 50% success rate over 12 consecutive operations. Furthermore, the framework scales effectively to multi-robot training, achieving up to a 2 times improvement in efficiency when using dual robots. The experiment videos are available at https://sites.google.com/view/hil-daft/.

## Content
Vision-language-action (VLA) models demonstrate strong generalization in robotic manipulation but face challenges in complex, real-world tasks. While supervised fine-tuning with demonstrations is constrained by data quality, reinforcement learning (RL) offers a promising alternative. We propose a human-in-the-loop dual-actor fine-tuning framework grounded in RL. The framework integrates a primary actor for robust multi-task performance with a refinement actor for latent-space adaptation. Beyond standard physical interventions, we introduce a lightweight talk-and-tweak scheme that converts human corrections into semantically grounded language commands, thereby generating a new dataset for policy learning. In real-world multi-task experiments, our approach achieves 100% success across three tasks within 101 minutes of online fine-tuning. For long-horizon tasks, it sustains a 50% success rate over 12 consecutive operations. Furthermore, the framework scales effectively to multi-robot training, achieving up to a 2 times improvement in efficiency when using dual robots. The experiment videos are available at https://sites.google.com/view/hil-daft/.

## 개요
Vision-language-action (VLA) 모델은 로봇 조작에서 강력한 일반화 능력을 보여주지만, 복잡한 실제 작업에서는 어려움에 직면합니다. 시연 데이터를 통한 지도 미세 조정은 데이터 품질에 제약을 받는 반면, 강화 학습(RL)은 유망한 대안을 제시합니다. 우리는 RL에 기반한 인간-루프 이중 행동자 미세 조정 프레임워크를 제안합니다. 이 프레임워크는 강력한 다중 작업 성능을 위한 기본 행동자와 잠재 공간 적응을 위한 정제 행동자를 통합합니다. 표준적인 물리적 개입 외에도, 우리는 인간의 교정을 의미적으로 기반한 언어 명령으로 변환하여 정책 학습을 위한 새로운 데이터셋을 생성하는 경량의 talk-and-tweak 방식을 도입합니다. 실제 다중 작업 실험에서, 우리의 접근 방식은 101분의 온라인 미세 조정 내에 세 가지 작업에서 100% 성공률을 달성합니다. 장기 작업의 경우, 12회 연속 작업에서 50%의 성공률을 유지합니다. 또한, 이 프레임워크는 다중 로봇 훈련으로 효과적으로 확장되어, 이중 로봇 사용 시 최대 2배의 효율성 향상을 달성합니다. 실험 비디오는 https://sites.google.com/view/hil-daft/에서 확인할 수 있습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 로봇 조작에서 강력한 일반화 능력을 보여주지만, 복잡한 실제 작업에서는 어려움에 직면합니다. 시연 데이터를 통한 지도 미세 조정은 데이터 품질에 제약을 받는 반면, 강화 학습(RL)은 유망한 대안을 제시합니다. 우리는 RL에 기반한 인간-루프 이중 행동자 미세 조정 프레임워크를 제안합니다. 이 프레임워크는 강력한 다중 작업 성능을 위한 기본 행동자와 잠재 공간 적응을 위한 정제 행동자를 통합합니다. 표준적인 물리적 개입 외에도, 우리는 인간의 교정을 의미적으로 기반한 언어 명령으로 변환하여 정책 학습을 위한 새로운 데이터셋을 생성하는 경량의 talk-and-tweak 방식을 도입합니다. 실제 다중 작업 실험에서, 우리의 접근 방식은 101분의 온라인 미세 조정 내에 세 가지 작업에서 100% 성공률을 달성합니다. 장기 작업의 경우, 12회 연속 작업에서 50%의 성공률을 유지합니다. 또한, 이 프레임워크는 다중 로봇 훈련으로 효과적으로 확장되어, 이중 로봇 사용 시 최대 2배의 효율성 향상을 달성합니다. 실험 비디오는 https://sites.google.com/view/hil-daft/에서 확인할 수 있습니다.
