---
$id: ent_paper_position_vision_language_actio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning'
  zh: 'Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning'
  ko: 'Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning'
summary:
  en: 'arXiv:2606.30686v1 Announce Type: new Abstract: Vision-Language-Action (VLA) systems, built on pretrained vision-language
    models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted
    as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization.
    This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient
    to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation
    protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing
    that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability.
    As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic
    matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap
    has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of
    performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research
    direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical
    generalization. Such designs make it possible to causally attribute performance without requiring access to model internals,
    and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence.
    Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization
    can be meaningfully evaluated.'
  zh: 本文是一篇立场论文，由arXiv预印本发布，核心论点是当前基于视觉-语言模型（VLM）构建的视觉-语言-动作（VLA）系统在机器人操作基准上的性能提升，并不能被验证为真正的物理推理能力。作者指出，主流评估指标“任务成功率”无法区分语义匹配与物理泛化，导致性能改进存在多种竞争性解释，并提出了通过引入受控变量来分别测量语义与物理泛化的新评估方向。
  ko: 'arXiv:2606.30686v1 Announce Type: new Abstract: Vision-Language-Action (VLA) systems, built on pretrained vision-language
    models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted
    as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization.
    This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient
    to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation
    protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing
    that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability.
    As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic
    matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap
    has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of
    performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research
    direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical
    generalization. Such designs make it possible to causally attribute performance without requiring access to model internals,
    and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence.
    Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization
    can be meaningfully evaluated.'
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
- position
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30686v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (943 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning'
  url: https://arxiv.org/abs/2606.30686
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该论文质疑了当前机器人学习领域的一个普遍假设：VLA系统在基准测试上的性能提升，意味着从互联网数据中学到的语义表征能够迁移到物理执行泛化。作者将VLA策略分解为语义映射和物理动作决策两个部分，并证明任务成功率这一主导评估指标无法区分这两种能力来源。因此，基准性能的改进可能源于语义匹配、分布重叠或真正的物理泛化等多种原因，而现有评估协议无法独立验证。论文进一步指出，这种“可识别性差距”因“叙事漂移”而加剧，即后续系统在未隔离因果机制的情况下继承并强化了先前对性能提升的解释。为解决此问题，作者提议设计引入受控变量的评估方案，以分别测量语义和物理泛化，从而在不依赖模型内部结构的情况下实现因果归因。

## 核心内容
### 核心论点
- 当前VLA系统在机器人操作基准上的性能提升，常被解释为从互联网规模数据中学到的语义表征能够迁移到物理执行泛化。本文认为这一假设缺乏独立验证，且无法在现有评估协议下进行测试。
- 作者将VLA策略分解为两个独立组件：**语义映射**（理解场景与指令）和**物理动作决策**（执行具体操作）。任务成功率作为主导评估指标，无法区分性能提升究竟来自语义映射的改进还是物理决策能力的增强。

### 可识别性差距与叙事漂移
- 基准性能的改进与多种竞争性解释一致，包括：语义匹配（模型仅识别已知模式）、分布重叠（测试数据与训练数据相似）以及真正的物理泛化（模型理解物理因果关系）。
- 这种“可识别性差距”因“叙事漂移”而强化：后续系统在未隔离因果机制的情况下，继承并强化了先前对性能提升的语义泛化解释，导致领域内形成循环论证。

### 提出的解决方案
- 作者建议设计引入**受控变量**的评估方案，例如通过改变物体物理属性（如重量、摩擦系数）或任务环境布局，来分别测量语义泛化与物理泛化能力。
- 这种设计能够在不访问模型内部结构的情况下实现因果归因，并实证评估VLM主干网络作为语义接口（而非隐含物理能力来源）的实际作用。

### 结论与意义
- 本文并非否定VLM在机器人学中的作用，而是旨在澄清：只有在能够独立测量语义与物理泛化的评估条件下，关于物理泛化的主张才能被有意义地验证。这为未来机器人学习基准的设计提供了关键方法论指导。

## Overview
Vision-Language-Action (VLA) systems, built on pretrained vision-language models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization. This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability. As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical generalization. Such designs make it possible to causally attribute performance without requiring access to model internals, and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence. Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization can be meaningfully evaluated.

## 参考
- http://arxiv.org/abs/2606.30686v1

## 개요
이 논문은 현재 로봇 학습 분야의 일반적인 가정, 즉 VLA 시스템의 벤치마크 성능 향상이 인터넷 데이터에서 학습된 의미론적 표현이 물리적 실행 일반화로 전이될 수 있음을 의미한다는 가정에 의문을 제기합니다. 저자는 VLA 정책을 의미론적 매핑과 물리적 동작 결정의 두 부분으로 분해하고, 지배적인 평가 지표인 작업 성공률이 이 두 능력의 원천을 구분할 수 없음을 증명합니다. 따라서 벤치마크 성능의 개선은 의미론적 매칭, 분포 중첩 또는 진정한 물리적 일반화 등 여러 이유에서 비롯될 수 있으며, 기존 평가 프로토콜은 이를 독립적으로 검증할 수 없습니다. 논문은 나아가 이러한 "식별 가능성 격차"가 "서술적 표류"로 인해 악화된다고 지적합니다. 즉, 후속 시스템이 인과 메커니즘을 분리하지 않은 채 이전 성능 향상에 대한 해석을 계승하고 강화한다는 것입니다. 이 문제를 해결하기 위해 저자는 통제 변수를 도입한 평가 방식을 설계하여 의미론적 및 물리적 일반화를 각각 측정함으로써 모델 내부 구조에 의존하지 않고 인과 귀인을 가능하게 할 것을 제안합니다.

## 핵심 내용
### 핵심 주장
- 현재 VLA 시스템의 로봇 조작 벤치마크 성능 향상은 종종 인터넷 규모 데이터에서 학습된 의미론적 표현이 물리적 실행 일반화로 전이될 수 있다는 해석으로 이어집니다. 본 논문은 이 가정이 독립적 검증을 결여하며 기존 평가 프로토콜 하에서 테스트될 수 없다고 주장합니다.
- 저자는 VLA 정책을 두 개의 독립적인 구성 요소로 분해합니다: **의미론적 매핑**(장면과 지시 이해) 및 **물리적 동작 결정**(구체적 조작 실행). 작업 성공률은 지배적인 평가 지표로서 성능 향상이 의미론적 매핑의 개선에서 비롯된 것인지 물리적 결정 능력의 강화에서 비롯된 것인지를 구분할 수 없습니다.

### 식별 가능성 격차와 서술적 표류
- 벤치마크 성능의 개선은 여러 경쟁적 해석과 일치합니다: 의미론적 매칭(모델이 알려진 패턴만 인식), 분포 중첩(테스트 데이터가 훈련 데이터와 유사), 그리고 진정한 물리적 일반화(모델이 물리적 인과 관계를 이해)를 포함합니다.
- 이러한 "식별 가능성 격차"는 "서술적 표류"로 인해 강화됩니다: 후속 시스템이 인과 메커니즘을 분리하지 않은 채 이전 성능 향상에 대한 의미론적 일반화 해석을 계승하고 강화하여, 해당 분야에서 순환 논증이 형성됩니다.

### 제안된 해결책
- 저자는 **통제 변수**를 도입한 평가 방식을 설계할 것을 제안합니다. 예를 들어 물체의 물리적 속성(무게, 마찰 계수 등)이나 작업 환경 배치를 변경하여 의미론적 일반화와 물리적 일반화 능력을 각각 측정하는 것입니다.
- 이러한 설계는 모델 내부 구조에 접근하지 않고도 인과 귀인을 가능하게 하며, VLM 백본이 암묵적 물리 능력의 원천이 아닌 의미론적 인터페이스로서의 실제 역할을 실증적으로 평가할 수 있게 합니다.

### 결론 및 의의
- 본 논문은 VLM의 로봇 공학에서의 역할을 부정하는 것이 아니라, 의미론적 및 물리적 일반화를 독립적으로 측정할 수 있는 평가 조건 하에서만 물리적 일반화에 대한 주장이 의미 있게 검증될 수 있음을 명확히 하는 것을 목표로 합니다. 이는 향후 로봇 학습 벤치마크 설계에 중요한 방법론적 지침을 제공합니다.
