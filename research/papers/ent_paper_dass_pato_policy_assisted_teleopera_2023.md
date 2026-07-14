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
  zh: PATO是一种策略辅助遥操作系统，利用学得的分层辅助策略在示范数据采集过程中自主执行重复性子任务，并仅在不确定时请求人工输入，从而使一名操作员能够并行控制多个机器人。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.04708v2.
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
Large-scale data is an essential component of machine learning as demonstrated in recent advances in natural language processing and computer vision research. However, collecting large-scale robotic data is much more expensive and slower as each operator can control only a single robot at a time. To make this costly data collection process efficient and scalable, we propose Policy Assisted TeleOperation (PATO), a system which automates part of the demonstration collection process using a learned assistive policy. PATO autonomously executes repetitive behaviors in data collection and asks for human input only when it is uncertain about which subtask or behavior to execute. We conduct teleoperation user studies both with a real robot and a simulated robot fleet and demonstrate that our assisted teleoperation system reduces human operators' mental load while improving data collection efficiency. Further, it enables a single operator to control multiple robots in parallel, which is a first step towards scalable robotic data collection. For code and video results, see https://clvrai.com/pato

## 核心内容
Large-scale data is an essential component of machine learning as demonstrated in recent advances in natural language processing and computer vision research. However, collecting large-scale robotic data is much more expensive and slower as each operator can control only a single robot at a time. To make this costly data collection process efficient and scalable, we propose Policy Assisted TeleOperation (PATO), a system which automates part of the demonstration collection process using a learned assistive policy. PATO autonomously executes repetitive behaviors in data collection and asks for human input only when it is uncertain about which subtask or behavior to execute. We conduct teleoperation user studies both with a real robot and a simulated robot fleet and demonstrate that our assisted teleoperation system reduces human operators' mental load while improving data collection efficiency. Further, it enables a single operator to control multiple robots in parallel, which is a first step towards scalable robotic data collection. For code and video results, see https://clvrai.com/pato

## 参考
- http://arxiv.org/abs/2212.04708v2

