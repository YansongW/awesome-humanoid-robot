---
$id: ent_paper_anchorvla_bridging_discrete_de_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
  zh: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
  ko: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
summary:
  en: 'arXiv:2607.03182v1 Announce Type: new Abstract: Autonomous driving planning requires translating navigation intent,
    traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action
    models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level
    semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory
    prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation
    with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action
    alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose
    AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit
    interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation
    represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than
    a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the
    selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making.
    By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences,
    AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous
    generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art
    Success Rate of 77.28 and a competitive Driving Score of 89.92.'
  zh: AnchorVLA 是一个由研究者提出的分层决策锚定视觉-语言-动作规划框架，旨在解决现有 VLA 规划器在连续轨迹生成中语义-动作对齐困难与推理效率低下的问题。其核心贡献在于引入轨迹模式锚点作为高层推理与连续执行之间的显式接口，并在
    Bench2Drive 闭环基准上取得了 77.28 的成功率与 89.92 的驾驶分数。
  ko: 'arXiv:2607.03182v1 Announce Type: new Abstract: Autonomous driving planning requires translating navigation intent,
    traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action
    models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level
    semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory
    prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation
    with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action
    alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose
    AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit
    interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation
    represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than
    a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the
    selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making.
    By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences,
    AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous
    generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art
    Success Rate of 77.28 and a competitive Driving Score of 89.92.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- anchorvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03182v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (895 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning (arXiv)'
  url: https://arxiv.org/abs/2607.03182
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有 VLA 规划器主要依赖基于规划头的轨迹预测或全轨迹自回归生成，前者对连续轨迹的约束较弱，后者则因使用低信息密度的坐标令牌长序列而导致离散化误差与推理效率低下。AnchorVLA 通过决策即锚点表示将行为级驾驶决策编码为锚点令牌，每个令牌代表完整的局部运动模式而非单一坐标点，随后利用决策锚定残差流在选定锚点定义的残差空间中生成精细的连续轨迹。这种设计保留了基于 LLM 的决策能力，同时提升了推理效率与语义-动作对齐效果。

## 核心内容
### 方法架构
AnchorVLA 采用分层决策锚定框架，包含两个核心模块：
- **Decision-as-Anchor Representation**：将高层驾驶决策（如变道、减速）表示为紧凑的锚点令牌，每个令牌编码一个完整的局部运动模式，而非传统方法中的单一坐标点。这使模型能够基于语义丰富的锚点进行推理，而非自回归生成低效的航点序列。
- **Decision-Anchored Residual Flow**：在选定锚点定义的残差空间中生成精细的连续轨迹，捕捉高层决策后的多模态执行细化。该模块通过残差流机制实现连续轨迹的灵活生成，避免了离散化误差。

### 实验设置与关键结果
- **基准测试**：在 Bench2Drive 闭环仿真基准上进行评估，该基准涵盖多种驾驶场景与语言指令。
- **性能指标**：AnchorVLA 取得了 77.28 的成功率（state-of-the-art）与 89.92 的驾驶分数，在语义-动作对齐与推理效率上显著优于现有 VLA 规划器。
- **对比优势**：相比基于规划头的方法，AnchorVLA 通过锚点显式约束轨迹生成；相比全轨迹自回归方法，其推理速度更快且避免了低信息密度坐标令牌带来的问题。

### 结论
AnchorVLA 通过引入轨迹模式锚点作为高层推理与连续执行之间的显式接口，有效解决了现有 VLA 规划器的语义-动作对齐困难与推理效率低下问题。实验证明其在闭环驾驶任务中达到了领先性能，为自动驾驶规划中的视觉-语言-动作模型提供了新的设计范式。

## Overview
Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.

## 参考
- http://arxiv.org/abs/2607.03182v1

## 개요
기존 VLA 플래너는 주로 플래닝 헤드 기반의 궤적 예측 또는 전체 궤적 자기회귀 생성에 의존하는데, 전자는 연속 궤적에 대한 제약이 약하고, 후자는 정보 밀도가 낮은 좌표 토큰의 긴 시퀀스를 사용하여 이산화 오류와 추론 효율 저하를 초래합니다. AnchorVLA는 결정을 앵커 표현으로 인코딩하여 행동 수준의 운전 결정을 앵커 토큰으로 표현하며, 각 토큰은 단일 좌표점이 아닌 완전한 국소 운동 패턴을 나타냅니다. 이후 결정 앵커링 잔차 흐름을 통해 선택된 앵커가 정의하는 잔차 공간에서 정밀한 연속 궤적을 생성합니다. 이러한 설계는 LLM 기반의 결정 능력을 유지하면서 추론 효율과 의미-행동 정렬 효과를 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
AnchorVLA는 계층적 결정 앵커링 프레임워크를 채택하며, 두 가지 핵심 모듈로 구성됩니다:
- **Decision-as-Anchor Representation**: 고수준 운전 결정(예: 차선 변경, 감속)을 컴팩트한 앵커 토큰으로 표현하며, 각 토큰은 전통적인 방법의 단일 좌표점이 아닌 완전한 국소 운동 패턴을 인코딩합니다. 이를 통해 모델은 비효율적인 웨이포인트 시퀀스를 자기회귀적으로 생성하는 대신 의미적으로 풍부한 앵커를 기반으로 추론할 수 있습니다.
- **Decision-Anchored Residual Flow**: 선택된 앵커가 정의하는 잔차 공간에서 정밀한 연속 궤적을 생성하여 고수준 결정 이후의 다중 모드 실행 세부화를 포착합니다. 이 모듈은 잔차 흐름 메커니즘을 통해 연속 궤적의 유연한 생성을 가능하게 하여 이산화 오류를 방지합니다.

### 실험 설정 및 주요 결과
- **벤치마크**: Bench2Drive 폐루프 시뮬레이션 벤치마크에서 평가되었으며, 다양한 운전 시나리오와 언어 명령을 포함합니다.
- **성능 지표**: AnchorVLA는 77.28의 성공률(state-of-the-art)과 89.92의 운전 점수를 달성하여 의미-행동 정렬 및 추론 효율에서 기존 VLA 플래너를 크게 능가합니다.
- **비교 우위**: 플래닝 헤드 기반 방법과 비교하여 AnchorVLA는 앵커를 통해 궤적 생성을 명시적으로 제약하며, 전체 궤적 자기회귀 방법과 비교하여 추론 속도가 빠르고 정보 밀도가 낮은 좌표 토큰으로 인한 문제를 피합니다.

### 결론
AnchorVLA는 궤적 패턴 앵커를 고수준 추론과 연속 실행 사이의 명시적 인터페이스로 도입하여 기존 VLA 플래너의 의미-행동 정렬 어려움과 추론 효율 저하 문제를 효과적으로 해결합니다. 실험을 통해 폐루프 운전 작업에서 선도적인 성능을 달성함을 입증했으며, 자율주행 계획에서의 시각-언어-행동 모델에 새로운 설계 패러다임을 제공합니다.
