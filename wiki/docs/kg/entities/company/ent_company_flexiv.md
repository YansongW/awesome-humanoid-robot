---
id: ent_company_flexiv
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 非夕科技
  en: Flexiv
status: active
sources:
- id: src_flexiv_official
  type: website
  url: https://www.flexiv.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 非夕科技 / Flexiv

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 非夕科技（上海非夕机器人科技有限公司） |
| **英文名** | Flexiv |
| **总部** | 中国上海 |
| **成立时间** | 2016 年 |
| **官网** | [https://www.flexiv.cn](https://www.flexiv.cn) |
| **供应链环节** | 整机 OEM / 自适应机器人 |
| **企业属性** | 通用智能机器人独角兽 |
| **母公司/所属集团** | 无 |
| **数据来源** | 非夕官网、百度百科、中国工博会展商资料、TechNode |

## 公司简介

非夕科技由王世全与多位斯坦福校友于 2016 年创办，核心创始团队源自斯坦福大学机器人和人工智能实验室。公司提出“自适应机器人”品类，致力于将工业级力控、计算机视觉与人工智能技术深度融合，使机械臂能够像人一样手眼配合，在不确定环境下完成复杂任务。

非夕的产品线涵盖自适应机械臂 Rizon（拂晓）、力控型并联机器人 Moonlight（玄晖）、力控夹爪 Grav（星擎）、AMR 移动平台及全感知自适应机器人 Enlight（初昕）等。公司在汽车、3C 电子、医疗、航空、物流等行业提供柔性装配、曲面打磨、插拔分拣等解决方案，并牵头制定国家标准《机器人自适应能力技术要求》。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 自适应机械臂 | 七轴力控协作机器人 | Rizon 4 / Rizon 4s / Rizon 10 | 精密装配、打磨、上下料 |
| 力控并联机器人 | 接触式工艺自动化 | Moonlight | 打磨、抛光、贴合 |
| 力控夹爪 | 工业级力控末端 | Grav | 抓取、插拔 |
| 移动操作平台 | AMR + 机械臂 | 非夕 AMR 移动平台 | 产线物流、移动操作 |

## 代表产品

### Rizon 10

> Rizon 10：请访问 [官方资料](https://www.flexiv.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 臂展 941 mm | 非夕官网 |
| 重量 | 38 kg | 非夕官网 |
| 自由度 | 7 DOF | 非夕官网 |
| 负载/扭矩 | 10 kg | 非夕官网 |
| 速度/转速 | 标准末端线速度 1.0 m/s | 非夕官网 |
| 力感知精度 | 0.2 N | 非夕官网 |
| 接口/通信 | Profinet / Modbus TCP/IP | 非夕官网 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：仿人七自由度设计、工业级力控、IP65 防护、CE/ETL 双认证，支持任意角度安装与 AMR/AGV 集成。

**应用场景**：带线束插拔、精密装配、柔性打磨、曲面作业、IDC 运维。

### Moonlight 玄晖

> Moonlight：请访问 [官方资料](https://www.flexiv.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 力控精度 | 工业级力控 | 非夕官网 |
| 接口/通信 | 支持非夕控制系统 | 非夕官网 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：全球首款力控型并联机器人，融入非夕多年力控与传感技术，适配接触式工艺自动化。

**应用场景**：打磨、抛光、贴合、精密加工。

## 供应链位置

- **上游关键零部件/材料**：自研力传感器、关节一体化驱动器、机械结构；外购电机、减速器、视觉相机、计算平台。
- **下游客户/应用场景**：汽车、3C、医疗、航空、物流等行业的制造产线与自动化集成商。
- **主要竞争对手/对标**：ABB、FANUC、Universal Robots、大族机器人。

## 知识图谱节点与关系

- 公司实体：`ent_company_flexiv`
- 产品实体：`ent_product_flexiv_rizon_10`、`ent_product_flexiv_moonlight`
- 关键关系：
  - `ent_company_flexiv` -- `manufactures` --> `ent_product_flexiv_rizon_10`
  - `ent_company_flexiv` -- `manufactures` --> `ent_product_flexiv_moonlight`

## 参考资料

1. [非夕科技官网](https://www.flexiv.cn)
2. [百度百科 – Flexiv](https://baike.baidu.com/item/Flexiv/55718139)
3. [非夕官网 – Rizon 产品参数](https://www.flexiv.cn/product/rizon)
4. [TechNode – 非夕科技：自适应机器人带来的时代变革](https://cn.technode.com/post/2020-01-05/flexiv-cb-2020/)
5. [中国工博会 – 非夕科技展商推介](https://www.shifair.com/informationDetails/46551.html)