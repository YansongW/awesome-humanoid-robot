---
$id: ent_paper_dreamdojo_a_generalist_robot_w_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos'
  zh: 世界模型开始变成机器人策略的试验场
  ko: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos'
summary:
  en: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos is a knowledge node related to paper in the
    humanoid robot value chain.'
  zh: DreamDojo 是一个通用机器人世界模型，由研究团队基于 44,000 小时的第一人称人类视频训练而成。其核心贡献在于通过连续潜在动作解决动作标签稀缺问题，并实现了实时推理速度（10.81 FPS），支持远程操控、策略评估和基于模型的规划等应用。
  ko: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos is a knowledge node related to paper in the
    humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- contact_rich
- fall_recovery
- load_carrying
- safety
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06949v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (833 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos (arXiv)'
  url: https://arxiv.org/abs/2602.06949
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 世界模型开始变成机器人策略的试验场 project page
  url: https://dreamdojo-world.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
DreamDojo 旨在从大规模无标注人类视频中学习通用世界动态，尤其针对灵巧机器人任务。该模型利用 44,000 小时的第一人称视频作为预训练数据，覆盖了丰富的日常场景和技能，是迄今为止用于世界模型预训练的最大视频数据集。为解决动作标签不足的问题，DreamDojo 引入了连续潜在动作作为统一代理动作，从而从无标签视频中迁移交互知识。在少量目标机器人数据上进行后训练后，模型展现出对物理规律的理解和精确的动作控制能力。此外，研究团队设计了一个蒸馏流程，将模型加速至实时速度（10.81 FPS），并提升了上下文一致性。

## 核心内容
### 方法
- **数据驱动**：使用 44,000 小时的第一人称人类视频作为预训练数据，涵盖多样化的日常场景、物体和技能，旨在覆盖广泛的世界动态。
- **动作标签缺失解决方案**：引入连续潜在动作作为统一代理动作，从无标签视频中提取交互知识，实现跨任务的知识迁移。
- **后训练**：在少量目标机器人数据上进行微调，使模型适应具体机器人平台，同时保持对物理规律的理解。

### 架构
- 基于生成式世界模型框架，能够模拟不同环境中的动作结果。
- 蒸馏流程将模型加速至 10.81 FPS 的实时推理速度，并提升上下文一致性。

### 实验设置
- 在多个具有挑战性的分布外（OOD）基准上进行系统评估，重点测试开放世界和接触密集型任务。
- 对比基线包括现有世界模型方法，验证 DreamDojo 在模拟复杂交互方面的优势。

### 关键数字
- 预训练数据规模：44,000 小时第一人称视频，为当前最大世界模型预训练数据集。
- 推理速度：蒸馏后达到 10.81 FPS，满足实时应用需求。

### 结论
DreamDojo 展示了从大规模人类视频中学习通用世界模型的可行性，尤其在灵巧机器人任务中。其应用包括实时远程操控、策略评估和基于模型的规划，为通用机器人世界模型的发展奠定了基础。

## Overview
Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.81 FPS and further improves context consistency. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

## 参考
- http://arxiv.org/abs/2602.06949v1

## 개요
DreamDojo는 대규모 무주석 인간 비디오에서 일반적인 세계 역학을 학습하는 것을 목표로 하며, 특히 손재주 있는 로봇 작업에 중점을 둡니다. 이 모델은 44,000시간의 1인칭 비디오를 사전 학습 데이터로 사용하며, 풍부한 일상 장면과 기술을 포함하여 현재 세계 모델 사전 학습에 사용된 가장 큰 비디오 데이터 세트입니다. 동작 라벨 부족 문제를 해결하기 위해 DreamDojo는 연속 잠재 동작을 통합 대리 동작으로 도입하여 무주석 비디오에서 상호작용 지식을 전이합니다. 소량의 대상 로봇 데이터로 사후 학습한 후, 모델은 물리 법칙에 대한 이해와 정밀한 동작 제어 능력을 보여줍니다. 또한 연구 팀은 모델을 실시간 속도(10.81 FPS)로 가속화하고 컨텍스트 일관성을 향상시키는 증류 프로세스를 설계했습니다.

## 핵심 내용
### 방법
- **데이터 기반**: 44,000시간의 1인칭 인간 비디오를 사전 학습 데이터로 사용하며, 다양한 일상 장면, 객체 및 기술을 포함하여 광범위한 세계 역학을 다루는 것을 목표로 합니다.
- **동작 라벨 부족 해결**: 연속 잠재 동작을 통합 대리 동작으로 도입하여 무주석 비디오에서 상호작용 지식을 추출하고, 작업 간 지식 전이를 실현합니다.
- **사후 학습**: 소량의 대상 로봇 데이터로 미세 조정하여 모델을 특정 로봇 플랫폼에 적응시키면서 물리 법칙에 대한 이해를 유지합니다.

### 아키텍처
- 생성적 세계 모델 프레임워크를 기반으로 하여 다양한 환경에서의 동작 결과를 시뮬레이션할 수 있습니다.
- 증류 프로세스는 모델을 10.81 FPS의 실시간 추론 속도로 가속화하고 컨텍스트 일관성을 향상시킵니다.

### 실험 설정
- 여러 도전적인 분포 외(OOD) 벤치마크에서 체계적으로 평가하며, 개방형 세계 및 접촉 집약적 작업에 중점을 둡니다.
- 비교 기준에는 기존 세계 모델 방법이 포함되어 DreamDojo가 복잡한 상호작용 시뮬레이션에서의 우수성을 검증합니다.

### 주요 수치
- 사전 학습 데이터 규모: 44,000시간의 1인칭 비디오로, 현재 가장 큰 세계 모델 사전 학습 데이터 세트입니다.
- 추론 속도: 증류 후 10.81 FPS에 도달하여 실시간 응용 요구를 충족합니다.

### 결론
DreamDojo는 대규모 인간 비디오에서 일반적인 세계 모델을 학습하는 가능성을 보여주며, 특히 손재주 있는 로봇 작업에서 두드러집니다. 그 응용에는 실시간 원격 제어, 정책 평가 및 모델 기반 계획이 포함되어 일반 로봇 세계 모델 개발의 기초를 마련합니다.
