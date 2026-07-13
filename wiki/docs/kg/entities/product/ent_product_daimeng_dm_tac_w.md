---
id: ent_product_daimeng_dm_tac_w
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 戴盟 DM-Tac W 视触觉传感器
  en: Daimeng DM-Tac W Vision-based Tactile Sensor
status: active
sources:
- id: src_daimeng_dm_tac_w_ithome
  type: website
  url: https://www.ithome.com/0/845/740.htm
- title: 戴盟机器人发布全球首款多维高分辨率高频率视触觉传感器 - IT之家
- id: src_daimeng_dm_tac_w_robot_china
  type: website
  url: https://www.robot-china.com/news/202504/17/92577.html
- title: 戴盟机器人发布全球首款多维高分辨率高频率视触觉传感器 - 中国机器人网
- id: src_daimeng_zhihu
  type: website
  url: https://zhuanlan.zhihu.com/p/1895159053673539398
- title: 戴盟机器人正式发布革命性家族产品 DM-Tac W、DM-Hand1、DM-EXton
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 戴盟 DM-Tac W 视触觉传感器 / Daimeng DM-Tac W Vision-based Tactile Sensor

## 概述

DM-Tac W 是戴盟机器人于 2025 年 4 月发布的全球首款多维高分辨率高频率视触觉传感器。该传感器将摄像头集成于传感器内部，当物体接触传感表面时，实时捕捉密闭光场中的形变特征，并结合原创解析算法解算光场变化，实现稳定、鲁棒的稠密触觉感知。

## 工作原理 / 技术架构

DM-Tac W 基于视觉-触觉融合原理：弹性体表层的几何形变由内置微型相机成像，通过追踪表面标记或纹理的位移场，利用光度立体或光流法反演出接触面的三维形貌与作用力分布。设接触面积为 \(A\)，法向力为 \(F_n\)，则接触压强

\[
p = \frac{F_n}{A}
\]

切向力 \(F_t\) 引起的剪切应力为

\[
\tau = \frac{F_t}{A}
\]

传感器每平方厘米覆盖约 \(4\times 10^4\) 个感知单元，对应空间节距约 \(50\,\mu\text{m}\)，远高于人类手指皮肤约 \(240\,/\text{cm}^2\) 的触觉密度。基于该超高密度阵列，DM-Tac W 可同时捕捉形貌、纹理、软硬、滑移、正压力与切向力等多模态信息。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 感知单元密度 | 约 \(4\times 10^4\,/\text{cm}^2\) |
| 可感知模态 | 形貌、纹理、软硬、滑移、正压力、切向力 |
| 传感器厚度（用于 DM-Hand1 的衍生版本） | 毫米级 |
| 外形尺寸 | 未公开 |
| 单点力量程 | 未公开 |
| 采样频率 | 未公开 |
| 通信接口 | 未公开 |

## 应用场景

- 机器人夹爪与灵巧手的触觉感知
- 易碎、易变形物体的柔顺抓取
- 精密零部件装配中的力/位混合控制
- 自适应抓握力调节与滑移检测
- 医疗手术与康复机器人末端感知

## 供应链关系

DM-Tac W 由戴盟机器人研发制造。上游包括微型相机模组、弹性体材料、LED/照明光源与嵌入式计算单元；中游为戴盟自研的光场解析算法与传感器结构；下游集成于戴盟 DM-Hand1 五指灵巧手，也可适配第三方夹爪与末端执行器。戴盟同期发布的 DM-EXton 为穿戴式遥操作数据采集系统，与 DM-Tac W、DM-Hand1 共同构成“感知-操作-学习”产品家族。

## 来源与验证

核心参数与工作原理来自 IT之家、中国机器人网及戴盟官方发布资料。传感器外形尺寸、力量程、采样频率、通信接口等细节未公开披露，标注为“未公开”。