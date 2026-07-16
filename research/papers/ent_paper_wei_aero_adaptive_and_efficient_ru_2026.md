---
$id: ent_paper_wei_aero_adaptive_and_efficient_ru_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AERO: Adaptive and Efficient Runtime-Aware OTA Updates for Energy-Harvesting IoT'
  zh: AERO：面向能量收集物联网的自适应高效运行时感知空中固件更新
  ko: 'AERO: 에너지 수확 IoT를 위한 적응적이고 효율적인 런타임 인식 OTA 업데이트'
summary:
  en: AERO introduces a runtime-aware over-the-air update mechanism that models firmware update tasks as a directed acyclic
    graph and jointly schedules them with routine tasks under intermittent energy and timing constraints, aiming to improve
    update reliability and consistency in energy-harvesting IoT devices.
  zh: AERO提出了一种运行时感知的空中固件更新机制，将固件更新任务建模为有向无环图，并在间歇性能量与时间约束下和常规任务联合调度，以提高能量收集物联网设备的更新可靠性与一致性。
  ko: AERO는 런타임 인식 Over-The-Air 업데이트 메커니즘을 제안하여 펌웨어 업데이트 작업을 방향성 비순환 그래프로 모델링하고, 간헐적인 에너지와 시간 제약 하에서 일상 작업과 공동으로 예약하여 에너지
    수확 IoT 장치의 업데이트 신뢰성과 일관성을 향상시키고자 한다.
domains:
- 08_software_middleware
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- system
tags:
- ota_update
- runtime_update
- dag_scheduling
- energy_harvesting
- intermittent_power
- embedded_systems
- firmware_update
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.16935v1.
sources:
- id: src_001
  type: paper
  title: 'AERO: Adaptive and Efficient Runtime-Aware OTA Updates for Energy-Harvesting IoT'
  url: https://arxiv.org/abs/2601.16935
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
Energy-harvesting (EH) Internet of Things (IoT) devices operate under intermittent energy availability, which disrupts task execution and makes energy-intensive over-the-air (OTA) updates particularly challenging. Conventional OTA update mechanisms rely on reboots and incur significant overhead, rendering them unsuitable for intermittently powered systems. Recent live OTA update techniques reduce reboot overhead but still lack mechanisms to ensure consistency when updates interact with runtime execution. This paper presents AERO, an Adaptive and Efficient Runtime-Aware OTA update mechanism that integrates update tasks into the device's Directed Acyclic Graph (DAG) and schedules them alongside routine tasks under energy and timing constraints. By identifying update-affected execution regions and dynamically adjusting dependencies, AERO ensures consistent up date integration while adapting to intermittent energy availability. Experiments on representative workloads demonstrate improved update reliability and efficiency compared to existing live update approaches.

## 核心内容
Energy-harvesting (EH) Internet of Things (IoT) devices operate under intermittent energy availability, which disrupts task execution and makes energy-intensive over-the-air (OTA) updates particularly challenging. Conventional OTA update mechanisms rely on reboots and incur significant overhead, rendering them unsuitable for intermittently powered systems. Recent live OTA update techniques reduce reboot overhead but still lack mechanisms to ensure consistency when updates interact with runtime execution. This paper presents AERO, an Adaptive and Efficient Runtime-Aware OTA update mechanism that integrates update tasks into the device's Directed Acyclic Graph (DAG) and schedules them alongside routine tasks under energy and timing constraints. By identifying update-affected execution regions and dynamically adjusting dependencies, AERO ensures consistent up date integration while adapting to intermittent energy availability. Experiments on representative workloads demonstrate improved update reliability and efficiency compared to existing live update approaches.

## 参考
- http://arxiv.org/abs/2601.16935v1

