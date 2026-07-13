# 宇树 G1 / Unitree G1

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [宇树科技 / Unitree Robotics](../companies/company_unitree.md) |
| **产品类别** | 紧凑型人形机器人 |
| **发布时间** | 2024 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [Unitree G1 产品页](https://www.unitree.com/g1) |

## 产品概述

宇树 G1 是 Unitree 面向教育、科研与开发者推出的紧凑型人形机器人，以激进定价和高可及性著称。G1 身高约 127 cm，体重约 35 kg，基础版拥有 23 个自由度，EDU 版可扩展至 43 DOF 并配备 Dex3-1 五指灵巧手与 NVIDIA Jetson Orin 计算模块。

G1 采用 3D LiDAR、深度相机与 8 核 CPU（EDU 版增加 Jetson Orin），支持 ROS2、Python/C++ SDK 与 OTA 升级。其可折叠设计便于运输与部署，成为全球出货量领先的人形开发平台之一。

## 产品图片

> Unitree G1：请访问 [官方资料](https://www.unitree.com/g1) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 127 cm（高） | 公开规格 |
| 重量 | 约 35 kg | 公开规格 |
| 自由度（整机） | 23–43 DOF | 基础版/EDU 版配置差异 |
| 关键性能指标 | 关节峰值扭矩 90–120 N·m；负载约 2 kg | 公开规格 |
| 行走速度 | 约 2 m/s | 公开规格 |
| 续航 | 约 1.5–2 小时（9,000 mAh 快拆电池） | 公开规格 |
| 计算平台 | 8 核 CPU；EDU 版可选 NVIDIA Jetson Orin | 公开规格 |
| 价格 | 约 16,000 USD / 国内 9.9 万元起 | 媒体报道 |

## 供应链位置

- **制造商**：[宇树科技 / Unitree Robotics](../companies/company_unitree.md)
- **核心零部件/技术来源**：自研关节电机与驱动器、3D LiDAR、Intel RealSense 深度相机、NVIDIA Jetson Orin（EDU 版）。
- **下游应用/客户**：高校、教育机构、开发者、AI 研究与商用展示。

## 知识图谱节点与关系

- 产品实体：`ent_product_unitree_g1`
- 制造商实体：`ent_company_unitree`
- 关键关系：
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_g1`（`ent_company_unitree` → `manufactures` → `ent_product_unitree_g1`）

## 应用场景

- **教育演示**：高校、中小学与科技馆用于机器人课程、展览与竞赛。
- **AI 与机器人研究**：开发者社区进行模仿学习、强化学习与多模态交互实验。
- **轻量商业**：零售展示、导览迎宾与小批量物流试点。

## 竞争对比

| 对比项 | Unitree G1 | Unitree H1 | Unitree R1 |
|--------|------------|------------|------------|
| 定位 | 紧凑型开发平台 | 全尺寸高动态平台 | 入门级开发平台 |
| 身高 | 127 cm | 180 cm | 121 cm |
| 价格 | 约 16,000 USD | 约 90,000 USD | 约 5,900 USD |
| 核心优势 | 性价比高、EDU 版功能全 | 高动态运动、负载大 | 超低门槛、开发者友好 |

## 选购与部署建议

- 教育/研究机构建议优先选择 G1 EDU 版以获得 SDK、ROS2 与 Jetson Orin 计算支持。
- 部署时需确保场地有足够安全空间，并配置急停装置与防护围栏。

## 参考资料

1. [Unitree G1 产品页](https://www.unitree.com/g1)
2. [Robozaps – Unitree G1 Review](https://blog.robozaps.com/b/unitree-g1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [Humanoid Index – G1](https://humanoidindex.org/robots/g1)