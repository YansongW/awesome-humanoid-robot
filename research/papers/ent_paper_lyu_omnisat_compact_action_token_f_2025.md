---
$id: ent_paper_lyu_omnisat_compact_action_token_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniSAT: Compact Action Token, Faster Auto Regression'
  zh: OmniSAT
  ko: 'OmniSAT: Compact Action Token, Faster Auto Regression'
summary:
  en: 'OmniSAT: Compact Action Token, Faster Auto Regression (OmniSAT), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by University of Science and Technology of China.'
  zh: OmniSAT是中国科学技术大学于2025年提出的大型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于提出Omni Swift Action Tokenizer，通过B-Spline编码与多阶段残差量化将动作序列压缩6.8倍，同时保持重建质量，显著加速自回归训练收敛。
  ko: 'OmniSAT: Compact Action Token, Faster Auto Regression (OmniSAT), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by University of Science and Technology of China.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- omnisat
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.09667v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OmniSAT: Compact Action Token, Faster Auto Regression (arXiv)'
  url: https://arxiv.org/abs/2510.09667
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OmniSAT source
  url: https://doi.org/10.48550/arXiv.2510.09667
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型主要分为扩散模型与自回归模型两类：前者依赖计算密集的迭代去噪过程，后者虽支持高效优化与灵活序列构建，但在处理长动作块时面临序列过长与高维度的挑战。OmniSAT通过创新的动作分词器解决此问题，首先利用B-Spline编码对动作值域与时间跨度进行归一化，随后对位置、旋转与夹爪子空间执行多阶段残差量化，生成粗到细粒度的离散令牌。在Droid大规模数据集上预训练后，该分词器将训练序列长度压缩6.8倍并降低目标熵，同时通过跨本体学习策略融合机器人与人形演示数据，利用异构第一人称视频实现可扩展的辅助监督。

## 核心内容
### 方法架构
OmniSAT的核心是Omni Swift Action Tokenizer，其工作流程分为两步：
1. **B-Spline编码**：对原始动作值域与时间跨度进行归一化，生成连续且一致的表示。
2. **多阶段残差量化**：将编码后的动作分解为位置、旋转与夹爪三个子空间，每个子空间通过粗到细的残差量化生成离散令牌，最终组合为紧凑的动作序列。

### 实验设置
- **预训练数据集**：Droid大规模数据集。
- **训练效率**：动作序列长度压缩6.8倍，目标熵显著降低。
- **跨本体学习**：构建统一动作模式空间，联合利用机器人演示与人类第一人称视频数据，实现异构监督信号的协同训练。

### 关键结果
- **压缩性能**：在保持重建质量的前提下，OmniSAT实现比现有熵引导与令牌频率方法更高的压缩比。
- **训练收敛**：自回归训练收敛速度显著提升，模型性能在真实机器人操作与仿真实验中均优于基线方法。
- **泛化能力**：跨本体学习策略使模型能够从人类视频中提取有效动作模式，增强对未见场景的适应性。

## Overview
Existing Vision-Language-Action (VLA) models can be broadly categorized into diffusion-based and auto-regressive (AR) approaches: diffusion models capture continuous action distributions but rely on computationally heavy iterative denoising. In contrast, AR models enable efficient optimization and flexible sequence construction, making them better suited for large-scale pretraining. To further improve AR efficiency, particularly when action chunks induce extended and high-dimensional sequences, prior work applies entropy-guided and token-frequency techniques to shorten the sequence length. However, such compression struggled with \textit{poor reconstruction or inefficient compression}. Motivated by this, we introduce an Omni Swift Action Tokenizer, which learns a compact, transferable action representation. Specifically, we first normalize value ranges and temporal horizons to obtain a consistent representation with B-Spline encoding. Then, we apply multi-stage residual quantization to the position, rotation, and gripper subspaces, producing compressed discrete tokens with coarse-to-fine granularity for each part. After pre-training on the large-scale dataset Droid, the resulting discrete tokenization shortens the training sequence by 6.8$\times$, and lowers the target entropy. To further explore the potential of OmniSAT, we develop a cross-embodiment learning strategy that builds on the unified action-pattern space and jointly leverages robot and human demonstrations. It enables scalable auxiliary supervision from heterogeneous egocentric videos. Across diverse real-robot and simulation experiments, OmniSAT encompasses higher compression while preserving reconstruction quality, enabling faster AR training convergence and model performance.

