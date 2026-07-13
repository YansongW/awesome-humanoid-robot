---
id: ent_product_shenyuan_mll_6axis_sensor
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 神源生 MLL 系列六维力传感器
  en: Shenyuansheng MLL Series 6-Axis Force Sensor
status: active
sources:
- id: src_shenyuan_mll_manual
  type: report
  url: https://img01.71360.com/file/read/www/M00/DD/67/wKj0iWKRfEqANO5NAG_wOPOpt2A835.pdf
- title: 六维力传感器产品手册 - 南京神源生智能科技有限公司
- id: src_shenyuan_mll_report
  type: report
  url: https://pdf.dfcfw.com/pdf/H3_AP202404151630231635_1.pdf
- title: 六维力传感器：人机末端力觉来源，行业格局变化在即 - 东方财富
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 神源生 MLL 系列六维力传感器 / Shenyuansheng MLL Series 6-Axis Force Sensor

## 概述

MLL 系列是南京神源生智能科技有限公司推出的铝合金模拟量六维力传感器，面向科学仪器、精密测试与机器人末端力控应用。该系列基于应变式弹性体结构，可同时测量三维力 $F_x/F_y/F_z$ 与三维力矩 $T_x/T_y/T_z$，具有高刚度、高分辨率与低耦合特性。

## 工作原理 / 技术架构

六维力传感器弹性体在受力时产生应变，粘贴在弹性体上的应变片组成惠斯通电桥，输出电压信号经放大、滤波与模数转换后，由解耦矩阵将六通道原始信号映射为笛卡尔力/力矩：

$$
\mathbf{F} = C \cdot \mathbf{V}
$$

其中 $\mathbf{F}=[F_x,F_y,F_z,T_x,T_y,T_z]^T$，$\mathbf{V}$ 为六通道电压向量，$C$ 为标定得到的 $6\times6$ 解耦矩阵。MLL 系列采用 16 芯航空插头模拟量差分输出，可配合 NST 系列数据采集器实现多协议通信。

## 关键参数表

| 参数 | 典型值（MLL 系列） |
|------|------------------|
| 力程 $F_x/F_y/F_z$ | 50 N / 100 N / 200 N / 500 N / 1000 N / 2000 N |
| 力矩程 $T_x/T_y/T_z$ | 2.5 N·m / 4 N·m / 6 N·m / 12 N·m / 20 N·m / 40 N·m |
| 材质 | 铝合金 |
| 尺寸 | Φ100 mm × 40–41 mm |
| 重量（含线缆） | 约 920–970 g |
| 防护等级 | IP65 |
| 过载能力 | 250% FS–400% FS（依型号） |
| 非线性 | ≤0.05% FS |
| 重复性 | ≤0.2% FS |
| 精度 | ≤0.2% FS |
| 零点漂移 | ≤0.02% FS/10 min |
| 温度零点漂移 | ≤0.2% FS/10°C |
| 工作温度 | 0°C–40°C |
| 输出接口 | 16 芯航空插头，模拟量差分输出 |
| 推荐工作电压 | DC 6 V |

## 应用场景

- 协作机器人拖动示教与力控装配
- 机器人打磨、抛光与去毛刺
- 科学实验与生物力学测试平台
- 航空航天零部件力学测试

## 供应链关系

神源生处于六维力传感器产业链中游，上游采购应变片、弹性体铝合金、信号调理芯片与接插件；下游客户包括协作机器人厂商、人形机器人本体企业、科研院所与自动化集成商。MLL 系列在神源生产品矩阵中定位为科研与精密测试级，与 GLL/GGT 等工业级系列互补。

## 来源与验证

参数主要来源于神源生《六维力传感器产品手册》（https://img01.71360.com/file/read/www/M00/DD/67/wKj0iWKRfEqANO5NAG_wOPOpt2A835.pdf）及东方财富行业研究报告（https://pdf.dfcfw.com/pdf/H3_AP202404151630231635_1.pdf）。具体型号参数以出厂标定证书为准。