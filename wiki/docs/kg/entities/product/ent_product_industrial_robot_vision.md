---
id: ent_product_industrial_robot_vision
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 工业机器人视觉系统
  en: Industrial Robot Vision System
status: active
sources:
- id: src_cognex_insight3800
  type: website
  url: https://docs.cognex.com/is2d_2320/web/EN/is3800-manual/Content/Topics/specifications/specifications-3800.htm
- id: src_cognex_insight3800_vsk
  type: website
  url: https://www.vsk.com.tw/machine-vision-systems/cognex-in-sight-3800.html
- id: src_cognex_company
  type: website
  url: https://www.cognex.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 工业机器人视觉系统 / Industrial Robot Vision System

## 概述

工业机器人视觉系统是为机器人提供环境感知、目标定位与质量检测能力的机器视觉产品，通常由工业相机、光源、镜头、图像处理单元与通信接口组成。本词条以康耐视（Cognex）In-Sight 3800 旗舰智能相机为代表，给出工业机器人视觉系统的典型技术参数。

## 工作原理 / 技术架构

In-Sight 3800 采用全局快门 CMOS 传感器采集图像，内置多核处理器运行规则式与边缘学习（Edge Learning）AI 工具，可在设备端完成缺陷检测、OCR、装配验证与机器人引导。处理结果通过千兆以太网或数字 I/O 输出给 PLC/机器人控制器。多色照明与高速液态镜头（HSLL）可适应不同景深与表面特性。

视觉系统的空间分辨率 \(R\)（mm/pixel）由视野宽度 \(W\) 与图像水平像素数 \(N_x\) 决定：
\[
R=\frac{W}{N_x}.
\]
该参数直接决定系统可检测的最小特征尺寸。

## 关键参数表

| 规格项 | 数值（以 Cognex In-Sight 3800 为例） | 备注/来源 |
|--------|--------------------------------------|-----------|
| 产品定位 | AI + 规则型工业智能相机 | Cognex |
| 分辨率 | 1.4 / 3 / 5 / 8 / 12 / 16 MP 可选 | Cognex |
| 传感器 | 全局快门 CMOS | Cognex |
| 像素尺寸 | 3.45 µm / 2.74 µm（依型号） | Cognex |
| 帧率 | 最高 125 fps（1.4 MP 单色） | Cognex |
| 处理内存 | 4 GB 闪存 / 512 MB SDRAM | Cognex |
| 接口 | 2×GbE、USB-C、4 路高速输出 | Cognex |
| 供电 | 24 VDC ±10%，最大 2.0 A | Cognex |
| 防护等级 | IP67 | VSK |
| 工作温度 | 0–40 °C | Cognex |
| 检测速度 | 每分钟最多 2,500 个零件（标称） | VSK |
| 开发环境 | EasyBuilder / In-Sight Explorer | Cognex |

## 应用场景

- 机器人抓取引导与位姿估计
- 产线缺陷检测与装配验证
- 一维/二维码读取与追溯
- 分拣、涂胶与焊接质量监控

## 供应链关系

工业机器人视觉系统由康耐视、基恩士、海康机器人、奥普特等视觉厂商供应，上游包括 CMOS 传感器、镜头、LED 光源、FPGA/SoC 与工业连接器；下游为工业机器人 OEM、系统集成商与终端制造用户。在知识图谱中，`ent_product_industrial_robot_vision` 作为感知层产品，通常通过 `used_in` 关系连接机器人整机或自动化产线。

## 来源与验证

- [Cognex In-Sight 3800 Specifications](https://docs.cognex.com/is2d_2320/web/EN/is3800-manual/Content/Topics/specifications/specifications-3800.htm)
- [Cognex In-Sight 3800 机器视觉旗舰智慧相机](https://www.vsk.com.tw/machine-vision-systems/cognex-in-sight-3800.html)
- [Cognex Official](https://www.cognex.com)