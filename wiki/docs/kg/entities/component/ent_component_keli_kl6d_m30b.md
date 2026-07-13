---
id: ent_component_keli_kl6d_m30b
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 柯力传感 KL6D-M30-B 系列六维力/力矩传感器
  en: Keli KL6D-M30-B Six-axis Force/Torque Sensor
status: active
sources:
- id: src_keli_official
  type: website
  url: https://www.kelichina.com/
- id: src_sina_keli
  type: website
  url: https://finance.sina.com.cn/stock/relnews/cn/2025-04-03/doc-inerwmtr2673181.shtml
- id: src_aibangbots
  type: website
  url: https://www.aibangbots.com/a/2708
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 柯力传感 KL6D-M30-B 系列六维力/力矩传感器

## 概述

KL6D-M30-B 系列是宁波柯力传感科技股份有限公司（上交所：603662）面向机器人场景开发的六维力/力矩传感器。该产品基于高精度电阻应变式测量原理，可同时测量三维力（$F_x, F_y, F_z$）与三维力矩（$M_x, M_y, M_z$），公开报道精度达 **0.1% FS**，采样率为 **1 kHz**，主要用于人形机器人手腕/脚踝、协作机器人末端及工业机械臂力控场景。

## 工作原理 / 技术架构

六维力传感器的弹性体结构上布有多组应变片。当外力/力矩作用于传感器时，弹性体产生微小形变，导致应变片电阻变化。应变片组成惠斯通电桥，输出电压信号与应变成正比：

$$
\Delta V = V_{\text{in}} \cdot \frac{\Delta R}{4R}
$$

其中 $V_{\text{in}}$ 为激励电压，$\Delta R/R$ 为应变片相对电阻变化。传感器采集多路桥路信号后，通过结构解耦与算法解耦将原始输出映射到六维力/力矩向量：

$$
\mathbf{F} = \begin{bmatrix} F_x & F_y & F_z & M_x & M_y & M_z \end{bmatrix}^{\mathsf{T}}
$$

测量精度通常以满量程（Full Scale, FS）的百分比表示。若某型号满量程力为 $F_{\text{FS}}$，则绝对力分辨率约为：

$$
\Delta F = F_{\text{FS}} \times 0.1\%
$$

柯力公开披露其具备高速采样数字通讯能力，并可通过外接数采模块实现与机器人控制器的实时数据交互。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 宁波柯力传感科技股份有限公司 |
| 类型 | 机器人专用六维力/力矩传感器 |
| 测量原理 | 高精度电阻应变式 |
| 精度 | 0.1% FS（公开报道） |
| 采样率 | 1 kHz（公开报道） |
| 测量维度 | 6D（三维力 + 三维力矩） |
| 通信方式 | 高速采样数字通讯（外接数采） |
| 尺寸 | 未公开 |
| 重量 | 未公开 |
| 价格 | 未公开 |

## 应用场景

- **人形机器人力控**：安装于手腕、脚踝，实现柔顺抓取、平衡调节与安全交互。
- **协作机器人末端**：拖动示教、精密装配、力控打磨与抛光。
- **工业机械臂**：受力检测、插拔力监测与柔性产线质量控制。
- **汽车测试**：悬架、转向系统动态力学分析。

## 供应链关系

在公司—产品—零部件网络中，KL6D-M30-B 属于**机器人感知零部件层**：

- **上游**：应变片、高性能结构钢、ASIC 信号调理芯片、封装材料、精密加工服务。
- **自身位置**：`ent_company_keli -- manufactures --> ent_component_keli_kl6d_m30b`；`ent_component_keli_kl6d_m30b -- used_in --> ent_product_humanoid_robot_wrist`。
- **下游**：人形机器人整机厂、协作机器人厂商、工业自动化集成商及汽车 OEM。

## 来源与验证

- 柯力传感官网：https://www.kelichina.com/
- 新浪财经报道：https://finance.sina.com.cn/stock/relnews/cn/2025-04-03/doc-inerwmtr2673181.shtml
- 爱邦机器人行业整理：https://www.aibangbots.com/a/2708

0.1% FS 精度与 1 kHz 采样率来自公开报道；具体型号的机械尺寸、量程范围与价格未在官方公开资料中披露。