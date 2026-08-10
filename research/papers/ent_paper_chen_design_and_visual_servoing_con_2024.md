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
  zh: 本文提出了一种名为MicroNeuro的缆索驱动混合双段柔性机器人内窥镜，用于脑室内肿瘤活检，并开发了基于图像的视觉伺服框架，通过在线雅可比估计和约束模型预测控制提升跟踪精度与鲁棒性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.09679v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (595 chars, DeepSeek).'
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
传统刚性内窥镜在处理脑深部肿瘤时存在灵活性不足、操作受限及视角固定等问题。为此，本研究设计了双段柔性机器人内窥镜MicroNeuro，旨在实现脑深部灵巧的手术活检操作。针对控制模型的不确定性，团队实现了基于图像的视觉伺服系统，结合在线机器人雅可比估计以提高运动精度。同时，引入带约束的模型预测控制，显著增强了柔性机器人对移动目标的适应性跟踪能力和抗外部干扰能力。

## 核心内容
### 系统设计
- **MicroNeuro** 采用缆索驱动的混合双段柔性结构，专为脑室内肿瘤活检设计，可在脑深部实现灵巧操作。
- 双段设计允许独立控制，提升末端执行器的灵活性与可达性。

### 控制方法
- **基于图像的视觉伺服（IBVS）**：通过在线估计机器人雅可比矩阵，补偿控制模型的不确定性，提高运动精度。
- **约束模型预测控制（MPC）**：在控制过程中施加约束，增强柔性机器人对动态目标的跟踪能力，并有效抵抗外部干扰。

### 实验与结果
- 实验表明，所提控制系统显著提升了运动稳定性与精度。
- 在仿体（phantom）测试中，系统展现出在神经外科手术中的实际应用潜力，验证了其可行性。

### 结论
MicroNeuro结合在线雅可比估计与约束MPC的视觉伺服框架，为脑室内活检提供了一种高精度、强鲁棒性的解决方案，有望推动柔性机器人在神经外科中的临床转化。

## Overview
Traditional rigid endoscopes have challenges in flexibly treating tumors located deep in the brain, and low operability and fixed viewing angles limit its development. This study introduces a novel dual-segment flexible robotic endoscope MicroNeuro, designed to perform biopsies with dexterous surgical manipulation deep in the brain. Taking into account the uncertainty of the control model, an image-based visual servoing with online robot Jacobian estimation has been implemented to enhance motion accuracy. Furthermore, the application of model predictive control with constraints significantly bolsters the flexible robot's ability to adaptively track mobile objects and resist external interference. Experimental results underscore that the proposed control system enhances motion stability and precision. Phantom testing substantiates its considerable potential for deployment in neurosurgery.

## Overview
Traditional rigid endoscopes face challenges in flexibly treating tumors located deep in the brain, and their low operability and fixed viewing angles limit their development. This study introduces a novel dual-segment flexible robotic endoscope, MicroNeuro, designed to perform biopsies with dexterous surgical manipulation deep in the brain. Considering the uncertainty of the control model, an image-based visual servoing with online robot Jacobian estimation has been implemented to enhance motion accuracy. Furthermore, the application of model predictive control with constraints significantly bolsters the flexible robot's ability to adaptively track moving objects and resist external interference. Experimental results underscore that the proposed control system enhances motion stability and precision. Phantom testing substantiates its considerable potential for deployment in neurosurgery.

## Content
Traditional rigid endoscopes face challenges in flexibly treating tumors located deep in the brain, and their low operability and fixed viewing angles limit their development. This study introduces a novel dual-segment flexible robotic endoscope, MicroNeuro, designed to perform biopsies with dexterous surgical manipulation deep in the brain. Considering the uncertainty of the control model, an image-based visual servoing with online robot Jacobian estimation has been implemented to enhance motion accuracy. Furthermore, the application of model predictive control with constraints significantly bolsters the flexible robot's ability to adaptively track moving objects and resist external interference. Experimental results underscore that the proposed control system enhances motion stability and precision. Phantom testing substantiates its considerable potential for deployment in neurosurgery.

## 参考
- http://arxiv.org/abs/2402.09679v2

## 개요
전통적인 강성 내시경은 뇌심부 종양을 다룰 때 유연성 부족, 조작 제한, 고정된 시야 등의 문제가 있습니다. 이를 해결하기 위해 본 연구는 이중 분절 유연 로봇 내시경 MicroNeuro를 설계하여 뇌심부에서 정교한 생검 수술을 구현하고자 했습니다. 제어 모델의 불확실성을 해결하기 위해 팀은 온라인 로봇 야코비안 추정을 결합한 이미지 기반 시각 서보 시스템을 구현하여 운동 정밀도를 향상시켰습니다. 동시에 제약 조건이 있는 모델 예측 제어를 도입하여 유연 로봇의 이동 표적에 대한 적응형 추적 능력과 외부 간섭 저항 능력을 크게 강화했습니다.

## 핵심 내용
### 시스템 설계
- **MicroNeuro**는 케이블 구동 방식의 혼합 이중 분절 유연 구조를 채택하며, 뇌실 내 종양 생검 전용으로 설계되어 뇌심부에서 정교한 조작이 가능합니다.
- 이중 분절 설계는 독립적인 제어를 허용하여 말단 실행기의 유연성과 도달성을 향상시킵니다.

### 제어 방법
- **이미지 기반 시각 서보(IBVS)**: 온라인으로 로봇 야코비안 행렬을 추정하여 제어 모델의 불확실성을 보상하고 운동 정밀도를 향상시킵니다.
- **제약 모델 예측 제어(MPC)**: 제어 과정에서 제약 조건을 적용하여 유연 로봇의 동적 표적 추적 능력을 강화하고 외부 간섭에 효과적으로 저항합니다.

### 실험 및 결과
- 실험 결과, 제안된 제어 시스템은 운동 안정성과 정밀도를 크게 향상시켰습니다.
- 팬텀(phantom) 테스트에서 시스템은 신경외과 수술에서의 실제 적용 가능성을 보여주며 타당성을 검증했습니다.

### 결론
MicroNeuro는 온라인 야코비안 추정과 제약 MPC를 결합한 시각 서보 프레임워크를 통해 뇌실 내 생검을 위한 고정밀, 강건성 솔루션을 제공하며, 유연 로봇의 신경외과 임상 전환을 촉진할 잠재력을 지닙니다.
