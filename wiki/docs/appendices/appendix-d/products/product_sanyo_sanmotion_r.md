# 山洋 SANMOTION R 系列伺服电机 / Sanyo Denki SANMOTION R Series Servo Motor

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [山洋电气 / Sanyo Denki](../companies/company_sanyo_denki.md) |
| **产品类别** | 伺服电机 / 精密运动核心部件 |
| **发布时间** | 2010 年代持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.sanyodenki.com](https://www.sanyodenki.com) |

## 产品概述

山洋 SANMOTION R 系列是面向半导体、医疗、机器人与精密自动化设备的高性能交流伺服电机，功率覆盖 10 W 至 5 kW。

产品以小型化、高响应、低齿槽转矩和高分辨率编码器为特点，适配空间受限、高精度和高动态响应的应用场景。SANMOTION R 系列与山洋 R ADVANCED 伺服驱动器配套，可为人形机器人手指、腕部等精细关节提供可靠的精密运动方案。

## 产品图片

> Sanyo SANMOTION R：请访问 [官方资料](https://www.sanyodenki.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 交流伺服电机 | 山洋官网 |
| 机座号 | 20–130 mm（视型号） | 产品手册 |
| 额定功率 | 10 W – 5 kW | 产品手册 |
| 额定转速 | 1000–6000 rpm | 产品手册 |
| 最大扭矩 | 未公开（视型号） | 产品手册 |
| 编码器 | 20 位绝对值（参考） | 产品手册 |
| 防护等级 | IP65（部分型号） | 产品手册 |
| 绝缘等级 | Class F（参考） | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[山洋电气 / Sanyo Denki](../companies/company_sanyo_denki.md)
- **核心零部件/技术来源**：自研电机设计与制造工艺；稀土磁材、轴承、编码器芯片、铜线、绝缘材料外购。
- **下游应用/客户**：半导体设备商、医疗机器人厂商、人形机器人整机厂、协作机器人、精密定位平台。

## 知识图谱节点与关系

- 零部件实体：`ent_component_sanyo_sanmotion_r_motor`
- 制造商实体：`ent_company_sanyo_denki`
- 关键关系：
  - `rel_ent_company_sanyo_denki_manufactures_ent_component_sanyo_sanmotion_r_motor`（`ent_company_sanyo_denki` → `manufactures` → `ent_component_sanyo_sanmotion_r_motor`）
  - `ent_component_sanyo_sanmotion_r_drive` -- `uses` --> `ent_component_sanyo_sanmotion_r_motor`

## 应用场景

- **半导体设备**：晶圆传输、精密定位、贴片机。
- **医疗机器人**：手术机器人、康复机器人精细关节。
- **人形机器人**：手指、腕部、头部等空间受限关节。
- **协作机器人**：轻量化关节模组。

## 竞争对比

| 对比项 | 山洋 SANMOTION R | 安川 Σ-7 | 松下 A6 |
|--------|------------------|----------|---------|
| 定位 | 小型化高精度伺服电机 | 高端通用伺服 | 高速响应伺服 |
| 机座号 | 20–130 mm | 20–180 mm | 20–180 mm |
| 编码器 | 20 位绝对值（参考） | 24 位绝对值 | 23 位绝对值 |
| 核心优势 | 小型化、低噪音、高可靠 | 高端精度与可靠性 | 高速高响应 |

## 选购与部署建议

- 根据安装空间、负载惯量与动态响应要求选择机座号与转速。
- 建议配套山洋 R ADVANCED 系列驱动器以获得最佳性能。
- 人形机器人手指等应用需重点评估低速平稳性与编码器分辨率。

## 相关词条

- [制造商：山洋电气 / Sanyo Denki](../companies/company_sanyo_denki.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [山洋电气官网](https://www.sanyodenki.com)
2. 山洋 SANMOTION R 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)