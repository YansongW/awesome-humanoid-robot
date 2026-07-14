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
  en: This paper proposes a real-time CNN-based framework to densify sparse intensity images from low-cost non-repeating scanning
    LiDAR, enabling illumination-invariant reflectance estimation for robotic perception tasks such as loop closure and lane
    detection.
  zh: 本文提出了一种基于CNN的实时框架，用于将低成本非重复扫描激光雷达的稀疏强度图像稠密化，从而实现对光照不敏感的反射率估计，并应用于回环检测和车道检测等机器人感知任务。
  ko: 본 논문은 저비용 비반복 스캐닝 LiDAR의 희소 강도 이미지를 실시간으로 고밀도화하는 CNN 기반 프레임워크를 제안하여, 루프 클로저 및 차선 검출과 같은 로봇 인식 작업을 위한 조명 불변 반사율 추정을 가능하게
    한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.10398v2.
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
## 概述
Conventionally, human intuition defines vision as a modality of passive optical sensing, relying on ambient light to perceive the environment. However, active optical sensing, which involves emitting and receiving signals, offers unique advantages by capturing both radiometric and geometric properties of the environment, independent of external illumination conditions. This work focuses on advancing active optical sensing using Light Detection and Ranging (LiDAR), which captures intensity data, enabling the estimation of surface reflectance that remains invariant under varying illumination. Such properties are crucial for robotic perception tasks, including detection, recognition, segmentation, and Simultaneous Localization and Mapping (SLAM). A key challenge with low-cost LiDARs lies in the sparsity of scan data, which limits their broader application. To address this limitation, this work introduces an innovative framework for generating dense LiDAR intensity images from sparse data, leveraging the unique attributes of non-repeating scanning LiDAR (NRS-LiDAR). We tackle critical challenges, including intensity calibration and the transition from static to dynamic scene domains, facilitating the reconstruction of dense intensity images in real-world settings. The key contributions of this work include a comprehensive dataset for LiDAR intensity image densification, a densification network tailored for NRS-LiDAR, and diverse applications such as loop closure and traffic lane detection using the generated dense intensity images. Experimental results validate the efficacy of the proposed approach, which successfully integrates computer vision techniques with LiDAR data processing, enhancing the applicability of low-cost LiDAR systems and establishing a novel paradigm for robotic vision via active optical sensing--LiDAR as a Camera.

## 核心内容
Conventionally, human intuition defines vision as a modality of passive optical sensing, relying on ambient light to perceive the environment. However, active optical sensing, which involves emitting and receiving signals, offers unique advantages by capturing both radiometric and geometric properties of the environment, independent of external illumination conditions. This work focuses on advancing active optical sensing using Light Detection and Ranging (LiDAR), which captures intensity data, enabling the estimation of surface reflectance that remains invariant under varying illumination. Such properties are crucial for robotic perception tasks, including detection, recognition, segmentation, and Simultaneous Localization and Mapping (SLAM). A key challenge with low-cost LiDARs lies in the sparsity of scan data, which limits their broader application. To address this limitation, this work introduces an innovative framework for generating dense LiDAR intensity images from sparse data, leveraging the unique attributes of non-repeating scanning LiDAR (NRS-LiDAR). We tackle critical challenges, including intensity calibration and the transition from static to dynamic scene domains, facilitating the reconstruction of dense intensity images in real-world settings. The key contributions of this work include a comprehensive dataset for LiDAR intensity image densification, a densification network tailored for NRS-LiDAR, and diverse applications such as loop closure and traffic lane detection using the generated dense intensity images. Experimental results validate the efficacy of the proposed approach, which successfully integrates computer vision techniques with LiDAR data processing, enhancing the applicability of low-cost LiDAR systems and establishing a novel paradigm for robotic vision via active optical sensing--LiDAR as a Camera.

## 参考
- http://arxiv.org/abs/2508.10398v2

