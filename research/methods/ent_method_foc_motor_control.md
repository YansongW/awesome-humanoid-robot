---
$id: ent_method_foc_motor_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Field-Oriented Control (FOC)
  zh: 磁场定向控制（FOC）
  ko: 자장 지향 제어(FOC)
summary:
  en: A motor-control method that transforms three-phase currents into a rotating dq reference frame to enable independent
    control of torque and flux, similar to a DC machine.
  zh: 将三相电流变换到旋转的dq坐标系，分别控制转矩与磁通，使交流电机获得类似直流电机的调速性能。
  ko: 삼상 전류를 회전하는 dq 좌표계로 변환하여 토크와 자속을 독립 제어하는 모터 제어 방식.
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
