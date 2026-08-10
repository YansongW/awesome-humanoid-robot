---
$id: ent_paper_physics_models_for_sim_to_real_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
  zh: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
  ko: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
summary:
  en: 'arXiv:2606.28805v2 Announce Type: replace Abstract: At competitive speeds and spins, a table tennis ball follows complex,
    counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement
    learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity
    simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures
    real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling
    inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses
    on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level
    play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact.
    that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we
    model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations.
    For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals
    into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component
    to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping.
    Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces
    prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL
    policies for the first real-world robot table tennis AI agent capable of competing against professional players.'
  zh: 本文提出了一套用于机器人乒乓球从仿真到真实迁移的物理模型，涵盖空气动力学、球台接触和球拍接触三大模块。该工作在277场职业比赛数据上验证，将落点预测中位误差降低59%，并首次训练出能与职业选手对战的真实世界机器人AI智能体。
  ko: 'arXiv:2606.28805v2 Announce Type: replace Abstract: At competitive speeds and spins, a table tennis ball follows complex,
    counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement
    learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity
    simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures
    real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling
    inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses
    on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level
    play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact.
    that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we
    model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations.
    For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals
    into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component
    to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping.
    Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces
    prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL
    policies for the first real-world robot table tennis AI agent capable of competing against professional players.'
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
- physics_models_for_sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.28805v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1330 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis (arXiv)
  url: https://arxiv.org/abs/2606.28805
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
在高速高旋条件下，乒乓球轨迹复杂且反直觉，机器人需在毫秒级时间内精确追踪并回击。由于真实环境训练成本极高且危险，高保真仿真成为关键，但策略的可迁移性严重依赖仿真对真实动力学的忠实还原——在对抗性比赛中，任何建模误差都会成为对手可攻击的弱点。现有机器人乒乓球研究多局限于有限的速度和旋转范围，无法捕捉职业级比赛中的丰富球路。为此，本文提出了空气动力学、球台接触和球拍接触三大物理模型，在空气动力学方程中将阻力和马格努斯力系数建模为雷诺数和旋转比的函数；球台接触模型考虑球体屈曲对恢复系数的影响，并引入残差修正瞬时点接触模型；球拍接触模型则采用残差神经网络补充法向、切向恢复系数及扭转自旋阻尼。在277场职业比赛数据集上，该模型将落点预测中位误差降低59%，并首次训练出能与职业选手对战的真实世界机器人AI智能体。

## 核心内容
### 核心贡献
本文针对机器人乒乓球从仿真到真实迁移中的物理建模难题，提出了三组高保真物理模型，覆盖球飞行、球台接触和球拍接触三大关键环节。

### 方法架构
- **空气动力学模型**：将阻力系数（drag coefficient）和马格努斯力系数（Magnus force coefficient）建模为雷诺数（Reynolds number）和旋转比（spin ratio）的函数，取代传统固定系数假设，从而准确捕捉高速高旋下的复杂轨迹。
- **球台接触模型**：考虑乒乓球在撞击台面时发生的球体屈曲（ball buckling）效应，将其对恢复系数（coefficient of restitution）的影响纳入模型；同时引入残差项（residuals）修正传统的瞬时点接触模型（instantaneous point-contact model），提升弹跳预测精度。
- **球拍接触模型**：采用残差神经网络（residual neural network）组件，补充法向恢复系数（normal coefficient of restitution）、切向恢复系数（tangential coefficient of restitution）以及扭转自旋阻尼（torsional spin damping）的建模，使球拍与球的交互更贴近真实物理。

### 实验设置与关键数字
- **数据集**：前所未有的规模，包含277场职业比赛（competitive matches）的真实数据，覆盖广泛的速度和旋转范围。
- **性能提升**：落点预测中位误差（median landing-position error）降低59%，显著优于现有模型。
- **应用成果**：基于该物理模型训练的强化学习（RL）策略，首次使真实世界机器人乒乓球AI智能体具备与职业选手（professional players）对战的能力。

### 结论
本文通过精细化的物理建模，大幅提升了仿真环境对真实乒乓球动力学的还原度，为高动态对抗性运动中的sim-to-real迁移提供了有效方案。该工作不仅推动了机器人乒乓球领域的发展，也为其他需要高保真物理仿真的机器人任务（如球类运动、高速操控）提供了可借鉴的建模思路。

