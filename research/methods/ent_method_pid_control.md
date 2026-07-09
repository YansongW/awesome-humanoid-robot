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
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-09'
  confidence: high
  notes: Standard control theory; PID is universally used in motor drives and robot joint control.
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
# PID Control / PID控制 / PID 제어

## 抽象

> **生活实例**：开车时若方向偏左，人会小幅回正（比例）、若长期偏离则持续修正（积分）、若偏离速度过快则提前反向打盘（微分）。PID 就是这三种修正的数学化。
>
> **自然语言逻辑**：给定目标值与实际值的误差 $e(t)$，控制器输出 $u(t)$ 由误差本身、误差的积分（累积误差）、误差的微分（变化趋势）加权相加得到。

## 形式化定义

$$u(t) = K_p e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt},$$

其中 $K_p, K_i, K_d$ 分别为比例、积分、微分增益。离散实现时常用位置式或增量式 PID。

## 关键参数直觉

| 参数 | 作用 | 过大的后果 |
|------|------|-----------|
| $K_p$ | 按当前误差快速响应 | 振荡、超调 |
| $K_i$ | 消除稳态误差 | 积分饱和、响应迟缓 |
| $K_d$ | 抑制快速变化、预测趋势 | 对噪声敏感 |

## 与其他知识点的关系

- `requires` → 反馈控制理论 / 误差信号
- `complements` → [ent_method_impedance_control]
- `implemented_on` → 伺服驱动器 / 机器人关节
