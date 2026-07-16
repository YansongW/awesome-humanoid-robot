---
$id: ent_paper_lv_f1_a_vision_language_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions'
  zh: F1
  ko: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions'
summary:
  en: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions (F1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Harbin Institute of Technology (Shenzhen).'
  zh: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions (F1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Harbin Institute of Technology (Shenzhen).'
  ko: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions (F1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Harbin Institute of Technology (Shenzhen).'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- f1
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.06951v2.
sources:
- id: src_001
  type: paper
  title: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions (arXiv)'
  url: https://arxiv.org/abs/2509.06951
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: F1 source
  url: https://doi.org/10.48550/arXiv.2509.06951
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Executing language-conditioned tasks in dynamic visual environments remains a central challenge in embodied AI. Existing Vision-Language-Action (VLA) models predominantly adopt reactive state-to-action mappings, often leading to short-sighted behaviors and poor robustness in dynamic scenes. In this paper, we introduce F1, a pretrained VLA framework which integrates the visual foresight generation into decision-making pipeline. F1 adopts a Mixture-of-Transformer architecture with dedicated modules for perception, foresight generation, and control, thereby bridging understanding, generation, and actions. At its core, F1 employs a next-scale prediction mechanism to synthesize goal-conditioned visual foresight as explicit planning targets. By forecasting plausible future visual states, F1 reformulates action generation as a foresight-guided inverse dynamics problem, enabling actions that implicitly achieve visual goals. To endow F1 with robust and generalizable capabilities, we propose a three-stage training recipe on an extensive dataset comprising over 330k trajectories across 136 diverse tasks. This training scheme enhances modular reasoning and equips the model with transferable visual foresight, which is critical for complex and dynamic environments. Extensive evaluations on real-world tasks and simulation benchmarks demonstrate F1 consistently outperforms existing approaches, achieving substantial gains in both task success rate and generalization ability.

## 核心内容
Executing language-conditioned tasks in dynamic visual environments remains a central challenge in embodied AI. Existing Vision-Language-Action (VLA) models predominantly adopt reactive state-to-action mappings, often leading to short-sighted behaviors and poor robustness in dynamic scenes. In this paper, we introduce F1, a pretrained VLA framework which integrates the visual foresight generation into decision-making pipeline. F1 adopts a Mixture-of-Transformer architecture with dedicated modules for perception, foresight generation, and control, thereby bridging understanding, generation, and actions. At its core, F1 employs a next-scale prediction mechanism to synthesize goal-conditioned visual foresight as explicit planning targets. By forecasting plausible future visual states, F1 reformulates action generation as a foresight-guided inverse dynamics problem, enabling actions that implicitly achieve visual goals. To endow F1 with robust and generalizable capabilities, we propose a three-stage training recipe on an extensive dataset comprising over 330k trajectories across 136 diverse tasks. This training scheme enhances modular reasoning and equips the model with transferable visual foresight, which is critical for complex and dynamic environments. Extensive evaluations on real-world tasks and simulation benchmarks demonstrate F1 consistently outperforms existing approaches, achieving substantial gains in both task success rate and generalization ability.

## 参考
- http://arxiv.org/abs/2509.06951v2

## Overview
Executing language-conditioned tasks in dynamic visual environments remains a central challenge in embodied AI. Existing Vision-Language-Action (VLA) models predominantly adopt reactive state-to-action mappings, often leading to short-sighted behaviors and poor robustness in dynamic scenes. In this paper, we introduce F1, a pretrained VLA framework which integrates the visual foresight generation into decision-making pipeline. F1 adopts a Mixture-of-Transformer architecture with dedicated modules for perception, foresight generation, and control, thereby bridging understanding, generation, and actions. At its core, F1 employs a next-scale prediction mechanism to synthesize goal-conditioned visual foresight as explicit planning targets. By forecasting plausible future visual states, F1 reformulates action generation as a foresight-guided inverse dynamics problem, enabling actions that implicitly achieve visual goals. To endow F1 with robust and generalizable capabilities, we propose a three-stage training recipe on an extensive dataset comprising over 330k trajectories across 136 diverse tasks. This training scheme enhances modular reasoning and equips the model with transferable visual foresight, which is critical for complex and dynamic environments. Extensive evaluations on real-world tasks and simulation benchmarks demonstrate F1 consistently outperforms existing approaches, achieving substantial gains in both task success rate and generalization ability.

## Content
Executing language-conditioned tasks in dynamic visual environments remains a central challenge in embodied AI. Existing Vision-Language-Action (VLA) models predominantly adopt reactive state-to-action mappings, often leading to short-sighted behaviors and poor robustness in dynamic scenes. In this paper, we introduce F1, a pretrained VLA framework which integrates the visual foresight generation into decision-making pipeline. F1 adopts a Mixture-of-Transformer architecture with dedicated modules for perception, foresight generation, and control, thereby bridging understanding, generation, and actions. At its core, F1 employs a next-scale prediction mechanism to synthesize goal-conditioned visual foresight as explicit planning targets. By forecasting plausible future visual states, F1 reformulates action generation as a foresight-guided inverse dynamics problem, enabling actions that implicitly achieve visual goals. To endow F1 with robust and generalizable capabilities, we propose a three-stage training recipe on an extensive dataset comprising over 330k trajectories across 136 diverse tasks. This training scheme enhances modular reasoning and equips the model with transferable visual foresight, which is critical for complex and dynamic environments. Extensive evaluations on real-world tasks and simulation benchmarks demonstrate F1 consistently outperforms existing approaches, achieving substantial gains in both task success rate and generalization ability.

## 개요
동적 시각 환경에서 언어 조건화된 작업을 실행하는 것은 임베디드 AI의 핵심 과제로 남아 있습니다. 기존의 Vision-Language-Action(VLA) 모델은 주로 반응적 상태-행동 매핑을 채택하여 동적 장면에서 근시안적 행동과 낮은 견고성을 초래하는 경우가 많습니다. 본 논문에서는 의사 결정 파이프라인에 시각적 예측 생성을 통합한 사전 학습된 VLA 프레임워크인 F1을 소개합니다. F1은 인식, 예측 생성 및 제어를 위한 전용 모듈을 갖춘 Mixture-of-Transformer 아키텍처를 채택하여 이해, 생성 및 행동을 연결합니다. 핵심적으로 F1은 다음 스케일 예측 메커니즘을 사용하여 목표 조건화된 시각적 예측을 명시적 계획 목표로 합성합니다. 가능한 미래 시각 상태를 예측함으로써 F1은 행동 생성을 예측 기반 역동역학 문제로 재구성하여 시각적 목표를 암시적으로 달성하는 행동을 가능하게 합니다. F1에 강력하고 일반화 가능한 능력을 부여하기 위해 136개의 다양한 작업에 걸쳐 330k 이상의 궤적으로 구성된 광범위한 데이터셋에서 3단계 훈련 레시피를 제안합니다. 이 훈련 방식은 모듈식 추론을 강화하고 복잡하고 동적인 환경에 중요한 전이 가능한 시각적 예측을 모델에 부여합니다. 실제 작업 및 시뮬레이션 벤치마크에 대한 광범위한 평가는 F1이 기존 접근 방식을 일관되게 능가하며 작업 성공률과 일반화 능력 모두에서 상당한 향상을 달성함을 보여줍니다.

## 핵심 내용
동적 시각 환경에서 언어 조건화된 작업을 실행하는 것은 임베디드 AI의 핵심 과제로 남아 있습니다. 기존의 Vision-Language-Action(VLA) 모델은 주로 반응적 상태-행동 매핑을 채택하여 동적 장면에서 근시안적 행동과 낮은 견고성을 초래하는 경우가 많습니다. 본 논문에서는 의사 결정 파이프라인에 시각적 예측 생성을 통합한 사전 학습된 VLA 프레임워크인 F1을 소개합니다. F1은 인식, 예측 생성 및 제어를 위한 전용 모듈을 갖춘 Mixture-of-Transformer 아키텍처를 채택하여 이해, 생성 및 행동을 연결합니다. 핵심적으로 F1은 다음 스케일 예측 메커니즘을 사용하여 목표 조건화된 시각적 예측을 명시적 계획 목표로 합성합니다. 가능한 미래 시각 상태를 예측함으로써 F1은 행동 생성을 예측 기반 역동역학 문제로 재구성하여 시각적 목표를 암시적으로 달성하는 행동을 가능하게 합니다. F1에 강력하고 일반화 가능한 능력을 부여하기 위해 136개의 다양한 작업에 걸쳐 330k 이상의 궤적으로 구성된 광범위한 데이터셋에서 3단계 훈련 레시피를 제안합니다. 이 훈련 방식은 모듈식 추론을 강화하고 복잡하고 동적인 환경에 중요한 전이 가능한 시각적 예측을 모델에 부여합니다. 실제 작업 및 시뮬레이션 벤치마크에 대한 광범위한 평가는 F1이 기존 접근 방식을 일관되게 능가하며 작업 성공률과 일반화 능력 모두에서 상당한 향상을 달성함을 보여줍니다.
