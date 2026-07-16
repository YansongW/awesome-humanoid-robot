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

## Overview
Achieving expressive and generalizable whole-body motion control is essential for deploying humanoid robots in real-world environments. In this work, we propose UniTracker, a three-stage training framework that enables robust and scalable motion tracking across a wide range of human behaviors. In the first stage, we train a teacher policy with privileged observations to generate high-quality actions. In the second stage, we introduce a Conditional Variational Autoencoder (CVAE) to model a universal student policy that can be deployed directly on real hardware. The CVAE structure allows the policy to learn a global latent representation of motion, enhancing generalization to unseen behaviors and addressing the limitations of standard MLP-based policies under partial observations. Unlike pure MLPs that suffer from drift in global attributes like orientation, our CVAE-student policy incorporates global intent during training by aligning a partial-observation prior to the full-observation encoder. In the third stage, we introduce a fast adaptation module that fine-tunes the universal policy on harder motion sequences that are difficult to track directly. This adaptation can be performed both for single sequences and in batch mode, further showcasing the flexibility and scalability of our approach. We evaluate UniTracker in both simulation and real-world settings using a Unitree G1 humanoid, demonstrating strong performance in motion diversity, tracking accuracy, and deployment robustness.

## Content
Achieving expressive and generalizable whole-body motion control is essential for deploying humanoid robots in real-world environments. In this work, we propose UniTracker, a three-stage training framework that enables robust and scalable motion tracking across a wide range of human behaviors. In the first stage, we train a teacher policy with privileged observations to generate high-quality actions. In the second stage, we introduce a Conditional Variational Autoencoder (CVAE) to model a universal student policy that can be deployed directly on real hardware. The CVAE structure allows the policy to learn a global latent representation of motion, enhancing generalization to unseen behaviors and addressing the limitations of standard MLP-based policies under partial observations. Unlike pure MLPs that suffer from drift in global attributes like orientation, our CVAE-student policy incorporates global intent during training by aligning a partial-observation prior to the full-observation encoder. In the third stage, we introduce a fast adaptation module that fine-tunes the universal policy on harder motion sequences that are difficult to track directly. This adaptation can be performed both for single sequences and in batch mode, further showcasing the flexibility and scalability of our approach. We evaluate UniTracker in both simulation and real-world settings using a Unitree G1 humanoid, demonstrating strong performance in motion diversity, tracking accuracy, and deployment robustness.

## 개요
인간형 로봇을 실제 환경에 배치하기 위해서는 표현력이 풍부하고 일반화 가능한 전신 동작 제어가 필수적입니다. 본 연구에서는 다양한 인간 행동에 걸쳐 강건하고 확장 가능한 동작 추적을 가능하게 하는 3단계 훈련 프레임워크인 UniTracker를 제안합니다. 첫 번째 단계에서는 특권 관측(privileged observations)을 활용한 교사 정책(teacher policy)을 훈련하여 고품질 행동을 생성합니다. 두 번째 단계에서는 조건부 변분 오토인코더(Conditional Variational Autoencoder, CVAE)를 도입하여 실제 하드웨어에 직접 배포할 수 있는 범용 학생 정책(universal student policy)을 모델링합니다. CVAE 구조는 정책이 동작의 전역 잠재 표현(global latent representation)을 학습할 수 있게 하여, 미처 경험하지 못한 행동에 대한 일반화를 향상시키고 부분 관측 하에서 표준 MLP 기반 정책의 한계를 해결합니다. 방향과 같은 전역 속성에서 드리프트(drift)가 발생하는 순수 MLP와 달리, 본 CVAE-학생 정책은 부분 관측 사전(prior)을 전체 관측 인코더(encoder)에 정렬하여 훈련 중 전역 의도(global intent)를 통합합니다. 세 번째 단계에서는 직접 추적하기 어려운 더 어려운 동작 시퀀스에 대해 범용 정책을 미세 조정하는 빠른 적응 모듈(fast adaptation module)을 도입합니다. 이 적응은 단일 시퀀스와 배치 모드 모두에서 수행될 수 있어, 본 접근법의 유연성과 확장성을 더욱 입증합니다. 우리는 Unitree G1 인간형 로봇을 사용하여 시뮬레이션과 실제 환경 모두에서 UniTracker를 평가하며, 동작 다양성, 추적 정확도 및 배치 강건성에서 뛰어난 성능을 보여줍니다.

## 핵심 내용
인간형 로봇을 실제 환경에 배치하기 위해서는 표현력이 풍부하고 일반화 가능한 전신 동작 제어가 필수적입니다. 본 연구에서는 다양한 인간 행동에 걸쳐 강건하고 확장 가능한 동작 추적을 가능하게 하는 3단계 훈련 프레임워크인 UniTracker를 제안합니다. 첫 번째 단계에서는 특권 관측을 활용한 교사 정책을 훈련하여 고품질 행동을 생성합니다. 두 번째 단계에서는 조건부 변분 오토인코더(CVAE)를 도입하여 실제 하드웨어에 직접 배포할 수 있는 범용 학생 정책을 모델링합니다. CVAE 구조는 정책이 동작의 전역 잠재 표현을 학습할 수 있게 하여, 미처 경험하지 못한 행동에 대한 일반화를 향상시키고 부분 관측 하에서 표준 MLP 기반 정책의 한계를 해결합니다. 방향과 같은 전역 속성에서 드리프트가 발생하는 순수 MLP와 달리, 본 CVAE-학생 정책은 부분 관측 사전을 전체 관측 인코더에 정렬하여 훈련 중 전역 의도를 통합합니다. 세 번째 단계에서는 직접 추적하기 어려운 더 어려운 동작 시퀀스에 대해 범용 정책을 미세 조정하는 빠른 적응 모듈을 도입합니다. 이 적응은 단일 시퀀스와 배치 모드 모두에서 수행될 수 있어, 본 접근법의 유연성과 확장성을 더욱 입증합니다. 우리는 Unitree G1 인간형 로봇을 사용하여 시뮬레이션과 실제 환경 모두에서 UniTracker를 평가하며, 동작 다양성, 추적 정확도 및 배치 강건성에서 뛰어난 성능을 보여줍니다.
