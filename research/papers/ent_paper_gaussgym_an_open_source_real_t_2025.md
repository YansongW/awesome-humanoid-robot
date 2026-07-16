---
$id: ent_paper_gaussgym_an_open_source_real_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
  zh: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
  ko: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
summary:
  en: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels is a 2025 work on locomotion for
    humanoid robots.'
  zh: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels is a 2025 work on locomotion for
    humanoid robots.'
  ko: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels is a 2025 work on locomotion for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gaussgym
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.15352v1.
sources:
- id: src_001
  type: paper
  title: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels (arXiv)'
  url: https://arxiv.org/abs/2510.15352
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present a novel approach for photorealistic robot simulation that integrates 3D Gaussian Splatting as a drop-in renderer within vectorized physics simulators such as IsaacGym. This enables unprecedented speed -- exceeding 100,000 steps per second on consumer GPUs -- while maintaining high visual fidelity, which we showcase across diverse tasks. We additionally demonstrate its applicability in a sim-to-real robotics setting. Beyond depth-based sensing, our results highlight how rich visual semantics improve navigation and decision-making, such as avoiding undesirable regions. We further showcase the ease of incorporating thousands of environments from iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit), and outputs from generative video models like Veo, enabling rapid creation of realistic training worlds. This work bridges high-throughput simulation and high-fidelity perception, advancing scalable and generalizable robot learning. All code and data will be open-sourced for the community to build upon. Videos, code, and data available at https://escontrela.me/gauss_gym/.

## 核心内容
We present a novel approach for photorealistic robot simulation that integrates 3D Gaussian Splatting as a drop-in renderer within vectorized physics simulators such as IsaacGym. This enables unprecedented speed -- exceeding 100,000 steps per second on consumer GPUs -- while maintaining high visual fidelity, which we showcase across diverse tasks. We additionally demonstrate its applicability in a sim-to-real robotics setting. Beyond depth-based sensing, our results highlight how rich visual semantics improve navigation and decision-making, such as avoiding undesirable regions. We further showcase the ease of incorporating thousands of environments from iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit), and outputs from generative video models like Veo, enabling rapid creation of realistic training worlds. This work bridges high-throughput simulation and high-fidelity perception, advancing scalable and generalizable robot learning. All code and data will be open-sourced for the community to build upon. Videos, code, and data available at https://escontrela.me/gauss_gym/.

## 参考
- http://arxiv.org/abs/2510.15352v1

## Overview
We present a novel approach for photorealistic robot simulation that integrates 3D Gaussian Splatting as a drop-in renderer within vectorized physics simulators such as IsaacGym. This enables unprecedented speed -- exceeding 100,000 steps per second on consumer GPUs -- while maintaining high visual fidelity, which we showcase across diverse tasks. We additionally demonstrate its applicability in a sim-to-real robotics setting. Beyond depth-based sensing, our results highlight how rich visual semantics improve navigation and decision-making, such as avoiding undesirable regions. We further showcase the ease of incorporating thousands of environments from iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit), and outputs from generative video models like Veo, enabling rapid creation of realistic training worlds. This work bridges high-throughput simulation and high-fidelity perception, advancing scalable and generalizable robot learning. All code and data will be open-sourced for the community to build upon. Videos, code, and data available at https://escontrela.me/gauss_gym/.

## Content
We present a novel approach for photorealistic robot simulation that integrates 3D Gaussian Splatting as a drop-in renderer within vectorized physics simulators such as IsaacGym. This enables unprecedented speed -- exceeding 100,000 steps per second on consumer GPUs -- while maintaining high visual fidelity, which we showcase across diverse tasks. We additionally demonstrate its applicability in a sim-to-real robotics setting. Beyond depth-based sensing, our results highlight how rich visual semantics improve navigation and decision-making, such as avoiding undesirable regions. We further showcase the ease of incorporating thousands of environments from iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit), and outputs from generative video models like Veo, enabling rapid creation of realistic training worlds. This work bridges high-throughput simulation and high-fidelity perception, advancing scalable and generalizable robot learning. All code and data will be open-sourced for the community to build upon. Videos, code, and data available at https://escontrela.me/gauss_gym/.

## 개요
본 논문은 3D 가우시안 스플래팅(3D Gaussian Splatting)을 IsaacGym과 같은 벡터화된 물리 시뮬레이터 내에서 플러그인 렌더러로 통합하는 사실적인 로봇 시뮬레이션을 위한 새로운 접근 방식을 제시합니다. 이를 통해 소비자용 GPU에서 초당 100,000 스텝을 초과하는 전례 없는 속도를 달성하면서도 높은 시각적 충실도를 유지하며, 다양한 작업에서 그 성능을 입증합니다. 또한 sim-to-real 로봇 환경에서의 적용 가능성을 보여줍니다. 깊이 기반 센싱을 넘어, 풍부한 시각적 의미론이 바람직하지 않은 영역을 회피하는 등 내비게이션과 의사 결정을 어떻게 개선하는지 강조합니다. iPhone 스캔, 대규모 장면 데이터셋(예: GrandTour, ARKit), Veo와 같은 생성형 비디오 모델의 출력물을 통해 수천 개의 환경을 손쉽게 통합하여 현실적인 훈련 세계를 신속하게 생성할 수 있음을 추가로 보여줍니다. 이 연구는 고처리량 시뮬레이션과 고충실도 인식을 연결하여 확장 가능하고 일반화 가능한 로봇 학습을 발전시킵니다. 모든 코드와 데이터는 커뮤니티가 활용할 수 있도록 오픈소스로 공개될 예정입니다. 비디오, 코드, 데이터는 https://escontrela.me/gauss_gym/에서 확인할 수 있습니다.

## 핵심 내용
본 논문은 3D 가우시안 스플래팅(3D Gaussian Splatting)을 IsaacGym과 같은 벡터화된 물리 시뮬레이터 내에서 플러그인 렌더러로 통합하는 사실적인 로봇 시뮬레이션을 위한 새로운 접근 방식을 제시합니다. 이를 통해 소비자용 GPU에서 초당 100,000 스텝을 초과하는 전례 없는 속도를 달성하면서도 높은 시각적 충실도를 유지하며, 다양한 작업에서 그 성능을 입증합니다. 또한 sim-to-real 로봇 환경에서의 적용 가능성을 보여줍니다. 깊이 기반 센싱을 넘어, 풍부한 시각적 의미론이 바람직하지 않은 영역을 회피하는 등 내비게이션과 의사 결정을 어떻게 개선하는지 강조합니다. iPhone 스캔, 대규모 장면 데이터셋(예: GrandTour, ARKit), Veo와 같은 생성형 비디오 모델의 출력물을 통해 수천 개의 환경을 손쉽게 통합하여 현실적인 훈련 세계를 신속하게 생성할 수 있음을 추가로 보여줍니다. 이 연구는 고처리량 시뮬레이션과 고충실도 인식을 연결하여 확장 가능하고 일반화 가능한 로봇 학습을 발전시킵니다. 모든 코드와 데이터는 커뮤니티가 활용할 수 있도록 오픈소스로 공개될 예정입니다. 비디오, 코드, 데이터는 https://escontrela.me/gauss_gym/에서 확인할 수 있습니다.
