---
id: ent_component_shenyuan_mll_sensor_core
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 神源生 MLL 系列六维力传感器核心零部件
  en: Shenyuansheng MLL Series 6-Axis Force Sensor Core Component
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_shenyuan_mll_datasheet
  type: datasheet
- title: 神源生 MLL 系列六维力传感器产品手册
  url: https://img01.71360.com/file/read/www/M00/DD/67/wKj0iWKRfEqANO5NAG_wOPOpt2A835.pdf
- id: src_shenyuan_mll_official
  type: website
- title: 神源生 MLL 系列六维力传感器产品页
  url: http://www.nbit6d.com/product/687.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数综合自神源生官方产品页与公开产品手册；缺失值标注为“未公开”。
---


# 神源生 MLL 系列六维力传感器核心零部件 / Shenyuansheng MLL Series 6-Axis Force Sensor Core Component

## 概述

神源生 MLL 系列六维力传感器核心零部件是南京神源生智能科技有限公司（NBIT）开发的铝合金模拟量六维力传感器的核心感知单元。该系列传感器同时测量三维力 $F_x$、$F_y$、$F_z$ 与三维力矩 $M_x$、$M_y$、$M_z$，具有刚度高、分辨率高、精度高的特点，面向科学仪器、精密测试、协作机器人拖动示教以及人形机器人手腕/脚踝力控等应用。南京神源生依托南京航空航天大学仿生结构与材料防护研究所，专注于多维力传感器、力测控技术与科学仪器的研发与产业化。

## 工作原理 / 技术架构

MLL 系列基于应变式测量原理。弹性体采用高强度铝合金结构，在六个测量通道上布置应变计。当外部力/力矩作用于弹性体时，结构产生微小形变，应变计电阻变化经惠斯通电桥转换为电压信号，再经信号放大、模数转换与多维解耦算法得到六维力/力矩输出。

六维力传感器的解耦模型可表示为

$$
\mathbf{F} = \mathbf{C} \cdot \mathbf{V}
$$

其中 $\mathbf{F} = [F_x, F_y, F_z, M_x, M_y, M_z]^\mathrm{T}$ 为待测力/力矩向量，$\mathbf{V}$ 为六通道电压输出向量，$\mathbf{C} \in \mathbb{R}^{6 \times 6}$ 为标定矩阵，由六维联合加载标定实验确定。

串扰（crosstalk）是衡量六维力传感器各通道耦合程度的关键指标，定义为对第 $j$ 个方向加载额定载荷时，其他方向输出变化与对应满量程之比的最大值：

$$
\varepsilon_{\mathrm{xt}} = \max_{i \neq j} \left( \frac{|\Delta V_i|}{\mathrm{FS}_i} \right) \times 100\%
$$

式中 $\Delta V_i$ 为第 $i$ 通道输出变化量，$\mathrm{FS}_i$ 为第 $i$ 通道满量程。MLL 系列通过结构优化与标定补偿，将耦合误差控制在较低水平。

## 关键参数表

| 参数 | 典型值 / 范围 | 备注 |
|------|--------------|------|
| 量程 $F_x/F_y/F_z$ | 50/50/100 N ~ 2000/2000/2000 N（依型号） | MLJ55002AA0 ~ MLJ92004AA0 |
| 量程 $M_x/M_y/M_z$ | 2.5/2.5/4 N·m ~ 40/40/40 N·m | 依型号 |
| 非线性 | ≤ 0.05% FS | 配合 NST 采集器 |
| 重复性 | ≤ 0.2% FS | 产品手册 |
| 精度 | ≤ 0.2% FS | 产品手册 |
| 耦合误差 | ≤ 1% FS | 产品手册 |
| 过载能力 | 250% FS ~ 400% FS | 依型号 |
| 分辨率 | 0.1% FS / 24 bit ADC | 配合 NST 采集器 |
| 供电 | DC 5–24 V | 产品手册 |
| 输出 | 模拟量 / USB / RS485（配采集器） | 产品手册 |
| 采样频率 | 最高 1000 Hz | 产品手册 |
| 工作温度 | 0 ℃ ~ +40 ℃ | 产品手册 |
| 重量 | 约 200–970 g（含线缆，依型号） | 产品手册 |
| 价格 | 未公开 | - |

## 应用场景

- 协作机器人拖动示教与碰撞检测
- 人形机器人手腕、脚踝力控与平衡调节
- 医疗手术机器人力反馈与精细操作
- 3C 装配、抛光打磨等工业力控
- 科学实验、生物力学测试与测力平台

## 供应链关系

制造商为南京神源生智能科技有限公司（`ent_company_shenyuan`）。该核心零部件被用于其产品实体 `ent_product_shenyuan_mll_6axis_sensor`，并进一步供应给人形机器人 OEM、协作机器人厂商以及科研院所。上游关键原材料包括航空铝合金、应变片、信号调理芯片、电缆与接插件；下游客户涵盖协作/人形机器人整机厂、医疗机器人企业与高校科研单位。知识图谱中的关键关系为：`ent_company_shenyuan` -- `manufactures` --> `ent_component_shenyuan_mll_sensor_core`。

## 来源与验证

本卡片参数综合自神源生官网 MLL 系列六维力传感器产品页（http://www.nbit6d.com/product/687.html）及公开产品手册。价格、特定型号详细尺寸等未公开参数已标注为“未公开”。