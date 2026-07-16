---
$id: ent_paper_gao_a_taxonomy_for_evaluating_gene_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Taxonomy for Evaluating Generalist Robot Manipulation Policies
  zh: 评估通用机器人操作策略的分类法
  ko: 범용 로봇 조작 정책 평가를 위한 분류법
summary:
  en: Proposes STAR-Gen, a taxonomy of visual, semantic, and behavioral generalization for visuo-lingual robot manipulation
    policies, and instantiates it through 1,600+ real-world trials on Bridge V2 and ALOHA 2.
  zh: 提出STAR-Gen分类法，用于评估视觉-语言机器人操作策略的视觉、语义和行为泛化能力，并通过Bridge V2和ALOHA 2上的1600多次真实世界试验进行了实例化。
  ko: 시각-언어 로봇 조작 정책의 시각적, 의미적, 행동적 일반화를 분류하는 STAR-Gen 분류법을 제안하고, Bridge V2와 ALOHA 2에서 1,600회 이상의 실제 시험을 통해 구현함.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- generalist_robot_manipulation
- generalization_taxonomy
- visual_generalization
- semantic_generalization
- behavioral_generalization
- bridge_v2
- aloha_2
- benchmark
- evaluation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.01238v3.
sources:
- id: src_001
  type: paper
  title: A Taxonomy for Evaluating Generalist Robot Manipulation Policies
  url: https://arxiv.org/abs/2503.01238
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Machine learning for robot manipulation promises to unlock generalization to novel tasks and environments. But how should we measure the progress of these policies towards generalization? Evaluating and quantifying generalization is the Wild West of modern robotics, with each work proposing and measuring different types of generalization in their own, often difficult to reproduce settings. In this work, our goal is (1) to outline the forms of generalization we believe are important for robot manipulation in a comprehensive and fine-grained manner, and (2) to provide reproducible guidelines for measuring these notions of generalization. We first propose STAR-Gen, a taxonomy of generalization for robot manipulation structured around visual, semantic, and behavioral generalization. Next, we instantiate STAR-Gen with two case studies on real-world benchmarking: one based on open-source models and the Bridge V2 dataset, and another based on the bimanual ALOHA 2 platform that covers more dexterous and longer horizon tasks. Our case studies reveal many interesting insights: for example, we observe that open-source vision-language-action models often struggle with semantic generalization, despite pre-training on internet-scale language datasets. We provide videos and other supplementary material at stargen-taxonomy.github.io.

## 核心内容
Machine learning for robot manipulation promises to unlock generalization to novel tasks and environments. But how should we measure the progress of these policies towards generalization? Evaluating and quantifying generalization is the Wild West of modern robotics, with each work proposing and measuring different types of generalization in their own, often difficult to reproduce settings. In this work, our goal is (1) to outline the forms of generalization we believe are important for robot manipulation in a comprehensive and fine-grained manner, and (2) to provide reproducible guidelines for measuring these notions of generalization. We first propose STAR-Gen, a taxonomy of generalization for robot manipulation structured around visual, semantic, and behavioral generalization. Next, we instantiate STAR-Gen with two case studies on real-world benchmarking: one based on open-source models and the Bridge V2 dataset, and another based on the bimanual ALOHA 2 platform that covers more dexterous and longer horizon tasks. Our case studies reveal many interesting insights: for example, we observe that open-source vision-language-action models often struggle with semantic generalization, despite pre-training on internet-scale language datasets. We provide videos and other supplementary material at stargen-taxonomy.github.io.

## 参考
- http://arxiv.org/abs/2503.01238v3

## Overview
Machine learning for robot manipulation promises to unlock generalization to novel tasks and environments. But how should we measure the progress of these policies towards generalization? Evaluating and quantifying generalization is the Wild West of modern robotics, with each work proposing and measuring different types of generalization in their own, often difficult to reproduce settings. In this work, our goal is (1) to outline the forms of generalization we believe are important for robot manipulation in a comprehensive and fine-grained manner, and (2) to provide reproducible guidelines for measuring these notions of generalization. We first propose STAR-Gen, a taxonomy of generalization for robot manipulation structured around visual, semantic, and behavioral generalization. Next, we instantiate STAR-Gen with two case studies on real-world benchmarking: one based on open-source models and the Bridge V2 dataset, and another based on the bimanual ALOHA 2 platform that covers more dexterous and longer horizon tasks. Our case studies reveal many interesting insights: for example, we observe that open-source vision-language-action models often struggle with semantic generalization, despite pre-training on internet-scale language datasets. We provide videos and other supplementary material at stargen-taxonomy.github.io.

