---
id: ent_component_jiangsu_leili_stepper_motor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 江苏雷利 57BYGH 混合式步进电机
  en: Jiangsu Leili 57BYGH Hybrid Stepper Motor
status: active
sources:
- id: src_leili_57bygh_page
  type: website
  url: https://www.leili-motor.net/product/57bygh.html
- id: src_leili_company_about
  type: website
  url: https://www.leili-motor.net/about/
- id: src_wantmotor_57bygh
  type: website
  url: https://www.wantmotor.com/products/57bygh-series/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 江苏雷利 57BYGH 混合式步进电机 / Jiangsu Leili 57BYGH Hybrid Stepper Motor

## 概述

57BYGH 系列是江苏雷利电机股份有限公司（Jiangsu Leili Motor Co., Ltd.）生产的两相混合式步进电机，机座尺寸为 57 mm（NEMA 23），兼具永磁式与反应式步进电机的优点，具有定位精度高、转矩大、运行平稳等特点。该系列广泛应用于 3D 打印机、CNC 雕刻机、纺织机械、医疗设备、安防云台及小型机器人关节等场景。

## 工作原理 / 技术架构

混合式步进电机转子由轴向充磁的永磁体与带齿的软磁材料组成，定子为均匀分布的多极绕组。通过依次切换定子相电流，使转子齿与定子磁场对齐，从而实现步进旋转。

步距角 $\theta_s$ 由转子齿数 $N_r$ 与相数 $m$ 决定：

$$
\theta_s = \frac{360^\circ}{N_r \cdot m}
$$

57BYGH 系列典型步距角为 $1.8^\circ$/step，即每转 200 步。通过驱动器微步细分后，实际步距角可进一步减小：

$$
\theta_{\mu} = \frac{\theta_s}{n_{\text{microstep}}}
$$

例如 16 细分时 $\theta_{\mu} = 0.1125^\circ$。

保持转矩（holding torque）是步进电机在额定电流下静止时可承受的最大外部转矩：

$$
\tau_{\text{hold}} \propto N \cdot I \cdot \Phi
$$

其中 $N$ 为绕组匝数，$I$ 为相电流，$\Phi$ 为永磁体磁通。57BYGH 系列保持转矩常见范围为 0.4 ~ 1.8 N·m。

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 机座型号 | 57 mm（NEMA 23） |
| 电机类型 | 两相混合式步进电机 |
| 步距角 | 1.8° / step（200 steps/rev） |
| 相数 | 2 相 |
| 保持转矩 | 0.4 ~ 1.8 N·m（依型号） |
| 额定电流 | 1.0 ~ 4.0 A（依型号） |
| 额定电压 | 2.4 ~ 6.0 V（依型号，电感压降） |
| 相电阻 | 0.3 ~ 5.6 Ω（依型号） |
| 相电感 | 0.6 ~ 10 mH（依型号） |
| 转子惯量 | 135 ~ 460 g·cm²（依型号） |
| 绝缘等级 | Class B / F |
| 防护等级 | IP40（可定制 IP54） |
| 工作温度 | -20 °C ~ 50 °C |
| 引线数 | 4 / 6 / 8 线（依型号） |

## 应用场景

- 3D 打印机与 CNC 雕刻机定位轴；
- 纺织机械、包装机械的精确定位；
- 医疗设备、安防云台、舞台灯光的低速精确转动；
- 小型机器人关节、机械臂与自动化夹具；
- 阀门控制、打印机等办公设备。

## 供应链关系

`ent_component_jiangsu_leili_stepper_motor` 由江苏雷利电机股份有限公司设计制造，属于执行层零部件中的步进电机类别。其上游依赖硅钢片、永磁体、漆包线、轴承与机壳等；下游面向 3D 打印、CNC、医疗、安防与小型机器人等整机厂商。该电机通常与步进驱动器配套使用，在机器人领域可作为低惯量、低成本的关节或末端执行器驱动单元。

## 来源与验证

- 江苏雷利官网 57BYGH 产品页列出机座尺寸 57 mm、步距角 1.8°、保持转矩范围、额定电流、相电阻/电感等参数区间。
- 江苏雷利公司简介页面说明了其在步进电机、直流电机、伺服电机领域的产品布局。
- WantMotor 的 57BYGH 系列参考页提供了行业通用的 NEMA 23 步进电机参数区间，与官方数据一致。
- 表中具体数值为系列范围，单型号精确参数需以对应 datasheet 为准。