## 개요
기존의 Vision-Language-Action (VLA) 모델은 크게 확산 기반(diffusion-based)과 자기회귀(auto-regressive, AR) 접근법으로 분류할 수 있습니다. 확산 모델은 연속적인 행동 분포를 포착하지만 계산량이 많은 반복적 잡음 제거에 의존합니다. 반면, AR 모델은 효율적인 최적화와 유연한 시퀀스 구성을 가능하게 하여 대규모 사전 학습에 더 적합합니다. 특히 행동 청크(action chunk)가 길고 고차원적인 시퀀스를 유발할 때 AR 효율성을 더욱 개선하기 위해, 기존 연구는 엔트로피 기반 및 토큰 빈도 기법을 적용하여 시퀀스 길이를 단축했습니다. 그러나 이러한 압축은 \textit{재구성 성능 저하 또는 비효율적인 압축}이라는 문제를 겪었습니다. 이에 착안하여, 우리는 Omni Swift Action Tokenizer를 소개합니다. 이는 간결하고 전이 가능한 행동 표현을 학습합니다. 구체적으로, 먼저 값 범위와 시간적 지평을 정규화하여 B-Spline 인코딩으로 일관된 표현을 얻습니다. 그런 다음, 위치, 회전, 그리퍼 하위 공간에 다단계 잔차 양자화(multi-stage residual quantization)를 적용하여 각 부분에 대해 거친 수준에서 세밀한 수준까지의 압축된 이산 토큰을 생성합니다. 대규모 데이터셋 Droid에서 사전 학습한 결과, 생성된 이산 토큰화는 학습 시퀀스를 6.8배 단축하고 목표 엔트로피를 낮춥니다. OmniSAT의 잠재력을 더 탐구하기 위해, 통합된 행동 패턴 공간을 기반으로 하고 로봇 및 인간 시연을 공동으로 활용하는 교차 체현 학습 전략(cross-embodiment learning strategy)을 개발합니다. 이를 통해 이질적인 자기중심적 비디오(heterogeneous egocentric videos)로부터 확장 가능한 보조 감독을 가능하게 합니다. 다양한 실제 로봇 및 시뮬레이션 실험에서 OmniSAT은 재구성 품질을 유지하면서 더 높은 압축률을 제공하여, 더 빠른 AR 학습 수렴과 모델 성능을 가능하게 합니다.

## 핵심 내용
기존의 Vision-Language-Action (VLA) 모델은 크게 확산 기반(diffusion-based)과 자기회귀(auto-regressive, AR) 접근법으로 분류할 수 있습니다. 확산 모델은 연속적인 행동 분포를 포착하지만 계산량이 많은 반복적 잡음 제거에 의존합니다. 반면, AR 모델은 효율적인 최적화와 유연한 시퀀스 구성을 가능하게 하여 대규모 사전 학습에 더 적합합니다. 특히 행동 청크(action chunk)가 길고 고차원적인 시퀀스를 유발할 때 AR 효율성을 더욱 개선하기 위해, 기존 연구는 엔트로피 기반 및 토큰 빈도 기법을 적용하여 시퀀스 길이를 단축했습니다. 그러나 이러한 압축은 \textit{재구성 성능 저하 또는 비효율적인 압축}이라는 문제를 겪었습니다. 이에 착안하여, 우리는 Omni Swift Action Tokenizer를 소개합니다. 이는 간결하고 전이 가능한 행동 표현을 학습합니다. 구체적으로, 먼저 값 범위와 시간적 지평을 정규화하여 B-Spline 인코딩으로 일관된 표현을 얻습니다. 그런 다음, 위치, 회전, 그리퍼 하위 공간에 다단계 잔차 양자화(multi-stage residual quantization)를 적용하여 각 부분에 대해 거친 수준에서 세밀한 수준까지의 압축된 이산 토큰을 생성합니다. 대규모 데이터셋 Droid에서 사전 학습한 결과, 생성된 이산 토큰화는 학습 시퀀스를 6.8배 단축하고 목표 엔트로피를 낮춥니다. OmniSAT의 잠재력을 더 탐구하기 위해, 통합된 행동 패턴 공간을 기반으로 하고 로봇 및 인간 시연을 공동으로 활용하는 교차 체현 학습 전략(cross-embodiment learning strategy)을 개발합니다. 이를 통해 이질적인 자기중심적 비디오(heterogeneous egocentric videos)로부터 확장 가능한 보조 감독을 가능하게 합니다. 다양한 실제 로봇 및 시뮬레이션 실험에서 OmniSAT은 재구성 품질을 유지하면서 더 높은 압축률을 제공하여, 더 빠른 AR 학습 수렴과 모델 성능을 가능하게 합니다.

## 参考
- http://arxiv.org/abs/2510.09667v1
