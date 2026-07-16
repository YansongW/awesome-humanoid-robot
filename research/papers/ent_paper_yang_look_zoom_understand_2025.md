---
$id: ent_paper_yang_look_zoom_understand_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Look Zoom Understand
  zh: EyeVLA
  ko: Look Zoom Understand
summary:
  en: Look Zoom Understand (EyeVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Shanghai Jiao Tong University, Institute of Automation, Chinese Academy of Sciences, Dalian University of Technology.
  zh: Look Zoom Understand (EyeVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Shanghai Jiao Tong University, Institute of Automation, Chinese Academy of Sciences, Dalian University of Technology.
  ko: Look Zoom Understand (EyeVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Shanghai Jiao Tong University, Institute of Automation, Chinese Academy of Sciences, Dalian University of Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eyevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15279v2.
sources:
- id: src_001
  type: paper
  title: Look Zoom Understand (arXiv)
  url: https://arxiv.org/abs/2511.15279
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EyeVLA source
  url: https://doi.org/10.48550/arXiv.2511.15279
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In embodied AI, visual perception should be active rather than passive: the system must decide where to look and at what scale to sense to acquire maximally informative data under pixel and spatial budget constraints. Existing vision models coupled with fixed RGB-D cameras fundamentally fail to reconcile wide-area coverage with fine-grained detail acquisition, severely limiting their efficacy in open-world robotic applications. We study the task of language-guided active visual perception: given a single RGB image and a natural language instruction, the agent must output pan, tilt, and zoom adjustments of a real PTZ (pan-tilt-zoom) camera to acquire the most informative view for the specified task. We propose EyeVLA, a unified framework that addresses this task by integrating visual perception, language understanding, and physical camera control within a single autoregressive vision-language-action model. EyeVLA introduces a semantically rich and efficient hierarchical action encoding that compactly tokenizes continuous camera adjustments and embeds them into the VLM vocabulary for joint multimodal reasoning. Through a data-efficient pipeline comprising pseudo-label generation, iterative IoU-controlled data refinement, and reinforcement learning with Group Relative Policy Optimization (GRPO), we transfer the open-world understanding of a pre-trained VLM to an embodied active perception policy using only 500 real-world samples. Evaluations on 50 diverse real-world scenes across five independent evaluation runs demonstrate that EyeVLA achieves an average task completion rate of 96%. Our work establishes a new paradigm for instruction-driven active visual information acquisition in multimodal embodied systems.

## 核心内容
In embodied AI, visual perception should be active rather than passive: the system must decide where to look and at what scale to sense to acquire maximally informative data under pixel and spatial budget constraints. Existing vision models coupled with fixed RGB-D cameras fundamentally fail to reconcile wide-area coverage with fine-grained detail acquisition, severely limiting their efficacy in open-world robotic applications. We study the task of language-guided active visual perception: given a single RGB image and a natural language instruction, the agent must output pan, tilt, and zoom adjustments of a real PTZ (pan-tilt-zoom) camera to acquire the most informative view for the specified task. We propose EyeVLA, a unified framework that addresses this task by integrating visual perception, language understanding, and physical camera control within a single autoregressive vision-language-action model. EyeVLA introduces a semantically rich and efficient hierarchical action encoding that compactly tokenizes continuous camera adjustments and embeds them into the VLM vocabulary for joint multimodal reasoning. Through a data-efficient pipeline comprising pseudo-label generation, iterative IoU-controlled data refinement, and reinforcement learning with Group Relative Policy Optimization (GRPO), we transfer the open-world understanding of a pre-trained VLM to an embodied active perception policy using only 500 real-world samples. Evaluations on 50 diverse real-world scenes across five independent evaluation runs demonstrate that EyeVLA achieves an average task completion rate of 96%. Our work establishes a new paradigm for instruction-driven active visual information acquisition in multimodal embodied systems.

## 参考
- http://arxiv.org/abs/2511.15279v2

## Overview
In embodied AI, visual perception should be active rather than passive: the system must decide where to look and at what scale to sense to acquire maximally informative data under pixel and spatial budget constraints. Existing vision models coupled with fixed RGB-D cameras fundamentally fail to reconcile wide-area coverage with fine-grained detail acquisition, severely limiting their efficacy in open-world robotic applications. We study the task of language-guided active visual perception: given a single RGB image and a natural language instruction, the agent must output pan, tilt, and zoom adjustments of a real PTZ (pan-tilt-zoom) camera to acquire the most informative view for the specified task. We propose EyeVLA, a unified framework that addresses this task by integrating visual perception, language understanding, and physical camera control within a single autoregressive vision-language-action model. EyeVLA introduces a semantically rich and efficient hierarchical action encoding that compactly tokenizes continuous camera adjustments and embeds them into the VLM vocabulary for joint multimodal reasoning. Through a data-efficient pipeline comprising pseudo-label generation, iterative IoU-controlled data refinement, and reinforcement learning with Group Relative Policy Optimization (GRPO), we transfer the open-world understanding of a pre-trained VLM to an embodied active perception policy using only 500 real-world samples. Evaluations on 50 diverse real-world scenes across five independent evaluation runs demonstrate that EyeVLA achieves an average task completion rate of 96%. Our work establishes a new paradigm for instruction-driven active visual information acquisition in multimodal embodied systems.

## Content
In embodied AI, visual perception should be active rather than passive: the system must decide where to look and at what scale to sense to acquire maximally informative data under pixel and spatial budget constraints. Existing vision models coupled with fixed RGB-D cameras fundamentally fail to reconcile wide-area coverage with fine-grained detail acquisition, severely limiting their efficacy in open-world robotic applications. We study the task of language-guided active visual perception: given a single RGB image and a natural language instruction, the agent must output pan, tilt, and zoom adjustments of a real PTZ (pan-tilt-zoom) camera to acquire the most informative view for the specified task. We propose EyeVLA, a unified framework that addresses this task by integrating visual perception, language understanding, and physical camera control within a single autoregressive vision-language-action model. EyeVLA introduces a semantically rich and efficient hierarchical action encoding that compactly tokenizes continuous camera adjustments and embeds them into the VLM vocabulary for joint multimodal reasoning. Through a data-efficient pipeline comprising pseudo-label generation, iterative IoU-controlled data refinement, and reinforcement learning with Group Relative Policy Optimization (GRPO), we transfer the open-world understanding of a pre-trained VLM to an embodied active perception policy using only 500 real-world samples. Evaluations on 50 diverse real-world scenes across five independent evaluation runs demonstrate that EyeVLA achieves an average task completion rate of 96%. Our work establishes a new paradigm for instruction-driven active visual information acquisition in multimodal embodied systems.

## 개요
임베디드 AI에서 시각적 인식은 수동적이 아닌 능동적이어야 합니다. 시스템은 픽셀 및 공간 예산 제약 하에서 최대한 정보를 얻기 위해 어디를 보고 어떤 스케일로 감지할지 결정해야 합니다. 고정 RGB-D 카메라와 결합된 기존의 비전 모델은 광범위한 영역 커버리지와 세밀한 디테일 획득을 근본적으로 조화시키지 못하며, 이는 개방형 세계 로봇 응용에서의 효용성을 심각하게 제한합니다. 우리는 언어 기반 능동적 시각 인식 과제를 연구합니다. 단일 RGB 이미지와 자연어 명령이 주어지면 에이전트는 실제 PTZ(팬-틸트-줌) 카메라의 팬, 틸트, 줌 조정을 출력하여 지정된 작업에 가장 유용한 뷰를 획득해야 합니다. 우리는 이 과제를 해결하기 위해 시각적 인식, 언어 이해, 물리적 카메라 제어를 단일 자기회귀 비전-언어-행동 모델에 통합한 통합 프레임워크인 EyeVLA를 제안합니다. EyeVLA는 의미적으로 풍부하고 효율적인 계층적 행동 인코딩을 도입하여 연속적인 카메라 조정을 간결하게 토큰화하고 VLM 어휘에 임베딩하여 공동 다중 모드 추론을 가능하게 합니다. 의사 레이블 생성, 반복적 IoU 제어 데이터 정제, GRPO(Group Relative Policy Optimization)를 사용한 강화 학습으로 구성된 데이터 효율적인 파이프라인을 통해 사전 훈련된 VLM의 개방형 세계 이해를 단 500개의 실제 세계 샘플만으로 임베디드 능동적 인식 정책으로 전이합니다. 5개의 독립적인 평가 실행에 걸친 50개의 다양한 실제 세계 장면에 대한 평가는 EyeVLA가 평균 작업 완료율 96%를 달성함을 보여줍니다. 우리의 연구는 다중 모드 임베디드 시스템에서 명령 기반 능동적 시각 정보 획득을 위한 새로운 패러다임을 확립합니다.

## 핵심 내용
임베디드 AI에서 시각적 인식은 수동적이 아닌 능동적이어야 합니다. 시스템은 픽셀 및 공간 예산 제약 하에서 최대한 정보를 얻기 위해 어디를 보고 어떤 스케일로 감지할지 결정해야 합니다. 고정 RGB-D 카메라와 결합된 기존의 비전 모델은 광범위한 영역 커버리지와 세밀한 디테일 획득을 근본적으로 조화시키지 못하며, 이는 개방형 세계 로봇 응용에서의 효용성을 심각하게 제한합니다. 우리는 언어 기반 능동적 시각 인식 과제를 연구합니다. 단일 RGB 이미지와 자연어 명령이 주어지면 에이전트는 실제 PTZ(팬-틸트-줌) 카메라의 팬, 틸트, 줌 조정을 출력하여 지정된 작업에 가장 유용한 뷰를 획득해야 합니다. 우리는 이 과제를 해결하기 위해 시각적 인식, 언어 이해, 물리적 카메라 제어를 단일 자기회귀 비전-언어-행동 모델에 통합한 통합 프레임워크인 EyeVLA를 제안합니다. EyeVLA는 의미적으로 풍부하고 효율적인 계층적 행동 인코딩을 도입하여 연속적인 카메라 조정을 간결하게 토큰화하고 VLM 어휘에 임베딩하여 공동 다중 모드 추론을 가능하게 합니다. 의사 레이블 생성, 반복적 IoU 제어 데이터 정제, GRPO(Group Relative Policy Optimization)를 사용한 강화 학습으로 구성된 데이터 효율적인 파이프라인을 통해 사전 훈련된 VLM의 개방형 세계 이해를 단 500개의 실제 세계 샘플만으로 임베디드 능동적 인식 정책으로 전이합니다. 5개의 독립적인 평가 실행에 걸친 50개의 다양한 실제 세계 장면에 대한 평가는 EyeVLA가 평균 작업 완료율 96%를 달성함을 보여줍니다. 우리의 연구는 다중 모드 임베디드 시스템에서 명령 기반 능동적 시각 정보 획득을 위한 새로운 패러다임을 확립합니다.
