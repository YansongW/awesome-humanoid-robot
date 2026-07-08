---
$id: ent_paper_wei_aero_adaptive_and_efficient_ru_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AERO: Adaptive and Efficient Runtime-Aware OTA Updates for Energy-Harvesting
    IoT'
  zh: AERO：面向能量收集物联网的自适应高效运行时感知空中固件更新
  ko: 'AERO: 에너지 수확 IoT를 위한 적응적이고 효율적인 런타임 인식 OTA 업데이트'
summary:
  en: AERO introduces a runtime-aware over-the-air update mechanism that models firmware
    update tasks as a directed acyclic graph and jointly schedules them with routine
    tasks under intermittent energy and timing constraints, aiming to improve update
    reliability and consistency in energy-harvesting IoT devices.
  zh: AERO提出了一种运行时感知的空中固件更新机制，将固件更新任务建模为有向无环图，并在间歇性能量与时间约束下和常规任务联合调度，以提高能量收集物联网设备的更新可靠性与一致性。
  ko: AERO는 런타임 인식 Over-The-Air 업데이트 메커니즘을 제안하여 펌웨어 업데이트 작업을 방향성 비순환 그래프로 모델링하고, 간헐적인
    에너지와 시간 제약 하에서 일상 작업과 공동으로 예약하여 에너지 수확 IoT 장치의 업데이트 신뢰성과 일관성을 향상시키고자 한다.
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
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; requires human review
    against the full paper text before final verification.
sources:
- id: src_001
  type: paper
  title: 'AERO: Adaptive and Efficient Runtime-Aware OTA Updates for Energy-Harvesting
    IoT'
  url: https://arxiv.org/abs/2601.16935
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

Energy-harvesting Internet of Things devices operate under intermittent power availability, which complicates long-running tasks and makes energy-intensive over-the-air firmware updates especially difficult. Conventional OTA mechanisms rely on rebooting the device, incurring substantial energy and time overhead that is poorly suited to intermittently powered systems. Recent live-update techniques reduce reboot overhead, but they generally lack explicit mechanisms to keep runtime execution consistent when an update is integrated while ordinary tasks are active.

This paper presents AERO, an Adaptive and Efficient Runtime-Aware OTA update mechanism. AERO treats the firmware as a directed acyclic graph of tasks and encodes incoming updates in a lightweight, dependency-driven packet format. It identifies mutually dependent update groups and the execution blocks affected by an update, dynamically adjusts the task DAG at runtime, and schedules update tasks together with routine tasks under both energy and deadline constraints. The goal is to ensure that updates are integrated consistently without requiring a full reboot, while adapting to the variable energy availability typical of harvesting environments.

The authors evaluate AERO on a TI MSP430FR5994 platform equipped with FRAM and a solar energy harvester, using workloads that include MiBench Quick Sort, AES encryption, LeNet-5, and a heart rate monitor application. The reported results indicate improved update reliability and efficiency relative to existing live-update approaches.

## Key Contributions

- A lightweight dependency-driven OTA packet format that encodes update tasks, routine dependencies, and update operations.
- A formal definition of mutually dependent update groups and update-affected blocks for analyzing the scope of a firmware update.
- A runtime DAG adjustment algorithm that integrates update tasks with routine tasks while preserving execution consistency.
- A unified scheduling method that schedules update and routine tasks together under intermittent energy availability and task deadlines.

## Relevance to Humanoid Robotics

Although AERO targets energy-harvesting IoT devices rather than humanoid robots directly, its runtime-aware, energy-adaptive scheduling and consistent live-update techniques are relevant to the low-power embedded subsystems and sensor networks that often appear in humanoid platforms. Humanoid robots typically contain numerous distributed microcontrollers, motor controllers, and sensor nodes that may need firmware updates without shutting down the entire system. AERO's approach of modeling updates as DAG tasks and scheduling them jointly with normal operations under energy constraints could inform the design of update mechanisms for these subsystems, particularly in scenarios where power budgets are tight or energy is harvested.
