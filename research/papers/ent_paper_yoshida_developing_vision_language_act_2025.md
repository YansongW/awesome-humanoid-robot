---
$id: ent_paper_yoshida_developing_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Developing Vision-Language-Action Model from Egocentric Videos
  zh: Developing Vision-Language-Action Model from Egocentric Videos
  ko: Developing Vision-Language-Action Model from Egocentric Videos
summary:
  en: Developing Vision-Language-Action Model from Egocentric Videos (Developing Vision-Language-Action Model from Egocentric
    Videos), is a 2025 large vision-language-action model for robotic manipulation, introduced by Institute of Science Tokyo,
    NII LLMC, Sony Interactive Entertainment.
  zh: Developing Vision-Language-Action Model from Egocentric Videos (Developing Vision-Language-Action Model from Egocentric
    Videos), is a 2025 large vision-language-action model for robotic manipulation, introduced by Institute of Science Tokyo,
    NII LLMC, Sony Interactive Entertainment.
  ko: Developing Vision-Language-Action Model from Egocentric Videos (Developing Vision-Language-Action Model from Egocentric
    Videos), is a 2025 large vision-language-action model for robotic manipulation, introduced by Institute of Science Tokyo,
    NII LLMC, Sony Interactive Entertainment.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- developing_vision_language_act
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21986v1.
sources:
- id: src_001
  type: paper
  title: Developing Vision-Language-Action Model from Egocentric Videos (arXiv)
  url: https://arxiv.org/abs/2509.21986
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Developing Vision-Language-Action Model from Egocentric Videos source
  url: https://doi.org/10.48550/arXiv.2509.21986
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Egocentric videos capture how humans manipulate objects and tools, providing diverse motion cues for learning object manipulation. Unlike the costly, expert-driven manual teleoperation commonly used in training Vision-Language-Action models (VLAs), egocentric videos offer a scalable alternative. However, prior studies that leverage such videos for training robot policies typically rely on auxiliary annotations, such as detailed hand-pose recordings. Consequently, it remains unclear whether VLAs can be trained directly from raw egocentric videos. In this work, we address this challenge by leveraging EgoScaler, a framework that extracts 6DoF object manipulation trajectories from egocentric videos without requiring auxiliary recordings. We apply EgoScaler to four large-scale egocentric video datasets and automatically refine noisy or incomplete trajectories, thereby constructing a new large-scale dataset for VLA pre-training. Our experiments with a state-of-the-art $π_0$ architecture in both simulated and real-robot environments yield three key findings: (i) pre-training on our dataset improves task success rates by over 20\% compared to training from scratch, (ii) the performance is competitive with that achieved using real-robot datasets, and (iii) combining our dataset with real-robot data yields further improvements. These results demonstrate that egocentric videos constitute a promising and scalable resource for advancing VLA research.

## 核心内容
Egocentric videos capture how humans manipulate objects and tools, providing diverse motion cues for learning object manipulation. Unlike the costly, expert-driven manual teleoperation commonly used in training Vision-Language-Action models (VLAs), egocentric videos offer a scalable alternative. However, prior studies that leverage such videos for training robot policies typically rely on auxiliary annotations, such as detailed hand-pose recordings. Consequently, it remains unclear whether VLAs can be trained directly from raw egocentric videos. In this work, we address this challenge by leveraging EgoScaler, a framework that extracts 6DoF object manipulation trajectories from egocentric videos without requiring auxiliary recordings. We apply EgoScaler to four large-scale egocentric video datasets and automatically refine noisy or incomplete trajectories, thereby constructing a new large-scale dataset for VLA pre-training. Our experiments with a state-of-the-art $π_0$ architecture in both simulated and real-robot environments yield three key findings: (i) pre-training on our dataset improves task success rates by over 20\% compared to training from scratch, (ii) the performance is competitive with that achieved using real-robot datasets, and (iii) combining our dataset with real-robot data yields further improvements. These results demonstrate that egocentric videos constitute a promising and scalable resource for advancing VLA research.

## 参考
- http://arxiv.org/abs/2509.21986v1

## Overview
Egocentric videos capture how humans manipulate objects and tools, providing diverse motion cues for learning object manipulation. Unlike the costly, expert-driven manual teleoperation commonly used in training Vision-Language-Action models (VLAs), egocentric videos offer a scalable alternative. However, prior studies that leverage such videos for training robot policies typically rely on auxiliary annotations, such as detailed hand-pose recordings. Consequently, it remains unclear whether VLAs can be trained directly from raw egocentric videos. In this work, we address this challenge by leveraging EgoScaler, a framework that extracts 6DoF object manipulation trajectories from egocentric videos without requiring auxiliary recordings. We apply EgoScaler to four large-scale egocentric video datasets and automatically refine noisy or incomplete trajectories, thereby constructing a new large-scale dataset for VLA pre-training. Our experiments with a state-of-the-art $π_0$ architecture in both simulated and real-robot environments yield three key findings: (i) pre-training on our dataset improves task success rates by over 20\% compared to training from scratch, (ii) the performance is competitive with that achieved using real-robot datasets, and (iii) combining our dataset with real-robot data yields further improvements. These results demonstrate that egocentric videos constitute a promising and scalable resource for advancing VLA research.

