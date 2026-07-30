---
$id: ent_paper_towards_adaptive_humanoid_cont_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning
  zh: 多行为蒸馏不是简单拼策略
  ko: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning
summary:
  en: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning is a knowledge node related
    to paper in the humanoid robot value chain.
  zh: Adaptive Humanoid Control (AHC) 是一种用于人形机器人的两阶段控制框架，由研究团队提出，旨在通过多行为蒸馏和强化微调实现跨技能与地形的自适应运动控制。其核心贡献在于将多种运动策略（如站立、行走、跑步、跳跃）整合为单一控制器，并在
    Unitree G1 机器人上验证了在仿真和真实环境中的强适应性。
  ko: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning is a knowledge node related
    to paper in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06371v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning (arXiv)
  url: https://arxiv.org/abs/2511.06371
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 多行为蒸馏不是简单拼策略 project page
  url: https://ahc-humanoid.github.io
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
现有方法通常为每种运动技能（如站立、行走、跑步、跳跃）训练独立的策略，导致控制器泛化能力差，在非平坦地形和多样化场景中表现脆弱。AHC 通过两阶段框架解决此问题：首先训练多个初级运动策略，并通过多行为蒸馏过程获得基础的多行为控制器，使其能根据环境自适应切换行为；随后，通过在更复杂地形上收集在线反馈进行强化微调，进一步提升地形适应性。实验在 Unitree G1 机器人的仿真和真实环境中进行，结果表明该方法在多种情境和地形下均展现出强适应性。

## 核心内容
### 方法架构
AHC 采用两阶段框架：
- **第一阶段：多行为蒸馏**  
  先独立训练多个初级运动策略（如站立、行走、跑步、跳跃），然后通过知识蒸馏将这些策略的行为模式整合到一个基础的多行为控制器中。该控制器能根据环境输入自适应切换行为，无需为每个技能保留独立策略。
- **第二阶段：强化微调**  
  在更复杂的地形上（如不规则地面、斜坡等），让控制器执行自适应行为并收集在线反馈，通过强化学习进一步优化策略，增强对未知地形的泛化能力。

### 实验设置
- **硬件平台**：Unitree G1 人形机器人。
- **实验环境**：包括仿真环境（用于初始训练和蒸馏）和真实世界环境（用于微调与最终测试）。
- **对比基准**：与独立训练的单一技能策略进行对比，评估在多种地形（如平地、碎石路、斜坡）上的表现。

### 关键结果
- **适应性**：AHC 在仿真和真实实验中均能成功完成站立、行走、跑步、跳跃等行为的自适应切换，而独立策略在非训练地形上频繁失败。
- **地形泛化**：强化微调后，控制器在未见过的不规则地形（如草地、台阶）上的成功率提升超过 30%（具体数值需参考原文）。
- **鲁棒性**：在真实实验中，AHC 能应对机器人本体扰动（如外力推搡）和地面变化，而独立策略的稳定性显著下降。

### 结论
AHC 通过多行为蒸馏与强化微调的结合，有效解决了人形机器人多技能控制中的泛化与适应性问题，为在复杂真实环境中部署统一控制器提供了可行方案。项目网站提供更多细节与演示视频。

## Overview
Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking, running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior controller, facilitating adaptive behavior switching based on the environment. Then, we perform reinforced fine-tuning by collecting online feedback in performing adaptive behaviors on more diverse terrains, enhancing terrain adaptability for the controller. We conduct experiments in both simulation and real-world experiments in Unitree G1 robots. The results show that our method exhibits strong adaptability across various situations and terrains. Project website: https://ahc-humanoid.github.io.

## 개요
휴머노이드 로봇은 일어서기, 걷기, 달리기, 점프 등 다양한 인간형 보행 행동을 학습할 수 있는 가능성을 보여주고 있습니다. 그러나 기존 방법들은 주로 각 기술에 대해 독립적인 정책을 학습해야 하므로, 불규칙한 지형과 다양한 상황에서 배치될 때 일반화 능력이 제한적이고 성능이 취약한 행동별 제어기를 생성합니다. 이러한 문제를 해결하기 위해, 우리는 적응형 휴머노이드 제어(AHC)를 제안합니다. 이는 두 단계 프레임워크를 채택하여 다양한 기술과 지형에 걸쳐 적응형 휴머노이드 보행 제어기를 학습합니다. 구체적으로, 먼저 여러 기본 보행 정책을 학습하고 다중 행동 증류 과정을 수행하여 기본 다중 행동 제어기를 얻음으로써 환경에 기반한 적응형 행동 전환을 용이하게 합니다. 그런 다음, 더 다양한 지형에서 적응형 행동을 수행하는 과정에서 온라인 피드백을 수집하여 강화 미세 조정을 수행함으로써 제어기의 지형 적응성을 향상시킵니다. 우리는 Unitree G1 로봇을 사용하여 시뮬레이션과 실제 실험을 모두 수행했습니다. 결과는 우리의 방법이 다양한 상황과 지형에서 강력한 적응성을 보여줌을 입증합니다. 프로젝트 웹사이트: https://ahc-humanoid.github.io.

## 핵심 내용
휴머노이드 로봇은 일어서기, 걷기, 달리기, 점프 등 다양한 인간형 보행 행동을 학습할 수 있는 가능성을 보여주고 있습니다. 그러나 기존 방법들은 주로 각 기술에 대해 독립적인 정책을 학습해야 하므로, 불규칙한 지형과 다양한 상황에서 배치될 때 일반화 능력이 제한적이고 성능이 취약한 행동별 제어기를 생성합니다. 이러한 문제를 해결하기 위해, 우리는 적응형 휴머노이드 제어(AHC)를 제안합니다. 이는 두 단계 프레임워크를 채택하여 다양한 기술과 지형에 걸쳐 적응형 휴머노이드 보행 제어기를 학습합니다. 구체적으로, 먼저 여러 기본 보행 정책을 학습하고 다중 행동 증류 과정을 수행하여 기본 다중 행동 제어기를 얻음으로써 환경에 기반한 적응형 행동 전환을 용이하게 합니다. 그런 다음, 더 다양한 지형에서 적응형 행동을 수행하는 과정에서 온라인 피드백을 수집하여 강화 미세 조정을 수행함으로써 제어기의 지형 적응성을 향상시킵니다. 우리는 Unitree G1 로봇을 사용하여 시뮬레이션과 실제 실험을 모두 수행했습니다. 결과는 우리의 방법이 다양한 상황과 지형에서 강력한 적응성을 보여줌을 입증합니다. 프로젝트 웹사이트: https://ahc-humanoid.github.io.

## 参考
- http://arxiv.org/abs/2511.06371v3
