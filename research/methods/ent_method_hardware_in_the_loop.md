---
$id: ent_method_hardware_in_the_loop
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Hardware-in-the-Loop (HIL)
  zh: 硬件在环测试（HIL）
  ko: 하드웨어 인 더 루프(HIL)
summary:
  en: A validation method where real hardware controllers interact with a real-time simulation of the plant, enabling safe
    and repeatable testing of control software.
  zh: 真实硬件控制器与被控对象实时仿真模型交互的验证方法，可安全、可重复地测试控制软件。
  ko: 실제 하드웨어 컨트롤러가 플랜트의 실시간 시뮬레이션과 상호작용하여 제어 소프트웨어를 안전하고 반복 가능하게 검증하는 방법.
domains:
- 04_assembly_integration_testing
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_11
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-09.md#9.9.5 SiL/HiL：软件在环与硬件在环 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
硬件在环测试（HIL）是人形机器人领域的重要method。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
**SiL（Software-in-the-Loop）**在纯软件环境中验证控制算法；**HiL（Hardware-in-the-Loop）**将真实控制器与实时仿真模型连接，验证硬件接口与实时性能。

!!! note "术语解释：SiL、HiL、实时仿真、 plant model、控制器"
    - **SiL（软件在环）**：算法在仿真环境中运行的验证方式。
    - **HiL（硬件在环）**：真实控制器与仿真被控对象连接的验证方式。
    - **实时仿真（real-time simulation）**：仿真步长与实际时间同步的仿真。
    - **plant model**：被控对象的数学模型。
    - **控制器（controller）**：执行控制算法的硬件或软件。

SiL/HiL 对比：

| 方式 | 控制器 | 被控对象 | 用途 |
|---|---|---|---|
| SiL | 软件模型 | 软件模型 | 算法开发、参数调优 |
| HiL | 真实硬件 | 实时仿真 | 接口验证、实时性、故障注入 |

```mermaid
flowchart TD
    A["控制算法"] --> B{"验证阶段"}
    B -->|"早期"| C["SiL: 仿真控制器 + 仿真机器人"]
    B -->|"中期"| D["HiL: 真实控制器 + 实时仿真机器人"]
    B -->|"后期"| E["实物测试台"]
```

## 参考
- Wiki extraction
- 项目 Wiki：chapter-09.md#9.9.5 SiL/HiL：软件在环与硬件在环

