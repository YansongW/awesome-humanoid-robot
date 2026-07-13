# 高通 RB5 / 机器人平台

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [高通 / Qualcomm](../companies/company_qualcomm.md) |
| **产品类别** | 机器人边缘 AI 开发平台 |
| **发布时间** | 2020 年发布 RB5 |
| **状态** | 量产/商用 |
| **官网/来源** | 见正文参考资料 |

## 产品概述

Qualcomm Robotics RB5 平台基于 QRB5165 SoC，集成第 5 代 AI 引擎、支持 7 路并发摄像头、5G/Wi-Fi 6 连接与丰富的传感器接口，是 AMR、配送机器人、无人机与人形机器人原型开发的常用边缘计算平台。高通机器人平台强调异构计算、连接能力与开发者生态。

## 产品图片

> 高通 RB5 / 机器人平台：请访问 [官方资料](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| SoC | Qualcomm QRB5165 | 高通官网 |
| AI 算力 | 第 5 代 AI 引擎，15 TOPS | 高通公开资料 |
| CPU | Kryo 585 八核（最高 2.84 GHz） | 高通官网 |
| GPU | Adreno 650 | 高通官网 |
| ISP | 支持 7 路摄像头并发 | 高通官网 |
| 连接 | 5G、Wi-Fi 6、蓝牙 5.1、GPS | 高通官网 |
| 接口 | USB 3.1、PCIe、MIPI CSI、GPIO | 开发套件资料 |
| 价格 | 开发套件约 449 USD（参考价） | 高通/经销商 |

## 供应链位置

- **制造商**：[高通 / Qualcomm](../companies/company_qualcomm.md)
- **核心零部件/技术来源**：台积电代工、ARM IP、存储器、射频前端、基带、传感器生态。
- **下游应用/客户**：AMR 厂商、无人机厂商、服务机器人厂商、开发者与教育机构。

## 知识图谱节点与关系

- 产品实体：`ent_product_qualcomm_rb5`
- 制造商实体：`ent_company_qualcomm`
- 关键关系：
  - `rel_ent_company_qualcomm_manufactures_ent_product_qualcomm_rb5`（`ent_company_qualcomm` → `manufactures` → `ent_product_qualcomm_rb5`）
  - `ent_product_qualcomm_rb5` -- `uses` --> `ent_component_qrb5165_soc`
  - `ent_product_qualcomm_rb5` -- `supports` --> `ent_component_5g_module`

## 应用场景

- **AMR**：仓储物流自主移动机器人感知与导航。
- **配送机器人**：户外/室内配送，依赖 5G 与 AI 视觉。
- **无人机**：航拍、巡检、物流无人机的边缘 AI 与连接。

## 竞争对比

| 对比项 | RB5 | NVIDIA Jetson AGX Orin | 地平线 Journey 5 |
|--------|------|------|------|
| 算力 | 15 TOPS | 275 TOPS | 128 TOPS |
| 连接 | 集成 5G/Wi-Fi 6 | 需外接模块 | 需外接模块 |
| 生态 | ROS 2 + 移动端生态 | CUDA/Isaac 强 | 智驾生态 |

## 选购与部署建议

- 根据算力/精度/场景需求选择对应型号，优先考虑官方支持的工具链与生态兼容性。
- 部署前确认供电、散热、机械接口与通信协议是否满足整机要求。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：高通 / Qualcomm](../companies/company_qualcomm.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [高通 / Qualcomm 官方产品/公司页面](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)
2. [Qualcomm Robotics RB5 页面](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)