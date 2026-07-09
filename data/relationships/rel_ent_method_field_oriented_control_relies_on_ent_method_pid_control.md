---
$id: rel_ent_method_field_oriented_control_relies_on_ent_method_pid_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: relies_on
source:
  id: ent_method_field_oriented_control
  name:
    en: Field-Oriented Control
    zh: 磁场定向控制
target:
  id: ent_method_pid_control
  name:
    en: PID Control
    zh: PID控制
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: FOC typically uses PI/PID current controllers in the d-q frame to regulate flux and torque currents.
  zh: FOC 通常在 d-q 坐标系中使用 PI/PID 电流控制器调节磁链电流与转矩电流。
verification:
  status: pending
  reviewed_by: ai
  reviewed_at: '2026-07-09'
  confidence: medium
  notes: Standard industrial practice; specific tuning details need verification.
sources:
- id: src_mohan_2003
  type: other
  title: "N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013"
  url: https://doi.org/10.1002/9781118704810
  date: '2013-01-01'
  accessed_at: '2026-07-09'
---
