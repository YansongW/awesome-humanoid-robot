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
  zh: 'arXiv:2604.04834v2 Announce Type: replace-cross Abstract: Robotic Vision-Language-Action (VLA) models generalize well
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.04834v2.
sources:
- id: src_001
  type: paper
  title: 'E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes'
  url: https://arxiv.org/abs/2604.04834
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.

## 核心内容
Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.

## 参考
- http://arxiv.org/abs/2604.04834v2

## Overview
Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.

## Content
Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.

## 개요
Robotic Vision-Language-Action (VLA) 모델은 개방형 조작 작업에서 일반화 성능이 뛰어나지만, 극도로 낮은 조도, 모션 블러, 블랙 클리핑과 같은 센싱 단계의 열화에 취약합니다. 본 논문에서는 기존 프레임 기반 비전이 신뢰할 수 없을 때 조작의 강건성을 향상시키는 이벤트 증강 VLA 프레임워크인 E-VLA를 제안합니다. E-VLA는 이벤트로부터 이미지를 재구성하는 대신, 이벤트 스트림의 움직임 및 구조적 단서를 직접 활용하여 열악한 조건에서도 의미론적 인식과 인식-행동 일관성을 유지합니다. DAVIS346 이벤트 카메라를 갖춘 오픈소스 원격 조작 플랫폼을 구축하고, 다양한 작업과 조명 조건에서 실제 세계의 동기화된 RGB-이벤트-행동 조작 데이터셋을 수집했습니다. 또한, 경량화된 사전 학습 호환 이벤트 통합 전략을 제안하고 안정적인 배포를 위한 이벤트 윈도잉을 연구했습니다. 실험 결과, 누적 이벤트 맵을 RGB 이미지에 오버레이하는 간단한 파라미터 없는 융합조차도 어둡고 심한 블러가 있는 장면에서 강건성을 크게 향상시킬 수 있음을 보여줍니다: 20 lux에서 Pick-Place 작업의 경우, 이미지만 사용했을 때 0%에서 오버레이 융합 시 60%, 당사의 이벤트 어댑터 사용 시 90%로 성공률이 증가했습니다. 심한 모션 블러(1000ms 노출 프록시) 조건에서는 Pick-Place가 0%에서 20-25%로, Sorting이 5%에서 32.5%로 향상되었습니다. 전반적으로 E-VLA는 이벤트 기반 인식이 VLA 모델에 효과적으로 통합될 수 있다는 체계적인 증거를 제공하며, 기존 프레임 기반 이미징을 넘어서는 강건한 구현 지능을 지향합니다. 코드와 데이터셋은 https://github.com/JJayzee/E-VLA에서 제공될 예정입니다.

## 핵심 내용
Robotic Vision-Language-Action (VLA) 모델은 개방형 조작 작업에서 일반화 성능이 뛰어나지만, 극도로 낮은 조도, 모션 블러, 블랙 클리핑과 같은 센싱 단계의 열화에 취약합니다. 본 논문에서는 기존 프레임 기반 비전이 신뢰할 수 없을 때 조작의 강건성을 향상시키는 이벤트 증강 VLA 프레임워크인 E-VLA를 제안합니다. E-VLA는 이벤트로부터 이미지를 재구성하는 대신, 이벤트 스트림의 움직임 및 구조적 단서를 직접 활용하여 열악한 조건에서도 의미론적 인식과 인식-행동 일관성을 유지합니다. DAVIS346 이벤트 카메라를 갖춘 오픈소스 원격 조작 플랫폼을 구축하고, 다양한 작업과 조명 조건에서 실제 세계의 동기화된 RGB-이벤트-행동 조작 데이터셋을 수집했습니다. 또한, 경량화된 사전 학습 호환 이벤트 통합 전략을 제안하고 안정적인 배포를 위한 이벤트 윈도잉을 연구했습니다. 실험 결과, 누적 이벤트 맵을 RGB 이미지에 오버레이하는 간단한 파라미터 없는 융합조차도 어둡고 심한 블러가 있는 장면에서 강건성을 크게 향상시킬 수 있음을 보여줍니다: 20 lux에서 Pick-Place 작업의 경우, 이미지만 사용했을 때 0%에서 오버레이 융합 시 60%, 당사의 이벤트 어댑터 사용 시 90%로 성공률이 증가했습니다. 심한 모션 블러(1000ms 노출 프록시) 조건에서는 Pick-Place가 0%에서 20-25%로, Sorting이 5%에서 32.5%로 향상되었습니다. 전반적으로 E-VLA는 이벤트 기반 인식이 VLA 모델에 효과적으로 통합될 수 있다는 체계적인 증거를 제공하며, 기존 프레임 기반 이미징을 넘어서는 강건한 구현 지능을 지향합니다. 코드와 데이터셋은 https://github.com/JJayzee/E-VLA에서 제공될 예정입니다.
