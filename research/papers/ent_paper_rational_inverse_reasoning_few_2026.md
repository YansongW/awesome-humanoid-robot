---
$id: ent_paper_rational_inverse_reasoning_few_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Rational Inverse Reasoning: Few-Shot Imitation by Inferring Intent through Planning'
  zh: 'Rational Inverse Reasoning: Few-Shot Imitation by Inferring Intent through Planning'
  ko: 'Rational Inverse Reasoning: Few-Shot Imitation by Inferring Intent through Planning'
summary:
  en: 'arXiv:2508.08983v2 Announce Type: replace Abstract: Humans can learn a new manipulation task from one or two demonstrations
    and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast,
    typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object
    set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning
    occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather
    than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference
    over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured
    task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate
    programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded
    feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a
    2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration.
    Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality
    and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and
    three-shot settings.'
  zh: Rational Inverse Reasoning (RIR) 是一种面向机器人少样本模仿学习的新方法，由研究团队提出。其核心贡献在于将模仿学习转化为对潜在解释程序的推理，通过视觉语言模型 (VLM) 提出候选程序，并结合分层规划器的有界理性似然进行迭代优化。在2D推理基准和真实Franka
    FR3机器人上，RIR仅需一次演示即可恢复可迁移的任务结构，并在新布局和物体集下将下游成功率提升34和28个百分点。
  ko: 'arXiv:2508.08983v2 Announce Type: replace Abstract: Humans can learn a new manipulation task from one or two demonstrations
    and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast,
    typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object
    set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning
    occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather
    than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference
    over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured
    task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate
    programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded
    feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a
    2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration.
    Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality
    and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and
    three-shot settings.'
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
- rational_inverse_reasoning
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.08983v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (998 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Rational Inverse Reasoning: Few-Shot Imitation by Inferring Intent through Planning (arXiv)'
  url: https://arxiv.org/abs/2508.08983
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
RIR 的核心思想是，机器人泛化能力不足的根本原因在于学习抽象层次过低，需要推断演示者行为背后的潜在意图，而非简单复现其动作。该方法将少样本模仿学习建模为对潜在解释程序的推理，这些程序是紧凑、可执行的意图描述，能将物体中心场景映射为结构化的任务与运动规划 (TAMP) 规范。具体实现中，视觉语言模型 (VLM) 负责生成候选程序，而分层规划器则提供有界理性似然作为反馈。通过VLM程序提议与规划器反馈的迭代结合，RIR能逼近一个关于简洁可执行程序的后验分布。实验表明，RIR在2D推理基准和真实Franka FR3机器人上，仅需一次演示即可恢复可迁移的任务结构，并在显著变化的新布局和物体集下，将一次和三次演示设置的下游成功率分别提升34和28个百分点。

## 核心内容
### 方法概述
RIR 将少样本模仿学习形式化为对潜在解释程序的推理过程。其核心思想是，泛化需要推断演示者行为背后的潜在意图，而非简单复现其动作。该方法将意图表示为紧凑、可执行的程序，这些程序能将物体中心场景映射为结构化的任务与运动规划 (TAMP) 规范，包括目标、子目标和约束。

### 架构与流程
- **程序提议**：视觉语言模型 (VLM) 基于演示视频和场景信息，提出候选解释程序。
- **规划器反馈**：分层规划器为每个候选程序计算有界理性似然，评估其作为演示者意图解释的合理性。
- **迭代优化**：通过VLM程序提议与规划器反馈的迭代结合，RIR逐步精炼候选集，逼近一个关于简洁可执行程序的后验分布。

### 实验设置与关键结果
- **基准测试**：在2D推理基准和真实Franka FR3机器人上进行评估。
- **演示数量**：RIR仅需一次演示即可恢复可迁移的任务结构。
- **泛化能力**：在显著变化的新布局和物体集下，RIR展现出强大的泛化能力。
- **性能提升**：与缺乏显式理性和规划接地推理的VLM规划基线相比，RIR在**一次演示**设置下将下游成功率提升**34个百分点**，在**三次演示**设置下提升**28个百分点**。

### 结论
RIR 通过将少样本模仿学习转化为对潜在意图的推理，显著提升了机器人在新环境下的泛化能力。该方法的核心优势在于利用VLM和规划器的协同作用，从极少量演示中提取可迁移的任务结构，为机器人少样本学习提供了新的思路。

## Overview
Humans can learn a new manipulation task from one or two demonstrations and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast, typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a 2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration. Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and three-shot settings.

## 参考
- http://arxiv.org/abs/2508.08983v2

## 개요
RIR의 핵심 아이디어는 로봇의 일반화 능력 부족의 근본 원인이 학습 추상화 수준이 너무 낮기 때문이며, 시연자의 행동 뒤에 숨은 잠재적 의도를 추론해야지 단순히 그 동작을 재현해서는 안 된다는 점입니다. 이 방법은 퓨샷 모방 학습을 잠재적 설명 프로그램에 대한 추론으로 모델링하며, 이러한 프로그램은 객체 중심 장면을 구조화된 작업 및 운동 계획(TAMP) 사양으로 매핑하는 간결하고 실행 가능한 의도 설명입니다. 구체적으로, 비전-언어 모델(VLM)이 후보 프로그램을 생성하고, 계층적 플래너가 제한된 합리성 우도를 피드백으로 제공합니다. VLM 프로그램 제안과 플래너 피드백의 반복적 결합을 통해 RIR은 간결하고 실행 가능한 프로그램에 대한 사후 분포에 근접할 수 있습니다. 실험 결과, RIR은 2D 추론 벤치마크와 실제 Franka FR3 로봇에서 단 한 번의 시연만으로도 전이 가능한 작업 구조를 복구할 수 있었으며, 크게 변화된 새로운 레이아웃과 객체 집합에서 1회 및 3회 시연 설정의 하류 성공률을 각각 34퍼센트 포인트와 28퍼센트 포인트 향상시켰습니다.

## 핵심 내용
### 방법 개요
RIR은 퓨샷 모방 학습을 잠재적 설명 프로그램에 대한 추론 과정으로 형식화합니다. 핵심 아이디어는 일반화를 위해서는 시연자의 행동 뒤에 숨은 잠재적 의도를 추론해야 하며, 단순히 동작을 재현해서는 안 된다는 점입니다. 이 방법은 의도를 객체 중심 장면을 목표, 하위 목표 및 제약 조건을 포함한 구조화된 작업 및 운동 계획(TAMP) 사양으로 매핑하는 간결하고 실행 가능한 프로그램으로 표현합니다.

### 아키텍처 및 프로세스
- **프로그램 제안**: 비전-언어 모델(VLM)이 시연 비디오와 장면 정보를 기반으로 후보 설명 프로그램을 제안합니다.
- **플래너 피드백**: 계층적 플래너가 각 후보 프로그램에 대해 제한된 합리성 우도를 계산하여 시연자 의도의 설명으로서의 타당성을 평가합니다.
- **반복 최적화**: VLM 프로그램 제안과 플래너 피드백의 반복적 결합을 통해 RIR은 후보 집합을 점진적으로 정제하여 간결하고 실행 가능한 프로그램에 대한 사후 분포에 근접합니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 2D 추론 벤치마크와 실제 Franka FR3 로봇에서 평가를 수행했습니다.
- **시연 수**: RIR은 단 한 번의 시연만으로도 전이 가능한 작업 구조를 복구할 수 있습니다.
- **일반화 능력**: 크게 변화된 새로운 레이아웃과 객체 집합에서 RIR은 강력한 일반화 능력을 보여줍니다.
- **성능 향상**: 명시적 합리성 및 계획 기반 추론이 부족한 VLM 계획 베이스라인과 비교하여, RIR은 **1회 시연** 설정에서 하류 성공률을 **34퍼센트 포인트** 향상시키고, **3회 시연** 설정에서 **28퍼센트 포인트** 향상시킵니다.

### 결론
RIR은 퓨샷 모방 학습을 잠재적 의도에 대한 추론으로 전환함으로써 로봇의 새로운 환경에서의 일반화 능력을 크게 향상시킵니다. 이 방법의 핵심 강점은 VLM과 플래너의 협력적 역할을 활용하여 극소량의 시연에서 전이 가능한 작업 구조를 추출한다는 점이며, 로봇 퓨샷 학습에 새로운 방향을 제시합니다.
