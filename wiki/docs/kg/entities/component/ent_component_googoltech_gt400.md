---
id: ent_component_googoltech_gt400
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 固高科技 GT-400 运动控制卡
  en: Googol Technology GT-400 Motion Control Card
status: active
sources:
- id: src_ent_component_googoltech_gt400_1
  type: website
  url: http://www.googoltech.com/pro_view-26.html
- id: src_ent_component_googoltech_gt400_2
  type: website
  url: http://www.googoltech.com/down-377.html
- id: src_ent_component_googoltech_gt400_3
  type: website
  url: https://pdf.directindustry.com/pdf/googol-technology-hk-limited-85573.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 固高科技 GT-400 运动控制卡 / Googol Technology GT-400 Motion Control Card

## 概述

固高科技 GT-400 系列是一款面向工业运动控制的多轴运动控制卡，可控制 2 轴或 4 轴伺服/步进电机，采用 PCI/ISA/PC104 总线或独立网络接口，广泛应用于机器人控制平台、数控机床、激光切割机、半导体设备及教育科研原型系统。GT-400 依托固高自研的运动控制算法库，支持点位、连续轨迹、电子齿轮等控制模式，并可与固高 GSHD 系列伺服驱动器、GUC 系列嵌入式控制器形成完整运动控制链路。

## 工作原理 / 技术架构

GT-400 通过板载 DSP/FPGA 实现多轴插补与伺服控制。控制周期为 200 μs，对应位置环刷新频率为 5 kHz。位置控制误差 $e(t)$ 经 PID 补偿及速度/加速度前馈后生成速度指令，再经编码器反馈闭环完成精确定位：

$$
u(t) = K_p e(t) + K_i \int e(t)\,dt + K_d \frac{de(t)}{dt} + K_v \dot{r}(t) + K_a \ddot{r}(t)
$$

其中 $r(t)$ 为规划轨迹，$K_v$、$K_a$ 分别为速度前馈与加速度前馈系数。GT-400 支持 ABZ 差分增量式编码器输入，编码器信号频率可达 8 MHz，并具备每轴专用原点、限位、驱动报警等光电隔离 I/O。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 控制轴数 | 2 轴 / 4 轴（视型号） | 固高科技官网 |
| 控制周期 | 200 μs | 产品手册 |
| 最大输出脉冲频率 | 1 MHz | 产品手册 |
| 控制模式 | 点位 / 连续轨迹 / 电子齿轮 | 产品手册 |
| 编码器输入 | 4 路 ABZ 差分，频率 8 MHz | 产品手册 |
| 通用数字 I/O | 16 路光电隔离输入/输出 | 产品手册 |
| 每轴专用 I/O | 原点、正负限位、驱动报警、伺服使能 | 产品手册 |
| 位置捕获 | 1 路探针输入同时捕获多轴位置 | 产品手册 |
| 总线接口 | PCI / ISA / PC104 / GE 运动控制器 / 网络接口（可选） | 产品手册 |
| 供电 | +5 V Icc=2 A；±12 V Icc=60 mA；+24 V/+12 V Icc=2 A | 产品手册 |
| 工作温度 | 0–60 °C | 产品手册 |
| 工作湿度 | 5%–90% RH（无凝露） | 产品手册 |
| 尺寸 | 185 mm × 122 mm | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **机器人控制平台**：作为上位控制器实现多轴联动、轨迹规划与伺服闭环，适用于 SCARA、六轴工业机器人及人形机器人原型开发。
- **数控机床与激光加工**：控制 XY 平台、切割头随动，实现高速、高精度的轮廓加工。
- **半导体设备**：晶圆传输、精密平台定位等对多轴同步要求较高的场景。
- **教育科研**：配合固高运动控制函数库与示例代码，用于运动控制算法验证与教学实验。

## 供应链关系

- **制造商**：固高科技 / Googol Technology（`ent_company_googoltech`）。
- **上游关键零部件/材料**：DSP/ARM 控制芯片、FPGA、PCI/ISA 总线接口芯片、光电隔离器件、PCB、接插件。
- **下游客户/应用场景**：工业机器人厂商、数控机床制造商、激光设备商、半导体设备商、高校与研究机构。
- **竞争/对标**：汇川技术、雷赛智能、柏楚电子、PMAC、Galil 等运动控制卡产品。
- **知识图谱关系**：`ent_company_googoltech` — `manufactures` → `ent_component_googoltech_gt400`；该控制卡常与 `ent_component_googoltech_gshd` 伺服驱动器配套使用。

## 来源与验证

1. [固高科技 GT 系列运动控制卡官方产品页](http://www.googoltech.com/pro_view-26.html)
2. [GT-400 系列运动控制卡 Datasheet 下载页](http://www.googoltech.com/down-377.html)
3. [DirectIndustry 固高科技产品手册目录](https://pdf.directindustry.com/pdf/googol-technology-hk-limited-85573.html)
4. [附录 D 企业 Wiki：固高科技](../../../appendices/appendix-d/companies/company_googoltech.md)