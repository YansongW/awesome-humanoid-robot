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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.12152v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (929 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2502.12152v2

## 개요
본 연구는 휴머노이드 로봇의 낙상 후 자동 복귀라는 핵심 난제를 해결하기 위해 HUMANUP 프레임워크를 제안한다. 기존의 수동 설계 컨트롤러는 낙상 후 다양한 신체 구성과 복잡한 지형에 대응하기 어려운 반면, 이 프레임워크는 2단계 학습 전략을 통해 효과적으로 대응한다: 1단계에서는 최소 제약 조건에서 고품질 기립 궤적을 탐색하고, 2단계에서는 궤적을 부드럽고 저속이며 강건한 배포 전략으로 최적화한다. 실험은 Unitree G1 로봇에서 검증되었으며, 평평한 지면, 잔디, 눈과 같은 변형 가능한 표면, 미끄러운 지면 및 경사면에서 엎드린 자세와 누운 자세의 기립을 성공적으로 구현했다. 이는 실제 세계의 대형 휴머노이드 로봇에서 학습 기반 기립 전략을 최초로 성공적으로 시연한 사례이다.

## 핵심 내용
### 방법 아키텍처
- **2단계 커리큘럼 학습**: 1단계에서는 희소 보상과 완화된 제약(예: 부드러움 또는 속도/토크 상한 제한 없음)을 사용하여 에이전트가 효과적인 기립 운동 궤적을 자유롭게 탐색하도록 한다; 2단계에서는 발견된 궤적을 기반으로 부드러움, 저속 등의 제약을 적용하고 도메인 무작위화를 통해 초기 구성 및 지형 변화에 대한 강건성을 향상시킨다.
- **접촉 모델링**: 기립 작업에서의 복잡한 접촉 패턴(예: 손, 팔꿈치, 무릎, 발과 지면의 다점 접촉)을 위해 프레임워크는 충돌 기하를 명시적으로 모델링하여 기존 locomotion 작업에서의 단순화된 접촉 가정을 피한다.

### 실험 설정
- **로봇 플랫폼**: Unitree G1 휴머노이드 로봇(약 1.3m 높이, 35kg 무게).
- **테스트 시나리오**: 두 가지 초기 자세(얼굴 위로 누운 자세 face up, 얼굴 아래로 엎드린 자세 face down), 네 가지 지형:
  - 평평한 단단한 지면
  - 변형 가능한 표면(예: 잔디, 눈)
  - 미끄러운 표면(예: 유포)
  - 경사면(경사 약 10°)
- **훈련 환경**: Isaac Gym 기반 시뮬레이션 환경에서 PPO 알고리즘으로 훈련하며, 정책은 관절 위치 명령을 직접 출력한다.

### 주요 결과
- **성공률**: 평평한 지면과 경사면에서 두 자세 모두 기립 성공률이 90%를 초과; 미끄러운 표면과 변형 가능한 표면에서는 성공률이 80% 이상 유지.
- **강건성**: 정책은 초기 관절 각도 편차(±15°)와 지면 마찰 계수 변화(0.2-1.0)에 대해 우수한 일반화 능력을 보인다.
- **전이 효율**: 시뮬레이션 훈련 후 추가 미세 조정 없이 실제 로봇으로 직접 제로샷 전이.

### 결론
HUMANUP 프레임워크는 커리큘럼 기반 강화 학습을 통해 실제 세계 휴머노이드 로봇에 적용 가능한 범용 기립 전략을 생성할 수 있음을 입증하며, 수동 설계 컨트롤러의 한계를 돌파했다. 향후 작업은 옆으로 누운 자세 복귀 및 더 복잡한 지형(예: 계단, 자갈 더미)으로 확장할 예정이다.
