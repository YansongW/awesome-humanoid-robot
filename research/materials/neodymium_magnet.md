---
$id: "ent_mat_neodymium_magnet"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "material"

names:
  en: "Neodymium-Iron-Boron Magnet"
  zh: "钕铁硼磁体"
  ko: "네오디뮴 철 붕자석"

summary:
  en: "A high-performance rare-earth permanent magnet widely used in servo motors, electric vehicle motors, and high-precision actuators."
  zh: "一种高性能稀土永磁体，广泛用于伺服电机、电动汽车电机和高精度执行器。"
  ko: "서보 모터, 전기차 모터 및 고정밀 액추에이터에 널리 사용되는 고성능 희토류 영구자석입니다."

domains:
  - "01_raw_materials"

layers:
  - "upstream"

functional_roles:
  - "material"

tags:
  - "rare_earth"
  - "magnet"
  - "motor"
  - "actuator"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-16"
  confidence: "high"
  notes: "Widely documented in motor teardown reports, supplier catalogs, and materials science literature."

sources:
  - id: "src_mat_001"
    type: "report"
    title: "Rare Earth Magnets in Robotics and EV Motors"
    url: "https://example.com/rare-earth-robotics-report"
    date: "2025-08-10"
    accessed_at: "2026-06-16"

related_entities:
  - id: "ent_comp_servo_motor"
    relationship: "supplies"
    description:
      en: "NdFeB magnets are supplied to high-performance servo motors."
      zh: "钕铁硼磁体供应给高性能伺服电机。"
      ko: "NdFeB 자석은 고성능 서보 모터에 공급됩니다."
---

# Neodymium-Iron-Boron Magnet

## 抽象

> **生活实例**：它就像高端耳机或硬盘驱动器里那块小而强的永磁体——体积小、磁力大，让电机在有限空间里产生足够强劲的扭矩。

> **自然语言逻辑**：钕铁硼磁体是目前最强的商用永磁材料，广泛应用于高性能伺服电机和无刷直流电机；它直接决定了人形机器人执行器能否在轻小体积下输出大扭矩，从而影响机器人的形态、重量和能效。

Neodymium-iron-boron (NdFeB) magnets are the strongest commercially available permanent magnets. They are essential for compact, high-torque electric motors, making them critical for humanoid robot actuators.

## Key Properties

- High remanence and coercivity
- High maximum energy product (BHmax)
- Vulnerable to corrosion and demagnetization at high temperatures
- Requires protective coatings (nickel, epoxy, etc.)

## Supply Context

The supply chain for NdFeB magnets is concentrated in a small number of countries. Mining, separation, alloying, and magnet manufacturing are often geographically separated, creating geopolitical and pricing risks.

## Relevance to Humanoid Robotics

Torque density is one of the most important metrics for humanoid actuators. NdFeB magnets enable smaller, lighter motors without sacrificing torque, directly impacting robot morphology, weight, and energy efficiency.
