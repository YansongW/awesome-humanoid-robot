---
id: ent_component_sumitomo_fine_cyclo
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 住友重工 Fine Cyclo 精密摆线减速机
  en: Sumitomo Fine Cyclo Precision Cycloidal Reducer
status: active
sources:
- id: src_sumitomo_catalog
  type: white_paper
  url: https://www.regal.dk/wp-content/uploads/2022/11/Fine-Cyclo_CAT_EN_991369_06_2021_WEB.pdf
- id: src_sumitomo_fca
  type: website
  url: https://emeia.sumitomodrive.com/en-gb/product/fine-cyclo-series-fc-type
- id: src_sumitomo_official
  type: website
  url: https://us.sumitomodrive.com/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 住友重工 Fine Cyclo 精密摆线减速机

## 概述

Fine Cyclo 是日本住友重机械工业（Sumitomo Heavy Industries）旗下 Sumitomo Drive Technologies 推出的精密摆线减速机系列。该系列将摆线针轮与行星传动相结合，具有高刚性、高扭矩、低背隙与耐冲击的特点，广泛应用于工业机器人、协作机器人关节、半导体设备及数控机床等高精度传动场景。

## 工作原理 / 技术架构

Fine Cyclo 采用摆线（cycloid）齿形啮合：输入轴带动偏心轴承，驱动一个或多个摆线轮在环形齿壳内滚动；摆线轮齿数与针齿齿数相差 1，形成多齿同时啮合，从而获得高减速比与零机械背隙。

单级减速比可表示为：

$$
i = \frac{z_{\text{ring}} - z_{\text{cycloid}}}{z_{\text{cycloid}}}
$$

其中 $z_{\text{ring}}$ 为针齿壳齿数，$z_{\text{cycloid}}$ 为摆线轮齿数。输出扭矩与输入扭矩的关系为：

$$
T_{\text{out}} = T_{\text{in}} \cdot i \cdot \eta
$$

$\eta$ 为传动效率，Fine Cyclo 典型效率 $\eta \ge 90\%$。其低背隙（Lost Motion）特性使 A 系列可达 $<1$ arcmin，C 系列典型值 $\le 3$ arcmin，满足伺服系统与机器人关节对定位精度的要求。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 住友重机械工业 / Sumitomo Drive Technologies |
| 类型 | 精密摆线减速机 |
| 系列 | A / C / DA / UA / T 等系列 |
| 框号范围 | 40–220 mm（系列范围） |
| 单级减速比 | 3:1 – 100:1（系列范围） |
| 额定输出扭矩 | 10–8,000 N·m（系列范围） |
| 背隙（Lost Motion） | $<1$ arcmin（A 系列典型）；$\le 3$ arcmin（C 系列典型） |
| 传动效率 | $\ge 90\%$ |
| 最高输入转速 | 5,000 rpm（部分系列）；A 系列可达 6,150 rpm |
| 防护等级 | IP54（典型） |
| 润滑方式 | 终身润滑油脂 |
| 价格 | 未公开 |

## 应用场景

- **协作机器人关节**：为关节模组提供高扭矩密度与低背隙传动。
- **工业机器人**：底座、肩部、腕部等需要高刚性与耐冲击的部位。
- **半导体/数控机床**：精密转台、分度机构、晶圆搬运模块。
- **自动化产线**：伺服压机、包装机械、精密定位平台。

## 供应链关系

在公司—产品—零部件网络中，Fine Cyclo 处于**精密传动零部件层**：

- **上游**：特种合金钢、精密轴承、润滑剂、密封件、铸件、电机。
- **自身位置**：`ent_company_sumitomo -- manufactures --> ent_component_sumitomo_fine_cyclo`。
- **下游**：工业机器人厂商、协作机器人厂商、人形机器人整机厂、半导体设备及数控机床制造商。

## 来源与验证

- Fine Cyclo 产品目录 PDF：https://www.regal.dk/wp-content/uploads/2022/11/Fine-Cyclo_CAT_EN_991369_06_2021_WEB.pdf
- Sumitomo Fine Cyclo A-Series FC Type 产品页：https://emeia.sumitomodrive.com/en-gb/product/fine-cyclo-series-fc-type
- Sumitomo Drive Technologies 官网：https://us.sumitomodrive.com/

减速比、扭矩范围、背隙与效率等核心数据来自住友重工公开产品手册；具体型号的选型报价需联系厂商或授权代理商确认。