---
$id: ent_paper_humanoid_hanoi_investigating_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement'
  zh: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement'
  ko: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement'
summary:
  en: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- humanoid_hanoi
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.13850v3.
sources:
- id: src_001
  type: paper
  title: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement (arXiv)'
  url: https://arxiv.org/abs/2602.13850
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We investigate a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level. In our architecture, all skills execute through a shared, task-agnostic whole-body controller (WBC), providing a consistent closed-loop interface for skill composition, in contrast to non-shared designs that use separate low-level controllers per skill. We find that naively reusing the same pretrained WBC can reduce robustness over long horizons, as new skills and their compositions induce shifted state and command distributions. We address this with a simple data aggregation procedure that augments shared-WBC training with rollouts from closed-loop skill execution under domain randomization. To evaluate the approach, we introduce Humanoid Hanoi, a long-horizon Tower-of-Hanoi box rearrangement benchmark, and report results in simulation and on the Digit V3 humanoid robot, demonstrating fully autonomous rearrangement over extended horizons and quantifying the benefits of the shared-WBC approach over non-shared baselines. Project page: https://osudrl.github.io/Humanoid_Hanoi/

## 核心内容
We investigate a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level. In our architecture, all skills execute through a shared, task-agnostic whole-body controller (WBC), providing a consistent closed-loop interface for skill composition, in contrast to non-shared designs that use separate low-level controllers per skill. We find that naively reusing the same pretrained WBC can reduce robustness over long horizons, as new skills and their compositions induce shifted state and command distributions. We address this with a simple data aggregation procedure that augments shared-WBC training with rollouts from closed-loop skill execution under domain randomization. To evaluate the approach, we introduce Humanoid Hanoi, a long-horizon Tower-of-Hanoi box rearrangement benchmark, and report results in simulation and on the Digit V3 humanoid robot, demonstrating fully autonomous rearrangement over extended horizons and quantifying the benefits of the shared-WBC approach over non-shared baselines. Project page: https://osudrl.github.io/Humanoid_Hanoi/

## 参考
- http://arxiv.org/abs/2602.13850v3

## Overview
We investigate a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level. In our architecture, all skills execute through a shared, task-agnostic whole-body controller (WBC), providing a consistent closed-loop interface for skill composition, in contrast to non-shared designs that use separate low-level controllers per skill. We find that naively reusing the same pretrained WBC can reduce robustness over long horizons, as new skills and their compositions induce shifted state and command distributions. We address this with a simple data aggregation procedure that augments shared-WBC training with rollouts from closed-loop skill execution under domain randomization. To evaluate the approach, we introduce Humanoid Hanoi, a long-horizon Tower-of-Hanoi box rearrangement benchmark, and report results in simulation and on the Digit V3 humanoid robot, demonstrating fully autonomous rearrangement over extended horizons and quantifying the benefits of the shared-WBC approach over non-shared baselines. Project page: https://osudrl.github.io/Humanoid_Hanoi/

## Content
We investigate a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level. In our architecture, all skills execute through a shared, task-agnostic whole-body controller (WBC), providing a consistent closed-loop interface for skill composition, in contrast to non-shared designs that use separate low-level controllers per skill. We find that naively reusing the same pretrained WBC can reduce robustness over long horizons, as new skills and their compositions induce shifted state and command distributions. We address this with a simple data aggregation procedure that augments shared-WBC training with rollouts from closed-loop skill execution under domain randomization. To evaluate the approach, we introduce Humanoid Hanoi, a long-horizon Tower-of-Hanoi box rearrangement benchmark, and report results in simulation and on the Digit V3 humanoid robot, demonstrating fully autonomous rearrangement over extended horizons and quantifying the benefits of the shared-WBC approach over non-shared baselines. Project page: https://osudrl.github.io/Humanoid_Hanoi/

## 개요
본 연구는 휴머노이드의 상자 재배치를 위한 스킬 기반 프레임워크를 조사하며, 작업 수준에서 재사용 가능한 스킬을 순차적으로 실행하여 장기적인 수행을 가능하게 합니다. 우리 아키텍처에서는 모든 스킬이 공유된 작업 비특화 전신 제어기(WBC)를 통해 실행되며, 이는 스킬별로 별도의 하위 수준 제어기를 사용하는 비공유 설계와 달리 일관된 폐루프 인터페이스를 제공합니다. 동일한 사전 훈련된 WBC를 단순히 재사용하면 새로운 스킬과 그 조합이 상태 및 명령 분포를 변화시켜 장기적인 수행에서 강건성이 저하될 수 있음을 발견했습니다. 이에 대해 도메인 무작위화 하에서 폐루프 스킬 실행의 롤아웃을 통해 공유 WBC 훈련을 보강하는 간단한 데이터 수집 절차를 제안합니다. 접근법 평가를 위해 장기적인 하노이 탑 상자 재배치 벤치마크인 Humanoid Hanoi를 도입하고, 시뮬레이션 및 Digit V3 휴머노이드 로봇에서의 결과를 보고하며, 확장된 기간 동안 완전 자율 재배치를 입증하고 공유 WBC 접근법의 비공유 기준선 대비 이점을 정량화합니다. 프로젝트 페이지: https://osudrl.github.io/Humanoid_Hanoi/

## 핵심 내용
본 연구는 휴머노이드의 상자 재배치를 위한 스킬 기반 프레임워크를 조사하며, 작업 수준에서 재사용 가능한 스킬을 순차적으로 실행하여 장기적인 수행을 가능하게 합니다. 우리 아키텍처에서는 모든 스킬이 공유된 작업 비특화 전신 제어기(WBC)를 통해 실행되며, 이는 스킬별로 별도의 하위 수준 제어기를 사용하는 비공유 설계와 달리 일관된 폐루프 인터페이스를 제공합니다. 동일한 사전 훈련된 WBC를 단순히 재사용하면 새로운 스킬과 그 조합이 상태 및 명령 분포를 변화시켜 장기적인 수행에서 강건성이 저하될 수 있음을 발견했습니다. 이에 대해 도메인 무작위화 하에서 폐루프 스킬 실행의 롤아웃을 통해 공유 WBC 훈련을 보강하는 간단한 데이터 수집 절차를 제안합니다. 접근법 평가를 위해 장기적인 하노이 탑 상자 재배치 벤치마크인 Humanoid Hanoi를 도입하고, 시뮬레이션 및 Digit V3 휴머노이드 로봇에서의 결과를 보고하며, 확장된 기간 동안 완전 자율 재배치를 입증하고 공유 WBC 접근법의 비공유 기준선 대비 이점을 정량화합니다. 프로젝트 페이지: https://osudrl.github.io/Humanoid_Hanoi/
