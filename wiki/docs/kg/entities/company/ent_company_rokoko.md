---
id: ent_company_rokoko
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Rokoko
  en: Rokoko
status: active
sources:
- id: src_rokoko_official
  type: website
  url: https://rokoko.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---





# Rokoko / Rokoko

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Rokoko |
| **英文名** | Rokoko |
| **总部** | 丹麦哥本哈根 |
| **成立时间** | 2014 年 |
| **官网** | [https://rokoko.com](https://rokoko.com) |
| **供应链环节** | 惯性动作捕捉、动画数据、人机交互数据采集 |
| **企业属性** | 初创公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | Rokoko 官网、CGW 新闻、Animation Xpress |

## 公司简介

Rokoko 是一家面向独立创作者、游戏、影视、体育科学与机器人领域的惯性动作捕捉（mocap）公司，以高性价比、易用性和实时流媒体能力著称。

核心产品 Smartsuit Pro II 是一套全身惯性动作捕捉套装，内置 17–19 颗 9-DOF IMU 传感器，通过 Wi-Fi 与免费 Rokoko Studio 软件连接，可实时录制、清理、编辑并将动画流式传输到 Unreal Engine、Unity、Blender、Maya、MotionBuilder 等主流 3D 工具。Rokoko 还提供 Smartgloves 手部追踪、Face Capture 面部捕捉以及 Video to Animation 等 AI 驱动的动画工具。

Rokoko 的动作数据也越来越多地用于机器人领域，为人形机器人、数字人和具身智能模型提供自然动作参考与训练数据。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 全身动作捕捉 | 惯性动捕套装 | Smartsuit Pro II | 动画、游戏、VFX |
| 手部动作捕捉 | 手指追踪手套 | Smartgloves | 手部动画、机器人灵巧手 |
| 软件平台 | 录制、编辑、流媒体 | Rokoko Studio | 动捕后期、实时驱动 |
| AI 动画工具 | 视频/单摄像头驱动动画 | Rokoko Video / Motion Library | 快速动画生成 |

## 代表产品

### Rokoko Smartsuit Pro II

> Rokoko Smartsuit Pro II：请访问 [官方资料](https://rokoko.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感器数量 | 17× 或 19× 9-DOF IMU | Rokoko 官网 |
| 3D 方向精度 | ±1° | Rokoko 公开规格 |
| 采样/流传输 | 200 fps | Rokoko 公开规格 |
| 加速度计量程 | 16 g | Rokoko 公开规格 |
| 无线连接 | Wi-Fi（最大约 100 m） | Rokoko 公开规格 |
| 续航 | 约 6 小时 | Rokoko 公开规格 |
| 套装尺寸 | S / M / L / XL | Rokoko 官网 |
| 价格 | 约 2,745 USD 起 | 公开报价 |

**技术亮点**：Sensor Fusion 2.0 低漂移算法、多层追踪（楼梯/梯子）、高冲击运动优化、可水洗面料、与 Smartgloves 原生集成、一键实时流媒体。

**应用场景**：影视动画、游戏角色、虚拟直播/VTubing、体育生物力学分析、机器人/人形机器人动作参考数据采集。

### Rokoko Smartgloves

> Rokoko Smartgloves：请访问 [官方资料](https://rokoko.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感器数量 | 7× 6-DOF 手部追踪器 | Rokoko 公开规格 |
| 采样率 | 100 Hz | Rokoko 公开规格 |
| 延迟 | 约 20 ms | Rokoko 公开规格 |
| 无线连接 | 2.4 / 5 GHz Wi-Fi | Rokoko 公开规格 |
| 磁力计 | 无（抗磁干扰） | Rokoko 公开规格 |
| 3D 方向精度 | ±1° | Rokoko 公开规格 |
| 价格 | 约 995 USD | 公开报价 |

**技术亮点**：无磁计设计抗干扰、亚毫米级指尖追踪、与 Smartsuit Pro II 共享电池与 Wi-Fi 链路、原生集成 Rokoko Studio。

**应用场景**：手部动画、虚拟角色直播、机器人灵巧手操作数据采集、人机交互研究。

## 供应链位置

- **上游关键零部件/材料**：MEMS IMU 传感器、Wi-Fi 模块、可穿戴纺织品、锂电池、传感器融合算法芯片。
- **下游客户/应用场景**：独立动画师、游戏工作室（Ubisoft、EA 等）、影视 VFX、体育科研机构、机器人/人形机器人公司。
- **主要竞争对手/对标**：Xsens / Movella、Noitom Perception Neuron、StretchSense、Manus、Vicon（光学动捕）。

## 知识图谱节点与关系

- 公司实体：`ent_company_rokoko`
- 产品/平台实体：`ent_product_rokoko_smartsuit_pro_ii`、`ent_product_rokoko_smartgloves`
- 关键关系：
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartsuit_pro_ii`（`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartsuit_pro_ii`）
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartgloves`（`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartgloves`）

## 参考资料

1. [Rokoko 官网](https://rokoko.com)
2. [CGW – Rokoko Smartsuit Pro II 发布](https://www.cgw.com/Press-Center/News/2021/Rokoko-Launches-the-Next-Gen-Smartsuit-Pro-II.aspx)
3. [Animation Xpress – Rokoko Smartsuit Pro II](https://www.animationxpress.com/latest-news/motion-capture-company-rokoko-launches-smartsuit-pro-ii/)
4. [Rokoko Studio 下载页](https://rokoko.com/studio)