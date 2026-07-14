---
$id: ent_method_dexterous_manipulation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Dexterous Manipulation
  zh: 灵巧操作
  ko: 손재주 있는 조작
summary:
  en: The ability to manipulate objects with multi-fingered hands using fine finger motions, contact regulation, and in-hand
    reorientation.
  zh: 利用多指手的精细手指运动、接触调节与手中重定向来操作物体的能力。
  ko: 다지 손을 이용한 섬세한 손가락 움직임·접촉 조절·손 내 재배향으로 물체를 조작하는 능력.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_16
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body populated from chapter-09.md section "9.4.2 灵巧手与夹爪：自由度、驱动与成本权衡" by scripts/backfill_method_bodies_from_wiki.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
9.4.2 灵巧手与夹爪：自由度、驱动与成本权衡相关内容如下。

### 9.4.2 灵巧手与夹爪：自由度、驱动与成本权衡
机器人手部主要分为**多指灵巧手（dexterous hand）**与**二指/三指夹爪（gripper）**。灵巧手自由度高、适应性强，但控制复杂、成本高；夹爪结构简单、成本低，但只能完成有限抓取类型。

!!! note "术语解释：灵巧手、夹爪、欠驱动、全驱动、自适应抓取"
    - **灵巧手（dexterous hand）**：具有多手指、多自由度、可完成复杂操作的末端执行器。
    - **夹爪（gripper）**：通常自由度较少、结构简单的抓取装置。
    - **欠驱动（underactuated）**：执行器数量少于自由度，通过机械耦合传递运动。
    - **全驱动（fully actuated）**：每个自由度由独立执行器驱动。
    - **自适应抓取（adaptive grasp）**：手根据物体形状自动包络的抓取方式。

| 类型 | 自由度 | 驱动方式 | 优点 | 缺点 | 代表 |
|---|---|---|---|---|---|
| 全驱动灵巧手 | 16–24 | 电机/腱/直驱 | 高灵巧 | 复杂、贵 | Shadow Hand、HIT Hand |
| 欠驱动灵巧手 | 8–16 | 腱/杆/差动 | 自适应、轻 | 控制精度低 | Robotiq 3F、SVH |
| 二指夹爪 | 1–2 | 电机+丝杠 | 简单、可靠 | 类型受限 | Robotiq 2F |
| 软体手 | 多变 | 气动/线缆 | 顺应、安全 | 力控难 | RBO Hand、PneuNet |

```mermaid
flowchart TD
    A["手部选择"] --> B{"任务复杂度?"}
    B -->|"高"| C["多指灵巧手"]
    B -->|"中"| D["欠驱动三指手"]
    B -->|"低"| E["二指夹爪"]
    C --> F["高灵巧/高成本"]
    D --> G["自适应/中等成本"]
    E --> H["简单/低成本"]
```

## 参考
- 详见 chapter-09.md。

