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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00139v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (809 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.00139v2

## 개요
DexGrasp-VLA는 범용 로봇의 정밀 조작에서 훈련 데이터 부족 문제를 해결하기 위해 공유 자율 프레임워크를 제안한다. 이 프레임워크는 제어 작업을 거시적 팔 운동과 미시적 손 운동으로 분해한다: 인간 조작자는 VR 원격 조작을 통해 로봇 팔의 자세를 유도하고, 자율 DexGrasp-VLA 정책은 실시간 촉각 및 시각 피드백을 활용하여 손의 정밀 제어를 처리한다. 이러한 분업은 조작자의 인지 부하를 크게 줄이고 고품질의 팔-손 협조 시연 데이터를 효율적으로 수집할 수 있게 한다. 이 데이터를 기반으로 팀은 엔드투엔드 VLA 정책을 훈련하고, 거시적 및 미시적 운동의 고유 표현과 공유 표현을 포착하여 더 자연스러운 협조를 구현하는 새로운 Arm-Hand Feature Enhancement 모듈을 도입했다. 또한, 오류 수정 원격 조작 시스템은 인간-인-더-루프 실패 복구를 통한 지속적인 정책 개선을 가능하게 한다.

## 핵심 내용
### 방법
- **공유 자율 프레임워크**: 제어를 거시적 운동(팔)과 미시적 운동(손)으로 분해한다. 인간 조작자는 VR 원격 조작을 통해 팔 자세를 제어하고, 자율 DexGrasp-VLA 정책은 실시간 촉각 및 시각 피드백을 활용하여 손의 정밀 제어를 처리한다.
- **Arm-Hand Feature Enhancement 모듈**: 이 모듈은 엔드투엔드 VLA 정책에 내장되어 거시적 및 미시적 운동의 고유 표현과 공유 표현을 동시에 포착하여 팔-손 협조의 자연스러움을 향상시킨다.
- **오류 수정 원격 조작 시스템**: 정책 실패 시 인간이 개입할 수 있게 하여 인간-인-더-루프 실패 복구 메커니즘을 통해 지속적인 정책 개선을 구현한다.

### 실험 설정
- **데이터 수집**: 공유 자율 프레임워크를 통해 최소한의 인력 비용으로 고품질 팔-손 협조 시연 데이터를 생성한다.
- **평가 대상**: 보지 못한 인스턴스를 포함한 다양한 물체를 포함한다.
- **성능 지표**: 성공률.

### 주요 수치 및 결론
- **성공률**: 보지 못한 인스턴스를 포함한 다양한 물체에서 90%의 성공률을 달성한다.
- **효율성**: 인간 조작자의 인지 부하를 크게 줄여 효율적인 데이터 수집을 구현한다.
- **일반화 능력**: 보지 못한 물체에 대해 우수한 일반화 성능을 보인다.
- **지속적 개선**: 오류 수정 원격 조작 시스템은 정책의 지속적 최적화를 지원한다.
