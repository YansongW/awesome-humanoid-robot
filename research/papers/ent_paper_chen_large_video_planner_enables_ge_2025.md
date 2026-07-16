---
$id: ent_paper_chen_large_video_planner_enables_ge_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Large Video Planner Enables Generalizable Robot Control
  zh: LVP
  ko: Large Video Planner Enables Generalizable Robot Control
summary:
  en: Large Video Planner Enables Generalizable Robot Control (LVP), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by MIT, UC Berkeley, Harvard.
  zh: Large Video Planner Enables Generalizable Robot Control (LVP), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by MIT, UC Berkeley, Harvard.
  ko: Large Video Planner Enables Generalizable Robot Control (LVP), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by MIT, UC Berkeley, Harvard.
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
- lvp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15840v2.
sources:
- id: src_001
  type: paper
  title: Large Video Planner Enables Generalizable Robot Control (arXiv)
  url: https://arxiv.org/abs/2512.15840
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LVP source
  url: https://doi.org/10.48550/arXiv.2512.15840
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
General-purpose robots require decision-making models that generalize across diverse tasks and environments. Recent works build robot foundation models by extending multimodal large language models (MLLMs) with action outputs, creating vision-language-action (VLA) systems. These efforts are motivated by the intuition that MLLMs' large-scale language and image pretraining can be effectively transferred to the action output modality. In this work, we explore an alternative paradigm of using large-scale video pretraining as a primary modality for building robot foundation models. Unlike static images and language, videos capture spatio-temporal sequences of states and actions in the physical world that are naturally aligned with robotic behavior. We curate an internet-scale video dataset of human activities and task demonstrations, and train, for the first time at a foundation-model scale, an open video model for generative robotics planning. The model produces zero-shot video plans for novel scenes and tasks, which we post-process to extract executable robot actions. We evaluate task-level generalization through third-party selected tasks in the wild and real-robot experiments, demonstrating successful physical execution. Together, these results show robust instruction following, strong generalization, and real-world feasibility. We release both the model and dataset to support open, reproducible video-based robot learning. Our website is available at https://www.boyuan.space/large-video-planner/.

## 核心内容
General-purpose robots require decision-making models that generalize across diverse tasks and environments. Recent works build robot foundation models by extending multimodal large language models (MLLMs) with action outputs, creating vision-language-action (VLA) systems. These efforts are motivated by the intuition that MLLMs' large-scale language and image pretraining can be effectively transferred to the action output modality. In this work, we explore an alternative paradigm of using large-scale video pretraining as a primary modality for building robot foundation models. Unlike static images and language, videos capture spatio-temporal sequences of states and actions in the physical world that are naturally aligned with robotic behavior. We curate an internet-scale video dataset of human activities and task demonstrations, and train, for the first time at a foundation-model scale, an open video model for generative robotics planning. The model produces zero-shot video plans for novel scenes and tasks, which we post-process to extract executable robot actions. We evaluate task-level generalization through third-party selected tasks in the wild and real-robot experiments, demonstrating successful physical execution. Together, these results show robust instruction following, strong generalization, and real-world feasibility. We release both the model and dataset to support open, reproducible video-based robot learning. Our website is available at https://www.boyuan.space/large-video-planner/.

## 参考
- http://arxiv.org/abs/2512.15840v2

## Overview
General-purpose robots require decision-making models that generalize across diverse tasks and environments. Recent works build robot foundation models by extending multimodal large language models (MLLMs) with action outputs, creating vision-language-action (VLA) systems. These efforts are motivated by the intuition that MLLMs' large-scale language and image pretraining can be effectively transferred to the action output modality. In this work, we explore an alternative paradigm of using large-scale video pretraining as a primary modality for building robot foundation models. Unlike static images and language, videos capture spatio-temporal sequences of states and actions in the physical world that are naturally aligned with robotic behavior. We curate an internet-scale video dataset of human activities and task demonstrations, and train, for the first time at a foundation-model scale, an open video model for generative robotics planning. The model produces zero-shot video plans for novel scenes and tasks, which we post-process to extract executable robot actions. We evaluate task-level generalization through third-party selected tasks in the wild and real-robot experiments, demonstrating successful physical execution. Together, these results show robust instruction following, strong generalization, and real-world feasibility. We release both the model and dataset to support open, reproducible video-based robot learning. Our website is available at https://www.boyuan.space/large-video-planner/.

