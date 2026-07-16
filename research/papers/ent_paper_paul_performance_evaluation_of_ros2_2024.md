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

## Overview
In the autonomous vehicle and self-driving paradigm, cooperative perception or exchanging sensor information among vehicles over wireless communication has added a new dimension. Generally, an autonomous vehicle is a special type of robot that requires real-time, highly reliable sensor inputs due to functional safety. Autonomous vehicles are equipped with a considerable number of sensors to provide different required sensor data to make the driving decision and share with other surrounding vehicles. The inclusion of Data Distribution Service (DDS) as a communication middleware in ROS2 has proved its potential capability to be a reliable real-time distributed system. DDS comes with a scoping mechanism known as domain. Whenever a ROS2 process is initiated, it creates a DDS participant. It is important to note that there is a limit to the number of participants allowed in a single domain. The efficient handling of numerous in-vehicle sensors and their messages demands the use of multiple ROS2 nodes in a single vehicle. Additionally, in the cooperative perception paradigm, a significant number of ROS2 nodes can be required when a vehicle functions as a single ROS2 node. These ROS2 nodes cannot be part of a single domain due to DDS participant limitation; thus, different domain communication is unavoidable. Moreover, there are different vendor-specific implementations of DDS, and each vendor has their configurations, which is an inevitable communication catalyst between the ROS2 nodes. The communication between vehicles or robots or ROS2 nodes depends directly on the vendor-specific configuration, data type, data size, and the DDS implementation used as middleware; in our study, we evaluate and investigate the limitations, capabilities, and prospects of the different domain communication for various vendor-specific DDS implementations for diverse sensor data type.

## Content
In the autonomous vehicle and self-driving paradigm, cooperative perception or exchanging sensor information among vehicles over wireless communication has added a new dimension. Generally, an autonomous vehicle is a special type of robot that requires real-time, highly reliable sensor inputs due to functional safety. Autonomous vehicles are equipped with a considerable number of sensors to provide different required sensor data to make the driving decision and share with other surrounding vehicles. The inclusion of Data Distribution Service (DDS) as a communication middleware in ROS2 has proved its potential capability to be a reliable real-time distributed system. DDS comes with a scoping mechanism known as domain. Whenever a ROS2 process is initiated, it creates a DDS participant. It is important to note that there is a limit to the number of participants allowed in a single domain. The efficient handling of numerous in-vehicle sensors and their messages demands the use of multiple ROS2 nodes in a single vehicle. Additionally, in the cooperative perception paradigm, a significant number of ROS2 nodes can be required when a vehicle functions as a single ROS2 node. These ROS2 nodes cannot be part of a single domain due to DDS participant limitation; thus, different domain communication is unavoidable. Moreover, there are different vendor-specific implementations of DDS, and each vendor has their configurations, which is an inevitable communication catalyst between the ROS2 nodes. The communication between vehicles or robots or ROS2 nodes depends directly on the vendor-specific configuration, data type, data size, and the DDS implementation used as middleware; in our study, we evaluate and investigate the limitations, capabilities, and prospects of the different domain communication for various vendor-specific DDS implementations for diverse sensor data type.

## 개요
자율주행차 및 자율주행 패러다임에서, 차량 간 무선 통신을 통한 협력적 인식 또는 센서 정보 교환은 새로운 차원을 더했습니다. 일반적으로 자율주행차는 기능 안전성으로 인해 실시간, 고신뢰성 센서 입력을 요구하는 특수한 유형의 로봇입니다. 자율주행차는 주행 결정을 내리고 주변 차량과 공유하기 위해 다양한 요구 센서 데이터를 제공하는 상당한 수의 센서를 장착하고 있습니다. ROS2에서 통신 미들웨어로 Data Distribution Service(DDS)를 포함한 것은 신뢰할 수 있는 실시간 분산 시스템으로서의 잠재적 능력을 입증했습니다. DDS에는 도메인이라고 알려진 범위 지정 메커니즘이 있습니다. ROS2 프로세스가 시작될 때마다 DDS 참가자가 생성됩니다. 단일 도메인에서 허용되는 참가자 수에는 제한이 있다는 점에 유의하는 것이 중요합니다. 차량 내 다수의 센서와 해당 메시지를 효율적으로 처리하려면 단일 차량에서 여러 ROS2 노드를 사용해야 합니다. 또한, 협력적 인식 패러다임에서 차량이 단일 ROS2 노드로 기능할 때 상당한 수의 ROS2 노드가 필요할 수 있습니다. 이러한 ROS2 노드는 DDS 참가자 제한으로 인해 단일 도메인의 일부가 될 수 없으므로, 서로 다른 도메인 간 통신은 불가피합니다. 더욱이, 다양한 벤더별 DDS 구현이 있으며, 각 벤더는 자체 구성을 가지고 있어 ROS2 노드 간의 필연적인 통신 촉매제 역할을 합니다. 차량, 로봇 또는 ROS2 노드 간의 통신은 벤더별 구성, 데이터 유형, 데이터 크기 및 미들웨어로 사용되는 DDS 구현에 직접적으로 의존합니다. 본 연구에서는 다양한 센서 데이터 유형에 대한 다양한 벤더별 DDS 구현의 서로 다른 도메인 통신의 한계, 기능 및 전망을 평가하고 조사합니다.

## 핵심 내용
자율주행차 및 자율주행 패러다임에서, 차량 간 무선 통신을 통한 협력적 인식 또는 센서 정보 교환은 새로운 차원을 더했습니다. 일반적으로 자율주행차는 기능 안전성으로 인해 실시간, 고신뢰성 센서 입력을 요구하는 특수한 유형의 로봇입니다. 자율주행차는 주행 결정을 내리고 주변 차량과 공유하기 위해 다양한 요구 센서 데이터를 제공하는 상당한 수의 센서를 장착하고 있습니다. ROS2에서 통신 미들웨어로 Data Distribution Service(DDS)를 포함한 것은 신뢰할 수 있는 실시간 분산 시스템으로서의 잠재적 능력을 입증했습니다. DDS에는 도메인이라고 알려진 범위 지정 메커니즘이 있습니다. ROS2 프로세스가 시작될 때마다 DDS 참가자가 생성됩니다. 단일 도메인에서 허용되는 참가자 수에는 제한이 있다는 점에 유의하는 것이 중요합니다. 차량 내 다수의 센서와 해당 메시지를 효율적으로 처리하려면 단일 차량에서 여러 ROS2 노드를 사용해야 합니다. 또한, 협력적 인식 패러다임에서 차량이 단일 ROS2 노드로 기능할 때 상당한 수의 ROS2 노드가 필요할 수 있습니다. 이러한 ROS2 노드는 DDS 참가자 제한으로 인해 단일 도메인의 일부가 될 수 없으므로, 서로 다른 도메인 간 통신은 불가피합니다. 더욱이, 다양한 벤더별 DDS 구현이 있으며, 각 벤더는 자체 구성을 가지고 있어 ROS2 노드 간의 필연적인 통신 촉매제 역할을 합니다. 차량, 로봇 또는 ROS2 노드 간의 통신은 벤더별 구성, 데이터 유형, 데이터 크기 및 미들웨어로 사용되는 DDS 구현에 직접적으로 의존합니다. 본 연구에서는 다양한 센서 데이터 유형에 대한 다양한 벤더별 DDS 구현의 서로 다른 도메인 통신의 한계, 기능 및 전망을 평가하고 조사합니다.
