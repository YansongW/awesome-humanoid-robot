---
id: ent_component_xiangming_ec_fan
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 祥明 EC 风机
  en: Xiangming EC Fan
status: active
sources:
- id: src_xiangming_ec_series
  type: website
  url: https://www.czxmdj.com/product/ecfan/
- id: src_xiangming_2024_report
  type: website
  url: https://pdf.dfcfw.com/pdf/H2_AN202504251684872562_1.pdf
- id: src_sina_xiangming_qa
  type: website
  url: https://finance.sina.com.cn/stock/roll/2024-08-15/doc-inckwhxp0625406.shtml
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 祥明 EC 风机 / Xiangming EC Fan

## 概述

祥明 EC 风机是常州祥明智能动力股份有限公司（Xiangming Intelligent Power）推出的电子换向（Electronically Commutated，EC）风机产品线。EC 风机将永磁无刷直流电机/永磁同步电机、驱动控制器与叶轮集成于一体，通过电子换向取代传统罩极电机或异步电机，实现高效率、宽调速与智能控制。祥明智能是国内微特电机与风机核心供应商，其 EC 风机覆盖暖通空调（HVAC）、数据中心、冷链、医疗设备及新能源汽车热管理等领域。

## 工作原理 / 技术架构

EC 风机采用外转子永磁同步/无刷直流电机结构，定子为三相分布式绕组，转子为表面贴装永磁体的叶轮毂。控制器根据霍尔传感器或无传感器算法检测转子位置，按六步换向或 FOC 方式对三相绕组通电，实现无刷运行。

风机气动功率与电机电功率的关系为：

$$
P_{\text{air}} = \eta_{\text{fan}} \cdot P_{\text{elec}} = \eta_{\text{fan}} \cdot U \cdot I
$$

其中 $U$、$I$ 为直流母线电压与电流，$\eta_{\text{fan}}$ 为风机整体效率（含电机与叶轮），优质 EC 风机效率可达 70 %–90 %。

调速通常采用 PWM 或 0–10 V 模拟量信号，转速 $n$ 与占空比 $D$ 近似成线性关系：

$$
n(D) = n_{\max} \cdot D
$$

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 电机类型 | 外转子永磁无刷直流/同步电机 |
| 换向方式 | 电子换向（EC） |
| 供电电压 | 12–48 VDC / 110–310 VDC / 100–230 VAC / 380–400 VAC（依系列） |
| 额定功率范围 | 数瓦至 5000 W（覆盖多系列） |
| 叶轮直径范围 | 60 mm ~ 500 mm |
| 控制方式 | PWM、0–10 V、RS-485 / Modbus（部分型号） |
| 防护等级 | IP20 ~ IP68（依型号） |
| 工作温度 | -30 °C ~ 60 °C（依型号） |
| 典型效率 | 70 % ~ 90 % |
| 调速范围 | 0 ~ 100 % 额定转速 |
| 噪声 | 依型号与转速，通常低于同风量交流风机 |
| 认证 | CE、UL、CCC、RoHS（依型号） |

## 应用场景

- 数据中心与通信基站精密空调与散热；
- 商用/家用 HVAC 系统新风与排风；
- 冷链物流冷藏车与冷柜换热；
- 新能源汽车电池包、电机控制器与座舱热管理；
- 医疗设备、服务器、工业控制柜散热；
- 机器人系统内部热管理与温控。

## 供应链关系

`ent_component_xiangming_ec_fan` 由 `ent_company_xiangming`（祥明智能）设计制造，属于热管理/机电零部件类别。其上游包括硅钢片、永磁体、漆包线、驱动 IC、功率器件、叶轮塑料/金属件等；下游面向 HVAC、数据中心、新能源汽车与工业设备整机厂商。在机器人产业链中，EC 风机可作为 `ent_product_humanoid_robot_joint` 或整机机柜的散热部件，保障关节驱动器与控制器的热可靠性。

## 来源与验证

- 祥明智能官网 EC 风机产品页列出了电压、功率、直径、防护与控制方式等产品系列信息。
- 祥明智能 2024 年年度报告披露 EC 风机、热管理风机在数据中心、新能源汽车、储能等领域的应用进展。
- 新浪财经投资者问答栏目中公司回复了 EC 风机在手订单与客户拓展情况。
- 由于官网未公开每一具体型号的完整风压-风量曲线与效率数据，表中效率与功率范围为行业公开典型值与系列概述信息，未对具体型号作臆测。