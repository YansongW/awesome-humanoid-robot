---
$id: ent_paper_embedding_classical_balance_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
  zh: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
  ko: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
summary:
  en: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: 本文提出一种将经典平衡控制指标嵌入强化学习框架的统一策略，用于人形机器人的自主恢复。该工作由研究团队于2026年发表，核心贡献在于通过捕获点、质心状态和质心动量作为特权评论家输入与塑形奖励，使单一策略覆盖从踝关节策略到多触点站立的完整恢复谱系，在Unitree
    H1-2上达到93.4%恢复率。
  ko: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embedding_classical_balance_co
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.08619v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery (arXiv)
  url: https://arxiv.org/abs/2603.08619
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有强化学习方法将人形机器人恢复视为纯任务奖励问题，缺乏对平衡状态的显式表征。本文通过嵌入经典平衡指标（捕获点、质心状态、质心动量）作为特权评论家输入，并直接围绕这些量设计塑形奖励，使演员网络仅依赖本体感觉即可实现零样本硬件迁移。该策略无需参考轨迹或脚本化接触，即可处理小扰动下的踝/髋关节策略、大推力下的补偿步态，以及利用手肘膝盖的多触点倒地站立。在Isaac Lab中训练的Unitree H1-2策略，在随机初始姿态和未脚本化倒地配置下达到93.4%恢复率。消融实验表明移除平衡信息结构会导致站立学习完全失败，证实这些指标提供了有意义的训练信号而非偶然结构。

## 核心内容
### 方法架构
- **平衡指标嵌入**：将捕获点（Capture Point）、质心状态（CoM state）和质心动量（Centroidal Momentum）作为特权信息输入评论家网络，同时基于这些量设计塑形奖励函数
- **演员-评论家框架**：演员网络仅使用本体感觉（关节位置/速度、IMU数据）进行零样本硬件迁移，评论家网络在训练时获取特权平衡指标
- **无参考轨迹设计**：不依赖任何预设运动轨迹或脚本化接触序列，完全通过强化学习自主发现恢复策略

### 实验设置
- **训练环境**：Isaac Lab仿真平台，使用Unitree H1-2人形机器人模型
- **测试配置**：包含随机初始姿态（不同倒地角度/方向）和未脚本化倒地场景（模拟真实跌倒动力学）
- **迁移验证**：Sim-to-sim迁移至MuJoCo环境，以及初步硬件实验

### 关键结果
- **恢复性能**：在随机初始姿态和未脚本化倒地配置下达到93.4%恢复率
- **策略多样性**：单一策略自动涌现出踝关节策略（小扰动）、髋关节策略（中等扰动）、补偿步态（大推力）、多触点站立（利用手肘膝盖）
- **消融实验**：移除平衡信息结构后，站立学习完全失败（0%恢复率），证明这些指标提供了关键学习信号
- **泛化能力**：成功迁移至MuJoCo仿真环境，初步硬件实验验证了跨环境泛化性

### 结论
嵌入可解释的平衡结构显著减少了人形机器人处于失败状态的时间，将自主恢复的能力边界从单一站立任务扩展至包含倒地、补偿步态和多触点站立的完整恢复谱系。该方法为将经典控制理论融入现代强化学习框架提供了有效范式。

## Overview
Humanoid robots remain vulnerable to falls and unrecoverable failure states, limiting their practical utility in unstructured environments. While reinforcement learning has demonstrated stand-up behaviors, existing approaches treat recovery as a pure task-reward problem without an explicit representation of the balance state. We present a unified RL policy that addresses this limitation by embedding classical balance metrics: capture point, center-of-mass state, and centroidal momentum, as privileged critic inputs and shaping rewards directly around these quantities during training, while the actor relies solely on proprioception for zero-shot hardware transfer. Without reference trajectories or scripted contacts, a single policy spans the full recovery spectrum: ankle and hip strategies for small disturbances, corrective stepping under large pushes, and compliant falling with multi-contact stand-up using the hands, elbows, and knees. Trained on the Unitree H1-2 in Isaac Lab, the policy achieves a 93.4% recovery rate across randomized initial poses and unscripted fall configurations. An ablation study shows that removing the balance-informed structure causes stand-up learning to fail entirely, confirming that these metrics provide a meaningful learning signal rather than incidental structure. Sim-to-sim transfer to MuJoCo and preliminary hardware experiments further demonstrate cross-environment generalization. These results show that embedding interpretable balance structure into the learning framework substantially reduces time spent in failure states and broadens the envelope of autonomous recovery.

