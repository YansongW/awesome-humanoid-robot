---
$id: ent_paper_jia_video2act_a_dual_system_video_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling'
  zh: Video2Act
  ko: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling'
summary:
  en: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (Video2Act), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Sun Yat-sen University, Wuhan University, Hong Kong University
    of Science and Technology.'
  zh: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (Video2Act), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Sun Yat-sen University, Wuhan University, Hong Kong University
    of Science and Technology.'
  ko: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (Video2Act), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Sun Yat-sen University, Wuhan University, Hong Kong University
    of Science and Technology.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- video2act
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.03044v3.
sources:
- id: src_001
  type: paper
  title: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (arXiv)'
  url: https://arxiv.org/abs/2512.03044
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Video2Act source
  url: https://doi.org/10.48550/arXiv.2512.03044
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robust perception and dynamics modeling are fundamental to real-world robotic policy learning. Recent methods employ video diffusion models (VDMs) to enhance robotic policies, improving their understanding and modeling of the physical world. However, existing approaches overlook the coherent and physically consistent motion representations inherently encoded across frames in VDMs. To this end, we propose Video2Act, a framework that efficiently guides robotic action learning by explicitly integrating spatial and motion-aware representations. Building on the inherent representations of VDMs, we extract foreground boundaries and inter-frame motion variations while filtering out background noise and task-irrelevant biases. These refined representations are then used as additional conditioning inputs to a diffusion transformer (DiT) action head, enabling it to reason about what to manipulate and how to move. To mitigate inference inefficiency, we propose an asynchronous dual-system design, where the VDM functions as the slow System 2 and the DiT head as the fast System 1, working collaboratively to generate adaptive actions. By providing motion-aware conditions to System 1, Video2Act maintains stable manipulation even with low-frequency updates from the VDM. For evaluation, Video2Act surpasses previous state-of-the-art VLA methods by 7.7% in simulation and 21.7% in real-world tasks in terms of average success rate, further exhibiting strong generalization capabilities.

## 核心内容
Robust perception and dynamics modeling are fundamental to real-world robotic policy learning. Recent methods employ video diffusion models (VDMs) to enhance robotic policies, improving their understanding and modeling of the physical world. However, existing approaches overlook the coherent and physically consistent motion representations inherently encoded across frames in VDMs. To this end, we propose Video2Act, a framework that efficiently guides robotic action learning by explicitly integrating spatial and motion-aware representations. Building on the inherent representations of VDMs, we extract foreground boundaries and inter-frame motion variations while filtering out background noise and task-irrelevant biases. These refined representations are then used as additional conditioning inputs to a diffusion transformer (DiT) action head, enabling it to reason about what to manipulate and how to move. To mitigate inference inefficiency, we propose an asynchronous dual-system design, where the VDM functions as the slow System 2 and the DiT head as the fast System 1, working collaboratively to generate adaptive actions. By providing motion-aware conditions to System 1, Video2Act maintains stable manipulation even with low-frequency updates from the VDM. For evaluation, Video2Act surpasses previous state-of-the-art VLA methods by 7.7% in simulation and 21.7% in real-world tasks in terms of average success rate, further exhibiting strong generalization capabilities.

## 参考
- http://arxiv.org/abs/2512.03044v3

## Overview
Robust perception and dynamics modeling are fundamental to real-world robotic policy learning. Recent methods employ video diffusion models (VDMs) to enhance robotic policies, improving their understanding and modeling of the physical world. However, existing approaches overlook the coherent and physically consistent motion representations inherently encoded across frames in VDMs. To this end, we propose Video2Act, a framework that efficiently guides robotic action learning by explicitly integrating spatial and motion-aware representations. Building on the inherent representations of VDMs, we extract foreground boundaries and inter-frame motion variations while filtering out background noise and task-irrelevant biases. These refined representations are then used as additional conditioning inputs to a diffusion transformer (DiT) action head, enabling it to reason about what to manipulate and how to move. To mitigate inference inefficiency, we propose an asynchronous dual-system design, where the VDM functions as the slow System 2 and the DiT head as the fast System 1, working collaboratively to generate adaptive actions. By providing motion-aware conditions to System 1, Video2Act maintains stable manipulation even with low-frequency updates from the VDM. For evaluation, Video2Act surpasses previous state-of-the-art VLA methods by 7.7% in simulation and 21.7% in real-world tasks in terms of average success rate, further exhibiting strong generalization capabilities.

