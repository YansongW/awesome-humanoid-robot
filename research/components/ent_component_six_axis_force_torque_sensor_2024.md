---
$id: ent_component_six_axis_force_torque_sensor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Six Axis Force Torque Sensor
  zh: 六维力传感器
  ko: Six Axis Force Torque Sensor
summary:
  en: Sensor measuring forces and torques in all six degrees of freedom, critical for force-controlled manipulation.
  zh: '核心内容 ## 神源生 MLL 系列六维力传感器 / Shenyuansheng MLL Series 6-Axis Force Sensor'
  ko: 6자유도의 힘과 토크를 측정하는 센서, 힘 제어 조작에 필수적.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- force_control
- force_torque_sensor
- sensor
- six_axis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_shenyuan_6axis_sensor.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Six Axis Force Torque Sensor
  url: https://en.wikipedia.org/wiki/Force-sensing_resistor
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
六维力传感器是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 神源生 MLL 系列六维力传感器 / Shenyuansheng MLL Series 6-Axis Force Sensor

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [神源生科技 / Shenyuansheng](../companies/company_shenyuan.md) |
| **产品类别** | 铝合金模拟量六维力/力矩传感器 |
| **发布时间** | 持续在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [神源生 MLL 系列六维力传感器产品/资料页](http://www.nbit6d.com/product/687.html) |

### 产品概述

神源生 MLL 系列是针对科学仪器、精密测试及机器人应用设计的铝合金模拟量六维力传感器，可同时测量正交三方向的力与力矩。产品具有高刚度、高分辨率与低耦合误差特点，可选配 NST 系列数据采集器实现数字输出与实时分析。

### 产品图片

> 神源生 MLL 系列六维力传感器：请访问 [官方资料](http://www.nbit6d.com/product/687.html) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 铝合金模拟量六维力传感器 | 神源生官网 |
| 力测量范围（Fx/Fy/Fz） | 50 / 50 / 100 N（典型型号） | 神源生官网 |
| 力矩测量范围（Mx/My/Mz） | 2 / 2 / 4 Nm（典型型号） | 神源生官网 |
| 精度 | ≤ 0.5% FS | 神源生官网 |
| 分辨率 | 24 bit（配合采集器） | 神源生官网 |
| 过载能力 | ≥ 300% FS | 神源生官网 |
| 耦合误差 | ≤ 2% FS | 神源生官网 |
| 供电 | 5 – 24 VDC | 神源生官网 |
| 输出 | 模拟量 / USB / RS485（配采集器） | 神源生官网 |
| 采样频率 | 最高 1000 Hz | 神源生官网 |
| 工作温度 | 0℃ – +60℃ | 神源生官网 |
| 重量 | 约 200 g（因型号而异） | 神源生官网 |
| 价格 | 未公开 | - |

### 供应链位置

- **制造商**：[神源生科技 / Shenyuansheng](../companies/company_shenyuan.md)
- **核心零部件/技术来源**：航空铝合金、应变片、信号调理芯片、电缆与接插件
- **下游应用/客户**：协作机器人、人形机器人、医疗机器人、航空航天测试、高校科研

### 知识图谱节点与关系

- 产品实体：`ent_product_shenyuan_mll_6axis_sensor`
- 零部件实体：`ent_component_shenyuan_mll_sensor_core`
- 制造商实体：`ent_company_shenyuan`
- 关键关系：
  - `rel_ent_company_shenyuan_manufactures_ent_product_shenyuan_mll_6axis_sensor`（`ent_company_shenyuan` → `manufactures` → `ent_product_shenyuan_mll_6axis_sensor`）
  - `rel_ent_company_shenyuan_manufactures_ent_component_shenyuan_mll_sensor_core`（`ent_company_shenyuan` → `manufactures` → `ent_component_shenyuan_mll_sensor_core`）
  - `ent_product_shenyuan_mll_6axis_sensor` -- `uses` --> `ent_component_shenyuan_mll_sensor_core`

### 应用场景

- **协作机器人拖动示教、人形机器人手腕/脚踝力控、医疗手术力反馈、3C 装配、科学实验**

### 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 见规格参数表 | 同类产品 | 同类产品 |
| 核心优势 | 官方公开性能指标 | 竞品公开指标 | 竞品公开指标 |
| 生态/服务 | 制造商官方支持 | 竞品生态 | 竞品生态 |

### 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

### 相关词条

- [制造商：神源生科技 / Shenyuansheng](../companies/company_shenyuan.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

### 参考资料

1. [神源生科技官网](https://www.shenyuansheng.com)
2. [神源生 MLL 系列六维力传感器产品/资料页](http://www.nbit6d.com/product/687.html)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../index-companies.md)

## 参考
- [Six Axis Force Torque Sensor](https://en.wikipedia.org/wiki/Force-sensing_resistor)
- 项目 Wiki：appendix-d/products/product_shenyuan_6axis_sensor.md


