---
$id: ent_paper_chen_internvla_m1_a_spatially_guide_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy'
  zh: InternVLA-M1
  ko: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy'
summary:
  en: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (InternVLA-M1), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Intern Robotics, Shanghai AI Laboratory.'
  zh: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (InternVLA-M1), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Intern Robotics, Shanghai AI Laboratory.'
  ko: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (InternVLA-M1), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Intern Robotics, Shanghai AI Laboratory.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- internvla_m1
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13778v1.
sources:
- id: src_001
  type: paper
  title: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (arXiv)'
  url: https://arxiv.org/abs/2510.13778
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: InternVLA-M1 source
  url: https://doi.org/10.48550/arXiv.2510.13778
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce InternVLA-M1, a unified framework for spatial grounding and robot control that advances instruction-following robots toward scalable, general-purpose intelligence. Its core idea is spatially guided vision-language-action training, where spatial grounding serves as the critical link between instructions and robot actions. InternVLA-M1 employs a two-stage pipeline: (i) spatial grounding pre-training on over 2.3M spatial reasoning data to determine ``where to act'' by aligning instructions with visual, embodiment-agnostic positions, and (ii) spatially guided action post-training to decide ``how to act'' by generating embodiment-aware actions through plug-and-play spatial prompting. This spatially guided training recipe yields consistent gains: InternVLA-M1 outperforms its variant without spatial guidance by +14.6% on SimplerEnv Google Robot, +17% on WidowX, and +4.3% on LIBERO Franka, while demonstrating stronger spatial reasoning capability in box, point, and trace prediction. To further scale instruction following, we built a simulation engine to collect 244K generalizable pick-and-place episodes, enabling a 6.2% average improvement across 200 tasks and 3K+ objects. In real-world clustered pick-and-place, InternVLA-M1 improved by 7.3%, and with synthetic co-training, achieved +20.6% on unseen objects and novel configurations. Moreover, in long-horizon reasoning-intensive scenarios, it surpassed existing works by over 10%. These results highlight spatially guided training as a unifying principle for scalable and resilient generalist robots. Code and models are available at https://github.com/InternRobotics/InternVLA-M1.

## 核心内容
We introduce InternVLA-M1, a unified framework for spatial grounding and robot control that advances instruction-following robots toward scalable, general-purpose intelligence. Its core idea is spatially guided vision-language-action training, where spatial grounding serves as the critical link between instructions and robot actions. InternVLA-M1 employs a two-stage pipeline: (i) spatial grounding pre-training on over 2.3M spatial reasoning data to determine ``where to act'' by aligning instructions with visual, embodiment-agnostic positions, and (ii) spatially guided action post-training to decide ``how to act'' by generating embodiment-aware actions through plug-and-play spatial prompting. This spatially guided training recipe yields consistent gains: InternVLA-M1 outperforms its variant without spatial guidance by +14.6% on SimplerEnv Google Robot, +17% on WidowX, and +4.3% on LIBERO Franka, while demonstrating stronger spatial reasoning capability in box, point, and trace prediction. To further scale instruction following, we built a simulation engine to collect 244K generalizable pick-and-place episodes, enabling a 6.2% average improvement across 200 tasks and 3K+ objects. In real-world clustered pick-and-place, InternVLA-M1 improved by 7.3%, and with synthetic co-training, achieved +20.6% on unseen objects and novel configurations. Moreover, in long-horizon reasoning-intensive scenarios, it surpassed existing works by over 10%. These results highlight spatially guided training as a unifying principle for scalable and resilient generalist robots. Code and models are available at https://github.com/InternRobotics/InternVLA-M1.

## 参考
- http://arxiv.org/abs/2510.13778v1

## Overview
We introduce InternVLA-M1, a unified framework for spatial grounding and robot control that advances instruction-following robots toward scalable, general-purpose intelligence. Its core idea is spatially guided vision-language-action training, where spatial grounding serves as the critical link between instructions and robot actions. InternVLA-M1 employs a two-stage pipeline: (i) spatial grounding pre-training on over 2.3M spatial reasoning data to determine ``where to act'' by aligning instructions with visual, embodiment-agnostic positions, and (ii) spatially guided action post-training to decide ``how to act'' by generating embodiment-aware actions through plug-and-play spatial prompting. This spatially guided training recipe yields consistent gains: InternVLA-M1 outperforms its variant without spatial guidance by +14.6% on SimplerEnv Google Robot, +17% on WidowX, and +4.3% on LIBERO Franka, while demonstrating stronger spatial reasoning capability in box, point, and trace prediction. To further scale instruction following, we built a simulation engine to collect 244K generalizable pick-and-place episodes, enabling a 6.2% average improvement across 200 tasks and 3K+ objects. In real-world clustered pick-and-place, InternVLA-M1 improved by 7.3%, and with synthetic co-training, achieved +20.6% on unseen objects and novel configurations. Moreover, in long-horizon reasoning-intensive scenarios, it surpassed existing works by over 10%. These results highlight spatially guided training as a unifying principle for scalable and resilient generalist robots. Code and models are available at https://github.com/InternRobotics/InternVLA-M1.

