---
$id: ent_component_joint_motor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Joint Motor
  zh: 关节电机
  ko: Joint Motor
summary:
  en: Compact motor integrated into a robot joint, often paired with a reducer and encoder to form an actuator module.
  zh: '- 输出峰值扭矩：\(\tau_{peak} = 120\ \text{N·m}\) - 输出连续 RMS 转矩：\(\tau_{rms} = 35\ \text{N·m}\) - 输出最大角速度：\(\omega_{out,max}
    = 8\ \text{rad/s}\) - 减速器效率：\(\eta = 0.85\)'
  ko: 로봇 관절에 통합된 컴팩트한 모터, 일반적으로 감속기 및 인코더와 짝을 이루어 액추에이터 모듈을 형성.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- actuator
- component
- integrated
- joint_motor
- motor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Body backfilled from chapter-04.md#4.7.6 选型算例：髋关节电机+减速器 by scripts/backfill_nonpaper_entries.py. | WP4 trilingual
    backfill 2026-08-10: closed unclosed code fence(s) and removed duplicate stale translation block(s) (pre-existing ingestion
    defect).  [2026-08-12] body upgraded to textbook-grade (.staging/textbook_grade_run/b2_b2): zh 概述/核心内容/参考 rewritten from
    card + graph neighbors + wiki chapters + first-hand sources (number whitelist audit passed); en/ko sections to be regenerated
    by translate pipeline.'
sources:
- id: src_001
  type: website
  title: Joint Motor
  url: https://en.wikipedia.org/wiki/Servomotor
  date: '2024'
  accessed_at: '2026-07-02'
---
## 概述

关节电机（Joint Motor）是人形机器人旋转执行器的核心动力源，通常由无框力矩电机与减速器一体化集成，输出峰值扭矩可达 120 N·m、连续 RMS 转矩 35 N·m、最大角速度 8 rad/s。它真正改变的不是电机本身，而是"电机—减速器—编码器—驱动器"的集成方式——将动力、传动与感知封装为一个可直接装入关节的机电单元。

## 核心内容

### 是什么：准确定义

关节电机是安装在机器人关节处、直接驱动连杆相对运动的电机组件。在人形机器人产业链中，它属于 `component`（零部件）类型，价值链层级为上游（upstream），领域编码为 `02_components`。与普通工业电机不同，关节电机的设计约束来自机器人本体：峰值扭矩密度、连续热管理能力、背隙、透明度（backdrivability）以及轴向尺寸，而非单纯的额定功率。

关节电机通常采用**无框力矩电机（frameless torque motor）**形态——只有定子与转子，无外壳、无轴承、无编码器，这些部件由关节结构件、交叉滚子轴承和编码器分别承担。电机转子直接或经减速器耦合到输出法兰，形成"关节电机 + 减速器 + 编码器 + 驱动器"的集成执行器（integrated actuator）。这种形态在 Tesla Optimus、Unitree H1 等整机中均有应用（工程判断，基于语料中实体关系示例）。

### 为什么存在：痛点与历史定位

在关节电机成为标准方案之前，机器人关节设计面临一个根本矛盾：**电机的高转速低扭矩特性与关节的低转速高扭矩需求不匹配**。直接驱动（direct drive）虽然消除了减速器的背隙与摩擦，但要求电机极低速大扭矩，导致电机体积与重量急剧膨胀，不适合 60 kg 级人形机器人的髋关节等大扭矩关节。

谐波减速器与行星减速器的成熟，使"高转速小电机 + 大减速比"成为可能。但减速比并非越大越好：减速比增大虽提升输出扭矩，却同时降低输出速度上限、增加反射惯量与背隙，并恶化透明度——即外力反向驱动关节时的顺滑程度。关节电机的设计本质是在**扭矩、速度、透明度、热管理**四个维度之间寻找平衡点。

历史定位上，关节电机是"电机—减速器—编码器—驱动器"四合一集成的产物。它真正改变的不是电机技术本身，而是**执行器的可采购性**——整机厂无需自行匹配电机与减速器，而是直接采购经过标定的关节模组，将精力集中在整机动力学与控制算法上。

### 原理拆解

**① 扭矩放大：减速比的决定性作用**

关节电机的输出扭矩由电机扭矩经减速器放大得到。设电机峰值转矩为 \(\tau_{m,peak}\)，减速器效率为 \(\eta\)，减速比为 \(G\)，则输出峰值扭矩近似为：

$$
\tau_{peak} \approx G \cdot \tau_{m,peak} \cdot \eta
$$

以 60 kg 级人形机器人髋关节屈伸为例，设计指标为输出峰值扭矩 120 N·m、连续 RMS 转矩 35 N·m、最大角速度 8 rad/s、减速器效率 0.85。候选电机峰值转矩 3.0 N·m、连续 RMS 转矩 1.0 N·m、最大转速 300 rad/s。

按峰值转矩初选减速比：

$$
G \ge \frac{\tau_{peak}}{\tau_{m,peak} \, \eta} = \frac{120}{3.0 \times 0.85} \approx 47.1
$$

**② 速度上限：减速比的另一侧约束**

减速比同时受电机最高转速约束。输出最大角速度 8 rad/s 对应电机侧转速需求：

