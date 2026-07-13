---
id: ent_product_tashan_tactile_skin
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 他山科技 TS-F+ 多模态触觉传感器
  en: Tashan TS-F+ Multimodal Tactile Sensor
status: active
sources:
- id: src_tashan_official
  type: website
  url: https://www.iteschina.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 他山科技 TS-F+ 多模态触觉传感器 / Tashan TS-F+ Multimodal Tactile Sensor

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [他山科技 / Tashan Technology](../../../appendices/appendix-d/companies/company_tashan.md) |
| **产品类别** | 多模态触觉传感器 / 电子皮肤 |
| **发布时间** | 2024 年（世界机器人大会首发） |
| **状态** | 量产/商用 |
| **官网/来源** | [他山科技官网](https://www.iteschina.com) |

## 产品概述

他山科技 TS-F+ 多模态触觉传感器是一款面向人形机器人灵巧手与电子皮肤的高集成度电容式触觉传感单元。传感器搭载他山科技自研的数模混合 AI 触感芯片，基于 R-SpiNNaker 分布式类脑架构与脉冲神经网络（SNN），可从混合信号中提取 7–10 维触觉信息，包括三维力、材质识别、接近觉与接触位置等。

TS-F+ 支持在复杂环境下对柔性、易碎、异形物体的自适应力抓取，可完成握笔、倒水、抓鸡蛋等精细操作。他山科技还基于 MuJoCo 与 NVIDIA Isaac Sim 推出了开源触觉仿真模型，使开发者能够在仿真环境中低成本训练触觉感知策略，并与真实传感器数据对齐。

## 产品图片

> Tashan TS-F+：请访问 [官方资料](https://www.iteschina.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感原理 | 电容式 | 官网/公开报道 |
| 感知维度 | 三维力、材质、接近觉、接触位置等 7–10 维 | 公开报道 |
| 核心芯片 | 自研数模混合 AI 触感芯片 | 公开报道 |
| 芯片架构 | R-SpiNNaker 分布式类脑架构 | 公开报道 |
| 算法模型 | 三维空间电容层析 + SNN 脉冲神经网络 | 公开报道 |
| 空间分辨率 | 未公开 | - |
| 传感点密度 | 未公开 | - |
| 量程（法向力） | 未公开 | - |
| 响应时间 | 未公开 | - |
| 采样频率 | 未公开 | - |
| 通信接口 | 数字接口（兼容主流机器人总线） | 官网公开资料 |
| 供电电压 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 防护等级 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[他山科技 / Tashan Technology](../../../appendices/appendix-d/companies/company_tashan.md)
- **核心零部件/技术来源**：自研数模混合 AI 触感芯片、R-SpiNNaker 类脑架构、电容式敏感材料；柔性基材与封装材料外购。
- **下游应用/客户**：人形机器人灵巧手、协作机器人末端、电子皮肤、汽车内饰、家电触控、消费电子。

## 知识图谱节点与关系

- 产品实体：`ent_product_tashan_tactile_skin`
- 制造商实体：`ent_company_tashan`
- 零部件实体：`ent_component_tashan_tactile_sensor_chip`
- 关键关系：
  - `rel_ent_company_tashan_manufactures_ent_product_tashan_tactile_skin`（`ent_company_tashan` → `manufactures` --> `ent_product_tashan_tactile_skin`）
  - `rel_ent_company_tashan_manufactures_ent_component_tashan_tactile_sensor_chip`（`ent_company_tashan` → `manufactures` --> `ent_component_tashan_tactile_sensor_chip`）
  - `rel_ent_product_tashan_tactile_skin_uses_ent_component_tashan_tactile_sensor_chip`（`ent_product_tashan_tactile_skin` → `uses` --> `ent_component_tashan_tactile_sensor_chip`）

## 应用场景

- **人形机器人灵巧手**：指尖/指腹触觉感知，实现精细抓取、滑移检测与材质识别。
- **电子皮肤**：覆盖机器人手臂、躯干，提供接近觉与接触觉安全保护。
- **汽车与家电**：方向盘、座椅、触控面板的智能力/材质感知。
- **具身智能训练**：结合仿真模型进行触觉策略训练与 sim-to-real 迁移。

## 竞争对比

| 对比项 | 他山 TS-F+ | 帕西尼 PX-6AX | XELA uSkin |
|--------|------------|---------------|------------|
| 传感原理 | 电容式 + AI 芯片 | 6D 霍尔阵列式 | 磁阻式 3 轴 |
| 感知维度 | 7–10 维 | 15 种触觉信息 | 3 轴力 |
| 特色能力 | 材质识别、接近觉、开源仿真 | 高集成灵巧手 | 高密度 3 轴、柔软耐用 |
| 核心优势 | 类脑芯片 + 仿真生态 | 全栈传感器-灵巧手-整机 | 易于集成、数字输出 |

## 选购与部署建议

- 需根据灵巧手或电子皮肤的曲面结构定制传感器贴附方案。
- 仿真模型可与真实传感器数据混训，建议在项目早期即引入触觉仿真以积累数据。

## 参考资料

1. [他山科技官网](https://www.iteschina.com)
2. [SENSOR CHINA 2025 – 他山科技参展报道](https://www.sekorm.com/news/584921525.html)
3. [21 世纪经济报道 – 他山科技 CEO 专访](http://mp.weixin.qq.com/s?__biz=Mzk4ODE4MjkzNA==&mid=2247484687&idx=1&sn=84fba2c156a5ed6bbac57f2f0dc097e7)
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)