## Content
General-purpose robots require decision-making models that generalize across diverse tasks and environments. Recent works build robot foundation models by extending multimodal large language models (MLLMs) with action outputs, creating vision-language-action (VLA) systems. These efforts are motivated by the intuition that MLLMs' large-scale language and image pretraining can be effectively transferred to the action output modality. In this work, we explore an alternative paradigm of using large-scale video pretraining as a primary modality for building robot foundation models. Unlike static images and language, videos capture spatio-temporal sequences of states and actions in the physical world that are naturally aligned with robotic behavior. We curate an internet-scale video dataset of human activities and task demonstrations, and train, for the first time at a foundation-model scale, an open video model for generative robotics planning. The model produces zero-shot video plans for novel scenes and tasks, which we post-process to extract executable robot actions. We evaluate task-level generalization through third-party selected tasks in the wild and real-robot experiments, demonstrating successful physical execution. Together, these results show robust instruction following, strong generalization, and real-world feasibility. We release both the model and dataset to support open, reproducible video-based robot learning. Our website is available at https://www.boyuan.space/large-video-planner/.

## 개요
범용 로봇은 다양한 작업과 환경에서 일반화되는 의사 결정 모델을 필요로 합니다. 최근 연구들은 멀티모달 대규모 언어 모델(MLLM)에 행동 출력을 확장하여 비전-언어-행동(VLA) 시스템을 구축함으로써 로봇 기반 모델을 개발하고 있습니다. 이러한 노력은 MLLM의 대규모 언어 및 이미지 사전 학습이 행동 출력 모달리티로 효과적으로 전이될 수 있다는 직관에 기반합니다. 본 연구에서는 대규모 비디오 사전 학습을 로봇 기반 모델 구축의 주요 모달리티로 활용하는 대안적 패러다임을 탐구합니다. 정적 이미지 및 언어와 달리, 비디오는 물리적 세계에서 상태와 행동의 시공간적 시퀀스를 포착하며, 이는 로봇 행동과 자연스럽게 정렬됩니다. 우리는 인간 활동 및 작업 시연의 인터넷 규모 비디오 데이터셋을 선별하고, 처음으로 기반 모델 규모에서 생성적 로봇 계획을 위한 오픈 비디오 모델을 학습시킵니다. 이 모델은 새로운 장면과 작업에 대해 제로샷 비디오 계획을 생성하며, 이를 후처리하여 실행 가능한 로봇 행동을 추출합니다. 우리는 실제 환경에서 제3자가 선정한 작업과 실제 로봇 실험을 통해 작업 수준 일반화를 평가하며, 성공적인 물리적 실행을 입증합니다. 이러한 결과는 강력한 명령 수행, 뛰어난 일반화, 그리고 실제 환경에서의 실현 가능성을 보여줍니다. 우리는 모델과 데이터셋을 모두 공개하여 개방적이고 재현 가능한 비디오 기반 로봇 학습을 지원합니다. 웹사이트는 https://www.boyuan.space/large-video-planner/ 에서 확인할 수 있습니다.

## 핵심 내용
범용 로봇은 다양한 작업과 환경에서 일반화되는 의사 결정 모델을 필요로 합니다. 최근 연구들은 멀티모달 대규모 언어 모델(MLLM)에 행동 출력을 확장하여 비전-언어-행동(VLA) 시스템을 구축함으로써 로봇 기반 모델을 개발하고 있습니다. 이러한 노력은 MLLM의 대규모 언어 및 이미지 사전 학습이 행동 출력 모달리티로 효과적으로 전이될 수 있다는 직관에 기반합니다. 본 연구에서는 대규모 비디오 사전 학습을 로봇 기반 모델 구축의 주요 모달리티로 활용하는 대안적 패러다임을 탐구합니다. 정적 이미지 및 언어와 달리, 비디오는 물리적 세계에서 상태와 행동의 시공간적 시퀀스를 포착하며, 이는 로봇 행동과 자연스럽게 정렬됩니다. 우리는 인간 활동 및 작업 시연의 인터넷 규모 비디오 데이터셋을 선별하고, 처음으로 기반 모델 규모에서 생성적 로봇 계획을 위한 오픈 비디오 모델을 학습시킵니다. 이 모델은 새로운 장면과 작업에 대해 제로샷 비디오 계획을 생성하며, 이를 후처리하여 실행 가능한 로봇 행동을 추출합니다. 우리는 실제 환경에서 제3자가 선정한 작업과 실제 로봇 실험을 통해 작업 수준 일반화를 평가하며, 성공적인 물리적 실행을 입증합니다. 이러한 결과는 강력한 명령 수행, 뛰어난 일반화, 그리고 실제 환경에서의 실현 가능성을 보여줍니다. 우리는 모델과 데이터셋을 모두 공개하여 개방적이고 재현 가능한 비디오 기반 로봇 학습을 지원합니다. 웹사이트는 https://www.boyuan.space/large-video-planner/ 에서 확인할 수 있습니다.
