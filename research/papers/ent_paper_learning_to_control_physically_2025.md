---
$id: ent_paper_learning_to_control_physically_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
  zh: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
  ko: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
summary:
  en: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a 2025 work on physics-based
    character animation for humanoid robots.
  zh: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a 2025 work on physics-based
    character animation for humanoid robots.
  ko: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a 2025 work on physics-based
    character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- learning_to_control_physically
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08500v1.
sources:
- id: src_001
  type: paper
  title: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions (arXiv)
  url: https://arxiv.org/abs/2512.08500
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 核心内容
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 参考
- http://arxiv.org/abs/2512.08500v1

## Overview
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## Content
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 개요
비디오 데이터는 3D 캐릭터 모션 컨트롤러를 학습하는 데 모션 캡처 데이터보다 비용 효율적이지만, 비디오에서 직접 현실적이고 다양한 행동을 합성하는 것은 여전히 어려운 과제입니다. 기존 접근 방식은 일반적으로 물리 기반 모방을 위해 기성 모션 재구성 기술을 사용하여 3D 궤적을 얻습니다. 이러한 재구성 방법은 일반화에 어려움을 겪는데, 3D 학습 데이터(잠재적으로 부족할 수 있음)가 필요하거나 물리적으로 타당한 포즈를 생성하지 못해 인간-객체 상호작용(HOI)이나 비인간 캐릭터와 같은 까다로운 시나리오에 적용하기 어렵습니다. 우리는 비디오에서 추출한 널리 사용 가능한 2D 키포인트 궤적만을 직접 활용하여 제어 정책을 학습하는 새로운 모션 모방 프레임워크인 Mimic2DM을 도입하여 이 문제를 해결합니다. 재투영 오차를 최소화함으로써, 2D 모션 데이터만을 사용하여 물리 시뮬레이션에서 임의의 2D 참조 모션을 추적할 수 있는 일반적인 단일 시점 2D 모션 추적 정책을 학습합니다. 이 정책은 서로 다른 또는 약간 다른 시점에서 캡처된 다양한 2D 모션으로 학습될 경우, 여러 시점을 집계하여 3D 모션 추적 능력을 추가로 획득할 수 있습니다. 또한, 우리는 트랜스포머 기반의 자기회귀 2D 모션 생성기를 개발하고 이를 계층적 제어 프레임워크에 통합하여, 생성기가 고품질의 2D 참조 궤적을 생성하여 추적 정책을 안내하도록 합니다. 제안된 접근 방식은 다재다능하며, 명시적인 3D 모션 데이터에 의존하지 않고 춤, 축구 드리블, 동물 움직임 등 다양한 영역에서 물리적으로 타당하고 다양한 모션을 효과적으로 학습하여 합성할 수 있음을 보여줍니다. 프로젝트 웹사이트: https://jiann-li.github.io/mimic2dm/

## 핵심 내용
비디오 데이터는 3D 캐릭터 모션 컨트롤러를 학습하는 데 모션 캡처 데이터보다 비용 효율적이지만, 비디오에서 직접 현실적이고 다양한 행동을 합성하는 것은 여전히 어려운 과제입니다. 기존 접근 방식은 일반적으로 물리 기반 모방을 위해 기성 모션 재구성 기술을 사용하여 3D 궤적을 얻습니다. 이러한 재구성 방법은 일반화에 어려움을 겪는데, 3D 학습 데이터(잠재적으로 부족할 수 있음)가 필요하거나 물리적으로 타당한 포즈를 생성하지 못해 인간-객체 상호작용(HOI)이나 비인간 캐릭터와 같은 까다로운 시나리오에 적용하기 어렵습니다. 우리는 비디오에서 추출한 널리 사용 가능한 2D 키포인트 궤적만을 직접 활용하여 제어 정책을 학습하는 새로운 모션 모방 프레임워크인 Mimic2DM을 도입하여 이 문제를 해결합니다. 재투영 오차를 최소화함으로써, 2D 모션 데이터만을 사용하여 물리 시뮬레이션에서 임의의 2D 참조 모션을 추적할 수 있는 일반적인 단일 시점 2D 모션 추적 정책을 학습합니다. 이 정책은 서로 다른 또는 약간 다른 시점에서 캡처된 다양한 2D 모션으로 학습될 경우, 여러 시점을 집계하여 3D 모션 추적 능력을 추가로 획득할 수 있습니다. 또한, 우리는 트랜스포머 기반의 자기회귀 2D 모션 생성기를 개발하고 이를 계층적 제어 프레임워크에 통합하여, 생성기가 고품질의 2D 참조 궤적을 생성하여 추적 정책을 안내하도록 합니다. 제안된 접근 방식은 다재다능하며, 명시적인 3D 모션 데이터에 의존하지 않고 춤, 축구 드리블, 동물 움직임 등 다양한 영역에서 물리적으로 타당하고 다양한 모션을 효과적으로 학습하여 합성할 수 있음을 보여줍니다. 프로젝트 웹사이트: https://jiann-li.github.io/mimic2dm/
