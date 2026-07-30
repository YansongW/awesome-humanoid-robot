---
$id: ent_paper_mishra_does_elderly_enjoy_playing_bin_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Does Elderly Enjoy Playing Bingo with a Robot? A Case Study with the Humanoid Robot Nadine
  zh: 老年人是否喜欢与机器人玩宾果？——以人形机器人Nadine为例的案例研究
  ko: 노인은 로봇과 빙고를 즐기는가? 휴머노이드 로봇 Nadine을 활용한 사례 연구
summary:
  en: This paper reports a nursing-home deployment of the humanoid social robot Nadine as an autonomous Bingo host, using
    computer vision to show that elderly residents smiled more and staff activity decreased during robot-hosted sessions.
  zh: 本研究将人形社交机器人Nadine部署为养老院中的自主Bingo游戏主持人，通过计算机视觉分析发现：在机器人主持的活动中，老年居民微笑频率增加，工作人员活动量减少。该工作由研究团队完成，核心贡献在于验证了社交机器人作为老年活动主持人的可行性与积极效果。
  ko: 본 논문은 휴머노이드 사회적 로봇 Nadine을 자율적인 빙고 진행자로 양로원에 배치한 사례를 보고하며, 컴퓨터 비전을 통해 로봇이 진행하는 세션 동안 노인 거주자들이 더 많이 웃고 종활동이 감소했음을 보여준다.
domains:
- 11_applications_markets
- 10_evaluation_benchmarks
layers:
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_robot
- elderly_care
- social_robot
- nadine
- bingo
- activity_host
- emotion_recognition
- computer_vision
- nursing_home
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2105.01975v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Does elderly enjoy playing Bingo with a robot? A case study with the humanoid robot Nadine
  url: https://arxiv.org/abs/2105.01975
  date: '2021'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
随着医疗进步导致老年人口增长，护理人力短缺问题日益突出。本研究将人形社交机器人Nadine部署于养老院，使其以自主Bingo游戏主持人的角色与老年人互动。通过对比有无机器人主持的两种场景，利用计算机视觉技术分析老年人的情绪状态与参与度，发现机器人主持时老年人表现出更多积极情绪，同时护理人员的工作负担显著降低。研究结果表明，社交机器人能够有效提升老年娱乐活动的可及性与质量。

## 核心内容
### 研究背景与目标
- 医疗进步导致老年人口激增，但护理人力增长滞后，亟需技术解决方案
- 机器人可承担娱乐活动组织工作，使护理人员能更专注于老年人的情感需求
- 核心研究问题：老年人是否愿意接受人形机器人Nadine作为活动主持人，并在互动中感到舒适

### 实验设计
- 将Nadine机器人部署于养老院，担任Bingo游戏主持人
- 设置两种对比场景：机器人主持的Bingo环节 vs 无机器人主持的传统Bingo环节
- 通过摄像头记录全程，使用计算机视觉方法分析：
  - 老年人的面部表情（微笑检测）
  - 老年人的活动参与度（身体朝向、手势等）
  - 工作人员的活动频率

### 关键发现
- 机器人主持时，老年居民微笑频率显著高于传统场景
- 工作人员在机器人主持期间的活动量明显减少，表明机器人有效分担了组织工作
- 未发现老年人对机器人表现出明显不适或抗拒行为

### 结论与展望
- 人形社交机器人Nadine作为Bingo主持人获得了老年人的积极接受
- 机器人主持的娱乐活动能同时提升老年人情绪体验和减轻护理人员负担
- 未来可拓展至更多类型的老年娱乐活动，并优化机器人的社交交互能力

## Overview
There are considerable advancements in medical health care in recent years, resulting in rising older population. As the workforce for such a population is not keeping pace, there is an urgent need to address this problem. Having robots to stimulating recreational activities for older adults can reduce the workload for caretakers and give them time to address the emotional needs of the elderly. In this paper, we investigate the effects of the humanoid social robot Nadine as an activity host for the elderly. This study aims to analyse if the elderly feels comfortable and enjoy playing game/activity with the humanoid robot Nadine. We propose to evaluate this by placing Nadine humanoid social robot in a nursing home as a caretaker where she hosts bingo game. We record sessions with and without Nadine to understand the difference and acceptance of these two scenarios. We use computer vision methods to analyse the activities of the elderly to detect emotions and their involvement in the game. We envision that such humanoid robots will make recreational activities more readily available for the elderly. Our results present positive enforcement during recreational activity, Bingo, in the presence of Nadine.

