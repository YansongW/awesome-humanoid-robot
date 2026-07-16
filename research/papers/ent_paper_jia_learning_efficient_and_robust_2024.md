---
$id: ent_paper_jia_learning_efficient_and_robust_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping
  zh: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping
  ko: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping
summary:
  en: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping (Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant
    Language Mapping), is a 2024 large vision-language-action model for robotic manipulation, introduced by Brown University,
    Northeastern University, and published at IEEE Robotics Autom. Lett. 2024.
  zh: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping (Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant
    Language Mapping), is a 2024 large vision-language-action model for robotic manipulation, introduced by Brown University,
    Northeastern University, and published at IEEE Robotics Autom. Lett. 2024.
  ko: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping (Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant
    Language Mapping), is a 2024 large vision-language-action model for robotic manipulation, introduced by Brown University,
    Northeastern University, and published at IEEE Robotics Autom. Lett. 2024.
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
- learning_efficient_and_robust
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.15677v2.
sources:
- id: src_001
  type: website
  title: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping source
  url: https://doi.org/10.1109/LRA.2025.3583614
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Controlling robots through natural language is pivotal for enhancing human-robot collaboration and synthesizing complex robot behaviors. Recent works that are trained on large robot datasets show impressive generalization abilities. However, such pretrained methods are (1) often fragile to unseen scenarios, and (2) expensive to adapt to new tasks. This paper introduces Grounded Equivariant Manipulation (GEM), a robust yet efficient approach that leverages pretrained vision-language models with equivariant language mapping for language-conditioned manipulation tasks. Our experiments demonstrate GEM's high sample efficiency and generalization ability across diverse tasks in both simulation and the real world. GEM achieves similar or higher performance with orders of magnitude fewer robot data compared with major data-efficient baselines such as CLIPort and VIMA. Finally, our approach demonstrates greater robustness compared to large VLA model, e.g, OpenVLA, at correctly interpreting natural language commands on unseen objects and poses. Code, data, and training details are available https://saulbatman.github.io/gem_page/

## 核心内容
Controlling robots through natural language is pivotal for enhancing human-robot collaboration and synthesizing complex robot behaviors. Recent works that are trained on large robot datasets show impressive generalization abilities. However, such pretrained methods are (1) often fragile to unseen scenarios, and (2) expensive to adapt to new tasks. This paper introduces Grounded Equivariant Manipulation (GEM), a robust yet efficient approach that leverages pretrained vision-language models with equivariant language mapping for language-conditioned manipulation tasks. Our experiments demonstrate GEM's high sample efficiency and generalization ability across diverse tasks in both simulation and the real world. GEM achieves similar or higher performance with orders of magnitude fewer robot data compared with major data-efficient baselines such as CLIPort and VIMA. Finally, our approach demonstrates greater robustness compared to large VLA model, e.g, OpenVLA, at correctly interpreting natural language commands on unseen objects and poses. Code, data, and training details are available https://saulbatman.github.io/gem_page/

## 参考
- http://arxiv.org/abs/2406.15677v2

## Overview
Controlling robots through natural language is pivotal for enhancing human-robot collaboration and synthesizing complex robot behaviors. Recent works that are trained on large robot datasets show impressive generalization abilities. However, such pretrained methods are (1) often fragile to unseen scenarios, and (2) expensive to adapt to new tasks. This paper introduces Grounded Equivariant Manipulation (GEM), a robust yet efficient approach that leverages pretrained vision-language models with equivariant language mapping for language-conditioned manipulation tasks. Our experiments demonstrate GEM's high sample efficiency and generalization ability across diverse tasks in both simulation and the real world. GEM achieves similar or higher performance with orders of magnitude fewer robot data compared with major data-efficient baselines such as CLIPort and VIMA. Finally, our approach demonstrates greater robustness compared to large VLA model, e.g, OpenVLA, at correctly interpreting natural language commands on unseen objects and poses. Code, data, and training details are available https://saulbatman.github.io/gem_page/

