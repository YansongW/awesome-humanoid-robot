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
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#4.5.2 磁场定向控制（FOC）的数学结构 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
磁场定向控制（FOC）是人形机器人领域的重要method。以下内容整理自项目 Wiki，供深入查阅。

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
- Wiki extraction
- 项目 Wiki：chapter-04.md#4.5.2 磁场定向控制（FOC）的数学结构

