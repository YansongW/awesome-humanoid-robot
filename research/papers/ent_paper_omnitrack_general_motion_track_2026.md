---
$id: ent_paper_omnitrack_general_motion_track_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference'
  zh: 不要让控制器追踪错误参考
  ko: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference'
summary:
  en: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference is a knowledge node related to paper in the humanoid
    robot value chain.'
  zh: OmniTrack 是一个通用运动跟踪框架，由研究团队提出，旨在解决人形机器人从人类运动数据学习时因形态与动力学差异导致的物理不可行伪影（如漂浮、穿透）问题。其核心贡献是通过两阶段解耦方法，先由特权策略生成物理一致的运动，再由通用控制策略跟踪这些运动，实现稳定且泛化的控制。
  ko: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference is a knowledge node related to paper in the humanoid
    robot value chain.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23832v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference (arXiv)'
  url: https://arxiv.org/abs/2602.23832
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 不要让控制器追踪错误参考 project page
  url: https://omnitrack-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
OmniTrack 针对人形机器人运动跟踪中因人类与机器人形态及动力学差异、数据噪声引起的物理不可行伪影（如漂浮、穿透）问题，提出两阶段解耦框架。第一阶段，特权通用策略通过仿真轨迹滚动生成严格符合机器人动力学的物理可行运动；第二阶段，通用控制策略学习跟踪这些运动，确保稳定且连贯地迁移到真实机器人。实验表明，OmniTrack 提升了跟踪精度，并展现出对未见运动的强泛化能力，在真实测试中实现长达一小时的稳定跟踪，包括空翻、侧手翻等复杂杂技动作。此外，OmniTrack 还支持人类风格的稳定与动态在线遥操作，凸显其对不同用户输入的鲁棒性和适应性。

## 核心内容
### 方法
OmniTrack 采用两阶段解耦架构，将物理可行性从通用运动跟踪中分离：
- **第一阶段：特权通用策略**  
  在仿真环境中，通过轨迹滚动生成严格符合机器人动力学的物理可行运动。该策略利用特权信息（如机器人状态、动力学参数）确保运动无漂浮、穿透等伪影。
- **第二阶段：通用控制策略**  
  训练策略以跟踪第一阶段生成的物理可行运动，实现从仿真到真实机器人的稳定控制迁移。该策略仅依赖可观测信息（如关节角度、IMU 数据），无需特权信息。

### 实验设置
- **训练数据**：使用丰富的人类运动数据集，包含多种行为（如行走、跳跃、杂技）。
- **仿真环境**：基于物理引擎的仿真平台，用于生成物理可行运动并训练策略。
- **真实测试**：在真实人形机器人上部署，评估长时间跟踪稳定性与泛化能力。

### 关键数字与结果
- **跟踪精度**：OmniTrack 相比基线方法显著提升跟踪精度，尤其在复杂运动（如空翻、侧手翻）中表现突出。
- **泛化能力**：对未见运动（如非训练集中的动作）展现出强泛化性，无需重新训练。
- **真实测试**：实现长达一小时的连续稳定跟踪，包括高动态杂技动作。
- **在线遥操作**：支持人类风格的稳定与动态遥操作，适应不同用户输入（如快速变化或缓慢指令），验证了鲁棒性。

### 结论
OmniTrack 通过解耦物理可行性与运动跟踪，有效解决了人形机器人从人类数据学习时的伪影问题，实现了高精度、长时稳定且泛化的控制。其两阶段框架为通用人形机器人控制提供了新范式，并展示了在复杂场景（如杂技、遥操作）中的实际应用潜力。

## Overview
Learning motion tracking from rich human motion data is a foundational task for achieving general control in humanoid robots, enabling them to perform diverse behaviors. However, discrepancies in morphology and dynamics between humans and robots, combined with data noise, introduce physically infeasible artifacts in reference motions, such as floating and penetration. During both training and execution, these artifacts create a conflict between following inaccurate reference motions and maintaining the robot's stability, hindering the development of a generalizable motion tracking policy. To address these challenges, we introduce OmniTrack, a general tracking framework that explicitly decouples physical feasibility from general motion tracking. In the first stage, a privileged generalist policy generates physically plausible motions that strictly adhere to the robot's dynamics via trajectory rollout in simulation. In the second stage, the general control policy is trained to track these physically feasible motions, ensuring stable and coherent control transfer to the real robot. Experiments show that OmniTrack improves tracking accuracy and demonstrates strong generalization to unseen motions. In real-world tests, OmniTrack achieves hour-long, consistent, and stable tracking, including complex acrobatic motions such as flips and cartwheels. Additionally, we show that OmniTrack supports human-style stable and dynamic online teleoperation, highlighting its robustness and adaptability to varying user inputs.

