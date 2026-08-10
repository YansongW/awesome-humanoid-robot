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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.04834v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1047 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2604.04834v2

## 개요
E-VLA 프레임워크는 이벤트 카메라(DAVIS346)의 데이터 스트림을 통합하여 기존 RGB 프레임 기반 비전이 어두운 환경과 흐릿한 장면에서 가지는 취약성을 극복합니다. 연구팀은 오픈소스 원격 조작 플랫폼을 구축하고, 다양한 작업과 조명 조건에 걸친 동기화된 RGB-이벤트-행동 데이터셋을 수집했습니다. 그들은 사전 훈련된 모델과 호환되는 경량 이벤트 통합 전략을 제안하고, 안정적인 배포를 위한 이벤트 윈도우화를 연구했습니다. 실험 결과, 단순한 파라미터 비의존적 융합(예: 누적 이벤트 맵을 RGB 이미지에 오버레이)만으로도 강건성이 크게 향상되어, 20 lux 어두운 환경의 Pick-Place 작업에서 성공률이 0%에서 60%로 상승했으며, 이벤트 어댑터를 사용하면 90%에 도달했습니다.

## 핵심 내용
### 방법 개요
E-VLA의 핵심 아이디어는 이벤트를 전통적인 이미지로 재구성하는 대신, 이벤트 스트림의 움직임 및 구조 정보를 직접 활용하는 것입니다. 이는 재구성 과정에서의 정보 손실과 계산 오버헤드를 피하면서, 사전 훈련된 VLA 모델과의 호환성을 유지합니다.

### 아키텍처 설계
- **이벤트 통합 전략**: 두 가지 경량 방식을 제안합니다:
  - **파라미터 비의존적 융합**: 누적 이벤트 맵을 RGB 이미지에 직접 오버레이하여 추가 채널로 입력합니다.
  - **이벤트 어댑터**: 이벤트 특징을 더 유연하게 융합하기 위한 학습 가능한 경량 모듈입니다.
- **이벤트 윈도우화**: 이벤트 누적 시간 창 길이를 조정하여 실시간성과 정보 완전성 간의 균형을 맞추고, 동적 장면에서의 안정적인 배포를 보장합니다.

### 실험 설정
- **하드웨어 플랫폼**: DAVIS346 이벤트 카메라 기반 오픈소스 원격 조작 플랫폼으로, RGB 프레임과 이벤트 스트림을 동시에 출력할 수 있습니다.
- **데이터셋**: 다양한 작업(예: Pick-Place, Sorting)과 조명 조건(밝은 환경부터 20 lux 극도로 어두운 환경까지)을 포괄하는 동기화된 RGB-이벤트-행동 데이터를 수집했습니다.
- **비교 기준선**: 순수 RGB 이미지 입력을 사용하는 VLA 모델을 기준으로 삼아, 다양한 이벤트 융합 전략의 효과를 비교했습니다.

### 주요 실험 결과
- **어두운 환경(20 lux)**:
  - Pick-Place 작업: 순수 이미지 기준선 성공률 0%, 오버레이 융합 시 60%로 상승, 이벤트 어댑터는 90% 도달.
- **심각한 모션 블러(1000 ms 노출 시뮬레이션)**:
  - Pick-Place 작업: 0%에서 20-25%로 상승.
  - Sorting 작업: 5%에서 32.5%로 상승.
- **결론**: 가장 단순한 파라미터 비의존적 융합만으로도 상당한 개선을 얻을 수 있으며, 이벤트 어댑터는 극한 조건에서 더 우수한 성능을 보입니다.

### 결론 및 전망
E-VLA 시스템은 이벤트 기반 인식이 VLA 모델에 효과적으로 통합될 수 있음을 체계적으로 입증하며, 전통적인 프레임 기반 이미징을 넘어선 강건한 임베디드 인텔리전스를 위한 실현 가능한 경로를 제시합니다. 코드와 데이터셋은 GitHub에 오픈소스로 공개될 예정입니다.
