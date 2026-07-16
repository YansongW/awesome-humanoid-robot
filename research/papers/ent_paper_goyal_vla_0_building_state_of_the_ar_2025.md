---
$id: ent_paper_goyal_vla_0_building_state_of_the_ar_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification'
  zh: VLA-0
  ko: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification'
summary:
  en: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (VLA-0), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Nvidia.'
  zh: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (VLA-0), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Nvidia.'
  ko: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (VLA-0), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Nvidia.'
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
- vla_0
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13054v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (arXiv)'
  url: https://arxiv.org/abs/2510.13054
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-0 source
  url: https://doi.org/10.48550/arXiv.2510.13054
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action models (VLAs) hold immense promise for enabling generalist robot manipulation. However, the best way to build them remains an open question. Current approaches often add complexity, such as modifying the existing vocabulary of a Vision-Language Model (VLM) with action tokens or introducing special action heads. Curiously, the simplest strategy of representing actions directly as text has remained largely unexplored. This work introduces VLA-0 to investigate this idea. We find that VLA-0 is not only effective; it is surprisingly powerful. With the right design, VLA-0 outperforms more involved models. On LIBERO, a popular benchmark for evaluating VLAs, VLA-0 outperforms all existing methods trained on the same robotic data, including $π_0.5$-KI, OpenVLA-OFT and SmolVLA. Furthermore, without large-scale robotics-specific training, it outperforms methods trained on large-scale robotic data, like $π_0.5$-KI, $π_0$, GR00T-N1 and MolmoAct. These findings also translate to the real world, where VLA-0 outperforms SmolVLA, a VLA model pre-trained on large-scale real data. This paper summarizes our unexpected findings and spells out the specific techniques required to unlock the high performance of this simple yet potent VLA design. Visual results, code, and trained models are provided here: https://vla0.github.io/.

## 核心内容
Vision-Language-Action models (VLAs) hold immense promise for enabling generalist robot manipulation. However, the best way to build them remains an open question. Current approaches often add complexity, such as modifying the existing vocabulary of a Vision-Language Model (VLM) with action tokens or introducing special action heads. Curiously, the simplest strategy of representing actions directly as text has remained largely unexplored. This work introduces VLA-0 to investigate this idea. We find that VLA-0 is not only effective; it is surprisingly powerful. With the right design, VLA-0 outperforms more involved models. On LIBERO, a popular benchmark for evaluating VLAs, VLA-0 outperforms all existing methods trained on the same robotic data, including $π_0.5$-KI, OpenVLA-OFT and SmolVLA. Furthermore, without large-scale robotics-specific training, it outperforms methods trained on large-scale robotic data, like $π_0.5$-KI, $π_0$, GR00T-N1 and MolmoAct. These findings also translate to the real world, where VLA-0 outperforms SmolVLA, a VLA model pre-trained on large-scale real data. This paper summarizes our unexpected findings and spells out the specific techniques required to unlock the high performance of this simple yet potent VLA design. Visual results, code, and trained models are provided here: https://vla0.github.io/.

## 参考
- http://arxiv.org/abs/2510.13054v1

## Overview
Vision-Language-Action models (VLAs) hold immense promise for enabling generalist robot manipulation. However, the best way to build them remains an open question. Current approaches often add complexity, such as modifying the existing vocabulary of a Vision-Language Model (VLM) with action tokens or introducing special action heads. Curiously, the simplest strategy of representing actions directly as text has remained largely unexplored. This work introduces VLA-0 to investigate this idea. We find that VLA-0 is not only effective; it is surprisingly powerful. With the right design, VLA-0 outperforms more involved models. On LIBERO, a popular benchmark for evaluating VLAs, VLA-0 outperforms all existing methods trained on the same robotic data, including $π_0.5$-KI, OpenVLA-OFT and SmolVLA. Furthermore, without large-scale robotics-specific training, it outperforms methods trained on large-scale robotic data, like $π_0.5$-KI, $π_0$, GR00T-N1 and MolmoAct. These findings also translate to the real world, where VLA-0 outperforms SmolVLA, a VLA model pre-trained on large-scale real data. This paper summarizes our unexpected findings and spells out the specific techniques required to unlock the high performance of this simple yet potent VLA design. Visual results, code, and trained models are provided here: https://vla0.github.io/.

