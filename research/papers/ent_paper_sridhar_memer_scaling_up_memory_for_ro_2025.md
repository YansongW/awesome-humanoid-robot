---
$id: ent_paper_sridhar_memer_scaling_up_memory_for_ro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval'
  zh: MemER
  ko: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval'
summary:
  en: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (MemER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University.'
  zh: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (MemER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University.'
  ko: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (MemER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University.'
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
- memer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.20328v1.
sources:
- id: src_001
  type: paper
  title: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (arXiv)'
  url: https://arxiv.org/abs/2510.20328
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MemER source
  url: https://doi.org/10.48550/arXiv.2510.20328
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans routinely rely on memory to perform tasks, yet most robot policies lack this capability; our goal is to endow robot policies with the same ability. Naively conditioning on long observation histories is computationally expensive and brittle under covariate shift, while indiscriminate subsampling of history leads to irrelevant or redundant information. We propose a hierarchical policy framework, where the high-level policy is trained to select and track previous relevant keyframes from its experience. The high-level policy uses selected keyframes and the most recent frames when generating text instructions for a low-level policy to execute. This design is compatible with existing vision-language-action (VLA) models and enables the system to efficiently reason over long-horizon dependencies. In our experiments, we finetune Qwen2.5-VL-7B-Instruct and $π_{0.5}$ as the high-level and low-level policies respectively, using demonstrations supplemented with minimal language annotations. Our approach, MemER, outperforms prior methods on three real-world long-horizon robotic manipulation tasks that require minutes of memory. Videos and code can be found at https://jen-pan.github.io/memer/.

## 核心内容
Humans routinely rely on memory to perform tasks, yet most robot policies lack this capability; our goal is to endow robot policies with the same ability. Naively conditioning on long observation histories is computationally expensive and brittle under covariate shift, while indiscriminate subsampling of history leads to irrelevant or redundant information. We propose a hierarchical policy framework, where the high-level policy is trained to select and track previous relevant keyframes from its experience. The high-level policy uses selected keyframes and the most recent frames when generating text instructions for a low-level policy to execute. This design is compatible with existing vision-language-action (VLA) models and enables the system to efficiently reason over long-horizon dependencies. In our experiments, we finetune Qwen2.5-VL-7B-Instruct and $π_{0.5}$ as the high-level and low-level policies respectively, using demonstrations supplemented with minimal language annotations. Our approach, MemER, outperforms prior methods on three real-world long-horizon robotic manipulation tasks that require minutes of memory. Videos and code can be found at https://jen-pan.github.io/memer/.

## 参考
- http://arxiv.org/abs/2510.20328v1

## Overview
Humans routinely rely on memory to perform tasks, yet most robot policies lack this capability; our goal is to endow robot policies with the same ability. Naively conditioning on long observation histories is computationally expensive and brittle under covariate shift, while indiscriminate subsampling of history leads to irrelevant or redundant information. We propose a hierarchical policy framework, where the high-level policy is trained to select and track previous relevant keyframes from its experience. The high-level policy uses selected keyframes and the most recent frames when generating text instructions for a low-level policy to execute. This design is compatible with existing vision-language-action (VLA) models and enables the system to efficiently reason over long-horizon dependencies. In our experiments, we finetune Qwen2.5-VL-7B-Instruct and $π_{0.5}$ as the high-level and low-level policies respectively, using demonstrations supplemented with minimal language annotations. Our approach, MemER, outperforms prior methods on three real-world long-horizon robotic manipulation tasks that require minutes of memory. Videos and code can be found at https://jen-pan.github.io/memer/.

## Content
Humans routinely rely on memory to perform tasks, yet most robot policies lack this capability; our goal is to endow robot policies with the same ability. Naively conditioning on long observation histories is computationally expensive and brittle under covariate shift, while indiscriminate subsampling of history leads to irrelevant or redundant information. We propose a hierarchical policy framework, where the high-level policy is trained to select and track previous relevant keyframes from its experience. The high-level policy uses selected keyframes and the most recent frames when generating text instructions for a low-level policy to execute. This design is compatible with existing vision-language-action (VLA) models and enables the system to efficiently reason over long-horizon dependencies. In our experiments, we finetune Qwen2.5-VL-7B-Instruct and $π_{0.5}$ as the high-level and low-level policies respectively, using demonstrations supplemented with minimal language annotations. Our approach, MemER, outperforms prior methods on three real-world long-horizon robotic manipulation tasks that require minutes of memory. Videos and code can be found at https://jen-pan.github.io/memer/.

## 개요
인간은 작업을 수행할 때 일상적으로 기억에 의존하지만, 대부분의 로봇 정책에는 이러한 능력이 부족합니다. 본 연구의 목표는 로봇 정책에 동일한 능력을 부여하는 것입니다. 긴 관찰 이력을 단순히 조건화하는 것은 계산 비용이 많이 들고 공변량 이동(covariate shift)에 취약하며, 이력을 무분별하게 서브샘플링하면 관련 없거나 중복된 정보가 발생합니다. 우리는 계층적 정책 프레임워크를 제안합니다. 여기서 상위 수준 정책은 경험에서 이전의 관련 키프레임을 선택하고 추적하도록 훈련됩니다. 상위 수준 정책은 하위 수준 정책이 실행할 텍스트 명령을 생성할 때 선택된 키프레임과 가장 최근 프레임을 사용합니다. 이 설계는 기존의 시각-언어-행동(VLA) 모델과 호환되며, 시스템이 장기 의존성을 효율적으로 추론할 수 있게 합니다. 실험에서 우리는 Qwen2.5-VL-7B-Instruct와 $π_{0.5}$를 각각 상위 수준 및 하위 수준 정책으로 미세 조정했으며, 최소한의 언어 주석이 추가된 시연 데이터를 사용했습니다. 우리의 접근 방식인 MemER는 수 분의 기억을 필요로 하는 세 가지 실제 장기 로봇 조작 작업에서 이전 방법보다 뛰어난 성능을 보였습니다. 비디오와 코드는 https://jen-pan.github.io/memer/에서 확인할 수 있습니다.

## 핵심 내용
인간은 작업을 수행할 때 일상적으로 기억에 의존하지만, 대부분의 로봇 정책에는 이러한 능력이 부족합니다. 본 연구의 목표는 로봇 정책에 동일한 능력을 부여하는 것입니다. 긴 관찰 이력을 단순히 조건화하는 것은 계산 비용이 많이 들고 공변량 이동(covariate shift)에 취약하며, 이력을 무분별하게 서브샘플링하면 관련 없거나 중복된 정보가 발생합니다. 우리는 계층적 정책 프레임워크를 제안합니다. 여기서 상위 수준 정책은 경험에서 이전의 관련 키프레임을 선택하고 추적하도록 훈련됩니다. 상위 수준 정책은 하위 수준 정책이 실행할 텍스트 명령을 생성할 때 선택된 키프레임과 가장 최근 프레임을 사용합니다. 이 설계는 기존의 시각-언어-행동(VLA) 모델과 호환되며, 시스템이 장기 의존성을 효율적으로 추론할 수 있게 합니다. 실험에서 우리는 Qwen2.5-VL-7B-Instruct와 $π_{0.5}$를 각각 상위 수준 및 하위 수준 정책으로 미세 조정했으며, 최소한의 언어 주석이 추가된 시연 데이터를 사용했습니다. 우리의 접근 방식인 MemER는 수 분의 기억을 필요로 하는 세 가지 실제 장기 로봇 조작 작업에서 이전 방법보다 뛰어난 성능을 보였습니다. 비디오와 코드는 https://jen-pan.github.io/memer/에서 확인할 수 있습니다.
