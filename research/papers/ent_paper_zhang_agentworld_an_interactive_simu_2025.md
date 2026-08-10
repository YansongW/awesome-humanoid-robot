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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.07770v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (904 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2508.07770v2

## 개요
AgentWorld은 가정용 이동 조작 능력 개발을 위한 인터랙티브 시뮬레이션 플랫폼으로, 텐센트 Robotics X와 상하이교통대학이 공동으로 제안했습니다. 이 플랫폼은 자동화된 장면 구축 기능을 통합하여 레이아웃 생성, 의미론적 자산 배치, 시각적 재질 구성 및 물리 시뮬레이션 실행을 지원하며, 바퀴형 섀시와 휴머노이드 운동 정책을 기반으로 한 이중 모드 원격 조작 데이터 수집 시스템을 동시에 지원합니다. 이로부터 생성된 AgentWorld Dataset은 픽-앤-플레이스, 푸시-풀과 같은 기본 동작부터 음료 서빙, 음식 가열과 같은 다단계 작업까지 포괄하며, 장면은 거실, 침실, 주방을 포함합니다. 행동 클로닝, 액션 청킹 트랜스포머, 확산 정책 및 비전-언어-행동 모델과 같은 모방 학습 방법에 대한 광범위한 벤치마킹을 통해, 이 데이터셋은 시뮬레이션-실제 전이 작업에서 효과성을 입증했으며, 복잡한 가정 환경에서 확장 가능한 로봇 기술 습득을 위한 완전한 솔루션을 제공합니다.

## 핵심 내용
### 플랫폼 아키텍처
AgentWorld의 핵심은 두 가지 주요 모듈로 구성됩니다:
- **자동화된 장면 구축**: 레이아웃 생성, 의미론적 자산 배치, 시각적 재질 구성 및 물리 시뮬레이션을 지원하여 다양한 가정 환경을 빠르게 생성할 수 있습니다.
- **이중 모드 원격 조작 시스템**: 바퀴형 섀시와 휴머노이드 운동 정책을 동시에 지원하여 로봇 조작 데이터를 효율적으로 수집합니다.

### 데이터셋 및 작업
AgentWorld Dataset은 세 가지 가정 장면(거실, 침실, 주방)을 포괄하며, 작업은 다음과 같이 구분됩니다:
- **기본 동작**: 픽-앤-플레이스, 푸시-풀 등.
- **다단계 활동**: 음료 서빙, 음식 가열과 같은 복잡한 작업.

### 실험 설정 및 벤치마킹
연구팀은 다양한 모방 학습 방법에 대해 벤치마킹을 수행했습니다:
- 행동 클로닝(Behavior Cloning)
- 액션 청킹 트랜스포머(Action Chunking Transformers)
- 확산 정책(Diffusion Policies)
- 비전-언어-행동 모델(Vision-Language-Action Models)

실험 결과, 이 데이터셋은 시뮬레이션-실제 전이 작업에서 효과적임을 보여주며, 시뮬레이션 훈련과 실제 배포 간의 격차를 해소할 수 있음을 입증했습니다.

### 결론
AgentWorld은 복잡한 가정 환경에서 확장 가능한 로봇 기술 습득을 위한 완전한 솔루션을 제공합니다. 코드와 데이터셋은 오픈소스로 공개되었으며, 접속 주소는 다음과 같습니다: https://yizhengzhang1.github.io/agent_world/