## 개요
휴머노이드 로봇은 여전히 넘어짐과 복구 불가능한 실패 상태에 취약하여, 비정형 환경에서의 실용적 유용성을 제한합니다. 강화 학습이 일어서기 행동을 입증했지만, 기존 접근법은 균형 상태에 대한 명시적 표현 없이 복구를 순수 작업-보상 문제로만 다룹니다. 우리는 이러한 한계를 해결하기 위해 고전적 균형 지표(포착점, 질량 중심 상태, 중심 운동량)를 특권 비평가 입력으로 내장하고, 훈련 중 이러한 양을 중심으로 직접 보상을 형성하는 통합 RL 정책을 제시합니다. 행위자는 제로샷 하드웨어 전이를 위해 고유 감각에만 의존합니다. 참조 궤적이나 스크립트된 접촉 없이, 단일 정책이 전체 복구 스펙트럼(작은 교란에 대한 발목 및 엉덩이 전략, 큰 밀림에 대한 교정 스텝, 손, 팔꿈치, 무릎을 사용한 다중 접촉 일어서기를 포함한 순응적 넘어짐)을 포괄합니다. Isaac Lab에서 Unitree H1-2로 훈련된 이 정책은 무작위 초기 자세와 스크립트되지 않은 넘어짐 구성에서 93.4%의 복구율을 달성합니다. 절제 연구는 균형 정보 구조를 제거하면 일어서기 학습이 완전히 실패함을 보여주며, 이 지표가 우연한 구조가 아닌 의미 있는 학습 신호를 제공함을 확인합니다. MuJoCo로의 시뮬-시뮬 전이와 예비 하드웨어 실험은 추가로 환경 간 일반화를 입증합니다. 이러한 결과는 해석 가능한 균형 구조를 학습 프레임워크에 내장하면 실패 상태에서 소요되는 시간을 크게 줄이고 자율 복구의 범위를 확장함을 보여줍니다.

## 핵심 내용
휴머노이드 로봇은 여전히 넘어짐과 복구 불가능한 실패 상태에 취약하여, 비정형 환경에서의 실용적 유용성을 제한합니다. 강화 학습이 일어서기 행동을 입증했지만, 기존 접근법은 균형 상태에 대한 명시적 표현 없이 복구를 순수 작업-보상 문제로만 다룹니다. 우리는 이러한 한계를 해결하기 위해 고전적 균형 지표(포착점, 질량 중심 상태, 중심 운동량)를 특권 비평가 입력으로 내장하고, 훈련 중 이러한 양을 중심으로 직접 보상을 형성하는 통합 RL 정책을 제시합니다. 행위자는 제로샷 하드웨어 전이를 위해 고유 감각에만 의존합니다. 참조 궤적이나 스크립트된 접촉 없이, 단일 정책이 전체 복구 스펙트럼(작은 교란에 대한 발목 및 엉덩이 전략, 큰 밀림에 대한 교정 스텝, 손, 팔꿈치, 무릎을 사용한 다중 접촉 일어서기를 포함한 순응적 넘어짐)을 포괄합니다. Isaac Lab에서 Unitree H1-2로 훈련된 이 정책은 무작위 초기 자세와 스크립트되지 않은 넘어짐 구성에서 93.4%의 복구율을 달성합니다. 절제 연구는 균형 정보 구조를 제거하면 일어서기 학습이 완전히 실패함을 보여주며, 이 지표가 우연한 구조가 아닌 의미 있는 학습 신호를 제공함을 확인합니다. MuJoCo로의 시뮬-시뮬 전이와 예비 하드웨어 실험은 추가로 환경 간 일반화를 입증합니다. 이러한 결과는 해석 가능한 균형 구조를 학습 프레임워크에 내장하면 실패 상태에서 소요되는 시간을 크게 줄이고 자율 복구의 범위를 확장함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2603.08619v1
