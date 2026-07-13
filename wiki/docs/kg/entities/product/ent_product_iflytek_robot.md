---
id: ent_product_iflytek_robot
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 科大讯飞机器人
  en: 科大讯飞机器人
status: active
sources:
- id: src_ent_product_iflytek_robot
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 科大讯飞机器人

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [科大讯飞 / iFlytek](../../../appendices/appendix-d/companies/company_iflytek.md) |
| **产品类别** | 具身智能机器人/服务机器人 |
| **发布时间** | 2023–2024 年逐步发布相关方案 |
| **状态** | 方案/合作开发中 |
| **官网/来源** | 见正文参考资料 |

## 产品概述

科大讯飞机器人方案以讯飞星火大模型与机器人超脑为核心，结合领先的语音交互、自然语言理解与多模态感知能力，面向服务机器人、养老陪护、教育、导览等场景提供智能体大脑。公司在运动控制与整机方面多与合作伙伴联合开发，强调“大脑”与交互能力赋能。

## 产品图片

> 科大讯飞机器人：请访问 [官方资料](https://www.iflytek.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 核心能力 | 语音识别、自然语言理解、多模态交互、任务规划 | 科大讯飞官网 |
| 大脑平台 | 讯飞星火大模型 + 机器人超脑 | 科大讯飞公开资料 |
| 语音交互 | 远场拾音、方言识别、多轮对话 | 科大讯飞公开资料 |
| 视觉理解 | 结合讯飞星火多模态能力 | 公开报道 |
| 运动控制 | 与整机合作伙伴联合开发 | 未公开 |
| 部署方式 | 云端 + 边缘端 | 科大讯飞官网 |
| 典型场景 | 导览、陪护、教育、医疗 | 公开报道 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[科大讯飞 / iFlytek](../../../appendices/appendix-d/companies/company_iflytek.md)
- **核心零部件/技术来源**：AI 芯片/服务器、麦克风阵列、摄像头模组、整机合作伙伴。
- **下游应用/客户**：服务机器人 OEM、养老机构、教育机构、医疗机构、展厅/政务。

## 知识图谱节点与关系

- 产品实体：`ent_product_iflytek_robot`
- 制造商实体：`ent_company_iflytek`
- 关键关系：
  - `rel_ent_company_iflytek_manufactures_ent_product_iflytek_robot`（`ent_company_iflytek` → `manufactures` → `ent_product_iflytek_robot`）
  - `ent_product_iflytek_robot` -- `uses` --> `ent_product_iflytek_xinghuo`
  - `ent_product_iflytek_robot` -- `uses` --> `ent_component_voice_array`

## 应用场景

- **展厅导览**：基于语音与视觉的迎宾、讲解、问答。
- **养老陪护**：情感陪伴、健康提醒、紧急呼叫联动。
- **教育互动**：AI 教师、编程教育、儿童陪伴。

## 竞争对比

| 对比项 | 讯飞机器人 | 商汤具身方案 | 优必选 Walker |
|--------|------|------|------|
| 核心优势 | 语音交互与中文大模型 | 视觉与多模态 | 整机与运动控制 |
| 模式 | 大脑+生态合作 | 模型+感知方案 | 自研整机 |
| 场景 | 服务/养老/教育 | 工业/服务 | 教育/商用 |

## 选购与部署建议

- 根据算力/精度/场景需求选择对应型号，优先考虑官方支持的工具链与生态兼容性。
- 部署前确认供电、散热、机械接口与通信协议是否满足整机要求。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：科大讯飞 / iFlytek](../../../appendices/appendix-d/companies/company_iflytek.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [科大讯飞 / iFlytek 官方产品/公司页面](https://www.iflytek.com)
2. [科大讯飞官网](https://www.iflytek.com)
3. 科大讯飞星火大模型发布会