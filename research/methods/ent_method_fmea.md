---
$id: ent_method_fmea
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Failure Mode and Effects Analysis (FMEA)
  zh: 失效模式与影响分析（FMEA）
  ko: 고장 모드 및 영향 분석(FMEA)
summary:
  en: A bottom-up reliability method that identifies potential failure modes, their causes and effects, and prioritizes actions
    to mitigate risk.
  zh: '概述 8.6.6 可靠性工程与失效模式分析相关内容如下。 ## 核心内容 #### 8.6.6 可靠性工程与失效模式分析 人形机器人在长周期运行中面临机械磨损、电子老化、软件缺陷与环境应力等多重失效风险。可靠性工程（reliability
    engineering）通过定量方法预测、分配并改进系统可靠性，是降低全生命周期成本与保障安全运行的关键[90][91][95]。'
  ko: 잠재적 고장 모드·원인·영향을 식별하고 위험 완화 조치의 우선순위를 정하는 상향식 신뢰성 방법.
domains:
- 05_mass_production
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_13
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
8.6.6 可靠性工程与失效模式分析相关内容如下。
## 核心内容
#### 8.6.6 可靠性工程与失效模式分析
人形机器人在长周期运行中面临机械磨损、电子老化、软件缺陷与环境应力等多重失效风险。**可靠性工程（reliability engineering）**通过定量方法预测、分配并改进系统可靠性，是降低全生命周期成本与保障安全运行的关键[90][91][95]。

!!! note "术语解释：可靠性工程、失效、生命周期成本、环境应力"
    - **可靠性工程（reliability engineering）**：研究并提升产品在规定条件下规定时间内完成功能能力的学科。
    - **失效（failure）**：产品丧失规定功能的事件。
    - **生命周期成本（LCC）**：产品全寿命周期内的总成本。
    - **环境应力（environmental stress）**：温度、湿度、振动、粉尘等外部作用。

**可靠性函数** \(R(t)\) 定义为产品在时间 \(t\) 内不失效的概率：

$$
R(t) = P(T > t)
$$

其中 \(T\) 为失效前时间。对应的**累积失效分布函数**为 \(F(t) = 1 - R(t)\)。**失效率**（hazard rate 或 failure rate）\(\lambda(t)\) 为：

$$
\lambda(t) = \frac{f(t)}{R(t)} = -\frac{d}{dt} \ln R(t)
$$

其中 \(f(t) = dF/dt\) 为失效概率密度。

!!! note "术语解释：可靠性函数、累积失效分布、失效率、失效概率密度"
    - **可靠性函数（reliability function）**：产品在时间 t 内正常工作的概率。
    - **累积失效分布（cumulative distribution function, CDF）**：在时间 t 前失效的概率。
    - **失效率（failure rate）**：单位时间内失效的概率。
    - **失效概率密度（probability density function, PDF）**：失效时间的概率密度。

典型电子与机械产品的失效率随时间呈**浴盆曲线（bathtub curve）**：

1. **早期失效期（infant mortality）**：失效率较高，通常由制造缺陷、装配错误引起，可通过老化筛选（burn-in）降低。
2. **随机失效期（useful life）**：失效率近似常数，是产品主要工作阶段。
3. **磨损失效期（wear-out）**：失效率随时间上升，由疲劳、磨损、老化导致。

!!! note "术语解释：浴盆曲线、早期失效、随机失效、磨损失效、老化筛选"
    - **浴盆曲线（bathtub curve）**：失效率随时间变化的 U 形曲线。
    - **早期失效（infant mortality）**：产品初期较高的失效率。
    - **随机失效（random failure）**：偶发、不可预测的失效。
    - **磨损失效（wear-out failure）**：长期使用后性能退化导致的失效。
    - **老化筛选（burn-in）**：通过早期运行剔除潜在缺陷。

当失效率为常数 \(\lambda\) 时，可靠性函数为指数分布：

$$
R(t) = e^{-\lambda t}
$$

**平均失效间隔时间（MTBF, Mean Time Between Failures）**为：

$$
\text{MTBF} = \frac{1}{\lambda}
$$

对于不可修产品，使用 **MTTF（Mean Time To Failure）**。

!!! note "术语解释：指数分布、平均失效间隔时间、平均失效前时间"
    - **指数分布（exponential distribution）**：常失效率下的寿命分布。
    - **平均失效间隔时间（MTBF）**：可修产品两次失效间的平均时间。
    - **平均失效前时间（MTTF）**：不可修产品失效前的平均时间。

**失效模式与影响分析（FMEA, Failure Mode and Effects Analysis）**是系统识别潜在失效、评估风险并优先改进的方法。每个失效模式从三个维度评分：

