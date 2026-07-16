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
  zh: 'arXiv:2606.30686v1 Announce Type: new Abstract: Vision-Language-Action (VLA) systems, built on pretrained vision-language
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30686v1.
sources:
- id: src_001
  type: paper
  title: 'Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning'
  url: https://arxiv.org/abs/2606.30686
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) systems, built on pretrained vision-language models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization. This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability. As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical generalization. Such designs make it possible to causally attribute performance without requiring access to model internals, and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence. Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization can be meaningfully evaluated.

## 核心内容
Vision-Language-Action (VLA) systems, built on pretrained vision-language models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization. This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability. As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical generalization. Such designs make it possible to causally attribute performance without requiring access to model internals, and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence. Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization can be meaningfully evaluated.

## 参考
- http://arxiv.org/abs/2606.30686v1

## Overview
Vision-Language-Action (VLA) systems, built on pretrained vision-language models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization. This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability. As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical generalization. Such designs make it possible to causally attribute performance without requiring access to model internals, and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence. Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization can be meaningfully evaluated.

## Content
Vision-Language-Action (VLA) systems, built on pretrained vision-language models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization. This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability. As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical generalization. Such designs make it possible to causally attribute performance without requiring access to model internals, and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence. Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization can be meaningfully evaluated.

## 개요
사전 훈련된 비전-언어 모델(VLM)을 기반으로 구축된 비전-언어-행동(VLA) 시스템은 로봇 조작 벤치마크에서 빠르게 성능이 향상되고 있습니다. 이러한 성과는 일반적으로 인터넷 규모 데이터에서 학습된 의미적 표현이 물리적 실행 일반화로 전이된다는 증거로 해석됩니다. 본 포지션 페이퍼는 이러한 해석의 기저 가정, 즉 의미적 일반화가 물리적 행동 결정을 지원하기에 충분하다는 가정이 독립적으로 검증되지 않았으며, 현재 평가 프로토콜 하에서 테스트될 수 없다고 주장합니다. 우리는 VLA 정책을 의미적 매핑과 물리적 행동 결정으로 분해하고, 지배적인 평가 지표인 작업 성공률이 이 두 능력 원천을 구분할 수 없음을 보여줌으로써 이 주장을 뒷받침합니다. 결과적으로, 벤치마크 성능 향상은 의미적 매칭, 분포적 중첩, 진정한 물리적 일반화를 포함한 여러 경쟁적 설명과 일치합니다. 우리는 또한 이러한 식별 가능성 격차가 서술적 표류(narrative drift)를 통해 강화되어 왔다고 주장합니다. 이는 연속적인 시스템들이 기저 인과 메커니즘을 분리하지 않고 성능 향상에 대한 이전 해석을 계승하고 강화하는 현상입니다. 이러한 한계를 해결하기 위해, 우리는 의미적 일반화와 물리적 일반화를 별도로 측정하기 위해 통제된 변동을 도입하는 평가 설계에 기반한 연구 방향을 제안합니다. 이러한 설계는 모델 내부에 접근하지 않고도 성능을 인과적으로 귀속시킬 수 있게 하며, VLM 백본이 물리적 능력의 암묵적 원천이 아닌 의미적 인터페이스로서의 역할을 경험적으로 평가할 수 있게 합니다. 우리의 목표는 로봇공학에서 VLM의 역할을 반박하는 것이 아니라, 물리적 일반화에 대한 주장이 의미 있게 평가될 수 있는 조건을 명확히 하는 것입니다.

## 핵심 내용
사전 훈련된 비전-언어 모델(VLM)을 기반으로 구축된 비전-언어-행동(VLA) 시스템은 로봇 조작 벤치마크에서 빠르게 성능이 향상되고 있습니다. 이러한 성과는 일반적으로 인터넷 규모 데이터에서 학습된 의미적 표현이 물리적 실행 일반화로 전이된다는 증거로 해석됩니다. 본 포지션 페이퍼는 이러한 해석의 기저 가정, 즉 의미적 일반화가 물리적 행동 결정을 지원하기에 충분하다는 가정이 독립적으로 검증되지 않았으며, 현재 평가 프로토콜 하에서 테스트될 수 없다고 주장합니다. 우리는 VLA 정책을 의미적 매핑과 물리적 행동 결정으로 분해하고, 지배적인 평가 지표인 작업 성공률이 이 두 능력 원천을 구분할 수 없음을 보여줌으로써 이 주장을 뒷받침합니다. 결과적으로, 벤치마크 성능 향상은 의미적 매칭, 분포적 중첩, 진정한 물리적 일반화를 포함한 여러 경쟁적 설명과 일치합니다. 우리는 또한 이러한 식별 가능성 격차가 서술적 표류(narrative drift)를 통해 강화되어 왔다고 주장합니다. 이는 연속적인 시스템들이 기저 인과 메커니즘을 분리하지 않고 성능 향상에 대한 이전 해석을 계승하고 강화하는 현상입니다. 이러한 한계를 해결하기 위해, 우리는 의미적 일반화와 물리적 일반화를 별도로 측정하기 위해 통제된 변동을 도입하는 평가 설계에 기반한 연구 방향을 제안합니다. 이러한 설계는 모델 내부에 접근하지 않고도 성능을 인과적으로 귀속시킬 수 있게 하며, VLM 백본이 물리적 능력의 암묵적 원천이 아닌 의미적 인터페이스로서의 역할을 경험적으로 평가할 수 있게 합니다. 우리의 목표는 로봇공학에서 VLM의 역할을 반박하는 것이 아니라, 물리적 일반화에 대한 주장이 의미 있게 평가될 수 있는 조건을 명확히 하는 것입니다.
