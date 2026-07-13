---
id: ent_product_abb_irb_8700
type: product
domain: 04_assembly_integration_testing
theoretical_depth: system
names:
  zh: ABB IRB 8700
  en: ABB IRB 8700
aliases:
- IRB 8700
- ABB 重载机器人
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_abb_irb8700_global
  type: website
  url: https://global.abb/products/robotics/industrial-robots/irb-8700
- title: IRB 8700 Industrial Robot | ABB
- id: src_abb_irb8700_gongboshi
  type: website
  url: https://www.gongboshi.cn/index.php?file=news&homepage=abbrobot&itemid=17
- title: ABB隆重推出多用途工业机器人 IRB 8700 | 工博士
- id: src_abb_irb8700_weisi
  type: website
  url: http://www.weisizhineng.com/sell/show.php?itemid=13612
- title: ABB 机器人 IRB 8700-800/3.50 | 惟思智能
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# ABB IRB 8700

## 概述

ABB IRB 8700 是 ABB 第八代高负载高性能六轴工业机器人，也是 ABB 当前负载能力最大的多用途工业机器人之一。其设计兼顾高产能、紧凑 footprint、简单维护与低总体拥有成本，主要面向重型物料搬运、大型工件机加工上下料、点焊、压铸取件与汽车总装等重载场景。IRB 8700 采用单电机单减速器设计、配重与机械弹簧平衡、Foundry Plus 2 防护等级，并支持 LeanID 集成线缆包技术。

## 工作原理 / 技术架构

IRB 8700 为六轴串联机械臂，各关节均为旋转关节。其正向运动学通过 Denavit-Hartenberg（D-H）参数描述，末端位姿 $T_{6}^{0}$ 由各关节角 $q_1,\dots,q_6$ 的齐次变换矩阵连乘得到：

$$
T_{6}^{0}(q) = A_1(q_1) A_2(q_2) \cdots A_6(q_6)
$$

其中每个 $A_i$ 包含连杆扭角 $\alpha_{i-1}$、连杆长度 $a_{i-1}$、关节偏距 $d_i$ 与关节角 $\theta_i$。

区别于同级别产品常用的双电机/双减速器方案，IRB 8700 每个关节仅采用一台电机和一套传动装置，并通过安全配重与机械弹簧实现平衡，避免气弹簧漏气风险。该简化设计降低了零部件总数，从而提升可靠性、缩短节拍并提高精度。

运动控制采用 ABB TrueMove 与 QuickMove 算法，保证路径精度与最短节拍。重复定位精度 ±0.05 mm。手腕垂直向下时负载可达 1000 kg（针对 800/3.50 型号），满足大型铸件、电池 PACK 等重型工件搬运。

## 关键参数表

| 参数 | IRB 8700-550/4.20 | IRB 8700-800/3.50 | 备注 |
|------|-------------------|-------------------|------|
| 轴数 | 6 | 6 | 串联机械臂 |
| 额定负载 | 550 kg | 800 kg | 腕部下 |
| 手腕垂直向下负载 | 620 kg | 1000 kg | 特殊姿态 |
| 配套 LeanID 时负载 | 475 kg | 630 kg | 线缆包影响 |
| 工作范围 | 4.2 m | 3.5 m | 关节 1 中心到腕部中心 |
| 重复定位精度 | ±0.05 mm | ±0.05 mm | ISO 9283 |
| 最大转动惯量 | 725 kg·m² | 725 kg·m² | 官方资料 |
| 防护等级 | IP67 / Foundry Plus 2 | IP67 / Foundry Plus 2 | 铸造/恶劣环境 |
| 安装方式 | 落地式 | 落地式 | 标准配置 |
| 本体重量 | 约 4525 kg | 约 4525 kg | 官方/集成商资料 |
| 控制器 | IRC5 / OmniCore | IRC5 / OmniCore | 视配置 |
| 速度优势 | 较同级别机器人快 25% | 较同级别机器人快 25% | ABB 官方 |

## 应用场景

- **汽车制造业**：白车身点焊、大型冲压件搬运、底盘总成装配，利用 4.2 m 臂展覆盖整车工位。
- **金属加工与铸造**：机床上下料、压铸取件、砂型搬运，Foundry Plus 2 防护适应高温、粉尘环境。
- **重型物流**：港口、钢铁、风电等行业的大型零部件码垛与转运。
- **新能源电池**：电池 PACK 模组搬运与装配，满足大负载与高精度定位需求。

## 供应链关系

ABB IRB 8700 属于 **工业机器人整机层**，核心零部件包括大功率伺服电机、精密减速器（ABB 自研或外购）、控制器、线缆包与结构铸件。ABB 自研 RobotWare 软件、TrueMove/QuickMove 运动控制算法与 LeanID 线缆包方案，向下游汽车、金属加工、物流等终端用户提供机器人本体、集成应用与售后服务。其减速器、电机等关键零部件仍依赖 ABB 全球供应链体系。

## 来源与验证

- ABB 官方 IRB 8700 产品页：https://global.abb/products/robotics/industrial-robots/irb-8700
- ABB 机器人新品发布报道：https://www.gongboshi.cn/index.php?file=news&homepage=abbrobot&itemid=17
- 集成商产品参数页：http://www.weisizhineng.com/sell/show.php?itemid=13612

本体重量、能耗等参数在不同经销商资料中存在差异，表中采用官方及主流集成商数据；部分型号配置（如控制器版本、防护选项）需以实际订单为准。