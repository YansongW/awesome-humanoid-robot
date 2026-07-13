---
id: ent_component_thk_lm_guide
schema_version: 1
type: component
'title:': THK LM 导轨
domain: 02_components
theoretical_depth: system
names:
  zh: THK LM 导轨
  en: THK LM Guide
status: active
sources:
- id: src_thk_lm_guide_official
  type: website
  url: https://www.thk.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# THK LM 导轨 / THK LM Guide

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [THK](../../../appendices/appendix-d/companies/company_thk.md) |
| **产品类别** | 直线运动 / LM 导轨 |
| **发布时间** | 1972 年首次推出，现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [THK 官网](https://www.thk.com) |

## 产品概述

THK LM 导轨是世界上首款直线运动导轨，开创了滚动直线运动技术。SHS、SSR、SNR/SNS 等系列产品以低摩擦、高刚性、高定位精度著称，是机床、半导体设备、机器人和自动化平台的核心导向部件。

THK 持续推出防尘、低发尘、耐腐蚀及智能监测版本，满足从洁净室到重切削的多元化需求。

## 产品图片

> THK LM 导轨：请访问 [官方资料](https://www.thk.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 导轨宽度 | 15–125 mm | 产品手册 |
| 精度等级 | 普通 / H / P / SP / UP | 产品手册 |
| 额定动载荷 | 依型号而定 | 产品手册 |
| 滑块型式 | 法兰 / 四方 / 宽幅 / 微型 | 产品手册 |
| 材质 | 轴承钢 / 不锈钢 | 产品手册 |
| 应用温度 | -20 °C – +80 °C（标准） | 产品手册 |
| 润滑 | 润滑脂 / 油润滑 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[THK](../../../appendices/appendix-d/companies/company_thk.md)
- **核心零部件/技术来源**：高品质轴承钢、滚珠、润滑脂、密封件、不锈钢材、精密磨削。
- **下游应用/客户**：机床厂商、半导体设备、机器人 OEM、汽车、医疗设备。

## 知识图谱节点与关系

- 零部件实体：`ent_component_thk_lm_guide`
- 制造商实体：`ent_company_thk`
- 关键关系：
  - `rel_ent_company_thk_manufactures_ent_component_thk_lm_guide`（`ent_company_thk` --> `manufactures` --> `ent_component_thk_lm_guide`）

## 应用场景

- **数控机床**：进给轴、刀库、工作台精密导向。
- **半导体设备**：晶圆搬运、光刻平台、检测平台。
- **人形机器人**：直线关节模组、躯干升降机构。
- **医疗设备**：影像设备、手术机器人定位平台。

## 竞争对比

| 对比项 | THK LM 导轨 | NSK | HIWIN |
|--------|-------------|-----|-------|
| 核心优势 | 发明者、品牌、全系列 | 轴承协同、洁净室方案 | 性价比、本土服务 |
| 交付周期 | 中等 | 中等 | 较短 |
| 服务响应 | 中等 | 中等 | 快速 |
| 价格水平 | 高端 | 高端 | 中端 |

## 选购与部署建议

- 根据负载方向与大小选择滑块型式与数量，高精度应用推荐 P 级以上并配对使用。
- 导轨安装基面需保证平面度与平行度，润滑脂补充周期视环境与运行速度而定。

## 参考资料

1. [THK 官网](https://www.thk.com)
2. [THK LM 导轨产品页](https://www.thk.com/products/lm_guide/)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)