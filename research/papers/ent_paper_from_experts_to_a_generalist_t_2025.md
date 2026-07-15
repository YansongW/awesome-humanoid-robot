---
$id: ent_paper_from_experts_to_a_generalist_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots'
  zh: 从专家到通用：走向人形机器人的通用全身控制
  ko: 'From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots'
summary:
  en: This work transforms camera images/multi-view observations, proprioceptive states and joint sequences, and simulated
    interaction data into trackable body objects, which can be used to track the body, and through the World Model/video prediction,
    the whole-body Controller/WBC/MPC training or the combination of whole-body strategies, the final output is the whole-body
    trajectory/action sequence and the low-level controller target. The key is to put the world model/video prediction, whole
    body controller/WBC/MPC in the same training/deployment link, reducing the discontinuity between high-level targets and
    low-level actions.
  zh: 这篇工作把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过世界模型/视频预测、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把世界模型/视频预测、全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
  ko: 这篇工作把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过世界模型/视频预测、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把世界模型/视频预测、全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- balance
- behavioral_foundation_model
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (028). Institution: Peking University. Full title: From Experts to a Generalist:
    Toward General Whole-Body Control for Humanoid Robots. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: 从专家到通用：走向人形机器人的通用全身控制 project page
  url: https://beingbeyond.github.io/BumbleBee/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
这篇工作把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过世界模型/视频预测、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把世界模型/视频预测、全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

## 개요
这篇工作把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过世界模型/视频预测、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把世界模型/视频预测、全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

