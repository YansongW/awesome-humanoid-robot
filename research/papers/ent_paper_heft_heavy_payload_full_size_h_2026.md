---
$id: ent_paper_heft_heavy_payload_full_size_h_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum'
  zh: HEFT：面向重载全尺寸人形的全身遥操作
  ko: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum'
summary:
  en: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum
    is a paper on Teleoperation for humanoid robotics. HEFT：面向重载全尺寸人形的全身遥操作.'
  zh: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum
    is a paper on Teleoperation for humanoid robotics. HEFT：面向重载全尺寸人形的全身遥操作.'
  ko: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum
    is a paper on Teleoperation for humanoid robotics. HEFT：面向重载全尺寸人形的全身遥操作.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- heft
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02332v1.
sources:
- id: src_001
  type: website
  title: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum'
  url: '2607.02332'
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
General motion tracking and teleoperation offer a promising path to scalable humanoid skill acquisition, yet most existing frameworks are validated on compact platforms or without real payload interaction, leaving full-size humanoids with real payloads largely unexplored. Scaling to full-size humanoids introduces two compounding challenges: their larger inertia and tighter balance margins make tracking highly sensitive to noise, drift, and retargeting errors from commodity VR trackers, while their payload potential remains largely underutilized. We present HEFT, a heavy-payload full-size humanoid teleoperation framework that addresses both challenges. HEFT learns from deployable noisy VR references with physically plausible reconstructed references through Privileged Motion Guidance (PMG), and uses a Windowed Payload Curriculum (WPC) with expert-guided payload caps to acquire robust heavy-payload tracking. We deploy HEFT on L7, a 175cm, 65kg humanoid. The robot tracks motions including turns, forward/backward locomotion, and squats under payloads up to 24kg.

## 核心内容
General motion tracking and teleoperation offer a promising path to scalable humanoid skill acquisition, yet most existing frameworks are validated on compact platforms or without real payload interaction, leaving full-size humanoids with real payloads largely unexplored. Scaling to full-size humanoids introduces two compounding challenges: their larger inertia and tighter balance margins make tracking highly sensitive to noise, drift, and retargeting errors from commodity VR trackers, while their payload potential remains largely underutilized. We present HEFT, a heavy-payload full-size humanoid teleoperation framework that addresses both challenges. HEFT learns from deployable noisy VR references with physically plausible reconstructed references through Privileged Motion Guidance (PMG), and uses a Windowed Payload Curriculum (WPC) with expert-guided payload caps to acquire robust heavy-payload tracking. We deploy HEFT on L7, a 175cm, 65kg humanoid. The robot tracks motions including turns, forward/backward locomotion, and squats under payloads up to 24kg.

## 参考
- http://arxiv.org/abs/2607.02332v1

