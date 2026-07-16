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


