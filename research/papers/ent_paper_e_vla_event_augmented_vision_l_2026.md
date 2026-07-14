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
  en: "arXiv:2604.04834v2 Announce Type: replace-cross \nAbstract: Robotic Vision-Language-Action\
    \ (VLA) models generalize well for open-ended manipulation, but their perception\
    \ is fragile under sensing-stage degradations such as extreme low light, motion\
    \ blur, and black clipping. We present E-VLA, an event-augmented VLA framework\
    \ that improves manipulation robustness when conventional frame-based vision becomes\
    \ unreliable. Instead of reconstructing images from events, E-VLA directly leverages\
    \ motion and structural cues in event streams to preserve semantic perception\
    \ and perception-action consistency under adverse conditions. We build an open-source\
    \ teleoperation platform with a DAVIS346 event camera and collect a real-world\
    \ synchronized RGB-event-action manipulation dataset across diverse tasks and\
    \ illuminations. We also propose lightweight, pretrained-compatible event integration\
    \ strategies and study event windowing for stable deployment. Experiments show\
    \ that even a simple parameter-free fusion, i.e., overlaying accumulated event\
    \ maps onto RGB images, could substantially improve robustness in dark and heavy-blur\
    \ scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60%\
    \ with overlay fusion and to 90% with our event adapter; under severe motion blur\
    \ (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting\
    \ from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven\
    \ perception can be effectively integrated into VLA models, pointing toward robust\
    \ embodied intelligence beyond conventional frame-based imaging. Code and dataset\
    \ will be available at https://github.com/JJayzee/E-VLA."
  zh: "arXiv:2604.04834v2 Announce Type: replace-cross \nAbstract: Robotic Vision-Language-Action\
    \ (VLA) models generalize well for open-ended manipulation, but their perception\
    \ is fragile under sensing-stage degradations such as extreme low light, motion\
    \ blur, and black clipping. We present E-VLA, an event-augmented VLA framework\
    \ that improves manipulation robustness when conventional frame-based vision becomes\
    \ unreliable. Instead of reconstructing images from events, E-VLA directly leverages\
    \ motion and structural cues in event streams to preserve semantic perception\
    \ and perception-action consistency under adverse conditions. We build an open-source\
    \ teleoperation platform with a DAVIS346 event camera and collect a real-world\
    \ synchronized RGB-event-action manipulation dataset across diverse tasks and\
    \ illuminations. We also propose lightweight, pretrained-compatible event integration\
    \ strategies and study event windowing for stable deployment. Experiments show\
    \ that even a simple parameter-free fusion, i.e., overlaying accumulated event\
    \ maps onto RGB images, could substantially improve robustness in dark and heavy-blur\
    \ scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60%\
    \ with overlay fusion and to 90% with our event adapter; under severe motion blur\
    \ (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting\
    \ from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven\
    \ perception can be effectively integrated into VLA models, pointing toward robust\
    \ embodied intelligence beyond conventional frame-based imaging. Code and dataset\
    \ will be available at https://github.com/JJayzee/E-VLA."
  ko: "arXiv:2604.04834v2 Announce Type: replace-cross \nAbstract: Robotic Vision-Language-Action\
    \ (VLA) models generalize well for open-ended manipulation, but their perception\
    \ is fragile under sensing-stage degradations such as extreme low light, motion\
    \ blur, and black clipping. We present E-VLA, an event-augmented VLA framework\
    \ that improves manipulation robustness when conventional frame-based vision becomes\
    \ unreliable. Instead of reconstructing images from events, E-VLA directly leverages\
    \ motion and structural cues in event streams to preserve semantic perception\
    \ and perception-action consistency under adverse conditions. We build an open-source\
    \ teleoperation platform with a DAVIS346 event camera and collect a real-world\
    \ synchronized RGB-event-action manipulation dataset across diverse tasks and\
    \ illuminations. We also propose lightweight, pretrained-compatible event integration\
    \ strategies and study event windowing for stable deployment. Experiments show\
    \ that even a simple parameter-free fusion, i.e., overlaying accumulated event\
    \ maps onto RGB images, could substantially improve robustness in dark and heavy-blur\
    \ scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60%\
    \ with overlay fusion and to 90% with our event adapter; under severe motion blur\
    \ (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting\
    \ from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven\
    \ perception can be effectively integrated into VLA models, pointing toward robust\
    \ embodied intelligence beyond conventional frame-based imaging. Code and dataset\
    \ will be available at https://github.com/JJayzee/E-VLA."
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
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: 'E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred
    Scenes'
  url: https://arxiv.org/abs/2604.04834
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
arXiv:2604.04834v2 Announce Type: replace-cross 
Abstract: Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.

## Overview
arXiv:2604.04834v2 Announce Type: replace-cross 
Abstract: Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.

## 개요
arXiv:2604.04834v2 Announce Type: replace-cross 
Abstract: Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illuminations. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and heavy-blur scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms-exposure proxy), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.
