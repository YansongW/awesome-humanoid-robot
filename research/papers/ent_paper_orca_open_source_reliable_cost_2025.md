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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.04259v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (953 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2504.04259v2

## 개요
ORCA 핸드는 정밀 조작 연구에서 하드웨어 비용이 높고 유지보수가 복잡하며 접근성이 낮은 문제를 해결하기 위해 설계되었습니다. 17자유도의 텐돈 구동 방식을 채택하고 촉각 센서를 통합했으며, 팝업 조인트, 자동 캘리브레이션, 장력 시스템 등의 혁신적인 설계를 통해 복잡성을 낮추면서 신뢰성과 정밀도를 향상시켰습니다. 이 핸드는 8시간 이내에 조립이 가능하고 재료비가 2,000 CHF 미만이며, 10,000회 이상의 연속 조작 사이클 내구성 테스트를 통과했습니다. ORCA는 원격 조작, 모방 학습, 제로샷 sim-to-real 강화 학습 등의 작업에서 뛰어난 성능을 보여주며, 연구 커뮤니티에 신뢰할 수 있고 비용 효율적인 정밀 조작 플랫폼을 제공합니다.

## 핵심 내용
### 설계 목표와 과제
범용 로봇은 인간과 유사한 손재주와 민첩성을 필요로 하며, 인간형 형태는 방대한 인간 손 상호작용 데이터셋을 활용하는 데 도움이 됩니다. 그러나 정밀 조작의 주요 병목은 소프트웨어뿐만 아니라 하드웨어에 있습니다. 인간의 능력에 근접한 로봇 핸드는 종종 비용이 높거나 부피가 크거나 기업 수준의 유지보수가 필요하여 연구 및 실제 응용에서의 보급을 제한합니다.

### ORCA 핸드 핵심 설계
- **자유도 및 구동**: ORCA 핸드는 17자유도를 가지며 텐돈 구동 방식을 채택하여 인간 손의 운동 메커니즘을 모사합니다.
- **혁신적인 기계 설계**:
  - **팝업 조인트**: 조립 및 유지보수 과정을 단순화합니다.
  - **자동 캘리브레이션 시스템**: 수동 캘리브레이션의 복잡성과 시간을 줄입니다.
  - **장력 시스템**: 텐돈 구동의 신뢰성과 정밀도를 향상시킵니다.
- **통합 촉각 센서**: 핸드가 접촉력과 물체 형상을 인식할 수 있게 하여 조작 능력을 강화합니다.
- **비용 및 조립**: 재료비가 2,000 CHF 미만이고 완전 조립 시간이 8시간 미만으로 연구 진입 장벽을 크게 낮춥니다.

### 실험 및 성능 평가
- **내구성 테스트**: ORCA 핸드는 10,000회 이상의 연속 조작 사이클(약 20시간) 동안 하드웨어 고장이 발생하지 않았으며, 유일한 제한은 실험 자체의 지속 시간이었습니다.
- **작업 벤치마크 테스트**:
  - **원격 조작**: 원격 제어를 통해 정밀 조작 작업을 수행합니다.
  - **모방 학습**: 인간 시연에서 조작 기술을 학습합니다.
  - **제로샷 sim-to-real 강화 학습**: 시뮬레이션에서 훈련된 정책을 추가 미세 조정 없이 실제 핸드에 직접 전이합니다.
- **비디오 및 리소스**: 데모 비디오는 https://youtu.be/kUbPSYMmOds 에서 시청할 수 있으며, 설계 파일, 소스 코드 및 문서는 https://srl.ethz.ch/orcahand 에서 확인할 수 있습니다.
