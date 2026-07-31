---
$id: ent_paper_dit4dit_jointly_modeling_video_dynamics_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control'
  zh: 'DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control'
  ko: 'DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control'
summary:
  en: 'Vision-Language-Action (VLA) models have emerged as a promising paradigm for robot learning, but their representations
    are still largely inherited from static image-text pretraining, leaving physical dynamics to be learned from comparatively
    limited action data. Institutions per source list: Mondo Robotics（摩多机器人）、香港科技大学（广州）、香港科技大学.'
  zh: DiT4DiT 是一个端到端的视频-动作模型，由北京大学等机构提出，核心贡献在于将视频扩散 Transformer 与动作扩散 Transformer 级联，利用视频生成过程的中间去噪特征作为动作预测的时序条件。该模型在 LIBERO
    和 RoboCasa GR1 基准上达到 98.6% 和 50.8% 的平均成功率，且训练数据量大幅减少，样本效率提升超 10 倍，收敛速度加快 7 倍。
  ko: 'Vision-Language-Action (VLA) models have emerged as a promising paradigm for robot learning, but their representations
    are still largely inherited from static image-text pretraining, leaving physical dynamics to be learned from comparatively
    limited action data. Institutions per source list: Mondo Robotics（摩多机器人）、香港科技大学（广州）、香港科技大学.'
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
- dit4dit
- jointly
- modeling
- video
- dynamics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 347 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2603.10448 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2603.10448v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.10448 DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control'
  url: https://arxiv.org/abs/2603.10448
  accessed_at: '2026-07-31'
  date: '2026-03-11'
- id: src_002
  type: website
  title: Project page
  url: https://dit4dit.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://github.com/Mondo-Robotics/DiT4DiT
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有视觉-语言-动作模型多继承自静态图文预训练，对物理动力学的学习依赖有限的动作数据。DiT4DiT 创新性地将视频生成模型作为机器人策略学习的有效基础，通过耦合视频扩散 Transformer 与动作扩散 Transformer，在统一级联框架中提取视频生成过程的中间去噪特征，而非直接使用重建的未来帧。该模型采用双流匹配目标，为视频预测、隐藏状态提取和动作推理分别设置解耦的时间步与噪声尺度，实现两个模块的联合训练。在仿真和真实世界基准测试中，DiT4DiT 以更少训练数据取得领先性能，并在 Unitree G1 机器人上展现出优异的零样本泛化能力。

## 核心内容
### 方法架构
DiT4DiT 采用级联框架，包含两个核心模块：
- **视频扩散 Transformer (Video Diffusion Transformer)**：负责生成视频预测，其内部中间层的去噪特征被提取为时序条件。
- **动作扩散 Transformer (Action Diffusion Transformer)**：接收上述时序条件，用于预测机器人动作序列。
- 关键创新在于不依赖重建的未来帧，而是利用视频生成过程中的隐藏状态作为动作预测的“时序锚点”，从而更直接地捕捉物理动力学。

### 训练目标
- 提出**双流匹配目标 (dual flow-matching objective)**，为视频预测和动作推理分别设置解耦的时间步与噪声尺度。
- 视频预测模块和动作推理模块通过共享的隐藏状态提取过程实现联合训练，无需分阶段优化。

### 实验设置与关键数字
- **仿真基准**：
  - **LIBERO**：平均成功率 98.6%，训练数据量显著少于对比方法。
  - **RoboCasa GR1**：平均成功率 50.8%，同样在数据效率上表现突出。
- **真实世界基准**：
  - **Unitree G1 机器人**：实现优越的真实世界性能，并展现出强零样本泛化能力（无需微调即可适应新场景）。
- **效率提升**：
  - 样本效率提升超过 10 倍（即达到相同性能所需训练数据减少 90% 以上）。
  - 收敛速度加快高达 7 倍（训练轮次或时间大幅缩短）。

### 结论
DiT4DiT 证明视频生成可以作为机器人策略学习的有效缩放代理，通过利用视频模型固有的时空结构与隐式物理知识，显著降低对大规模动作数据的依赖。代码与模型已开源。

