---
$id: ent_paper_fame_force_adaptive_rl_for_exp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid'
  zh: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid'
  ko: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid'
summary:
  en: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: FAME 是一个力自适应强化学习框架，由研究团队提出，用于扩展全尺寸人形机器人的操作包络。其核心贡献在于通过学习潜在上下文编码，使站立策略能根据上肢关节配置和双手交互力进行在线适应，从而提升在外部手部力干扰下的平衡能力。
  ko: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid is a 2026 work on loco-manipulation
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
- fame
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.08961v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid (arXiv)'
  url: https://arxiv.org/abs/2603.08961v1
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid project page'
  url: https://fame10.github.io/Fame/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
FAME 框架针对人形机器人双手操作时，外部手部力通过运动链传播并限制可行操作包络的问题，提出了一种力自适应强化学习方案。该框架在训练时，对每只手施加多样化的球形采样 3D 力，并结合上肢姿态课程，使策略暴露于连续变化的手臂配置下的操作扰动。部署时，交互力从机器人动力学估计，输入同一编码器，实现无需腕部力/扭矩传感器的在线适应。在仿真中，FAME 在五种固定手臂配置下，将平均站立成功率提升至 73.84%，显著优于课程基线（51.40%）和基础策略（29.44%）。该策略已在全尺寸 Unitree H12 人形机器人上部署，并在代表性负载交互场景中验证了鲁棒性。

## 核心内容
### 方法
- **问题定义**：人形机器人双手操作时，外部手部力通过运动链传播，限制可行操作包络，维持平衡是关键挑战。
- **FAME 框架**：提出力自适应强化学习框架，将站立策略条件化于一个学习到的潜在上下文编码，该编码编码上肢关节配置和双手交互力。
- **训练策略**：
  - 在仿真中，对每只手施加多样化的球形采样 3D 力，注入扰动。
  - 结合上肢姿态课程，使策略暴露于连续变化的手臂配置下的操作扰动。
- **部署策略**：
  - 交互力从机器人动力学估计，输入同一编码器。
  - 实现无需腕部力/扭矩传感器的在线适应。

### 实验设置
- **仿真环境**：五种固定手臂配置，随机化手部力和指令基座高度。
- **基线对比**：
  - 基础策略：无课程或力自适应。
  - 课程基线：仅使用上肢姿态课程，无力自适应。
- **真实机器人**：全尺寸 Unitree H12 人形机器人。

### 关键结果
- **仿真性能**：
  - FAME 平均站立成功率：73.84%
  - 课程基线：51.40%
  - 基础策略：29.44%
- **真实机器人验证**：在代表性负载交互场景中测试鲁棒性，包括非对称单臂负载和对称双臂负载。

### 结论
FAME 通过力自适应强化学习，显著扩展了人形机器人的操作包络，在仿真和真实机器人上均验证了有效性。代码和视频已公开。

## Overview
Maintaining balance under external hand forces is critical for humanoid bimanual manipulation, where interaction forces propagate through the kinematic chain and constrain the feasible manipulation envelope. We propose \textbf{FAME}, a force-adaptive reinforcement learning framework that conditions a standing policy on a learned latent context encoding upper-body joint configuration and bimanual interaction forces. During training, we apply diverse, spherically sampled 3D forces on each hand to inject disturbances in simulation together with an upper-body pose curriculum, exposing the policy to manipulation-induced perturbations across continuously varying arm configurations. At deployment, interaction forces are estimated from the robot dynamics and fed to the same encoder, enabling online adaptation without wrist force/torque sensors. In simulation across five fixed arm configurations with randomized hand forces and commanded base heights, FAME improves mean standing success to 73.84%, compared to 51.40% for the curriculum-only baseline and 29.44% for the base policy. We further deploy the learned policy on a full-scale Unitree H12 humanoid and evaluate robustness in representative load-interaction scenarios, including asymmetric single-arm load and symmetric bimanual load. Code and videos are available on https://fame10.github.io/Fame/

## Overview
Maintaining balance under external hand forces is critical for humanoid bimanual manipulation, where interaction forces propagate through the kinematic chain and constrain the feasible manipulation envelope. We propose **FAME**, a force-adaptive reinforcement learning framework that conditions a standing policy on a learned latent context encoding upper-body joint configuration and bimanual interaction forces. During training, we apply diverse, spherically sampled 3D forces on each hand to inject disturbances in simulation together with an upper-body pose curriculum, exposing the policy to manipulation-induced perturbations across continuously varying arm configurations. At deployment, interaction forces are estimated from the robot dynamics and fed to the same encoder, enabling online adaptation without wrist force/torque sensors. In simulation across five fixed arm configurations with randomized hand forces and commanded base heights, FAME improves mean standing success to 73.84%, compared to 51.40% for the curriculum-only baseline and 29.44% for the base policy. We further deploy the learned policy on a full-scale Unitree H12 humanoid and evaluate robustness in representative load-interaction scenarios, including asymmetric single-arm load and symmetric bimanual load. Code and videos are available on https://fame10.github.io/Fame/

