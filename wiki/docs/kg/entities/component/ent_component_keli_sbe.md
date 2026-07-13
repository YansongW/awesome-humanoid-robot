---
id: ent_component_keli_sbe
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 柯力传感 SBE 应变式传感器
  en: Keli Sensing Technology SBE Strain-Gauge Load Cell
status: active
sources:
- id: src_ent_component_keli_sbe_1
  type: website
  url: https://www.kelichina.com
- id: src_ent_component_keli_sbe_2
  type: website
  url: https://www.elecfans.com/yuanqijian/sensor/20180228640745_3.html
- id: src_ent_component_keli_sbe_3
  type: website
  url: http://www.lanse-china.com/news_show.asp?iid=986
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 柯力传感 SBE 应变式传感器 / Keli Sensing Technology SBE Strain-Gauge Load Cell

## 概述

柯力传感 SBE 系列为悬臂梁结构应变式称重/测力传感器，典型型号如 SBE-1t，适用于叉车秤、低平面台秤、平台秤及工业自动化称重系统。柯力传感（上交所：603662）是国内力学传感器市场占有率第一的企业，SBE 系列以其结构稳定、线性度与重复性良好、长期可靠性高等特点，广泛应用于工业衡器、自动化产线、汽车测试及质量控制场景。

## 工作原理 / 技术架构

SBE 传感器基于电阻应变效应：弹性体在载荷 $F$ 作用下产生应变 $\varepsilon = \Delta L / L$，粘贴在弹性体表面的应变片电阻发生相对变化

$$
\frac{\Delta R}{R} = K \varepsilon
$$

其中 $K$ 为应变片灵敏系数。多枚应变片组成惠斯通电桥，输出电压 $V_{\text{out}}$ 与供桥电压 $V_{\text{in}}$ 及应变成正比：

$$
V_{\text{out}} = V_{\text{in}} \cdot \frac{\Delta R}{4R} = V_{\text{in}} \cdot \frac{K \varepsilon}{4}
$$

通过标定，输出信号与载荷 $F$ 之间建立线性关系，实现质量或力的测量。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 传感器类型 | 悬臂梁式应变称重传感器 | 经销商资料 |
| 测量原理 | 电阻应变式 | 经销商资料 |
| 典型型号 | SBE-1t（额定载荷 1 t） | 公开资料 |
| 输出信号 | mV/V（毫伏/伏） | 应变式传感器通用标准 |
| 综合精度 | 未公开（按 OIML R60 C3 级常见设计） | 官方未披露 |
| 输入/输出阻抗 | 未公开 | 官方未披露 |
| 工作温度 | 未公开 | 官方未披露 |
| 防护等级 | 未公开 | 官方未披露 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **工业衡器**：叉车秤、平台秤、料斗秤、配料秤的核心测力元件。
- **自动化产线**：产品称重、分选、灌装量的在线检测与质量控制。
- **汽车测试**：零部件受力测试、装配力监测。
- **机器人与智能装备**：可作为辅助测力元件集成于末端执行器或称重系统。

## 供应链关系

- **制造商**：柯力传感 / Keli Sensing Technology（`ent_company_keli`）。
- **上游关键零部件/材料**：高精度应变片、合金钢/不锈钢弹性体、ASIC 信号调理芯片、密封材料、电缆。
- **下游客户/应用场景**：工业衡器制造商、自动化设备商、汽车 OEM、物流仓储系统、机器人集成商。
- **竞争/对标**：HBM、Vishay、梅特勒-托利多、中航电测、汉威科技等。
- **知识图谱关系**：`ent_company_keli` — `manufactures` → `ent_component_keli_sbe`；柯力传感六维力传感器 `ent_component_keli_kl6d_m30b` 用于 `ent_product_humanoid_robot_wrist`，SBE 系列则主要面向工业称重场景。

## 来源与验证

1. [附录 D 企业 Wiki：柯力传感](../../../appendices/appendix-d/companies/company_keli.md)
2. [电子发烧友网：悬臂梁结构传感器系列说明](https://www.elecfans.com/yuanqijian/sensor/20180228640745_3.html)
3. [兰瑟称重传感器：柯力 SBE-1t 产品信息](http://www.lanse-china.com/news_show.asp?iid=986)

注：柯力传感官方未公开 SBE 系列完整 datasheet，上表除型号与结构类型外，具体电气与精度参数标注为“未公开”，建议通过柯力传感官方渠道索取选型手册。