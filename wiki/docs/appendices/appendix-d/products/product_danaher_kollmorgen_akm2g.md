# Kollmorgen AKM2G 伺服电机 / AKM2G

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [丹纳赫（Kollmorgen） / Danaher（Kollmorgen）](../companies/company_danaher.md) |
| **产品类别** | 伺服电机 |
| **发布时间** | 2018 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [丹纳赫（Kollmorgen） 官网](https://www.danaher.com) |

## 产品概述

Kollmorgen AKM2G 是丹纳赫旗下 Kollmorgen 推出的新一代同步伺服电机，提供更高的转矩密度与更丰富的配置选项。

电机涵盖 40 mm 至 180 mm 机座，可选多种反馈装置与绕组，配合 AKD 伺服驱动器可实现即插即用，广泛应用于机器人、半导体与精密自动化设备。

## 产品图片

> Kollmorgen AKM2G 伺服电机：请访问 [官方资料](https://www.danaher.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 同步伺服电机 | 官方资料 |
| 功率范围 | 0.03 kW ~ 7.2 kW（具体范围依型号） | 官方资料 |
| 峰值扭矩 | 0.16 Nm ~ 53 Nm | 官方资料 |
| 最高转速 | 8,000 rpm | 官方资料 |
| 框架尺寸 | 40 / 60 / 80 / 130 / 180 mm | 官方资料 |
| 反馈类型 | 旋变 / 增量式 / 单圈或多圈绝对值编码器 | 官方资料 |
| 防护等级 | IP65（可选轴封） | 官方资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[丹纳赫（Kollmorgen） / Danaher（Kollmorgen）](../companies/company_danaher.md)
- **核心零部件/技术来源**：自研电机设计与磁路优化；磁材、轴承、编码器、绕组绝缘材料外购。
- **下游应用/客户**：工业机器人、协作机器人、半导体设备、包装机械、人形机器人关节。

## 知识图谱节点与关系

- 产品实体：`ent_product_danaher_kollmorgen_akm2g`
- 制造商实体：`ent_company_danaher`
- 关键关系：
  - `ent_company_danaher` → `manufactures` → `ent_product_danaher_kollmorgen_akm2g`（关系文件：`rel_ent_company_danaher_manufactures_ent_product_danaher_kollmorgen_akm2g.md`）

## 应用场景

- **工业机器人**：关节伺服与外部轴。
- **协作机器人**：低惯量、高安全性的关节动力。
- **半导体设备**：晶圆搬运与精密定位。
- **人形机器人**：手臂、腿部、腰部关节动力单元。

## 竞争对比

| 对比项 | Kollmorgen AKM2G 伺服电机 | Panasonic MINAS A6 | Yaskawa Σ-7 |
|--------|---------------|--------|--------|
| 机座尺寸 | 40–180 mm | 未公开 | 未公开 |
| 峰值扭矩 | 0.16–53 Nm | 未公开 | 未公开 |
| 最高转速 | 8,000 rpm | 未公开 | 未公开 |
| 价格 | 未公开 | 未公开 | 未公开 |

## 选购与部署建议

在需要高转矩密度与定制绕组的机器人关节应用中，可优先考虑 AKM2G；选型时需确认安装法兰、反馈类型与驱动器匹配。

## 参考资料

1. [丹纳赫（Kollmorgen） 官网](https://www.danaher.com)
2. [Kollmorgen AKM2G 伺服电机 产品页](https://www.kollmorgen.com/en-us/products/motors/servo-motors/akm2g-servo-motors)
3. Kollmorgen AKM2G servo motor datasheet