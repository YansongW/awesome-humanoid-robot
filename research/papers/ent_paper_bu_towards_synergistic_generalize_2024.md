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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08001v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (844 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2410.08001v3

## 개요
RoboDual은 일반 정책의 낮은 추론 효율성과 높은 훈련 비용, 그리고 전용 정책의 부족한 일반화 능력 문제를 해결하기 위해 협력적 이중 시스템 아키텍처를 제안한다. 이 시스템은 고수준 작업 이해와 이산 동작 출력을 담당하는 비전-언어-동작(VLA) 기반의 일반 정책과, 다단계 동작 전개를 수행하고 일반 정책의 출력을 정밀하게 조건으로 삼는 확산 트랜스포머 기반의 전용 정책을 포함한다. 실험 결과, RoboDual은 OpenVLA에 비해 실제 환경에서 26.7% 성능 향상, CALVIN 벤치마크에서 12% 향상을 보였으며, 단 5%의 데모 데이터만으로도 강력한 성능을 유지하면서 실제 배포 시 제어 주파수를 3.8배 향상시켰다.

## 핵심 내용
### 방법
RoboDual의 핵심은 일반 정책과 전용 정책의 장점을 결합하는 협력적 이중 시스템이다:
- **일반 정책**: 비전-언어-동작(VLA) 모델 기반으로, 고수준 작업 이해를 담당하고 이산화된 동작 명령을 출력한다.
- **전용 정책**: 확산 트랜스포머(Diffusion Transformer) 기반으로, 일반 정책이 출력한 고수준 작업 이해와 이산 동작을 조건으로 삼아 다단계 동작 전개를 수행하여 정밀한 저수준 제어를 구현한다.

### 아키텍처
- 일반 정책은 작업 수준 추론과 동작 계획을 제공하고, 전용 정책은 효율적이고 정밀한 궤적 실행에 집중한다.
- 전용 정책은 2000만 개의 훈련 가능한 파라미터만 포함하여 경량 특성을 유지한다.

### 실험 설정
- 실제 세계 시나리오와 CALVIN 벤치마크에서 평가를 수행했다.
- OpenVLA를 기준 모델로 비교했다.

### 주요 수치
- 실제 세계 설정에서 OpenVLA 대비 RoboDual은 26.7% 성능 향상을 달성했다.
- CALVIN 벤치마크에서 12% 성능 향상을 보였다.
- 단 5%의 데모 데이터만 사용하여 강력한 성능을 유지했다.
- 실제 배포에서 제어 주파수를 3.8배 향상시켰다.

### 결론
RoboDual은 협력적 이중 시스템 설계를 통해 일반 정책과 전용 정책 각각의 한계를 효과적으로 해결하며, 일반화 능력을 유지하면서 추론 효율성, 훈련 비용 효율성, 배포 성능을 크게 향상시켰다. 코드는 공개될 예정이며, 프로젝트 페이지는 https://opendrivelab.com/RoboDual/ 에서 확인할 수 있다.
