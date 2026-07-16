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
  zh: Grounding Language with Visual Affordances over Unstructured Data (HULC++), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Freiburg, University of Technology Nuremberg, and published
    at ICRA 2023.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.01911v3.
sources:
- id: src_001
  type: website
  title: HULC++ source
  url: https://doi.org/10.1109/ICRA48891.2023.10160396
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Recent works have shown that Large Language Models (LLMs) can be applied to ground natural language to a wide variety of robot skills. However, in practice, learning multi-task, language-conditioned robotic skills typically requires large-scale data collection and frequent human intervention to reset the environment or help correcting the current policies. In this work, we propose a novel approach to efficiently learn general-purpose language-conditioned robot skills from unstructured, offline and reset-free data in the real world by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language. We evaluate our method in extensive experiments both in simulated and real-world robotic tasks, achieving state-of-the-art performance on the challenging CALVIN benchmark and learning over 25 distinct visuomotor manipulation tasks with a single policy in the real world. We find that when paired with LLMs to break down abstract natural language instructions into subgoals via few-shot prompting, our method is capable of completing long-horizon, multi-tier tasks in the real world, while requiring an order of magnitude less data than previous approaches. Code and videos are available at http://hulc2.cs.uni-freiburg.de

## 核心内容
Recent works have shown that Large Language Models (LLMs) can be applied to ground natural language to a wide variety of robot skills. However, in practice, learning multi-task, language-conditioned robotic skills typically requires large-scale data collection and frequent human intervention to reset the environment or help correcting the current policies. In this work, we propose a novel approach to efficiently learn general-purpose language-conditioned robot skills from unstructured, offline and reset-free data in the real world by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language. We evaluate our method in extensive experiments both in simulated and real-world robotic tasks, achieving state-of-the-art performance on the challenging CALVIN benchmark and learning over 25 distinct visuomotor manipulation tasks with a single policy in the real world. We find that when paired with LLMs to break down abstract natural language instructions into subgoals via few-shot prompting, our method is capable of completing long-horizon, multi-tier tasks in the real world, while requiring an order of magnitude less data than previous approaches. Code and videos are available at http://hulc2.cs.uni-freiburg.de

## 参考
- http://arxiv.org/abs/2210.01911v3

## Overview
Recent works have shown that Large Language Models (LLMs) can be applied to ground natural language to a wide variety of robot skills. However, in practice, learning multi-task, language-conditioned robotic skills typically requires large-scale data collection and frequent human intervention to reset the environment or help correcting the current policies. In this work, we propose a novel approach to efficiently learn general-purpose language-conditioned robot skills from unstructured, offline and reset-free data in the real world by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language. We evaluate our method in extensive experiments both in simulated and real-world robotic tasks, achieving state-of-the-art performance on the challenging CALVIN benchmark and learning over 25 distinct visuomotor manipulation tasks with a single policy in the real world. We find that when paired with LLMs to break down abstract natural language instructions into subgoals via few-shot prompting, our method is capable of completing long-horizon, multi-tier tasks in the real world, while requiring an order of magnitude less data than previous approaches. Code and videos are available at http://hulc2.cs.uni-freiburg.de

## Content
Recent works have shown that Large Language Models (LLMs) can be applied to ground natural language to a wide variety of robot skills. However, in practice, learning multi-task, language-conditioned robotic skills typically requires large-scale data collection and frequent human intervention to reset the environment or help correcting the current policies. In this work, we propose a novel approach to efficiently learn general-purpose language-conditioned robot skills from unstructured, offline and reset-free data in the real world by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language. We evaluate our method in extensive experiments both in simulated and real-world robotic tasks, achieving state-of-the-art performance on the challenging CALVIN benchmark and learning over 25 distinct visuomotor manipulation tasks with a single policy in the real world. We find that when paired with LLMs to break down abstract natural language instructions into subgoals via few-shot prompting, our method is capable of completing long-horizon, multi-tier tasks in the real world, while requiring an order of magnitude less data than previous approaches. Code and videos are available at http://hulc2.cs.uni-freiburg.de

## 개요
최근 연구들은 대규모 언어 모델(LLM)이 자연어를 다양한 로봇 기술에 적용할 수 있음을 보여주었습니다. 그러나 실제로 다중 작업, 언어 조건부 로봇 기술을 학습하려면 일반적으로 대규모 데이터 수집과 환경 재설정 또는 현재 정책 수정을 위한 빈번한 인간 개입이 필요합니다. 본 연구에서는 자기 지도 시각-언어 어포던스 모델(self-supervised visuo-lingual affordance model)을 활용하여 실제 세계에서 구조화되지 않은 오프라인 및 리셋 없는 데이터로부터 범용 언어 조건부 로봇 기술을 효율적으로 학습하는 새로운 접근 방식을 제안합니다. 이 모델은 전체 데이터의 1%만 언어로 주석 처리하면 됩니다. 우리는 시뮬레이션 및 실제 로봇 작업에서 광범위한 실험을 통해 방법을 평가했으며, 까다로운 CALVIN 벤치마크에서 최첨단 성능을 달성하고 실제 세계에서 단일 정책으로 25개 이상의 다양한 시각운동 조작 작업을 학습했습니다. LLM과 결합하여 추상적인 자연어 명령을 소수의 예시 프롬프팅(few-shot prompting)을 통해 하위 목표로 분해할 때, 우리의 방법은 이전 접근 방식보다 훨씬 적은 데이터로 실제 세계에서 장기적이고 다계층 작업을 완료할 수 있음을 발견했습니다. 코드와 비디오는 http://hulc2.cs.uni-freiburg.de에서 확인할 수 있습니다.

## 핵심 내용
최근 연구들은 대규모 언어 모델(LLM)이 자연어를 다양한 로봇 기술에 적용할 수 있음을 보여주었습니다. 그러나 실제로 다중 작업, 언어 조건부 로봇 기술을 학습하려면 일반적으로 대규모 데이터 수집과 환경 재설정 또는 현재 정책 수정을 위한 빈번한 인간 개입이 필요합니다. 본 연구에서는 자기 지도 시각-언어 어포던스 모델(self-supervised visuo-lingual affordance model)을 활용하여 실제 세계에서 구조화되지 않은 오프라인 및 리셋 없는 데이터로부터 범용 언어 조건부 로봇 기술을 효율적으로 학습하는 새로운 접근 방식을 제안합니다. 이 모델은 전체 데이터의 1%만 언어로 주석 처리하면 됩니다. 우리는 시뮬레이션 및 실제 로봇 작업에서 광범위한 실험을 통해 방법을 평가했으며, 까다로운 CALVIN 벤치마크에서 최첨단 성능을 달성하고 실제 세계에서 단일 정책으로 25개 이상의 다양한 시각운동 조작 작업을 학습했습니다. LLM과 결합하여 추상적인 자연어 명령을 소수의 예시 프롬프팅(few-shot prompting)을 통해 하위 목표로 분해할 때, 우리의 방법은 이전 접근 방식보다 훨씬 적은 데이터로 실제 세계에서 장기적이고 다계층 작업을 완료할 수 있음을 발견했습니다. 코드와 비디오는 http://hulc2.cs.uni-freiburg.de에서 확인할 수 있습니다.
