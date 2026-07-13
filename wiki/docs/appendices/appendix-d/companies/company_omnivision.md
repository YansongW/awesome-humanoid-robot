# 豪威科技（OmniVision） / OmniVision

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 豪威科技（OmniVision） |
| **英文名** | OmniVision |
| **总部** | 美国加利福尼亚州圣克拉拉 |
| **成立时间** | 1995 |
| **官网** | [https://www.ovt.com](https://www.ovt.com) |
| **供应链环节** | CMOS 图像传感器、汽车/机器人视觉、显示驱动 |
| **企业属性** | 韦尔股份（Will Semiconductor）子公司、全球 CIS 设计龙头 |
| **母公司/所属集团** | Will Semiconductor（韦尔股份，603501） |
| **数据来源** | OmniVision 官网、韦尔股份年报、产品 datasheet |

## 公司简介

OmniVision 是全球领先的 CMOS 图像传感器设计公司，产品覆盖移动、汽车、安防、工业与机器人视觉。

豪威科技（OmniVision）成立于 1995 年，2019 年被中国韦尔股份收购，现为韦尔股份全资子公司。OmniVision 提供从 VGA 到数千万像素的 CMOS 图像传感器，覆盖移动设备、汽车 ADAS、安防监控、工业视觉与机器人导航。其 OX 系列车载图像传感器、OG 系列全局快门工业传感器与 OV 系列移动传感器被广泛应用于人形机器人头部视觉、SLAM 导航与物体识别。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 汽车图像传感器 | ADAS/环视/舱内 | OX08D10 / OX03C10 / OX05B1S | 自动驾驶、机器人导航 |
| 移动/机器人视觉 | 高像素/低功耗 | OV50H / OV64B / OV32C | 手机、机器人 |
| 机器视觉/全局快门 | 工业检测与高速 | OG0VA / OG01A / OG02B | 工业、无人机 |
| 显示驱动/触控 | 面板驱动 | TD4377 等 | 手机、车载 |

## 代表产品

### OmniVision OX08D10 汽车/机器人 8MP 图像传感器

> OmniVision OX08D10 汽车/机器人 8MP 图像传感器：请访问 [官方资料](https://www.ovt.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 车规级 8MP CMOS 图像传感器 | 官网/datasheet |
| 有效像素 | 8 MP | 官网/datasheet |
| 光学尺寸 | 1/1.7" | 官网/datasheet |
| 像素尺寸 | 2.1 µm | 官网/datasheet |
| 快门 | 卷帘快门（含 HDR） | 官网/datasheet |
| 最大帧率 | 最高 60 fps | 官网/datasheet |
| 动态范围 | 120 dB HDR | 官网/datasheet |
| LED 闪烁抑制 | 支持 LFM | 官网/datasheet |
| 功能安全 | ASIL-B | 官网/datasheet |
| 接口 | MIPI D-PHY / C-PHY | 官网/datasheet |
| 输出格式 | RAW / YUV | 官网/datasheet |
| 工作温度 | -40℃ – +105℃（车规级） | 官网/datasheet |
| 封装 | COB / CSP | 官网/datasheet |
| 价格 | 未公开 | - |

**技术亮点**：高分辨率、大像素、120 dB HDR 与 LED 闪烁抑制，具备 ASIL-B 功能安全等级，适合高可靠机器人与汽车视觉。

**应用场景**：人形机器人头部主摄、无人车/AMR 导航、ADAS 前视、工业检测相机、安防监控。

### OmniVision OG0VA 全局快门图像传感器

> OmniVision OG0VA 全局快门图像传感器：请访问 [官方资料](https://www.ovt.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 全局快门 CMOS 图像传感器 | 官网 |
| 有效像素 | 未公开 | - |
| 快门 | 全局快门 | 官网 |
| 应用 | 工业视觉、机器人视觉、AR/VR | 官网 |
| 价格 | 未公开 | - |

**技术亮点**：全局快门设计减少高速运动伪影，适合工业检测与机器人视觉。

**应用场景**：机器视觉相机、无人机避障、AR/VR 追踪、高速运动分析。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工（TSMC 等）、封装测试、光学滤光片、微透镜、载板、ISP 算法授权
- **下游客户/应用场景**：智能手机 OEM、汽车 Tier 1、机器人整机厂、工业相机厂商、安防监控品牌、医疗设备商
- **主要竞争对手/对标**：Sony Semiconductor、Samsung Electro-Mechanics、格科微、思特威、韦尔股份其他品牌、ams OSRAM

## 知识图谱节点与关系

- 公司实体：`ent_company_omnivision`
- 产品实体：`ent_product_omnivision_ox08d10`
- 零部件实体：`ent_component_omnivision_ox08d10_sensor`
- 关键关系：
  - `ent_company_omnivision` -- `manufactures` --> `ent_product_omnivision_ox08d10`
  - `ent_company_omnivision` -- `manufactures` --> `ent_component_omnivision_ox08d10_sensor`
  - `ent_product_omnivision_ox08d10` -- `uses` --> `ent_component_omnivision_ox08d10_sensor`

## 参考资料

1. [OmniVision 官网](https://www.ovt.com)
2. [OmniVision OX08D10 汽车/机器人 8MP 图像传感器 产品/资料页](https://www.ovt.com/products/ox08d10)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)