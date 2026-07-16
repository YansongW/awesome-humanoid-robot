---
$id: ent_paper_he_viral_visual_sim_to_real_at_sc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation'
  zh: VIRAL：面向人形机器人移动操作的大规模视觉仿真到现实迁移
  ko: 'VIRAL: 인간형 로봇 로코-매니퓰레이션을 위한 대규모 비전 시뮬레이션-투-리얼'
summary:
  en: VIRAL is a visual sim-to-real framework that trains a privileged RL teacher for humanoid loco-manipulation entirely
    in simulation and distills it into an RGB-only student policy, enabling zero-shot deployment on a Unitree G1 humanoid.
  zh: VIRAL 是一种视觉仿真到现实迁移框架，仅在仿真中训练特权强化学习教师策略，并将其蒸馏为仅依赖 RGB 图像的学生策略，从而实现宇树 G1 人形机器人移动操作技能的零样本真实部署。
  ko: VIRAL은 시뮬레이션에서 특권 RL 교사 정책을 학습하고 RGB 전용 학생 정책으로 증류하여 인간형 로봇의 로코-매니퓰레이션 기술을 실제 하드웨어에 제로샷으로 배포하는 비전 기반 시뮬-투-리얼 프레임워크이다.
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
- visual_sim_to_real
- loco_manipulation
- humanoid_robotics
- teacher_student_distillation
- domain_randomization
- rgb_policy
- zero_shot_transfer
- unitree_g1
- whole_body_control
- dagger_behavior_cloning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15200v2.
sources:
- id: src_001
  type: paper
  title: 'VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2511.15200
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills. We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning. We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. To bridge the sim-to-real gap, VIRAL combines large-scale visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays--with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 humanoid, the resulting RGB-based policy performs continuous loco-manipulation for up to 54 cycles, generalizing to diverse spatial and appearance variations without any real-world fine-tuning, and approaching expert-level teleoperation performance. Extensive ablations dissect the key design choices required to make RGB-based humanoid loco-manipulation work in practice.

## 核心内容
A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills. We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning. We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. To bridge the sim-to-real gap, VIRAL combines large-scale visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays--with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 humanoid, the resulting RGB-based policy performs continuous loco-manipulation for up to 54 cycles, generalizing to diverse spatial and appearance variations without any real-world fine-tuning, and approaching expert-level teleoperation performance. Extensive ablations dissect the key design choices required to make RGB-based humanoid loco-manipulation work in practice.

## 参考
- http://arxiv.org/abs/2511.15200v2

## Overview
A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills. We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning. We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. To bridge the sim-to-real gap, VIRAL combines large-scale visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays--with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 humanoid, the resulting RGB-based policy performs continuous loco-manipulation for up to 54 cycles, generalizing to diverse spatial and appearance variations without any real-world fine-tuning, and approaching expert-level teleoperation performance. Extensive ablations dissect the key design choices required to make RGB-based humanoid loco-manipulation work in practice.

## Content
A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills. We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning. We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. To bridge the sim-to-real gap, VIRAL combines large-scale visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays--with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 humanoid, the resulting RGB-based policy performs continuous loco-manipulation for up to 54 cycles, generalizing to diverse spatial and appearance variations without any real-world fine-tuning, and approaching expert-level teleoperation performance. Extensive ablations dissect the key design choices required to make RGB-based humanoid loco-manipulation work in practice.

