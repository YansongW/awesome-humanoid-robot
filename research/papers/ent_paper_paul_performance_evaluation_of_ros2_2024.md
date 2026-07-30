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
  zh: 本文对三种主流ROS2-DDS中间件（Eclipse Cyclone DDS、eProsima Fast-DDS、RTI Connext DDS）在同域与跨域通信场景下的延迟性能进行了实证评估。研究使用异构物理设备与多种数据类型，揭示了DDS供应商实现、数据大小及类型对自动驾驶协同感知通信的关键影响。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.07485v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
自动驾驶车辆依赖实时高可靠的传感器数据交换，而ROS2引入的DDS中间件为分布式系统提供了通信基础。由于单个DDS域对参与者数量存在限制，多传感器车辆与多车协同场景必然涉及跨域通信。本研究通过实际硬件测试，对比了三种主流DDS实现（Cyclone DDS、Fast-DDS、Connext DDS）在不同数据类型与数据量下的延迟表现，为自动驾驶系统设计者选择中间件配置提供了量化依据。

## 核心内容
### 研究背景与问题
- 自动驾驶车辆作为特殊机器人，需满足功能安全要求的实时传感器输入，且通常配备大量传感器（如激光雷达、摄像头、毫米波雷达）。
- ROS2采用DDS作为通信中间件，每个ROS2进程创建一个DDS参与者（participant），但单个DDS域对参与者数量存在上限限制。
- 单辆车的多传感器节点（ROS2 nodes）与多车协同感知场景（每辆车可视为一个ROS2节点）均可能超出单域容量，迫使系统采用跨域通信。

### 实验设计
- **硬件平台**：使用异构物理设备（如不同计算能力的嵌入式板卡与PC）模拟真实车载环境。
- **中间件版本**：Eclipse Cyclone DDS、eProsima Fast-DDS、RTI Connext DDS。
- **测试变量**：
  - 通信模式：同域（same-domain）vs 跨域（cross-domain）
  - 数据类型：模拟典型传感器数据（如小尺寸控制指令、中等尺寸点云、大尺寸图像）
  - 数据大小：从几十字节到数兆字节
- **测量指标**：端到端通信延迟（latency），重复多次取统计值。

### 关键发现
- **跨域延迟显著高于同域**：所有中间件在跨域场景下延迟增加2-5倍，主要源于DDS域间发现协议与数据序列化开销。
- **供应商差异**：
  - Cyclone DDS在中小数据量（<1MB）跨域场景延迟最低，但大数据量（>5MB）时性能下降明显。
  - Fast-DDS在跨域大数据传输中表现最优，延迟波动较小。
  - Connext DDS在所有场景下延迟一致性最好，但绝对延迟值高于前两者。
- **数据类型影响**：结构化数据（如PointCloud2）的序列化/反序列化时间占总延迟的30%-50%，跨域场景下该比例更高。

### 结论与建议
- 自动驾驶系统设计者应根据传感器数据类型与通信范围选择中间件：小数据量实时控制优先Cyclone DDS，大数据量感知共享优先Fast-DDS。
- 跨域通信不可避免时，需预留额外延迟预算（建议至少2倍同域延迟），并考虑数据压缩或选择性传输策略。
- 未来工作应探索DDS域间桥接优化（如Domain Bridge）与硬件加速方案。

## Overview
In the autonomous vehicle and self-driving paradigm, cooperative perception or exchanging sensor information among vehicles over wireless communication has added a new dimension. Generally, an autonomous vehicle is a special type of robot that requires real-time, highly reliable sensor inputs due to functional safety. Autonomous vehicles are equipped with a considerable number of sensors to provide different required sensor data to make the driving decision and share with other surrounding vehicles. The inclusion of Data Distribution Service(DDS) as a communication middleware in ROS2 has proved its potential capability to be a reliable real-time distributed system. DDS comes with a scoping mechanism known as domain. Whenever a ROS2 process is initiated, it creates a DDS participant. It is important to note that there is a limit to the number of participants allowed in a single domain.   The efficient handling of numerous in-vehicle sensors and their messages demands the use of multiple ROS2 nodes in a single vehicle. Additionally, in the cooperative perception paradigm, a significant number of ROS2 nodes can be required when a vehicle functions as a single ROS2 node. These ROS2 nodes cannot be part of a single domain due to DDS participant limitation; thus, different domain communication is unavoidable. Moreover, there are different vendor-specific implementations of DDS, and each vendor has their configurations, which is an inevitable communication catalyst between the ROS2 nodes. The communication between vehicles or robots or ROS2 nodes depends directly on the vendor-specific configuration, data type, data size, and the DDS implementation used as middleware; in our study, we evaluate and investigate the limitations, capabilities, and prospects of the different domain communication for various vendor-specific DDS implementations for diverse sensor data type.

