---
$id: ent_paper_chen_design_and_visual_servoing_con_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design and Visual Servoing Control of MicroNeuro for Intraventricular Biopsy
  zh: 用于脑室内活检的混合双段柔性神经外科机器人 MicroNeuro 设计与视觉伺服控制
  ko: 뇌실 생검을 위한 하이브리드 이중 세그먼트 유연한 신경외과 로봇 MicroNeuro의 설계 및 시각 서보 제어
summary:
  en: This paper presents MicroNeuro, a cable-driven hybrid dual-segment flexible robotic endoscope for intraventricular brain-tumor
    biopsy, together with an image-based visual servoing framework that uses online Jacobian estimation and constrained model
    predictive control to improve tracking accuracy and robustness.
  zh: 本文介绍了MicroNeuro，一种用于脑室内脑肿瘤活检的线缆驱动混合双段柔性机器人内窥镜，以及一种基于图像的视觉伺服框架，该框架利用在线雅可比估计和约束模型预测控制来提高跟踪精度和鲁棒性。
  ko: 본 논문은 뇌실 내 뇌종양 생검을 위한 케이블 구동 하이브리드 이중 세그먼트 유연한 로봇 내시경 MicroNeuro와 온라인 자코비안 추정 및 제약 조건이 있는 모델 예측 제어를 사용하는 이미지 기반 시각 서보
    프레임워크를 제시하여 추적 정확도와 견고성을 향상시킨다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- visual_servoing
- model_predictive_control
- online_jacobian_estimation
- continuum_robot
- flexible_endoscope
- neurosurgery
- intraventricular_biopsy
- cable_driven_robot
- dual_segment
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.09679v2.
sources:
- id: src_001
  type: paper
  title: Design and Visual Servoing Control of a Hybrid Dual-Segment Flexible Neurosurgical Robot for Intraventricular Biopsy
  url: https://arxiv.org/abs/2402.09679
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Traditional rigid endoscopes have challenges in flexibly treating tumors located deep in the brain, and low operability and fixed viewing angles limit its development. This study introduces a novel dual-segment flexible robotic endoscope MicroNeuro, designed to perform biopsies with dexterous surgical manipulation deep in the brain. Taking into account the uncertainty of the control model, an image-based visual servoing with online robot Jacobian estimation has been implemented to enhance motion accuracy. Furthermore, the application of model predictive control with constraints significantly bolsters the flexible robot's ability to adaptively track mobile objects and resist external interference. Experimental results underscore that the proposed control system enhances motion stability and precision. Phantom testing substantiates its considerable potential for deployment in neurosurgery.

## 核心内容
Traditional rigid endoscopes have challenges in flexibly treating tumors located deep in the brain, and low operability and fixed viewing angles limit its development. This study introduces a novel dual-segment flexible robotic endoscope MicroNeuro, designed to perform biopsies with dexterous surgical manipulation deep in the brain. Taking into account the uncertainty of the control model, an image-based visual servoing with online robot Jacobian estimation has been implemented to enhance motion accuracy. Furthermore, the application of model predictive control with constraints significantly bolsters the flexible robot's ability to adaptively track mobile objects and resist external interference. Experimental results underscore that the proposed control system enhances motion stability and precision. Phantom testing substantiates its considerable potential for deployment in neurosurgery.

## 参考
- http://arxiv.org/abs/2402.09679v2

