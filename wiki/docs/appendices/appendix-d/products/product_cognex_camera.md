# 康耐视 In-Sight 3800 视觉系统 / Cognex In-Sight 3800 Vision System

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [康耐视 / Cognex](../companies/company_cognex.md) |
| **产品类别** | AI + 规则型工业视觉系统 |
| **发布时间** | 2024 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [康耐视官网](https://www.cognex.com) |

## 产品概述

康耐视 In-Sight 3800 是一款面向高速制造场景的高性能工业视觉系统，集成了 AI 边缘学习（ViDi EL）与规则型视觉工具，可在同一平台上完成缺陷检测、OCR、装配验证与零件分类等任务。

该系统提供 1.4 MP 至 16 MP 六种分辨率型号，采用全局快门 CMOS 传感器，最大单色帧率可达 125 fps，并配备多色 RGBW+IR 照明、HDR+ 高动态范围以及可选的 HSLL 高速液态镜头。In-Sight 3800 防护等级达 IP67，支持多种工业以太网协议，是汽车、电子、食品、医疗与机器人视觉导引等场景的高端选择。

## 产品图片

> Cognex In-Sight 3800：请访问 [官方资料](https://www.cognex.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | AI + 规则型工业视觉系统 | 官方 datasheet |
| 分辨率 | 1.4 / 3 / 5 / 8 / 12 / 16 MP（6 种型号） | 官方 datasheet |
| 传感器 | 1/2.3" – 1.1" CMOS，全局快门 | 官方 datasheet |
| 最大帧率（单色/彩色） | 125 fps / 52 fps（IS3801） | 官方 datasheet |
| 像素尺寸 | 3.45 μm / 2.74 μm | 官方 datasheet |
| 镜头接口 | C 接口 | 官方 datasheet |
| 内存 | 4 GB | 官方 datasheet |
| 图像处理内存 | 512 MB / 1 GB | 官方 datasheet |
| 照明 | 多色 RGBW + IR，可选高级照明 | 官方 datasheet |
| 动态范围 | HDR+ | 官方 datasheet |
| 防护等级 | IP67 | 官方 datasheet |
| 通信协议 | TCP/IP、PROFINET、EtherNet/IP、Modbus TCP、SLMP | 官方 datasheet |
| 供电 | 24 V DC ± 10%，最大 2.0 A | 官方 datasheet |
| 工作温度 | 0℃ – 40℃ | 官方 datasheet |
| 重量 | 约 570 g（裸机） | 官方 datasheet |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[康耐视 / Cognex](../companies/company_cognex.md)
- **核心零部件/技术来源**：自研 ViDi EL 边缘学习算法与 In-Sight Vision Suite 软件；CMOS 传感器、光学镜头、照明模块、FPGA/SoC 外购。
- **下游应用/客户**：汽车、消费电子、半导体、食品医药、物流仓储、机器人 OEM。

## 知识图谱节点与关系

- 零部件实体：`ent_component_cognex_insight_3800`
- 制造商实体：`ent_company_cognex`
- 关键关系：
  - `rel_ent_company_cognex_manufactures_ent_component_cognex_insight_3800`（`ent_company_cognex` → `manufactures` --> `ent_component_cognex_insight_3800`）

## 应用场景

- **缺陷检测**：电子元器件、汽车零部件、食品包装表面瑕疵检测。
- **OCR 与追溯**：激光蚀刻、喷码、标签字符识别与序列号管理。
- **装配验证**：零部件有无、位置、方向与完整性检查。
- **机器人视觉导引**：人形机器人/工业机器人抓取定位与路径规划。

## 竞争对比

| 对比项 | 康耐视 In-Sight 3800 | 基恩士 CV-X | 海康机器人 MV-CS |
|--------|----------------------|-------------|------------------|
| 类型 | AI + 规则型视觉系统 | 智能相机/视觉系统 | 工业相机/视觉系统 |
| 分辨率 | 1.4 – 16 MP | 多型号 | 多型号 |
| AI 能力 | ViDi EL 边缘学习 | 内置 AI 图像处理 | AI 视觉算法 |
| 防护等级 | IP67 | 因型号而异 | 因型号而异 |
| 核心优势 | 国际品牌、生态成熟 | 直销服务、FA 整合 | 成本优势、本土化 |

## 选购与部署建议

- 根据检测视野、精度与产线速度选择分辨率与帧率型号，并确认镜头与照明配置。
- 复杂场景建议先使用 EasyBuilder 快速验证，再用电子表格进行高度定制开发。

## 参考资料

1. [康耐视官网](https://www.cognex.com)
2. [康耐视 In-Sight 3800 产品页](https://www.cognex.com/zh-cn/products/2d-machine-vision-systems/in-sight-3800)
3. [康耐视 In-Sight 3800 datasheet](https://www.cognex.cn/zh-cn/tools-and-resources/resource-center/in-sight-3800-datasheet)
4. [附录 D 企业目录](../index-companies.md)