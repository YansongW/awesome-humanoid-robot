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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.05306v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (525 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2403.05306v1

## Overview
This study evaluates the effectiveness of collaborative robots in coexistence, collaboration, and synergy modes by comparing manual and robot-assisted assembly of roller conveyor sections. The experiment utilized a KUKA LBR iiwa 7 R800 robotic arm and a SCHUNK Co-act EGP-C 64 gripper, and the results showed that collaborative operations significantly improved ergonomic conditions and reduced operators' mental workload, although assembly time increased by approximately 15%. The robot operation was intuitive and easy to use, guiding users to follow the correct sequence of procedures.

## Content
### Methods
- Compared the processes of manual assembly and robot-assisted assembly of roller conveyor sections.
- Robot-assisted assembly employed a KUKA LBR iiwa 7 R800 robotic arm and a SCHUNK Co-act EGP-C 64 gripper.
- Tested three operation modes: coexistence, collaboration, and synergy.

### Experimental Setup
- Evaluation metrics included assembly time, ergonomic conditions, and mental workload.
- Operators were required to complete the assembly task of the roller conveyor section.

### Key Results
- Collaborative operations improved ergonomic conditions and reduced mental workload.
- Assembly time increased by approximately 15%, but this did not significantly impact overall efficiency.
- Robot operation was intuitive and guided users to follow the correct sequence of procedures.

### Conclusions
- Collaborative robots can enhance operator comfort and safety in industrial assembly, but time costs must be weighed.
- Future work could further optimize collaboration modes to reduce assembly time.

## 개요
이 연구는 수동 조립과 로봇 보조 조립 롤러 컨베이어 구간을 비교하여, 공존, 협력, 협동의 세 가지 모드에서 협동 로봇의 효과성을 평가했습니다. 실험에는 KUKA LBR iiwa 7 R800 로봇 팔과 SCHUNK Co-act EGP-C 64 그리퍼가 사용되었으며, 협동 작업이 인체공학적 조건을 크게 개선하고 작업자의 인지 부하를 낮추는 것으로 나타났지만, 조립 시간은 약 15% 증가했습니다. 로봇 작업은 직관적이고 사용하기 쉬우며, 사용자가 올바른 공정 순서를 따르도록 안내할 수 있습니다.

## 핵심 내용
### 방법
- 수동 조립과 로봇 보조 조립 롤러 컨베이어 구간의 과정을 비교했습니다.
- 로봇 보조 조립에는 KUKA LBR iiwa 7 R800 로봇 팔과 SCHUNK Co-act EGP-C 64 그리퍼가 사용되었습니다.
- 공존, 협력, 협동의 세 가지 작업 모드를 테스트했습니다.

### 실험 설정
- 평가 지표에는 조립 시간, 인체공학적 조건, 인지 부하가 포함됩니다.
- 작업자는 롤러 컨베이어 구간의 조립 작업을 완료해야 합니다.

### 주요 결과
- 협동 작업은 인체공학적 조건을 개선하고 인지 부하를 낮췄습니다.
- 조립 시간은 약 15% 증가했지만, 전체 효율성에는 큰 영향을 미치지 않았습니다.
- 로봇 작업은 직관적이며, 사용자가 올바른 공정 순서를 따르도록 안내할 수 있습니다.

### 결론
- 협동 로봇은 산업 조립에서 작업자의 편안함과 안전성을 향상시킬 수 있지만, 시간 비용을 고려해야 합니다.
- 향후 협동 모드를 더욱 최적화하여 조립 시간을 단축할 수 있습니다.