| 维度 | 符号 | 含义 | 典型评分 |
|---|---|---|---|
| 严重度 | S | 失效后果的严重程度 | 1–10 |
| 发生度 | O | 失效原因发生的可能性 | 1–10 |
| 探测度 | D | 当前控制措施探测失效的能力 | 1–10 |

**风险优先数（RPN）**为：

$$
\text{RPN} = S \times O \times D
$$

RPN 越高，越需优先采取改进措施。

!!! note "术语解释：失效模式、严重度、发生度、探测度、风险优先数"
    - **失效模式（failure mode）**：产品失效的具体表现形式。
    - **严重度（severity）**：失效后果的严重程度。
    - **发生度（occurrence）**：失效原因出现的频率。
    - **探测度（detection）**：发现失效原因或模式的能力。
    - **风险优先数（RPN）**：S、O、D 的乘积，用于风险排序。

人形机器人典型 FMEA 示例：

| 子系统 | 失效模式 | 潜在影响 | S | O | D | RPN | 改进措施 |
|---|---|---|---|---|---|---|---|
| 膝关节谐波减速器 | 柔轮疲劳裂纹 | 关节卡死、跌倒 | 9 | 4 | 5 | 180 | 疲劳试验、定期更换 |
| 电池包 | 单体热失控 | 起火、整机损毁 | 10 | 2 | 4 | 80 | BMS、热熔断、阻燃材料 |
| 踝六轴力传感器 | 零点漂移 | 平衡控制失稳 | 8 | 5 | 4 | 160 | 在线标定、冗余传感 |
| 急停回路 | 触点粘连 | 无法安全停机 | 10 | 2 | 3 | 60 | 双通道、自检 |
| 主控制器 | 软件崩溃 | 运动失控 | 9 | 3 | 3 | 81 | 看门狗、安全监控器 |

!!! note "术语解释：柔轮疲劳、热失控、零点漂移、触点粘连、看门狗"
    - **柔轮疲劳（flexspline fatigue）**：谐波减速器柔轮的循环疲劳。
    - **热失控（thermal runaway）**：电池温度失控的链式反应。
    - **零点漂移（zero drift）**：传感器零点随时间偏移。
    - **触点粘连（contact welding）**：继电器触点熔焊在一起。
    - **看门狗（watchdog）**：监测程序运行并在异常时复位的电路。

**可靠性框图（RBD, Reliability Block Diagram）**用图形表示系统各单元的可靠性逻辑关系：

- **串联系统**：任一单元失效则系统失效。总可靠性为各单元可靠性之积：
  $$
  R_s(t) = \prod_{i=1}^{n} R_i(t)
  $$
- **并联系统**：所有单元失效系统才失效。总不可靠性为各单元不可靠性之积：
  $$
  R_s(t) = 1 - \prod_{i=1}^{n} [1 - R_i(t)]
  $$

!!! note "术语解释：可靠性框图、串联系统、并联系统、冗余"
    - **可靠性框图（RBD）**：表示系统可靠性逻辑关系的框图。
    - **串联系统（series system）**：所有单元必须正常工作的系统。
    - **并联系统（parallel system）**：至少一个单元正常工作的系统。
    - **冗余（redundancy）**：通过重复配置提高可靠性。

**冗余设计**是提高人形机器人安全性的重要手段：

- **主动冗余（active redundancy）**：多个单元同时工作，如双编码器、双通道急停。
- **备用冗余（standby redundancy）**：备用单元在主单元失效后切换。
- **异构冗余（diverse redundancy）**：使用不同类型部件实现同一功能，降低共因失效风险。

!!! note "术语解释：主动冗余、备用冗余、异构冗余、共因失效"
    - **主动冗余（active redundancy）**：并联同时运行的冗余。
    - **备用冗余（standby redundancy）**：备用单元平时不工作。
    - **异构冗余（diverse redundancy）**：采用不同原理或来源的冗余。
    - **共因失效（common cause failure）**：同一原因导致多个单元同时失效。

对于疲劳与磨损主导的部件，寿命常可用 **Weibull 分布**描述：

$$
R(t) = \exp\left[-\left(\frac{t}{\eta}\right)^\beta\right]
$$

其中 \(\eta\) 为特征寿命，\(\beta\) 为形状参数。当 \(\beta < 1\) 时对应早期失效期；\(\beta = 1\) 退化为指数分布；\(\beta > 1\) 对应磨损失效期。

!!! note "术语解释：Weibull 分布、特征寿命、形状参数"
    - **Weibull 分布（Weibull distribution）**：描述寿命数据的灵活分布。
    - **特征寿命（characteristic life）**：Weibull 分布中的尺度参数。
    - **形状参数（shape parameter）**：决定 Weibull 分布形态的参数。

**Python 算例：系统可靠性与冗余效益**

以下代码计算由电机、减速器、驱动器、控制器组成的串联关节系统可靠性，并比较单通道与双通道冗余急停回路的可靠性。

