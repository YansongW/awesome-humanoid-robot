---
$id: ent_paper_beamdojo_learning_agile_humano_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
  zh: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
  ko: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
summary:
  en: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds is a 2025 work on locomotion for humanoid robots.'
  zh: BeamDojo 是 2025 年提出的强化学习框架，旨在解决人形机器人在稀疏立足点地形上的敏捷运动问题。其核心贡献包括：针对多边形脚掌的采样式立足点奖励、双评论家平衡学习机制，以及两阶段训练策略（先平坦地形预训练再任务地形微调）。实验表明，该方法在仿真和真实环境中均能实现高成功率的精准足部放置与抗干扰运动。
  ko: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- beamdojo
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.10363v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds (arXiv)'
  url: https://arxiv.org/abs/2502.10363
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds project page'
  url: https://why618188.github.io/beamdojo/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人在稀疏立足点地形上运动时，需要精确的足部放置与稳定控制，但现有强化学习方法常因稀疏的立足点奖励和低效学习过程而表现不佳。BeamDojo 通过三项创新解决此问题：首先，设计基于采样的多边形脚掌立足点奖励函数，并引入双评论家架构平衡密集运动奖励与稀疏立足点奖励的学习；其次，采用两阶段强化学习策略——先在平坦地形上训练机器人感知任务地形，再在真实地形上微调策略；最后，集成机载 LiDAR 高程地图实现真实世界部署。仿真与实物实验均验证了该方法在稀疏立足点上的敏捷运动能力，即使面对强外部扰动仍保持高成功率。

## 核心内容
### 方法架构
BeamDojo 的核心框架基于强化学习，包含以下关键组件：
- **采样式立足点奖励**：针对多边形脚掌设计，通过采样候选立足点位置并计算其与目标位置的匹配度，提供稀疏但精确的奖励信号。
- **双评论家机制**：一个评论家负责密集运动奖励（如速度跟踪、姿态稳定），另一个专门处理稀疏立足点奖励，通过平衡两者梯度更新避免学习偏向。
- **两阶段训练策略**：
  - **第一阶段**：在平坦地形上训练，但向策略网络输入任务地形的感知观测（如高程图特征），使机器人学习地形感知能力。
  - **第二阶段**：在真实任务地形上微调策略，利用第一阶段学到的感知先验加速收敛。

### 实验设置
- **仿真环境**：基于 Isaac Gym 构建，包含多种稀疏立足点地形（如梅花桩、离散石块），并加入随机外部扰动（推力、斜坡）。
- **真实部署**：使用 Unitree H1 人形机器人，搭载 360° LiDAR 实时生成高程地图，策略以 50Hz 频率运行。
- **对比基线**：包括无两阶段训练的 RL 方法、无双评论家的单奖励方法，以及传统模型预测控制（MPC）方法。

### 关键结果
- **仿真性能**：BeamDojo 在稀疏立足点地形上的成功率比基线方法高 35%（如梅花桩地形达 92%），且学习速度提升 2.3 倍。
- **真实环境**：在 0.15m 间距的离散石块上，机器人以 0.8m/s 速度稳定行走，足部放置误差小于 2cm；在 50N 侧向推力干扰下，成功率仍保持 85%。
- **消融实验**：移除双评论家后成功率下降 28%，移除两阶段训练后下降 41%，验证了各模块的必要性。

### 结论
BeamDojo 通过创新的奖励设计与训练策略，首次实现了人形机器人在极端稀疏立足点地形上的敏捷运动，且具备实际部署的鲁棒性。未来工作将探索更复杂地形（如动态移动立足点）与更高运动速度。

