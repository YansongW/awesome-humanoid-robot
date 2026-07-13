---
id: ent_component_aurora_jft
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 奥普光电/禹衡光学 JFT 系列绝对式光栅尺
  en: Aurora Optics / Yuheng Optics JFT Series Absolute Linear Encoder
status: active
sources:
- id: src_ent_component_aurora_jft_1
  type: website
  url: https://pdf.dfcfw.com/pdf/H3_AP202210201579322747_1.pdf
- id: src_ent_component_aurora_jft_2
  type: website
  url: https://www.sohu.com/a/454244878_715708
- id: src_ent_component_aurora_jft_3
  type: website
  url: https://c.chuandong.com/698/news_241653.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 奥普光电/禹衡光学 JFT 系列绝对式光栅尺 / Aurora Optics / Yuheng Optics JFT Series Absolute Linear Encoder

## 概述

JFT 系列是长春禹衡光学有限公司（奥普光电控股子公司，深交所：002338）推出的高精度绝对式光栅尺，2019 年通过中国机床工具工业协会新产品鉴定并正式产业化。该系列产品采用游标码加 M 序列编解码、全阵列扫描、光电集成及大面积平行蓝光等技术，定位于高端数控机床全闭环控制，可替代海德汉 LCD100 等国际同类产品，是国内光栅尺国产替代的重要代表。

## 工作原理 / 技术架构

绝对式光栅尺在标尺上刻有绝对位置编码图案，读数头通过 LED 光源照射光栅，光电探测器接收调制光信号后，由 ASIC 解码芯片直接输出绝对位置值。游标码与 M 序列的组合使系统在通电瞬间即可确定唯一绝对位置，无需回零。其位置分辨力 $\Delta x$ 由光栅栅距 $g$ 与电子细分倍数 $N$ 决定：

$$
\Delta x = \frac{g}{N}
$$

JFT 系列分辨力可达 0.01 μm（10 nm），准确度达到 ±3 μm/m。重复性误差则反映了读数头在相同位置多次测量的一致性，公开资料给出 ±0.2 μm。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 产品类型 | 绝对式光栅尺 | 公开研报 |
| 最大量程 | 可达 4240 mm | 搜狐报道 |
| 标准截面尺寸 | 85.0 mm × 37.0 mm | 研报对比数据 |
| 标准测量范围 | 140 – 420 mm（与海徳汉 LCD100 对标款） | 研报对比数据 |
| 准确度 | ±3 μm/m | 搜狐报道 |
| 重复性 | ±0.2 μm | 搜狐报道 |
| 分辨力 | 0.01 μm / 0.005 μm / 0.0025 μm（可选） | 研报 |
| 最大运动速度 | 180 m/min | 研报 |
| 工作温度 | 0 – 50 °C | 研报 |
| 防护等级 | IP53 / IP64（通压缩空气） | 研报 |
| 通信接口 | BiSS-C、Drive-CliQ、Fanuc 协议等（以具体型号为准） | 公开资料 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **高端数控机床**：车床、铣床、磨床、加工中心的全闭环进给轴位置反馈，补偿丝杠热伸长与反向间隙。
- **坐标测量机**：高精度直线位移测量，提高重复测量精度。
- **半导体设备**：精密运动平台、晶圆传输机构的位置检测。
- **人形机器人与工业机器人**：直线模组、SCARA 手臂等需要高分辨率直线反馈的场合。

## 供应链关系

- **制造商**：奥普光电控股子公司禹衡光学 / Aurora Optics — Yuheng Optics（`ent_company_aurora_optics`）。
- **上游关键零部件/材料**：光学玻璃/金属光栅基板、蓝光 LED、光电探测器、ASIC 解码芯片、精密轴承、电子元器件。
- **下游客户/应用场景**：高端数控机床制造商、坐标测量机厂商、半导体设备商、机器人整机厂。
- **竞争/对标**：海德汉（Heidenhain）LCD100/LC 系列、雷尼绍（Renishaw）、发格（Fagor）、西班牙 MicroE。
- **知识图谱关系**：`ent_company_aurora_optics` — `manufactures` → `ent_component_aurora_jft`；该光栅尺可作为 `ent_product_humanoid_joint` 等直线运动模组的反馈元件。

## 来源与验证

1. [民生证券：国内光栅编码器龙头，布局高端数控迎业绩拐点](https://pdf.dfcfw.com/pdf/H3_AP202210201579322747_1.pdf)
2. [搜狐：禹衡光学布局高端传感器](https://www.sohu.com/a/454244878_715708)
3. [中国传动网：长春禹衡光学 2020 产品推介](https://c.chuandong.com/698/news_241653.html)
4. [附录 D 企业 Wiki：奥普光电](../../../appendices/appendix-d/companies/company_aurora_optics.md)

注：JFT 系列官方产品 datasheet 未在公开网络直接获取，上表参数来源于上市公司研报及行业公开报道，具体型号参数应以禹衡光学官方技术文件为准。