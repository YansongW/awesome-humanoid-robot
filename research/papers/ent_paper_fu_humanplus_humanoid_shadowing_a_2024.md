---
$id: ent_paper_fu_humanplus_humanoid_shadowing_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanPlus: Humanoid Shadowing and Imitation from Humans'
  zh: HumanPlus：从人类进行人形机器人影子跟随与模仿
  ko: 'HumanPlus: 인간으로부터의 휴머노이드 섀도잉 및 모방'
summary:
  en: HumanPlus introduces a full-stack system that enables a 33-DoF 180 cm humanoid
    to shadow human body and hand motion in real time from a single RGB camera, and
    to learn autonomous vision-based manipulation and locomotion skills from as few
    as 40 collected demonstrations.
  zh: HumanPlus 提出了一套完整系统，使 33 自由度、180 cm 的人形机器人仅通过单目 RGB 相机实时跟随人体与手部动作，并利用多达 40 个采集示教学习基于自我中心视觉的自主操作与移动技能。
  ko: HumanPlus는 33-DoF, 180cm 휴머노이드가 단일 RGB 카메라로 인간의 신체 및 손 동작을 실시간 따라 하고, 수집된 최대
    40개의 시연으로부터 자기 중심 시각 기반의 자율 조작 및 이동 기술을 학습할 수 있는 전체 시스템을 제안한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_shadowing
- humanoid_imitation
- behavior_cloning
- sim_to_real
- reinforcement_learning
- whole_body_control
- dexterous_manipulation
- egocentric_vision
- transformer_policy
- human_motion_retargeting
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the paper PDF and abstract; hardware specs, success rates,
    and citation mapping require human review before verification.
sources:
- id: src_001
  type: paper
  title: 'HumanPlus: Humanoid Shadowing and Imitation from Humans'
  url: https://arxiv.org/abs/2406.10454
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Humanoids are appealing as general-purpose platforms because their human-like morphology lets them use environments and tools designed for people. HumanPlus addresses the practical challenge of turning large-scale human data into useful humanoid skills, despite high-dimensional perception and control, morphological mismatches, and the lack of a data pipeline for learning autonomous whole-body skills from egocentric vision. The paper presents a full-stack system instantiated on a customized 33-DoF, 180 cm humanoid built on the Unitree H1 robot with two 6-DoF Inspire-Robots RH56DFX dexterous hands and two head-mounted Razer Kiyo Pro RGB cameras.

The system first trains a low-level Humanoid Shadowing Transformer (HST) in simulation with proximal policy optimization (PPO) on roughly 40 hours of retargeted AMASS human motion. HST takes proprioception plus a retargeted humanoid target pose and outputs 19-dimensional body joint position setpoints at 50 Hz, which are tracked by a 1000 Hz PD controller. At runtime, a single RGB camera feeds World-Grounded Humans with Accurate Motion (WHAM) for body pose estimation and HaMeR for hand pose estimation; both estimators run on an NVIDIA RTX4090 GPU and retarget SMPL-X/MANO parameters to the robot. This lets a single human operator shadow whole-body motion in real time, while the robot collects binocular egocentric demonstrations.

Collected shadowing data are then used to train a decoder-only Humanoid Imitation Transformer (HIT) via supervised behavior cloning. HIT processes ResNet features from two egocentric RGB cameras, proprioception, and positional embeddings to predict a chunk of 50 target poses. An L2 feature loss on predicted future image features regularizes the policy with forward-dynamics information, discouraging neglect of visual input. HIT runs onboard at 25 Hz and sends target poses to HST asynchronously. The system demonstrates autonomous tasks including wearing a shoe and walking, unloading objects from warehouse racks, folding a sweatshirt, rearranging objects, typing "AI", and greeting another robot, with reported task-success rates of 60-100% using up to 40 demonstrations.

## Key Contributions

• A full-stack humanoid system for learning both whole-body motion and autonomous skills from human data.
• A low-level Humanoid Shadowing Transformer trained with reinforcement learning on 40 hours of AMASS motion and deployed zero-shot for real-time, single-RGB-camera whole-body shadowing.
• A Humanoid Imitation Transformer that combines action prediction with forward-dynamics feature regularization, enabling efficient learning from as few as 40 binocular egocentric demonstrations.
• Real-world demonstrations of complex whole-body manipulation and locomotion tasks, including shoe wearing, warehouse unloading, clothes folding, typing, and bimanual robot greeting.

## Relevance to Humanoid Robotics

HumanPlus is highly relevant because it directly tackles a core scaling bottleneck for humanoid deployment: how to generate large amounts of useful whole-body robot data without expensive motion-capture suites or exoskeleton teleoperation. By enabling a single operator to shadow a full-size humanoid through a commodity RGB camera, it provides a low-cost, scalable data-collection pipeline. The subsequent imitation stage shows that high-DoF, vision-based autonomous skills can be learned from small demonstration counts, bridging the gap between abundant human video data and real humanoid capabilities. Its hardware integration of legged base, dexterous hands, and egocentric cameras also makes it a concrete reference point for full-stack humanoid system design.
