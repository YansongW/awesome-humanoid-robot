---
$id: ent_paper_peng_aheadance_anticipatory_humanoi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AHEADance: Anticipatory Humanoid Dance from Streaming Audio'
  zh: 'AHEADance: Anticipatory Humanoid Dance from Streaming Audio'
  ko: 'AHEADance: Anticipatory Humanoid Dance from Streaming Audio'
summary:
  en: A humanoid that dances to streamed music must commit each motion chunk before it has heard the music that chunk accompanies,
    and must continue from motion it has already committed. We present AHEADance, a robot-native streaming dance generator
    executed on a humanoid robot by a whole-body tracker. ListenAhead conditions each chunk on heard music and a frozen music
    model's forecasts of the coming ...
  zh: AHEADance 是一种面向人形机器人的流式舞蹈生成器，由 Tianhu Peng、Yukun Wang、Lingfan Bao、Yiyang Jia、Chengxu Zhou 提出，并在 Unitree G1 实体机器人上通过全身跟踪器执行。其核心是
    ListenAhead 机制：以已听到的音乐和冻结音乐模型对后续音乐的预测为条件生成动作块，并按目标时间对齐、按可靠性加权；配合 Commit Forcing 训练策略，使低活动比例从 83.5% 降至 10.3%。
  ko: A humanoid that dances to streamed music must commit each motion chunk before it has heard the music that chunk accompanies,
    and must continue from motion it has already committed. We present AHEADance, a robot-native streaming dance generator
    executed on a humanoid robot by a whole-body tracker. ListenAhead conditions each chunk on heard music and a frozen music
    model's forecasts of the coming ...
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
- humanoid_dance
- streaming_motion_generation
- music_conditioned_motion
- whole_body_tracking
- unitree_g1
- motion_synchronization
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.13370);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.13370 AHEADance: Anticipatory Humanoid Dance from Streaming Audio'
  url: https://arxiv.org/abs/2611.13370
  date: '2026-11-09'
  accessed_at: '2026-11-16'
---

## 概述

人形机器人随流式音乐跳舞时，必须在听到某段音乐之前就确定与之对应的动作块，并且要从已经承诺的动作继续下去。为此作者提出 AHEADance，一个机器人原生的流式舞蹈生成器，由全身跟踪器在人形机器人上执行。ListenAhead 让每个动作块同时以已听到的音乐和冻结音乐模型对即将到来音乐的预测为条件，预测按目标时间对齐并按可靠性加权。这些预测几乎能像真实未来一样携带即将到来的节拍时序，使生成器与音乐更同步，并把更多运动能量集中在歌曲的节拍频率上。Commit Forcing 则训练模型从自身已承诺的动作块继续生成，同时更新潜在历史与下一动作块的解码边界，将低活动比例从 83.5% 降至 10.3%，接近真实舞蹈水平。三个音乐评估器分别在真实 G1 舞蹈上验证，用于测试同步性、歌曲与风格；在实体 Unitree G1 上，机器人随音乐起舞、音乐停止即静止，且未发生跌倒。

## 核心内容

### 问题背景
流式音乐驱动的人形舞蹈面临一个根本矛盾：机器人必须在听到某段音乐之前就提交与之配套的动作块，同时还要从已经提交的动作继续，保持动作的连贯性。这要求生成器既能预判未来音乐，又能稳定地自我延续。

### 方法
- **ListenAhead**：每个动作块的条件不仅包括已听到的音乐，还包括一个冻结音乐模型对即将到来音乐的预测；预测按目标时间对齐，并按可靠性加权。
- **Commit Forcing**：训练模型从自身已承诺的动作块继续生成，同时更新潜在历史与下一动作块的解码边界。
- **执行方式**：生成器为机器人原生设计，由全身跟踪器在人形机器人上执行。

### 实验设置与关键结果
- 预测几乎能像真实未来一样携带即将到来的节拍时序；借助预测，生成器与音乐更同步，并把更多运动能量集中在歌曲的节拍频率上。
- Commit Forcing 将低活动比例从 83.5% 降至 10.3%，达到真实舞蹈的水平。
- 三个音乐评估器分别在真实 G1 舞蹈上验证，用于测试同步性、歌曲与风格。
- 在实体 Unitree G1 上，机器人随音乐播放起舞，音乐停止时静止，且未发生跌倒。

### 结论
AHEADance 通过预测未来音乐与自我承诺延续两项机制，实现了流式条件下人形机器人的同步舞蹈生成，并在实体 Unitree G1 上验证了可行性与稳定性。

## Overview

A humanoid that dances to streamed music must commit each motion chunk before it has heard the music that chunk accompanies, and must continue from motion it has already committed. We present AHEADance, a robot-native streaming dance generator executed on a humanoid robot by a whole-body tracker. ListenAhead conditions each chunk on heard music and a frozen music model's forecasts of the coming music, aligned to their target times and weighted by reliability. The forecasts carry the timing of upcoming beats almost as well as the actual future; with them, the generator is better synchronized with the music and concentrates more motion energy at its song's beat frequency. Commit Forcing trains continuation from the model's own committed chunks, updating both the latent history and the decoded boundary of the next chunk; it reduces low activity from 83.5% to 10.3%, the level of real dance. Three music evaluators, each validated on real G1 dance, test synchronization, song and style. On a physical Unitree G1, it dances while the music plays and comes to rest when it stops, without a fall. Project page: https://ihcr.github.io/AHEADance

## 参考
- https://arxiv.org/abs/2611.13370
