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
    Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
使Linux内核大部分可抢占以提供确定性低延迟实时行为的内核补丁集，常用于机器人控制。

## 核心内容
### Linux RT-PREEMPT的定义与定位
Linux RT-PREEMPT属于 **software_platform** 类型。 所属领域包括：08_software_middleware。 价值链层级：intelligence。 使Linux内核大部分可抢占以提供确定性低延迟实时行为的内核补丁集，常用于机器人控制。 英文名称为 *Linux RT-PREEMPT*。 韩文名称为 *Linux RT-PREEMPT*。

### Linux RT-PREEMPT的工作原理与技术架构
Linux RT-PREEMPT的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用Linux RT-PREEMPT需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
Linux RT-PREEMPT已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- software_platform
- chapter_22
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键software_platform之一，Linux RT-PREEMPT在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction

