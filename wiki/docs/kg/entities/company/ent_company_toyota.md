---
id: ent_company_toyota
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 丰田汽车（机器人业务）
  en: Toyota Motor Corporation (Robotics Division)
status: active
sources:
- id: src_toyota_t_hr3_tw
  type: website
  url: https://www.toyota.com.tw/startyourimpossible/mobility-solutions/t-hr3.html
- id: src_toyota_partner_robot
  type: website
  url: https://global.toyota/en/mobility/partner-robot/
- id: src_robotico_t_hr3
  type: website
  url: https://robotico.market/toyota/t-hr3
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 丰田汽车（机器人业务）

## 概述

丰田汽车公司（Toyota Motor Corporation）是全球最大的汽车制造商之一，同时通过其 Partner Robot 事业部与丰田研究院（Toyota Research Institute, TRI）积极布局机器人技术。丰田的机器人业务以“为人类提供移动自由”为愿景，重点开发人形机器人、辅助机器人与远程操控技术。其代表性产品 T-HR3 是第三代 Partner Robot，于 2017 年发布，采用主从式远程操控（Master Maneuvering System, MMS）架构，旨在探索家庭协助、医疗护理、灾难救援及太空作业等场景中安全的人机协作。

## 工作原理 / 技术架构

T-HR3 的核心技术是扭矩伺服模块（Torque Servo Module, TSM）与主操纵系统（MMS）。TSM 由电机、减速齿轮与扭矩传感器组成，安装于机器人每个关节，可实时测量并控制关节输出扭矩，实现柔顺运动与接触力反馈。T-HR3 全身共配置 32 个可控关节（部分资料称 29 个身体部位加 10 个手指），操作员通过穿戴式主手臂、主脚控制器与头戴显示器（HMD）向机器人映射动作，机器人同时将末端接触力反馈给操作员。

其控制链路可抽象为：

$$
\text{操作员动作} \xrightarrow{\text{MMS 传感器}} \text{主控制器} \xrightarrow{\text{高速通信}} \text{从控制器} \xrightarrow{\text{TSM 扭矩控制}} \text{机器人关节}.
$$

T-HR3 还具备自干涉预防技术（Self-interference Prevention Technology），可在操作员与机器人运动冲突时自动调整，防止机构损坏。丰田与 Tamagawa Seiki、Nidec Copal Electronics 合作开发了 TSM 技术。

## 关键参数表

| 参数 | T-HR3 人形机器人 |
|---|---|
| 身高 | $1.54\,\text{m}$ |
| 体重 | $75\,\text{kg}$ |
| 自由度 | 32（含 10 指） / 部分资料为 29 身体部位 + 10 指 |
| 负载能力 | $5\,\text{kg}$ |
| 行走速度 | $3\,\text{km/h}$ |
| 续航 | 约 $2\,\text{h}$ |
| 操控方式 | 主从式远程操控（MMS） |
| 力反馈 | 关节扭矩伺服模块（TSM）实现双向力反馈 |
| 脚底传感器 | 六维力/力矩传感器 |
| 商业状态 | 研究/演示原型，未公开销售 |

## 应用场景

丰田机器人业务聚焦于需要安全人机共存与远程在场的场景：

- **家庭与生活辅助**：T-HR3 可远程执行取物、开关门、照顾老人或行动不便者等任务。
- **医疗护理与远程手术支持**：在疫情期间，T-HR3 被用于远程护理演示，未来可拓展至远程医疗辅助。
- **灾难救援**：在危险或无法进入的环境中，由操作员远程控制机器人执行搜索与物资搬运。
- **工业与建筑现场**：远程操控使人类技能能够在危险环境中延伸，减少人员风险。
- **太空探索**：丰田与日本宇宙航空研究开发机构（JAXA）等合作，研究机器人在太空基地建设与维护中的应用。

## 供应链关系

丰田在机器人产业链中扮演“终端系统制造商与集成商”角色。其上游包括电机与传感器供应商（如 Tamagawa Seiki、Nidec Copal）、减速器与结构件供应商、计算平台供应商；中游为丰田自身研发机构（Partner Robot 事业部、TRI）完成整机设计、控制算法开发与系统集成；下游面向医疗机构、灾害管理机构、航天机构及潜在的消费/服务市场。与单纯销售零部件的供应商不同，丰田机器人业务更强调从汽车制造中积累的精密机械、电机控制与安全系统能力向人形机器人领域的迁移。

## 来源与验证

- 丰田台湾官网 T-HR3 页面列出 T-HR3 高度 $1540\,\text{mm}$、32 个关节、99.78% 操控范围，并介绍 MMS 与 TSM 技术。
- 丰田全球官网 Partner Robot 页面阐述丰田以“ Mobility for All ”为理念，开发 partner robots 以支持人类日常生活。
- Robotico Market 产品页汇总 T-HR3 的 $1.54\,\text{m}$ 身高、$75\,\text{kg}$ 体重、$5\,\text{kg}$ 负载、32 DOF、$2\,\text{h}$ 续航、$3\,\text{km/h}$ 速度及脚底六维力传感器等参数。