## Overview
Vision-Language-Action (VLA) models have emerged as a promising paradigm for robot learning, but their representations are still largely inherited from static image-text pretraining, leaving physical dynamics to be learned from comparatively limited action data. Generative video models, by contrast, encode rich spatiotemporal structure and implicit physics, making them a compelling foundation for robotic manipulation. But their potentials are not fully explored in the literature. To bridge the gap, we introduce DiT4DiT, an end-to-end Video-Action Model that couples a video Diffusion Transformer with an action Diffusion Transformer in a unified cascaded framework. Instead of relying on reconstructed future frames, DiT4DiT extracts intermediate denoising features from the video generation process and uses them as temporally grounded conditions for action prediction. We further propose a dual flow-matching objective with decoupled timesteps and noise scales for video prediction, hidden-state extraction, and action inference, enabling coherent joint training of both modules. Across simulation and real-world benchmarks, DiT4DiT achieves state-of-the-art results, reaching average success rates of 98.6% on LIBERO and 50.8% on RoboCasa GR1 while using substantially less training data. On the Unitree G1 robot, it also delivers superior real-world performance and strong zero-shot generalization. Importantly, DiT4DiT improves sample efficiency by over 10x and speeds up convergence by up to 7x, demonstrating that video generation can serve as an effective scaling proxy for robot policy learning. We release code and models at https://dit4dit.github.io/.

## 参考
- https://arxiv.org/abs/2603.10448
- https://dit4dit.github.io/
- https://github.com/Mondo-Robotics/DiT4DiT
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존의 시각-언어-행동 모델은 대부분 정적 이미지-텍스트 사전 학습에서 파생되었으며, 물리적 역학 학습은 제한된 행동 데이터에 의존합니다. DiT4DiT는 비디오 생성 모델을 로봇 정책 학습의 효과적인 기반으로 혁신적으로 활용하며, 비디오 확산 Transformer와 행동 확산 Transformer를 결합하여 통합된 계단식 프레임워크에서 비디오 생성 과정의 중간 잡음 제거 특징을 추출합니다. 이는 재구성된 미래 프레임을 직접 사용하는 대신에 이루어집니다. 해당 모델은 이중 흐름 매칭 목표를 채택하여 비디오 예측, 은닉 상태 추출 및 행동 추론을 위해 각각 분리된 시간 단계와 잡음 척도를 설정함으로써 두 모듈의 공동 훈련을 실현합니다. 시뮬레이션 및 실제 세계 벤치마크에서 DiT4DiT는 더 적은 훈련 데이터로 최고 성능을 달성했으며, Unitree G1 로봇에서 뛰어난 제로샷 일반화 능력을 보여주었습니다.

## 핵심 내용
### 방법 아키텍처
DiT4DiT는 계단식 프레임워크를 채택하며, 두 가지 핵심 모듈로 구성됩니다:
- **비디오 확산 Transformer (Video Diffusion Transformer)**: 비디오 예측을 생성하며, 내부 중간 계층의 잡음 제거 특징이 시간적 조건으로 추출됩니다.
- **행동 확산 Transformer (Action Diffusion Transformer)**: 위의 시간적 조건을 수신하여 로봇 행동 시퀀스를 예측하는 데 사용됩니다.
- 핵심 혁신은 재구성된 미래 프레임에 의존하지 않고, 비디오 생성 과정의 은닉 상태를 행동 예측을 위한 "시간적 앵커"로 활용하여 물리적 역학을 더 직접적으로 포착하는 데 있습니다.

### 훈련 목표
- **이중 흐름 매칭 목표 (dual flow-matching objective)**를 제안하여 비디오 예측과 행동 추론을 위해 각각 분리된 시간 단계와 잡음 척도를 설정합니다.
- 비디오 예측 모듈과 행동 추론 모듈은 공유된 은닉 상태 추출 과정을 통해 공동 훈련되며, 단계별 최적화가 필요하지 않습니다.

### 실험 설정 및 주요 수치
- **시뮬레이션 벤치마크**:
  - **LIBERO**: 평균 성공률 98.6%, 비교 방법보다 훈련 데이터 양이 현저히 적습니다.
  - **RoboCasa GR1**: 평균 성공률 50.8%, 데이터 효율성에서도 두드러진 성과를 보입니다.
- **실제 세계 벤치마크**:
  - **Unitree G1 로봇**: 우수한 실제 세계 성능을 달성하고, 강력한 제로샷 일반화 능력(미세 조정 없이 새로운 시나리오에 적응)을 보여줍니다.
- **효율성 향상**:
  - 샘플 효율성이 10배 이상 향상됨(즉, 동일한 성능을 달성하는 데 필요한 훈련 데이터가 90% 이상 감소).
  - 수렴 속도가 최대 7배 빨라짐(훈련 에폭 또는 시간이 크게 단축).

### 결론
DiT4DiT는 비디오 생성이 로봇 정책 학습의 효과적인 스케일링 대리자 역할을 할 수 있음을 증명하며, 비디오 모델의 고유한 시공간 구조와 암시적 물리 지식을 활용하여 대규모 행동 데이터에 대한 의존성을 크게 줄입니다. 코드와 모델은 오픈소스로 공개되었습니다.
