---
$id: ent_method_action_chunking_transformer
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Action Chunking with Transformers (ACT)
  zh: 动作分块变压器（ACT）
  ko: 트랜스포머를 이용한 행동 청킹(ACT)
summary:
  en: An imitation-learning method that predicts a sequence of future actions as a chunk using a transformer, reducing compounding
    errors in long-horizon tasks.
  zh: 核心内容 配电系统把电池能量安全地输送到各负载，并在故障时快速切断。与消费电子产品不同，人形机器人的配电网络同时承载千瓦级瞬时功率、数十个低压子系统和高频 PWM 电机驱动电流，任何单一保护器件的误动作或失效都可能引发整机停机甚至安全事故。因此，配电与保护设计必须回到电路理论、电磁学、热学和功能安全标准，进行定量分析与协调配置。
  ko: 트랜스포머로 미래 행동 시퀀스를 한 덩어리로 예측하여 장기 과제의 오차 누적을 줄이는 모방 학습 방법.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_18
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-06.md#6.5.4 配电与保护：fuses, contactors, E-stop, hot-swap, harness sizing by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
动作分块变压器（ACT）是人形机器人领域的重要method。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
配电系统把电池能量安全地输送到各负载，并在故障时快速切断。与消费电子产品不同，人形机器人的配电网络同时承载千瓦级瞬时功率、数十个低压子系统和高频 PWM 电机驱动电流，任何单一保护器件的误动作或失效都可能引发整机停机甚至安全事故。因此，配电与保护设计必须回到电路理论、电磁学、热学和功能安全标准，进行定量分析与协调配置。

!!! note "术语解释：熔断器、接触器、急停、热插拔、线束、继电器、保护协调、分断能力"
    - **熔断器（fuse）**：过流时通过熔体熔化切断电路的一次性保护元件。
    - **接触器（contactor）**：大电流电磁开关，用于接通/断开主电路，通常具备灭弧能力。
    - **急停（E-stop, emergency stop）**：紧急情况下立即切断动力的安全装置，通常要求符合 ISO 13850 或 IEC 60947-5-5。
    - **热插拔（hot-swap）**：在不关闭系统的情况下更换电池或模块，需要抑制插拔浪涌电流。
    - **线束（wire harness）**：连接各子系统的导线和连接器集合，需注意截面积、压降、温升和屏蔽。
    - **继电器（relay）**：电控开关，用于小电流控制大电流回路。
    - **保护协调（protection coordination）**：确保上下级保护器件在故障时按正确顺序动作，避免越级跳闸。
    - **分断能力（breaking capacity / interrupting rating）**：保护器件能安全切断的最大故障电流。

## 参考
- Wiki extraction
- 项目 Wiki：chapter-06.md#6.5.4 配电与保护：fuses, contactors, E-stop, hot-swap, harness sizing


