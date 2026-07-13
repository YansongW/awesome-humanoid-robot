---
id: ent_company_panasonic
schema_version: 1
type: company
'title:': Panasonic Holdings Corporation / Panasonic Industry Co., Ltd.
domain: 02_components
theoretical_depth: system
names:
  zh: 松下控股 / 松下电器机电
  en: Panasonic Holdings Corporation / Panasonic Industry Co., Ltd.
aliases:
- 松下控股 / 松下电器机电
- Panasonic
status: active
sources:
- id: ent_company_panasonic_official
  type: website
  url: https://www.panasonic.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13 00:00:00+00:00
---





# 松下控股 / 松下电器机电 / Panasonic Holdings Corporation / Panasonic Industry Co., Ltd.

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 松下控股 / 松下电器机电 |
| **英文名** | Panasonic Holdings Corporation / Panasonic Industry Co., Ltd. |
| **总部** | 日本大阪 |
| **成立时间** | 1918 年 |
| **官网** | [https://www.panasonic.com](https://www.panasonic.com) |
| **供应链环节** | 工业自动化、伺服电机、PLC、传感器、电子元器件 |
| **企业属性** | 上市公司（TYO：6752，控股公司）；工业自动化业务由 Panasonic Industry 运营 |
| **母公司/所属集团** | Panasonic Holdings Corporation |
| **数据来源** | Panasonic 官网、Panasonic Industry 产品样本、公开财报 |

## 公司简介

松下是全球知名的电子与工业自动化产品制造商，其工业自动化业务由 Panasonic Industry 负责运营。

Panasonic Industry 提供 MINAS 系列伺服系统、FP 系列 PLC、传感器、连接器、电池、电机等工业自动化核心零部件。MINAS A6 系列以 2.0 kHz 速度响应、23 位绝对值编码器和紧凑设计著称，广泛应用于电子制造、半导体、机器人与精密平台。松下还为机器人提供圆柱电池与无刷电机等关键零部件。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 伺服系统 | 高速响应伺服电机/驱动 | MINAS A6 系列 | 电子、半导体、机器人 |
| PLC / 控制器 | 紧凑型可编程控制器 | FP-XH / FP0H / FP7 | 3C、包装、设备 |
| 元器件与电池 | 传感器、连接器、电池 | PM 继电器 / 18650 圆柱电池 | 汽车、机器人、能源 |

## 代表产品

### Panasonic MINAS A6 伺服系统

> Panasonic MINAS A6 伺服系统：请访问 [官方资料](https://www.panasonic.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 交流伺服电机 + 驱动器 | 官方资料 |
| 功率范围 | 50 W ~ 5 kW | 官方资料（依型号） |
| 速度响应 | 2.0 kHz | 官方资料 |
| 编码器 | 23 位绝对值编码器 | 官方资料 |
| 通信接口 | EtherCAT / RTEX / Modbus（依型号） | 官方资料 |
| 控制模式 | 位置 / 速度 / 转矩 / 全闭环 | 官方资料 |
| 防护等级 | IP67（电机，依型号）/ IP20（驱动器） | 官方资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：2.0 kHz 高速响应、23 位高精度绝对值编码器、紧凑轻量化设计、丰富的总线选项。

**应用场景**：3C 电子贴片、半导体设备、数控机床、工业机械手、人形机器人手臂与手指关节。

## 与人形机器人的关联

人形机器人手指、手腕等小空间关节需要小型、高速响应伺服，MINAS A6 的紧凑电机与高精度编码器可为人形机器人末端关节提供精细力控基础。

## 供应链位置

- **上游关键零部件/材料**：稀土磁材、硅钢片、编码器芯片、功率半导体、PCB、外壳
- **下游客户/应用场景**：3C 电子、半导体、汽车、机器人、医疗设备
- **主要竞争对手/对标**：Yaskawa, Mitsubishi Electric, Inovance, Kollmorgen

## 知识图谱节点与关系

- 公司实体：`ent_company_panasonic`
- 产品实体：`ent_product_panasonic_minas_a6`
- 关键关系：
  - `ent_company_panasonic` -- `manufactures` --> `ent_product_panasonic_minas_a6`

## 参考资料

1. [松下控股 / 松下电器机电 官网](https://www.panasonic.com)
2. [Panasonic MINAS A6 伺服系统 产品页](https://industry.panasonic.com/global/en/motor/servo_motor/a6)
3. Panasonic Industry MINAS A6 servo catalog