---
$id: rel_ent_robot_system_inmoov_uses_ent_comp_servo_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_inmoov
  name:
    en: InMoov
    zh: InMoov 3D 打印人形机器人
target:
  id: ent_comp_servo_motor
  name:
    en: High-Performance Servo Motor
    zh: 高性能伺服电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: InMoov is actuated by standard hobby servos (community-common models such as MG996R and HS-805BB),
    with no custom actuators.
  zh: InMoov 由标准航模舵机驱动（社区常用型号 MG996R、HS-805BB 等），无定制执行器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/inmoov.md 确认标准航模舵机方案；目标实体为知识图谱舵机通用条目，InMoov 所用具体型号为社区选型而非官方指定。
sources:
- id: src_001
  type: website
  title: InMoov Official Project Page
  url: https://inmoov.fr/project/
  accessed_at: '2026-07-01'
---
