---
id: ent_company_xvariable
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 自变量机器人
  en: Xvariable / X Square Robot
status: active
sources:
- id: src_xvariable_official
  type: website
  url: https://x2robot.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 自变量机器人 / Xvariable / X Square Robot

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 自变量机器人 |
| **英文名** | Xvariable / X Square Robot |
| **总部** | 中国广东深圳 |
| **成立时间** | 2023 年 12 月 |
| **官网** | [https://x2robot.com](https://x2robot.com) |
| **供应链环节** | 整机+大模型 / 通用轮式仿人形机器人 + 具身智能大模型 |
| **企业属性** | 端到端具身智能大模型 WALL-A/B、软硬一体 |
| **母公司/所属集团** | 无 |
| **数据来源** | 自变量机器人官网、产品页、关于我们 |

## 公司简介

自变量机器人聚焦自研通用具身智能大模型，以“大脑+小脑”端到端架构驱动轮式仿人形机器人在开放环境中完成精细操作。

公司推出的 GreatWall 系列 WALL-A 操作大模型具备自主感知、决策与高精度操作能力；2025 年 8 月发布 Quanta X2 新一代通用轮式仿人形机器人，全身 62 个自由度、单臂展 765 mm、重复定位精度 ±0.03 mm，搭载 2D 激光雷达、RGBD、3D-TOF 等多模态传感器，面向工业组装、家庭服务与酒店等场景。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 通用轮式仿人形机器人 | 科研、工业、服务 | Quanta X1 / Quanta X2 | 科研教育、工业组装、酒店服务 |
| 灵巧手 | 精细操作 | ArtiXon Hand | 科研、工业、服务机器人末端 |

## 代表产品

### 自变量 Quanta X2（量子 2 号）

![自变量 Quanta X2（量子 2 号）](https://x2robot-open.oss-cn-shenzhen.aliyuncs.com/quantum2_qiepian/x2/12_m.png)


| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 身高 164 cm；工作高度 0–2 m | 自变量官网 |
| 重量 | 未公开 | - |
| 自由度 | 全身 62 DOF；躯干 6 DOF；单手灵巧手 20 DOF | 自变量官网 |
| 负载/扭矩 | 单臂额定负载 6 kg；最大双臂负载 25 kg | 自变量官网 |
| 速度/转速 | 末端速度 1.8 m/s；底盘移动速度 1 m/s | 自变量官网 |
| 续航 | 未公开 | - |
| 接口/通信 | 2D 激光雷达、超声波×4、RGBD、3D-TOF、单点 TOF、红外；WALL-A 端到端大模型 | 自变量官网 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：百亿参数 WALL-A 端到端操作大模型、全身 62 DOF、±0.03 mm 重复定位、仿人五指灵巧手、跨任务跨场景泛化

**应用场景**：工业组装、线束整理、酒店纸巾换新、晾衣服、杂物收纳、制作饮品、科研教育。

### 自变量 Quanta X1（量子 1 号）

> 自变量 Quanta X1（量子 1 号）：请访问 [官方资料](https://x2robot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 工作高度 0–1 m | 公开报道 |
| 重量 | 未公开 | - |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | WALL-A 大模型、机械外骨骼/VR 遥操作 | 公开报道 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：轮式双臂科研平台，支持远程遥操、数据采集与模型验证

**应用场景**：科研教育、具身智能算法验证。

## 供应链位置

- **上游关键零部件/材料**：自研 WALL-A 大模型、关节、灵巧手、传感器、计算平台；外购电机、减速器、电池、相机模组。
- **下游客户/应用场景**：工业制造、酒店服务、新零售、科研教育、家庭服务。
- **主要竞争对手/对标**：智元机器人、Figure AI、Astribot、银河通用

## 知识图谱节点与关系

- 公司实体：`ent_company_xvariable`
- 产品实体：`ent_product_xvariable_quanta_x2`
- 零部件实体：`ent_component_xvariable_artixon_hand`
- 关键关系：
  - `ent_company_xvariable` -- `manufactures` --> `ent_product_xvariable_quanta_x2`
  - `ent_company_xvariable` -- `manufactures` --> `ent_component_xvariable_artixon_hand`
  - `ent_product_xvariable_quanta_x2` -- `uses` --> `ent_component_xvariable_artixon_hand`

## 参考资料

1. [自变量机器人官网](https://x2robot.com)
2. [Quanta X2 产品页](https://x2robot.com/product/quantum2)
3. [关于我们](https://x2robot.com/about)