---
$id: ent_paper_vo_clutter_resistant_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding
  zh: OBEYED-VLA
  ko: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding
summary:
  en: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding (OBEYED-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Arkansas.
  zh: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding (OBEYED-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Arkansas.
  ko: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding (OBEYED-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Arkansas.
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
- obeyed_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22519v2.
sources:
- id: src_001
  type: paper
  title: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding (arXiv)
  url: https://arxiv.org/abs/2512.22519
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OBEYED-VLA source
  url: https://doi.org/10.48550/arXiv.2512.22519
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent Vision-Language-Action (VLA) models have made impressive progress toward general-purpose robotic manipulation by post-training large Vision-Language Models (VLMs) for action prediction. Yet most VLAs entangle perception and control in a monolithic pipeline optimized purely for action, which can erode language-conditioned grounding. In our real-world tabletop tests, policies over-grasp when the target is absent, are distracted by clutter, and overfit to background appearance.   To address these issues, we propose OBEYED-VLA (OBject-centric and gEometrY groundED VLA), a framework that explicitly disentangles perceptual grounding from action reasoning. Instead of operating directly on raw RGB, OBEYED-VLA augments VLAs with a perception module that grounds multi-view inputs into task-conditioned, object-centric, and geometry-aware observations. This module includes a VLM-based object-centric grounding stage that selects task-relevant object regions across camera views, along with a complementary geometric grounding stage that emphasizes the 3D structure of these objects over their appearance. The resulting grounded views are then fed to a pretrained VLA policy, which we fine-tune exclusively on single-object demonstrations collected without environmental clutter or non-target objects.   On a real-world UR10e tabletop setup, OBEYED-VLA substantially improves robustness over strong VLA baselines across four challenging regimes and multiple difficulty levels: distractor objects, absent-target rejection, background appearance changes, and cluttered manipulation of unseen objects. Ablation studies confirm that both semantic grounding and geometry-aware grounding are critical to these gains. Overall, the results indicate that making perception an explicit, object-centric component is an effective way to strengthen and generalize VLA-based robotic manipulation.

## 核心内容
Recent Vision-Language-Action (VLA) models have made impressive progress toward general-purpose robotic manipulation by post-training large Vision-Language Models (VLMs) for action prediction. Yet most VLAs entangle perception and control in a monolithic pipeline optimized purely for action, which can erode language-conditioned grounding. In our real-world tabletop tests, policies over-grasp when the target is absent, are distracted by clutter, and overfit to background appearance.   To address these issues, we propose OBEYED-VLA (OBject-centric and gEometrY groundED VLA), a framework that explicitly disentangles perceptual grounding from action reasoning. Instead of operating directly on raw RGB, OBEYED-VLA augments VLAs with a perception module that grounds multi-view inputs into task-conditioned, object-centric, and geometry-aware observations. This module includes a VLM-based object-centric grounding stage that selects task-relevant object regions across camera views, along with a complementary geometric grounding stage that emphasizes the 3D structure of these objects over their appearance. The resulting grounded views are then fed to a pretrained VLA policy, which we fine-tune exclusively on single-object demonstrations collected without environmental clutter or non-target objects.   On a real-world UR10e tabletop setup, OBEYED-VLA substantially improves robustness over strong VLA baselines across four challenging regimes and multiple difficulty levels: distractor objects, absent-target rejection, background appearance changes, and cluttered manipulation of unseen objects. Ablation studies confirm that both semantic grounding and geometry-aware grounding are critical to these gains. Overall, the results indicate that making perception an explicit, object-centric component is an effective way to strengthen and generalize VLA-based robotic manipulation.

## 参考
- http://arxiv.org/abs/2512.22519v2

## Overview
Recent Vision-Language-Action (VLA) models have made impressive progress toward general-purpose robotic manipulation by post-training large Vision-Language Models (VLMs) for action prediction. Yet most VLAs entangle perception and control in a monolithic pipeline optimized purely for action, which can erode language-conditioned grounding. In our real-world tabletop tests, policies over-grasp when the target is absent, are distracted by clutter, and overfit to background appearance. To address these issues, we propose OBEYED-VLA (OBject-centric and gEometrY groundED VLA), a framework that explicitly disentangles perceptual grounding from action reasoning. Instead of operating directly on raw RGB, OBEYED-VLA augments VLAs with a perception module that grounds multi-view inputs into task-conditioned, object-centric, and geometry-aware observations. This module includes a VLM-based object-centric grounding stage that selects task-relevant object regions across camera views, along with a complementary geometric grounding stage that emphasizes the 3D structure of these objects over their appearance. The resulting grounded views are then fed to a pretrained VLA policy, which we fine-tune exclusively on single-object demonstrations collected without environmental clutter or non-target objects. On a real-world UR10e tabletop setup, OBEYED-VLA substantially improves robustness over strong VLA baselines across four challenging regimes and multiple difficulty levels: distractor objects, absent-target rejection, background appearance changes, and cluttered manipulation of unseen objects. Ablation studies confirm that both semantic grounding and geometry-aware grounding are critical to these gains. Overall, the results indicate that making perception an explicit, object-centric component is an effective way to strengthen and generalize VLA-based robotic manipulation.

## Content
Recent Vision-Language-Action (VLA) models have made impressive progress toward general-purpose robotic manipulation by post-training large Vision-Language Models (VLMs) for action prediction. Yet most VLAs entangle perception and control in a monolithic pipeline optimized purely for action, which can erode language-conditioned grounding. In our real-world tabletop tests, policies over-grasp when the target is absent, are distracted by clutter, and overfit to background appearance. To address these issues, we propose OBEYED-VLA (OBject-centric and gEometrY groundED VLA), a framework that explicitly disentangles perceptual grounding from action reasoning. Instead of operating directly on raw RGB, OBEYED-VLA augments VLAs with a perception module that grounds multi-view inputs into task-conditioned, object-centric, and geometry-aware observations. This module includes a VLM-based object-centric grounding stage that selects task-relevant object regions across camera views, along with a complementary geometric grounding stage that emphasizes the 3D structure of these objects over their appearance. The resulting grounded views are then fed to a pretrained VLA policy, which we fine-tune exclusively on single-object demonstrations collected without environmental clutter or non-target objects. On a real-world UR10e tabletop setup, OBEYED-VLA substantially improves robustness over strong VLA baselines across four challenging regimes and multiple difficulty levels: distractor objects, absent-target rejection, background appearance changes, and cluttered manipulation of unseen objects. Ablation studies confirm that both semantic grounding and geometry-aware grounding are critical to these gains. Overall, the results indicate that making perception an explicit, object-centric component is an effective way to strengthen and generalize VLA-based robotic manipulation.

## 개요
최근 Vision-Language-Action(VLA) 모델은 대규모 Vision-Language Model(VLM)을 행동 예측을 위해 후속 학습(post-training)함으로써 범용 로봇 조작 분야에서 인상적인 진전을 이루었습니다. 그러나 대부분의 VLA는 순수하게 행동에 최적화된 단일 파이프라인에서 인식과 제어를 얽어매어, 언어 조건부 접지(grounding)를 약화시킬 수 있습니다. 실제 탁상 실험에서 정책은 대상이 없을 때 과도하게 잡으려 하고, 잡동사니에 주의가 산만해지며, 배경 외관에 과적합되는 현상을 보였습니다.  
이러한 문제를 해결하기 위해, 우리는 OBEYED-VLA(OBject-centric and gEometrY groundED VLA)를 제안합니다. 이 프레임워크는 인식 접지(perceptual grounding)와 행동 추론(action reasoning)을 명시적으로 분리합니다. OBEYED-VLA는 원시 RGB를 직접 처리하는 대신, 다중 뷰 입력을 작업 조건부, 객체 중심, 기하학 인식 관측으로 접지하는 인식 모듈로 VLA를 보강합니다. 이 모듈은 카메라 뷰 전체에서 작업 관련 객체 영역을 선택하는 VLM 기반 객체 중심 접지 단계와, 이러한 객체의 외관보다 3D 구조를 강조하는 보완적 기하학 접지 단계를 포함합니다. 결과적으로 생성된 접지된 뷰는 사전 학습된 VLA 정책에 입력되며, 이 정책은 환경 잡동사니나 비대상 객체 없이 수집된 단일 객체 시연 데이터로만 미세 조정됩니다.  
실제 UR10e 탁상 설정에서 OBEYED-VLA는 네 가지 도전적 영역과 여러 난이도 수준(방해 객체, 부재 대상 거부, 배경 외관 변화, 보지 못한 객체의 잡동사니 조작)에서 강력한 VLA 기준선 대비 견고성을 크게 향상시킵니다. 절제 연구는 의미적 접지와 기하학 인식 접지 모두가 이러한 성과에 중요함을 확인합니다. 전반적으로, 결과는 인식을 명시적이고 객체 중심적인 구성 요소로 만드는 것이 VLA 기반 로봇 조작을 강화하고 일반화하는 효과적인 방법임을 시사합니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델은 대규모 Vision-Language Model(VLM)을 행동 예측을 위해 후속 학습함으로써 범용 로봇 조작 분야에서 인상적인 진전을 이루었습니다. 그러나 대부분의 VLA는 순수하게 행동에 최적화된 단일 파이프라인에서 인식과 제어를 얽어매어, 언어 조건부 접지를 약화시킬 수 있습니다. 실제 탁상 실험에서 정책은 대상이 없을 때 과도하게 잡으려 하고, 잡동사니에 주의가 산만해지며, 배경 외관에 과적합되는 현상을 보였습니다.  
이러한 문제를 해결하기 위해, 우리는 OBEYED-VLA(OBject-centric and gEometrY groundED VLA)를 제안합니다. 이 프레임워크는 인식 접지와 행동 추론을 명시적으로 분리합니다. OBEYED-VLA는 원시 RGB를 직접 처리하는 대신, 다중 뷰 입력을 작업 조건부, 객체 중심, 기하학 인식 관측으로 접지하는 인식 모듈로 VLA를 보강합니다. 이 모듈은 카메라 뷰 전체에서 작업 관련 객체 영역을 선택하는 VLM 기반 객체 중심 접지 단계와, 이러한 객체의 외관보다 3D 구조를 강조하는 보완적 기하학 접지 단계를 포함합니다. 결과적으로 생성된 접지된 뷰는 사전 학습된 VLA 정책에 입력되며, 이 정책은 환경 잡동사니나 비대상 객체 없이 수집된 단일 객체 시연 데이터로만 미세 조정됩니다.  
실제 UR10e 탁상 설정에서 OBEYED-VLA는 네 가지 도전적 영역과 여러 난이도 수준(방해 객체, 부재 대상 거부, 배경 외관 변화, 보지 못한 객체의 잡동사니 조작)에서 강력한 VLA 기준선 대비 견고성을 크게 향상시킵니다. 절제 연구는 의미적 접지와 기하학 인식 접지 모두가 이러한 성과에 중요함을 확인합니다. 전반적으로, 결과는 인식을 명시적이고 객체 중심적인 구성 요소로 만드는 것이 VLA 기반 로봇 조작을 강화하고 일반화하는 효과적인 방법임을 시사합니다.
