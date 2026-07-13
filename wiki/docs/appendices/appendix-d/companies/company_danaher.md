# 丹纳赫 / Danaher Corporation

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 丹纳赫 |
| **英文名** | Danaher Corporation |
| **总部** | 美国华盛顿特区 |
| **成立时间** | 1969 年 |
| **官网** | [https://www.danaher.com](https://www.danaher.com) |
| **供应链环节** | 生命科学、诊断、环境与应用解决方案、工业运动控制 |
| **企业属性** | 上市公司（NYSE：DHR） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | Danaher 官网、年报、Kollmorgen 产品资料 |

## 公司简介

丹纳赫是全球科学与技术创新企业，通过旗下品牌提供生命科学与工业自动化解决方案。

丹纳赫旗下拥有 Kollmorgen（运动控制）、Tektronix（测试测量）、Beckman Coulter（生命科学）等众多品牌。在工业自动化领域，Kollmorgen 提供伺服电机、驱动器、直线电机、减速机与运动控制器，以高功率密度与定制化能力著称。其 AKM2G 同步伺服电机可为工业机器人、协作机器人及人形机器人关节提供紧凑型、高性能的动力单元。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 运动控制 | 伺服电机与驱动 | Kollmorgen AKM / AKD | 机器人、包装、半导体 |
| 线性运动 | 直线电机、导轨、丝杠 | Kollmorgen DDL / Thomson | 精密平台、医疗 |
| 自动化软件 | 运动控制与仿真 | Kollmorgen Motion Toolbox | 机器设计、数字孪生 |

## 代表产品

### Kollmorgen AKM2G 伺服电机

> Kollmorgen AKM2G 伺服电机：请访问 [官方资料](https://www.danaher.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 同步伺服电机 | 官方资料 |
| 功率范围 | 0.03 kW ~ 7.2 kW（具体范围依型号） | 官方资料 |
| 峰值扭矩 | 0.16 Nm ~ 53 Nm | 官方资料 |
| 最高转速 | 8,000 rpm | 官方资料 |
| 框架尺寸 | 40 / 60 / 80 / 130 / 180 mm | 官方资料 |
| 反馈类型 | 旋变 / 增量式 / 单圈或多圈绝对值编码器 | 官方资料 |
| 防护等级 | IP65（可选轴封） | 官方资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：高转矩密度、丰富的框架尺寸与反馈选项、与 AKD 系列伺服驱动即插即用、适合紧凑机器人关节。

**应用场景**：工业机器人关节、协作机器人、半导体设备、包装机械、人形机器人手臂与腿部关节。

## 与人形机器人的关联

人形机器人对关节电机的转矩密度、发热与可靠性要求极高，AKM2G 提供多规格框架与定制绕组，是关节模组动力单元的可选方案之一。

## 供应链位置

- **上游关键零部件/材料**：稀土磁材、硅钢片、轴承、编码器、绕组材料、铝合金外壳
- **下游客户/应用场景**：工业机器人、半导体设备、医疗装备、包装印刷、航空航天、人形机器人
- **主要竞争对手/对标**：Siemens, Panasonic, Yaskawa, Inovance

## 知识图谱节点与关系

- 公司实体：`ent_company_danaher`
- 产品实体：`ent_product_danaher_kollmorgen_akm2g`
- 关键关系：
  - `ent_company_danaher` -- `manufactures` --> `ent_product_danaher_kollmorgen_akm2g`

## 参考资料

1. [丹纳赫 官网](https://www.danaher.com)
2. [Kollmorgen AKM2G 伺服电机 产品页](https://www.kollmorgen.com/en-us/products/motors/servo-motors/akm2g-servo-motors)
3. Kollmorgen AKM2G servo motor datasheet