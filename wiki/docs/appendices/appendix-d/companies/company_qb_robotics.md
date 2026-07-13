# qb Soft Robotics / qb Soft Robotics

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | qb Soft Robotics |
| **英文名** | qb Soft Robotics |
| **总部** | 意大利比萨 |
| **成立时间** | 2011 |
| **官网** | [https://qbrobotics.com](https://qbrobotics.com) |
| **供应链环节** | 软体灵巧手 / 软体机器人 / 五指夹爪 |
| **企业属性** | 软体机器人技术先锋 |
| **母公司/所属集团** | qbrobotics Srl |
| **数据来源** | 官网、产品手册、公开报道、WAIC 2026 报道 |

## 公司简介

基于软体机器人技术的仿人灵巧手开发商。

qb Soft Robotics（qbrobotics）源自意大利比萨，专注于软体机器人与仿生五指灵巧手。qb SoftHand 系列利用单电机腱驱动与软体关节协同，实现类人抓取与高度环境适应性，具有自复位、高负载重量比、即插即用等特点，广泛应用于科研、教育、协作机器人及人机交互领域。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| qb SoftHand Research | 科研版五指软体手 | qb SoftHand | 科研、教育 |
| qb SoftHand2 Research | 增强版双协同 | SoftHand2 | 研究、工业测试 |
| qb SoftHand Industry | 工业版 | SoftHand Industry | 协作机器人、人机交互 |

## 代表产品

### qb SoftHand 五指软体灵巧手 / qb SoftHand 5-Finger Soft Robotic Hand

> qb SoftHand 五指软体灵巧手：请访问 [官方资料](https://qbrobotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 1:1 仿人手，具体未公开 | 公开资料 |
| 重量 | 500 g | 公开资料 |
| 手指数 | 5 | 公开资料 |
| 自由度 | 19 关节 / 1 主动协同（单电机） | 公开资料 |
| 指尖捏紧力 | 62 N | 公开资料 |
| 额定负载 | 1.7 kg（捏紧状态） | 公开资料 |
| 张手到握拳 | 1.1 s | 公开资料 |
| 通信接口 | USB / RS485 | 公开资料 |
| 兼容性 | ROS、UR+ 认证 | 公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：软体材料与腱驱动协同、自复位关节、单电机即插即用、高负载自重比、安全人机交互。

**应用场景**：科研抓取、教育演示、协作机器人末端、医疗康复、人机交互。


### qb SoftHand2 Research / qb SoftHand2 Research

> qb SoftHand2 Research：请访问 [官方资料](https://qbrobotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 0.94 kg | 公开资料 |
| 自由度 | 19 关节 / 双电机 / 双协同 | 公开资料 |
| 额定负载 | 2 kg（捏持）/ 3 kg（抓握） | 公开资料 |
| 张手到握拳 | 约 1 s | 公开资料 |
| 通信接口 | USB / RS485 | 公开资料 |
| 兼容性 | ROS / ROS2 | 公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：第二协同运动提升在手中操作能力，可在不旋转手腕的情况下调整物体姿态。

**应用场景**：高级抓取研究、工业测试、人机协作、复杂物体操作。


## 供应链位置

- **上游关键零部件/材料**：弹性体材料、肌腱/软驱动、电机、传感器、3D 打印结构件
- **下游客户/应用场景**：高校、研究机构、协作机器人厂商、医疗康复、工业测试
- **主要竞争对手/对标**：Shadow Robot、Pisa/IIT SoftHand、Robotiq、Agile Robots

## 知识图谱节点与关系

- 公司实体：`ent_company_qb_robotics`
- 产品/零部件实体：`ent_product_qb_hand`
- 关键关系：
  - `ent_company_qb_robotics` -- `manufactures` --> `ent_product_qb_hand`

## 参考资料

1. [官网](https://qbrobotics.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://qbrobotics.com)（请按实际产品型号核对）