---
$id: ent_paper_mees_grounding_language_with_visual_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Grounding Language with Visual Affordances over Unstructured Data
  zh: HULC++
  ko: Grounding Language with Visual Affordances over Unstructured Data
summary:
  en: Grounding Language with Visual Affordances over Unstructured Data (HULC++), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Freiburg, University of Technology Nuremberg, and published
    at ICRA 2023.
  zh: HULC++ 是弗莱堡大学与纽伦堡工业大学于 2022 年提出的通用视觉-语言-动作模型，发表于 ICRA 2023。其核心贡献在于利用自监督视觉-语言可供性模型，仅需标注 1% 的数据即可从非结构化、离线且无需重置的真实世界数据中高效学习语言条件化机器人技能，并在
    CALVIN 基准上达到最优性能。
  ko: Grounding Language with Visual Affordances over Unstructured Data (HULC++), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Freiburg, University of Technology Nuremberg, and published
    at ICRA 2023.
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
- hulc
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.01911v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (791 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: HULC++ source
  url: https://doi.org/10.1109/ICRA48891.2023.10160396
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
HULC++ 通过自监督视觉-语言可供性模型，解决了传统机器人技能学习中需要大规模数据收集和频繁人工干预的问题。该方法仅需对 1% 的数据进行语言标注，即可从非结构化、离线且无需重置的真实世界数据中学习通用语言条件化技能。在模拟和真实世界的广泛实验中，HULC++ 在 CALVIN 基准上取得了最优性能，并能在真实世界中通过单一策略学习超过 25 种不同的视觉运动操作任务。结合大语言模型通过少样本提示将抽象自然语言指令分解为子目标后，该方法能以比先前方法少一个数量级的数据完成长时域、多层级任务。

## 核心内容
### 方法架构
HULC++ 的核心创新在于自监督视觉-语言可供性模型，该模型通过以下方式实现高效学习：
- **自监督训练**：利用视觉和语言之间的内在关联，仅需 1% 的数据进行语言标注，其余数据通过自监督方式学习视觉可供性。
- **语言条件化**：将自然语言指令与视觉特征对齐，使模型能够理解并执行多种语言描述的任务。

### 实验设置
- **基准测试**：在 CALVIN 基准上进行评估，该基准包含多种语言条件化操作任务。
- **真实世界任务**：学习超过 25 种不同的视觉运动操作任务，包括抓取、放置、推拉等。
- **数据效率**：与先前方法相比，所需数据量减少一个数量级。

### 关键结果
- **CALVIN 基准**：达到最优性能，显著优于现有方法。
- **真实世界表现**：单一策略成功完成 25 种以上任务，且无需频繁人工干预。
- **长时域任务**：结合大语言模型后，能够通过少样本提示分解抽象指令，完成多层级、长时域任务。

### 结论
HULC++ 通过自监督视觉-语言可供性模型，显著降低了机器人技能学习对标注数据和人工干预的依赖，为通用机器人操作提供了高效、可扩展的解决方案。代码和视频已开源。

## Overview
Recent works have shown that Large Language Models (LLMs) can be applied to ground natural language to a wide variety of robot skills. However, in practice, learning multi-task, language-conditioned robotic skills typically requires large-scale data collection and frequent human intervention to reset the environment or help correcting the current policies. In this work, we propose a novel approach to efficiently learn general-purpose language-conditioned robot skills from unstructured, offline and reset-free data in the real world by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language. We evaluate our method in extensive experiments both in simulated and real-world robotic tasks, achieving state-of-the-art performance on the challenging CALVIN benchmark and learning over 25 distinct visuomotor manipulation tasks with a single policy in the real world. We find that when paired with LLMs to break down abstract natural language instructions into subgoals via few-shot prompting, our method is capable of completing long-horizon, multi-tier tasks in the real world, while requiring an order of magnitude less data than previous approaches. Code and videos are available at http://hulc2.cs.uni-freiburg.de

## 参考
- http://arxiv.org/abs/2210.01911v3

## 개요
HULC++는 자기지도 시각-언어 어포던스 모델을 통해 전통적인 로봇 스킬 학습에서 요구되는 대규모 데이터 수집과 빈번한 인간 개입 문제를 해결합니다. 이 방법은 데이터의 1%만 언어로 주석을 달아 비구조화되고 오프라인이며 리셋이 필요 없는 실제 세계 데이터에서 일반적인 언어 조건화 스킬을 학습할 수 있습니다. 시뮬레이션과 실제 세계의 광범위한 실험에서 HULC++는 CALVIN 벤치마크에서 최적의 성능을 달성했으며, 실제 세계에서 단일 정책으로 25가지 이상의 다양한 시각-운동 조작 작업을 학습할 수 있습니다. 대규모 언어 모델을 결합하여 소수 샷 프롬프트를 통해 추상적인 자연어 명령을 하위 목표로 분해하면, 이 방법은 이전 방법보다 한 자릿수 적은 데이터로 장시간, 다계층 작업을 완료할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
HULC++의 핵심 혁신은 자기지도 시각-언어 어포던스 모델로, 다음 방식을 통해 효율적인 학습을 구현합니다:
- **자기지도 훈련**: 시각과 언어 간의 내재적 연관성을 활용하여 데이터의 1%만 언어로 주석을 달고, 나머지 데이터는 자기지도 방식으로 시각 어포던스를 학습합니다.
- **언어 조건화**: 자연어 명령을 시각적 특징과 정렬하여 모델이 다양한 언어로 설명된 작업을 이해하고 실행할 수 있게 합니다.

### 실험 설정
- **벤치마크 테스트**: 다양한 언어 조건화 조작 작업을 포함하는 CALVIN 벤치마크에서 평가합니다.
- **실제 세계 작업**: 잡기, 놓기, 밀기, 당기기 등 25가지 이상의 다양한 시각-운동 조작 작업을 학습합니다.
- **데이터 효율성**: 이전 방법과 비교하여 필요한 데이터 양이 한 자릿수 감소합니다.

### 주요 결과
- **CALVIN 벤치마크**: 최적의 성능을 달성하여 기존 방법보다 현저히 우수합니다.
- **실제 세계 성능**: 단일 정책으로 25가지 이상의 작업을 성공적으로 완료하며 빈번한 인간 개입이 필요 없습니다.
- **장시간 작업**: 대규모 언어 모델을 결합하면 소수 샷 프롬프트를 통해 추상적인 명령을 분해하여 다계층, 장시간 작업을 완료할 수 있습니다.

### 결론
HULC++는 자기지도 시각-언어 어포던스 모델을 통해 로봇 스킬 학습에서 주석 데이터와 인간 개입에 대한 의존도를 현저히 낮추어, 일반적인 로봇 조작을 위한 효율적이고 확장 가능한 솔루션을 제공합니다. 코드와 비디오는 오픈소스로 공개되었습니다.
