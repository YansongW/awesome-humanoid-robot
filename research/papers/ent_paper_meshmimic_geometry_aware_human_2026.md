---
$id: ent_paper_meshmimic_geometry_aware_human_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction'
  zh: 'MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction'
  ko: 'MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction'
summary:
  en: 'MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- meshmimic
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.15733v1.
sources:
- id: src_001
  type: paper
  title: 'MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction (arXiv)'
  url: https://arxiv.org/abs/2602.15733
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid motion control has witnessed significant breakthroughs in recent years, with deep reinforcement learning (RL) emerging as a primary catalyst for achieving complex, human-like behaviors. However, the high dimensionality and intricate dynamics of humanoid robots make manual motion design impractical, leading to a heavy reliance on expensive motion capture (MoCap) data. These datasets are not only costly to acquire but also frequently lack the necessary geometric context of the surrounding physical environment. Consequently, existing motion synthesis frameworks often suffer from a decoupling of motion and scene, resulting in physical inconsistencies such as contact slippage or mesh penetration during terrain-aware tasks. In this work, we present MeshMimic, an innovative framework that bridges 3D scene reconstruction and embodied intelligence to enable humanoid robots to learn coupled "motion-terrain" interactions directly from video. By leveraging state-of-the-art 3D vision models, our framework precisely segments and reconstructs both human trajectories and the underlying 3D geometry of terrains and objects. We introduce an optimization algorithm based on kinematic consistency to extract high-quality motion data from noisy visual reconstructions, alongside a contact-invariant retargeting method that transfers human-environment interaction features to the humanoid agent. Experimental results demonstrate that MeshMimic achieves robust, highly dynamic performance across diverse and challenging terrains. Our approach proves that a low-cost pipeline utilizing only consumer-grade monocular sensors can facilitate the training of complex physical interactions, offering a scalable path toward the autonomous evolution of humanoid robots in unstructured environments.

## 核心内容
Humanoid motion control has witnessed significant breakthroughs in recent years, with deep reinforcement learning (RL) emerging as a primary catalyst for achieving complex, human-like behaviors. However, the high dimensionality and intricate dynamics of humanoid robots make manual motion design impractical, leading to a heavy reliance on expensive motion capture (MoCap) data. These datasets are not only costly to acquire but also frequently lack the necessary geometric context of the surrounding physical environment. Consequently, existing motion synthesis frameworks often suffer from a decoupling of motion and scene, resulting in physical inconsistencies such as contact slippage or mesh penetration during terrain-aware tasks. In this work, we present MeshMimic, an innovative framework that bridges 3D scene reconstruction and embodied intelligence to enable humanoid robots to learn coupled "motion-terrain" interactions directly from video. By leveraging state-of-the-art 3D vision models, our framework precisely segments and reconstructs both human trajectories and the underlying 3D geometry of terrains and objects. We introduce an optimization algorithm based on kinematic consistency to extract high-quality motion data from noisy visual reconstructions, alongside a contact-invariant retargeting method that transfers human-environment interaction features to the humanoid agent. Experimental results demonstrate that MeshMimic achieves robust, highly dynamic performance across diverse and challenging terrains. Our approach proves that a low-cost pipeline utilizing only consumer-grade monocular sensors can facilitate the training of complex physical interactions, offering a scalable path toward the autonomous evolution of humanoid robots in unstructured environments.

## 参考
- http://arxiv.org/abs/2602.15733v1

## Overview
Humanoid motion control has witnessed significant breakthroughs in recent years, with deep reinforcement learning (RL) emerging as a primary catalyst for achieving complex, human-like behaviors. However, the high dimensionality and intricate dynamics of humanoid robots make manual motion design impractical, leading to a heavy reliance on expensive motion capture (MoCap) data. These datasets are not only costly to acquire but also frequently lack the necessary geometric context of the surrounding physical environment. Consequently, existing motion synthesis frameworks often suffer from a decoupling of motion and scene, resulting in physical inconsistencies such as contact slippage or mesh penetration during terrain-aware tasks. In this work, we present MeshMimic, an innovative framework that bridges 3D scene reconstruction and embodied intelligence to enable humanoid robots to learn coupled "motion-terrain" interactions directly from video. By leveraging state-of-the-art 3D vision models, our framework precisely segments and reconstructs both human trajectories and the underlying 3D geometry of terrains and objects. We introduce an optimization algorithm based on kinematic consistency to extract high-quality motion data from noisy visual reconstructions, alongside a contact-invariant retargeting method that transfers human-environment interaction features to the humanoid agent. Experimental results demonstrate that MeshMimic achieves robust, highly dynamic performance across diverse and challenging terrains. Our approach proves that a low-cost pipeline utilizing only consumer-grade monocular sensors can facilitate the training of complex physical interactions, offering a scalable path toward the autonomous evolution of humanoid robots in unstructured environments.