$$
G \le \frac{\omega_{m,max}}{\omega_{out,max}} = \frac{300}{8} = 37.5
$$

步骤 1 与步骤 2 冲突：候选电机峰值转矩不足或最高转速不足，需重新选型。换用峰值转矩 4.5 N·m、最大转速 400 rad/s 的电机后：

$$
G \ge \frac{120}{4.5 \times 0.85} \approx 31.4, \qquad
G \le \frac{400}{8} = 50
$$

取 \(G = 40\) 兼顾扭矩裕量与速度裕量。

**③ 连续热校验：RMS 转矩决定持续能力**

峰值扭矩决定瞬时能力，连续 RMS 转矩决定持续工作能力。电机侧连续转矩需求为：

$$
\tau_{m,rms} = \frac{\tau_{rms}}{G \eta} = \frac{35}{40 \times 0.85} \approx 1.03\ \text{N·m}
$$

略大于电机连续转矩 1.0 N·m，可通过提高 \(G\) 至 42 或选用连续转矩 1.2 N·m 的电机解决。

**④ 热阻模型：允许损耗功率**

设电机相电阻 \(R = 0.30\ \Omega\)，热阻 \(R_{th} = 1.8\ \text{K/W}\)，允许温升 \(\Delta T = 115\ \text{K}\)，则允许损耗功率为：

$$
P_{loss,allow} = \frac{\Delta T}{R_{th}} = \frac{115}{1.8} \approx 63.9\ \text{W}
$$

该值需与电机铜损 \(I^2 R\) 对比，确保连续工况下温升不超限（工程判断，基于语料中热校验参数）。

### 关键参数与规格

关节电机的核心规格参数如下表所示（数字均来自语料）：

| 参数 | 符号 | 数值 | 说明 |
|------|------|------|------|
| 输出峰值扭矩 | \(\tau_{peak}\) | 120 N·m | 瞬时最大输出 |
| 输出连续 RMS 转矩 | \(\tau_{rms}\) | 35 N·m | 持续工作能力 |
| 输出最大角速度 | \(\omega_{out,max}\) | 8 rad/s | 输出端速度上限 |
| 减速器效率 | \(\eta\) | 0.85 | 扭矩传递效率 |
| 候选电机峰值转矩 | \(\tau_{m,peak}\) | 3.0 N·m（初选）/ 4.5 N·m（重选） | 电机侧瞬时能力 |
| 候选电机连续转矩 | \(\tau_{m,cont}\) | 1.0 N·m | 电机侧持续能力 |
| 候选电机最大转速 | \(\omega_{m,max}\) | 300 rad/s（初选）/ 400 rad/s（重选） | 电机侧速度上限 |
| 电机相电阻 | \(R\) | 0.30 Ω | 铜损计算 |
| 热阻 | \(R_{th}\) | 1.8 K/W | 温升计算 |
| 允许温升 | \(\Delta T\) | 115 K | 绝缘等级约束 |

### 横向对比

关节电机与相近方案的对比如下：

| 维度 | 关节电机（集成执行器） | 直驱电机 | 传统伺服电机 + 外部减速器 |
|------|----------------------|---------|--------------------------|
| 集成度 | 高：电机、减速器、编码器、驱动器一体化 | 中：电机直接驱动，无减速器 | 低：各部件独立安装 |
| 背隙 | 小（谐波减速器背隙极小） | 零（无减速器） | 取决于减速器选型 |
| 透明度 | 中（受减速器摩擦影响） | 高（无减速器摩擦） | 低（减速器摩擦与齿隙） |
| 扭矩密度 | 高（减速比放大） | 低（需大体积电机） | 中（结构松散） |
| 轴向尺寸 | 紧凑 | 大 | 大 |
| 典型应用 | 人形机器人髋/膝/踝关节 | 低扭矩高精度关节 | 工业机械臂 |

关节电机的核心优势在于**扭矩密度与集成度**，代价是透明度略逊于直驱。对于 60 kg 级人形机器人的髋关节屈伸（峰值 120 N·m），直驱方案需要极大体积的电机，工程上不可行（工程判断）。

### 谁在用·应用案例

关节电机是当前人形机器人整机的主流执行器方案。语料中的实体关系示例显示：

- **Tesla Optimus**（`ent_robot_system_tesla_optimus`）使用谐波减速器与无框力矩电机，旋转执行器是其组成部分。
- **Unitree H1**（`ent_robot_unitree_h1_humanoid_robot_2024`）同样使用谐波减速器与无框力矩电机，旋转执行器是其组成部分。
- **谐波减速器**（`ent_component_harmonic_reducer_2024`）是旋转执行器的一部分，而旋转执行器（`ent_component_rotary_actuator_2024`）是整机的一部分。

在供应链层面，**CubeMars**（`ent_company_cubemars_2024`）是紧凑型一体化机器人关节电机和执行器供应商，属于零部件制造商类型，其产品覆盖关节电机与执行器模组。关节电机的选型流程（如上述四步法）直接服务于整机厂的关节设计。

### 局限与边界

关节电机的局限性主要体现在：

