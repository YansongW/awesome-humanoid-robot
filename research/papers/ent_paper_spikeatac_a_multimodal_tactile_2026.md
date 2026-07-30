---
$id: ent_paper_spikeatac_a_multimodal_tactile_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SpikeATac: A Multimodal Tactile Finger with Taxelized Dynamic Sensing for Dexterous Manipulation'
  zh: 'SpikeATac: A Multimodal Tactile Finger with Taxelized Dynamic Sensing for Dexterous Manipulation'
  ko: 'SpikeATac: A Multimodal Tactile Finger with Taxelized Dynamic Sensing for Dexterous Manipulation'
summary:
  en: 'arXiv:2510.27048v3 Announce Type: replace Abstract: In this work, we introduce SpikeATac, a multimodal tactile finger
    combining a taxelized and highly sensitive dynamic response (PVDF) with a static transduction method (capacitive) for
    multimodal touch sensing. Named for its `spiky'' response, SpikeATac''s 16-taxel PVDF film sampled at 4 kHz provides fast,
    sensitive dynamic signals to the very onset and breaking of contact. We characterize the sensitivity of the different
    modalities, and show that SpikeATac provides the ability to stop quickly and delicately when grasping fragile, deformable
    objects. Beyond parallel grasping, we show that SpikeATac can be used in a learning-based framework to achieve new capabilities
    on a dexterous multifingered robot hand. We use reinforcement learning from human feedback to fine-tune the behavior of
    a policy to modulate force. Our hardware platform and learning pipeline together enable a difficult dexterous and contact-rich
    task that has not previously been achieved: in-hand manipulation of fragile objects. Videos are available at https://roamlab.github.io/spikeatac/
    .'
  zh: SpikeATac 是一种多模态触觉手指，由 RoamLab 团队提出，结合了基于 PVDF 的动态传感（16 个 taxel，4 kHz 采样率）与电容式静态传感。其核心贡献在于实现了对易碎、可变形物体的快速轻柔抓取，并首次通过人类反馈强化学习（RLHF）在灵巧多指机器人手上完成易碎物体的手内操作。
  ko: 'arXiv:2510.27048v3 Announce Type: replace Abstract: In this work, we introduce SpikeATac, a multimodal tactile finger
    combining a taxelized and highly sensitive dynamic response (PVDF) with a static transduction method (capacitive) for
    multimodal touch sensing. Named for its `spiky'' response, SpikeATac''s 16-taxel PVDF film sampled at 4 kHz provides fast,
    sensitive dynamic signals to the very onset and breaking of contact. We characterize the sensitivity of the different
    modalities, and show that SpikeATac provides the ability to stop quickly and delicately when grasping fragile, deformable
    objects. Beyond parallel grasping, we show that SpikeATac can be used in a learning-based framework to achieve new capabilities
    on a dexterous multifingered robot hand. We use reinforcement learning from human feedback to fine-tune the behavior of
    a policy to modulate force. Our hardware platform and learning pipeline together enable a difficult dexterous and contact-rich
    task that has not previously been achieved: in-hand manipulation of fragile objects. Videos are available at https://roamlab.github.io/spikeatac/
    .'
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
- robotics
- spikeatac
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.27048v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SpikeATac: A Multimodal Tactile Finger with Taxelized Dynamic Sensing for Dexterous Manipulation (arXiv)'
  url: https://arxiv.org/abs/2510.27048
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
SpikeATac 多模态触觉手指集成了高灵敏度的动态 PVDF 传感与电容式静态传感，其 16 个 taxel 以 4 kHz 频率采样，能快速捕捉接触开始与结束的“尖峰”动态信号。研究团队表征了不同模态的灵敏度，证明该手指在抓取易碎、可变形物体时能实现快速轻柔的停止。此外，SpikeATac 被集成到基于学习的框架中，通过人类反馈强化学习微调策略以调节力控，从而在灵巧多指机器人手上实现了此前未达成的接触密集型任务——易碎物体的手内操作。

## 核心内容
### 方法
- **硬件设计**：SpikeATac 手指结合了两种传感模态——动态 PVDF 薄膜（16 个 taxel，4 kHz 采样率）提供对接触起止的快速灵敏响应，电容式传感器则提供静态触觉信息。
- **学习框架**：采用人类反馈强化学习（RLHF）来微调策略行为，使机器人能够根据触觉反馈动态调节抓取力。

