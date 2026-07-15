---
$id: ent_paper_a_mobile_robot_hand_arm_teleop_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Mobile Robot Hand-Arm Teleoperation System by Vision and IMU
  zh: A Mobile Robot Hand-Arm Teleoperation System by Vision and IMU
  ko: A Mobile Robot Hand-Arm Teleoperation System by Vision and IMU
summary:
  en: A Mobile Robot Hand-Arm Teleoperation System by Vision and IMU is a 2020 work on teleoperation for humanoid robots,
    with open-source code available.
  zh: A Mobile Robot Hand-Arm Teleoperation System by Vision and IMU is a 2020 work on teleoperation for humanoid robots,
    with open-source code available.
  ko: A Mobile Robot Hand-Arm Teleoperation System by Vision and IMU is a 2020 work on teleoperation for humanoid robots,
    with open-source code available.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_mobile_robot_hand_arm_teleop
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.05212v1.
sources:
- id: src_001
  type: website
  title: A Mobile Robot Hand-Arm Teleoperation System by Vision and IMU project page
  url: https://smilels.github.io/multimodal-translation-teleop/
  date: '2020'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we present a multimodal mobile teleoperation system that consists of a novel vision-based hand pose regression network (Transteleop) and an IMU-based arm tracking method. Transteleop observes the human hand through a low-cost depth camera and generates not only joint angles but also depth images of paired robot hand poses through an image-to-image translation process. A keypoint-based reconstruction loss explores the resemblance in appearance and anatomy between human and robotic hands and enriches the local features of reconstructed images. A wearable camera holder enables simultaneous hand-arm control and facilitates the mobility of the whole teleoperation system. Network evaluation results on a test dataset and a variety of complex manipulation tasks that go beyond simple pick-and-place operations show the efficiency and stability of our multimodal teleoperation system.

## 核心内容
In this paper, we present a multimodal mobile teleoperation system that consists of a novel vision-based hand pose regression network (Transteleop) and an IMU-based arm tracking method. Transteleop observes the human hand through a low-cost depth camera and generates not only joint angles but also depth images of paired robot hand poses through an image-to-image translation process. A keypoint-based reconstruction loss explores the resemblance in appearance and anatomy between human and robotic hands and enriches the local features of reconstructed images. A wearable camera holder enables simultaneous hand-arm control and facilitates the mobility of the whole teleoperation system. Network evaluation results on a test dataset and a variety of complex manipulation tasks that go beyond simple pick-and-place operations show the efficiency and stability of our multimodal teleoperation system.

## 参考
- http://arxiv.org/abs/2003.05212v1

