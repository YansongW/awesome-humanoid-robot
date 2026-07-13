---
id: ent_company_cross_dimension
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 跨维智能
  en: Cross-Dimension / DexForce
status: active
sources:
- id: src_cross_dimension_official
  type: website
  url: https://www.dexforce.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 跨维智能 / Cross-Dimension / DexForce

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 跨维智能（跨维（深圳）智能数字科技有限公司） |
| **英文名** | Cross-Dimension / DexForce |
| **总部** | 中国深圳（北京、上海、珠海设有分公司） |
| **成立时间** | 2021 年 6 月 |
| **官网** | [https://www.dexforce.com](https://www.dexforce.com) |
| **供应链环节** | 传感器 / 具身智能 AI 与 3D 视觉 |
| **企业属性** | 国家高新技术企业、具身智能方案商 |
| **母公司/所属集团** | 无 |
| **数据来源** | 跨维智能官网、WAIC 2026 展商名录、机器之心、PingWest |

## 公司简介

跨维智能是一家以 Sim2Real 为核心、专注高通用性具身智能技术的国家高新技术企业。公司团队由全球 Top 2% 顶尖科学家领衔，在 3D 生成式 AI、多模态大模型及机器人应用方面积累了深厚技术，致力于通过自研引擎实现具身智能的规模化商业落地。

公司打造了 DexVerse™ 具身智能引擎、DexSense 纯视觉空间与具身智能传感器、DexForce W1 / W1 Pro 通用人形机器人等软硬一体产品矩阵。其核心商业模式是利用仿真生成海量合成数据，训练 VLA 模型并直接迁移到真机，从而缩短机器人进入新场景的部署周期。截至 2026 年，跨维已服务汽车、3C、半导体、家电、物流等 30 余个行业。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 具身智能机器人 | 可落地的高精度移动操作平台 | DexForce W1 / W1 Pro | 科研教育、商业服务、智能制造 |
| 智能视觉传感器 | 纯视觉 3D 感知与空间智能 | DexSense | 工业上下料、拆码垛、质检 |
| 具身智能引擎 | Sim2Real 数据生成与模型训练 | DexVerse™ / EmbodiChain | 算法开发、场景部署 |

## 代表产品

### DexForce W1 Pro

> DexForce W1 Pro：请访问 [官方资料](https://www.dexforce.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 170 cm（全尺寸） | 官方公开资料 |
| 重量 | 未公开 | - |
| 自由度 | 34+ 动力单元 / 机械手可选 6 DOF 灵巧手或二指夹爪 | PingWest |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 支持 EmbodiChain 开发平台、ROS/Modbus/TCP | 官网 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：自研纯视觉双目传感器（帧率 60 Hz、双目标定误差 ≤±0.05 像素）、Engine-driven Sim2Real VLA、全身谐波关节与全向运动底盘，重复定位精度 ≤0.5 mm。

**应用场景**：高精度柔性装配、带操作巡检、物料分拣、家庭助理、商业导览与科研教育。

### DexSense 纯视觉传感器

> DexSense：请访问 [官方资料](https://www.dexforce.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 视场角 | 水平 90° / 垂直 60°（仿人视野） | PingWest |
| 深度精度 | 三维轮廓还原误差 ≤1 mm | PingWest |
| 帧率 | 最高 60 Hz | PingWest |
| 接口/通信 | 支持 TCP / Modbus | 官网 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：首创双目估计大模型，零样本任意场景深度估计；微秒级多相机同步；可在 DexVerse 中完成仿真到真机的快速迁移。

**应用场景**：无序抓取、拆码垛、定位装配、工业质检。

## 供应链位置

- **上游关键零部件/材料**：自研纯视觉传感器与算法，外购谐波减速器、电机、计算单元、结构件。
- **下游客户/应用场景**：广汽、美的、海尔、松下、蓝思科技等制造业头部客户；科研教育、商业服务集成商。
- **主要竞争对手/对标**：梅卡曼德、奥比中光、智元机器人。

## 知识图谱节点与关系

- 公司实体：`ent_company_cross_dimension`
- 产品实体：`ent_product_cross_dimension_dexforce_w1_pro`、`ent_product_cross_dimension_dexsense`
- 关键关系：
  - `ent_company_cross_dimension` -- `manufactures` --> `ent_product_cross_dimension_dexforce_w1_pro`
  - `ent_company_cross_dimension` -- `manufactures` --> `ent_product_cross_dimension_dexsense`

## 参考资料

1. [跨维智能官网](https://www.dexforce.com)
2. [WAIC 2026 展商名录 - 聚展网](https://www.jufair.com/information/319685.html)
3. [PingWest – 跨维智能发布 DexForce W1 Pro](https://www.pingwest.com/a/306441)
4. [机器之心 – 从空间智能到具身智能](https://www.jiqizhixin.com)