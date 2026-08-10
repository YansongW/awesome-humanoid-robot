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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.13850v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (901 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.13850v3

## 개요
이 연구는 휴머노이드 로봇의 상자 재배치 작업을 위해 재사용 가능한 스킬 기반의 장시간 실행 프레임워크를 제안한다. 모든 스킬은 공유된 작업 비의존적 전신 제어기(WBC)를 통해 실행되며, 스킬 조합을 위한 일관된 폐루프 인터페이스를 제공한다. 이는 각 스킬이 독립적인 하위 제어기를 사용하는 비공유 설계와 대조적이다. 연구는 사전 훈련된 WBC를 직접 재사용할 경우 새로운 스킬 및 그 조합으로 인해 상태와 명령 분포가 이동하여 장시간 견고성이 저하된다는 점을 발견했다. 이를 해결하기 위해 저자들은 도메인 무작위화 조건에서 폐루프 스킬 실행으로부터 데이터를 수집하여 공유 WBC 훈련을 강화하는 간단한 데이터 집계 방법을 제안한다. 이 방법을 평가하기 위해 Humanoid Hanoi 벤치마크(장시간 하노이 탑 상자 재배치 작업)를 도입하고, 시뮬레이션 및 Digit V3 휴머노이드 로봇에서 실험을 수행했다.

## 핵심 내용
### 방법 아키텍처
- **스킬 프레임워크**: 장시간 작업을 재사용 가능한 스킬 시퀀스(예: 잡기, 이동, 놓기)로 분해하며, 모든 스킬은 동일한 작업 비의존적 전신 제어기(WBC)를 통해 실행된다.
- **공유 WBC 설계**: 각 스킬에 대해 독립적으로 하위 제어기를 훈련하는 비공유 방법과 달리, 공유 WBC는 통합된 폐루프 인터페이스를 제공하여 스킬 조합을 단순화하고 일관성을 유지한다.
- **데이터 집계**: 사전 훈련된 WBC를 직접 재사용할 때 발생하는 장시간 견고성 저하 문제를 해결하기 위해, 도메인 무작위화 조건에서 폐루프 스킬 실행으로부터 롤아웃 데이터를 수집하여 공유 WBC 훈련을 강화한다.

### 실험 설정
- **벤치마크**: Humanoid Hanoi, 즉 장시간 하노이 탑 상자 재배치 작업을 도입하며, 로봇이 상자를 순서대로 목표 위치로 이동해야 한다.
- **하드웨어 플랫폼**: Digit V3 휴머노이드 로봇으로, 시뮬레이션 환경과 실제 로봇 모두에서 실험을 수행한다.
- **비교 기준**: 독립적인 하위 제어기를 사용하는 비공유 WBC 방법과 비교한다.

### 주요 결과
- 공유 WBC 방법은 장시간 작업에서 비공유 기준선보다 현저히 우수하여 완전 자율적인 상자 재배치를 달성했다.
- 데이터 집계는 상태 및 명령 분포 이동 문제를 효과적으로 완화하여 장시간 실행의 견고성을 향상시켰다.
- Digit V3 로봇에서 이 방법은 완전한 하노이 탑 작업을 성공적으로 완료하여 실제 시나리오에서의 실현 가능성을 검증했다.

### 결론
이 연구는 공유 전신 제어기와 데이터 집계의 결합이 휴머노이드 로봇의 장시간 조작 작업에서 효과적임을 입증하며, 스킬 조합 및 전신 제어에 대한 새로운 설계 방향을 제시한다.
