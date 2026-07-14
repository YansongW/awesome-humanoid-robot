---
$id: ent_method_whole_body_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Whole-Body Control (WBC)
  zh: 全身控制（WBC）
  ko: 전신 제어(WBC)
summary:
  en: A control framework that coordinates all joints and contacts of a humanoid to achieve multiple tasks such as balance,
    gaze, and manipulation.
  zh: 协调人形机器人所有关节与接触点，以同时实现平衡、注视、操作等多任务的统一控制框架。
  ko: 휴로봇의 모든 관절과 접촉점을 조율하여 균형·시선·조작 등 다중 작업을 동시에 수행하는 제어 프레임워크.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_14
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body populated from chapter-08.md section "8.4.10 全身控制" by scripts/backfill_method_bodies_from_wiki.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
8.4.10 全身控制相关内容如下。

#### 8.4.10 全身控制
人形机器人同时需要完成多个任务：保持平衡、跟踪期望落脚点、操作物体、避免奇异与自碰撞。**全身控制（Whole-Body Control, WBC）**通过把多个任务映射到关节空间，并在冗余自由度中协调这些任务，是现代高动态人形机器人控制的核心框架[53][54][55]。

!!! note "术语解释：全身控制（WBC）、任务空间、冗余协调、多任务控制"
    - **全身控制（Whole-Body Control, WBC）**：同时协调全身多自由度完成多项任务的控制框架。
    - **任务空间（task space）**：描述特定任务变量的空间，如质心位置、末端位姿。
    - **冗余协调（redundancy resolution）**：在冗余自由度内分配任务优先级。
    - **多任务控制（multi-task control）**：同时实现多个可能相互冲突的任务目标。

## 参考
- 详见 chapter-08.md。

