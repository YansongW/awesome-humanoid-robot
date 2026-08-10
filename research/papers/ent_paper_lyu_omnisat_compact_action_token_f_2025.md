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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.09667v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (753 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.09667v1

## 개요
기존 비전-언어-행동 모델은 주로 확산 모델과 자기회귀 모델의 두 가지 유형으로 나뉜다: 전자는 계산 집약적인 반복 잡음 제거 과정에 의존하고, 후자는 효율적인 최적화와 유연한 시퀀스 구성을 지원하지만, 긴 행동 블록을 처리할 때 시퀀스 과다와 고차원성이라는 과제에 직면한다. OmniSAT는 혁신적인 행동 토크나이저를 통해 이 문제를 해결하는데, 먼저 B-Spline 인코딩을 사용하여 행동 값 범위와 시간 범위를 정규화한 다음, 위치, 회전 및 그리퍼 하위 공간에 대해 다단계 잔차 양자화를 수행하여 조밀한 수준에서 세밀한 수준의 이산 토큰을 생성한다. Droid 대규모 데이터셋에서 사전 훈련된 이 토크나이저는 훈련 시퀀스 길이를 6.8배 압축하고 목표 엔트로피를 낮추며, 동시에 교차 본체 학습 전략을 통해 로봇 시연과 휴머노이드 시연 데이터를 융합하고 이기종 1인칭 비디오를 활용하여 확장 가능한 보조 감독을 구현한다.

## 핵심 내용
### 방법 아키텍처
OmniSAT의 핵심은 Omni Swift Action Tokenizer로, 그 작업 흐름은 두 단계로 나뉜다:
1. **B-Spline 인코딩**: 원시 행동 값 범위와 시간 범위를 정규화하여 연속적이고 일관된 표현을 생성한다.
2. **다단계 잔차 양자화**: 인코딩된 행동을 위치, 회전 및 그리퍼의 세 하위 공간으로 분해하고, 각 하위 공간은 조밀한 수준에서 세밀한 수준의 잔차 양자화를 통해 이산 토큰을 생성하며, 최종적으로 컴팩트한 행동 시퀀스로 결합된다.

### 실험 설정
- **사전 훈련 데이터셋**: Droid 대규모 데이터셋.
- **훈련 효율성**: 행동 시퀀스 길이가 6.8배 압축되고 목표 엔트로피가 현저히 감소한다.
- **교차 본체 학습**: 통합된 행동 패턴 공간을 구축하고, 로봇 시연과 인간 1인칭 비디오 데이터를 공동으로 활용하여 이기종 감독 신호의 협력 훈련을 구현한다.

### 핵심 결과
- **압축 성능**: 재구성 품질을 유지하면서 OmniSAT는 기존 엔트로피 유도 및 토큰 빈도 방법보다 더 높은 압축 비율을 달성한다.
- **훈련 수렴**: 자기회귀 훈련 수렴 속도가 현저히 향상되며, 모델 성능은 실제 로봇 조작 및 시뮬레이션 실험 모두에서 기준 방법보다 우수하다.
- **일반화 능력**: 교차 본체 학습 전략을 통해 모델이 인간 비디오에서 효과적인 행동 패턴을 추출할 수 있어, 보지 못한 장면에 대한 적응성이 강화된다.
