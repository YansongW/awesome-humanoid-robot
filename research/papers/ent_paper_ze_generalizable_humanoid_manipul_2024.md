---
$id: ent_paper_ze_generalizable_humanoid_manipul_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalizable Humanoid Manipulation with 3D Diffusion Policies
  zh: 基于3D扩散策略的可泛化人形机器人操作
  ko: 3D 확산 정책을 이용한 일반화 가능한 휴머노이드 조작
summary:
  en: This paper presents a real-world imitation-learning system that enables a full-sized
    humanoid robot to perform Pick&Place, Pour, and Wipe skills in diverse unseen
    scenes using data collected in a single scene, combining whole-upper-body teleoperation,
    a 25-DoF GR1 platform with a height-adjustable cart and head-mounted LiDAR, and
    an improved egocentric 3D Diffusion Policy (iDP3) that runs entirely on onboard
    compute.
  zh: 本文提出了一个真实世界的模仿学习系统，使全尺寸人形机器人仅利用单一场景采集的数据，就能够在多种未见过场景中完成抓取放置、倾倒和擦拭任务；系统结合了上半身全身遥操作、带可调高度推车和头戴LiDAR的25自由度GR1平台，以及一种完全在机载计算上运行的改进型自我中心3D扩散策略（iDP3）。
  ko: 본 논문은 전신 상반신 원격조작, 높이 조절 가능한 카트와 머리 장착 LiDAR를 갖춘 25자유도 GR1 플랫폼, 그리고 온보드 컴퓨팅에서
    완전히 작동하는 개선된 자아중심 3D 확산 정책(iDP3)을 결합하여 단일 장면에서 수집한 데이터만으로 다양한 보지 못한 장면에서 픽앤플레이스,
    부으며, 닦기 기술을 수행할 수 있는 실제 모방 학습 시스템을 제시한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 09_data_datasets
- 10_evaluation_benchmarks
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- humanoid
- manipulation
- imitation_learning
- diffusion_policy
- 3d_vision
- egocentric_perception
- teleoperation
- visuomotor_policy
- scene_generalization
- dexterous_manipulation
- fourier_gr1
- apple_vision_pro
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from arXiv full text (v3, 2025-09-09); all claims traced to
    the paper, but numerical results and exact demonstration counts should be double-checked
    against the PDF tables before full verification.
sources:
- id: src_001
  type: paper
  title: Generalizable Humanoid Manipulation with 3D Diffusion Policies
  url: https://arxiv.org/abs/2410.10803
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Autonomous manipulation by full-sized humanoid robots has largely been confined to the scene in which the policy was trained. The authors attribute this limitation to the weak generalization of existing visuomotor methods and the high cost of collecting diverse, in-the-wild humanoid robot data. To address this, they build a complete real-world imitation-learning pipeline composed of a whole-upper-body teleoperation interface, a full-sized humanoid robot platform, and an improved 3D Diffusion Policy named iDP3.

The hardware platform is a Fourier GR1 humanoid robot with Inspire dexterous hands; the authors enable the upper body (head, waist, arms, and hands) totaling 25 degrees of freedom and fix the robot on a movable, height-adjustable cart in place of using the lower body. A head-mounted Intel RealSense L515 LiDAR camera supplies egocentric 3D point clouds. The teleoperation system uses an Apple Vision Pro to track the operator's head, waist, arms, and hands, maps these to the robot via inverse kinematics (RelaxedIK for the arms), and streams the robot's egocentric LiDAR view back to the operator for immersive feedback.

The learning algorithm, iDP3, reformulates the prior third-person 3D Diffusion Policy into an egocentric camera-frame representation, removing the need for camera calibration and point-cloud segmentation. It scales up the number of sampled 3D points, replaces the MLP encoder with a pyramid convolutional encoder, and lengthens the action prediction horizon to cope with noisy human demonstrations and sensor data. The trained policy runs at 15 Hz on the robot's onboard computer. Across more than 2,000 real-world evaluation rollouts, the system demonstrates that skills learned from data collected in only one scene can generalize to a variety of previously unseen indoor scenes.

## Key Contributions

- A real-world humanoid robot learning platform that combines a 25-DoF Fourier GR1 upper body, height-adjustable cart, and head-mounted Intel RealSense L515 LiDAR for egocentric 3D perception.
- A whole-upper-body teleoperation system using Apple Vision Pro that maps human head, waist, arm, and hand motion to the robot and streams egocentric LiDAR feedback to the operator.
- An improved 3D Diffusion Policy (iDP3) that operates on egocentric camera-frame point clouds, scales up vision input, uses a pyramid convolutional encoder, and employs a longer prediction horizon.
- Empirical demonstration that a full-sized humanoid robot can generalize Pick&Place, Pour, and Wipe skills to diverse unseen real-world scenes using training data from a single scene.
- More than 2,000 real-world policy rollouts providing rigorous evaluation of the system's effectiveness and generalization.

## Relevance to Humanoid Robotics

This work is highly relevant to humanoid robotics because it demonstrates an end-to-end pipeline that goes beyond hardware demonstration to produce generalizable autonomous manipulation on a full-sized humanoid robot. By tightly integrating teleoperation, a configurable robot platform, and a 3D visuomotor policy, the authors show that humanoid robots can acquire skills in one environment and deploy them in unstructured, previously unseen environments without recalibration or re-segmentation. This directly addresses one of the major bottlenecks in scaling humanoid robots beyond laboratories: data efficiency and real-world generalization. The identification of data scalability, sensor noise, and lower-body balance as remaining limitations also provides concrete directions for the humanoid-robot research community.
