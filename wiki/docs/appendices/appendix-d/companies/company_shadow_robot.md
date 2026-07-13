# Shadow Robot Company / Shadow Robot Company

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Shadow Robot Company |
| **英文名** | Shadow Robot Company |
| **总部** | 英国伦敦 |
| **成立时间** | 1987 |
| **官网** | [https://www.shadowrobot.com](https://www.shadowrobot.com) |
| **供应链环节** | 仿人灵巧手 / 机器人末端执行器 / 科研平台 |
| **企业属性** | 全球领先灵巧手企业、科研级产品 |
| **母公司/所属集团** | Shadow Robot Company Ltd. |
| **数据来源** | 官网、产品手册、公开报道、WAIC 2026 报道 |

## 公司简介

全球最先进的仿人灵巧手研发商之一，深耕科研与高端应用。

Shadow Robot Company 成立于 1987 年，总部位于英国伦敦，长期专注于高度仿人机器人灵巧手的研发。Shadow Dexterous Hand 拥有与人类手部相近的尺寸和运动学，被广泛应用于机器人抓取研究、遥操作、医疗手术、核工业及人形机器人领域，是 ROS/EtherCAT 生态中最具代表性的科研级灵巧手之一。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Shadow Dexterous Hand | 高自由度科研级 | 五指灵巧手 | 科研、医疗 |
| Shadow Hand Lite | 轻量化低成本 | 四指灵巧手 | 教育、商业 |
| Teleoperation Systems | 遥操作 | Shadow Glove | 远程操控、核工业 |

## 代表产品

### Shadow Dexterous Hand / Shadow Dexterous Hand

> Shadow Dexterous Hand：请访问 [官方资料](https://www.shadowrobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 仿人成年男性手尺寸 | 官方规格书 |
| 重量 | 4.3 kg（含前臂） | 官方规格书 |
| 自由度 | 20 主动 + 4 被动 / 24 关节 | 官方规格书 |
| 负载 | 强力抓握 4–5 kg | 官方规格书 / 公开报道 |
| 运动速度 | 典型关节 1.0 Hz | 官方规格书 |
| 通信接口 | EtherCAT | 官方规格书 |
| 控制频率 | 位置环 1 kHz / 力矩环 5 kHz | 官方规格书 |
| 供电电压 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：高度仿生运动学、指尖/手掌触觉传感器、ROS 全集成、位置/力/扭矩多模式控制，可完成穿针、捏取等精细动作。

**应用场景**：高校与科研机构抓取研究、医疗手术训练、核工业遥操作、人形机器人高端验证。


### Shadow Hand Lite / Shadow Hand Lite

> Shadow Hand Lite：请访问 [官方资料](https://www.shadowrobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 自由度 | 未公开 | - |
| 负载 | 未公开 | - |
| 指尖力 | 未公开 | - |
| 通信接口 | EtherCAT | 产品手册 |
| 供电电压 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：在保持 Shadow Hand 精细操作能力的同时精简结构，面向更广泛的教育与商业应用。

**应用场景**：教育演示、商业展示、轻量科研、服务机器人。


## 供应链位置

- **上游关键零部件/材料**：微型电机、腱绳、力/触觉传感器、铝合金/工程塑料、EtherCAT 控制板
- **下游客户/应用场景**：高校与研究机构、医疗手术、核工业、遥操作、人形机器人
- **主要竞争对手/对标**：SCHUNK、qb Soft Robotics、Agile Robots、因时机器人

## 知识图谱节点与关系

- 公司实体：`ent_company_shadow_robot`
- 产品/零部件实体：`ent_product_shadow_dexterous_hand`
- 关键关系：
  - `ent_company_shadow_robot` -- `manufactures` --> `ent_product_shadow_dexterous_hand`

## 参考资料

1. [官网](https://www.shadowrobot.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.shadowrobot.com)（请按实际产品型号核对）