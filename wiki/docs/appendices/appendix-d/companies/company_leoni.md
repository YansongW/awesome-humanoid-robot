# 莱尼 / LEONI

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 莱尼 |
| **英文名** | LEONI |
| **总部** | 德国纽伦堡 |
| **成立时间** | 1917 |
| **官网** | [https://www.leoni.com](https://www.leoni.com) |
| **供应链环节** | 电缆、线束、连接系统 |
| **企业属性** | 上市公司（XETRA: LEO） |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、年报、产品 catalog |

## 公司简介

LEONI 是全球领先的电缆与线束系统供应商，业务覆盖汽车、工业、医疗与通信。其 Dacar 数据电缆、机器人电缆与定制线束可满足高柔性、耐扭转、耐油、耐弯折的人形机器人布线需求。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Dacar 数据电缆 | 车载/工业数据通信 | Dacar 302 | ADAS、机器人传感器网络 |
| 机器人电缆 | 高柔性动力/控制电缆 | LEONI Robotic Cable | 工业机器人、协作机器人 |
| 线束系统 | 整车/整机线束 | 定制线束 | 汽车、人形机器人 OEM |

## 代表产品

### LEONI Dacar® 302 汽车以太网电缆

> LEONI Dacar® 302 汽车以太网电缆：请访问 [官方资料](https://www.leoni.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 芯线数 | 1 对（2 芯） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 传输速率 | 100 Mbps（100BASE-T1） | 官方 catalog |
| 耐温范围 | -40°C ~ +105°C | 官方 catalog |
| 屏蔽 | 整体屏蔽 | 产品资料 |
| 应用场景 | 车载/机器人传感器网络、摄像头、LiDAR | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：专为单对以太网设计，轻量、耐高温、屏蔽良好，适合机器人长距离数据通信。

**应用场景**：自动驾驶/机器人传感器总线、工业相机、LiDAR、域控制器互联。

### LEONI 机器人高柔性电缆

> LEONI 机器人高柔性电缆：请访问 [官方资料](https://www.leoni.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 芯线数 | 按定制（常见 4G0.75 mm²） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 300/500 V | 产品资料 |
| 防护等级 | IP40（线缆本体，取决于连接器） | 产品资料 |
| 弯曲寿命 | 未公开 | 官方 datasheet |
| 应用场景 | 机器人关节、拖链、伺服电机连接 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：高柔性、耐扭转、耐油、阻燃，适合连续运动的机器人关节与拖链布线。

**应用场景**：工业机器人、协作机器人、人形机器人关节、CNC 机床拖链。

## 供应链位置

- **上游关键零部件/材料**：铜杆、PVC/TPE/PUR 绝缘材料、铝箔/编织屏蔽、连接器
- **下游客户/应用场景**：汽车主机厂、机器人 OEM、工业自动化、医疗设备
- **主要竞争对手/对标**：Prysmian、Nexans、Lapp、Igus、Coroplast

## 知识图谱节点与关系

- 公司实体：`ent_company_leoni`
- 产品实体：`ent_product_leoni_dacar_302`
- 零部件实体：`ent_component_leoni_dacar_302`
- 关键关系：
  - `rel_ent_company_leoni_manufactures_ent_product_leoni_dacar_302`（`ent_company_leoni` → `manufactures` → `ent_product_leoni_dacar_302`）
  - `rel_ent_company_leoni_manufactures_ent_component_leoni_dacar_302`（`ent_company_leoni` → `manufactures` → `ent_component_leoni_dacar_302`）

## 参考资料

1. [官网](https://www.leoni.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 产品目录](../index-products.md)