## Content
We introduce InternVLA-M1, a unified framework for spatial grounding and robot control that advances instruction-following robots toward scalable, general-purpose intelligence. Its core idea is spatially guided vision-language-action training, where spatial grounding serves as the critical link between instructions and robot actions. InternVLA-M1 employs a two-stage pipeline: (i) spatial grounding pre-training on over 2.3M spatial reasoning data to determine ``where to act'' by aligning instructions with visual, embodiment-agnostic positions, and (ii) spatially guided action post-training to decide ``how to act'' by generating embodiment-aware actions through plug-and-play spatial prompting. This spatially guided training recipe yields consistent gains: InternVLA-M1 outperforms its variant without spatial guidance by +14.6% on SimplerEnv Google Robot, +17% on WidowX, and +4.3% on LIBERO Franka, while demonstrating stronger spatial reasoning capability in box, point, and trace prediction. To further scale instruction following, we built a simulation engine to collect 244K generalizable pick-and-place episodes, enabling a 6.2% average improvement across 200 tasks and 3K+ objects. In real-world clustered pick-and-place, InternVLA-M1 improved by 7.3%, and with synthetic co-training, achieved +20.6% on unseen objects and novel configurations. Moreover, in long-horizon reasoning-intensive scenarios, it surpassed existing works by over 10%. These results highlight spatially guided training as a unifying principle for scalable and resilient generalist robots. Code and models are available at https://github.com/InternRobotics/InternVLA-M1.

## 개요
우리는 InternVLA-M1을 소개합니다. 이는 공간적 근거(grounding)와 로봇 제어를 위한 통합 프레임워크로, 명령 수행 로봇을 확장 가능한 범용 지능으로 발전시킵니다. 핵심 아이디어는 공간적으로 유도된 시각-언어-행동 훈련으로, 공간적 근거가 명령과 로봇 행동 사이의 중요한 연결고리 역할을 합니다. InternVLA-M1은 두 단계 파이프라인을 사용합니다: (i) 230만 개 이상의 공간 추론 데이터에 대한 공간적 근거 사전 훈련을 통해 명령을 시각적, 구현체에 구애받지 않는 위치와 정렬하여 "어디에서 행동할지" 결정하고, (ii) 플러그 앤 플레이 공간 프롬프팅을 통해 구현체 인식 행동을 생성하여 "어떻게 행동할지" 결정하는 공간적으로 유도된 행동 후속 훈련입니다. 이 공간적으로 유도된 훈련 방식은 일관된 성능 향상을 가져옵니다: InternVLA-M1은 공간적 유도가 없는 변형 모델보다 SimplerEnv Google Robot에서 +14.6%, WidowX에서 +17%, LIBERO Franka에서 +4.3% 더 뛰어난 성능을 보이며, 상자, 점, 궤적 예측에서 더 강력한 공간 추론 능력을 입증합니다. 명령 수행을 더욱 확장하기 위해, 우리는 244K개의 일반화 가능한 집어 옮기기(pick-and-place) 에피소드를 수집하는 시뮬레이션 엔진을 구축하여 200개 작업과 3000개 이상의 객체에서 평균 6.2%의 개선을 가능하게 했습니다. 실제 환경의 군집 집어 옮기기에서 InternVLA-M1은 7.3% 향상되었으며, 합성 공동 훈련을 통해 보지 못한 객체와 새로운 구성에서 +20.6%를 달성했습니다. 또한, 장기적이고 추론 집약적인 시나리오에서는 기존 연구보다 10% 이상 뛰어난 성능을 보였습니다. 이러한 결과는 공간적으로 유도된 훈련이 확장 가능하고 탄력적인 범용 로봇을 위한 통합 원리임을 강조합니다. 코드와 모델은 https://github.com/InternRobotics/InternVLA-M1에서 확인할 수 있습니다.

## 핵심 내용
우리는 InternVLA-M1을 소개합니다. 이는 공간적 근거(grounding)와 로봇 제어를 위한 통합 프레임워크로, 명령 수행 로봇을 확장 가능한 범용 지능으로 발전시킵니다. 핵심 아이디어는 공간적으로 유도된 시각-언어-행동 훈련으로, 공간적 근거가 명령과 로봇 행동 사이의 중요한 연결고리 역할을 합니다. InternVLA-M1은 두 단계 파이프라인을 사용합니다: (i) 230만 개 이상의 공간 추론 데이터에 대한 공간적 근거 사전 훈련을 통해 명령을 시각적, 구현체에 구애받지 않는 위치와 정렬하여 "어디에서 행동할지" 결정하고, (ii) 플러그 앤 플레이 공간 프롬프팅을 통해 구현체 인식 행동을 생성하여 "어떻게 행동할지" 결정하는 공간적으로 유도된 행동 후속 훈련입니다. 이 공간적으로 유도된 훈련 방식은 일관된 성능 향상을 가져옵니다: InternVLA-M1은 공간적 유도가 없는 변형 모델보다 SimplerEnv Google Robot에서 +14.6%, WidowX에서 +17%, LIBERO Franka에서 +4.3% 더 뛰어난 성능을 보이며, 상자, 점, 궤적 예측에서 더 강력한 공간 추론 능력을 입증합니다. 명령 수행을 더욱 확장하기 위해, 우리는 244K개의 일반화 가능한 집어 옮기기(pick-and-place) 에피소드를 수집하는 시뮬레이션 엔진을 구축하여 200개 작업과 3000개 이상의 객체에서 평균 6.2%의 개선을 가능하게 했습니다. 실제 환경의 군집 집어 옮기기에서 InternVLA-M1은 7.3% 향상되었으며, 합성 공동 훈련을 통해 보지 못한 객체와 새로운 구성에서 +20.6%를 달성했습니다. 또한, 장기적이고 추론 집약적인 시나리오에서는 기존 연구보다 10% 이상 뛰어난 성능을 보였습니다. 이러한 결과는 공간적으로 유도된 훈련이 확장 가능하고 탄력적인 범용 로봇을 위한 통합 원리임을 강조합니다. 코드와 모델은 https://github.com/InternRobotics/InternVLA-M1에서 확인할 수 있습니다.
