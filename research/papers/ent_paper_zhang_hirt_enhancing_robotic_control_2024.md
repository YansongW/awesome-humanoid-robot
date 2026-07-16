---
$id: ent_paper_zhang_hirt_enhancing_robotic_control_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers'
  zh: HiRT
  ko: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers'
summary:
  en: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers (HiRT), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences, Tsinghua University,
    University of California, Berkeley, Shanghai Qizhi Institute, and published at CoRL 2024.'
  zh: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers (HiRT), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences, Tsinghua University,
    University of California, Berkeley, Shanghai Qizhi Institute, and published at CoRL 2024.'
  ko: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers (HiRT), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences, Tsinghua University,
    University of California, Berkeley, Shanghai Qizhi Institute, and published at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hirt
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.05273v3.
sources:
- id: src_001
  type: paper
  title: HiRT source
  url: https://proceedings.mlr.press/v270/zhang25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Large Vision-Language-Action (VLA) models, leveraging powerful pre trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic ma nipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## 核心内容
Large Vision-Language-Action (VLA) models, leveraging powerful pre trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic ma nipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## 参考
- http://arxiv.org/abs/2410.05273v3

## Overview
Large Vision-Language-Action (VLA) models, leveraging powerful pre-trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic manipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## Content
Large Vision-Language-Action (VLA) models, leveraging powerful pre-trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic manipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## 개요
대규모 Vision-Language-Action(VLA) 모델은 강력한 사전 훈련된 Vision-Language Models(VLMs) 백엔드를 활용하여 뛰어난 일반화 능력 덕분에 로봇 제어에서 가능성을 보여주고 있습니다. 그러나 이러한 성공에는 대가가 따릅니다. 수십억 개의 매개변수를 가진 VLM 백엔드에 의존함으로써 높은 계산 비용과 추론 지연 시간이 발생하여, 테스트 시나리오가 주로 준정적(quasi-static) 작업으로 제한되고 빠른 상호작용이 필요한 동적 작업에서 성능이 저하됩니다. 이러한 한계를 해결하기 위해 본 논문에서는 유연한 주파수와 성능 간의 균형을 가능하게 하는 계층적 로봇 트랜스포머 프레임워크인 HiRT를 제안합니다. HiRT는 VLM을 낮은 주파수로 실행하여 일시적으로 불변하는 특징을 포착하는 동시에, 느리게 업데이트되는 특징에 의해 안내되는 고주파수 비전 기반 정책을 통해 실시간 상호작용을 가능하게 합니다. 시뮬레이션과 실제 환경 모두에서의 실험 결과는 기준 방법에 비해 상당한 개선을 보여줍니다. 경험적으로, 정적 작업에서는 제어 주파수를 두 배로 늘리고 비슷한 성공률을 달성했습니다. 또한, 이전 VLA 모델에 도전적인 새로운 실제 동적 조작 작업에서 HiRT는 성공률을 48%에서 75%로 향상시켰습니다.

## 핵심 내용
대규모 Vision-Language-Action(VLA) 모델은 강력한 사전 훈련된 Vision-Language Models(VLMs) 백엔드를 활용하여 뛰어난 일반화 능력 덕분에 로봇 제어에서 가능성을 보여주고 있습니다. 그러나 이러한 성공에는 대가가 따릅니다. 수십억 개의 매개변수를 가진 VLM 백엔드에 의존함으로써 높은 계산 비용과 추론 지연 시간이 발생하여, 테스트 시나리오가 주로 준정적(quasi-static) 작업으로 제한되고 빠른 상호작용이 필요한 동적 작업에서 성능이 저하됩니다. 이러한 한계를 해결하기 위해 본 논문에서는 유연한 주파수와 성능 간의 균형을 가능하게 하는 계층적 로봇 트랜스포머 프레임워크인 HiRT를 제안합니다. HiRT는 VLM을 낮은 주파수로 실행하여 일시적으로 불변하는 특징을 포착하는 동시에, 느리게 업데이트되는 특징에 의해 안내되는 고주파수 비전 기반 정책을 통해 실시간 상호작용을 가능하게 합니다. 시뮬레이션과 실제 환경 모두에서의 실험 결과는 기준 방법에 비해 상당한 개선을 보여줍니다. 경험적으로, 정적 작업에서는 제어 주파수를 두 배로 늘리고 비슷한 성공률을 달성했습니다. 또한, 이전 VLA 모델에 도전적인 새로운 실제 동적 조작 작업에서 HiRT는 성공률을 48%에서 75%로 향상시켰습니다.
