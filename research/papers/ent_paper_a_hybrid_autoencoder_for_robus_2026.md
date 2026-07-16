---
$id: ent_paper_a_hybrid_autoencoder_for_robus_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
  zh: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
  ko: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
summary:
  en: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion is
    a 2026 work on locomotion for humanoid robots.
  zh: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion is
    a 2026 work on locomotion for humanoid robots.
  ko: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion is
    a 2026 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_hybrid_autoencoder_for_robus
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.05855v1.
sources:
- id: src_001
  type: paper
  title: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
    (arXiv)
  url: https://arxiv.org/abs/2602.05855
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reliable terrain perception is a critical prerequisite for the deployment of humanoid robots in unstructured, human-centric environments. While traditional systems often rely on manually engineered, single-sensor pipelines, this paper presents a learning-based framework that uses an intermediate, robot-centric heightmap representation. A hybrid Encoder-Decoder Structure (EDS) is introduced, utilizing a Convolutional Neural Network (CNN) for spatial feature extraction fused with a Gated Recurrent Unit (GRU) core for temporal consistency. The architecture integrates multimodal data from an Intel RealSense depth camera, a LIVOX MID-360 LiDAR processed via efficient spherical projection, and an onboard IMU. Quantitative results demonstrate that multimodal fusion improves reconstruction accuracy by 7.2% over depth-only and 9.9% over LiDAR-only configurations. Furthermore, the integration of a 3.2 s temporal context reduces mapping drift.

## 核心内容
Reliable terrain perception is a critical prerequisite for the deployment of humanoid robots in unstructured, human-centric environments. While traditional systems often rely on manually engineered, single-sensor pipelines, this paper presents a learning-based framework that uses an intermediate, robot-centric heightmap representation. A hybrid Encoder-Decoder Structure (EDS) is introduced, utilizing a Convolutional Neural Network (CNN) for spatial feature extraction fused with a Gated Recurrent Unit (GRU) core for temporal consistency. The architecture integrates multimodal data from an Intel RealSense depth camera, a LIVOX MID-360 LiDAR processed via efficient spherical projection, and an onboard IMU. Quantitative results demonstrate that multimodal fusion improves reconstruction accuracy by 7.2% over depth-only and 9.9% over LiDAR-only configurations. Furthermore, the integration of a 3.2 s temporal context reduces mapping drift.

## 参考
- http://arxiv.org/abs/2602.05855v1

## Overview
Reliable terrain perception is a critical prerequisite for the deployment of humanoid robots in unstructured, human-centric environments. While traditional systems often rely on manually engineered, single-sensor pipelines, this paper presents a learning-based framework that uses an intermediate, robot-centric heightmap representation. A hybrid Encoder-Decoder Structure (EDS) is introduced, utilizing a Convolutional Neural Network (CNN) for spatial feature extraction fused with a Gated Recurrent Unit (GRU) core for temporal consistency. The architecture integrates multimodal data from an Intel RealSense depth camera, a LIVOX MID-360 LiDAR processed via efficient spherical projection, and an onboard IMU. Quantitative results demonstrate that multimodal fusion improves reconstruction accuracy by 7.2% over depth-only and 9.9% over LiDAR-only configurations. Furthermore, the integration of a 3.2 s temporal context reduces mapping drift.

## Content
Reliable terrain perception is a critical prerequisite for the deployment of humanoid robots in unstructured, human-centric environments. While traditional systems often rely on manually engineered, single-sensor pipelines, this paper presents a learning-based framework that uses an intermediate, robot-centric heightmap representation. A hybrid Encoder-Decoder Structure (EDS) is introduced, utilizing a Convolutional Neural Network (CNN) for spatial feature extraction fused with a Gated Recurrent Unit (GRU) core for temporal consistency. The architecture integrates multimodal data from an Intel RealSense depth camera, a LIVOX MID-360 LiDAR processed via efficient spherical projection, and an onboard IMU. Quantitative results demonstrate that multimodal fusion improves reconstruction accuracy by 7.2% over depth-only and 9.9% over LiDAR-only configurations. Furthermore, the integration of a 3.2 s temporal context reduces mapping drift.

## 개요
신뢰할 수 있는 지형 인식은 인간형 로봇이 비정형적이고 인간 중심적인 환경에서 배치되기 위한 중요한 전제 조건입니다. 기존 시스템은 종종 수동으로 설계된 단일 센서 파이프라인에 의존하는 반면, 본 논문은 중간 단계의 로봇 중심 높이 맵 표현을 사용하는 학습 기반 프레임워크를 제시합니다. 하이브리드 인코더-디코더 구조(EDS)가 도입되었으며, 공간 특징 추출을 위한 합성곱 신경망(CNN)과 시간적 일관성을 위한 게이트 순환 유닛(GRU) 코어를 융합하여 활용합니다. 이 아키텍처는 Intel RealSense 깊이 카메라, 효율적인 구형 투영을 통해 처리된 LIVOX MID-360 LiDAR, 그리고 온보드 IMU의 다중 모달 데이터를 통합합니다. 정량적 결과는 다중 모달 융합이 깊이 전용 구성 대비 7.2%, LiDAR 전용 구성 대비 9.9%의 재구성 정확도 향상을 보여줍니다. 또한 3.2초의 시간적 맥락 통합은 매핑 드리프트를 줄입니다.

## 핵심 내용
신뢰할 수 있는 지형 인식은 인간형 로봇이 비정형적이고 인간 중심적인 환경에서 배치되기 위한 중요한 전제 조건입니다. 기존 시스템은 종종 수동으로 설계된 단일 센서 파이프라인에 의존하는 반면, 본 논문은 중간 단계의 로봇 중심 높이 맵 표현을 사용하는 학습 기반 프레임워크를 제시합니다. 하이브리드 인코더-디코더 구조(EDS)가 도입되었으며, 공간 특징 추출을 위한 합성곱 신경망(CNN)과 시간적 일관성을 위한 게이트 순환 유닛(GRU) 코어를 융합하여 활용합니다. 이 아키텍처는 Intel RealSense 깊이 카메라, 효율적인 구형 투영을 통해 처리된 LIVOX MID-360 LiDAR, 그리고 온보드 IMU의 다중 모달 데이터를 통합합니다. 정량적 결과는 다중 모달 융합이 깊이 전용 구성 대비 7.2%, LiDAR 전용 구성 대비 9.9%의 재구성 정확도 향상을 보여줍니다. 또한 3.2초의 시간적 맥락 통합은 매핑 드리프트를 줄입니다.
