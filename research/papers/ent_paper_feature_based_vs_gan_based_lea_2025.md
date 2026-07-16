---
$id: ent_paper_feature_based_vs_gan_based_lea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why'
  zh: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why'
  ko: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why'
summary:
  en: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why is a 2025 work on physics-based character animation
    for humanoid robots.'
  zh: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why is a 2025 work on physics-based character animation
    for humanoid robots.'
  ko: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why is a 2025 work on physics-based character animation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- feature_based_vs_gan_based_lea
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.05906v2.
sources:
- id: src_001
  type: paper
  title: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why (arXiv)'
  url: https://arxiv.org/abs/2507.05906
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This survey provides a comparative analysis of feature-based and GAN-based approaches to learning from demonstrations, with a focus on the structure of reward functions and their implications for policy learning. Feature-based methods offer dense, interpretable rewards that excel at high-fidelity motion imitation, yet often require sophisticated representations of references and struggle with generalization in unstructured settings. GAN-based methods, in contrast, use implicit, distributional supervision that enables scalability and adaptation flexibility, but are prone to training instability and coarse reward signals. Recent advancements in both paradigms converge on the importance of structured motion representations, which enable smoother transitions, controllable synthesis, and improved task integration. We argue that the dichotomy between feature-based and GAN-based methods is increasingly nuanced: rather than one paradigm dominating the other, the choice should be guided by task-specific priorities such as fidelity, diversity, interpretability, and adaptability. This work outlines the algorithmic trade-offs and design considerations that underlie method selection, offering a framework for principled decision-making in learning from demonstrations.

## 核心内容
This survey provides a comparative analysis of feature-based and GAN-based approaches to learning from demonstrations, with a focus on the structure of reward functions and their implications for policy learning. Feature-based methods offer dense, interpretable rewards that excel at high-fidelity motion imitation, yet often require sophisticated representations of references and struggle with generalization in unstructured settings. GAN-based methods, in contrast, use implicit, distributional supervision that enables scalability and adaptation flexibility, but are prone to training instability and coarse reward signals. Recent advancements in both paradigms converge on the importance of structured motion representations, which enable smoother transitions, controllable synthesis, and improved task integration. We argue that the dichotomy between feature-based and GAN-based methods is increasingly nuanced: rather than one paradigm dominating the other, the choice should be guided by task-specific priorities such as fidelity, diversity, interpretability, and adaptability. This work outlines the algorithmic trade-offs and design considerations that underlie method selection, offering a framework for principled decision-making in learning from demonstrations.

## 参考
- http://arxiv.org/abs/2507.05906v2

## Overview
This survey provides a comparative analysis of feature-based and GAN-based approaches to learning from demonstrations, with a focus on the structure of reward functions and their implications for policy learning. Feature-based methods offer dense, interpretable rewards that excel at high-fidelity motion imitation, yet often require sophisticated representations of references and struggle with generalization in unstructured settings. GAN-based methods, in contrast, use implicit, distributional supervision that enables scalability and adaptation flexibility, but are prone to training instability and coarse reward signals. Recent advancements in both paradigms converge on the importance of structured motion representations, which enable smoother transitions, controllable synthesis, and improved task integration. We argue that the dichotomy between feature-based and GAN-based methods is increasingly nuanced: rather than one paradigm dominating the other, the choice should be guided by task-specific priorities such as fidelity, diversity, interpretability, and adaptability. This work outlines the algorithmic trade-offs and design considerations that underlie method selection, offering a framework for principled decision-making in learning from demonstrations.

## Content
This survey provides a comparative analysis of feature-based and GAN-based approaches to learning from demonstrations, with a focus on the structure of reward functions and their implications for policy learning. Feature-based methods offer dense, interpretable rewards that excel at high-fidelity motion imitation, yet often require sophisticated representations of references and struggle with generalization in unstructured settings. GAN-based methods, in contrast, use implicit, distributional supervision that enables scalability and adaptation flexibility, but are prone to training instability and coarse reward signals. Recent advancements in both paradigms converge on the importance of structured motion representations, which enable smoother transitions, controllable synthesis, and improved task integration. We argue that the dichotomy between feature-based and GAN-based methods is increasingly nuanced: rather than one paradigm dominating the other, the choice should be guided by task-specific priorities such as fidelity, diversity, interpretability, and adaptability. This work outlines the algorithmic trade-offs and design considerations that underlie method selection, offering a framework for principled decision-making in learning from demonstrations.

## 개요
본 설문은 시연 학습에서 특징 기반 방법과 GAN 기반 방법을 비교 분석하며, 보상 함수의 구조와 정책 학습에 미치는 영향에 초점을 맞춥니다. 특징 기반 방법은 고충실도 동작 모방에 뛰어난 조밀하고 해석 가능한 보상을 제공하지만, 종종 정교한 참조 표현이 필요하고 비구조적 환경에서 일반화에 어려움을 겪습니다. 반면 GAN 기반 방법은 암시적이고 분포적인 감독을 사용하여 확장성과 적응 유연성을 가능하게 하지만, 훈련 불안정성과 거친 보상 신호에 취약합니다. 두 패러다임의 최근 발전은 구조화된 동작 표현의 중요성에 수렴하며, 이는 더 부드러운 전환, 제어 가능한 합성, 향상된 작업 통합을 가능하게 합니다. 우리는 특징 기반 방법과 GAN 기반 방법 간의 이분법이 점점 더 미묘해지고 있다고 주장합니다. 한 패러다임이 다른 패러다임을 지배하기보다는, 충실도, 다양성, 해석 가능성, 적응성과 같은 작업별 우선순위에 따라 선택이 이루어져야 합니다. 본 연구는 방법 선택의 기저에 있는 알고리즘적 트레이드오프와 설계 고려 사항을 설명하며, 시연 학습에서 원칙적인 의사 결정을 위한 프레임워크를 제공합니다.

## 핵심 내용
본 설문은 시연 학습에서 특징 기반 방법과 GAN 기반 방법을 비교 분석하며, 보상 함수의 구조와 정책 학습에 미치는 영향에 초점을 맞춥니다. 특징 기반 방법은 고충실도 동작 모방에 뛰어난 조밀하고 해석 가능한 보상을 제공하지만, 종종 정교한 참조 표현이 필요하고 비구조적 환경에서 일반화에 어려움을 겪습니다. 반면 GAN 기반 방법은 암시적이고 분포적인 감독을 사용하여 확장성과 적응 유연성을 가능하게 하지만, 훈련 불안정성과 거친 보상 신호에 취약합니다. 두 패러다임의 최근 발전은 구조화된 동작 표현의 중요성에 수렴하며, 이는 더 부드러운 전환, 제어 가능한 합성, 향상된 작업 통합을 가능하게 합니다. 우리는 특징 기반 방법과 GAN 기반 방법 간의 이분법이 점점 더 미묘해지고 있다고 주장합니다. 한 패러다임이 다른 패러다임을 지배하기보다는, 충실도, 다양성, 해석 가능성, 적응성과 같은 작업별 우선순위에 따라 선택이 이루어져야 합니다. 본 연구는 방법 선택의 기저에 있는 알고리즘적 트레이드오프와 설계 고려 사항을 설명하며, 시연 학습에서 원칙적인 의사 결정을 위한 프레임워크를 제공합니다.
