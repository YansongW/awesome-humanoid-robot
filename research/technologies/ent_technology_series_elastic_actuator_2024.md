---
$id: ent_technology_series_elastic_actuator_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: technology
names:
  en: Series Elastic Actuator
  zh: 串联弹性执行器
  ko: Series Elastic Actuator
summary:
  en: Actuator with an elastic element in series with the motor and load, enabling accurate force control and shock tolerance.
  zh: 在电机和负载之间串联弹性元件的执行器，可实现精确的力控和抗冲击能力。
  ko: 모터와 부하 사이에 탄성 요소를 직렬로 배치한 액추에이터, 정확한 힘 제어 및 충격 내성 가능.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- force_control
- safety
- sea
- series_elastic_actuator
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-04.md#4.4.2 串联弹性执行器（SEA） by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Series Elastic Actuator
  url: https://en.wikipedia.org/wiki/Series_elastic_actuator
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
串联弹性执行器是人形机器人领域的重要technology。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
1995 年 Pratt 与 Williamson 提出 **串联弹性执行器**（Series Elastic Actuator, SEA），在电机与输出端之间串入一个弹性体（弹簧或弹性扭杆）[1]。其基本思想是把力控问题转化为位移控制问题：输出力矩与弹簧变形成正比

$$
\tau_{\text{out}} = K_s \, (\theta_m/G - \theta_l)
$$

其中 \(K_s\) 为串联弹簧刚度，\(\theta_m\) 为电机转角，\(\theta_l\) 为负载输出转角，\(G\) 为减速比。通过测量弹簧两端的角度差即可估算输出力矩，无需昂贵的大力矩传感器。

## 参考
- [Series Elastic Actuator](https://en.wikipedia.org/wiki/Series_elastic_actuator)
- 项目 Wiki：chapter-04.md#4.4.2 串联弹性执行器（SEA）

