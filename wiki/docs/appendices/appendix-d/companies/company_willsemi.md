# 韦尔股份 / Will Semiconductor

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 韦尔股份 |
| **英文名** | Will Semiconductor |
| **总部** | 中国上海 |
| **成立时间** | 2007（2019 年收购 OmniVision） |
| **官网** | [https://www.willsemi.com / https://www.ovt.com](https://www.willsemi.com) |
| **供应链环节** | CMOS 图像传感器（OmniVision）、半导体分立器件、电源管理 IC |
| **企业属性** | 上市公司（603501）、全球前三 CMOS 图像传感器供应商 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 韦尔股份年报、OmniVision 官网、公开产品 brief |

## 公司简介

韦尔股份（Will Semiconductor）是中国领先的半导体设计公司，旗下豪威科技（OmniVision）是全球知名的 CMOS 图像传感器供应商。OmniVision 产品覆盖手机、汽车、安防、医疗与工业视觉，OV50H 等 50MP 高像素传感器已被广泛应用于国内高端旗舰机型。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 手机 CIS | 高像素主摄/广角 | OV50H / OV64B / OV32C | 智能手机 |
| 汽车 CIS | 环视/前视/舱内 | OX08B / OX03C 等 | 智能汽车 |
| 安防/工业 CIS | 低照度、全局快门 | OS02 / OG0 系列 | 安防、机器人 |
| 分立器件与 PMIC | 功率器件、电源管理 | MOSFET、LDO 等 | 消费电子、汽车 |

## 代表产品

### 韦尔股份 OmniVision OV50H 图像传感器

> 韦尔股份 OmniVision OV50H 图像传感器：请访问 [官方资料](https://www.willsemi.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 50MP CMOS 图像传感器 | OmniVision 官网 |
| 有效像素 | 50 MP（8192 × 6144） | OmniVision 官网 |
| 像素尺寸 | 1.197 µm | OmniVision 官网 |
| 光学尺寸 | 1/1.3" | OmniVision 官网 |
| 技术 | PureCel®Plus-S、DCG™ HDR、H/V QPD | OmniVision 官网 |
| 帧率 | 50MP@30fps / 12.5MP@120fps | OmniVision 官网 |
| HDR | DCG / Staggered HDR | OmniVision 官网 |
| 对焦 | H/V QPD PDAF，100% 覆盖率 | OmniVision 官网 |
| 输出格式 | 10/12/14-bit RGB RAW | OmniVision 官网 |
| 接口 | 4-lane MIPI / C-PHY | OmniVision 官网 |
| 功耗 | 活动模式约 1395 mW（50MP@30fps） | OmniVision 官网 |
| 工作温度 | -30℃ – +85℃ | OmniVision 官网 |
| 封装 | COB / RW | OmniVision 官网 |
| 价格 | 未公开 | - |

**技术亮点**：PureCel®Plus-S 堆栈、DCG™ HDR、H/V QPD 全向对焦，低光与高速对焦表现优异。

**应用场景**：高端智能手机主摄/广角、笔记本摄像头、视频会议、机器人视觉、车载感知。

### 韦尔股份 OmniVision 汽车图像传感器

> 韦尔股份 OmniVision 汽车图像传感器：请访问 [官方资料](https://www.willsemi.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 车规级 CMOS 图像传感器 | OmniVision 官网 |
| 应用 | ADAS、环视、舱内监控 | OmniVision 官网 |
| 特色 | 高动态范围、LED 闪烁抑制 | OmniVision 官网 |
| 价格 | 未公开 | - |

**技术亮点**：ASIL 功能安全支持，满足汽车电子严苛标准。

**应用场景**：自动驾驶感知、DMS/OMS、电子后视镜。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、封装测试、光学镜头、滤光片、ISP 算法
- **下游客户/应用场景**：智能手机 OEM、笔记本厂商、车载 Tier1、机器人、医疗设备
- **主要竞争对手/对标**：Sony、Samsung ISOCELL、SmartSens、GalaxyCore

## 知识图谱节点与关系

- 公司实体：`ent_company_willsemi`
- 产品实体：`ent_product_willsemi_ov50h`
- 零部件实体：`ent_component_willsemi_ov50h_sensor`
- 关键关系：
  - `ent_company_willsemi` -- `manufactures` --> `ent_product_willsemi_ov50h`
  - `ent_company_willsemi` -- `manufactures` --> `ent_component_willsemi_ov50h_sensor`
  - `ent_product_willsemi_ov50h` -- `uses` --> `ent_component_willsemi_ov50h_sensor`

## 参考资料

1. [韦尔股份官网](https://www.willsemi.com)
2. [韦尔股份 OmniVision OV50H 图像传感器产品/资料页](https://www.ovt.com/products/ov50h/)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)