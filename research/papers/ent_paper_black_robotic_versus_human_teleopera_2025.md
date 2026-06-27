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
  en: Presents a within-subjects comparison of robotic (Franka Panda) and human (mixed-reality
    HoloLens 2 follower) teleoperation for remote diagnostic ultrasound on a phantom,
    reporting statistically equivalent completion time and image-space tracking accuracy,
    but more consistent and lower applied force for human teleoperation.
  zh: 本文在超声体模上对比了机器人（Franka Panda）与人类（混合现实HoloLens 2跟随者）远程超声遥操作系统，报告两者在完成时间和图像空间跟踪精度上无显著差异，而人类遥操作的施力更加一致且幅度更低。
  ko: 본 논문은 팬텀을 대상으로 로봇(Franka Panda)과 인간(혼합현실 HoloLens 2 추종자) 원격 초음파 원격조작을 비교하여,
    완료 시간과 영상 공간 추적 정확도에서 통계적으로 유의한 차이가 없으나 인간 원격조작이 더 일관되고 낮은 힘을 가함을 보고한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv full text (v1, 2025-11-10); requires human review
    before verification.
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

## Overview

Diagnostic ultrasound is safe and inexpensive, but expert sonographers are concentrated in larger cities, leaving rural populations with long waits and costly travel. Tele-ultrasound can bridge this gap through either robotic teleoperation or, more recently, human teleoperation, in which a novice follower tracks a virtual probe shown in mixed reality. The two paradigms had not been directly compared, making it unclear whether the lower-cost human approach could match robotic performance.

The authors built analogous robotic and human teleoperation systems that shared the same expert haptic interface and WebRTC communication layer. The robotic follower was a Franka Panda arm with an impedance controller holding a BK Medical linear transducer; the human follower wore a HoloLens 2 headset and aligned a real probe with a virtual one. A within-subjects experiment on a Blue Phantom branched 2-vessel training block compared human teleoperation, robotic teleoperation, and direct scanning using completion time, image-space tracking error, and force consistency metrics.

Overall completion time differed by only 1.8% between human and robotic teleoperation and showed no statistical significance. Image-space root-mean-square tracking error differed by 0.5% and likewise showed no practical difference. However, force application—measured by vessel eccentricity—was significantly more consistent and lower in amplitude for human teleoperation than for the impedance-controlled robot, and direct scanning outperformed both on speed and force.

## Key Contributions

- First direct experimental comparison of robotic and human teleoperation for remote ultrasound.
- Demonstrated that human teleoperation achieves statistically equivalent completion time and image-space tracking accuracy to robotic teleoperation.
- Showed that human teleoperation produces more consistent and lower applied force than the impedance-controlled robot.
- Quantified practical differences in setup time, cost, portability, and calibration burden favoring human teleoperation.
- Validated the human-as-follower paradigm as a viable lower-complexity alternative to telerobotic ultrasound.

## Relevance to Humanoid Robotics

Although the paper studies ultrasound rather than humanoid robots, it is a directly relevant case study in human-in-the-loop teleoperation. Replacing a fixed robot with a human follower creates a flexible, low-cost, rapidly deployable telepresence actuator, an architecture that can inform humanoid remote-operation systems in mass-deployment or telepresence scenarios. The results suggest that, when a task can be decomposed into tracked end-effector motions and force guidance, a human surrogate may match or exceed a conventional robot on key performance metrics while remaining more practical.
