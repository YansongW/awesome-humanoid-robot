---
$id: ent_paper_chiang_mobility_vla_multimodal_instru_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs'
  zh: Mobility VLA
  ko: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs'
summary:
  en: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs (Mobility VLA), is a
    2024 large vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL24.'
  zh: Mobility VLA 是 Google DeepMind 于 2024 年发表在 CoRL24 上的分层视觉-语言-动作（VLA）导航策略。它结合了长上下文 VLM 的环境理解与常识推理能力，以及基于拓扑图的鲁棒低级导航策略，用于解决多模态指令导航任务（MINT）。在
    836m² 的真实环境中，Mobility VLA 在“我应该把这个塑料箱放回哪里？”等此前未解决的多模态指令上取得了高端到端成功率。
  ko: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs (Mobility VLA), is a
    2024 large vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL24.'
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
- mobility_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.07775v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (689 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Mobility VLA source
  url: https://proceedings.mlr.press/v270/xu25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Mobility VLA 旨在构建一个能够理解自然语言和图像等多模态指令并执行有用导航的智能体。它针对一类称为 MINT 的导航任务，其中环境先验通过预先录制的演示视频提供。该模型采用分层架构：高层策略使用长上下文 VLM，将演示视频和多模态用户指令作为输入，以在演示视频中找到目标帧；低层策略则利用该目标帧和离线构建的拓扑图，在每个时间步生成机器人动作。在 836m² 的真实世界环境中，Mobility VLA 成功解决了此前无法处理的多模态指令，例如用户手持塑料箱时询问“我应该把这个放回哪里？”。

## 核心内容
### 方法
Mobility VLA 采用分层视觉-语言-动作（VLA）导航策略，结合了长上下文 VLM 和基于拓扑图的低级策略。

### 架构
- **高层策略**：使用长上下文 VLM，将演示视频和多模态用户指令（自然语言和图像）作为输入，输出演示视频中的目标帧。
- **低层策略**：基于离线构建的拓扑图，利用目标帧在每个时间步生成机器人动作。

### 实验设置
- **环境**：836m² 的真实世界环境。
- **任务**：多模态指令导航任务（MINT），其中环境先验通过预先录制的演示视频提供。

### 关键数字
- 在 836m² 的真实环境中进行测试。
- 成功解决了此前未解决的多模态指令，例如“Where should I return this?”（用户手持塑料箱时）。

### 结论
Mobility VLA 展示了结合长上下文 VLM 和拓扑图在解决多模态指令导航任务中的有效性，实现了高端到端成功率。

## Overview
An elusive goal in navigation research is to build an intelligent agent that can understand multimodal instructions including natural language and image, and perform useful navigation. To achieve this, we study a widely useful category of navigation tasks we call Multimodal Instruction Navigation with demonstration Tours (MINT), in which the environment prior is provided through a previously recorded demonstration video. Recent advances in Vision Language Models (VLMs) have shown a promising path in achieving this goal as it demonstrates capabilities in perceiving and reasoning about multimodal inputs. However, VLMs are typically trained to predict textual output and it is an open research question about how to best utilize them in navigation. To solve MINT, we present Mobility VLA, a hierarchical Vision-Language-Action (VLA) navigation policy that combines the environment understanding and common sense reasoning power of long-context VLMs and a robust low-level navigation policy based on topological graphs. The high-level policy consists of a long-context VLM that takes the demonstration tour video and the multimodal user instruction as input to find the goal frame in the tour video. Next, a low-level policy uses the goal frame and an offline constructed topological graph to generate robot actions at every timestep. We evaluated Mobility VLA in a 836m^2 real world environment and show that Mobility VLA has a high end-to-end success rates on previously unsolved multimodal instructions such as "Where should I return this?" while holding a plastic bin. A video demonstrating Mobility VLA can be found here: https://youtu.be/-Tof__Q8_5s

## 参考
- http://arxiv.org/abs/2407.07775v2

## 개요
Mobility VLA는 자연어와 이미지 등 다중 모달 명령을 이해하고 유용한 내비게이션을 수행할 수 있는 에이전트를 구축하는 것을 목표로 한다. 이는 MINT라는 내비게이션 작업 클래스를 대상으로 하며, 환경 사전 정보는 사전 녹화된 데모 비디오를 통해 제공된다. 이 모델은 계층적 아키텍처를 채택한다: 상위 정책은 장기 컨텍스트 VLM을 사용하여 데모 비디오와 다중 모달 사용자 명령을 입력으로 받아 데모 비디오에서 목표 프레임을 찾는다; 하위 정책은 해당 목표 프레임과 오프라인으로 구축된 토폴로지 맵을 활용하여 각 시간 단계에서 로봇 동작을 생성한다. 836m²의 실제 환경에서 Mobility VLA는 사용자가 플라스틱 상자를 들고 "이걸 어디에 돌려놓아야 하나요?"라고 묻는 등 이전에는 처리할 수 없었던 다중 모달 명령을 성공적으로 해결했다.

## 핵심 내용
### 방법
Mobility VLA는 장기 컨텍스트 VLM과 토폴로지 맵 기반의 하위 정책을 결합한 계층적 비전-언어-동작(VLA) 내비게이션 정책을 채택한다.

### 아키텍처
- **상위 정책**: 장기 컨텍스트 VLM을 사용하여 데모 비디오와 다중 모달 사용자 명령(자연어 및 이미지)을 입력으로 받아 데모 비디오에서 목표 프레임을 출력한다.
- **하위 정책**: 오프라인으로 구축된 토폴로지 맵을 기반으로 목표 프레임을 활용하여 각 시간 단계에서 로봇 동작을 생성한다.

### 실험 설정
- **환경**: 836m²의 실제 환경.
- **작업**: 다중 모달 명령 내비게이션 작업(MINT), 환경 사전 정보는 사전 녹화된 데모 비디오를 통해 제공된다.

### 주요 수치
- 836m²의 실제 환경에서 테스트됨.
- "Where should I return this?"(사용자가 플라스틱 상자를 들고 있을 때)와 같은 이전에 해결되지 않은 다중 모달 명령을 성공적으로 해결함.

### 결론
Mobility VLA는 장기 컨텍스트 VLM과 토폴로지 맵을 결합하여 다중 모달 명령 내비게이션 작업을 해결하는 데 효과적임을 입증했으며, 높은 종단 간 성공률을 달성했다.
