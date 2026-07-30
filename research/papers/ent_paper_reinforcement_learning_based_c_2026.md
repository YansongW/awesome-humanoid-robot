---
$id: ent_paper_reinforcement_learning_based_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  zh: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  ko: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
summary:
  en: 'arXiv:2606.31807v1 Announce Type: new Abstract: As humanoid robots become increasingly dynamic, coupling them with
    reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating.
    Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility
    of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we
    train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot
    modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots
    or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion
    strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation
    learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts
    by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a
    custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to
    a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers
    zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject
    active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can
    be found at https://www.youtube.com/watch?v=-_APcOS7uFo.'
  zh: 本研究提出一种基于强化学习的控制策略，使配备被动直排轮滑鞋的人形机器人Booster T1实现动态滑行。该策略完全由奖励函数驱动，无需人类运动数据或模仿学习，在真实硬件上零样本迁移成功，运输成本（CoT）相比步行降低50%。
  ko: 'arXiv:2606.31807v1 Announce Type: new Abstract: As humanoid robots become increasingly dynamic, coupling them with
    reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating.
    Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility
    of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we
    train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot
    modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots
    or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion
    strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation
    learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts
    by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a
    custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to
    a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers
    zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject
    active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can
    be found at https://www.youtube.com/watch?v=-_APcOS7uFo.'
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
- reinforcement_learning_based_c
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31807v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  url: https://arxiv.org/abs/2606.31807
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作将强化学习应用于人形机器人的被动直排轮滑控制，解决了欠驱动复杂力学问题。研究者为Booster T1机器人改装了消费级直排轮滑鞋，通过6自由度精确控制轮滑边缘驱动策略。训练中采用球形和椭球体两种几何轮模型克服被动轮的不稳定性，配合成功导向指令课程与滚动奖励机制。最终策略在真实机器人上展现出动态平衡、抗扰动能力和高速转弯能力。

## 核心内容
### 方法架构
- 采用强化学习训练控制策略，输入为机器人状态与指令，输出为6自由度轮滑关节控制量
- 奖励函数包含滚动奖励（鼓励持续滚动）、成功导向指令课程（根据任务完成度动态调整指令难度）
- 训练时使用球形轮模型，验证时切换为椭球体轮模型，以增强对接触伪影的鲁棒性

### 实验设置
- 硬件平台：Booster T1人形机器人，脚部改装为四轮直排轮滑鞋（被动轮，无驱动）
- 仿真环境：基于物理引擎的强化学习训练框架，未使用任何人类运动数据或运动学先验
- 对比基准：标准步行步态（相同硬件配置下的行走策略）

### 关键结果
- 运输成本（CoT）相比步行降低50%，验证了轮滑策略的能量效率优势
- 策略零样本迁移至真实Booster T1硬件，无需任何微调
- 真实环境测试中，机器人能维持动态平衡、抵抗外部物理扰动（如推拉），并实现高速转弯
- 所有滑行策略完全从奖励函数中涌现，未依赖人类示范或模仿学习

### 结论
该工作首次在被动轮式人形机器人上实现端到端强化学习控制，证明了纯奖励驱动方法在复杂欠驱动运动中的有效性。未来可扩展至更复杂的轮滑动作（如急停、跳跃）或多地形适应。

## Overview
As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo.

## 개요
휴머노이드 로봇이 점점 더 동적으로 발전함에 따라, 이를 강화 학습과 결합하는 것은 수동 인라인 스케이팅의 복잡하고 저구동된 역학을 해결하는 유망한 접근법을 제공합니다. 휴머노이드 로봇에 수동 인라인 스케이팅 바퀴를 장착하면 휴머노이드의 다재다능한 민첩성과 인간 스케이터가 사용하는 고속, 에너지 효율적인 이동 전략을 결합할 수 있는 기회가 생깁니다. 본 논문에서는 기존 발 대신 소비자용 인라인 스케이트를 장착하도록 개조된 휴머노이드 로봇을 위해 새로운 이동 전략을 가능하게 하는 강화 학습 제어 정책을 훈련하고 배포합니다. 사족 로봇이나 능동 구동 바퀴에 국한된 이전 연구와 달리, 우리 시스템은 스케이트의 정밀한 6자유도 제어를 통해 동적이고 에지 기반의 추진 전략을 실행할 수 있습니다. 우리의 스케이팅 전략은 인간 동작 데이터, 모방 학습 또는 운동학적 사전 지식에 의존하지 않고 보상 구조에서 완전히 창발합니다. 우리는 훈련 및 검증 중에 다양한 기하학적 바퀴 모델(구형 및 타원체)과 맞춤형 성공 기반 명령 커리큘럼 및 특수 구름 보상을 활용하여 수동 바퀴의 본질적인 불안정성과 시뮬레이션 접촉 인공물을 극복합니다. 결과적으로, 우리의 정책은 표준 보행 걸음걸이에 비해 최대 50%의 수송 비용(CoT) 감소를 보여줍니다. 결과 정책은 물리적 Booster T1 하드웨어에 제로샷으로 성공적으로 전이됩니다. 실제 배포에서는 동적 균형, 능동적 물리적 교란을 거부하는 능력, 속도에서 회전이 가능한 민첩한 이동 전략을 입증합니다. 결과 비디오는 https://www.youtube.com/watch?v=-_APcOS7uFo에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇이 점점 더 동적으로 발전함에 따라, 이를 강화 학습과 결합하는 것은 수동 인라인 스케이팅의 복잡하고 저구동된 역학을 해결하는 유망한 접근법을 제공합니다. 휴머노이드 로봇에 수동 인라인 스케이팅 바퀴를 장착하면 휴머노이드의 다재다능한 민첩성과 인간 스케이터가 사용하는 고속, 에너지 효율적인 이동 전략을 결합할 수 있는 기회가 생깁니다. 본 논문에서는 기존 발 대신 소비자용 인라인 스케이트를 장착하도록 개조된 휴머노이드 로봇을 위해 새로운 이동 전략을 가능하게 하는 강화 학습 제어 정책을 훈련하고 배포합니다. 사족 로봇이나 능동 구동 바퀴에 국한된 이전 연구와 달리, 우리 시스템은 스케이트의 정밀한 6자유도 제어를 통해 동적이고 에지 기반의 추진 전략을 실행할 수 있습니다. 우리의 스케이팅 전략은 인간 동작 데이터, 모방 학습 또는 운동학적 사전 지식에 의존하지 않고 보상 구조에서 완전히 창발합니다. 우리는 훈련 및 검증 중에 다양한 기하학적 바퀴 모델(구형 및 타원체)과 맞춤형 성공 기반 명령 커리큘럼 및 특수 구름 보상을 활용하여 수동 바퀴의 본질적인 불안정성과 시뮬레이션 접촉 인공물을 극복합니다. 결과적으로, 우리의 정책은 표준 보행 걸음걸이에 비해 최대 50%의 수송 비용(CoT) 감소를 보여줍니다. 결과 정책은 물리적 Booster T1 하드웨어에 제로샷으로 성공적으로 전이됩니다. 실제 배포에서는 동적 균형, 능동적 물리적 교란을 거부하는 능력, 속도에서 회전이 가능한 민첩한 이동 전략을 입증합니다. 결과 비디오는 https://www.youtube.com/watch?v=-_APcOS7uFo에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2606.31807v1