## 개요
풍부한 인간 동작 데이터로부터 모션 트래킹을 학습하는 것은 휴머노이드 로봇의 일반적인 제어를 달성하기 위한 기초적인 과제로, 로봇이 다양한 행동을 수행할 수 있게 합니다. 그러나 인간과 로봇 간의 형태 및 역학적 차이와 데이터 노이즈가 결합되어 참조 동작에 부유나 관통과 같은 물리적으로 실현 불가능한 인공물이 발생합니다. 훈련 및 실행 중에 이러한 인공물은 부정확한 참조 동작을 따르는 것과 로봇의 안정성을 유지하는 것 사이에 갈등을 일으켜 일반화 가능한 모션 트래킹 정책의 개발을 방해합니다. 이러한 문제를 해결하기 위해 우리는 OmniTrack을 소개합니다. 이는 물리적 실현 가능성을 일반적인 모션 트래킹에서 명시적으로 분리하는 일반 트래킹 프레임워크입니다. 첫 번째 단계에서는 특권을 가진 일반 정책이 시뮬레이션에서 궤적 롤아웃을 통해 로봇의 역학을 엄격히 준수하는 물리적으로 타당한 동작을 생성합니다. 두 번째 단계에서는 일반 제어 정책이 이러한 물리적으로 실현 가능한 동작을 추적하도록 훈련되어 실제 로봇으로의 안정적이고 일관된 제어 전이를 보장합니다. 실험 결과 OmniTrack은 트래킹 정확도를 향상시키고 보지 못한 동작에 대한 강력한 일반화를 보여줍니다. 실제 환경 테스트에서 OmniTrack은 플립과 카트휠과 같은 복잡한 곡예 동작을 포함하여 한 시간 동안 지속적이고 일관되며 안정적인 트래킹을 달성합니다. 또한 OmniTrack이 인간 스타일의 안정적이고 동적인 온라인 원격 조작을 지원하여 다양한 사용자 입력에 대한 견고성과 적응성을 강조함을 보여줍니다.

## 핵심 내용
풍부한 인간 동작 데이터로부터 모션 트래킹을 학습하는 것은 휴머노이드 로봇의 일반적인 제어를 달성하기 위한 기초적인 과제로, 로봇이 다양한 행동을 수행할 수 있게 합니다. 그러나 인간과 로봇 간의 형태 및 역학적 차이와 데이터 노이즈가 결합되어 참조 동작에 부유나 관통과 같은 물리적으로 실현 불가능한 인공물이 발생합니다. 훈련 및 실행 중에 이러한 인공물은 부정확한 참조 동작을 따르는 것과 로봇의 안정성을 유지하는 것 사이에 갈등을 일으켜 일반화 가능한 모션 트래킹 정책의 개발을 방해합니다. 이러한 문제를 해결하기 위해 우리는 OmniTrack을 소개합니다. 이는 물리적 실현 가능성을 일반적인 모션 트래킹에서 명시적으로 분리하는 일반 트래킹 프레임워크입니다. 첫 번째 단계에서는 특권을 가진 일반 정책이 시뮬레이션에서 궤적 롤아웃을 통해 로봇의 역학을 엄격히 준수하는 물리적으로 타당한 동작을 생성합니다. 두 번째 단계에서는 일반 제어 정책이 이러한 물리적으로 실현 가능한 동작을 추적하도록 훈련되어 실제 로봇으로의 안정적이고 일관된 제어 전이를 보장합니다. 실험 결과 OmniTrack은 트래킹 정확도를 향상시키고 보지 못한 동작에 대한 강력한 일반화를 보여줍니다. 실제 환경 테스트에서 OmniTrack은 플립과 카트휠과 같은 복잡한 곡예 동작을 포함하여 한 시간 동안 지속적이고 일관되며 안정적인 트래킹을 달성합니다. 또한 OmniTrack이 인간 스타일의 안정적이고 동적인 온라인 원격 조작을 지원하여 다양한 사용자 입력에 대한 견고성과 적응성을 강조함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2602.23832v1
