# 海克斯康 / Hexagon

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 海克斯康 |
| **英文名** | Hexagon |
| **总部** | 瑞典斯德哥尔摩 |
| **成立时间** | 1975 年（前身为 Hexagon AB，1990 年代转型） |
| **官网** | [https://hexagon.com](https://hexagon.com) |
| **供应链环节** | 精密测量、三坐标测量机、工业软件、智能制造、传感器 |
| **企业属性** | 上市公司（OMX: HEXA B）、全球计量与工业软件龙头 |
| **母公司/所属集团** | 无（Hexagon AB 为上市主体） |
| **数据来源** | Hexagon 官网、年报、产品手册、公开新闻稿 |

## 公司简介

海克斯康是全球领先的数字 reality 解决方案提供商，通过高精度测量、传感器与工业软件赋能机器人零部件与整机的几何量测与质量控制。

海克斯康业务覆盖测量技术（三坐标测量机、便携式测量臂、激光跟踪仪）、地理空间信息技术与工业软件（MSC、Simufact、Romax 等）。在机器人领域，海克斯康的高精度三坐标测量机与光学测量系统被广泛用于关节、减速器、连杆与整机精度标定。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 坐标测量机 | 高精度几何量测 | GLOBAL / Leitz / TIGO | 汽车零部件、航空航天、机器人零部件 |
| 便携式测量与扫描 | 现场尺寸检测与逆向 | ROMER 测量臂 / Leica 激光跟踪仪 | 装配、产线检测、机器人标定 |
| 工业软件 | 仿真与制造智能 | MSC Adams / Simufact / Q-DAS | 机器人动力学仿真、工艺优化 |

## 代表产品

### 海克斯康三坐标测量机 / GLOBAL 系列

> 海克斯康三坐标测量机 / GLOBAL 系列：请访问 [官方资料](https://hexagon.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 测量范围 | 500×700×500 mm 至 2000×4000×1500 mm 多种规格 | Hexagon 产品手册 |
| 精度 | MPE_E 约 1.5 + L/350 µm（视型号） | Hexagon 产品手册 |
| 探测系统 | HP-S-X5 / HH-T / 触发式测头 | Hexagon 产品手册 |
| 软件 | PC-DMIS / QUINDOS | Hexagon 官网 |
| 结构 | 花岗石工作台、气浮导轨、钢制桥架 | Hexagon 产品手册 |
| 温度补偿 | 自动温度补偿 | Hexagon 产品手册 |
| 接口 | USB / 以太网 | Hexagon 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高精度与高稳定性、丰富的测头与软件生态、广泛应用于汽车与航空航天级零部件检测。

**应用场景**：机器人关节/减速器几何检测、汽车零件、航空航天结构件、模具检测。

### 海克斯康 ROMER 便携式测量臂

> 海克斯康 ROMER 便携式测量臂：请访问 [官方资料](https://hexagon.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 测量范围 | 1.8 m – 4.5 m（臂长） | Hexagon 产品手册 |
| 精度 | 空间精度 ±0.020–±0.060 mm（视型号） | Hexagon 产品手册 |
| 测头 | 触发式 / 扫描式 / 激光扫描测头 | Hexagon 产品手册 |
| 自由度 | 6 轴 / 7 轴 | Hexagon 产品手册 |
| 软件 | PC-DMIS Portable | Hexagon 官网 |
| 便携性 | 可现场部署、无需气源 | Hexagon 产品手册 |
| 接口 | USB / Wi-Fi | Hexagon 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：现场快速检测、无需恒温车间、支持扫描与逆向工程、适配产线抽检与机器人标定。

**应用场景**：机器人整机装配检测、焊接夹具检测、铸件/钣金件尺寸验证、逆向工程。

## 供应链位置

- **上游关键零部件/材料**：高精度光栅尺、气浮轴承、花岗石、测头传感器、工业软件 IP。
- **下游客户/应用场景**：汽车、航空航天、电子、医疗、机器人零部件与整机制造商。
- **主要竞争对手/对标**：蔡司（ZEISS）、温泽（Wenzel）、法如（FARO）、尼康（Nikon Metrology）。

## 知识图谱节点与关系

- 公司实体：`ent_company_hexagon`
- 产品实体：`ent_product_hexagon_cmm`、`ent_product_hexagon_romer_arm`
- 关键关系：
  - `ent_company_hexagon` -- `manufactures` --> `ent_product_hexagon_cmm`
  - `ent_company_hexagon` -- `manufactures` --> `ent_product_hexagon_romer_arm`
  - `ent_product_hexagon_cmm` -- `uses` --> `ent_component_linear_encoder`
  - `ent_product_hexagon_romer_arm` -- `uses` --> `ent_component_probe_sensor`

## 参考资料

1. [官网](https://hexagon.com)
2. [Hexagon 官网](https://hexagon.com)
3. Hexagon GLOBAL 系列与 ROMER 产品手册