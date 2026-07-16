---
$id: ent_paper_lin_embodiedcoder_parameterized_em_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model'
  zh: EmbodiedCoder
  ko: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model'
summary:
  en: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (EmbodiedCoder), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by University of Chinese Academy of Sciences (UCAS),
    Institute of Automation, Chinese Academy of Sciences (CASIA), New Laboratory of Pattern Recognition (NLPR), State Key
    Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Beihang University, Chinese University of Hong Kong.'
  zh: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (EmbodiedCoder), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by University of Chinese Academy of Sciences (UCAS),
    Institute of Automation, Chinese Academy of Sciences (CASIA), New Laboratory of Pattern Recognition (NLPR), State Key
    Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Beihang University, Chinese University of Hong Kong.'
  ko: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (EmbodiedCoder), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by University of Chinese Academy of Sciences (UCAS),
    Institute of Automation, Chinese Academy of Sciences (CASIA), New Laboratory of Pattern Recognition (NLPR), State Key
    Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Beihang University, Chinese University of Hong Kong.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodiedcoder
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.06207v2.
sources:
- id: src_001
  type: paper
  title: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (arXiv)'
  url: https://arxiv.org/abs/2510.06207
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EmbodiedCoder source
  url: https://doi.org/10.48550/arXiv.2510.06207
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability.In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning.This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments.Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## 核心内容
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability.In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning.This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments.Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## 参考
- http://arxiv.org/abs/2510.06207v2

## Overview
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability. In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning. This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments. Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## Content
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability. In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning. This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments. Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## 개요
최근 로봇 제어 방법의 발전은 엔드투엔드 비전-언어-행동 프레임워크부터 사전 정의된 프리미티브를 갖춘 모듈식 시스템에 이르기까지, 로봇이 자연어 명령을 따르는 능력을 향상시켰습니다. 그럼에도 불구하고 많은 접근 방식은 대규모 주석 데이터셋에 의존하고 해석 가능성이 제한적이어서 다양한 환경으로 확장하는 데 여전히 어려움을 겪고 있습니다. 본 연구에서는 코딩 모델을 활용하여 실행 가능한 로봇 궤적을 직접 생성하는 훈련 없는 프레임워크인 EmbodiedCoder를 소개합니다. 고수준 명령을 코드에 기반함으로써 EmbodiedCoder는 추가 데이터 수집이나 미세 조정 없이 유연한 객체 형상 매개변수화와 조작 궤적 합성을 가능하게 합니다. 이 코딩 기반 패러다임은 인식과 조작을 연결하는 투명하고 일반화 가능한 방법을 제공합니다. 실제 모바일 로봇 실험에서 EmbodiedCoder는 다양한 장기 작업에서 강력한 성능을 달성하고 새로운 객체와 환경에 효과적으로 일반화됨을 보여줍니다. 우리의 결과는 고수준 추론과 저수준 제어를 연결하는 해석 가능한 접근 방식을 입증하며, 고정된 프리미티브를 넘어 다재다능한 로봇 지능으로 나아갑니다. 프로젝트 페이지: https://embodiedcoder.github.io/EmbodiedCoder/

## 핵심 내용
최근 로봇 제어 방법의 발전은 엔드투엔드 비전-언어-행동 프레임워크부터 사전 정의된 프리미티브를 갖춘 모듈식 시스템에 이르기까지, 로봇이 자연어 명령을 따르는 능력을 향상시켰습니다. 그럼에도 불구하고 많은 접근 방식은 대규모 주석 데이터셋에 의존하고 해석 가능성이 제한적이어서 다양한 환경으로 확장하는 데 여전히 어려움을 겪고 있습니다. 본 연구에서는 코딩 모델을 활용하여 실행 가능한 로봇 궤적을 직접 생성하는 훈련 없는 프레임워크인 EmbodiedCoder를 소개합니다. 고수준 명령을 코드에 기반함으로써 EmbodiedCoder는 추가 데이터 수집이나 미세 조정 없이 유연한 객체 형상 매개변수화와 조작 궤적 합성을 가능하게 합니다. 이 코딩 기반 패러다임은 인식과 조작을 연결하는 투명하고 일반화 가능한 방법을 제공합니다. 실제 모바일 로봇 실험에서 EmbodiedCoder는 다양한 장기 작업에서 강력한 성능을 달성하고 새로운 객체와 환경에 효과적으로 일반화됨을 보여줍니다. 우리의 결과는 고수준 추론과 저수준 제어를 연결하는 해석 가능한 접근 방식을 입증하며, 고정된 프리미티브를 넘어 다재다능한 로봇 지능으로 나아갑니다. 프로젝트 페이지: https://embodiedcoder.github.io/EmbodiedCoder/
