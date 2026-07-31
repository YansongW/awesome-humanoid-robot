---
$id: rel_ent_robot_system_berkeley_humanoid_lite_mentions_ent_method_foc_motor_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_robot_system_berkeley_humanoid_lite
  name:
    en: Berkeley Humanoid Lite
    zh: 伯克利轻量人形机器人
target:
  id: ent_method_foc_motor_control
  name:
    en: Field-Oriented Control (FOC)
    zh: 磁场定向控制（FOC）
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Berkeley Humanoid Lite mentions Field-Oriented Control (FOC).
  zh: 伯克利轻量人形机器人提及磁场定向控制（FOC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - 门槛：需要自己打印摆线减速器并装配 22 台执行器、焊接 CAN 总线、烧录 FOC
    固件，嵌入式与 3D 打印经验不足者容易卡壳；16 kg 机型已需要一定的操作安全意识；非零基础友好。'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_system_berkeley_humanoid_lite
  url: https://kg.rounds-tech.com/entry/ent_robot_system_berkeley_humanoid_lite/
  accessed_at: '2026-07-31'
---
