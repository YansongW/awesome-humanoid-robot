---
$id: ent_paper_liu_omnireason_a_temporal_guided_v_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving'
  zh: OmniReason
  ko: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving'
summary:
  en: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving (OmniReason), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and Technology
    (Guangzhou), The Hong Kong University of Science and Technology.'
  zh: OmniReason 是香港科技大学（广州）与香港科技大学于2025年提出的大型视觉-语言-动作模型，专为自动驾驶设计。其核心贡献在于通过时间引导机制解决现有模型缺乏认知惯性导致的决策抖动问题，并在 Bench2Drive 和 nuScenes
    基准上取得显著性能提升。
  ko: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving (OmniReason), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and Technology
    (Guangzhou), The Hong Kong University of Science and Technology.'
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
- omnireason
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.00789v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (846 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2509.00789
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OmniReason source
  url: https://doi.org/10.48550/arXiv.2509.00789
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前视觉-语言模型因缺乏认知惯性，只能处理孤立快照，无法形成连续环境理解，导致复杂多步操作失败。OmniReason 通过 CogDriver 框架引入稀疏时间记忆与时空知识蒸馏，构建稳定内部表征。该框架包含两个关键组件：CogDriver-Data 数据集提供叙事标注以学习时间动态，CogDriver-Agent 架构通过决策连贯性训练实现稳定状态维护。实验表明，该方法在闭环驾驶评分上提升22%，在平均 L2 误差上降低21%。

## 核心内容
### 方法架构
- **CogDriver 框架**：核心思想是为视觉-语言模型注入认知惯性，通过稀疏时间记忆模块维持连续内部状态表征。
- **CogDriver-Data 数据集**：大规模视觉-语言-动作数据集，其叙事标注作为监督信号，显式建模时间动态与持久意图。
- **CogDriver-Agent 架构**：采用稀疏时间记忆机制，结合时空知识蒸馏损失函数，强制模型学习决策连贯性。

### 实验设置
- **基准测试**：在 Bench2Drive（闭环评估）和 nuScenes（开环评估）上验证。
- **评估指标**：Driving Score（闭环驾驶评分）与 mean L2 error（平均 L2 误差）。

### 关键结果
- **Bench2Drive**：闭环 Driving Score 提升22%，达到新最优水平。
- **nuScenes**：平均 L2 误差降低21%，在模仿精度上显著超越现有方法。
- **消融实验**：稀疏时间记忆与知识蒸馏的联合使用对性能提升贡献最大，单独移除任一模块均导致性能下降。

### 结论
OmniReason 通过时间引导的视觉-语言-动作框架，成功弥合了自动驾驶中长时决策与瞬时模仿之间的鸿沟，为更可靠的自主驾驶系统提供了新范式。项目链接：https://ocean-luna.github.io/CogDriver.github.io/。

## Overview
The pursuit of autonomous agents capable of temporally coherent planning is hindered by a fundamental flaw in current vision-language models (VLMs): they lack cognitive inertia. Operating on isolated snapshots, these models cannot form a continuous understanding of the environment, leading to erratic decision jitter and a failure to execute complex, multi-step maneuvers. To remedy this, we introduce CogDriver, a framework designed to build a stable internal representation by instilling this crucial cognitive property. Our work makes two key contributions: (1) We present CogDriver-Data, a large-scale vision-language-action dataset whose narrative annotations provide the supervisory signal for learning temporal dynamics and persistent intent. (2) We develop the CogDriver-Agent, an architecture featuring a sparse temporal memory to maintain a stable internal state. This is enabled by a spatiotemporal knowledge distillation approach that explicitly teaches decision coherence. Comprehensive experiments validate our paradigm: CogDriver-Agent achieves a 22% increase in the closed-loop Driving Score on Bench2Drive and a 21% reduction in mean L2 error on nuScenes, establishing a new state-of-the-art. These significant gains in both long-term decision-making and imitation accuracy provide strong evidence that our agent successfully maintains a temporally coherent internal state, bridging the gap toward more reliable autonomous driving. Project link: https://ocean-luna.github.io/CogDriver.github.io/.

## 参考
- http://arxiv.org/abs/2509.00789v2

## 개요
현재 비전-언어 모델은 인지 관성(cognitive inertia)이 부족하여 고립된 스냅샷만 처리할 수 있고, 연속적인 환경 이해를 형성하지 못해 복잡한 다단계 조작이 실패합니다. OmniReason은 CogDriver 프레임워크를 통해 희소 시간 메모리와 시공간 지식 증류를 도입하여 안정적인 내부 표현을 구축합니다. 이 프레임워크는 두 가지 핵심 구성 요소를 포함합니다: CogDriver-Data 데이터셋은 시간 역학을 학습하기 위한 내러티브 주석을 제공하고, CogDriver-Agent 아키텍처는 결정 일관성 훈련을 통해 안정적인 상태 유지를 구현합니다. 실험 결과, 이 방법은 폐루프 주행 점수에서 22% 향상, 평균 L2 오차에서 21% 감소를 달성했습니다.

## 핵심 내용
### 방법 아키텍처
- **CogDriver 프레임워크**: 핵심 아이디어는 비전-언어 모델에 인지 관성을 주입하여 희소 시간 메모리 모듈을 통해 연속적인 내부 상태 표현을 유지하는 것입니다.
- **CogDriver-Data 데이터셋**: 대규모 비전-언어-행동 데이터셋으로, 내러티브 주석을 감독 신호로 사용하여 시간 역학과 지속적 의도를 명시적으로 모델링합니다.
- **CogDriver-Agent 아키텍처**: 희소 시간 메모리 메커니즘을 채택하고, 시공간 지식 증류 손실 함수를 결합하여 모델이 결정 일관성을 학습하도록 강제합니다.

### 실험 설정
- **벤치마크**: Bench2Drive(폐루프 평가) 및 nuScenes(개루프 평가)에서 검증.
- **평가 지표**: Driving Score(폐루프 주행 점수) 및 mean L2 error(평균 L2 오차).

### 주요 결과
- **Bench2Drive**: 폐루프 Driving Score가 22% 향상되어 새로운 최고 수준에 도달.
- **nuScenes**: 평균 L2 오차가 21% 감소하여 모방 정확도에서 기존 방법을 크게 능가.
- **소거 실험**: 희소 시간 메모리와 지식 증류의 결합 사용이 성능 향상에 가장 큰 기여를 하며, 각 모듈을 개별적으로 제거하면 성능이 저하됨.

### 결론
OmniReason은 시간 기반 비전-언어-행동 프레임워크를 통해 자율 주행에서 장기 결정과 순간 모방 사이의 간극을 성공적으로 메우며, 더 신뢰할 수 있는 자율 주행 시스템을 위한 새로운 패러다임을 제공합니다. 프로젝트 링크: https://ocean-luna.github.io/CogDriver.github.io/.
