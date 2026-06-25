---
$id: ent_paper_mishra_does_elderly_enjoy_playing_bin_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Does Elderly Enjoy Playing Bingo with a Robot? A Case Study with the Humanoid
    Robot Nadine
  zh: 老年人是否喜欢与机器人玩宾果？——以人形机器人Nadine为例的案例研究
  ko: 노인은 로봇과 빙고를 즐기는가? 휴머노이드 로봇 Nadine을 활용한 사례 연구
summary:
  en: This paper reports a nursing-home deployment of the humanoid social robot Nadine
    as an autonomous Bingo host, using computer vision to show that elderly residents
    smiled more and staff activity decreased during robot-hosted sessions.
  zh: 本文报告了将人形社交机器人Nadine作为自主宾果游戏主持人部署在疗养院的案例，通过计算机视觉分析表明，在机器人主持的活动期间，老年居民笑得更多，工作人员活动减少。
  ko: 본 논문은 휴머노이드 사회적 로봇 Nadine을 자율적인 빙고 진행자로 양로원에 배치한 사례를 보고하며, 컴퓨터 비전을 통해 로봇이 진행하는
    세션 동안 노인 거주자들이 더 많이 웃고 종활동이 감소했음을 보여준다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and supplied metadata; requires human review against
    full paper before final verification.
sources:
- id: src_001
  type: paper
  title: Does elderly enjoy playing Bingo with a robot? A case study with the humanoid
    robot Nadine
  url: https://arxiv.org/abs/2105.01975
  date: '2021'
  accessed_at: '2026-06-26'
---


## Overview

The paper addresses the growing need for assistive technologies for aging populations by deploying the humanoid social robot Nadine as an autonomous Bingo activity host in a nursing home. The authors recorded 24 sessions hosted by Nadine and 2 sessions hosted by human caretakers, then applied deep-neural-network computer vision methods—including face detection, expression recognition, action detection, and optical flow—to quantify residents' happiness, movement, and staff activity. The study aims to determine whether elderly users feel comfortable with and enjoy interacting with a realistic humanoid robot during a structured recreational activity.

Nadine's Bingo-hosting module was developed and integrated with her affective engine and speech synthesis, which were adapted for elderly users. The robot autonomously managed the game flow using fabricated buzzers, a touch-screen controller, microphones, 3D cameras, web cameras, and a TV display. The vision-based analysis produced objective metrics comparing robot-hosted and caretaker-hosted sessions, with a focus on smiling frequency, resident movement, and care-staff movement as proxy indicators of enjoyment, engagement, and workload.

Results indicated positive effects during Nadine-hosted Bingo: residents smiled more and staff movement decreased, suggesting both user acceptance and a potential reduction in caretaker workload. The authors compare Nadine's humanoid capabilities with prior recreational robots for elderly care and argue that such humanoid robots can make recreational activities more readily available for older adults.

## Key Contributions

- Deployed the realistic humanoid social robot Nadine as an autonomous Bingo activity host in a nursing home.
- Developed a Bingo-hosting module and adapted Nadine's affective engine and speech synthesis for elderly users.
- Evaluated sessions objectively using DNN-based computer vision to measure residents' smiling, movement, and care-staff activity.
- Showed statistically that residents smiled more and staff moved less during Nadine-hosted Bingo, indicating acceptance and reduced workload.
- Compared Nadine's humanoid capabilities with prior recreational robots for elderly care.

## Relevance to Humanoid Robotics

This work is directly relevant to humanoid robotics because it demonstrates a real-world deployment of a realistic humanoid robot in an eldercare facility, focusing on user acceptance and practical utility rather than laboratory demonstration. The results suggest that humanoid form factors and social capabilities can help automate structured group activities for elderly users, potentially reducing caregiver burden while maintaining or improving participant engagement. For the humanoid-robot knowledge base, the paper provides evidence for the application-market potential of social humanoids in healthcare and assisted-living settings, as well as an evaluation methodology combining autonomous behavior generation with vision-based outcome metrics.
