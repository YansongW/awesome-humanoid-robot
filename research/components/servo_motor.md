---
$id: "ent_comp_servo_motor"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "component"

names:
  en: "High-Performance Servo Motor"
  zh: "高性能伺服电机"
  ko: "고성능 서보 모터"

summary:
  en: "A compact electric motor with precise position, velocity, and torque control, used as the core actuator in humanoid robot joints."
  zh: "一种具有精确位置、速度和扭矩控制的紧凑型电机，用于人形机器人关节的核心执行器。"
  ko: "정밀한 위치, 속도 및 토크 제어가 가능한 소형 전동기로, 휨로봇 관절의 핵심 액추에이터로 사용됩니다."

domains:
  - "02_components"

layers:
  - "upstream"

functional_roles:
  - "component"

tags:
  - "motor"
  - "actuator"
  - "joint"
  - "torque_density"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-16"
  confidence: "high"
  notes: "Common component in humanoid robot teardowns and actuator design discussions."

sources:
  - id: "src_comp_001"
    type: "report"
    title: "Humanoid Robot Actuator Survey 2025"
    url: "https://example.com/actuator-survey-2025"
    date: "2025-12-01"
    accessed_at: "2026-06-16"

related_entities:
  - id: "ent_mat_neodymium_magnet"
    relationship: "consumes"
    description:
      en: "High-performance servo motors consume NdFeB permanent magnets."
      zh: "高性能伺服电机消耗钕铁硼永磁体。"
      ko: "고성능 서보 모터는 NdFeB 영구자석을 사용합니다."
---

# High-Performance Servo Motor

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像电动自行车的轮毂电机——体积不大，但能按照你的意图精确地输出力气、速度和位置，让车轮转到你想让它转到的角度。

> **自然语言逻辑**：高性能伺服电机是人形机器人关节的核心执行器，能把电能转化为精确可控的机械运动；它直接决定了机器人能走多快、抓多重、动作有多灵活，通常与减速器、编码器和控制器一起组成完整的关节模组。

Servo motors are the primary actuators in most humanoid robots. They convert electrical energy into precise mechanical motion, enabling walking, balancing, manipulation, and expressive movement.

## Key Metrics

- Torque density (Nm/kg)
- Peak torque and continuous torque
- Speed and bandwidth
- Efficiency and thermal performance
- Size and weight

## Integration

In humanoid robots, servo motors are typically combined with gearboxes or harmonic drives, encoders, and controllers to form complete actuator modules. The choice of motor directly constrains joint range, speed, force, and overall robot dynamics.

## Manufacturing Notes

Motor manufacturing involves precision winding, magnet insertion, rotor balancing, and assembly in clean, controlled environments. High-performance motors often use rare-earth magnets and specialized laminations to maximize torque density.