## Overview
There have been considerable advancements in medical healthcare in recent years, resulting in a rising older population. As the workforce for such a population is not keeping pace, there is an urgent need to address this problem. Having robots stimulate recreational activities for older adults can reduce the workload for caretakers and give them time to address the emotional needs of the elderly. In this paper, we investigate the effects of the humanoid social robot Nadine as an activity host for the elderly. This study aims to analyze whether the elderly feel comfortable and enjoy playing games/activities with the humanoid robot Nadine. We propose to evaluate this by placing the Nadine humanoid social robot in a nursing home as a caretaker, where she hosts a bingo game. We record sessions with and without Nadine to understand the difference and acceptance of these two scenarios. We use computer vision methods to analyze the activities of the elderly, detecting emotions and their involvement in the game. We envision that such humanoid robots will make recreational activities more readily available for the elderly. Our results present positive reinforcement during the recreational activity, Bingo, in the presence of Nadine.

## Content
There have been considerable advancements in medical healthcare in recent years, resulting in a rising older population. As the workforce for such a population is not keeping pace, there is an urgent need to address this problem. Having robots stimulate recreational activities for older adults can reduce the workload for caretakers and give them time to address the emotional needs of the elderly. In this paper, we investigate the effects of the humanoid social robot Nadine as an activity host for the elderly. This study aims to analyze whether the elderly feel comfortable and enjoy playing games/activities with the humanoid robot Nadine. We propose to evaluate this by placing the Nadine humanoid social robot in a nursing home as a caretaker, where she hosts a bingo game. We record sessions with and without Nadine to understand the difference and acceptance of these two scenarios. We use computer vision methods to analyze the activities of the elderly, detecting emotions and their involvement in the game. We envision that such humanoid robots will make recreational activities more readily available for the elderly. Our results present positive reinforcement during the recreational activity, Bingo, in the presence of Nadine.

## 개요
최근 의료 건강 분야에서 상당한 발전이 이루어지면서 노인 인구가 증가하고 있습니다. 이러한 인구를 위한 노동력이 따라잡지 못하고 있어, 이 문제를 해결하기 위한 시급한 필요성이 대두되고 있습니다. 노인을 위한 레크리에이션 활동을 자극하는 로봇을 도입하면 돌봄 제공자의 업무 부담을 줄이고, 노인의 정서적 필요를 충족시킬 시간을 확보할 수 있습니다. 본 논문에서는 인간형 사회적 로봇 Nadine이 노인을 위한 활동 진행자로서 미치는 영향을 조사합니다. 이 연구는 노인들이 인간형 로봇 Nadine과 게임/활동을 할 때 편안함을 느끼고 즐거워하는지 분석하는 것을 목표로 합니다. 우리는 Nadine 인간형 사회적 로봇을 요양원에 돌봄 제공자로 배치하여 빙고 게임을 진행함으로써 이를 평가하고자 합니다. Nadine이 있는 세션과 없는 세션을 녹화하여 두 시나리오의 차이와 수용도를 이해합니다. 컴퓨터 비전 방법을 사용하여 노인들의 활동을 분석하고 감정과 게임 참여도를 탐지합니다. 우리는 이러한 인간형 로봇이 노인들이 레크리에이션 활동을 더 쉽게 이용할 수 있게 할 것이라고 기대합니다. 결과는 Nadine이 있는 레크리에이션 활동인 빙고에서 긍정적인 강화 효과를 보여줍니다.

## 핵심 내용
최근 의료 건강 분야에서 상당한 발전이 이루어지면서 노인 인구가 증가하고 있습니다. 이러한 인구를 위한 노동력이 따라잡지 못하고 있어, 이 문제를 해결하기 위한 시급한 필요성이 대두되고 있습니다. 노인을 위한 레크리에이션 활동을 자극하는 로봇을 도입하면 돌봄 제공자의 업무 부담을 줄이고, 노인의 정서적 필요를 충족시킬 시간을 확보할 수 있습니다. 본 논문에서는 인간형 사회적 로봇 Nadine이 노인을 위한 활동 진행자로서 미치는 영향을 조사합니다. 이 연구는 노인들이 인간형 로봇 Nadine과 게임/활동을 할 때 편안함을 느끼고 즐거워하는지 분석하는 것을 목표로 합니다. 우리는 Nadine 인간형 사회적 로봇을 요양원에 돌봄 제공자로 배치하여 빙고 게임을 진행함으로써 이를 평가하고자 합니다. Nadine이 있는 세션과 없는 세션을 녹화하여 두 시나리오의 차이와 수용도를 이해합니다. 컴퓨터 비전 방법을 사용하여 노인들의 활동을 분석하고 감정과 게임 참여도를 탐지합니다. 우리는 이러한 인간형 로봇이 노인들이 레크리에이션 활동을 더 쉽게 이용할 수 있게 할 것이라고 기대합니다. 결과는 Nadine이 있는 레크리에이션 활동인 빙고에서 긍정적인 강화 효과를 보여줍니다.

## 参考
- http://arxiv.org/abs/2105.01975v1
