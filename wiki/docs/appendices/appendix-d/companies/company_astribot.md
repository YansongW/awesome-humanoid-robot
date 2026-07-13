# 星尘智能 / Astribot

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 星尘智能 |
| **英文名** | Astribot |
| **总部** | 中国广东深圳 |
| **成立时间** | 2022 年 |
| **官网** | [https://www.astribot.com](https://www.astribot.com) |
| **供应链环节** | 整机 OEM / 轮式人形机器人 + 操作型 AI 机器人 |
| **企业属性** | 绳驱传动、Design for AI、AI 机器人助理 |
| **母公司/所属集团** | 无 |
| **数据来源** | Astribot 官网、RobotScope、百度百科 |

## 公司简介

星尘智能专注通用 AI 机器人助理，以绳驱传动和高动态操作能力为核心，打造可在真实环境中干活的轮式人形机器人。

2024 年 8 月，星尘智能发布 Astribot S1，定位“全能操作型”AI 机器人，具备接近成年人的操作速度与精度，可完成叠衣、炒菜、写书法、泡功夫茶等复杂任务。2025 年推出 S1-U 半身商用版本与 T1 紧凑型轮式产品线，持续扩大科研、服务与工业场景落地。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 全尺寸操作型人形 | 科研、服务、柔性制造 | Astribot S1 | 科研教育、新零售、智慧养老 |
| 商用/紧凑版本 | 半身商用、低成本轮式 | S1-U / T1 | 商业服务、家庭助理 |

## 代表产品

### Astribot S1

![Astribot S1](https://cdn.shopify.com/s/files/1/0659/1437/2184/files/Astribot_image_1_resized.png?v=1768350773&width=800)

> 图片来源：Astribot 产品资料图（第三方经销商）。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 170 cm（高） | Astribot 官网 |
| 重量 | 80 kg | Astribot 官网 |
| 自由度 | 全身 23 DOF（单臂 7 DOF×2，躯干 4 DOF，头部 2 DOF，全向轮式底盘 3 DOF） | Astribot 官网 / 技术文档 |
| 负载/扭矩 | 单臂水平伸展额定负载 5 kg，峰值 10 kg | Astribot 官网 |
| 速度/转速 | 末端最高速度 ≥10 m/s | Astribot 官网 |
| 续航 | 4–6 小时（支持插电） | Astribot 官网 |
| 接口/通信 | ROS 2 / Python SDK、Gigabit Ethernet、Wi-Fi | 技术文档 |
| 价格 | 科研版约 ¥50 万；企业/科研级约 $96,000–$150,000 | 公开报道 |

**技术亮点**：绳驱传动、±0.1 mm 重复定位精度、100 m/s² 末端加速度、力控安全、VR 遥操作与零代码可视化界面

**应用场景**：叠衣、炒菜、清洁、书法、泡功夫茶、科研实验、养老陪护、新零售展示。

### Astribot S1-U

> Astribot S1-U：请访问 [官方资料](https://www.astribot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

**技术亮点**：S1 的半身商用版本，面向桌面与服务场景，降低部署门槛

**应用场景**：商业服务、展厅导览、桌面操作。

## 供应链位置

- **上游关键零部件/材料**：自研绳驱执行器、高性能电机、力/扭矩传感器、计算平台；外购相机、激光雷达、电池。
- **下游客户/应用场景**：科研教育、智慧养老、家庭服务、新零售展示、柔性制造小批量装配。
- **主要竞争对手/对标**：Figure 02、特斯拉 Optimus、优必选 Walker、智元机器人

## 知识图谱节点与关系

- 公司实体：`ent_company_astribot`
- 产品实体：`ent_product_astribot_s1`
- 零部件实体：`ent_component_astribot_cable_actuator`
- 关键关系：
  - `ent_company_astribot` -- `manufactures` --> `ent_product_astribot_s1`
  - `ent_company_astribot` -- `manufactures` --> `ent_component_astribot_cable_actuator`
  - `ent_product_astribot_s1` -- `uses` --> `ent_component_astribot_cable_actuator`

## 参考资料

1. [Astribot 官网产品页](https://www.astribot.com/en/product)
2. [RobotScope – Astribot 公司资料](https://robotscope.net/companies/astribot/)
3. [百度百科 – Astribot S1](https://baike.baidu.com/item/Astribot%20S1/64813493)