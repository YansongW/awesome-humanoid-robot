---
$id: ent_paper_e_vla_event_augmented_vision_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes'
  zh: 'E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes'
  ko: 'E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes'
summary:
  en: 'arXiv:2604.04834v2 Announce Type: replace-cross Abstract: Robotic Vision-Language-Action (VLA) models generalize well
    for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light,
    motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness
    when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly
    leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency
    under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world
    synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight,
    pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that
    even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve
    robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with
    overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves
    from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception
    can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based
    imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.'
  zh: E-VLA 是由研究团队提出的事件增强型视觉-语言-动作框架，旨在解决传统帧基视觉在极端低光、运动模糊等退化场景下的操作鲁棒性问题。其核心贡献在于直接利用事件流中的运动与结构线索，无需重建图像即可保持语义感知与感知-动作一致性，并在真实数据集上验证了有效性。
  ko: 'arXiv:2604.04834v2 Announce Type: replace-cross Abstract: Robotic Vision-Language-Action (VLA) models generalize well
    for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light,
    motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness
    when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly
    leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency
    under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world
    synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight,
    pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that
    even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve
    robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with
    overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves
    from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception
    can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based
    imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- e_vla
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.04834v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes'
  url: https://arxiv.org/abs/2604.04834
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
E-VLA 框架通过集成事件相机（DAVIS346）的数据流，克服了传统 RGB 帧基视觉在黑暗和模糊场景下的脆弱性。研究团队构建了开源遥操作平台，收集了跨多种任务与光照条件的同步 RGB-事件-动作数据集。他们提出了轻量级、兼容预训练模型的事件集成策略，并研究了事件窗口化以实现稳定部署。实验表明，即使简单的参数无关融合（如将累积事件图叠加到 RGB 图像上）也能显著提升鲁棒性，在 20 lux 黑暗环境下的 Pick-Place 任务中成功率从 0% 提升至 60%，而使用事件适配器更达到 90%。

## 核心内容
### 方法概述
E-VLA 的核心思路是直接利用事件流中的运动与结构信息，而非将事件重建为传统图像。这避免了重建过程中的信息损失与计算开销，同时保持了与预训练 VLA 模型的兼容性。

### 架构设计
- **事件集成策略**：提出了两种轻量级方案：
  - **参数无关融合**：将累积事件图直接叠加到 RGB 图像上，作为额外通道输入。
  - **事件适配器**：一个可学习的轻量模块，用于更灵活地融合事件特征。
- **事件窗口化**：通过调整事件累积的时间窗口长度，平衡实时性与信息完整性，确保在动态场景中的稳定部署。

### 实验设置
- **硬件平台**：基于 DAVIS346 事件相机的开源遥操作平台，可同时输出 RGB 帧与事件流。
- **数据集**：收集了涵盖多种任务（如 Pick-Place、Sorting）与光照条件（从明亮到 20 lux 极暗）的同步 RGB-事件-动作数据。
- **对比基线**：以纯 RGB 图像输入的 VLA 模型作为基准，对比不同事件融合策略的效果。

### 关键实验结果
- **黑暗场景（20 lux）**：
  - Pick-Place 任务：纯图像基线成功率 0%，叠加融合提升至 60%，事件适配器达到 90%。
- **严重运动模糊（模拟 1000 ms 曝光）**：
  - Pick-Place 任务：从 0% 提升至 20-25%。
  - Sorting 任务：从 5% 提升至 32.5%。
- **结论**：即使最简单的参数无关融合也能带来显著提升，而事件适配器在极端条件下表现更优。

### 结论与展望
E-VLA 系统性地证明了事件驱动感知可有效集成到 VLA 模型中，为超越传统帧基成像的鲁棒具身智能提供了可行路径。代码与数据集将在 GitHub 上开源。

## Overview
Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.

