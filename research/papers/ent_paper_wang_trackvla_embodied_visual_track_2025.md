---
$id: ent_paper_wang_trackvla_embodied_visual_track_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TrackVLA: Embodied Visual Tracking in the Wild'
  zh: TrackVLA
  ko: 'TrackVLA: Embodied Visual Tracking in the Wild'
summary:
  en: 'TrackVLA: Embodied Visual Tracking in the Wild (TrackVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Peking University, Galbot, Beihang University, Beijing Normal University, Beijing Academy
    of Artificial Intelligence, and published at CoRL25.'
  zh: 'TrackVLA: Embodied Visual Tracking in the Wild (TrackVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Peking University, Galbot, Beihang University, Beijing Normal University, Beijing Academy
    of Artificial Intelligence, and published at CoRL25.'
  ko: 'TrackVLA: Embodied Visual Tracking in the Wild (TrackVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Peking University, Galbot, Beihang University, Beijing Normal University, Beijing Academy
    of Artificial Intelligence, and published at CoRL25.'
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
- robotic_manipulation
- trackvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23189v1.
sources:
- id: src_001
  type: paper
  title: 'TrackVLA: Embodied Visual Tracking in the Wild (arXiv)'
  url: https://arxiv.org/abs/2505.23189
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TrackVLA source
  url: https://doi.org/10.48550/arXiv.2505.23189
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Embodied visual tracking is a fundamental skill in Embodied AI, enabling an agent to follow a specific target in dynamic environments using only egocentric vision. This task is inherently challenging as it requires both accurate target recognition and effective trajectory planning under conditions of severe occlusion and high scene dynamics. Existing approaches typically address this challenge through a modular separation of recognition and planning. In this work, we propose TrackVLA, a Vision-Language-Action (VLA) model that learns the synergy between object recognition and trajectory planning. Leveraging a shared LLM backbone, we employ a language modeling head for recognition and an anchor-based diffusion model for trajectory planning. To train TrackVLA, we construct an Embodied Visual Tracking Benchmark (EVT-Bench) and collect diverse difficulty levels of recognition samples, resulting in a dataset of 1.7 million samples. Through extensive experiments in both synthetic and real-world environments, TrackVLA demonstrates SOTA performance and strong generalizability. It significantly outperforms existing methods on public benchmarks in a zero-shot manner while remaining robust to high dynamics and occlusion in real-world scenarios at 10 FPS inference speed. Our project page is: https://pku-epic.github.io/TrackVLA-web.

## 核心内容
Embodied visual tracking is a fundamental skill in Embodied AI, enabling an agent to follow a specific target in dynamic environments using only egocentric vision. This task is inherently challenging as it requires both accurate target recognition and effective trajectory planning under conditions of severe occlusion and high scene dynamics. Existing approaches typically address this challenge through a modular separation of recognition and planning. In this work, we propose TrackVLA, a Vision-Language-Action (VLA) model that learns the synergy between object recognition and trajectory planning. Leveraging a shared LLM backbone, we employ a language modeling head for recognition and an anchor-based diffusion model for trajectory planning. To train TrackVLA, we construct an Embodied Visual Tracking Benchmark (EVT-Bench) and collect diverse difficulty levels of recognition samples, resulting in a dataset of 1.7 million samples. Through extensive experiments in both synthetic and real-world environments, TrackVLA demonstrates SOTA performance and strong generalizability. It significantly outperforms existing methods on public benchmarks in a zero-shot manner while remaining robust to high dynamics and occlusion in real-world scenarios at 10 FPS inference speed. Our project page is: https://pku-epic.github.io/TrackVLA-web.

## 参考
- http://arxiv.org/abs/2505.23189v1

## Overview
Embodied visual tracking is a fundamental skill in Embodied AI, enabling an agent to follow a specific target in dynamic environments using only egocentric vision. This task is inherently challenging as it requires both accurate target recognition and effective trajectory planning under conditions of severe occlusion and high scene dynamics. Existing approaches typically address this challenge through a modular separation of recognition and planning. In this work, we propose TrackVLA, a Vision-Language-Action (VLA) model that learns the synergy between object recognition and trajectory planning. Leveraging a shared LLM backbone, we employ a language modeling head for recognition and an anchor-based diffusion model for trajectory planning. To train TrackVLA, we construct an Embodied Visual Tracking Benchmark (EVT-Bench) and collect diverse difficulty levels of recognition samples, resulting in a dataset of 1.7 million samples. Through extensive experiments in both synthetic and real-world environments, TrackVLA demonstrates SOTA performance and strong generalizability. It significantly outperforms existing methods on public benchmarks in a zero-shot manner while remaining robust to high dynamics and occlusion in real-world scenarios at 10 FPS inference speed. Our project page is: https://pku-epic.github.io/TrackVLA-web.

