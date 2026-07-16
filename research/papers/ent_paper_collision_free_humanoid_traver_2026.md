---
$id: ent_paper_collision_free_humanoid_traver_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes
  zh: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes
  ko: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes
summary:
  en: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- collision_free_humanoid_traver
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.16035v2.
sources:
- id: src_001
  type: paper
  title: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes (arXiv)
  url: https://arxiv.org/abs/2601.16035
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We study the problem of collision-free humanoid traversal in cluttered indoor scenes, such as hurdling over objects scattered on the floor, crouching under low-hanging obstacles, or squeezing through narrow passages. To achieve this goal, the humanoid needs to map its perception of surrounding obstacles with diverse spatial layouts and geometries to the corresponding traversal skills. However, the lack of an effective representation that captures humanoid-obstacle relationships during collision avoidance makes directly learning such mappings difficult. We therefore propose Humanoid Potential Field (HumanoidPF), which encodes these relationships as collision-free motion directions, significantly facilitating RL-based traversal skill learning. We also find that HumanoidPF exhibits a surprisingly negligible sim-to-real gap as a perceptual representation. To further enable generalizable traversal skills through diverse and challenging cluttered indoor scenes, we further propose a hybrid scene generation method, incorporating crops of realistic 3D indoor scenes and procedurally synthesized obstacles. We successfully transfer our policy to the real world and develop a teleoperation system where users could command the humanoid to traverse in cluttered indoor scenes with just a single click. Extensive experiments are conducted in both simulation and the real world to validate the effectiveness of our method. Demos and code can be found in our website: https://axian12138.github.io/CAT/.

## 核心内容
We study the problem of collision-free humanoid traversal in cluttered indoor scenes, such as hurdling over objects scattered on the floor, crouching under low-hanging obstacles, or squeezing through narrow passages. To achieve this goal, the humanoid needs to map its perception of surrounding obstacles with diverse spatial layouts and geometries to the corresponding traversal skills. However, the lack of an effective representation that captures humanoid-obstacle relationships during collision avoidance makes directly learning such mappings difficult. We therefore propose Humanoid Potential Field (HumanoidPF), which encodes these relationships as collision-free motion directions, significantly facilitating RL-based traversal skill learning. We also find that HumanoidPF exhibits a surprisingly negligible sim-to-real gap as a perceptual representation. To further enable generalizable traversal skills through diverse and challenging cluttered indoor scenes, we further propose a hybrid scene generation method, incorporating crops of realistic 3D indoor scenes and procedurally synthesized obstacles. We successfully transfer our policy to the real world and develop a teleoperation system where users could command the humanoid to traverse in cluttered indoor scenes with just a single click. Extensive experiments are conducted in both simulation and the real world to validate the effectiveness of our method. Demos and code can be found in our website: https://axian12138.github.io/CAT/.

## 参考
- http://arxiv.org/abs/2601.16035v2

## Overview
We study the problem of collision-free humanoid traversal in cluttered indoor scenes, such as hurdling over objects scattered on the floor, crouching under low-hanging obstacles, or squeezing through narrow passages. To achieve this goal, the humanoid needs to map its perception of surrounding obstacles with diverse spatial layouts and geometries to the corresponding traversal skills. However, the lack of an effective representation that captures humanoid-obstacle relationships during collision avoidance makes directly learning such mappings difficult. We therefore propose Humanoid Potential Field (HumanoidPF), which encodes these relationships as collision-free motion directions, significantly facilitating RL-based traversal skill learning. We also find that HumanoidPF exhibits a surprisingly negligible sim-to-real gap as a perceptual representation. To further enable generalizable traversal skills through diverse and challenging cluttered indoor scenes, we further propose a hybrid scene generation method, incorporating crops of realistic 3D indoor scenes and procedurally synthesized obstacles. We successfully transfer our policy to the real world and develop a teleoperation system where users could command the humanoid to traverse in cluttered indoor scenes with just a single click. Extensive experiments are conducted in both simulation and the real world to validate the effectiveness of our method. Demos and code can be found in our website: https://axian12138.github.io/CAT/.

