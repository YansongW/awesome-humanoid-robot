---
id: ent_component_rulink_flexible_electrode
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 柔灵科技纳米金属颗粒柔性电极
  en: Rulink Nanometal Flexible Electrode
status: active
sources:
- id: src_rulink_flexolink
  type: website
- title: Flexolink AI Official Website
  url: https://www.flexolinkai.com
- id: src_rulink_36kr
  type: website
- title: 36Kr PitchHub – 柔灵科技项目信息
  url: https://pitchhub.36kr.com/project/1678511003644934
- id: src_rulink_sina
  type: website
- title: 新浪财经 – 柔灵科技纳米金属颗粒柔性电极报道
  url: https://finance.sina.com.cn/tech/roll/2023-03-25/doc-imymzwik2697598.shtml
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Only material-level and product-application information is publicly
    available; device-level specifications marked as 未公开.
---


# 柔灵科技纳米金属颗粒柔性电极 / Rulink Nanometal Flexible Electrode

## 概述

柔灵科技（Rulink / Flexolink AI）纳米金属颗粒柔性电极是一种以纳米金属颗粒为导电填料、柔性聚合物为基底的干式柔性电极材料。该电极面向非侵入式脑机接口（BCI）、表面肌电（sEMG）信号采集与机器人电子皮肤等应用，强调与皮肤共形贴合、低运动伪影与长期佩戴舒适性。它是柔灵 Airdream 额贴式脑电睡眠贴片、3D 互动式肌电手环等产品的核心传感界面。

## 工作原理 / 技术架构

柔性电极通过将纳米金属颗粒均匀铺设于柔性高分子基底上，形成导电逾渗网络。当金属颗粒体积分数 $p$ 超过逾渗阈值 $p_c$ 时，颗粒间形成连续导电通路，电极 sheet resistance 显著下降。逾渗导电行为常用幂律描述：

$$
\sigma \propto (p - p_c)^t
$$

其中 $\sigma$ 为电导率，$t$ 为逾渗指数。纳米级颗粒尺寸可在保证柔性的同时提高颗粒分布密度，降低皮肤–电极接触阻抗。

在信号采集应用中，皮肤–电极界面阻抗 $Z$ 与接触面积 $A$、材料电导率及频率有关：

$$
Z \approx \frac{\rho \cdot d}{A}
$$

其中 $\rho$ 为等效电阻率，$d$ 为导电层有效厚度。柔灵官方报道指出，通过颗粒尺寸与铺设工艺优化，可在柔性与导电性之间取得平衡，但未公开具体阻抗数值。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 电极材料 | 纳米金属颗粒 + 柔性聚合物基底 | 柔灵科技公开报道 |
| 产品形态 | 柔性贴片 / 电子皮肤 / 肌电手环电极 | 柔灵科技公开报道 |
| 最小可感知力（配合灵巧手/肌电手环） | 0.1 N | IT之家/天极网报道 |
| 应用设备重量（Airdream 单通道） | 4 g | 36Kr / 新浪财经报道 |
| 监测精度（Airdream 睡眠监测） | 医疗级 93% / 家居级 86–87% | 柔灵科技公开报道 |
| 认证状态 | Airdream 已取得中国 NMPA 医疗器械注册证 | 柔灵科技公开报道 |
| 皮肤–电极阻抗 | 未公开 | - |
| 通道数 | 未公开 | - |
| 采样率 | 未公开 | - |
| 拉伸/弯折循环寿命 | 未公开 | - |
| 电极尺寸 | 未公开 | - |

## 应用场景

- **非侵入式脑机接口**：用于额贴式睡眠监测、注意力/疲劳检测。
- **表面肌电手势识别**：集成于 3D 互动式肌电手环，实现 AR/VR 手势交互与机器人遥操作。
- **机器人电子皮肤**：为人形机器人提供触觉与压力感知界面。
- **医疗健康与康养**：长期生理信号监测、智慧养老设备。

## 供应链关系

- **上游**：纳米金属颗粒、柔性聚合物（PDMS/PI 等）、低噪声生物电前端芯片、封装材料。
- **制造商**：`ent_company_rulink` -- `manufactures` --> `ent_component_rulink_flexible_electrode`。
- **下游产品**：柔灵 Airdream 睡眠贴片、肌电手环、电子皮肤模组；机器人厂商与医疗设备商。
- **竞争对手/对标**：Neuralink（侵入式）、Meta 神经手环、Interlink Electronics、能斯达电子皮肤。

## 来源与验证

1. Flexolink AI 官网：https://www.flexolinkai.com
2. 36Kr PitchHub 项目页：https://pitchhub.36kr.com/project/1678511003644934
3. 新浪财经报道：https://finance.sina.com.cn/tech/roll/2023-03-25/doc-imymzwik2697598.shtml
4. 中国日报/生辉等公开报道

> 注：纳米金属颗粒柔性电极的材料电导率、皮肤–电极阻抗、通道数、采样率等器件级参数未在官方公开资料中披露，已标注为“未公开”。