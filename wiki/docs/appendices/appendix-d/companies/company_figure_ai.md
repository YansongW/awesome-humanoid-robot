# Figure AI / Figure AI

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Figure AI |
| **英文名** | Figure AI |
| **总部** | 美国加利福尼亚州森尼韦尔 |
| **成立时间** | 2022 |
| **官网** | [https://www.figure.ai](https://www.figure.ai) |
| **供应链环节** | 人形机器人整机厂、具身智能 |
| **企业属性** | 初创公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | Figure AI 官网、公开融资与部署报道、第三方规格汇编 |

## 公司简介

Figure AI 是专注于通用人形机器人的初创公司，主打工业制造场景，Figure 02 已在宝马斯帕坦堡工厂进行试点。

Figure AI 自研 Helix 多模态 AI 模型，使机器人可通过自然语言指令和视觉演示学习新任务。Figure 02 拥有更高的计算与感知能力，目标是替代重复性、危险性的人工劳动。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Figure 02 人形机器人 | 工业人形 | Figure 02 | 汽车制造、物流、仓储 |
| Figure 03 人形机器人 | 新一代通用/家庭 | Figure 03 | 工业、未来家庭服务 |

## 代表产品

### Figure 02

> Figure 02：请访问 [官方资料](https://www.figure.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 168 cm（高） | 公开资料 |
| 重量 | 约 70 kg | 公开资料 |
| 自由度 | 全身 28；手部未单独披露 | Humanoid.guide 等 |
| 负载/扭矩 | 搬运约 20–25 kg | 公开资料 |
| 速度/转速 | 约 1.2 m/s（4.32 km/h） | 公开资料 |
| 续航 | 约 5 小时 | 公开资料 |
| 接口/通信 | 双 NVIDIA GPU 计算、6×RGB 相机、语音交互 | 公开资料 |
| 价格 | 未公开（试点项目约 130,000 USD 估算） | 第三方估计 |

**技术亮点**：Helix 多模态 AI、宝马工厂部署验证、躯干集成电池、6×RGB 相机与语音交互、3 倍于 Figure 01 的算力。

**应用场景**：汽车装配线 kitting、物料搬运、仓储分拣。


### Figure 03

> Figure 03：请访问 [官方资料](https://www.figure.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 170 cm（高） | 公开报道 |
| 重量 | 约 60–70 kg | 公开报道 |
| 自由度 | 40+；手部 16×2 | 公开报道 |
| 负载/扭矩 | 约 25 kg | 公开报道 |
| 速度/转速 | 约 1.2 m/s | 公开报道 |
| 续航 | 约 5+ 小时（2.25 kWh） | 公开报道 |
| 接口/通信 | Helix VLA 模型、语音交互 | 公开报道 |
| 价格 | 未公开 | - |

**技术亮点**：更高自由度手部、面向家庭与工业的通用设计、Helix VLA 端到端推理。

**应用场景**：工业制造、未来家庭协助、零售服务。


## 供应链位置

- **上游关键零部件/材料**：NVIDIA GPU 计算、电机/减速器、传感器与电池包外购或定制。
- **下游客户/应用场景**：BMW 斯帕坦堡工厂、物流与制造企业。
- **主要竞争对手/对标**：Tesla Optimus、Boston Dynamics Atlas、Agility Robotics Digit、Apptronik Apollo。

## 知识图谱节点与关系

- 公司实体：`ent_company_figure_ai`
- 产品/平台实体：`ent_product_figure_ai_figure_02`、`ent_product_figure_ai_figure_03`
- 关键关系：
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02`（`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`）
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_03`（`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_03`）

## 参考资料

1. [Figure AI 官网](https://www.figure.ai)
2. [Humanoid.guide Figure 02 规格](https://humanoid.guide/product/figure-02/)
3. [The Robot Report 对 Figure 02 的报道](https://www.therobotreport.com/figure-02-advances-humanoid-robotics-frontier)