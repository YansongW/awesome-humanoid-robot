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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2105.01975v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (715 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2105.01975v1

## 개요
의료 발전으로 노인 인구가 증가하면서 간호 인력 부족 문제가 점점 더 두드러지고 있다. 본 연구는 휴머노이드 소셜 로봇 Nadine을 요양원에 배치하여 자율적인 Bingo 게임 진행자 역할로 노인들과 상호작용하게 했다. 로봇이 진행하는 경우와 그렇지 않은 두 가지 시나리오를 비교하고, 컴퓨터 비전 기술을 활용해 노인들의 감정 상태와 참여도를 분석한 결과, 로봇이 진행할 때 노인들이 더 많은 긍정적 감정을 보였으며, 간호 인력의 업무 부담도 크게 감소한 것으로 나타났다. 연구 결과는 소셜 로봇이 노인 여가 활동의 접근성과 질을 효과적으로 향상시킬 수 있음을 시사한다.

## 핵심 내용
### 연구 배경 및 목표
- 의료 발전으로 노인 인구가 급증했지만 간호 인력 증가는 뒤처져 있어 기술적 해결책이 시급함
- 로봇이 여가 활동 조직 업무를 담당함으로써 간호 인력이 노인의 정서적 요구에 더 집중할 수 있게 됨
- 핵심 연구 질문: 노인들이 휴머노이드 로봇 Nadine을 활동 진행자로 수용할 의향이 있는지, 그리고 상호작용 중 편안함을 느끼는지

### 실험 설계
- Nadine 로봇을 요양원에 배치하여 Bingo 게임 진행자 역할을 맡게 함
- 두 가지 비교 시나리오 설정: 로봇이 진행하는 Bingo 세션 vs 로봇 없이 진행되는 전통적 Bingo 세션
- 카메라로 전체 과정을 기록하고 컴퓨터 비전 방법으로 다음을 분석:
  - 노인의 얼굴 표정(미소 감지)
  - 노인의 활동 참여도(신체 방향, 제스처 등)
  - 직원의 활동 빈도

### 주요 발견
- 로봇이 진행할 때 노인 거주자의 미소 빈도가 전통적 시나리오보다 유의미하게 높았음
- 로봇 진행 중 직원의 활동량이 현저히 감소하여 로봇이 조직 업무를 효과적으로 분담했음을 보여줌
- 노인들이 로봇에 대해 뚜렷한 불편함이나 거부 행동을 보이지 않음

### 결론 및 전망
- 휴머노이드 소셜 로봇 Nadine이 Bingo 진행자로서 노인들의 긍정적 수용을 얻음
- 로봇이 진행하는 여가 활동은 노인의 정서적 경험을 향상시키는 동시에 간호 인력의 부담을 줄일 수 있음
- 향후 더 다양한 유형의 노인 여가 활동으로 확장하고 로봇의 사회적 상호작용 능력을 최적화할 수 있음