## Content
Controlling robots through natural language is pivotal for enhancing human-robot collaboration and synthesizing complex robot behaviors. Recent works that are trained on large robot datasets show impressive generalization abilities. However, such pretrained methods are (1) often fragile to unseen scenarios, and (2) expensive to adapt to new tasks. This paper introduces Grounded Equivariant Manipulation (GEM), a robust yet efficient approach that leverages pretrained vision-language models with equivariant language mapping for language-conditioned manipulation tasks. Our experiments demonstrate GEM's high sample efficiency and generalization ability across diverse tasks in both simulation and the real world. GEM achieves similar or higher performance with orders of magnitude fewer robot data compared with major data-efficient baselines such as CLIPort and VIMA. Finally, our approach demonstrates greater robustness compared to large VLA model, e.g, OpenVLA, at correctly interpreting natural language commands on unseen objects and poses. Code, data, and training details are available https://saulbatman.github.io/gem_page/

## 개요
자연어를 통한 로봇 제어는 인간-로봇 협업을 강화하고 복잡한 로봇 행동을 합성하는 데 핵심적입니다. 대규모 로봇 데이터셋으로 학습된 최근 연구들은 뛰어난 일반화 능력을 보여줍니다. 그러나 이러한 사전 학습 방법은 (1) 보지 못한 시나리오에 취약하고, (2) 새로운 작업에 적응하는 데 비용이 많이 듭니다. 본 논문은 언어 조건부 조작 작업을 위해 등변 언어 매핑을 갖춘 사전 학습된 비전-언어 모델을 활용하는 강력하면서도 효율적인 접근 방식인 Grounded Equivariant Manipulation (GEM)을 소개합니다. 실험을 통해 시뮬레이션과 실제 환경 모두에서 다양한 작업에 걸쳐 GEM의 높은 샘플 효율성과 일반화 능력을 입증했습니다. GEM은 CLIPort 및 VIMA와 같은 주요 데이터 효율적 기준선과 비교하여 훨씬 적은 로봇 데이터로 유사하거나 더 높은 성능을 달성합니다. 마지막으로, 우리의 접근 방식은 OpenVLA와 같은 대규모 VLA 모델에 비해 보지 못한 객체와 자세에 대한 자연어 명령을 올바르게 해석하는 데 있어 더 큰 강건성을 보여줍니다. 코드, 데이터 및 학습 세부 정보는 https://saulbatman.github.io/gem_page/ 에서 확인할 수 있습니다.

## 핵심 내용
자연어를 통한 로봇 제어는 인간-로봇 협업을 강화하고 복잡한 로봇 행동을 합성하는 데 핵심적입니다. 대규모 로봇 데이터셋으로 학습된 최근 연구들은 뛰어난 일반화 능력을 보여줍니다. 그러나 이러한 사전 학습 방법은 (1) 보지 못한 시나리오에 취약하고, (2) 새로운 작업에 적응하는 데 비용이 많이 듭니다. 본 논문은 언어 조건부 조작 작업을 위해 등변 언어 매핑을 갖춘 사전 학습된 비전-언어 모델을 활용하는 강력하면서도 효율적인 접근 방식인 Grounded Equivariant Manipulation (GEM)을 소개합니다. 실험을 통해 시뮬레이션과 실제 환경 모두에서 다양한 작업에 걸쳐 GEM의 높은 샘플 효율성과 일반화 능력을 입증했습니다. GEM은 CLIPort 및 VIMA와 같은 주요 데이터 효율적 기준선과 비교하여 훨씬 적은 로봇 데이터로 유사하거나 더 높은 성능을 달성합니다. 마지막으로, 우리의 접근 방식은 OpenVLA와 같은 대규모 VLA 모델에 비해 보지 못한 객체와 자세에 대한 자연어 명령을 올바르게 해석하는 데 있어 더 큰 강건성을 보여줍니다. 코드, 데이터 및 학습 세부 정보는 https://saulbatman.github.io/gem_page/ 에서 확인할 수 있습니다.
