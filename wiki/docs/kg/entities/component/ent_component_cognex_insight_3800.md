---
id: ent_component_cognex_insight_3800
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 康耐视 In-Sight 3800 视觉系统
  en: Cognex In-Sight 3800 Vision System
status: active
sources:
- id: src_cognex_is3800_product
  type: website
  url: https://www.cognex.com/zh-cn/products/2d-machine-vision-systems/in-sight-3800
- id: src_cognex_is3800_datasheet
  type: white_paper
  url: https://www.cognex.cn/zh-cn/tools-and-resources/resource-center/in-sight-3800-datasheet
- id: src_cognex_docs
  type: website
  url: https://docs.cognex.com/is2d_2330/EN/IS3800_Reference_Manual.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 康耐视 In-Sight 3800 视觉系统

## 概述

In-Sight 3800 是美国康耐视（Cognex, NASDAQ: CGNX）推出的高性能工业视觉系统，集成了 AI 边缘学习（ViDi EL）与规则型视觉工具，可在同一硬件平台上完成缺陷检测、OCR、装配验证与零件分类等任务。该系统提供 1.4 MP 至 16 MP 六种分辨率型号，采用全局快门 CMOS 传感器，最高单色帧率可达 125 fps，并配备多色 RGBW+IR 照明、HDR+ 高动态范围及可选 HSLL 高速液态镜头，防护等级达 IP67。

## 工作原理 / 技术架构

In-Sight 3800 将图像采集、处理与通信集成于一体。其光学系统通过 C 接口镜头或 Cognex 高速液态镜头（HSLL）成像，传感器输出经 FPGA/SoC 预处理后进行 AI 推理或规则算法运算。

空间分辨率由视野（Field of View, FOV）与图像宽度决定：

$$
\text{分辨率} = \frac{\text{FOV}}{N_{\text{pixels}}}
$$

其中 $N_{\text{pixels}}$ 为图像对应方向的像素数。以 IS3801（1440×1080）为例，若水平视野为 144 mm，则水平分辨率约为 $0.1 \ \text{mm/pixel}$。

ViDi EL 边缘学习工具基于示例训练，无需大量标注数据即可实现分割、分类与读取任务；规则型工具则提供测量、计数、读码与逻辑运算能力。两者在同一平台上并行运行，满足高速产线的复杂检测需求。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | Cognex Corporation |
| 类型 | AI + 规则型工业视觉系统 |
| 分辨率 | 1.4 / 3 / 5 / 8 / 12 / 16 MP（6 种型号） |
| 传感器 | 1/2.3" – 1.1" CMOS，全局快门 |
| 最大帧率（全分辨率） | 125 fps（单色 IS3801）/ 52 fps（彩色 IS3801） |
| 像素尺寸 | 3.45 μm / 2.74 μm |
| 镜头接口 | C 接口，可选 HSLL 高速液态镜头 |
| 内部内存 | 4 GB |
| 图像处理内存 | 512 MB / 1 GB |
| 照明 | 多色 RGBW + IR，可选高级照明模块 |
| 动态范围 | HDR+ |
| 通信协议 | TCP/IP、PROFINET、EtherNet/IP、Modbus TCP、SLMP |
| 供电 | 24 V DC ± 10%，最大 2.0 A |
| 工作温度 | 0 °C – 40 °C |
| 防护等级 | IP67 |
| 裸机重量 | 约 570 g |
| 价格 | 未公开 |

## 应用场景

- **缺陷检测**：电子元器件、汽车零部件、食品包装表面瑕疵检测。
- **OCR 与追溯**：激光蚀刻、喷码、标签字符识别与序列号管理。
- **装配验证**：零部件有无、位置、方向与完整性检查。
- **机器人视觉导引**：工业机器人/人形机器人抓取定位与路径规划。

## 供应链关系

在公司—产品—零部件网络中，In-Sight 3800 处于**机器视觉零部件层**：

- **上游**：CMOS 图像传感器、光学镜头、LED/红外照明、FPGA/SoC 处理芯片、散热与结构件。
- **自身位置**：`ent_company_cognex -- manufactures --> ent_component_cognex_insight_3800`；`ent_component_cognex_insight_3800 -- used_in --> ent_product_industrial_robot_vision`。
- **下游**：汽车、消费电子、半导体、食品医药、物流仓储、机器人 OEM 及自动化集成商。

## 来源与验证

- Cognex In-Sight 3800 产品页：https://www.cognex.com/zh-cn/products/2d-machine-vision-systems/in-sight-3800
- Cognex In-Sight 3800 Datasheet：https://www.cognex.cn/zh-cn/tools-and-resources/resource-center/in-sight-3800-datasheet
- Cognex In-Sight 3800 Reference Manual：https://docs.cognex.com/is2d_2330/EN/IS3800_Reference_Manual.pdf

分辨率、帧率、传感器规格、接口与供电参数均来自官方 datasheet；价格需通过 Cognex 或其授权代理商询价。