---
$id: ent_paper_synagent_generalizable_coopera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy'
  zh: SynAgent｜通过单独与合作的智能体协同进行可推广的合作人形操作
  ko: 'SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy'
summary:
  en: Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due
    to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this
    paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation
    by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent
    human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving
    retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial
    relationships among humans and objects. Building upon this refined da
  zh: SynAgent 是一个由研究团队提出的统一框架，旨在解决具身智能中可控协作人形操控的难题。其核心贡献在于通过“从单智能体到协作智能体协同”策略，将单智能体的人-物交互技能迁移至多智能体的人-物-人场景，并显著提升了跨物体的泛化能力。
  ko: SynAgent 先从相机图像/多视角观测恢复场景、目标或运动表征，再用教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配生成全身轨迹/动作序列、地形/场景表征。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- scene_understanding
- synagent
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: SynAgent: Generalizable
    Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy. [2026-07-29] zh content backfilled from English
    abstract via scripts/sinicize_english_cards.py'
sources:
- id: src_001
  type: website
  title: SynAgent project page
  url: https://yw0208.github.io/synagent/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
SynAgent 框架通过创新的“从单智能体到协作智能体协同”方法，有效应对了协作人形操控中数据稀缺、多智能体协调复杂及泛化能力有限等挑战。该框架首先利用基于 Delaunay 四面体化构建的交互网格，提出了一种保持交互的重定向方法，以在运动迁移过程中忠实维持人与物体间的空间关系。在此基础上，SynAgent 采用单智能体预训练与适应范式，通过分散训练和多智能体 PPO 算法，从丰富的单智能体数据中引导出协同行为。最后，框架通过条件 VAE 开发了轨迹条件生成策略，并利用多教师蒸馏技术从运动模仿先验中学习，实现了稳定且可控的物体级轨迹执行。

## 核心内容
### 方法架构
SynAgent 框架的核心流程分为三个关键阶段：

1.  **保持交互的重定向**：
    *   为解决从单智能体到多智能体场景运动迁移时的语义完整性，提出了基于 **Interact Mesh** 的重定向方法。
    *   **Interact Mesh** 通过 **Delaunay tetrahedralization** 构建，能够精确捕捉并保持人与物体之间的空间关系。
    *   该方法确保了迁移后的多智能体交互在物理上合理且语义一致。

2.  **单智能体预训练与适应范式**：
    *   利用丰富的单智能体人-物交互数据作为起点。
    *   采用**分散训练**策略，每个智能体独立学习，并通过**多智能体 PPO** 算法进行协同优化。
    *   该范式能够从单智能体数据中有效引导出多智能体的协作行为，解决了数据稀缺问题。

3.  **轨迹条件生成策略**：
    *   基于**条件 VAE** 开发，用于生成稳定且可控的物体级轨迹。
    *   通过**多教师蒸馏**技术，从多个运动模仿先验中学习，提升了策略的鲁棒性和控制精度。
    *   该策略使得智能体能够根据给定的轨迹条件，执行精确的协作操控动作。

### 实验设置与结果
*   **基准对比**：在**协作模仿**和**轨迹条件控制**两项任务上，SynAgent 均显著优于现有基线方法。
*   **泛化能力**：实验证明 SynAgent 能够有效泛化到**多种不同几何形状的物体**，展现了其强大的跨物体泛化能力。
*   **关键数据**：论文未在摘要中提供具体数值，但强调实验结果的优越性。代码与数据将在论文发表后公开。

### 结论
SynAgent 通过创新的“从单智能体到协作智能体协同”框架，成功解决了协作人形操控中的核心难题，为具身智能在复杂多智能体场景下的应用提供了可扩展且物理合理的解决方案。

## Overview
Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: http://yw0208.github.io/synagent

## 개요
제어 가능한 협력적 휴머노이드 조작은 심각한 데이터 부족, 다중 에이전트 협력의 복잡성, 그리고 객체 간 일반화의 한계로 인해 구현 지능(embodied intelligence)의 근본적이면서도 어려운 문제입니다. 본 논문에서는 단일 에이전트-객체 상호작용에서 다중 에이전트 인간-객체-인간 시나리오로 기술을 전이하기 위해 Solo-to-Cooperative Agent Synergy를 활용하여 확장 가능하고 물리적으로 타당한 협력 조작을 가능하게 하는 통합 프레임워크인 SynAgent를 제시합니다. 동작 전이 중 의미적 무결성을 유지하기 위해, Delaunay 사면체화를 통해 구축된 Interact Mesh를 기반으로 하는 상호작용 보존 리타겟팅 방법을 도입하여 인간과 객체 간의 공간적 관계를 충실히 유지합니다. 이 정제된 데이터를 기반으로, 분산 훈련과 다중 에이전트 PPO를 통해 풍부한 단일 인간 데이터로부터 시너지 협력 행동을 부트스트래핑하는 단일 에이전트 사전 훈련 및 적응 패러다임을 제안합니다. 마지막으로, 조건부 VAE를 사용한 궤적 조건 생성 정책을 개발하고, 동작 모방 사전 정보로부터 다중 교사 증류를 통해 훈련하여 안정적이고 제어 가능한 객체 수준 궤적 실행을 달성합니다. 광범위한 실험을 통해 SynAgent가 협력 모방과 궤적 조건 제어 모두에서 기존 기준선을 크게 능가하며, 다양한 객체 형상에 걸쳐 일반화됨을 입증합니다. 코드와 데이터는 출판 후 공개될 예정입니다. 프로젝트 페이지: http://yw0208.github.io/synagent

## 핵심 내용
제어 가능한 협력적 휴머노이드 조작은 심각한 데이터 부족, 다중 에이전트 협력의 복잡성, 그리고 객체 간 일반화의 한계로 인해 구현 지능(embodied intelligence)의 근본적이면서도 어려운 문제입니다. 본 논문에서는 단일 에이전트-객체 상호작용에서 다중 에이전트 인간-객체-인간 시나리오로 기술을 전이하기 위해 Solo-to-Cooperative Agent Synergy를 활용하여 확장 가능하고 물리적으로 타당한 협력 조작을 가능하게 하는 통합 프레임워크인 SynAgent를 제시합니다. 동작 전이 중 의미적 무결성을 유지하기 위해, Delaunay 사면체화를 통해 구축된 Interact Mesh를 기반으로 하는 상호작용 보존 리타겟팅 방법을 도입하여 인간과 객체 간의 공간적 관계를 충실히 유지합니다. 이 정제된 데이터를 기반으로, 분산 훈련과 다중 에이전트 PPO를 통해 풍부한 단일 인간 데이터로부터 시너지 협력 행동을 부트스트래핑하는 단일 에이전트 사전 훈련 및 적응 패러다임을 제안합니다. 마지막으로, 조건부 VAE를 사용한 궤적 조건 생성 정책을 개발하고, 동작 모방 사전 정보로부터 다중 교사 증류를 통해 훈련하여 안정적이고 제어 가능한 객체 수준 궤적 실행을 달성합니다. 광범위한 실험을 통해 SynAgent가 협력 모방과 궤적 조건 제어 모두에서 기존 기준선을 크게 능가하며, 다양한 객체 형상에 걸쳐 일반화됨을 입증합니다. 코드와 데이터는 출판 후 공개될 예정입니다. 프로젝트 페이지: http://yw0208.github.io/synagent

## 参考
- Semantic Scholar search: SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy
