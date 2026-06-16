---
$id: "rel_mat_comp_neodymium_servo"
$schema: "../../schema/v1/relationship_schema.json"
$version: 1

type: "supplies"

source:
  id: "ent_mat_neodymium_magnet"
  name:
    en: "Neodymium-Iron-Boron Magnet"
    zh: "钕铁硼磁体"
    ko: "네오디뮴 철 붕자석"

target:
  id: "ent_comp_servo_motor"
  name:
    en: "High-Performance Servo Motor"
    zh: "高性能伺服电机"
    ko: "고성능 서보 모터"

domains:
  source_domain: "01_raw_materials"
  target_domain: "02_components"

description:
  en: "Neodymium-iron-boron magnets are a key input material for high-performance servo motors used in humanoid robot actuators."
  zh: "钕铁硼磁体是人形机器人执行器所用高性能伺服电机的关键输入材料。"
  ko: "네오디뮴 철 붕자석은 휨로봇 액추에이터에 사용되는 고성능 서보 모터의 핵심 입력 재료입니다."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-16"
  confidence: "high"
  notes: "Documented across motor teardowns, supplier specifications, and robotics actuator design literature."

sources:
  - id: "src_rel_001"
    type: "report"
    title: "Rare Earth Magnets in Robotics and EV Motors"
    url: "https://example.com/rare-earth-robotics-report"
    date: "2025-08-10"
    accessed_at: "2026-06-16"
---
