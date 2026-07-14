---
$id: ent_paper_yin_unitracker_learning_universal_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots'
  zh: UniTracker：面向人形机器人的通用全身运动追踪器
  ko: 'UniTracker: 휴머노이드 로봇을 위한 범용 전신 동작 추적기'
summary:
  en: UniTracker is a three-stage learning framework that trains a privileged full-observation teacher policy, a CVAE-based
    universal student policy whose partial-observation prior is aligned with a full-observation encoder, and a lightweight
    residual-decoder adaptation module to track thousands of whole-body motions on a Unitree G1 humanoid.
  zh: UniTracker是一个三阶段学习框架：先训练具有完整观测特权的教师策略，再训练将部分观测先验与完整观测编码器对齐以获得全局运动隐表示的CVAE通用学生策略，最后通过轻量级残差解码器自适应模块在Unitree G1人形机器人上追踪数千种全身运动。
  ko: UniTracker는 전체 관측 특권 교사 정책, 부분 관측 사전 분포를 전체 관측 인코더와 정렬하여 전역 운동 잠재 표현을 학습하는 CVAE 기반 범용 학생 정책, 그리고 경량 잔차 디코더 적응 모듈을 통해
    Unitree G1 휴머노이드 로봇에서 수천 개의 전신 동작을 추적하는 세 단계 학습 프레임워크이다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_robot
- whole_body_motion_tracking
- teacher_student_distillation
- cvae
- latent_alignment
- fast_adaptation
- unitree_g1
- motion_imitation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.07356v3.
sources:
- id: src_001
  type: paper
  title: 'UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots'
  url: https://arxiv.org/abs/2507.07356
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Achieving expressive and generalizable whole-body motion control is essential for deploying humanoid robots in real-world environments. In this work, we propose UniTracker, a three-stage training framework that enables robust and scalable motion tracking across a wide range of human behaviors. In the first stage, we train a teacher policy with privileged observations to generate high-quality actions. In the second stage, we introduce a Conditional Variational Autoencoder (CVAE) to model a universal student policy that can be deployed directly on real hardware. The CVAE structure allows the policy to learn a global latent representation of motion, enhancing generalization to unseen behaviors and addressing the limitations of standard MLP-based policies under partial observations. Unlike pure MLPs that suffer from drift in global attributes like orientation, our CVAE-student policy incorporates global intent during training by aligning a partial-observation prior to the full-observation encoder. In the third stage, we introduce a fast adaptation module that fine-tunes the universal policy on harder motion sequences that are difficult to track directly. This adaptation can be performed both for single sequences and in batch mode, further showcasing the flexibility and scalability of our approach. We evaluate UniTracker in both simulation and real-world settings using a Unitree G1 humanoid, demonstrating strong performance in motion diversity, tracking accuracy, and deployment robustness.

## 核心内容
Achieving expressive and generalizable whole-body motion control is essential for deploying humanoid robots in real-world environments. In this work, we propose UniTracker, a three-stage training framework that enables robust and scalable motion tracking across a wide range of human behaviors. In the first stage, we train a teacher policy with privileged observations to generate high-quality actions. In the second stage, we introduce a Conditional Variational Autoencoder (CVAE) to model a universal student policy that can be deployed directly on real hardware. The CVAE structure allows the policy to learn a global latent representation of motion, enhancing generalization to unseen behaviors and addressing the limitations of standard MLP-based policies under partial observations. Unlike pure MLPs that suffer from drift in global attributes like orientation, our CVAE-student policy incorporates global intent during training by aligning a partial-observation prior to the full-observation encoder. In the third stage, we introduce a fast adaptation module that fine-tunes the universal policy on harder motion sequences that are difficult to track directly. This adaptation can be performed both for single sequences and in batch mode, further showcasing the flexibility and scalability of our approach. We evaluate UniTracker in both simulation and real-world settings using a Unitree G1 humanoid, demonstrating strong performance in motion diversity, tracking accuracy, and deployment robustness.

## 参考
- http://arxiv.org/abs/2507.07356v3

