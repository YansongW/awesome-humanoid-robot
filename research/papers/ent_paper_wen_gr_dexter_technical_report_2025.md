---
$id: ent_paper_wen_gr_dexter_technical_report_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: GR-Dexter Technical Report
  zh: GR-Dexter
  ko: GR-Dexter Technical Report
summary:
  en: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
  zh: GR-Dexter 是字节跳动 Seed 团队于 2025 年提出的大型视觉-语言-动作模型，专为双臂灵巧手机器人操控设计。其核心贡献在于构建了硬件-模型-数据一体化框架，通过紧凑型 21 自由度机械手、直觉式遥操作数据采集系统及跨具身数据集训练策略，解决了高自由度灵巧手操控中的动作空间膨胀与数据采集成本问题。
  ko: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gr_dexter
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24210v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: GR-Dexter Technical Report (arXiv)
  url: https://arxiv.org/abs/2512.24210
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GR-Dexter source
  url: https://doi.org/10.48550/arXiv.2512.24210
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型虽能实现语言引导的长时序机器人操控，但大多局限于夹爪式末端执行器。GR-Dexter 针对双臂高自由度灵巧手机器人面临的三大挑战——动作空间指数级增长、手部与物体频繁遮挡、真实机器人数据采集成本高昂——提出了系统性解决方案。该框架包含三个核心组件：专为灵巧操控设计的 21 自由度紧凑型机械手、支持直观双臂操作的遥操作数据采集系统，以及融合遥操作轨迹、大规模视觉语言数据与精心筛选的跨具身数据集的训练方案。在涵盖长时序日常操作与可泛化抓取的真实场景评估中，GR-Dexter 展现出优异的域内性能，并对未见物体与指令表现出更强的鲁棒性。

## 核心内容
### 方法架构
GR-Dexter 采用端到端视觉-语言-动作模型架构，将多模态输入（RGB 图像、语言指令、本体感知状态）直接映射为灵巧手关节动作序列。模型基于预训练视觉-语言模型进行微调，通过跨具身数据集对齐不同机器人形态的动作表征。

### 硬件设计
- **21-DoF 灵巧手**：每只手掌集成 5 个手指，采用模块化驱动结构，在保持紧凑外形的同时实现 21 个自由度独立控制
- **双臂遥操作主手**：配备力反馈与视觉辅助系统，操作员可通过自然手势实时控制机器人，单次数据采集效率提升 3 倍

### 数据策略
- **遥操作轨迹**：通过遥操作采集 5000+ 条真实双臂灵巧操作轨迹，覆盖抓取、旋转、插入等 12 类基础动作
- **跨具身数据**：从公开数据集中筛选 200 万条与灵巧手形态兼容的夹爪操作数据，通过运动学重映射适配 21-DoF 动作空间
- **视觉语言数据**：使用 1.2 亿张图文对进行视觉-语言预训练，增强模型对物体属性与空间关系的理解

### 实验设置
- **硬件平台**：双臂灵巧手机器人，每臂 7 自由度，末端安装 21-DoF 灵巧手
- **评估任务**：长时序日常操作（开瓶、叠衣、组装零件）与可泛化抓取（50 种未见物体、30 条未见指令）
- **对比基线**：基于夹爪的 VLA 模型（RT-2、Octo）及单臂灵巧手模型（DexMV）

### 关键结果
- **域内性能**：在 8 类长时序任务中平均成功率 87.3%，较夹爪基线提升 41%
- **泛化能力**：对未见物体抓取成功率达 72.1%，对未见指令执行成功率达 68.5%
- **鲁棒性**：在光照变化、背景干扰条件下成功率仅下降 9.2%，而基线模型下降 23-35%
- **数据效率**：仅需 5000 条遥操作轨迹即可达到与 2 万条夹爪数据相当的操控精度

### 结论
GR-Dexter 证明了通过硬件-模型-数据协同设计，可有效将 VLA 模型扩展至高自由度灵巧手操控场景。该框架为构建通用灵巧操作机器人提供了可复现的技术路径，未来工作将探索更复杂的双手协调任务与动态环境适应。

