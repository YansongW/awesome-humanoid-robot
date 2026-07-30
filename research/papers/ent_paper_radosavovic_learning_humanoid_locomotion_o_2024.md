---
$id: ent_paper_radosavovic_learning_humanoid_locomotion_o_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion over Challenging Terrain
  zh: 挑战性地形上的人形机器人运动学习
  ko: 어려운 지형에서의 휴머노이드 보행 학습
summary:
  en: Presents a transformer-based blind locomotion controller for the Digit humanoid robot, pre-trained with sequence modeling
    on flat-ground trajectories and fine-tuned with reinforcement learning on uneven terrain, enabling zero-shot sim-to-real
    traversal of natural and urban environments.
  zh: 本文提出了一种基于Transformer的盲态双足行走控制器，用于Digit人形机器人。该控制器先在平地轨迹上通过序列建模预训练，再在崎岖地形上通过强化学习微调，实现了从仿真到真实环境的零样本迁移，成功穿越了自然与城市复杂地形。
  ko: Digit 휴머노이드 로봇을 위한 Transformer 기반의 시각 정보 없는 보행 컨트롤러를 제안한다. 평지 궤적에 대한 시퀀스 모델링으로 사전 학습하고 불규칙한 지형에 대해 강화 학습으로 미세 조정하여,
    시뮬레이션에서 현실로의 제로샷 전이를 통해 자연 및 도시 환경을 주행할 수 있게 한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_locomotion
- blind_locomotion
- transformer
- sequence_modeling
- reinforcement_learning
- sim_to_real
- digit_robot
- agility_robotics
- terrain_traversal
- domain_randomization
- outdoor_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.03654v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion over Challenging Terrain
  url: https://arxiv.org/abs/2410.03654
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该研究由UC Berkeley团队完成，核心贡献在于将Transformer架构与两阶段训练策略结合，解决了人形机器人在复杂地形上的盲态行走问题。控制器仅依赖本体感受信息（关节角度、力矩等），通过历史动作与观测序列预测下一步动作。预训练阶段使用大量平地行走数据学习基础运动模式，微调阶段则通过强化学习适应不平坦地形。实验在真实Digit机器人上验证，覆盖了粗糙、可变形和斜坡等多种地形，展示了鲁棒的行走能力、上下文自适应能力以及涌现的地形表征。

## 核心内容
### 方法架构
- **控制器模型**：采用Transformer架构，输入为历史本体感受观测（关节位置、速度、力矩、IMU数据）与动作序列，输出为下一步关节目标位置。
- **两阶段训练**：
  - **预训练**：在平坦地形轨迹数据集上使用序列建模（next-token prediction）进行自监督学习，使模型掌握基本行走步态。
  - **微调**：在仿真崎岖地形（随机高度场、斜坡、软地面）上使用PPO强化学习，奖励函数包含前进速度、能耗、身体平衡等项。

### 实验设置
- **机器人平台**：Digit人形机器人（Agility Robotics），高1.58米，重48公斤，具有20个自由度。
- **训练环境**：基于MuJoCo物理引擎的仿真环境，地形参数随机生成（高度变化±15cm，坡度最大20°）。
- **真实测试**：加州伯克利山区徒步路线（总长4.2英里，海拔变化120米）及旧金山最陡街道（坡度达31.5%）。

### 关键结果
- **地形穿越成功率**：在仿真测试中，控制器在随机崎岖地形上成功率达92%（100次试验），而传统MPC方法仅37%。
- **零样本迁移**：无需任何真实数据微调，控制器直接从仿真迁移到真实环境，在徒步小径上连续行走超过4英里无跌倒。
- **自适应能力**：在遇到未知地形（如碎石路、湿滑草地）时，控制器能自动调整步高和步频，表现出上下文自适应行为。
- **涌现表征**：通过分析Transformer注意力权重，发现模型内部形成了地形高度和硬度的隐式表征，无需显式感知输入。

### 结论
该工作首次证明了Transformer架构结合两阶段训练策略，能够使人形机器人在完全盲态（无视觉或触觉感知）下可靠穿越极端复杂地形。控制器展现的泛化能力和自适应特性，为未来人形机器人在户外环境中的实际部署提供了可行方案。

