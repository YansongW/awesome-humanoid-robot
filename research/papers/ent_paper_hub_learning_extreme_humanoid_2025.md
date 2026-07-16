---
$id: ent_paper_hub_learning_extreme_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuB: Learning Extreme Humanoid Balance'
  zh: 'HuB: Learning Extreme Humanoid Balance'
  ko: 'HuB: Learning Extreme Humanoid Balance'
summary:
  en: 'HuB: Learning Extreme Humanoid Balance is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'HuB: Learning Extreme Humanoid Balance is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'HuB: Learning Extreme Humanoid Balance is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hub
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.07294v2.
sources:
- id: src_001
  type: paper
  title: 'HuB: Learning Extreme Humanoid Balance (arXiv)'
  url: https://arxiv.org/abs/2505.07294
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HuB: Learning Extreme Humanoid Balance project page'
  url: https://hub-robot.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The human body demonstrates exceptional motor capabilities-such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters-both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances-such as a forceful soccer strike-while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## 核心内容
The human body demonstrates exceptional motor capabilities-such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters-both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances-such as a forceful soccer strike-while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## 参考
- http://arxiv.org/abs/2505.07294v2

## Overview
The human body demonstrates exceptional motor capabilities—such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters—both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances—such as a forceful soccer strike—while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## Content
The human body demonstrates exceptional motor capabilities—such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters—both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances—such as a forceful soccer strike—while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## 개요
인간의 신체는 한 발로 안정적으로 서 있거나 다리를 1.5미터 이상 들어 올려 하이킥을 수행하는 등 뛰어난 운동 능력을 보여주며, 이 모두 정밀한 균형 제어를 필요로 합니다. 최근 휴머노이드 제어 연구는 강화 학습을 활용하여 인간의 움직임을 추적함으로써 기술을 습득해 왔지만, 이러한 패러다임을 균형 집약적 작업에 적용하는 것은 여전히 어려운 과제입니다. 본 연구에서는 참조 동작 오류로 인한 불안정성, 형태학적 불일치로 인한 학습 어려움, 센서 노이즈 및 모델링되지 않은 동역학으로 인한 시뮬레이션-실제 격차라는 세 가지 주요 장애물을 식별합니다. 이러한 문제를 해결하기 위해 우리는 HuB(Humanoid Balance)라는 통합 프레임워크를 제안합니다. 이 프레임워크는 참조 동작 정제, 균형 인식 정책 학습, 시뮬레이션-실제 견고성 훈련을 통합하며, 각 구성 요소는 특정 문제를 해결하도록 설계되었습니다. 우리는 Unitree G1 휴머노이드 로봇을 사용하여 Swallow Balance와 Bruce Lee's Kick과 같은 극단적인 한발 자세를 포함한 까다로운 준정적 균형 작업에서 접근 방식을 검증합니다. 우리의 정책은 강력한 물리적 교란(예: 강한 축구 슛)에도 안정적으로 유지되는 반면, 기준 방법은 이러한 작업을 완료하는 데 지속적으로 실패합니다. 프로젝트 웹사이트: https://hub-robot.github.io

## 핵심 내용
인간의 신체는 한 발로 안정적으로 서 있거나 다리를 1.5미터 이상 들어 올려 하이킥을 수행하는 등 뛰어난 운동 능력을 보여주며, 이 모두 정밀한 균형 제어를 필요로 합니다. 최근 휴머노이드 제어 연구는 강화 학습을 활용하여 인간의 움직임을 추적함으로써 기술을 습득해 왔지만, 이러한 패러다임을 균형 집약적 작업에 적용하는 것은 여전히 어려운 과제입니다. 본 연구에서는 참조 동작 오류로 인한 불안정성, 형태학적 불일치로 인한 학습 어려움, 센서 노이즈 및 모델링되지 않은 동역학으로 인한 시뮬레이션-실제 격차라는 세 가지 주요 장애물을 식별합니다. 이러한 문제를 해결하기 위해 우리는 HuB(Humanoid Balance)라는 통합 프레임워크를 제안합니다. 이 프레임워크는 참조 동작 정제, 균형 인식 정책 학습, 시뮬레이션-실제 견고성 훈련을 통합하며, 각 구성 요소는 특정 문제를 해결하도록 설계되었습니다. 우리는 Unitree G1 휴머노이드 로봇을 사용하여 Swallow Balance와 Bruce Lee's Kick과 같은 극단적인 한발 자세를 포함한 까다로운 준정적 균형 작업에서 접근 방식을 검증합니다. 우리의 정책은 강력한 물리적 교란(예: 강한 축구 슛)에도 안정적으로 유지되는 반면, 기준 방법은 이러한 작업을 완료하는 데 지속적으로 실패합니다. 프로젝트 웹사이트: https://hub-robot.github.io
