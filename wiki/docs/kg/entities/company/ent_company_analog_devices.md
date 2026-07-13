---
id: ent_company_analog_devices
type: company
'title:': Analog Devices / Analog Devices
domain: 02_components
theoretical_depth: system
aliases:
- Analog Devices
- Analog Devices
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_analog_devices_official
  type: website
  url: https://www.analog.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# analog_devices

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Analog Devices |
| **英文名** | Analog Devices |
| **总部** | 美国马萨诸塞州诺伍德 |
| **成立时间** | 1965 |
| **官网** | [https://www.analog.com](https://www.analog.com) |
| **供应链环节** | 模拟/混合信号 IC、惯性测量单元（IMU）、传感器接口 |
| **企业属性** | 上市公司（NASDAQ: ADI）、全球领先半导体公司 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、产品 datasheet、公开财报 |

## 公司简介

Analog Devices 是全球领先的模拟、混合信号与数字信号处理半导体公司，其 iSensor MEMS IMU 被广泛应用于机器人、航空航天与工业自动化。

ADI 提供高性能惯性测量单元（IMU）、加速度计、陀螺仪与信号调理芯片。ADIS16495 属于战术级 6 轴 IMU，具备低漂移、高抗冲击与宽温工作特性，适用于人形机器人姿态估计、导航与运动控制。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| iSensor IMU | 战术/工业级 IMU | ADIS16495 / ADIS16475 / ADIS16465 | 机器人、无人机、自动驾驶、工业控制 |
| MEMS 加速度计/陀螺仪 | 通用运动传感 | ADXL 系列 / ADIS 系列 | 消费电子、汽车、工业 |
| 信号链与电源 | 模拟前端与转换 | ADC/DAC / 放大器 / 电源管理 | 传感器接口、控制系统 |

## 代表产品

### Analog Devices ADIS16495

> Analog Devices ADIS16495：请访问 [官方资料](https://www.analog.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 封装 | 24 引脚模块（带连接器接口） | 官方 datasheet |
| 传感器类型 | 6 轴 IMU（3 轴陀螺仪 + 3 轴加速度计） | 官方 datasheet |
| 加速度计量程 | ±8 g | 官方 datasheet |
| 陀螺仪量程 | ±125°/s / ±450°/s / ±2000°/s（可选） | 官方 datasheet |
| 运行偏置稳定性 | 0.8°/hr（典型） | 官方 datasheet |
| 角随机游走 | 0.09°/√hr | 官方 datasheet |
| 接口 | SPI | 官方 datasheet |
| 供电电压 | 3.0 V – 3.6 V | 官方 datasheet |
| 工作电流 | 89 mA | 官方 datasheet |
| 工作温度 | -40°C ~ +105°C | 官方 datasheet |
| 抗冲击 | 2000 g | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：战术级精度、全温区校准、高抗冲击、SPI 数字输出，适合高动态机器人姿态估计。

**应用场景**：人形机器人 IMU、无人机飞控、自动驾驶、工业稳定平台、精密仪器。

### Analog Devices ADIS16475

> Analog Devices ADIS16475：请访问 [官方资料](https://www.analog.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感器类型 | 6 轴 IMU | 官方 datasheet |
| 封装 | 14 引脚模块 | 官方 datasheet |
| 陀螺仪量程 | ±125°/s / ±500°/s（可选） | 官方 datasheet |
| 加速度计量程 | ±8 g | 官方 datasheet |
| 工作温度 | -40°C ~ +105°C | 官方 datasheet |
| 接口 | SPI | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：小尺寸战术级 IMU，适合空间受限但对精度要求高的机器人平台。

**应用场景**：小型人形机器人、外骨骼、无人机、AGV。

## 供应链位置

- **上游关键零部件/材料**：MEMS 晶圆、ASIC 代工、封装材料、精密电阻电容
- **下游客户/应用场景**：机器人 OEM、无人机、自动驾驶、航空航天、工业自动化、医疗设备
- **主要竞争对手/对标**：Bosch Sensortec、STMicroelectronics、TDK InvenSense、Honeywell、NovAtel

## 知识图谱节点与关系

- 公司实体：`ent_company_analog_devices`
- 产品实体：`ent_component_analog_devices_adis16495`
- 产品实体：`ent_component_analog_devices_adis16475`
- 关键关系：
  - `ent_company_analog_devices` -- `manufactures` --> `ent_component_analog_devices_adis16495`
  - `ent_company_analog_devices` -- `manufactures` --> `ent_component_analog_devices_adis16475`

## 参考资料

1. [官网](https://www.analog.com)
2. [产品资料与公开报道](https://www.analog.com)
3. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)