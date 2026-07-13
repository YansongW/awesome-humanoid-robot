---
id: ent_company_onrobot
schema_version: 1
type: company
domain: 02_components
theoretical_depth: system
names:
  zh: OnRobot（昂乐）
  en: OnRobot
status: active
sources:
- id: src_ent_company_onrobot_official
  type: website
  url: https://www.onrobot.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# OnRobot（昂乐） / OnRobot

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | OnRobot（昂乐） |
| **英文名** | OnRobot |
| **总部** | 丹麦欧登塞（Odense） |
| **成立时间** | 2015 |
| **官网** | [https://www.onrobot.com](https://www.onrobot.com) |
| **供应链环节** | 协作机器人末端执行器、六维力传感器、电动夹爪、真空吸盘 |
| **企业属性** | 私有公司、协作机器人末端生态龙头 |
| **母公司/所属集团** | OnRobot A/S（曾与 Perception Robotics、OptoForce 合并） |
| **数据来源** | OnRobot 官网、产品 datasheet、行业报道 |

## 公司简介

OnRobot 是丹麦协作机器人末端工具一站式供应商，提供力/力矩传感器、电动夹爪、真空吸盘与快换装置。

OnRobot 总部位于丹麦机器人产业集群欧登塞，致力于为协作机器人提供即插即用的末端执行器生态。其 HEX 系列六维力/力矩传感器可与 Universal Robots、FANUC、KUKA 等主流协作机器人无缝集成，实现力控装配、抛光、测试与人机协作。除力觉产品外，OnRobot 还提供 RG2/RG6 电动夹爪、VGC 真空夹爪、Gecko 壁虎吸盘及 Quick Changer 快换装置。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| HEX 力/力矩传感器 | 机器人末端六维力控 | HEX-E / HEX-H / HEX-E QC | 装配、抛光、测试 |
| 电动夹爪 | 自适应夹持 | RG2 / RG6 / RG2-FT | 协作机器人上下料 |
| 真空/软体夹爪 | 不规则与薄片抓取 | VGC10 / Gecko SP | 物流、包装、食品 |
| 快换装置 | 末端工具快速切换 | Quick Changer | 多工具协作产线 |

## 代表产品

### OnRobot HEX-E QC 六维力/力矩传感器

> OnRobot HEX-E QC 六维力/力矩传感器：请访问 [官方资料](https://www.onrobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 六维力/力矩传感器 | 官网 |
| 力测量范围（Fx/Fy/Fz） | ±100 N / ±100 N / ±200 N | 官网/datasheet |
| 力矩测量范围（Mx/My/Mz） | ±10 Nm / ±10 Nm / ±10 Nm | 官网/datasheet |
| 精度 | 未公开 | - |
| 分辨率 | 未公开 | - |
| 采样频率 | 未公开 | - |
| 过载能力 | 约 500% FS | 官网/datasheet |
| 防护等级 | IP67 | 官网/datasheet |
| 通信接口 | TCP/IP、USB、EtherNet/IP、PROFINET | 官网/datasheet |
| 集成接口 | Quick Changer / 机器人法兰 | 官网/datasheet |
| 供电 | 24 V DC | 官网/datasheet |
| 重量 | 约 350 g | 官网/datasheet |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：专为协作机器人优化的六维力传感方案，内置 Quick Changer 快换接口，支持 UR、FANUC、KUKA 等主流品牌即插即用，防护等级达 IP67。

**应用场景**：协作机器人力控装配、恒力打磨/抛光、插拔测试、表面质量检测、人形机器人手臂末端力觉。

### OnRobot RG2-FT 智能夹爪

> OnRobot RG2-FT 智能夹爪：请访问 [官方资料](https://www.onrobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 带力/扭矩指尖的电动夹爪 | 官网 |
| 夹持行程 | 未公开 | - |
| 夹持力 | 未公开 | - |
| 力觉 | 指尖集成 F/T 传感 | 官网 |
| 价格 | 未公开 | - |

**技术亮点**：在电动夹爪指尖集成力/扭矩与接近传感，实现更精细的抓取控制。

**应用场景**：协作机器人上下料、精密装配、易碎/异形物体抓取。

## 供应链位置

- **上游关键零部件/材料**：铝合金结构件、力敏元件、信号处理芯片、接插件、密封材料、机器人快换标准件
- **下游客户/应用场景**：协作机器人用户、汽车/3C 装配、人形机器人手臂、物流包装、自动化集成商
- **主要竞争对手/对标**：ATI Industrial Automation、Robotiq、SCHUNK、Bota Systems、坤维科技、宇立仪器

## 知识图谱节点与关系

- 公司实体：`ent_company_onrobot`
- 产品实体：`ent_product_onrobot_hex_e`
- 零部件实体：`ent_component_onrobot_hex_e_sensor`
- 关键关系：
  - `ent_company_onrobot` -- `manufactures` --> `ent_product_onrobot_hex_e`
  - `ent_company_onrobot` -- `manufactures` --> `ent_component_onrobot_hex_e_sensor`
  - `ent_product_onrobot_hex_e` -- `uses` --> `ent_component_onrobot_hex_e_sensor`

## 参考资料

1. [OnRobot 官网](https://www.onrobot.com)
2. [OnRobot HEX-E QC 六维力/力矩传感器 产品/资料页](https://www.onrobot.com/en/products/he-x)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)