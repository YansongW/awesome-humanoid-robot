---
id: ent_company_omron
schema_version: 1
type: company
'title:': OMRON Corporation
domain: 02_components
theoretical_depth: system
names:
  zh: 欧姆龙
  en: OMRON Corporation
aliases:
- 欧姆龙
- OMRON
status: active
sources:
- id: ent_company_omron_official
  type: website
  url: https://www.omron.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13 00:00:00+00:00
---





# 欧姆龙 / OMRON Corporation

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 欧姆龙 |
| **英文名** | OMRON Corporation |
| **总部** | 日本京都 |
| **成立时间** | 1933 年 |
| **官网** | [https://www.omron.com](https://www.omron.com) |
| **供应链环节** | 工业自动化、控制设备、传感器、伺服系统、工业机器人 |
| **企业属性** | 上市公司（TYO：6645） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 欧姆龙官网、产品手册、公开财报 |

## 公司简介

欧姆龙是以“Sensing & Control + Think”为核心技术的全球工业自动化与电子元器件企业。

欧姆龙工业自动化业务覆盖 PLC、运动控制、机器视觉、传感器、安全组件及工业机器人，产品以高可靠性和紧凑设计著称。其 Sysmac 平台将逻辑、运动、机器人和视觉整合在同一架构下，可为 3C 电子、汽车、食品包装等行业提供从单机到整线的自动化能力。其传感与控制技术亦可用于人形机器人环境感知与执行单元。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 控制器 / PLC | 逻辑与运动一体化 | NX / NJ Sysmac | 3C、汽车、包装 |
| 伺服与运动控制 | 高精度电机控制 | 1S / G5 系列伺服 | 电子、机床、机器人 |
| 视觉与传感器 | 检测、测量与识别 | FH 视觉系统 / E3AS 光电 | 质检、定位、机器人引导 |

## 代表产品

### OMRON NJ501 Sysmac 控制器

> OMRON NJ501 Sysmac 控制器：请访问 [官方资料](https://www.omron.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 机器自动化控制器（MAC） | 官方资料 |
| 最大控制轴数 | 64 轴（EtherCAT） | 官方资料 |
| 最大 I/O 点数 | 2,560 点 | 官方资料（依型号） |
| 程序容量 | 未公开 | 未公开 |
| 通信接口 | EtherCAT、EtherNet/IP、USB、OPC UA | 官方资料 |
| 编程标准 | IEC 61131-3 / PLCopen 运动控制功能块 | 官方资料 |
| 供电电压 | 24 VDC | 官方资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：PLC 与运动控制融合、最多 64 轴 EtherCAT 同步控制、统一编程环境 Sysmac Studio。

**应用场景**：3C 电子装配、汽车零件加工、包装机械、机器人单元控制、人形机器人关节运动控制。

## 与人形机器人的关联

人形机器人关节数量多、对同步运动控制要求高，Sysmac 的多轴 EtherCAT 控制能力与紧凑 I/O 可为中小规模人形机器人本体开发与测试提供控制平台。

## 供应链位置

- **上游关键零部件/材料**：MCU、传感器芯片、功率半导体、PCB、连接器、编码器
- **下游客户/应用场景**：3C 电子、汽车、食品饮料、医疗、半导体设备
- **主要竞争对手/对标**：Mitsubishi Electric, Siemens, Schneider Electric, Keyence

## 知识图谱节点与关系

- 公司实体：`ent_company_omron`
- 产品实体：`ent_product_omron_nj501`
- 关键关系：
  - `ent_company_omron` -- `manufactures` --> `ent_product_omron_nj501`

## 参考资料

1. [欧姆龙 官网](https://www.omron.com)
2. [OMRON NJ501 Sysmac 控制器 产品页](https://www.omron.com.cn/products/family/3194/)
3. OMRON FA product catalog / Sysmac Studio documentation