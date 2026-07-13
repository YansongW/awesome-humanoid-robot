---
id: ent_company_boston_dynamics
schema_version: 1
type: company
'title:': Boston Dynamics
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 波士顿动力
  en: Boston Dynamics
aliases:
- 波士顿动力
- Boston Dynamics
status: active
sources:
- id: src_boston_dynamics_official
  type: website
  url: https://bostondynamics.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 波士顿动力 / Boston Dynamics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 波士顿动力 |
| **英文名** | Boston Dynamics |
| **总部** | 美国马萨诸塞州沃尔瑟姆 |
| **成立时间** | 1992 |
| **官网** | [https://bostondynamics.com](https://bostondynamics.com) |
| **供应链环节** | 人形/足式机器人整机厂、工业自动化 |
| **企业属性** | 现代汽车集团子公司 |
| **母公司/所属集团** | Hyundai Motor Group（现代汽车集团） |
| **数据来源** | Boston Dynamics 官网、产品规格页、公开报道 |

## 公司简介

波士顿动力源自 MIT 的机器人公司，以 Atlas、Spot 等腿式机器人闻名，2024 年发布全电动 Atlas，定位企业级工业人形机器人。

波士顿动力长期引领腿式机器人运动控制研究。新一代电动 Atlas 面向重载工业搬运与汽车装配场景，强调 360° 感知、IP67 防护与自主换电；Spot 四足机器人已实现规模化商业部署。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Atlas 人形机器人 | 企业级工业人形 | Atlas（电动版） | 汽车制造、重载搬运 |
| Spot 四足机器人 | 移动巡检平台 | Spot | 工业巡检、测绘、安防 |
| Stretch 物流机器人 | 仓储装卸 | Stretch | 卡车/货柜装卸 |

## 代表产品

### Boston Dynamics Atlas（电动版）

> Boston Dynamics Atlas（电动版）：请访问 [官方资料](https://bostondynamics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 190 cm（高） | Boston Dynamics 产品页 |
| 重量 | 约 90 kg | Boston Dynamics 产品页 |
| 自由度 | 56 | Boston Dynamics 产品页 |
| 负载/扭矩 | 瞬时 50 kg / 持续 30 kg | Boston Dynamics 产品页 |
| 速度/转速 | 未公开 | - |
| 续航 | 约 4 小时；支持自主换电 | Boston Dynamics 产品页 |
| 接口/通信 | Orbit 平台、Wi-Fi、企业系统集成 | 官方披露 |
| 价格 | 未公开（企业询价） | - |

**技术亮点**：全电动执行器、360° 视觉与触觉感知、连续关节运动、IP67 防护、自主换电与 Orbit 车队管理。

**应用场景**：现代汽车等制造企业的零件排序、重载搬运、户外与恶劣环境作业。


### Boston Dynamics Spot

> Boston Dynamics Spot：请访问 [官方资料](https://bostondynamics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 83 cm（高，站立） | Boston Dynamics 产品页 |
| 重量 | 约 32 kg | 公开资料 |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 约 14 kg | 公开资料 |
| 速度/转速 | 约 1.6 m/s | 公开资料 |
| 续航 | 约 90 分钟 | 公开资料 |
| 接口/通信 | Spot SDK、Ethernet、Wi-Fi | 官方披露 |
| 价格 | 约 74,500 USD 起 | 公开报价 |

**技术亮点**：四足机动、多传感器载荷、自主导航、成熟商业部署与开发者生态。

**应用场景**：工业设施巡检、建筑测绘、公共安全、科研教育。


## 供应链位置

- **上游关键零部件/材料**：现代 Mobis 供应链、电机/执行器、高性能传感器、NVIDIA Jetson 等计算模块。
- **下游客户/应用场景**：现代汽车集团、工业企业、能源/建筑客户、研究机构。
- **主要竞争对手/对标**：Tesla Optimus、Figure AI、Apptronik Apollo、Agility Robotics Digit。

## 知识图谱节点与关系

- 公司实体：`ent_company_boston_dynamics`
- 产品/平台实体：`ent_product_boston_dynamics_atlas_electric`、`ent_product_boston_dynamics_spot`
- 关键关系：
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_atlas_electric`（`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_atlas_electric`）
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_spot`（`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_spot`）

## 参考资料

1. [Boston Dynamics 官网](https://bostondynamics.com)
2. [Boston Dynamics Atlas 产品页](https://bostondynamics.com/products/atlas/)
3. [Boston Dynamics Spot 产品页](https://bostondynamics.com/products/spot/)