## Content
We study the problem of collision-free humanoid traversal in cluttered indoor scenes, such as hurdling over objects scattered on the floor, crouching under low-hanging obstacles, or squeezing through narrow passages. To achieve this goal, the humanoid needs to map its perception of surrounding obstacles with diverse spatial layouts and geometries to the corresponding traversal skills. However, the lack of an effective representation that captures humanoid-obstacle relationships during collision avoidance makes directly learning such mappings difficult. We therefore propose Humanoid Potential Field (HumanoidPF), which encodes these relationships as collision-free motion directions, significantly facilitating RL-based traversal skill learning. We also find that HumanoidPF exhibits a surprisingly negligible sim-to-real gap as a perceptual representation. To further enable generalizable traversal skills through diverse and challenging cluttered indoor scenes, we further propose a hybrid scene generation method, incorporating crops of realistic 3D indoor scenes and procedurally synthesized obstacles. We successfully transfer our policy to the real world and develop a teleoperation system where users could command the humanoid to traverse in cluttered indoor scenes with just a single click. Extensive experiments are conducted in both simulation and the real world to validate the effectiveness of our method. Demos and code can be found in our website: https://axian12138.github.io/CAT/.

## 개요
본 연구는 복잡한 실내 환경에서 인간형 로봇의 충돌 없는 이동 문제를 다룹니다. 예를 들어 바닥에 흩어진 장애물을 뛰어넘거나, 낮게 걸린 장애물 아래로 웅크려 지나가거나, 좁은 통로를 비집고 지나가는 등의 상황을 포함합니다. 이러한 목표를 달성하기 위해 인간형 로봇은 다양한 공간 배치와 기하학적 형태를 가진 주변 장애물에 대한 인식을 해당 이동 기술에 매핑해야 합니다. 그러나 충돌 회피 과정에서 인간형 로봇과 장애물 간의 관계를 포착하는 효과적인 표현이 부족하여 이러한 매핑을 직접 학습하기 어렵습니다. 따라서 우리는 **Humanoid Potential Field (HumanoidPF)**를 제안합니다. 이는 이러한 관계를 충돌 없는 이동 방향으로 인코딩하여 강화 학습 기반 이동 기술 학습을 크게 촉진합니다. 또한 HumanoidPF는 지각 표현으로서 시뮬레이션과 실제 환경 간의 격차가 놀라울 정도로 미미함을 발견했습니다. 다양하고 도전적인 복잡한 실내 환경에서 일반화 가능한 이동 기술을 더욱 가능하게 하기 위해, 현실적인 3D 실내 장면의 일부와 절차적으로 합성된 장애물을 결합한 하이브리드 장면 생성 방법을 추가로 제안합니다. 우리는 정책을 실제 세계로 성공적으로 전이하고, 사용자가 단 한 번의 클릭으로 인간형 로봇을 복잡한 실내 환경에서 이동하도록 명령할 수 있는 원격 조작 시스템을 개발했습니다. 시뮬레이션과 실제 환경 모두에서 광범위한 실험을 수행하여 방법의 효과를 검증했습니다. 데모와 코드는 웹사이트(https://axian12138.github.io/CAT/)에서 확인할 수 있습니다.

## 핵심 내용
본 연구는 복잡한 실내 환경에서 인간형 로봇의 충돌 없는 이동 문제를 다룹니다. 예를 들어 바닥에 흩어진 장애물을 뛰어넘거나, 낮게 걸린 장애물 아래로 웅크려 지나가거나, 좁은 통로를 비집고 지나가는 등의 상황을 포함합니다. 이러한 목표를 달성하기 위해 인간형 로봇은 다양한 공간 배치와 기하학적 형태를 가진 주변 장애물에 대한 인식을 해당 이동 기술에 매핑해야 합니다. 그러나 충돌 회피 과정에서 인간형 로봇과 장애물 간의 관계를 포착하는 효과적인 표현이 부족하여 이러한 매핑을 직접 학습하기 어렵습니다. 따라서 우리는 **Humanoid Potential Field (HumanoidPF)**를 제안합니다. 이는 이러한 관계를 충돌 없는 이동 방향으로 인코딩하여 강화 학습 기반 이동 기술 학습을 크게 촉진합니다. 또한 HumanoidPF는 지각 표현으로서 시뮬레이션과 실제 환경 간의 격차가 놀라울 정도로 미미함을 발견했습니다. 다양하고 도전적인 복잡한 실내 환경에서 일반화 가능한 이동 기술을 더욱 가능하게 하기 위해, 현실적인 3D 실내 장면의 일부와 절차적으로 합성된 장애물을 결합한 하이브리드 장면 생성 방법을 추가로 제안합니다. 우리는 정책을 실제 세계로 성공적으로 전이하고, 사용자가 단 한 번의 클릭으로 인간형 로봇을 복잡한 실내 환경에서 이동하도록 명령할 수 있는 원격 조작 시스템을 개발했습니다. 시뮬레이션과 실제 환경 모두에서 광범위한 실험을 수행하여 방법의 효과를 검증했습니다. 데모와 코드는 웹사이트(https://axian12138.github.io/CAT/)에서 확인할 수 있습니다.
