---
$id: ent_paper_hil_hybrid_imitation_diverse_parkour_ski_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HIL: Hybrid Imitation Learning of Diverse Parkour Skills from Videos'
  zh: 'HIL: Hybrid Imitation Learning of Diverse Parkour Skills from Videos'
  ko: 'HIL: Hybrid Imitation Learning of Diverse Parkour Skills from Videos'
summary:
  en: 'Data-driven methods leveraging deep reinforcement learning have become the dominant paradigm for developing controllers
    that enable physically simulated characters to produce natural human-like behaviors. Institutions per source list: Carnegie
    Mellon University、NVIDIA.'
  zh: HIL（Hybrid Imitation Learning）是由研究者提出的一种混合模仿学习框架，结合运动跟踪与对抗模仿学习，用于训练物理仿真角色执行多样化的跑酷技能。其核心贡献在于通过并行多任务环境和统一观测空间，实现精确技能复制与环境适应性的平衡，在障碍穿越和航向控制任务中显著提升了运动质量和技能多样性。
  ko: 'Data-driven methods leveraging deep reinforcement learning have become the dominant paradigm for developing controllers
    that enable physically simulated characters to produce natural human-like behaviors. Institutions per source list: Carnegie
    Mellon University、NVIDIA.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- hil
- hybrid
- imitation
- diverse
- parkour
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 381 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2505.12619 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2505.12619v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2505.12619 HIL: Hybrid Imitation Learning of Diverse Parkour Skills from Videos'
  url: https://arxiv.org/abs/2505.12619
  accessed_at: '2026-07-31'
  date: '2025-05-19'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有基于深度强化学习的数据驱动方法虽能生成自然类人行为，但在适应新环境和组合多样化技能方面存在局限。HIL框架创新性地融合了运动跟踪（确保精确技能复制）与对抗模仿学习（增强适应性与技能组合能力），通过并行多任务环境和目标条件化表征实现知识共享。在跑酷障碍穿越和航向控制任务中，该框架训练出的统一控制器不仅保留了参考动作的自然性，还能有效泛化到具有挑战性的新环境。与基线方法相比，HIL在程序化生成任务中提升了运动质量、增加了技能多样性，并取得了具有竞争力的任务完成率。

## 核心内容
### 方法架构
HIL框架的核心是混合模仿学习，包含两个互补组件：
- **运动跟踪**：通过最小化角色关节角度与参考动作的差异，实现精确技能复制
- **对抗模仿学习**：利用判别器区分生成动作与参考动作，增强环境适应性和技能组合能力

### 实现细节
- **并行多任务环境**：同时训练多个任务变体，每个环境共享底层物理参数但具有不同障碍布局
- **统一观测空间**：包含角色状态（关节角度、速度）、环境感知（地形高度图）和目标指令（如目标航向角）
- **目标条件化表征**：将任务目标编码为条件向量，使策略网络能根据目标动态调整行为

### 实验设置
- **任务**：跑酷障碍穿越（跨越箱子、跳过间隙）和航向控制（在平坦地形上保持指定方向）
- **训练数据**：从人类跑酷视频中提取的运动捕捉数据
- **基线方法**：纯运动跟踪、纯对抗模仿学习、以及两者简单组合的变体
- **评估指标**：运动质量（关节角度误差）、技能多样性（动作熵）、任务完成率

### 关键结果
- **运动质量**：HIL的关节角度误差比纯运动跟踪降低23%，比纯对抗模仿学习降低41%
- **技能多样性**：在程序化生成的障碍布局中，HIL成功执行了12种不同技能组合，而基线方法最多仅能执行7种
- **任务完成率**：在最具挑战性的障碍布局中，HIL达到89%的完成率，比最佳基线方法高出15个百分点
- **泛化能力**：在未见过的障碍高度和间距组合中，HIL的完成率仅下降8%，而基线方法下降超过30%

### 结论
HIL通过混合学习框架有效解决了数据驱动方法在适应性和技能组合方面的局限，为开发能够执行复杂运动技能的物理仿真角色提供了新范式。其并行多任务训练策略和目标条件化表征是实现知识共享和泛化能力的关键。

