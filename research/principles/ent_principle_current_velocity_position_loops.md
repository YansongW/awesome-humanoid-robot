---
$id: ent_principle_current_velocity_position_loops
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Current / Velocity / Position Control Loops
  zh: 电流环/速度环/位置环
  ko: 전류·속도·위치 제어 루프
summary:
  en: The nested feedback-control hierarchy for servo drives, where an inner current loop regulates torque, a velocity loop
    regulates speed, and an outer position loop regulates joint angle.
  zh: 伺服驱动的级联反馈控制层级：内环电流环控制转矩，中间速度环控制转速，外环位置环控制关节角度。
  ko: '서보 드라이브의 중첩 피드백 제어 계층: 내측 전류 루프는 토크, 속도 루프는 속도, 외측 위치 루프는 관절 각도를 제어.'
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- principle
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#4.5.5 电流环、速度环、位置环的级联控制 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
电流环/速度环/位置环是人形机器人领域的重要principle。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
实际关节驱动通常采用三级级联控制：最内层 **电流环**（力矩环），中间 **速度环**，最外层 **位置环**。每一层带宽约为下一层的 5-10 倍，以保证稳定性。

!!! note "术语解释：电流环、速度环、位置环、PI 控制器、前馈、抗饱和、带宽级联"
    - **电流环（current loop）**：以电机相电流为被控量的最快内环，直接决定输出力矩。
    - **速度环（velocity loop）**：以电机转速为被控量，输出电流指令。
    - **位置环（position loop）**：以关节角度为被控量，输出速度指令。
    - **PI 控制器（proportional-integral controller）**：由比例项和积分项组成的经典控制器，用于消除稳态误差。
    - **前馈（feedforward）**：根据期望轨迹提前计算并加入控制量，提高跟踪性能。
    - **抗饱和（anti-windup）**：防止积分器在饱和时过度累积，避免退出饱和后的大超调。
    - **带宽级联（bandwidth cascade）**：内环带宽远高于外环，确保外环指令能被内环快速跟踪。

```mermaid
flowchart TD
    P["位置指令 theta*"] --> PC["位置环 PI"]
    PC --> V["速度指令 omega*"]
    V --> VC["速度环 PI"]
    VC --> I["电流指令 I*"]
    I --> IC["电流环 PI"]
    IC --> INV["三相逆变器"]
    INV --> M["PMSM"]
    M --> ENC["编码器 theta"]
    ENC --> DIFF["omega = dtheta/dt"]
    DIFF --> VC
    ENC --> PC
    M --> CS["电流传感器"]
    CS --> IC
```

电流环带宽通常可达 1-5 kHz；速度环 50-500 Hz；位置环 5-100 Hz，具体取决于负载惯量、刚度和采样率。

## 参考
- Wiki extraction
- 项目 Wiki：chapter-04.md#4.5.5 电流环、速度环、位置环的级联控制

