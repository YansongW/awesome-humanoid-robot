---
$id: ent_paper_cvpr_2025_oral_tokenhsi_unifie_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
  zh: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
  ko: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
summary:
  en: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization is a 2025
    work on physics-based character animation for humanoid robots.'
  zh: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization is a 2025
    work on physics-based character animation for humanoid robots.'
  ko: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization is a 2025
    work on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- cvpr_2025_oral_tokenhsi
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.19901v2.
sources:
- id: src_001
  type: paper
  title: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization (arXiv)'
  url: https://arxiv.org/abs/2503.19901
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization project
    page'
  url: https://liangpan99.github.io/TokenHSI/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Synthesizing diverse and physically plausible Human-Scene Interactions (HSI) is pivotal for both computer animation and embodied AI. Despite encouraging progress, current methods mainly focus on developing separate controllers, each specialized for a specific interaction task. This significantly hinders the ability to tackle a wide variety of challenging HSI tasks that require the integration of multiple skills, e.g., sitting down while carrying an object. To address this issue, we present TokenHSI, a single, unified transformer-based policy capable of multi-skill unification and flexible adaptation. The key insight is to model the humanoid proprioception as a separate shared token and combine it with distinct task tokens via a masking mechanism. Such a unified policy enables effective knowledge sharing across skills, thereby facilitating the multi-task training. Moreover, our policy architecture supports variable length inputs, enabling flexible adaptation of learned skills to new scenarios. By training additional task tokenizers, we can not only modify the geometries of interaction targets but also coordinate multiple skills to address complex tasks. The experiments demonstrate that our approach can significantly improve versatility, adaptability, and extensibility in various HSI tasks. Website: https://liangpan99.github.io/TokenHSI/

## 核心内容
Synthesizing diverse and physically plausible Human-Scene Interactions (HSI) is pivotal for both computer animation and embodied AI. Despite encouraging progress, current methods mainly focus on developing separate controllers, each specialized for a specific interaction task. This significantly hinders the ability to tackle a wide variety of challenging HSI tasks that require the integration of multiple skills, e.g., sitting down while carrying an object. To address this issue, we present TokenHSI, a single, unified transformer-based policy capable of multi-skill unification and flexible adaptation. The key insight is to model the humanoid proprioception as a separate shared token and combine it with distinct task tokens via a masking mechanism. Such a unified policy enables effective knowledge sharing across skills, thereby facilitating the multi-task training. Moreover, our policy architecture supports variable length inputs, enabling flexible adaptation of learned skills to new scenarios. By training additional task tokenizers, we can not only modify the geometries of interaction targets but also coordinate multiple skills to address complex tasks. The experiments demonstrate that our approach can significantly improve versatility, adaptability, and extensibility in various HSI tasks. Website: https://liangpan99.github.io/TokenHSI/

## 参考
- http://arxiv.org/abs/2503.19901v2

## Overview
Synthesizing diverse and physically plausible Human-Scene Interactions (HSI) is pivotal for both computer animation and embodied AI. Despite encouraging progress, current methods mainly focus on developing separate controllers, each specialized for a specific interaction task. This significantly hinders the ability to tackle a wide variety of challenging HSI tasks that require the integration of multiple skills, e.g., sitting down while carrying an object. To address this issue, we present TokenHSI, a single, unified transformer-based policy capable of multi-skill unification and flexible adaptation. The key insight is to model the humanoid proprioception as a separate shared token and combine it with distinct task tokens via a masking mechanism. Such a unified policy enables effective knowledge sharing across skills, thereby facilitating the multi-task training. Moreover, our policy architecture supports variable length inputs, enabling flexible adaptation of learned skills to new scenarios. By training additional task tokenizers, we can not only modify the geometries of interaction targets but also coordinate multiple skills to address complex tasks. The experiments demonstrate that our approach can significantly improve versatility, adaptability, and extensibility in various HSI tasks. Website: https://liangpan99.github.io/TokenHSI/

