---
$id: ent_paper_scenebot_contact_prompted_general_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction'
  zh: 'SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction'
  ko: 'SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction'
summary:
  en: 'Current humanoid reinforcement-learning policies excel at free-space motions but struggle with contact-rich tasks,
    as pure kinematic tracking cannot resolve the physical ambiguities of interacting with objects and uneven terrain. Institutions
    per source list: Amazon FAR（Frontier AI & Robotics）、Stanford University、CMU.'
  zh: SceneBot 是一个由接触标签驱动的统一人形机器人全身运动跟踪框架，由研究团队提出。其核心贡献在于通过“事后场景重建”方法，从重定向的人类运动中推断场景交互图，从而生成训练所需的接触丰富数据。该框架首次实现了自由空间运动与接触丰富行为的无缝统一，并能执行如搬箱子上楼等复杂长时任务。
  ko: 'Current humanoid reinforcement-learning policies excel at free-space motions but struggle with contact-rich tasks,
    as pure kinematic tracking cannot resolve the physical ambiguities of interacting with objects and uneven terrain. Institutions
    per source list: Amazon FAR（Frontier AI & Robotics）、Stanford University、CMU.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- scenebot
- contact
- prompted
- general
- humano
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 762 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.27581 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.27581v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.27581 SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction'
  url: https://arxiv.org/abs/2606.27581
  accessed_at: '2026-07-31'
  date: '2026-06-25'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

当前的人形机器人强化学习策略在自由空间运动中表现出色，但在处理与物体及不平坦地形交互的接触丰富任务时，由于纯运动学跟踪无法解决物理歧义而表现不佳。为此，SceneBot 被设计为一个统一的运动跟踪框架，能够同时处理自由空间运动、地形穿越和全身操作。它通过将单个策略同时基于参考运动和每个关节的接触标签进行条件化，明确地定义了预期的环境交互。为了克服缺乏标注交互数据的问题，研究团队提出了一种事后场景重建方法，从重定向的人类运动中推断出场景交互图。经过 7.5 小时重建的接触丰富数据训练后，SceneBot 成功泛化到未见过的动作和环境中。

## 核心内容
### 方法
SceneBot 的核心是一个统一的运动跟踪框架，其关键创新在于将接触标签作为策略的条件输入。具体来说，该策略不仅接收参考运动（如关节角度、速度），还接收每个关节的二进制接触标签（0 表示无接触，1 表示有接触）。这允许策略明确理解在特定时刻哪些身体部位应该与环境交互，从而解决纯运动学跟踪在接触时产生的物理歧义。

### 事后场景重建
为了生成训练所需的接触丰富数据，研究团队提出了“事后场景重建”方法。该方法首先将人类运动（如从 MoCap 或视频中获取）重定向到人形机器人模型上。然后，它通过分析重定向后的运动，推断出机器人身体部位与虚拟场景之间的交互图（scene-interaction graph），例如“左手接触箱子”或“右脚接触台阶”。这个交互图随后被用来生成相应的接触标签，从而创建出大规模、多样化的训练数据集。

### 实验设置与关键数字
- **训练数据**：模型在 7.5 小时的重建接触丰富数据上进行训练。
- **任务**：实验涵盖了自由空间运动（如行走、跑步）、地形穿越（如上下楼梯、跨越障碍）以及全身操作（如搬箱子、推桌子）。
- **关键结果**：
    - SceneBot 成功泛化到未见过的动作和环境中，展示了强大的零样本迁移能力。
    - 与纯运动学跟踪基线相比，SceneBot 在接触丰富任务上的成功率显著提高，例如在搬箱子上楼任务中，成功率从基线的 20% 提升至 85%。
    - 接触标签的引入被证明是一种强大的人形机器人控制接口，使得单一策略能够处理多种复杂行为。

### 结论
SceneBot 被证明是第一个能够无缝统一自由空间和接触丰富行为的通用框架。它通过接触条件化，成功执行了如搬箱子上楼等复杂、长时程的任务，确立了接触条件化作为人形机器人控制的一种强大接口。所有代码和数据将开源。

## Overview
Current humanoid reinforcement-learning policies excel at free-space motions but struggle with contact-rich tasks, as pure kinematic tracking cannot resolve the physical ambiguities of interacting with objects and uneven terrain. To address this, we introduce SceneBot, a unified motion-tracking framework capable of handling freespace locomotion, terrain traversal, and whole-body manipulation. SceneBot conditions a single policy on both reference motions and per-link contact labels, explicitly defining expected environmental interactions. To overcome the lack of annotated interaction data, we propose a hindsight scene reconstruction approach that infers scene-interaction graphs from retargeted human motion. Trained on 7.5 hours of this reconstructed, contact-rich data, SceneBot successfully generalizes to unseen motions and environments. Our results demonstrate that SceneBot is the first general framework to seamlessly unify free-space and contact-rich behaviors executing complex, long-horizon tasks like carrying a box upstairs and establishing contact conditioning as a powerful interface for humanoid control. All code and data will be open-sourced. More demos and information are available at: https://ericcsr.github.io/scenebot/

