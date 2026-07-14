---
$id: ent_application_logistics_warehouse
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: application_scenario
names:
  en: Logistics and Warehouse Automation
  zh: 物流仓储
  ko: 물류 및 창고 자동화
summary:
  en: The use of humanoid robots for picking, sorting, packing, and moving goods in logistics centers and warehouses.
  zh: 在物流中心与仓库中利用人形机器人进行拣选、分拣、包装与搬运。
  ko: 물류 센터와 창고에서 휴로봇을 이용한 피킹·분류·포장·운반 적용.
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
  notes: Body backfilled from chapter-08.md#8.9.4 Agility Digit：物流仓储专用人形 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
物流仓储是人形机器人领域的重要application_scenario。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
Agility Digit 定位于物流与仓储场景，设计强调在有限空间内搬运货物、上下台阶、长时间运行。

!!! note "术语解释：Digit、物流机器人、仓储自动化、末端配送"
    - **Digit**：Agility Robotics 开发的人形机器人。
    - **物流机器人（logistics robot）**：用于搬运、分拣、运输的机器人。
    - **仓储自动化（warehouse automation）**：利用机器人与系统自动完成仓储作业。
    - **末端配送（last-mile delivery）**：从配送中心到最终用户的最后一段物流。

Digit 的设计取舍包括：
- 腿部反屈膝（backward-bending knee）设计，便于下蹲搬运低处货物。
- 躯干上方设有货架空间，可在移动中暂存物品。
- 强调与现有仓库布局兼容，无需大幅改造环境。

```mermaid
flowchart TD
    A["Agility Digit"] --> B["反屈膝设计"]
    A --> C["躯干货架"]
    A --> D["紧凑机身"]
    B --> E["低位搬运"]
    C --> F["移动暂存"]
    D --> G["适配仓库通道"]
```

## 参考
- Wiki extraction
- 项目 Wiki：chapter-08.md#8.9.4 Agility Digit：物流仓储专用人形

