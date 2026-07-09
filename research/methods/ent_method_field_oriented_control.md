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
  en: A motor control technique that transforms three-phase stator currents into a rotating d-q reference frame aligned with the rotor flux, enabling independent torque and flux control.
  zh: 一种电机控制技术，将三相定子电流变换到与转子磁链对齐的旋转 d-q 坐标系，实现转矩与磁链的解耦控制。
  ko: 3상 정자 전류를 회전자 자속에 맞춘 d-q 좌표계로 변환하여 토크와 자속을 독립적으로 제어하는 모터 제어 기법.
domains:
- 02_components
- 07_ai_models_algorithms
layers:
- method
functional_roles:
- control
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
  status: pending
  reviewed_by: ai
  reviewed_at: '2026-07-09'
  confidence: medium
  notes: Standard motor-control concept; specific drive implementations and notation need manual verification.
sources:
- id: src_mohan_2003
  type: other
  title: "N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013"
  url: https://doi.org/10.1002/9781118704810
  date: '2013-01-01'
  accessed_at: '2026-07-09'
- id: src_krause_wasynczuk_sudhoff_2013
  type: other
  title: "P. C. Krause, O. Wasynczuk, and S. D. Sudhoff, Analysis of Electric Machinery and Drive Systems, 3rd ed., IEEE Press/Wiley, 2013"
  url: https://doi.org/10.1002/9781118526030
  date: '2013-01-01'
  accessed_at: '2026-07-09'
wiki_chapters:
- number: 4
  title: 第 4 章 执行器：人形机器人的“肌肉”
related_entities:
- id: ent_component_rotary_actuator_2024
  relationship: used_in
  description:
    en: FOC is widely used inside rotary actuator servo drives for PMSM/BLDC motors in humanoid joints.
    zh: FOC 广泛用于人形机器人关节旋转执行器中的 PMSM/BLDC 伺服驱动。
- id: ent_method_pid_control
  relationship: relies_on
  description:
    en: FOC typically uses PI/PID current controllers in the d-q frame to regulate flux and torque currents.
    zh: FOC 通常在 d-q 坐标系中使用 PI/PID 电流控制器调节磁链电流与转矩电流。
---

# Field-Oriented Control / 磁场定向控制 / 전계 지향 제어

## 抽象

> **生活实例**：骑旋转木马时，如果你始终面向木马中心旋转，复杂的三维晃动就被简化成“前后”和“左右”两个独立运动。FOC 就是把电机内部复杂的三相电流，变换到随转子一起转的坐标系里，让控制变得简单。
>
> **自然语言逻辑**：交流电机（PMSM/BLDC）的三相电流随时间正弦变化，直接控制困难。Clarke 变换把三相电流变到两相静止坐标系，Park 变换再变到与转子磁链同步旋转的 d-q 坐标系；在 d-q 系中电流分量分别对应磁链和转矩，可独立用 PI 控制。

## 关键变换

- **Clarke 变换**：$abc \rightarrow \alpha\beta$（三相到两相静止）
- **Park 变换**：$\alpha\beta \rightarrow dq$（静止到旋转坐标系）

在 d-q 坐标系下：

- $i_d$：直轴电流，主要影响磁链；
- $i_q$：交轴电流，主要产生电磁转矩；
- 典型策略令 $i_d = 0$，则转矩与 $i_q$ 成正比。

## 与其他知识点的关系

- `relies_on` → [ent_method_pid_control]
- `used_in` → [ent_component_rotary_actuator_2024]
- `requires` → Clarke/Park 变换 / 电机模型
