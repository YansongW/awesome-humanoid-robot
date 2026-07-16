---
$id: ent_paper_ye_learning_to_feel_the_future_dr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation'
  zh: DreamTacVLA
  ko: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation'
summary:
  en: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation (DreamTacVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Northwestern University.'
  zh: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation (DreamTacVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Northwestern University.'
  ko: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation (DreamTacVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Northwestern University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dreamtacvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23864v4.
sources:
- id: src_001
  type: paper
  title: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.23864
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DreamTacVLA source
  url: https://doi.org/10.48550/arXiv.2512.23864
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown remarkable generalization by mapping web-scale knowledge to robotic control, yet they remain blind to physical contact. Consequently, they struggle with contact-rich manipulation tasks that require reasoning about force, texture, and slip. While some approaches incorporate low-dimensional tactile signals, they fail to capture the high-resolution dynamics essential for such interactions. To address this limitation, we introduce DreamTacVLA, a framework that grounds VLA models in contact physics by learning to feel the future. Our model adopts a hierarchical perception scheme in which high-resolution tactile images serve as micro-vision inputs coupled with wrist-camera local vision and third-person macro vision. To reconcile these multi-scale sensory streams, we first train a unified policy with a Hierarchical Spatial Alignment (HSA) loss that aligns tactile tokens with their spatial counterparts in the wrist and third-person views. To further deepen the model's understanding of fine-grained contact dynamics, we finetune the system with a tactile world model that predicts future tactile signals. To mitigate tactile data scarcity and the wear-prone nature of tactile sensors, we construct a hybrid large-scale dataset sourced from both high-fidelity digital twin and real-world experiments. By anticipating upcoming tactile states, DreamTacVLA acquires a rich model of contact physics and conditions its actions on both real observations and imagined consequences. Across contact-rich manipulation tasks, it outperforms state-of-the-art VLA baselines, achieving up to 95% success, highlighting the importance of understanding physical contact for robust, touch-aware robotic agents.

## 核心内容
Vision-Language-Action (VLA) models have shown remarkable generalization by mapping web-scale knowledge to robotic control, yet they remain blind to physical contact. Consequently, they struggle with contact-rich manipulation tasks that require reasoning about force, texture, and slip. While some approaches incorporate low-dimensional tactile signals, they fail to capture the high-resolution dynamics essential for such interactions. To address this limitation, we introduce DreamTacVLA, a framework that grounds VLA models in contact physics by learning to feel the future. Our model adopts a hierarchical perception scheme in which high-resolution tactile images serve as micro-vision inputs coupled with wrist-camera local vision and third-person macro vision. To reconcile these multi-scale sensory streams, we first train a unified policy with a Hierarchical Spatial Alignment (HSA) loss that aligns tactile tokens with their spatial counterparts in the wrist and third-person views. To further deepen the model's understanding of fine-grained contact dynamics, we finetune the system with a tactile world model that predicts future tactile signals. To mitigate tactile data scarcity and the wear-prone nature of tactile sensors, we construct a hybrid large-scale dataset sourced from both high-fidelity digital twin and real-world experiments. By anticipating upcoming tactile states, DreamTacVLA acquires a rich model of contact physics and conditions its actions on both real observations and imagined consequences. Across contact-rich manipulation tasks, it outperforms state-of-the-art VLA baselines, achieving up to 95% success, highlighting the importance of understanding physical contact for robust, touch-aware robotic agents.

## 参考
- http://arxiv.org/abs/2512.23864v4

## Overview
Vision-Language-Action (VLA) models have shown remarkable generalization by mapping web-scale knowledge to robotic control, yet they remain blind to physical contact. Consequently, they struggle with contact-rich manipulation tasks that require reasoning about force, texture, and slip. While some approaches incorporate low-dimensional tactile signals, they fail to capture the high-resolution dynamics essential for such interactions. To address this limitation, we introduce DreamTacVLA, a framework that grounds VLA models in contact physics by learning to feel the future. Our model adopts a hierarchical perception scheme in which high-resolution tactile images serve as micro-vision inputs coupled with wrist-camera local vision and third-person macro vision. To reconcile these multi-scale sensory streams, we first train a unified policy with a Hierarchical Spatial Alignment (HSA) loss that aligns tactile tokens with their spatial counterparts in the wrist and third-person views. To further deepen the model's understanding of fine-grained contact dynamics, we finetune the system with a tactile world model that predicts future tactile signals. To mitigate tactile data scarcity and the wear-prone nature of tactile sensors, we construct a hybrid large-scale dataset sourced from both high-fidelity digital twin and real-world experiments. By anticipating upcoming tactile states, DreamTacVLA acquires a rich model of contact physics and conditions its actions on both real observations and imagined consequences. Across contact-rich manipulation tasks, it outperforms state-of-the-art VLA baselines, achieving up to 95% success, highlighting the importance of understanding physical contact for robust, touch-aware robotic agents.

## Content
Vision-Language-Action (VLA) models have shown remarkable generalization by mapping web-scale knowledge to robotic control, yet they remain blind to physical contact. Consequently, they struggle with contact-rich manipulation tasks that require reasoning about force, texture, and slip. While some approaches incorporate low-dimensional tactile signals, they fail to capture the high-resolution dynamics essential for such interactions. To address this limitation, we introduce DreamTacVLA, a framework that grounds VLA models in contact physics by learning to feel the future. Our model adopts a hierarchical perception scheme in which high-resolution tactile images serve as micro-vision inputs coupled with wrist-camera local vision and third-person macro vision. To reconcile these multi-scale sensory streams, we first train a unified policy with a Hierarchical Spatial Alignment (HSA) loss that aligns tactile tokens with their spatial counterparts in the wrist and third-person views. To further deepen the model's understanding of fine-grained contact dynamics, we finetune the system with a tactile world model that predicts future tactile signals. To mitigate tactile data scarcity and the wear-prone nature of tactile sensors, we construct a hybrid large-scale dataset sourced from both high-fidelity digital twin and real-world experiments. By anticipating upcoming tactile states, DreamTacVLA acquires a rich model of contact physics and conditions its actions on both real observations and imagined consequences. Across contact-rich manipulation tasks, it outperforms state-of-the-art VLA baselines, achieving up to 95% success, highlighting the importance of understanding physical contact for robust, touch-aware robotic agents.

## 개요
Vision-Language-Action (VLA) 모델은 웹 규모의 지식을 로봇 제어에 매핑하여 놀라운 일반화 능력을 보여주었지만, 물리적 접촉에는 여전히 무지합니다. 결과적으로, 힘, 질감, 미끄러짐에 대한 추론이 필요한 접촉이 많은 조작 작업에 어려움을 겪습니다. 일부 접근 방식은 저차원 촉각 신호를 통합하지만, 이러한 상호작용에 필수적인 고해상도 동역학을 포착하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 미래를 느끼는 학습을 통해 VLA 모델을 접촉 물리학에 기반하는 프레임워크인 DreamTacVLA를 소개합니다. 우리 모델은 고해상도 촉각 이미지를 손목 카메라의 로컬 비전 및 3인칭 매크로 비전과 결합된 마이크로 비전 입력으로 사용하는 계층적 인식 방식을 채택합니다. 이러한 다중 스케일 감각 스트림을 조화시키기 위해, 먼저 촉각 토큰을 손목 및 3인칭 뷰의 공간적 대응물과 정렬하는 계층적 공간 정렬(HSA) 손실로 통합 정책을 훈련합니다. 미세한 접촉 동역학에 대한 모델의 이해를 더욱 심화하기 위해, 미래 촉각 신호를 예측하는 촉각 세계 모델로 시스템을 미세 조정합니다. 촉각 데이터 부족과 촉각 센서의 마모 특성을 완화하기 위해, 고충실도 디지털 트윈과 실제 실험에서 얻은 하이브리드 대규모 데이터셋을 구축합니다. 다가오는 촉각 상태를 예측함으로써, DreamTacVLA는 풍부한 접촉 물리학 모델을 획득하고 실제 관찰과 상상된 결과 모두에 따라 행동을 조건화합니다. 접촉이 많은 조작 작업에서 최첨단 VLA 기준선을 능가하며 최대 95%의 성공률을 달성하여, 강건하고 촉각 인식이 가능한 로봇 에이전트를 위한 물리적 접촉 이해의 중요성을 강조합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 웹 규모의 지식을 로봇 제어에 매핑하여 놀라운 일반화 능력을 보여주었지만, 물리적 접촉에는 여전히 무지합니다. 결과적으로, 힘, 질감, 미끄러짐에 대한 추론이 필요한 접촉이 많은 조작 작업에 어려움을 겪습니다. 일부 접근 방식은 저차원 촉각 신호를 통합하지만, 이러한 상호작용에 필수적인 고해상도 동역학을 포착하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 미래를 느끼는 학습을 통해 VLA 모델을 접촉 물리학에 기반하는 프레임워크인 DreamTacVLA를 소개합니다. 우리 모델은 고해상도 촉각 이미지를 손목 카메라의 로컬 비전 및 3인칭 매크로 비전과 결합된 마이크로 비전 입력으로 사용하는 계층적 인식 방식을 채택합니다. 이러한 다중 스케일 감각 스트림을 조화시키기 위해, 먼저 촉각 토큰을 손목 및 3인칭 뷰의 공간적 대응물과 정렬하는 계층적 공간 정렬(HSA) 손실로 통합 정책을 훈련합니다. 미세한 접촉 동역학에 대한 모델의 이해를 더욱 심화하기 위해, 미래 촉각 신호를 예측하는 촉각 세계 모델로 시스템을 미세 조정합니다. 촉각 데이터 부족과 촉각 센서의 마모 특성을 완화하기 위해, 고충실도 디지털 트윈과 실제 실험에서 얻은 하이브리드 대규모 데이터셋을 구축합니다. 다가오는 촉각 상태를 예측함으로써, DreamTacVLA는 풍부한 접촉 물리학 모델을 획득하고 실제 관찰과 상상된 결과 모두에 따라 행동을 조건화합니다. 접촉이 많은 조작 작업에서 최첨단 VLA 기준선을 능가하며 최대 95%의 성공률을 달성하여, 강건하고 촉각 인식이 가능한 로봇 에이전트를 위한 물리적 접촉 이해의 중요성을 강조합니다.
