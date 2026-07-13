---
id: ent_company_kistler
schema_version: 1
type: company
domain: 02_components
theoretical_depth: system
names:
  zh: 奇石乐（Kistler）
  en: Kistler
status: active
sources:
- id: src_ent_company_kistler_official
  type: website
  url: https://www.kistler.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 奇石乐（Kistler） / Kistler

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 奇石乐（Kistler） |
| **英文名** | Kistler |
| **总部** | 瑞士温特图尔（Winterthur） |
| **成立时间** | 1950 |
| **官网** | [https://www.kistler.com](https://www.kistler.com) |
| **供应链环节** | 力/压力/加速度/扭矩传感器、压电测量与测试系统 |
| **企业属性** | 全球压电测量技术龙头、家族控股企业 |
| **母公司/所属集团** | Kistler Holding AG |
| **数据来源** | Kistler 官网、产品 datasheet、年报 |

## 公司简介

Kistler 是全球领先的压电式力、压力与加速度测量技术供应商，产品广泛用于汽车测试、机加工、机器人与工业自动化。

奇石乐（Kistler）以压电测量技术起家，提供从传感器、测量链到测试系统的完整解决方案。其力传感器覆盖单轴、三轴及六分量测量，可在高频动态载荷下保持高精度与低串扰。近年来，Kistler 将微型化与高集成度传感器引入协作机器人与精密装配领域，为人形机器人关节力控、足端力反馈与产线测试提供关键传感单元。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 压电式力传感器 | 动态力/多轴力测量 | 9107B / 9129AA / 9311B | 机加工、汽车测试、机器人 |
| 应变式力传感器 | 静态/准静态力测量 | 9247B 系列 | 称重、装配、压装 |
| 压力/加速度传感器 | 燃烧/碰撞/振动测试 | 6041A / 8762A | 汽车、航空航天 |
| 测量系统 | 数据采集与分析 | KiDAq / LabAmp | 测试台架、研发 |

## 代表产品

### Kistler 9107B 三分量力传感器

> Kistler 9107B 三分量力传感器：请访问 [官方资料](https://www.kistler.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 压电式三分量力传感器 | 官网 |
| 测量方向 | Fx / Fy / Fz | 官网/datasheet |
| 力测量范围（Fx/Fy） | 未公开 | - |
| 力测量范围（Fz） | 未公开 | - |
| 灵敏度 | 未公开 | - |
| 刚度 | 高刚度设计 | 官网/datasheet |
| 固有频率 | 未公开 | - |
| 串扰 | < ±1%（典型） | 官网/datasheet |
| 工作温度 | 未公开 | - |
| 防护等级 | 未公开 | - |
| 输出接口 | 压电电荷输出 + 配套电荷放大器 | 官网/datasheet |
| 尺寸 | 紧凑型法兰安装 | 官网/datasheet |
| 重量 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：压电石英晶体传感元件，三向动态力同步测量，高刚度与高固有频率，适合高频切削力与机器人动态力控。

**应用场景**：机加工切削力监测、机器人末端力控、结构动态测试、汽车底盘与悬架测试、人形机器人足端力反馈。

### Kistler 6041A 压电式压力传感器

> Kistler 6041A 压电式压力传感器：请访问 [官方资料](https://www.kistler.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 压电式压力传感器 | 官网 |
| 量程 | 未公开 | - |
| 应用 | 燃烧分析、动态压力测试 | 官网 |
| 价格 | 未公开 | - |

**技术亮点**：适用于内燃机燃烧分析与高频动态压力测量的压电式传感器。

**应用场景**：汽车发动机测试、航空航天推进系统、工业过程监测。

## 供应链位置

- **上游关键零部件/材料**：压电石英晶体、高强度合金、精密机械加工、电子测量仪器、屏蔽线缆与接插件
- **下游客户/应用场景**：汽车测试、机床与刀具、航空航天、机器人 OEM、工业自动化
- **主要竞争对手/对标**：ATI Industrial Automation、HBM（Hottinger Brüel & Kjær）、PCB Piezotronics、奇石乐集团内品牌、国内坤维科技

## 知识图谱节点与关系

- 公司实体：`ent_company_kistler`
- 产品实体：`ent_product_kistler_9107b`
- 零部件实体：`ent_component_kistler_9107b_sensor`
- 关键关系：
  - `ent_company_kistler` -- `manufactures` --> `ent_product_kistler_9107b`
  - `ent_company_kistler` -- `manufactures` --> `ent_component_kistler_9107b_sensor`
  - `ent_product_kistler_9107b` -- `uses` --> `ent_component_kistler_9107b_sensor`

## 参考资料

1. [Kistler 官网](https://www.kistler.com)
2. [Kistler 9107B 三分量力传感器 产品/资料页](https://www.kistler.com/en/products/force-sensors/9107b)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)