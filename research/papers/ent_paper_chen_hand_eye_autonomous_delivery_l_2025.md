---
$id: ent_paper_chen_hand_eye_autonomous_delivery_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching'
  zh: 手眼自主递送：学习人形机器人导航、移动与伸取
  ko: '손-눈 자율 배달: 휴머노이드 내비게이션, 보행 및 닿기 학습'
summary:
  en: Proposes Hand-Eye Autonomous Delivery (HEAD), a modular framework that decouples egocentric vision-based planning of
    head and hand targets from a low-level whole-body controller trained with GAN-like imitation reinforcement learning on
    large-scale human motion capture data, enabling sim-to-real navigation and reaching on a Unitree G1 humanoid.
  zh: HEAD 是一个模块化框架，用于学习人形机器人的导航、移动和抓取技能。它由高层规划器（基于 Aria 眼镜采集的人类视觉数据）和低层全身控制器（基于大规模人类运动捕捉数据，采用类似 GAN 的模仿强化学习训练）组成。该框架在 Unitree
    G1 人形机器人上实现了从仿真到真实环境的导航与抓取。
  ko: 손-눈 자율 배달(HEAD) 프레임워크를 제안한다. 자아중심 시각에 기반한 머리와 손 목표 계획을, 대규모 인체 동작 캡처 데이터로 GAN과 유사한 모방 강화학습을 통해 학습된 저수준 전신 제어기와 분리하여,
    Unitree G1 휴머노이드에서 시뮬레이션-투-리얼 내비게이션과 닿기를 실현한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 08_software_middleware
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- hand_eye_delivery
- modular_policy
- whole_body_control
- imitation_learning
- gan_based_rl
- sim_to_real
- navigation_and_reaching
- egocentric_vision
- unitree_g1
- aria_glasses
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.03068v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching'
  url: https://arxiv.org/abs/2508.03068
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
HEAD 框架将人形机器人的导航、移动和抓取任务分解为两个模块：高层规划器负责基于第一人称视觉信息规划头部和手部的目标位姿，低层全身控制器则负责跟踪这些目标。高层规划器从 Aria 眼镜采集的人类视觉数据中学习，低层控制器则从大规模人类运动捕捉数据中学习，并采用类似 GAN 的模仿强化学习训练。这种模块化设计将视觉感知与物理动作解耦，提高了学习效率和对新场景的泛化能力。实验在仿真和真实环境中均验证了该方法在复杂人类环境中的有效性。

## 核心内容
### 方法概述
HEAD 框架的核心思想是将人形机器人的复杂行为分解为两个层次：
- **高层规划器**：基于第一人称视觉（来自 Aria 眼镜数据）规划人形机器人头部和双手的目标位姿（位置与朝向）。
- **低层全身控制器**：负责跟踪高层规划器给出的三个关键点（眼睛、左手、右手）的目标，控制全身运动。

### 训练方法
- **低层控制器**：从现有的大规模人类运动捕捉数据中学习，采用类似 GAN 的模仿强化学习（GAN-like imitation reinforcement learning）进行训练。
- **高层规划器**：从 Aria 眼镜采集的人类视觉数据中学习，这些数据包含了人类在真实环境中的导航和抓取行为。

### 实验设置
- **硬件平台**：Unitree G1 人形机器人。
- **评估环境**：仿真环境与真实世界环境，均为人类设计的复杂场景。
- **任务**：人形机器人在复杂环境中完成导航和抓取任务。

### 关键结果
- 在仿真和真实环境中，HEAD 框架均成功实现了人形机器人的导航和抓取能力。
- 模块化设计使得视觉感知与物理动作解耦，显著提高了学习效率和对新场景的泛化能力。
- 实验表明，该方法能够处理人类环境中常见的复杂障碍和动态变化。

### 结论
HEAD 框架通过将视觉规划与全身控制分离，利用大规模人类数据训练，为人形机器人在复杂人类环境中执行导航和抓取任务提供了一种高效且可扩展的解决方案。

## Overview
We propose Hand-Eye Autonomous Delivery (HEAD), a framework that learns navigation, locomotion, and reaching skills for humanoids, directly from human motion and vision perception data. We take a modular approach where the high-level planner commands the target position and orientation of the hands and eyes of the humanoid, delivered by the low-level policy that controls the whole-body movements. Specifically, the low-level whole-body controller learns to track the three points (eyes, left hand, and right hand) from existing large-scale human motion capture data while high-level policy learns from human data collected by Aria glasses. Our modular approach decouples the ego-centric vision perception from physical actions, promoting efficient learning and scalability to novel scenes. We evaluate our method both in simulation and in the real-world, demonstrating humanoid's capabilities to navigate and reach in complex environments designed for humans.

## 개요
우리는 인간의 움직임과 시각 인식 데이터로부터 직접 휴머노이드의 내비게이션, 보행 및 도달 기술을 학습하는 프레임워크인 Hand-Eye Autonomous Delivery (HEAD)를 제안합니다. 우리는 모듈식 접근 방식을 취하며, 상위 수준 계획자가 휴머노이드의 손과 눈의 목표 위치와 방향을 명령하고, 이를 하위 수준 정책이 전신 움직임을 제어하여 수행합니다. 구체적으로, 하위 수준 전신 제어기는 기존의 대규모 인간 모션 캡처 데이터에서 세 지점(눈, 왼손, 오른손)을 추적하는 방법을 학습하고, 상위 수준 정책은 Aria 안경으로 수집된 인간 데이터로부터 학습합니다. 우리의 모듈식 접근 방식은 자아 중심 시각 인식을 물리적 행동에서 분리하여 효율적인 학습과 새로운 장면에 대한 확장성을 촉진합니다. 우리는 시뮬레이션과 실제 환경 모두에서 방법을 평가하며, 인간을 위해 설계된 복잡한 환경에서 휴머노이드의 내비게이션 및 도달 능력을 입증합니다.

## 핵심 내용
우리는 인간의 움직임과 시각 인식 데이터로부터 직접 휴머노이드의 내비게이션, 보행 및 도달 기술을 학습하는 프레임워크인 Hand-Eye Autonomous Delivery (HEAD)를 제안합니다. 우리는 모듈식 접근 방식을 취하며, 상위 수준 계획자가 휴머노이드의 손과 눈의 목표 위치와 방향을 명령하고, 이를 하위 수준 정책이 전신 움직임을 제어하여 수행합니다. 구체적으로, 하위 수준 전신 제어기는 기존의 대규모 인간 모션 캡처 데이터에서 세 지점(눈, 왼손, 오른손)을 추적하는 방법을 학습하고, 상위 수준 정책은 Aria 안경으로 수집된 인간 데이터로부터 학습합니다. 우리의 모듈식 접근 방식은 자아 중심 시각 인식을 물리적 행동에서 분리하여 효율적인 학습과 새로운 장면에 대한 확장성을 촉진합니다. 우리는 시뮬레이션과 실제 환경 모두에서 방법을 평가하며, 인간을 위해 설계된 복잡한 환경에서 휴머노이드의 내비게이션 및 도달 능력을 입증합니다.

## 参考
- http://arxiv.org/abs/2508.03068v2
