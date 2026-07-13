---
id: ent_component_skf_ball_screw
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: SKF 滚珠丝杠
  en: SKF Ball Screw
sources:
- id: src_skf_ball_screw_catalog
  type: datasheet
- title: SKF Ball Screw Catalogue
  url: https://prema.com.pl/wp-content/uploads/2022/06/SKF_-_Sruby_toczne_2012.pdf
- id: src_skf_official
  type: website
- title: SKF 官网
  url: https://www.skf.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from SKF ball screw catalogue and company profile;
    missing values marked as 未公开.
---


# SKF 滚珠丝杠 / SKF Ball Screw

## 概述

SKF 滚珠丝杠是斯凯孚集团（SKF Group）线性运动产品线的核心传动元件，用于将旋转运动转换为高精度直线运动。SKF 提供从滚压到磨削、从标准到定制的全系列滚珠丝杠，直径覆盖 6 mm 至 80 mm，导程覆盖 1 mm 至 50 mm，精度等级可达 G5，广泛应用于数控机床、工业机器人、医疗定位平台、半导体设备与人形机器人线性关节。

## 工作原理与技术架构

滚珠丝杠由丝杠轴、螺母、滚珠及返向器组成，其基本工作原理为：

1. **滚动接触传动**：电机驱动丝杠旋转，螺母内的滚珠在丝杠滚道与螺母滚道之间滚动，带动螺母沿轴向移动。
2. **低摩擦高效率**：滚动摩擦系数远低于滑动丝杠，传动效率通常可达 90% 以上。
3. **预紧与间隙消除**：通过双螺母预紧或单螺母变位预紧消除轴向间隙，提高定位精度与轴向刚度。
4. **精度等级**：按 ISO 3408-3 标准，SKF 滚珠丝杠精度等级覆盖 G5 – G9，其中 G5 级定位精度与磨削滚珠丝杠相当。

关键运动学关系：

- **直线位移与旋转角度**：
  $$
  x = \frac{\theta}{2\pi} \cdot P_h
  $$
  其中 $x$ 为直线位移，$\theta$ 为旋转角度，$P_h$ 为导程。

- **直线速度与转速**：
  $$
  v = n \cdot P_h
  $$
  其中 $v$ 为直线速度，$n$ 为丝杠转速（rev/s）。

- **推力与输入扭矩**：
  $$
  F = \frac{2\pi \eta T}{P_h}
  $$
  其中 $F$ 为轴向推力，$T$ 为输入扭矩，$\eta$ 为传动效率。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 丝杠直径 | 6 mm – 80 mm（系列范围）| SKF catalog |
| 导程 | 1 mm – 50 mm（系列范围）| SKF catalog |
| 精度等级 | G5 – G9（ISO 3408-3）| SKF catalog |
| 预紧方式 | 双螺母预紧 / 单螺母变位预紧 | SKF catalog |
| 材质 | 轴承钢 / 不锈钢 | SKF catalog |
| 传动效率 | 约 90% 以上 | SKF catalog |
| 额定动载荷 | 依型号 | SKF catalog |
| 最大行程 | 依型号与安装方式 | SKF catalog |
| 工作温度 | −20 °C ~ +80 °C（典型）| SKF company profile |
| 润滑 | 油脂 / 油润滑 | SKF catalog |
| 价格 | 未公开 | - |

## 应用场景

- **数控机床进给轴**：高精度、高效率的直线进给传动。
- **工业机器人**：SCARA、直角坐标机器人的直线驱动。
- **人形机器人线性关节**：将电机旋转运动转换为膝、踝等关节的直线推拉运动。
- **医疗定位平台**：影像设备、手术机器人中的精密直线定位。
- **半导体设备**：晶圆传输、光刻工作台的高精度定位。
- **新能源设备**：锂电池生产设备中的精密驱动。

## 供应链关系

- **上游**：特种钢材（轴承钢/不锈钢）、润滑脂、密封材料、陶瓷球、保持架、精密磨削设备。
- **制造商**：斯凯孚集团（SKF Group）通过关系 `ent_company_skf -- manufactures --> ent_component_skf_ball_screw` 记录于知识图谱。SKF 同时提供 `ent_component_skf_linear_motion` 直线导轨与线性模组，形成系统级解决方案。
- **下游**：机床、工业机器人、医疗、半导体、新能源、机器人 OEM。主要竞争对手包括 Schaeffler、NSK、NTN、Timken、THK、博世力士乐等。

## 来源与验证

丝杠直径、导程、精度等级、预紧方式、材质等参数来自 SKF 滚珠丝杠型录。额定动载荷、最大行程及具体型号价格需根据选型软件或报价确定，已标注为未公开或依型号。