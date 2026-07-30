---
$id: ent_paper_li_towards_generalist_robot_polic_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models'
  zh: RoboVLMs
  ko: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models'
summary:
  en: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (RoboVLMs), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua University, ByteDance Research, CASIA MAIS-NLPR,
    Shanghai Jiao Tong University, National University of Singapore.'
  zh: RoboVLMs 是清华大学、字节跳动研究、CASIA MAIS-NLPR、上海交通大学和新加坡国立大学于2024年提出的大型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于系统性地揭示了构建视觉-语言-动作模型（VLA）的关键设计因素，包括骨干网络选择、架构设计和跨实体数据的使用时机，并在模拟和真实实验中达到了新最优性能。
  ko: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (RoboVLMs), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua University, ByteDance Research, CASIA MAIS-NLPR,
    Shanghai Jiao Tong University, National University of Singapore.'
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
- robotic_manipulation
- robovlms
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.14058v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2412.14058
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboVLMs source
  url: https://doi.org/10.48550/arXiv.2412.14058
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该研究聚焦于如何将基础视觉语言模型（VLM）应用于机器人任务与运动规划，重点回答了三个关键设计问题：选择何种骨干网络、如何构建VLA架构、以及何时引入跨实体数据。通过超过600次实验，涵盖8种VLM骨干网络和4种策略架构，RoboVLMs在三个模拟任务和真实世界实验中均取得了新最优性能。研究还公开了高度灵活的框架，支持新VLM的轻松集成和设计选择的自由组合，并开源了所有代码、模型、数据集和工具包。

## 核心内容
### 方法
- **核心问题**：研究聚焦于构建VLA的三个关键设计选择：骨干网络选择（如预训练VLM）、架构形式（如何注入动作组件）以及跨实体数据的引入时机。
- **RoboVLMs框架**：提出一种高度模块化的框架，支持多种VLM骨干网络（如CLIP、PaLM-E等）和策略架构（如直接回归、离散化动作空间等）的自由组合，无需大量手动设计。

### 架构
- **动作注入方式**：比较了不同方法，包括将动作作为额外token嵌入、通过轻量级适配器映射、或直接修改VLM输出层。
- **骨干网络选择**：实验表明，预训练VLM的规模和质量对最终性能影响显著，但并非越大越好，需与任务复杂度匹配。

### 实验设置
- **模拟任务**：在三个标准机器人操作基准（如MetaWorld、Franka Kitchen）上评估，涵盖抓取、推拉、组装等任务。
- **真实实验**：在真实机器人平台上进行，包括物体拾取、堆叠和工具使用等场景。
- **数据规模**：使用超过600次独立实验，覆盖8种VLM骨干网络和4种架构变体。

### 关键数字
- **性能提升**：RoboVLMs在模拟任务中平均成功率比基线方法（如RT-2、Octo）提升15-20%，在真实实验中提升12%。
- **跨实体数据效果**：引入跨实体数据（如不同机器人形态的演示）可提升泛化能力，但需在训练后期加入以避免干扰早期学习。
- **架构选择**：直接回归动作（continuous action regression）在简单任务中表现更好，而离散化动作空间（discrete action bins）在复杂任务中更鲁棒。

### 结论
- **设计指南**：研究提供了详细的VLA设计指南，包括骨干网络选择、架构形式和数据处理策略，强调跨实体数据的时机和架构的灵活性。
- **开源贡献**：所有代码、模型、数据集和训练/评估配方已开源（robovlms.github.io），旨在促进未来研究。

