---
$id: ent_paper_example_based_motion_synthesis_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Example-based Motion Synthesis via Generative Motion Matching
  zh: Example-based Motion Synthesis via Generative Motion Matching
  ko: Example-based Motion Synthesis via Generative Motion Matching
summary:
  en: Example-based Motion Synthesis via Generative Motion Matching is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Example-based Motion Synthesis via Generative Motion Matching is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  ko: Example-based Motion Synthesis via Generative Motion Matching is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- example_based_motion_synthesis
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.00378v1.
sources:
- id: src_001
  type: paper
  title: Example-based Motion Synthesis via Generative Motion Matching (arXiv)
  url: https://arxiv.org/abs/2306.00378
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present GenMM, a generative model that "mines" as many diverse motions as possible from a single or few example sequences. In stark contrast to existing data-driven methods, which typically require long offline training time, are prone to visual artifacts, and tend to fail on large and complex skeletons, GenMM inherits the training-free nature and the superior quality of the well-known Motion Matching method. GenMM can synthesize a high-quality motion within a fraction of a second, even with highly complex and large skeletal structures. At the heart of our generative framework lies the generative motion matching module, which utilizes the bidirectional visual similarity as a generative cost function to motion matching, and operates in a multi-stage framework to progressively refine a random guess using exemplar motion matches. In addition to diverse motion generation, we show the versatility of our generative framework by extending it to a number of scenarios that are not possible with motion matching alone, including motion completion, key frame-guided generation, infinite looping, and motion reassembly. Code and data for this paper are at https://wyysf-98.github.io/GenMM/

## 核心内容
We present GenMM, a generative model that "mines" as many diverse motions as possible from a single or few example sequences. In stark contrast to existing data-driven methods, which typically require long offline training time, are prone to visual artifacts, and tend to fail on large and complex skeletons, GenMM inherits the training-free nature and the superior quality of the well-known Motion Matching method. GenMM can synthesize a high-quality motion within a fraction of a second, even with highly complex and large skeletal structures. At the heart of our generative framework lies the generative motion matching module, which utilizes the bidirectional visual similarity as a generative cost function to motion matching, and operates in a multi-stage framework to progressively refine a random guess using exemplar motion matches. In addition to diverse motion generation, we show the versatility of our generative framework by extending it to a number of scenarios that are not possible with motion matching alone, including motion completion, key frame-guided generation, infinite looping, and motion reassembly. Code and data for this paper are at https://wyysf-98.github.io/GenMM/

## 参考
- http://arxiv.org/abs/2306.00378v1

## Overview
We present GenMM, a generative model that "mines" as many diverse motions as possible from a single or few example sequences. In stark contrast to existing data-driven methods, which typically require long offline training time, are prone to visual artifacts, and tend to fail on large and complex skeletons, GenMM inherits the training-free nature and the superior quality of the well-known Motion Matching method. GenMM can synthesize a high-quality motion within a fraction of a second, even with highly complex and large skeletal structures. At the heart of our generative framework lies the generative motion matching module, which utilizes the bidirectional visual similarity as a generative cost function to motion matching, and operates in a multi-stage framework to progressively refine a random guess using exemplar motion matches. In addition to diverse motion generation, we show the versatility of our generative framework by extending it to a number of scenarios that are not possible with motion matching alone, including motion completion, key frame-guided generation, infinite looping, and motion reassembly. Code and data for this paper are at https://wyysf-98.github.io/GenMM/

## Content
We present GenMM, a generative model that "mines" as many diverse motions as possible from a single or few example sequences. In stark contrast to existing data-driven methods, which typically require long offline training time, are prone to visual artifacts, and tend to fail on large and complex skeletons, GenMM inherits the training-free nature and the superior quality of the well-known Motion Matching method. GenMM can synthesize a high-quality motion within a fraction of a second, even with highly complex and large skeletal structures. At the heart of our generative framework lies the generative motion matching module, which utilizes the bidirectional visual similarity as a generative cost function to motion matching, and operates in a multi-stage framework to progressively refine a random guess using exemplar motion matches. In addition to diverse motion generation, we show the versatility of our generative framework by extending it to a number of scenarios that are not possible with motion matching alone, including motion completion, key frame-guided generation, infinite looping, and motion reassembly. Code and data for this paper are at https://wyysf-98.github.io/GenMM/

## 개요
우리는 GenMM을 제시합니다. 이는 하나 또는 소수의 예제 시퀀스에서 가능한 한 다양한 모션을 "채굴"하는 생성 모델입니다. 일반적으로 긴 오프라인 학습 시간이 필요하고, 시각적 아티팩트가 발생하기 쉬우며, 크고 복잡한 골격에서 실패하는 경향이 있는 기존의 데이터 기반 방법들과는 대조적으로, GenMM은 잘 알려진 Motion Matching 방법의 학습 불필요성과 우수한 품질을 계승합니다. GenMM은 매우 복잡하고 큰 골격 구조에서도 1초 미만의 시간 내에 고품질 모션을 합성할 수 있습니다. 우리 생성 프레임워크의 핵심에는 생성적 모션 매칭 모듈이 있으며, 이는 양방향 시각적 유사성을 모션 매칭의 생성 비용 함수로 활용하고, 다단계 프레임워크에서 작동하여 예제 모션 매칭을 사용해 무작위 추측을 점진적으로 개선합니다. 다양한 모션 생성 외에도, 우리는 모션 완성, 키 프레임 기반 생성, 무한 루핑, 모션 재조립 등 모션 매칭만으로는 불가능한 여러 시나리오로 생성 프레임워크를 확장하여 그 다재다능함을 보여줍니다. 이 논문의 코드와 데이터는 https://wyysf-98.github.io/GenMM/ 에 있습니다.

## 핵심 내용
우리는 GenMM을 제시합니다. 이는 하나 또는 소수의 예제 시퀀스에서 가능한 한 다양한 모션을 "채굴"하는 생성 모델입니다. 일반적으로 긴 오프라인 학습 시간이 필요하고, 시각적 아티팩트가 발생하기 쉬우며, 크고 복잡한 골격에서 실패하는 경향이 있는 기존의 데이터 기반 방법들과는 대조적으로, GenMM은 잘 알려진 Motion Matching 방법의 학습 불필요성과 우수한 품질을 계승합니다. GenMM은 매우 복잡하고 큰 골격 구조에서도 1초 미만의 시간 내에 고품질 모션을 합성할 수 있습니다. 우리 생성 프레임워크의 핵심에는 생성적 모션 매칭 모듈이 있으며, 이는 양방향 시각적 유사성을 모션 매칭의 생성 비용 함수로 활용하고, 다단계 프레임워크에서 작동하여 예제 모션 매칭을 사용해 무작위 추측을 점진적으로 개선합니다. 다양한 모션 생성 외에도, 우리는 모션 완성, 키 프레임 기반 생성, 무한 루핑, 모션 재조립 등 모션 매칭만으로는 불가능한 여러 시나리오로 생성 프레임워크를 확장하여 그 다재다능함을 보여줍니다. 이 논문의 코드와 데이터는 https://wyysf-98.github.io/GenMM/ 에 있습니다.