```python
import numpy as np
import matplotlib.pyplot as plt

## 参考
- 详见 chapter-08.md。

## Overview
8.6.6 Reliability Engineering and Failure Mode Analysis related content is as follows.
## Content
#### 8.6.6 Reliability Engineering and Failure Mode Analysis
Humanoid robots face multiple failure risks during long-term operation, including mechanical wear, electronic aging, software defects, and environmental stress. **Reliability engineering** uses quantitative methods to predict, allocate, and improve system reliability, and is key to reducing life-cycle costs and ensuring safe operation[90][91][95].

!!! note "Term Explanation: Reliability Engineering, Failure, Life-Cycle Cost, Environmental Stress"
    - **Reliability engineering**: The discipline that studies and improves a product's ability to perform its required functions under stated conditions for a specified period of time.
    - **Failure**: The event when a product loses its ability to perform a required function.
    - **Life-Cycle Cost (LCC)**: The total cost of a product over its entire life cycle.
    - **Environmental stress**: External factors such as temperature, humidity, vibration, and dust.

The **reliability function** \(R(t)\) is defined as the probability that a product survives without failure for a time \(t\):

$$
R(t) = P(T > t)
$$

where \(T\) is the time to failure. The corresponding **cumulative distribution function of failure** is \(F(t) = 1 - R(t)\). The **hazard rate** or **failure rate** \(\lambda(t)\) is:

$$
\lambda(t) = \frac{f(t)}{R(t)} = -\frac{d}{dt} \ln R(t)
$$

where \(f(t) = dF/dt\) is the failure probability density.

!!! note "Term Explanation: Reliability Function, Cumulative Distribution Function of Failure, Failure Rate, Failure Probability Density"
    - **Reliability function**: The probability that a product operates normally for a time t.
    - **Cumulative distribution function (CDF)**: The probability of failure before time t.
    - **Failure rate**: The probability of failure per unit time.
    - **Probability density function (PDF)**: The probability density of failure times.

The failure rate of typical electronic and mechanical products over time follows a **bathtub curve**:

1. **Infant mortality**: High failure rate, usually caused by manufacturing defects or assembly errors, can be reduced by burn-in.
2. **Useful life**: The failure rate is approximately constant; this is the main operating period of the product.
3. **Wear-out**: The failure rate increases over time due to fatigue, wear, and aging.

!!! note "Term Explanation: Bathtub Curve, Infant Mortality, Random Failure, Wear-out Failure, Burn-in"
    - **Bathtub curve**: A U-shaped curve showing the failure rate over time.
    - **Infant mortality**: The high failure rate of a product early in its life.
    - **Random failure**: Occasional, unpredictable failures.
    - **Wear-out failure**: Failure caused by performance degradation after prolonged use.
    - **Burn-in**: A process of operating a product early in its life to eliminate potential defects.

When the failure rate is constant \(\lambda\), the reliability function follows an exponential distribution:

$$
R(t) = e^{-\lambda t}
$$

The **Mean Time Between Failures (MTBF)** is:

$$
\text{MTBF} = \frac{1}{\lambda}
$$

For non-repairable products, **MTTF (Mean Time To Failure)** is used.

!!! note "Term Explanation: Exponential Distribution, Mean Time Between Failures, Mean Time To Failure"
    - **Exponential distribution**: The life distribution under a constant failure rate.
    - **Mean Time Between Failures (MTBF)**: The average time between failures for repairable products.
    - **Mean Time To Failure (MTTF)**: The average time to failure for non-repairable products.

**Failure Mode and Effects Analysis (FMEA)** is a method for systematically identifying potential failures, assessing risks, and prioritizing improvements. Each failure mode is scored on three dimensions:

| Dimension | Symbol | Meaning | Typical Score |
|---|---|---|---|
| Severity | S | The severity of the failure consequence | 1–10 |
| Occurrence | O | The likelihood of the failure cause occurring | 1–10 |
| Detection | D | The ability of current controls to detect the failure | 1–10 |

The **Risk Priority Number (RPN)** is:

$$
\text{RPN} = S \times O \times D
$$

A higher RPN indicates a higher priority for implementing improvement actions.

!!! note "Term Explanation: Failure Mode, Severity, Occurrence, Detection, Risk Priority Number"
    - **Failure mode**: The specific manner in which a product fails.
    - **Severity**: The seriousness of the failure consequence.
    - **Occurrence**: The frequency with which a failure cause occurs.
    - **Detection**: The ability to detect the failure cause or mode.
    - **Risk Priority Number (RPN)**: The product of S, O, and D, used for risk ranking.

Example FMEA for a humanoid robot:

| Subsystem | Failure Mode | Potential Effect | S | O | D | RPN | Improvement Action |
|---|---|---|---|---|---|---|---|
| Knee joint harmonic drive | Flexspline fatigue crack | Joint lock, fall | 9 | 4 | 5 | 180 | Fatigue testing, periodic replacement |
| Battery pack | Cell thermal runaway | Fire, total robot destruction | 10 | 2 | 4 | 80 | BMS, thermal fuse, flame-retardant materials |
| Ankle 6-axis force sensor | Zero drift | Balance control instability | 8 | 5 | 4 | 160 | Online calibration, redundant sensing |
| Emergency stop circuit | Contact welding | Inability to safely stop | 10 | 2 | 3 | 60 | Dual-channel, self-test |
| Main controller | Software crash | Motion loss of control | 9 | 3 | 3 | 81 | Watchdog, safety monitor |

!!! note "Term Explanation: Flexspline Fatigue, Thermal Runaway, Zero Drift, Contact Welding, Watchdog"
    - **Flexspline fatigue**: Cyclic fatigue of the flexspline in a harmonic drive.
    - **Thermal runaway**: A chain reaction of uncontrolled temperature increase in a battery.
    - **Zero drift**: The shift of a sensor's zero point over time.
    - **Contact welding**: The welding together of relay contacts.
    - **Watchdog**: A circuit that monitors program execution and resets the system upon anomaly.

A **Reliability Block Diagram (RBD)** graphically represents the reliability logic relationships among system units:

- **Series system**: The system fails if any unit fails. Total reliability is the product of the reliabilities of each unit:
  $$
  R_s(t) = \prod_{i=1}^{n} R_i(t)
  $$
- **Parallel system**: The system fails only if all units fail. Total unreliability is the product of the unreliabilities of each unit:
  $$
  R_s(t) = 1 - \prod_{i=1}^{n} [1 - R_i(t)]
  $$

!!! note "Term Explanation: Reliability Block Diagram, Series System, Parallel System, Redundancy"
    - **Reliability Block Diagram (RBD)**: A diagram representing the reliability logic relationships of a system.
    - **Series system**: A system where all units must function correctly.
    - **Parallel system**: A system where at least one unit must function correctly.
    - **Redundancy**: The use of duplicate components to improve reliability.

**Redundancy design** is an important means of improving the safety of humanoid robots:

- **Active redundancy**: Multiple units operate simultaneously, e.g., dual encoders, dual-channel emergency stop.
- **Standby redundancy**: A backup unit is switched in when the primary unit fails.
- **Diverse redundancy**: Using different types of components to perform the same function, reducing the risk of common cause failures.

!!! note "Term Explanation: Active Redundancy, Standby Redundancy, Diverse Redundancy, Common Cause Failure"
    - **Active redundancy**: Redundancy where units operate in parallel simultaneously.
    - **Standby redundancy**: Redundancy where the backup unit is normally inactive.
    - **Diverse redundancy**: Redundancy using components based on different principles or from different sources.
    - **Common cause failure**: A failure where a single cause leads to the failure of multiple units simultaneously.

For components dominated by fatigue and wear, life is often described by the **Weibull distribution**:

$$
R(t) = \exp\left[-\left(\frac{t}{\eta}\right)^\beta\right]
$$

where \(\eta\) is the characteristic life, and \(\beta\) is the shape parameter. When \(\beta < 1\), it corresponds to the infant mortality period; \(\beta = 1\) reduces to the exponential distribution; \(\beta > 1\) corresponds to the wear-out period.

!!! note "Term Explanation: Weibull Distribution, Characteristic Life, Shape Parameter"
    - **Weibull distribution**: A flexible distribution for describing life data.
    - **Characteristic life**: The scale parameter in the Weibull distribution.
    - **Shape parameter**: The parameter that determines the shape of the Weibull distribution.

**Python Example: System Reliability and Redundancy Benefit**

The following code calculates the reliability of a series joint system composed of a motor, reducer, driver, and controller, and compares the reliability of a single-channel vs. a dual-channel redundant emergency stop circuit.

```python
import numpy as np
import matplotlib.pyplot as plt

