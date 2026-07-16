---
$id: ent_paper_genmo_a_generalist_model_for_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GENMO: A GENeralist Model for Human MOtion'
  zh: 'GENMO: A GENeralist Model for Human MOtion'
  ko: 'GENMO: A GENeralist Model for Human MOtion'
summary:
  en: 'GENMO: A GENeralist Model for Human MOtion is a 2025 work on human motion analysis and synthesis for humanoid robots.'
  zh: 'GENMO: A GENeralist Model for Human MOtion is a 2025 work on human motion analysis and synthesis for humanoid robots.'
  ko: 'GENMO: A GENeralist Model for Human MOtion is a 2025 work on human motion analysis and synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- genmo
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.01425v1.
sources:
- id: src_001
  type: paper
  title: 'GENMO: A GENeralist Model for Human MOtion (arXiv)'
  url: https://arxiv.org/abs/2505.01425
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'GENMO: A GENeralist Model for Human MOtion project page'
  url: https://research.nvidia.com/labs/dair/genmo/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Human motion modeling traditionally separates motion generation and estimation into distinct tasks with specialized models. Motion generation models focus on creating diverse, realistic motions from inputs like text, audio, or keyframes, while motion estimation models aim to reconstruct accurate motion trajectories from observations like videos. Despite sharing underlying representations of temporal dynamics and kinematics, this separation limits knowledge transfer between tasks and requires maintaining separate models. We present GENMO, a unified Generalist Model for Human Motion that bridges motion estimation and generation in a single framework. Our key insight is to reformulate motion estimation as constrained motion generation, where the output motion must precisely satisfy observed conditioning signals. Leveraging the synergy between regression and diffusion, GENMO achieves accurate global motion estimation while enabling diverse motion generation. We also introduce an estimation-guided training objective that exploits in-the-wild videos with 2D annotations and text descriptions to enhance generative diversity. Furthermore, our novel architecture handles variable-length motions and mixed multimodal conditions (text, audio, video) at different time intervals, offering flexible control. This unified approach creates synergistic benefits: generative priors improve estimated motions under challenging conditions like occlusions, while diverse video data enhances generation capabilities. Extensive experiments demonstrate GENMO's effectiveness as a generalist framework that successfully handles multiple human motion tasks within a single model.

## 核心内容
Human motion modeling traditionally separates motion generation and estimation into distinct tasks with specialized models. Motion generation models focus on creating diverse, realistic motions from inputs like text, audio, or keyframes, while motion estimation models aim to reconstruct accurate motion trajectories from observations like videos. Despite sharing underlying representations of temporal dynamics and kinematics, this separation limits knowledge transfer between tasks and requires maintaining separate models. We present GENMO, a unified Generalist Model for Human Motion that bridges motion estimation and generation in a single framework. Our key insight is to reformulate motion estimation as constrained motion generation, where the output motion must precisely satisfy observed conditioning signals. Leveraging the synergy between regression and diffusion, GENMO achieves accurate global motion estimation while enabling diverse motion generation. We also introduce an estimation-guided training objective that exploits in-the-wild videos with 2D annotations and text descriptions to enhance generative diversity. Furthermore, our novel architecture handles variable-length motions and mixed multimodal conditions (text, audio, video) at different time intervals, offering flexible control. This unified approach creates synergistic benefits: generative priors improve estimated motions under challenging conditions like occlusions, while diverse video data enhances generation capabilities. Extensive experiments demonstrate GENMO's effectiveness as a generalist framework that successfully handles multiple human motion tasks within a single model.

## 参考
- http://arxiv.org/abs/2505.01425v1

## Overview
Human motion modeling traditionally separates motion generation and estimation into distinct tasks with specialized models. Motion generation models focus on creating diverse, realistic motions from inputs like text, audio, or keyframes, while motion estimation models aim to reconstruct accurate motion trajectories from observations like videos. Despite sharing underlying representations of temporal dynamics and kinematics, this separation limits knowledge transfer between tasks and requires maintaining separate models. We present GENMO, a unified Generalist Model for Human Motion that bridges motion estimation and generation in a single framework. Our key insight is to reformulate motion estimation as constrained motion generation, where the output motion must precisely satisfy observed conditioning signals. Leveraging the synergy between regression and diffusion, GENMO achieves accurate global motion estimation while enabling diverse motion generation. We also introduce an estimation-guided training objective that exploits in-the-wild videos with 2D annotations and text descriptions to enhance generative diversity. Furthermore, our novel architecture handles variable-length motions and mixed multimodal conditions (text, audio, video) at different time intervals, offering flexible control. This unified approach creates synergistic benefits: generative priors improve estimated motions under challenging conditions like occlusions, while diverse video data enhances generation capabilities. Extensive experiments demonstrate GENMO's effectiveness as a generalist framework that successfully handles multiple human motion tasks within a single model.

