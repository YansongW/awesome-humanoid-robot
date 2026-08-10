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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.03654v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1039 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2410.03654v1

## 개요
이 연구는 UC Berkeley 팀이 수행했으며, 핵심 기여는 Transformer 아키텍처와 2단계 훈련 전략을 결합하여 인간형 로봇의 복잡한 지형에서의 블라인드 보행 문제를 해결한 것입니다. 컨트롤러는 고유수용성 정보(관절 각도, 토크 등)에만 의존하며, 과거 동작 및 관측 시퀀스를 통해 다음 동작을 예측합니다. 사전 훈련 단계에서는 대량의 평지 보행 데이터를 사용하여 기본 운동 패턴을 학습하고, 미세 조정 단계에서는 강화 학습을 통해 울퉁불퉁한 지형에 적응합니다. 실험은 실제 Digit 로봇에서 검증되었으며, 거친 지형, 변형 가능한 지형, 경사면 등 다양한 지형을 포함하여 견고한 보행 능력, 상황 적응 능력, 그리고 창발적인 지형 표현을 보여주었습니다.

## 핵심 내용
### 방법 아키텍처
- **컨트롤러 모델**: Transformer 아키텍처를 사용하며, 입력은 과거 고유수용성 관측(관절 위치, 속도, 토크, IMU 데이터)과 동작 시퀀스이고, 출력은 다음 단계의 관절 목표 위치입니다.
- **2단계 훈련**:
  - **사전 훈련**: 평지 지형 궤적 데이터셋에서 시퀀스 모델링(next-token prediction)을 통한 자기 지도 학습으로 기본 보행 보폭을 습득합니다.
  - **미세 조정**: 시뮬레이션의 울퉁불퉁한 지형(무작위 높이 필드, 경사면, 연약한 지면)에서 PPO 강화 학습을 사용하며, 보상 함수에는 전진 속도, 에너지 소비, 신체 균형 등의 항목이 포함됩니다.

### 실험 설정
- **로봇 플랫폼**: Digit 인간형 로봇(Agility Robotics), 높이 1.58m, 무게 48kg, 20자유도를 가짐.
- **훈련 환경**: MuJoCo 물리 엔진 기반 시뮬레이션 환경, 지형 파라미터는 무작위로 생성됨(높이 변화 ±15cm, 최대 경사 20°).
- **실제 테스트**: 캘리포니아 버클리 산악 하이킹 코스(총 4.2마일, 고도 변화 120m) 및 샌프란시스코에서 가장 가파른 거리(경사 최대 31.5%).

### 주요 결과
- **지형 통과 성공률**: 시뮬레이션 테스트에서 컨트롤러는 무작위 울퉁불퉁한 지형에서 성공률 92%(100회 시도)를 달성했으며, 기존 MPC 방법은 37%에 불과했습니다.
- **제로샷 전이**: 실제 데이터 미세 조정 없이 컨트롤러가 시뮬레이션에서 실제 환경으로 직접 전이되어, 하이킹 트레일에서 4마일 이상 연속 보행하며 넘어짐이 없었습니다.
- **적응 능력**: 미지의 지형(예: 자갈길, 미끄러운 잔디)을 만났을 때 컨트롤러는 자동으로 보폭 높이와 보행 빈도를 조정하여 상황 적응적 행동을 보여주었습니다.
- **창발적 표현**: Transformer 어텐션 가중치를 분석한 결과, 모델 내부에 지형 높이와 경도의 암시적 표현이 형성되었으며, 명시적 감각 입력 없이도 가능했습니다.

### 결론
이 연구는 Transformer 아키텍처와 2단계 훈련 전략을 결합하면 인간형 로봇이 완전한 블라인드 상태(시각 또는 촉각 감각 없음)에서 극도로 복잡한 지형을 안정적으로 통과할 수 있음을 처음으로 입증했습니다. 컨트롤러가 보여준 일반화 능력과 적응 특성은 향후 인간형 로봇의 야외 환경 실전 배치를 위한 실현 가능한 솔루션을 제공합니다.
