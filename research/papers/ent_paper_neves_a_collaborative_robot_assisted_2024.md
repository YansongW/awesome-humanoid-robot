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
  en: Neves, Duarte, and Neto (2024) compare manual and robot-assisted assembly of
    a roller conveyor section using a KUKA LBR iiwa 7 R800 with a SCHUNK Co-act EGP-C
    64 gripper, finding that collaborative operation improves ergonomics and reduces
    mental workload at the cost of a roughly 15% increase in assembly time.
  zh: Neves、Duarte 和 Neto（2024）使用 KUKA LBR iiwa 7 R800 机器人和 SCHUNK Co-act EGP-C 64
    夹爪，对比了人工与机器人辅助的滚筒输送机段装配过程，发现协作模式以装配时间增加约 15% 为代价，改善了人体工学并降低了心理负荷。
  ko: Neves, Duarte 및 Neto(2024)는 KUKA LBR iiwa 7 R800 로봇과 SCHUNK Co-act EGP-C 64
    그리퍼를 이용해 롤러 컨베이어 섹션의 수동 및 로봇 보조 조립을 비교하였으며, 협동 작업은 조립 시간이 약 15% 증가하는 대신 인체공학적
    여건을 개선하고 정신적 부하를 낮춘다고 보고한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the arXiv PDF; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: A Collaborative Robot-Assisted Manufacturing Assembly Process
  url: https://arxiv.org/abs/2403.05306v1
  date: '2024'
  accessed_at: '2026-06-26'
---

## Overview

Manufacturing assembly frequently forces human operators to perform complex, physically demanding tasks in non-ergonomic postures. This study addresses that problem by introducing a collaborative robot as a "third hand" in the assembly of a roller conveyor section, a real industrial use case. The work compares a purely manual assembly process with a human-robot collaborative process that spans three interaction modes: coexistence (shared space, separate workspace), cooperation (shared workspace, sequential tasks), and collaboration (shared workspace, simultaneous work with physical contact).

The experimental setup consists of a KUKA LBR iiwa 7 R800 collaborative robot equipped with a SCHUNK Co-act EGP-C 64 gripper. The assembly object has ten parts (P1–P10) plus components delivered in six boxes. In the collaborative scenario, the robot has two main functions: it brings boxes of small components and bolts to the operator in a prescribed sequence, and it holds larger parts in place while the operator fastens them. The operator triggers the robot sequence with a single input button and, when needed, uses hand-guiding at the end-effector to position the robot intuitively. Communication with the robot is implemented through the iiwaPy3 library.

Results show that the manual assembly took about six minutes, whereas the collaborative process took approximately seven minutes, corresponding to a 15% increase in task duration. Despite the longer execution time, the authors report improved ergonomic conditions, lower mental workload, a more organized workspace, and reduced risk of assembly-sequence errors, because the robot delivers the correct bolts for each step. The main limitation noted is the small number of trials, which prevented a thorough quantitative analysis of error reduction, and generalizability to other industries remains future work.

## Key Contributions

- Comparative evaluation of manual versus robot-assisted assembly across coexistence, cooperation, and collaboration modes.
- Demonstration of a collaborative robot as an intuitive "third hand" in a real industrial assembly use case.
- Quantified trade-off showing improved ergonomics and lower mental workload with only a 15% increase in assembly time.
- Identification of task allocation opportunities for collaborative robots in manufacturing assembly.

## Relevance to Humanoid Robotics

Humanoid robots are expected to operate alongside humans in mass-production assembly lines, where ergonomic assistance, task sequencing guidance, and safe mixed-initiative interaction are essential. This paper provides an empirical template for how such assistance can be structured: the robot augments the operator by delivering parts and acting as a third hand, while explicit modes of coexistence, cooperation, and collaboration define the level of shared workspace and physical contact. These findings are directly transferable to humanoid platforms that must share tight workspaces with human workers.

The study also highlights the practical trade-offs that matter for industrial adoption. A modest increase in cycle time can be acceptable if it yields measurable improvements in ergonomics, mental workload, and error avoidance. For humanoid robots entering manufacturing, this evidence supports the value proposition of helper roles that do not necessarily speed up every subtask but make the overall process safer, more intuitive, and less physically demanding.
