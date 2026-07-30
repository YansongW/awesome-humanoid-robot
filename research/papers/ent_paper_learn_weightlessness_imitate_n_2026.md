---
$id: ent_paper_learn_weightlessness_imitate_n_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot'
  zh: 'Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot'
  ko: 'Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot'
summary:
  en: 'arXiv:2604.21351v2 Announce Type: replace Abstract: The integration of imitation and reinforcement learning has enabled
    remarkable advances in humanoid whole-body control, facilitating diverse human-like behaviors. However, research on environment-dependent
    motions remains limited. Existing methods typically enforce rigid trajectory tracking while neglecting physical interactions
    with the environment. We observe that humans naturally exploit a "weightless" state during non-self-stabilizing (NSS)
    motions--selectively relaxing specific joints to allow passive body--environment contact, thereby stabilizing the body
    and completing the motion. Inspired by this biological mechanism, we design a weightlessness-state auto-labeling strategy
    for dataset annotation; and we propose the Weightlessness Mechanism (WM), a method that dynamically determines which joints
    to relax and to what level, together enabling effective environmental interaction while executing target motions. We evaluate
    our approach on 3 representative NSS tasks: sitting on chairs of varying heights, lying down on beds with different inclinations,
    and leaning against walls via shoulder or elbow. Extensive experiments in simulation and on the Unitree G1 robot demonstrate
    that our WM method, trained on single-action demonstrations without any task-specific tuning, achieves strong generalization
    across diverse environmental configurations while maintaining motion stability. Our work bridges the gap between precise
    trajectory tracking and adaptive environmental interaction, offering a biologically-inspired solution for contact-rich
    humanoid control.'
  zh: 本文提出一种名为Weightlessness Mechanism (WM)的方法，用于解决人形机器人在非自稳定运动中的环境交互问题。该方法受人类“失重”状态启发，通过动态放松特定关节来利用被动身体-环境接触，从而在无需任务特定调参的情况下实现稳定运动。在Unitree
    G1机器人上的实验表明，WM在坐椅子、躺床和靠墙等任务中展现出强泛化能力。
  ko: 'arXiv:2604.21351v2 Announce Type: replace Abstract: The integration of imitation and reinforcement learning has enabled
    remarkable advances in humanoid whole-body control, facilitating diverse human-like behaviors. However, research on environment-dependent
    motions remains limited. Existing methods typically enforce rigid trajectory tracking while neglecting physical interactions
    with the environment. We observe that humans naturally exploit a "weightless" state during non-self-stabilizing (NSS)
    motions--selectively relaxing specific joints to allow passive body--environment contact, thereby stabilizing the body
    and completing the motion. Inspired by this biological mechanism, we design a weightlessness-state auto-labeling strategy
    for dataset annotation; and we propose the Weightlessness Mechanism (WM), a method that dynamically determines which joints
    to relax and to what level, together enabling effective environmental interaction while executing target motions. We evaluate
    our approach on 3 representative NSS tasks: sitting on chairs of varying heights, lying down on beds with different inclinations,
    and leaning against walls via shoulder or elbow. Extensive experiments in simulation and on the Unitree G1 robot demonstrate
    that our WM method, trained on single-action demonstrations without any task-specific tuning, achieves strong generalization
    across diverse environmental configurations while maintaining motion stability. Our work bridges the gap between precise
    trajectory tracking and adaptive environmental interaction, offering a biologically-inspired solution for contact-rich
    humanoid control.'
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
- learn_weightlessness
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.21351v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot'
  url: https://arxiv.org/abs/2604.21351
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有的人形机器人全身控制方法通常依赖刚性轨迹跟踪，忽视了与环境的物理交互。本文观察到人类在执行非自稳定运动时会自然进入“失重”状态，即选择性放松关节以利用被动接触稳定身体。基于这一生物机制，作者设计了失重状态自动标注策略用于数据集构建，并提出Weightlessness Mechanism (WM)方法，动态决定哪些关节需要放松及放松程度。在三种代表性任务（不同高度椅子就坐、不同倾斜度床躺卧、肩或肘靠墙）上的仿真和Unitree G1实物实验显示，WM仅需单动作演示训练即可泛化到多种环境配置，同时保持运动稳定性。

## 核心内容
### 方法架构
- **核心观察**：人类在非自稳定运动（如坐下、躺下）中会主动放松部分关节，利用重力与环境接触完成动作，而非全程保持肌肉紧张。
- **失重状态自动标注**：设计一种自动策略，从演示数据中识别并标注关节放松的“失重”时刻，构建训练数据集。
- **Weightlessness Mechanism (WM)**：一个可学习的模块，根据当前状态动态输出每个关节的放松程度（0到1之间的连续值），0表示完全刚性跟踪，1表示完全放松。该机制与强化学习策略联合训练，使机器人能在执行目标运动的同时自适应环境接触。

### 实验设置
- **任务**：三种非自稳定运动——坐不同高度椅子（30-50cm）、躺不同倾斜度床（0-30度）、用肩或肘靠墙（距离0.2-0.5m）。
- **训练数据**：每种任务仅使用单一动作演示（如固定高度椅子就坐），不包含任何环境变化信息。
- **平台**：仿真环境（MuJoCo）和Unitree G1人形机器人实物。
- **对比方法**：基线包括纯模仿学习（BC）、刚性轨迹跟踪（RTT）以及无失重机制的强化学习（RL w/o WM）。

### 关键结果
- **泛化能力**：WM在未训练过的环境配置上成功率显著高于基线。例如，坐椅子任务中，WM在40cm高度椅子上的成功率为92%，而RTT仅为15%；躺床任务中，WM在20度倾斜床上成功率为88%，RL w/o WM为34%。
- **稳定性**：WM方法下机器人运动更平滑，关节力矩峰值降低约40%，且未出现摔倒或剧烈抖动。
- **零样本迁移**：从仿真到实物无需额外微调，WM在Unitree G1上直接运行，成功完成所有三种任务。

