---
$id: ent_paper_wu_moto_a_zero_shot_plug_in_inter_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation'
  zh: MoTo
  ko: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation'
summary:
  en: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (MoTo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Key Laboratory of Embodied Intelligence Systems, Beijing National
    Research Center for Information Science and Technology, School of Electrical and Electronic Engineering, Nanyang Technological
    University, School of IEA, Beijing University of Posts and Telecommunications, Department of Automation, Tsinghua University,
    and published at CoRL25.'
  zh: MoTo 是一个零样本即插即用的交互感知导航模块，由北京重点实验室、南洋理工大学、清华大学等机构联合提出，发表于 CoRL25。其核心贡献在于将固定基座操作基础模型扩展至移动操作场景，无需额外训练数据即可实现通用移动操作。
  ko: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (MoTo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Key Laboratory of Embodied Intelligence Systems, Beijing National
    Research Center for Information Science and Technology, School of Electrical and Electronic Engineering, Nanyang Technological
    University, School of IEA, Beijing University of Posts and Telecommunications, Department of Automation, Tsinghua University,
    and published at CoRL25.'
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
- moto
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.01658v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (688 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.01658
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MoTo source
  url: https://doi.org/10.48550/arXiv.2509.01658
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MoTo 针对传统移动操作方法难以泛化的问题，设计了一个即插即用模块，可与任意现成的固定基座操作基础模型结合。它通过交互感知导航策略生成机器人对接点，并利用多视角一致的视觉语言模型（VLM）提取交互关键点，同时优化移动基座与机械臂的运动规划目标。该方法在 OVMM 基准和真实场景中分别比现有最优方法高出 2.68% 和 16.67% 的成功率，且无需移动操作专家数据。

## 核心内容
### 方法架构
MoTo 作为即插即用模块，核心包含三个组件：
- **交互感知导航策略**：基于 VLM 生成目标物体和机械臂的交互关键点，通过多视角一致性确保准确性。
- **运动规划目标**：最小化两个关键点之间的距离，同时保证轨迹的物理可行性（如避障、关节限制）。
- **零样本能力**：无需移动操作专家数据，直接利用固定基座操作基础模型（如 RT-2、Octo）完成移动操作。

### 实验设置
- **基准测试**：在 OVMM（Open Vocabulary Mobile Manipulation）基准和真实场景中评估。
- **对比方法**：与 SOTA 移动操作方法（如 MOMA、M3）对比，MoTo 在 OVMM 上成功率达 2.68%（相对提升），真实场景达 16.67%。
- **关键参数**：VLM 使用 GPT-4V 生成关键点，轨迹优化采用二次规划（QP）求解。

### 结论
MoTo 通过即插即用设计，显著提升了固定基座操作基础模型的移动操作能力，零样本泛化至新任务和环境。未来工作可探索更高效的 VLM 推理和动态场景适应。

## Overview
Mobile manipulation stands as a core challenge in robotics, enabling robots to assist humans across varied tasks and dynamic daily environments. Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training. However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a fixed setting. Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability. Specifically, we propose an interaction-aware navigation policy to generate robot docking points for generalized mobile manipulation. To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base manipulation foundation models can be employed. We further propose motion planning objectives for the mobile base and robot arm, which minimize the distance between the two keypoints and maintain the physical feasibility of trajectories. In this way, MoTo guides the robot to move to the docking points where fixed-base manipulation can be successfully performed, and leverages VLM generation and trajectory optimization to achieve mobile manipulation in a zero-shot manner, without any requirement on mobile manipulation expert data. Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional training data.

## 参考
- http://arxiv.org/abs/2509.01658v1

## 개요
MoTo는 전통적인 이동 조작 방법이 일반화되기 어려운 문제를 해결하기 위해, 임의의 기존 고정 베이스 조작 기반 모델과 결합할 수 있는 플러그 앤 플레이 모듈을 설계했습니다. 이는 상호작용 인식 내비게이션 전략을 통해 로봇의 도킹 지점을 생성하고, 다중 시점 일관성을 갖춘 비전-언어 모델(VLM)을 활용하여 상호작용 핵심 지점을 추출하며, 동시에 이동 베이스와 로봇 팔의 운동 계획 목표를 최적화합니다. 이 방법은 OVMM 벤치마크와 실제 환경에서 각각 기존 최고 성능 방법보다 2.68% 및 16.67% 더 높은 성공률을 달성하며, 이동 조작 전문가 데이터가 필요하지 않습니다.

## 핵심 내용
### 방법 아키텍처
MoTo는 플러그 앤 플레이 모듈로서 핵심적으로 세 가지 구성 요소를 포함합니다:
- **상호작용 인식 내비게이션 전략**: VLM을 기반으로 대상 객체와 로봇 팔의 상호작용 핵심 지점을 생성하고, 다중 시점 일관성을 통해 정확성을 보장합니다.
- **운동 계획 목표**: 두 핵심 지점 간의 거리를 최소화하면서 궤적의 물리적 실현 가능성(예: 장애물 회피, 관절 제한)을 보장합니다.
- **제로샷 능력**: 이동 조작 전문가 데이터 없이 고정 베이스 조작 기반 모델(예: RT-2, Octo)을 직접 활용하여 이동 조작을 완료합니다.

### 실험 설정
- **벤치마크 테스트**: OVMM(Open Vocabulary Mobile Manipulation) 벤치마크와 실제 환경에서 평가합니다.
- **비교 방법**: SOTA 이동 조작 방법(예: MOMA, M3)과 비교하여, MoTo는 OVMM에서 성공률 2.68%(상대적 향상), 실제 환경에서 16.67%를 달성합니다.
- **핵심 매개변수**: VLM은 GPT-4V를 사용하여 핵심 지점을 생성하고, 궤적 최적화는 이차 계획(QP)을 통해 해결합니다.

### 결론
MoTo는 플러그 앤 플레이 설계를 통해 고정 베이스 조작 기반 모델의 이동 조작 능력을 크게 향상시키며, 새로운 작업과 환경에 제로샷으로 일반화합니다. 향후 연구에서는 더 효율적인 VLM 추론과 동적 환경 적응을 탐구할 수 있습니다.
