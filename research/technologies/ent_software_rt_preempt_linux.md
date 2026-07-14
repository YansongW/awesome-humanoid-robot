---
$id: ent_software_rt_preempt_linux
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: software_platform
names:
  en: Linux RT-PREEMPT
  zh: Linux RT-PREEMPT
  ko: Linux RT-PREEMPT
summary:
  en: A Linux kernel patchset that makes most of the kernel preemptible to provide deterministic, low-latency real-time behavior
    for robot control.
  zh: 使Linux内核大部分可抢占以提供确定性低延迟实时行为的内核补丁集，常用于机器人控制。
  ko: Linux 커널 대부분을 선점 가능하게 만들어 결정적·저지연 실시간 동작을 제공하는 커널 패치 집합.
domains:
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
tags:
- software_platform
- chapter_22
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-06.md#6.4.7 实时 Linux：PREEMPT_RT、cyclictest 与线程优先级 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
Linux RT-PREEMPT是人形机器人领域的重要software_platform。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
人形机器人的关节电流环、力控和平衡控制通常要求 0.5–2 ms 的硬实时周期，而标准 Linux 内核的调度延迟往往在数十到数百微秒之间抖动，无法满足最严苛回路的确定性需求。PREEMPT_RT（Real-Time Preemption）补丁把通用 Linux 改造成接近硬实时的操作系统，使人形机器人的实时控制任务能够以可预测的延迟运行。

!!! note "术语解释：PREEMPT_RT、实时抢占、调度延迟、硬实时控制"
    - **PREEMPT_RT（Real-Time Preemption）**：一组使 Linux 内核几乎所有代码段都可被抢占的补丁/配置，目标是让调度延迟降到微秒级。
    - **实时抢占（real-time preemption）**：高优先级实时任务可以中断内核中的低优先级执行路径。
    - **调度延迟（scheduling latency）**：从事件发生（如定时器到期）到相应线程真正开始执行之间的时间差。
    - **硬实时控制（hard real-time control）**：必须在截止期限前完成，否则会导致系统失稳或危险的控制任务。

## 参考
- Wiki extraction
- 项目 Wiki：chapter-06.md#6.4.7 实时 Linux：PREEMPT_RT、cyclictest 与线程优先级

