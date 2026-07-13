# Apptronik / Apptronik

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Apptronik |
| **英文名** | Apptronik |
| **总部** | 美国德克萨斯州奥斯汀 |
| **成立时间** | 2016 |
| **官网** | [https://apptronik.com](https://apptronik.com) |
| **供应链环节** | 通用人形机器人、NASA 合作背景 |
| **企业属性** | 初创公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | Apptronik 官网、Apollo 产品页、公开融资与合作报道 |

## 公司简介

Apptronik 从 NASA Valkyrie 项目中成长起来，Apollo 定位工业物流与制造，支持模块化底座与热插拔电池。

Apollo 采用模块化设计，上部身体可安装在双足腿、轮式底座或固定立柱上，适配不同作业场景。公司与 Mercedes-Benz、GXO、NASA 等合作推进试点。

Apptronik 的历史可追溯至 NASA 的 Valkyrie 人形机器人项目，团队积累了航天级执行器、高功率密度关节和安全协作控制方面的经验。除 Apollo 整机外，Apptronik 还向第三方提供定制执行器与关节模块。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Apollo 人形机器人 | 工业/物流人形 | Apollo | 制造、仓储、物流 |
| Apollo 软件栈 | 任务规划与人机交互 | Apptronik SDK | 现场部署、快速任务切换 |
| 机器人执行器/关节 | 核心零部件 | 定制执行器 | 第三方机器人、航天 |

## 代表产品

### Apptronik Apollo

> Apptronik Apollo：请访问 [官方资料](https://apptronik.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 173 cm（高） | 公开资料 |
| 重量 | 约 72.6–73 kg | 公开资料 |
| 自由度 | 71 | 公开资料 |
| 负载/扭矩 | 约 25 kg | 公开资料 |
| 速度/转速 | 约 3.4–5.4 km/h（不同来源） | 公开资料 |
| 续航 | 每块电池约 4 小时，热插拔支持 22 小时/日 | 公开资料 |
| 接口/通信 | NVIDIA Jetson AGX Orin + Orin NX、Apptronik SDK | 公开资料 |
| 价格 | 未公开（规模化目标 < 50,000 USD） | 公开报道 |

**技术亮点**：高负载、热插拔电池、模块化移动底座（双足/轮式/立柱）、力控安全架构、NASA 合作背景。

**应用场景**：汽车制造、仓储搬运、物流 kitting、航天与地面应用。

Apollo 的力控架构与模块化底座使其可根据任务需求在双足、轮式与固定立柱之间切换，降低部署改造成本。其软件栈支持自然语言指令与视觉引导抓取，便于非专业操作员快速部署。

> 注：Apollo 当前仅通过企业试点项目提供，具体报价需直接联系 Apptronik。

## 供应链位置

- **上游关键零部件/材料**：NVIDIA 计算平台、电机/线性执行器、传感器、结构件。
- **下游客户/应用场景**：Mercedes-Benz、GXO Logistics、NASA、Google。
- **主要竞争对手/对标**：Tesla Optimus、Figure 02、Boston Dynamics Atlas、Agility Robotics Digit。

## 知识图谱节点与关系

- 公司实体：`ent_company_apptronik`
- 产品/平台实体：`ent_product_apptronik_apollo`
- 关键关系：
  - `rel_ent_company_apptronik_manufactures_ent_product_apptronik_apollo`（`ent_company_apptronik` → `manufactures` → `ent_product_apptronik_apollo`）

## 参考资料

1. [Apptronik 官网](https://apptronik.com)
2. [Apptronik Apollo 产品页](https://apptronik.com/apollo)
3. [RoboZaps Apptronik Apollo Review](https://blog.robozaps.com/b/apptronik-apollo-review)