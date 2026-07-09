---
$id: ent_method_foc_motor_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  zh: 磁场定向控制(FOC)
  en: FOC
summary:
  zh: 磁场定向控制 的核心思想是把三相静止坐标系下的电流通过 Clark 变换 变到两相静止 \(\alpha\beta\) 坐标系，再通过 Park 变换 变到随转子旋转的 \(dq\) 坐标系，从而使交流量变成直流量，用 PI 控制器分别控制
    \(i_d\) 和 \(i_q\)
  en: 'FOC: 磁场定向控制 的核心思想是把三相静止坐标系下的电流通过 Clark 变换 变到两相静止 \(\alpha\beta\) 坐标系，再通过 Park 变换 变到随转子旋转的 \(dq\) 坐标系，从而使交流量变成直流量，用
    PI 控制器分别控制...'
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_4
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-09'
  confidence: medium
  notes: Extracted from Wiki chapter gap list; pending human verification.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
# 磁场定向控制(FOC)

磁场定向控制(FOC)是人形机器人产业链中的method相关知识节点。详见Wiki第4章《执行器：人形机器人的“肌肉”》。