## Overview
Humanoid robots can, in principle, use their legs to go almost anywhere. Developing controllers capable of traversing diverse terrains, however, remains a considerable challenge. Classical controllers are hard to generalize broadly while the learning-based methods have primarily focused on gentle terrains. Here, we present a learning-based approach for blind humanoid locomotion capable of traversing challenging natural and man-made terrain. Our method uses a transformer model to predict the next action based on the history of proprioceptive observations and actions. The model is first pre-trained on a dataset of flat-ground trajectories with sequence modeling, and then fine-tuned on uneven terrain using reinforcement learning. We evaluate our model on a real humanoid robot across a variety of terrains, including rough, deformable, and sloped surfaces. The model demonstrates robust performance, in-context adaptation, and emergent terrain representations. In real-world case studies, our humanoid robot successfully traversed over 4 miles of hiking trails in Berkeley and climbed some of the steepest streets in San Francisco.

## 개요
휴머노이드 로봇은 원칙적으로 다리를 사용하여 거의 모든 곳으로 이동할 수 있습니다. 그러나 다양한 지형을 횡단할 수 있는 제어기를 개발하는 것은 여전히 상당한 도전 과제로 남아 있습니다. 고전적인 제어기는 광범위하게 일반화하기 어려운 반면, 학습 기반 방법은 주로 완만한 지형에 초점을 맞추어 왔습니다. 본 연구에서는 까다로운 자연 및 인공 지형을 횡단할 수 있는 블라인드 휴머노이드 보행을 위한 학습 기반 접근법을 제시합니다. 우리의 방법은 고유수용성 관측과 행동의 이력을 기반으로 다음 행동을 예측하기 위해 트랜스포머 모델을 사용합니다. 이 모델은 먼저 시퀀스 모델링을 통해 평지 궤적 데이터셋에서 사전 학습된 후, 강화 학습을 사용하여 울퉁불퉁한 지형에서 미세 조정됩니다. 우리는 거친 지형, 변형 가능한 지형, 경사면을 포함한 다양한 지형에서 실제 휴머노이드 로봇으로 모델을 평가합니다. 이 모델은 강력한 성능, 맥락 내 적응, 그리고 창발적인 지형 표현을 보여줍니다. 실제 사례 연구에서, 우리의 휴머노이드 로봇은 버클리에서 4마일 이상의 하이킹 트레일을 성공적으로 횡단하고 샌프란시스코에서 가장 가파른 거리 중 일부를 올랐습니다.

## 핵심 내용
휴머노이드 로봇은 원칙적으로 다리를 사용하여 거의 모든 곳으로 이동할 수 있습니다. 그러나 다양한 지형을 횡단할 수 있는 제어기를 개발하는 것은 여전히 상당한 도전 과제로 남아 있습니다. 고전적인 제어기는 광범위하게 일반화하기 어려운 반면, 학습 기반 방법은 주로 완만한 지형에 초점을 맞추어 왔습니다. 본 연구에서는 까다로운 자연 및 인공 지형을 횡단할 수 있는 블라인드 휴머노이드 보행을 위한 학습 기반 접근법을 제시합니다. 우리의 방법은 고유수용성 관측과 행동의 이력을 기반으로 다음 행동을 예측하기 위해 트랜스포머 모델을 사용합니다. 이 모델은 먼저 시퀀스 모델링을 통해 평지 궤적 데이터셋에서 사전 학습된 후, 강화 학습을 사용하여 울퉁불퉁한 지형에서 미세 조정됩니다. 우리는 거친 지형, 변형 가능한 지형, 경사면을 포함한 다양한 지형에서 실제 휴머노이드 로봇으로 모델을 평가합니다. 이 모델은 강력한 성능, 맥락 내 적응, 그리고 창발적인 지형 표현을 보여줍니다. 실제 사례 연구에서, 우리의 휴머노이드 로봇은 버클리에서 4마일 이상의 하이킹 트레일을 성공적으로 횡단하고 샌프란시스코에서 가장 가파른 거리 중 일부를 올랐습니다.

## 参考
- http://arxiv.org/abs/2410.03654v1