## Content
Synthesizing diverse and physically plausible Human-Scene Interactions (HSI) is pivotal for both computer animation and embodied AI. Despite encouraging progress, current methods mainly focus on developing separate controllers, each specialized for a specific interaction task. This significantly hinders the ability to tackle a wide variety of challenging HSI tasks that require the integration of multiple skills, e.g., sitting down while carrying an object. To address this issue, we present TokenHSI, a single, unified transformer-based policy capable of multi-skill unification and flexible adaptation. The key insight is to model the humanoid proprioception as a separate shared token and combine it with distinct task tokens via a masking mechanism. Such a unified policy enables effective knowledge sharing across skills, thereby facilitating the multi-task training. Moreover, our policy architecture supports variable length inputs, enabling flexible adaptation of learned skills to new scenarios. By training additional task tokenizers, we can not only modify the geometries of interaction targets but also coordinate multiple skills to address complex tasks. The experiments demonstrate that our approach can significantly improve versatility, adaptability, and extensibility in various HSI tasks. Website: https://liangpan99.github.io/TokenHSI/

## 개요
다양하고 물리적으로 타당한 인간-장면 상호작용(HSI)을 합성하는 것은 컴퓨터 애니메이션과 구현형 AI 모두에 핵심적입니다. 고무적인 진전에도 불구하고, 현재 방법들은 주로 각각 특정 상호작용 작업에 특화된 개별 제어기를 개발하는 데 초점을 맞추고 있습니다. 이는 물건을 들고 앉는 것과 같이 여러 기술의 통합이 필요한 다양한 도전적인 HSI 작업을 처리하는 능력을 크게 저해합니다. 이 문제를 해결하기 위해, 우리는 다중 기술 통합과 유연한 적응이 가능한 단일 통합 트랜스포머 기반 정책인 TokenHSI를 제시합니다. 핵심 통찰은 인간형 고유 감각(proprioception)을 별도의 공유 토큰으로 모델링하고, 마스킹 메커니즘을 통해 이를 고유한 작업 토큰과 결합하는 것입니다. 이러한 통합 정책은 기술 간 효과적인 지식 공유를 가능하게 하여 다중 작업 훈련을 촉진합니다. 또한, 우리의 정책 아키텍처는 가변 길이 입력을 지원하여 학습된 기술을 새로운 시나리오에 유연하게 적응시킬 수 있습니다. 추가적인 작업 토크나이저를 훈련함으로써 상호작용 대상의 기하학적 구조를 수정할 수 있을 뿐만 아니라 여러 기술을 조정하여 복잡한 작업을 처리할 수 있습니다. 실험 결과는 우리의 접근 방식이 다양한 HSI 작업에서 다재다능성, 적응성, 확장성을 크게 향상시킬 수 있음을 보여줍니다. 웹사이트: https://liangpan99.github.io/TokenHSI/

## 핵심 내용
다양하고 물리적으로 타당한 인간-장면 상호작용(HSI)을 합성하는 것은 컴퓨터 애니메이션과 구현형 AI 모두에 핵심적입니다. 고무적인 진전에도 불구하고, 현재 방법들은 주로 각각 특정 상호작용 작업에 특화된 개별 제어기를 개발하는 데 초점을 맞추고 있습니다. 이는 물건을 들고 앉는 것과 같이 여러 기술의 통합이 필요한 다양한 도전적인 HSI 작업을 처리하는 능력을 크게 저해합니다. 이 문제를 해결하기 위해, 우리는 다중 기술 통합과 유연한 적응이 가능한 단일 통합 트랜스포머 기반 정책인 TokenHSI를 제시합니다. 핵심 통찰은 인간형 고유 감각(proprioception)을 별도의 공유 토큰으로 모델링하고, 마스킹 메커니즘을 통해 이를 고유한 작업 토큰과 결합하는 것입니다. 이러한 통합 정책은 기술 간 효과적인 지식 공유를 가능하게 하여 다중 작업 훈련을 촉진합니다. 또한, 우리의 정책 아키텍처는 가변 길이 입력을 지원하여 학습된 기술을 새로운 시나리오에 유연하게 적응시킬 수 있습니다. 추가적인 작업 토크나이저를 훈련함으로써 상호작용 대상의 기하학적 구조를 수정할 수 있을 뿐만 아니라 여러 기술을 조정하여 복잡한 작업을 처리할 수 있습니다. 실험 결과는 우리의 접근 방식이 다양한 HSI 작업에서 다재다능성, 적응성, 확장성을 크게 향상시킬 수 있음을 보여줍니다. 웹사이트: https://liangpan99.github.io/TokenHSI/
