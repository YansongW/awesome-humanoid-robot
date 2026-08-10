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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.05310v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP1 dedup merge 2026-08-06: merged
    ent_paper_learning_soccer_skills_for_hum_2026_1 into this card (rules: suffix_reingest). Backup+manifest: .staging/cleanup_wp12/.
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (996 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework (arXiv)'
  url: https://arxiv.org/abs/2602.05310
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 学习人形机器人的足球技能：渐进式感知-行动框架 project page
  url: https://soccer-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-06-26'
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

## 参考
- http://arxiv.org/abs/2602.05310v1

## 개요
인간형 로봇 축구 작업에서 모듈식 파이프라인의 불안정성과 엔드투엔드 프레임워크의 훈련 목표 충돌 문제를 해결하기 위해, 본 논문은 PAiD(Perception-Action integrated Decision-making) 점진적 아키텍처를 제안한다. 이 아키텍처는 축구 기술 학습을 세 가지 순차적 단계로 분해한다: 먼저 인간 동작 추적을 통해 기초 운동 기술을 획득하고, 그다음 경량 인식-행동 통합을 통해 위치 일반화를 달성하며, 마지막으로 물리 인식 sim-to-real 전이를 통해 시뮬레이션과 현실 간의 격차를 줄인다. 이러한 분할 정복 전략은 인식 통합 과정에서의 보상 충돌을 효과적으로 방지하고 sim-to-real 전이 격차를 최소화한다. Unitree G1 로봇에서의 실험은 이 방법이 고충실도 인간형 발차기 동작을 생성할 수 있으며, 정적 공, 구르는 공, 다양한 위치 및 외부 간섭 등 여러 조건에서 견고한 성능을 유지하고, 실내외 시나리오에서 일관된 실행을 보장함을 보여준다.

## 핵심 내용
### 방법 아키텍처
PAiD 프레임워크는 점진적 분해 전략을 채택하여 인간형 로봇 축구 기술 학습을 세 가지 핵심 단계로 나눈다:
- **운동 기술 획득 단계**: 인간 동작 추적(human motion tracking)을 통해 기초 운동 기술을 학습하고 안정적인 동작 프리미티브를 구축한다.
- **경량 인식-행동 통합 단계**: 기존 운동 기술을 기반으로 경량 인식 모듈을 통합하여 위치 일반화(positional generalization)를 달성하고, 기존 엔드투엔드 프레임워크에서의 인식과 운동 목표 간 충돌을 피한다.
- **물리 인식 sim-to-real 전이 단계**: 물리 인식 메커니즘을 도입하여 시뮬레이션 환경에서 실제 세계로의 전이 격차(sim-to-real gap)를 최소화한다.

### 실험 설정 및 주요 결과
- **하드웨어 플랫폼**: Unitree G1 인간형 로봇
- **테스트 조건**: 정적 공, 구르는 공, 다양한 발차기 위치 및 외부 간섭 등 여러 시나리오 포함
- **성능 표현**:
  - 고충실도(high-fidelity) 인간형 발차기 동작 구현
  - 실내외 시나리오에서 일관된 실행 효과(consistent execution) 유지
  - 동적 환경(예: 구르는 공) 및 외부 간섭에 대한 견고한 성능(robust performance) 입증

### 결론
이 분할 정복 전략(divide-and-conquer strategy)은 인간형 로봇 축구 능력에 대한 견고성 솔루션을 제공하며, 복잡한 구현형 기술 습득(complex embodied skill acquisition)을 위한 확장 가능한 프레임워크를 제시한다. 프로젝트 페이지: https://soccer-humanoid.github.io/
