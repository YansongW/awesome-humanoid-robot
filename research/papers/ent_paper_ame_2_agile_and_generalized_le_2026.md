---
$id: ent_paper_ame_2_agile_and_generalized_le_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
  zh: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
  ko: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
summary:
  en: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding is a 2026 work on locomotion
    for humanoid robots.'
  zh: AME-2 是 2026 年提出的一种基于注意力机制神经地图编码的强化学习框架，用于实现双足与四足机器人的敏捷且泛化的腿部运动。其核心贡献在于设计了一个可解释的注意力地图编码器，并结合了能处理噪声与遮挡的不确定性感知地图构建管线，显著提升了机器人在复杂地形上的运动能力。
  ko: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding is a 2026 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ame_2
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.08485v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (799 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding (arXiv)'
  url: https://arxiv.org/abs/2601.08485
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
AME-2 旨在解决现有腿部运动方法中敏捷性与泛化性难以兼得的问题。该框架通过一个新颖的注意力机制地图编码器，从局部与全局地图特征中提取关键信息，生成可解释且泛化的嵌入向量供强化学习策略使用。同时，它配套提出了一种基于学习的快速地图构建管线，该管线能将深度观测转换为带有不确定性的局部高程图，并融合里程计信息，从而在遮挡和噪声下提供鲁棒的地形表示。通过在四足和双足机器人上的仿真与真实世界实验，AME-2 验证了其在未见地形上兼具敏捷运动能力与强泛化性的优势。

## 核心内容
### 方法架构
AME-2 是一个统一的强化学习框架，其核心创新在于控制策略中集成了**注意力机制地图编码器**。该编码器首先提取局部与全局的地图特征，随后利用注意力机制聚焦于地形中的关键区域（如稀疏的落脚点），从而生成一个可解释且泛化的嵌入向量，用于驱动 RL 控制策略。

### 地图构建管线
为了向策略提供高质量的输入，AME-2 提出了一套**基于学习的地图构建管线**：
- 该管线使用神经网络将深度观测数据转换为局部高程图，并同时输出每个高程估计的**不确定性**。
- 通过融合里程计信息，该管线能生成对噪声和视觉遮挡具有鲁棒性的地形表示。
- 该管线被设计为可与并行仿真环境集成，使得控制器能够在**在线地图构建**的条件下进行训练，从而有效促进 sim-to-real 迁移。

### 实验设置与结果
- **机器人平台**：验证实验在四足机器人（quadruped）和双足机器人（biped）上同时进行。
- **实验环境**：包括仿真环境和真实世界实验，测试地形均为训练中未见的复杂地形。
- **关键表现**：基于 AME-2 框架训练出的控制器在两种机器人平台上均展现出**强大的敏捷性**（如跑酷动作）和**优秀的泛化能力**，能够成功应对仿真与真实世界中未见过的新地形。

## Overview
Achieving agile and generalized legged locomotion across terrains requires tight integration of perception and control, especially under occlusions and sparse footholds. Existing methods have demonstrated agility on parkour courses but often rely on end-to-end sensorimotor models with limited generalization and interpretability. By contrast, methods targeting generalized locomotion typically exhibit limited agility and struggle with visual occlusions. We introduce AME-2, a unified reinforcement learning (RL) framework for agile and generalized locomotion that incorporates a novel attention-based map encoder in the control policy. This encoder extracts local and global mapping features and uses attention mechanisms to focus on salient regions, producing an interpretable and generalized embedding for RL-based control. We further propose a learning-based mapping pipeline that provides fast, uncertainty-aware terrain representations robust to noise and occlusions, serving as policy inputs. It uses neural networks to convert depth observations into local elevations with uncertainties, and fuses them with odometry. The pipeline also integrates with parallel simulation so that we can train controllers with online mapping, aiding sim-to-real transfer. We validate AME-2 with the proposed mapping pipeline on a quadruped and a biped robot, and the resulting controllers demonstrate strong agility and generalization to unseen terrains in simulation and in real-world experiments.

## 参考
- http://arxiv.org/abs/2601.08485v2

## 개요
AME-2는 기존 보행 운동 방법에서 민첩성과 일반화 능력을 동시에 확보하기 어려운 문제를 해결하는 것을 목표로 합니다. 이 프레임워크는 새로운 어텐션 메커니즘 지도 인코더를 통해 로컬 및 글로벌 지도 특징에서 핵심 정보를 추출하고, 강화 학습 정책에 사용할 해석 가능하고 일반화된 임베딩 벡터를 생성합니다. 동시에, 깊이 관측을 불확실성을 포함한 로컬 고도 지도로 변환하고 오도메트리 정보를 융합하여 폐색과 노이즈 하에서도 강건한 지형 표현을 제공하는 학습 기반의 빠른 지도 구축 파이프라인을 제안합니다. 사족 보행 로봇과 이족 보행 로봇에서의 시뮬레이션 및 실제 세계 실험을 통해 AME-2는 미지의 지형에서 민첩한 운동 능력과 강력한 일반화 능력을 동시에 갖추는 이점을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
AME-2는 통합 강화 학습 프레임워크로, 핵심 혁신은 제어 정책에 **어텐션 메커니즘 지도 인코더**를 통합한 점입니다. 이 인코더는 먼저 로컬 및 글로벌 지도 특징을 추출한 후, 어텐션 메커니즘을 활용하여 지형의 핵심 영역(예: 희소한 착지 지점)에 집중함으로써 RL 제어 정책을 구동하는 해석 가능하고 일반화된 임베딩 벡터를 생성합니다.

### 지도 구축 파이프라인
정책에 고품질 입력을 제공하기 위해 AME-2는 **학습 기반 지도 구축 파이프라인**을 제안합니다:
- 이 파이프라인은 신경망을 사용하여 깊이 관측 데이터를 로컬 고도 지도로 변환하고, 동시에 각 고도 추정의 **불확실성**을 출력합니다.
- 오도메트리 정보를 융합함으로써, 이 파이프라인은 노이즈와 시각적 폐색에 강건한 지형 표현을 생성할 수 있습니다.
- 이 파이프라인은 병렬 시뮬레이션 환경과 통합되도록 설계되어, 컨트롤러가 **온라인 지도 구축** 조건에서 훈련될 수 있으며, 이를 통해 sim-to-real 전이를 효과적으로 촉진합니다.

### 실험 설정 및 결과
- **로봇 플랫폼**: 검증 실험은 사족 보행 로봇(quadruped)과 이족 보행 로봇(biped)에서 동시에 수행되었습니다.
- **실험 환경**: 시뮬레이션 환경과 실제 세계 실험을 포함하며, 테스트 지형은 모두 훈련 중에 보지 못한 복잡한 지형입니다.
- **주요 성과**: AME-2 프레임워크 기반으로 훈련된 컨트롤러는 두 로봇 플랫폼 모두에서 **강력한 민첩성**(예: 파쿠르 동작)과 **우수한 일반화 능력**을 보여주며, 시뮬레이션과 실제 세계에서 보지 못한 새로운 지형을 성공적으로 처리했습니다.
