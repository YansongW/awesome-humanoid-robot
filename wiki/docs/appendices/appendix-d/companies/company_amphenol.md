# 安费诺 / Amphenol

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 安费诺 |
| **英文名** | Amphenol |
| **总部** | 美国康涅狄格州沃灵福德（Wallingford） |
| **成立时间** | 1932 |
| **官网** | [https://www.amphenol.com](https://www.amphenol.com) |
| **供应链环节** | 连接器、接插件、天线、线缆组件 |
| **企业属性** | 上市公司（NYSE: APH） |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、年报、产品 datasheet |

## 公司简介

Amphenol 是全球第二大连接器制造商，产品覆盖军事/航天、通信、汽车与工业市场。其高密度、高可靠连接器与线缆组件被用于机器人控制器、传感器、伺服系统与通信模块。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Minitek MicroSpace | 1.27 mm 紧凑型连接 | Minitek MicroSpace | 汽车电子、机器人控制器 |
| M12 / M8 圆形连接器 | 工业通信与传感器 | Amphenol M12 X-Code | 工业自动化、机器人 |
| RF 与天线 | 无线连接 | 5G/IoT 天线 | 移动机器人、AGV/AMR |

## 代表产品

### Amphenol Minitek MicroSpace 1.27 mm 线对板连接器

> Amphenol Minitek MicroSpace 1.27 mm 线对板连接器：请访问 [官方资料](https://www.amphenol.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 40（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 1.27 mm | 官方 catalog |
| 应用场景 | 汽车电子、机器人控制器、传感器接口 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：1.27 mm 紧凑间距，满足空间受限设计，支持自动化装配与多种镀层。

**应用场景**：机器人控制板、电机驱动、BMS、工业控制器、车载 ECU。

### Amphenol M12 X-Code 8 位圆形连接器

> Amphenol M12 X-Code 8 位圆形连接器：请访问 [官方资料](https://www.amphenol.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 8 | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP67 | 产品资料 |
| 传输速率 | 10 GbE | 产品资料 |
| 应用场景 | 工业以太网、机器人传感器、视觉系统 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：M12 标准接口，工业级防水防尘，支持高速以太网与高振动环境。

**应用场景**：协作机器人、工业机器人、AGV/AMR、工业相机、LiDAR。

## 供应链位置

- **上游关键零部件/材料**：铜合金、高性能塑料、电镀材料、线缆、磁材
- **下游客户/应用场景**：汽车、通信、工业自动化、机器人、航空航天
- **主要竞争对手/对标**：TE Connectivity、Molex、Hirose、JAE、J.S.T.

## 知识图谱节点与关系

- 公司实体：`ent_company_amphenol`
- 产品实体：`ent_product_amphenol_minitek_microspace`
- 零部件实体：`ent_component_amphenol_minitek_microspace`
- 关键关系：
  - `rel_ent_company_amphenol_manufactures_ent_product_amphenol_minitek_microspace`（`ent_company_amphenol` → `manufactures` → `ent_product_amphenol_minitek_microspace`）
  - `rel_ent_company_amphenol_manufactures_ent_component_amphenol_minitek_microspace`（`ent_company_amphenol` → `manufactures` → `ent_component_amphenol_minitek_microspace`）

## 参考资料

1. [官网](https://www.amphenol.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 产品目录](../index-products.md)