---
id: ent_company_thk
schema_version: 1
type: company
'title:': THK Co., Ltd.
domain: 02_components
theoretical_depth: system
names:
  zh: 日本帝业技凯
  en: THK Co., Ltd.
status: active
sources:
- id: src_thk_official
  type: website
  url: https://www.thk.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 日本帝业技凯 / THK Co., Ltd.

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 日本帝业技凯 |
| **英文名** | THK Co., Ltd. |
| **总部** | 日本东京 |
| **成立时间** | 1971 |
| **官网** | [https://www.thk.com](https://www.thk.com) |
| **供应链环节** | 直线运动系统 / LM 导轨 / 滚珠丝杠 / 执行器 |
| **企业属性** | 上市公司（TYO.6481）、国际品牌 |
| **母公司/所属集团** | 独立 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

全球直线运动系统先驱，LM 导轨（直线导轨）发明者与行业标准制定者。

THK 于 1972 年开发出世界上首款直线运动导轨（LM Guide），奠定了现代滚动直线运动技术基础。公司产品覆盖 LM 导轨、滚珠丝杠、执行器、交叉滚柱导轨、智能关节模组等，广泛应用于机床、半导体、机器人、汽车与医疗设备。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| LM 导轨 | 直线导轨龙头 | SHS/SSR/SNR/SNS 系列 | 机床、机器人 |
| 滚珠丝杠 | 精密传动 | BNK/BIF/BLK 系列 | 机床、自动化 |
| 执行器 | 机电一体模组 | SKR/VR 系列 | 机器人、3C |
| 智能关节 | 集成旋转/直线关节 | 未公开型号 | 人形机器人 |

## 代表产品

### LM 导轨 / LM Guide

> LM 导轨：请访问 [官方资料](https://www.thk.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 导轨宽度 | 15–125 mm | 产品手册 |
| 精度等级 | 普通 / H / P / SP / UP | 产品手册 |
| 额定动载荷 | 依型号而定 | 产品手册 |
| 滑块型式 | 法兰 / 四方 / 宽幅 / 微型 | 产品手册 |
| 材质 | 轴承钢 / 不锈钢 | 产品手册 |
| 应用温度 | -20 °C – +80 °C | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：低摩擦、高刚性、高定位精度，全球装机量最大的直线导轨品牌。

**应用场景**：数控机床、半导体设备、人形机器人关节、自动化平台。

### 滚珠丝杠 / Ball Screw

> 滚珠丝杠：请访问 [官方资料](https://www.thk.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 丝杠直径 | Ø4–Ø120 mm | 产品手册 |
| 导程 | 1–50 mm | 产品手册 |
| 精度等级 | C0–C10 | 产品手册 |
| 额定动载荷 | 依型号而定 | 产品手册 |
| 预紧方式 | 双螺母 / 单螺母偏移 | 产品手册 |
| 材质 | 轴承钢 / 不锈钢 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高精度磨制丝杠、螺母配置丰富，可配合 THK 导轨形成完整线性方案。

**应用场景**：高精度机床、人形机器人线性关节、医疗设备、电子制造。

## 供应链位置

- **上游关键零部件/材料**：高品质轴承钢、滚珠、润滑脂、密封件、不锈钢材
- **下游客户/应用场景**：机床厂商、半导体设备、机器人 OEM、汽车、医疗
- **主要竞争对手/对标**：NSK、HIWIN、Schneeberger、南京工艺、秦川机床

## 知识图谱节点与关系

- 公司实体：`ent_company_thk`
- 产品/零部件实体：`ent_component_thk_lm_guide`, `ent_component_thk_ball_screw`
- 关键关系：
  - `ent_company_thk` -- `manufactures` --> `ent_component_thk_lm_guide`
  - `ent_company_thk` -- `manufactures` --> `ent_component_thk_ball_screw`

## 参考资料

1. [THK 官网](https://www.thk.com)
2. [THK 年报/投资者关系](https://www.thk.com/ir/)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)