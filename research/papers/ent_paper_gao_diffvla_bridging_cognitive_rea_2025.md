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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17148v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (743 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.17148v4

## 개요
기존의 엔드투엔드 주행 모델은 물리적으로 타당한 궤적을 생성할 수 있지만, 세계 지식(world knowledge)이 부족하여 긴 꼬리(long-tail) 시나리오를 처리하기 어렵습니다. Vision-Language-Action (VLA) 모델은 세계 지식을 활용해 복잡한 상황을 처리할 수 있지만, 3D 추론 능력이 부족하여 물리적으로 실행 불가능한 동작을 초래할 수 있습니다. DiffVLA++는 세 가지 핵심 모듈을 통해 이러한 모순을 해결합니다: 의미 기반 궤적을 직접 생성하는 VLA 모듈, 밀집 궤적 어휘(dense trajectory vocabulary)를 갖춰 물리적 실행 가능성을 보장하는 E2E 모듈, 그리고 핵심인 메트릭 기반 궤적 스코어러(metric-guided trajectory scorer)입니다. 이 스코어러는 두 모듈의 출력을 정렬하여 인지적 추론과 물리적 실행 가능성의 유기적 융합을 실현합니다.

## 핵심 내용
### 방법 아키텍처
DiffVLA++는 세 가지 모듈이 협력하는 아키텍처를 채택합니다:
- **VLA 모듈**: 의미 기반 주행 궤적을 직접 생성하며, 세계 지식을 활용해 장면 이해와 추론을 수행합니다.
- **E2E 모듈**: 밀집 궤적 어휘(dense trajectory vocabulary)를 갖춰 생성된 궤적의 물리적 실행 가능성을 보장합니다.
- **메트릭 기반 궤적 스코어러**(Metric-Guided Trajectory Scorer): 핵심 혁신 구성 요소로, 메트릭 기준을 통해 VLA와 E2E 모듈의 출력을 정렬하여 두 모듈의 상호 보완적 장점을 통합합니다.

### 실험 설정
- ICCV 2025 자율주행 그랜드 챌린지(Autonomous Grand Challenge) 리더보드에서 평가를 수행했습니다.
- 주요 지표: EPDMS(End-to-End Planning and Driving Metric Score)

### 주요 결과
- 최종 EPDMS 점수는 49.12에 도달하여 인지적 추론과 엔드투엔드 계획 정렬의 효과성을 검증했습니다.

### 결론
DiffVLA++는 메트릭 기반 정렬 메커니즘을 통해 기존 E2E 모델의 세계 지식 부족과 VLA 모델의 물리적 실행 가능성 부족이라는 이중 문제를 성공적으로 해결하며, 자율주행의 긴 꼬리 시나리오 처리에 새로운 패러다임을 제시합니다.