## Content
Maintaining balance under external hand forces is critical for humanoid bimanual manipulation, where interaction forces propagate through the kinematic chain and constrain the feasible manipulation envelope. We propose **FAME**, a force-adaptive reinforcement learning framework that conditions a standing policy on a learned latent context encoding upper-body joint configuration and bimanual interaction forces. During training, we apply diverse, spherically sampled 3D forces on each hand to inject disturbances in simulation together with an upper-body pose curriculum, exposing the policy to manipulation-induced perturbations across continuously varying arm configurations. At deployment, interaction forces are estimated from the robot dynamics and fed to the same encoder, enabling online adaptation without wrist force/torque sensors. In simulation across five fixed arm configurations with randomized hand forces and commanded base heights, FAME improves mean standing success to 73.84%, compared to 51.40% for the curriculum-only baseline and 29.44% for the base policy. We further deploy the learned policy on a full-scale Unitree H12 humanoid and evaluate robustness in representative load-interaction scenarios, including asymmetric single-arm load and symmetric bimanual load. Code and videos are available on https://fame10.github.io/Fame/

## 개요
외부 손 힘 하에서 균형 유지는 인간형 양손 조작에 있어 매우 중요하며, 상호작용 힘이 운동학적 체인을 통해 전파되어 가능한 조작 범위를 제한합니다. 본 논문에서는 **FAME**을 제안합니다. 이는 학습된 잠재 컨텍스트(상체 관절 구성 및 양손 상호작용 힘을 인코딩)에 기반하여 서 있는 정책을 조건화하는 힘 적응형 강화 학습 프레임워크입니다. 훈련 중에는 각 손에 다양하게 구형 샘플링된 3D 힘을 적용하여 시뮬레이션에서 교란을 주고, 상체 자세 커리큘럼과 함께 연속적으로 변화하는 팔 구성에서 조작 유발 섭동에 정책을 노출시킵니다. 배포 시에는 로봇 동역학으로부터 상호작용 힘을 추정하여 동일한 인코더에 입력함으로써 손목 힘/토크 센서 없이 온라인 적응을 가능하게 합니다. 무작위 손 힘과 명령된 베이스 높이를 가진 다섯 가지 고정 팔 구성에서의 시뮬레이션에서 FAME은 평균 서기 성공률을 73.84%로 향상시켰으며, 이는 커리큘럼 전용 기준선의 51.40% 및 기본 정책의 29.44%보다 높은 수치입니다. 또한 학습된 정책을 실제 크기의 Unitree H12 인간형 로봇에 배포하여 비대칭 단일 팔 하중 및 대칭 양손 하중을 포함한 대표적인 하중 상호작용 시나리오에서 강건성을 평가했습니다. 코드와 비디오는 https://fame10.github.io/Fame/ 에서 확인할 수 있습니다.

## 핵심 내용
외부 손 힘 하에서 균형 유지는 인간형 양손 조작에 있어 매우 중요하며, 상호작용 힘이 운동학적 체인을 통해 전파되어 가능한 조작 범위를 제한합니다. 본 논문에서는 **FAME**을 제안합니다. 이는 학습된 잠재 컨텍스트(상체 관절 구성 및 양손 상호작용 힘을 인코딩)에 기반하여 서 있는 정책을 조건화하는 힘 적응형 강화 학습 프레임워크입니다. 훈련 중에는 각 손에 다양하게 구형 샘플링된 3D 힘을 적용하여 시뮬레이션에서 교란을 주고, 상체 자세 커리큘럼과 함께 연속적으로 변화하는 팔 구성에서 조작 유발 섭동에 정책을 노출시킵니다. 배포 시에는 로봇 동역학으로부터 상호작용 힘을 추정하여 동일한 인코더에 입력함으로써 손목 힘/토크 센서 없이 온라인 적응을 가능하게 합니다. 무작위 손 힘과 명령된 베이스 높이를 가진 다섯 가지 고정 팔 구성에서의 시뮬레이션에서 FAME은 평균 서기 성공률을 73.84%로 향상시켰으며, 이는 커리큘럼 전용 기준선의 51.40% 및 기본 정책의 29.44%보다 높은 수치입니다. 또한 학습된 정책을 실제 크기의 Unitree H12 인간형 로봇에 배포하여 비대칭 단일 팔 하중 및 대칭 양손 하중을 포함한 대표적인 하중 상호작용 시나리오에서 강건성을 평가했습니다. 코드와 비디오는 https://fame10.github.io/Fame/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2603.08961v1
