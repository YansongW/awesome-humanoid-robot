---
$id: ent_paper_bu_towards_synergistic_generalize_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation
  zh: RoboDual
  ko: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation
summary:
  en: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation (RoboDual), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong Univeristy, The University of Hong Kong, AgiBot, Shanghai
    AI Lab.
  zh: RoboDual 是上海交通大学、香港大学、AgiBot 和上海人工智能实验室于 2024 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于设计了一个协同双系统，融合通用策略的高层推理能力与专用策略的精确执行效率，显著提升了性能与部署效率。
  ko: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation (RoboDual), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong Univeristy, The University of Hong Kong, AgiBot, Shanghai
    AI Lab.
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
- robodual
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08001v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation (arXiv)
  url: https://arxiv.org/abs/2410.08001
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboDual source
  url: https://doi.org/10.48550/arXiv.2410.08001
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
RoboDual 针对通用策略推理效率低、训练成本高，以及专用策略泛化能力不足的问题，提出了一种协同双系统架构。该系统包含一个基于视觉-语言-动作（VLA）的通用策略，负责高层任务理解与离散动作输出；以及一个基于扩散变换器的专用策略，用于多步动作展开，并精细地以通用策略的输出为条件。实验表明，相比 OpenVLA，RoboDual 在真实场景中性能提升 26.7%，在 CALVIN 基准上提升 12%，且仅需 5% 的演示数据即可保持强性能，同时将实际部署中的控制频率提升 3.8 倍。

## 核心内容
### 方法
RoboDual 的核心是一个协同双系统，旨在结合通用策略与专用策略的优势：
- **通用策略**：基于视觉-语言-动作（VLA）模型，负责高层任务理解，并输出离散化的动作指令。
- **专用策略**：基于扩散变换器（Diffusion Transformer），以通用策略输出的高层任务理解和离散动作为条件，执行多步动作展开，实现精确的底层控制。

### 架构
- 通用策略提供任务级推理与动作规划，专用策略则专注于高效、精确的轨迹执行。
- 专用策略仅包含 2000 万个可训练参数，保持了轻量级特性。

### 实验设置
- 在真实世界场景和 CALVIN 基准上进行了评估。
- 与 OpenVLA 作为基线模型进行对比。

### 关键数字
- 在真实世界设置中，相比 OpenVLA，RoboDual 实现了 26.7% 的性能提升。
- 在 CALVIN 基准上，性能提升 12%。
- 仅使用 5% 的演示数据，即可保持强性能。
- 在实际部署中，控制频率提升 3.8 倍。

### 结论
RoboDual 通过协同双系统设计，有效解决了通用策略与专用策略各自的局限性，在保持泛化能力的同时，显著提升了推理效率、训练成本效益和部署性能。代码将公开，项目页面位于：https://opendrivelab.com/RoboDual/。

## Overview
The increasing demand for versatile robotic systems to operate in diverse and dynamic environments has emphasized the importance of a generalist policy, which leverages a large cross-embodiment data corpus to facilitate broad adaptability and high-level reasoning. However, the generalist would struggle with inefficient inference and cost-expensive training. The specialist policy, instead, is curated for specific domain data and excels at task-level precision with efficiency. Yet, it lacks the generalization capacity for a wide range of applications. Inspired by these observations, we introduce RoboDual, a synergistic dual-system that supplements the merits of both generalist and specialist policy. A diffusion transformer-based specialist is devised for multi-step action rollouts, exquisitely conditioned on the high-level task understanding and discretized action output of a vision-language-action (VLA) based generalist. Compared to OpenVLA, RoboDual achieves 26.7% improvement in real-world setting and 12% gain on CALVIN by introducing a specialist policy with merely 20M trainable parameters. It maintains strong performance with 5% of demonstration data only, and enables a 3.8 times higher control frequency in real-world deployment. Code would be made publicly available. Our project page is hosted at: https://opendrivelab.com/RoboDual/

## 개요
다양하고 동적인 환경에서 작동할 수 있는 다목적 로봇 시스템에 대한 수요 증가는 대규모 교차 체현 데이터 코퍼스를 활용하여 광범위한 적응성과 고수준 추론을 가능하게 하는 일반주의 정책의 중요성을 강조해 왔습니다. 그러나 일반주의 정책은 비효율적인 추론과 고비용 훈련이라는 문제를 겪습니다. 반면, 전문가 정책은 특정 도메인 데이터에 맞춰 제작되어 효율성과 함께 작업 수준의 정밀도에서 뛰어납니다. 하지만 광범위한 응용을 위한 일반화 능력이 부족합니다. 이러한 관찰에서 영감을 받아, 우리는 일반주의 정책과 전문가 정책의 장점을 모두 보완하는 시너지 이중 시스템인 RoboDual을 소개합니다. 확산 트랜스포머 기반의 전문가 정책은 다단계 행동 롤아웃을 위해 설계되었으며, 비전-언어-행동(VLA) 기반 일반주의 정책의 고수준 작업 이해와 이산화된 행동 출력에 정교하게 조건화됩니다. OpenVLA와 비교하여 RoboDual은 단 2천만 개의 훈련 가능한 파라미터를 가진 전문가 정책을 도입함으로써 실제 환경에서 26.7%의 성능 향상과 CALVIN에서 12%의 이득을 달성했습니다. 또한, 데모 데이터의 5%만으로도 강력한 성능을 유지하며, 실제 배포에서 3.8배 더 높은 제어 주파수를 가능하게 합니다. 코드는 공개될 예정입니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://opendrivelab.com/RoboDual/

## 핵심 내용
다양하고 동적인 환경에서 작동할 수 있는 다목적 로봇 시스템에 대한 수요 증가는 대규모 교차 체현 데이터 코퍼스를 활용하여 광범위한 적응성과 고수준 추론을 가능하게 하는 일반주의 정책의 중요성을 강조해 왔습니다. 그러나 일반주의 정책은 비효율적인 추론과 고비용 훈련이라는 문제를 겪습니다. 반면, 전문가 정책은 특정 도메인 데이터에 맞춰 제작되어 효율성과 함께 작업 수준의 정밀도에서 뛰어납니다. 하지만 광범위한 응용을 위한 일반화 능력이 부족합니다. 이러한 관찰에서 영감을 받아, 우리는 일반주의 정책과 전문가 정책의 장점을 모두 보완하는 시너지 이중 시스템인 RoboDual을 소개합니다. 확산 트랜스포머 기반의 전문가 정책은 다단계 행동 롤아웃을 위해 설계되었으며, 비전-언어-행동(VLA) 기반 일반주의 정책의 고수준 작업 이해와 이산화된 행동 출력에 정교하게 조건화됩니다. OpenVLA와 비교하여 RoboDual은 단 2천만 개의 훈련 가능한 파라미터를 가진 전문가 정책을 도입함으로써 실제 환경에서 26.7%의 성능 향상과 CALVIN에서 12%의 이득을 달성했습니다. 또한, 데모 데이터의 5%만으로도 강력한 성능을 유지하며, 실제 배포에서 3.8배 더 높은 제어 주파수를 가능하게 합니다. 코드는 공개될 예정입니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://opendrivelab.com/RoboDual/

## 参考
- http://arxiv.org/abs/2410.08001v3