## Content
Humanoid motion control has witnessed significant breakthroughs in recent years, with deep reinforcement learning (RL) emerging as a primary catalyst for achieving complex, human-like behaviors. However, the high dimensionality and intricate dynamics of humanoid robots make manual motion design impractical, leading to a heavy reliance on expensive motion capture (MoCap) data. These datasets are not only costly to acquire but also frequently lack the necessary geometric context of the surrounding physical environment. Consequently, existing motion synthesis frameworks often suffer from a decoupling of motion and scene, resulting in physical inconsistencies such as contact slippage or mesh penetration during terrain-aware tasks. In this work, we present MeshMimic, an innovative framework that bridges 3D scene reconstruction and embodied intelligence to enable humanoid robots to learn coupled "motion-terrain" interactions directly from video. By leveraging state-of-the-art 3D vision models, our framework precisely segments and reconstructs both human trajectories and the underlying 3D geometry of terrains and objects. We introduce an optimization algorithm based on kinematic consistency to extract high-quality motion data from noisy visual reconstructions, alongside a contact-invariant retargeting method that transfers human-environment interaction features to the humanoid agent. Experimental results demonstrate that MeshMimic achieves robust, highly dynamic performance across diverse and challenging terrains. Our approach proves that a low-cost pipeline utilizing only consumer-grade monocular sensors can facilitate the training of complex physical interactions, offering a scalable path toward the autonomous evolution of humanoid robots in unstructured environments.

## 개요
휴머노이드 모션 제어는 최근 몇 년간 상당한 돌파구를 마련했으며, 심층 강화 학습(RL)이 복잡하고 인간과 유사한 행동을 구현하는 주요 촉매제로 부상했습니다. 그러나 휴머노이드 로봇의 높은 차원성과 복잡한 동역학으로 인해 수동 모션 설계는 비실용적이며, 고가의 모션 캡처(MoCap) 데이터에 크게 의존하게 됩니다. 이러한 데이터셋은 획득 비용이 높을 뿐만 아니라 주변 물리적 환경의 필요한 기하학적 맥락이 자주 부족합니다. 결과적으로 기존 모션 합성 프레임워크는 종종 모션과 장면의 분리로 인해 지형 인식 작업 중 접촉 미끄러짐이나 메쉬 관통과 같은 물리적 불일치를 겪습니다. 본 연구에서는 3D 장면 재구성과 체화된 지능을 연결하여 휴머노이드 로봇이 비디오에서 직접 결합된 "모션-지형" 상호작용을 학습할 수 있도록 하는 혁신적인 프레임워크인 MeshMimic을 제시합니다. 최첨단 3D 비전 모델을 활용하여, 우리의 프레임워크는 인간 궤적과 지형 및 객체의 기저 3D 기하학을 정밀하게 분할하고 재구성합니다. 우리는 운동학적 일관성에 기반한 최적화 알고리즘을 도입하여 노이즈가 있는 시각적 재구성에서 고품질 모션 데이터를 추출하고, 접촉 불변 리타겟팅 방법을 통해 인간-환경 상호작용 특징을 휴머노이드 에이전트로 전송합니다. 실험 결과는 MeshMimic이 다양하고 도전적인 지형에서 강력하고 고도로 동적인 성능을 달성함을 보여줍니다. 우리의 접근 방식은 소비자용 단안 센서만을 활용하는 저비용 파이프라인이 복잡한 물리적 상호작용 훈련을 촉진할 수 있음을 증명하며, 비구조적 환경에서 휴머노이드 로봇의 자율적 진화를 위한 확장 가능한 경로를 제공합니다.

## 핵심 내용
휴머노이드 모션 제어는 최근 몇 년간 상당한 돌파구를 마련했으며, 심층 강화 학습(RL)이 복잡하고 인간과 유사한 행동을 구현하는 주요 촉매제로 부상했습니다. 그러나 휴머노이드 로봇의 높은 차원성과 복잡한 동역학으로 인해 수동 모션 설계는 비실용적이며, 고가의 모션 캡처(MoCap) 데이터에 크게 의존하게 됩니다. 이러한 데이터셋은 획득 비용이 높을 뿐만 아니라 주변 물리적 환경의 필요한 기하학적 맥락이 자주 부족합니다. 결과적으로 기존 모션 합성 프레임워크는 종종 모션과 장면의 분리로 인해 지형 인식 작업 중 접촉 미끄러짐이나 메쉬 관통과 같은 물리적 불일치를 겪습니다. 본 연구에서는 3D 장면 재구성과 체화된 지능을 연결하여 휴머노이드 로봇이 비디오에서 직접 결합된 "모션-지형" 상호작용을 학습할 수 있도록 하는 혁신적인 프레임워크인 MeshMimic을 제시합니다. 최첨단 3D 비전 모델을 활용하여, 우리의 프레임워크는 인간 궤적과 지형 및 객체의 기저 3D 기하학을 정밀하게 분할하고 재구성합니다. 우리는 운동학적 일관성에 기반한 최적화 알고리즘을 도입하여 노이즈가 있는 시각적 재구성에서 고품질 모션 데이터를 추출하고, 접촉 불변 리타겟팅 방법을 통해 인간-환경 상호작용 특징을 휴머노이드 에이전트로 전송합니다. 실험 결과는 MeshMimic이 다양하고 도전적인 지형에서 강력하고 고도로 동적인 성능을 달성함을 보여줍니다. 우리의 접근 방식은 소비자용 단안 센서만을 활용하는 저비용 파이프라인이 복잡한 물리적 상호작용 훈련을 촉진할 수 있음을 증명하며, 비구조적 환경에서 휴머노이드 로봇의 자율적 진화를 위한 확장 가능한 경로를 제공합니다.
