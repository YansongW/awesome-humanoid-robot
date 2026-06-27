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
  en: UniTracker is a three-stage learning framework that trains a privileged full-observation
    teacher policy, a CVAE-based universal student policy whose partial-observation
    prior is aligned with a full-observation encoder, and a lightweight residual-decoder
    adaptation module to track thousands of whole-body motions on a Unitree G1 humanoid.
  zh: UniTracker是一个三阶段学习框架：先训练具有完整观测特权的教师策略，再训练将部分观测先验与完整观测编码器对齐以获得全局运动隐表示的CVAE通用学生策略，最后通过轻量级残差解码器自适应模块在Unitree
    G1人形机器人上追踪数千种全身运动。
  ko: UniTracker는 전체 관측 특권 교사 정책, 부분 관측 사전 분포를 전체 관측 인코더와 정렬하여 전역 운동 잠재 표현을 학습하는 CVAE
    기반 범용 학생 정책, 그리고 경량 잔차 디코더 적응 모듈을 통해 Unitree G1 휴머노이드 로봇에서 수천 개의 전신 동작을 추적하는 세
    단계 학습 프레임워크이다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full paper before verification.
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

## Overview

UniTracker addresses whole-body motion tracking for humanoid robots through a scalable three-stage training pipeline. The first stage learns a privileged teacher policy using full observations to generate high-fidelity reference actions. The second stage distills this knowledge into a CVAE-based universal student policy that captures a global latent representation of motion and aligns a partial-observation prior with a full-observation encoder to inject global intent. The third stage adds a lightweight residual decoder that quickly adapts the student to challenging motions, supporting both per-instance and batch adaptation.

## Key Contributions

- A three-stage training framework combining a privileged teacher, a CVAE-based universal student, and fast adaptation.
- A CVAE-based universal policy that captures motion diversity and integrates global context via KL alignment between partial- and full-observation encoders.
- A lightweight residual-decoder fast adaptation module for per-instance and batch motion fine-tuning.
- Real-world validation on a Unitree G1 humanoid tracking over 8,100 motions with a single policy.

## Relevance to Humanoid Robotics

UniTracker is highly relevant to humanoid deployment because it aims to make a single learned policy generalize across thousands of diverse whole-body reference motions on real hardware. By improving expressiveness, reducing orientation drift, and supporting fast adaptation, it advances scalable and robust whole-body controllers for humanoid robots.