## Content
Machine learning for robot manipulation promises to unlock generalization to novel tasks and environments. But how should we measure the progress of these policies towards generalization? Evaluating and quantifying generalization is the Wild West of modern robotics, with each work proposing and measuring different types of generalization in their own, often difficult to reproduce settings. In this work, our goal is (1) to outline the forms of generalization we believe are important for robot manipulation in a comprehensive and fine-grained manner, and (2) to provide reproducible guidelines for measuring these notions of generalization. We first propose STAR-Gen, a taxonomy of generalization for robot manipulation structured around visual, semantic, and behavioral generalization. Next, we instantiate STAR-Gen with two case studies on real-world benchmarking: one based on open-source models and the Bridge V2 dataset, and another based on the bimanual ALOHA 2 platform that covers more dexterous and longer horizon tasks. Our case studies reveal many interesting insights: for example, we observe that open-source vision-language-action models often struggle with semantic generalization, despite pre-training on internet-scale language datasets. We provide videos and other supplementary material at stargen-taxonomy.github.io.

## 개요
로봇 조작을 위한 머신러닝은 새로운 작업과 환경에 대한 일반화를 가능하게 할 것으로 기대됩니다. 하지만 이러한 정책의 일반화 진전을 어떻게 측정해야 할까요? 일반화의 평가와 정량화는 현대 로봇공학의 '무법지대(Wild West)'와 같아서, 각 연구마다 서로 다른 유형의 일반화를 제안하고 측정하며, 종종 재현이 어려운 환경에서 이루어집니다. 본 연구의 목표는 (1) 로봇 조작에 중요하다고 생각되는 일반화의 형태를 포괄적이고 세밀하게 정리하고, (2) 이러한 일반화 개념을 측정하기 위한 재현 가능한 지침을 제공하는 것입니다. 먼저 시각적, 의미적, 행동적 일반화를 중심으로 구성된 로봇 조작 일반화 분류 체계인 STAR-Gen을 제안합니다. 다음으로, 실제 벤치마킹을 위한 두 가지 사례 연구를 통해 STAR-Gen을 구체화합니다. 하나는 오픈소스 모델과 Bridge V2 데이터셋을 기반으로 하고, 다른 하나는 더 정교하고 장기적인 작업을 다루는 양손 ALOHA 2 플랫폼을 기반으로 합니다. 사례 연구를 통해 많은 흥미로운 통찰을 얻었습니다. 예를 들어, 오픈소스 시각-언어-행동 모델이 인터넷 규모의 언어 데이터셋으로 사전 학습되었음에도 불구하고 의미적 일반화에 어려움을 겪는 것을 관찰했습니다. 비디오 및 기타 보충 자료는 stargen-taxonomy.github.io에서 제공합니다.

## 핵심 내용
로봇 조작을 위한 머신러닝은 새로운 작업과 환경에 대한 일반화를 가능하게 할 것으로 기대됩니다. 하지만 이러한 정책의 일반화 진전을 어떻게 측정해야 할까요? 일반화의 평가와 정량화는 현대 로봇공학의 '무법지대(Wild West)'와 같아서, 각 연구마다 서로 다른 유형의 일반화를 제안하고 측정하며, 종종 재현이 어려운 환경에서 이루어집니다. 본 연구의 목표는 (1) 로봇 조작에 중요하다고 생각되는 일반화의 형태를 포괄적이고 세밀하게 정리하고, (2) 이러한 일반화 개념을 측정하기 위한 재현 가능한 지침을 제공하는 것입니다. 먼저 시각적, 의미적, 행동적 일반화를 중심으로 구성된 로봇 조작 일반화 분류 체계인 STAR-Gen을 제안합니다. 다음으로, 실제 벤치마킹을 위한 두 가지 사례 연구를 통해 STAR-Gen을 구체화합니다. 하나는 오픈소스 모델과 Bridge V2 데이터셋을 기반으로 하고, 다른 하나는 더 정교하고 장기적인 작업을 다루는 양손 ALOHA 2 플랫폼을 기반으로 합니다. 사례 연구를 통해 많은 흥미로운 통찰을 얻었습니다. 예를 들어, 오픈소스 시각-언어-행동 모델이 인터넷 규모의 언어 데이터셋으로 사전 학습되었음에도 불구하고 의미적 일반화에 어려움을 겪는 것을 관찰했습니다. 비디오 및 기타 보충 자료는 stargen-taxonomy.github.io에서 제공합니다.
