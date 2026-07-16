---
$id: ent_paper_yang_vlaser_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning'
  zh: Vlaser
  ko: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning'
summary:
  en: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (Vlaser), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Science and Technology of China, Shanghai AI Laboratory, Shanghai
    Jiao Tong University, Zhejiang University, Nanjing University, Fudan University, Tsinghua University, NUS, Northeastern
    University, Shenzhen University.'
  zh: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (Vlaser), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Science and Technology of China, Shanghai AI Laboratory, Shanghai
    Jiao Tong University, Zhejiang University, Nanjing University, Fudan University, Tsinghua University, NUS, Northeastern
    University, Shenzhen University.'
  ko: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (Vlaser), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Science and Technology of China, Shanghai AI Laboratory, Shanghai
    Jiao Tong University, Zhejiang University, Nanjing University, Fudan University, Tsinghua University, NUS, Northeastern
    University, Shenzhen University.'
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
- vision_language_action
- vla
- vlaser
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.11027v2.
sources:
- id: src_001
  type: paper
  title: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (arXiv)'
  url: https://arxiv.org/abs/2510.11027
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Vlaser source
  url: https://doi.org/10.48550/arXiv.2510.11027
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot control, few studies directly address the critical gap between upstream VLM-based reasoning and downstream VLA policy learning. In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning capability, which is a foundational vision-language model designed to integrate high-level reasoning with low-level control for embodied agents. Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks - including spatial reasoning, embodied grounding, embodied QA, and task planning. Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and embodied-specific policy learning data. Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.

## 核心内容
While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot control, few studies directly address the critical gap between upstream VLM-based reasoning and downstream VLA policy learning. In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning capability, which is a foundational vision-language model designed to integrate high-level reasoning with low-level control for embodied agents. Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks - including spatial reasoning, embodied grounding, embodied QA, and task planning. Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and embodied-specific policy learning data. Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.

## 参考
- http://arxiv.org/abs/2510.11027v2

## Overview
While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot control, few studies directly address the critical gap between upstream VLM-based reasoning and downstream VLA policy learning. In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning capability, which is a foundational vision-language model designed to integrate high-level reasoning with low-level control for embodied agents. Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks - including spatial reasoning, embodied grounding, embodied QA, and task planning. Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and embodied-specific policy learning data. Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.

## Content
While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot control, few studies directly address the critical gap between upstream VLM-based reasoning and downstream VLA policy learning. In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning capability, which is a foundational vision-language model designed to integrate high-level reasoning with low-level control for embodied agents. Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks - including spatial reasoning, embodied grounding, embodied QA, and task planning. Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and embodied-specific policy learning data. Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.

## 개요
상당한 연구가 시각-언어 모델(VLM)을 사용한 체화된 추론 능력 개발이나 고급 VLM을 시각-언어-행동(VLA) 모델에 통합하여 엔드투엔드 로봇 제어를 수행하는 데 집중되어 왔지만, 상위 VLM 기반 추론과 하위 VLA 정책 학습 간의 중요한 격차를 직접적으로 해결한 연구는 거의 없습니다. 본 연구에서는 체화된 추론과 VLA 정책 학습을 연결하는 첫걸음으로, Vlaser를 소개합니다. Vlaser는 시너지적 체화된 추론 능력을 갖춘 시각-언어-행동 모델로, 체화된 에이전트를 위해 고수준 추론과 저수준 제어를 통합하도록 설계된 기초 시각-언어 모델입니다. 고품질의 Vlaser-6M 데이터셋을 기반으로 구축된 Vlaser는 공간 추론, 체화된 접지, 체화된 QA, 작업 계획을 포함한 다양한 체화된 추론 벤치마크에서 최첨단 성능을 달성합니다. 또한, 서로 다른 VLM 초기화가 지도 학습 기반 VLA 미세 조정에 미치는 영향을 체계적으로 조사하여, 인터넷 규모의 사전 학습 데이터와 체화된 특화 정책 학습 데이터 간의 도메인 차이를 완화하는 새로운 통찰력을 제공합니다. 이러한 통찰력을 바탕으로, 우리의 접근 방식은 WidowX 벤치마크에서 최첨단 결과를, Google Robot 벤치마크에서 경쟁력 있는 성능을 달성합니다.

## 핵심 내용
상당한 연구가 시각-언어 모델(VLM)을 사용한 체화된 추론 능력 개발이나 고급 VLM을 시각-언어-행동(VLA) 모델에 통합하여 엔드투엔드 로봇 제어를 수행하는 데 집중되어 왔지만, 상위 VLM 기반 추론과 하위 VLA 정책 학습 간의 중요한 격차를 직접적으로 해결한 연구는 거의 없습니다. 본 연구에서는 체화된 추론과 VLA 정책 학습을 연결하는 첫걸음으로, Vlaser를 소개합니다. Vlaser는 시너지적 체화된 추론 능력을 갖춘 시각-언어-행동 모델로, 체화된 에이전트를 위해 고수준 추론과 저수준 제어를 통합하도록 설계된 기초 시각-언어 모델입니다. 고품질의 Vlaser-6M 데이터셋을 기반으로 구축된 Vlaser는 공간 추론, 체화된 접지, 체화된 QA, 작업 계획을 포함한 다양한 체화된 추론 벤치마크에서 최첨단 성능을 달성합니다. 또한, 서로 다른 VLM 초기화가 지도 학습 기반 VLA 미세 조정에 미치는 영향을 체계적으로 조사하여, 인터넷 규모의 사전 학습 데이터와 체화된 특화 정책 학습 데이터 간의 도메인 차이를 완화하는 새로운 통찰력을 제공합니다. 이러한 통찰력을 바탕으로, 우리의 접근 방식은 WidowX 벤치마크에서 최첨단 결과를, Google Robot 벤치마크에서 경쟁력 있는 성능을 달성합니다.
