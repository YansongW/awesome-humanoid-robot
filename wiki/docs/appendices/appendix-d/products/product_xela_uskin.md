# XELA Robotics uSkin 高密度 3 轴触觉传感器 / XELA Robotics uSkin High-Density 3-Axis Tactile Sensor

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [XELA Robotics](../companies/company_xela.md) |
| **产品类别** | 高密度 3 轴柔性触觉传感器 / 电子皮肤 |
| **发布时间** | 2018 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [XELA Robotics 官网](https://www.xelarobotics.com) |

## 产品概述

XELA Robotics uSkin 是一款面向机器人夹爪与灵巧手的高密度三轴柔性触觉传感器。uSkin 采用磁阻式传感原理，每个传感单元（taxel）可独立测量 X、Y、Z 三轴力，分辨率达 0.1 gf，采样频率 500 Hz，并通过数字输出方式将布线简化为最少 4 根线。

uSkin 的柔软弹性体外壳使其能够贴合复杂曲面、缓冲过载并保护被抓取物体，广泛应用于 Robotiq、Weiss Robotics、Wonik Robotics、Tesollo DG-5F 等主流夹爪与灵巧手。2026 年，XELA 计划将标准传感点尺寸从 4 mm × 4 mm 缩小至 2.5 mm × 2.5 mm，进一步提升空间分辨率。

## 产品图片

> XELA uSkin：请访问 [官方资料](https://www.xelarobotics.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感原理 | 磁阻式 3 轴力传感 | 官网公开资料 |
| 感知维度 | X、Y、Z 三轴力 | 官网公开资料 |
| 标准传感点尺寸 | 4 mm × 4 mm | 官网/公开报道 |
| 下一代传感点尺寸 | 2.5 mm × 2.5 mm（2026 年 Q2） | Engineering.com |
| 单个 taxel 法向力量程 | 最高 1500 gf（约 14.7 N） | XELA Catalog 2025 |
| 分辨率 | 0.1 gf（约 1 mN） | 官网公开资料 |
| 采样频率 | 500 Hz | 官网公开资料 |
| 输出方式 | 数字输出 | 官网公开资料 |
| 布线需求 | 最少 4 线读取全部传感器 | 产品手册 |
| 封装材料 | 柔软弹性体 | 官网公开资料 |
| 标准型号 | uSPa 11/21/22/44/46、uSCu、uSPr 系列 | 官网公开资料 |
| 通信接口 | 数字总线（具体协议未公开） | 产品手册 |
| 供电电压 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 防护等级 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[XELA Robotics](../companies/company_xela.md)
- **核心零部件/技术来源**：自研磁阻式 3 轴传感芯片、弹性体外壳与 uAi 软件平台；微控制器、柔性基材外购。
- **下游应用/客户**：人形机器人灵巧手、工业夹爪、物流仓储、农业采摘、科研院校、医疗假肢。

## 知识图谱节点与关系

- 产品实体：`ent_product_xela_uskin`
- 制造商实体：`ent_company_xela`
- 零部件实体：`ent_component_xela_uskin_module`
- 关键关系：
  - `rel_ent_company_xela_manufactures_ent_product_xela_uskin`（`ent_company_xela` → `manufactures` --> `ent_product_xela_uskin`）
  - `rel_ent_company_xela_manufactures_ent_component_xela_uskin_module`（`ent_company_xela` → `manufactures` --> `ent_component_xela_uskin_module`）
  - `rel_ent_product_xela_uskin_uses_ent_component_xela_uskin_module`（`ent_product_xela_uskin` → `uses` --> `ent_component_xela_uskin_module`）

## 应用场景

- **人形机器人灵巧手**：指尖、指腹、手掌的全手触觉覆盖。
- **工业夹爪力控**：Robotiq、Weiss Robotics 等夹爪的直接集成，实现力/滑移反馈。
- **物流分拣**：异形、易碎、柔软物品的安全抓取。
- **农业采摘**：果蔬等脆弱对象的自适应采摘。
- **医疗假肢**：为假肢提供接近人类皮肤的力感知。

## 竞争对比

| 对比项 | XELA uSkin | SynTouch BioTac | 帕西尼 PX-6AX |
|--------|------------|-----------------|---------------|
| 传感原理 | 磁阻式 3 轴 | 流体/电极/热传导 | 6D 霍尔阵列 |
| 感知维度 | 3 轴力 | 力+振动+温度 | 15 种触觉信息 |
| 传感点密度 | 4 mm（标准）/ 2.5 mm（规划） | 单点仿生 | 阵列式 |
| 核心优势 | 柔软、易集成、数字输出 | 仿生、鲁棒 | 高密度、灵巧手全栈 |

## 选购与部署建议

- 根据夹爪或灵巧手的几何尺寸选择 uSPa（平面）、uSCu（曲面）或 uSPr（夹爪保护）系列。
- 传感器对磁场敏感，部署时需避开强磁场与铁磁性材料，必要时使用参考传感器补偿。
- 数字输出简化了硬件集成，但需在机器人控制器侧预留对应驱动或 SDK。

## 参考资料

1. [XELA Robotics 官网](https://www.xelarobotics.com)
2. [XELA Robotics 产品目录 2025](https://49063741.fs1.hubspotusercontent-na2.net/hubfs/49063741/XELA%20Robotics%20-%20Catalog%202025.pdf)
3. [Engineering.com – uSkin integrated into Tesollo DG-5F](https://www.engineering.com/uskin-tactile-sensors-integrated-into-tesollo-dg-5f-robot-hand/)
4. [XELA Robotics 技术页](https://xelarobotics.com/technology/)
5. [附录 D 企业目录](../index-companies.md)