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
  zh: Humanoid Hanoi 是 2026 年关于人形机器人全身控制与操作的研究工作。其核心贡献在于提出一种基于共享全身控制器（WBC）的技能组合框架，并引入数据聚合方法提升长时域任务鲁棒性。该方法在 Digit V3 人形机器人上实现了全自主的汉诺塔箱子重排任务。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.13850v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement (arXiv)'
  url: https://arxiv.org/abs/2602.13850
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人形机器人箱子重排任务，提出了一种基于可复用技能的长时域执行框架。所有技能通过一个共享的、任务无关的全身控制器（WBC）执行，提供一致的闭环接口用于技能组合，这与每个技能使用独立底层控制器的非共享设计形成对比。研究发现，直接复用预训练的 WBC 会因新技能及其组合导致状态和指令分布偏移，从而降低长时域鲁棒性。为此，作者提出一种简单的数据聚合方法，通过在域随机化条件下从闭环技能执行中收集数据来增强共享 WBC 的训练。为评估该方法，研究引入了 Humanoid Hanoi 基准测试（长时域汉诺塔箱子重排任务），并在仿真和 Digit V3 人形机器人上进行了实验。

## 核心内容
### 方法架构
- **技能框架**：将长时域任务分解为可复用的技能序列（如抓取、移动、放置），所有技能通过同一个任务无关的全身控制器（WBC）执行。
- **共享 WBC 设计**：与每个技能独立训练底层控制器的非共享方法不同，共享 WBC 提供统一的闭环接口，简化技能组合并保持一致性。
- **数据聚合**：针对直接复用预训练 WBC 导致的长时域鲁棒性下降问题，提出在域随机化条件下，从闭环技能执行中收集 rollout 数据，用于增强共享 WBC 的训练。

### 实验设置
- **基准测试**：引入 Humanoid Hanoi，即长时域汉诺塔箱子重排任务，要求机器人将箱子按顺序移动到目标位置。
- **硬件平台**：Digit V3 人形机器人，在仿真环境和真实机器人上均进行实验。
- **对比基线**：与使用独立底层控制器的非共享 WBC 方法进行对比。

### 关键结果
- 共享 WBC 方法在长时域任务中显著优于非共享基线，实现了全自主的箱子重排。
- 数据聚合有效缓解了状态和指令分布偏移问题，提升了长时域执行的鲁棒性。
- 在 Digit V3 机器人上，该方法成功完成了完整的汉诺塔任务，验证了其在实际场景中的可行性。

### 结论
该工作证明了共享全身控制器结合数据聚合在人形机器人长时域操作任务中的有效性，为技能组合和全身控制提供了新的设计思路。

## Overview
We investigate a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level. In our architecture, all skills execute through a shared, task-agnostic whole-body controller (WBC), providing a consistent closed-loop interface for skill composition, in contrast to non-shared designs that use separate low-level controllers per skill. We find that naively reusing the same pretrained WBC can reduce robustness over long horizons, as new skills and their compositions induce shifted state and command distributions. We address this with a simple data aggregation procedure that augments shared-WBC training with rollouts from closed-loop skill execution under domain randomization. To evaluate the approach, we introduce Humanoid Hanoi, a long-horizon Tower-of-Hanoi box rearrangement benchmark, and report results in simulation and on the Digit V3 humanoid robot, demonstrating fully autonomous rearrangement over extended horizons and quantifying the benefits of the shared-WBC approach over non-shared baselines. Project page: https://osudrl.github.io/Humanoid_Hanoi/

## 개요
본 연구는 휴머노이드의 상자 재배치를 위한 스킬 기반 프레임워크를 조사하며, 작업 수준에서 재사용 가능한 스킬을 순차적으로 실행하여 장기적인 수행을 가능하게 합니다. 우리 아키텍처에서는 모든 스킬이 공유된 작업 비특화 전신 제어기(WBC)를 통해 실행되며, 이는 스킬별로 별도의 하위 수준 제어기를 사용하는 비공유 설계와 달리 일관된 폐루프 인터페이스를 제공합니다. 동일한 사전 훈련된 WBC를 단순히 재사용하면 새로운 스킬과 그 조합이 상태 및 명령 분포를 변화시켜 장기적인 수행에서 강건성이 저하될 수 있음을 발견했습니다. 이에 대해 도메인 무작위화 하에서 폐루프 스킬 실행의 롤아웃을 통해 공유 WBC 훈련을 보강하는 간단한 데이터 수집 절차를 제안합니다. 접근법 평가를 위해 장기적인 하노이 탑 상자 재배치 벤치마크인 Humanoid Hanoi를 도입하고, 시뮬레이션 및 Digit V3 휴머노이드 로봇에서의 결과를 보고하며, 확장된 기간 동안 완전 자율 재배치를 입증하고 공유 WBC 접근법의 비공유 기준선 대비 이점을 정량화합니다. 프로젝트 페이지: https://osudrl.github.io/Humanoid_Hanoi/

## 핵심 내용
본 연구는 휴머노이드의 상자 재배치를 위한 스킬 기반 프레임워크를 조사하며, 작업 수준에서 재사용 가능한 스킬을 순차적으로 실행하여 장기적인 수행을 가능하게 합니다. 우리 아키텍처에서는 모든 스킬이 공유된 작업 비특화 전신 제어기(WBC)를 통해 실행되며, 이는 스킬별로 별도의 하위 수준 제어기를 사용하는 비공유 설계와 달리 일관된 폐루프 인터페이스를 제공합니다. 동일한 사전 훈련된 WBC를 단순히 재사용하면 새로운 스킬과 그 조합이 상태 및 명령 분포를 변화시켜 장기적인 수행에서 강건성이 저하될 수 있음을 발견했습니다. 이에 대해 도메인 무작위화 하에서 폐루프 스킬 실행의 롤아웃을 통해 공유 WBC 훈련을 보강하는 간단한 데이터 수집 절차를 제안합니다. 접근법 평가를 위해 장기적인 하노이 탑 상자 재배치 벤치마크인 Humanoid Hanoi를 도입하고, 시뮬레이션 및 Digit V3 휴머노이드 로봇에서의 결과를 보고하며, 확장된 기간 동안 완전 자율 재배치를 입증하고 공유 WBC 접근법의 비공유 기준선 대비 이점을 정량화합니다. 프로젝트 페이지: https://osudrl.github.io/Humanoid_Hanoi/

## 参考
- http://arxiv.org/abs/2602.13850v3
