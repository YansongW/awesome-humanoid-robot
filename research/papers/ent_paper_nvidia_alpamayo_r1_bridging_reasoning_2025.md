---
$id: ent_paper_nvidia_alpamayo_r1_bridging_reasoning_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail'
  zh: Alpamayo-R1
  ko: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail'
summary:
  en: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail (Alpamayo-R1),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore.'
  zh: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail (Alpamayo-R1),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore.'
  ko: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail (Alpamayo-R1),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- alpamayo_r1
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00088v2.
sources:
- id: src_001
  type: paper
  title: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail (arXiv)'
  url: https://arxiv.org/abs/2511.00088
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Alpamayo-R1 source
  url: https://doi.org/10.48550/arXiv.2511.00088
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
End-to-end architectures trained via imitation learning have advanced autonomous driving by scaling model size and data, yet performance remains brittle in safety-critical long-tail scenarios where supervision is sparse and causal understanding is limited. We introduce Alpamayo-R1 (AR1), a vision-language-action model (VLA) that integrates Chain of Causation reasoning with trajectory planning for complex driving scenarios. Our approach features three key innovations: (1) the Chain of Causation (CoC) dataset, built through a hybrid auto-labeling and human-in-the-loop pipeline producing decision-grounded, causally linked reasoning traces aligned with driving behaviors; (2) a modular VLA architecture combining Cosmos-Reason, a vision-language model pre-trained for Physical AI, with a diffusion-based trajectory decoder that generates dynamically feasible trajectories in real time; (3) a multi-stage training strategy using supervised fine-tuning to elicit reasoning and reinforcement learning (RL) to enforce reasoning-action consistency and optimize reasoning quality. AR1 achieves up to a 12% improvement in planning accuracy on challenging cases compared to a trajectory-only baseline, with a 35% reduction in close encounter rate in closed-loop simulation. RL post-training improves reasoning quality by 45% and reasoning-action consistency by 37%. Model scaling from 0.5B to 7B parameters shows consistent improvements. On-vehicle road tests confirm real-time performance (99 ms latency) and successful urban deployment. By bridging interpretable reasoning with precise control, AR1 demonstrates a practical path towards Level 4 autonomous driving. Model weights are available at https://huggingface.co/nvidia/Alpamayo-R1-10B with inference code at https://github.com/NVlabs/alpamayo.

## 核心内容
End-to-end architectures trained via imitation learning have advanced autonomous driving by scaling model size and data, yet performance remains brittle in safety-critical long-tail scenarios where supervision is sparse and causal understanding is limited. We introduce Alpamayo-R1 (AR1), a vision-language-action model (VLA) that integrates Chain of Causation reasoning with trajectory planning for complex driving scenarios. Our approach features three key innovations: (1) the Chain of Causation (CoC) dataset, built through a hybrid auto-labeling and human-in-the-loop pipeline producing decision-grounded, causally linked reasoning traces aligned with driving behaviors; (2) a modular VLA architecture combining Cosmos-Reason, a vision-language model pre-trained for Physical AI, with a diffusion-based trajectory decoder that generates dynamically feasible trajectories in real time; (3) a multi-stage training strategy using supervised fine-tuning to elicit reasoning and reinforcement learning (RL) to enforce reasoning-action consistency and optimize reasoning quality. AR1 achieves up to a 12% improvement in planning accuracy on challenging cases compared to a trajectory-only baseline, with a 35% reduction in close encounter rate in closed-loop simulation. RL post-training improves reasoning quality by 45% and reasoning-action consistency by 37%. Model scaling from 0.5B to 7B parameters shows consistent improvements. On-vehicle road tests confirm real-time performance (99 ms latency) and successful urban deployment. By bridging interpretable reasoning with precise control, AR1 demonstrates a practical path towards Level 4 autonomous driving. Model weights are available at https://huggingface.co/nvidia/Alpamayo-R1-10B with inference code at https://github.com/NVlabs/alpamayo.

