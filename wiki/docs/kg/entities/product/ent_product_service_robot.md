---
id: ent_product_service_robot
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 服务机器人
  en: Service Robot
status: active
sources:
- id: src_ifr_service_robot_def
  type: website
  url: https://ifr.org/service-robots
- id: src_ifr_wr_service_methods
  type: website
  url: https://ifr.org/img/worldrobotics/Sources___Methods_WR_2025_Service_Robots.pdf
- id: src_ifr_def_service_2026
  type: website
  url: https://ifr.org/img/worldrobotics/Definition_Service_Robots_2026.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 服务机器人 / Service Robot

## 概述

根据 ISO 8373:2021，服务机器人（service robot）是指“用于个人用途或专业用途，为人类或设备执行有用任务的机器人”。与工业机器人不同，服务机器人的分类依据是应用场景而非机械构型；只要机器人不用于工业自动化环境中的可编程多用途 manipulator 任务，即可归入服务机器人统计范畴。国际机器人联合会（IFR）每年发布《World Robotics Service Robots》报告，对个人服务机器人与专业服务机器人进行全球统计。

## 工作原理 / 技术架构

服务机器人通常由以下子系统构成：

- **感知系统**：激光雷达、摄像头、IMU、超声波、触觉传感器等，用于环境建模、定位与障碍物检测。
- **决策与规划**：基于 SLAM、路径规划、行为树或深度学习模型，实现自主导航与任务决策。
- **执行机构**：移动底盘、机械臂、末端执行器、显示屏、语音模块等，完成具体的物理或交互任务。
- **人机交互（HRI）**：语音、触摸屏、手势、视觉等方式与用户交互。
- **通信与调度**：Wi-Fi / 4G / 5G / 云端调度，实现多机协作与远程监控。

自主程度（degree of autonomy）是服务机器人的核心属性，定义为“基于当前状态和感知，在无人工干预的情况下执行预期任务的能力”。ISO 8373 指出，服务机器人的自主程度可从部分自主（含人机交互）到完全自主不等。

## 关键参数表

由于服务机器人是产品类别而非单一型号，以下参数为行业典型范围或分类维度：

| 参数项 | 典型范围 / 说明 |
|---|---|
| 分类维度 | 个人/消费级 vs. 专业服务级 |
| 移动方式 | 轮式、履带式、足式、飞行、水下 |
| 导航方式 | SLAM 激光、视觉 SLAM、磁条/二维码、GPS/RTK |
| 自主性 | 部分自主至完全自主 |
| 典型负载 | 0–100 kg（视应用场景） |
| 典型速度 | 0.5–2 m/s（室内移动平台） |
| 续航 | 未公开（因产品差异极大） |
| 通信接口 | Wi-Fi / 4G / 5G / 以太网 / 云端 |
| 主要应用 | 配送、清洁、导览、安防、康养、农业、物流 |

## 应用场景

- **餐饮与酒店配送**：如擎朗 T10、普渡 BellaBot 等配送机器人。
- **家庭清洁**：扫地机器人、擦窗机器人等消费级产品。
- **医疗康养**：康复训练、陪护、药品配送、手术辅助（医疗机器人单独分类）。
- **公共安防与巡检**：机场、园区、电力管廊的巡逻与异常检测。
- **仓储物流**：AMR、AGV、分拣机器人被 IFR 统计为专业服务机器人。

## 供应链关系

- **上游**：激光雷达、摄像头、IMU、电机、电池、控制器、语音与显示模组、AI 芯片。
- **中游**：服务机器人整机制造商（如 Keenon、Pudu、BlueBotics、Locus Robotics 等）以及导航/调度软件供应商。
- **下游**：餐饮、酒店、医院、商场、机场、物流仓库、家庭用户。
- **图谱位置**：`ent_product_service_robot` 作为产品类别，与 `ent_company_keenon`、`ent_company_pudu` 等制造商及 `ent_product_keenon_service_robot`、`ent_product_pudu_service_robot` 等具体产品实体形成层级关系。

## 来源与验证

- 服务机器人定义与分类直接引用 ISO 8373:2021，通过 IFR 官方页面与《World Robotics 2025 Service Robots》方法论文档验证。
- 典型应用场景参考 IFR 应用分类方案与附录 D 重点企业/产品 Wiki。