---
$id: ent_paper_orca_open_source_reliable_cost_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning'
  zh: 'ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning'
  ko: 'ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning'
summary:
  en: 'ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning
    is a 2025 work on hardware design for humanoid robots.'
  zh: ORCA 是一款由 ETH Zurich 团队设计的开源、低成本、高可靠性的仿人机器人手部硬件，具备 17 个自由度、肌腱驱动和集成触觉传感器。其核心贡献在于将组装时间缩短至 8 小时以内，材料成本控制在 2,000 CHF 以下，并能在超过
    10,000 次连续操作循环中无故障运行。该手部支持遥操作、模仿学习和零样本 sim-to-real 强化学习等多种任务。
  ko: 'ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning
    is a 2025 work on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- orca
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.04259v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning
    (arXiv)'
  url: https://arxiv.org/abs/2504.04259
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning
    project page'
  url: https://www.orcahand.com/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ORCA 手部旨在解决灵巧操作研究中硬件成本高、维护复杂和可及性差的问题。它采用 17 个自由度的肌腱驱动设计，并集成了触觉传感器，通过弹出式关节、自动校准和张力系统等创新设计，在降低复杂性的同时提升了可靠性和精度。该手部可在 8 小时内完成组装，材料成本低于 2,000 CHF，并经过超过 10,000 次连续操作循环的耐久性测试。ORCA 在遥操作、模仿学习和零样本 sim-to-real 强化学习等任务中均表现出色，为研究社区提供了一个可靠且经济高效的灵巧操作平台。

## 核心内容
### 设计目标与挑战
通用机器人需要具备类似人类的灵巧性和敏捷性，而仿人形态有助于利用大量人类手部交互数据集。然而，灵巧操作的主要瓶颈不仅在于软件，更在于硬件。接近人类能力的机器人手部往往成本高昂、体积庞大或需要企业级维护，限制了其在研究和实际应用中的普及。

### ORCA 手部核心设计
- **自由度与驱动**：ORCA 手部拥有 17 个自由度，采用肌腱驱动方式，模拟人类手部的运动机制。
- **创新机械设计**：
  - **弹出式关节**：简化了组装和维护过程。
  - **自动校准系统**：减少了手动校准的复杂性和时间。
  - **张力系统**：提高了肌腱驱动的可靠性和精度。
- **集成触觉传感器**：使手部能够感知接触力和物体形状，增强操作能力。
- **成本与组装**：材料成本低于 2,000 CHF，完全组装时间少于 8 小时，显著降低了研究门槛。

### 实验与性能评估
- **耐久性测试**：ORCA 手部在超过 10,000 次连续操作循环（约 20 小时）中未出现硬件故障，唯一限制是实验本身的持续时间。
- **任务基准测试**：
  - **遥操作**：通过远程控制完成精细操作任务。
  - **模仿学习**：从人类演示中学习操作技能。
  - **零样本 sim-to-real 强化学习**：在仿真中训练的策略直接迁移到真实手部，无需额外微调。
- **视频与资源**：演示视频可在 https://youtu.be/kUbPSYMmOds 观看，设计文件、源代码和文档可在 https://srl.ethz.ch/orcahand 获取。

## Overview
General-purpose robots should possess human-like dexterity and agility to perform tasks with the same versatility as us. A human-like form factor further enables the use of vast datasets of human-hand interactions. However, the primary bottleneck in dexterous manipulation lies not only in software but arguably even more in hardware. Robotic hands that approach human capabilities are often prohibitively expensive, bulky, or require enterprise-level maintenance, limiting their accessibility for broader research and practical applications. What if the research community could get started with reliable dexterous hands within a day? We present the open-source ORCA hand, a reliable and anthropomorphic 17-DoF tendon-driven robotic hand with integrated tactile sensors, fully assembled in less than eight hours and built for a material cost below 2,000 CHF. We showcase ORCA's key design features such as popping joints, auto-calibration, and tensioning systems that significantly reduce complexity while increasing reliability, accuracy, and robustness. We benchmark the ORCA hand across a variety of tasks, ranging from teleoperation and imitation learning to zero-shot sim-to-real reinforcement learning. Furthermore, we demonstrate its durability, withstanding more than 10,000 continuous operation cycles - equivalent to approximately 20 hours - without hardware failure, the only constraint being the duration of the experiment itself. Video is here: https://youtu.be/kUbPSYMmOds. Design files, source code, and documentation are available at https://srl.ethz.ch/orcahand.