## Overview
Energy-harvesting (EH) Internet of Things (IoT) devices operate under intermittent energy availability, which disrupts task execution and makes energy-intensive over-the-air (OTA) updates particularly challenging. Conventional OTA update mechanisms rely on reboots and incur significant overhead, rendering them unsuitable for intermittently powered systems. Recent live OTA update techniques reduce reboot overhead but still lack mechanisms to ensure consistency when updates interact with runtime execution. This paper presents AERO, an Adaptive and Efficient Runtime-Aware OTA update mechanism that integrates update tasks into the device's Directed Acyclic Graph (DAG) and schedules them alongside routine tasks under energy and timing constraints. By identifying update-affected execution regions and dynamically adjusting dependencies, AERO ensures consistent update integration while adapting to intermittent energy availability. Experiments on representative workloads demonstrate improved update reliability and efficiency compared to existing live update approaches.

## Content
Energy-harvesting (EH) Internet of Things (IoT) devices operate under intermittent energy availability, which disrupts task execution and makes energy-intensive over-the-air (OTA) updates particularly challenging. Conventional OTA update mechanisms rely on reboots and incur significant overhead, rendering them unsuitable for intermittently powered systems. Recent live OTA update techniques reduce reboot overhead but still lack mechanisms to ensure consistency when updates interact with runtime execution. This paper presents AERO, an Adaptive and Efficient Runtime-Aware OTA update mechanism that integrates update tasks into the device's Directed Acyclic Graph (DAG) and schedules them alongside routine tasks under energy and timing constraints. By identifying update-affected execution regions and dynamically adjusting dependencies, AERO ensures consistent update integration while adapting to intermittent energy availability. Experiments on representative workloads demonstrate improved update reliability and efficiency compared to existing live update approaches.

## 개요
에너지 하베스팅(EH) 사물인터넷(IoT) 장치는 간헐적인 에너지 가용성 하에서 작동하며, 이는 작업 실행을 방해하고 에너지 집약적인 무선(OTA) 업데이트를 특히 어렵게 만듭니다. 기존의 OTA 업데이트 메커니즘은 재부팅에 의존하며 상당한 오버헤드를 발생시켜 간헐적 전원 시스템에 부적합합니다. 최근의 라이브 OTA 업데이트 기술은 재부팅 오버헤드를 줄이지만, 업데이트가 런타임 실행과 상호작용할 때 일관성을 보장하는 메커니즘이 여전히 부족합니다. 본 논문에서는 AERO(Adaptive and Efficient Runtime-Aware OTA update mechanism)를 제안합니다. 이는 업데이트 작업을 장치의 방향성 비순환 그래프(DAG)에 통합하고, 에너지 및 시간 제약 조건 하에서 일상 작업과 함께 스케줄링합니다. 업데이트에 영향을 받는 실행 영역을 식별하고 종속성을 동적으로 조정함으로써, AERO는 간헐적인 에너지 가용성에 적응하면서 일관된 업데이트 통합을 보장합니다. 대표적인 워크로드에 대한 실험 결과, 기존 라이브 업데이트 방식에 비해 업데이트 신뢰성과 효율성이 향상되었음을 보여줍니다.

## 핵심 내용
에너지 하베스팅(EH) 사물인터넷(IoT) 장치는 간헐적인 에너지 가용성 하에서 작동하며, 이는 작업 실행을 방해하고 에너지 집약적인 무선(OTA) 업데이트를 특히 어렵게 만듭니다. 기존의 OTA 업데이트 메커니즘은 재부팅에 의존하며 상당한 오버헤드를 발생시켜 간헐적 전원 시스템에 부적합합니다. 최근의 라이브 OTA 업데이트 기술은 재부팅 오버헤드를 줄이지만, 업데이트가 런타임 실행과 상호작용할 때 일관성을 보장하는 메커니즘이 여전히 부족합니다. 본 논문에서는 AERO(Adaptive and Efficient Runtime-Aware OTA update mechanism)를 제안합니다. 이는 업데이트 작업을 장치의 방향성 비순환 그래프(DAG)에 통합하고, 에너지 및 시간 제약 조건 하에서 일상 작업과 함께 스케줄링합니다. 업데이트에 영향을 받는 실행 영역을 식별하고 종속성을 동적으로 조정함으로써, AERO는 간헐적인 에너지 가용성에 적응하면서 일관된 업데이트 통합을 보장합니다. 대표적인 워크로드에 대한 실험 결과, 기존 라이브 업데이트 방식에 비해 업데이트 신뢰성과 효율성이 향상되었음을 보여줍니다.
