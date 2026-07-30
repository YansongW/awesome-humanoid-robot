---
$id: ent_paper_cui_end_to_end_dexterous_arm_hand_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection'
  zh: DexGrasp-VLA
  ko: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection'
summary:
  en: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection (DexGrasp-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.'
  zh: DexGrasp-VLA 是字节跳动 Seed 团队于 2025 年提出的大型视觉-语言-动作模型，旨在实现类人灵巧操作。其核心贡献在于提出一种共享自主框架，将宏观臂部运动与微观手部运动分离，通过人类 VR 遥操作控制臂部姿态，同时由自主
    DexGrasp-VLA 策略处理手部精细控制，从而高效收集高质量数据。实验表明，该方法在多种物体上达到 90% 的成功率，并支持通过纠错遥操作实现持续策略改进。
  ko: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection (DexGrasp-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexgrasp_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00139v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA
    Policy for Efficient Data Collection (arXiv)'
  url: https://arxiv.org/abs/2511.00139
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DexGrasp-VLA source
  url: https://doi.org/10.48550/arXiv.2511.00139
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DexGrasp-VLA 针对通用机器人灵巧操作中训练数据稀缺的问题，提出了一种共享自主框架。该框架将控制任务分解为宏观臂部运动和微观手部运动：人类操作员通过 VR 遥操作引导机器人臂部姿态，而自主 DexGrasp-VLA 策略则利用实时触觉和视觉反馈处理手部精细控制。这种分工显著降低了操作员的认知负荷，并实现了高质量臂-手协调演示数据的高效收集。基于这些数据，团队训练了一个端到端 VLA 策略，并引入了新颖的 Arm-Hand Feature Enhancement 模块，以捕捉宏观与微观运动的独特和共享表征，从而实现更自然的协调。此外，纠错遥操作系统允许通过人在回路中的失败恢复进行持续策略改进。

## 核心内容
### 方法
- **共享自主框架**：将控制分为宏观运动（臂部）和微观运动（手部）。人类操作员通过 VR 遥操作控制臂部姿态，而自主 DexGrasp-VLA 策略利用实时触觉和视觉反馈处理手部精细控制。
- **Arm-Hand Feature Enhancement 模块**：该模块嵌入端到端 VLA 策略中，能够同时捕捉宏观和微观运动的独特表征与共享表征，从而提升臂-手协调的自然度。
- **纠错遥操作系统**：允许人类在策略失败时介入，通过人在回路中的失败恢复机制实现持续策略改进。

### 实验设置
- **数据收集**：通过共享自主框架，以最小人力成本生成高质量臂-手协调演示数据。
- **评估对象**：涵盖多种物体，包括未见过的实例。
- **性能指标**：成功率。

### 关键数字与结论
- **成功率**：在多种物体上达到 90% 的成功率，包括未见过的实例。
- **效率**：显著降低了人类操作员的认知负荷，实现了高效数据收集。
- **泛化能力**：对未见物体表现出良好的泛化性能。
- **持续改进**：纠错遥操作系统支持策略的持续优化。

## Overview
Achieving human-like dexterous manipulation remains a major challenge for general-purpose robots. While Vision-Language-Action (VLA) models show potential in learning skills from demonstrations, their scalability is limited by scarce high-quality training data. Existing data collection methods face inherent constraints: manual teleoperation overloads human operators, while automated planning often produces unnatural motions. We propose a Shared Autonomy framework that divides control between macro and micro motions. A human operator guides the robot's arm pose through intuitive VR teleoperation, while an autonomous DexGrasp-VLA policy handles fine-grained hand control using real-time tactile and visual feedback. This division significantly reduces cognitive load and enables efficient collection of high-quality coordinated arm-hand demonstrations. Using this data, we train an end-to-end VLA policy enhanced with our novel Arm-Hand Feature Enhancement module, which captures both distinct and shared representations of macro and micro movements for more natural coordination. Our Corrective Teleoperation system enables continuous policy improvement through human-in-the-loop failure recovery. Experiments demonstrate that our framework generates high-quality data with minimal manpower and achieves a 90% success rate across diverse objects, including unseen instances. Comprehensive evaluations validate the system's effectiveness in developing dexterous manipulation capabilities.

## 개요
인간과 같은 정교한 조작 능력을 달성하는 것은 범용 로봇에게 여전히 주요 과제로 남아 있습니다. Vision-Language-Action(VLA) 모델은 시연을 통해 기술을 학습할 가능성을 보여주지만, 고품질 훈련 데이터의 부족으로 확장성에 한계가 있습니다. 기존 데이터 수집 방법은 본질적인 제약에 직면합니다. 수동 원격 조작은 인간 작업자에게 과부하를 주고, 자동화된 계획은 종종 부자연스러운 움직임을 생성합니다. 우리는 거시적 움직임과 미시적 움직임 간의 제어를 분할하는 공유 자율성(Shared Autonomy) 프레임워크를 제안합니다. 인간 작업자는 직관적인 VR 원격 조작을 통해 로봇의 팔 자세를 안내하고, 자율적인 DexGrasp-VLA 정책은 실시간 촉각 및 시각 피드백을 사용하여 세밀한 손 제어를 처리합니다. 이러한 분할은 인지 부하를 크게 줄이고 고품질의 조정된 팔-손 시연을 효율적으로 수집할 수 있게 합니다. 이 데이터를 사용하여, 우리는 거시적 및 미시적 움직임의 고유하고 공유된 표현을 모두 포착하여 더 자연스러운 조정을 가능하게 하는 새로운 Arm-Hand Feature Enhancement 모듈로 강화된 종단간 VLA 정책을 훈련합니다. 우리의 Corrective Teleoperation 시스템은 인간이 개입하는 실패 복구를 통해 지속적인 정책 개선을 가능하게 합니다. 실험은 우리의 프레임워크가 최소한의 인력으로 고품질 데이터를 생성하고, 보지 못한 객체를 포함한 다양한 객체에서 90%의 성공률을 달성함을 보여줍니다. 포괄적인 평가는 시스템이 정교한 조작 능력을 개발하는 데 효과적임을 입증합니다.

## 핵심 내용
인간과 같은 정교한 조작 능력을 달성하는 것은 범용 로봇에게 여전히 주요 과제로 남아 있습니다. Vision-Language-Action(VLA) 모델은 시연을 통해 기술을 학습할 가능성을 보여주지만, 고품질 훈련 데이터의 부족으로 확장성에 한계가 있습니다. 기존 데이터 수집 방법은 본질적인 제약에 직면합니다. 수동 원격 조작은 인간 작업자에게 과부하를 주고, 자동화된 계획은 종종 부자연스러운 움직임을 생성합니다. 우리는 거시적 움직임과 미시적 움직임 간의 제어를 분할하는 공유 자율성(Shared Autonomy) 프레임워크를 제안합니다. 인간 작업자는 직관적인 VR 원격 조작을 통해 로봇의 팔 자세를 안내하고, 자율적인 DexGrasp-VLA 정책은 실시간 촉각 및 시각 피드백을 사용하여 세밀한 손 제어를 처리합니다. 이러한 분할은 인지 부하를 크게 줄이고 고품질의 조정된 팔-손 시연을 효율적으로 수집할 수 있게 합니다. 이 데이터를 사용하여, 우리는 거시적 및 미시적 움직임의 고유하고 공유된 표현을 모두 포착하여 더 자연스러운 조정을 가능하게 하는 새로운 Arm-Hand Feature Enhancement 모듈로 강화된 종단간 VLA 정책을 훈련합니다. 우리의 Corrective Teleoperation 시스템은 인간이 개입하는 실패 복구를 통해 지속적인 정책 개선을 가능하게 합니다. 실험은 우리의 프레임워크가 최소한의 인력으로 고품질 데이터를 생성하고, 보지 못한 객체를 포함한 다양한 객체에서 90%의 성공률을 달성함을 보여줍니다. 포괄적인 평가는 시스템이 정교한 조작 능력을 개발하는 데 효과적임을 입증합니다.

## 参考
- http://arxiv.org/abs/2511.00139v2
