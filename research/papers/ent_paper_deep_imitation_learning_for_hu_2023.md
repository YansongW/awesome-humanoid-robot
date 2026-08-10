---
$id: ent_paper_deep_imitation_learning_for_hu_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation
  zh: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation
  ko: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation
summary:
  en: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation is a 2023 work on teleoperation for
    humanoid robots, with open-source code available.
  zh: TRILL 是一个用于人形机器人全身移动操作技能训练的数据高效框架，由 UT Austin 团队于 2023 年提出。其核心贡献在于通过直观的 VR 人机接口采集人类演示数据，并利用全身控制公式将操作员的任务空间指令转化为机器人的关节力矩驱动，从而高效学习复杂的传感器运动技能。
  ko: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation is a 2023 work on teleoperation for
    humanoid robots, with open-source code available.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deep_imitation_learning_for_hu
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.01952v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (805 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation (arXiv)
  url: https://arxiv.org/abs/2309.01952
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation project page
  url: https://ut-austin-rpl.github.io/TRILL/
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
针对人形机器人因自由度极高而难以收集任务演示和训练策略的难题，TRILL 框架提供了一种数据高效的解决方案。该框架通过直观的 VR 界面收集人类演示数据，并采用全身控制公式将操作员的任务空间指令转化为机器人的关节力矩驱动，同时稳定其动力学。通过使用专为全身移动操作设计的高层动作抽象，该方法能够高效学习复杂的传感器运动技能。TRILL 的有效性在仿真和真实机器人上均得到了验证，能够执行多种移动操作任务。

## 核心内容
### 方法概述
TRILL 框架的核心在于解决人形机器人移动操作（loco-manipulation）策略学习的三大挑战：高自由度带来的数据收集困难、策略训练效率低下以及复杂传感器运动技能的习得。

### 数据收集与接口
- 采用直观的 **VR 界面** 进行人类演示数据采集，降低操作门槛。
- 操作员通过 VR 设备发出任务空间指令，无需直接操控机器人关节。

### 控制与学习架构
- **全身控制公式**：将操作员的任务空间指令转化为机器人的关节力矩驱动，同时稳定其动力学，确保机器人平衡与安全。
- **高层动作抽象**：针对人形机器人移动操作任务设计，将复杂动作分解为可学习的抽象单元，提升学习效率。
- 通过深度模仿学习（Deep Imitation Learning）从演示数据中直接学习传感器运动技能。

### 实验设置与结果
- **仿真环境**：在模拟环境中验证 TRILL 框架的可行性。
- **真实机器人**：在真实人形机器人上执行多种移动操作任务，包括但不限于搬运、抓取等。
- **关键结论**：TRILL 在数据效率上显著优于传统方法，能够从有限的人类演示中泛化出鲁棒的策略。

### 开源与资源
- 项目代码已开源，相关视频与补充材料可在项目页面获取：https://ut-austin-rpl.github.io/TRILL

## Overview
We tackle the problem of developing humanoid loco-manipulation skills with deep imitation learning. The difficulty of collecting task demonstrations and training policies for humanoids with a high degree of freedom presents substantial challenges. We introduce TRILL, a data-efficient framework for training humanoid loco-manipulation policies from human demonstrations. In this framework, we collect human demonstration data through an intuitive Virtual Reality (VR) interface. We employ the whole-body control formulation to transform task-space commands by human operators into the robot's joint-torque actuation while stabilizing its dynamics. By employing high-level action abstractions tailored for humanoid loco-manipulation, our method can efficiently learn complex sensorimotor skills. We demonstrate the effectiveness of TRILL in simulation and on a real-world robot for performing various loco-manipulation tasks. Videos and additional materials can be found on the project page: https://ut-austin-rpl.github.io/TRILL.

## 参考
- http://arxiv.org/abs/2309.01952v2

## 개요
인간형 로봇은 자유도가 매우 높아 작업 시연 수집과 정책 훈련이 어려운 문제를 해결하기 위해, TRILL 프레임워크는 데이터 효율적인 솔루션을 제공합니다. 이 프레임워크는 직관적인 VR 인터페이스를 통해 인간 시연 데이터를 수집하고, 전신 제어 공식을 사용하여 작업자의 작업 공간 명령을 로봇의 관절 토크 구동으로 변환하면서 동시에 그 동역학을 안정화합니다. 전신 이동 조작을 위해 설계된 고수준 동작 추상화를 사용함으로써, 이 방법은 복잡한 센서 운동 기술을 효율적으로 학습할 수 있습니다. TRILL의 효과는 시뮬레이션과 실제 로봇 모두에서 검증되었으며, 다양한 이동 조작 작업을 수행할 수 있습니다.

## 핵심 내용
### 방법 개요
TRILL 프레임워크의 핵심은 인간형 로봇의 이동 조작(loco-manipulation) 정책 학습에서 발생하는 세 가지 주요 과제를 해결하는 데 있습니다: 높은 자유도로 인한 데이터 수집 어려움, 정책 훈련 효율성 저하, 그리고 복잡한 센서 운동 기술 습득입니다.

### 데이터 수집 및 인터페이스
- 직관적인 **VR 인터페이스**를 사용하여 인간 시연 데이터를 수집하며, 작업 진입 장벽을 낮춥니다.
- 작업자는 VR 장치를 통해 작업 공간 명령을 내리며, 로봇 관절을 직접 조작할 필요가 없습니다.

### 제어 및 학습 아키텍처
- **전신 제어 공식**: 작업자의 작업 공간 명령을 로봇의 관절 토크 구동으로 변환하면서 동시에 그 동역학을 안정화하여 로봇의 균형과 안전을 보장합니다.
- **고수준 동작 추상화**: 인간형 로봇의 이동 조작 작업을 위해 설계되었으며, 복잡한 동작을 학습 가능한 추상 단위로 분해하여 학습 효율을 향상시킵니다.
- 심층 모방 학습(Deep Imitation Learning)을 통해 시연 데이터에서 센서 운동 기술을 직접 학습합니다.

### 실험 설정 및 결과
- **시뮬레이션 환경**: 시뮬레이션 환경에서 TRILL 프레임워크의 타당성을 검증합니다.
- **실제 로봇**: 실제 인간형 로봇에서 운반, 파지 등을 포함한 다양한 이동 조작 작업을 수행합니다.
- **핵심 결론**: TRILL은 데이터 효율성에서 기존 방법보다 현저히 우수하며, 제한된 인간 시연에서 강건한 정책을 일반화할 수 있습니다.

### 오픈소스 및 리소스
- 프로젝트 코드는 오픈소스로 공개되었으며, 관련 비디오 및 추가 자료는 프로젝트 페이지에서 확인할 수 있습니다: https://ut-austin-rpl.github.io/TRILL
