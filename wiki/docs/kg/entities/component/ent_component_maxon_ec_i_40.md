---
id: ent_component_maxon_ec_i_40
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Maxon EC-i 40 无刷直流电机
  en: Maxon EC-i 40 Brushless DC Motor
status: active
sources:
- id: src_maxon_eci40_datasheet
  type: datasheet
- title: maxon EC-i Program 2017-18 Datasheet
  url: https://www.servo.com.sg/sites/default/files/2018-01/ECI_Program_2017-18.pdf
- id: src_maxon_ec40_traceparts
  type: website
- title: TraceParts - Maxon EC 40 Specifications
  url: https://www.traceparts.com/en/product/maxon-motor-ag-ec-40-o40-mm-brushless-120-watt-with-hall-sensors
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自 maxon 公开产品手册与 TraceParts；缺失值标注为“未公开”。
---


# Maxon EC-i 40 无刷直流电机 / Maxon EC-i 40 Brushless DC Motor

## 概述

EC-i 40 是 maxon 推出的 Ø40 mm 铁芯无刷直流电机系列，具有高扭矩密度、低齿槽转矩和紧凑结构。该系列采用优化的磁路设计与多极内转子，机械时间常数低于 3 ms，最高转速可达 15000 rpm，常用于协作机器人关节、外骨骼、AGV 驱动轮、医疗手持工具与精密自动化设备。

## 工作原理 / 技术架构

无刷直流电机通过电子换向替代机械电刷，三相定子绕组产生旋转磁场，驱动永磁转子旋转。电磁转矩可近似表示为

$$
T = k_t \cdot I
$$

其中 $k_t$ 为转矩常数（单位 mNm/A），$I$ 为相电流。电机输出机械功率 $P$ 与转速 $n$、转矩 $T$ 的关系为

$$
P = T \cdot \omega = T \cdot \frac{2\pi n}{60}
$$

其中 $n$ 单位为 rpm，$\omega$ 为角速度（rad/s）。EC-i 系列采用铁芯绕组与钢法兰/外壳，兼具良好的散热与机械稳定性。

## 关键参数表

| 参数 | 典型值 / 范围 | 备注 |
|------|--------------|------|
| 机座直径 | Ø40 mm | maxon 产品手册 |
| 额定功率 | 50–130 W（系列范围）；100 W（典型） | 依绕组型号 |
| 额定扭矩 | 219–234 mNm（100 W 型） | 产品手册 |
| 堵转扭矩 | 2860–4330 mNm（100 W 型） | 产品手册 |
| 额定转速 | 3930–4340 rpm（100 W 型） | 产品手册 |
| 最高转速 | 10000 rpm（EC-i 40 系列） | 产品手册 |
| 效率 | 最高 89% | 产品手册 |
| 转矩常数 $k_t$ | 27.5–31 mNm/A（100 W 型） | 产品手册 |
| 转子惯量 | 44 g·cm²（100 W 型） | 产品手册 |
| 机械时间常数 | 0.48–0.64 ms | 产品手册 |
| 工作温度 | -40 ℃ ~ +125 ℃ | 产品手册 |
| 重量 | 约 390 g（标准配置） | 产品手册 |
| 价格 | 未公开 | - |

## 应用场景

- 协作机器人关节模组
- 外骨骼助力系统
- AGV/AMR 驱动轮
- 医疗手持工具与手术器械
- 光学平台与精密自动化设备

## 供应链关系

制造商为 Maxon Motor / maxon Group（`ent_company_maxon`）。上游关键原材料包括稀土永磁体（钕铁硼）、铜线、硅钢片、轴承与铝外壳；下游客户包括协作/人形机器人 OEM、医疗器械制造商与航空航天厂商。知识图谱中的关键关系为：`ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_i_40`。

## 来源与验证

本卡片参数引自 maxon EC-i 系列公开产品手册及 TraceParts 产品页。具体型号价格未公开。