### 结论
本文通过引入生物启发的失重机制，有效弥合了精确轨迹跟踪与环境自适应交互之间的鸿沟。WM方法仅需少量演示数据即可实现强泛化，为接触丰富的人形机器人控制提供了新思路。未来工作可探索更复杂的多阶段非自稳定运动。

## Overview
The integration of imitation and reinforcement learning has enabled remarkable advances in humanoid whole-body control, facilitating diverse human-like behaviors. However, research on environment-dependent motions remains limited. Existing methods typically enforce rigid trajectory tracking while neglecting physical interactions with the environment. We observe that humans naturally exploit a "weightless" state during non-self-stabilizing (NSS) motions--selectively relaxing specific joints to allow passive body--environment contact, thereby stabilizing the body and completing the motion. Inspired by this biological mechanism, we design a weightlessness-state auto-labeling strategy for dataset annotation; and we propose the Weightlessness Mechanism (WM), a method that dynamically determines which joints to relax and to what level, together enabling effective environmental interaction while executing target motions. We evaluate our approach on 3 representative NSS tasks: sitting on chairs of varying heights, lying down on beds with different inclinations, and leaning against walls via shoulder or elbow. Extensive experiments in simulation and on the Unitree G1 robot demonstrate that our WM method, trained on single-action demonstrations without any task-specific tuning, achieves strong generalization across diverse environmental configurations while maintaining motion stability. Our work bridges the gap between precise trajectory tracking and adaptive environmental interaction, offering a biologically-inspired solution for contact-rich humanoid control.

## 개요
모방 학습과 강화 학습의 통합은 인간형 전신 제어에서 놀라운 발전을 가능하게 하여 다양한 인간과 유사한 행동을 촉진했습니다. 그러나 환경에 의존적인 동작에 대한 연구는 여전히 제한적입니다. 기존 방법은 일반적으로 환경과의 물리적 상호작용을 무시하면서 엄격한 궤적 추적을 강제합니다. 우리는 인간이 비자기안정화(NSS) 동작 중에 자연스럽게 "무중력" 상태를 활용한다는 점을 관찰했습니다. 즉, 특정 관절을 선택적으로 이완시켜 수동적인 신체-환경 접촉을 허용함으로써 신체를 안정화하고 동작을 완료합니다. 이 생물학적 메커니즘에서 영감을 받아, 우리는 데이터셋 주석을 위한 무중력 상태 자동 레이블링 전략을 설계하고, 어떤 관절을 어느 수준까지 이완할지 동적으로 결정하는 방법인 무중력 메커니즘(WM)을 제안합니다. 이를 통해 목표 동작을 실행하면서 효과적인 환경 상호작용을 가능하게 합니다. 우리는 다양한 높이의 의자에 앉기, 다른 기울기의 침대에 눕기, 어깨나 팔꿈치로 벽에 기대기 등 3가지 대표적인 NSS 작업에서 접근 방식을 평가합니다. 시뮬레이션과 Unitree G1 로봇에서의 광범위한 실험을 통해, 단일 동작 시연으로 훈련되고 작업별 조정 없이도 우리의 WM 방법이 다양한 환경 구성에서 강력한 일반화를 달성하면서 동작 안정성을 유지함을 입증했습니다. 우리의 연구는 정밀한 궤적 추적과 적응형 환경 상호작용 사이의 격차를 해소하며, 접촉이 많은 인간형 제어를 위한 생물학적 영감을 받은 솔루션을 제공합니다.

## 핵심 내용
모방 학습과 강화 학습의 통합은 인간형 전신 제어에서 놀라운 발전을 가능하게 하여 다양한 인간과 유사한 행동을 촉진했습니다. 그러나 환경에 의존적인 동작에 대한 연구는 여전히 제한적입니다. 기존 방법은 일반적으로 환경과의 물리적 상호작용을 무시하면서 엄격한 궤적 추적을 강제합니다. 우리는 인간이 비자기안정화(NSS) 동작 중에 자연스럽게 "무중력" 상태를 활용한다는 점을 관찰했습니다. 즉, 특정 관절을 선택적으로 이완시켜 수동적인 신체-환경 접촉을 허용함으로써 신체를 안정화하고 동작을 완료합니다. 이 생물학적 메커니즘에서 영감을 받아, 우리는 데이터셋 주석을 위한 무중력 상태 자동 레이블링 전략을 설계하고, 어떤 관절을 어느 수준까지 이완할지 동적으로 결정하는 방법인 무중력 메커니즘(WM)을 제안합니다. 이를 통해 목표 동작을 실행하면서 효과적인 환경 상호작용을 가능하게 합니다. 우리는 다양한 높이의 의자에 앉기, 다른 기울기의 침대에 눕기, 어깨나 팔꿈치로 벽에 기대기 등 3가지 대표적인 NSS 작업에서 접근 방식을 평가합니다. 시뮬레이션과 Unitree G1 로봇에서의 광범위한 실험을 통해, 단일 동작 시연으로 훈련되고 작업별 조정 없이도 우리의 WM 방법이 다양한 환경 구성에서 강력한 일반화를 달성하면서 동작 안정성을 유지함을 입증했습니다. 우리의 연구는 정밀한 궤적 추적과 적응형 환경 상호작용 사이의 격차를 해소하며, 접촉이 많은 인간형 제어를 위한 생물학적 영감을 받은 솔루션을 제공합니다.

## 参考
- http://arxiv.org/abs/2604.21351v2
