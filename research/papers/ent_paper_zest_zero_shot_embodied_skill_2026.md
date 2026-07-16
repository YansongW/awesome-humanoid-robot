---
$id: ent_paper_zest_zero_shot_embodied_skill_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control'
  zh: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control'
  ko: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control'
summary:
  en: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- loco_manipulation
- whole_body_control
- zest
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.00401v1.
sources:
- id: src_001
  type: paper
  title: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control (arXiv)'
  url: https://arxiv.org/abs/2602.00401
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Achieving robust, human-like whole-body control on humanoid robots for agile, contact-rich behaviors remains a central challenge, demanding heavy per-skill engineering and a brittle process of tuning controllers. We introduce ZEST (Zero-shot Embodied Skill Transfer), a streamlined motion-imitation framework that trains policies via reinforcement learning from diverse sources -- high-fidelity motion capture, noisy monocular video, and non-physics-constrained animation -- and deploys them to hardware zero-shot. ZEST generalizes across behaviors and platforms while avoiding contact labels, reference or observation windows, state estimators, and extensive reward shaping. Its training pipeline combines adaptive sampling, which focuses training on difficult motion segments, and an automatic curriculum using a model-based assistive wrench, together enabling dynamic, long-horizon maneuvers. We further provide a procedure for selecting joint-level gains from approximate analytical armature values for closed-chain actuators, along with a refined model of actuators. Trained entirely in simulation with moderate domain randomization, ZEST demonstrates remarkable generality. On Boston Dynamics' Atlas humanoid, ZEST learns dynamic, multi-contact skills (e.g., army crawl, breakdancing) from motion capture. It transfers expressive dance and scene-interaction skills, such as box-climbing, directly from videos to Atlas and the Unitree G1. Furthermore, it extends across morphologies to the Spot quadruped, enabling acrobatics, such as a continuous backflip, through animation. Together, these results demonstrate robust zero-shot deployment across heterogeneous data sources and embodiments, establishing ZEST as a scalable interface between biological movements and their robotic counterparts.

## 核心内容
Achieving robust, human-like whole-body control on humanoid robots for agile, contact-rich behaviors remains a central challenge, demanding heavy per-skill engineering and a brittle process of tuning controllers. We introduce ZEST (Zero-shot Embodied Skill Transfer), a streamlined motion-imitation framework that trains policies via reinforcement learning from diverse sources -- high-fidelity motion capture, noisy monocular video, and non-physics-constrained animation -- and deploys them to hardware zero-shot. ZEST generalizes across behaviors and platforms while avoiding contact labels, reference or observation windows, state estimators, and extensive reward shaping. Its training pipeline combines adaptive sampling, which focuses training on difficult motion segments, and an automatic curriculum using a model-based assistive wrench, together enabling dynamic, long-horizon maneuvers. We further provide a procedure for selecting joint-level gains from approximate analytical armature values for closed-chain actuators, along with a refined model of actuators. Trained entirely in simulation with moderate domain randomization, ZEST demonstrates remarkable generality. On Boston Dynamics' Atlas humanoid, ZEST learns dynamic, multi-contact skills (e.g., army crawl, breakdancing) from motion capture. It transfers expressive dance and scene-interaction skills, such as box-climbing, directly from videos to Atlas and the Unitree G1. Furthermore, it extends across morphologies to the Spot quadruped, enabling acrobatics, such as a continuous backflip, through animation. Together, these results demonstrate robust zero-shot deployment across heterogeneous data sources and embodiments, establishing ZEST as a scalable interface between biological movements and their robotic counterparts.

## 参考
- http://arxiv.org/abs/2602.00401v1

## Overview
Achieving robust, human-like whole-body control on humanoid robots for agile, contact-rich behaviors remains a central challenge, demanding heavy per-skill engineering and a brittle process of tuning controllers. We introduce ZEST (Zero-shot Embodied Skill Transfer), a streamlined motion-imitation framework that trains policies via reinforcement learning from diverse sources -- high-fidelity motion capture, noisy monocular video, and non-physics-constrained animation -- and deploys them to hardware zero-shot. ZEST generalizes across behaviors and platforms while avoiding contact labels, reference or observation windows, state estimators, and extensive reward shaping. Its training pipeline combines adaptive sampling, which focuses training on difficult motion segments, and an automatic curriculum using a model-based assistive wrench, together enabling dynamic, long-horizon maneuvers. We further provide a procedure for selecting joint-level gains from approximate analytical armature values for closed-chain actuators, along with a refined model of actuators. Trained entirely in simulation with moderate domain randomization, ZEST demonstrates remarkable generality. On Boston Dynamics' Atlas humanoid, ZEST learns dynamic, multi-contact skills (e.g., army crawl, breakdancing) from motion capture. It transfers expressive dance and scene-interaction skills, such as box-climbing, directly from videos to Atlas and the Unitree G1. Furthermore, it extends across morphologies to the Spot quadruped, enabling acrobatics, such as a continuous backflip, through animation. Together, these results demonstrate robust zero-shot deployment across heterogeneous data sources and embodiments, establishing ZEST as a scalable interface between biological movements and their robotic counterparts.

