---
$id: ent_paper_guhur_instruction_driven_history_awa_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Instruction-driven history-aware policies for robotic manipulations
  zh: Hiveformer
  ko: Instruction-driven history-aware policies for robotic manipulations
summary:
  en: Instruction-driven history-aware policies for robotic manipulations (Hiveformer), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Inria, École normale supérieure, CNRS, PSL Research University, IIIT Hyderabad,
    and published at CoRL 2022.
  zh: Instruction-driven history-aware policies for robotic manipulations (Hiveformer), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Inria, École normale supérieure, CNRS, PSL Research University, IIIT Hyderabad,
    and published at CoRL 2022.
  ko: Instruction-driven history-aware policies for robotic manipulations (Hiveformer), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Inria, École normale supérieure, CNRS, PSL Research University, IIIT Hyderabad,
    and published at CoRL 2022.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- hiveformer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.04899v3.
sources:
- id: src_001
  type: paper
  title: Hiveformer source
  url: https://proceedings.mlr.press/v205/guhur23a.html
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
In human environments, robots are expected to accomplish a variety of manipulation tasks given simple natural language instructions. Yet, robotic manipulation is extremely challenging as it requires fine-grained motor control, long-term memory as well as generalization to previously unseen tasks and environments. To address these challenges, we propose a unified transformer-based approach that takes into account multiple inputs. In particular, our transformer architecture integrates (i) natural language instructions and (ii) multi-view scene observations while (iii) keeping track of the full history of observations and actions. Such an approach enables learning dependencies between history and instructions and improves manipulation precision using multiple views. We evaluate our method on the challenging RLBench benchmark and on a real-world robot. Notably, our approach scales to 74 diverse RLBench tasks and outperforms the state of the art. We also address instruction-conditioned tasks and demonstrate excellent generalization to previously unseen variations.

## 核心内容
In human environments, robots are expected to accomplish a variety of manipulation tasks given simple natural language instructions. Yet, robotic manipulation is extremely challenging as it requires fine-grained motor control, long-term memory as well as generalization to previously unseen tasks and environments. To address these challenges, we propose a unified transformer-based approach that takes into account multiple inputs. In particular, our transformer architecture integrates (i) natural language instructions and (ii) multi-view scene observations while (iii) keeping track of the full history of observations and actions. Such an approach enables learning dependencies between history and instructions and improves manipulation precision using multiple views. We evaluate our method on the challenging RLBench benchmark and on a real-world robot. Notably, our approach scales to 74 diverse RLBench tasks and outperforms the state of the art. We also address instruction-conditioned tasks and demonstrate excellent generalization to previously unseen variations.

## 参考
- http://arxiv.org/abs/2209.04899v3

## Overview
In human environments, robots are expected to accomplish a variety of manipulation tasks given simple natural language instructions. Yet, robotic manipulation is extremely challenging as it requires fine-grained motor control, long-term memory as well as generalization to previously unseen tasks and environments. To address these challenges, we propose a unified transformer-based approach that takes into account multiple inputs. In particular, our transformer architecture integrates (i) natural language instructions and (ii) multi-view scene observations while (iii) keeping track of the full history of observations and actions. Such an approach enables learning dependencies between history and instructions and improves manipulation precision using multiple views. We evaluate our method on the challenging RLBench benchmark and on a real-world robot. Notably, our approach scales to 74 diverse RLBench tasks and outperforms the state of the art. We also address instruction-conditioned tasks and demonstrate excellent generalization to previously unseen variations.

## Content
In human environments, robots are expected to accomplish a variety of manipulation tasks given simple natural language instructions. Yet, robotic manipulation is extremely challenging as it requires fine-grained motor control, long-term memory as well as generalization to previously unseen tasks and environments. To address these challenges, we propose a unified transformer-based approach that takes into account multiple inputs. In particular, our transformer architecture integrates (i) natural language instructions and (ii) multi-view scene observations while (iii) keeping track of the full history of observations and actions. Such an approach enables learning dependencies between history and instructions and improves manipulation precision using multiple views. We evaluate our method on the challenging RLBench benchmark and on a real-world robot. Notably, our approach scales to 74 diverse RLBench tasks and outperforms the state of the art. We also address instruction-conditioned tasks and demonstrate excellent generalization to previously unseen variations.

## 개요
인간 환경에서 로봇은 간단한 자연어 명령을 통해 다양한 조작 작업을 수행할 것으로 기대됩니다. 그러나 로봇 조작은 세밀한 운동 제어, 장기 기억, 그리고 이전에 보지 못한 작업과 환경에 대한 일반화를 요구하기 때문에 매우 어렵습니다. 이러한 문제를 해결하기 위해, 우리는 여러 입력을 고려하는 통합 트랜스포머 기반 접근 방식을 제안합니다. 특히, 우리의 트랜스포머 아키텍처는 (i) 자연어 명령과 (ii) 다중 시점 장면 관측을 통합하면서 (iii) 관측과 행동의 전체 이력을 추적합니다. 이러한 접근 방식은 이력과 명령 간의 의존성을 학습하고, 다중 시점을 사용하여 조작 정밀도를 향상시킵니다. 우리는 이 방법을 까다로운 RLBench 벤치마크와 실제 로봇에서 평가했습니다. 특히, 우리의 접근 방식은 74개의 다양한 RLBench 작업으로 확장 가능하며 최첨단 성능을 능가합니다. 또한 명령 조건부 작업을 다루며 이전에 보지 못한 변형에 대한 뛰어난 일반화 능력을 입증했습니다.

## 핵심 내용
인간 환경에서 로봇은 간단한 자연어 명령을 통해 다양한 조작 작업을 수행할 것으로 기대됩니다. 그러나 로봇 조작은 세밀한 운동 제어, 장기 기억, 그리고 이전에 보지 못한 작업과 환경에 대한 일반화를 요구하기 때문에 매우 어렵습니다. 이러한 문제를 해결하기 위해, 우리는 여러 입력을 고려하는 통합 트랜스포머 기반 접근 방식을 제안합니다. 특히, 우리의 트랜스포머 아키텍처는 (i) 자연어 명령과 (ii) 다중 시점 장면 관측을 통합하면서 (iii) 관측과 행동의 전체 이력을 추적합니다. 이러한 접근 방식은 이력과 명령 간의 의존성을 학습하고, 다중 시점을 사용하여 조작 정밀도를 향상시킵니다. 우리는 이 방법을 까다로운 RLBench 벤치마크와 실제 로봇에서 평가했습니다. 특히, 우리의 접근 방식은 74개의 다양한 RLBench 작업으로 확장 가능하며 최첨단 성능을 능가합니다. 또한 명령 조건부 작업을 다루며 이전에 보지 못한 변형에 대한 뛰어난 일반화 능력을 입증했습니다.
