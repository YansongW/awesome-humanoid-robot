---
$id: ent_paper_preprint_dynamic_modeling_gait_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '[Preprint] Dynamic Modeling, Gait Synthesis, and Control of a Novel Subsurface Bore Propagator'
  zh: '[Preprint] Dynamic Modeling, Gait Synthesis, and Control of a Novel Subsurface Bore Propagator'
  ko: '[Preprint] Dynamic Modeling, Gait Synthesis, and Control of a Novel Subsurface Bore Propagator'
summary:
  en: 'arXiv:2607.00569v1 Announce Type: new Abstract: In this article, we present dynamic modeling, gait synthesis, and feedback
    control design for a modular novel subsurface robot, designed for human-free subsurface exploration and excavation. The
    subsurface propagator design is based on two major aspects: 1) anchor and propel movement like an earthworm and 2) excavation
    similar to tunnel boring machines. This design is decoupled into five separate modules: one drill head to excavate and
    create cavity for propagation, two modules to anchor the robot, and two modules to enable propagation of the body. In
    order to design a controller for each of the modules, dynamic models using the Euler-Lagrange framework are developed.
    These mathematical models are used as a baseline to design controlled decoupled operation of the different joint movements.
    The operation of robotic assembly is constructed via a centralized state machine for gait synthesis with integration of
    the designed feedback controller. The controllers are tested on the real robot geometry to aid sim-to-real integration:
    A physics-based Unity simulation using a CAD model of the robot and integration of the trained controller via ROS verifies
    the performance of the robot. The experimental results demonstrate that the proposed design, controllers and the gait
    synthesis strategy together are capable of anchoring the robot in place and creating an total advancement of 30\,mm into
    the soil after completing 3 gait cycles.'
  zh: 本文提出一种模块化地下推进机器人的动力学建模、步态合成与反馈控制设计。该机器人结合蚯蚓式锚定推进与隧道掘进机式挖掘原理，由钻头、锚定模块和推进模块共五个单元组成。实验表明，经过三个步态周期后，机器人可在土壤中实现30毫米的总推进距离。
  ko: 'arXiv:2607.00569v1 Announce Type: new Abstract: In this article, we present dynamic modeling, gait synthesis, and feedback
    control design for a modular novel subsurface robot, designed for human-free subsurface exploration and excavation. The
    subsurface propagator design is based on two major aspects: 1) anchor and propel movement like an earthworm and 2) excavation
    similar to tunnel boring machines. This design is decoupled into five separate modules: one drill head to excavate and
    create cavity for propagation, two modules to anchor the robot, and two modules to enable propagation of the body. In
    order to design a controller for each of the modules, dynamic models using the Euler-Lagrange framework are developed.
    These mathematical models are used as a baseline to design controlled decoupled operation of the different joint movements.
    The operation of robotic assembly is constructed via a centralized state machine for gait synthesis with integration of
    the designed feedback controller. The controllers are tested on the real robot geometry to aid sim-to-real integration:
    A physics-based Unity simulation using a CAD model of the robot and integration of the trained controller via ROS verifies
    the performance of the robot. The experimental results demonstrate that the proposed design, controllers and the gait
    synthesis strategy together are capable of anchoring the robot in place and creating an total advancement of 30\,mm into
    the soil after completing 3 gait cycles.'
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
- robotics
- preprint_dynamic_modeling_gait
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00569v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: '[Preprint] Dynamic Modeling, Gait Synthesis, and Control of a Novel Subsurface Bore Propagator (arXiv)'
  url: https://arxiv.org/abs/2607.00569
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
该研究针对无人地下探测与挖掘需求，设计了一种新型模块化地下推进机器人。其运动机制融合了蚯蚓的锚定-推进模式和隧道掘进机的挖掘原理，整体结构分为五个独立模块：一个用于挖掘并创造推进空腔的钻头、两个锚定模块和两个推进模块。基于Euler-Lagrange框架为每个模块建立了动力学模型，并以此为基础设计了各关节运动的解耦控制方案。通过集中式状态机实现步态合成，并将反馈控制器集成其中。为促进仿真到实物的迁移，研究者在基于物理的Unity仿真环境中使用机器人CAD模型进行测试，并通过ROS集成控制器验证性能。

## 核心内容
### 机器人设计与建模
- 机器人采用模块化架构，包含五个独立模块：钻头模块负责挖掘并形成推进所需的空腔；两个锚定模块用于固定机器人位置；两个推进模块实现主体向前运动。
- 运动机制借鉴两种生物/工程原理：蚯蚓的锚定-推进运动模式，以及隧道掘进机的挖掘方式。
- 动力学建模基于Euler-Lagrange框架，为每个模块建立数学模型，作为设计关节运动解耦控制的基础。

### 控制与步态合成
- 控制架构采用集中式状态机进行步态合成，并集成反馈控制器，实现各模块的协调运作。
- 控制器设计以动力学模型为基准，确保不同关节运动的解耦操作。

