# Bota Systems（博塔系统） / Bota Systems

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Bota Systems（博塔系统） |
| **英文名** | Bota Systems |
| **总部** | 瑞士苏黎世 |
| **成立时间** | 2019 |
| **官网** | [https://www.bota-systems.com](https://www.bota-systems.com) |
| **供应链环节** | 六维力/力矩传感器、协作机器人末端力觉 |
| **企业属性** | 私有公司、ETH Zurich 衍生企业 |
| **母公司/所属集团** | 独立运营 |
| **数据来源** | Bota Systems 官网、产品 datasheet、行业评测 |

## 公司简介

Bota Systems 是瑞士专注于协作机器人和人形机器人应用的六维力/力矩传感器供应商，以紧凑、高性价比的力觉方案著称。

Bota Systems 由 ETH Zurich 研究团队孵化，致力于为协作机器人、人形机器人及医疗机器人提供高精度、低成本的六维力/力矩传感器。其产品采用先进的硅应变计与紧凑机械设计，可在狭小空间内实现可靠的力控与碰撞检测，已广泛应用于机器人装配、抛光、测试及具身智能研究。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| SensONE 系列 | 协作机器人六维力传感器 | SensONE / SensONE Mini | 协作机器人、人形机器人手腕 |
| MiniONE 系列 | 超微型六维力传感器 | MiniONE | 医疗机器人、灵巧手、研究 |
| OEM / 定制模组 | 嵌入式力觉传感单元 | 定制 F/T 模组 | 机器人关节、测试平台 |

## 代表产品

### Bota Systems SensONE 六维力传感器

> Bota Systems SensONE 六维力传感器：请访问 [官方资料](https://www.bota-systems.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 六维力/力矩传感器 | 官网 |
| 直径 | 约 80 mm | 官网/datasheet |
| 高度 | 约 21 mm | 官网/datasheet |
| 重量 | 约 290 g | 官网/datasheet |
| 力测量范围（Fx/Fy） | ±200 N | 官网/datasheet |
| 力测量范围（Fz） | ±500 N | 官网/datasheet |
| 力矩测量范围（Mx/My/Mz） | ±8 Nm | 官网/datasheet |
| 精度 | 未公开 | - |
| 过载能力 | 约 500% FS | 官网/datasheet |
| 采样频率 | 最高 1000 Hz | 官网/datasheet |
| 通信接口 | EtherCAT / Ethernet / USB / RS485 / CAN | 官网/datasheet |
| 防护等级 | IP67 | 官网/datasheet |
| 供电 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：专为协作机器人末端优化的紧凑结构，内置高精度硅应变计与多轴解耦算法，支持即插即用与主流机器人接口，具备高过载保护与工业级防护。

**应用场景**：协作机器人力控、拖动示教、精密装配、抛光打磨、人形机器人手腕/脚踝力觉反馈、医疗康复机器人。

### Bota Systems MiniONE 超微型六维力传感器

> Bota Systems MiniONE 超微型六维力传感器：请访问 [官方资料](https://www.bota-systems.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 超微型六维力传感器 | 官网 |
| 直径 | 约 15 mm | 官网 |
| 高度 | 约 8 mm | 官网 |
| 重量 | 约 5 g | 官网 |
| 力/力矩量程 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：面向医疗机器人、灵巧手等空间极度受限场景的超微型六维力传感方案。

**应用场景**：医疗微创手术器械、机器人灵巧手指端、微型力控夹爪、学术研究。

## 供应链位置

- **上游关键零部件/材料**：高强度铝合金/不锈钢、硅应变计、信号调理芯片、精密机加工、接插件与线缆
- **下游客户/应用场景**：协作机器人、人形机器人、医疗机器人、自动化产线、科研院所
- **主要竞争对手/对标**：ATI Industrial Automation、OnRobot、Robotiq、坤维科技、宇立仪器、柯力传感

## 知识图谱节点与关系

- 公司实体：`ent_company_bota_systems`
- 产品实体：`ent_product_bota_systems_sensone`
- 零部件实体：`ent_component_bota_systems_sensone_sensor`
- 关键关系：
  - `ent_company_bota_systems` -- `manufactures` --> `ent_product_bota_systems_sensone`
  - `ent_company_bota_systems` -- `manufactures` --> `ent_component_bota_systems_sensone_sensor`
  - `ent_product_bota_systems_sensone` -- `uses` --> `ent_component_bota_systems_sensone_sensor`

## 参考资料

1. [Bota Systems 官网](https://www.bota-systems.com)
2. [Bota Systems SensONE 六维力传感器 产品/资料页](https://www.bota-systems.com/sensone)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)