---
$id: ent_paper_flexible_motion_in_betweening_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Flexible Motion In-betweening with Diffusion Models
  zh: Flexible Motion In-betweening with Diffusion Models
  ko: Flexible Motion In-betweening with Diffusion Models
summary:
  en: Flexible Motion In-betweening with Diffusion Models is a 2024 work on human motion analysis and synthesis for humanoid
    robots.
  zh: Flexible Motion In-betweening with Diffusion Models is a 2024 work on human motion analysis and synthesis for humanoid
    robots.
  ko: Flexible Motion In-betweening with Diffusion Models is a 2024 work on human motion analysis and synthesis for humanoid
    robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flexible_motion_in_betweening
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.11126v2.
sources:
- id: src_001
  type: paper
  title: Flexible Motion In-betweening with Diffusion Models (arXiv)
  url: https://arxiv.org/abs/2405.11126
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Motion in-betweening, a fundamental task in character animation, consists of generating motion sequences that plausibly interpolate user-provided keyframe constraints. It has long been recognized as a labor-intensive and challenging process. We investigate the potential of diffusion models in generating diverse human motions guided by keyframes. Unlike previous inbetweening methods, we propose a simple unified model capable of generating precise and diverse motions that conform to a flexible range of user-specified spatial constraints, as well as text conditioning. To this end, we propose Conditional Motion Diffusion In-betweening (CondMDI) which allows for arbitrary dense-or-sparse keyframe placement and partial keyframe constraints while generating high-quality motions that are diverse and coherent with the given keyframes. We evaluate the performance of CondMDI on the text-conditioned HumanML3D dataset and demonstrate the versatility and efficacy of diffusion models for keyframe in-betweening. We further explore the use of guidance and imputation-based approaches for inference-time keyframing and compare CondMDI against these methods.

## 核心内容
Motion in-betweening, a fundamental task in character animation, consists of generating motion sequences that plausibly interpolate user-provided keyframe constraints. It has long been recognized as a labor-intensive and challenging process. We investigate the potential of diffusion models in generating diverse human motions guided by keyframes. Unlike previous inbetweening methods, we propose a simple unified model capable of generating precise and diverse motions that conform to a flexible range of user-specified spatial constraints, as well as text conditioning. To this end, we propose Conditional Motion Diffusion In-betweening (CondMDI) which allows for arbitrary dense-or-sparse keyframe placement and partial keyframe constraints while generating high-quality motions that are diverse and coherent with the given keyframes. We evaluate the performance of CondMDI on the text-conditioned HumanML3D dataset and demonstrate the versatility and efficacy of diffusion models for keyframe in-betweening. We further explore the use of guidance and imputation-based approaches for inference-time keyframing and compare CondMDI against these methods.

## 参考
- http://arxiv.org/abs/2405.11126v2

## Overview
Motion in-betweening, a fundamental task in character animation, consists of generating motion sequences that plausibly interpolate user-provided keyframe constraints. It has long been recognized as a labor-intensive and challenging process. We investigate the potential of diffusion models in generating diverse human motions guided by keyframes. Unlike previous inbetweening methods, we propose a simple unified model capable of generating precise and diverse motions that conform to a flexible range of user-specified spatial constraints, as well as text conditioning. To this end, we propose Conditional Motion Diffusion In-betweening (CondMDI) which allows for arbitrary dense-or-sparse keyframe placement and partial keyframe constraints while generating high-quality motions that are diverse and coherent with the given keyframes. We evaluate the performance of CondMDI on the text-conditioned HumanML3D dataset and demonstrate the versatility and efficacy of diffusion models for keyframe in-betweening. We further explore the use of guidance and imputation-based approaches for inference-time keyframing and compare CondMDI against these methods.

