---
$id: ent_paper_an_robotic_assistant_completing_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models'
  zh: Robotic Assistant
  ko: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models'
summary:
  en: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (Robotic Assistant),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by ETH Zurich, MIT, Stanford University.'
  zh: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (Robotic Assistant),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by ETH Zurich, MIT, Stanford University.'
  ko: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (Robotic Assistant),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by ETH Zurich, MIT, Stanford University.'
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
- robotic_assistant
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25713v1.
sources:
- id: src_001
  type: paper
  title: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.25713
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Robotic Assistant source
  url: https://doi.org/10.48550/arXiv.2510.25713
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We adapt a pre-trained Vision-Language-Action (VLA) model (Open-VLA) for dexterous human-robot collaboration with minimal language prompting. Our approach adds (i) FiLM conditioning to visual backbones for task-aware perception, (ii) an auxiliary intent head that predicts collaborator hand pose and target cues, and (iii) action-space post-processing that predicts compact deltas (position/rotation) and PCA-reduced finger joints before mapping to full commands. Using a multi-view, teleoperated Franka and Mimic-hand dataset augmented with MediaPipe hand poses, we demonstrate that delta actions are well-behaved and that four principal components explain ~96% of hand-joint variance. Ablations identify action post-processing as the primary performance driver; auxiliary intent helps, FiLM is mixed, and a directional motion loss is detrimental. A real-time stack (~0.3 s latency on one RTX 4090) composes "pick-up" and "pass" into a long-horizon behavior. We surface "trainer overfitting" to specific demonstrators as the key limitation.

## 核心内容
We adapt a pre-trained Vision-Language-Action (VLA) model (Open-VLA) for dexterous human-robot collaboration with minimal language prompting. Our approach adds (i) FiLM conditioning to visual backbones for task-aware perception, (ii) an auxiliary intent head that predicts collaborator hand pose and target cues, and (iii) action-space post-processing that predicts compact deltas (position/rotation) and PCA-reduced finger joints before mapping to full commands. Using a multi-view, teleoperated Franka and Mimic-hand dataset augmented with MediaPipe hand poses, we demonstrate that delta actions are well-behaved and that four principal components explain ~96% of hand-joint variance. Ablations identify action post-processing as the primary performance driver; auxiliary intent helps, FiLM is mixed, and a directional motion loss is detrimental. A real-time stack (~0.3 s latency on one RTX 4090) composes "pick-up" and "pass" into a long-horizon behavior. We surface "trainer overfitting" to specific demonstrators as the key limitation.

## 参考
- http://arxiv.org/abs/2510.25713v1

## Overview
We adapt a pre-trained Vision-Language-Action (VLA) model (Open-VLA) for dexterous human-robot collaboration with minimal language prompting. Our approach adds (i) FiLM conditioning to visual backbones for task-aware perception, (ii) an auxiliary intent head that predicts collaborator hand pose and target cues, and (iii) action-space post-processing that predicts compact deltas (position/rotation) and PCA-reduced finger joints before mapping to full commands. Using a multi-view, teleoperated Franka and Mimic-hand dataset augmented with MediaPipe hand poses, we demonstrate that delta actions are well-behaved and that four principal components explain ~96% of hand-joint variance. Ablations identify action post-processing as the primary performance driver; auxiliary intent helps, FiLM is mixed, and a directional motion loss is detrimental. A real-time stack (~0.3 s latency on one RTX 4090) composes "pick-up" and "pass" into a long-horizon behavior. We surface "trainer overfitting" to specific demonstrators as the key limitation.

## Content
We adapt a pre-trained Vision-Language-Action (VLA) model (Open-VLA) for dexterous human-robot collaboration with minimal language prompting. Our approach adds (i) FiLM conditioning to visual backbones for task-aware perception, (ii) an auxiliary intent head that predicts collaborator hand pose and target cues, and (iii) action-space post-processing that predicts compact deltas (position/rotation) and PCA-reduced finger joints before mapping to full commands. Using a multi-view, teleoperated Franka and Mimic-hand dataset augmented with MediaPipe hand poses, we demonstrate that delta actions are well-behaved and that four principal components explain ~96% of hand-joint variance. Ablations identify action post-processing as the primary performance driver; auxiliary intent helps, FiLM is mixed, and a directional motion loss is detrimental. A real-time stack (~0.3 s latency on one RTX 4090) composes "pick-up" and "pass" into a long-horizon behavior. We surface "trainer overfitting" to specific demonstrators as the key limitation.

## 개요
우리는 최소한의 언어 프롬프트로 정교한 인간-로봇 협업을 위해 사전 훈련된 Vision-Language-Action (VLA) 모델(Open-VLA)을 적용합니다. 우리의 접근 방식은 (i) 작업 인식 지각을 위한 시각적 백본에 FiLM 조건화 추가, (ii) 협업자 손 자세 및 대상 신호를 예측하는 보조 의도 헤드, (iii) 전체 명령으로 매핑하기 전에 압축된 델타(위치/회전) 및 PCA 축소 손가락 관절을 예측하는 행동 공간 후처리를 추가합니다. MediaPipe 손 자세로 증강된 다중 뷰, 원격 조작 Franka 및 Mimic-hand 데이터셋을 사용하여 델타 행동이 잘 작동하며 네 개의 주성분이 손 관절 분산의 약 96%를 설명함을 입증합니다. 절제 연구는 행동 후처리가 주요 성능 동인임을 식별합니다. 보조 의도는 도움이 되고, FiLM은 혼합적이며, 방향성 운동 손실은 해롭습니다. 실시간 스택(하나의 RTX 4090에서 약 0.3초 지연 시간)은 "집기"와 "전달"을 장기 행동으로 구성합니다. 우리는 특정 시연자에 대한 "훈련자 과적합"을 주요 한계로 제시합니다.

## 핵심 내용
우리는 최소한의 언어 프롬프트로 정교한 인간-로봇 협업을 위해 사전 훈련된 Vision-Language-Action (VLA) 모델(Open-VLA)을 적용합니다. 우리의 접근 방식은 (i) 작업 인식 지각을 위한 시각적 백본에 FiLM 조건화 추가, (ii) 협업자 손 자세 및 대상 신호를 예측하는 보조 의도 헤드, (iii) 전체 명령으로 매핑하기 전에 압축된 델타(위치/회전) 및 PCA 축소 손가락 관절을 예측하는 행동 공간 후처리를 추가합니다. MediaPipe 손 자세로 증강된 다중 뷰, 원격 조작 Franka 및 Mimic-hand 데이터셋을 사용하여 델타 행동이 잘 작동하며 네 개의 주성분이 손 관절 분산의 약 96%를 설명함을 입증합니다. 절제 연구는 행동 후처리가 주요 성능 동인임을 식별합니다. 보조 의도는 도움이 되고, FiLM은 혼합적이며, 방향성 운동 손실은 해롭습니다. 실시간 스택(하나의 RTX 4090에서 약 0.3초 지연 시간)은 "집기"와 "전달"을 장기 행동으로 구성합니다. 우리는 특정 시연자에 대한 "훈련자 과적합"을 주요 한계로 제시합니다.
