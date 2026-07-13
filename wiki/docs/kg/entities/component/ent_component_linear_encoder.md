---
id: ent_component_linear_encoder
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 线性编码器
  en: Linear Encoder
status: active
sources:
- id: src_ent_component_linear_encoder_heidenhain_catalog
  type: document
  url: https://www.heidenhain.de/fileadmin/pdf/zh_CN/Prospekte/PR_Linear_Encoders_for_Numerically_Controlled_Machine_Tools_ID571470_zh.pdf
- id: src_ent_component_linear_encoder_celiss
  type: website
  url: https://www.celiss.com/product/66898.html
- id: src_ent_component_linear_encoder_heidenhain_web
  type: website
  url: https://www.heidenhain.de/en/products/linear-encoders/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 线性编码器 / Linear Encoder

## 概述

线性编码器（Linear Encoder）是一种将直线位移转换为电信号的精密测量元件，常用于数控机床、机器人直线关节、半导体设备及高精度定位平台的位置反馈。按照测量原理可分为光电式、磁电式和感应式；高端数控系统普遍采用封闭式玻璃光栅尺，具有精度高、抗污染能力强和可靠性好的特点。

## 工作原理与技术架构

以 HEIDENHAIN LC 416/LC 496 封闭式绝对式直线光栅尺为例，其测量基准为 DIADUR 玻璃光栅尺带，栅距 $g=20\ \mu\text{m}$，通过光电扫描读取绝对位置信息。绝对式编码器在通电后即可输出唯一位置值，无需回零。

测量步距由栅距与电子细分倍数决定：

$$
\Delta x = \frac{g}{N_{\text{int}}}
$$

其中 $N_{\text{int}}$ 为细分倍数。当 $N_{\text{int}}=20\,000$ 时：

$$
\Delta x = \frac{20\ \mu\text{m}}{20\,000} = 0.001\ \mu\text{m} = 1\ \text{nm}
$$

玻璃材料的热膨胀系数约为：

$$
\alpha_{\text{therm}} \approx 8\times 10^{-6}\ \text{K}^{-1}
$$

使用安装架时略有增加。系统精度主要由光栅尺刻度误差、安装误差及热漂移共同决定。

位置数据通过 EnDat 2.2、DRIVE-CLiQ、Fanuc、Mitsubishi 或 Panasonic 串行接口传输，支持功能安全等级 SIL2 / PL d。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 代表型号 | HEIDENHAIN LC 416 / LC 496 | 封闭式绝对式 |
| 测量基准 | DIADUR 玻璃光栅尺 | 栅距 20 μm |
| 精度等级 | ±3 μm / ±5 μm | 全量程 |
| 测量长度 | 120 mm – 2040 mm | 更长需拼接 |
| 测量步距 | 0.001 μm（±3 μm）/ 0.010 μm（±5 μm） | 1 nm / 10 nm |
| 数据接口 | EnDat 2.2 / DRIVE-CLiQ / Fanuc / Mitsubishi / Panasonic | — |
| 供电电压 | DC 3.6 V – 14 V（EnDat）/ DC 10 V – 28.8 V（DRIVE-CLiQ） | — |
| 最大移动速度 | 180 m/min | — |
| 最大加速度 | ≤100 m/s² | — |
| 驱动力 | ≤5 N | — |
| 工作温度 | 0 ℃ ~ 50 ℃ | — |
| 防护等级 | IP53 / IP64（接入压缩空气 DA400） | — |
| 功能安全 | SIL2 / PL d | 部分型号 |
| 质量 | 0.2 kg + 0.55 kg/m | 不含安装架 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **数控机床**：进给轴全闭环位置反馈，提高轮廓精度。
- **机器人直线关节**：直线电机、滚珠丝杠模组的高精度定位。
- **半导体与平板显示**：光刻、检测、搬运平台的纳米级定位。
- **三坐标测量机与精密平台**：位移测量与误差补偿。

## 供应链关系

- **主要制造商**：HEIDENHAIN（德国）、Renishaw（英国）、NUMERIK JENA（德国）等。
- **上游关键物料**：玻璃/钢带光栅基体、LED/光电探测器、专用 ASIC、电缆、铝壳。
- **下游集成**：数控系统厂商、伺服驱动厂商、机器人整机厂、精密测量设备商。
- **知识图谱关系**：
  - `ent_company_heidenhain` — `manufactures` → `ent_component_linear_encoder`
  - `ent_component_linear_encoder` — `feedback_to` → 伺服驱动/数控系统节点

## 来源与验证

- HEIDENHAIN 直线光栅尺中文样本公布了 LC 416/LC 496 的栅距、精度等级、测量长度、测量步距、接口、供电、速度、加速度、防护等级、功能安全及质量参数。
- Celiss 产品页给出 LC 195P 的精度等级 3.0 μm、栅距 20 μm、测量步距 1 nm、Pana01 接口及电源 3.6–14 V。
- HEIDENHAIN 官网作为品牌与产品系列来源。