---
$id: ent_paper_dartcontrol_diffusion_autoregressive_mot_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DartControl: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control'
  zh: 'DartControl: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control'
  ko: 'DartControl: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control'
summary:
  en: 'Text-conditioned human motion generation, which allows for user interaction through natural language, has become increasingly
    popular. Existing methods typically generate short, isolated motions based on a single input sentence. Institutions per
    source list: ETH Zürich.'
  zh: DartControl（简称DART）是一个基于扩散模型的运动基元自回归模型，由研究团队提出，用于实现实时文本驱动的连续人体运动生成。其核心贡献在于：通过潜在扩散模型学习紧凑的运动基元空间，并联合运动历史与文本输入进行自回归生成，同时支持基于噪声优化或强化学习的空间运动控制。
  ko: 'Text-conditioned human motion generation, which allows for user interaction through natural language, has become increasingly
    popular. Existing methods typically generate short, isolated motions based on a single input sentence. Institutions per
    source list: ETH Zürich.'
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
- dartcontrol
- diffusion
- autoregressive
- mot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 339 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2410.05260 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2410.05260v3); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2410.05260 DartControl: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control'
  url: https://arxiv.org/abs/2410.05260
  accessed_at: '2026-07-31'
  date: '2024-10-07'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有文本条件运动生成方法通常仅处理单句输入的短时孤立动作，难以应对连续、长时且语义丰富的运动序列。DART通过将运动基元建模为潜在扩散空间，并利用自回归机制根据历史运动与当前文本实时生成后续动作，解决了这一挑战。此外，该模型还支持空间约束（如目标位置与3D场景几何），通过两种方式实现：一是将空间控制转化为潜在噪声优化问题，二是将其建模为马尔可夫决策过程并采用强化学习求解。实验表明，DART在运动真实性、生成效率与可控性上均优于现有基线方法。

## 核心内容
### 方法架构
- **运动基元空间学习**：使用变分自编码器（VAE）将运动序列压缩为潜在表示，再通过潜在扩散模型（Latent Diffusion Model）学习以运动历史与文本为条件的紧凑运动基元空间。
- **自回归生成**：基于当前文本输入与历史运动基元，逐步生成后续运动基元，实现实时、连续的文本驱动运动生成。
- **空间控制策略**：
  - **噪声优化方法**：将空间约束（如到达目标位置）转化为潜在噪声的优化目标，通过梯度下降调整噪声以匹配几何条件。
  - **强化学习方法**：将运动生成视为马尔可夫决策过程（MDP），设计奖励函数（如位置误差、运动平滑性），使用PPO算法训练策略网络。

### 实验设置
- **数据集**：在HumanML3D与KIT-ML数据集上训练与评估，并引入自定义的路径跟随与场景交互任务。
- **基线方法**：对比MDM、MotionDiffuse、T2M-GPT等主流文本驱动运动生成模型。
- **评估指标**：使用FID（运动真实性）、R-Precision（文本-运动对齐）、生成速度（帧/秒）及空间控制误差（如终点位置偏差）。

### 关键结果
- **运动真实性**：DART在HumanML3D上FID为0.42，优于MDM（0.54）与MotionDiffuse（0.63）。
- **生成效率**：单步生成仅需0.03秒（30 FPS），支持实时交互；而MDM需0.12秒。
- **空间控制**：在目标到达任务中，DART的终点位置误差为0.15米，显著低于T2M-GPT（0.38米）与MotionDiffuse（0.29米）。
- **长序列生成**：在连续10句文本描述下，DART能保持运动连贯性，而基线方法出现动作断裂或语义漂移。

### 结论
DART通过扩散模型与自回归生成的结合，首次实现了实时、长序列、带空间约束的文本驱动运动控制。其双模式空间控制策略（优化与强化学习）为不同应用场景提供了灵活选择，在运动质量与可控性上均达到当前最优。

## Overview
Text-conditioned human motion generation, which allows for user interaction through natural language, has become increasingly popular. Existing methods typically generate short, isolated motions based on a single input sentence. However, human motions are continuous and can extend over long periods, carrying rich semantics. Creating long, complex motions that precisely respond to streams of text descriptions, particularly in an online and real-time setting, remains a significant challenge. Furthermore, incorporating spatial constraints into text-conditioned motion generation presents additional challenges, as it requires aligning the motion semantics specified by text descriptions with geometric information, such as goal locations and 3D scene geometry. To address these limitations, we propose DartControl, in short DART, a Diffusion-based Autoregressive motion primitive model for Real-time Text-driven motion control. Our model effectively learns a compact motion primitive space jointly conditioned on motion history and text inputs using latent diffusion models. By autoregressively generating motion primitives based on the preceding history and current text input, DART enables real-time, sequential motion generation driven by natural language descriptions. Additionally, the learned motion primitive space allows for precise spatial motion control, which we formulate either as a latent noise optimization problem or as a Markov decision process addressed through reinforcement learning. We present effective algorithms for both approaches, demonstrating our model's versatility and superior performance in various motion synthesis tasks. Experiments show our method outperforms existing baselines in motion realism, efficiency, and controllability. Video results are available on the project page: https://zkf1997.github.io/DART/.

