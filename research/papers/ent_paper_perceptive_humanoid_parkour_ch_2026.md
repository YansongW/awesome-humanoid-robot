---
$id: ent_paper_perceptive_humanoid_parkour_ch_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching'
  zh: 跑酷的难点不是单技能，而是长程组合
  ko: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching'
summary:
  en: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching is a knowledge node related to paper
    in the humanoid robot value chain.'
  zh: While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility
    and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments
    demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and
    perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that
    enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses.
    Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted
    atomic human skills into long-horizon kinematic trajectories. This frame
  ko: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching is a knowledge node related to paper
    in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.15827v2.
sources:
- id: src_001
  type: paper
  title: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching (arXiv)'
  url: https://arxiv.org/abs/2602.15827
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 跑酷的难点不是单技能，而是长程组合 project page
  url: https://php-parkour.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses. Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted atomic human skills into long-horizon kinematic trajectories. This framework enables the flexible composition and smooth transition of complex skill chains while preserving the elegance and fluidity of dynamic human motions. Next, we train motion-tracking reinforcement learning (RL) expert policies for these composed motions, and distill them into a single depth-based, multi-skill student policy, using a combination of DAgger and RL. Crucially, the combination of perception and skill composition enables autonomous, context-aware decision-making: using only onboard depth sensing and a discrete 2D velocity command, the robot selects and executes whether to step over, climb onto, vault or roll off obstacles of varying geometries and heights. We validate our framework with extensive real-world experiments on a Unitree G1 humanoid robot, demonstrating highly dynamic parkour skills such as climbing tall obstacles up to 1.25m (96% robot height), as well as long-horizon multi-obstacle traversal with closed-loop adaptation to real-time obstacle perturbations.

## 核心内容
While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses. Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted atomic human skills into long-horizon kinematic trajectories. This framework enables the flexible composition and smooth transition of complex skill chains while preserving the elegance and fluidity of dynamic human motions. Next, we train motion-tracking reinforcement learning (RL) expert policies for these composed motions, and distill them into a single depth-based, multi-skill student policy, using a combination of DAgger and RL. Crucially, the combination of perception and skill composition enables autonomous, context-aware decision-making: using only onboard depth sensing and a discrete 2D velocity command, the robot selects and executes whether to step over, climb onto, vault or roll off obstacles of varying geometries and heights. We validate our framework with extensive real-world experiments on a Unitree G1 humanoid robot, demonstrating highly dynamic parkour skills such as climbing tall obstacles up to 1.25m (96% robot height), as well as long-horizon multi-obstacle traversal with closed-loop adaptation to real-time obstacle perturbations.

## 参考
- http://arxiv.org/abs/2602.15827v2

## Overview
While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses. Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted atomic human skills into long-horizon kinematic trajectories. This framework enables the flexible composition and smooth transition of complex skill chains while preserving the elegance and fluidity of dynamic human motions. Next, we train motion-tracking reinforcement learning (RL) expert policies for these composed motions, and distill them into a single depth-based, multi-skill student policy, using a combination of DAgger and RL. Crucially, the combination of perception and skill composition enables autonomous, context-aware decision-making: using only onboard depth sensing and a discrete 2D velocity command, the robot selects and executes whether to step over, climb onto, vault or roll off obstacles of varying geometries and heights. We validate our framework with extensive real-world experiments on a Unitree G1 humanoid robot, demonstrating highly dynamic parkour skills such as climbing tall obstacles up to 1.25m (96% robot height), as well as long-horizon multi-obstacle traversal with closed-loop adaptation to real-time obstacle perturbations.

## Content
While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses. Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted atomic human skills into long-horizon kinematic trajectories. This framework enables the flexible composition and smooth transition of complex skill chains while preserving the elegance and fluidity of dynamic human motions. Next, we train motion-tracking reinforcement learning (RL) expert policies for these composed motions, and distill them into a single depth-based, multi-skill student policy, using a combination of DAgger and RL. Crucially, the combination of perception and skill composition enables autonomous, context-aware decision-making: using only onboard depth sensing and a discrete 2D velocity command, the robot selects and executes whether to step over, climb onto, vault or roll off obstacles of varying geometries and heights. We validate our framework with extensive real-world experiments on a Unitree G1 humanoid robot, demonstrating highly dynamic parkour skills such as climbing tall obstacles up to 1.25m (96% robot height), as well as long-horizon multi-obstacle traversal with closed-loop adaptation to real-time obstacle perturbations.

