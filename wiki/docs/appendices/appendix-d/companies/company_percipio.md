# 图漾科技 / Percipio.XYZ

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 图漾科技 |
| **英文名** | Percipio.XYZ |
| **总部** | 中国上海 |
| **成立时间** | 2015 |
| **官网** | [https://www.percipio.xyz](https://www.percipio.xyz) |
| **供应链环节** | 3D 工业相机、机器视觉、深度感知 |
| **企业属性** | 私有公司、独立 3D 机器视觉供应商 |
| **母公司/所属集团** | 独立 |
| **数据来源** | 官网、公开报道、经销商 datasheet |

## 公司简介

图漾科技是全球领先的 3D 工业相机供应商，以高性价比的主动双目/结构光相机切入工业自动化与物流市场。

图漾科技专注于 3D 机器视觉硬件与配套软件方案，产品覆盖 FM、FS、PM、PS 等工业 3D 相机系列。公司采用独立视觉产品供应商模式，为设备商和系统集成商提供高性价比的深度相机，广泛应用于工业分拣、抓取、测量、检测等场景。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| FM 系列 | 工业 3D 相机 | FM811 / FM851 / FM855 | 工业分拣、抓取、测量 |
| FS 系列 | 短距高精度相机 | FS820 | 眼在手上、协作机器人 |
| PM/PS 系列 | ToF / 结构光 | PM801 / PS800 | 物流、人形计数、安防 |

## 代表产品

### 图漾科技 FM851-E2

> 图漾科技 FM851-E2：请访问 [官方资料](https://www.percipio.xyz) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 125 mm × 85 mm × 30 mm | 经销商 datasheet |
| 重量 | 500 g | 经销商 datasheet |
| 深度技术 | 主动双目结构光 | 官方 datasheet |
| 工作距离 | 0.2 m – 1.0 m | 经销商 datasheet |
| FOV（H/V） | 63° / 48° | 经销商 datasheet |
| 深度分辨率 | 1280 × 960 | 经销商 datasheet |
| RGB 分辨率 | 2560 × 1920 | 经销商 datasheet |
| Z 向精度 | ±0.1 mm @ 200 mm | 经销商 datasheet |
| 接口 | Gigabit Ethernet / M8 触发 | 经销商 datasheet |
| 防护等级 | IP65 | 经销商 datasheet |
| 价格 | 约 USD 2,199 | Seeed Studio |

**技术亮点**：百万级深度分辨率、千兆网接口、IP65 防护、硬触发与多机融合，适合工业级精密作业。

**应用场景**：机器人无序抓取、上下料、工业测量、3D 检测、Bin Picking。

### 图漾科技 FS820

> 图漾科技 FS820：请访问 [官方资料](https://www.percipio.xyz) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 工作距离 | 0.3 m – 1.3 m | Seeed Studio |
| 深度技术 | 主动双目结构光 | 官方 datasheet |
| 帧率 | 5 fps | Seeed Studio |
| RGB 分辨率 | 2 MP | Seeed Studio |
| 接口 | Gigabit Ethernet | 官方 datasheet |
| 特点 | 体积小巧，适合眼在手上安装 | 官方 datasheet |
| 价格 | 约 USD 749 | Seeed Studio |

**技术亮点**：短距高精度、小体积、低功耗，专为协作机器人眼在手上场景优化。

**应用场景**：协作机器人抓取、精密装配、医疗机器人、柔性生产线。

## 供应链位置

- **上游关键零部件/材料**：CMOS 传感器、激光器/投影仪、工业以太网芯片、光学镜头、结构光算法
- **下游客户/应用场景**：工业机器人、协作机器人、物流自动化、3C/半导体检测、医疗设备
- **主要竞争对手/对标**：奥比中光、海康机器人、Intel RealSense、康耐视、基恩士

## 知识图谱节点与关系

- 公司实体：`ent_company_percipio`
- 产品实体：`ent_component_percipio_fm851_e2`
- 产品实体：`ent_component_percipio_fs820`
- 关键关系：
  - `ent_company_percipio` -- `manufactures` --> `ent_component_percipio_fm851_e2`
  - `ent_company_percipio` -- `manufactures` --> `ent_component_percipio_fs820`

## 参考资料

1. [官网](https://www.percipio.xyz)
2. [产品资料与公开报道](https://www.percipio.xyz)
3. [附录 D 产品目录](../index-products.md)