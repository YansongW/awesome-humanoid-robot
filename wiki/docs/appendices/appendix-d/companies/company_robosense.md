# 速腾聚创 / RoboSense

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 速腾聚创 |
| **英文名** | RoboSense |
| **总部** | 中国深圳 |
| **成立时间** | 2014 |
| **官网** | [https://www.robosense.ai](https://www.robosense.ai) |
| **供应链环节** | 激光雷达、机器人视觉、AI 感知芯片 |
| **企业属性** | 上市公司（HKEX: 2498）、AI 驱动的机器人技术公司 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、招股说明书、公开财报与新闻 |

## 公司简介

速腾聚创是全球激光雷达市占率领先企业，专注于数字激光雷达芯片与机器人感知解决方案。

速腾聚创依托自研 SPAD-SoC、VCSEL 与驱动芯片，提供覆盖 ADAS 与机器人领域的全固态数字激光雷达。其 E1R 等产品已在割草机器人、无人配送、人形机器人等场景大规模应用。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| M 系列 | 车规级 MEMS 激光雷达 | M1 / M1 Plus / M3 | 乘用车 ADAS |
| E 系列 | 全固态数字激光雷达 | E1 / E1R | 机器人、AMR、割草机、人形机器人 |
| 感知软件 | HyperVision | RS-LiDAR-Perception | 自动驾驶、机器人感知 |

## 代表产品

### 速腾聚创 E1R

> 速腾聚创 E1R：请访问 [官方资料](https://www.robosense.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 69.5 × 95 × 43 mm | 官方商店 |
| 重量 | 330 g（不含线） | 官方商店 |
| 深度技术 | 全固态数字激光雷达（SPAD-SoC + 2D VCSEL） | 官方 datasheet |
| FOV | 120° × 90° | 官方 datasheet |
| 探测距离 | 75 m（30 m @ 10% 反射率） | 官方 datasheet |
| 点频 | 260,000 点/秒（单回波）；520,000 点/秒（双回波） | 官方 datasheet |
| 角分辨率 | 0.625° × 0.625° | 官方 datasheet |
| 盲区 | <0.1 m | 官方 datasheet |
| 功耗 | <10 W | 官方 datasheet |
| 防护等级 | IP67 / IP6K9K | 官方 datasheet |
| 价格 | 约 USD 999 | 官方商店 |

**技术亮点**：全固态无机械扫描、超宽 FOV、小盲区、车规级可靠性，专为机器人前向/环视感知设计。

**应用场景**：人形机器人、AMR/AGV、割草机器人、无人配送、工业巡检。

### 速腾聚创 M1 Plus

> 速腾聚创 M1 Plus：请访问 [官方资料](https://www.robosense.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 深度技术 | MEMS 半固态激光雷达 | 官方 datasheet |
| FOV | 120°(H) × 25°(V) | 官方 datasheet |
| 探测距离 | 180 m @ 10% 反射率 | 官方 datasheet |
| 角分辨率 | 0.1° × 0.1° | 官方 datasheet |
| 点频 | 未公开 | 未公开 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：车规级 MEMS 方案、已在多款车型量产，适合乘用车前向主激光雷达。

**应用场景**：乘用车 ADAS、Robotaxi、干线物流。

## 供应链位置

- **上游关键零部件/材料**：VCSEL 激光器、SPAD-SoC 芯片、驱动 IC、光学镜片、MEMS 微镜
- **下游客户/应用场景**：乘用车 OEM（比亚迪、小鹏、吉利等）、人形机器人、AMR、无人配送、割草机器人
- **主要竞争对手/对标**：禾赛科技、览沃 Livox、华为、Ouster、Luminar、Innovusion

## 知识图谱节点与关系

- 公司实体：`ent_company_robosense`
- 产品实体：`ent_component_robosense_e1r`
- 产品实体：`ent_component_robosense_m1_plus`
- 关键关系：
  - `ent_company_robosense` -- `manufactures` --> `ent_component_robosense_e1r`
  - `ent_company_robosense` -- `manufactures` --> `ent_component_robosense_m1_plus`

## 参考资料

1. [官网](https://www.robosense.ai)
2. [产品资料与公开报道](https://www.robosense.ai)
3. [附录 D 产品目录](../index-products.md)