# 索尼半导体解决方案（Sony Semiconductor Solutions） / Sony Semiconductor Solutions

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 索尼半导体解决方案（Sony Semiconductor Solutions） |
| **英文名** | Sony Semiconductor Solutions |
| **总部** | 日本神奈川县厚木市 |
| **成立时间** | 2016 |
| **官网** | [https://www.sony-semicon.co.jp](https://www.sony-semicon.co.jp) |
| **供应链环节** | CMOS 图像传感器、3D 传感、堆栈式视觉传感器、激光雷达 SPAD |
| **企业属性** | 索尼集团全资子公司、全球图像传感器龙头 |
| **母公司/所属集团** | Sony Group Corporation |
| **数据来源** | Sony Semiconductor 官网、产品 datasheet、索尼年报 |

## 公司简介

索尼半导体解决方案是全球最大的 CMOS 图像传感器供应商，产品覆盖移动、汽车、工业与机器人视觉。

索尼半导体解决方案继承索尼在图像传感器领域的技术积累，提供从移动 CIS、车载 CIS、工业视觉到 3D 深度传感的全栈方案。其堆栈式 CMOS、背照式技术、全局快门与 SPAD dToF 传感器在机器人视觉、SLAM、避障与目标识别中扮演核心角色。IMX500 系列智能视觉传感器更是首次在传感器端集成 AI 推理能力，为低延迟边缘视觉提供新范式。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 工业/机器人图像传感器 | 高速全局快门/高动态 | IMX500 / IMX397 / IMX426 | 机器人视觉、工业检测 |
| 车载图像传感器 | ADAS/舱内监控 | IMX490 / IMX623 / OX08D4Q | 自动驾驶、机器人导航 |
| 3D/深度传感 | iToF/dToF/SPAD | IMX611 / IMX590 / IMX459 | AR/VR、机器人避障 |
| 智能视觉传感器 | 端侧 AI 推理 | IMX500 / IMX501 | 边缘 AI、具身智能 |

## 代表产品

### Sony IMX500 智能视觉传感器

> Sony IMX500 智能视觉传感器：请访问 [官方资料](https://www.sony-semicon.co.jp) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 堆栈式 CMOS 图像传感器 + AI 推理 | 官网/datasheet |
| 有效像素 | 约 1230 万（4056 × 3040） | 官网/datasheet |
| 光学尺寸 | 1/2.3 型 | 官网/datasheet |
| 像素尺寸 | 未公开 | - |
| 快门 | 卷帘快门 | 官网/datasheet |
| 最大帧率 | 未公开 | - |
| AI 能力 | 传感器端 AI 模型推理 | 官网/datasheet |
| 输出格式 | 元数据 / 图像 + 元数据 | 官网/datasheet |
| 接口 | MIPI D-PHY / SLVS-EC | 官网/datasheet |
| 供电 | 未公开 | - |
| 功耗 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 封装 | COB / CSP | 官网/datasheet |
| 价格 | 未公开 | - |

**技术亮点**：全球首款传感器内 AI 推理图像传感器，堆栈式集成 AI 处理单元，仅输出元数据即可实现低功耗、低带宽、高隐私的视觉识别。

**应用场景**：机器人视觉感知、智能监控、零售分析、工业质检、具身智能边缘设备、ADAS。

### Sony IMX611 SPAD dToF 深度传感器

> Sony IMX611 SPAD dToF 深度传感器：请访问 [官方资料](https://www.sony-semicon.co.jp) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | SPAD dToF 深度传感器 | 官网 |
| 分辨率 | 未公开 | - |
| 测距范围 | 未公开 | - |
| 应用 | AR/VR、机器人避障、3D 扫描 | 官网 |
| 价格 | 未公开 | - |

**技术亮点**：基于单光子雪崩二极管（SPAD）的 dToF 深度传感，适合中远距离 3D 感知。

**应用场景**：机器人导航避障、AR/VR 空间映射、手势识别、三维测量。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工（TSMC/索尼自有产线）、封装测试、光学滤光片、微透镜、载板与驱动 IC
- **下游客户/应用场景**：智能手机 OEM、汽车 Tier 1、机器人整机厂、安防与工业视觉厂商、AR/VR 设备商
- **主要竞争对手/对标**：Samsung Electro-Mechanics、OmniVision、格科微、思特威、ams OSRAM、STMicroelectronics

## 知识图谱节点与关系

- 公司实体：`ent_company_sony_semiconductor`
- 产品实体：`ent_product_sony_semiconductor_imx500`
- 零部件实体：`ent_component_sony_semiconductor_imx500_sensor`
- 关键关系：
  - `ent_company_sony_semiconductor` -- `manufactures` --> `ent_product_sony_semiconductor_imx500`
  - `ent_company_sony_semiconductor` -- `manufactures` --> `ent_component_sony_semiconductor_imx500_sensor`
  - `ent_product_sony_semiconductor_imx500` -- `uses` --> `ent_component_sony_semiconductor_imx500_sensor`

## 参考资料

1. [Sony Semiconductor Solutions 官网](https://www.sony-semicon.co.jp)
2. [Sony IMX500 智能视觉传感器 产品/资料页](https://www.sony-semicon.co.jp/products/common/IMX500.html)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)