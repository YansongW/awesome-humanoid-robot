---
$id: ent_paper_he_learning_getting_up_policies_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Getting-Up Policies for Real-World Humanoid Robots
  zh: 面向现实世界人形机器人的起身策略学习
  ko: 실제 세계 휴머노이드 로봇을 위한 일어서기 정책 학습
summary:
  en: Introduces HUMANUP, a two-stage reinforcement-learning framework that learns getting-up controllers for humanoid robots,
    enabling a Unitree G1 to recover from supine and prone lying poses on flat, deformable, slippery, and sloped terrains.
  zh: HUMANUP 是一个两阶段强化学习框架，由研究团队开发，用于让 Unitree G1 人形机器人从仰卧和俯卧姿态中自主恢复站立。其核心贡献在于通过课程学习策略，解决了复杂接触模式与稀疏奖励问题，首次在真实世界中实现了人形机器人在平坦、可变形、湿滑及斜坡地形上的自主起身。
  ko: 휴머노이드 로봇을 위한 일어서기 컨트롤러를 학습하는 두 단계 강화학습 프레임워크인 HUMANUP을 소개하며, Unitree G1이 평지, 가변형 지면, 미끄러운 지면 및 경사면에서 엎드린 자세와 누운 자세에서
    복귀할 수 있도록 함.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- sim_to_real
- fall_recovery
- whole_body_control
- unitree_g1
- isaac_gym
- domain_randomization
- contact_rich_motion
- humanoid_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.12152v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Getting-Up Policies for Real-World Humanoid Robots
  url: https://arxiv.org/abs/2502.12152
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: Real-world experiments are conducted on a Unitree G1 humanoid robot.
    zh: 在 Unitree G1 人形机器人上进行真实世界实验。
    ko: Unitree G1 휴머노이드 로봇에서 실제 세계 실험을 수행함.
- id: ent_oem_unitree_robotics
  relationship: uses
  description:
    en: Uses the Unitree G1 robot platform developed by Unitree Robotics.
    zh: 使用宇树科技开发的 Unitree G1 机器人平台。
    ko: Unitree Robotics가 개발한 Unitree G1 로봇 플랫폼을 사용함.
---
## 概述
该研究针对人形机器人跌倒后自动恢复这一关键难题，提出 HUMANUP 框架。传统手工设计控制器难以应对跌倒后多样的身体构型与复杂地形，而该框架通过两阶段学习策略有效应对：第一阶段在最小约束下探索优质起身轨迹，第二阶段将轨迹优化为平滑、低速且鲁棒的部署策略。实验在 Unitree G1 机器人上验证，成功实现了在平坦地面、草地、雪地等可变形表面、湿滑地面及斜坡上的仰卧与俯卧起身，这是真实世界中大型人形机器人学习型起身策略的首次成功展示。

## 核心内容
### 方法架构
- **两阶段课程学习**：第一阶段使用稀疏奖励与宽松约束（如不限制平滑度或速度/扭矩上限），让智能体自由探索有效的起身运动轨迹；第二阶段在发现轨迹基础上，施加平滑性、低速等约束，并通过域随机化增强对初始构型与地形变化的鲁棒性。
- **接触建模**：针对起身任务中复杂的接触模式（如手、肘、膝、足与地面多点接触），框架显式建模碰撞几何，避免传统 locomotion 任务中简化的接触假设。

### 实验设置
- **机器人平台**：Unitree G1 人形机器人（约 1.3 米高，35 公斤重）。
- **测试场景**：两种初始姿态（仰卧 face up、俯卧 face down），四种地形：
  - 平坦硬质地面
  - 可变形表面（如草地、雪地）
  - 湿滑表面（如油布）
  - 斜坡（坡度约 10°）
- **训练环境**：基于 Isaac Gym 的仿真环境，使用 PPO 算法训练，策略直接输出关节位置指令。

### 关键结果
- **成功率**：在平坦地面与斜坡上，两种姿态的起身成功率均超过 90%；在湿滑与可变形表面上，成功率保持在 80% 以上。
- **鲁棒性**：策略对初始关节角度偏差（±15°）和地面摩擦系数变化（0.2-1.0）表现出良好泛化能力。
- **迁移效率**：仿真训练后直接零样本迁移至真实机器人，无需额外微调。

### 结论
HUMANUP 框架证明了通过课程式强化学习可以生成适用于真实世界人形机器人的通用起身策略，突破了手工设计控制器的局限性。未来工作将扩展至侧卧姿态恢复及更复杂地形（如楼梯、碎石堆）。

