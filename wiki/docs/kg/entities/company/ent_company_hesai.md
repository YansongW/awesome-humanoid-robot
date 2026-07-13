---
id: ent_company_hesai
type: company
'title:': 禾赛科技 / Hesai Technology
domain: 02_components
theoretical_depth: system
aliases:
- 禾赛科技
- Hesai Technology
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_hesai_official
  type: website
  url: https://www.hesaitech.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# hesai

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 禾赛科技 |
| **英文名** | Hesai Technology |
| **总部** | 中国上海 |
| **成立时间** | 2014 |
| **官网** | [https://www.hesaitech.com](https://www.hesaitech.com) |
| **供应链环节** | 激光雷达、3D 感知、自动驾驶与机器人 LiDAR |
| **企业属性** | 上市公司（NASDAQ: HSAI / HKEX: 2525） |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、招股说明书、公开财报与新闻 |

## 公司简介

禾赛科技是全球领先的激光雷达公司，产品覆盖车载 ADAS、自动驾驶与机器人领域。

禾赛科技具备芯片、光学、机械与算法全栈自研能力，拥有 Maxwell 智能制造中心。其 AT、ET、FT、QT 系列激光雷达已在多家头部车企量产上车，并为机器人与具身智能提供 3D 感知方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| AT 系列 | 车规级超高清远距激光雷达 | AT128 / AT512 / ATX | ADAS、自动驾驶 |
| ET 系列 | 超薄舱内远距激光雷达 | ET25 | 前向感知、乘用车 |
| FT/JT 系列 | 纯固态近距补盲/机器人激光雷达 | FT120 / JT 系列 | 机器人、自动驾驶补盲 |

## 代表产品

### 禾赛科技 ET25

> 禾赛科技 ET25：请访问 [官方资料](https://www.hesaitech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 厚度 | 25 mm | 官方新闻稿 |
| 深度技术 | 905 nm 车规级激光雷达 | 官方 datasheet |
| FOV | 120°(H) × 25°(V) | 官方新闻稿 |
| 探测距离 | 250 m @ 10% 反射率（无挡风玻璃）；225 m（挡风玻璃后） | 官方新闻稿 |
| 点频 | 超过 300 万点/秒 | 官方新闻稿 |
| 角分辨率 | 0.05° × 0.05° | 官方新闻稿 |
| 功耗 | 12 W | 官方新闻稿 |
| 噪声 | <25 dB（舱内） | 官方新闻稿 |
| 重量 | 未公开 | 未公开 |
| 接口 | 未公开 | 未公开 |

**技术亮点**：超薄 25 mm 机身、可置于挡风玻璃后、250 m 远距探测、低功耗低噪声，专为乘用车舱内设计。

**应用场景**：乘用车 ADAS、自动驾驶前向感知、高端机器人远距导航。

### 禾赛科技 AT128

> 禾赛科技 AT128：请访问 [官方资料](https://www.hesaitech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 通道数 | 128 | 官方 datasheet |
| FOV | 120°(H) × 25.4°(V) | 官方 datasheet |
| 探测距离 | 200 m @ 10% 反射率 | 官方 datasheet |
| 点频 | 153.6 万点/秒 | 官方 datasheet |
| 角分辨率 | 0.1° × 0.2° | 官方 datasheet |
| 扫描方式 | 一维转镜 + 芯片化收发 | 官方 datasheet |
| 激光波长 | 905 nm | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：半固态架构、车规级可靠性、高线束密度，已成为多家车企前向主激光雷达方案。

**应用场景**：乘用车 NOA、Robotaxi、干线物流、高端移动机器人。

## 供应链位置

- **上游关键零部件/材料**：905/1550 nm 激光器、SPAD/SiPM 接收芯片、扫描电机、光学镜片、ASIC 芯片
- **下游客户/应用场景**：乘用车 OEM（理想、长安、上汽等）、Robotaxi、物流机器人、无人配送、人形机器人
- **主要竞争对手/对标**：速腾聚创、览沃 Livox、华为、大疆 Livox、Velodyne/Ouster、Luminar

## 知识图谱节点与关系

- 公司实体：`ent_company_hesai`
- 产品实体：`ent_component_hesai_et25`
- 产品实体：`ent_component_hesai_at128`
- 关键关系：
  - `ent_company_hesai` -- `manufactures` --> `ent_component_hesai_et25`
  - `ent_company_hesai` -- `manufactures` --> `ent_component_hesai_at128`

## 参考资料

1. [官网](https://www.hesaitech.com)
2. [产品资料与公开报道](https://www.hesaitech.com)
3. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)