### 实验设置
- **灵敏度表征**：对动态与静态模态的灵敏度进行了定量分析，验证了 PVDF 在检测微小接触变化上的优势。
- **任务验证**：在平行抓取任务中，SpikeATac 能快速轻柔地停止抓取动作，避免损坏易碎物体；在灵巧多指手上，通过 RLHF 训练的策略成功实现了易碎物体的手内操作，这是此前未达成的接触密集型任务。

### 关键数字与结论
- **采样率**：PVDF 动态传感以 4 kHz 采样，确保对接触事件的快速响应。
- **taxel 数量**：16 个 taxel 提供空间分辨的动态触觉信息。
- **核心成果**：首次在灵巧多指机器人手上实现易碎物体的手内操作，展示了 SpikeATac 硬件与 RLHF 学习管线的协同能力。

### 结论
SpikeATac 通过多模态触觉融合与学习驱动策略，显著提升了机器人在接触密集型任务中的精细操作能力，尤其适用于易碎物体的抓取与操作。相关视频和更多细节可访问项目网站。

## Overview
In this work, we introduce SpikeATac, a multimodal tactile finger combining a taxelized and highly sensitive dynamic response (PVDF) with a static transduction method (capacitive) for multimodal touch sensing. Named for its `spiky' response, SpikeATac's 16-taxel PVDF film sampled at 4 kHz provides fast, sensitive dynamic signals to the very onset and breaking of contact. We characterize the sensitivity of the different modalities, and show that SpikeATac provides the ability to stop quickly and delicately when grasping fragile, deformable objects. Beyond parallel grasping, we show that SpikeATac can be used in a learning-based framework to achieve new capabilities on a dexterous multifingered robot hand. We use reinforcement learning from human feedback to fine-tune the behavior of a policy to modulate force. Our hardware platform and learning pipeline together enable a difficult dexterous and contact-rich task that has not previously been achieved: in-hand manipulation of fragile objects. Videos are available at https://roamlab.github.io/spikeatac/ .

## 개요
본 연구에서는 정적 변환 방식(정전용량)과 결합된 택셀화된 고감도 동적 응답(PVDF)을 갖춘 다중 모드 촉각 손가락인 SpikeATac을 소개합니다. 다중 모드 촉각 감지를 위해 설계된 SpikeATac은 '뾰족한' 응답에서 이름을 따왔으며, 4kHz로 샘플링된 16-택셀 PVDF 필름은 접촉 시작과 해제 시점에 빠르고 민감한 동적 신호를 제공합니다. 우리는 다양한 모드의 감도를 특성화하고, SpikeATac이 깨지기 쉽고 변형 가능한 물체를 잡을 때 빠르고 섬세하게 멈출 수 있는 능력을 제공함을 보여줍니다. 평행 잡기 외에도, SpikeATac이 학습 기반 프레임워크에서 사용되어 다중 손가락 로봇 손에서 새로운 능력을 달성할 수 있음을 입증합니다. 우리는 인간 피드백을 통한 강화 학습을 사용하여 힘을 조절하는 정책의 행동을 미세 조정합니다. 하드웨어 플랫폼과 학습 파이프라인을 통해 이전에 달성되지 못했던 어려운 정밀 접촉 작업인 깨지기 쉬운 물체의 손 안 조작이 가능해졌습니다. 비디오는 https://roamlab.github.io/spikeatac/ 에서 확인할 수 있습니다.

## 핵심 내용
본 연구에서는 정적 변환 방식(정전용량)과 결합된 택셀화된 고감도 동적 응답(PVDF)을 갖춘 다중 모드 촉각 손가락인 SpikeATac을 소개합니다. 다중 모드 촉각 감지를 위해 설계된 SpikeATac은 '뾰족한' 응답에서 이름을 따왔으며, 4kHz로 샘플링된 16-택셀 PVDF 필름은 접촉 시작과 해제 시점에 빠르고 민감한 동적 신호를 제공합니다. 우리는 다양한 모드의 감도를 특성화하고, SpikeATac이 깨지기 쉽고 변형 가능한 물체를 잡을 때 빠르고 섬세하게 멈출 수 있는 능력을 제공함을 보여줍니다. 평행 잡기 외에도, SpikeATac이 학습 기반 프레임워크에서 사용되어 다중 손가락 로봇 손에서 새로운 능력을 달성할 수 있음을 입증합니다. 우리는 인간 피드백을 통한 강화 학습을 사용하여 힘을 조절하는 정책의 행동을 미세 조정합니다. 하드웨어 플랫폼과 학습 파이프라인을 통해 이전에 달성되지 못했던 어려운 정밀 접촉 작업인 깨지기 쉬운 물체의 손 안 조작이 가능해졌습니다. 비디오는 https://roamlab.github.io/spikeatac/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2510.27048v3
