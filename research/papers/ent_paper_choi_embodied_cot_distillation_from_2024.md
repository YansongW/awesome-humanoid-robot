---
$id: ent_paper_choi_embodied_cot_distillation_from_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodied CoT Distillation From LLM To Off-the-shelf Agents
  zh: Embodied CoT Distillation From LLM To Off-the-shelf Agents
  ko: Embodied CoT Distillation From LLM To Off-the-shelf Agents
summary:
  en: Embodied CoT Distillation From LLM To Off-the-shelf Agents (Embodied CoT Distillation From LLM To Off-the-shelf Agents),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Sungkyunkwan University, Department
    of Computer Science and Engineering, Sungkyunkwan University, and published at ICML 2024.
  zh: DeDer 是一个由成均馆大学计算机科学系提出的框架，旨在将大型语言模型（LLM）的具身推理能力蒸馏至小型语言模型（sLM）中，用于机器人操作任务。其核心贡献在于通过分层策略（推理-规划）和具身知识图谱，使sLM能在ALFRED基准上超越领先的语言规划与蒸馏方法，实现高效部署。
  ko: Embodied CoT Distillation From LLM To Off-the-shelf Agents (Embodied CoT Distillation From LLM To Off-the-shelf Agents),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Sungkyunkwan University, Department
    of Computer Science and Engineering, Sungkyunkwan University, and published at ICML 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodied_cot_distillation_from
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.11499v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (850 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Embodied CoT Distillation From LLM To Off-the-shelf Agents source
  url: https://openreview.net/forum?id=M4Htd52HMH
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
DeDer 框架通过将LLM的决策过程分解为推理策略与规划策略，解决了在容量受限设备上执行复杂具身任务的挑战。推理策略从LLM的具身上下文学习与自我验证生成的数据中蒸馏而来，能生成有效推理；规划策略则基于这些推理高效生成优化计划。为提升推理质量，DeDer 引入了具身知识图谱，并通过对比提示注意力模型实现单次推理生成多条推理。实验表明，基于sLM的DeDer在ALFRED基准上表现优于现有方法。

## 核心内容
### 方法架构
- **分层策略**：DeDer 将LLM的决策过程重构为两层：
  - **推理策略（Reasoning-policy）**：从LLM通过具身上下文学习与自我验证生成的数据中蒸馏，输出中间推理（rationales）。
  - **规划策略（Planning-policy）**：以推理为指导，高效生成可执行计划。
- **关键组件**：
  - **具身知识图谱（Embodied Knowledge Graph）**：增强中间推理质量，使其更贴合具身任务。
  - **对比提示注意力模型（Contrastively Prompted Attention Model）**：通过单次推理生成多条推理，提升效率。

### 实验设置
- **基准**：ALFRED（具身任务导航与操作基准）。
- **对比方法**：领先的语言规划方法（如LLM-based planners）与蒸馏方法（如直接蒸馏LLM至sLM）。
- **部署设备**：容量受限的现成设备（off-the-shelf devices）。

### 关键结果
- DeDer 在ALFRED上的成功率与效率均超越所有对比方法，验证了sLM策略的适用性。
- 蒸馏后的sLM在推理生成速度上显著优于LLM，同时保持任务完成质量。

### 结论
DeDer 证明了通过分层蒸馏与知识图谱增强，sLM可以替代LLM在具身任务中实现高效决策，为资源受限场景下的机器人操作提供了可行方案。

## Overview
We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

## 参考
- http://arxiv.org/abs/2412.11499v1

## 개요
DeDer 프레임워크는 LLM의 의사 결정 과정을 추론 전략과 계획 전략으로 분해하여, 용량이 제한된 장치에서 복잡한 구현 작업을 수행하는 과제를 해결합니다. 추론 전략은 LLM의 구현 맥락 학습과 자기 검증으로 생성된 데이터에서 증류되어 유효한 추론을 생성할 수 있으며, 계획 전략은 이러한 추론을 기반으로 최적화된 계획을 효율적으로 생성합니다. 추론 품질을 향상시키기 위해 DeDer는 구현 지식 그래프를 도입하고, 대조 프롬프트 주의 모델을 통해 단일 추론으로 여러 추론을 생성합니다. 실험 결과, sLM 기반 DeDer는 ALFRED 벤치마크에서 기존 방법보다 우수한 성능을 보였습니다.

## 핵심 내용
### 방법 아키텍처
- **계층적 전략**: DeDer는 LLM의 의사 결정 과정을 두 계층으로 재구성합니다:
  - **추론 전략(Reasoning-policy)**: LLM이 구현 맥락 학습과 자기 검증으로 생성한 데이터에서 증류되어 중간 추론(rationales)을 출력합니다.
  - **계획 전략(Planning-policy)**: 추론을 지침으로 삼아 실행 가능한 계획을 효율적으로 생성합니다.
- **핵심 구성 요소**:
  - **구현 지식 그래프(Embodied Knowledge Graph)**: 중간 추론의 품질을 향상시켜 구현 작업에 더 적합하게 만듭니다.
  - **대조 프롬프트 주의 모델(Contrastively Prompted Attention Model)**: 단일 추론으로 여러 추론을 생성하여 효율성을 높입니다.

### 실험 설정
- **벤치마크**: ALFRED(구현 작업 내비게이션 및 조작 벤치마크).
- **비교 방법**: 선도적인 언어 계획 방법(예: LLM 기반 플래너) 및 증류 방법(예: LLM을 sLM으로 직접 증류).
- **배포 장치**: 용량이 제한된 기성 장치(off-the-shelf devices).

### 주요 결과
- DeDer는 ALFRED에서 성공률과 효율성 모두 모든 비교 방법을 능가하여 sLM 전략의 적용 가능성을 검증했습니다.
- 증류된 sLM은 추론 생성 속도에서 LLM보다 크게 우수하면서도 작업 완료 품질을 유지했습니다.

### 결론
DeDer는 계층적 증류와 지식 그래프 강화를 통해 sLM이 LLM을 대체하여 구현 작업에서 효율적인 의사 결정을 달성할 수 있음을 입증했으며, 자원 제한 시나리오에서의 로봇 조작에 실현 가능한 솔루션을 제공합니다.
