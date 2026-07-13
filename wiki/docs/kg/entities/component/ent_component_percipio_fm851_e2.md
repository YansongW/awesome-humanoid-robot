---
id: ent_component_percipio_fm851_e2
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: 图漾科技 FM851-E2 工业 3D 相机
  en: Percipio FM851-E2 Industrial 3D Camera
sources:
- id: src_percipio_fm851_e2_official
  type: website
- title: Percipio FM851-E2 Product Page
  url: https://en.percipio.xyz/product-f-series/fm851-e2/
- id: src_percipio_fm851_e2_datasheet
  type: datasheet
- title: FM851-E2 Specifications V1.2
  url: https://en.percipio.xyz/product-f-series/fm851-e2/
- id: src_seeed_fm851
  type: datasheet
- title: Percipio 3D Camera FM851 Datasheet
  url: https://files.seeedstudio.com/products/114992602/FM851-EN.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-13'
  review_notes: Specifications from official product page and distributor datasheets;
    conflicting values across sources are noted.
---


# 图漾科技 FM851-E2 工业 3D 相机 / Percipio FM851-E2 Industrial 3D Camera

## 概述

图漾科技 FM851-E2 是一款面向工业自动化与机器人视觉的主动双目结构光 3D 相机，采用双 IR 相机、结构光投影器与 RGB 相机一体化设计，由板载 FPGA/视觉处理器完成深度计算与 RGB-D 对齐，主机端无需额外深度处理。相机通过千兆以太网输出点云、深度图、IR 图与彩色图，支持硬件触发与多机融合，适用于无序抓取、上下料、3D 检测等场景。

## 工作原理 / 技术架构

FM851-E2 基于主动双目（Active Stereo）原理：红外结构光投影器向场景投射编码图案，左右红外相机同步采集经物体表面调制的图像；通过三角测量与半全局/局部匹配算法计算视差，并转换为深度值。RGB 相机同步采集彩色图像，经 ISP 处理后与深度图进行配准，输出对齐的 RGB-D 帧。

深度 $Z$ 与视差 $d$ 的关系可近似表示为：
$$Z = \frac{f \cdot B}{d}$$
其中 $f$ 为等效焦距（像素），$B$ 为左右相机基线长度。基线越大，远距离精度越高，但近处盲区增大。

板载视觉处理器在 FPGA 内完成图像预处理、深度计算与点云生成，通过千兆网以 UDP/RTP 或 SDK 协议输出，降低主机 CPU/GPU 负载。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 深度技术 | 主动双目结构光 | 官方产品页 |
| 工作距离 | 0.7 m – 6.0 m | Percipio 官方 |
| 工作距离（经销商） | 0.2 m – 1.0 m / 0.7 m – 6.0 m | 不同渠道存在差异 |
| FOV（H/V） | 58° / 48° | Percipio 官方 |
| 深度分辨率 | 1280 × 960 | 官方 / Seeed datasheet |
| RGB 分辨率 | 1280 × 960 | Percipio 官方；部分经销商标注 2560×1920 |
| Z 向精度 | 1.78 mm @ 1 m；4.27 mm @ 1.5 m | Percipio 官方 |
| XY 精度 | 9.60 mm @ 1 m；14.41 mm @ 1.5 m | Percipio 官方 |
| 帧率 | 最高 26–30 fps（视分辨率） | Seeed / 经销商 |
| 基线 | 79 mm | Seeed datasheet |
| 数据接口 | RJ45 千兆以太网 | 官方产品页 |
| 电源/触发接口 | M8 A-Code，6-pin | 官方产品页 |
| 供电 | DC 24 V / PoE（IEEE 802.3af/at） | 官方产品页 |
| 功耗 | 2.9 W – 5.2 W | 官方 / Seeed |
| 防护等级 | IP54 | Percipio 官方；部分经销商标注 IP65 |
| 尺寸 | 124 × 28.6 × 86.8 mm | Percipio 官方 |
| 重量 | 410 g | Percipio 官方；部分经销商标注 500 g |
| 工作温度 | 0 °C – 45 °C | 官方 |
| 存储温度 | -10 °C – 55 °C | 官方 |
| SDK | PercipioSDK / OpenNI 2 / Halcon，C/C++ | Seeed datasheet |

## 应用场景

- **机器人无序抓取（Bin Picking）**：提供稠密点云与 6D 位姿估计输入。
- **工业上下料与装配**：毫米级 Z 向精度满足一般零件定位需求。
- **3D 检测与测量**：用于尺寸、缺陷与体积检测。
- **物流拆码垛**：中远距离大视野场景下的托盘与包裹识别。

## 供应链关系

- **制造商**：图漾科技 Percipio.XYZ（ent_company_percipio），中国上海 3D 机器视觉供应商。
- **上游关键物料**：CMOS 图像传感器、IR 激光投影器、工业以太网 PHY/FPGA、光学镜头、结构光算法 IP。
- **下游整机集成**：工业机器人、协作机器人、AGV/AMR、3D 检测与物流自动化设备厂商。
- **竞争/对标**：奥比中光、海康机器人、Intel RealSense、康耐视、基恩士。

## 来源与验证

- Percipio FM851-E2 官方产品页：https://en.percipio.xyz/product-f-series/fm851-e2/
- Seeed Studio FM851  datasheet：https://files.seeedstudio.com/products/114992602/FM851-EN.pdf
- 图漾科技官网：https://www.percipio.xyz