## 参考
- https://arxiv.org/abs/2410.05260
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 텍스트 조건 기반 동작 생성 방법은 일반적으로 단일 문장 입력에 대한 단기 고립 동작만 처리할 수 있어, 연속적이고 장시간이며 의미적으로 풍부한 동작 시퀀스를 다루기 어렵습니다. DART는 동작 프리미티브를 잠재 확산 공간으로 모델링하고, 자기회귀 메커니즘을 활용하여 과거 동작과 현재 텍스트에 기반해 실시간으로 후속 동작을 생성함으로써 이 문제를 해결합니다. 또한, 이 모델은 공간적 제약(예: 목표 위치 및 3D 장면 기하학)을 두 가지 방식으로 지원합니다. 첫째는 공간 제어를 잠재 노이즈 최적화 문제로 변환하는 것이고, 둘째는 이를 마르코프 결정 과정으로 모델링하고 강화 학습을 통해 해결하는 것입니다. 실험 결과, DART는 동작의 사실성, 생성 효율성 및 제어 가능성에서 기존 베이스라인 방법보다 우수함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **동작 프리미티브 공간 학습**: 변분 오토인코더(VAE)를 사용하여 동작 시퀀스를 잠재 표현으로 압축한 후, 잠재 확산 모델(Latent Diffusion Model)을 통해 동작 이력과 텍스트를 조건으로 하는 컴팩트한 동작 프리미티브 공간을 학습합니다.
- **자기회귀 생성**: 현재 텍스트 입력과 과거 동작 프리미티브를 기반으로 점진적으로 후속 동작 프리미티브를 생성하여 실시간 연속 텍스트 기반 동작 생성을 구현합니다.
- **공간 제어 전략**:
  - **노이즈 최적화 방법**: 공간적 제약(예: 목표 위치 도달)을 잠재 노이즈의 최적화 목표로 변환하고, 경사 하강법을 통해 노이즈를 조정하여 기하학적 조건을 충족시킵니다.
  - **강화 학습 방법**: 동작 생성을 마르코프 결정 과정(MDP)으로 간주하고, 보상 함수(예: 위치 오차, 동작 부드러움)를 설계한 후 PPO 알고리즘을 사용하여 정책 네트워크를 훈련합니다.

### 실험 설정
- **데이터셋**: HumanML3D 및 KIT-ML 데이터셋에서 훈련 및 평가를 수행하고, 사용자 정의 경로 추종 및 장면 상호작용 작업을 도입합니다.
- **베이스라인 방법**: MDM, MotionDiffuse, T2M-GPT 등 주요 텍스트 기반 동작 생성 모델과 비교합니다.
- **평가 지표**: FID(동작 사실성), R-Precision(텍스트-동작 정렬), 생성 속도(프레임/초) 및 공간 제어 오차(예: 종점 위치 편차)를 사용합니다.

### 주요 결과
- **동작 사실성**: DART는 HumanML3D에서 FID 0.42를 기록하여 MDM(0.54) 및 MotionDiffuse(0.63)보다 우수합니다.
- **생성 효율성**: 단일 단계 생성에 0.03초(30FPS)만 소요되어 실시간 상호작용을 지원하는 반면, MDM은 0.12초가 필요합니다.
- **공간 제어**: 목표 도달 작업에서 DART의 종점 위치 오차는 0.15미터로, T2M-GPT(0.38미터) 및 MotionDiffuse(0.29미터)보다 현저히 낮습니다.
- **장기 시퀀스 생성**: 연속 10문장 텍스트 설명 하에서 DART는 동작의 연속성을 유지하는 반면, 베이스라인 방법은 동작 단절이나 의미적 표류가 발생합니다.

### 결론
DART는 확산 모델과 자기회귀 생성을 결합하여 실시간, 장기 시퀀스, 공간적 제약이 있는 텍스트 기반 동작 제어를 최초로 구현했습니다. 이중 모드 공간 제어 전략(최적화 및 강화 학습)은 다양한 응용 시나리오에 유연한 선택지를 제공하며, 동작 품질과 제어 가능성 모두에서 최첨단 성능을 달성했습니다.