## 参考
- http://arxiv.org/abs/2511.00088v2

## Overview
End-to-end architectures trained via imitation learning have advanced autonomous driving by scaling model size and data, yet performance remains brittle in safety-critical long-tail scenarios where supervision is sparse and causal understanding is limited. We introduce Alpamayo-R1 (AR1), a vision-language-action model (VLA) that integrates Chain of Causation reasoning with trajectory planning for complex driving scenarios. Our approach features three key innovations: (1) the Chain of Causation (CoC) dataset, built through a hybrid auto-labeling and human-in-the-loop pipeline producing decision-grounded, causally linked reasoning traces aligned with driving behaviors; (2) a modular VLA architecture combining Cosmos-Reason, a vision-language model pre-trained for Physical AI, with a diffusion-based trajectory decoder that generates dynamically feasible trajectories in real time; (3) a multi-stage training strategy using supervised fine-tuning to elicit reasoning and reinforcement learning (RL) to enforce reasoning-action consistency and optimize reasoning quality. AR1 achieves up to a 12% improvement in planning accuracy on challenging cases compared to a trajectory-only baseline, with a 35% reduction in close encounter rate in closed-loop simulation. RL post-training improves reasoning quality by 45% and reasoning-action consistency by 37%. Model scaling from 0.5B to 7B parameters shows consistent improvements. On-vehicle road tests confirm real-time performance (99 ms latency) and successful urban deployment. By bridging interpretable reasoning with precise control, AR1 demonstrates a practical path towards Level 4 autonomous driving. Model weights are available at https://huggingface.co/nvidia/Alpamayo-R1-10B with inference code at https://github.com/NVlabs/alpamayo.

## Content
End-to-end architectures trained via imitation learning have advanced autonomous driving by scaling model size and data, yet performance remains brittle in safety-critical long-tail scenarios where supervision is sparse and causal understanding is limited. We introduce Alpamayo-R1 (AR1), a vision-language-action model (VLA) that integrates Chain of Causation reasoning with trajectory planning for complex driving scenarios. Our approach features three key innovations: (1) the Chain of Causation (CoC) dataset, built through a hybrid auto-labeling and human-in-the-loop pipeline producing decision-grounded, causally linked reasoning traces aligned with driving behaviors; (2) a modular VLA architecture combining Cosmos-Reason, a vision-language model pre-trained for Physical AI, with a diffusion-based trajectory decoder that generates dynamically feasible trajectories in real time; (3) a multi-stage training strategy using supervised fine-tuning to elicit reasoning and reinforcement learning (RL) to enforce reasoning-action consistency and optimize reasoning quality. AR1 achieves up to a 12% improvement in planning accuracy on challenging cases compared to a trajectory-only baseline, with a 35% reduction in close encounter rate in closed-loop simulation. RL post-training improves reasoning quality by 45% and reasoning-action consistency by 37%. Model scaling from 0.5B to 7B parameters shows consistent improvements. On-vehicle road tests confirm real-time performance (99 ms latency) and successful urban deployment. By bridging interpretable reasoning with precise control, AR1 demonstrates a practical path towards Level 4 autonomous driving. Model weights are available at https://huggingface.co/nvidia/Alpamayo-R1-10B with inference code at https://github.com/NVlabs/alpamayo.

