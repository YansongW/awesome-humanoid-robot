---
$id: ent_paper_kang_clip_rt_learning_language_cond_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision'
  zh: CLIP-RT
  ko: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision'
summary:
  en: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (CLIP-RT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Seoul National University, and published at RSS25.'
  zh: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (CLIP-RT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Seoul National University, and published at RSS25.'
  ko: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (CLIP-RT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Seoul National University, and published at RSS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- clip_rt
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.00508v4.
sources:
- id: src_001
  type: paper
  title: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (arXiv)'
  url: https://arxiv.org/abs/2411.00508
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CLIP-RT source
  url: https://doi.org/10.48550/arXiv.2411.00508
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Teaching robots desired skills in real-world environments remains challenging, especially for non-experts. A key bottleneck is that collecting robotic data often requires expertise or specialized hardware, limiting accessibility and scalability. We posit that natural language offers an intuitive and accessible interface for robot learning. To this end, we study two aspects: (1) enabling non-experts to collect robotic data through natural language supervision (e.g., "move the arm to the right") and (2) training robot policies directly from this supervision. Specifically, we introduce a data collection framework that collects robot demonstrations based on natural language supervision and further augments these demonstrations. We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor policies from this supervision. CLIP-RT adapts the pretrained CLIP model and learns to predict language-based motion primitives via contrastive imitation learning. We train CLIP-RT on the Open X-Embodiment dataset and finetune it on in-domain data collected by our framework. In real-world evaluations, CLIP-RT demonstrates strong capabilities in learning novel manipulation skills, outperforming OpenVLA (7B parameters) by 24% in average success rates, while using 7x fewer parameters (1B). We further assess CLIP-RT's capabilities in few-shot generalization and collaborative scenarios involving large pretrained models or humans. In simulated environments, CLIP-RT also yields strong performance, achieving a 93.1% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.

## 核心内容
Teaching robots desired skills in real-world environments remains challenging, especially for non-experts. A key bottleneck is that collecting robotic data often requires expertise or specialized hardware, limiting accessibility and scalability. We posit that natural language offers an intuitive and accessible interface for robot learning. To this end, we study two aspects: (1) enabling non-experts to collect robotic data through natural language supervision (e.g., "move the arm to the right") and (2) training robot policies directly from this supervision. Specifically, we introduce a data collection framework that collects robot demonstrations based on natural language supervision and further augments these demonstrations. We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor policies from this supervision. CLIP-RT adapts the pretrained CLIP model and learns to predict language-based motion primitives via contrastive imitation learning. We train CLIP-RT on the Open X-Embodiment dataset and finetune it on in-domain data collected by our framework. In real-world evaluations, CLIP-RT demonstrates strong capabilities in learning novel manipulation skills, outperforming OpenVLA (7B parameters) by 24% in average success rates, while using 7x fewer parameters (1B). We further assess CLIP-RT's capabilities in few-shot generalization and collaborative scenarios involving large pretrained models or humans. In simulated environments, CLIP-RT also yields strong performance, achieving a 93.1% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.

## 参考
- http://arxiv.org/abs/2411.00508v4

## Overview
Teaching robots desired skills in real-world environments remains challenging, especially for non-experts. A key bottleneck is that collecting robotic data often requires expertise or specialized hardware, limiting accessibility and scalability. We posit that natural language offers an intuitive and accessible interface for robot learning. To this end, we study two aspects: (1) enabling non-experts to collect robotic data through natural language supervision (e.g., "move the arm to the right") and (2) training robot policies directly from this supervision. Specifically, we introduce a data collection framework that collects robot demonstrations based on natural language supervision and further augments these demonstrations. We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor policies from this supervision. CLIP-RT adapts the pretrained CLIP model and learns to predict language-based motion primitives via contrastive imitation learning. We train CLIP-RT on the Open X-Embodiment dataset and finetune it on in-domain data collected by our framework. In real-world evaluations, CLIP-RT demonstrates strong capabilities in learning novel manipulation skills, outperforming OpenVLA (7B parameters) by 24% in average success rates, while using 7x fewer parameters (1B). We further assess CLIP-RT's capabilities in few-shot generalization and collaborative scenarios involving large pretrained models or humans. In simulated environments, CLIP-RT also yields strong performance, achieving a 93.1% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.

## Content
Teaching robots desired skills in real-world environments remains challenging, especially for non-experts. A key bottleneck is that collecting robotic data often requires expertise or specialized hardware, limiting accessibility and scalability. We posit that natural language offers an intuitive and accessible interface for robot learning. To this end, we study two aspects: (1) enabling non-experts to collect robotic data through natural language supervision (e.g., "move the arm to the right") and (2) training robot policies directly from this supervision. Specifically, we introduce a data collection framework that collects robot demonstrations based on natural language supervision and further augments these demonstrations. We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor policies from this supervision. CLIP-RT adapts the pretrained CLIP model and learns to predict language-based motion primitives via contrastive imitation learning. We train CLIP-RT on the Open X-Embodiment dataset and finetune it on in-domain data collected by our framework. In real-world evaluations, CLIP-RT demonstrates strong capabilities in learning novel manipulation skills, outperforming OpenVLA (7B parameters) by 24% in average success rates, while using 7x fewer parameters (1B). We further assess CLIP-RT's capabilities in few-shot generalization and collaborative scenarios involving large pretrained models or humans. In simulated environments, CLIP-RT also yields strong performance, achieving a 93.1% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.

## 개요
실제 환경에서 로봇에게 원하는 기술을 가르치는 것은 특히 비전문가에게 여전히 어려운 과제입니다. 주요 병목 현상 중 하나는 로봇 데이터 수집에 종종 전문 지식이나 특수 하드웨어가 필요하여 접근성과 확장성이 제한된다는 점입니다. 우리는 자연어가 로봇 학습을 위한 직관적이고 접근 가능한 인터페이스를 제공한다고 가정합니다. 이를 위해 두 가지 측면을 연구합니다: (1) 비전문가가 자연어 감독(예: "팔을 오른쪽으로 움직여")을 통해 로봇 데이터를 수집할 수 있도록 하는 것, (2) 이 감독으로부터 직접 로봇 정책을 훈련하는 것입니다. 구체적으로, 자연어 감독을 기반으로 로봇 시연을 수집하고 이러한 시연을 추가로 증강하는 데이터 수집 프레임워크를 소개합니다. 그런 다음 이 감독으로부터 언어 조건부 시각운동 정책을 학습하는 새로운 시각-언어-행동(VLA) 모델인 CLIP-RT를 제시합니다. CLIP-RT는 사전 훈련된 CLIP 모델을 적용하고 대조적 모방 학습을 통해 언어 기반 운동 프리미티브를 예측하는 방법을 학습합니다. 우리는 Open X-Embodiment 데이터셋에서 CLIP-RT를 훈련하고, 우리 프레임워크로 수집된 도메인 내 데이터로 미세 조정합니다. 실제 환경 평가에서 CLIP-RT는 새로운 조작 기술을 학습하는 데 강력한 능력을 보여주며, 7배 적은 매개변수(1B)를 사용하면서 OpenVLA(7B 매개변수)보다 평균 성공률에서 24% 더 뛰어난 성능을 보였습니다. 또한 CLIP-RT의 소수 샷 일반화 및 대규모 사전 훈련 모델이나 인간과의 협업 시나리오에서의 능력을 평가합니다. 시뮬레이션 환경에서도 CLIP-RT는 강력한 성능을 발휘하여 LIBERO 벤치마크에서 93.1%의 평균 성공률과 163Hz의 추론 처리량을 달성했습니다.

## 핵심 내용
실제 환경에서 로봇에게 원하는 기술을 가르치는 것은 특히 비전문가에게 여전히 어려운 과제입니다. 주요 병목 현상 중 하나는 로봇 데이터 수집에 종종 전문 지식이나 특수 하드웨어가 필요하여 접근성과 확장성이 제한된다는 점입니다. 우리는 자연어가 로봇 학습을 위한 직관적이고 접근 가능한 인터페이스를 제공한다고 가정합니다. 이를 위해 두 가지 측면을 연구합니다: (1) 비전문가가 자연어 감독(예: "팔을 오른쪽으로 움직여")을 통해 로봇 데이터를 수집할 수 있도록 하는 것, (2) 이 감독으로부터 직접 로봇 정책을 훈련하는 것입니다. 구체적으로, 자연어 감독을 기반으로 로봇 시연을 수집하고 이러한 시연을 추가로 증강하는 데이터 수집 프레임워크를 소개합니다. 그런 다음 이 감독으로부터 언어 조건부 시각운동 정책을 학습하는 새로운 시각-언어-행동(VLA) 모델인 CLIP-RT를 제시합니다. CLIP-RT는 사전 훈련된 CLIP 모델을 적용하고 대조적 모방 학습을 통해 언어 기반 운동 프리미티브를 예측하는 방법을 학습합니다. 우리는 Open X-Embodiment 데이터셋에서 CLIP-RT를 훈련하고, 우리 프레임워크로 수집된 도메인 내 데이터로 미세 조정합니다. 실제 환경 평가에서 CLIP-RT는 새로운 조작 기술을 학습하는 데 강력한 능력을 보여주며, 7배 적은 매개변수(1B)를 사용하면서 OpenVLA(7B 매개변수)보다 평균 성공률에서 24% 더 뛰어난 성능을 보였습니다. 또한 CLIP-RT의 소수 샷 일반화 및 대규모 사전 훈련 모델이나 인간과의 협업 시나리오에서의 능력을 평가합니다. 시뮬레이션 환경에서도 CLIP-RT는 강력한 성능을 발휘하여 LIBERO 벤치마크에서 93.1%의 평균 성공률과 163Hz의 추론 처리량을 달성했습니다.