1. **热管理瓶颈**：连续 RMS 转矩受热阻与允许温升约束。上述算例中，电机侧连续转矩需求 1.03 N·m 略超电机连续转矩 1.0 N·m，需通过提高减速比或换用更大连续转矩电机解决。高负载工况下的热积累是关节电机持续输出的硬边界。
2. **减速比两难**：减速比需同时满足峰值扭矩下限与速度上限。初选电机时，减速比需求区间 [47.1, 37.5] 为空集，说明电机选型不当会导致无解。这一矛盾在高速轻载与低速重载需求并存的关节（如髋关节）中尤为突出。
3. **透明度受限**：减速器引入摩擦与反射惯量，降低外力反向驱动的顺滑程度，影响力控精度。谐波减速器的柔轮变形也带来非线性。
4. **峰值与连续能力差距大**：120 N·m 峰值与 35 N·m 连续 RMS 的比值约 3.4 倍（按语料数据推算），意味着关节只能短时爆发，持续高负载能力有限。

### 常见误区

1. **"关节电机就是普通电机"**——错。关节电机是无框力矩电机形态，无外壳、无轴承、无编码器，依赖关节结构件承载。普通电机无法直接装入关节。
2. **"减速比越大越好"**——错。减速比受速度上限约束。上述算例中，初选电机时减速比需求区间为空集，说明盲目增大减速比会导致输出速度不足。
3. **"峰值扭矩决定电机选型"**——错。连续 RMS 转矩与热校验同样关键。算例中峰值扭矩满足后，连续转矩 1.03 N·m 仍略超电机 1.0 N·m 能力，需微调减速比或换电机。
4. **"效率 0.85 可以忽略"**——错。效率直接进入减速比计算公式的分母，0.85 的效率意味着约 15% 的扭矩损失，直接影响减速比下限。
5. **"关节电机与减速器是独立采购的"**——错。当前趋势是一体化集成执行器，整机厂直接采购标定好的关节模组，而非自行匹配电机与减速器。

### 相关知识

- `ent_company_cubemars_2024` — 紧凑型一体化机器人关节电机和执行器供应商，属于零部件制造商类型，是关节电机产业链上游的关键厂商。
- `ent_component_harmonic_reducer_2024` — 谐波减速器是关节电机的核心传动部件，语料中明确其为旋转执行器的一部分。
- `ent_component_rotary_actuator_2024` — 旋转执行器是关节电机与减速器、编码器集成的完整模组，是整机关节的物理载体。
- `ent_robot_system_tesla_optimus` — Tesla Optimus 使用谐波减速器与无框力矩电机，是关节电机方案的典型整机应用。
- `ent_robot_unitree_h1_humanoid_robot_2024` — Unitree H1 同样采用谐波减速器与无框力矩电机，验证了关节电机方案在国产整机中的普及度。

## 参考