## 개요
8.6.6 신뢰성 공학과 고장 모드 분석 관련 내용은 다음과 같습니다.
## 핵심 내용
#### 8.6.6 신뢰성 공학과 고장 모드 분석
휴머노이드 로봇은 장기 운전 중 기계적 마모, 전자 부품 노화, 소프트웨어 결함 및 환경 응력 등 다양한 고장 위험에 직면합니다. **신뢰성 공학(reliability engineering)**은 정량적 방법을 통해 시스템 신뢰성을 예측, 할당 및 개선하며, 전 생애 주기 비용을 절감하고 안전 운전을 보장하는 핵심 요소입니다[90][91][95].

!!! note "용어 설명: 신뢰성 공학, 고장, 생애 주기 비용, 환경 응력"
    - **신뢰성 공학(reliability engineering)**: 제품이 규정된 조건에서 규정된 시간 동안 기능을 수행할 수 있는 능력을 연구하고 향상시키는 학문.
    - **고장(failure)**: 제품이 규정된 기능을 상실하는 사건.
    - **생애 주기 비용(LCC)**: 제품의 전체 수명 주기 동안의 총 비용.
    - **환경 응력(environmental stress)**: 온도, 습도, 진동, 분진 등 외부 작용.

**신뢰성 함수** \(R(t)\)는 제품이 시간 \(t\) 동안 고장 나지 않을 확률로 정의됩니다:

