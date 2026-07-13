---
id: ent_product_zeiss_prismo
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 蔡司 PRISMO 三坐标测量机
  en: ZEISS PRISMO Coordinate Measuring Machine
status: active
sources:
- id: src_zeiss_prismo_official
  type: website
  url: https://www.zeiss.com/metrology/products/systems/cmm/bridge-type-cmms/prismo.html
- id: src_cmm_compass_prismo
  type: website
  url: https://cmm-compass.com/comparison/
- id: src_pmc_prismo_navigator
  type: website
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12473876/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 蔡司 PRISMO 三坐标测量机 / ZEISS PRISMO Coordinate Measuring Machine

## 概述

ZEISS PRISMO 是卡尔·蔡司（Carl Zeiss）工业测量事业部推出的旗舰桥式三坐标测量机（Coordinate Measuring Machine，CMM），以高速扫描、亚微米级精度与多传感器能力著称。PRISMO 广泛应用于航空航天、汽车、医疗器械、精密模具及科研计量等领域，可对复杂几何零件进行接触式扫描与光学测量，并支持自动化产线集成。

## 工作原理 / 技术架构

PRISMO 采用桥式结构：X 轴横梁在 granite 工作台上沿 Y 方向移动，Z 轴主轴带动测头在 X、Z 方向移动。三轴均采用空气轴承导向与直线电机或摩擦驱动，配合 ZEISS VAST 系列主动扫描测头，实现高速、低力的连续扫描。

测量误差按 ISO 10360 标准以最大允许长度测量误差 $MPE_{E0}$ 表示：

$$
MPE_{E0} = a + \frac{L}{K}
$$

其中：
- $a$ 为固定误差分量（µm），反映几何误差与测头系统误差；
- $L$ 为被测长度（mm）；
- $K$ 为长度相关误差分母，值越大表示随长度增加的误差越小。

对于标准 PRISMO，在 19–21 °C 条件下：

$$
MPE_{E0} = 0.9 + \frac{L}{350}\ \mu\text{m}
$$

在更宽的 15–30 °C 范围内，部分型号指标为：

$$
MPE_{E0} = 1.2 + \frac{L}{250}\ \mu\text{m}
$$

PRISMO Ultra 等高端配置可进一步达到：

$$
MPE_{E0} = 0.5 + \frac{L}{500}\ \mu\text{m}
$$

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 机型结构 | 桥式 CMM |
| 测量范围（X/Y/Z） | 700 × 900 × 500 mm 至 1600 × 4200 × 1400 mm（依配置） |
| 典型量程 | 900 × 1200 × 700 mm / 900 × 1500 × 650 mm |
| 长度测量误差 $MPE_{E0}$ | 0.9 + L/350 µm（19–21 °C 标准版） |
| 扫描探测误差 $MPE_{THP}$ | 1.7 µm（典型值，依测头） |
| 重复性 | 未公开具体数值 |
| 导向方式 | 四面空气轴承 |
| 驱动方式 | 直线电机 / 摩擦驱动（依型号） |
| 测头系统 | ZEISS VAST XT gold / VAST navigator 等主动扫描测头 |
| 测量软件 | ZEISS CALYPSO |
| 标尺系统 | ZERODUR 玻璃陶瓷光栅尺，分辨率 20 nm |
| 温度补偿 | CAA（Computer Aided Accuracy）动态补偿 |
| 工作温度 | 19–21 °C（标准精度）；15–30 °C（选配 HTG/fortis） |
| 最大扫描速度 | 500 mm/s（依配置） |
| 应用行业 | 航空航天、汽车、医疗、精密模具、能源 |

## 应用场景

- 航空发动机叶片、涡轮盘等复杂曲面高精度检测；
- 汽车动力总成、变速箱、底盘零部件几何尺寸与公差验证；
- 医疗器械植入物、手术器械精密测量；
- 精密模具、齿轮、轴承的形位公差与表面轮廓检测；
- 计量实验室基准传递与校准；
- 机器人零部件、关节减速器等关键部件的出厂检测。

## 供应链关系

`ent_product_zeiss_prismo` 由 `ent_company_zeiss`（卡尔·蔡司）设计制造，属于高端精密测量设备产品节点。其上游依赖 granite 基座、空气轴承、直线电机/驱动、ZERODUR 光栅尺、VAST 测头、传感器、控制软件与机械结构件；向下服务于航空航天、汽车、医疗及通用制造行业的质量控制与计量部门。在机器人产业链中，PRISMO 可用于 `ent_product_humanoid_robot_joint` 等关键零部件的精密尺寸与形位公差检测，保障整机装配精度。

## 来源与验证

- ZEISS 官网 PRISMO 产品页确认其为桥式 CMM，具备高速扫描、VAST 传感器、空气轴承与多传感器能力，并提供典型精度指标。
- CMM Compass 对比表明确列出 PRISMO 的 $MPE_{E0} = 0.9 + L/350\ \mu\text{m}$ 及 15–30 °C 工作温度范围。
- PMC 研究论文中使用的 ZEISS PRISMO Navigator 量程为 900 × 1200 × 700 mm，最大允许误差为 $0.9 + L/350\ \mu\text{m}$，与官方数据一致。
- 本条目未对未公开的重复性、具体型号尺寸等参数进行臆测。