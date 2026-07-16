---
$id: ent_paper_ye_actdistill_general_action_guid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models'
  zh: ActDistill
  ko: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models'
summary:
  en: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (ActDistill),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of
    Technology Sydney, Advanced Institute of Big Data.'
  zh: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (ActDistill),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of
    Technology Sydney, Advanced Institute of Big Data.'
  ko: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (ActDistill),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of
    Technology Sydney, Advanced Institute of Big Data.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- actdistill
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18082v3.
sources:
- id: src_001
  type: paper
  title: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.18082
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ActDistill source
  url: https://doi.org/10.48550/arXiv.2511.18082
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.

## 核心内容
Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.

## 参考
- http://arxiv.org/abs/2511.18082v3

## Overview
Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.

## Content
Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.

## 개요
최근 Vision-Language-Action(VLA) 모델은 뛰어난 유연성과 일반화 능력을 보여주었지만, 로봇 조작 분야에서의 배포는 여전히 높은 계산 부하와 추론 지연 시간으로 인해 제한적입니다. 본 연구에서는 ActDistill을 제안합니다. 이는 기존 VLA 모델의 행동 예측 능력을 경량화된 모델로 전이하는 일반적인 행동 기반 자기 유도 증류 프레임워크입니다. 주로 시각-언어 상관관계에 초점을 맞춘 기존 효율성 전략과 달리, ActDistill은 행동 사전 정보를 활용하여 지식 전이와 모델 압축을 유도함으로써 VLA 모델의 행동 지향적 효율성을 달성합니다. 구체적으로, 잘 훈련된 VLA 모델을 교사 모델로 사용하고, 그래프 구조화 캡슐화 전략을 도입하여 행동 예측의 계층적 진화를 명시적으로 모델링합니다. 그래프로 캡슐화된 교사 모델에서 파생된 학생 모델에는 동적 라우터가 추가로 장착되어, 행동 예측 요구에 따라 계산 경로를 적응적으로 선택하며, 계층적 그래프 기반 감독을 통해 원활하고 효율적인 진화를 보장합니다. 추론 중에는 그래프 관련 보조 구성 요소가 제거되어, 학생 모델은 동적으로 라우팅된 레이어만 실행하고 최소한의 계산과 지연 시간으로 고정밀 행동을 예측할 수 있습니다. 임베디드 벤치마크 실험 결과, ActDistill은 전체 규모 VLA 모델과 동등하거나 더 우수한 성능을 달성하면서도 계산량을 50% 이상 줄이고 최대 1.67배의 속도 향상을 보여, 효율적인 임베디드 지능을 위한 일반적인 패러다임을 구축합니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델은 뛰어난 유연성과 일반화 능력을 보여주었지만, 로봇 조작 분야에서의 배포는 여전히 높은 계산 부하와 추론 지연 시간으로 인해 제한적입니다. 본 연구에서는 ActDistill을 제안합니다. 이는 기존 VLA 모델의 행동 예측 능력을 경량화된 모델로 전이하는 일반적인 행동 기반 자기 유도 증류 프레임워크입니다. 주로 시각-언어 상관관계에 초점을 맞춘 기존 효율성 전략과 달리, ActDistill은 행동 사전 정보를 활용하여 지식 전이와 모델 압축을 유도함으로써 VLA 모델의 행동 지향적 효율성을 달성합니다. 구체적으로, 잘 훈련된 VLA 모델을 교사 모델로 사용하고, 그래프 구조화 캡슐화 전략을 도입하여 행동 예측의 계층적 진화를 명시적으로 모델링합니다. 그래프로 캡슐화된 교사 모델에서 파생된 학생 모델에는 동적 라우터가 추가로 장착되어, 행동 예측 요구에 따라 계산 경로를 적응적으로 선택하며, 계층적 그래프 기반 감독을 통해 원활하고 효율적인 진화를 보장합니다. 추론 중에는 그래프 관련 보조 구성 요소가 제거되어, 학생 모델은 동적으로 라우팅된 레이어만 실행하고 최소한의 계산과 지연 시간으로 고정밀 행동을 예측할 수 있습니다. 임베디드 벤치마크 실험 결과, ActDistill은 전체 규모 VLA 모델과 동등하거나 더 우수한 성능을 달성하면서도 계산량을 50% 이상 줄이고 최대 1.67배의 속도 향상을 보여, 효율적인 임베디드 지능을 위한 일반적인 패러다임을 구축합니다.