$$
R(t) = P(T > t)
$$

여기서 \(T\)는 고장 전 시간입니다. 이에 대응하는 **누적 고장 분포 함수**는 \(F(t) = 1 - R(t)\)입니다. **고장률**(hazard rate 또는 failure rate) \(\lambda(t)\)는 다음과 같습니다:

$$
\lambda(t) = \frac{f(t)}{R(t)} = -\frac{d}{dt} \ln R(t)
$$

여기서 \(f(t) = dF/dt\)는 고장 확률 밀도입니다.

!!! note "용어 설명: 신뢰성 함수, 누적 고장 분포, 고장률, 고장 확률 밀도"
    - **신뢰성 함수(reliability function)**: 제품이 시간 t 동안 정상 작동할 확률.
    - **누적 고장 분포(cumulative distribution function, CDF)**: 시간 t 이전에 고장 날 확률.
    - **고장률(failure rate)**: 단위 시간당 고장 확률.
    - **고장 확률 밀도(probability density function, PDF)**: 고장 시간의 확률 밀도.

일반적인 전자 및 기계 제품의 고장률은 시간에 따라 **욕조 곡선(bathtub curve)**을 나타냅니다:

1. **초기 고장기(infant mortality)**: 고장률이 높으며, 일반적으로 제조 결함이나 조립 오류로 인해 발생하며, 번인(burn-in)을 통해 감소시킬 수 있습니다.
2. **우발 고장기(useful life)**: 고장률이 거의 일정하며, 제품의 주요 작동 단계입니다.
3. **마모 고장기(wear-out)**: 피로, 마모, 노화로 인해 고장률이 시간에 따라 증가합니다.

!!! note "용어 설명: 욕조 곡선, 초기 고장, 우발 고장, 마모 고장, 번인"
    - **욕조 곡선(bathtub curve)**: 고장률의 시간적 변화를 나타내는 U자형 곡선.
    - **초기 고장(infant mortality)**: 제품 초기 단계의 높은 고장률.
    - **우발 고장(random failure)**: 우발적이고 예측 불가능한 고장.
    - **마모 고장(wear-out failure)**: 장기 사용 후 성능 저하로 인한 고장.
    - **번인(burn-in)**: 초기 운전을 통해 잠재적 결함을 제거하는 과정.

고장률이 상수 \(\lambda\)일 때, 신뢰성 함수는 지수 분포를 따릅니다:

$$
R(t) = e^{-\lambda t}
$$

**평균 고장 간격(MTBF, Mean Time Between Failures)**은 다음과 같습니다:

$$
\text{MTBF} = \frac{1}{\lambda}
$$

수리 불가능한 제품의 경우 **MTTF(Mean Time To Failure)**를 사용합니다.

!!! note "용어 설명: 지수 분포, 평균 고장 간격, 평균 고장 전 시간"
    - **지수 분포(exponential distribution)**: 일정 고장률 하의 수명 분포.
    - **평균 고장 간격(MTBF)**: 수리 가능한 제품의 두 고장 사이 평균 시간.
    - **평균 고장 전 시간(MTTF)**: 수리 불가능한 제품의 고장 전 평균 시간.

**고장 모드 및 영향 분석(FMEA, Failure Mode and Effects Analysis)**은 잠재적 고장을 체계적으로 식별하고, 위험을 평가하며, 우선적으로 개선하는 방법입니다. 각 고장 모드는 세 가지 차원에서 평가됩니다:

| 차원 | 기호 | 의미 | 일반적인 점수 |
|---|---|---|---|
| 심각도 | S | 고장 결과의 심각한 정도 | 1–10 |
| 발생도 | O | 고장 원인 발생 가능성 | 1–10 |
| 검출도 | D | 현재 통제 조치가 고장을 검출하는 능력 | 1–10 |

**위험 우선 순위 수(RPN)**는 다음과 같습니다:

$$
\text{RPN} = S \times O \times D
$$

RPN이 높을수록 개선 조치를 우선적으로 취해야 합니다.

!!! note "용어 설명: 고장 모드, 심각도, 발생도, 검출도, 위험 우선 순위 수"
    - **고장 모드(failure mode)**: 제품 고장의 구체적인 표현 형태.
    - **심각도(severity)**: 고장 결과의 심각한 정도.
    - **발생도(occurrence)**: 고장 원인이 발생하는 빈도.
    - **검출도(detection)**: 고장 원인 또는 모드를 발견하는 능력.
    - **위험 우선 순위 수(RPN)**: S, O, D의 곱으로, 위험 순위를 매기는 데 사용.

