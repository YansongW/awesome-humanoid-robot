---
id: ent_product_magic_atom_magicbot_gen1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 魔法原子 MagicBot Gen1
  en: MagicLab MagicBot Gen1
status: active
sources:
- id: src_magiclab_human
  type: website
  url: https://www.magiclab.top/human
- title: MagicLab 通用人形机器人——MagicBot Gen1
- id: src_baiduwiki_magiclab
  type: website
  url: https://baike.baidu.com/en/item/Magiclab%20Robotics%20Technology%20(Wuxi)%20Co.,%20Ltd./1538573
- title: Magiclab Robotics Technology (Wuxi) Co., Ltd. — Baiduwiki
- id: src_robotscope_magiclab
  type: website
  url: https://robotscope.net/companies/magic-lab/
- title: MagicLab Series A — RobotScope
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 魔法原子 MagicBot Gen1 / MagicLab MagicBot Gen1

## 概述

MagicBot Gen1（代号“小麦”）是魔法原子（MagicLab / Magiclab Robotics Technology）推出的全尺寸通用人形机器人，定位于工业柔性生产、商业导览与家庭健康服务。整机站立尺寸约 1,740 × 580 × 280 mm，整机重量约 70 kg，具备 42 个主动自由度，单臂负载 ≥7.5 kg，全身静态负载达 40 kg。该产品搭载魔法原子自研场景大模型“原子万象”，并已在 2026 年央视春晚等公开场合亮相。

## 工作原理 / 技术架构

### 机身自由度配置
MagicBot Gen1 的 42 个主动自由度分布如下：

- 颈部：2 DOF（偏航 + 俯仰）；
- 单臂：7 DOF（肩 3 + 肘 1 + 腕 3）；
- 单手：11 DOF（6 主动 + 5 被动）；
- 腰部：2 DOF（偏航 + 横滚）；
- 单腿：6 DOF（髋 3 + 膝 1 + 踝 2）。

整机运动学为浮动基座（floating base）多刚体系统，机体位姿 $T_b \in SE(3)$ 与关节角 $\mathbf{q} \in \mathbb{R}^{42}$ 共同决定末端执行器位姿：

$$
T_{\text{ee}} = f_{\text{FK}}(T_b, \mathbf{q})
$$

### 驱动与结构
- **结构材料**：航空级铝制骨架 + 碳纤维外壳 + PC+ABS 外观件；
- **减速器**：谐波减速器 / 行星减速器；
- **最大关节扭矩**：≥350 N·m（膝关节）；
- **运动速度**：≥4 km/h；
- **热管理**：智能风冷散热。

### 感知与智能
- **高算力模块**：8 核 CPU + 100 TOPS AI 算力；
- **感知传感器**：3D LiDAR + 2× 深度相机 + 3× 鱼眼相机；
- **音频模块**：环形麦克风阵列 + 扬声器；
- **无线通信**：WiFi 6、5G、蓝牙 5.2；
- **导航**：自研导航算法，支持自主建图、避障与路径规划；
- **操作算法**：6D 视觉伺服 + 全身模仿学习 + 浮动基座设计。

### 能源系统
- 电池容量：25 Ah（1.35 kWh）；
- 续航：3–5 h；
- 充电时间：约 3 h；
- 支持快速换电，换电即唤醒。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 站立尺寸 | 1,740 × 580 × 280 mm |
| 整机重量 | 约 70 kg |
| 手臂伸展长度 | 800 mm（肩关节至指尖） |
| 大腿 + 小腿长度 | 960 mm（510 mm + 450 mm） |
| 总自由度 | 42（主动自由度） |
| 单臂自由度 | 7 |
| 单手自由度 | 11（6 主动 + 5 被动） |
| 腰部自由度 | 2 |
| 单腿自由度 | 6 |
| 最大关节扭矩 | ≥350 N·m |
| 运动速度 | ≥4 km/h |
| 单臂负载 | ≥7.5 kg |
| 全身静态负载 | 40 kg |
| 高算力模块 | 8 核 CPU + 100 TOPS AI |
| 感知传感器 | 3D LiDAR + 2× 深度相机 + 3× 鱼眼相机 |
| 无线通信 | WiFi 6 / 5G / 蓝牙 5.2 |
| 电池容量 | 25 Ah（1.35 kWh） |
| 续航 | 3–5 h |
| 充电时间 | 约 3 h |
| 防护等级 | IP66（防尘防水） |

## 应用场景

- **工业柔性生产**：物料搬运、装配辅助、多机协作；
- **商业导览**：企业展厅、博物馆、科技馆、景区讲解；
- **家庭健康服务**：2026 年 4 月签署 1.5 亿元大健康行业订单，聚焦居家健康管理与智能陪护；
- **科研教育**：人形机器人算法验证与二次开发。

## 供应链关系

MagicBot Gen1 位于“人形机器人整机—自研零部件—上游材料/算力”链条的整机层：

- **整机厂商**：魔法原子机器人科技（无锡）有限公司；
- **自研率**：公司宣称硬件自研率约 90%，覆盖关节模组、灵巧手、减速器、驱动器等；
- **感知与计算**：3D LiDAR、深度相机、鱼眼相机、高算力 AI 模块由多家供应商提供；
- **能源**：锂电池组；
- **下游客户**：汽车产业链、半导体、3C、医疗、核化等行业头部企业。

## 来源与验证

- MagicLab 官网人形机器人产品页（https://www.magiclab.top/human）
- Baiduwiki Magiclab 词条
- RobotScope 融资与公司数据库

> 注：部分参数（如关节峰值扭矩分布、电机型号、减速器传动比）未在公开资料中完整披露，标注为“未公开”。