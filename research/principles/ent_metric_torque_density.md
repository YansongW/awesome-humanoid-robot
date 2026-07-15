---
$id: ent_metric_torque_density
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Torque Density
  zh: 转矩密度
  ko: 토크 밀도
summary:
  en: The ratio of continuous output torque to actuator mass or volume, a key figure of merit for compact, high-performance
    humanoid joints.
  zh: 1. **扭矩密度** \(\tau_d = \tau_{\text{peak}} / m\)（单位：N·m/kg）或 N·m/L，衡量单位质量/体积能产生多大扭矩。 2. **功率密度** \(P_d = P_{\text{peak}}
    / m\)（单位：W/kg），衡量单位质量能输出多大机械功率。
  ko: 액추에이터 질량·부피 대비 연속 출력 토크 비율로, 휴로봇 관절의 소형·고성능을 평가하는 핵심 지표.
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- concept
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
### 4.1.2 功率密度、扭矩密度与动态响应

## 核心内容
把执行器看作一个能量转换装置，其核心指标可归结为两点：

1. **扭矩密度** \(\tau_d = \tau_{\text{peak}} / m\)（单位：N·m/kg）或 N·m/L，衡量单位质量/体积能产生多大扭矩。
2. **功率密度** \(P_d = P_{\text{peak}} / m\)（单位：W/kg），衡量单位质量能输出多大机械功率。

二者通过电机转速关联：

$$
P = \tau \, \omega
$$

其中 \(\omega\) 为角速度（rad/s）。电机本体通常在高转速、低扭矩区运行效率最高；机器人关节需要低转速、高扭矩，因此必须借助减速器进行"扭矩放大"。这一匹配是本章后续讨论的核心。

机器人动态响应还可用 **机械时间常数** 描述：

$$
\tau_m = \frac{J \, R}{k_t^2}
$$

其中 \(J\) 为转子与负载的等效转动惯量，\(R\) 为电枢电阻，\(k_t\) 为转矩常数。时间常数越小，电机加减速越快。

!!! note "术语解释：转动惯量、机械时间常数、转矩常数"
    - **转动惯量（moment of inertia）**：物体抵抗角加速度的能力，类比平动中的质量。离转轴越远、质量越大，转动惯量越大。单位 kg·m²。
    - **机械时间常数（mechanical time constant）**：电机从静止加速到约 63% 稳态转速所需的时间，反映机械响应快慢。
    - **转矩常数（torque constant）**：电机电流与产生转矩之间的比例系数 \(\tau = k_t I\)。单位 N·m/A，其大小取决于磁场强度与绕组有效长度。

```mermaid
flowchart LR
    A["任务需求<br/>力矩 速度 带宽"] --> B["电机本体<br/>高速低扭"]
    B --> C["传动机构<br/>减速增扭"]
    C --> D["关节输出<br/>低速高扭"]
    E["质量/体积约束"] --> B
    E --> C
    F["热与续航"] --> G["效率与损耗"]
    G --> B
    G --> C
```

## 参考
- Wiki extraction