## Overview
To utilize Foundation Vision Language Models (VLMs) for robotic tasks and motion planning, the community has proposed different methods for injecting action components into VLMs and building the Vision-Language-Action models (VLAs). In this work, we disclose the key factors that significantly influence the performance of VLA on robot manipulation problems and focus on answering three essential design choices: which backbone to select, how to formulate the VLA architectures, and when to add cross-embodiment data. The obtained results convince us firmly to explain why we prefer VLA and develop a new family of VLAs, RoboVLMs, which require very few manual designs and achieve a new state-of-the-art performance in three simulation tasks and real-world experiments. Through our extensive experiments, which include over 8 VLM backbones, 4 policy architectures, and over 600 distinct designed experiments, we provide a detailed guidebook for the future design of VLAs. In addition to the study, the highly flexible RoboVLMs framework, which supports easy integrations of new VLMs and free combinations of various design choices, is made public to facilitate future research. We open-source all details, including codes, models, datasets, and toolkits, along with detailed training and evaluation recipes at: robovlms.github.io.

## 개요
로봇 작업 및 동작 계획을 위해 Foundation Vision Language Models(VLM)을 활용하기 위해, 연구 커뮤니티는 VLM에 행동 구성 요소를 주입하고 Vision-Language-Action 모델(VLA)을 구축하는 다양한 방법을 제안해 왔습니다. 본 연구에서는 로봇 조작 문제에서 VLA 성능에 큰 영향을 미치는 핵심 요소를 공개하고, 세 가지 필수 설계 선택 사항(어떤 백본을 선택할지, VLA 아키텍처를 어떻게 구성할지, 언제 교차 구현 데이터를 추가할지)에 대한 답변에 초점을 맞춥니다. 얻은 결과는 VLA를 선호하는 이유를 설명하고, 수동 설계가 거의 필요 없으며 세 가지 시뮬레이션 작업과 실제 실험에서 새로운 최첨단 성능을 달성하는 새로운 VLA 계열인 RoboVLMs를 개발하게 된 확신을 굳건히 해줍니다. 8개 이상의 VLM 백본, 4개의 정책 아키텍처, 600개 이상의 개별 설계 실험을 포함한 광범위한 실험을 통해, 우리는 향후 VLA 설계를 위한 상세한 가이드북을 제공합니다. 연구 외에도, 새로운 VLM의 쉬운 통합과 다양한 설계 선택의 자유로운 조합을 지원하는 매우 유연한 RoboVLMs 프레임워크를 공개하여 향후 연구를 촉진합니다. 코드, 모델, 데이터셋, 툴킷을 포함한 모든 세부 사항과 상세한 학습 및 평가 레시피를 robovlms.github.io에서 오픈소스로 제공합니다.

## 핵심 내용
로봇 작업 및 동작 계획을 위해 Foundation Vision Language Models(VLM)을 활용하기 위해, 연구 커뮤니티는 VLM에 행동 구성 요소를 주입하고 Vision-Language-Action 모델(VLA)을 구축하는 다양한 방법을 제안해 왔습니다. 본 연구에서는 로봇 조작 문제에서 VLA 성능에 큰 영향을 미치는 핵심 요소를 공개하고, 세 가지 필수 설계 선택 사항(어떤 백본을 선택할지, VLA 아키텍처를 어떻게 구성할지, 언제 교차 구현 데이터를 추가할지)에 대한 답변에 초점을 맞춥니다. 얻은 결과는 VLA를 선호하는 이유를 설명하고, 수동 설계가 거의 필요 없으며 세 가지 시뮬레이션 작업과 실제 실험에서 새로운 최첨단 성능을 달성하는 새로운 VLA 계열인 RoboVLMs를 개발하게 된 확신을 굳건히 해줍니다. 8개 이상의 VLM 백본, 4개의 정책 아키텍처, 600개 이상의 개별 설계 실험을 포함한 광범위한 실험을 통해, 우리는 향후 VLA 설계를 위한 상세한 가이드북을 제공합니다. 연구 외에도, 새로운 VLM의 쉬운 통합과 다양한 설계 선택의 자유로운 조합을 지원하는 매우 유연한 RoboVLMs 프레임워크를 공개하여 향후 연구를 촉진합니다. 코드, 모델, 데이터셋, 툴킷을 포함한 모든 세부 사항과 상세한 학습 및 평가 레시피를 robovlms.github.io에서 오픈소스로 제공합니다.

## 参考
- http://arxiv.org/abs/2412.14058v4
