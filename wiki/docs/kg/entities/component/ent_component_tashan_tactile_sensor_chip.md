---
id: ent_component_tashan_tactile_sensor_chip
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 他山科技数模混合 AI 触感芯片
  en: Tashan Mixed-Signal AI Tactile Sensor Chip
status: active
sources:
- id: src_tashan_intro_pdf
  type: datasheet
- title: 他山科技及芯片应用场景介绍
  url: https://download.s21i.co99.net/16926955/0/0/ABUIABA9GAAghZfIqQYo0p2srAc.pdf?f=%E4%BB%96%E5%B1%B1%E7%A7%91%E6%8A%80%E5%8F%8A%E8%8A%AF%E7%89%87%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF%E4%BB%8B%E7%BB%8D.pdf&v=1697778565
- id: src_tashan_sensor_china
  type: website
- title: SENSOR CHINA 2025 他山科技参展报道
  url: https://www.sekorm.com/news/584921525.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自他山科技公开资料与 SENSOR CHINA 报道；缺失值标注为“未公开”。
---


# 他山科技数模混合 AI 触感芯片 / Tashan Mixed-Signal AI Tactile Sensor Chip

## 概述

他山科技数模混合 AI 触感芯片（内部曾用代号 Ruby）是全球首款面向触觉感知的数模混合 AI 专用芯片。该芯片基于 R-SpiNNaker 分布式类脑架构，集成三维空间电容层析算法与脉冲神经网络（SNN），用于机器人指尖、电子皮肤与灵巧手等多维触觉感知。他山科技由清华背景的跨国研发团队创立，2017 年成立于北京。

## 工作原理 / 技术架构

芯片采用电容式触觉感知，通过检测电极间电容变化获取接触力、材质、接近觉与接触位置等信息。电容分辨率可达 1.6 aF（$10^{-18}$ F），转换速度 0.5 ms。R-SpiNNaker 架构模拟人体传入神经、中枢神经与传出神经三类神经元，支持片内单核/双核及小规模片间分布式 SNN 计算，实现多触觉单元的动态协同感知与协同控制。

电容变化量 $\Delta C$ 与介电常数、电极间距及接触面积相关，在平行板近似下：

$$
\Delta C \approx \varepsilon_0 \varepsilon_r \frac{\Delta A}{d} - \varepsilon_0 \varepsilon_r A \frac{\Delta d}{d^2}
$$

其中 $\varepsilon_0$ 为真空介电常数，$\varepsilon_r$ 为相对介电常数，$A$ 为电极面积，$d$ 为电极间距。芯片通过高分辨率 CDC（电容数字转换器）将皮法乃至阿法级电容变化转换为数字信号，再由 SNN 进行时序特征提取与材质识别。

## 关键参数表

| 参数 | 典型值 | 备注 |
|------|--------|------|
| 架构 | R-SpiNNaker 分布式类脑架构 | 他山科技公开资料 |
| 感知维度 | 三维力、材质、接近觉、接触位置等 7–10 维 | 公开报道 |
| 电容分辨率 | 1.6 aF | 产品资料 |
| 转换速度 | 0.5 ms | 产品资料 |
| 测力分辨率 | 0.01 N | 公开报道 |
| 材质识别 | 可识别 30+ 种材质 | 公开报道 |
| 接近觉距离 | 非接触识别 10 cm；接近觉位置判断 2 cm | 公开报道 |
| 产品系列 | TS3 / TS3A / TS3F / TS3M / TS4M 等 | 产品资料 |
| 代表芯片 TS3F500 | ARM Cortex-M3，64 MHz，256 KB Flash，96 KB SRAM，24 bit CDC × 32 | 产品资料 |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

## 应用场景

- 人形机器人灵巧手与电子皮肤
- 柔性/易碎物品自适应抓取
- 精密装配与力控操作
- 服务机器人触觉交互
- 汽车智能座舱与家电触控

## 供应链关系

制造商为北京他山科技有限公司（`ent_company_tashan`）。该芯片被其产品实体 `ent_product_tashan_tactile_skin` 使用。上游关键原材料包括电容敏感材料、柔性基材、ASIC 工艺、MEMS 代工与硅胶封装；下游客户包括人形机器人 OEM、灵巧手厂商、汽车电子与消费电子厂商。知识图谱中的关键关系为：`ent_company_tashan` -- `manufactures` --> `ent_component_tashan_tactile_sensor_chip`。

## 来源与验证

本卡片参数引自他山科技公开产品介绍资料与 SENSOR CHINA 2025 报道。具体型号量产状态、功耗、封装尺寸未公开。