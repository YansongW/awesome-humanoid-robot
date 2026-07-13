---
$id: ent_method_pid_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: PID Control
  zh: PID控制
  ko: PID 제어
summary:
  en: A foundational feedback control method that computes a control signal as a linear combination of proportional, integral,
    and derivative terms of the tracking error.
  zh: 一种基础反馈控制方法，将控制量表示为跟踪误差的比例、积分、微分三项线性组合。
  ko: 추적 오차의 비례·적분·미분 항의 선형 조합으로 제어 신호를 계산하는 기초 피드백 제어 방법.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- control
- feedback
- joint_control
- actuator
- classical_control
- wiki_gap
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko.
sources:
- id: src_astrom_hagglund_2006
  type: other
  title: K. J. Åström and T. Hägglund, Advanced PID Control, ISA, 2006
  url: https://www.ieeectl.org/awards/astrom-hagglund-advanced-pid-control/
  date: '2006-01-01'
  accessed_at: '2026-07-09'
- id: src_ogata_2010
  type: other
  title: K. Ogata, Modern Control Engineering, 5th ed., Prentice Hall, 2010
  url: https://doi.org/10.1002/9780470544162
  date: '2010-01-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_method_impedance_control
  relationship: mentions
  description:
    en: PID control regulates position or velocity; impedance control extends this to regulate dynamic interaction forces
      with the environment.
    zh: PID 控制调节位置或速度；阻抗控制进一步调节与环境的动态交互力。
---
