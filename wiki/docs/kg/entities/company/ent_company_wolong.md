---
id: ent_company_wolong
schema_version: 1
type: company
'title:': Wolong Electric Drive
domain: 02_components
theoretical_depth: system
names:
  zh: 卧龙电驱
  en: Wolong Electric Drive
status: active
sources:
- id: src_wolong_official
  type: website
  url: https://www.wolong.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 卧龙电驱 / Wolong Electric Drive

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 卧龙电驱 |
| **英文名** | Wolong Electric Drive |
| **总部** | 中国绍兴 |
| **成立时间** | 1984 |
| **官网** | [https://www.wolong.com](https://www.wolong.com) |
| **供应链环节** | 电机 / 驱动 / 新能源汽车电机 / 工业电机 |
| **企业属性** | 上市公司（SH.600580）、国内品牌 |
| **母公司/所属集团** | 卧龙控股集团有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

全球知名电机与驱动解决方案供应商，工业电机与新能源汽车电机领域龙头。

卧龙电驱主营电机及驱动控制产品，涵盖低压/高压电机、伺服电机、新能源汽车驱动电机、工业变频器与储能系统。公司近年布局人形机器人与具身智能领域，提供高功率密度伺服电机与关节驱动解决方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 工业电机 | 低压/高压异步/同步电机 | WE3、WE4 系列 | 工业、能源 |
| 伺服电机 | 通用与专用伺服 | WM 系列 | 机床、机器人 |
| 新能源驱动电机 | 乘用车/商用车电机 | EV 平台 | 新能源汽车 |

## 代表产品

### 伺服电机 / Wolong Servo Motor

> 伺服电机：请访问 [官方资料](https://www.wolong.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 40/60/80/130 法兰 | 产品手册 |
| 重量 | 0.5–10 kg | 产品手册 |
| 额定功率 | 100 W – 7.5 kW | 产品手册 |
| 额定扭矩 | 0.32–48 N·m | 产品手册 |
| 额定转速 | 3,000 rpm | 产品手册 |
| 最高转速 | 6,000 rpm | 产品手册 |
| 防护等级 | IP65（部分型号） | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高功率密度、宽调速范围、支持多种编码器，适配机器人关节与自动化设备。

**应用场景**：工业机器人、人形机器人、数控机床、包装机械、新能源产线。

### 变频器 / 伺服驱动器 / Wolong Variable Frequency / Servo Drive

> 变频器 / 伺服驱动器：请访问 [官方资料](https://www.wolong.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | 产品手册 |
| 重量 | 未公开 | 产品手册 |
| 功率范围 | 0.4 kW – 630 kW | 产品手册 |
| 控制方式 | V/F、矢量、伺服 | 产品手册 |
| 通信协议 | Modbus、CANopen、EtherCAT | 产品手册 |
| 供电电压 | 单相/三相 220/380/690 V | 产品手册 |
| 保护功能 | 过压、过流、过热、短路 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：覆盖低压到高压全功率段，支持多总线，适用于大型自动化与新能源装备。

**应用场景**：工业产线、风机水泵、电梯、新能源车辆、人形机器人大功率关节。

## 供应链位置

- **上游关键零部件/材料**：硅钢片、铜线、磁材、轴承、功率器件（IGBT/SiC）、控制器芯片
- **下游客户/应用场景**：工业企业、新能源车企、机器人整机厂、能源装备、家电
- **主要竞争对手/对标**：西门子、ABB、WEG、汇川技术、大洋电机

## 知识图谱节点与关系

- 公司实体：`ent_company_wolong`
- 产品/零部件实体：`ent_component_wolong_servo_motor`, `ent_component_wolong_drive`
- 关键关系：
  - `ent_company_wolong` -- `manufactures` --> `ent_component_wolong_servo_motor`
  - `ent_company_wolong` -- `manufactures` --> `ent_component_wolong_drive`

## 参考资料

1. [官网](https://www.wolong.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）