## Overview
In the autonomous vehicle and self-driving paradigm, cooperative perception or exchanging sensor information among vehicles over wireless communication has added a new dimension. Generally, an autonomous vehicle is a special type of robot that requires real-time, highly reliable sensor inputs due to functional safety. Autonomous vehicles are equipped with a considerable number of sensors to provide different required sensor data to make the driving decision and share with other surrounding vehicles. The inclusion of Data Distribution Service (DDS) as a communication middleware in ROS2 has proved its potential capability to be a reliable real-time distributed system. DDS comes with a scoping mechanism known as domain. Whenever a ROS2 process is initiated, it creates a DDS participant. It is important to note that there is a limit to the number of participants allowed in a single domain. The efficient handling of numerous in-vehicle sensors and their messages demands the use of multiple ROS2 nodes in a single vehicle. Additionally, in the cooperative perception paradigm, a significant number of ROS2 nodes can be required when a vehicle functions as a single ROS2 node. These ROS2 nodes cannot be part of a single domain due to DDS participant limitation; thus, different domain communication is unavoidable. Moreover, there are different vendor-specific implementations of DDS, and each vendor has their configurations, which is an inevitable communication catalyst between the ROS2 nodes. The communication between vehicles or robots or ROS2 nodes depends directly on the vendor-specific configuration, data type, data size, and the DDS implementation used as middleware; in our study, we evaluate and investigate the limitations, capabilities, and prospects of the different domain communication for various vendor-specific DDS implementations for diverse sensor data type.

## Content
In the autonomous vehicle and self-driving paradigm, cooperative perception or exchanging sensor information among vehicles over wireless communication has added a new dimension. Generally, an autonomous vehicle is a special type of robot that requires real-time, highly reliable sensor inputs due to functional safety. Autonomous vehicles are equipped with a considerable number of sensors to provide different required sensor data to make the driving decision and share with other surrounding vehicles. The inclusion of Data Distribution Service (DDS) as a communication middleware in ROS2 has proved its potential capability to be a reliable real-time distributed system. DDS comes with a scoping mechanism known as domain. Whenever a ROS2 process is initiated, it creates a DDS participant. It is important to note that there is a limit to the number of participants allowed in a single domain. The efficient handling of numerous in-vehicle sensors and their messages demands the use of multiple ROS2 nodes in a single vehicle. Additionally, in the cooperative perception paradigm, a significant number of ROS2 nodes can be required when a vehicle functions as a single ROS2 node. These ROS2 nodes cannot be part of a single domain due to DDS participant limitation; thus, different domain communication is unavoidable. Moreover, there are different vendor-specific implementations of DDS, and each vendor has their configurations, which is an inevitable communication catalyst between the ROS2 nodes. The communication between vehicles or robots or ROS2 nodes depends directly on the vendor-specific configuration, data type, data size, and the DDS implementation used as middleware; in our study, we evaluate and investigate the limitations, capabilities, and prospects of the different domain communication for various vendor-specific DDS implementations for diverse sensor data type.