휴머노이드 로봇의 일반적인 FMEA 예시:

| 하위 시스템 | 고장 모드 | 잠재적 영향 | S | O | D | RPN | 개선 조치 |
|---|---|---|---|---|---|---|---|
| 무릎 관절 하모닉 감속기 | 플렉스 스플라인 피로 균열 | 관절 고착, 넘어짐 | 9 | 4 | 5 | 180 | 피로 시험, 정기 교체 |
| 배터리 팩 | 셀 열 폭주 | 화재, 기기 전체 손상 | 10 | 2 | 4 | 80 | BMS, 열 퓨즈, 난연 재료 |
| 발목 6축 힘 센서 | 영점 드리프트 | 균형 제어 불안정 | 8 | 5 | 4 | 160 | 온라인 보정, 중복 센서 |
| 비상 정지 회로 | 접점 용착 | 안전 정지 불가 | 10 | 2 | 3 | 60 | 이중 채널, 자체 점검 |
| 주 제어기 | 소프트웨어 충돌 | 운동 제어 상실 | 9 | 3 | 3 | 81 | 워치독, 안전 모니터 |

!!! note "용어 설명: 플렉스 스플라인 피로, 열 폭주, 영점 드리프트, 접점 용착, 워치독"
    - **플렉스 스플라인 피로(flexspline fatigue)**: 하모닉 감속기 플렉스 스플라인의 반복 피로.
    - **열 폭주(thermal runaway)**: 배터리 온도가 통제 불능 상태가 되는 연쇄 반응.
    - **영점 드리프트(zero drift)**: 센서 영점이 시간에 따라 변하는 현상.
    - **접점 용착(contact welding)**: 릴레이 접점이 용융되어 붙는 현상.
    - **워치독(watchdog)**: 프로그램 실행을 모니터링하고 이상 시 리셋하는 회로.

**신뢰성 블록 다이어그램(RBD, Reliability Block Diagram)**은 시스템 각 구성 요소의 신뢰성 논리 관계를 그래픽으로 나타냅니다:

- **직렬 시스템**: 하나의 구성 요소가 고장 나면 시스템이 고장 납니다. 총 신뢰성은 각 구성 요소 신뢰성의 곱입니다:
  $$
  R_s(t) = \prod_{i=1}^{n} R_i(t)
  $$
- **병렬 시스템**: 모든 구성 요소가 고장 나야 시스템이 고장 납니다. 총 비신뢰성은 각 구성 요소 비신뢰성의 곱입니다:
  $$
  R_s(t) = 1 - \prod_{i=1}^{n} [1 - R_i(t)]
  $$

!!! note "용어 설명: 신뢰성 블록 다이어그램, 직렬 시스템, 병렬 시스템, 이중화"
    - **신뢰성 블록 다이어그램(RBD)**: 시스템 신뢰성 논리 관계를 나타내는 블록 다이어그램.
    - **직렬 시스템(series system)**: 모든 구성 요소가 정상 작동해야 하는 시스템.
    - **병렬 시스템(parallel system)**: 적어도 하나의 구성 요소가 정상 작동하는 시스템.
    - **이중화(redundancy)**: 반복 구성을 통해 신뢰성을 높이는 방법.

**이중화 설계**는 휴머노이드 로봇의 안전성을 높이는 중요한 수단입니다:

- **능동 이중화(active redundancy)**: 여러 구성 요소가 동시에 작동, 예: 이중 엔코더, 이중 채널 비상 정지.
- **대기 이중화(standby redundancy)**: 주 구성 요소가 고장 난 후 대기 구성 요소가 전환되어 작동.
- **이종 이중화(diverse redundancy)**: 동일 기능을 위해 다른 유형의 부품을 사용하여 공통 원인 고장 위험을 낮춤.

!!! note "용어 설명: 능동 이중화, 대기 이중화, 이종 이중화, 공통 원인 고장"
    - **능동 이중화(active redundancy)**: 병렬로 동시에 작동하는 이중화.
    - **대기 이중화(standby redundancy)**: 대기 구성 요소가 평소에는 작동하지 않음.
    - **이종 이중화(diverse redundancy)**: 다른 원리나 출처의 이중화를 사용.
    - **공통 원인 고장(common cause failure)**: 동일한 원인으로 여러 구성 요소가 동시에 고장 나는 현상.

피로와 마모가 지배적인 부품의 수명은 종종 **와이블 분포(Weibull distribution)**로 설명됩니다:

$$
R(t) = \exp\left[-\left(\frac{t}{\eta}\right)^\beta\right]
$$

