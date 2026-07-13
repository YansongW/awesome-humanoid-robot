---
id: ent_company_schunk
schema_version: 1
type: company
'title:': SCHUNK GmbH
domain: 02_components
theoretical_depth: system
names:
  zh: SCHUNK GmbH
  en: SCHUNK GmbH
status: active
sources:
- id: src_schunk_official
  type: website
  url: https://www.schunk.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# SCHUNK GmbH / SCHUNK GmbH

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | SCHUNK GmbH |
| **英文名** | SCHUNK GmbH |
| **总部** | 德国劳芬（Lauffen am Neckar） |
| **成立时间** | 1945 |
| **官网** | [https://www.schunk.com](https://www.schunk.com) |
| **供应链环节** | 抓取系统 / 五指灵巧手 / 夹持技术 |
| **企业属性** | 家族企业、全球抓取技术领导者 |
| **母公司/所属集团** | SCHUNK GmbH & Co. KG |
| **数据来源** | 官网、产品手册、公开报道、WAIC 2026 报道 |

## 公司简介

全球领先的抓取系统、夹持技术与机器人末端执行器供应商。

SCHUNK 成立于 1945 年，总部位于德国劳芬，是全球夹持技术与抓取系统领域的领导者。公司产品覆盖机床夹具、自动化夹爪、协作机器人末端执行器以及 SVH 五指灵巧手。SCHUNK SVH 是全球首款通过 DGUV 认证、可用于协作操作的五指机械手，广泛应用于服务机器人、协作机器人及工业装配场景。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 平行夹爪 | 工业自动化 | PGN-plus | 机床上下料 |
| 协作机器人夹爪 | 人机协作 | Co-act EGP-C | 协作装配 |
| SVH 五指灵巧手 | 仿人多指 | SCHUNK SVH | 服务机器人、协作机器人 |

## 代表产品

### SCHUNK SVH 五指灵巧手 / SCHUNK SVH 5-Finger Hand

> SCHUNK SVH 五指灵巧手：请访问 [官方资料](https://www.schunk.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 总长 242 mm | 公开资料 |
| 重量 | 1.3 kg | 公开资料 |
| 手指数 | 5 | 公开资料 |
| 自由度 | 9（五指各 1 + 手腕 4） | 公开资料 |
| 关节数 | 20 | 公开资料 |
| 电机数 | 9 | 公开资料 |
| 供电电压 | DC 24 V | 公开资料 |
| 通信接口 | RS485 | 公开资料 |
| 建议负载 | 约 2.5 kg | 公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：首款通过 DGUV 认证的五指协作手、齿轮/连杆传动、防滑橡胶抓握面，适合安全人机协作。

**应用场景**：服务机器人抓取、协作机器人装配、医疗辅助、科研平台。


### Co-act EGP-C 协作夹爪 / SCHUNK Co-act EGP-C

> Co-act EGP-C 协作夹爪：请访问 [官方资料](https://www.schunk.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 自由度 | 1 | 产品手册 |
| 夹持力 | 未公开 | - |
| 供电电压 | DC 24 V | 产品手册 |
| 通信接口 | 未公开 | - |
| 防护等级 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：专为协作机器人设计的安全电动夹爪，具备力控与人机协作安全特性。

**应用场景**：协作装配、电子检测、包装搬运、人机共线。


## 供应链位置

- **上游关键零部件/材料**：电机、减速器、传感器、铝合金/钢构件、密封件
- **下游客户/应用场景**：汽车制造、电子装配、协作机器人、物流、医疗
- **主要竞争对手/对标**：Robotiq、Shadow Robot、大寰机器人、钧舵机器人

## 知识图谱节点与关系

- 公司实体：`ent_company_schunk`
- 产品/零部件实体：`ent_product_schunk_svh`
- 关键关系：
  - `ent_company_schunk` -- `manufactures` --> `ent_product_schunk_svh`

## 参考资料

1. [官网](https://www.schunk.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.schunk.com)（请按实际产品型号核对）