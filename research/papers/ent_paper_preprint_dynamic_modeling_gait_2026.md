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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00569v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (691 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.00569v1

## 개요
이 연구는 무인 지하 탐사 및 굴착 요구를 위해 새로운 모듈식 지하 추진 로봇을 설계하였다. 그 운동 메커니즘은 지렁이의 앵커-추진 패턴과 터널 굴착기의 굴착 원리를 융합하였으며, 전체 구조는 다섯 개의 독립 모듈로 나뉜다: 추진 공동을 만들기 위해 굴착하는 드릴 비트 하나, 두 개의 앵커 모듈, 그리고 두 개의 추진 모듈이다. Euler-Lagrange 프레임워크를 기반으로 각 모듈에 대한 동역학 모델을 구축하였고, 이를 바탕으로 각 관절 운동의 비연성 제어 방식을 설계하였다. 집중식 상태 머신을 통해 보행 합성을 구현하고, 피드백 컨트롤러를 통합하였다. 시뮬레이션에서 실물로의 전이를 촉진하기 위해, 연구자들은 물리 기반 Unity 시뮬레이션 환경에서 로봇 CAD 모델을 사용하여 테스트하고, ROS 통합 컨트롤러로 성능을 검증하였다.

## 핵심 내용
### 로봇 설계 및 모델링
- 로봇은 모듈식 아키텍처를 채택하며, 다섯 개의 독립 모듈을 포함한다: 드릴 비트 모듈은 굴착 및 추진에 필요한 공동 형성을 담당하고, 두 개의 앵커 모듈은 로봇 위치를 고정하며, 두 개의 추진 모듈은 본체의 전진 운동을 구현한다.
- 운동 메커니즘은 두 가지 생물/공학 원리를 차용한다: 지렁이의 앵커-추진 운동 패턴과 터널 굴착기의 굴착 방식이다.
- 동역학 모델링은 Euler-Lagrange 프레임워크를 기반으로 각 모듈에 대한 수학적 모델을 구축하며, 이는 관절 운동의 비연성 제어 설계의 기초가 된다.

### 제어 및 보행 합성
- 제어 아키텍처는 집중식 상태 머신을 사용하여 보행 합성을 수행하고, 피드백 컨트롤러를 통합하여 각 모듈의 협조 작동을 구현한다.
- 컨트롤러 설계는 동역학 모델을 기준으로 하여 서로 다른 관절 운동의 비연성 작동을 보장한다.

### 시뮬레이션 및 실험 검증
- sim-to-real 전이를 촉진하기 위해, 물리 기반 Unity 시뮬레이션 환경에서 로봇 CAD 모델을 사용하여 테스트하고, ROS를 통해 훈련된 컨트롤러를 통합한다.
- 실험 결과: 제안된 설계, 컨트롤러 및 보행 합성 전략이 로봇의 앵커 기능을 효과적으로 구현할 수 있으며, 세 개의 보행 주기를 완료한 후 토양에서 총 30mm의 추진 거리를 달성한다.