## Overview
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## Overview
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model, we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduce prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## Content
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model, we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduce prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## 参考
- http://arxiv.org/abs/2606.28805v2

## 개요
고속·고회전 조건에서 탁구공의 궤적은 복잡하고 직관에 반하며, 로봇은 밀리초 단위의 시간 내에 정밀하게 추적하고 되받아쳐야 합니다. 실제 환경에서의 훈련 비용은 매우 높고 위험하기 때문에, 고충실도 시뮬레이션이 핵심이 되지만, 정책의 전이 가능성은 시뮬레이션이 실제 역학을 얼마나 충실히 재현하는지에 크게 의존합니다——경쟁적인 경기에서는 어떤 모델링 오차도 상대가 공격할 수 있는 약점이 됩니다. 기존의 로봇 탁구 연구는 대부분 제한된 속도와 회전 범위에 국한되어 있어, 프로 수준 경기에서 나타나는 다양한 구질을 포착하지 못합니다. 이를 위해 본 논문은 공기역학, 탁구대 접촉, 라켓 접촉의 세 가지 물리 모델을 제안합니다. 공기역학 방정식에서는 항력 계수와 마그누스 힘 계수를 레이놀즈 수와 회전비의 함수로 모델링하고, 탁구대 접촉 모델은 공의 좌굴이 반발 계수에 미치는 영향을 고려하며, 순간 점접촉 모델에 잔차 보정을 도입합니다. 라켓 접촉 모델은 잔차 신경망을 사용하여 법선·접선 반발 계수 및 비틀림 스핀 감쇠를 보완합니다. 277경기의 프로 경기 데이터셋에서 이 모델은 낙점 예측 중앙 오차를 59% 줄였으며, 처음으로 프로 선수와 대결할 수 있는 실제 세계 로봇 AI 에이전트를 훈련시켰습니다.

## 핵심 내용
### 핵심 기여
본 논문은 로봇 탁구의 시뮬레이션-실제 전이에서 발생하는 물리 모델링 문제를 해결하기 위해, 공의 비행, 탁구대 접촉, 라켓 접촉의 세 가지 핵심 단계를 포괄하는 세 가지 고충실도 물리 모델을 제안합니다.

### 방법 구조
- **공기역학 모델**: 항력 계수와 마그누스 힘 계수를 레이놀즈 수와 회전비의 함수로 모델링하여 기존의 고정 계수 가정을 대체함으로써, 고속·고회전 조건에서의 복잡한 궤적을 정확히 포착합니다.
- **탁구대 접촉 모델**: 탁구공이 탁구대에 충돌할 때 발생하는 공의 좌굴 효과를 고려하여, 이를 반발 계수에 미치는 영향으로 모델에 포함시킵니다. 또한 잔차 항을 도입하여 기존의 순간 점접촉 모델을 보정함으로써 바운스 예측 정밀도를 향상시킵니다.
- **라켓 접촉 모델**: 잔차 신경망 구성 요소를 사용하여 법선 반발 계수, 접선 반발 계수 및 비틀림 스핀 감쇠의 모델링을 보완함으로써, 라켓과 공의 상호작용이 실제 물리에 더 가깝게 만듭니다.

### 실험 설정 및 주요 수치
- **데이터셋**: 전례 없는 규모로, 277경기의 프로 경기 실제 데이터를 포함하며, 광범위한 속도와 회전 범위를 포괄합니다.
- **성능 향상**: 낙점 예측 중앙 오차가 59% 감소하여 기존 모델보다 크게 우수합니다.
- **응용 성과**: 이 물리 모델을 기반으로 훈련된 강화 학습 정책은 처음으로 실제 세계 로봇 탁구 AI 에이전트가 프로 선수와 대결할 수 있는 능력을 갖추게 했습니다.

### 결론
본 논문은 정밀한 물리 모델링을 통해 시뮬레이션 환경의 실제 탁구 역학 재현도를 크게 향상시켰으며, 고동적 경쟁 스포츠에서의 sim-to-real 전이를 위한 효과적인 해결책을 제공합니다. 이 작업은 로봇 탁구 분야의 발전을 촉진했을 뿐만 아니라, 고충실도 물리 시뮬레이션이 필요한 다른 로봇 작업(예: 구기 스포츠, 고속 조작)에도 참고할 수 있는 모델링 접근 방식을 제시합니다.