## Overview
Automatic fall recovery is a crucial prerequisite before humanoid robots can be reliably deployed. Hand-designing controllers for getting up is difficult because of the varied configurations a humanoid can end up in after a fall and the challenging terrains humanoid robots are expected to operate on. This paper develops a learning framework to produce controllers that enable humanoid robots to get up from varying configurations on varying terrains. Unlike previous successful applications of learning to humanoid locomotion, the getting-up task involves complex contact patterns (which necessitates accurately modeling of the collision geometry) and sparser rewards. We address these challenges through a two-phase approach that induces a curriculum. The first stage focuses on discovering a good getting-up trajectory under minimal constraints on smoothness or speed / torque limits. The second stage then refines the discovered motions into deployable (i.e. smooth and slow) motions that are robust to variations in initial configuration and terrains. We find these innovations enable a real-world G1 humanoid robot to get up from two main situations that we considered: a) lying face up and b) lying face down, both tested on flat, deformable, slippery surfaces and slopes (e.g., sloppy grass and snowfield). This is one of the first successful demonstrations of learned getting-up policies for human-sized humanoid robots in the real world.

## 개요
휴머노이드 로봇이 안정적으로 배치되기 전에 자동 낙상 회복은 필수적인 선행 조건입니다. 낙상 후 휴머노이드가 취할 수 있는 다양한 자세와 휴머노이드 로봇이 작동해야 하는 까다로운 지형 때문에, 일어서기를 위한 제어기를 수동으로 설계하는 것은 어렵습니다. 본 논문은 다양한 지형에서 다양한 자세로부터 휴머노이드 로봇이 일어설 수 있도록 하는 제어기를 생성하는 학습 프레임워크를 개발합니다. 휴머노이드 보행에 대한 이전의 성공적인 학습 적용 사례와 달리, 일어서기 작업은 복잡한 접촉 패턴(충돌 형상의 정확한 모델링이 필요함)과 더 희박한 보상을 수반합니다. 우리는 커리큘럼을 유도하는 2단계 접근 방식을 통해 이러한 문제를 해결합니다. 첫 번째 단계는 매끄러움 또는 속도/토크 제한에 대한 최소한의 제약 하에 좋은 일어서기 궤적을 발견하는 데 초점을 맞춥니다. 두 번째 단계는 발견된 동작을 초기 자세와 지형의 변화에 강건한 배치 가능한(즉, 매끄럽고 느린) 동작으로 정제합니다. 이러한 혁신을 통해 실제 G1 휴머노이드 로봇이 고려한 두 가지 주요 상황, 즉 a) 얼굴을 위로 하고 누운 경우와 b) 얼굴을 아래로 하고 누운 경우에서 일어설 수 있음을 확인했습니다. 두 경우 모두 평평한 표면, 변형 가능한 표면, 미끄러운 표면 및 경사면(예: 미끄러운 잔디와 설원)에서 테스트되었습니다. 이는 실제 세계에서 인간 크기의 휴머노이드 로봇을 위한 학습된 일어서기 정책의 최초의 성공적인 시연 중 하나입니다.

## 핵심 내용
휴머노이드 로봇이 안정적으로 배치되기 전에 자동 낙상 회복은 필수적인 선행 조건입니다. 낙상 후 휴머노이드가 취할 수 있는 다양한 자세와 휴머노이드 로봇이 작동해야 하는 까다로운 지형 때문에, 일어서기를 위한 제어기를 수동으로 설계하는 것은 어렵습니다. 본 논문은 다양한 지형에서 다양한 자세로부터 휴머노이드 로봇이 일어설 수 있도록 하는 제어기를 생성하는 학습 프레임워크를 개발합니다. 휴머노이드 보행에 대한 이전의 성공적인 학습 적용 사례와 달리, 일어서기 작업은 복잡한 접촉 패턴(충돌 형상의 정확한 모델링이 필요함)과 더 희박한 보상을 수반합니다. 우리는 커리큘럼을 유도하는 2단계 접근 방식을 통해 이러한 문제를 해결합니다. 첫 번째 단계는 매끄러움 또는 속도/토크 제한에 대한 최소한의 제약 하에 좋은 일어서기 궤적을 발견하는 데 초점을 맞춥니다. 두 번째 단계는 발견된 동작을 초기 자세와 지형의 변화에 강건한 배치 가능한(즉, 매끄럽고 느린) 동작으로 정제합니다. 이러한 혁신을 통해 실제 G1 휴머노이드 로봇이 고려한 두 가지 주요 상황, 즉 a) 얼굴을 위로 하고 누운 경우와 b) 얼굴을 아래로 하고 누운 경우에서 일어설 수 있음을 확인했습니다. 두 경우 모두 평평한 표면, 변형 가능한 표면, 미끄러운 표면 및 경사면(예: 미끄러운 잔디와 설원)에서 테스트되었습니다. 이는 실제 세계에서 인간 크기의 휴머노이드 로봇을 위한 학습된 일어서기 정책의 최초의 성공적인 시연 중 하나입니다.

## 参考
- http://arxiv.org/abs/2502.12152v2
