---
$id: ent_component_dexterous_hand_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Dexterous Hand
  zh: 灵巧手
  ko: 민첩한 손
summary:
  en: Multi-fingered robotic end-effector with independent joint control, designed for human-like grasping and in-hand manipulation.
  zh: 具有独立关节控制的多指机器人末端执行器，用于类人抓取与手中操作。
  ko: 인간과 유사한 파지 및 손 안에서의 조작을 위해 설계된 독립적인 관절 제어가 가능한 다지 로봇 엔드 이펙터.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- hand
- dexterous
- grasping
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-09.md#9.4.2 灵巧手与夹爪：自由度、驱动与成本权衡 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Robotic Hand
  url: https://en.wikipedia.org/wiki/Robotic_hand
  date: '2024'
  accessed_at: '2026-07-13'
---
## 概述
灵巧手是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
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
- [Robotic Hand](https://en.wikipedia.org/wiki/Robotic_hand)
- 项目 Wiki：chapter-09.md#9.4.2 灵巧手与夹爪：自由度、驱动与成本权衡

