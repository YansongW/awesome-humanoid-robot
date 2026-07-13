---
id: ent_product_rulink_tactile_sensor
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 柔灵科技 3D 互动式肌电手环
  en: Rulink 3D Interactive EMG Wristband
status: active
sources:
- id: src_rulink_pitchhub
  type: website
  url: https://pitchhub.36kr.com/project/1678511003644934
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 柔灵科技 3D 互动式肌电手环 / Rulink 3D Interactive EMG Wristband

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [柔灵科技 / Rulink](../../../appendices/appendix-d/companies/company_rulink.md) |
| **产品类别** | 柔性肌电/触觉传感器手环 |
| **发布时间** | 2022 年起持续迭代 |
| **状态** | 商用 |
| **官网/来源** | [柔灵科技 36Kr 项目页](https://pitchhub.36kr.com/project/1678511003644934) |

## 产品概述

柔灵科技 3D 互动式肌电手环是一款基于柔性电子皮肤的表面肌电（sEMG）传感设备。手环采用纳米金属颗粒柔性电极与轻量化设计，可贴合人体手臂皮肤，采集前臂肌电信号并通过 AI 算法解码手势与运动意图，实现与虚拟对象的无控制器交互。

该产品可与 AR 眼镜配合使用，使用户能够通过手势完成拿取、旋转、移动虚拟对象或菜单选择等操作。其柔性传感器技术同样适用于机器人遥操作与人形机器人末端力/意图感知，是电子皮肤与神经交互领域的代表性产品。

## 产品图片

> Rulink EMG Wristband：请访问 [官方资料](https://pitchhub.36kr.com/project/1678511003644934) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感类型 | 柔性表面肌电（sEMG） | 公开报道 |
| 电极材料 | 新型纳米金属颗粒柔性电极 | 公开报道 |
| 感知维度 | 肌电信号、手势运动意图 | 公开报道 |
| 通道数 | 未公开 | - |
| 采样率 | 未公开 | - |
| 量程 | 未公开 | - |
| 响应时间 | 未公开 | - |
| 通信接口 | 未公开 | - |
| 供电方式 | 未公开 | - |
| 重量 | 未公开 | - |
| 续航 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[柔灵科技 / Rulink](../../../appendices/appendix-d/companies/company_rulink.md)
- **核心零部件/技术来源**：自研纳米金属颗粒柔性电极、AI 信号分离与解码算法；柔性基材、生物电前端芯片外购。
- **下游应用/客户**：AR/VR 设备、机器人遥操作、假肢控制、智能穿戴、医疗康复。

## 知识图谱节点与关系

- 产品实体：`ent_product_rulink_tactile_sensor`
- 制造商实体：`ent_company_rulink`
- 零部件实体：`ent_component_rulink_flexible_electrode`
- 关键关系：
  - `rel_ent_company_rulink_manufactures_ent_product_rulink_tactile_sensor`（`ent_company_rulink` → `manufactures` --> `ent_product_rulink_tactile_sensor`）
  - `rel_ent_company_rulink_manufactures_ent_component_rulink_flexible_electrode`（`ent_company_rulink` → `manufactures` --> `ent_component_rulink_flexible_electrode`）
  - `rel_ent_product_rulink_tactile_sensor_uses_ent_component_rulink_flexible_electrode`（`ent_product_rulink_tactile_sensor` → `uses` --> `ent_component_rulink_flexible_electrode`）

## 应用场景

- **AR/VR 交互**：无控制器手势识别与虚拟对象操控。
- **机器人遥操作**：通过肌电信号驱动机器人手臂或灵巧手完成模仿动作。
- **假肢控制**：为截肢患者提供自然的手势意图识别。
- **人形机器人电子皮肤**：作为柔性触觉/意图感知模组集成于机器人肢体。

## 竞争对比

| 对比项 | 柔灵肌电手环 | Meta 神经手环 | 能斯达柔性传感器 |
|--------|--------------|---------------|------------------|
| 传感原理 | 柔性 sEMG 电极 | 肌电 + 神经信号 | 柔性压阻/压电 |
| 形态 | 手环/表带 | 手环/手表 | 薄膜/贴片 |
| 交互能力 | 手势 + 3D 虚拟交互 | 手势/输入 | 压力/应变感知 |
| 核心优势 | 纳米柔性电极、轻便 | 生态整合 | 多品类柔性传感 |

## 选购与部署建议

- 部署前需确认电极与皮肤的贴合稳定性，建议配套固定带或弹性织物。
- 肌电信号受个体差异影响较大，需针对用户进行少量校准或迁移学习。

## 参考资料

1. [36Kr PitchHub – 柔灵科技项目信息](https://pitchhub.36kr.com/project/1678511003644934)
2. [DH Capital – 柔灵科技专访](https://www.dh-capital.cn/blog/7f0a7eeafb4)
3. [KEE Sleep – 柔灵科技创始人访谈](https://www.keesleep.com/news/info/3305.html)
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)