- [Servomotor - Wikipedia](https://en.wikipedia.org/wiki/Servomotor)
- [Humanoid Robot Full Development Workflow](https://github.com/YansongW/awesome-humanoid-robot/tree/main/docs/humanoid_full_development_workflow_v3.md)
- [Chapter 02: Knowledge Graph & Entity System](https://github.com/YansongW/awesome-humanoid-robot/tree/main/wiki/docs/chapters/chapter-02.md)
- [Chapter 04: Components](https://github.com/YansongW/awesome-humanoid-robot/tree/main/wiki/docs/chapters/chapter-04.md)

## Overview

Joint motors are the core power source for rotary actuators in humanoid robots, typically integrating frameless torque motors with reducers into a single unit, delivering peak torque up to 120 N·m, continuous RMS torque of 35 N·m, and a maximum angular velocity of 8 rad/s. What truly changes is not the motor itself, but the integration approach of "motor—reducer—encoder—driver"—packaging power, transmission, and sensing into a single electromechanical unit that can be directly installed into a joint.

## Content

### What It Is: Precise Definition

A joint motor is a motor assembly installed at a robot's joint that directly drives the relative motion of connecting links. In the humanoid robot industry chain, it falls under the `component` type, with a value chain level of upstream, and a domain code of `02_components`. Unlike ordinary industrial motors, the design constraints for joint motors come from the robot body itself: peak torque density, continuous thermal management capability, backlash, backdrivability, and axial dimensions—rather than simple rated power.

Joint motors typically adopt the **frameless torque motor** form—consisting only of a stator and rotor, with no housing, bearings, or encoder, as these components are handled separately by the joint structural parts, cross-roller bearings, and encoder. The motor rotor is coupled directly or through a reducer to the output flange, forming an integrated actuator of "joint motor + reducer + encoder + driver." This form is applied in complete machines such as Tesla Optimus and Unitree H1 (engineering judgment, based on entity-relationship examples in the corpus).

### Why It Exists: Pain Points and Historical Positioning

Before joint motors became the standard solution, robot joint design faced a fundamental contradiction: **the high-speed, low-torque characteristics of motors did not match the low-speed, high-torque requirements of joints**. Direct drive eliminated the backlash and friction of reducers, but required extremely low-speed, high-torque motors, causing motor size and weight to balloon—unsuitable for high-torque joints like the hip joint of a 60 kg-class humanoid robot.

The maturation of harmonic reducers and planetary reducers made "high-speed small motor + large reduction ratio" possible. However, a larger reduction ratio is not always better: while it increases output torque, it simultaneously reduces the maximum output speed, increases reflected inertia and backlash, and degrades transparency—that is, the smoothness when external forces drive the joint in reverse. The essence of joint motor design is finding a balance among the four dimensions of **torque, speed, transparency, and thermal management**.

Historically, the joint motor is the product of the four-in-one integration of "motor—reducer—encoder—driver." What truly changes is not motor technology itself, but the **procurability of actuators**—OEMs no longer need to match motors and reducers themselves, but can directly purchase calibrated joint modules, focusing their efforts on whole-machine dynamics and control algorithms.

### Principle Breakdown

**① Torque Amplification: The Decisive Role of the Reduction Ratio**

The output torque of a joint motor is obtained by amplifying the motor torque through the reducer. Let the motor peak torque be \(\tau_{m,peak}\), reducer efficiency be \(\eta\), and reduction ratio be \(G\); then the output peak torque is approximately:

$$
\tau_{peak} \approx G \cdot \tau_{m,peak} \cdot \eta
$$

Taking the hip flexion-extension of a 60 kg-class humanoid robot as an example, the design specifications are output peak torque of 120 N·m, continuous RMS torque of 35 N·m, maximum angular velocity of 8 rad/s, and reducer efficiency of 0.85. The candidate motor has a peak torque of 3.0 N·m, continuous RMS torque of 1.0 N·m, and maximum speed of 300 rad/s.

Preliminary reduction ratio selection based on peak torque:

$$
G \ge \frac{\tau_{peak}}{\tau_{m,peak} \, \eta} = \frac{120}{3.0 \times 0.85} \approx 47.1
$$

**② Speed Upper Limit: The Other Constraint on the Reduction Ratio**

The reduction ratio is also constrained by the motor's maximum speed. The output maximum angular velocity of 8 rad/s corresponds to a motor-side speed requirement of:

$$
G \le \frac{\omega_{m,max}}{\omega_{out,max}} = \frac{300}{8} = 37.5
$$

Steps 1 and 2 conflict: the candidate motor has insufficient peak torque or insufficient maximum speed, requiring reselection. After switching to a motor with a peak torque of 4.5 N·m and a maximum speed of 400 rad/s:

$$
G \ge \frac{120}{4.5 \times 0.85} \approx 31.4, \qquad
G \le \frac{400}{8} = 50
$$

Taking \(G = 40\) balances torque margin and speed margin.

**③ Continuous Thermal Verification: RMS Torque Determines Sustained Capability**

Peak torque determines instantaneous capability, while continuous RMS torque determines sustained working capability. The motor-side continuous torque requirement is:

$$
\tau_{m,rms} = \frac{\tau_{rms}}{G \eta} = \frac{35}{40 \times 0.85} \approx 1.03\ \text{N·m}
$$

This slightly exceeds the motor's continuous torque of 1.0 N·m, which can be resolved by increasing \(G\) to 42 or selecting a motor with a continuous torque of 1.2 N·m.

**④ Thermal Resistance Model: Allowable Power Loss**

Let the motor phase resistance be \(R = 0.30\ \Omega\), thermal resistance be \(R_{th} = 1.8\ \text{K/W}\), and allowable temperature rise be \(\Delta T = 115\ \text{K}\); then the allowable power loss is:

$$
P_{loss,allow} = \frac{\Delta T}{R_{th}} = \frac{115}{1.8} \approx 63.9\ \text{W}
$$

This value must be compared with the motor's copper loss \(I^2 R\) to ensure the temperature rise does not exceed limits under continuous operating conditions (engineering judgment, based on thermal verification parameters in the corpus).

### Key Parameters and Specifications

The core specification parameters of joint motors are shown in the table below (all figures from the corpus):

| Parameter | Symbol | Value | Description |
|-----------|--------|-------|-------------|
| Output peak torque | \(\tau_{peak}\) | 120 N·m | Instantaneous maximum output |
| Output continuous RMS torque | \(\tau_{rms}\) | 35 N·m | Sustained working capability |
| Output maximum angular velocity | \(\omega_{out,max}\) | 8 rad/s | Output-side speed upper limit |
| Reducer efficiency | \(\eta\) | 0.85 | Torque transmission efficiency |
| Candidate motor peak torque | \(\tau_{m,peak}\) | 3.0 N·m (initial) / 4.5 N·m (reselected) | Motor-side instantaneous capability |
| Candidate motor continuous torque | \(\tau_{m,cont}\) | 1.0 N·m | Motor-side sustained capability |
| Candidate motor maximum speed | \(\omega_{m,max}\) | 300 rad/s (initial) / 400 rad/s (reselected) | Motor-side speed upper limit |
| Motor phase resistance | \(R\) | 0.30 Ω | Copper loss calculation |
| Thermal resistance | \(R_{th}\) | 1.8 K/W | Temperature rise calculation |
| Allowable temperature rise | \(\Delta T\) | 115 K | Insulation class constraint |

### Horizontal Comparison

A comparison between joint motors and similar approaches is as follows:

| Dimension | Joint Motor (Integrated Actuator) | Direct Drive Motor | Traditional Servo Motor + External Reducer |
|-----------|----------------------------------|--------------------|--------------------------------------------|
| Integration level | High: motor, reducer, encoder, driver integrated | Medium: motor drives directly, no reducer | Low: components installed independently |
| Backlash | Small (harmonic reducers have minimal backlash) | Zero (no reducer) | Depends on reducer selection |
| Transparency | Medium (affected by reducer friction) | High (no reducer friction) | Low (reducer friction and gear backlash) |
| Torque density | High (amplified by reduction ratio) | Low (requires large motor volume) | Medium (loose structure) |
| Axial dimensions | Compact | Large | Large |
| Typical applications | Humanoid robot hip/knee/ankle joints | Low-torque high-precision joints | Industrial robotic arms |

The core advantage of joint motors lies in **torque density and integration level**, at the cost of slightly lower transparency compared to direct drive. For hip flexion-extension (peak 120 N·m) in a 60 kg-class humanoid robot, a direct drive solution would require an extremely large motor, which is not engineering-feasible (engineering judgment).

### Who Uses It: Application Cases

Joint motors are the mainstream actuator solution for current humanoid robot complete machines. Entity-relationship examples in the corpus show:

- **Tesla Optimus** (`ent_robot_system_tesla_optimus`) uses harmonic reducers and frameless torque motors, with rotary actuators as a component.
- **Unitree H1** (`ent_robot_unitree_h1_humanoid_robot_2024`) also uses harmonic reducers and frameless torque motors, with rotary actuators as a component.
- **Harmonic reducer** (`ent_component_harmonic_reducer_2024`) is part of the rotary actuator, while the rotary actuator (`ent_component_rotary_actuator_2024`) is part of the complete machine.

At the supply chain level, **CubeMars** (`ent_company_cubemars_2024`) is a supplier of compact integrated robot joint motors and actuators, classified as a component manufacturer, with products covering joint motors and actuator modules. The joint motor selection process (such as the four-step method above) directly serves the joint design of OEMs.

### Limitations and Boundaries

The limitations of joint motors are mainly reflected in:

1. **Thermal management bottleneck**: Continuous RMS torque is constrained by thermal resistance and allowable temperature rise. In the above example, the motor-side continuous torque requirement of 1.03 N·m slightly exceeds the motor's continuous torque of 1.0 N·m, requiring a higher reduction ratio or a motor with greater continuous torque. Heat accumulation under high-load conditions is a hard boundary for continuous output of joint motors.
2. **Reduction ratio dilemma**: The reduction ratio must simultaneously satisfy the peak torque lower limit and the speed upper limit. With the initially selected motor, the required reduction ratio interval [47.1, 37.5] is an empty set, indicating that improper motor selection leads to no solution. This contradiction is particularly prominent in joints with coexisting high-speed light-load and low-speed heavy-load requirements (such as the hip joint).
3. **Limited transparency**: The reducer introduces friction and reflected inertia, reducing the smoothness of reverse driving by external forces and affecting force control accuracy. The flexspline deformation of harmonic reducers also introduces nonlinearity.
4. **Large gap between peak and continuous capability**: The ratio of 120 N·m peak to 35 N·m continuous RMS is approximately 3.4 times (calculated from corpus data), meaning the joint can only burst briefly, with limited sustained high-load capability.

### Common Misconceptions

1. **"A joint motor is just an ordinary motor"**—Wrong. Joint motors adopt the frameless torque motor form, with no housing, bearings, or encoder, relying on joint structural parts for support. Ordinary motors cannot be directly installed into joints.
2. **"The larger the reduction ratio, the better"**—Wrong. The reduction ratio is constrained by the speed upper limit. In the above example, the required reduction ratio interval for the initially selected motor is an empty set, showing that blindly increasing the reduction ratio leads to insufficient output speed.
3. **"Peak torque determines motor selection"**—Wrong. Continuous RMS torque and thermal verification are equally critical. In the example, after satisfying peak torque, the continuous torque of 1.03 N·m still slightly exceeds the motor's 1.0 N·m capability, requiring fine-tuning of the reduction ratio or a motor change.
4. **"An efficiency of 0.85 can be ignored"**—Wrong. Efficiency directly enters the denominator of the reduction ratio calculation formula; an efficiency of 0.85 means approximately 15% torque loss, directly affecting the reduction ratio lower limit.
5. **"Joint motors and reducers are purchased independently"**—Wrong. The current trend is integrated actuators, where OEMs directly purchase calibrated joint modules rather than matching motors and reducers themselves.

### Related Knowledge

- `ent_company_cubemars_2024` — Supplier of compact integrated robot joint motors and actuators, classified as a component manufacturer, and a key upstream player in the joint motor industry chain.
- `ent_component_harmonic_reducer_2024` — Harmonic reducers are the core transmission component of joint motors; the corpus explicitly identifies them as part of the rotary actuator.
- `ent_component_rotary_actuator_2024` — The rotary actuator is a complete module integrating the joint motor, reducer, and encoder, serving as the physical carrier of the robot joint.
- `ent_robot_system_tesla_optimus` — Tesla Optimus uses harmonic reducers and frameless torque motors, representing a typical complete-machine application of the joint motor solution.
- `ent_robot_unitree_h1_humanoid_robot_2024` — Unitree H1 also adopts harmonic reducers and frameless torque motors, validating the prevalence of the joint motor solution in domestic complete machines.

## 개요

관절 모터(Joint Motor)는 휴머노이드 로봇 회전 액추에이터의 핵심 동력원으로, 일반적으로 프레임리스 토크 모터와 감속기가 일체형으로 통합되어 있으며, 출력 피크 토크는 120 N·m, 연속 RMS 토크 35 N·m, 최대 각속도 8 rad/s에 달합니다. 이것이 진정으로 바꾼 것은 모터 자체가 아니라 "모터—감속기—엔코더—드라이버"의 통합 방식입니다. 즉, 동력, 전동 및 감지를 하나의 관절에 직접 장착할 수 있는 전기기계 유닛으로 패키징한 것입니다.

## 핵심 내용

### 무엇인가: 정확한 정의

관절 모터는 로봇 관절에 설치되어 링크의 상대 운동을 직접 구동하는 모터 어셈블리입니다. 휴머노이드 로봇 산업 체인에서 이는 `component`(부품) 유형에 속하며, 가치 사슬 계층은 업스트림(upstream), 도메인 코드는 `02_components`입니다. 일반 산업용 모터와 달리 관절 모터의 설계 제약은 로봇 본체에서 비롯됩니다: 피크 토크 밀도, 연속 열 관리 능력, 백래시, 투명성(backdrivability) 및 축 방향 치수이며, 단순한 정격 출력이 아닙니다.

관절 모터는 일반적으로 **프레임리스 토크 모터(frameless torque motor)** 형태를 사용합니다—고정자와 회전자만 있으며, 하우징, 베어링, 엔코더가 없고, 이러한 부품은 관절 구조 부재, 크로스 롤러 베어링 및 엔코더가 각각 담당합니다. 모터 회전자는 직접 또는 감속기를 통해 출력 플랜지에 결합되어 "관절 모터 + 감속기 + 엔코더 + 드라이버"의 통합 액추에이터(integrated actuator)를 형성합니다. 이러한 형태는 Tesla Optimus, Unitree H1 등의 완성 로봇에 모두 적용되었습니다(엔지니어링 판단, 코퍼스의 엔티티 관계 예시 기반).

### 왜 존재하는가: 문제점과 역사적 위치

관절 모터가 표준 솔루션이 되기 전, 로봇 관절 설계는 근본적인 모순에 직면했습니다: **모터의 고속 저토크 특성과 관절의 저속 고토크 요구 간의 불일치**. 직접 구동(direct drive)은 감속기의 백래시와 마찰을 제거하지만, 모터가 극저속 대토크를 요구하여 모터 부피와 무게가 급격히 증가하며, 60 kg급 휴머노이드 로봇의 고관절과 같은 대토크 관절에 적합하지 않습니다.

고조파 감속기와 유성 감속기의 성숙으로 "고속 소형 모터 + 대감속비"가 가능해졌습니다. 그러나 감속비가 클수록 좋은 것은 아닙니다: 감속비 증가는 출력 토크를 높이지만, 동시에 출력 속도 상한을 낮추고, 반사 관성과 백래시를 증가시키며, 투명성—즉 외력이 관절을 역방향으로 구동할 때의 부드러움—을 악화시킵니다. 관절 모터 설계의 본질은 **토크, 속도, 투명성, 열 관리**의 네 가지 차원 사이에서 균형점을 찾는 것입니다.

역사적 위치에서 관절 모터는 "모터—감속기—엔코더—드라이버" 4-in-1 통합의 산물입니다. 이것이 진정으로 바꾼 것은 모터 기술 자체가 아니라 **액추에이터의 조달 가능성**입니다—완성차 업체는 모터와 감속기를 직접 매칭할 필요 없이, 보정된 관절 모듈을 직접 조달하여 완성차 동역학 및 제어 알고리즘에 집중할 수 있습니다.

### 원리 분해

**① 토크 증폭: 감속비의 결정적 역할**

관절 모터의 출력 토크는 모터 토크가 감속기를 통해 증폭되어 얻어집니다. 모터 피크 토크를 \(\tau_{m,peak}\), 감속기 효율을 \(\eta\), 감속비를 \(G\)라고 하면, 출력 피크 토크는 근사적으로:

$$
\tau_{peak} \approx G \cdot \tau_{m,peak} \cdot \eta
$$

60 kg급 휴머노이드 로봇 고관절 굴곡/신전을 예로 들면, 설계 사양은 출력 피크 토크 120 N·m, 연속 RMS 토크 35 N·m, 최대 각속도 8 rad/s, 감속기 효율 0.85입니다. 후보 모터 피크 토크 3.0 N·m, 연속 RMS 토크 1.0 N·m, 최대 회전 속도 300 rad/s.

피크 토크 기준으로 감속비 초기 선정:

$$
G \ge \frac{\tau_{peak}}{\tau_{m,peak} \, \eta} = \frac{120}{3.0 \times 0.85} \approx 47.1
$$

**② 속도 상한: 감속비의 다른 측면 제약**

감속비는 동시에 모터 최고 회전 속도의 제약을 받습니다. 출력 최대 각속도 8 rad/s는 모터 측 회전 속도 요구에 해당:

$$
G \le \frac{\omega_{m,max}}{\omega_{out,max}} = \frac{300}{8} = 37.5
$$

단계 1과 단계 2가 충돌합니다: 후보 모터의 피크 토크 부족 또는 최고 회전 속도 부족으로 재선정이 필요합니다. 피크 토크 4.5 N·m, 최대 회전 속도 400 rad/s의 모터로 교체한 후:

$$
G \ge \frac{120}{4.5 \times 0.85} \approx 31.4, \qquad
G \le \frac{400}{8} = 50
$$

\(G = 40\)을 선택하여 토크 여유와 속도 여유를 모두 고려합니다.

**③ 연속 열 검증: RMS 토크가 지속 능력 결정**

피크 토크는 순간 능력을 결정하고, 연속 RMS 토크는 지속 작업 능력을 결정합니다. 모터 측 연속 토크 요구는:

$$
\tau_{m,rms} = \frac{\tau_{rms}}{G \eta} = \frac{35}{40 \times 0.85} \approx 1.03\ \text{N·m}
$$

모터 연속 토크 1.0 N·m보다 약간 크므로, \(G\)를 42로 높이거나 연속 토크 1.2 N·m의 모터를 선택하여 해결할 수 있습니다.

**④ 열저항 모델: 허용 손실 전력**

모터 상 저항 \(R = 0.30\ \Omega\), 열저항 \(R_{th} = 1.8\ \text{K/W}\), 허용 온도 상승 \(\Delta T = 115\ \text{K}\)라고 하면, 허용 손실 전력은:

$$
P_{loss,allow} = \frac{\Delta T}{R_{th}} = \frac{115}{1.8} \approx 63.9\ \text{W}
$$

이 값은 모터 구리 손실 \(I^2 R\)과 비교하여 연속 운전 조건에서 온도 상승이 한도를 초과하지 않는지 확인해야 합니다(엔지니어링 판단, 코퍼스의 열 검증 매개변수 기반).

### 핵심 매개변수 및 사양

관절 모터의 핵심 사양 매개변수는 아래 표와 같습니다(모든 수치는 코퍼스에서 가져옴):

| 매개변수 | 기호 | 값 | 설명 |
|------|------|------|------|
| 출력 피크 토크 | \(\tau_{peak}\) | 120 N·m | 순간 최대 출력 |
| 출력 연속 RMS 토크 | \(\tau_{rms}\) | 35 N·m | 지속 작업 능력 |
| 출력 최대 각속도 | \(\omega_{out,max}\) | 8 rad/s | 출력단 속도 상한 |
| 감속기 효율 | \(\eta\) | 0.85 | 토크 전달 효율 |
| 후보 모터 피크 토크 | \(\tau_{m,peak}\) | 3.0 N·m(초기 선정) / 4.5 N·m(재선정) | 모터 측 순간 능력 |
| 후보 모터 연속 토크 | \(\tau_{m,cont}\) | 1.0 N·m | 모터 측 지속 능력 |
| 후보 모터 최대 회전 속도 | \(\omega_{m,max}\) | 300 rad/s(초기 선정) / 400 rad/s(재선정) | 모터 측 속도 상한 |
| 모터 상 저항 | \(R\) | 0.30 Ω | 구리 손실 계산 |
| 열저항 | \(R_{th}\) | 1.8 K/W | 온도 상승 계산 |
| 허용 온도 상승 | \(\Delta T\) | 115 K | 절연 등급 제약 |

### 횡적 비교

관절 모터와 유사 솔루션의 비교는 다음과 같습니다:

| 차원 | 관절 모터(통합 액추에이터) | 직접 구동 모터 | 기존 서보 모터 + 외부 감속기 |
|------|----------------------|---------|--------------------------|
| 통합도 | 높음: 모터, 감속기, 엔코더, 드라이버 일체화 | 중간: 모터 직접 구동, 감속기 없음 | 낮음: 각 부품 독립 설치 |
| 백래시 | 작음(고조파 감속기 백래시 극히 작음) | 영(감속기 없음) | 감속기 선정에 따라 다름 |
| 투명성 | 중간(감속기 마찰 영향) | 높음(감속기 마찰 없음) | 낮음(감속기 마찰 및 치 간극) |
| 토크 밀도 | 높음(감속비 증폭) | 낮음(대형 모터 필요) | 중간(구조가 느슨함) |
| 축 방향 치수 | 컴팩트 | 큼 | 큼 |
| 대표적 적용 | 휴머노이드 로봇 고/슬/발목 관절 | 저토크 고정밀 관절 | 산업용 로봇 팔 |

관절 모터의 핵심 장점은 **토크 밀도와 통합도**이며, 대가는 투명성이 직접 구동보다 약간 떨어진다는 점입니다. 60 kg급 휴머노이드 로봇의 고관절 굴곡/신전(피크 120 N·m)의 경우, 직접 구동 솔루션은 극도로 큰 모터 부피가 필요하여 공학적으로 불가능합니다(엔지니어링 판단).

### 누가 사용하는가·적용 사례

관절 모터는 현재 휴머노이드 로봇 완성차의 주류 액추에이터 솔루션입니다. 코퍼스의 엔티티 관계 예시는 다음을 보여줍니다:

- **Tesla Optimus**(`ent_robot_system_tesla_optimus`)는 고조파 감속기와 프레임리스 토크 모터를 사용하며, 회전 액추에이터는 그 구성 요소입니다.
- **Unitree H1**(`ent_robot_unitree_h1_humanoid_robot_2024`)도 고조파 감속기와 프레임리스 토크 모터를 사용하며, 회전 액추에이터는 그 구성 요소입니다.
- **고조파 감속기**(`ent_component_harmonic_reducer_2024`)는 회전 액추에이터의 일부이며, 회전 액추에이터(`ent_component_rotary_actuator_2024`)는 완성차의 일부입니다.

공급망 측면에서 **CubeMars**(`ent_company_cubemars_2024`)는 컴팩트한 일체형 로봇 관절 모터 및 액추에이터 공급업체로, 부품 제조사 유형에 속하며, 그 제품은 관절 모터와 액추에이터 모듈을 포괄합니다. 관절 모터 선정 프로세스(위의 4단계 방법 등)는 완성차 업체의 관절 설계에 직접적으로 기여합니다.

### 한계와 경계

관절 모터의 한계는 주로 다음과 같습니다:

1. **열 관리 병목**: 연속 RMS 토크는 열저항과 허용 온도 상승의 제약을 받습니다. 위의 계산 예에서 모터 측 연속 토크 요구 1.03 N·m는 모터 연속 토크 1.0 N·m를 약간 초과하므로, 감속비를 높이거나 더 큰 연속 토크 모터로 교체해야 합니다. 고부하 조건에서의 열 축적은 관절 모터의 지속 출력에 대한 하드 경계입니다.
2. **감속비 딜레마**: 감속비는 피크 토크 하한과 속도 상한을 동시에 충족해야 합니다. 초기 선정 모터에서 감속비 요구 구간 [47.1, 37.5]은 공집합으로, 모터 선정이 부적절하면 해가 없음을 의미합니다. 이 모순은 고속 경부하와 저속 중부하 요구가 공존하는 관절(예: 고관절)에서 특히 두드러집니다.
3. **투명성 제한**: 감속기는 마찰과 반사 관성을 도입하여 외력 역방향 구동의 부드러움을 낮추고, 힘 제어 정밀도에 영향을 줍니다. 고조파 감속기의 플렉스 스플라인 변형도 비선형성을 가져옵니다.
4. **피크와 연속 능력의 큰 격차**: 120 N·m 피크와 35 N·m 연속 RMS의 비율은 약 3.4배(코퍼스 데이터 기준 추산)로, 관절이 짧은 시간 동안만 폭발적으로 출력할 수 있고 지속 고부하 능력은 제한적임을 의미합니다.

### 일반적인 오해

1. **"관절 모터는 일반 모터다"**—틀림. 관절 모터는 프레임리스 토크 모터 형태로, 하우징, 베어링, 엔코더가 없으며 관절 구조 부재에 의존합니다. 일반 모터는 관절에 직접 장착할 수 없습니다.
2. **"감속비가 클수록 좋다"**—틀림. 감속비는 속도 상한의 제약을 받습니다. 위의 계산 예에서 초기 선정 모터의 감속비 요구 구간이 공집합인 것은, 무작정 감속비를 키우면 출력 속도가 부족해짐을 의미합니다.
3. **"피크 토크가 모터 선정을 결정한다"**—틀림. 연속 RMS 토크와 열 검증도 동일하게 중요합니다. 계산 예에서 피크 토크를 충족한 후에도 연속 토크 1.03 N·m가 모터 1.0 N·m 능력을 여전히 약간 초과하므로, 감속비를 미세 조정하거나 모터를 교체해야 합니다.
4. **"효율 0.85는 무시할 수 있다"**—틀림. 효율은 감속비 계산 공식의 분모에 직접 들어가며, 0.85의 효율은 약 15%의 토크 손실을 의미하여 감속비 하한에 직접 영향을 줍니다.
5. **"관절 모터와 감속기는 독립적으로 조달된다"**—틀림. 현재 추세는 일체형 통합 액추에이터로, 완성차 업체는 보정된 관절 모듈을 직접 조달하며 모터와 감속기를 직접 매칭하지 않습니다.

### 관련 지식

- `ent_company_cubemars_2024` — 컴팩트한 일체형 로봇 관절 모터 및 액추에이터 공급업체로, 부품 제조사 유형에 속하며 관절 모터 산업 체인의 업스트림 핵심 기업입니다.
- `ent_component_harmonic_reducer_2024` — 고조파 감속기는 관절 모터의 핵심 전동 부품으로, 코퍼스에서 회전 액추에이터의 일부임을 명시합니다.
- `ent_component_rotary_actuator_2024` — 회전 액추에이터는 관절 모터와 감속기, 엔코더가 통합된 완전한 모듈로, 완성차 관절의 물리적 캐리어입니다.
- `ent_robot_system_tesla_optimus` — Tesla Optimus는 고조파 감속기와 프레임리스 토크 모터를 사용하며, 관절 모터 솔루션의 대표적인 완성차 적용 사례입니다.
- `ent_robot_unitree_h1_humanoid_robot_2024` — Unitree H1도 고조파 감속기와 프레임리스 토크 모터를 채택하여, 관절 모터 솔루션이 국산 완성차에서 보편화되었음을 검증합니다.
