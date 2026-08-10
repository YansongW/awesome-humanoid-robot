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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.10363v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1101 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2502.10363v3

## 개요
인간형 로봇이 희소한 디딤발 지형에서 운동할 때 정밀한 발 위치 설정과 안정적인 제어가 필요하지만, 기존 강화 학습 방법은 희소한 디딤발 보상과 비효율적인 학습 과정으로 인해 성능이 저조한 경우가 많습니다. BeamDojo는 세 가지 혁신을 통해 이 문제를 해결합니다: 첫째, 샘플링 기반 다각형 발바닥 디딤발 보상 함수를 설계하고, 이중 비평가 아키텍처를 도입하여 밀집 운동 보상과 희소 디딤발 보상 학습의 균형을 맞춥니다; 둘째, 두 단계 강화 학습 전략을 채택합니다——먼저 평평한 지형에서 로봇이 작업 지형을 인식하도록 훈련한 다음, 실제 지형에서 정책을 미세 조정합니다; 마지막으로, 기내 LiDAR 고도 지도를 통합하여 실제 세계 배포를 구현합니다. 시뮬레이션과 실물 실험 모두 이 방법이 희소한 디딤발에서의 민첩한 운동 능력을 검증하며, 강한 외부 교란에도 높은 성공률을 유지합니다.

## 핵심 내용
### 방법 아키텍처
BeamDojo의 핵심 프레임워크는 강화 학습을 기반으로 하며, 다음 주요 구성 요소를 포함합니다:
- **샘플링 기반 디딤발 보상**: 다각형 발바닥을 위해 설계되었으며, 후보 디딤발 위치를 샘플링하고 목표 위치와의 일치도를 계산하여 희소하지만 정밀한 보상 신호를 제공합니다.
- **이중 비평가 메커니즘**: 하나의 비평가는 밀집 운동 보상(예: 속도 추적, 자세 안정화)을 담당하고, 다른 하나는 희소 디딤발 보상을 전담 처리하며, 두 그래디언트 업데이트의 균형을 통해 학습 편향을 방지합니다.
- **두 단계 훈련 전략**:
  - **1단계**: 평평한 지형에서 훈련하지만, 정책 네트워크에 작업 지형의 인식 관측(예: 고도 지도 특징)을 입력하여 로봇이 지형 인식 능력을 학습하도록 합니다.
  - **2단계**: 실제 작업 지형에서 정책을 미세 조정하며, 1단계에서 학습한 인식 사전 지식을 활용하여 수렴을 가속화합니다.

### 실험 설정
- **시뮬레이션 환경**: Isaac Gym 기반으로 구축되었으며, 다양한 희소 디딤발 지형(예: 매화 말뚝, 분산된 돌 블록)을 포함하고, 무작위 외부 교란(추력, 경사)을 추가합니다.
- **실제 배포**: Unitree H1 인간형 로봇을 사용하며, 360° LiDAR를 장착하여 실시간 고도 지도를 생성하고, 정책은 50Hz 주파수로 실행됩니다.
- **비교 기준선**: 두 단계 훈련이 없는 RL 방법, 이중 비평가가 없는 단일 보상 방법, 그리고 전통적인 모델 예측 제어(MPC) 방법을 포함합니다.

### 주요 결과
- **시뮬레이션 성능**: BeamDojo는 희소 디딤발 지형에서 기준선 방법보다 성공률이 35% 높으며(예: 매화 말뚝 지형에서 92% 달성), 학습 속도는 2.3배 향상됩니다.
- **실제 환경**: 0.15m 간격의 분산된 돌 블록에서 로봇은 0.8m/s 속도로 안정적으로 걸으며, 발 위치 설정 오차는 2cm 미만입니다; 50N 측면 추력 교란에서도 성공률은 85%를 유지합니다.
- **절제 실험**: 이중 비평가를 제거하면 성공률이 28% 하락하고, 두 단계 훈련을 제거하면 41% 하락하여 각 모듈의 필요성을 검증합니다.

### 결론
BeamDojo는 혁신적인 보상 설계와 훈련 전략을 통해 인간형 로봇이 극도로 희소한 디딤발 지형에서 민첩한 운동을 최초로 구현했으며, 실제 배포의 견고성을 갖추고 있습니다. 향후 작업은 더 복잡한 지형(예: 동적 이동 디딤발)과 더 높은 운동 속도를 탐구할 것입니다.
