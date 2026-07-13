# 瀚博半导体 SV100 / Vastai SV100

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [瀚博半导体 / Vastai Technologies](../companies/company_vastai.md) |
| **产品类别** | 云端 AI 推理与视频处理加速卡 |
| **发布时间** | SV100 系列随公司产品迭代发布 |
| **状态** | 量产/商用 |
| **官网/来源** | 瀚博半导体官网、产品手册 |

## 产品概述

瀚博半导体 SV100 是面向云端 AI 推理与视频理解场景的高性能加速卡，融合 AI 计算与视频编解码能力，适用于多模态内容处理。

SV100 基于瀚博自研 AI 与视频处理架构，支持 INT8/FP16 等精度，可同时处理多路高清视频流并运行深度学习模型。其视频+AI 融合特性，使其在直播转码、内容审核、智慧安防及机器人视觉回传等场景中具备优势。

## 产品图片

> 瀚博半导体 SV100：请访问 [官方资料](https://www.vastai.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 加速器 | 瀚博 SV100 | 瀚博半导体官网 |
| 架构 | 自研 AI 推理 + 视频处理架构 | 瀚博半导体公开资料 |
| 制程 | 7 nm | 公开报道 |
| AI 算力 | INT8 约 200 TOPS 级 | 瀚博半导体公开资料 |
| 显存 | 32 GB LPDDR4X / HBM（视型号） | 公开报道 |
| 视频能力 | 多路 4K/8K 视频编解码 | 瀚博半导体公开资料 |
| 接口 | PCIe Gen4 | 公开报道 |
| 功耗 | 约 75–150 W | 公开报道 |
| 软件栈 | VastStream、SDK | 瀚博半导体公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[瀚博半导体 / Vastai Technologies](../companies/company_vastai.md)
- **核心零部件/技术来源**：自研 AI/视频架构、晶圆代工、存储器、封测、PCB、散热。
- **下游应用/客户**：互联网视频平台、云计算厂商、电信运营商、智慧城市、机器人公司。

## 知识图谱节点与关系

- 产品实体：`ent_product_vastai_sv100`
- 零部件实体：`ent_component_vastai_sv100_accelerator`
- 制造商实体：`ent_company_vastai`
- 关键关系：
  - `rel_ent_company_vastai_manufactures_ent_product_vastai_sv100`（`ent_company_vastai` → `manufactures` --> `ent_product_vastai_sv100`）
  - `rel_ent_company_vastai_manufactures_ent_component_vastai_sv100_accelerator`（`ent_company_vastai` → `manufactures` --> `ent_component_vastai_sv100_accelerator`）
  - `ent_product_vastai_sv100` -- `uses` --> `ent_component_vastai_sv100_accelerator`

## 应用场景

- **云端视频理解**：实时视频分析、内容审核、智能推荐。
- **直播与云游戏**：高密度视频转码与低延迟串流。
- **机器人视觉回传**：边缘/云端协同处理机器人多路视频数据。

## 竞争对比

| 对比项 | 瀚博 SV100 | 寒武纪 MLU370 | NVIDIA T4 |
|--------|------|------|------|
| 能力 | AI + 视频融合 | AI 推理/训练 | AI 推理 |
| 视频 | 强 | 弱 | 中 |
| 生态 | VastStream | Neuware | CUDA |
| 国产化 | 自主可控 | 自主可控 | 受出口管制影响 |

## 选购与部署建议

- 优先评估视频路数、分辨率与 AI 模型并发需求是否匹配 SV100 能力。
- 部署前确认 VastStream 对目标视频格式与模型框架的支持。
- 建议通过瀚博半导体官方渠道获取最新驱动、SDK 与参考方案。

## 相关词条

- [制造商：瀚博半导体 / Vastai Technologies](../companies/company_vastai.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [瀚博半导体官网](https://www.vastai.com)
2. [瀚博半导体产品页](https://www.vastai.com/products.html)
3. 瀚博半导体产品发布会资料