## Content
Vision-Language-Action models (VLAs) hold immense promise for enabling generalist robot manipulation. However, the best way to build them remains an open question. Current approaches often add complexity, such as modifying the existing vocabulary of a Vision-Language Model (VLM) with action tokens or introducing special action heads. Curiously, the simplest strategy of representing actions directly as text has remained largely unexplored. This work introduces VLA-0 to investigate this idea. We find that VLA-0 is not only effective; it is surprisingly powerful. With the right design, VLA-0 outperforms more involved models. On LIBERO, a popular benchmark for evaluating VLAs, VLA-0 outperforms all existing methods trained on the same robotic data, including $π_0.5$-KI, OpenVLA-OFT and SmolVLA. Furthermore, without large-scale robotics-specific training, it outperforms methods trained on large-scale robotic data, like $π_0.5$-KI, $π_0$, GR00T-N1 and MolmoAct. These findings also translate to the real world, where VLA-0 outperforms SmolVLA, a VLA model pre-trained on large-scale real data. This paper summarizes our unexpected findings and spells out the specific techniques required to unlock the high performance of this simple yet potent VLA design. Visual results, code, and trained models are provided here: https://vla0.github.io/.

## 개요
Vision-Language-Action 모델(VLA)은 범용 로봇 조작을 가능하게 하는 데 큰 잠재력을 지니고 있습니다. 그러나 이를 구축하는 최적의 방법은 여전히 미해결 과제로 남아 있습니다. 현재 접근 방식은 기존 Vision-Language Model(VLM)의 어휘에 액션 토큰을 추가하거나 특수 액션 헤드를 도입하는 등 복잡성을 더하는 경우가 많습니다. 흥미롭게도, 액션을 직접 텍스트로 표현하는 가장 간단한 전략은 거의 탐구되지 않았습니다. 본 연구에서는 이 아이디어를 조사하기 위해 VLA-0을 소개합니다. 우리는 VLA-0이 효과적일 뿐만 아니라 놀라울 정도로 강력하다는 사실을 발견했습니다. 적절한 설계를 통해 VLA-0은 더 복잡한 모델보다 뛰어난 성능을 보입니다. VLA 평가를 위한 인기 벤치마크인 LIBERO에서 VLA-0은 동일한 로봇 데이터로 학습된 모든 기존 방법($π_0.5$-KI, OpenVLA-OFT, SmolVLA 포함)을 능가합니다. 또한, 대규모 로봇 특화 학습 없이도 $π_0.5$-KI, $π_0$, GR00T-N1, MolmoAct와 같은 대규모 로봇 데이터로 학습된 방법보다 우수한 성능을 보입니다. 이러한 결과는 실제 환경에서도 확인되며, VLA-0은 대규모 실제 데이터로 사전 학습된 VLA 모델인 SmolVLA를 능가합니다. 본 논문은 예상치 못한 발견을 요약하고, 이 단순하면서도 강력한 VLA 설계의 높은 성능을 구현하는 데 필요한 구체적인 기술을 설명합니다. 시각적 결과, 코드, 학습된 모델은 다음에서 확인할 수 있습니다: https://vla0.github.io/.

## 핵심 내용
Vision-Language-Action 모델(VLA)은 범용 로봇 조작을 가능하게 하는 데 큰 잠재력을 지니고 있습니다. 그러나 이를 구축하는 최적의 방법은 여전히 미해결 과제로 남아 있습니다. 현재 접근 방식은 기존 Vision-Language Model(VLM)의 어휘에 액션 토큰을 추가하거나 특수 액션 헤드를 도입하는 등 복잡성을 더하는 경우가 많습니다. 흥미롭게도, 액션을 직접 텍스트로 표현하는 가장 간단한 전략은 거의 탐구되지 않았습니다. 본 연구에서는 이 아이디어를 조사하기 위해 VLA-0을 소개합니다. 우리는 VLA-0이 효과적일 뿐만 아니라 놀라울 정도로 강력하다는 사실을 발견했습니다. 적절한 설계를 통해 VLA-0은 더 복잡한 모델보다 뛰어난 성능을 보입니다. VLA 평가를 위한 인기 벤치마크인 LIBERO에서 VLA-0은 동일한 로봇 데이터로 학습된 모든 기존 방법($π_0.5$-KI, OpenVLA-OFT, SmolVLA 포함)을 능가합니다. 또한, 대규모 로봇 특화 학습 없이도 $π_0.5$-KI, $π_0$, GR00T-N1, MolmoAct와 같은 대규모 로봇 데이터로 학습된 방법보다 우수한 성능을 보입니다. 이러한 결과는 실제 환경에서도 확인되며, VLA-0은 대규모 실제 데이터로 사전 학습된 VLA 모델인 SmolVLA를 능가합니다. 본 논문은 예상치 못한 발견을 요약하고, 이 단순하면서도 강력한 VLA 설계의 높은 성능을 구현하는 데 필요한 구체적인 기술을 설명합니다. 시각적 결과, 코드, 학습된 모델은 다음에서 확인할 수 있습니다: https://vla0.github.io/.
