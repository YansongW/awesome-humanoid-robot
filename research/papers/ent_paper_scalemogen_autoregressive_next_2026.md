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
  zh: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation is a paper on 人体动作 for humanoid robotics.
    用下一尺度自回归把文本生成的人体动作做成由粗到细.'
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
    Next-Scale Prediction for Human Motion Generation.'
sources:
- id: src_001
  type: website
  title: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-emporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## 核心内容
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-emporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## 参考
- Semantic Scholar search: ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation

## Overview
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-temporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## Content
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-temporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## 개요
본 논문에서는 텍스트 기반 인간 동작 생성을 위한 스케일 단위 자기회귀 프레임워크인 ScaleMoGen을 제시합니다. 기존의 표준 다음 토큰 예측에 의존하는 자기회귀 접근법과 달리, ScaleMoGen은 동작 생성을 조대한 단계에서 세밀한 단계로 진행되는 과정으로 구성합니다. 우리는 3D 동작을 점차 세분화되는 여러 골격-시간적 스케일에 걸쳐 구성적 이산 토큰으로 양자화하고, 다음 스케일의 토큰 맵을 자기회귀적으로 예측하여 동작을 생성하는 방법을 학습합니다. 구조적 무결성을 유지하기 위해, 우리의 동작 토크나이저와 양자화기는 모든 스케일의 이산 토큰이 골격 계층 구조를 엄격히 보존하도록 명시적으로 설계되었습니다. 또한, 비트 단위 양자화 및 예측을 사용하여 토크나이저 어휘를 효율적으로 확장함으로써 동작 세부 사항을 보존하고 최적화를 안정화합니다. 광범위한 실험을 통해 ScaleMoGen이 최첨단 성능을 달성함을 입증하며, HumanML3D에서 FID 0.030 (MoMask의 0.045 대비), SnapMoGen 데이터셋에서 CLIP Score 0.693 (MoMask++의 0.685 대비)을 기록했습니다. 또한, 우리의 골격-시간적 다중 스케일 표현이 학습 없이 텍스트 기반 동작 편집을 자연스럽게 지원함을 보여줍니다.

## 핵심 내용
본 논문에서는 텍스트 기반 인간 동작 생성을 위한 스케일 단위 자기회귀 프레임워크인 ScaleMoGen을 제시합니다. 기존의 표준 다음 토큰 예측에 의존하는 자기회귀 접근법과 달리, ScaleMoGen은 동작 생성을 조대한 단계에서 세밀한 단계로 진행되는 과정으로 구성합니다. 우리는 3D 동작을 점차 세분화되는 여러 골격-시간적 스케일에 걸쳐 구성적 이산 토큰으로 양자화하고, 다음 스케일의 토큰 맵을 자기회귀적으로 예측하여 동작을 생성하는 방법을 학습합니다. 구조적 무결성을 유지하기 위해, 우리의 동작 토크나이저와 양자화기는 모든 스케일의 이산 토큰이 골격 계층 구조를 엄격히 보존하도록 명시적으로 설계되었습니다. 또한, 비트 단위 양자화 및 예측을 사용하여 토크나이저 어휘를 효율적으로 확장함으로써 동작 세부 사항을 보존하고 최적화를 안정화합니다. 광범위한 실험을 통해 ScaleMoGen이 최첨단 성능을 달성함을 입증하며, HumanML3D에서 FID 0.030 (MoMask의 0.045 대비), SnapMoGen 데이터셋에서 CLIP Score 0.693 (MoMask++의 0.685 대비)을 기록했습니다. 또한, 우리의 골격-시간적 다중 스케일 표현이 학습 없이 텍스트 기반 동작 편집을 자연스럽게 지원함을 보여줍니다.
