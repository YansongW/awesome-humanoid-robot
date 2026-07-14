---
$id: ent_paper_extremcontrol_low_latency_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
  zh: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
  ko: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
summary:
  en: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control is a 2026 work on teleoperation for
    humanoid robots.'
  zh: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control is a 2026 work on teleoperation for
    humanoid robots.'
  ko: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control is a 2026 work on teleoperation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- extremcontrol
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11321v3.
sources:
- id: src_001
  type: paper
  title: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control (arXiv)'
  url: https://arxiv.org/abs/2602.11321
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Building a low-latency humanoid teleoperation system is essential for collecting diverse reactive and dynamic demonstrations. However, existing approaches rely on heavily pre-processed human-to-humanoid motion retargeting and position-only PD control, resulting in substantial latency that severely limits responsiveness and prevents tasks requiring rapid feedback and fast reactions. To address this problem, we propose ExtremControl, a low latency whole-body control framework that: (1) operates directly on SE(3) poses of selected rigid links, primarily humanoid extremities, to avoid full-body retargeting; (2) utilizes a Cartesian-space mapping to directly convert human motion to humanoid link targets; and (3) incorporates velocity feedforward control at low level to support highly responsive behavior under rapidly changing control interfaces. We further provide a unified theoretical formulation of ExtremControl and systematically validate its effectiveness through experiments in both simulation and real-world environments. Building on ExtremControl, we implement a low-latency humanoid teleoperation system that supports both optical motion capture and VR-based motion tracking, achieving end-to-end latency as low as 50ms and enabling highly responsive behaviors such as ping-pong ball balancing, juggling, and real-time return, thereby substantially surpassing the 200ms latency limit observed in prior work.

## 核心内容
Building a low-latency humanoid teleoperation system is essential for collecting diverse reactive and dynamic demonstrations. However, existing approaches rely on heavily pre-processed human-to-humanoid motion retargeting and position-only PD control, resulting in substantial latency that severely limits responsiveness and prevents tasks requiring rapid feedback and fast reactions. To address this problem, we propose ExtremControl, a low latency whole-body control framework that: (1) operates directly on SE(3) poses of selected rigid links, primarily humanoid extremities, to avoid full-body retargeting; (2) utilizes a Cartesian-space mapping to directly convert human motion to humanoid link targets; and (3) incorporates velocity feedforward control at low level to support highly responsive behavior under rapidly changing control interfaces. We further provide a unified theoretical formulation of ExtremControl and systematically validate its effectiveness through experiments in both simulation and real-world environments. Building on ExtremControl, we implement a low-latency humanoid teleoperation system that supports both optical motion capture and VR-based motion tracking, achieving end-to-end latency as low as 50ms and enabling highly responsive behaviors such as ping-pong ball balancing, juggling, and real-time return, thereby substantially surpassing the 200ms latency limit observed in prior work.

## 参考
- http://arxiv.org/abs/2602.11321v3

