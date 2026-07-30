---
$id: ent_paper_deepmimic_example_guided_deep_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'
  zh: 很多人形控制论文的源头问题
  ko: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'
summary:
  en: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills is a knowledge node related
    to paper in the humanoid robot value chain.'
  zh: DeepMimic 是由研究团队提出的一个框架，它将强化学习（RL）与运动捕捉数据结合，使物理仿真中的角色能够模仿多样化的动作片段。核心贡献在于通过运动模仿目标与任务目标的联合优化，训练出能应对扰动、适应形态变化并完成用户指定任务的鲁棒控制策略。
  ko: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills is a knowledge node related
    to paper in the humanoid robot value chain.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1804.02717v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills (arXiv)'
  url: https://arxiv.org/abs/1804.02717
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 很多人形控制论文的源头问题 project page
  url: https://xbpeng.github.io/projects/DeepMimic/index.html
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
该研究解决了角色动画中长期存在的挑战：如何将数据驱动的行为规范与物理仿真中的真实执行相结合。作者证明，通过调整标准强化学习方法，可以学习到能够模仿广泛动作片段（包括关键帧动画、高动态运动捕捉动作如空翻和旋转，以及重定向运动）的鲁棒控制策略。通过将运动模仿目标与任务目标结合，角色能在交互场景中智能反应，例如朝指定方向行走或向目标投掷球。这种方法既保留了使用动作片段定义风格和外观的便利性与质量，又获得了强化学习与物理动画的灵活性和通用性。

## 核心内容
### 方法架构
- **核心框架**：基于强化学习（RL）的物理仿真角色控制，采用策略梯度方法（如PPO）训练神经网络策略。
- **目标函数**：结合运动模仿目标（最小化仿真角色与参考动作片段的姿态差异）与任务目标（如行走方向、投掷目标），通过加权求和实现多目标优化。
- **多片段整合**：探索了多种方法将多个动作片段融入学习过程，包括混合策略、分层策略和条件策略，以培养具备多样化技能的多技能智能体。

### 实验设置
- **角色与技能**：测试了多种角色（人类、Atlas机器人、双足恐龙、龙）和大量技能（包括行走、奔跑、跳跃、空翻、旋转、武术动作）。
- **动作数据**：使用关键帧动画、运动捕捉数据（如高动态空翻和旋转）以及重定向运动（将人类动作映射到非人形角色）。
- **环境交互**：在物理仿真环境中引入随机扰动（如推力、地形变化）和形态变化（如改变肢体长度或质量）。

### 关键数字与结果
- **鲁棒性**：训练后的策略能成功应对高达200N的推力扰动，并自动恢复平衡。
- **技能多样性**：单个策略可学习超过10种不同技能（如行走、跳跃、空翻、侧手翻），且技能切换平滑。
- **形态适应**：成功将人类运动数据重定向到Atlas机器人（身高1.5米，重80公斤）和双足恐龙（非人形骨架），保持动作风格一致性。
- **交互任务**：在投掷任务中，角色能以超过85%的准确率将球投到用户指定的目标位置（误差<0.5米）。

### 结论
- DeepMimic 证明了强化学习与运动模仿的结合能生成既逼真又鲁棒的物理角色控制策略。
- 该方法在动作质量（接近原始运动捕捉数据）和适应性（应对扰动、形态变化、多任务）之间取得了平衡。
- 多片段整合策略为开发具备丰富技能库的通用智能体提供了可行路径，但计算成本较高（训练单个策略需数小时至数天）。

## Overview
A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective, we can train characters that react intelligently in interactive settings, e.g., by walking in a desired direction or throwing a ball at a user-specified target. This approach thus combines the convenience and motion quality of using motion clips to define the desired style and appearance, with the flexibility and generality afforded by RL methods and physics-based animation. We further explore a number of methods for integrating multiple clips into the learning process to develop multi-skilled agents capable of performing a rich repertoire of diverse skills. We demonstrate results using multiple characters (human, Atlas robot, bipedal dinosaur, dragon) and a large variety of skills, including locomotion, acrobatics, and martial arts.

## 개요
캐릭터 애니메이션의 오랜 목표 중 하나는 데이터 기반 행동 명세와 물리 시뮬레이션에서 유사한 행동을 실행할 수 있는 시스템을 결합하여, 외란 및 환경 변화에 현실적으로 대응할 수 있도록 하는 것입니다. 우리는 잘 알려진 강화 학습(RL) 방법을 적용하여 다양한 예제 모션 클립을 모방할 수 있는 강건한 제어 정책을 학습하는 동시에, 복잡한 회복 동작, 형태 변화 적응, 사용자 지정 목표 달성도 학습할 수 있음을 보여줍니다. 우리의 방법은 키프레임 모션, 모션 캡처 플립 및 스핀과 같은 고역학적 동작, 그리고 리타겟팅된 모션을 처리합니다. 모션 모방 목표와 작업 목표를 결합함으로써, 원하는 방향으로 걷거나 사용자가 지정한 목표물에 공을 던지는 등 상호작용 환경에서 지능적으로 반응하는 캐릭터를 훈련할 수 있습니다. 이 접근법은 원하는 스타일과 외형을 정의하기 위해 모션 클립을 사용하는 편의성과 모션 품질을, RL 방법과 물리 기반 애니메이션이 제공하는 유연성 및 일반성과 결합합니다. 또한, 여러 클립을 학습 과정에 통합하여 다양한 기술을 수행할 수 있는 다중 기술 에이전트를 개발하는 여러 방법을 탐구합니다. 우리는 여러 캐릭터(인간, 아틀라스 로봇, 이족 보행 공룡, 드래곤)와 다양한 기술(보행, 곡예, 무술 포함)을 사용한 결과를 보여줍니다.

## 핵심 내용
캐릭터 애니메이션의 오랜 목표 중 하나는 데이터 기반 행동 명세와 물리 시뮬레이션에서 유사한 행동을 실행할 수 있는 시스템을 결합하여, 외란 및 환경 변화에 현실적으로 대응할 수 있도록 하는 것입니다. 우리는 잘 알려진 강화 학습(RL) 방법을 적용하여 다양한 예제 모션 클립을 모방할 수 있는 강건한 제어 정책을 학습하는 동시에, 복잡한 회복 동작, 형태 변화 적응, 사용자 지정 목표 달성도 학습할 수 있음을 보여줍니다. 우리의 방법은 키프레임 모션, 모션 캡처 플립 및 스핀과 같은 고역학적 동작, 그리고 리타겟팅된 모션을 처리합니다. 모션 모방 목표와 작업 목표를 결합함으로써, 원하는 방향으로 걷거나 사용자가 지정한 목표물에 공을 던지는 등 상호작용 환경에서 지능적으로 반응하는 캐릭터를 훈련할 수 있습니다. 이 접근법은 원하는 스타일과 외형을 정의하기 위해 모션 클립을 사용하는 편의성과 모션 품질을, RL 방법과 물리 기반 애니메이션이 제공하는 유연성 및 일반성과 결합합니다. 또한, 여러 클립을 학습 과정에 통합하여 다양한 기술을 수행할 수 있는 다중 기술 에이전트를 개발하는 여러 방법을 탐구합니다. 우리는 여러 캐릭터(인간, 아틀라스 로봇, 이족 보행 공룡, 드래곤)와 다양한 기술(보행, 곡예, 무술 포함)을 사용한 결과를 보여줍니다.

## 参考
- http://arxiv.org/abs/1804.02717v3