## 개요
모방 학습을 통해 훈련된 엔드투엔드 아키텍처는 모델 크기와 데이터를 확장하여 자율 주행을 발전시켰지만, 감독이 부족하고 인과 관계 이해가 제한적인 안전에 중요한 롱테일 시나리오에서는 성능이 여전히 취약합니다. 우리는 복잡한 주행 시나리오를 위해 인과 사슬 추론과 궤적 계획을 통합하는 비전-언어-행동 모델(VLA)인 Alpamayo-R1(AR1)을 소개합니다. 우리의 접근 방식은 세 가지 주요 혁신을 특징으로 합니다: (1) 하이브리드 자동 레이블링 및 인간-인-더-루프 파이프라인을 통해 구축된 인과 사슬(CoC) 데이터셋으로, 주행 행동과 정렬된 결정 기반의 인과적으로 연결된 추론 흔적을 생성합니다; (2) Physical AI를 위해 사전 훈련된 비전-언어 모델인 Cosmos-Reason과 실시간으로 동적으로 실행 가능한 궤적을 생성하는 확산 기반 궤적 디코더를 결합한 모듈식 VLA 아키텍처; (3) 추론을 유도하기 위한 지도 미세 조정과 추론-행동 일관성을 강화하고 추론 품질을 최적화하기 위한 강화 학습(RL)을 사용하는 다단계 훈련 전략. AR1은 궤적 전용 기준선과 비교하여 까다로운 사례에서 계획 정확도를 최대 12% 향상시키고, 폐루프 시뮬레이션에서 근접 조우율을 35% 감소시킵니다. RL 사후 훈련은 추론 품질을 45%, 추론-행동 일관성을 37% 향상시킵니다. 0.5B에서 7B 파라미터로의 모델 확장은 일관된 개선을 보여줍니다. 차량 내 도로 테스트는 실시간 성능(99ms 지연 시간)과 성공적인 도시 배치를 확인합니다. 해석 가능한 추론과 정밀한 제어를 연결함으로써 AR1은 레벨 4 자율 주행을 향한 실용적인 경로를 보여줍니다. 모델 가중치는 https://huggingface.co/nvidia/Alpamayo-R1-10B에서, 추론 코드는 https://github.com/NVlabs/alpamayo에서 확인할 수 있습니다.

## 핵심 내용
모방 학습을 통해 훈련된 엔드투엔드 아키텍처는 모델 크기와 데이터를 확장하여 자율 주행을 발전시켰지만, 감독이 부족하고 인과 관계 이해가 제한적인 안전에 중요한 롱테일 시나리오에서는 성능이 여전히 취약합니다. 우리는 복잡한 주행 시나리오를 위해 인과 사슬 추론과 궤적 계획을 통합하는 비전-언어-행동 모델(VLA)인 Alpamayo-R1(AR1)을 소개합니다. 우리의 접근 방식은 세 가지 주요 혁신을 특징으로 합니다: (1) 하이브리드 자동 레이블링 및 인간-인-더-루프 파이프라인을 통해 구축된 인과 사슬(CoC) 데이터셋으로, 주행 행동과 정렬된 결정 기반의 인과적으로 연결된 추론 흔적을 생성합니다; (2) Physical AI를 위해 사전 훈련된 비전-언어 모델인 Cosmos-Reason과 실시간으로 동적으로 실행 가능한 궤적을 생성하는 확산 기반 궤적 디코더를 결합한 모듈식 VLA 아키텍처; (3) 추론을 유도하기 위한 지도 미세 조정과 추론-행동 일관성을 강화하고 추론 품질을 최적화하기 위한 강화 학습(RL)을 사용하는 다단계 훈련 전략. AR1은 궤적 전용 기준선과 비교하여 까다로운 사례에서 계획 정확도를 최대 12% 향상시키고, 폐루프 시뮬레이션에서 근접 조우율을 35% 감소시킵니다. RL 사후 훈련은 추론 품질을 45%, 추론-행동 일관성을 37% 향상시킵니다. 0.5B에서 7B 파라미터로의 모델 확장은 일관된 개선을 보여줍니다. 차량 내 도로 테스트는 실시간 성능(99ms 지연 시간)과 성공적인 도시 배치를 확인합니다. 해석 가능한 추론과 정밀한 제어를 연결함으로써 AR1은 레벨 4 자율 주행을 향한 실용적인 경로를 보여줍니다. 모델 가중치는 https://huggingface.co/nvidia/Alpamayo-R1-10B에서, 추론 코드는 https://github.com/NVlabs/alpamayo에서 확인할 수 있습니다.
