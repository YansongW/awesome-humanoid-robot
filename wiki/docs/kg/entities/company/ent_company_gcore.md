---
id: ent_company_gcore
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 格科微
  en: GalaxyCore
status: active
sources:
- id: src_gcore_official
  type: website
  url: https://www.gcoreinc.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 格科微 / GalaxyCore

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 格科微 |
| **英文名** | GalaxyCore |
| **总部** | 中国上海 |
| **成立时间** | 2003 |
| **官网** | [https://www.gcoreinc.com](https://www.gcoreinc.com) |
| **供应链环节** | CMOS 图像传感器、显示驱动芯片 |
| **企业属性** | 科创板上市公司（688728）、Fab-Lite 模式 CIS 设计龙头 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 格科微官网、招股书、产品新闻稿 |

## 公司简介

格科微（GalaxyCore）是中国领先的 CMOS 图像传感器与显示驱动芯片设计公司，采用设计+制造+封测一体化的 Fab-Lite 模式。公司产品覆盖从 QVGA 到 50MP 全系列 CIS，广泛应用于手机、可穿戴、汽车电子、智能家居与工业视觉等领域。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 手机 CMOS 传感器 | 高像素/低成本 | GC32E2 / GC50 系列 | 智能手机 |
| 非手机 CMOS 传感器 | 安防/车载/工业 | GC2083 / GC4653 等 | 安防、车载、IoT |
| 显示驱动芯片 | TDDI/AMOLED | FHD TDDI / AMOLED DDIC | 手机、可穿戴 |
| 特色工艺 | 单芯片高像素 | 非堆栈 32MP/50MP | 中端旗舰手机 |

## 代表产品

### 格科微 GC32E2 CMOS 图像传感器

> 格科微 GC32E2 CMOS 图像传感器：请访问 [官方资料](https://www.gcoreinc.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 32MP CMOS 图像传感器 | 格科微官网 |
| 有效像素 | 32 MP | 格科微官网 |
| 像素尺寸 | 0.7 µm | 格科微官网 |
| 光学尺寸 | 1/3.1" | 格科微官网 |
| 工艺 | 背照式（BSI） | 格科微官网 |
| 快门 | 卷帘快门 | 格科微官网 |
| HDR | 单帧 DAG HDR | 格科微官网 |
| 对焦 | PDAF 相位检测对焦 | 格科微官网 |
| 输出格式 | RAW 10 / 12 | 格科微官网 |
| 接口 | MIPI D-PHY | 格科微官网 |
| 封装 | COB / COM | 格科微官网 |
| 帧率 | 最高 15 fps（全分辨率） | 格科微官网 |
| 工作温度 | -20℃ – +70℃ | 格科微官网 |
| 价格 | 未公开 | - |

**技术亮点**：第二代单芯片 32MP、0.7 µm 像素、DAG HDR、PDAF、AON 低功耗，兼顾高像素与成本优势。

**应用场景**：智能手机前摄、平板电脑、机器人视觉、可穿戴设备、视频通话。

### 格科微 GC50 系列 50MP CMOS 图像传感器

> 格科微 GC50 系列 50MP CMOS 图像传感器：请访问 [官方资料](https://www.gcoreinc.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 50MP CMOS 图像传感器 | 格科微官网 |
| 特色 | 非堆栈 0.61 µm 像素 | 格科微官网 |
| 应用 | 智能手机主摄 | 格科微官网 |
| 价格 | 未公开 | - |

**技术亮点**：全球首款非堆栈 0.61 µm 50MP 传感器，推动高像素下沉。

**应用场景**：中端旗舰手机主摄、超广角。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、封装测试、彩色滤光片、微透镜、载板
- **下游客户/应用场景**：智能手机 OEM、ODM、平板、机器人、IoT 摄像头厂商
- **主要竞争对手/对标**：Sony、Samsung ISOCELL、OmniVision、SmartSens

## 知识图谱节点与关系

- 公司实体：`ent_company_gcore`
- 产品实体：`ent_product_gcore_gc32e2`
- 零部件实体：`ent_component_gcore_gc32e2_sensor`
- 关键关系：
  - `ent_company_gcore` -- `manufactures` --> `ent_product_gcore_gc32e2`
  - `ent_company_gcore` -- `manufactures` --> `ent_component_gcore_gc32e2_sensor`
  - `ent_product_gcore_gc32e2` -- `uses` --> `ent_component_gcore_gc32e2_sensor`

## 参考资料

1. [格科微官网](https://www.gcoreinc.com)
2. [格科微 GC32E2 CMOS 图像传感器产品/资料页](https://en.gcoreinc.com/news/detail-67)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)