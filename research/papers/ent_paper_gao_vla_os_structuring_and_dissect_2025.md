---
$id: ent_paper_gao_vla_os_structuring_and_dissect_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models'
  zh: VLA-OS
  ko: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models'
summary:
  en: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (VLA-OS),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore,
    University of Science and Technology of China, Tsinghua University, Nanyang Technological University, and published at
    NIPS25.'
  zh: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (VLA-OS),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore,
    University of Science and Technology of China, Tsinghua University, Nanyang Technological University, and published at
    NIPS25.'
  ko: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (VLA-OS),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore,
    University of Science and Technology of China, Tsinghua University, Nanyang Technological University, and published at
    NIPS25.'
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
- vla_os
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.17561v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.17561
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-OS source
  url: https://doi.org/10.48550/arXiv.2506.17561
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and components to be further improved. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable performance than other paradigms on task performance, pretraining, generalization ability, scalability, and continual learning ability, albeit at the cost of slower training and inference speeds.

## 核心内容
Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and components to be further improved. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable performance than other paradigms on task performance, pretraining, generalization ability, scalability, and continual learning ability, albeit at the cost of slower training and inference speeds.

## 参考
- http://arxiv.org/abs/2506.17561v1

## Overview
Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and components to be further improved. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable performance than other paradigms on task performance, pretraining, generalization ability, scalability, and continual learning ability, albeit at the cost of slower training and inference speeds.

## Content
Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and components to be further improved. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable performance than other paradigms on task performance, pretraining, generalization ability, scalability, and continual learning ability, albeit at the cost of slower training and inference speeds.

## 개요
최근 Vision-Language-Action(VLA) 모델에 대한 연구는 종단 간 행동 생성 패러다임에서 작업 계획 후 행동 생성을 포함하는 파이프라인으로 전환되었으며, 다양한 복잡하고 장기적인 조작 작업에서 향상된 성능을 보여주고 있습니다. 그러나 기존 접근 방식은 네트워크 아키텍처, 계획 패러다임, 표현 방식 및 훈련 데이터 소스 측면에서 상당한 차이를 보여, 연구자들이 성능 향상의 정확한 원인과 추가 개선이 필요한 구성 요소를 식별하기 어렵게 만듭니다. 네트워크 아키텍처와 훈련 데이터로부터 분리된 다양한 계획 패러다임과 표현의 영향을 체계적으로 조사하기 위해, 본 논문에서는 다양한 작업 계획 패러다임을 지원하는 통합 VLA 아키텍처 시리즈인 VLA-OS를 소개하고, 다양한 객체 범주(강체 및 변형체), 시각적 양식(2D 및 3D), 환경(시뮬레이션 및 실제 세계), 엔드 이펙터(그리퍼 및 다관절 손)에 걸친 포괄적인 통제 실험 세트를 설계합니다. 우리의 결과는 다음을 보여줍니다: 1) 시각적으로 기반한 계획 표현이 일반적으로 언어 계획 표현보다 우수합니다; 2) 계층적 VLA 패러다임은 일반적으로 작업 성능, 사전 훈련, 일반화 능력, 확장성 및 지속적 학습 능력에서 다른 패러다임보다 우수하거나 유사한 성능을 달성하지만, 훈련 및 추론 속도가 느리다는 단점이 있습니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델에 대한 연구는 종단 간 행동 생성 패러다임에서 작업 계획 후 행동 생성을 포함하는 파이프라인으로 전환되었으며, 다양한 복잡하고 장기적인 조작 작업에서 향상된 성능을 보여주고 있습니다. 그러나 기존 접근 방식은 네트워크 아키텍처, 계획 패러다임, 표현 방식 및 훈련 데이터 소스 측면에서 상당한 차이를 보여, 연구자들이 성능 향상의 정확한 원인과 추가 개선이 필요한 구성 요소를 식별하기 어렵게 만듭니다. 네트워크 아키텍처와 훈련 데이터로부터 분리된 다양한 계획 패러다임과 표현의 영향을 체계적으로 조사하기 위해, 본 논문에서는 다양한 작업 계획 패러다임을 지원하는 통합 VLA 아키텍처 시리즈인 VLA-OS를 소개하고, 다양한 객체 범주(강체 및 변형체), 시각적 양식(2D 및 3D), 환경(시뮬레이션 및 실제 세계), 엔드 이펙터(그리퍼 및 다관절 손)에 걸친 포괄적인 통제 실험 세트를 설계합니다. 우리의 결과는 다음을 보여줍니다: 1) 시각적으로 기반한 계획 표현이 일반적으로 언어 계획 표현보다 우수합니다; 2) 계층적 VLA 패러다임은 일반적으로 작업 성능, 사전 훈련, 일반화 능력, 확장성 및 지속적 학습 능력에서 다른 패러다임보다 우수하거나 유사한 성능을 달성하지만, 훈련 및 추론 속도가 느리다는 단점이 있습니다.