## Content
Robust perception and dynamics modeling are fundamental to real-world robotic policy learning. Recent methods employ video diffusion models (VDMs) to enhance robotic policies, improving their understanding and modeling of the physical world. However, existing approaches overlook the coherent and physically consistent motion representations inherently encoded across frames in VDMs. To this end, we propose Video2Act, a framework that efficiently guides robotic action learning by explicitly integrating spatial and motion-aware representations. Building on the inherent representations of VDMs, we extract foreground boundaries and inter-frame motion variations while filtering out background noise and task-irrelevant biases. These refined representations are then used as additional conditioning inputs to a diffusion transformer (DiT) action head, enabling it to reason about what to manipulate and how to move. To mitigate inference inefficiency, we propose an asynchronous dual-system design, where the VDM functions as the slow System 2 and the DiT head as the fast System 1, working collaboratively to generate adaptive actions. By providing motion-aware conditions to System 1, Video2Act maintains stable manipulation even with low-frequency updates from the VDM. For evaluation, Video2Act surpasses previous state-of-the-art VLA methods by 7.7% in simulation and 21.7% in real-world tasks in terms of average success rate, further exhibiting strong generalization capabilities.

## 개요
강건한 인식과 동역학 모델링은 실제 로봇 정책 학습의 핵심입니다. 최근 방법들은 비디오 확산 모델(VDM)을 활용하여 로봇 정책을 향상시키고, 물리적 세계에 대한 이해와 모델링 능력을 개선합니다. 그러나 기존 접근법은 VDM이 프레임 간에 본질적으로 인코딩한 일관되고 물리적으로 일관된 움직임 표현을 간과합니다. 이를 해결하기 위해, 우리는 공간 및 움직임 인식 표현을 명시적으로 통합하여 로봇 행동 학습을 효율적으로 안내하는 프레임워크인 Video2Act를 제안합니다. VDM의 본질적 표현을 기반으로, 배경 잡음과 작업 관련 없는 편향을 걸러내면서 전경 경계와 프레임 간 움직임 변화를 추출합니다. 이러한 정제된 표현은 확산 트랜스포머(DiT) 행동 헤드에 추가 조건 입력으로 사용되어, 무엇을 조작하고 어떻게 움직일지 추론할 수 있게 합니다. 추론 비효율성을 완화하기 위해, VDM이 느린 시스템 2로, DiT 헤드가 빠른 시스템 1로 기능하여 협력적으로 적응형 행동을 생성하는 비동기 이중 시스템 설계를 제안합니다. 시스템 1에 움직임 인식 조건을 제공함으로써, Video2Act는 VDM의 낮은 빈도 업데이트에도 안정적인 조작을 유지합니다. 평가 결과, Video2Act는 평균 성공률 기준 시뮬레이션에서 7.7%, 실제 작업에서 21.7% 향상된 성능을 보이며, 이전 최첨단 VLA 방법을 능가하고 강력한 일반화 능력을 입증합니다.

## 핵심 내용
강건한 인식과 동역학 모델링은 실제 로봇 정책 학습의 핵심입니다. 최근 방법들은 비디오 확산 모델(VDM)을 활용하여 로봇 정책을 향상시키고, 물리적 세계에 대한 이해와 모델링 능력을 개선합니다. 그러나 기존 접근법은 VDM이 프레임 간에 본질적으로 인코딩한 일관되고 물리적으로 일관된 움직임 표현을 간과합니다. 이를 해결하기 위해, 우리는 공간 및 움직임 인식 표현을 명시적으로 통합하여 로봇 행동 학습을 효율적으로 안내하는 프레임워크인 Video2Act를 제안합니다. VDM의 본질적 표현을 기반으로, 배경 잡음과 작업 관련 없는 편향을 걸러내면서 전경 경계와 프레임 간 움직임 변화를 추출합니다. 이러한 정제된 표현은 확산 트랜스포머(DiT) 행동 헤드에 추가 조건 입력으로 사용되어, 무엇을 조작하고 어떻게 움직일지 추론할 수 있게 합니다. 추론 비효율성을 완화하기 위해, VDM이 느린 시스템 2로, DiT 헤드가 빠른 시스템 1로 기능하여 협력적으로 적응형 행동을 생성하는 비동기 이중 시스템 설계를 제안합니다. 시스템 1에 움직임 인식 조건을 제공함으로써, Video2Act는 VDM의 낮은 빈도 업데이트에도 안정적인 조작을 유지합니다. 평가 결과, Video2Act는 평균 성공률 기준 시뮬레이션에서 7.7%, 실제 작업에서 21.7% 향상된 성능을 보이며, 이전 최첨단 VLA 방법을 능가하고 강력한 일반화 능력을 입증합니다.