## 개요
범용 로봇은 인간과 같은 손재주와 민첩성을 갖추어 우리와 동일한 다재다능함으로 작업을 수행해야 합니다. 인간과 유사한 형태는 인간 손 상호작용에 대한 방대한 데이터셋의 활용을 더욱 가능하게 합니다. 그러나 정교한 조작의 주요 병목은 소프트웨어뿐만 아니라 하드웨어에도 더 크게 존재합니다. 인간의 능력에 근접한 로봇 손은 종종 엄청나게 비싸거나, 부피가 크거나, 기업 수준의 유지보수가 필요하여 광범위한 연구와 실제 응용에 대한 접근성을 제한합니다. 연구 커뮤니티가 하루 안에 신뢰할 수 있는 정교한 손을 사용할 수 있다면 어떨까요? 우리는 오픈소스 ORCA 손을 소개합니다. 이는 신뢰할 수 있고 인간형 17자유도 텐던 구동 로봇 손으로, 촉각 센서가 통합되어 있으며 8시간 이내에 완전 조립이 가능하고 재료비가 2,000 CHF 미만입니다. 우리는 ORCA의 주요 설계 특징인 팝핑 조인트, 자동 캘리브레이션, 텐셔닝 시스템을 선보이며, 이는 복잡성을 크게 줄이면서 신뢰성, 정확성, 견고성을 향상시킵니다. 우리는 원격 조작 및 모방 학습에서 제로샷 시뮬레이션-실제 강화 학습에 이르기까지 다양한 작업에서 ORCA 손을 벤치마킹합니다. 또한, 하드웨어 고장 없이 10,000회 이상의 연속 작동 사이클(약 20시간에 해당)을 견디는 내구성을 입증했으며, 유일한 제약은 실험 자체의 지속 시간이었습니다. 비디오는 여기에서 확인할 수 있습니다: https://youtu.be/kUbPSYMmOds. 설계 파일, 소스 코드 및 문서는 https://srl.ethz.ch/orcahand에서 제공됩니다.

## 핵심 내용
범용 로봇은 인간과 같은 손재주와 민첩성을 갖추어 우리와 동일한 다재다능함으로 작업을 수행해야 합니다. 인간과 유사한 형태는 인간 손 상호작용에 대한 방대한 데이터셋의 활용을 더욱 가능하게 합니다. 그러나 정교한 조작의 주요 병목은 소프트웨어뿐만 아니라 하드웨어에도 더 크게 존재합니다. 인간의 능력에 근접한 로봇 손은 종종 엄청나게 비싸거나, 부피가 크거나, 기업 수준의 유지보수가 필요하여 광범위한 연구와 실제 응용에 대한 접근성을 제한합니다. 연구 커뮤니티가 하루 안에 신뢰할 수 있는 정교한 손을 사용할 수 있다면 어떨까요? 우리는 오픈소스 ORCA 손을 소개합니다. 이는 신뢰할 수 있고 인간형 17자유도 텐던 구동 로봇 손으로, 촉각 센서가 통합되어 있으며 8시간 이내에 완전 조립이 가능하고 재료비가 2,000 CHF 미만입니다. 우리는 ORCA의 주요 설계 특징인 팝핑 조인트, 자동 캘리브레이션, 텐셔닝 시스템을 선보이며, 이는 복잡성을 크게 줄이면서 신뢰성, 정확성, 견고성을 향상시킵니다. 우리는 원격 조작 및 모방 학습에서 제로샷 시뮬레이션-실제 강화 학습에 이르기까지 다양한 작업에서 ORCA 손을 벤치마킹합니다. 또한, 하드웨어 고장 없이 10,000회 이상의 연속 작동 사이클(약 20시간에 해당)을 견디는 내구성을 입증했으며, 유일한 제약은 실험 자체의 지속 시간이었습니다. 비디오는 여기에서 확인할 수 있습니다: https://youtu.be/kUbPSYMmOds. 설계 파일, 소스 코드 및 문서는 https://srl.ethz.ch/orcahand에서 제공됩니다.

## 参考
- http://arxiv.org/abs/2504.04259v2
