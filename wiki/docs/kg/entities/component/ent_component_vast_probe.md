---
id: ent_component_vast_probe
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: ZEISS VAST 扫描测头
  en: ZEISS VAST Scanning Probe
status: active
sources:
- id: src_zeiss_vast_gold
  type: website
  url: https://www.zeiss.com/metrology/en/systems/cmms/probes-sensors/tactile-probes/active-scanning-probes/vast-gold.html
- id: src_zeiss_vast_xt_gold
  type: website
  url: https://www.zeiss.si/metrology/products/sensors/on-cmm/tactile-scanning-probe/vast-xt-gold.html
- id: src_cmm_quarterly_rds_vast_xxt
  type: website
  url: https://cmm-quarterly.squarespace.com/articles/mechanics-of-the-zeiss-rds-vast-xxt-probe-head-an-engineering-analysis
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# ZEISS VAST 扫描测头 / ZEISS VAST Scanning Probe

## 概述

ZEISS VAST 是卡尔·蔡司（Carl Zeiss）工业质量解决方案旗下的主动式扫描测头系列，广泛应用于三坐标测量机（CMM）与机器人辅助检测系统。VAST 测头通过在扫描过程中维持恒定测力，实现对复杂曲面、自由曲面及精密结构的高速、高精度接触式测量。该系列包括 VAST gold、VAST XT gold、VAST XTR gold 与 VAST XXT 等型号，分别适配不同量程、精度与测针配置需求。

## 工作原理 / 技术架构

VAST 测头基于主动扫描（active scanning）原理：测头内部的传感器实时监测测针与工件之间的接触力，并通过闭环控制使测力保持恒定。当测针沿工件轮廓移动时，测头的三维位移传感器记录测针球心位置，从而反推出工件表面坐标。

- **恒力控制**：测力可在 50–1000 mN 范围内按工件材料与测针几何编程设定，降低薄壁或软质工件变形。
- **测针兼容性**：VAST gold 支持最长 800 mm、最重 800 g 的测针，以及非对称测针配置；配合 RDS  articulating 转接座时，测针角度可在 −135° 至 135° 范围内调节。
- **扫描效率**：配合 ZEISS navigator 技术，系统可根据目标精度自动推荐最佳扫描速度；FlyScan 与 QuickChange 功能可分别缩短扫描路径与自动换针时间。
- **动态性能**：集成碰撞保护与动态阻尼，支持连续扫描并降低意外碰撞导致的损坏风险。

测力与弯曲误差的关系可近似表示为
\[
\delta \approx \frac{F L^3}{3 E I}
\]
其中 \(F\) 为测力，\(L\) 为测针有效长度，\(E\) 为测针材料弹性模量，\(I\) 为测针截面惯性矩。恒力控制有助于将该误差保持在可预测范围内。

## 关键参数表

| 参数项 | VAST gold / XT gold | VAST XXT（配合 RDS） |
|---|---|---|
| 测力范围 | 50–1000 mN | 未公开 |
| 最大测针长度 | 800 mm | 未公开（通常用于小型测针） |
| 最大测针重量 | 800 g | 未公开 |
| 测针角度调节 | −135° 至 135°（配合 RDS） | 20,736 个离散位姿（2.5° 步进） |
| 扫描方式 | 连续扫描 + 单点测量 | 连续扫描 |
| 重复精度 | 未公开 | 未公开 |
| 工作温度 | 未公开 | 未公开 |

注：具体测量精度、重复性与温度规格需以蔡司官方校准证书与产品手册为准。

## 应用场景

- **高精度三坐标测量**：发动机缸体、涡轮叶片、齿轮箱壳体的形位公差检测。
- **机器人柔性检测**：将 VAST 测头集成于机器人末端，执行在线或近线尺寸检测。
- **逆向工程**：通过连续扫描获取自由曲面点云，用于 CAD 模型重建。
- **医疗与航空精密件**：髋臼杯、航空结构件等复杂几何的高精度测量。

## 供应链关系

- **上游**：高精度轴承、应变/位移传感器、测针球（红宝石/氮化硅）、电子控制板、精密机械结构件。
- **制造商**：卡尔·蔡司工业质量解决方案（ZEISS IQS）设计并制造 VAST 测头。
- **下游**：三坐标测量机整机厂、机器人集成商、汽车/航空/医疗制造企业质检部门。
- **图谱位置**：`ent_company_zeiss` → `manufactures` → `ent_component_vast_probe`；该组件通过 `used_in` 关系连接 CMM 与机器人检测单元。

## 来源与验证

- 测力范围、测针长度与重量等公开参数来自 ZEISS VAST gold 官方产品页。
- VAST XT gold 与 RDS/VAST-XXT 机械结构信息来自 ZEISS 区域官网及 CMM Quarterly 工程分析文章。
- 未公开项已在参数表中标注，未作臆测。