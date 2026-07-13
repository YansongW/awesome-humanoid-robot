# 商汤日日新 / 具身多模态模型

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [商汤科技 / SenseTime](../companies/company_sensetime.md) |
| **产品类别** | 多模态大模型/具身智能模型 |
| **发布时间** | 2023 年发布日日新，持续迭代 |
| **状态** | 商用/API 服务 |
| **官网/来源** | 见正文参考资料 |

## 产品概述

商汤日日新（SenseNova）是商汤科技打造的多模态大模型体系，覆盖自然语言、图像、视频、语音与代码生成。结合 SenseCore 大装置与计算机视觉优势，日日新面向具身智能提供视觉语言理解、任务规划与动作生成能力，可部署于云端或适配机器人端侧。

## 产品图片

> 商汤日日新 / 具身多模态模型：请访问 [官方资料](https://www.sensetime.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 模型系列 | 日日新 SenseNova（语言/视觉/多模态/具身） | 商汤官网 |
| 参数规模 | 数十亿至千亿级（多规格） | 商汤公开资料 |
| 能力 | 图像理解、视频分析、自然语言交互、任务规划 | 商汤公开资料 |
| 具身能力 | 视觉语言动作支持、环境理解、指令跟随 | 公开报道 |
| 部署 | 云端 API / 私有化 / 端侧适配 | 商汤官网 |
| 训练算力 | SenseCore 大装置 | 商汤官网 |
| 接口 | 商汤 API / 企业定制 | 商汤官网 |
| 价格 | 按调用量/私有化部署计费 | 商汤官网 |

## 供应链位置

- **制造商**：[商汤科技 / SenseTime](../companies/company_sensetime.md)
- **核心零部件/技术来源**：GPU/AI 芯片集群、数据标注、开源框架、算力合作伙伴。
- **下游应用/客户**：车企、机器人厂商、互联网平台、金融/医疗/教育客户。

## 知识图谱节点与关系

- 产品实体：`ent_product_sensetime_ruyi`
- 制造商实体：`ent_company_sensetime`
- 关键关系：
  - `rel_ent_company_sensetime_manufactures_ent_product_sensetime_ruyi`（`ent_company_sensetime` → `manufactures` → `ent_product_sensetime_ruyi`）
  - `ent_product_sensetime_ruyi` -- `runs_on` --> `ent_product_sensetime_sensecore`
  - `ent_product_sensetime_ruyi` -- `generates` --> `ent_data_robot_task_plan`

## 应用场景

- **人形机器人大脑**：理解自然语言指令并规划动作序列。
- **视觉导航**：结合视觉 SLAM 与语义理解实现环境交互。
- **工业质检**：多模态缺陷检测与报告生成。

## 竞争对比

| 对比项 | 日日新 | GPT-4V | 华为盘古 |
|--------|------|------|------|
| 视觉理解 | 中文场景强 | 英文通用强 | 行业/具身优化 |
| 部署 | 云+端+私有化 | 云端 API | 云+端+私有化 |
| 算力 | SenseCore | Azure/OpenAI | 昇腾 |

## 选购与部署建议

- 根据算力/精度/场景需求选择对应型号，优先考虑官方支持的工具链与生态兼容性。
- 部署前确认供电、散热、机械接口与通信协议是否满足整机要求。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：商汤科技 / SenseTime](../companies/company_sensetime.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [商汤科技 / SenseTime 官方产品/公司页面](https://www.sensetime.com)
2. [商汤官网](https://www.sensetime.com)
3. 商汤日日新发布会资料