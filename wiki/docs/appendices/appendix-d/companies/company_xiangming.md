# 祥明智能 / Xiangming Intelligent

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 祥明智能 |
| **英文名** | Xiangming Intelligent Technology |
| **总部** | 中国常州 |
| **成立时间** | 1995 |
| **官网** | [https://www.xiangmingmotor.com](https://www.xiangmingmotor.com) |
| **供应链环节** | 电机 / EC 风机 / 驱动控制 |
| **企业属性** | 上市公司（SZ.301226）、国内品牌 |
| **母公司/所属集团** | 常州祥明智能动力股份有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

国内 EC 风机与智能电机领先企业，产品聚焦高效节能与数字化驱动。

祥明智能专业从事 EC（Electronically Commutated）电机、风机及智能驱动控制系统的研发与生产，产品广泛应用于 HVAC、冷链、通信、新能源汽车与机器人热管理。公司具备电机设计、电子控制与系统集成能力，可为机器人提供高效散热风机、伺服风机及定制化驱动方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| EC 电机 | 永磁无刷高效电机 | EC 系列 | HVAC、冷链、机器人 |
| EC 风机 | 离心/轴流高效风机 | XM-EC 系列 | 数据中心、新能源汽车、机器人 |
| 智能驱动 | 电机控制器与 BMS | 未公开 | 风机、泵、机器人热管理 |

## 代表产品

### EC 永磁无刷电机 / Xiangming EC Permanent Magnet BLDC Motor

> EC 永磁无刷电机：请访问 [官方资料](https://www.xiangmingmotor.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø60–Ø250 mm（系列范围） | 产品手册 |
| 额定功率 | 20 W–1 kW | 产品手册 |
| 额定转速 | 1,000–4,000 rpm | 产品手册 |
| 额定电压 | 24–380 VAC / VDC | 产品手册 |
| 效率 | ≥80%（部分型号 ≥90%） | 产品手册 |
| 调速方式 | 0–10 V / PWM / Modbus 可选 | 产品手册 |
| 防护等级 | IP44–IP55 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：电子换向、高效率、宽调速范围，支持智能控制与远程监控，适合节能与热管理场景。

**应用场景**：人形机器人热管理、新能源汽车热管理、数据中心散热、冷链通风。

### EC 离心风机 / Xiangming EC Centrifugal Fan

> EC 离心风机：请访问 [官方资料](https://www.xiangmingmotor.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 叶轮直径 | 133–400 mm（系列范围） | 产品手册 |
| 风量 | 100–5,000 m³/h | 产品手册 |
| 静压 | 50–1,500 Pa | 产品手册 |
| 额定功率 | 30–750 W | 产品手册 |
| 供电电压 | 24–380 VAC / VDC | 产品手册 |
| 噪音水平 | ≤ 70 dB(A) | 产品手册 |
| 调速接口 | 0–10 V / PWM / RS-485 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高效叶轮设计、低噪音、集成 EC 电机与控制器，可直接替换传统 AC 风机实现节能。

**应用场景**：机器人整机的散热与热管理、通信基站、新能源储能、暖通空调。

## 供应链位置

- **上游关键零部件/材料**：永磁体、硅钢片、铜线、电子元器件、塑料粒子、铝材
- **下游客户/应用场景**：HVAC 设备商、数据中心、新能源汽车、机器人整机厂、冷链物流
- **主要竞争对手/对标**：ebm-papst、Ziehl-Abegg、泛仕达、朗伟股份、江苏雷利

## 知识图谱节点与关系

- 公司实体：`ent_company_xiangming`
- 产品/零部件实体：`ent_component_xiangming_ec_motor`, `ent_component_xiangming_ec_fan`
- 关键关系：
  - `ent_company_xiangming` -- `manufactures` --> `ent_component_xiangming_ec_motor`
  - `ent_company_xiangming` -- `manufactures` --> `ent_component_xiangming_ec_fan`

## 参考资料

1. [官网](https://www.xiangmingmotor.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.xiangmingmotor.com/product)（请按实际产品型号核对）