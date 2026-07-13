# 思特威 / SmartSens

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 思特威 |
| **英文名** | SmartSens |
| **总部** | 中国上海 |
| **成立时间** | 2011 |
| **官网** | [https://www.smartsenstech.com](https://www.smartsenstech.com) |
| **供应链环节** | CMOS 图像传感器（安防、机器视觉、车载、手机） |
| **企业属性** | 科创板上市公司（688213）、国内 CIS 设计领军企业 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 思特威官网、产品发布新闻、公开 datasheet |

## 公司简介

思特威（SmartSens）是技术先进的 CMOS 图像传感器供应商，拥有 SmartGS™ 全局快门、SFCPixel®、PixGain HDR® 等自研技术。公司产品覆盖安防监控、机器视觉、智能车载电子与智能手机四大领域，并已向机器人视觉、工业检测等场景拓展。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 智能手机 CIS | 高像素旗舰主摄 | SC580XS / SC550XS | 旗舰手机 |
| 机器视觉 CIS | 全局快门 | SC130GS / SC235HGS 等 | 工业相机、机器人 |
| 安防监控 CIS | 星光级低照度 | SC850SL / SC880SL | 安防、车载 |
| 车载电子 CIS | 车规级图像传感器 | SC120AT / SC220AT 等 | ADAS、DMS |

## 代表产品

### 思特威 SC580XS CMOS 图像传感器

> 思特威 SC580XS CMOS 图像传感器：请访问 [官方资料](https://www.smartsenstech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 50MP CMOS 图像传感器 | 思特威官网 |
| 有效像素 | 50 MP | 思特威官网 |
| 像素尺寸 | 1.22 µm | 思特威官网 |
| 光学尺寸 | 1/1.28" | 思特威官网 |
| 工艺 | 22 nm HKMG Stack | 思特威官网 |
| HDR | PixGain HDR® / 三重曝光 HDR | 思特威官网 |
| 动态范围 | 最高 120 dB | 思特威官网 |
| 读取噪声 | 低至 0.7 e⁻ | 思特威官网 |
| 对焦 | AllPix ADAF® / Sparse PDAF | 思特威官网 |
| 视频 | 4K 120 fps（四合一模式） | 思特威官网 |
| 接口 | MIPI C-PHY / D-PHY | 思特威官网 |
| 功耗 | 50MP@25fps 约 500 mW | 思特威官网 |
| 工作温度 | -20℃ – +70℃ | 思特威官网 |
| 价格 | 未公开 | - |

**技术亮点**：22 nm HKMG Stack、SFCPixel®-2、PixGain HDR®、AllPix ADAF® 全像素对焦，旗舰级影像性能。

**应用场景**：旗舰智能手机主摄、超广角、机器人视觉、工业检测、无人机航拍。

### 思特威 SmartGS™ 全局快门机器视觉传感器

> 思特威 SmartGS™ 全局快门机器视觉传感器：请访问 [官方资料](https://www.smartsenstech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 全局快门 CMOS | 思特威官网 |
| 分辨率 | 1.3MP – 9MP 多型号 | 思特威官网 |
| 特色 | 高帧率、低噪声 | 思特威官网 |
| 价格 | 未公开 | - |

**技术亮点**：SmartGS™ 技术，适合高速运动目标捕捉与机器视觉检测。

**应用场景**：工业机器人检测、物流读码、机器人导航。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、封测、光学镜头、滤光片、ISP 算法
- **下游客户/应用场景**：智能手机 OEM、安防厂商、车载 Tier1、机器人、工业相机
- **主要竞争对手/对标**：Sony、Samsung ISOCELL、OmniVision、GalaxyCore

## 知识图谱节点与关系

- 公司实体：`ent_company_smartsens`
- 产品实体：`ent_product_smartsens_sc580xs`
- 零部件实体：`ent_component_smartsens_sc580xs_sensor`
- 关键关系：
  - `ent_company_smartsens` -- `manufactures` --> `ent_product_smartsens_sc580xs`
  - `ent_company_smartsens` -- `manufactures` --> `ent_component_smartsens_sc580xs_sensor`
  - `ent_product_smartsens_sc580xs` -- `uses` --> `ent_component_smartsens_sc580xs_sensor`

## 参考资料

1. [思特威官网](https://www.smartsenstech.com)
2. [思特威 SC580XS CMOS 图像传感器产品/资料页](https://www.smartsenstech.com/en/m)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)