## Content
Motion in-betweening, a fundamental task in character animation, consists of generating motion sequences that plausibly interpolate user-provided keyframe constraints. It has long been recognized as a labor-intensive and challenging process. We investigate the potential of diffusion models in generating diverse human motions guided by keyframes. Unlike previous inbetweening methods, we propose a simple unified model capable of generating precise and diverse motions that conform to a flexible range of user-specified spatial constraints, as well as text conditioning. To this end, we propose Conditional Motion Diffusion In-betweening (CondMDI) which allows for arbitrary dense-or-sparse keyframe placement and partial keyframe constraints while generating high-quality motions that are diverse and coherent with the given keyframes. We evaluate the performance of CondMDI on the text-conditioned HumanML3D dataset and demonstrate the versatility and efficacy of diffusion models for keyframe in-betweening. We further explore the use of guidance and imputation-based approaches for inference-time keyframing and compare CondMDI against these methods.

## 개요
모션 인비트위닝(Motion in-betweening)은 캐릭터 애니메이션의 기본적인 작업으로, 사용자가 제공한 키프레임 제약 조건을 그럴듯하게 보간하는 모션 시퀀스를 생성하는 것으로 구성됩니다. 이는 오랫동안 노동 집약적이고 까다로운 과정으로 인식되어 왔습니다. 우리는 키프레임에 의해 안내되는 다양한 인간 모션을 생성하는 데 있어 확산 모델의 잠재력을 조사합니다. 이전의 인비트위닝 방법과 달리, 우리는 텍스트 조건화뿐만 아니라 사용자가 지정한 유연한 범위의 공간적 제약 조건을 따르는 정밀하고 다양한 모션을 생성할 수 있는 간단한 통합 모델을 제안합니다. 이를 위해, 우리는 조건부 모션 확산 인비트위닝(Conditional Motion Diffusion In-betweening, CondMDI)을 제안합니다. 이는 임의의 밀집 또는 희소 키프레임 배치와 부분 키프레임 제약 조건을 허용하면서, 주어진 키프레임과 다양하고 일관된 고품질 모션을 생성합니다. 우리는 텍스트 조건화된 HumanML3D 데이터셋에서 CondMDI의 성능을 평가하고, 키프레임 인비트위닝을 위한 확산 모델의 다재다능함과 효율성을 입증합니다. 또한, 추론 시간 키프레이밍을 위한 가이던스 및 임퓨테이션 기반 접근법의 사용을 탐구하고, 이러한 방법들과 CondMDI를 비교합니다.

## 핵심 내용
모션 인비트위닝(Motion in-betweening)은 캐릭터 애니메이션의 기본적인 작업으로, 사용자가 제공한 키프레임 제약 조건을 그럴듯하게 보간하는 모션 시퀀스를 생성하는 것으로 구성됩니다. 이는 오랫동안 노동 집약적이고 까다로운 과정으로 인식되어 왔습니다. 우리는 키프레임에 의해 안내되는 다양한 인간 모션을 생성하는 데 있어 확산 모델의 잠재력을 조사합니다. 이전의 인비트위닝 방법과 달리, 우리는 텍스트 조건화뿐만 아니라 사용자가 지정한 유연한 범위의 공간적 제약 조건을 따르는 정밀하고 다양한 모션을 생성할 수 있는 간단한 통합 모델을 제안합니다. 이를 위해, 우리는 조건부 모션 확산 인비트위닝(Conditional Motion Diffusion In-betweening, CondMDI)을 제안합니다. 이는 임의의 밀집 또는 희소 키프레임 배치와 부분 키프레임 제약 조건을 허용하면서, 주어진 키프레임과 다양하고 일관된 고품질 모션을 생성합니다. 우리는 텍스트 조건화된 HumanML3D 데이터셋에서 CondMDI의 성능을 평가하고, 키프레임 인비트위닝을 위한 확산 모델의 다재다능함과 효율성을 입증합니다. 또한, 추론 시간 키프레이밍을 위한 가이던스 및 임퓨테이션 기반 접근법의 사용을 탐구하고, 이러한 방법들과 CondMDI를 비교합니다.
