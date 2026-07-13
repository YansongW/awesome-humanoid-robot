---
id: ent_component_weihong_ncstudio
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 维宏 NcStudio 雕刻机数控系统
  en: Weihong NcStudio CNC Engraving Control System
status: active
sources:
- id: src_weihong_official
  type: website
  url: https://www.weihong.com.cn
- id: src_stylecnc_weihong_ncstudio
  type: website
  url: https://www.stylecnc.cn/cnc-software/Weihong-Ncstudio-CNC-Controller-V5-5-60-ENGLISH-Setup.html
- id: src_gongkong_weihong_v10
  type: document
  url: http://fs.gongkong.com/files/technicalData/201211/2009112717261700001.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 维宏 NcStudio 雕刻机数控系统 / Weihong NcStudio CNC Engraving Control System

## 概述

维宏 NcStudio 是上海维宏电子科技股份有限公司开发的 PC-based 数控系统，面向广告雕刻机、木工雕刻机、小型 CNC 铣床及切割机。系统由上位机控制软件与 PCI/PCIe 运动控制卡组成，支持 3–5 轴联动、G 代码译码、刀具补偿、速度前瞻与样条插补，在国内雕刻机市场占有率较高。

## 工作原理 / 技术架构

NcStudio 采用“上位机 + 运动控制卡”两级架构。上位机软件完成加工程序解析、刀补、速度规划与插补计算；运动控制卡通过 PCI/PCIe 总线接收插补指令，由板载 FPGA 输出差分脉冲/方向信号驱动伺服或步进电机。系统同时采集编码器零点、伺服报警、伺服使能及限位等 I/O 信号，实现半闭环位置控制。

脉冲输出频率直接影响单轴极限速度。若脉冲当量为 \(p\)（mm/pulse），脉冲频率为 \(f_p\)，则理论最大进给速度为
\[
v_{\max}=f_p \cdot p.
\]
NcStudio 可选脉冲输出频率为 160 kbit/s 或 1 Mbit/s，典型控制精度标称为 0.001 mm。

## 关键参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | PC-based CNC 软件 + PCI/PCIe 运动控制卡 | 维宏产品手册 |
| 控制轴数 | 3–5 轴 | 产品手册 |
| 联动轴数 | 3/4/5 轴（视配置） | 产品手册 |
| 插补方式 | 直线 / 圆弧 / 样条 | 产品手册 |
| 脉冲输出频率 | 160 kbit/s 或 1 Mbit/s | StyleCNC 技术说明 |
| 控制精度 | 0.001 mm（参考） | 产品手册 |
| 接口 | PCI / PCIe / 以太网 | 产品手册 |
| 支持文件格式 | G 代码、PLT、DXF、ENG | StyleCNC 技术说明 |
| I/O 供电 | 24 VDC 外部 I/O | StyleCNC 技术说明 |
| 主轴转速设定 | 0–100 000 rpm（软件参数） | 产品手册 |
| 操作系统 | Windows 2000/XP/7/10/11 | 各版本说明 |

## 应用场景

- 木工雕刻与雕花
- 广告字牌、标识切割
- 模具加工与玉石雕刻
- 3C 结构件小批量加工

## 供应链关系

维宏股份（`ent_company_weihong`）制造 NcStudio 控制系统的软硬件。上游依赖工业计算机、FPGA/DSP、PCB、接插件、显示面板；下游客户为雕刻机、切割机及小型 CNC 机床制造商。在知识图谱中，`ent_company_weihong` 通过 `manufactures` 关系指向 `ent_component_weihong_ncstudio`，该组件作为控制核心集成于 CNC 整机。

## 来源与验证

- [维宏股份官网](https://www.weihong.com.cn)
- [维宏 NcStudio CNC 控制器 V5.5.60 设置说明](https://www.stylecnc.cn/cnc-software/Weihong-Ncstudio-CNC-Controller-V5-5-60-ENGLISH-Setup.html)
- [维宏四轴雕刻机控制系统 Ncstudio V10 用户手册](http://fs.gongkong.com/files/technicalData/201211/2009112717261700001.pdf)