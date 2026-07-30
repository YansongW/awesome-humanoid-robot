---
$id: ent_paper_neves_a_collaborative_robot_assisted_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Collaborative Robot-Assisted Manufacturing Assembly Process
  zh: 协作机器人辅助的制造装配过程
  ko: 협동 로봇 보조 제조 조립 공정
summary:
  en: Neves, Duarte, and Neto (2024) compare manual and robot-assisted assembly of a roller conveyor section using a KUKA
    LBR iiwa 7 R800 with a SCHUNK Co-act EGP-C 64 gripper, finding that collaborative operation improves ergonomics and reduces
    mental workload at the cost of a roughly 15% increase in assembly time.
  zh: Duarte 与 Neto（2024）对比了人工与机器人辅助装配滚轮输送段的过程，使用 KUKA LBR iiwa 7 R800 机械臂与 SCHUNK Co-act EGP-C 64 夹爪。研究发现协作操作改善了人体工学并降低了脑力负荷，但装配时间增加了约
    15%。
  ko: Neves, Duarte 및 Neto(2024)는 KUKA LBR iiwa 7 R800 로봇과 SCHUNK Co-act EGP-C 64 그리퍼를 이용해 롤러 컨베이어 섹션의 수동 및 로봇 보조 조립을 비교하였으며,
    협동 작업은 조립 시간이 약 15% 증가하는 대신 인체공학적 여건을 개선하고 정신적 부하를 낮춘다고 보고한다.
domains:
- 04_assembly_integration_testing
- 03_manufacturing_processes
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- process
tags:
- human_robot_collaboration
- collaborative_robot
- industrial_cobot
- manufacturing_assembly
- assembly_sequencing
- ergonomics
- third_hand
- task_allocation
- kuka_lbr_iiwa
- schunk_gripper
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.05306v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: A Collaborative Robot-Assisted Manufacturing Assembly Process
  url: https://arxiv.org/abs/2403.05306v1
  date: '2024'
  accessed_at: '2026-06-26'
---
## 概述
该研究通过对比人工与机器人辅助装配滚轮输送段，评估了协作机器人在共存、协作与协同三种模式下的有效性。实验采用 KUKA LBR iiwa 7 R800 机械臂与 SCHUNK Co-act EGP-C 64 夹爪，结果显示协作操作显著改善了人体工学条件并降低了操作者的脑力负荷，尽管装配时间增加了约 15%。机器人操作直观易用，能引导用户遵循正确的工序顺序。

## 核心内容
### 方法
- 对比人工装配与机器人辅助装配滚轮输送段的过程。
- 机器人辅助装配采用 KUKA LBR iiwa 7 R800 机械臂与 SCHUNK Co-act EGP-C 64 夹爪。
- 测试三种操作模式：共存、协作与协同。

### 实验设置
- 评估指标包括装配时间、人体工学条件与脑力负荷。
- 操作者需完成滚轮输送段的装配任务。

### 关键结果
- 协作操作改善了人体工学条件，降低了脑力负荷。
- 装配时间增加了约 15%，但未显著影响整体效率。
- 机器人操作直观，能引导用户遵循正确的工序顺序。

### 结论
- 协作机器人在工业装配中能提升操作者舒适度与安全性，但需权衡时间成本。
- 未来可进一步优化协作模式以缩短装配时间。

## Overview
An effective human-robot collaborative process results in the reduction of the operator's workload, promoting a more efficient, productive, safer and less error-prone working environment. However, the implementation of collaborative robots in industry is still challenging. In this work, we compare manual and robot-assisted assembly processes to evaluate the effectiveness of collaborative robots while featuring different modes of operation (coexistence, cooperation and collaboration). Results indicate an improvement in ergonomic conditions and ease of execution without substantially compromising assembly time. Furthermore, the robot is intuitive to use and guides the user on the proper sequencing of the process.

## 개요
효과적인 인간-로봇 협업 과정은 작업자의 업무 부담을 줄여주며, 보다 효율적이고 생산적이며 안전하고 오류 가능성이 낮은 작업 환경을 조성합니다. 그러나 산업 현장에서 협업 로봇의 도입은 여전히 어려운 과제로 남아 있습니다. 본 연구에서는 수동 조립 공정과 로봇 지원 조립 공정을 비교하여, 다양한 작동 모드(공존, 협력, 협업)에서 협업 로봇의 효과를 평가합니다. 결과는 조립 시간을 크게 희생하지 않으면서도 인체공학적 조건과 작업 용이성이 개선됨을 보여줍니다. 또한, 로봇은 직관적으로 사용할 수 있으며 사용자에게 적절한 공정 순서를 안내합니다.

## 핵심 내용
효과적인 인간-로봇 협업 과정은 작업자의 업무 부담을 줄여주며, 보다 효율적이고 생산적이며 안전하고 오류 가능성이 낮은 작업 환경을 조성합니다. 그러나 산업 현장에서 협업 로봇의 도입은 여전히 어려운 과제로 남아 있습니다. 본 연구에서는 수동 조립 공정과 로봇 지원 조립 공정을 비교하여, 다양한 작동 모드(공존, 협력, 협업)에서 협업 로봇의 효과를 평가합니다. 결과는 조립 시간을 크게 희생하지 않으면서도 인체공학적 조건과 작업 용이성이 개선됨을 보여줍니다. 또한, 로봇은 직관적으로 사용할 수 있으며 사용자에게 적절한 공정 순서를 안내합니다.

## 参考
- http://arxiv.org/abs/2403.05306v1
