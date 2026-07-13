---
id: ent_component_heidenhain_rcn_8380
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 海德汉 RCN 8380 绝对式角度编码器
  en: Heidenhain RCN 8380 Absolute Angle Encoder
status: active
sources:
- id: src_ent_component_heidenhain_rcn_8380_1
  type: website
  url: https://www.e-motionsupply.com/Heidenhain_Absolute_Angle_Encoder_667590_01_p/667590-01.htm
- id: src_ent_component_heidenhain_rcn_8380_2
  type: website
  url: http://www.shzex.com/index.php?m=Content&a=index&id=2643
- id: src_ent_component_heidenhain_rcn_8380_3
  type: website
  url: https://www.ostbridge-tech.com/product/absolute-angle-encoder-with-integral-bearing-heidenhain-rcn-8000-rcn-8001.html
- id: src_ent_component_heidenhain_rcn_8380_4
  type: website
  url: https://www.heidenhain.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 海德汉 RCN 8380 绝对式角度编码器

## 概述

海德汉（Heidenhain）RCN 8380 是带内置轴承与集成定子联轴器的绝对式角度编码器，属于 RCN 8000 系列。它通过光电扫描玻璃码盘上的纯二进制图案，在通电或受到干扰后立即提供绝对位置值，无需轴先回零。该编码器以 ±2.0″ 的系统精度和 29 位单圈分辨率著称，广泛应用于高端数控转台、精密测量仪器、半导体设备及人形机器人关节的高精度角度反馈。

## 工作原理 / 技术架构

RCN 8380 采用光电绝对式扫描原理。光源照射刻有精细码道的玻璃码盘，光电探测器将透射/反射的光强分布转换为数字位置码。单圈位置数为 $2^{29} = 536\,870\,912$，对应的角分辨率（最小可分辨步距）为

$$
\Delta\theta = \frac{360°}{2^{29}} = 6.705 \times 10^{-7}° \approx 2.4\ \mu\mathrm{as}
$$

编码器同时输出增量信号，线数为 32,768 线/圈；增量信号经 4 倍频后可进一步提高插补分辨率。系统精度（system accuracy）±2.0″ 表示编码器输出角度与真实角度之间的最大允许误差，远优于一般工业旋转编码器。

信号接口采用 EnDat 2.2 同步串行接口，可同时传输绝对位置、增量信号与诊断数据；模拟输出为约 1 Vpp 正弦信号，截止频率 400 kHz。编码器内置温度传感器，可补偿热漂移。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 绝对式角度编码器，单圈 | e-Motion Supply / shzex |
| 系统精度 | ±2.0″ | 公开规格 |
| 每转位置数 | 536,870,912（29 bit） | 公开规格 |
| 线数 | 32,768 | 公开规格 |
| 输出代码 | 二进制 | 公开规格 |
| 模拟输出 | ~1 Vpp | 公开规格 |
| 数据接口 | EnDat 2.2 | 公开规格 |
| 供电电压 | 3.6–14 VDC | 公开规格 |
| 空心轴直径 | 60 mm（667596-01）/ 100 mm（667590-01） | 型号依赖 |
| 最大机械转速 | 500 r/min | 公开规格 |
| 防护等级 | IP64 | 公开规格 |
| 工作温度 | 0°C 至 +50°C | 公开规格 |
| 电气连接 | 法兰插座 Ultra-Lock 12 针 | 公开规格 |
| 重量 | 未公开 | 未公开 |
| 价格 | 未公开 | 经销商询价 |

## 应用场景

- **高端数控转台与五轴机床**：为 C 轴、A 轴提供高精度角度反馈，实现精密铣削与测量。
- **半导体与平板显示设备**：用于精密旋转台、对准平台与曝光系统。
- **人形机器人关节**：在高性能关节模组中替代普通光电编码器，提升位置环精度与低速稳定性。
- **天文望远镜与精密仪器**：用于方位/俯仰轴的高精度角位置测量。

## 供应链关系

RCN 8380 由 `ent_company_heidenhain` 设计制造。上游包括高精度玻璃码盘、光电扫描 ASIC、精密轴承、外壳铝材与电子元器件；下游面向高端伺服系统、数控机床、半导体设备与人形机器人关节制造商。在知识图谱中，该零部件可被 `ent_product_humanoid_robot_joint` 或具体整机关节模组使用，关系为 `used_in`。

## 来源与验证

- RCN 8380 的关键规格（±2.0″ 精度、29 位分辨率、32,768 线、EnDat 2.2、IP64）来自 e-Motion Supply、夕资工业设备与 Ostbridge 等渠道公布的产品型号数据。
- 空心轴直径随订货号变化（60 mm / 100 mm）在多个经销商页面中一致。
- 海德汉官网作为品牌与产品系列权威来源。