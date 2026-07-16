---
$id: ent_paper_tactile_and_vision_conditioned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
  zh: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
  ko: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
summary:
  en: 'arXiv:2607.09218v1 Announce Type: new Abstract: Whole-arm manipulation involves direct contact with the environment
    while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This
    setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples
    motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become
    physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented
    in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon
    controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed
    tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics
    model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction
    forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact
    Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over
    predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC
    in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution
    of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on
    a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories:
    turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic'
  zh: 'arXiv:2607.09218v1 Announce Type: new Abstract: Whole-arm manipulation involves direct contact with the environment
    while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This
    setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples
    motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become
    physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented
    in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon
    controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed
    tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics
    model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction
    forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact
    Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over
    predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC
    in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution
    of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on
    a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories:
    turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic'
  ko: 'arXiv:2607.09218v1 Announce Type: new Abstract: Whole-arm manipulation involves direct contact with the environment
    while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This
    setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples
    motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become
    physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented
    in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon
    controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed
    tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics
    model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction
    forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact
    Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over
    predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC
    in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution
    of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on
    a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories:
    turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- tactile_and_vision_conditioned
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09218v2.
sources:
- id: src_001
  type: paper
  title: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation (arXiv)
  url: https://arxiv.org/abs/2607.09218
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Whole-arm manipulation involves direct contact with the environment while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories: turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic

## 核心内容
Whole-arm manipulation involves direct contact with the environment while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories: turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic

## 参考
- http://arxiv.org/abs/2607.09218v2

## Overview
Whole-arm manipulation involves direct contact with the environment while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories: turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic

## Content
Whole-arm manipulation involves direct contact with the environment while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories: turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic

## 개요
전완 조작(Whole-arm manipulation)은 로봇이 접촉이 형성, 미끄러짐, 분리됨에 따라 여러 링크에 접촉을 분산시키면서 작업을 완료하기 위해 환경과 직접 접촉하는 것을 포함합니다. 이러한 설정은 많은 학습 기반 조작 파이프라인에서 일반적으로 암묵적으로 가정되는 가정들을 깨뜨립니다: 팔 구성이 운동과 접촉 힘을 밀접하게 결합하고, 접촉 상태가 폐색 하에서 부분적으로 관찰되며, 순수 학습된 롤아웃은 분포 이동 하에서 물리적으로 일관성이 없어질 수 있는데, 이는 많은 다중 링크 접촉 구성이 데이터에서 드물게 표현되기 때문입니다. 이를 해결하기 위해, 우리는 TACTIC(Tactile and Vision Conditioned Contact-Centric Control)을 제안합니다. 이는 전완 조작을 위한 후퇴 수평 제어기입니다. TACTIC은 RGB-D, 분산 촉각 센싱, 그리고 컴팩트한 2D 근접 표현을 결합한 접촉 중심 하이브리드 예측 모델을 사용합니다. 이 모델은 학습된, 행동 조건화된 잠재 역학 모델을 접촉 야코비안을 통해 해석적 운동학과 결합하여, 미래 접촉 구성과 상호작용 힘의 롤아웃을 가능하게 합니다. TACTIC은 이러한 롤아웃을 접촉 인식 행동 샘플링을 갖춘 샘플링 기반 MPC 계획기에 통합합니다: 접촉 야코비안 기반 투영은 샘플링된 행동 시퀀스를 힘 조절 방향으로 유도하고, 예측된 근접성과 상호작용 힘에 대해 정의된 목표는 작업 진행과 전완 힘 조절 간의 균형을 맞춥니다. 우리는 TACTIC을 시뮬레이션에서 최신 모델 기반 및 모델 프리 방법과 비교 평가하고, 각 설계 선택의 기여도를 분리하는 절제 연구를 수행합니다. TACTIC은 다른 방법들보다 일관되게 우수한 성능을 보입니다. 또한, 다중 접촉 궤적을 필요로 하는 세 가지 전완 조작 작업(마네킹 뒤집기 및 재배치, 3D 동적 미로에서 목표 도달)에서 분산 촉각 센싱을 갖춘 로봇으로 실제 세계 성능을 입증합니다. 웹사이트: https://emprise.cs.cornell.edu/tactic

## 핵심 내용
전완 조작(Whole-arm manipulation)은 로봇이 접촉이 형성, 미끄러짐, 분리됨에 따라 여러 링크에 접촉을 분산시키면서 작업을 완료하기 위해 환경과 직접 접촉하는 것을 포함합니다. 이러한 설정은 많은 학습 기반 조작 파이프라인에서 일반적으로 암묵적으로 가정되는 가정들을 깨뜨립니다: 팔 구성이 운동과 접촉 힘을 밀접하게 결합하고, 접촉 상태가 폐색 하에서 부분적으로 관찰되며, 순수 학습된 롤아웃은 분포 이동 하에서 물리적으로 일관성이 없어질 수 있는데, 이는 많은 다중 링크 접촉 구성이 데이터에서 드물게 표현되기 때문입니다. 이를 해결하기 위해, 우리는 TACTIC(Tactile and Vision Conditioned Contact-Centric Control)을 제안합니다. 이는 전완 조작을 위한 후퇴 수평 제어기입니다. TACTIC은 RGB-D, 분산 촉각 센싱, 그리고 컴팩트한 2D 근접 표현을 결합한 접촉 중심 하이브리드 예측 모델을 사용합니다. 이 모델은 학습된, 행동 조건화된 잠재 역학 모델을 접촉 야코비안을 통해 해석적 운동학과 결합하여, 미래 접촉 구성과 상호작용 힘의 롤아웃을 가능하게 합니다. TACTIC은 이러한 롤아웃을 접촉 인식 행동 샘플링을 갖춘 샘플링 기반 MPC 계획기에 통합합니다: 접촉 야코비안 기반 투영은 샘플링된 행동 시퀀스를 힘 조절 방향으로 유도하고, 예측된 근접성과 상호작용 힘에 대해 정의된 목표는 작업 진행과 전완 힘 조절 간의 균형을 맞춥니다. 우리는 TACTIC을 시뮬레이션에서 최신 모델 기반 및 모델 프리 방법과 비교 평가하고, 각 설계 선택의 기여도를 분리하는 절제 연구를 수행합니다. TACTIC은 다른 방법들보다 일관되게 우수한 성능을 보입니다. 또한, 다중 접촉 궤적을 필요로 하는 세 가지 전완 조작 작업(마네킹 뒤집기 및 재배치, 3D 동적 미로에서 목표 도달)에서 분산 촉각 센싱을 갖춘 로봇으로 실제 세계 성능을 입증합니다. 웹사이트: https://emprise.cs.cornell.edu/tactic