### 仿真与实验验证
- 为促进sim-to-real迁移，在基于物理的Unity仿真环境中使用机器人CAD模型进行测试，并通过ROS集成训练好的控制器。
- 实验结果表明：所提出的设计、控制器和步态合成策略能够有效实现机器人的锚定功能，并在完成三个步态周期后，在土壤中实现30毫米的总推进距离。

## Overview
In this article, we present dynamic modeling, gait synthesis, and feedback control design for a modular novel subsurface robot, designed for human-free subsurface exploration and excavation. The subsurface propagator design is based on two major aspects: 1) anchor and propel movement like an earthworm and 2) excavation similar to tunnel boring machines. This design is decoupled into five separate modules: one drill head to excavate and create cavity for propagation, two modules to anchor the robot, and two modules to enable propagation of the body. In order to design a controller for each of the modules, dynamic models using the Euler-Lagrange framework are developed. These mathematical models are used as a baseline to design controlled decoupled operation of the different joint movements. The operation of robotic assembly is constructed via a centralized state machine for gait synthesis with integration of the designed feedback controller. The controllers are tested on the real robot geometry to aid sim-to-real integration: A physics-based Unity simulation using a CAD model of the robot and integration of the trained controller via ROS verifies the performance of the robot. The experimental results demonstrate that the proposed design, controllers and the gait synthesis strategy together are capable of anchoring the robot in place and creating an total advancement of 30\,mm into the soil after completing 3 gait cycles.

## 개요
본 논문에서는 인간이 없는 지하 탐사 및 굴착을 위해 설계된 모듈형 신형 지하 로봇의 동적 모델링, 보행 합성 및 피드백 제어 설계를 제시합니다. 지하 전파기 설계는 두 가지 주요 측면에 기반합니다: 1) 지렁이와 같은 앵커 및 추진 운동, 2) 터널 굴착기와 유사한 굴착입니다. 이 설계는 다섯 개의 개별 모듈로 분리됩니다: 전파를 위한 공동을 굴착하고 생성하는 하나의 드릴 헤드, 로봇을 고정하는 두 개의 모듈, 그리고 몸체의 전파를 가능하게 하는 두 개의 모듈입니다. 각 모듈의 제어기를 설계하기 위해 오일러-라그랑주 프레임워크를 사용한 동적 모델이 개발됩니다. 이러한 수학적 모델은 다양한 관절 움직임의 제어된 분리 동작을 설계하기 위한 기준으로 사용됩니다. 로봇 어셈블리의 작동은 설계된 피드백 제어기를 통합한 중앙 집중식 상태 머신을 통해 보행 합성으로 구성됩니다. 제어기는 실제 로봇 형상에서 테스트되어 시뮬레이션-실제 통합을 지원합니다: 로봇의 CAD 모델을 사용한 물리 기반 Unity 시뮬레이션과 ROS를 통한 훈련된 제어기 통합이 로봇의 성능을 검증합니다. 실험 결과는 제안된 설계, 제어기 및 보행 합성 전략이 함께 로봇을 제자리에 고정하고 3회의 보행 사이클 완료 후 토양 속으로 총 30mm의 전진을 생성할 수 있음을 보여줍니다.

## 핵심 내용
본 논문에서는 인간이 없는 지하 탐사 및 굴착을 위해 설계된 모듈형 신형 지하 로봇의 동적 모델링, 보행 합성 및 피드백 제어 설계를 제시합니다. 지하 전파기 설계는 두 가지 주요 측면에 기반합니다: 1) 지렁이와 같은 앵커 및 추진 운동, 2) 터널 굴착기와 유사한 굴착입니다. 이 설계는 다섯 개의 개별 모듈로 분리됩니다: 전파를 위한 공동을 굴착하고 생성하는 하나의 드릴 헤드, 로봇을 고정하는 두 개의 모듈, 그리고 몸체의 전파를 가능하게 하는 두 개의 모듈입니다. 각 모듈의 제어기를 설계하기 위해 오일러-라그랑주 프레임워크를 사용한 동적 모델이 개발됩니다. 이러한 수학적 모델은 다양한 관절 움직임의 제어된 분리 동작을 설계하기 위한 기준으로 사용됩니다. 로봇 어셈블리의 작동은 설계된 피드백 제어기를 통합한 중앙 집중식 상태 머신을 통해 보행 합성으로 구성됩니다. 제어기는 실제 로봇 형상에서 테스트되어 시뮬레이션-실제 통합을 지원합니다: 로봇의 CAD 모델을 사용한 물리 기반 Unity 시뮬레이션과 ROS를 통한 훈련된 제어기 통합이 로봇의 성능을 검증합니다. 실험 결과는 제안된 설계, 제어기 및 보행 합성 전략이 함께 로봇을 제자리에 고정하고 3회의 보행 사이클 완료 후 토양 속으로 총 30mm의 전진을 생성할 수 있음을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.00569v1