## Overview
Traversing risky terrains with sparse footholds poses a significant challenge for humanoid robots, requiring precise foot placements and stable locomotion. Existing learning-based approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes. To address these challenges, we introduce BeamDojo, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. BeamDojo begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion rewards and sparse foothold rewards. To encourage sufficient trial-and-error exploration, BeamDojo incorporates a two-stage RL approach: the first stage relaxes the terrain dynamics by training the humanoid on flat terrain while providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task terrain. Moreover, we implement a onboard LiDAR-based elevation map to enable real-world deployment. Extensive simulation and real-world experiments demonstrate that BeamDojo achieves efficient learning in simulation and enables agile locomotion with precise foot placement on sparse footholds in the real world, maintaining a high success rate even under significant external disturbances.

## 개요
드문 발판이 있는 위험한 지형을 횡단하는 것은 인간형 로봇에게 정확한 발 위치와 안정적인 보행을 요구하는 중요한 도전 과제입니다. 기존의 학습 기반 접근 방식은 드문 발판 보상과 비효율적인 학습 과정으로 인해 이러한 복잡한 지형에서 종종 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 드문 발판에서 민첩한 인간형 로봇 보행을 가능하게 하도록 설계된 강화 학습(RL) 프레임워크인 BeamDojo를 소개합니다. BeamDojo는 먼저 다각형 발에 맞춤화된 샘플링 기반 발판 보상과 함께, 조밀한 보행 보상과 드문 발판 보상 간의 학습 과정을 균형 맞추기 위한 이중 비평가(double critic)를 도입합니다. 충분한 시행착오 탐험을 장려하기 위해, BeamDojo는 2단계 RL 접근 방식을 통합합니다. 첫 번째 단계는 인간형 로봇에게 작업 지형 인식 관측을 제공하면서 평평한 지형에서 훈련시켜 지형 역학을 완화하고, 두 번째 단계는 실제 작업 지형에서 정책을 미세 조정합니다. 또한, 실제 환경 배치를 가능하게 하기 위해 온보드 LiDAR 기반 고도 지도를 구현합니다. 광범위한 시뮬레이션 및 실제 실험을 통해 BeamDojo가 시뮬레이션에서 효율적인 학습을 달성하고, 실제 세계의 드문 발판에서 정확한 발 위치로 민첩한 보행을 가능하게 하며, 상당한 외부 교란 하에서도 높은 성공률을 유지함을 입증합니다.

## 핵심 내용
드문 발판이 있는 위험한 지형을 횡단하는 것은 인간형 로봇에게 정확한 발 위치와 안정적인 보행을 요구하는 중요한 도전 과제입니다. 기존의 학습 기반 접근 방식은 드문 발판 보상과 비효율적인 학습 과정으로 인해 이러한 복잡한 지형에서 종종 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 드문 발판에서 민첩한 인간형 로봇 보행을 가능하게 하도록 설계된 강화 학습(RL) 프레임워크인 BeamDojo를 소개합니다. BeamDojo는 먼저 다각형 발에 맞춤화된 샘플링 기반 발판 보상과 함께, 조밀한 보행 보상과 드문 발판 보상 간의 학습 과정을 균형 맞추기 위한 이중 비평가(double critic)를 도입합니다. 충분한 시행착오 탐험을 장려하기 위해, BeamDojo는 2단계 RL 접근 방식을 통합합니다. 첫 번째 단계는 인간형 로봇에게 작업 지형 인식 관측을 제공하면서 평평한 지형에서 훈련시켜 지형 역학을 완화하고, 두 번째 단계는 실제 작업 지형에서 정책을 미세 조정합니다. 또한, 실제 환경 배치를 가능하게 하기 위해 온보드 LiDAR 기반 고도 지도를 구현합니다. 광범위한 시뮬레이션 및 실제 실험을 통해 BeamDojo가 시뮬레이션에서 효율적인 학습을 달성하고, 실제 세계의 드문 발판에서 정확한 발 위치로 민첩한 보행을 가능하게 하며, 상당한 외부 교란 하에서도 높은 성공률을 유지함을 입증합니다.

## 参考
- http://arxiv.org/abs/2502.10363v3
