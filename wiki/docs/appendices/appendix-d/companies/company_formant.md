# Formant / Formant

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Formant |
| **英文名** | Formant |
| **总部** | 美国加利福尼亚州旧金山 |
| **成立时间** | 2017 年 |
| **官网** | [https://formant.io](https://formant.io) |
| **供应链环节** | 机器人数据平台、远程运维、车队管理、遥操作 |
| **企业属性** | 初创公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | Formant 官网、BMW i Ventures 投资新闻、The Robot Report |

## 公司简介

Formant 是一家专注于机器人运营（Robot Operations, RobOps）的云计算公司，为机器人开发商与终端企业提供统一的数据、监控、分析与远程操作平台。

平台支持 ROS/ROS2 及任意机器人 SDK，通过一条命令或轻量级 Agent 即可将机器人接入云端。Formant 提供实时遥测可视化、告警、数据记录、远程遥控（teleoperation）、任务调度与车队级分析，帮助企业以更少工程资源实现规模化部署。其客户涵盖农业、仓储、巡检、清洁与制造等多个领域。

Formant 在 2022 年完成 1,800 万美元 A 轮融资，2024 年再获 BMW i Ventures 领投的 2,100 万美元融资，进一步扩展其车队运营与数据平台能力。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 机器人数据平台 | 实时遥测、日志、可视化 | Formant Observe | 车队监控、故障排查 |
| 远程操作平台 | 低延迟遥操作与人机协作 | Formant Operate | 异常干预、复杂场景控制 |
| 数据分析平台 | 车队级洞察与 KPI | Formant Analyze | 运营优化、ROI 报告 |
| 应用构建框架 | 白标/定制机器人应用 | Formant Platform SDK | 多品牌车队集成 |

## 代表产品

### Formant 数据与操作平台

> Formant Platform：请访问 [官方资料](https://formant.io) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 公有云 SaaS / 私有化部署 | Formant 官网 |
| 接入方式 | Formant Agent（一条命令安装） | Formant 文档 |
| 支持中间件 | ROS 1 / ROS 2、MQTT、REST API | 公开资料 |
| 数据类型 | 遥测、日志、视频、点云、地图 | Formant 文档 |
| 遥操作延迟 | 未公开（依赖网络与边缘代理） | - |
| 车队规模 | 支持数千台机器人 | BMW i Ventures 新闻 |
| 安全合规 | SOC 2、GDPR、加密传输 | Formant 官网 |
| 价格 | 按设备/数据量订阅 | 官方询价 |

**技术亮点**：开箱即用的机器人数据可视化、低代码告警与自动化工作流、跨品牌车队统一管理、远程遥控与一键接管、与 PickNik MoveIt 等生态集成。

**应用场景**：AMR 仓储车队监控、农业机器人远程诊断、巡检机器人异常接管、清洁服务机器人规模化运营。

### Formant Teleoperation

> Formant Teleoperation：请访问 [官方资料](https://formant.io) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 控制方式 | 键盘、游戏手柄、触屏、自定义 API | Formant 文档 |
| 视频流 | 多路摄像头实时回传 | 公开资料 |
| 地图与导航 | 2D/3D 地图叠加、点击目标点导航 | Formant 文档 |
| 安全机制 | 紧急停止、权限管理、审计日志 | 公开资料 |
| 网络适应性 | 弱网/断网重连、边缘缓存 | Formant 文档 |
| 价格 | 包含在企业订阅中 | 官方询价 |

**技术亮点**：浏览器端低延迟遥控、多摄像头与传感器融合视图、与 Formant 数据平台原生联动、权限分级与操作审计。

**应用场景**：仓库拥堵场景人工接管、户外巡检异常处理、半自主机器人的远程辅助操作、新员工培训与机器人演示。

## 供应链位置

- **上游关键零部件/材料**：AWS/Google Cloud/Azure 云基础设施、边缘计算模块、ROS/ROS2、视频编解码与网络传输技术。
- **下游客户/应用场景**：SoftBank Robotics、BP、Blue River Technology（John Deere）、Burro、Knightscope、Scythe 等机器人厂商与终端企业。
- **主要竞争对手/对标**：InOrbit、Freedom Robotics、AWS RoboMaker、Google Cloud Robotics、Boston Dynamics Orbit。

## 知识图谱节点与关系

- 公司实体：`ent_company_formant`
- 产品/平台实体：`ent_product_formant_platform`、`ent_product_formant_teleoperation`
- 关键关系：
  - `rel_ent_company_formant_manufactures_ent_product_formant_platform`（`ent_company_formant` → `manufactures` → `ent_product_formant_platform`）
  - `rel_ent_company_formant_manufactures_ent_product_formant_teleoperation`（`ent_company_formant` → `manufactures` → `ent_product_formant_teleoperation`）

## 参考资料

1. [Formant 官网](https://formant.io)
2. [BMW i Ventures – Formant 投资新闻](https://www.bmwiventures.com/news/operationalizing-robot-fleets-at-scale-our-lead-investment-in-formant)
3. [The Robot Report – Formant 与 SoftBank 合作](https://www.therobotreport.com/formants-data-platform-comes-to-softbanks-cleaning-robots/)
4. [SignalFire – Formant 投资博客](https://www.signalfire.com/blog/formant-robotics-investor)