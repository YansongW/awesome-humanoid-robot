---
$id: ent_paper_lee_bring_my_cup_personalizing_vis_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
  zh: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
  ko: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
summary:
  en: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (Bring My Cup Personalizing
    Vision-Language-Action Models with Visual Attentive Prompting), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by POSTECH, GSAI, IME, dblab.
  zh: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (Bring My Cup Personalizing
    Vision-Language-Action Models with Visual Attentive Prompting), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by POSTECH, GSAI, IME, dblab.
  ko: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (Bring My Cup Personalizing
    Vision-Language-Action Models with Visual Attentive Prompting), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by POSTECH, GSAI, IME, dblab.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bring_my_cup_personalizing_vis
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20014v3.
sources:
- id: src_001
  type: paper
  title: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (arXiv)
  url: https://arxiv.org/abs/2512.20014
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting source
  url: https://doi.org/10.48550/arXiv.2512.20014
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.

## 核心内容
While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.

## 参考
- http://arxiv.org/abs/2512.20014v3

## Overview
While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.

## Content
While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.

## 개요
Vision-Language-Action(VLA) 모델은 일반적인 명령에 대해 잘 일반화되지만, "내 컵 가져와"와 같은 개인화된 명령에서는 어려움을 겪습니다. 이 경우 로봇은 시각적으로 유사한 객체들 중에서 특정 하나의 객체에 대해 행동해야 합니다. 본 연구에서는 VLA가 훈련 중에 보지 못한 사용자 특정 객체를 단 몇 장의 참조 이미지만으로 식별하고 제어해야 하는 개인 객체 조작 설정을 다룹니다. 이 문제를 해결하기 위해, 우리는 Visual Attentive Prompting(VAP)을 제안합니다. 이는 간단하면서도 효과적인 훈련 없는 지각 어댑터로, 고정된 VLA에 하향식 선택적 주의를 부여합니다. VAP는 참조 이미지를 비모수적 시각 메모리로 취급하고, 개방형 어휘 탐지 및 임베딩 기반 매칭을 통해 장면 내 개인 객체를 접지한 후, 객체를 강조하고 명령을 재작성하여 이 접지를 시각적 프롬프트로 주입합니다. 우리는 Personalized-SIMPLER 및 Personalized-VLABench라는 두 가지 시뮬레이션 벤치마크와 실제 탁상용 벤치마크를 구축하여 여러 로봇과 작업에서 개인화된 조작을 평가합니다. 실험 결과, VAP는 성공률과 올바른 객체 조작 모두에서 일반 정책 및 토큰 학습 기준선을 일관되게 능가하며, 의미 이해와 인스턴스 수준 제어 간의 격차를 해소하는 데 기여합니다.

## 핵심 내용
Vision-Language-Action(VLA) 모델은 일반적인 명령에 대해 잘 일반화되지만, "내 컵 가져와"와 같은 개인화된 명령에서는 어려움을 겪습니다. 이 경우 로봇은 시각적으로 유사한 객체들 중에서 특정 하나의 객체에 대해 행동해야 합니다. 본 연구에서는 VLA가 훈련 중에 보지 못한 사용자 특정 객체를 단 몇 장의 참조 이미지만으로 식별하고 제어해야 하는 개인 객체 조작 설정을 다룹니다. 이 문제를 해결하기 위해, 우리는 Visual Attentive Prompting(VAP)을 제안합니다. 이는 간단하면서도 효과적인 훈련 없는 지각 어댑터로, 고정된 VLA에 하향식 선택적 주의를 부여합니다. VAP는 참조 이미지를 비모수적 시각 메모리로 취급하고, 개방형 어휘 탐지 및 임베딩 기반 매칭을 통해 장면 내 개인 객체를 접지한 후, 객체를 강조하고 명령을 재작성하여 이 접지를 시각적 프롬프트로 주입합니다. 우리는 Personalized-SIMPLER 및 Personalized-VLABench라는 두 가지 시뮬레이션 벤치마크와 실제 탁상용 벤치마크를 구축하여 여러 로봇과 작업에서 개인화된 조작을 평가합니다. 실험 결과, VAP는 성공률과 올바른 객체 조작 모두에서 일반 정책 및 토큰 학습 기준선을 일관되게 능가하며, 의미 이해와 인스턴스 수준 제어 간의 격차를 해소하는 데 기여합니다.