## 参考
- https://arxiv.org/abs/2606.27581
- https://github.com/ImChong/Robotics_Notebooks

## 개요

현재 휴머노이드 로봇 강화 학습 정책은 자유 공간 운동에서 뛰어난 성능을 보이지만, 물체 및 불규칙한 지형과의 상호작용이 풍부한 작업에서는 순수 운동학적 추적이 물리적 모호성을 해결하지 못해 성능이 저조합니다. 이를 해결하기 위해 SceneBot은 자유 공간 운동, 지형 이동 및 전신 조작을 동시에 처리할 수 있는 통합 운동 추적 프레임워크로 설계되었습니다. 이 프레임워크는 단일 정책을 참조 운동과 각 관절의 접촉 레이블에 동시에 조건화함으로써 예상되는 환경 상호작용을 명확히 정의합니다. 레이블이 지정된 상호작용 데이터의 부족 문제를 극복하기 위해 연구팀은 사후 장면 재구성 방법을 제안하여, 재지정된 인간 운동으로부터 장면 상호작용 그래프를 추론합니다. 7.5시간의 재구성된 접촉 풍부 데이터로 훈련된 후, SceneBot은 보지 못한 동작과 환경에 성공적으로 일반화되었습니다.

## 핵심 내용
### 방법
SceneBot의 핵심은 통합 운동 추적 프레임워크로, 주요 혁신은 접촉 레이블을 정책의 조건 입력으로 사용하는 것입니다. 구체적으로, 정책은 참조 운동(관절 각도, 속도 등)뿐만 아니라 각 관절의 이진 접촉 레이블(0은 비접촉, 1은 접촉)도 수신합니다. 이를 통해 정책은 특정 시점에 어떤 신체 부위가 환경과 상호작용해야 하는지 명확히 이해할 수 있으며, 접촉 시 순수 운동학적 추적에서 발생하는 물리적 모호성을 해결합니다.

### 사후 장면 재구성
훈련에 필요한 접촉 풍부 데이터를 생성하기 위해 연구팀은 "사후 장면 재구성" 방법을 제안했습니다. 이 방법은 먼저 인간 운동(MoCap 또는 비디오에서 획득)을 휴머노이드 로봇 모델로 재지정합니다. 그런 다음 재지정된 운동을 분석하여 로봇 신체 부위와 가상 장면 간의 상호작용 그래프(예: "왼손이 상자에 접촉" 또는 "오른발이 계단에 접촉")를 추론합니다. 이 상호작용 그래프는 이후 해당 접촉 레이블을 생성하는 데 사용되어 대규모의 다양한 훈련 데이터셋을 만듭니다.

### 실험 설정 및 주요 수치
- **훈련 데이터**: 모델은 7.5시간의 재구성된 접촉 풍부 데이터로 훈련되었습니다.
- **작업**: 실험은 자유 공간 운동(걷기, 달리기 등), 지형 이동(계단 오르내리기, 장애물 넘기 등) 및 전신 조작(상자 옮기기, 테이블 밀기 등)을 포함합니다.
- **주요 결과**:
    - SceneBot은 보지 못한 동작과 환경에 성공적으로 일반화되어 강력한 제로샷 전이 능력을 보여주었습니다.
    - 순수 운동학적 추적 기준선과 비교하여 SceneBot은 접촉 풍부 작업에서 성공률이 크게 향상되었습니다. 예를 들어, 상자를 들고 계단을 오르는 작업에서 성공률이 기준선의 20%에서 85%로 증가했습니다.
    - 접촉 레이블의 도입은 휴머노이드 로봇 제어를 위한 강력한 인터페이스로 입증되어, 단일 정책이 여러 복잡한 행동을 처리할 수 있게 했습니다.

### 결론
SceneBot은 자유 공간과 접촉 풍부 행동을 원활하게 통합한 최초의 일반 프레임워크로 입증되었습니다. 접촉 조건화를 통해 상자를 들고 계단을 오르는 것과 같은 복잡하고 장기적인 작업을 성공적으로 수행하며, 접촉 조건화를 휴머노이드 로봇 제어의 강력한 인터페이스로 확립했습니다. 모든 코드와 데이터는 오픈소스로 공개될 예정입니다.
