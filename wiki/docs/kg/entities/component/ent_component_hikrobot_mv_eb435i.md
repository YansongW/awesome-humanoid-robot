---
id: ent_component_hikrobot_mv_eb435i
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 海康机器人 MV-EB435i
  en: Hikrobot MV-EB435i
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_hikrobot_mv_eb435i_datasheet
  type: datasheet
- title: Hikrobot MV-EB435i 技术参数表
  url: https://m.gys.cn/zhinengshexiangji/5377166828.html
- id: src_hikrobot_official
  type: website
- title: 海康机器人 MV-EB435i 感知相机发布
  url: http://www.agv-amr.com/news/show.php?itemid=1489
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自海康机器人 MV-EB435i 经销商技术参数表与官方发布报道；缺失值标注为“未公开”。
---


# 海康机器人 MV-EB435i / Hikrobot MV-EB435i

## 概述

海康机器人 MV-EB435i 是一款低成本、小体积、宽视场角的 RGB-D 智能立体相机，采用主动双目技术，可同步输出深度图与彩色图。该相机面向工业场景设计，主要用于机器人避障、空间扫描、物体识别、测量与定位引导，并已广泛应用于海康机器人 AMR/AGV 产品。

## 工作原理 / 技术架构

MV-EB435i 基于双目立体视觉与主动红外结构光。左右相机对同一场景成像，通过三角测量计算像素视差 $d$，再结合基线 $B$ 与焦距 $f$ 计算深度 $Z$：

$$
Z = \frac{B \cdot f}{d}
$$

深度检测精度在 0.2–3 m 工作距离内约为 1.5%。相机内置硬件级深度图像处理方案，通过 USB 3.0 同步输出左右 IR 图、彩色图与深度图，并配备窄带滤光片以增强抗环境光干扰能力。

## 关键参数表

| 参数 | 典型值 | 备注 |
|------|--------|------|
| 尺寸 | 91 mm × 26 mm × 31 mm | 经销商 datasheet |
| 重量 | 约 170 g | 经销商 datasheet |
| 深度技术 | 主动双目 + 红外结构光 | 官方发布 |
| 视场角 | 84° × 55° | 经销商 datasheet |
| 近视场 | 310 mm × 210 mm @ 0.2 m | 经销商 datasheet |
| 远视场 | 9200 mm × 5200 mm @ 4.8 m | 经销商 datasheet |
| 净距离（CD） | 200 mm | 经销商 datasheet |
| 测量范围（MR） | 4800 mm | 经销商 datasheet |
| 深度图检测精度 | 1.5% @ 0.2 m – 3 m | 经销商 datasheet |
| 空洞率 | < 0.2% | 经销商 datasheet |
| 分辨率 | 1280 × 720 @ 30 fps；640 × 360 @ 30 fps | 经销商 datasheet |
| 数据类型 | 左右 IR 图、彩色图、深度图 | 经销商 datasheet |
| 激光安全等级 | Class 1 | 经销商 datasheet |
| 接口 | USB 3.0（兼容 USB 2.0） | 经销商 datasheet |
| 供电 | 5 VDC（USB 供电） | 经销商 datasheet |
| 典型功耗 | 4.5 W @ 5 VDC | 经销商 datasheet |
| 工作温度 | 0 ℃ ~ +45 ℃ | 经销商 datasheet |
| 防护等级 | 未公开 | - |
| 价格 | 未公开 | - |

## 应用场景

- AMR/AGV 避障与导航
- 空间扫描与三维重建
- 物体识别、测量与定位引导
- 机器人引导与工业上下料
- 体感交互与智能安防

## 供应链关系

制造商为杭州海康机器人股份有限公司（`ent_company_hikrobot`），海康威视控股子公司。上游关键原材料包括 CMOS 图像传感器、ISP 芯片、激光器、光学镜头与主控 SoC；下游客户包括 3C/半导体制造、汽车、锂电、物流仓储、AMR/AGV 与人形机器人感知模组厂商。知识图谱中的关键关系为：`ent_company_hikrobot` -- `manufactures` --> `ent_component_hikrobot_mv_eb435i`。

## 来源与验证

本卡片参数引自海康机器人 MV-EB435i 经销商技术参数表与官方发布报道。防护等级、批量价格、核心 SoC 型号未公开。