# 海克斯康三坐标测量机

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [海克斯康 / Hexagon](../companies/company_hexagon.md) |
| **产品类别** | 精密几何量测设备 |
| **发布时间** | 持续迭代，GLOBAL 系列为经典产品线 |
| **状态** | 量产/商用 |
| **官网/来源** | 见正文参考资料 |

## 产品概述

海克斯康三坐标测量机（CMM）是工业计量领域的核心设备，通过接触式测头在三维空间内获取工件几何尺寸与形位公差。GLOBAL 系列作为海克斯康经典桥式 CMM，以高精度、高稳定性与丰富的测头/软件生态，广泛应用于机器人关节、减速器、连杆等核心零部件的精度检测与质量控制。

## 产品图片

> 海克斯康三坐标测量机：请访问 [官方资料](https://hexagon.com/products/coordinate-measuring-machines) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 测量范围 | 500×700×500 mm 至 2000×4000×1500 mm | Hexagon 产品手册 |
| 精度 | MPE_E 约 1.5 + L/350 µm（视型号） | Hexagon 产品手册 |
| 探测系统 | HP-S-X5 / HH-T / 触发式测头 | Hexagon 产品手册 |
| 软件 | PC-DMIS / QUINDOS | Hexagon 官网 |
| 结构 | 花岗石工作台、气浮导轨、钢制桥架 | Hexagon 产品手册 |
| 温度补偿 | 自动温度补偿 | Hexagon 产品手册 |
| 接口 | USB / 以太网 | Hexagon 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[海克斯康 / Hexagon](../companies/company_hexagon.md)
- **核心零部件/技术来源**：高精度光栅尺、气浮轴承、花岗石、测头传感器、工业软件。
- **下游应用/客户**：汽车零部件、航空航天、电子、医疗器械、机器人零部件制造商。

## 知识图谱节点与关系

- 产品实体：`ent_product_hexagon_cmm`
- 制造商实体：`ent_company_hexagon`
- 关键关系：
  - `rel_ent_company_hexagon_manufactures_ent_product_hexagon_cmm`（`ent_company_hexagon` → `manufactures` → `ent_product_hexagon_cmm`）
  - `ent_product_hexagon_cmm` -- `uses` --> `ent_component_linear_encoder`
  - `ent_product_hexagon_cmm` -- `measures` --> `ent_component_robot_gearbox`

## 应用场景

- **机器人关节检测**：测量关节壳体、输出法兰、轴承孔几何精度。
- **减速器检测**：齿轮、摆线轮、针齿壳的齿形与位置度测量。
- **整机标定**：结合测量臂进行机器人连杆参数与 DH 参数标定。

## 竞争对比

| 对比项 | Hexagon GLOBAL | ZEISS PRISMO | Wenzel LH |
|--------|------|------|------|
| 精度等级 | 微米级 | 亚微米级 | 微米级 |
| 软件 | PC-DMIS | CALYPSO | WM | Quartis |
| 优势 | 生态与稳定性 | 最高精度 | 性价比 |

## 选购与部署建议

- 根据算力/精度/场景需求选择对应型号，优先考虑官方支持的工具链与生态兼容性。
- 部署前确认供电、散热、机械接口与通信协议是否满足整机要求。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：海克斯康 / Hexagon](../companies/company_hexagon.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [海克斯康 / Hexagon 官方产品/公司页面](https://hexagon.com/products/coordinate-measuring-machines)
2. [Hexagon 官网](https://hexagon.com)
3. Hexagon GLOBAL 系列技术手册