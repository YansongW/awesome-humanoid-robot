---
id: ent_component_optitrack_motive_system_core
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: OptiTrack 红外追踪相机模块
  en: OptiTrack Infrared Tracking Camera Module
status: active
sources:
- id: src_ent_component_optitrack_motive_system_core_official
  type: website
  url: https://optitrack.com/cameras/
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# OptiTrack 红外追踪相机模块 / OptiTrack Infrared Tracking Camera Module

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [OptiTrack](../../../appendices/appendix-d/companies/company_optitrack.md) |
| **产品类别** | 光学动作捕捉系统 |
| **发布时间** | PrimeX 系列持续在售；Motive 3 现行 |
| **状态** | 量产/商用 |
| **官网/来源** | [OptiTrack 相机产品页](https://optitrack.com/cameras/) |

## 产品概述

OptiTrack 运动捕捉系统由 PrimeX 系列红外相机、Motive 追踪软件与主动/被动标记点组成，可在室内环境下实现亚毫米级、低延迟的 6DoF 位姿追踪。该系统广泛应用于人形机器人运动验证、遥操作训练、步态分析、无人机/AGV 定位标定以及影视动画制作。

## 产品图片

> OptiTrack 运动捕捉系统：请访问 [官方资料](https://optitrack.com/cameras/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系统组成 | PrimeX 相机 + Motive 软件 + 标记点 | 官网 |
| 代表相机 | PrimeX 13（1.3 MP）、PrimeX 41（2048×2048） | 产品页 |
| 追踪精度 | 亚毫米级（未公开精确值） | 公开资料 |
| 延迟 | 低至数毫秒级 | 产品页 |
| 最大帧率 | PrimeX 13：240 fps；PrimeX 41：180 fps | 产品页 |
| 视场角 | 未公开 | 产品页 |
| 同步方式 | eSync / 以太网 | 产品页 |
| 软件接口 | Motive 3、C/C++ SDK、Python、ROS、VRPN | 官网 |
| 工作距离 | 未公开 | 产品页 |
| 价格 | 未公开 | 商务报价 |

## 供应链位置

- **制造商**：[OptiTrack](../../../appendices/appendix-d/companies/company_optitrack.md)
- **核心零部件/技术来源**：红外图像传感器、光学镜头、FPGA/处理芯片、红外照明、校准算法、网络同步与 3D 解算软件
- **下游应用/客户**：影视动画公司、机器人/无人机研发团队、高校与科研院所、体育/康复机构

## 知识图谱节点与关系

- 产品实体：`ent_product_optitrack_motive_system`
- 零部件实体：`ent_component_optitrack_motive_system_core`
- 制造商实体：`ent_company_optitrack`
- 关键关系：
  - `rel_ent_company_optitrack_manufactures_ent_product_optitrack_motive_system`（`ent_company_optitrack` → `manufactures` → `ent_product_optitrack_motive_system`）
  - `rel_ent_company_optitrack_manufactures_ent_component_optitrack_motive_system_core`（`ent_company_optitrack` → `manufactures` → `ent_component_optitrack_motive_system_core`）
  - `rel_ent_product_optitrack_motive_system_uses_ent_component_optitrack_motive_system_core`（`ent_product_optitrack_motive_system` → `uses` → `ent_component_optitrack_motive_system_core`）

## 应用场景

- **人形机器人运动标定**：捕捉全身关节轨迹，验证运动规划与控制算法。
- **遥操作训练**：记录操作员手部/身体动作，用于训练遥操作策略。
- **无人机/AGV 定位验证**：提供高精度 ground truth，评估 SLAM 与定位算法。
- **影视动画与游戏**：角色动作采集与实时虚拟制作。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 光学红外动作捕捉 | Vicon Vero/Vantage | Qualisys Miqus/Arqus |
| 精度 | 亚毫米级 | 亚毫米级 | 亚毫米级 |
| 延迟 | 低延迟 | 低延迟 | 低延迟 |
| 价格 | 未公开 | 高端 | 高端 |

## 选购与部署建议

- 根据捕捉空间大小与精度需求选择相机数量与型号。
- 确保场地具备可控的红外反射条件，避免阳光与强红外干扰。
- 部署前进行系统校准，并验证 SDK 与目标软件栈的接口兼容性。

## 相关词条

- [制造商：OptiTrack](../../../appendices/appendix-d/companies/company_optitrack.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [OptiTrack 官网](https://optitrack.com)
2. [OptiTrack 相机产品页](https://optitrack.com/cameras/)
3. Motive 软件文档与公开技术资料
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)