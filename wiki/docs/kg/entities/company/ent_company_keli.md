---
id: ent_company_keli
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 柯力传感
  en: 柯力传感
status: active
sources:
- id: src_keli_official
  type: website
  url: https://www.kelichina.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 柯力传感 / 柯力传感

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 柯力传感 |
| **英文名** | Keli Sensing Technology |
| **总部** | 中国浙江宁波 |
| **成立时间** | 1995 |
| **官网** | [https://www.kelichina.com](https://www.kelichina.com) |
| **供应链环节** | 应变式传感器、六维力/力矩传感器、工业物联网 |
| **企业属性** | 上市公司（上交所：603662）、国家级制造业单项冠军 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 柯力传感官网、年报、上证 e 互动、公开研报 |

## 公司简介

柯力传感（Keli Sensing Technology）是中国领先的传感器与物联网系统集成商，连续十余年保持国内力学传感器市场占有率第一。

公司以应变式称重传感器起家，逐步拓展至多物理量传感器、工业物联网平台与机器人传感器。在机器人领域，柯力传感重点布局六维力/力矩传感器、关节力矩传感器与触觉传感器，已向上汽通用五菱、智元机器人、华为、字节跳动等客户送样或供货，目标成为全球机器人全身传感器核心供应商。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 力学传感器及仪表 | 称重/测力 | SBE / KELI 系列 | 工业衡器、自动化设备 |
| 六维力/力矩传感器 | 机器人末端与关节力控 | KL6D-M30-B 系列 | 人形机器人、协作机器人 |
| 关节力矩传感器 | 旋转关节力矩 | 未公开 | 人形机器人、工业机器人 |
| 工业物联网 | 场景化系统集成 | 智慧物流、智能库房 | 智能制造、智慧城市 |

## 代表产品

### 柯力传感 KL6D-M30-B 系列六维力传感器

> Keli KL6D-M30-B：请访问 [官方资料](https://www.kelichina.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 机器人专用六维力传感器 | 公开报道 |
| 精度 | 0.1% FS | 公开报道 |
| 采样率 | 1 kHz | 公开报道 |
| 测量原理 | 高精度电阻应变式 | 公开报道 |
| 通信方式 | 高速采样数字通讯（外接数采） | 公开报道 |
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：专为机器人手腕、脚腕与工业机械臂末端设计，结构解耦与算法解耦结合，实现高速采样数字通讯。

**应用场景**：人形机器人手腕/脚踝力控、协作机器人末端、工业机械臂受力检测、精密装配。

### 柯力传感 SBE 应变式传感器

> Keli SBE：请访问 [官方资料](https://www.kelichina.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 应变式力传感器 | 经销商资料 |
| 测量原理 | 电阻应变式 | 经销商资料 |
| 特点 | 高精度、结构稳定、线性度与重复性良好 | 经销商资料 |
| 应用领域 | 称重、测力、工业自动化、质量控制 | 经销商资料 |
| 量程 | 未公开 | - |
| 精度 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：长期可靠性高，适用于集成到各类称重和测力系统中。

**应用场景**：工业自动化产线、试验机、称重系统、汽车测试。

## 供应链位置

- **上游关键零部件/材料**：应变片、高性能钢材、ASIC 芯片、封装材料、精密加工
- **下游客户/应用场景**：工业衡器、人形机器人、协作机器人、汽车 OEM、智慧物流、智慧城市
- **主要竞争对手/对标**：宇立仪器、坤维科技、HBM、Vishay、汉威科技

## 知识图谱节点与关系

- 公司实体：`ent_company_keli`
- 产品实体：`ent_component_keli_kl6d_m30b`
- 产品实体：`ent_component_keli_sbe`
- 关键关系：
  - `ent_company_keli` -- `manufactures` --> `ent_component_keli_kl6d_m30b`
  - `ent_company_keli` -- `manufactures` --> `ent_component_keli_sbe`
  - `ent_component_keli_kl6d_m30b` -- `used_in` --> `ent_product_humanoid_robot_wrist`

## 参考资料

1. [柯力传感官网](https://www.kelichina.com)
2. [新浪财经 – 柯力传感六维力传感器送样智元](https://finance.sina.com.cn/stock/relnews/cn/2025-04-03/doc-inerwmtr2673181.shtml)
3. [人形机器人核心零部件报告 – 柯力传感](http://mp.weixin.qq.com/s?__biz=MzIxNTcxNTczNQ==&mid=2247528030&idx=1&sn=3b1493830db732656e3ba2fc0ac3de39)
4. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)