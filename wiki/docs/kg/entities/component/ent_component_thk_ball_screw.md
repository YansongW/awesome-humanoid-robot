---
id: ent_component_thk_ball_screw
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: THK 精密滚珠丝杠
  en: THK Precision Ball Screw
sources:
- id: src_thk_official
  type: website
- title: THK Official Website
  url: https://www.thk.com
- id: src_thk_ball_screw_catalog
  type: datasheet
- title: THK Ball Screw Catalog
  url: https://www.savoietransmissions.com/wp-content/uploads/2019/06/vis-a-billes-THK.pdf
- id: src_faxiangongchang_ball_screw_2026
  type: report
- title: China Precision Bearing and Ball Screw Industry 2026
  url: https://faxiangongchang.com/en/reports/china-precision-bearing-screw-2026
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  review_notes: THK Ball Screw is a product family; exact per-model parameters vary
    by diameter, lead, length and accuracy grade.
---


# THK 精密滚珠丝杠 / THK Precision Ball Screw

## 概述

THK 精密滚珠丝杠是日本 THK 公司直线运动系统的核心产品之一，通过滚动接触将旋转运动转换为直线运动，具有高效率、低摩擦、微米级定位精度和长寿命等特点。产品涵盖精密研磨级（C0–C5）与轧制级（C7–C10）两大系列，广泛应用于数控机床、半导体设备、机器人线性关节、医疗设备和 3D 打印机。在人形机器人中，滚珠丝杠常与电机、导轨配合构成线性执行器（Linear Actuator），用于手指、腕部或腿部线性驱动。

## 工作原理 / 技术架构

滚珠丝杠由丝杠轴、螺母和循环滚珠组成。丝杠轴与螺母之间填充精密滚珠，滚珠沿螺旋滚道滚动并经由循环器返回起点，形成连续滚动接触。相比滑动丝杠，滚珠丝杠的摩擦系数显著降低（约 0.003），传动效率可达 90% 以上。

关键运动学关系：

- **导程与直线位移**：
  $$s = p \cdot n$$
  其中 $s$ 为螺母直线位移（mm），$p$ 为导程（mm/rev），$n$ 为丝杠旋转圈数。

- **定位精度**：
  由 JIS B 1192（ISO 3408）定义的精度等级 C0–C10 控制，核心指标为 300 mm 行程内的导程误差。C0 级误差 ≤ 3.5 µm/300 mm，C10 级 ≤ 210 µm/300 mm。

- **预紧方式**：
  双螺母垫片预紧、单螺母偏移预紧或端盖预紧，用于消除轴向间隙（backlash）。

THK 滚珠丝杠采用 SCM440 铬钼钢或 SUJ2 轴承钢制造，经表面淬火或渗碳处理，表面硬度达 58–62 HRC。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 丝杠直径范围 | 4 mm – 120 mm | THK 产品手册 |
| 导程范围 | 1 mm – 50 mm（公制） | THK 产品手册 |
| 精度等级 | C0 / C1 / C2 / C3 / C5 / C7 / C8 / C10 | JIS B 1192 / THK |
| 导程误差（C0） | ≤ 3.5 µm / 300 mm | 行业研报 |
| 导程误差（C3） | ≤ 12 µm / 300 mm | 行业研报 |
| 导程误差（C5） | ≤ 23 µm / 300 mm | 行业研报 |
| 导程误差（C7） | ≤ 52 µm / 300 mm | 行业研报 |
| 导程误差（C10） | ≤ 210 µm / 300 mm | 行业研报 |
| 传动效率 | 约 90% | THK 技术资料 |
| 材质 | SCM440 / SUJ2，表面硬度 58–62 HRC | THK 技术资料 |
| 预紧方式 | 双螺母 / 单螺母偏移 / 端盖预紧 | THK 产品手册 |
| 润滑 | 润滑脂或油润滑 | THK 技术资料 |

## 应用场景

- **数控机床进给轴**：C3/C5 级研磨丝杠实现微米级加工精度。
- **人形机器人线性关节**：配合 THK LM 导轨构成直线执行器，用于手指、腕部伸缩或腿部线性驱动。
- **半导体设备**：C0/C1 级超高精度定位平台。
- **医疗设备**：CT 床、手术机器人中的平稳、低噪音直线运动。
- **3D 打印机与自动化平台**：C7/C10 级轧制丝杠实现经济型定位。

## 供应链关系

- **制造商**：THK Co., Ltd.（ent_company_thk），日本东京上市公司，直线运动系统先驱。
- **上游关键物料**：高品质轴承钢、滚珠、润滑脂、密封件、不锈钢材。
- **下游整机集成**：机床厂商、半导体设备商、机器人 OEM、汽车、医疗、3C 自动化设备商。
- **竞争/对标**：NSK、HIWIN（上银）、Schneeberger、南京工艺、秦川机床。

## 来源与验证

- THK 官网：https://www.thk.com
- THK Ball Screw Catalog：https://www.savoietransmissions.com/wp-content/uploads/2019/06/vis-a-billes-THK.pdf
- China Precision Bearing and Ball Screw Industry 2026：https://faxiangongchang.com/en/reports/china-precision-bearing-screw-2026