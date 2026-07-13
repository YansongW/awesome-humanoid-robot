---
id: ent_component_sunrise_m4313sxx
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 宇立仪器 M4313SXX 系列六维力传感器
  en: Sunrise Instruments M4313SXX Six-axis Force Sensor
status: active
sources:
- id: src_sunrise_official
  type: website
  url: https://www.srisensor.com.cn/
- id: src_sunrise_m4313
  type: website
  url: https://srisensor.com.cn/1634.html
- id: src_sunrise_catalog
  type: white_paper
  url: https://www.worldrobotconference.com/profile/robot/download/2025/06/26/2025%20Force%20Sensor%20Product%20catalog_20250626104353A040.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 宇立仪器 M4313SXX 系列六维力传感器

## 概述

M4313SXX 系列是南宁宇立仪器有限公司（Sunrise Instruments）推出的工业级六维力/力矩传感器，专为协作机器人与工业机器人设计。该系列基于应变式测量原理，精度优于 **0.5% FS**，具备高达 **5 倍额定载荷的过载能力**，并支持 Ethernet TCP/IP、EtherCAT、RS485、RS232、USB 等多种通信方式，可直接安装到机器人末端或关节部位。

## 工作原理 / 技术架构

M4313SXX 采用应变式弹性体结构，外力/力矩作用于弹性体时产生应变，粘贴在弹性体上的应变片阻值变化，经惠斯通电桥转换为电压信号。六组桥路信号经放大、滤波与解耦算法处理后，得到六维力/力矩输出：

$$
\mathbf{F} = \begin{bmatrix} F_x & F_y & F_z & M_x & M_y & M_z \end{bmatrix}^{\mathsf{T}}
$$

若传感器额定力/力矩为 $F_{\text{FS}}$，则基于 0.5% FS 精度的可分辨力变化约为：

$$
\Delta F = F_{\text{FS}} \times 0.5\%
$$

该系列具备优异的零漂性能（$0.05\%/10℃$），并可在各轴承受 100 次 5 倍额定过载后仍保持不失效，适合冲击载荷较大的工业现场。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 南宁宇立仪器有限公司 / Sunrise Instruments |
| 类型 | 工业级六维力/力矩传感器 |
| 精度 | 优于 0.5% FS |
| 非线性/迟滞 | $< 0.5\%$ FS |
| 串扰 | $< 3\%$ FS |
| 过载能力 | 最高 5 倍额定量程 |
| 零漂性能 | 0.05%/10℃ |
| 通信接口 | Ethernet TCP/IP、EtherCAT、RS485、RS232、USB |
| 机械接口 | ISO 法兰接口 |
| 防护等级 | IP65（系列典型），部分型号可达 IP68 |
| 典型量程（力/力矩） | 50–800 N / 5–80 N·m（依型号） |
| 典型尺寸（OD×H） | 60–91 mm × 22.8–44.5 mm（依型号） |
| 典型重量 | 0.12–1.21 kg（依型号） |
| 价格 | 未公开 |

## 应用场景

- **协作机器人末端力控**：拖动示教、精密装配、力控打磨与去毛刺。
- **工业机器人腕部/脚踝**：柔顺抓取、平衡控制与人机安全交互。
- **人形机器人**：手腕、脚踝六维力反馈，支撑全身力控与步态调节。
- **汽车测试与精密装配**：悬架测试、插件力监测、3C 产线力控。

## 供应链关系

在公司—产品—零部件网络中，M4313SXX 属于**机器人力觉传感零部件层**：

- **上游**：应变片、弹性体钢材、信号调理电路、多接口数采模块、精密加工服务。
- **自身位置**：`ent_company_sunrise -- manufactures --> ent_component_sunrise_m4313sxx`。
- **下游**：协作机器人厂商、人形机器人 OEM、工业自动化集成商、汽车测试设备商。

## 来源与验证

- 宇立仪器官网：https://www.srisensor.com.cn/
- M4313XXX 系列产品页：https://srisensor.com.cn/1634.html
- 宇立仪器力传感器产品目录 PDF：https://www.worldrobotconference.com/profile/robot/download/2025/06/26/2025%20Force%20Sensor%20Product%20catalog_20250626104353A040.pdf

精度、过载能力、零漂与通信接口均来自宇立仪器官方公开资料；具体型号的量程、尺寸与重量可在产品目录中按型号查询，价格未公开。