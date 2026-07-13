---
id: ent_company_pal_robotics
schema_version: 1
type: company
'title:': PAL Robotics
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: PAL Robotics
  en: PAL Robotics
aliases:
- PAL Robotics
- PAL Robotics
status: active
sources:
- id: src_pal_robotics_official
  type: website
  url: https://pal-robotics.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# PAL Robotics / PAL Robotics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | PAL Robotics |
| **英文名** | PAL Robotics |
| **总部** | 西班牙巴塞罗那 |
| **成立时间** | 2004 |
| **官网** | [https://pal-robotics.com](https://pal-robotics.com) |
| **供应链环节** | 研究型人形机器人、开源 ROS 平台、服务机器人 |
| **企业属性** | 私营公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | PAL Robotics 官网、TALOS 产品页、官方数据手册 |

## 公司简介

PAL Robotics 是欧洲领先的服务与研究机器人公司，TALOS 双足人形机器人以高动态控制、ROS/ROS 2 全栈开源和工业级扭矩控制著称。

TALOS 面向 AI、机器学习、运动控制与工业 4.0 研究，提供全关节扭矩反馈、2 kHz 控制回路与 EtherCAT 通信；同时公司提供 TIAGo、REEM-C 等平台。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| TALOS | 双足人形研究平台 | TALOS | 工业研究、AI 与运动控制 |
| TIAGo / REEM-C | 服务/研究机器人 | TIAGo / REEM-C | 人机交互、养老、科研 |

## 代表产品

### PAL Robotics TALOS

> PAL Robotics TALOS：请访问 [官方资料](https://pal-robotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 175 cm（高） | PAL Robotics 产品页 |
| 重量 | 95 kg | PAL Robotics 产品页 |
| 自由度 | 32（腿 6×2、臂 7×2、腰 2、颈 2、夹爪 1×2） | 官方数据手册 |
| 负载/扭矩 | 单臂伸展状态 6 kg | PAL Robotics 产品页 |
| 速度/转速 | 约 3 km/h | 第三方汇总 |
| 续航 | 行走 1.5 h / 待机 3 h（1080 Wh） | 官方数据手册 |
| 接口/通信 | ROS / ROS 2、EtherCAT、Ubuntu LTS RT | 官方数据手册 |
| 价格 | 按需报价 | - |

**技术亮点**：全扭矩反馈关节、2 kHz 控制、ROS/ROS 2 开源、工业级工具操作、可定制头部与夹爪。

**应用场景**：机器人研究、运动控制算法验证、工业 4.0 示范、人机交互研究。


### PAL Robotics REEM-C

> PAL Robotics REEM-C：请访问 [官方资料](https://pal-robotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 165 cm（高） | 公开资料 |
| 重量 | 约 80 kg | 公开资料 |
| 自由度 | 44 | 公开资料 |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | ROS | 公开资料 |
| 价格 | 按需报价 | - |

**技术亮点**：早期全尺寸人形研究平台，为 TALOS 奠定硬件与 ROS 控制基础。

**应用场景**：人机交互、导航与运动研究。


## 供应链位置

- **上游关键零部件/材料**：电机/驱动、力/力矩传感器、计算模块、结构件与电池。
- **下游客户/应用场景**：研究机构（Inria、NASA、DARPA）、欧盟研究项目、服务机器人客户。
- **主要竞争对手/对标**：Boston Dynamics Atlas（研究/工业）、其他研究人形平台。

## 知识图谱节点与关系

- 公司实体：`ent_company_pal_robotics`
- 产品/平台实体：`ent_product_pal_robotics_talos`、`ent_product_pal_robotics_reem_c`
- 关键关系：
  - `rel_ent_company_pal_robotics_manufactures_ent_product_pal_robotics_talos`（`ent_company_pal_robotics` → `manufactures` → `ent_product_pal_robotics_talos`）
  - `rel_ent_company_pal_robotics_manufactures_ent_product_pal_robotics_reem_c`（`ent_company_pal_robotics` → `manufactures` → `ent_product_pal_robotics_reem_c`）

## 参考资料

1. [PAL Robotics 官网](https://pal-robotics.com)
2. [TALOS 产品页](https://pal-robotics.com/robot/talos/)
3. [TALOS 官方数据手册 PDF](https://pal-robotics.com/wp-content/uploads/2024/05/Datasheet-TALOS.pdf)