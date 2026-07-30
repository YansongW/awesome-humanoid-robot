---
$id: ent_paper_embrace_collisions_humanoid_sh_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions'
  zh: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions'
  ko: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions'
summary:
  en: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: Embrace Collisions 是 2025 年提出的人形机器人全身控制框架，由研究团队开发。其核心贡献在于利用 GPU 加速的刚体物理模拟器训练策略，使机器人能在真实世界中实时执行包含随机接触和大幅躯干旋转的全身运动，突破了传统仅限手脚接触环境的限制。
  ko: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embrace_collisions
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.01465v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions (arXiv)'
  url: https://arxiv.org/abs/2502.01465
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions project page'
  url: https://project-instinct.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
以往人形机器人研究仅将机器人视为双足移动操作平台，只允许手脚与环境接触。然而人类会利用全身各部位与环境互动，例如坐椅子、从地面起身或在地板上翻滚。这种非手脚接触会为模型预测控制和强化学习方法带来巨大挑战，因为不可预测的接触序列使得模型预测控制几乎无法实时规划。为此，该工作提出一个通用的人形运动框架，接收离散运动指令并实时控制机器人电机动作。通过 GPU 加速的刚体模拟器，训练出的全身控制策略即使在随机接触、极大机器人基座旋转甚至不可行运动指令下，也能在真实世界中实时跟随高层指令。

## 核心内容
### 方法概述
- 提出通用人形运动框架，输入为离散运动指令，输出为实时电机动作。
- 采用 GPU 加速的刚体物理模拟器进行训练，实现零样本 sim-to-real 迁移。

### 核心挑战与解决
- **挑战一**：非手脚接触导致接触序列不可预测，传统模型预测控制无法实时规划。
- **挑战二**：零样本 sim-to-real 强化学习方法高度依赖 GPU 模拟器加速和碰撞检测简化。
- **挑战三**：人形机器人缺乏极端躯干运动，使得终止条件、运动指令和奖励设计等组件难以设计。
- **解决方案**：训练全身控制策略，使其能处理随机接触、极大机器人基座旋转（如大幅扭转）以及不可行的运动指令。

### 实验设置与关键结果
- 在真实世界中实时运行，验证了策略对随机接触和极端躯干运动的鲁棒性。
- 具体关键数字未在正文中提供，但项目页面（https://project-instinct.github.io）包含更多细节。

### 结论
该框架为人形机器人实现类人全身交互运动（如坐、躺、翻滚）提供了可行方案，突破了传统手脚接触的范式。

## Overview
Previous humanoid robot research works treat the robot as a bipedal mobile manipulation platform, where only the feet and hands contact the environment. However, we humans use all body parts to interact with the world, e.g., we sit in chairs, get up from the ground, or roll on the floor. Contacting the environment using body parts other than feet and hands brings significant challenges in both model-predictive control and reinforcement learning-based methods. An unpredictable contact sequence makes it almost impossible for model-predictive control to plan ahead in real time. The success of the zero-shot sim-to-real reinforcement learning method for humanoids heavily depends on the acceleration of GPU-based rigid-body physical simulator and simplification of the collision detection. Lacking extreme torso movement of the humanoid research makes all other components non-trivial to design, such as termination conditions, motion commands and reward designs. To address these potential challenges, we propose a general humanoid motion framework that takes discrete motion commands and controls the robot's motor action in real time. Using a GPU-accelerated rigid-body simulator, we train a humanoid whole-body control policy that follows the high-level motion command in the real world in real time, even with stochastic contacts and extremely large robot base rotation and not-so-feasible motion command. More details at https://project-instinct.github.io

## 개요
기존의 휴머노이드 로봇 연구는 로봇을 이족 보행 이동 조작 플랫폼으로 간주하여 발과 손만 환경과 접촉하도록 설계되었습니다. 그러나 인간은 의자에 앉거나, 바닥에서 일어나거나, 바닥에서 구르는 등 모든 신체 부위를 사용하여 세계와 상호작용합니다. 발과 손 이외의 신체 부위를 사용하여 환경과 접촉하는 것은 모델 예측 제어(Model Predictive Control)와 강화 학습 기반 방법 모두에 상당한 도전 과제를 제기합니다. 예측 불가능한 접촉 순서는 모델 예측 제어가 실시간으로 사전 계획을 수립하는 것을 거의 불가능하게 만듭니다. 휴머노이드를 위한 제로샷 시뮬레이션-실제(Sim-to-Real) 강화 학습 방법의 성공은 GPU 기반 강체 물리 시뮬레이터의 가속화와 충돌 감지의 단순화에 크게 의존합니다. 휴머노이드 연구에서 극단적인 상체 움직임이 부족하면 종료 조건, 동작 명령, 보상 설계와 같은 다른 모든 구성 요소를 설계하기가 쉽지 않습니다. 이러한 잠재적 도전 과제를 해결하기 위해, 우리는 이산 동작 명령을 입력받아 로봇의 모터 동작을 실시간으로 제어하는 일반적인 휴머노이드 동작 프레임워크를 제안합니다. GPU 가속 강체 시뮬레이터를 사용하여, 확률적 접촉, 극도로 큰 로봇 베이스 회전, 그리고 실현 가능성이 낮은 동작 명령이 있더라도 실제 세계에서 고수준 동작 명령을 실시간으로 따르는 휴머노이드 전신 제어 정책을 훈련합니다. 자세한 내용은 https://project-instinct.github.io 에서 확인할 수 있습니다.

## 핵심 내용
기존의 휴머노이드 로봇 연구는 로봇을 이족 보행 이동 조작 플랫폼으로 간주하여 발과 손만 환경과 접촉하도록 설계되었습니다. 그러나 인간은 의자에 앉거나, 바닥에서 일어나거나, 바닥에서 구르는 등 모든 신체 부위를 사용하여 세계와 상호작용합니다. 발과 손 이외의 신체 부위를 사용하여 환경과 접촉하는 것은 모델 예측 제어와 강화 학습 기반 방법 모두에 상당한 도전 과제를 제기합니다. 예측 불가능한 접촉 순서는 모델 예측 제어가 실시간으로 사전 계획을 수립하는 것을 거의 불가능하게 만듭니다. 휴머노이드를 위한 제로샷 시뮬레이션-실제 강화 학습 방법의 성공은 GPU 기반 강체 물리 시뮬레이터의 가속화와 충돌 감지의 단순화에 크게 의존합니다. 휴머노이드 연구에서 극단적인 상체 움직임이 부족하면 종료 조건, 동작 명령, 보상 설계와 같은 다른 모든 구성 요소를 설계하기가 쉽지 않습니다. 이러한 잠재적 도전 과제를 해결하기 위해, 우리는 이산 동작 명령을 입력받아 로봇의 모터 동작을 실시간으로 제어하는 일반적인 휴머노이드 동작 프레임워크를 제안합니다. GPU 가속 강체 시뮬레이터를 사용하여, 확률적 접촉, 극도로 큰 로봇 베이스 회전, 그리고 실현 가능성이 낮은 동작 명령이 있더라도 실제 세계에서 고수준 동작 명령을 실시간으로 따르는 휴머노이드 전신 제어 정책을 훈련합니다. 자세한 내용은 https://project-instinct.github.io 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2502.01465v1
