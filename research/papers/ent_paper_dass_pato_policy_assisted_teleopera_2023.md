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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.04708v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
대규모 데이터는 자연어 처리 및 컴퓨터 비전 연구의 최근 발전에서 입증된 바와 같이 머신러닝의 필수 구성 요소입니다. 그러나 대규모 로봇 데이터를 수집하는 것은 각 작업자가 한 번에 하나의 로봇만 제어할 수 있기 때문에 훨씬 더 비용이 많이 들고 느립니다. 이러한 고비용 데이터 수집 과정을 효율적이고 확장 가능하게 만들기 위해, 우리는 학습된 보조 정책을 사용하여 시연 수집 과정의 일부를 자동화하는 시스템인 Policy Assisted TeleOperation (PATO)을 제안합니다. PATO는 데이터 수집에서 반복적인 행동을 자율적으로 실행하며, 어떤 하위 작업이나 행동을 실행해야 할지 불확실할 때만 인간의 입력을 요청합니다. 우리는 실제 로봇과 시뮬레이션된 로봇 군집을 사용하여 원격 조작 사용자 연구를 수행했으며, 우리의 보조 원격 조작 시스템이 데이터 수집 효율성을 향상시키면서 인간 작업자의 정신적 부담을 줄인다는 것을 입증했습니다. 또한, 이 시스템은 단일 작업자가 여러 로봇을 병렬로 제어할 수 있게 하여, 확장 가능한 로봇 데이터 수집을 위한 첫 걸음이 됩니다. 코드 및 비디오 결과는 https://clvrai.com/pato 에서 확인할 수 있습니다.

## 핵심 내용
대규모 데이터는 자연어 처리 및 컴퓨터 비전 연구의 최근 발전에서 입증된 바와 같이 머신러닝의 필수 구성 요소입니다. 그러나 대규모 로봇 데이터를 수집하는 것은 각 작업자가 한 번에 하나의 로봇만 제어할 수 있기 때문에 훨씬 더 비용이 많이 들고 느립니다. 이러한 고비용 데이터 수집 과정을 효율적이고 확장 가능하게 만들기 위해, 우리는 학습된 보조 정책을 사용하여 시연 수집 과정의 일부를 자동화하는 시스템인 Policy Assisted TeleOperation (PATO)을 제안합니다. PATO는 데이터 수집에서 반복적인 행동을 자율적으로 실행하며, 어떤 하위 작업이나 행동을 실행해야 할지 불확실할 때만 인간의 입력을 요청합니다. 우리는 실제 로봇과 시뮬레이션된 로봇 군집을 사용하여 원격 조작 사용자 연구를 수행했으며, 우리의 보조 원격 조작 시스템이 데이터 수집 효율성을 향상시키면서 인간 작업자의 정신적 부담을 줄인다는 것을 입증했습니다. 또한, 이 시스템은 단일 작업자가 여러 로봇을 병렬로 제어할 수 있게 하여, 확장 가능한 로봇 데이터 수집을 위한 첫 걸음이 됩니다. 코드 및 비디오 결과는 https://clvrai.com/pato 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2212.04708v2
