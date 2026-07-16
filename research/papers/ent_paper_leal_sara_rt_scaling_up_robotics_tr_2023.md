---
$id: ent_paper_leal_sara_rt_scaling_up_robotics_tr_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention'
  zh: SARA-RT
  ko: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention'
summary:
  en: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention (SARA-RT), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google, and published at ICRA 2023.'
  zh: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention (SARA-RT), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google, and published at ICRA 2023.'
  ko: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention (SARA-RT), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google, and published at ICRA 2023.'
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
- robotic_manipulation
- sara_rt
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.01990v1.
sources:
- id: src_001
  type: website
  title: SARA-RT source
  url: https://doi.org/10.1109/ICRA57147.2024.10611597
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment. SARA-RT relies on the new method of fine-tuning proposed by us, called up-training. It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality. We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models, the first VLA robotic policies pre-trained on internet-scale data, as well as (b) Point Cloud Transformer (PCT) robotic policies operating on large point clouds. We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.

## 核心内容
We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment. SARA-RT relies on the new method of fine-tuning proposed by us, called up-training. It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality. We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models, the first VLA robotic policies pre-trained on internet-scale data, as well as (b) Point Cloud Transformer (PCT) robotic policies operating on large point clouds. We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.

## 参考
- http://arxiv.org/abs/2312.01990v1

## Overview
We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment. SARA-RT relies on the new method of fine-tuning proposed by us, called up-training. It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality. We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models, the first VLA robotic policies pre-trained on internet-scale data, as well as (b) Point Cloud Transformer (PCT) robotic policies operating on large point clouds. We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.

## Content
We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment. SARA-RT relies on the new method of fine-tuning proposed by us, called up-training. It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality. We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models, the first VLA robotic policies pre-trained on internet-scale data, as well as (b) Point Cloud Transformer (PCT) robotic policies operating on large point clouds. We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.

## 개요
우리는 로봇 트랜스포머(Robotics Transformers, RT)의 로봇 탑재 배포를 위한 확장 문제를 해결하는 새로운 패러다임인 SARA-RT(Self-Adaptive Robust Attention for Robotics Transformers)를 제시합니다. SARA-RT는 우리가 제안한 새로운 미세 조정 방법인 업트레이닝(up-training)에 기반합니다. 이 방법은 사전 훈련되거나 이미 미세 조정된 이차 시간 복잡도의 트랜스포머 기반 로봇 정책(수십억 파라미터의 거대한 비전-언어-행동 모델(VLA) 포함)을 높은 품질을 유지하는 효율적인 선형 어텐션 버전으로 변환합니다. 우리는 SARA-RT의 효과를 다음을 가속화함으로써 입증합니다: (a) 최근 도입된 RT-2 모델 클래스(인터넷 규모 데이터로 사전 훈련된 최초의 VLA 로봇 정책) 및 (b) 대규모 포인트 클라우드에서 작동하는 포인트 클라우드 트랜스포머(PCT) 로봇 정책. 또한, SARA 현상에 대한 더 깊은 통찰을 제공하는 엄격한 수학적 분석으로 결과를 보완합니다.

## 핵심 내용
우리는 로봇 트랜스포머(Robotics Transformers, RT)의 로봇 탑재 배포를 위한 확장 문제를 해결하는 새로운 패러다임인 SARA-RT(Self-Adaptive Robust Attention for Robotics Transformers)를 제시합니다. SARA-RT는 우리가 제안한 새로운 미세 조정 방법인 업트레이닝(up-training)에 기반합니다. 이 방법은 사전 훈련되거나 이미 미세 조정된 이차 시간 복잡도의 트랜스포머 기반 로봇 정책(수십억 파라미터의 거대한 비전-언어-행동 모델(VLA) 포함)을 높은 품질을 유지하는 효율적인 선형 어텐션 버전으로 변환합니다. 우리는 SARA-RT의 효과를 다음을 가속화함으로써 입증합니다: (a) 최근 도입된 RT-2 모델 클래스(인터넷 규모 데이터로 사전 훈련된 최초의 VLA 로봇 정책) 및 (b) 대규모 포인트 클라우드에서 작동하는 포인트 클라우드 트랜스포머(PCT) 로봇 정책. 또한, SARA 현상에 대한 더 깊은 통찰을 제공하는 엄격한 수학적 분석으로 결과를 보완합니다.
