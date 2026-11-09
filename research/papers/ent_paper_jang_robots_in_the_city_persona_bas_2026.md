---
$id: ent_paper_jang_robots_in_the_city_persona_bas_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robots in the City: Persona-Based Perceptions of Urban Robots'
  zh: 'Robots in the City: Persona-Based Perceptions of Urban Robots'
  ko: 'Robots in the City: Persona-Based Perceptions of Urban Robots'
summary:
  en: Pedestrians increasingly encounter robots in urban public spaces without interacting with them, but how robots change
    the perceived safety of a street remains unclear. We examine how robot presence and type affect perceived safety across
    urban contexts. We generate 18 images of Seoul streets that vary in time of day, road class, and robot condition (no robot,
    a delivery robot, or a humanoid). Two ...
  zh: 该研究考察城市街道中机器人的存在与类型如何影响行人的感知安全性，由 Keonhee Jang、Kanghoon Lee、Seokwoo Yun、Namwoo Kim 与 Yoonjin Yoon 完成。作者生成 18 张首尔街景图像，覆盖不同时段、道路等级与机器人条件（无机器人、配送机器人、人形机器人），并让两个多模态大模型
    Qwen3.8-27B 与 Gemma4-26B 分别在 500 个合成 persona 条件下进行成对选择，同时招募 25 名人类被试完成同一任务。结果显示模型与人类均更偏好无机器人街道，且更倾向配送机器人而非人形机器人，但模型在夜间效应与人形机器人偏好上与人类存在明显偏差。
  ko: Pedestrians increasingly encounter robots in urban public spaces without interacting with them, but how robots change
    the perceived safety of a street remains unclear. We examine how robot presence and type affect perceived safety across
    urban contexts. We generate 18 images of Seoul streets that vary in time of day, road class, and robot condition (no robot,
    a delivery robot, or a humanoid). Two ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- urban_robotics
- perceived_safety
- multimodal_large_language_models
- synthetic_personas
- humanoid_robots
- human_robot_interaction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.05954);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.05954 Robots in the City: Persona-Based Perceptions of Urban Robots'
  url: https://arxiv.org/abs/2611.05954
  date: '2026-11-04'
  accessed_at: '2026-11-09'
---

## 概述

研究关注行人在城市公共空间中即使不与机器人互动，机器人出现是否仍会改变街道的感知安全性。作者以首尔街道为场景，系统变化时段、道路等级和机器人条件，构建成对比较任务，并用 persona 条件化的多模态大模型模拟不同人群的判断，再与真实人类被试结果对照。两个模型都更偏好没有机器人的街道，并在配送机器人与人类形机器人之间更倾向后者之外的配送机器人；机器人被选择的比例在夜间更高，在年长 persona 中更低，道路等级影响相对较小。模型给出的理由中，配送机器人多被视为物理障碍，人形机器人则被视为威胁或保护来源。与人类相比，模型同样表现出夜间更接受机器人的倾向，但选择人形机器人而非配送机器人的比例远低于人类，Gemma 对人形机器人的夜间效应约为人类的三倍。

## 核心内容

### 问题背景
行人在城市公共空间中越来越常遇到机器人，但往往并不与其发生交互。机器人出现是否会改变街道的感知安全性，以及这种影响是否随时段、道路类型和机器人形态而变化，尚不清楚。作者据此设计研究，比较机器人存在与类型对感知安全的影响，并检验 persona 条件化的多模态大模型能否复现人类判断。

### 方法
- 场景构建：生成 18 张首尔街景图像，变化维度包括时段（含夜间）、道路等级与机器人条件（无机器人、配送机器人、人形机器人）。
- 模型被试：使用两个多模态大模型 Qwen3.8-27B 与 Gemma4-26B，各自以 500 个合成 persona 为条件。
- 任务：在每一对图像中选择感知更安全的一张。
- 人类对照：25 名人类被试完成同一成对选择任务。
- 分析：比较模型与人类的选择倾向，并检视模型给出的选择理由。

### 关键结果
- 两个模型均更偏好没有机器人的街道。
- 在机器人类型上，模型更偏好配送机器人而非人形机器人。
- 机器人被选择的比例在夜间更高，在年长 persona 中更低；道路等级的影响较小。
- 模型理由中，配送机器人常被描述为物理障碍，人形机器人则被描述为威胁或保护来源。
- 与人类一致，两个模型在夜间更常选择机器人；但模型选择人形机器人而非配送机器人的比例远低于人类。
- Gemma 对人形机器人的夜间效应约为人类的三倍。

### 结论
机器人对感知安全的影响取决于其出现的时间，夜间效应尤为突出。persona 条件化的多模态大模型只能捕捉人类判断的一部分，在机器人形态偏好与夜间效应强度上与人类存在系统性差异。

## Overview

Pedestrians increasingly encounter robots in urban public spaces without interacting with them, but how robots change the perceived safety of a street remains unclear. We examine how robot presence and type affect perceived safety across urban contexts. We generate 18 images of Seoul streets that vary in time of day, road class, and robot condition (no robot, a delivery robot, or a humanoid). Two multimodal large language models (MLLMs), Qwen3.8-27B and Gemma4-26B, each conditioned on 500 synthetic personas, choose the safer image in each pair, and 25 human respondents complete the same task. Both models prefer streets without robots and favor the delivery robot over the humanoid. Robots are chosen more often at night and less often by older personas, whereas road class has smaller effects. In the model rationales, the delivery robot appears as a physical obstacle, whereas the humanoid appears as either a threat or a source of protection. Like humans, both models chose robots more often at night, but chose the humanoid over the delivery robot far less often, and Gemma showed a night effect for the humanoid about three times that of humans. These results show that the effect of a robot on perceived safety depends on when it appears, and that persona-conditioned MLLMs capture only part of human judgments.

## 参考
- https://arxiv.org/abs/2611.05954