## 개요
최근 인간형 로봇 보행 기술의 발전으로 다양한 지형에서 안정적인 보행이 가능해졌지만, 고도로 역동적인 인간 동작의 민첩성과 적응성을 구현하는 것은 여전히 해결되지 않은 과제입니다. 특히 복잡한 환경에서의 민첩한 파쿠르는 저수준의 강건성뿐만 아니라 인간과 유사한 동작 표현력, 장기적인 기술 구성, 그리고 인식 기반 의사 결정을 요구합니다. 본 논문에서는 인간형 로봇이 도전적인 장애물 코스를 자율적으로 장기간 비전 기반 파쿠르를 수행할 수 있도록 하는 모듈식 프레임워크인 Perceptive Humanoid Parkour (PHP)를 제시합니다. 우리의 접근 방식은 먼저 특징 공간에서의 최근접 이웃 탐색으로 정식화된 모션 매칭을 활용하여 리타겟팅된 원자적 인간 기술을 장기적인 운동학적 궤적으로 구성합니다. 이 프레임워크는 역동적인 인간 동작의 우아함과 유연성을 유지하면서 복잡한 기술 체인의 유연한 구성과 부드러운 전환을 가능하게 합니다. 다음으로, 이러한 구성된 동작에 대한 동작 추적 강화 학습(RL) 전문가 정책을 훈련하고, DAgger와 RL의 조합을 사용하여 이를 단일 깊이 기반 다중 기술 학생 정책으로 증류합니다. 결정적으로, 인식과 기술 구성의 결합은 자율적이고 상황 인식적인 의사 결정을 가능하게 합니다: 온보드 깊이 센싱과 이산적인 2D 속도 명령만을 사용하여 로봇은 다양한 기하학적 형태와 높이의 장애물을 넘거나, 올라가거나, 도약하거나, 굴러 내려오는 동작을 선택하고 실행합니다. 우리는 Unitree G1 인간형 로봇을 사용한 광범위한 실제 실험을 통해 프레임워크를 검증했으며, 최대 1.25m(로봇 높이의 96%) 높이의 장애물을 오르는 것과 같은 고도로 역동적인 파쿠르 기술과 실시간 장애물 변동에 대한 폐쇄 루프 적응을 통한 장기간 다중 장애물 통과를 입증했습니다.

## 핵심 내용
최근 인간형 로봇 보행 기술의 발전으로 다양한 지형에서 안정적인 보행이 가능해졌지만, 고도로 역동적인 인간 동작의 민첩성과 적응성을 구현하는 것은 여전히 해결되지 않은 과제입니다. 특히 복잡한 환경에서의 민첩한 파쿠르는 저수준의 강건성뿐만 아니라 인간과 유사한 동작 표현력, 장기적인 기술 구성, 그리고 인식 기반 의사 결정을 요구합니다. 본 논문에서는 인간형 로봇이 도전적인 장애물 코스를 자율적으로 장기간 비전 기반 파쿠르를 수행할 수 있도록 하는 모듈식 프레임워크인 Perceptive Humanoid Parkour (PHP)를 제시합니다. 우리의 접근 방식은 먼저 특징 공간에서의 최근접 이웃 탐색으로 정식화된 모션 매칭을 활용하여 리타겟팅된 원자적 인간 기술을 장기적인 운동학적 궤적으로 구성합니다. 이 프레임워크는 역동적인 인간 동작의 우아함과 유연성을 유지하면서 복잡한 기술 체인의 유연한 구성과 부드러운 전환을 가능하게 합니다. 다음으로, 이러한 구성된 동작에 대한 동작 추적 강화 학습(RL) 전문가 정책을 훈련하고, DAgger와 RL의 조합을 사용하여 이를 단일 깊이 기반 다중 기술 학생 정책으로 증류합니다. 결정적으로, 인식과 기술 구성의 결합은 자율적이고 상황 인식적인 의사 결정을 가능하게 합니다: 온보드 깊이 센싱과 이산적인 2D 속도 명령만을 사용하여 로봇은 다양한 기하학적 형태와 높이의 장애물을 넘거나, 올라가거나, 도약하거나, 굴러 내려오는 동작을 선택하고 실행합니다. 우리는 Unitree G1 인간형 로봇을 사용한 광범위한 실제 실험을 통해 프레임워크를 검증했으며, 최대 1.25m(로봇 높이의 96%) 높이의 장애물을 오르는 것과 같은 고도로 역동적인 파쿠르 기술과 실시간 장애물 변동에 대한 폐쇄 루프 적응을 통한 장기간 다중 장애물 통과를 입증했습니다.
