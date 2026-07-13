---
id: ent_company_songyan_dynamics
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 松延动力
  en: Songyan Dynamics / Noetix Robotics
status: active
sources:
- id: src_songyan_dynamics_official
  type: website
  url: https://noetixrobotics.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 松延动力 / Songyan Dynamics / Noetix Robotics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 松延动力 |
| **英文名** | Songyan Dynamics / Noetix Robotics |
| **总部** | 中国北京（北京经济技术开发区） |
| **成立时间** | 2023 年 9 月 |
| **官网** | [https://noetixrobotics.com](https://noetixrobotics.com) |
| **供应链环节** | 整机 OEM / 通用人形机器人 + 仿生机器人 |
| **企业属性** | 高动态运动、小尺寸低成本、清华背景 |
| **母公司/所属集团** | 无 |
| **数据来源** | 松延动力官网、百度百科、OFweek/维科号 |

## 公司简介

松延动力聚焦高动态通用人形机器人与仿生机器人，以小尺寸、低成本、强运动性能推动机器人进入家庭与商业场景。

公司核心团队来自清华等高校，2025 年 3 月发布 N2 人形机器人，身高 1.18 m、体重 30 kg，可实现奔跑、跳跃、连续空翻等高难度动作；同年 10 月发布万元级消费级机器人 Bumi 小布米，进一步降低人形机器人使用门槛。2026 年登上央视春晚，展示多产品协同表演能力。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 高动态通用人形 | 高校科研、娱乐表演 | N2 / E1 | 科研教育、商业展示、竞赛 |
| 消费级人形 | 家庭陪伴、儿童教育 | Bumi 小布米 | 家庭教育、编程启蒙 |

## 代表产品

### 松延动力 N2

![松延动力 N2](https://www.noetixrobotics.com/mtsc/uploads/Ckeditor/Images/2025-12-25/N2.webp)


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

**技术亮点**：全球首个多场景连续空翻、MPC+强化学习运动控制、轻量化铝合金结构、双编码器关节、可选 NVIDIA Jetson Orin Nano Super

**应用场景**：高校科研、幼儿陪伴、娱乐表演、商业展示、机器人竞赛。

### Bumi 小布米

> Bumi 小布米：请访问 [官方资料](https://noetixrobotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 高约 94 cm | 公开报道 |
| 重量 | 约 12–17 kg | 公开报道 |
| 自由度 | 21 DOF | 公开报道 |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 图形化编程平台、开放运动控制接口 | 公开报道 |
| 价格 | 9998 元 | OFweek/公开报道 |

**技术亮点**：万元级消费级人形机器人、JD 平台首发、面向家庭教育与陪伴

**应用场景**：儿童教育、家庭陪伴、编程启蒙。

## 供应链位置

- **上游关键零部件/材料**：自研高性能关节电机与驱动器、铝合金结构件、深度相机、IMU、锂电池；核心零部件国产化率近 100%。
- **下游客户/应用场景**：高校、K12 教育、商业展示、家庭消费者。
- **主要竞争对手/对标**：宇树 G1、加速进化 Booster T1、众擎 PM01

## 知识图谱节点与关系

- 公司实体：`ent_company_songyan_dynamics`
- 产品实体：`ent_product_songyan_dynamics_n2`
- 零部件实体：`ent_component_songyan_joint_motor`
- 关键关系：
  - `ent_company_songyan_dynamics` -- `manufactures` --> `ent_product_songyan_dynamics_n2`
  - `ent_company_songyan_dynamics` -- `manufactures` --> `ent_component_songyan_joint_motor`
  - `ent_product_songyan_dynamics_n2` -- `uses` --> `ent_component_songyan_joint_motor`

## 参考资料

1. [松延动力 N2 产品页](https://noetixrobotics.com/n2)
2. [松延动力官网](https://noetixrobotics.com/)
3. [百度百科 – 松延动力 N2](https://baike.baidu.com/item/%E6%9D%BE%E5%BB%B6%E5%8A%A8%E5%8A%9BN2/67393633)