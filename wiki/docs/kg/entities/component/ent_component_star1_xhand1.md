---
id: ent_component_star1_xhand1
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 星动纪元 XHAND1 灵巧手
  en: RobotEra XHAND1 Dexterous Hand
status: active
sources:
- id: src_robotera_star1_pdf
  type: website
  url: https://www.robotera.com/upload/goods/20250108/c8e2f76b3177dd9f2483fef1176fe85e.pdf
- id: src_robotera_xhand1_pdf
  type: website
  url: https://www.robotera.com/upload/goods/20241208/2ab64afaae0098db948e9d4063951c28.pdf
- id: src_humanoid_guide_xhand1
  type: website
  url: https://humanoid.guide/product/xhand1/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 星动纪元 XHAND1 灵巧手 / RobotEra XHAND1 Dexterous Hand

## 概述

XHAND1 是星动纪元（RobotEra）推出的首款产品级五指灵巧手，专为高性能人形机器人设计，也可独立用于科研、工业遥操作与 AI 训练。该手采用全主动关节驱动方案，拇指与食指各 3 个自由度，其余三指各 2 个自由度，共 12 个主动自由度。XHAND1 具备高分辨率指尖触觉感知、电流环力控与反驱能力，已作为 STAR1 人形机器人的末端执行器实现抓握、工具操作与精细作业。

## 工作原理 / 技术架构

XHAND1 采用“全齿轮准直驱（Quasi-Direct Drive）”传动架构：

- **全主动关节**：12 个自由度均由独立电机 + 齿轮减速驱动，所有主动关节局部布置且解耦，避免欠驱动方案的自由度耦合问题。
- **力控与反驱**：每个关节可反驱，冲击时可通过电机电流感知外力，结合低阻尼设计实现电流环力控。关节输出力矩与电流的关系可表示为
  \[
  \tau = K_t \, I
  \]
  其中 \(K_t\) 为关节扭矩常数，\(I\) 为电机电流。通过控制电流即可间接控制力矩，实现柔顺抓取。
- **触觉感知**：每个指尖配备 270° 环绕式高密度三维力/温度触觉阵列（单指 120–300 个采样点），最小力分辨率约 0.05 N，可感知接触力、滑移、表面纹理与温度。
- **通信与控制**：支持 EtherCAT 与 RS485 通信，整手控制频率 83 Hz；提供 Linux SDK、C++/Python 接口与 ROS 支持，兼容 Vision Pro 遥操作与 MANUS 数据手套。

指尖载荷能力可近似用摩擦模型估算：最大指尖力 \(F_{\text{tip}}\) 与摩擦系数 \(\mu\) 决定单指可提起的重量 \(m = F_{\text{tip}} \mu / g\)。公开数据表明 XHAND1 指尖力 15 N，单指可提起超过 5 kg 负载。

## 关键参数表

| 参数项 | 数值 |
|---|---|
| 自由度 | 12 主动（拇指 3 + 食指 3 + 中指 2 + 无名指 2 + 小指 2） |
| 外形尺寸 | 191 mm × 94 mm × 47 mm |
| 重量 | 1.1 kg |
| 指尖力 | 15 N |
| 单手最大握力 | 80 N |
| 指尖夹持力 | ≥15 N |
| 最大抓取负载（掌心向上） | 25 kg |
| 最大抓取负载（掌心向下） | 16 kg |
| 食指侧摆角度 | ±15° |
| 拇指活动角度 | <110° |
| 最小抓取直径 | 16 mm |
| 指尖重复定位精度 | ±0.20 mm |
| 开合重复频率 | >2 Hz |
| 反驱阻尼 | ≤0.1 N·m |
| 触觉阵列 | 每指 120–300 个三维力采样点，270° 环绕 |
| 力控分辨率 | 约 0.05 N |
| 工作电压 | 24–72 V |
| 静态功耗 | 约 7 W（@48 V，0.15 A） |
| 峰值功耗 | 约 120 W（@48 V，2.5 A） |
| 通信接口 | EtherCAT / RS485 |
| 控制频率 | 83 Hz |
| 无负载抓握寿命 | 100 万次 |
| 工作温度 | −20 °C 至 60 °C |

## 应用场景

- **人形机器人末端执行器**：作为 STAR1/L7 人形机器人的手部，执行抓取、搬运、工具操作与精细装配。
- **遥操作与数据收集**：配合 Vision Pro 或 MANUS 手套进行远程操作，为模仿学习与强化学习采集 demonstration 数据。
- **工业柔性装配**：利用力控与触觉反馈完成插销、拧螺丝、分拣易损件等任务。
- **科研与假肢**：用于机器人灵巧操作算法验证、人机交互与假肢原型开发。

## 供应链关系

- **上游**：空心杯/微型伺服电机、精密齿轮、触觉传感器阵列、驱动电路板、结构件铝合金、线缆与接插件。
- **制造商**：星动纪元（RobotEra）自主研发与生产。
- **下游**：人形机器人整机（STAR1、L7）、科研机构、工业自动化集成商、医疗康复设备开发者。
- **图谱位置**：`ent_company_robotera` → `manufactures` → `ent_component_star1_xhand1`；并通过 `used_in` 关系嵌入 `ent_product_robotera_star1` 等人形机器人产品。

## 来源与验证

- 外形尺寸、自由度、负载与功耗等核心参数来自 RobotEra 官方 STAR1 与 XHAND1 产品资料 PDF。
- 触觉传感器细节、力控分辨率与遥操作兼容性来自 Humanoid.guide 及第三方经销商产品页。
- 未公开项已在表中标注或省略，未作臆测。