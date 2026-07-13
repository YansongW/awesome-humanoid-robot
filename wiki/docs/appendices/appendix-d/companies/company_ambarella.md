# 安霸 / Ambarella

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 安霸 |
| **英文名** | Ambarella |
| **总部** | 美国加利福尼亚州圣克拉拉 |
| **成立时间** | 2004 年 |
| **官网** | [https://www.ambarella.com](https://www.ambarella.com) |
| **供应链环节** | 视觉 AI SoC、ISP、视频编码、ADAS/机器人/安防 |
| **企业属性** | 上市公司（NASDAQ: AMBA） |
| **母公司/所属集团** | 无（独立上市主体） |
| **数据来源** | Ambarella 官网、产品手册、投资者新闻稿、行业研报 |

## 公司简介

Ambarella（安霸）是专注于低功耗、高分辨率视频与边缘 AI 视觉处理的半导体公司。其 CVflow 架构 AI 加速器集成 ISP、视频编解码与多传感器融合能力，广泛应用于安防相机、ADAS、无人机、机器人和工业视觉。CV72、CV7 等新一代 SoC 采用 5/4 nm 工艺，支持 Transformer 与 CNN 混合网络，具备领先的 AI 性能功耗比。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| CV72 / CV72S 系列 | 5 nm 主流边缘 AI 视觉 SoC | CV72S | 专业安防、智能相机、机器人视觉、工业检测 |
| CV7 系列 | 4 nm 旗舰 8K 视觉 AI SoC | CV7 | 高端安防、无人机、自动驾驶感知、8K 相机 |

## 代表产品

### Ambarella CV72

> Ambarella CV72：请访问 [官方资料](https://www.ambarella.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 5 nm（公开报道） | Ambarella 公开资料 |
| CPU | 双核 / 四核 Arm Cortex-A76（依版本最高 1.8 GHz） | Ambarella 公开资料 |
| AI 加速器 | 第三代 CVflow AI 加速器 | Ambarella 公开资料 |
| AI 算力 | 约 12 TOPS（CV72，公开报道） | Ambarella 公开资料 |
| ISP | 集成高性能 ISP，支持低照度 HDR、AI-ISP（AISP） | Ambarella 公开资料 |
| 视频 | 4Kp120 / 8Kp30 编码，多路视频并发 | Ambarella 公开资料 |
| 内存 | 支持 LPDDR4x / LPDDR5 / LPDDR5x | Ambarella 公开资料 |
| 接口 | PCIe、USB 3.2、GbE、MIPI CSI、雷达融合接口 | Ambarella 公开资料 |
| 功耗 | 典型 < 3 W（CV72S，公开报道） | Ambarella 公开资料 |
| 封装 | 未公开 | Ambarella 公开资料 |
| 价格 | 未公开 | Ambarella 公开资料 |

**技术亮点**：CVflow 3.0 支持 Transformer 与 CNN 并发、AI 增强 ISP、雷达-视觉融合、极低功耗、面向多路高清相机。

**应用场景**：**机器人视觉**：多路相机实时目标检测、语义分割与导航辅助；**智能安防相机**：边缘端 4K AI 分析、低照度彩色夜视、人脸/车牌识别；**工业视觉检测**：高速缺陷检测、尺寸测量、OCR 与条码识别

### Ambarella CV7

> Ambarella CV7：请访问 [官方资料](https://www.ambarella.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 4 nm（公开报道） | Ambarella 公开资料 |
| CPU | 四核 Arm Cortex-A73 | Ambarella 公开资料 |
| AI 加速器 | 第三代 CVflow AI 加速器 | Ambarella 公开资料 |
| AI 算力 | 较前代提升 2.5 倍以上 | Ambarella 公开资料 |
| 视频 | 8Kp60 多路视频，4Kp240 编码 | Ambarella 公开资料 |
| 功耗 | 未公开 | Ambarella 公开资料 |
| 价格 | 未公开 | Ambarella 公开资料 |

**技术亮点**：8K 视觉 AI、4 nm 工艺、更高 CPU 性能、面向旗舰级 AI 感知应用。

**应用场景**：8K 运动相机、高端安防、自动驾驶感知、无人机、视频会议。

## 供应链位置

- **上游关键零部件/材料**：三星 5/4 nm 晶圆代工、ARM IP、ISP/视频 IP、LPDDR5x 存储、封测、模组
- **下游客户/应用场景**：安防相机厂商、无人机公司、汽车 Tier1/OEM、机器人整机厂、视频会议设备商
- **主要竞争对手/对标**：Qualcomm QCS、NVIDIA Jetson、地平线征程、海思 HiSilicon、Novatek

## 知识图谱节点与关系

- 公司实体：`ent_company_ambarella`
- 产品实体：`ent_product_ambarella_cv72`、`ent_product_ambarella_cv7`
- 零部件实体：`ent_component_ambarella_cv72_chip`、`ent_component_ambarella_cv7_chip`
- 关键关系：
  - `ent_company_ambarella` -- `manufactures` --> `ent_product_ambarella_cv72`
  - `ent_company_ambarella` -- `manufactures` --> `ent_product_ambarella_cv7`
  - `ent_company_ambarella` -- `manufactures` --> `ent_component_ambarella_cv72_chip`
  - `ent_company_ambarella` -- `manufactures` --> `ent_component_ambarella_cv7_chip`
  - `ent_product_ambarella_cv72` -- `uses` --> `ent_component_ambarella_cv72_chip`
  - `ent_product_ambarella_cv7` -- `uses` --> `ent_component_ambarella_cv7_chip`

## 参考资料

1. [Ambarella 官网](https://www.ambarella.com)
2. [Ambarella CV72 产品页](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/)
3. [Ambarella CV7 新闻稿](https://www.ambarella.com/news/ambarella-launches-powerful-edge-ai-8k-vision-soc-with-industry-leading-ai-and-multi-sensor-perception-performance/)