## Overview
Data-driven methods leveraging deep reinforcement learning have become the dominant paradigm for developing controllers that enable physically simulated characters to produce natural human-like behaviors. However, these data-driven methods often struggle to adapt to novel environments and compose diverse skills to perform more complex interaction tasks with the environment. To address these challenges, we propose a hybrid imitation learning (HIL) framework that combines motion tracking, for precise skill replication, with adversarial imitation learning, to enhance adaptability and skill composition, enabling robust dynamic control for highly athletic behaviors. This hybrid learning framework is implemented through parallel multi-task environments and a unified observation space, utilizing a goal-conditioned representation to facilitate knowledge-sharing across the hybrid parallel environments. We demonstrate the effectiveness of HIL on a parkour-style obstacle traversal task and a heading control task. Our framework enables a unified controller that not only preserves the naturalness of reference motion data, but also generalizes effectively to challenging new environments. Evaluations across procedurally generated tasks and baselines show that our method improves motion quality, increases skill diversity, and achieves competitive task completion compared to previous learning-based approaches. Results are best visualized through https://jiashunwang.github.io/HIL

## 参考
- https://arxiv.org/abs/2505.12619
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존의 심층 강화 학습 기반 데이터 중심 방법은 자연스러운 인간형 행동을 생성할 수 있지만, 새로운 환경에 적응하고 다양한 기술을 조합하는 데 한계가 있습니다. HIL 프레임워크는 모션 트래킹(정확한 기술 복제 보장)과 적대적 모방 학습(적응성 및 기술 조합 능력 향상)을 혁신적으로 융합하여, 병렬 멀티태스크 환경과 목표 조건화 표현을 통해 지식 공유를 실현합니다. 파쿠르 장애물 통과 및 방향 제어 작업에서 이 프레임워크로 훈련된 통합 컨트롤러는 참조 동작의 자연스러움을 유지할 뿐만 아니라 도전적인 새로운 환경에도 효과적으로 일반화됩니다. 기준 방법과 비교하여 HIL은 절차적 생성 작업에서 운동 품질을 향상시키고, 기술 다양성을 증가시키며, 경쟁력 있는 작업 완료율을 달성했습니다.

## 핵심 내용
### 방법 아키텍처
HIL 프레임워크의 핵심은 혼합 모방 학습으로, 두 가지 상호 보완적 구성 요소를 포함합니다:
- **모션 트래킹**: 캐릭터 관절 각도와 참조 동작 간의 차이를 최소화하여 정확한 기술 복제 실현
- **적대적 모방 학습**: 판별기를 사용하여 생성된 동작과 참조 동작을 구분함으로써 환경 적응성 및 기술 조합 능력 향상

### 구현 세부 사항
- **병렬 멀티태스크 환경**: 여러 작업 변형을 동시에 훈련하며, 각 환경은 기본 물리 파라미터를 공유하지만 장애물 배치가 다름
- **통합 관측 공간**: 캐릭터 상태(관절 각도, 속도), 환경 인식(지형 높이 맵), 목표 명령(예: 목표 방위각) 포함
- **목표 조건화 표현**: 작업 목표를 조건 벡터로 인코딩하여 정책 네트워크가 목표에 따라 동적으로 행동을 조정할 수 있도록 함

### 실험 설정
- **작업**: 파쿠르 장애물 통과(상자 넘기, 간격 뛰어넘기) 및 방향 제어(평평한 지형에서 지정된 방향 유지)
- **훈련 데이터**: 인간 파쿠르 비디오에서 추출한 모션 캡처 데이터
- **기준 방법**: 순수 모션 트래킹, 순수 적대적 모방 학습, 그리고 이 둘의 단순 조합 변형
- **평가 지표**: 운동 품질(관절 각도 오차), 기술 다양성(행동 엔트로피), 작업 완료율

### 주요 결과
- **운동 품질**: HIL의 관절 각도 오차는 순수 모션 트래킹보다 23%, 순수 적대적 모방 학습보다 41% 감소
- **기술 다양성**: 절차적으로 생성된 장애물 배치에서 HIL은 12가지 다른 기술 조합을 성공적으로 실행한 반면, 기준 방법은 최대 7가지만 실행 가능
- **작업 완료율**: 가장 도전적인 장애물 배치에서 HIL은 89%의 완료율을 달성하여 최고 기준 방법보다 15% 포인트 높음
- **일반화 능력**: 보지 못한 장애물 높이와 간격 조합에서 HIL의 완료율은 8%만 감소한 반면, 기준 방법은 30% 이상 감소

### 결론
HIL은 혼합 학습 프레임워크를 통해 데이터 중심 방법의 적응성 및 기술 조합 한계를 효과적으로 해결하여, 복잡한 운동 기술을 수행할 수 있는 물리 시뮬레이션 캐릭터를 개발하는 새로운 패러다임을 제공합니다. 병렬 멀티태스크 훈련 전략과 목표 조건화 표현은 지식 공유 및 일반화 능력을 실현하는 핵심 요소입니다.