## Content
Embodied visual tracking is a fundamental skill in Embodied AI, enabling an agent to follow a specific target in dynamic environments using only egocentric vision. This task is inherently challenging as it requires both accurate target recognition and effective trajectory planning under conditions of severe occlusion and high scene dynamics. Existing approaches typically address this challenge through a modular separation of recognition and planning. In this work, we propose TrackVLA, a Vision-Language-Action (VLA) model that learns the synergy between object recognition and trajectory planning. Leveraging a shared LLM backbone, we employ a language modeling head for recognition and an anchor-based diffusion model for trajectory planning. To train TrackVLA, we construct an Embodied Visual Tracking Benchmark (EVT-Bench) and collect diverse difficulty levels of recognition samples, resulting in a dataset of 1.7 million samples. Through extensive experiments in both synthetic and real-world environments, TrackVLA demonstrates SOTA performance and strong generalizability. It significantly outperforms existing methods on public benchmarks in a zero-shot manner while remaining robust to high dynamics and occlusion in real-world scenarios at 10 FPS inference speed. Our project page is: https://pku-epic.github.io/TrackVLA-web.

## 개요
Embodied visual tracking은 Embodied AI의 기본 기술로, 에이전트가 동적 환경에서 단일 시점 비전만을 사용하여 특정 대상을 추적할 수 있게 합니다. 이 작업은 심각한 폐색과 높은 장면 동적성 조건에서 정확한 대상 인식과 효과적인 궤적 계획을 동시에 요구하기 때문에 본질적으로 어렵습니다. 기존 접근 방식은 일반적으로 인식과 계획을 모듈식으로 분리하여 이 문제를 해결합니다. 본 연구에서는 객체 인식과 궤적 계획 간의 시너지를 학습하는 Vision-Language-Action (VLA) 모델인 TrackVLA를 제안합니다. 공유된 LLM 백본을 활용하여 인식을 위한 언어 모델링 헤드와 궤적 계획을 위한 앵커 기반 확산 모델을 사용합니다. TrackVLA를 훈련하기 위해 Embodied Visual Tracking Benchmark (EVT-Bench)를 구축하고 다양한 난이도의 인식 샘플을 수집하여 170만 개의 샘플로 구성된 데이터셋을 만들었습니다. 합성 환경과 실제 환경 모두에서의 광범위한 실험을 통해 TrackVLA는 최고 성능과 강력한 일반화 능력을 입증했습니다. 이는 공개 벤치마크에서 제로샷 방식으로 기존 방법을 크게 능가하며, 실제 시나리오에서 10FPS 추론 속도로 높은 동적성과 폐색에 강건함을 유지합니다. 프로젝트 페이지는 다음과 같습니다: https://pku-epic.github.io/TrackVLA-web.

## 핵심 내용
Embodied visual tracking은 Embodied AI의 기본 기술로, 에이전트가 동적 환경에서 단일 시점 비전만을 사용하여 특정 대상을 추적할 수 있게 합니다. 이 작업은 심각한 폐색과 높은 장면 동적성 조건에서 정확한 대상 인식과 효과적인 궤적 계획을 동시에 요구하기 때문에 본질적으로 어렵습니다. 기존 접근 방식은 일반적으로 인식과 계획을 모듈식으로 분리하여 이 문제를 해결합니다. 본 연구에서는 객체 인식과 궤적 계획 간의 시너지를 학습하는 Vision-Language-Action (VLA) 모델인 TrackVLA를 제안합니다. 공유된 LLM 백본을 활용하여 인식을 위한 언어 모델링 헤드와 궤적 계획을 위한 앵커 기반 확산 모델을 사용합니다. TrackVLA를 훈련하기 위해 Embodied Visual Tracking Benchmark (EVT-Bench)를 구축하고 다양한 난이도의 인식 샘플을 수집하여 170만 개의 샘플로 구성된 데이터셋을 만들었습니다. 합성 환경과 실제 환경 모두에서의 광범위한 실험을 통해 TrackVLA는 최고 성능과 강력한 일반화 능력을 입증했습니다. 이는 공개 벤치마크에서 제로샷 방식으로 기존 방법을 크게 능가하며, 실제 시나리오에서 10FPS 추론 속도로 높은 동적성과 폐색에 강건함을 유지합니다. 프로젝트 페이지는 다음과 같습니다: https://pku-epic.github.io/TrackVLA-web.