## 개요
Robotic Vision-Language-Action (VLA) 모델은 개방형 조작 작업에서 일반화 성능이 뛰어나지만, 극도로 낮은 조도, 모션 블러, 블랙 클리핑과 같은 센싱 단계의 열화에 취약합니다. 본 논문에서는 기존 프레임 기반 비전이 신뢰할 수 없을 때 조작의 강건성을 향상시키는 이벤트 증강 VLA 프레임워크인 E-VLA를 제안합니다. E-VLA는 이벤트로부터 이미지를 재구성하는 대신, 이벤트 스트림의 움직임 및 구조적 단서를 직접 활용하여 열악한 조건에서도 의미론적 인식과 인식-행동 일관성을 유지합니다. DAVIS346 이벤트 카메라를 갖춘 오픈소스 원격 조작 플랫폼을 구축하고, 다양한 작업과 조명 조건에서 실제 세계의 동기화된 RGB-이벤트-행동 조작 데이터셋을 수집했습니다. 또한, 경량화된 사전 학습 호환 이벤트 통합 전략을 제안하고 안정적인 배포를 위한 이벤트 윈도잉을 연구했습니다. 실험 결과, 누적 이벤트 맵을 RGB 이미지에 오버레이하는 간단한 파라미터 없는 융합조차도 어둡고 심한 블러가 있는 장면에서 강건성을 크게 향상시킬 수 있음을 보여줍니다: 20 lux에서 Pick-Place 작업의 경우, 이미지만 사용했을 때 0%에서 오버레이 융합 시 60%, 당사의 이벤트 어댑터 사용 시 90%로 성공률이 증가했습니다. 심한 모션 블러(1000ms 노출 프록시) 조건에서는 Pick-Place가 0%에서 20-25%로, Sorting이 5%에서 32.5%로 향상되었습니다. 전반적으로 E-VLA는 이벤트 기반 인식이 VLA 모델에 효과적으로 통합될 수 있다는 체계적인 증거를 제공하며, 기존 프레임 기반 이미징을 넘어서는 강건한 구현 지능을 지향합니다. 코드와 데이터셋은 https://github.com/JJayzee/E-VLA에서 제공될 예정입니다.

## 핵심 내용
Robotic Vision-Language-Action (VLA) 모델은 개방형 조작 작업에서 일반화 성능이 뛰어나지만, 극도로 낮은 조도, 모션 블러, 블랙 클리핑과 같은 센싱 단계의 열화에 취약합니다. 본 논문에서는 기존 프레임 기반 비전이 신뢰할 수 없을 때 조작의 강건성을 향상시키는 이벤트 증강 VLA 프레임워크인 E-VLA를 제안합니다. E-VLA는 이벤트로부터 이미지를 재구성하는 대신, 이벤트 스트림의 움직임 및 구조적 단서를 직접 활용하여 열악한 조건에서도 의미론적 인식과 인식-행동 일관성을 유지합니다. DAVIS346 이벤트 카메라를 갖춘 오픈소스 원격 조작 플랫폼을 구축하고, 다양한 작업과 조명 조건에서 실제 세계의 동기화된 RGB-이벤트-행동 조작 데이터셋을 수집했습니다. 또한, 경량화된 사전 학습 호환 이벤트 통합 전략을 제안하고 안정적인 배포를 위한 이벤트 윈도잉을 연구했습니다. 실험 결과, 누적 이벤트 맵을 RGB 이미지에 오버레이하는 간단한 파라미터 없는 융합조차도 어둡고 심한 블러가 있는 장면에서 강건성을 크게 향상시킬 수 있음을 보여줍니다: 20 lux에서 Pick-Place 작업의 경우, 이미지만 사용했을 때 0%에서 오버레이 융합 시 60%, 당사의 이벤트 어댑터 사용 시 90%로 성공률이 증가했습니다. 심한 모션 블러(1000ms 노출 프록시) 조건에서는 Pick-Place가 0%에서 20-25%로, Sorting이 5%에서 32.5%로 향상되었습니다. 전반적으로 E-VLA는 이벤트 기반 인식이 VLA 모델에 효과적으로 통합될 수 있다는 체계적인 증거를 제공하며, 기존 프레임 기반 이미징을 넘어서는 강건한 구현 지능을 지향합니다. 코드와 데이터셋은 https://github.com/JJayzee/E-VLA에서 제공될 예정입니다.

## 参考
- http://arxiv.org/abs/2604.04834v2
