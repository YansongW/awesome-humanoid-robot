# 奇景光电（Himax Technologies） / Himax Technologies

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 奇景光电（Himax Technologies） |
| **英文名** | Himax Technologies |
| **总部** | 中国台湾台南（美国硅谷设办公室） |
| **成立时间** | 2001 |
| **官网** | [https://www.himax.com.tw](https://www.himax.com.tw) |
| **供应链环节** | 3D 传感模组、晶圆级光学（WLO）、CMOS 图像传感器、驱动 IC |
| **企业属性** | 纳斯达克上市公司（NASDAQ: HIMX）、台湾驱动 IC/光学模组厂商 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | Himax 官网、年报、产品新闻稿 |

## 公司简介

奇景光电是全球领先的显示驱动 IC、晶圆级光学（WLO）与 3D 传感解决方案供应商。

奇景光电（Himax Technologies）专注于显示驱动 IC、晶圆级光学（WLO）、3D 传感与低功耗 AI 视觉方案。其 WLO 技术可在晶圆级制造微型光学元件，为结构光、ToF 与 DOE 提供小型化、低成本的投射与接收模组。Himax 的 3D 传感整体解决方案（Structured Light Sensing Module）已广泛应用于智能手机人脸解锁、支付级 3D 识别与机器人视觉避障。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 3D 传感模组 | 结构光/主动双目 | SLiM / 3D Sensing Module | 手机、机器人、AR/VR |
| 晶圆级光学 WLO | DOE/准直镜头 | WLO 光学元件 | 3D 传感、光通信 |
| CMOS 图像传感器 | 低功耗/全局快门 | WiseEye / 定制 CIS | AIoT、机器人 |
| 显示驱动 IC | TDDI / OLED | LCD/OLED 驱动 | 手机、车载 |

## 代表产品

### Himax SLiM 3D 传感模组

> Himax SLiM 3D 传感模组：请访问 [官方资料](https://www.himax.com.tw) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 结构光 3D 传感模组 | 官网/新闻稿 |
| 深度技术 | 结构光 / 主动红外投射 | 官网/新闻稿 |
| 深度分辨率 | VGA 级（640 × 480）@ 30 fps | 官网/新闻稿 |
| 视场角 | 水平约 67°（典型） | 官网/新闻稿 |
| 工作距离 | 约 0.3 m – 1.0 m | 官网/新闻稿 |
| 深度精度 | 未公开 | - |
| 尺寸 | 小型化模组（具体未公开） | 官网/新闻稿 |
| 功耗 | 未公开 | - |
| 接口 | MIPI / USB2.0（因方案而异） | 官网/新闻稿 |
| 发射器 | VCSEL / EEL + WLO DOE | 官网/新闻稿 |
| 接收器 | NIR 增强 CMOS / ToF | 官网/新闻稿 |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：晶圆级光学（WLO）实现微型化结构光投射，集成发射与接收单元，支持支付级 3D 识别与机器人近距离感知。

**应用场景**：智能手机人脸解锁/支付、机器人避障与抓取、AR/VR 手势交互、智能门锁、3D 扫描。

### Himax WiseEye 超低功耗 AI 视觉方案

> Himax WiseEye 超低功耗 AI 视觉方案：请访问 [官方资料](https://www.himax.com.tw) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 超低功耗 AI 视觉传感方案 | 官网 |
| 传感器 | 自研超低功耗 CIS + AI 加速器 | 官网 |
| 功耗 | 毫瓦级 | 官网 |
| 应用 | 智能家电、机器人、AIoT | 官网 |
| 价格 | 未公开 | - |

**技术亮点**：在传感器端完成 AI 推理，支持人体/物体检测，适合电池供电设备。

**应用场景**：智能门锁、安防摄像头、机器人唤醒、可穿戴设备。

## 供应链位置

- **上游关键零部件/材料**：硅晶圆、光学玻璃/聚合物、VCSEL/EEL 激光芯片、封装载板、驱动 IC、晶圆级光学材料
- **下游客户/应用场景**：智能手机 OEM、机器人整机厂、AR/VR 设备商、安防与 AIoT 厂商、汽车 Tier 1
- **主要竞争对手/对标**：ams OSRAM、Sony Semiconductor、Samsung Electro-Mechanics、奥比中光、舜宇光学、丘钛科技

## 知识图谱节点与关系

- 公司实体：`ent_company_himax`
- 产品实体：`ent_product_himax_slim_3d`
- 零部件实体：`ent_component_himax_slim_3d_module`
- 关键关系：
  - `ent_company_himax` -- `manufactures` --> `ent_product_himax_slim_3d`
  - `ent_company_himax` -- `manufactures` --> `ent_component_himax_slim_3d_module`
  - `ent_product_himax_slim_3d` -- `uses` --> `ent_component_himax_slim_3d_module`

## 参考资料

1. [Himax Technologies 官网](https://www.himax.com.tw)
2. [Himax SLiM 3D 传感模组 产品/资料页](https://www.himax.com.tw/products/structured-light-sensing/)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)