여기서 \(\eta\)는 특성 수명, \(\beta\)는 형상 매개변수입니다. \(\beta < 1\)일 때는 초기 고장기에 해당하고, \(\beta = 1\)일 때는 지수 분포로 축소되며, \(\beta > 1\)일 때는 마모 고장기에 해당합니다.

!!! note "용어 설명: 와이블 분포, 특성 수명, 형상 매개변수"
    - **와이블 분포(Weibull distribution)**: 수명 데이터를 설명하는 유연한 분포.
    - **특성 수명(characteristic life)**: 와이블 분포의 척도 매개변수.
    - **형상 매개변수(shape parameter)**: 와이블 분포의 형태를 결정하는 매개변수.

**Python 예제: 시스템 신뢰성 및 이중화 효과**

다음 코드는 모터, 감속기, 드라이버, 제어기로 구성된 직렬 관절 시스템의 신뢰성을 계산하고, 단일 채널과 이중 채널 이중화 비상 정지 회로의 신뢰성을 비교합니다.

```python
import numpy as np
import matplotlib.pyplot as plt

## Overview
8.6.6 Reliability Engineering and Failure Mode Analysis related content is as follows.
## Content
#### 8.6.6 Reliability Engineering and Failure Mode Analysis
Humanoid robots face multiple failure risks during long-term operation, including mechanical wear, electronic aging, software defects, and environmental stress. **Reliability engineering** uses quantitative methods to predict, allocate, and improve system reliability, and is key to reducing life-cycle costs and ensuring safe operation[90][91][95].

!!! note "Terminology: Reliability Engineering, Failure, Life-Cycle Cost, Environmental Stress"
    - **Reliability engineering**: The discipline that studies and improves a product's ability to perform its required function under stated conditions for a specified period of time.
    - **Failure**: The event when a product loses its ability to perform a required function.
    - **Life-cycle cost (LCC)**: The total cost of a product over its entire life cycle.
    - **Environmental stress**: External factors such as temperature, humidity, vibration, and dust.

The **reliability function** \(R(t)\) is defined as the probability that a product survives without failure for a time \(t\):

$$
R(t) = P(T > t)
$$

where \(T\) is the time to failure. The corresponding **cumulative distribution function of failure** is \(F(t) = 1 - R(t)\). The **hazard rate** or **failure rate** \(\lambda(t)\) is:

$$
\lambda(t) = \frac{f(t)}{R(t)} = -\frac{d}{dt} \ln R(t)
$$

where \(f(t) = dF/dt\) is the failure probability density.

!!! note "Terminology: Reliability Function, Cumulative Distribution Function of Failure, Failure Rate, Failure Probability Density"
    - **Reliability function**: The probability that a product operates normally for a time \(t\).
    - **Cumulative distribution function (CDF)**: The probability of failure before time \(t\).
    - **Failure rate**: The probability of failure per unit time.
    - **Probability density function (PDF)**: The probability density of failure times.

The failure rate of typical electronic and mechanical products over time follows a **bathtub curve**:

1. **Infant mortality**: High failure rate, usually caused by manufacturing defects or assembly errors, can be reduced through burn-in.
2. **Useful life**: Failure rate is approximately constant; this is the main operating period of the product.
3. **Wear-out**: Failure rate increases over time, caused by fatigue, wear, and aging.

!!! note "Terminology: Bathtub Curve, Infant Mortality, Random Failure, Wear-out Failure, Burn-in"
    - **Bathtub curve**: A U-shaped curve showing the failure rate over time.
    - **Infant mortality**: The high failure rate of a product early in its life.
    - **Random failure**: Occasional, unpredictable failures.
    - **Wear-out failure**: Failures caused by performance degradation after prolonged use.
    - **Burn-in**: A process of operating a product early in its life to eliminate potential defects.

When the failure rate is constant \(\lambda\), the reliability function follows an exponential distribution:

$$
R(t) = e^{-\lambda t}
$$

The **Mean Time Between Failures (MTBF)** is:

$$
\text{MTBF} = \frac{1}{\lambda}
$$

For non-repairable products, **MTTF (Mean Time To Failure)** is used.

!!! note "Terminology: Exponential Distribution, Mean Time Between Failures, Mean Time To Failure"
    - **Exponential distribution**: The life distribution under a constant failure rate.
    - **Mean Time Between Failures (MTBF)**: The average time between failures for repairable products.
    - **Mean Time To Failure (MTTF)**: The average time to failure for non-repairable products.

**Failure Mode and Effects Analysis (FMEA)** is a method to systematically identify potential failures, assess risks, and prioritize improvements. Each failure mode is scored on three dimensions:

| Dimension | Symbol | Meaning | Typical Score |
|---|---|---|---|
| Severity | S | The severity of the failure consequence | 1–10 |
| Occurrence | O | The likelihood of the failure cause occurring | 1–10 |
| Detection | D | The ability of current controls to detect the failure | 1–10 |

The **Risk Priority Number (RPN)** is:

$$
\text{RPN} = S \times O \times D
$$

The higher the RPN, the more urgent the need for improvement actions.

!!! note "Terminology: Failure Mode, Severity, Occurrence, Detection, Risk Priority Number"
    - **Failure mode**: The specific way in which a product fails.
    - **Severity**: The seriousness of the failure consequence.
    - **Occurrence**: The frequency of the failure cause.
    - **Detection**: The ability to detect the failure cause or mode.
    - **Risk Priority Number (RPN)**: The product of S, O, and D, used for risk ranking.

Example FMEA for a humanoid robot:

| Subsystem | Failure Mode | Potential Effect | S | O | D | RPN | Improvement Action |
|---|---|---|---|---|---|---|---|
| Knee joint harmonic reducer | Flexspline fatigue crack | Joint lock-up, fall | 9 | 4 | 5 | 180 | Fatigue testing, periodic replacement |
| Battery pack | Cell thermal runaway | Fire, total robot destruction | 10 | 2 | 4 | 80 | BMS, thermal fuse, flame-retardant materials |
| Ankle 6-axis force sensor | Zero drift | Balance control instability | 8 | 5 | 4 | 160 | Online calibration, redundant sensing |
| Emergency stop circuit | Contact welding | Inability to stop safely | 10 | 2 | 3 | 60 | Dual-channel, self-test |
| Main controller | Software crash | Motion loss of control | 9 | 3 | 3 | 81 | Watchdog, safety monitor |

!!! note "Terminology: Flexspline Fatigue, Thermal Runaway, Zero Drift, Contact Welding, Watchdog"
    - **Flexspline fatigue**: Cyclic fatigue of the flexspline in a harmonic drive.
    - **Thermal runaway**: A chain reaction of uncontrolled temperature increase in a battery.
    - **Zero drift**: The shift of a sensor's zero point over time.
    - **Contact welding**: The welding together of relay contacts.
    - **Watchdog**: A circuit that monitors program execution and resets the system upon anomaly.

A **Reliability Block Diagram (RBD)** graphically represents the reliability logic relationships among system units:

- **Series system**: The system fails if any unit fails. Total reliability is the product of the reliabilities of each unit:
  $$
  R_s(t) = \prod_{i=1}^{n} R_i(t)
  $$
- **Parallel system**: The system fails only if all units fail. Total unreliability is the product of the unreliabilities of each unit:
  $$
  R_s(t) = 1 - \prod_{i=1}^{n} [1 - R_i(t)]
  $$

!!! note "Terminology: Reliability Block Diagram, Series System, Parallel System, Redundancy"
    - **Reliability Block Diagram (RBD)**: A diagram showing the reliability logic relationships of a system.
    - **Series system**: A system where all units must function for the system to function.
    - **Parallel system**: A system where at least one unit must function for the system to function.
    - **Redundancy**: The use of duplicate components to improve reliability.

**Redundancy design** is an important means of improving the safety of humanoid robots:

- **Active redundancy**: Multiple units operate simultaneously, e.g., dual encoders, dual-channel emergency stop.
- **Standby redundancy**: A backup unit is switched in when the primary unit fails.
- **Diverse redundancy**: Using different types of components to perform the same function, reducing the risk of common cause failures.

!!! note "Terminology: Active Redundancy, Standby Redundancy, Diverse Redundancy, Common Cause Failure"
    - **Active redundancy**: Redundancy where all units operate in parallel.
    - **Standby redundancy**: Redundancy where the backup unit is normally inactive.
    - **Diverse redundancy**: Redundancy using components based on different principles or from different sources.
    - **Common cause failure**: A failure where a single cause leads to the failure of multiple units simultaneously.

For components dominated by fatigue and wear, life is often described by the **Weibull distribution**:

$$
R(t) = \exp\left[-\left(\frac{t}{\eta}\right)^\beta\right]
$$

where \(\eta\) is the characteristic life, and \(\beta\) is the shape parameter. When \(\beta < 1\), it corresponds to the infant mortality period; \(\beta = 1\) reduces to the exponential distribution; \(\beta > 1\) corresponds to the wear-out period.

!!! note "Terminology: Weibull Distribution, Characteristic Life, Shape Parameter"
    - **Weibull distribution**: A flexible distribution for describing life data.
    - **Characteristic life**: The scale parameter in the Weibull distribution.
    - **Shape parameter**: The parameter that determines the shape of the Weibull distribution.

**Python Example: System Reliability and Redundancy Benefit**

The following code calculates the reliability of a series joint system consisting of a motor, reducer, driver, and controller, and compares the reliability of a single-channel vs. a dual-channel redundant emergency stop circuit.

```python
import numpy as np
import matplotlib.pyplot as plt
