---
$id: ent_paper_wang_robot_fleet_learning_via_polic_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robot Fleet Learning via Policy Merging
  zh: 通过策略融合的机器人车队学习
  ko: 정책 병합을 통한 로봇 군단 학습
summary:
  en: Proposes FLEET-MERGE, a distributed policy-merging method that consolidates
    recurrent neural network policies trained on heterogeneous local robot data without
    centralizing raw data, and introduces the FLEET-TOOLS tool-use benchmark.
  zh: 提出了FLEET-MERGE，一种分布式策略融合方法，能够在不集中原始数据的情况下整合在异构本地机器人数据上训练得到的循环神经网络策略，并引入了FLEET-TOOLS工具使用基准测试。
  ko: 원시 데이터를 중앙 집중화하지 않고 이질적인 로컬 로봇 데이터로 훈련된 순환 신경망 정책을 통합하는 분산 정책 병합 방법 FLEET-MERGE를
    제안하고 FLEET-TOOLS 도구 사용 벤치마크를 소개한다.
domains:
- 07_ai_models_algorithms
- 05_mass_production
- 08_software_middleware
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- policy_merging
- fleet_learning
- distributed_learning
- recurrent_neural_network
- manipulation
- tool_use
- meta_world
- drake_simulator
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; requires human review of full paper
    before verification.
sources:
- id: src_001
  type: paper
  title: Robot Fleet Learning via Policy Merging
  url: https://arxiv.org/abs/2310.01362
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Robot fleets generate massive, heterogeneous streaming data in distributed silos that cannot be easily stored or transmitted. This paper investigates policy merging (PoMe) as a bottom-up framework for fleet-level robot learning that avoids centralizing raw data by transmitting and merging trained model weights instead. The authors propose FLEET-MERGE, an instantiation of distributed learning that aligns multiple recurrent neural network (RNN) policies via soft and hard permutation operators, exploiting permutation invariance across layers and timesteps. The method is extended to merging many models and to iterative training-stage merging with reduced communication requirements.

In addition to the algorithmic contribution, the paper introduces FLEET-TOOLS, a novel robotic tool-use benchmark built in the Drake simulator. FLEET-TOOLS features compositional, contact-rich manipulation tasks involving tools such as a wrench, hammer, spatula, and knife, using a Panda arm with point-cloud observations and a ResNet18 vision encoder. The authors demonstrate that FLEET-MERGE can consolidate policies trained on 50 diverse Meta-World tasks into a single merged policy while retaining good performance on nearly all training tasks at test time, and report results on FLEET-TOOLS.

## Key Contributions

- Proposes policy merging (PoMe), a bottom-up framework for fleet-level robot learning that transmits trained model weights rather than raw data.
- Develops FLEET-MERGE, which aligns multiple RNN-parameterized policies using soft and hard permutation operators to handle permutation symmetries across layers and timesteps.
- Extends the merging approach to many models and to iterative training-stage merging with reduced communication requirements.
- Introduces FLEET-TOOLS, a new compositional contact-rich tool-use benchmark built in Drake for fleet policy learning.
- Demonstrates consolidation of 50 Meta-World manipulation tasks into a single merged policy without centralizing data.

## Relevance to Humanoid Robotics

Mass deployment of humanoid robots will create large, geographically distributed fleets that continuously collect heterogeneous manipulation data. Centralizing all such data is impractical due to bandwidth, storage, and privacy constraints. FLEET-MERGE offers a scalable mechanism to consolidate skills across these fleets by merging policy weights rather than raw observations, directly supporting mass-production-scale training and fleet-wide software updates for humanoids.

The method's focus on manipulation skill consolidation—including contact-rich tool use evaluated in FLEET-TOOLS—aligns closely with the dexterous manipulation capabilities required by humanoid robots in unstructured environments. By enabling distributed skill transfer without data centralization, the paper contributes to both the AI models/algorithms and software middleware layers of the humanoid-robot knowledge chain.
