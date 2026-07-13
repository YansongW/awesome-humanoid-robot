# 华为昇腾 / Atlas

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [华为 / Huawei](../companies/company_huawei.md) |
| **产品类别** | AI 计算平台/训练推理芯片 |
| **发布时间** | 2018 年发布昇腾 910/310，持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | 见正文参考资料 |

## 产品概述

华为昇腾是华为面向人工智能场景推出的计算平台与处理器系列，包括昇腾 910 训练芯片、昇腾 310 推理芯片及 Atlas 系列计算硬件。昇腾配合 CANN、MindSpore 与盘古大模型，构建起国产化 AI 软硬件生态，是具身智能与人形机器人大脑的国产算力底座之一。

## 产品图片

> 华为昇腾 / Atlas：请访问 [官方资料](https://www.hiascend.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 处理器 | 昇腾 910 / 310 系列 | 华为官网 |
| 算力 | 昇腾 910B FP16 约 320 TFLOPS / INT8 约 640 TOPS | 华为公开资料 |
| 内存 | HBM2e / LPDDR4X（视型号） | 华为公开资料 |
| 制程 | 7 nm（公开报道） | 公开报道 |
| Atlas 形态 | Atlas 800 训练服务器 / Atlas 300I 推理卡 | 华为官网 |
| 软件栈 | CANN、MindSpore、MindIE | 华为昇腾社区 |
| 功耗 | 约 310 W（昇腾 910 处理器） | 公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[华为 / Huawei](../companies/company_huawei.md)
- **核心零部件/技术来源**：自研达芬奇架构、晶圆代工、HBM 存储、封测、PCB、散热。
- **下游应用/客户**：互联网大厂、政企客户、智算中心、机器人整机厂、科研院所。

## 知识图谱节点与关系

- 产品实体：`ent_product_huawei_ascend`
- 制造商实体：`ent_company_huawei`
- 关键关系：
  - `rel_ent_company_huawei_manufactures_ent_product_huawei_ascend`（`ent_company_huawei` → `manufactures` → `ent_product_huawei_ascend`）
  - `ent_product_huawei_ascend` -- `uses` --> `ent_component_huawei_ascend_chip`
  - `ent_product_huawei_ascend` -- `runs` --> `ent_software_mindspore`

## 应用场景

- **具身智能大脑**：运行 VLA/VLM 大模型，实现感知、理解与任务规划。
- **大模型训练**：盘古及第三方大模型训练。
- **边缘推理**：Atlas 200I 等边缘设备用于机器人端侧推理。

## 竞争对比

| 对比项 | 昇腾 Atlas | NVIDIA Jetson/数据中心 | 寒武纪思元 |
|--------|------|------|------|
| 生态 | CANN + MindSpore + 盘古 | CUDA + PyTorch | Cambricon Neuware |
| 算力 | 高端训练/推理 | 全球领先 | 训练/推理 |
| 国产化 | 自主可控 | 受出口管制影响 | 自主可控 |

## 选购与部署建议

- 根据算力/精度/场景需求选择对应型号，优先考虑官方支持的工具链与生态兼容性。
- 部署前确认供电、散热、机械接口与通信协议是否满足整机要求。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：华为 / Huawei](../companies/company_huawei.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [华为 / Huawei 官方产品/公司页面](https://www.hiascend.com)
2. [华为昇腾社区](https://www.hiascend.com)
3. 华为 Atlas 产品手册