## 개요
휴머노이드 로봇의 실제 환경 배포를 가로막는 주요 장벽은 자율적인 이동-조작(loco-manipulation) 기술의 부재입니다. 본 논문에서는 시뮬레이션에서 완전히 휴머노이드 이동-조작을 학습하고, 제로샷(zero-shot)으로 실제 하드웨어에 배포하는 시각적 시뮬레이션-실제(sim-to-real) 프레임워크인 VIRAL을 소개합니다. VIRAL은 교사-학생(teacher-student) 설계를 따릅니다: 전체 상태에서 작동하는 특권 강화 학습(privileged RL) 교사는 델타 행동 공간(delta action space)과 참조 상태 초기화(reference state initialization)를 사용하여 장기적인 이동-조작을 학습합니다. 그런 다음 타일 렌더링(tiled rendering)을 통한 대규모 시뮬레이션을 통해 교사로부터 시각 기반 학생 정책(student policy)을 증류(distillation)하며, 온라인 DAgger와 행동 복제(behavior cloning)의 혼합으로 훈련됩니다. 계산 규모(compute scale)가 중요하다는 것을 발견했습니다: 시뮬레이션을 수십 개의 GPU(최대 64개)로 확장하면 교사와 학생 훈련 모두 신뢰할 수 있게 되는 반면, 낮은 계산 규모에서는 종종 실패합니다. 시뮬레이션-실제 격차(sim-to-real gap)를 해소하기 위해 VIRAL은 조명, 재질, 카메라 매개변수, 이미지 품질 및 센서 지연에 대한 대규모 시각적 도메인 무작위화(visual domain randomization)와 정교한 손과 카메라의 실제-시뮬레이션 정렬(real-to-sim alignment)을 결합합니다. Unitree G1 휴머노이드에 배포된 결과 RGB 기반 정책은 최대 54사이클 동안 연속적인 이동-조작을 수행하며, 실제 환경 미세 조정 없이 다양한 공간 및 외관 변화에 일반화되고, 전문가 수준의 원격 조작 성능에 근접합니다. 광범위한 절제 연구(ablation)를 통해 RGB 기반 휴머노이드 이동-조작을 실제로 작동시키기 위한 핵심 설계 선택을 분석합니다.

## 핵심 내용
휴머노이드 로봇의 실제 환경 배포를 가로막는 주요 장벽은 자율적인 이동-조작(loco-manipulation) 기술의 부재입니다. 본 논문에서는 시뮬레이션에서 완전히 휴머노이드 이동-조작을 학습하고, 제로샷(zero-shot)으로 실제 하드웨어에 배포하는 시각적 시뮬레이션-실제(sim-to-real) 프레임워크인 VIRAL을 소개합니다. VIRAL은 교사-학생(teacher-student) 설계를 따릅니다: 전체 상태에서 작동하는 특권 강화 학습(privileged RL) 교사는 델타 행동 공간(delta action space)과 참조 상태 초기화(reference state initialization)를 사용하여 장기적인 이동-조작을 학습합니다. 그런 다음 타일 렌더링(tiled rendering)을 통한 대규모 시뮬레이션을 통해 교사로부터 시각 기반 학생 정책(student policy)을 증류(distillation)하며, 온라인 DAgger와 행동 복제(behavior cloning)의 혼합으로 훈련됩니다. 계산 규모(compute scale)가 중요하다는 것을 발견했습니다: 시뮬레이션을 수십 개의 GPU(최대 64개)로 확장하면 교사와 학생 훈련 모두 신뢰할 수 있게 되는 반면, 낮은 계산 규모에서는 종종 실패합니다. 시뮬레이션-실제 격차(sim-to-real gap)를 해소하기 위해 VIRAL은 조명, 재질, 카메라 매개변수, 이미지 품질 및 센서 지연에 대한 대규모 시각적 도메인 무작위화(visual domain randomization)와 정교한 손과 카메라의 실제-시뮬레이션 정렬(real-to-sim alignment)을 결합합니다. Unitree G1 휴머노이드에 배포된 결과 RGB 기반 정책은 최대 54사이클 동안 연속적인 이동-조작을 수행하며, 실제 환경 미세 조정 없이 다양한 공간 및 외관 변화에 일반화되고, 전문가 수준의 원격 조작 성능에 근접합니다. 광범위한 절제 연구(ablation)를 통해 RGB 기반 휴머노이드 이동-조작을 실제로 작동시키기 위한 핵심 설계 선택을 분석합니다.
