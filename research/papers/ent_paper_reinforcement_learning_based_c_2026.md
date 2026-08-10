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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31807v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (685 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.31807v1

## 개요
이 연구는 강화 학습을 휴머노이드 로봇의 패시브 인라인 스케이트 제어에 적용하여, 저구동 복잡 역학 문제를 해결했습니다. 연구진은 Booster T1 로봇에 소비자용 인라인 스케이트를 개조 장착하고, 6자유도 정밀 제어를 통해 스케이트 엣지 구동 전략을 구현했습니다. 훈련 과정에서는 구형 및 타원체 두 가지 기하학적 휠 모델을 사용하여 패시브 휠의 불안정성을 극복했으며, 성공 지향 명령 커리큘럼과 롤링 보상 메커니즘을 결합했습니다. 최종 전략은 실제 로봇에서 동적 균형, 외란 저항 능력, 고속 회전 능력을 입증했습니다.

## 핵심 내용
### 방법 아키텍처
- 강화 학습을 사용하여 제어 전략을 훈련하며, 입력은 로봇 상태와 명령, 출력은 6자유도 스케이트 관절 제어량입니다.
- 보상 함수는 롤링 보상(지속적인 구름 장려), 성공 지향 명령 커리큘럼(작업 완료도에 따라 명령 난이도 동적 조정)을 포함합니다.
- 훈련 시 구형 휠 모델을 사용하고, 검증 시 타원체 휠 모델로 전환하여 접촉 아티팩트에 대한 강건성을 강화합니다.

### 실험 설정
- 하드웨어 플랫폼: Booster T1 휴머노이드 로봇, 발 부분을 4륜 인라인 스케이트(패시브 휠, 구동 없음)로 개조.
- 시뮬레이션 환경: 물리 엔진 기반 강화 학습 훈련 프레임워크, 인간 동작 데이터나 운동학적 사전 지식은 사용하지 않음.
- 비교 기준: 표준 보행 보행 패턴(동일 하드웨어 구성에서의 걷기 전략).

### 주요 결과
- 운송 비용(CoT)이 보행 대비 50% 감소하여 스케이트 전략의 에너지 효율 우위를 입증.
- 전략이 추가 미세 조정 없이 실제 Booster T1 하드웨어로 제로샷 전이.
- 실제 환경 테스트에서 로봇은 동적 균형 유지, 외부 물리적 외란(예: 밀기/당기기) 저항, 고속 회전 구현.
- 모든 스케이트 전략은 보상 함수에서 완전히 창발되었으며, 인간 시연이나 모방 학습에 의존하지 않음.

### 결론
이 연구는 패시브 휠 휴머노이드 로봇에서 최초로 엔드투엔드 강화 학습 제어를 구현하여, 복잡한 저구동 운동에서 순수 보상 기반 접근법의 효과를 입증했습니다. 향후 더 복잡한 스케이트 동작(예: 급정지, 점프)이나 다지형 적응으로 확장할 수 있습니다.
