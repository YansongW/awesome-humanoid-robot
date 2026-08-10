---
$id: ent_paper_scalemogen_autoregressive_next_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation'
  zh: 用下一尺度自回归把文本生成的人体动作做成由粗到细
  ko: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation'
summary:
  en: We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional
    autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine
    process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-emporal scales of increasing
    granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural
    integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly
    preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale
    up the tokenizer vocabulary to preserve motion details and stabilize optim
  zh: ScaleMoGen 是一种用于文本驱动人体运动生成的尺度级自回归框架。它由研究团队提出，核心贡献在于将运动生成建模为从粗到细的过程，通过自回归预测下一尺度的离散令牌图来实现。该方法在 HumanML3D 数据集上取得了 FID 0.030
    的领先性能，并支持无需训练的运动编辑。
  ko: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation is a paper on 人体动作 for humanoid robotics.
    用下一尺度自回归把文本生成的人体动作做成由粗到细.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_motion
- humanoid
- motion_synthesis
- scalemogen
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: ScaleMoGen: Autoregressive
    Next-Scale Prediction for Human Motion Generation. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (841 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
ScaleMoGen 创新性地将人体运动生成从传统的逐令牌预测转变为逐尺度预测。它首先将 3D 运动量化为多个骨骼-时间尺度的组合离散令牌，这些尺度具有递增的粒度。模型通过自回归方式预测下一尺度的令牌图，从而逐步生成精细的运动。为了保持运动的结构完整性，其设计的令牌化器和量化器确保每个尺度的离散令牌严格保留骨骼层级结构。此外，采用按位量化和预测技术有效扩大了令牌词汇量，以保留运动细节并稳定优化过程。

## 核心内容
### 方法架构
ScaleMoGen 的核心是一个尺度级自回归框架，将运动生成分解为从粗到细的多尺度过程。具体而言：
- **多尺度运动量化**：将 3D 人体运动量化为多个骨骼-时间尺度的组合离散令牌。这些尺度具有递增的粒度，从粗略的整体姿态到精细的局部关节运动。
- **自回归预测**：模型通过自回归方式预测下一尺度的令牌图，即从最粗的尺度开始，逐步生成更精细的运动细节。
- **结构保持设计**：运动令牌化器和量化器被明确设计为每个尺度的离散令牌严格保留骨骼层级结构，确保生成的运动在结构上合理。

### 关键技术
- **按位量化与预测**：采用按位量化技术，有效扩大了令牌词汇量，从而更好地保留运动细节，并稳定优化过程。

### 实验设置与结果
- **数据集**：在 HumanML3D 和 SnapMoGen 数据集上进行评估。
- **关键性能指标**：
  - 在 HumanML3D 数据集上，ScaleMoGen 的 FID 达到 0.030，优于 MoMask 的 0.045。
  - 在 SnapMoGen 数据集上，CLIP Score 达到 0.693，优于 MoMask++ 的 0.685。
- **额外能力**：该多尺度表示自然支持无需训练的文本引导运动编辑。

### 结论
ScaleMoGen 通过尺度级自回归预测，在文本驱动人体运动生成任务上取得了最先进的性能，并展示了在运动编辑方面的潜力。

## Overview
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-emporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## Overview
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-temporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## Content
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-temporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## 参考
- Semantic Scholar search: ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation

## 개요
ScaleMoGen은 인간 동작 생성을 기존의 토큰별 예측에서 스케일별 예측으로 혁신적으로 전환합니다. 먼저 3D 동작을 점진적으로 세분화된 여러 골격-시간 스케일의 조합된 이산 토큰으로 양자화합니다. 모델은 자기회귀 방식으로 다음 스케일의 토큰 맵을 예측하여 점진적으로 정밀한 동작을 생성합니다. 동작의 구조적 무결성을 유지하기 위해 설계된 토크나이저와 양자화기는 각 스케일의 이산 토큰이 골격 계층 구조를 엄격히 보존하도록 보장합니다. 또한, 비트 단위 양자화 및 예측 기술을 채택하여 토큰 어휘를 효과적으로 확장함으로써 동작 세부 사항을 보존하고 최적화 과정을 안정화합니다.

## 핵심 내용
### 방법 아키텍처
ScaleMoGen의 핵심은 동작 생성을 거친 단계에서 세밀한 단계로의 다중 스케일 과정으로 분해하는 스케일 수준 자기회귀 프레임워크입니다. 구체적으로:
- **다중 스케일 동작 양자화**: 3D 인간 동작을 여러 골격-시간 스케일의 조합된 이산 토큰으로 양자화합니다. 이러한 스케일은 대략적인 전체 자세에서 세밀한 국소 관절 동작까지 점진적으로 세분화됩니다.
- **자기회귀 예측**: 모델은 자기회귀 방식으로 다음 스케일의 토큰 맵을 예측합니다. 즉, 가장 거친 스케일에서 시작하여 점진적으로 더 세밀한 동작 세부 사항을 생성합니다.
- **구조 보존 설계**: 동작 토크나이저와 양자화기는 각 스케일의 이산 토큰이 골격 계층 구조를 엄격히 보존하도록 명시적으로 설계되어 생성된 동작이 구조적으로 타당함을 보장합니다.

### 핵심 기술
- **비트 단위 양자화 및 예측**: 비트 단위 양자화 기술을 채택하여 토큰 어휘를 효과적으로 확장함으로써 동작 세부 사항을 더 잘 보존하고 최적화 과정을 안정화합니다.

### 실험 설정 및 결과
- **데이터셋**: HumanML3D 및 SnapMoGen 데이터셋에서 평가되었습니다.
- **주요 성능 지표**:
  - HumanML3D 데이터셋에서 ScaleMoGen의 FID는 0.030으로, MoMask의 0.045보다 우수합니다.
  - SnapMoGen 데이터셋에서 CLIP Score는 0.693으로, MoMask++의 0.685보다 우수합니다.
- **추가 능력**: 이 다중 스케일 표현은 학습 없이도 텍스트 기반 동작 편집을 자연스럽게 지원합니다.

### 결론
ScaleMoGen은 스케일 수준 자기회귀 예측을 통해 텍스트 기반 인간 동작 생성 작업에서 최첨단 성능을 달성했으며, 동작 편집에서의 잠재력을 보여줍니다.