## Content
Egocentric videos capture how humans manipulate objects and tools, providing diverse motion cues for learning object manipulation. Unlike the costly, expert-driven manual teleoperation commonly used in training Vision-Language-Action models (VLAs), egocentric videos offer a scalable alternative. However, prior studies that leverage such videos for training robot policies typically rely on auxiliary annotations, such as detailed hand-pose recordings. Consequently, it remains unclear whether VLAs can be trained directly from raw egocentric videos. In this work, we address this challenge by leveraging EgoScaler, a framework that extracts 6DoF object manipulation trajectories from egocentric videos without requiring auxiliary recordings. We apply EgoScaler to four large-scale egocentric video datasets and automatically refine noisy or incomplete trajectories, thereby constructing a new large-scale dataset for VLA pre-training. Our experiments with a state-of-the-art $π_0$ architecture in both simulated and real-robot environments yield three key findings: (i) pre-training on our dataset improves task success rates by over 20\% compared to training from scratch, (ii) the performance is competitive with that achieved using real-robot datasets, and (iii) combining our dataset with real-robot data yields further improvements. These results demonstrate that egocentric videos constitute a promising and scalable resource for advancing VLA research.

## 개요
자기중심적 비디오는 인간이 물체와 도구를 조작하는 방식을 포착하여, 물체 조작 학습을 위한 다양한 움직임 단서를 제공합니다. 비전-언어-행동 모델(VLA) 훈련에 일반적으로 사용되는 고비용의 전문가 주도 수동 원격 조작과 달리, 자기중심적 비디오는 확장 가능한 대안을 제시합니다. 그러나 이러한 비디오를 로봇 정책 훈련에 활용한 이전 연구들은 일반적으로 상세한 손 자세 기록과 같은 보조 주석에 의존합니다. 결과적으로, 원시 자기중심적 비디오에서 직접 VLA를 훈련할 수 있는지 여부는 여전히 불분명합니다. 본 연구에서는 보조 기록 없이 자기중심적 비디오에서 6자유도 물체 조작 궤적을 추출하는 프레임워크인 EgoScaler를 활용하여 이 문제를 해결합니다. 우리는 EgoScaler를 네 개의 대규모 자기중심적 비디오 데이터셋에 적용하고, 노이즈가 있거나 불완전한 궤적을 자동으로 정제하여 VLA 사전 훈련을 위한 새로운 대규모 데이터셋을 구축합니다. 시뮬레이션 및 실제 로봇 환경 모두에서 최첨단 $π_0$ 아키텍처를 사용한 실험을 통해 세 가지 주요 결과를 도출했습니다: (i) 우리 데이터셋으로 사전 훈련하면 처음부터 훈련하는 것보다 작업 성공률이 20% 이상 향상되고, (ii) 성능이 실제 로봇 데이터셋을 사용한 경우와 경쟁력이 있으며, (iii) 우리 데이터셋과 실제 로봇 데이터를 결합하면 추가적인 개선이 이루어집니다. 이러한 결과는 자기중심적 비디오가 VLA 연구 발전을 위한 유망하고 확장 가능한 자원임을 보여줍니다.

## 핵심 내용
자기중심적 비디오는 인간이 물체와 도구를 조작하는 방식을 포착하여, 물체 조작 학습을 위한 다양한 움직임 단서를 제공합니다. 비전-언어-행동 모델(VLA) 훈련에 일반적으로 사용되는 고비용의 전문가 주도 수동 원격 조작과 달리, 자기중심적 비디오는 확장 가능한 대안을 제시합니다. 그러나 이러한 비디오를 로봇 정책 훈련에 활용한 이전 연구들은 일반적으로 상세한 손 자세 기록과 같은 보조 주석에 의존합니다. 결과적으로, 원시 자기중심적 비디오에서 직접 VLA를 훈련할 수 있는지 여부는 여전히 불분명합니다. 본 연구에서는 보조 기록 없이 자기중심적 비디오에서 6자유도 물체 조작 궤적을 추출하는 프레임워크인 EgoScaler를 활용하여 이 문제를 해결합니다. 우리는 EgoScaler를 네 개의 대규모 자기중심적 비디오 데이터셋에 적용하고, 노이즈가 있거나 불완전한 궤적을 자동으로 정제하여 VLA 사전 훈련을 위한 새로운 대규모 데이터셋을 구축합니다. 시뮬레이션 및 실제 로봇 환경 모두에서 최첨단 $π_0$ 아키텍처를 사용한 실험을 통해 세 가지 주요 결과를 도출했습니다: (i) 우리 데이터셋으로 사전 훈련하면 처음부터 훈련하는 것보다 작업 성공률이 20% 이상 향상되고, (ii) 성능이 실제 로봇 데이터셋을 사용한 경우와 경쟁력이 있으며, (iii) 우리 데이터셋과 실제 로봇 데이터를 결합하면 추가적인 개선이 이루어집니다. 이러한 결과는 자기중심적 비디오가 VLA 연구 발전을 위한 유망하고 확장 가능한 자원임을 보여줍니다.