## Content
Achieving robust, human-like whole-body control on humanoid robots for agile, contact-rich behaviors remains a central challenge, demanding heavy per-skill engineering and a brittle process of tuning controllers. We introduce ZEST (Zero-shot Embodied Skill Transfer), a streamlined motion-imitation framework that trains policies via reinforcement learning from diverse sources -- high-fidelity motion capture, noisy monocular video, and non-physics-constrained animation -- and deploys them to hardware zero-shot. ZEST generalizes across behaviors and platforms while avoiding contact labels, reference or observation windows, state estimators, and extensive reward shaping. Its training pipeline combines adaptive sampling, which focuses training on difficult motion segments, and an automatic curriculum using a model-based assistive wrench, together enabling dynamic, long-horizon maneuvers. We further provide a procedure for selecting joint-level gains from approximate analytical armature values for closed-chain actuators, along with a refined model of actuators. Trained entirely in simulation with moderate domain randomization, ZEST demonstrates remarkable generality. On Boston Dynamics' Atlas humanoid, ZEST learns dynamic, multi-contact skills (e.g., army crawl, breakdancing) from motion capture. It transfers expressive dance and scene-interaction skills, such as box-climbing, directly from videos to Atlas and the Unitree G1. Furthermore, it extends across morphologies to the Spot quadruped, enabling acrobatics, such as a continuous backflip, through animation. Together, these results demonstrate robust zero-shot deployment across heterogeneous data sources and embodiments, establishing ZEST as a scalable interface between biological movements and their robotic counterparts.

## 개요
휴머노이드 로봇에서 민첩하고 접촉이 많은 행동을 위한 강건하고 인간과 유사한 전신 제어를 달성하는 것은 여전히 핵심 과제로, 스킬별로 많은 엔지니어링과 취약한 컨트롤러 튜닝 과정을 요구합니다. 우리는 ZEST(Zero-shot Embodied Skill Transfer)를 소개합니다. 이는 간소화된 동작 모방 프레임워크로, 고충실도 모션 캡처, 노이즈가 있는 단안 비디오, 물리 제약이 없는 애니메이션 등 다양한 소스로부터 강화 학습을 통해 정책을 훈련하고, 이를 하드웨어에 제로샷으로 배포합니다. ZEST는 접촉 레이블, 참조 또는 관찰 윈도우, 상태 추정기, 광범위한 보상 설계를 피하면서 행동과 플랫폼 전반에 걸쳐 일반화됩니다. 훈련 파이프라인은 훈련을 어려운 동작 구간에 집중시키는 적응형 샘플링과 모델 기반 보조 렌치를 사용하는 자동 커리큘럼을 결합하여 동적이고 장기적인 기동을 가능하게 합니다. 또한 폐쇄 사슬 액추에이터에 대한 근사 분석 아마추어 값으로부터 관절 수준 게인을 선택하는 절차와 개선된 액추에이터 모델을 제공합니다. 중간 정도의 도메인 무작위화로 시뮬레이션에서 완전히 훈련된 ZEST는 놀라운 일반성을 보여줍니다. Boston Dynamics의 Atlas 휴머노이드에서 ZEST는 모션 캡처로부터 동적이고 다중 접촉 스킬(예: 군대 기어가기, 브레이크댄스)을 학습합니다. 또한 표현적인 춤과 상자 오르기와 같은 장면 상호작용 스킬을 비디오에서 직접 Atlas와 Unitree G1으로 전송합니다. 나아가 Spot 사족 로봇으로 형태를 넘어 확장되어 애니메이션을 통해 연속 백플립과 같은 곡예를 가능하게 합니다. 이러한 결과들은 이질적인 데이터 소스와 구현체 전반에 걸친 강건한 제로샷 배포를 입증하며, ZEST를 생물학적 움직임과 로봇 대응물 간의 확장 가능한 인터페이스로 확립합니다.

## 핵심 내용
휴머노이드 로봇에서 민첩하고 접촉이 많은 행동을 위한 강건하고 인간과 유사한 전신 제어를 달성하는 것은 여전히 핵심 과제로, 스킬별로 많은 엔지니어링과 취약한 컨트롤러 튜닝 과정을 요구합니다. 우리는 ZEST(Zero-shot Embodied Skill Transfer)를 소개합니다. 이는 간소화된 동작 모방 프레임워크로, 고충실도 모션 캡처, 노이즈가 있는 단안 비디오, 물리 제약이 없는 애니메이션 등 다양한 소스로부터 강화 학습을 통해 정책을 훈련하고, 이를 하드웨어에 제로샷으로 배포합니다. ZEST는 접촉 레이블, 참조 또는 관찰 윈도우, 상태 추정기, 광범위한 보상 설계를 피하면서 행동과 플랫폼 전반에 걸쳐 일반화됩니다. 훈련 파이프라인은 훈련을 어려운 동작 구간에 집중시키는 적응형 샘플링과 모델 기반 보조 렌치를 사용하는 자동 커리큘럼을 결합하여 동적이고 장기적인 기동을 가능하게 합니다. 또한 폐쇄 사슬 액추에이터에 대한 근사 분석 아마추어 값으로부터 관절 수준 게인을 선택하는 절차와 개선된 액추에이터 모델을 제공합니다. 중간 정도의 도메인 무작위화로 시뮬레이션에서 완전히 훈련된 ZEST는 놀라운 일반성을 보여줍니다. Boston Dynamics의 Atlas 휴머노이드에서 ZEST는 모션 캡처로부터 동적이고 다중 접촉 스킬(예: 군대 기어가기, 브레이크댄스)을 학습합니다. 또한 표현적인 춤과 상자 오르기와 같은 장면 상호작용 스킬을 비디오에서 직접 Atlas와 Unitree G1으로 전송합니다. 나아가 Spot 사족 로봇으로 형태를 넘어 확장되어 애니메이션을 통해 연속 백플립과 같은 곡예를 가능하게 합니다. 이러한 결과들은 이질적인 데이터 소스와 구현체 전반에 걸친 강건한 제로샷 배포를 입증하며, ZEST를 생물학적 움직임과 로봇 대응물 간의 확장 가능한 인터페이스로 확립합니다.
