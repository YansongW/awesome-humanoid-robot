# 优必选 / UBTECH Robotics

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 优必选科技 |
| **英文名** | UBTECH Robotics |
| **总部** | 中国深圳 |
| **成立时间** | 2012 年 |
| **官网** | [https://www.ubtrobot.com](https://www.ubtrobot.com) / [commercial.ubtrobot.com](https://www.commercial.ubtrobot.com/) |
| **供应链环节** | 整机 OEM / 工业与服务人形机器人 |
| **企业属性** | 上市公司（港交所 09880.HK）、国家级专精特新“小巨人” |
| **母公司/所属集团** | 无 |
| **数据来源** | 优必选官网、港交所公告、IT之家、WAIC 公开报道 |

## 公司简介

优必选是中国最早实现人形机器人商业化量产的企业之一，定位“人形机器人全栈技术+行业解决方案”提供商。

公司从教育服务机器人起步，逐步拓展到人工智能教育、物流、康养及工业制造领域。2023 年于港交所上市后，优必选重点推进 Walker 系列在新能源汽车总装、3C 制造等场景的规模化落地，并提出“人形机器人进工厂”战略。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 工业人形 | 7×24 小时产线作业、自主换电 | Walker S / S1 / S2 | 汽车总装、3C 装配、物流分拣 |
| 服务人形 | 迎宾导览、教育科研 | Walker X / Alpha 系列 | 展厅、教育、科研 |

## 代表产品

### Walker S2

> 优必选 Walker S2：请访问 [官方资料](https://www.ubtrobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 176 cm | 第三方经销商资料 |
| 重量 | 约 70 kg | 第三方经销商资料 |
| 自由度 | 52 DOF | Humanoid.Guide / 经销商资料 |
| 负载/扭矩 | 双臂负载 15 kg，单手 7 kg | 经销商公开规格 |
| 速度/转速 | 最大 2 m/s（约 7.2 km/h） | 公开报道 |
| 续航 | 约 2–2.5 h | 经销商资料 |
| 接口/通信 | Wi-Fi | 经销商资料 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：第四代仿生双臂、自主热插拔电池系统（官方宣称 3 分钟完成换电）、BrainNet 2.0 + Co-Agent 多模态任务规划。

**应用场景**：汽车工厂分拣搬运、产线上下料、夜间连续作业等。

### Walker S1

> 优必选 Walker S1：请访问 [官方资料](https://www.ubtrobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 172 cm | 公开报道 |
| 重量 | 约 65 kg | 公开报道 |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

**技术亮点**：面向工业场景的早期部署平台，与 Walker S2 共享部分运控与感知架构。

**应用场景**：新能源汽车产线实训、3C 工厂协作搬运。

## 供应链位置

- **上游关键零部件/材料**：自研伺服舵机与关节模组，外购谐波减速器、力传感器、电池、结构件（参见 [第 7 章 供应商地图](../../../chapters/chapter-07.md)）。
- **下游客户/应用场景**：比亚迪、富士康、Airbus、Texas Instruments 等制造客户；教育、展厅、康养机构。
- **主要竞争对手/对标**：特斯拉 Optimus、Figure 02、宇树 H1、傅利叶 GR 系列。

## 知识图谱节点与关系

- 公司实体：`ent_company_ubtech`
- 产品实体：`ent_product_ubtech_walker_s2`、`ent_product_ubtech_walker_s1`
- 关键关系：
  - `ent_company_ubtech` -- `manufactures` --> `ent_product_ubtech_walker_s2`
  - `ent_company_ubtech` -- `manufactures` --> `ent_product_ubtech_walker_s1`
  - `ent_product_ubtech_walker_s2` -- `uses` --> `ent_component_lithium_battery`

## 参考资料

1. [优必选官网](https://www.ubtrobot.com)
2. [优必选商用机器人官网](https://www.commercial.ubtrobot.com/)
3. [IT之家 – 优必选 Walker S2 报道](https://www.ithome.com)
4. [Humanoid.Guide – UBTECH Walker S2](https://humanoid.guide/product/walker-s2/)
5. [附录 D.4 重点产品 Wiki](../index-products.md)