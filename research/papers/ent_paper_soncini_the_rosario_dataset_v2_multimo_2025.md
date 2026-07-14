---
$id: ent_paper_soncini_the_rosario_dataset_v2_multimo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The Rosario Dataset v2: Multimodal Dataset for Agricultural Robotics'
  zh: 罗萨里奥数据集 v2：面向农业机器人的多模态数据集
  ko: '로사리오 데이터셋 v2: 농업 로보틱스를 위한 다중 모달 데이터셋'
summary:
  en: A two-hour-plus, hardware-synchronized multi-sensor dataset collected in a soybean field, providing stereo IR/RGB images,
    IMU, multi-band GNSS, wheel odometry, and 6-DoF ground truth for benchmarking multi-modal SLAM in agricultural robotics.
  zh: 在 soybean 农田采集的超过两小时硬件同步多传感器数据集，提供立体红外/彩色图像、IMU、多频段GNSS、轮式里程计及6自由度真值，用于农业机器人多模态SLAM的基准测试。
  ko: 콩밭에서 2시간 이상 하드웨어 동기화된 다중 센서 데이터셋으로, 스테레오 적외선/컬러 영상, IMU, 다중 대역 GNSS, 바퀴 주행거리 및 6자유도 참값을 제공하여 농업 로보틱스 멀티모달 SLAM 벤치마크를
    지원한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- dataset
- multimodal_slam
- sensor_fusion
- outdoor_localization
- gnss
- ground_truth
- loop_closure
- agricultural_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.21635v1.
sources:
- id: src_001
  type: paper
  title: 'The Rosario Dataset v2: Multimodal Dataset for Agricultural Robotics'
  url: https://arxiv.org/abs/2508.21635
  date: '2025'
  accessed_at: '2026-06-27'
  doi: 10.1177/02783649251368909
theoretical_depth:
- method
---
## 概述
We present a multi-modal dataset collected in a soybean crop field, comprising over two hours of recorded data from sensors such as stereo infrared camera, color camera, accelerometer, gyroscope, magnetometer, GNSS (Single Point Positioning, Real-Time Kinematic and Post-Processed Kinematic), and wheel odometry. This dataset captures key challenges inherent to robotics in agricultural environments, including variations in natural lighting, motion blur, rough terrain, and long, perceptually aliased sequences. By addressing these complexities, the dataset aims to support the development and benchmarking of advanced algorithms for localization, mapping, perception, and navigation in agricultural robotics. The platform and data collection system is designed to meet the key requirements for evaluating multi-modal SLAM systems, including hardware synchronization of sensors, 6-DOF ground truth and loops on long trajectories.   We run multimodal state-of-the art SLAM methods on the dataset, showcasing the existing limitations in their application on agricultural settings. The dataset and utilities to work with it are released on https://cifasis.github.io/rosariov2/.

## 核心内容
We present a multi-modal dataset collected in a soybean crop field, comprising over two hours of recorded data from sensors such as stereo infrared camera, color camera, accelerometer, gyroscope, magnetometer, GNSS (Single Point Positioning, Real-Time Kinematic and Post-Processed Kinematic), and wheel odometry. This dataset captures key challenges inherent to robotics in agricultural environments, including variations in natural lighting, motion blur, rough terrain, and long, perceptually aliased sequences. By addressing these complexities, the dataset aims to support the development and benchmarking of advanced algorithms for localization, mapping, perception, and navigation in agricultural robotics. The platform and data collection system is designed to meet the key requirements for evaluating multi-modal SLAM systems, including hardware synchronization of sensors, 6-DOF ground truth and loops on long trajectories.   We run multimodal state-of-the art SLAM methods on the dataset, showcasing the existing limitations in their application on agricultural settings. The dataset and utilities to work with it are released on https://cifasis.github.io/rosariov2/.

## 参考
- http://arxiv.org/abs/2508.21635v1

