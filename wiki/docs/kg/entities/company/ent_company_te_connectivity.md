---
id: ent_company_te_connectivity
schema_version: 1
type: company
'title:': 泰科电子 / TE Connectivity
domain: 02_components
theoretical_depth: system
names:
  zh: 泰科电子
  en: TE Connectivity
status: active
sources:
- id: src_te_connectivity_official
  type: website
  url: https://www.te.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 泰科电子 / TE Connectivity

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 泰科电子 |
| **英文名** | TE Connectivity |
| **总部** | 爱尔兰戈尔韦（运营总部美国宾夕法尼亚州 Berwyn） |
| **成立时间** | 1941（前身 AMP） |
| **官网** | [https://www.te.com](https://www.te.com) |
| **供应链环节** | 连接器、接插件、传感器、线缆线束 |
| **企业属性** | 上市公司（NYSE: TEL） |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、年报、产品 datasheet |

## 公司简介

TE Connectivity 是全球连接与传感领域龙头企业，年营收超百亿美元，产品覆盖交通、工业、通信与医疗市场。其连接器与线缆组件广泛应用于工业机器人、协作机器人、伺服驱动、传感器与通信模块。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| M12 / M8 圆形连接器 | 工业以太网与传感器连接 | M12 X-Code 8 位 | 工业机器人、协作机器人、视觉系统 |
| AMPMODU / Dynamic 系列 | 板端与线对板连接 | AMPMODU 2.0 mm | 控制器 I/O、电机反馈、电池管理 |
| 传感器与线束 | 力/温度/位置传感 | 力传感器、温度传感器 | 机器人关节、执行器、末端工具 |

## 代表产品

### TE Connectivity M12 X-Code 工业以太网连接器

> TE Connectivity M12 X-Code 工业以太网连接器：请访问 [官方资料](https://www.te.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 8 | IEC 61076-2-109 |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP67 | 官方 catalog |
| 传输速率 | 10 GbE（Cat6A） | 官方 catalog |
| 应用场景 | 工业机器人、协作机器人、传感器网络、视觉系统 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：M12 X-Code 编码防止误插，支持 10 GbE 工业以太网，金属锁紧、IP67 防护，适合高振动机器人环境。

**应用场景**：协作机器人关节通信、工业相机、LiDAR、力传感器、AGV/AMR 网络。

### TE Connectivity AMPMODU 2.0 mm 线对板连接器

> TE Connectivity AMPMODU 2.0 mm 线对板连接器：请访问 [官方资料](https://www.te.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 40（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 2.0 mm | 官方 catalog |
| 应用场景 | 控制器 I/O、伺服驱动反馈、电池管理 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：高密度、低成本、标准 2.0 mm 间距，适合 PCB 信号与电源分配。

**应用场景**：机器人控制器、伺服驱动板、传感器接口、工业自动化设备。

## 供应链位置

- **上游关键零部件/材料**：铜合金、工程塑料、电镀材料、半导体芯片、线缆
- **下游客户/应用场景**：工业机器人、协作机器人、汽车、通信设备、医疗设备
- **主要竞争对手/对标**：Amphenol、Molex、Hirose、JAE、J.S.T.、LEONI

## 知识图谱节点与关系

- 公司实体：`ent_company_te_connectivity`
- 产品实体：`ent_product_te_connectivity_m12`
- 零部件实体：`ent_component_te_connectivity_m12`
- 关键关系：
  - `rel_ent_company_te_connectivity_manufactures_ent_product_te_connectivity_m12`（`ent_company_te_connectivity` → `manufactures` → `ent_product_te_connectivity_m12`）
  - `rel_ent_company_te_connectivity_manufactures_ent_component_te_connectivity_m12`（`ent_company_te_connectivity` → `manufactures` → `ent_component_te_connectivity_m12`）

## 参考资料

1. [官网](https://www.te.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)