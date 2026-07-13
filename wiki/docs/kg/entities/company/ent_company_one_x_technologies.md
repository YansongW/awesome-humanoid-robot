---
id: ent_company_one_x_technologies
schema_version: 1
type: company
'title:': 1X Technologies
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 1X Technologies
  en: 1X Technologies
aliases:
- 1X Technologies
- 1X Technologies
status: active
sources:
- id: src_one_x_technologies_official
  type: website
  url: https://www.1x.tech
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 1X Technologies / 1X Technologies

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 1X Technologies |
| **英文名** | 1X Technologies |
| **总部** | 挪威 Moss / 美国加利福尼亚州圣克拉拉 |
| **成立时间** | 2014 |
| **官网** | [https://www.1x.tech](https://www.1x.tech) |
| **供应链环节** | 消费级人形机器人、具身学习 |
| **企业属性** | 初创公司（OpenAI 等投资） |
| **母公司/所属集团** | 无 |
| **数据来源** | 1X Technologies 官网、公开产品页、第三方规格汇总 |

## 公司简介

1X Technologies 致力于打造安全、轻量、面向家庭的通用人形机器人，采用肌腱驱动与软体外壳设计。

1X 的产品包括双足 NEO 与轮式双臂 EVE。NEO 强调家庭安全、低噪音与自然交互，通过 1X Studio 远程示教进行 embodied learning。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| NEO | 双足家用/商业人形 | NEO | 家庭服务、照护、零售 |
| EVE | 轮式双臂机器人 | EVE | 商业安保、物流、研究 |

## 代表产品

### 1X NEO

> 1X NEO：请访问 [官方资料](https://www.1x.tech) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 167–168 cm（高） | 公开资料 |
| 重量 | 约 30 kg | 公开资料 |
| 自由度 | 39 | HumanoidHub 汇总 |
| 负载/扭矩 | 整体搬运约 25 kg；最大举重约 70 kg | 公开资料 |
| 速度/转速 | 步行约 1.4 m/s；跑步最高约 6.2 m/s | 公开资料 |
| 续航 | 约 4 小时（842 Wh） | 公开资料 |
| 接口/通信 | 1X NEO Cortex（NVIDIA Jetson Thor）、Wi-Fi/蓝牙/5G | 公开资料 |
| 价格 | 20,000 USD + 499 USD/月 订阅；定金 200 USD | 公开资料 |

**技术亮点**：肌腱驱动 Myofibers、软体外壳与 3D 晶格聚合物、低噪音、面向家庭的安全设计、expert teleop embodied learning。

**应用场景**：家务、老年照护、轻商业服务、研究。


### 1X EVE

> 1X EVE：请访问 [官方资料](https://www.1x.tech) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 轮式移动、双臂操作 | 公开描述 |
| 价格 | 未公开 | - |

**技术亮点**：轮式双臂平台，可在商业环境中执行巡逻、物品递送等任务，为 NEO 提供先期数据与场景验证。

**应用场景**：商业安保、物流辅助、研究。


## 供应链位置

- **上游关键零部件/材料**：NVIDIA Jetson Thor 计算、肌腱驱动执行器、软体材料、视觉与麦克风阵列。
- **下游客户/应用场景**：家庭用户、养老机构、零售与安保企业。
- **主要竞争对手/对标**：Tesla Optimus、Figure 03、Apptronik Apollo。

## 知识图谱节点与关系

- 公司实体：`ent_company_one_x_technologies`
- 产品/平台实体：`ent_product_one_x_technologies_neo`、`ent_product_one_x_technologies_eve`
- 关键关系：
  - `rel_ent_company_one_x_technologies_manufactures_ent_product_one_x_technologies_neo`（`ent_company_one_x_technologies` → `manufactures` → `ent_product_one_x_technologies_neo`）
  - `rel_ent_company_one_x_technologies_manufactures_ent_product_one_x_technologies_eve`（`ent_company_one_x_technologies` → `manufactures` → `ent_product_one_x_technologies_eve`）

## 参考资料

1. [1X Technologies 官网](https://www.1x.tech)
2. [HumanoidHub 1X NEO 规格](https://www.humanoidhub.ai/robots/1x-neo)
3. [RoboZaps 1X NEO Review](https://blog.robozaps.com/b/1x-neo-review)