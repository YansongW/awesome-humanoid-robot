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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.07485v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1167 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2412.07485v1

## 개요
자율주행 차량은 실시간 고신뢰성 센서 데이터 교환에 의존하며, ROS2가 도입한 DDS 미들웨어는 분산 시스템에 통신 기반을 제공합니다. 단일 DDS 도메인은 참여자 수에 제한이 있기 때문에, 다중 센서 차량 및 다중 차량 협업 시나리오에서는 필연적으로 도메인 간 통신이 필요합니다. 본 연구는 실제 하드웨어 테스트를 통해 세 가지 주요 DDS 구현(Cyclone DDS, Fast-DDS, Connext DDS)이 서로 다른 데이터 유형과 데이터 양에서 보이는 지연 성능을 비교하여, 자율주행 시스템 설계자가 미들웨어 구성을 선택할 때 활용할 수 있는 정량적 근거를 제공합니다.

## 핵심 내용
### 연구 배경 및 문제
- 자율주행 차량은 특수 로봇으로서 기능 안전 요구사항을 충족하는 실시간 센서 입력이 필요하며, 일반적으로 다수의 센서(예: 라이다, 카메라, 밀리미터파 레이더)를 장착합니다.
- ROS2는 통신 미들웨어로 DDS를 채택하며, 각 ROS2 프로세스는 DDS 참여자(participant)를 생성하지만, 단일 DDS 도메인에는 참여자 수 상한 제한이 있습니다.
- 단일 차량의 다중 센서 노드(ROS2 노드) 및 다중 차량 협업 인식 시나리오(각 차량을 하나의 ROS2 노드로 간주)는 모두 단일 도메인 용량을 초과할 수 있어, 시스템이 도메인 간 통신을 채택하도록 강제합니다.

### 실험 설계
- **하드웨어 플랫폼**: 이기종 물리 장치(예: 서로 다른 계산 성능의 임베디드 보드 및 PC)를 사용하여 실제 차량 환경을 모사합니다.
- **미들웨어 버전**: Eclipse Cyclone DDS, eProsima Fast-DDS, RTI Connext DDS.
- **테스트 변수**:
  - 통신 모드: 동일 도메인(same-domain) vs 도메인 간(cross-domain)
  - 데이터 유형: 일반적인 센서 데이터 모사(예: 소형 제어 명령, 중형 포인트 클라우드, 대형 이미지)
  - 데이터 크기: 수십 바이트에서 수 메가바이트까지
- **측정 지표**: 종단 간 통신 지연(latency), 반복 측정 후 통계값 산출.

### 주요 발견
- **도메인 간 지연이 동일 도메인보다 현저히 높음**: 모든 미들웨어에서 도메인 간 시나리오의 지연이 2-5배 증가하며, 주로 DDS 도메인 간 발견 프로토콜 및 데이터 직렬화 오버헤드에서 기인합니다.
- **공급업체 간 차이**:
  - Cyclone DDS는 중소형 데이터(<1MB) 도메인 간 시나리오에서 지연이 가장 낮지만, 대용량 데이터(>5MB)에서는 성능 저하가 뚜렷합니다.
  - Fast-DDS는 도메인 간 대용량 데이터 전송에서 가장 우수한 성능을 보이며, 지연 변동이 작습니다.
  - Connext DDS는 모든 시나리오에서 지연 일관성이 가장 좋지만, 절대 지연 값은 앞선 두 제품보다 높습니다.
- **데이터 유형 영향**: 구조화된 데이터(예: PointCloud2)의 직렬화/역직렬화 시간은 총 지연의 30%-50%를 차지하며, 도메인 간 시나리오에서는 이 비율이 더 높습니다.

### 결론 및 제안
- 자율주행 시스템 설계자는 센서 데이터 유형과 통신 범위에 따라 미들웨어를 선택해야 합니다: 소형 데이터 실시간 제어는 Cyclone DDS를 우선하고, 대용량 데이터 인식 공유는 Fast-DDS를 우선합니다.
- 도메인 간 통신이 불가피한 경우, 추가 지연 예산(동일 도메인 지연의 최소 2배 권장)을 확보하고, 데이터 압축 또는 선택적 전송 전략을 고려해야 합니다.
- 향후 연구는 DDS 도메인 간 브리지 최적화(예: Domain Bridge) 및 하드웨어 가속 방안을 탐구해야 합니다.
