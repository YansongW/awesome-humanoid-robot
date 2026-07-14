---
$id: ent_method_gait_planning
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Gait Planning
  zh: 步态规划
  ko: 보행 패턴 계획
summary:
  en: The generation of footstep sequences, timing, and phase transitions that produce stable and efficient locomotion for
    legged robots.
  zh: 为腿足机器人生成稳定高效行走的足端落点序列、时机与相态转换。
  ko: 족욕 로봇의 안정적이고 효율적인 이동을 위해 보행 순서·시기·상태 전이를 생성하는 방법.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_15
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-08.md#运动范围与人类步态需求 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
步态规划是人形机器人领域的重要method。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
人类正常步态的关节运动范围（Range of Motion, ROM）为足部与腿部设计提供了重要参考：

| 关节 | 典型人类 ROM（步行） | 人形机器人设计目标 |
|---|---|---|
| 髋屈伸 | \(-30° \sim +30°\) | \(\pm 45°\) 以上 |
| 髋侧摆 | \(\pm 10°\) | \(\pm 20°\) 以上 |
| 髋旋转 | \(\pm 10°\) | \(\pm 30°\) 以上 |
| 膝屈伸 | \(0° \sim +60°\) | \(0° \sim +90°\) 以上 |
| 踝背屈/跖屈 | \(-10° \sim +20°\) | \(-20° \sim +30°\) 以上 |
| 踝内外翻 | \(\pm 5°\) | \(\pm 15°\) 以上 |

!!! note "术语解释：运动范围（ROM）、髋屈伸、髋侧摆、踝背屈/跖屈、踝内外翻"
    - **运动范围（Range of Motion, ROM）**：关节可活动的角度范围。
    - **髋屈伸（hip flexion/extension）**：大腿绕髋部前后摆动。
    - **髋侧摆（hip abduction/adduction）**：大腿绕髋部左右摆动。
    - **踝背屈/跖屈（ankle dorsiflexion/plantarflexion）**：脚背向上/脚尖向下的运动。
    - **踝内外翻（ankle inversion/eversion）**：脚掌绕前后轴向内/向外倾斜。

机器人关节 ROM 通常大于人类步行所需，以保留上下楼梯、跨越障碍、下蹲等动作余量。但过大的 ROM 会牺牲结构刚度与紧凑性，因此需在关节限位处设置软限位与硬限位双重保护。

```mermaid
flowchart TD
    A["人类步态 ROM 数据"] --> B["确定机器人关节 ROM 目标"]
    B --> C["结构/驱动设计"]
    C --> D["运动仿真验证"]
    D --> E{"满足任务?"}
    E -->|"否"| F["增加 ROM 或改变构型"]
    F --> C
    E -->|"是"| G["设置软硬限位"]
```

## 参考
- Wiki extraction
- 项目 Wiki：chapter-08.md#运动范围与人类步态需求

