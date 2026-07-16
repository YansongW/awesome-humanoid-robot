---
$id: ent_paper_deepmimic_example_guided_deep_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'
  zh: 很多人形控制论文的源头问题
  ko: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'
summary:
  en: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills is a knowledge node related
    to paper in the humanoid robot value chain.'
  zh: A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can
    execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental
    variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies
    capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes
    in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such
    as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective,
    we can train characters that react intelligently in interactive settings, e
  ko: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills is a knowledge node related
    to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- behavioral_foundation_model
- imitation_learning
- motion_tracker
- motion_tracking
- physics_based_control
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1804.02717v3.
sources:
- id: src_001
  type: paper
  title: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills (arXiv)'
  url: https://arxiv.org/abs/1804.02717
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 很多人形控制论文的源头问题 project page
  url: https://xbpeng.github.io/projects/DeepMimic/index.html
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective, we can train characters that react intelligently in interactive settings, e.g., by walking in a desired direction or throwing a ball at a user-specified target. This approach thus combines the convenience and motion quality of using motion clips to define the desired style and appearance, with the flexibility and generality afforded by RL methods and physics-based animation. We further explore a number of methods for integrating multiple clips into the learning process to develop multi-skilled agents capable of performing a rich repertoire of diverse skills. We demonstrate results using multiple characters (human, Atlas robot, bipedal dinosaur, dragon) and a large variety of skills, including locomotion, acrobatics, and martial arts.

## 核心内容
A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective, we can train characters that react intelligently in interactive settings, e.g., by walking in a desired direction or throwing a ball at a user-specified target. This approach thus combines the convenience and motion quality of using motion clips to define the desired style and appearance, with the flexibility and generality afforded by RL methods and physics-based animation. We further explore a number of methods for integrating multiple clips into the learning process to develop multi-skilled agents capable of performing a rich repertoire of diverse skills. We demonstrate results using multiple characters (human, Atlas robot, bipedal dinosaur, dragon) and a large variety of skills, including locomotion, acrobatics, and martial arts.

## 参考
- http://arxiv.org/abs/1804.02717v3

## Overview
A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective, we can train characters that react intelligently in interactive settings, e.g., by walking in a desired direction or throwing a ball at a user-specified target. This approach thus combines the convenience and motion quality of using motion clips to define the desired style and appearance, with the flexibility and generality afforded by RL methods and physics-based animation. We further explore a number of methods for integrating multiple clips into the learning process to develop multi-skilled agents capable of performing a rich repertoire of diverse skills. We demonstrate results using multiple characters (human, Atlas robot, bipedal dinosaur, dragon) and a large variety of skills, including locomotion, acrobatics, and martial arts.

## Content
A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective, we can train characters that react intelligently in interactive settings, e.g., by walking in a desired direction or throwing a ball at a user-specified target. This approach thus combines the convenience and motion quality of using motion clips to define the desired style and appearance, with the flexibility and generality afforded by RL methods and physics-based animation. We further explore a number of methods for integrating multiple clips into the learning process to develop multi-skilled agents capable of performing a rich repertoire of diverse skills. We demonstrate results using multiple characters (human, Atlas robot, bipedal dinosaur, dragon) and a large variety of skills, including locomotion, acrobatics, and martial arts.

## 개요
캐릭터 애니메이션의 오랜 목표 중 하나는 데이터 기반 행동 명세와 물리 시뮬레이션에서 유사한 행동을 실행할 수 있는 시스템을 결합하여, 외란 및 환경 변화에 현실적으로 대응할 수 있도록 하는 것입니다. 우리는 잘 알려진 강화 학습(RL) 방법을 적용하여 다양한 예제 모션 클립을 모방할 수 있는 강건한 제어 정책을 학습하는 동시에, 복잡한 회복 동작, 형태 변화 적응, 사용자 지정 목표 달성도 학습할 수 있음을 보여줍니다. 우리의 방법은 키프레임 모션, 모션 캡처 플립 및 스핀과 같은 고역학적 동작, 그리고 리타겟팅된 모션을 처리합니다. 모션 모방 목표와 작업 목표를 결합함으로써, 원하는 방향으로 걷거나 사용자가 지정한 목표물에 공을 던지는 등 상호작용 환경에서 지능적으로 반응하는 캐릭터를 훈련할 수 있습니다. 이 접근법은 원하는 스타일과 외형을 정의하기 위해 모션 클립을 사용하는 편의성과 모션 품질을, RL 방법과 물리 기반 애니메이션이 제공하는 유연성 및 일반성과 결합합니다. 또한, 여러 클립을 학습 과정에 통합하여 다양한 기술을 수행할 수 있는 다중 기술 에이전트를 개발하는 여러 방법을 탐구합니다. 우리는 여러 캐릭터(인간, 아틀라스 로봇, 이족 보행 공룡, 드래곤)와 다양한 기술(보행, 곡예, 무술 포함)을 사용한 결과를 보여줍니다.

## 핵심 내용
캐릭터 애니메이션의 오랜 목표 중 하나는 데이터 기반 행동 명세와 물리 시뮬레이션에서 유사한 행동을 실행할 수 있는 시스템을 결합하여, 외란 및 환경 변화에 현실적으로 대응할 수 있도록 하는 것입니다. 우리는 잘 알려진 강화 학습(RL) 방법을 적용하여 다양한 예제 모션 클립을 모방할 수 있는 강건한 제어 정책을 학습하는 동시에, 복잡한 회복 동작, 형태 변화 적응, 사용자 지정 목표 달성도 학습할 수 있음을 보여줍니다. 우리의 방법은 키프레임 모션, 모션 캡처 플립 및 스핀과 같은 고역학적 동작, 그리고 리타겟팅된 모션을 처리합니다. 모션 모방 목표와 작업 목표를 결합함으로써, 원하는 방향으로 걷거나 사용자가 지정한 목표물에 공을 던지는 등 상호작용 환경에서 지능적으로 반응하는 캐릭터를 훈련할 수 있습니다. 이 접근법은 원하는 스타일과 외형을 정의하기 위해 모션 클립을 사용하는 편의성과 모션 품질을, RL 방법과 물리 기반 애니메이션이 제공하는 유연성 및 일반성과 결합합니다. 또한, 여러 클립을 학습 과정에 통합하여 다양한 기술을 수행할 수 있는 다중 기술 에이전트를 개발하는 여러 방법을 탐구합니다. 우리는 여러 캐릭터(인간, 아틀라스 로봇, 이족 보행 공룡, 드래곤)와 다양한 기술(보행, 곡예, 무술 포함)을 사용한 결과를 보여줍니다.