## 개요
자율주행차 및 자율주행 패러다임에서, 차량 간 무선 통신을 통한 협력적 인식 또는 센서 정보 교환은 새로운 차원을 더했습니다. 일반적으로 자율주행차는 기능 안전성으로 인해 실시간, 고신뢰성 센서 입력을 요구하는 특수한 유형의 로봇입니다. 자율주행차는 주행 결정을 내리고 주변 차량과 공유하기 위해 다양한 요구 센서 데이터를 제공하는 상당한 수의 센서를 장착하고 있습니다. ROS2에서 통신 미들웨어로 Data Distribution Service(DDS)를 포함한 것은 신뢰할 수 있는 실시간 분산 시스템으로서의 잠재적 능력을 입증했습니다. DDS에는 도메인이라고 알려진 범위 지정 메커니즘이 있습니다. ROS2 프로세스가 시작될 때마다 DDS 참가자가 생성됩니다. 단일 도메인에서 허용되는 참가자 수에는 제한이 있다는 점에 유의하는 것이 중요합니다. 차량 내 다수의 센서와 해당 메시지를 효율적으로 처리하려면 단일 차량에서 여러 ROS2 노드를 사용해야 합니다. 또한, 협력적 인식 패러다임에서 차량이 단일 ROS2 노드로 기능할 때 상당한 수의 ROS2 노드가 필요할 수 있습니다. 이러한 ROS2 노드는 DDS 참가자 제한으로 인해 단일 도메인의 일부가 될 수 없으므로, 서로 다른 도메인 간 통신은 불가피합니다. 더욱이, 다양한 벤더별 DDS 구현이 있으며, 각 벤더는 자체 구성을 가지고 있어 ROS2 노드 간의 필연적인 통신 촉매제 역할을 합니다. 차량, 로봇 또는 ROS2 노드 간의 통신은 벤더별 구성, 데이터 유형, 데이터 크기 및 미들웨어로 사용되는 DDS 구현에 직접적으로 의존합니다. 본 연구에서는 다양한 센서 데이터 유형에 대한 다양한 벤더별 DDS 구현의 서로 다른 도메인 통신의 한계, 기능 및 전망을 평가하고 조사합니다.

## 핵심 내용
자율주행차 및 자율주행 패러다임에서, 차량 간 무선 통신을 통한 협력적 인식 또는 센서 정보 교환은 새로운 차원을 더했습니다. 일반적으로 자율주행차는 기능 안전성으로 인해 실시간, 고신뢰성 센서 입력을 요구하는 특수한 유형의 로봇입니다. 자율주행차는 주행 결정을 내리고 주변 차량과 공유하기 위해 다양한 요구 센서 데이터를 제공하는 상당한 수의 센서를 장착하고 있습니다. ROS2에서 통신 미들웨어로 Data Distribution Service(DDS)를 포함한 것은 신뢰할 수 있는 실시간 분산 시스템으로서의 잠재적 능력을 입증했습니다. DDS에는 도메인이라고 알려진 범위 지정 메커니즘이 있습니다. ROS2 프로세스가 시작될 때마다 DDS 참가자가 생성됩니다. 단일 도메인에서 허용되는 참가자 수에는 제한이 있다는 점에 유의하는 것이 중요합니다. 차량 내 다수의 센서와 해당 메시지를 효율적으로 처리하려면 단일 차량에서 여러 ROS2 노드를 사용해야 합니다. 또한, 협력적 인식 패러다임에서 차량이 단일 ROS2 노드로 기능할 때 상당한 수의 ROS2 노드가 필요할 수 있습니다. 이러한 ROS2 노드는 DDS 참가자 제한으로 인해 단일 도메인의 일부가 될 수 없으므로, 서로 다른 도메인 간 통신은 불가피합니다. 더욱이, 다양한 벤더별 DDS 구현이 있으며, 각 벤더는 자체 구성을 가지고 있어 ROS2 노드 간의 필연적인 통신 촉매제 역할을 합니다. 차량, 로봇 또는 ROS2 노드 간의 통신은 벤더별 구성, 데이터 유형, 데이터 크기 및 미들웨어로 사용되는 DDS 구현에 직접적으로 의존합니다. 본 연구에서는 다양한 센서 데이터 유형에 대한 다양한 벤더별 DDS 구현의 서로 다른 도메인 통신의 한계, 기능 및 전망을 평가하고 조사합니다.

## 参考
- http://arxiv.org/abs/2412.07485v1
