---
$id: ent_application_home_service
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: application_scenario
names:
  en: Home Service
  zh: 家庭服务
  ko: 가정 서비스
summary:
  en: The use of humanoid robots for domestic chores, security, entertainment, and eldercare within residential environments.
  zh: 在家庭环境中利用人形机器人完成家务、安防、娱乐与养老辅助。
  ko: 주거 환경에서 가사·보안·오락·노인 돌봄을 위해 휴로봇을 사용하는 적용.
domains:
- 11_applications_markets
layers:
- validation_markets
functional_roles:
- knowledge
tags:
- application
- chapter_27
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-09.md#9.10.4 UBTech Walker：家庭服务场景整机集成 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
家庭服务是人形机器人领域的重要application_scenario。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
Walker 系列面向家庭与商用服务场景，强调人机交互、安全与双臂操作能力。其躯干与头部设计注重外观亲和性，手臂自由度较多，手部可更换夹爪与灵巧手。与工厂物流机器人不同，服务场景要求机器人在有限空间内与人近距离互动，因此 Walker 的肩臂尺寸更接近人体比例，末端速度受限以满足协作安全标准；头部集成交互屏幕与表情灯带，可通过视觉与语音反馈建立用户信任。其手部采用可更换设计，可在二指夹爪与多指灵巧手之间切换，以兼顾简单递送与精细操作任务。

!!! note "术语解释：服务机器人、人机交互、双臂协调、可更换末端"
    - **服务机器人（service robot）**：在非工业环境中为人类提供服务的机器人。
    - **人机交互（Human-Robot Interaction, HRI）**：人与机器人之间的信息交换与协作。
    - **双臂协调（bimanual coordination）**：两只手臂协同完成任务。
    - **可更换末端（interchangeable end-effector）**：根据任务快速更换的手部工具。

Walker 子系统特点（公开资料）：

| 子系统 | 特点 |
|---|---|
| 下肢 | 双足步行，髋/膝/踝布局 |
| 躯干 | 电池与计算集成，可扩展模块 |
| 上肢 | 双臂 7-DOF，仿人臂长 |
| 手部 | 可换夹爪/灵巧手 |
| 头颈 | 显示屏+多相机，表情交互 |

```mermaid
flowchart TD
    A["Walker 整机"] --> B["双足下肢"]
    A --> C["双臂操作"]
    A --> D["可换手部"]
    A --> E["交互式头颈"]
    C --> F["家庭服务任务"]
    E --> G["人机交互"]
```

## 参考
- Wiki extraction
- 项目 Wiki：chapter-09.md#9.10.4 UBTech Walker：家庭服务场景整机集成

