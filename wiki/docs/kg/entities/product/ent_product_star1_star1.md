---
id: ent_product_star1_star1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 星动纪元 STAR1 高性能通用人形机器人
  en: Star1 STAR1 Humanoid Robot
status: active
sources:
- id: src_star1_robotsj
  type: article
  url: http://www.robotsj.cn/service/578.html
- title: 星动纪元 STAR1 高性能通用人形机器人
- id: src_star1_ithome
  type: article
  url: https://www.ithome.com/0/790/117.htm
- title: 星动纪元发布 STAR1：最大负载 160kg
- id: src_star1_official
  type: website
  url: https://www.robotera.com
- title: 星动纪元官网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 星动纪元 STAR1 / Star1 STAR1

## 概述

星动纪元 STAR1 是北京星动纪元科技有限公司于 2024 年 8 月发布的首款产品级高性能通用人形机器人，由清华大学交叉信息研究院孵化。STAR1 身高 171 cm、体重 63 kg，全身 55 个主动自由度，最高关节扭矩 400 N·m，最高转速 25 rad/s，室外真实场景奔跑速度达 3.6 m/s，整机最大负载 160 kg。STAR1 配备自研端到端原生机器人大模型 ERA-42 与 12 主动自由度五指灵巧手 XHAND1，强调高动态运动与精细操作的结合。

## 工作原理 / 技术架构

STAR1 采用软硬一体、为 AI 定义的硬件平台：

1. **全身运动**：双腿 12 自由度、双臂 14 自由度、腰部 3 自由度、颈部 2 自由度，共 55 主动自由度；自研一体化关节集成无框力矩电机、行星减速器、编码器与驱动器。
2. **高动态驱动**：最高关节扭矩 400 N·m、最高转速 25 rad/s，使机器人具备高爆发力短跑与复杂地形奔跑能力。
3. **灵巧操作**：XHAND1 单手 12 主动自由度，指尖阵列触觉全覆盖，单手抓握负载超过 25 kg。
4. **具身智能**：原生机器人大模型 ERA-42 融合世界模型，实现端到端泛化行走与操作；结合强化学习与模仿学习，使机器人能够在未建模环境中自适应。
5. **算力平台**：集成 Intel 高性能处理器与 NVIDIA Orin 计算资源，算力 275 TOPS。

关节功率可表示为

$$
P=\tau\,\omega,
$$

其中 $\tau=400\ \text{N·m}$、$\omega=25\ \text{rad/s}$ 对应关节瞬时机械功率可达 10 kW 量级，体现了 STAR1 的高动态设计取向。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 身高 | 171 cm |
| 体重 | 63 kg |
| 全身自由度 | 55（全主动） |
| 端侧算力 | 275 TOPS |
| 最高关节扭矩 | 400 N·m |
| 最高关节转速 | 25 rad/s |
| 室外奔跑速度 | 3.6 m/s |
| 整机最大负载 | 160 kg |
| 手臂负载 | ＞20 kg |
| 灵巧手 | XHAND1，单手 12 主动自由度，抓握＞25 kg |
| 双腿 / 双臂自由度 | 12 / 14 |
| 腰 / 颈自由度 | 3 / 2 |
| 传感器 | 指尖阵列触觉、深度相机、麦克风阵列、面部交互屏 |

## 应用场景

- **科研教育**：强化学习、模仿学习、端到端大模型研究平台。
- **工业搬运**：重载搬运、产线上下料、零件转运。
- **家庭服务**：清洁、整理、养老陪护。
- **商业服务**：迎宾导览、演艺展览、点餐送餐。
- **特种作业**：复杂地形巡检、应急救援。

## 供应链关系

- **上游**：自研一体化关节、XHAND1 灵巧手；外部供应 Intel/NVIDIA 计算平台、深度相机、触觉传感器、电池与结构材料。
- **同层**：星动纪元作为整机与算法开发商，提供 STAR1 机器人、ERA-42 大模型与遥操作系统。
- **下游**：科研机构、工业客户、商业服务运营商与家庭用户。

## 来源与验证

- 机器人世界 STAR1 参数页：http://www.robotsj.cn/service/578.html
- IT之家发布报道：https://www.ithome.com/0/790/117.htm
- 星动纪元官网：https://www.robotera.com