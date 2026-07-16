---
$id: ent_paper_huang_voxposer_composable_3d_value_m_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models'
  zh: VoxPoser
  ko: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models'
summary:
  en: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (VoxPoser), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, University of Illinois Urbana-Champaign,
    and published at CoRL 2023.'
  zh: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (VoxPoser), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, University of Illinois Urbana-Champaign,
    and published at CoRL 2023.'
  ko: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (VoxPoser), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, University of Illinois Urbana-Champaign,
    and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- vision_language_action
- vla
- voxposer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.05973v2.
sources:
- id: src_001
  type: paper
  title: VoxPoser source
  url: https://proceedings.mlr.press/v229/huang23b.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning and planning. Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck. In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given an open-set of instructions and an open-set of objects. We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction. More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into the observation space of the agent. The composed value maps are then used in a model-based planning framework to zero-shot synthesize closed-loop robot trajectories with robustness to dynamic perturbations. We further demonstrate how the proposed framework can benefit from online experiences by efficiently learning a dynamics model for scenes that involve contact-rich interactions. We present a large-scale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified in free-form natural language. Videos and code at https://voxposer.github.io

## 核心内容
Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning and planning. Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck. In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given an open-set of instructions and an open-set of objects. We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction. More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into the observation space of the agent. The composed value maps are then used in a model-based planning framework to zero-shot synthesize closed-loop robot trajectories with robustness to dynamic perturbations. We further demonstrate how the proposed framework can benefit from online experiences by efficiently learning a dynamics model for scenes that involve contact-rich interactions. We present a large-scale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified in free-form natural language. Videos and code at https://voxposer.github.io

## 参考
- http://arxiv.org/abs/2307.05973v2

## Overview
Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning and planning. Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck. In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given an open-set of instructions and an open-set of objects. We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction. More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into the observation space of the agent. The composed value maps are then used in a model-based planning framework to zero-shot synthesize closed-loop robot trajectories with robustness to dynamic perturbations. We further demonstrate how the proposed framework can benefit from online experiences by efficiently learning a dynamics model for scenes that involve contact-rich interactions. We present a large-scale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified in free-form natural language. Videos and code at https://voxposer.github.io

## Content
Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning and planning. Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck. In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given an open-set of instructions and an open-set of objects. We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction. More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into the observation space of the agent. The composed value maps are then used in a model-based planning framework to zero-shot synthesize closed-loop robot trajectories with robustness to dynamic perturbations. We further demonstrate how the proposed framework can benefit from online experiences by efficiently learning a dynamics model for scenes that involve contact-rich interactions. We present a large-scale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified in free-form natural language. Videos and code at https://voxposer.github.io

## 개요
대규모 언어 모델(LLM)은 추론 및 계획 형태로 로봇 조작에 활용할 수 있는 풍부한 실행 가능 지식을 보유한 것으로 나타났습니다. 이러한 발전에도 불구하고, 대부분의 접근 방식은 여전히 환경과의 물리적 상호작용을 수행하기 위해 사전 정의된 동작 프리미티브에 의존하고 있으며, 이는 주요 병목 현상으로 남아 있습니다. 본 연구에서는 개방형 명령어 집합과 개방형 객체 집합이 주어졌을 때, 다양한 조작 작업에 대해 로봇 궤적, 즉 6자유도 엔드 이펙터 웨이포인트의 밀집 시퀀스를 합성하는 것을 목표로 합니다. 이를 위해 먼저 LLM이 자유 형식 언어 명령어에서 어포던스와 제약 조건을 추론하는 데 탁월하다는 점을 관찰했습니다. 더 중요한 것은, 코드 작성 능력을 활용하여 시각-언어 모델(VLM)과 상호작용함으로써 3D 가치 맵을 구성하고, 이를 통해 지식을 에이전트의 관찰 공간에 정착시킬 수 있다는 점입니다. 구성된 가치 맵은 모델 기반 계획 프레임워크에서 사용되어 동적 교란에 강건한 폐루프 로봇 궤적을 제로샷 방식으로 합성합니다. 또한, 접촉이 많은 상호작용을 포함하는 장면에 대해 동역학 모델을 효율적으로 학습함으로써 제안된 프레임워크가 온라인 경험을 통해 이점을 얻을 수 있는 방법을 추가로 보여줍니다. 본 연구는 시뮬레이션 및 실제 로봇 환경 모두에서 제안된 방법에 대한 대규모 연구를 제시하며, 자유 형식 자연어로 지정된 다양한 일상 조작 작업을 수행할 수 있는 능력을 입증합니다. 비디오 및 코드는 https://voxposer.github.io 에서 확인할 수 있습니다.

## 핵심 내용
대규모 언어 모델(LLM)은 추론 및 계획 형태로 로봇 조작에 활용할 수 있는 풍부한 실행 가능 지식을 보유한 것으로 나타났습니다. 이러한 발전에도 불구하고, 대부분의 접근 방식은 여전히 환경과의 물리적 상호작용을 수행하기 위해 사전 정의된 동작 프리미티브에 의존하고 있으며, 이는 주요 병목 현상으로 남아 있습니다. 본 연구에서는 개방형 명령어 집합과 개방형 객체 집합이 주어졌을 때, 다양한 조작 작업에 대해 로봇 궤적, 즉 6자유도 엔드 이펙터 웨이포인트의 밀집 시퀀스를 합성하는 것을 목표로 합니다. 이를 위해 먼저 LLM이 자유 형식 언어 명령어에서 어포던스와 제약 조건을 추론하는 데 탁월하다는 점을 관찰했습니다. 더 중요한 것은, 코드 작성 능력을 활용하여 시각-언어 모델(VLM)과 상호작용함으로써 3D 가치 맵을 구성하고, 이를 통해 지식을 에이전트의 관찰 공간에 정착시킬 수 있다는 점입니다. 구성된 가치 맵은 모델 기반 계획 프레임워크에서 사용되어 동적 교란에 강건한 폐루프 로봇 궤적을 제로샷 방식으로 합성합니다. 또한, 접촉이 많은 상호작용을 포함하는 장면에 대해 동역학 모델을 효율적으로 학습함으로써 제안된 프레임워크가 온라인 경험을 통해 이점을 얻을 수 있는 방법을 추가로 보여줍니다. 본 연구는 시뮬레이션 및 실제 로봇 환경 모두에서 제안된 방법에 대한 대규모 연구를 제시하며, 자유 형식 자연어로 지정된 다양한 일상 조작 작업을 수행할 수 있는 능력을 입증합니다. 비디오 및 코드는 https://voxposer.github.io 에서 확인할 수 있습니다.
