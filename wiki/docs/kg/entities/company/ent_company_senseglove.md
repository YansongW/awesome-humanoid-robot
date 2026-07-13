---
id: ent_company_senseglove
type: company
'title:': SenseGlove（感融科技） / SenseGlove B.V.
domain: 02_components
theoretical_depth: system
aliases:
- SenseGlove B.V.
- SenseGlove（感融科技）
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_senseglove_official
  type: website
  url: https://senseglove.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# senseglove

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | SenseGlove（感融科技） |
| **英文名** | SenseGlove B.V. |
| **总部** | 荷兰代尔夫特 |
| **成立时间** | 2017 |
| **官网** | [https://senseglove.com](https://senseglove.com) |
| **供应链环节** | 力反馈手套、触觉反馈、遥操作人机接口 |
| **企业属性** | 初创公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | SenseGlove 官网、产品页、公开报道 |

## 公司简介

SenseGlove 是一家专注于力反馈与触觉反馈手套的荷兰初创公司，产品主要用于虚拟现实培训、遥操作机器人、医疗康复与工程仿真。其 Nova 系列无线手套能够为每只手指提供主动阻力反馈与振动触觉反馈，使用户在虚拟或远程环境中感知抓取力、形状与纹理。

SenseGlove 的力反馈方案被广泛应用于人形机器人遥操作、手术机器人训练、核电与太空遥操作等场景，可显著降低训练成本并提高操作精度。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Nova 系列 | 无线力反馈手套 | [SenseGlove Nova 2](../../../appendices/appendix-d/products/product_senseglove_nova_2.md) | 遥操作、VR 培训、医疗康复 |
| DK1/Exoskeleton | 早期外骨骼式力反馈手套 | SenseGlove DK1 | 研究、仿真 |
| 软件 SDK | 手部追踪与力反馈集成 | SenseGlove Unity/Unreal SDK | 开发者、系统集成商 |

## 代表产品

### SenseGlove Nova 2

> SenseGlove Nova 2：请访问 [官方资料](https://senseglove.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 无线力反馈手套 | SenseGlove 官网 |
| 反馈方式 | 4 主动阻力执行器 + 振动触觉反馈 | 产品页 |
| 手指覆盖 | 拇指、食指、中指、无名指 | 产品页 |
| 追踪 | 兼容 SteamVR / Quest 追踪器（需额外追踪器） | 产品页 |
| 无线连接 | 蓝牙 / 2.4 GHz 专有协议 | 产品页 |
| 电池续航 | 约 2–3 小时 | 产品页/未公开精确值 |
| 重量 | 约 320 g（单只，未公开精确值） | 公开资料 |
| 软件开发 | Unity、Unreal、C++ SDK | 官网 |
| 价格 | 未公开 | 商务报价 |

**技术亮点**：紧凑无线设计、4 路主动力反馈、高保真振动触觉、即插即用 SDK，适合人形机器人遥操作与复杂训练。

**应用场景**：人形机器人远程操作、手术机器人训练、VR 工业维修培训、核电/太空遥操作、康复手功能评估。

## 供应链位置

- **上游关键零部件/材料**：微型执行器/电机、柔性传动机构、传感器、电池、蓝牙模块、手套材料、追踪器兼容方案
- **下游客户/应用场景**：机器人遥操作、医疗培训、VR 仿真、汽车/航空维修培训、科研院所
- **主要竞争对手/对标**：HaptX、Manus VR、Meta Haptic Glove、StretchSense、CyberGlove

## 知识图谱节点与关系

- 公司实体：`ent_company_senseglove`
- 产品实体：`ent_product_senseglove_nova_2`
- 零部件实体：`ent_component_senseglove_nova_2_core`
- 关键关系：
  - `ent_company_senseglove` -- `manufactures` --> `ent_product_senseglove_nova_2`
  - `ent_company_senseglove` -- `manufactures` --> `ent_component_senseglove_nova_2_core`
  - `ent_product_senseglove_nova_2` -- `uses` --> `ent_component_senseglove_nova_2_core`

## 参考资料

1. [SenseGlove 官网](https://senseglove.com)
2. [SenseGlove Nova 2 产品页](https://senseglove.com/products/nova-2/)
3. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)