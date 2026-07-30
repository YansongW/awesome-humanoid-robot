---
$id: ent_paper_learning_soccer_skills_for_hum_2026_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
  zh: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
  ko: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
summary:
  en: 'Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 本文提出了一种名为PAiD的渐进式感知-动作框架，用于人形机器人足球技能学习。该工作由研究团队完成，核心贡献在于将复杂技能分解为运动技能获取、轻量级感知-动作集成和物理感知的sim-to-real迁移三个阶段，在Unitree G1机器人上实现了高保真、鲁棒性强的踢球动作。
  ko: 'Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_soccer_skills_for_hum
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.05310v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework (arXiv)'
  url: https://arxiv.org/abs/2602.05310
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
针对人形机器人足球任务中模块化流水线的不稳定性与端到端框架的训练目标冲突问题，本文提出了PAiD（Perception-Action integrated Decision-making）渐进式架构。该架构将足球技能学习分解为三个有序阶段：首先通过人体运动跟踪获取基础运动技能，然后进行轻量级感知-动作集成以实现位置泛化，最后通过物理感知的sim-to-real迁移缩小仿真与现实差距。这种分治策略有效避免了感知集成过程中的奖励冲突，并最小化了sim-to-real迁移的差距。在Unitree G1机器人上的实验表明，该方法能够生成高保真的人形踢球动作，并在静态球、滚动球、不同位置及外部干扰等多种条件下保持鲁棒性能，同时确保室内外场景的一致性执行。

## 核心内容
### 方法架构
PAiD框架采用渐进式分解策略，将人形机器人足球技能学习分为三个核心阶段：
- **运动技能获取阶段**：通过人体运动跟踪（human motion tracking）学习基础运动技能，建立稳定的动作基元。
- **轻量级感知-动作集成阶段**：在已有运动技能基础上，集成轻量级感知模块实现位置泛化（positional generalization），避免传统端到端框架中感知与运动目标的冲突。
- **物理感知sim-to-real迁移阶段**：引入物理感知机制，最小化仿真环境到真实世界的迁移差距（sim-to-real gap）。

### 实验设置与关键结果
- **硬件平台**：Unitree G1人形机器人
- **测试条件**：涵盖静态球、滚动球、不同踢球位置及外部干扰等多种场景
- **性能表现**：
  - 实现高保真（high-fidelity）的人形踢球动作
  - 在室内外场景中保持一致的执行效果（consistent execution）
  - 对动态环境（如滚动球）和外部干扰展现出鲁棒性能（robust performance）

### 结论
该分治策略（divide-and-conquer strategy）为人形机器人足球能力提供了鲁棒性解决方案，并为复杂具身技能学习（complex embodied skill acquisition）提供了一个可扩展的框架。项目页面：https://soccer-humanoid.github.io/

## Overview
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions-including static or rolling balls, various positions, and disturbances-while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## Overview
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions—including static or rolling balls, various positions, and disturbances—while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## Content
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions—including static or rolling balls, various positions, and disturbances—while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## 개요
축구는 인간형 로봇에게 중요한 도전 과제로, 인지 기반 킥 동작 및 전신 균형 제어와 같은 작업을 위해 긴밀하게 통합된 인지-행동 능력을 요구합니다. 기존 접근 방식은 모듈식 파이프라인에서 모듈 간 불안정성이나 종단 간 프레임워크에서 상충되는 훈련 목표로 인해 어려움을 겪습니다. 우리는 축구 기술 습득을 세 단계로 분해하는 점진적 아키텍처인 PAiD(Perception-Action integrated Decision-making)를 제안합니다: 인간 동작 추적을 통한 운동 기술 습득, 위치 일반화를 위한 경량 인지-행동 통합, 물리 인식 시뮬레이션-실제 전환. 이러한 단계적 분해는 안정적인 기초 기술을 확립하고, 인지 통합 중 보상 충돌을 방지하며, 시뮬레이션-실제 간 차이를 최소화합니다. Unitree G1 실험은 정지 또는 구르는 공, 다양한 위치, 외란을 포함한 다양한 조건에서 강건한 성능을 보이며, 실내 및 실외 시나리오에서 일관된 실행을 유지하는 고충실도 인간형 킥을 입증합니다. 우리의 분할 정복 전략은 강건한 인간형 축구 능력을 발전시키고, 복잡한 체화된 기술 습득을 위한 확장 가능한 프레임워크를 제공합니다. 프로젝트 페이지는 https://soccer-humanoid.github.io/에서 확인할 수 있습니다.

## 핵심 내용
축구는 인간형 로봇에게 중요한 도전 과제로, 인지 기반 킥 동작 및 전신 균형 제어와 같은 작업을 위해 긴밀하게 통합된 인지-행동 능력을 요구합니다. 기존 접근 방식은 모듈식 파이프라인에서 모듈 간 불안정성이나 종단 간 프레임워크에서 상충되는 훈련 목표로 인해 어려움을 겪습니다. 우리는 축구 기술 습득을 세 단계로 분해하는 점진적 아키텍처인 PAiD(Perception-Action integrated Decision-making)를 제안합니다: 인간 동작 추적을 통한 운동 기술 습득, 위치 일반화를 위한 경량 인지-행동 통합, 물리 인식 시뮬레이션-실제 전환. 이러한 단계적 분해는 안정적인 기초 기술을 확립하고, 인지 통합 중 보상 충돌을 방지하며, 시뮬레이션-실제 간 차이를 최소화합니다. Unitree G1 실험은 정지 또는 구르는 공, 다양한 위치, 외란을 포함한 다양한 조건에서 강건한 성능을 보이며, 실내 및 실외 시나리오에서 일관된 실행을 유지하는 고충실도 인간형 킥을 입증합니다. 우리의 분할 정복 전략은 강건한 인간형 축구 능력을 발전시키고, 복잡한 체화된 기술 습득을 위한 확장 가능한 프레임워크를 제공합니다. 프로젝트 페이지는 https://soccer-humanoid.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2602.05310v1