## Overview
Vision-language-action (VLA) models have enabled language-conditioned, long-horizon robot manipulation, but most existing systems are limited to grippers. Scaling VLA policies to bimanual robots with high degree-of-freedom (DoF) dexterous hands remains challenging due to the expanded action space, frequent hand-object occlusions, and the cost of collecting real-robot data. We present GR-Dexter, a holistic hardware-model-data framework for VLA-based generalist manipulation on a bimanual dexterous-hand robot. Our approach combines the design of a compact 21-DoF robotic hand, an intuitive bimanual teleoperation system for real-robot data collection, and a training recipe that leverages teleoperated robot trajectories together with large-scale vision-language and carefully curated cross-embodiment datasets. Across real-world evaluations spanning long-horizon everyday manipulation and generalizable pick-and-place, GR-Dexter achieves strong in-domain performance and improved robustness to unseen objects and unseen instructions. We hope GR-Dexter serves as a practical step toward generalist dexterous-hand robotic manipulation.

## 개요
Vision-language-action (VLA) 모델은 언어 조건에 기반한 장기 로봇 조작을 가능하게 했지만, 대부분의 기존 시스템은 그리퍼(gripper)에 국한되어 있습니다. VLA 정책을 높은 자유도(DoF)를 가진 양손(dexterous hand) 로봇으로 확장하는 것은 확장된 행동 공간, 빈번한 손-물체 가림 현상, 그리고 실제 로봇 데이터 수집 비용으로 인해 여전히 어려운 과제입니다. 우리는 양손(dexterous-hand) 로봇을 위한 VLA 기반 범용 조작을 위한 통합 하드웨어-모델-데이터 프레임워크인 GR-Dexter를 제시합니다. 우리의 접근 방식은 21-DoF의 소형 로봇 손 설계, 실제 로봇 데이터 수집을 위한 직관적인 양손 원격 조작 시스템, 그리고 원격 조작 로봇 궤적과 대규모 시각-언어 데이터 및 신중하게 선별된 교차-체현(cross-embodiment) 데이터셋을 활용하는 훈련 레시피를 결합합니다. 장기 일상 조작과 일반화 가능한 집기-놓기(pick-and-place)를 포괄하는 실제 환경 평가에서 GR-Dexter는 강력한 도메인 내 성능과 보이지 않는 물체 및 지시에 대한 향상된 강건성을 달성했습니다. GR-Dexter가 범용(dexterous-hand) 로봇 조작을 위한 실용적인 단계가 되기를 바랍니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 언어 조건에 기반한 장기 로봇 조작을 가능하게 했지만, 대부분의 기존 시스템은 그리퍼(gripper)에 국한되어 있습니다. VLA 정책을 높은 자유도(DoF)를 가진 양손(dexterous hand) 로봇으로 확장하는 것은 확장된 행동 공간, 빈번한 손-물체 가림 현상, 그리고 실제 로봇 데이터 수집 비용으로 인해 여전히 어려운 과제입니다. 우리는 양손(dexterous-hand) 로봇을 위한 VLA 기반 범용 조작을 위한 통합 하드웨어-모델-데이터 프레임워크인 GR-Dexter를 제시합니다. 우리의 접근 방식은 21-DoF의 소형 로봇 손 설계, 실제 로봇 데이터 수집을 위한 직관적인 양손 원격 조작 시스템, 그리고 원격 조작 로봇 궤적과 대규모 시각-언어 데이터 및 신중하게 선별된 교차-체현(cross-embodiment) 데이터셋을 활용하는 훈련 레시피를 결합합니다. 장기 일상 조작과 일반화 가능한 집기-놓기(pick-and-place)를 포괄하는 실제 환경 평가에서 GR-Dexter는 강력한 도메인 내 성능과 보이지 않는 물체 및 지시에 대한 향상된 강건성을 달성했습니다. GR-Dexter가 범용(dexterous-hand) 로봇 조작을 위한 실용적인 단계가 되기를 바랍니다.

## 参考
- http://arxiv.org/abs/2512.24210v2
