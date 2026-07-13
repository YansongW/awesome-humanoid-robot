# Scale AI / Scale AI

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Scale AI |
| **英文名** | Scale AI |
| **总部** | 美国加利福尼亚州旧金山 |
| **成立时间** | 2016 年 |
| **官网** | [https://scale.com](https://scale.com) |
| **供应链环节** | AI/机器人数据标注、数据引擎、模型评估、RLHF |
| **企业属性** | 初创公司（未上市） |
| **母公司/所属集团** | 无 |
| **数据来源** | Scale AI 官网、Scale 博客、公开融资报道 |

## 公司简介

Scale AI 是全球领先的 AI 训练数据基础设施公司，其核心产品 Scale Data Engine 覆盖数据收集、筛选、标注、强化学习人类反馈（RLHF）与模型评估全生命周期。

平台支持图像、视频、3D 点云、文本、音频、传感器融合等多模态数据，广泛应用于自动驾驶、机器人、大语言模型（LLM）与政府国防项目。Scale 提供两种模式：Rapid（由 Scale 管理平台与标注员团队完成）与 Self-Serve（企业使用 Scale 工具与自有团队协作）。2025 年，Scale 推出 Physical AI 项目，专门采集用于训练具身智能与机器人的第一视角演示数据。

2025 年 6 月，Meta 以 143 亿美元收购 Scale AI 49% 股权，公司估值达到 290 亿美元。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| AI 训练数据引擎 | 全生命周期数据平台 | Scale Data Engine | 自动驾驶、机器人、LLM |
| 生成式 AI 数据 | RLHF、微调、偏好对齐 | Scale Generative AI Data Engine | 大语言模型、多模态模型 |
| 政府与国防 | 安全 AI 决策平台 | Scale Donovan | 国防情报、指挥决策 |
| 模型测试评估 | 红队测试、安全评估 | Scale Test & Evaluation | 前沿模型安全 |
| 物理 AI 数据 | 机器人操作演示数据 | Scale Physical AI | 人形机器人、具身智能 |

## 代表产品

### Scale Data Engine

> Scale Data Engine：请访问 [官方资料](https://scale.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 支持数据类型 | 图像、视频、3D 点云、文本、音频、传感器融合 | Scale 官网 |
| 标注能力 | 2D/3D 边界框、语义分割、关键点、轨迹、属性 | Scale 文档 |
| 服务模式 | Rapid（托管）/ Self-Serve（自助） | Scale 官网 |
| 质量机制 | AI 预标注 + 人工审核 + 共识机制 | 公开资料 |
| 合规认证 | SOC 2 Type II、ISO 27001、FedRAMP High | Scale 官网 |
| 机器人数据 | 支持 LiDAR、相机、IMU、触觉等多传感器标注 | Scale 文档 |
| 价格 | 按任务复杂度计费（从几分钱到数美元/任务） | 公开报道 |

**技术亮点**：AI 辅助预标注、多模态数据流水线、企业级质量与安全合规、自动驾驶与机器人专用工具链、全球化众包与专家审核网络。

**应用场景**：自动驾驶感知模型训练、机器人抓取/导航数据标注、大语言模型 RLHF、医疗影像与国防情报分析。

### Scale Physical AI

> Scale Physical AI：请访问 [官方资料](https://scale.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 数据类型 | 第一视角（POV）操作演示视频 | Scale 新闻 |
| 采集方式 | 全球承包商佩戴设备采集 | 公开报道 |
| 任务场景 | 家务、装配、搬运、工具使用 | Scale 博客 |
| 标注内容 | 动作分段、物体交互、力反馈、语言指令 | 公开资料 |
| 目标模型 | 人形机器人 / 具身智能 VLA 模型 | Scale 新闻 |
| 价格 | 企业定制 | 官方询价 |

**技术亮点**：面向具身智能的大规模人类操作数据采集、多视角与多模态同步、动作-语言-视觉对齐、支持模仿学习与强化学习训练。

**应用场景**：人形机器人家务操作训练、工业装配技能学习、服务机器人交互策略、机器人基础模型数据供给。

## 供应链位置

- **上游关键零部件/材料**：AWS/Google Cloud/Azure 云基础设施、全球众包与专家标注网络、AI 预标注模型、数据安全与合规体系。
- **下游客户/应用场景**：OpenAI、Meta、Microsoft、Google、Toyota、GM、美国国防部、自动驾驶公司、机器人公司。
- **主要竞争对手/对标**：Appen、Labelbox、Surge AI、Tesla 自有标注团队、Covariant 数据飞轮。

## 知识图谱节点与关系

- 公司实体：`ent_company_scale_ai`
- 产品/平台实体：`ent_product_scale_data_engine`、`ent_product_scale_physical_ai`
- 关键关系：
  - `rel_ent_company_scale_ai_manufactures_ent_product_scale_data_engine`（`ent_company_scale_ai` → `manufactures` → `ent_product_scale_data_engine`）
  - `rel_ent_company_scale_ai_manufactures_ent_product_scale_physical_ai`（`ent_company_scale_ai` → `manufactures` → `ent_product_scale_physical_ai`）

## 参考资料

1. [Scale AI 官网](https://scale.com)
2. [Scale Data Engine 产品页](https://scale.com/data-engine)
3. [Scale Physical AI 博客](https://scale.com/blog/physical-ai)
4. [Scale AI 融资与估值报道](https://scale.com/blog)