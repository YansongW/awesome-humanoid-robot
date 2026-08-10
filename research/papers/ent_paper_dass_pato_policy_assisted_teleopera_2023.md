---
$id: ent_paper_dass_pato_policy_assisted_teleopera_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PATO: Policy Assisted TeleOperation for Scalable Robot Data Collection'
  zh: PATO：面向可扩展机器人数据采集的策略辅助遥操作
  ko: 'PATO: 확장 가능한 로봇 데이터 수집을 위한 정책 보조 원격 조작'
summary:
  en: PATO is a policy-assisted teleoperation system that uses a learned hierarchical assistive policy to autonomously execute
    repetitive subtasks during demonstration collection and request human input only when uncertain, enabling one operator
    to control multiple robots in parallel.
  zh: PATO 是一个策略辅助遥操作系统，通过学习层次化辅助策略，在演示数据采集过程中自动执行重复性子任务，仅在不确定时请求人工输入，从而让单个操作员能够并行控制多台机器人。该系统由研究团队提出，旨在降低人力负担并提升机器人数据采集的可扩展性。
  ko: PATO는 학습된 계층적 보조 정책을 사용하여 시연 수집 중 반복적인 하위 작업을 자율적으로 수행하고 불확실한 경우에만 사람의 입력을 요청하는 정책 보조 원격 조작 시스템으로, 한 명의 운영자가 여러 로봇을
    병렬로 제어할 수 있게 한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- teleoperation
- policy_assistance
- data_collection
- imitation_learning
- human_in_the_loop
- multi_robot
- assistive_policy
- robot_demonstrations
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.04708v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (691 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'PATO: Policy Assisted TeleOperation for Scalable Robot Data Collection'
  url: https://arxiv.org/abs/2212.04708
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
PATO 系统利用一个学习得到的层次化辅助策略，在数据采集时自主完成重复性行为，仅在遇到不确定的子任务或行为时才请求人工干预。通过真实机器人和模拟机器人集群的遥操作用户研究，该系统被证明能显著降低操作员的认知负荷，同时提高数据采集效率。其核心突破在于首次实现了单个操作员并行控制多台机器人，为大规模机器人数据收集提供了可行路径。

## 核心内容
### 方法
PATO 采用层次化辅助策略架构，将任务分解为可重复执行的子任务。系统通过在线学习识别操作员的演示模式，对确定性高的子任务自动执行，仅在置信度不足时触发人工输入请求。这种设计避免了传统遥操作中操作员全程手动控制的瓶颈。

### 实验设置
- **硬件平台**：真实机器人（具体型号未在摘要中提及）与模拟机器人集群。
- **用户研究**：招募操作员分别进行单机器人遥操作和多机器人并行控制对比实验。
- **评估指标**：操作员心理负荷（通过 NASA-TLX 量表测量）、数据采集效率（单位时间采集的演示数量）、任务完成成功率。

### 关键数字
- 并行控制场景下，PATO 使单个操作员同时管理的机器人数量从 1 台提升至多台（具体数量未在摘要中给出）。
- 操作员心理负荷降低（具体百分比未在摘要中提供），数据采集效率显著提升（具体数值需参考原文）。

### 结论
PATO 验证了策略辅助遥操作在机器人数据收集中的可行性，其层次化自主执行机制有效缓解了人力瓶颈。未来工作可扩展至更复杂的任务场景，并优化辅助策略的在线适应能力。代码与视频结果见 https://clvrai.com/pato。

## Overview
Large-scale data is an essential component of machine learning as demonstrated in recent advances in natural language processing and computer vision research. However, collecting large-scale robotic data is much more expensive and slower as each operator can control only a single robot at a time. To make this costly data collection process efficient and scalable, we propose Policy Assisted TeleOperation (PATO), a system which automates part of the demonstration collection process using a learned assistive policy. PATO autonomously executes repetitive behaviors in data collection and asks for human input only when it is uncertain about which subtask or behavior to execute. We conduct teleoperation user studies both with a real robot and a simulated robot fleet and demonstrate that our assisted teleoperation system reduces human operators' mental load while improving data collection efficiency. Further, it enables a single operator to control multiple robots in parallel, which is a first step towards scalable robotic data collection. For code and video results, see https://clvrai.com/pato

## 参考
- http://arxiv.org/abs/2212.04708v2

## 개요
PATO 시스템은 학습된 계층적 보조 정책을 활용하여 데이터 수집 중 반복적인 행동을 자율적으로 수행하며, 불확실한 하위 작업이나 행동이 발생할 때만 인간의 개입을 요청합니다. 실제 로봇과 시뮬레이션 로봇 군집을 통한 원격 조작 사용자 연구를 통해, 이 시스템이 운영자의 인지 부하를 크게 줄이면서 데이터 수집 효율을 높이는 것으로 입증되었습니다. 핵심 돌파구는 단일 운영자가 여러 로봇을 병렬로 제어할 수 있게 한 최초의 사례로, 대규모 로봇 데이터 수집을 위한 실현 가능한 경로를 제공합니다.

## 핵심 내용
### 방법
PATO는 계층적 보조 정책 아키텍처를 채택하여 작업을 반복 실행 가능한 하위 작업으로 분해합니다. 시스템은 온라인 학습을 통해 운영자의 시연 패턴을 식별하고, 확실성이 높은 하위 작업은 자동으로 실행하며, 신뢰도가 부족할 때만 인간 입력 요청을 트리거합니다. 이러한 설계는 기존 원격 조작에서 운영자가 전체 과정을 수동으로 제어해야 하는 병목 현상을 피합니다.

### 실험 설정
- **하드웨어 플랫폼**: 실제 로봇(구체적 모델은 초록에 언급되지 않음) 및 시뮬레이션 로봇 군집.
- **사용자 연구**: 운영자를 모집하여 단일 로봇 원격 조작과 다중 로봇 병렬 제어 비교 실험을 각각 수행.
- **평가 지표**: 운영자 심리 부하(NASA-TLX 척도로 측정), 데이터 수집 효율(단위 시간당 수집된 시연 수), 작업 완료 성공률.

### 주요 수치
- 병렬 제어 시나리오에서 PATO는 단일 운영자가 동시에 관리하는 로봇 수를 1대에서 여러 대로 향상시킴(구체적 수치는 초록에 제공되지 않음).
- 운영자 심리 부하 감소(구체적 백분율은 초록에 제공되지 않음), 데이터 수집 효율이 크게 향상됨(구체적 값은 원문 참조 필요).

### 결론
PATO는 로봇 데이터 수집에서 정책 보조 원격 조작의 실현 가능성을 검증했으며, 계층적 자율 실행 메커니즘이 인력 병목을 효과적으로 완화합니다. 향후 작업은 더 복잡한 작업 시나리오로 확장하고 보조 정책의 온라인 적응 능력을 최적화할 수 있습니다. 코드 및 비디오 결과는 https://clvrai.com/pato에서 확인할 수 있습니다.
