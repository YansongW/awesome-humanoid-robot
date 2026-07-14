---
$id: ent_paper_black_robotic_versus_human_teleopera_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic versus Human Teleoperation for Remote Ultrasound
  zh: 远程超声的机器人与人类遥操作对比
  ko: 원격 초음파를 위한 로봇 대 인간 원격조작 비교
summary:
  en: Presents a within-subjects comparison of robotic (Franka Panda) and human (mixed-reality HoloLens 2 follower) teleoperation
    for remote diagnostic ultrasound on a phantom, reporting statistically equivalent completion time and image-space tracking
    accuracy, but more consistent and lower applied force for human teleoperation.
  zh: 本文在超声体模上对比了机器人（Franka Panda）与人类（混合现实HoloLens 2跟随者）远程超声遥操作系统，报告两者在完成时间和图像空间跟踪精度上无显著差异，而人类遥操作的施力更加一致且幅度更低。
  ko: 본 논문은 팬텀을 대상으로 로봇(Franka Panda)과 인간(혼합현실 HoloLens 2 추종자) 원격 초음파 원격조작을 비교하여, 완료 시간과 영상 공간 추적 정확도에서 통계적으로 유의한 차이가 없으나
    인간 원격조작이 더 일관되고 낮은 힘을 가함을 보고한다.
domains:
- 11_applications_markets
- 06_design_engineering
- 08_software_middleware
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- teleoperation
- remote_ultrasound
- tele_ultrasound
- human_teleoperation
- robotic_teleoperation
- mixed_reality
- haptic_feedback
- human_in_the_loop
- franka_panda
- hololens_2
- web_rtc
- telepresence
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07275v1.
sources:
- id: src_001
  type: paper
  title: Robotic versus Human Teleoperation for Remote Ultrasound
  url: https://arxiv.org/abs/2511.07275
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
- system
---
## 概述
Diagnostic medical ultrasound is widely used, safe, and relatively low cost but requires a high degree of expertise to acquire and interpret the images. Personnel with this expertise are often not available outside of larger cities, leading to difficult, costly travel and long wait times for rural populations. To address this issue, tele-ultrasound techniques are being developed, including robotic teleoperation and recently human teleoperation, in which a novice user is remotely guided in a hand-over-hand manner through mixed reality to perform an ultrasound exam. These methods have not been compared, and their relative strengths are unknown. Human teleoperation may be more practical than robotics for small communities due to its lower cost and complexity, but this is only relevant if the performance is comparable. This paper therefore evaluates the differences between human and robotic teleoperation, examining practical aspects such as setup time and flexibility and experimentally comparing performance metrics such as completion time, position tracking, and force consistency. It is found that human teleoperation does not lead to statistically significant differences in completion time or position accuracy, with mean differences of 1.8% and 0.5%, respectively, and provides more consistent force application despite being substantially more practical and accessible.

## 核心内容
Diagnostic medical ultrasound is widely used, safe, and relatively low cost but requires a high degree of expertise to acquire and interpret the images. Personnel with this expertise are often not available outside of larger cities, leading to difficult, costly travel and long wait times for rural populations. To address this issue, tele-ultrasound techniques are being developed, including robotic teleoperation and recently human teleoperation, in which a novice user is remotely guided in a hand-over-hand manner through mixed reality to perform an ultrasound exam. These methods have not been compared, and their relative strengths are unknown. Human teleoperation may be more practical than robotics for small communities due to its lower cost and complexity, but this is only relevant if the performance is comparable. This paper therefore evaluates the differences between human and robotic teleoperation, examining practical aspects such as setup time and flexibility and experimentally comparing performance metrics such as completion time, position tracking, and force consistency. It is found that human teleoperation does not lead to statistically significant differences in completion time or position accuracy, with mean differences of 1.8% and 0.5%, respectively, and provides more consistent force application despite being substantially more practical and accessible.

## 参考
- http://arxiv.org/abs/2511.07275v1

