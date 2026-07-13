---
id: ent_company_zhaowei
schema_version: 1
type: company
'title:': Zhaowei Machinery & Electronics
domain: 02_components
theoretical_depth: system
names:
  zh: 兆威机电
  en: Zhaowei Machinery & Electronics
status: active
sources:
- id: src_zhaowei_official
  type: website
  url: https://www.zhaowei-china.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 兆威机电 / Zhaowei Machinery & Electronics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 兆威机电 |
| **英文名** | Zhaowei Machinery & Electronics |
| **总部** | 中国深圳 |
| **成立时间** | 2001 |
| **官网** | [https://www.zhaowei-china.com](https://www.zhaowei-china.com) |
| **供应链环节** | 微型驱动 / 微型电机 / 精密齿轮箱 |
| **企业属性** | 上市公司（SZ.003021）、国内品牌 |
| **母公司/所属集团** | 深圳市兆威机电股份有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

全球微型驱动系统龙头，为消费电子、汽车、医疗与机器人提供微型传动方案。

兆威机电专注于微型驱动系统，产品包括微型直流电机、精密齿轮箱、线性驱动模组与微型关节。公司在 3.4mm–38mm 直径范围内提供定制化微型传动解决方案，具备模具设计、齿轮加工和自动化组装能力。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 微型齿轮箱 | 精密减速传动 | 4mm–38mm 行星/蜗轮 | 手机、汽车、医疗 |
| 微型电机 | 直流有刷/无刷电机 | N20、N30、130 系列 | 消费电子、机器人 |
| 线性驱动模组 | 伸缩/升降模组 | PGM 系列 | 智能家居、汽车、机器人 |

## 代表产品

### 微型驱动系统 / Zhaowei Micro Drive System

> 微型驱动系统：请访问 [官方资料](https://www.zhaowei-china.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø4–Ø38 mm（系列范围） | 产品手册 |
| 重量 | 0.5–50 g | 产品手册 |
| 减速比 | 4:1 – 1,298:1 | 产品手册 |
| 额定扭矩 | 0.05–30 N·cm | 产品手册 |
| 空载转速 | 3,000–15,000 rpm | 产品手册 |
| 电机类型 | DC 有刷 / 无刷 | 产品手册 |
| 噪音水平 | ≤ 45 dB（部分型号） | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：超小体积、高减速比、低噪音、可定制输出轴与接口，适合机器人末端与微型关节。

**应用场景**：人形机器人手指/腕部、VR 手柄、汽车电子、医疗胰岛素泵、智能门锁。

### 微型关节模组 / Zhaowei Micro Joint Module

> 微型关节模组：请访问 [官方资料](https://www.zhaowei-china.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø10–Ø30 mm | 产品手册 |
| 重量 | 5–60 g | 产品手册 |
| 输出扭矩 | 0.1–5 N·cm | 产品手册 |
| 减速比 | 10:1 – 500:1 | 产品手册 |
| 供电电压 | DC 3–12 V | 产品手册 |
| 通信接口 | PWM / 模拟 | 产品手册 |
| 定位精度 | ±0.5° | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：电机+减速箱+输出机构一体化，结构紧凑，可直接集成到机器人手指与小型关节。

**应用场景**：仿生机器人手指、教育机器人、服务机器人头部/手部、智能家居执行器。

## 供应链位置

- **上游关键零部件/材料**：微型电机、POM/金属粉末冶金齿轮、轴承、轴、塑料粒子、磁材
- **下游客户/应用场景**：消费电子品牌、汽车 Tier 1、医疗器械、人形机器人整机厂、智能家居
- **主要竞争对手/对标**：Faulhaber、Maxon、尼得科、深圳拓邦、德昌电机

## 知识图谱节点与关系

- 公司实体：`ent_company_zhaowei`
- 产品/零部件实体：`ent_component_zhaowei_micro_drive`, `ent_component_zhaowei_micro_joint`
- 关键关系：
  - `ent_company_zhaowei` -- `manufactures` --> `ent_component_zhaowei_micro_drive`
  - `ent_company_zhaowei` -- `manufactures` --> `ent_component_zhaowei_micro_joint`

## 参考资料

1. [官网](https://www.zhaowei-china.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）