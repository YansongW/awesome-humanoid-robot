---
$id: ent_paper_gao_diffvla_bridging_cognitive_rea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment'
  zh: DiffVLA
  ko: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment'
summary:
  en: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment (DiffVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by RIX, Bosch, AIR, Tsinghua University, Shanghai
    Jiao Tong University.'
  zh: DiffVLA++ 是由 RIX、Bosch、AIR、清华大学和上海交通大学于 2025 年提出的增强型自动驾驶框架。其核心贡献在于通过度量引导对齐机制，将认知推理（VLA 模块）与端到端规划（E2E 模块）的优势相结合，在 ICCV
    2025 自动驾驶大挑战排行榜上取得了 49.12 的 EPDMS 分数。
  ko: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment (DiffVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by RIX, Bosch, AIR, Tsinghua University, Shanghai
    Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17148v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment (arXiv)'
  url: https://arxiv.org/abs/2510.17148
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DiffVLA source
  url: https://doi.org/10.48550/arXiv.2510.17148
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统端到端驾驶模型虽能生成物理上合理的轨迹，但因缺乏世界知识而难以应对长尾场景。Vision-Language-Action (VLA) 模型虽能利用世界知识处理复杂情况，但其三维推理能力不足可能导致物理上不可行的动作。DiffVLA++ 通过三个关键模块解决这一矛盾：直接生成语义驱动轨迹的 VLA 模块、配备密集轨迹词汇表确保物理可行性的 E2E 模块，以及核心的度量引导轨迹评分器。该评分器通过对齐两个模块的输出，实现了认知推理与物理可行性的有机融合。

## 核心内容
### 方法架构
DiffVLA++ 采用三模块协同架构：
- **VLA 模块**：直接生成语义驱动的驾驶轨迹，利用世界知识进行场景理解与推理
- **E2E 模块**：配备密集轨迹词汇表（dense trajectory vocabulary），确保生成轨迹的物理可行性
- **度量引导轨迹评分器**（Metric-Guided Trajectory Scorer）：核心创新组件，通过度量标准对齐 VLA 与 E2E 模块的输出，整合两者的互补优势

### 实验设置
- 在 ICCV 2025 自动驾驶大挑战（Autonomous Grand Challenge）排行榜上进行评估
- 主要指标：EPDMS（End-to-End Planning and Driving Metric Score）

### 关键结果
- 最终 EPDMS 分数达到 49.12，验证了认知推理与端到端规划对齐的有效性

### 结论
DiffVLA++ 通过度量引导对齐机制，成功解决了传统 E2E 模型缺乏世界知识与 VLA 模型物理可行性不足的双重问题，为自动驾驶中的长尾场景处理提供了新范式。

## Overview
Conventional end-to-end (E2E) driving models are effective at generating physically plausible trajectories, but often fail to generalize to long-tail scenarios due to the lack of essential world knowledge to understand and reason about surrounding environments. In contrast, Vision-Language-Action (VLA) models leverage world knowledge to handle challenging cases, but their limited 3D reasoning capability can lead to physically infeasible actions. In this work we introduce DiffVLA++, an enhanced autonomous driving framework that explicitly bridges cognitive reasoning and E2E planning through metric-guided alignment. First, we build a VLA module directly generating semantically grounded driving trajectories. Second, we design an E2E module with a dense trajectory vocabulary that ensures physical feasibility. Third, and most critically, we introduce a metric-guided trajectory scorer that guides and aligns the outputs of the VLA and E2E modules, thereby integrating their complementary strengths. The experiment on the ICCV 2025 Autonomous Grand Challenge leaderboard shows that DiffVLA++ achieves EPDMS of 49.12.

## 개요
기존의 종단간(E2E) 주행 모델은 물리적으로 타당한 궤적을 생성하는 데 효과적이지만, 주변 환경을 이해하고 추론하는 데 필요한 필수적인 세계 지식이 부족하여 롱테일(long-tail) 시나리오에 일반화하지 못하는 경우가 많습니다. 반면, Vision-Language-Action(VLA) 모델은 세계 지식을 활용하여 까다로운 사례를 처리하지만, 제한된 3D 추론 능력으로 인해 물리적으로 실행 불가능한 행동을 초래할 수 있습니다. 본 연구에서는 메트릭 기반 정렬을 통해 인지 추론과 E2E 계획을 명시적으로 연결하는 향상된 자율 주행 프레임워크인 DiffVLA++를 소개합니다. 첫째, 의미적으로 기반을 둔 주행 궤적을 직접 생성하는 VLA 모듈을 구축합니다. 둘째, 물리적 타당성을 보장하는 조밀한 궤적 어휘를 갖춘 E2E 모듈을 설계합니다. 셋째, 가장 중요하게는, VLA와 E2E 모듈의 출력을 안내하고 정렬하는 메트릭 기반 궤적 스코어러를 도입하여 상호 보완적인 강점을 통합합니다. ICCV 2025 Autonomous Grand Challenge 리더보드 실험 결과, DiffVLA++는 EPDMS 49.12를 달성했습니다.

## 핵심 내용
기존의 종단간(E2E) 주행 모델은 물리적으로 타당한 궤적을 생성하는 데 효과적이지만, 주변 환경을 이해하고 추론하는 데 필요한 필수적인 세계 지식이 부족하여 롱테일 시나리오에 일반화하지 못하는 경우가 많습니다. 반면, Vision-Language-Action(VLA) 모델은 세계 지식을 활용하여 까다로운 사례를 처리하지만, 제한된 3D 추론 능력으로 인해 물리적으로 실행 불가능한 행동을 초래할 수 있습니다. 본 연구에서는 메트릭 기반 정렬을 통해 인지 추론과 E2E 계획을 명시적으로 연결하는 향상된 자율 주행 프레임워크인 DiffVLA++를 소개합니다. 첫째, 의미적으로 기반을 둔 주행 궤적을 직접 생성하는 VLA 모듈을 구축합니다. 둘째, 물리적 타당성을 보장하는 조밀한 궤적 어휘를 갖춘 E2E 모듈을 설계합니다. 셋째, 가장 중요하게는, VLA와 E2E 모듈의 출력을 안내하고 정렬하는 메트릭 기반 궤적 스코어러를 도입하여 상호 보완적인 강점을 통합합니다. ICCV 2025 Autonomous Grand Challenge 리더보드 실험 결과, DiffVLA++는 EPDMS 49.12를 달성했습니다.

## 参考
- http://arxiv.org/abs/2510.17148v4
