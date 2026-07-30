---
$id: ent_paper_zhang_agentworld_an_interactive_simu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation'
  zh: AgentWorld
  ko: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation'
summary:
  en: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation (AgentWorld),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tencent Robotics X, Shanghai Jiao
    Tong University, and published at CoRL25.'
  zh: AgentWorld 是腾讯 Robotics X 与上海交通大学于 2025 年 CoRL 会议提出的交互式仿真平台，专为家庭场景下的移动操作机器人设计。其核心贡献在于结合自动化场景构建（布局生成、语义资产放置、视觉材质配置与物理仿真）与双模式遥操作系统，并发布了涵盖从基础动作到多阶段任务的
    AgentWorld Dataset，通过多种模仿学习方法的基准测试验证了其仿真到现实迁移的有效性。
  ko: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation (AgentWorld),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tencent Robotics X, Shanghai Jiao
    Tong University, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- agentworld
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.07770v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.07770
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AgentWorld source
  url: https://doi.org/10.48550/arXiv.2508.07770
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
AgentWorld 是一个面向家庭移动操作能力开发的交互式仿真平台，由腾讯 Robotics X 与上海交通大学联合提出。该平台集成了自动化场景构建功能，能够生成布局、放置语义资产、配置视觉材质并运行物理仿真，同时支持基于轮式底盘与人形运动策略的双模式遥操作数据采集系统。由此产生的 AgentWorld Dataset 覆盖了从拾取-放置、推-拉等基础动作，到服务饮品、加热食物等多阶段任务，场景涵盖客厅、卧室与厨房。通过对行为克隆、动作分块变换器、扩散策略及视觉-语言-动作模型等模仿学习方法的广泛基准测试，该数据集在仿真到现实迁移任务中展现出有效性，为复杂家庭环境中的可扩展机器人技能获取提供了完整解决方案。

## 核心内容
### 平台架构
AgentWorld 的核心由两大模块构成：
- **自动化场景构建**：支持布局生成、语义资产放置、视觉材质配置与物理仿真，可快速创建多样化的家庭环境。
- **双模式遥操作系统**：同时兼容轮式底盘与人形运动策略，用于高效收集机器人操作数据。

### 数据集与任务
AgentWorld Dataset 覆盖三类家庭场景（客厅、卧室、厨房），任务分为：
- **基础动作**：拾取-放置、推-拉等。
- **多阶段活动**：服务饮品、加热食物等复杂任务。

### 实验设置与基准测试
研究团队对多种模仿学习方法进行了基准测试，包括：
- 行为克隆（Behavior Cloning）
- 动作分块变换器（Action Chunking Transformers）
- 扩散策略（Diffusion Policies）
- 视觉-语言-动作模型（Vision-Language-Action Models）

实验结果表明，该数据集在仿真到现实迁移任务中表现有效，能够弥合仿真训练与真实部署之间的差距。

### 结论
AgentWorld 提供了一个完整的解决方案，用于在复杂家庭环境中实现可扩展的机器人技能获取。代码与数据集已开源，访问地址为：https://yizhengzhang1.github.io/agent_world/

## Overview
We introduce AgentWorld, an interactive simulation platform for developing household mobile manipulation capabilities. Our platform combines automated scene construction that encompasses layout generation, semantic asset placement, visual material configuration, and physics simulation, with a dual-mode teleoperation system supporting both wheeled bases and humanoid locomotion policies for data collection. The resulting AgentWorld Dataset captures diverse tasks ranging from primitive actions (pick-and-place, push-pull, etc.) to multistage activities (serve drinks, heat up food, etc.) across living rooms, bedrooms, and kitchens. Through extensive benchmarking of imitation learning methods including behavior cloning, action chunking transformers, diffusion policies, and vision-language-action models, we demonstrate the dataset's effectiveness for sim-to-real transfer. The integrated system provides a comprehensive solution for scalable robotic skill acquisition in complex home environments, bridging the gap between simulation-based training and real-world deployment. The code, datasets will be available at https://yizhengzhang1.github.io/agent_world/

## 개요
우리는 가정용 모바일 조작 능력 개발을 위한 대화형 시뮬레이션 플랫폼인 AgentWorld를 소개합니다. 이 플랫폼은 레이아웃 생성, 의미론적 자산 배치, 시각적 재질 구성 및 물리 시뮬레이션을 포함한 자동화된 장면 구축과, 데이터 수집을 위해 바퀴형 베이스와 휴머노이드 이동 정책을 모두 지원하는 이중 모드 원격 조작 시스템을 결합합니다. 그 결과 생성된 AgentWorld 데이터셋은 거실, 침실, 주방에서 기본 동작(집기-놓기, 밀기-당기기 등)부터 다단계 활동(음료 서빙, 음식 데우기 등)까지 다양한 작업을 포괄합니다. 행동 복제, 행동 청킹 트랜스포머, 확산 정책, 비전-언어-행동 모델을 포함한 모방 학습 방법의 광범위한 벤치마킹을 통해 시뮬레이션-실제 전이에 대한 데이터셋의 효과를 입증합니다. 통합 시스템은 복잡한 가정 환경에서 확장 가능한 로봇 기술 습득을 위한 포괄적인 솔루션을 제공하며, 시뮬레이션 기반 훈련과 실제 배포 간의 격차를 해소합니다. 코드와 데이터셋은 https://yizhengzhang1.github.io/agent_world/에서 제공될 예정입니다.

## 핵심 내용
우리는 가정용 모바일 조작 능력 개발을 위한 대화형 시뮬레이션 플랫폼인 AgentWorld를 소개합니다. 이 플랫폼은 레이아웃 생성, 의미론적 자산 배치, 시각적 재질 구성 및 물리 시뮬레이션을 포함한 자동화된 장면 구축과, 데이터 수집을 위해 바퀴형 베이스와 휴머노이드 이동 정책을 모두 지원하는 이중 모드 원격 조작 시스템을 결합합니다. 그 결과 생성된 AgentWorld 데이터셋은 거실, 침실, 주방에서 기본 동작(집기-놓기, 밀기-당기기 등)부터 다단계 활동(음료 서빙, 음식 데우기 등)까지 다양한 작업을 포괄합니다. 행동 복제, 행동 청킹 트랜스포머, 확산 정책, 비전-언어-행동 모델을 포함한 모방 학습 방법의 광범위한 벤치마킹을 통해 시뮬레이션-실제 전이에 대한 데이터셋의 효과를 입증합니다. 통합 시스템은 복잡한 가정 환경에서 확장 가능한 로봇 기술 습득을 위한 포괄적인 솔루션을 제공하며, 시뮬레이션 기반 훈련과 실제 배포 간의 격차를 해소합니다. 코드와 데이터셋은 https://yizhengzhang1.github.io/agent_world/에서 제공될 예정입니다.

## 参考
- http://arxiv.org/abs/2508.07770v2
