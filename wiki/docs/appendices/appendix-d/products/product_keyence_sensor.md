# 基恩士 SR-X100 AI 读码器 / Keyence SR-X100 AI Code Reader

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [基恩士 / Keyence](../companies/company_keyence.md) |
| **产品类别** | 工业 AI 读码器/视觉传感器 |
| **发布时间** | 持续在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [基恩士官网](https://www.keyence.com) |

## 产品概述

基恩士 SR-X100 是一款标准型 140 万像素 AI 读码器，内置 CMOS 图像传感器、高亮度红色 LED 照明与自动对焦机构，可快速读取二维码、DataMatrix、PDF417、Aztec 以及常见一维条码。

SR-X100 支持 70 – 1000 mm 读取距离，最小二维码分辨率可达 0.024 mm，并提供 Ethernet、RS-232C 与 USB 2.0 等多种通信接口，兼容 EtherNet/IP、PROFINET、MC 协议与 OPC UA。其 IP65/IP67 防护等级与紧凑机身（约 180 g）使其适合电子、汽车、物流与机器人等严苛工业环境。

## 产品图片

> Keyence SR-X100：请访问 [官方资料](https://www.keyence.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 标准型 AI 读码器 | 官方 datasheet |
| 图像传感器 | CMOS 图像传感器 | 官方 datasheet |
| 像素 | 1360 × 1024（140 万像素） | 官方 datasheet |
| 对焦 | 自动对焦 | 官方 datasheet |
| 照明光源 | 高亮度红色 LED | 官方 datasheet |
| 指示器光源 | 高亮度绿色 LED | 官方 datasheet |
| 支持二维码 | QR、MicroQR、DataMatrix、PDF417、Aztec 等 | 官方 datasheet |
| 支持一维码 | CODE39、CODE128、EAN/UPC 等 | 官方 datasheet |
| 最小分辨率（二维码） | 0.024 mm | 官方 datasheet |
| 最小分辨率（条码） | 0.082 mm | 官方 datasheet |
| 读取距离 | 70 – 1000 mm | 官方 datasheet |
| 视野范围 | 74 mm × 55 mm（距离 300 mm 时） | 官方 datasheet |
| 控制输入/输出 | 2 点输入 / 3 点输出 | 官方 datasheet |
| 通信接口 | Ethernet（100BASE-TX）、RS-232C、USB 2.0 | 官方 datasheet |
| 支持协议 | TCP/IP、EtherNet/IP、PROFINET、MC 协议、OPC UA 等 | 官方 datasheet |
| 供电 | 24 VDC +25%/-20% | 官方 datasheet |
| 功耗 | 约 650 mA | 官方 datasheet |
| 防护等级 | IP65 / IP67 | 官方 datasheet |
| 工作温度 | 0℃ – +45℃ | 官方 datasheet |
| 重量 | 约 180 g | 官方 datasheet |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[基恩士 / Keyence](../companies/company_keyence.md)
- **核心零部件/技术来源**：自研图像处理算法与自动对焦技术；CMOS 传感器、LED 照明、光学镜头、通信芯片外购。
- **下游应用/客户**：电子制造、汽车、物流仓储、食品医药、机器人 OEM。

## 知识图谱节点与关系

- 零部件实体：`ent_component_keyence_sr_x100`
- 制造商实体：`ent_company_keyence`
- 关键关系：
  - `rel_ent_company_keyence_manufactures_ent_component_keyence_sr_x100`（`ent_company_keyence` → `manufactures` --> `ent_component_keyence_sr_x100`）

## 应用场景

- **电子制造**：PCB 二维码读取、SMT 追溯、元器件标识识别。
- **物流仓储**：包裹条码快速扫描、分拣线批量读码。
- **汽车追溯**：零部件激光打标、装配工序追溯。
- **食品医药**：包装批号、有效期 OCR 与追溯管理。

## 竞争对比

| 对比项 | 基恩士 SR-X100 | 康耐视 DataMan 260 | 海康机器人 MV-ID |
|--------|----------------|--------------------|------------------|
| 像素 | 140 万 | 多型号 | 多型号 |
| 读取距离 | 70 – 1000 mm | 因型号而异 | 因型号而异 |
| 最小分辨率（二维码） | 0.024 mm | 因型号而异 | 因型号而异 |
| 通信协议 | EtherNet/IP、PROFINET、OPC UA 等 | 丰富 | 丰富 |
| 防护等级 | IP65/IP67 | IP65/IP67 | 因型号而异 |
| 核心优势 | 自动对焦、FA 生态整合 | 深度学习读码 | 成本优势、本土化 |

## 选购与部署建议

- 选型时确认条码类型、最小模块尺寸、读取距离与产线速度，并验证现场光照与振动影响。
- 对于低对比度、反光或破损条码，可评估 SR-X300 系列内置 AI 滤镜的版本。

## 参考资料

1. [基恩士官网](https://www.keyence.com)
2. [基恩士 SR-X100 产品页](https://www.keyence.com.cn/products/barcode/barcode-readers/sr-x/models/sr-x100/)
3. [基恩士 SR-X 系列规格](https://www.keyence.com.my/products/barcode/barcode-readers/sr-x/specs/)
4. [附录 D 企业目录](../index-companies.md)