## Content
Human motion modeling traditionally separates motion generation and estimation into distinct tasks with specialized models. Motion generation models focus on creating diverse, realistic motions from inputs like text, audio, or keyframes, while motion estimation models aim to reconstruct accurate motion trajectories from observations like videos. Despite sharing underlying representations of temporal dynamics and kinematics, this separation limits knowledge transfer between tasks and requires maintaining separate models. We present GENMO, a unified Generalist Model for Human Motion that bridges motion estimation and generation in a single framework. Our key insight is to reformulate motion estimation as constrained motion generation, where the output motion must precisely satisfy observed conditioning signals. Leveraging the synergy between regression and diffusion, GENMO achieves accurate global motion estimation while enabling diverse motion generation. We also introduce an estimation-guided training objective that exploits in-the-wild videos with 2D annotations and text descriptions to enhance generative diversity. Furthermore, our novel architecture handles variable-length motions and mixed multimodal conditions (text, audio, video) at different time intervals, offering flexible control. This unified approach creates synergistic benefits: generative priors improve estimated motions under challenging conditions like occlusions, while diverse video data enhances generation capabilities. Extensive experiments demonstrate GENMO's effectiveness as a generalist framework that successfully handles multiple human motion tasks within a single model.

## 개요
인간 동작 모델링은 전통적으로 동작 생성과 추정을 별개의 작업으로 분리하여 각각에 특화된 모델을 사용해 왔습니다. 동작 생성 모델은 텍스트, 오디오, 키프레임 등의 입력으로부터 다양하고 사실적인 동작을 생성하는 데 초점을 맞추는 반면, 동작 추정 모델은 비디오와 같은 관찰 데이터로부터 정확한 동작 궤적을 재구성하는 것을 목표로 합니다. 시간적 역학과 운동학의 기본 표현을 공유함에도 불구하고, 이러한 분리는 작업 간 지식 전달을 제한하고 별도의 모델을 유지해야 하는 단점이 있습니다. 본 논문에서는 동작 추정과 생성을 단일 프레임워크로 연결하는 통합된 인간 동작 제너럴리스트 모델인 GENMO를 제안합니다. 핵심 통찰은 동작 추정을 제약 조건이 있는 동작 생성으로 재정의하여, 출력 동작이 관찰된 조건 신호를 정확히 충족하도록 하는 것입니다. 회귀와 확산 간의 시너지를 활용하여 GENMO는 정확한 전역 동작 추정을 달성하는 동시에 다양한 동작 생성을 가능하게 합니다. 또한, 2D 주석과 텍스트 설명이 포함된 실제 비디오를 활용하는 추정 유도 학습 목표를 도입하여 생성 다양성을 향상시킵니다. 더 나아가, 새로운 아키텍처는 가변 길이 동작과 다양한 시간 간격의 혼합 다중 모달 조건(텍스트, 오디오, 비디오)을 처리하여 유연한 제어를 제공합니다. 이러한 통합 접근 방식은 시너지 효과를 창출합니다: 생성적 사전 지식은 폐색과 같은 까다로운 조건에서 추정 동작을 개선하고, 다양한 비디오 데이터는 생성 능력을 향상시킵니다. 광범위한 실험을 통해 GENMO가 단일 모델 내에서 여러 인간 동작 작업을 성공적으로 처리하는 제너럴리스트 프레임워크로서의 효과성을 입증합니다.

## 핵심 내용
인간 동작 모델링은 전통적으로 동작 생성과 추정을 별개의 작업으로 분리하여 각각에 특화된 모델을 사용해 왔습니다. 동작 생성 모델은 텍스트, 오디오, 키프레임 등의 입력으로부터 다양하고 사실적인 동작을 생성하는 데 초점을 맞추는 반면, 동작 추정 모델은 비디오와 같은 관찰 데이터로부터 정확한 동작 궤적을 재구성하는 것을 목표로 합니다. 시간적 역학과 운동학의 기본 표현을 공유함에도 불구하고, 이러한 분리는 작업 간 지식 전달을 제한하고 별도의 모델을 유지해야 하는 단점이 있습니다. 본 논문에서는 동작 추정과 생성을 단일 프레임워크로 연결하는 통합된 인간 동작 제너럴리스트 모델인 GENMO를 제안합니다. 핵심 통찰은 동작 추정을 제약 조건이 있는 동작 생성으로 재정의하여, 출력 동작이 관찰된 조건 신호를 정확히 충족하도록 하는 것입니다. 회귀와 확산 간의 시너지를 활용하여 GENMO는 정확한 전역 동작 추정을 달성하는 동시에 다양한 동작 생성을 가능하게 합니다. 또한, 2D 주석과 텍스트 설명이 포함된 실제 비디오를 활용하는 추정 유도 학습 목표를 도입하여 생성 다양성을 향상시킵니다. 더 나아가, 새로운 아키텍처는 가변 길이 동작과 다양한 시간 간격의 혼합 다중 모달 조건(텍스트, 오디오, 비디오)을 처리하여 유연한 제어를 제공합니다. 이러한 통합 접근 방식은 시너지 효과를 창출합니다: 생성적 사전 지식은 폐색과 같은 까다로운 조건에서 추정 동작을 개선하고, 다양한 비디오 데이터는 생성 능력을 향상시킵니다. 광범위한 실험을 통해 GENMO가 단일 모델 내에서 여러 인간 동작 작업을 성공적으로 처리하는 제너럴리스트 프레임워크로서의 효과성을 입증합니다.
