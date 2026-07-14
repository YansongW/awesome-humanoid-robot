---
$id: ent_method_field_oriented_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Field-Oriented Control
  zh: 磁场定向控制
  ko: 전계 지향 제어
summary:
  en: A motor control technique that transforms three-phase stator currents into a rotating d-q reference frame aligned with
    the rotor flux, enabling independent torque and flux control.
  zh: 一种电机控制技术，将三相定子电流变换到与转子磁链对齐的旋转 d-q 坐标系，实现转矩与磁链的解耦控制。
  ko: 3상 정자 전류를 회전자 자속에 맞춘 d-q 좌표계로 변환하여 토크와 자속을 독립적으로 제어하는 모터 제어 기법.
domains:
- 02_components
- 07_ai_models_algorithms
layers:
- upstream
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- motor
- pmsm
- bldc
- servo
- current_control
- actuator
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-04.md#4.5.2 磁场定向控制（FOC）的数学结构 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_mohan_2003
  type: other
  title: 'N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013'
  url: https://doi.org/10.1002/9781118704810
  date: '2013-01-01'
  accessed_at: '2026-07-09'
- id: src_krause_wasynczuk_sudhoff_2013
  type: other
  title: P. C. Krause, O. Wasynczuk, and S. D. Sudhoff, Analysis of Electric Machinery and Drive Systems, 3rd ed., IEEE Press/Wiley,
    2013
  url: https://doi.org/10.1002/9781118526030
  date: '2013-01-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_component_rotary_actuator_2024
  relationship: applies_to
  description:
    en: FOC is widely used inside rotary actuator servo drives for PMSM/BLDC motors in humanoid joints.
    zh: FOC 广泛用于人形机器人关节旋转执行器中的 PMSM/BLDC 伺服驱动。
- id: ent_method_pid_control
  relationship: requires
  description:
    en: FOC typically uses PI/PID current controllers in the d-q frame to regulate flux and torque currents.
    zh: FOC 通常在 d-q 坐标系中使用 PI/PID 电流控制器调节磁链电流与转矩电流。
---
## 概述
磁场定向控制是人形机器人领域的重要method。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
FOC 使 PMSM 的转矩控制解耦为对 \(i_d\) 和 \(i_q\) 的独立控制。在旋转 \(dq\) 坐标系中，定子电压方程为

$$
\begin{aligned}
v_d &= R_s i_d + L_d \frac{di_d}{dt} - \omega_e L_q i_q \\
v_q &= R_s i_q + L_q \frac{di_q}{dt} + \omega_e L_d i_d + \omega_e \lambda_f
\end{aligned}
$$

其中 \(R_s\) 为定子电阻，\(L_d\)、\(L_q\) 为 \(d\)、\(q\) 轴电感，\(\omega_e\) 为电角速度，\(\lambda_f\) 为永磁磁链。

## 参考
- [N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013](https://doi.org/10.1002/9781118704810)
- [P. C. Krause, O. Wasynczuk, and S. D. Sudhoff, Analysis of Electric Machinery and Drive Systems, 3rd ed., IEEE Press/Wiley, 2013](https://doi.org/10.1002/9781118526030)
- 项目 Wiki：chapter-04.md#4.5.2 磁场定向控制（FOC）的数学结构

