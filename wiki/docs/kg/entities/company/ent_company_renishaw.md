---
id: ent_company_renishaw
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 雷尼绍
  en: Renishaw
status: active
sources:
- id: src_renishaw_official
  type: website
  url: https://www.renishaw.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 雷尼绍 / Renishaw

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 雷尼绍 |
| **英文名** | Renishaw |
| **总部** | 英国格洛斯特郡（Wotton-under-Edge） |
| **成立时间** | 1973 |
| **官网** | [https://www.renishaw.com](https://www.renishaw.com) |
| **供应链环节** | 精密测量、编码器、机床测头、增材制造、医疗仪器 |
| **企业属性** | 上市公司（LSE: RSW）、全球计量与运动控制反馈龙头 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | Renishaw 官网、产品 datasheet、安装指南 |

## 公司简介

雷尼绍（Renishaw）是全球工程技术领域的跨国公司，专注于高精度测量与运动控制反馈技术。其产品包括坐标测量机测头、机床测头、RESOLUTE 绝对式光栅编码器、增材制造系统与神经外科医疗设备，广泛应用于机床、半导体、机器人和航空航天等领域。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 编码器系统 | 高精度位置反馈 | RESOLUTE / ATOM / TONiC | 机床、机器人、半导体 |
| 机床测头 | 在机测量与找正 | RMP60 / OMP60 | CNC 加工 |
| 坐标测量与标定 | 测头与软件 | SP25 / REVO | CMM、机器人标定 |
| 增材制造与医疗 | 金属 3D 打印、神外设备 | RenAM / neuroinspire | 航空航天、医疗 |

## 代表产品

### 雷尼绍 RESOLUTE 绝对式光栅编码器

> 雷尼绍 RESOLUTE 绝对式光栅编码器：请访问 [官方资料](https://www.renishaw.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 真正绝对式光学编码器 | Renishaw datasheet |
| 栅距 | 30 µm | Renishaw datasheet |
| 分辨率 | 最高 1 nm | Renishaw datasheet |
| 精度 | ±1 µm/m（RELA）/ ±5 µm/m（RTLA） | Renishaw datasheet |
| 最大速度 | 最高 100 m/s | Renishaw datasheet |
| 细分误差（SDE） | ±40 nm | Renishaw datasheet |
| 抖动 | 7 nm RMS | Renishaw datasheet |
| 接口 | BiSS C / DRIVE-CLiQ / FANUC / Mitsubishi / Panasonic | Renishaw datasheet |
| 防护等级 | IP64 | Renishaw datasheet |
| 工作温度 | 0℃ – +55℃ | Renishaw datasheet |
| 功能安全 | 可选 SIL2 / PL d | Renishaw datasheet |
| 价格 | 未公开 | - |

**技术亮点**：真正绝对式位置反馈、1 nm 分辨率、100 m/s 高速、多协议支持、功能安全可选。

**应用场景**：高精度数控机床、直线电机、机器人关节、半导体设备、三坐标测量机、天文望远镜。

### 雷尼绍 RMP60 无线电机床测头

> 雷尼绍 RMP60 无线电机床测头：请访问 [官方资料](https://www.renishaw.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 无线电触发式测头 | Renishaw 官网 |
| 传输 | 2.4 GHz 无线电 | Renishaw 官网 |
| 应用 | CNC 在机测量、找正 | Renishaw 官网 |
| 价格 | 未公开 | - |

**技术亮点**：360° 传输、抗干扰，提升加工精度与自动化水平。

**应用场景**：CNC 加工中心、车床在机测量。

## 供应链位置

- **上游关键零部件/材料**：光学读数头、玻璃/钢带/低膨胀合金栅尺、ASIC、电缆与连接器
- **下游客户/应用场景**：机床 OEM、机器人厂商、半导体设备、CMM 制造商、航空航天
- **主要竞争对手/对标**：Heidenhain、Mitutoyo、Fagor Automation、Newall

## 知识图谱节点与关系

- 公司实体：`ent_company_renishaw`
- 产品实体：`ent_product_renishaw_resolute_encoder`
- 零部件实体：`ent_component_renishaw_resolute_readhead`
- 关键关系：
  - `ent_company_renishaw` -- `manufactures` --> `ent_product_renishaw_resolute_encoder`
  - `ent_company_renishaw` -- `manufactures` --> `ent_component_renishaw_resolute_readhead`
  - `ent_product_renishaw_resolute_encoder` -- `uses` --> `ent_component_renishaw_resolute_readhead`

## 参考资料

1. [雷尼绍官网](https://www.renishaw.com)
2. [雷尼绍 RESOLUTE 绝对式光栅编码器产品/资料页](https://www.renishaw.com/en/resolute-absolute-encoder--9533)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)