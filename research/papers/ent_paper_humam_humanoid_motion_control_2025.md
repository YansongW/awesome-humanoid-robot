---
$id: ent_paper_humam_humanoid_motion_control_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba'
  zh: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba'
  ko: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba'
summary:
  en: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba is a 2025 work on locomotion for humanoid robots.'
  zh: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba is a 2025 work on locomotion for humanoid robots.'
  ko: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humam
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.18046v2.
sources:
- id: src_001
  type: paper
  title: 'HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba (arXiv)'
  url: https://arxiv.org/abs/2509.18046
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
End-to-end reinforcement learning (RL) for humanoid locomotion is appealing for its compact perception-action mapping, yet practical policies often suffer from training instability, inefficient feature fusion, and high actuation cost. We present HuMam, a state-centric end-to-end RL framework that employs a single-layer Mamba encoder to fuse robot-centric states with oriented footstep targets and a continuous phase clock. The policy outputs joint position targets tracked by a low-level PD loop and is optimized with PPO. A concise six-term reward balances contact quality, swing smoothness, foot placement, posture, and body stability while implicitly promoting energy saving. On the JVRC-1 humanoid in mc-mujoco, HuMam consistently improves learning efficiency, training stability, and overall task performance over a strong feedforward baseline, while reducing power consumption and torque peaks. To our knowledge, this is the first end-to-end humanoid RL controller that adopts Mamba as the fusion backbone, demonstrating tangible gains in efficiency, stability, and control economy.

## 核心内容
End-to-end reinforcement learning (RL) for humanoid locomotion is appealing for its compact perception-action mapping, yet practical policies often suffer from training instability, inefficient feature fusion, and high actuation cost. We present HuMam, a state-centric end-to-end RL framework that employs a single-layer Mamba encoder to fuse robot-centric states with oriented footstep targets and a continuous phase clock. The policy outputs joint position targets tracked by a low-level PD loop and is optimized with PPO. A concise six-term reward balances contact quality, swing smoothness, foot placement, posture, and body stability while implicitly promoting energy saving. On the JVRC-1 humanoid in mc-mujoco, HuMam consistently improves learning efficiency, training stability, and overall task performance over a strong feedforward baseline, while reducing power consumption and torque peaks. To our knowledge, this is the first end-to-end humanoid RL controller that adopts Mamba as the fusion backbone, demonstrating tangible gains in efficiency, stability, and control economy.

## 参考
- http://arxiv.org/abs/2509.18046v2

## Overview
End-to-end reinforcement learning (RL) for humanoid locomotion is appealing for its compact perception-action mapping, yet practical policies often suffer from training instability, inefficient feature fusion, and high actuation cost. We present HuMam, a state-centric end-to-end RL framework that employs a single-layer Mamba encoder to fuse robot-centric states with oriented footstep targets and a continuous phase clock. The policy outputs joint position targets tracked by a low-level PD loop and is optimized with PPO. A concise six-term reward balances contact quality, swing smoothness, foot placement, posture, and body stability while implicitly promoting energy saving. On the JVRC-1 humanoid in mc-mujoco, HuMam consistently improves learning efficiency, training stability, and overall task performance over a strong feedforward baseline, while reducing power consumption and torque peaks. To our knowledge, this is the first end-to-end humanoid RL controller that adopts Mamba as the fusion backbone, demonstrating tangible gains in efficiency, stability, and control economy.

## Content
End-to-end reinforcement learning (RL) for humanoid locomotion is appealing for its compact perception-action mapping, yet practical policies often suffer from training instability, inefficient feature fusion, and high actuation cost. We present HuMam, a state-centric end-to-end RL framework that employs a single-layer Mamba encoder to fuse robot-centric states with oriented footstep targets and a continuous phase clock. The policy outputs joint position targets tracked by a low-level PD loop and is optimized with PPO. A concise six-term reward balances contact quality, swing smoothness, foot placement, posture, and body stability while implicitly promoting energy saving. On the JVRC-1 humanoid in mc-mujoco, HuMam consistently improves learning efficiency, training stability, and overall task performance over a strong feedforward baseline, while reducing power consumption and torque peaks. To our knowledge, this is the first end-to-end humanoid RL controller that adopts Mamba as the fusion backbone, demonstrating tangible gains in efficiency, stability, and control economy.

## 개요
인간형 로봇의 보행을 위한 종단간 강화 학습(RL)은 간결한 지각-행동 매핑으로 주목받지만, 실제 정책은 종종 훈련 불안정성, 비효율적인 특징 융합, 높은 구동 비용 문제를 겪습니다. 본 논문에서는 단일 레이어 Mamba 인코더를 사용하여 로봇 중심 상태를 방향성 발자국 목표 및 연속 위상 클록과 융합하는 상태 중심 종단간 RL 프레임워크인 HuMam을 제안합니다. 정책은 저수준 PD 루프로 추적되는 관절 위치 목표를 출력하며 PPO로 최적화됩니다. 간결한 6항목 보상은 접촉 품질, 스윙 부드러움, 발 위치, 자세, 몸체 안정성을 균형 있게 조정하면서 에너지 절약을 암묵적으로 촉진합니다. mc-mujoco의 JVRC-1 인간형 로봇에서 HuMam은 강력한 피드포워드 기준선 대비 학습 효율성, 훈련 안정성, 전체 작업 성능을 일관되게 개선하면서 전력 소비와 토크 피크를 줄입니다. 본 연구는 Mamba를 융합 백본으로 채택한 최초의 종단간 인간형 로봇 RL 제어기로, 효율성, 안정성, 제어 경제성에서 실질적인 이점을 입증합니다.

## 핵심 내용
인간형 로봇의 보행을 위한 종단간 강화 학습(RL)은 간결한 지각-행동 매핑으로 주목받지만, 실제 정책은 종종 훈련 불안정성, 비효율적인 특징 융합, 높은 구동 비용 문제를 겪습니다. 본 논문에서는 단일 레이어 Mamba 인코더를 사용하여 로봇 중심 상태를 방향성 발자국 목표 및 연속 위상 클록과 융합하는 상태 중심 종단간 RL 프레임워크인 HuMam을 제안합니다. 정책은 저수준 PD 루프로 추적되는 관절 위치 목표를 출력하며 PPO로 최적화됩니다. 간결한 6항목 보상은 접촉 품질, 스윙 부드러움, 발 위치, 자세, 몸체 안정성을 균형 있게 조정하면서 에너지 절약을 암묵적으로 촉진합니다. mc-mujoco의 JVRC-1 인간형 로봇에서 HuMam은 강력한 피드포워드 기준선 대비 학습 효율성, 훈련 안정성, 전체 작업 성능을 일관되게 개선하면서 전력 소비와 토크 피크를 줄입니다. 본 연구는 Mamba를 융합 백본으로 채택한 최초의 종단간 인간형 로봇 RL 제어기로, 효율성, 안정성, 제어 경제성에서 실질적인 이점을 입증합니다.
