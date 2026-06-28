---
$id: ent_paper_gao_super_lidar_intensity_for_robo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Super LiDAR Intensity for Robotic Perception
  zh: 面向机器人感知的超级激光雷达强度
  ko: 로봇 인식을 위한 슈퍼 LiDAR 강도
summary:
  en: This paper proposes a real-time CNN-based framework to densify sparse intensity
    images from low-cost non-repeating scanning LiDAR, enabling illumination-invariant
    reflectance estimation for robotic perception tasks such as loop closure and lane
    detection.
  zh: 本文提出了一种基于CNN的实时框架，用于将低成本非重复扫描激光雷达的稀疏强度图像稠密化，从而实现对光照不敏感的反射率估计，并应用于回环检测和车道检测等机器人感知任务。
  ko: 본 논문은 저비용 비반복 스캐닝 LiDAR의 희소 강도 이미지를 실시간으로 고밀도화하는 CNN 기반 프레임워크를 제안하여, 루프 클로저
    및 차선 검출과 같은 로봇 인식 작업을 위한 조명 불변 반사율 추정을 가능하게 한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 09_data_datasets
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- lidar
- intensity_densification
- active_optical_sensing
- nrs_lidar
- low_cost_lidar
- illumination_invariant
- robotic_perception
- slam
- loop_closure
- lane_detection
- cnn
- encoder_decoder
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    required before promotion to verified status.
sources:
- id: src_001
  type: paper
  title: Super LiDAR Intensity for Robotic Perception
  url: https://arxiv.org/abs/2508.10398
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The paper addresses the limitation of low-cost LiDAR sensors, which produce sparse intensity scans that hinder their direct use in robotic perception tasks requiring dense, illumination-invariant reflectance images. It introduces a CNN-based encoder-decoder framework specifically designed for non-repeating scanning LiDAR (NRS-LiDAR), incorporating an Adaptive Fusion Module and a Dynamic Compensation Module. These modules adaptively compensate for distance and incidence-angle effects and bridge the gap between static and dynamic scene domains, enabling real-time densification of LiDAR intensity images in real-world settings.

The proposed framework is validated on applications including loop closure detection and traffic lane detection, demonstrating that dense intensity images from low-cost LiDAR can serve as camera-grade, illumination-invariant inputs for robotic vision. The authors argue that this work establishes a novel paradigm of 'LiDAR as a Camera' by integrating computer vision techniques with LiDAR data processing, thereby enhancing the applicability of low-cost LiDAR systems.

## Key Contributions

- First benchmark dataset for LiDAR intensity image densification with paired sparse-to-dense ground-truth data.
- Real-time densification network tailored for NRS-LiDAR that bridges the static-to-dynamic domain gap and performs adaptive intensity calibration.
- Validation on loop closure detection and traffic lane detection using dense intensity images generated from a low-cost LiDAR.
- Integration of computer vision techniques with LiDAR data processing to enhance the applicability of low-cost LiDAR systems.

## Relevance to Humanoid Robotics

The densification and calibration framework enables low-cost LiDAR to deliver camera-grade, illumination-invariant reflectance images, which is directly applicable to navigation and environmental awareness systems in humanoid robots. This supports robust localization and perception for humanoid platforms deployed in industrial tasks and mass-produced applications, particularly under varying illumination conditions where passive vision may fail.
