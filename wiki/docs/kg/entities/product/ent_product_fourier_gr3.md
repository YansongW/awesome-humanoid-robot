---
id: ent_product_fourier_gr3
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 傅利叶 GR-3
  en: Fourier GR-3
status: active
sources:
- id: src_fourier_official
  type: website
  url: https://www.fftai.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 傅利叶 GR-3 / Fourier GR-3

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [傅利叶智能 / Fourier Intelligence](../../../appendices/appendix-d/companies/company_fourier.md) |
| **产品类别** | 交互陪伴型人形机器人 |
| **发布时间** | 2025 年 8 月 |
| **状态** | 预售/量产准备 |
| **官网/来源** | [傅利叶官网](https://www.fftai.cn/about-medium-technical/47) |

## 产品概述

傅利叶 GR-3（内部代号 Care-bot）是傅利叶首款主打交互陪伴场景的全尺寸人形机器人。GR-3 身高 165 cm，体重 71 kg，全身配备 55 个自由度，并搭载 12 DOF 灵巧手。与传统金属感机器人不同，GR-3 采用莫兰迪暖色调、超跑级内饰包覆材料与“固特棉 GFOAM”软包内里，强调亲和力与安全感。

GR-3 搭载傅利叶自研全感交互系统，集成听觉、视觉、触觉三大模块，支持情感反馈与自然交互。其双电池热插拔架构单次续航约 3 小时，可在不间断供电状态下完成电池更换，适用于独居老人陪伴、儿童互动及康复辅助等场景。

## 产品图片

> Fourier GR-3：请访问 [官方资料](https://www.fftai.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 165 cm（高） | 傅利叶官网 |
| 重量 | 71 kg | 傅利叶官网 |
| 自由度（整机） | 55 DOF | 傅利叶官网 |
| 关键性能指标 | 12 DOF 灵巧手；单手负载能力未公开 | 公开规格 |
| 行走速度 | 未公开 | - |
| 续航 | 约 3 小时（双电池热插拔） | 傅利叶官网 |
| 计算平台 | 未公开 | - |
| 价格 | 未公开（2025 年 9 月开启预售） | 官方渠道 |

## 供应链位置

- **制造商**：[傅利叶智能 / Fourier Intelligence](../../../appendices/appendix-d/companies/company_fourier.md)
- **核心零部件/技术来源**：自研一体化执行器、全感交互系统、软包覆材料与电池系统；视觉与 AI 计算模块外购。
- **下游应用/客户**：养老陪伴、儿童互动、康复辅助、家庭服务。

## 知识图谱节点与关系

- 产品实体：`ent_product_fourier_gr3`
- 制造商实体：`ent_company_fourier`
- 关键关系：
  - `rel_ent_company_fourier_manufactures_ent_product_fourier_gr3`（`ent_company_fourier` → `manufactures` → `ent_product_fourier_gr3`）

## 应用场景

- **老年陪伴**：独居老人日常陪护、健康提醒、情感交流与紧急呼叫辅助。
- **儿童互动**：早教陪伴、游戏互动与自闭症儿童社交训练支持。
- **康复辅助**：家庭与社区场景下的轻度康复训练与运动鼓励。

## 竞争对比

| 对比项 | 傅利叶 GR-3 | 1X NEO | Tesla Optimus Gen 3 |
|--------|-------------|--------|---------------------|
| 定位 | 交互陪伴人形 | 家庭通用人形 | 通用/工业人形 |
| 整机 DOF | 55 | 75 | 28+ 躯干 + 22×2 手 |
| 续航 | 约 3 h（热插拔） | 未公开 | 约 2–4 h（估计） |
| 核心优势 | 软包覆安全设计、情感交互 | 肌腱驱动、静音、消费级目标 | 制造规模目标 |

## 选购与部署建议

- 养老机构或家庭用户应重点关注 GR-3 的隐私保护、跌倒检测与紧急呼叫机制。
- 部署前建议进行小范围试用，评估用户接受度、续航满足度与长期维护成本。

## 参考资料

1. [傅利叶 GR-3 官方介绍](https://www.fftai.cn/about-medium-technical/47)
2. [IT之家 – 傅利叶 GR-3 开启预售](https://www.ithome.com/0/881/148.htm)
3. [电子发烧友 – 傅利叶 GR-3 发布](http://mp.weixin.qq.com/s?__biz=MjM5NjIzMDkwMQ==&mid=2651763661)
4. [腾讯新闻 – 傅利叶 GR-3 发布](https://news.qq.com/rain/a/20250807A01N0G00)