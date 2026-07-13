# 罗克韦尔自动化 Integrated Architecture / ControlLogix

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [罗克韦尔自动化 / Rockwell Automation, Inc.](../companies/company_rockwell.md) |
| **产品类别** | 可编程自动化控制器 / 工业自动化平台 |
| **发布时间** | 未公开 |
| **状态** | 发布/商用 |
| **官网/来源** | [https://www.rockwellautomation.com](https://www.rockwellautomation.com) |

## 产品概述

ControlLogix 5580 是罗克韦尔自动化 Integrated Architecture 平台的核心 PAC，采用统一 Logix 控制引擎，集成标准、安全、运动与过程控制。

## 产品图片

> ControlLogix 5580：请访问 [官方资料](https://www.rockwellautomation.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 控制器类型 | 可编程自动化控制器（PAC） | Rockwell 官网 |
| 处理器 | 未公开 | Rockwell 官网 |
| I/O 扩展 | 模块化，支持本地与分布式 I/O | Rockwell 官网 |
| 通信协议 | EtherNet/IP、ControlNet、DeviceNet | Rockwell 官网 |
| 编程环境 | Studio 5000 Logix Designer | Rockwell 官网 |
| 防护等级 | IP20（控制柜内） | Rockwell 官网 |
| 安装方式 | DIN 导轨 / 面板安装 | Rockwell 官网 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[罗克韦尔自动化 / Rockwell Automation, Inc.](../companies/company_rockwell.md)
- **核心零部件/技术来源**：自研 Logix 控制引擎与 FactoryTalk 软件；外购半导体芯片、PCB、连接器、电源模块。
- **下游应用/客户**：汽车 OEM、消费品、生命科学、石油天然气、自动化集成商。

## 知识图谱节点与关系

- 产品实体：`ent_product_rockwell_automation`
- 制造商实体：`ent_company_rockwell`
- 关键关系：
  - `rel_ent_company_rockwell_manufactures_ent_product_rockwell_automation`（`ent_company_rockwell` → `manufactures` → `ent_product_rockwell_automation`）

## 应用场景

- **产线控制、机器人单元集成、人形机器人测试与装配线、数字化工厂 MES/OT 融合。**
- **商业服务**：用于导览、接待、展示与品牌互动。
- **工业制造**：在柔性产线执行搬运、装配、检测等任务。
- **科研教育**：作为机器人控制、AI 训练与具身智能研究的硬件平台。

## 扩展与生态

- 制造商提供官方 SDK、仿真工具与售后培训，具体细节需通过官方渠道确认。
- 可与主流 MES/WMS/PLC 系统对接，但接口协议需以官方文档为准。
- 建议部署前进行场景化验证与兼容性测试。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 未公开 | 同类产品视具体场景而定 |
| 核心优势 | 统一 Logix 控制引擎，集成标准、安全、运动与过程控制；通过 EtherNet/IP 实现机器人、伺服与信息化系统无缝连接。 | 未公开 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [ControlLogix 5580 产品页](https://www.rockwellautomation.com/en-us/products/hardware/allen-bradley/controllers/programmable-automation-controllers.html)
2. [罗克韦尔自动化 官网](https://www.rockwellautomation.com)
3. [公开资料与行业研报](https://www.rockwellautomation.com)