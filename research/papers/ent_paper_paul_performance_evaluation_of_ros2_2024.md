---
$id: ent_paper_paul_performance_evaluation_of_ros2_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Performance Evaluation of ROS2-DDS middleware implementations facilitating Cooperative Driving in Autonomous Vehicle
  zh: 促进自动驾驶协同驾驶的ROS2-DDS中间件实现性能评估
  ko: 자율주행 차량의 협력 주행을 위한 ROS2-DDS 미들웨어 구현체의 성능 평가
summary:
  en: This paper empirically evaluates same-domain and cross-domain ROS2-DDS communication latency across Eclipse Cyclone
    DDS, eProsima Fast-DDS, and RTI Connext DDS using heterogeneous physical devices and multiple data types.
  zh: 本文使用异构物理设备和多种数据类型，对Eclipse Cyclone DDS、eProsima Fast-DDS和RTI Connext DDS的域内和跨域ROS2-DDS通信延迟进行了实证评估。
  ko: 본 논문은 이종 물리적 장치와 다양한 데이터 유형을 사용하여 Eclipse Cyclone DDS, eProsima Fast-DDS, RTI Connext DDS의 동일 도메인 및 교차 도메인 ROS2-DDS
    통신 지연 시간을 실증적으로 평가한다.
domains:
- 08_software_middleware
- 10_evaluation_benchmarks
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- system
tags:
- ros2
- dds
- middleware
- autonomous_vehicles
- cooperative_perception
- multi_domain_communication
- cross_domain_latency
- latency_evaluation
- cyclone_dds
- fast_dds
- connext_dds
- real_time_communication
- heterogeneous_devices
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.07485v1.
sources:
- id: src_001
  type: paper
  title: Performance Evaluation of ROS2-DDS middleware implementations facilitating Cooperative Driving in Autonomous Vehicle
  url: https://arxiv.org/abs/2412.07485
  date: '2024'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
In the autonomous vehicle and self-driving paradigm, cooperative perception or exchanging sensor information among vehicles over wireless communication has added a new dimension. Generally, an autonomous vehicle is a special type of robot that requires real-time, highly reliable sensor inputs due to functional safety. Autonomous vehicles are equipped with a considerable number of sensors to provide different required sensor data to make the driving decision and share with other surrounding vehicles. The inclusion of Data Distribution Service(DDS) as a communication middleware in ROS2 has proved its potential capability to be a reliable real-time distributed system. DDS comes with a scoping mechanism known as domain. Whenever a ROS2 process is initiated, it creates a DDS participant. It is important to note that there is a limit to the number of participants allowed in a single domain.   The efficient handling of numerous in-vehicle sensors and their messages demands the use of multiple ROS2 nodes in a single vehicle. Additionally, in the cooperative perception paradigm, a significant number of ROS2 nodes can be required when a vehicle functions as a single ROS2 node. These ROS2 nodes cannot be part of a single domain due to DDS participant limitation; thus, different domain communication is unavoidable. Moreover, there are different vendor-specific implementations of DDS, and each vendor has their configurations, which is an inevitable communication catalyst between the ROS2 nodes. The communication between vehicles or robots or ROS2 nodes depends directly on the vendor-specific configuration, data type, data size, and the DDS implementation used as middleware; in our study, we evaluate and investigate the limitations, capabilities, and prospects of the different domain communication for various vendor-specific DDS implementations for diverse sensor data type.

## 核心内容
In the autonomous vehicle and self-driving paradigm, cooperative perception or exchanging sensor information among vehicles over wireless communication has added a new dimension. Generally, an autonomous vehicle is a special type of robot that requires real-time, highly reliable sensor inputs due to functional safety. Autonomous vehicles are equipped with a considerable number of sensors to provide different required sensor data to make the driving decision and share with other surrounding vehicles. The inclusion of Data Distribution Service(DDS) as a communication middleware in ROS2 has proved its potential capability to be a reliable real-time distributed system. DDS comes with a scoping mechanism known as domain. Whenever a ROS2 process is initiated, it creates a DDS participant. It is important to note that there is a limit to the number of participants allowed in a single domain.   The efficient handling of numerous in-vehicle sensors and their messages demands the use of multiple ROS2 nodes in a single vehicle. Additionally, in the cooperative perception paradigm, a significant number of ROS2 nodes can be required when a vehicle functions as a single ROS2 node. These ROS2 nodes cannot be part of a single domain due to DDS participant limitation; thus, different domain communication is unavoidable. Moreover, there are different vendor-specific implementations of DDS, and each vendor has their configurations, which is an inevitable communication catalyst between the ROS2 nodes. The communication between vehicles or robots or ROS2 nodes depends directly on the vendor-specific configuration, data type, data size, and the DDS implementation used as middleware; in our study, we evaluate and investigate the limitations, capabilities, and prospects of the different domain communication for various vendor-specific DDS implementations for diverse sensor data type.

## 参考
- http://arxiv.org/abs/2412.07485v1

