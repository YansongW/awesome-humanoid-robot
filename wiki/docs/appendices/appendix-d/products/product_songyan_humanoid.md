# 松延动力 N2 / Songyan N2

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [松延动力 / Songyan Dynamics / Noetix Robotics](../companies/company_songyan_dynamics.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | 2025 年 3 月 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://noetixrobotics.com](https://noetixrobotics.com) |

## 产品概述

高校科研、幼儿陪伴、娱乐表演、商业展示、机器人竞赛。

松延动力 N2 是 松延动力 的代表产品。全球首个多场景连续空翻、MPC+强化学习运动控制、轻量化铝合金结构、双编码器关节、可选 NVIDIA Jetson Orin Nano Super。主要规格包括：1180×470×290 mm（站立）（尺寸）、约 30 kg（重量）、18 DOF（单腿 5 DOF×2，单臂 4 DOF×2）（自由度）。

## 产品图片

![松延动力 N2](https://www.noetixrobotics.com/mtsc/uploads/Ckeditor/Images/2025-12-25/N2.webp)

> 图片来源：松延动力官网产品图。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 1180×470×290 mm（站立） | 松延官网 / 百度百科 |
| 重量 | 约 30 kg | 松延官网 |
| 自由度 | 18 DOF（单腿 5 DOF×2，单臂 4 DOF×2） | 松延官网 |
| 负载/扭矩 | 膝关节峰值扭矩 150 N·m；持续行走负载约 5 kg | 松延官网 |
| 速度/转速 | 奔跑速度峰值 3.5 m/s | 松延官网 / 百度百科 |
| 续航 | 约 1–2 小时（48 V / 7 Ah） | 松延官网 |
| 接口/通信 | Wi-Fi 6、蓝牙 5.2、OTA、二次开发接口（EDU 版） | 松延官网 |
| 价格 | 3.99 万元起 | 公开报道 |

## 供应链位置

- **制造商**：[松延动力 / Songyan Dynamics / Noetix Robotics](../companies/company_songyan_dynamics.md)
- **核心零部件/技术来源**：自研高性能关节电机与驱动器、铝合金结构件、深度相机、IMU、锂电池；核心零部件国产化率近 100%。
- **下游应用/客户**：高校科研、幼儿陪伴、娱乐表演、商业展示、机器人竞赛。

## 知识图谱节点与关系

- 产品实体：`ent_product_songyan_dynamics_n2`
- 制造商实体：`ent_company_songyan_dynamics`
- 关键关系：
  - `rel_ent_company_songyan_dynamics_manufactures_ent_product_songyan_dynamics_n2`（`ent_company_songyan_dynamics` → `manufactures` → `ent_product_songyan_dynamics_n2`）
  - `ent_product_songyan_dynamics_n2` -- `uses` --> `ent_component_songyan_joint_motor`

## 应用场景

- **高校科研、幼儿陪伴、娱乐表演、商业展示、机器人竞赛。**
- **商业服务**：用于导览、接待、展示与品牌互动。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 通用人形机器人 | 同类产品视具体场景而定 |
| 核心优势 | 全球首个多场景连续空翻、MPC+强化学习运动控制、轻量化铝合金结构、双编码器关节、可选 NVIDIA Jetson Orin Nano Super | 未公开 |
| 价格 | 3.99 万元起 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [松延动力 N2 产品页](https://noetixrobotics.com/n2)
2. [松延动力官网](https://noetixrobotics.com/)
3. [百度百科 – 松延动力 N2](https://baike.baidu.com/item/%E6%9D%BE%E5%BB%B6%E5%8A%A8%E5%8A%9BN2/67393633)