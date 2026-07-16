---
$id: ent_paper_li_qdepth_vla_quantized_depth_pre_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models'
  zh: QDepth-VLA
  ko: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models'
summary:
  en: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models (QDepth-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, University
    of the Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Science, Beijing Zhongke Huiling Robot
    Technology Co.'
  zh: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models (QDepth-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, University
    of the Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Science, Beijing Zhongke Huiling Robot
    Technology Co.'
  ko: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models (QDepth-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, University
    of the Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Science, Beijing Zhongke Huiling Robot
    Technology Co.'
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
- qdepth_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14836v3.
sources:
- id: src_001
  type: paper
  title: 'QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.14836
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: QDepth-VLA source
  url: https://doi.org/10.48550/arXiv.2510.14836
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Spatial perception and reasoning are crucial for Vision-Language-Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. To address this limitation, we propose QDepth-VLA, a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues. Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

## 核心内容
Spatial perception and reasoning are crucial for Vision-Language-Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. To address this limitation, we propose QDepth-VLA, a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues. Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

## 参考
- http://arxiv.org/abs/2510.14836v3

## Overview
Spatial perception and reasoning are crucial for Vision-Language-Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. To address this limitation, we propose QDepth-VLA, a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues. Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

## Content
Spatial perception and reasoning are crucial for Vision-Language-Action (VLA) models to accomplish fine-grained manipulation tasks. However, existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. To address this limitation, we propose QDepth-VLA, a general framework that augments VLA models with an auxiliary depth prediction task. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues. Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

## 개요
공간 인식과 추론은 Vision-Language-Action(VLA) 모델이 정밀한 조작 작업을 수행하는 데 필수적입니다. 그러나 기존 접근 방식은 정밀한 제어에 필요한 핵심 3D 구조를 이해하고 추론하는 능력이 부족한 경우가 많습니다. 이러한 한계를 해결하기 위해, 우리는 VLA 모델에 보조 깊이 예측 작업을 추가하는 일반 프레임워크인 QDepth-VLA를 제안합니다. VQ-VAE 인코더에서 얻은 깊이 맵의 양자화된 잠재 토큰을 예측하도록 전용 깊이 전문가가 설계되어, 모델이 중요한 기하학적 단서를 포착하는 깊이 인식 표현을 학습할 수 있게 합니다. 시뮬레이션 벤치마크와 실제 작업에 대한 실험 결과는 QDepth-VLA가 강력한 공간 추론 능력과 조작 작업에서 경쟁력 있는 성능을 보여줌을 입증합니다.

## 핵심 내용
공간 인식과 추론은 Vision-Language-Action(VLA) 모델이 정밀한 조작 작업을 수행하는 데 필수적입니다. 그러나 기존 접근 방식은 정밀한 제어에 필요한 핵심 3D 구조를 이해하고 추론하는 능력이 부족한 경우가 많습니다. 이러한 한계를 해결하기 위해, 우리는 VLA 모델에 보조 깊이 예측 작업을 추가하는 일반 프레임워크인 QDepth-VLA를 제안합니다. VQ-VAE 인코더에서 얻은 깊이 맵의 양자화된 잠재 토큰을 예측하도록 전용 깊이 전문가가 설계되어, 모델이 중요한 기하학적 단서를 포착하는 깊이 인식 표현을 학습할 수 있게 합니다. 시뮬레이션 벤치마크와 실제 작업에 대한 실험 결과는 QDepth-VLA가 강력한 공간 추론 능력과 조작 작업에서 경쟁력 있는 성능을 보여줌을 입증합니다.
