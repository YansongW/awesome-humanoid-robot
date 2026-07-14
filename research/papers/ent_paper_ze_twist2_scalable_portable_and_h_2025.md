---
$id: ent_paper_ze_twist2_scalable_portable_and_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System'
  zh: TWIST2：可扩展、便携且整体化的人形机器人数据采集系统
  ko: 'TWIST2: 확장 가능하고 휴대 가능하며 전체적인 휴머노이드 데이터 수집 시스템'
summary:
  en: TWIST2 introduces a portable, mocap-free whole-body humanoid teleoperation and data collection system using PICO4U VR
    tracking and a low-cost 2-DoF neck, together with a hierarchical visuomotor policy for autonomous full-body control.
  zh: TWIST2 介绍了一种使用 PICO4U VR 追踪与低成本二自由度颈部的便携、无动作捕捉全身人形机器人遥操作与数据采集系统，并提出了用于自主全身控制的分层视觉运动策略。
  ko: TWIST2는 PICO4U VR 추적과 저비용 2-DoF 목을 활용한 휴대 가능하고 mocap이 불필요한 전신 휴머노이드 원격 조작 및 데이터 수집 시스템을 제안하며, 자율 전신 제어를 위한 계층적 시각-운동
    정책을 함께 소개한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- teleoperation
- whole_body_control
- visuomotor_policy
- data_collection
- humanoid
- mocap_free
- diffusion_policy
- egocentric_vision
- reinforcement_learning
- retargeting
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.02832v1.
sources:
- id: src_001
  type: paper
  title: 'TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System'
  url: https://arxiv.org/abs/2511.02832
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Large-scale data has driven breakthroughs in robotics, from language models to vision-language-action models in bimanual manipulation. However, humanoid robotics lacks equally effective data collection frameworks. Existing humanoid teleoperation systems either use decoupled control or depend on expensive motion capture setups. We introduce TWIST2, a portable, mocap-free humanoid teleoperation and data collection system that preserves full whole-body control while advancing scalability. Our system leverages PICO4U VR for obtaining real-time whole-body human motions, with a custom 2-DoF robot neck (cost around $250) for egocentric vision, enabling holistic human-to-humanoid control. We demonstrate long-horizon dexterous and mobile humanoid skills and we can collect 100 demonstrations in 15 minutes with an almost 100% success rate. Building on this pipeline, we propose a hierarchical visuomotor policy framework that autonomously controls the full humanoid body based on egocentric vision. Our visuomotor policy successfully demonstrates whole-body dexterous manipulation and dynamic kicking tasks. The entire system is fully reproducible and open-sourced at https://yanjieze.com/TWIST2 . Our collected dataset is also open-sourced at https://twist-data.github.io .

## 核心内容
Large-scale data has driven breakthroughs in robotics, from language models to vision-language-action models in bimanual manipulation. However, humanoid robotics lacks equally effective data collection frameworks. Existing humanoid teleoperation systems either use decoupled control or depend on expensive motion capture setups. We introduce TWIST2, a portable, mocap-free humanoid teleoperation and data collection system that preserves full whole-body control while advancing scalability. Our system leverages PICO4U VR for obtaining real-time whole-body human motions, with a custom 2-DoF robot neck (cost around $250) for egocentric vision, enabling holistic human-to-humanoid control. We demonstrate long-horizon dexterous and mobile humanoid skills and we can collect 100 demonstrations in 15 minutes with an almost 100% success rate. Building on this pipeline, we propose a hierarchical visuomotor policy framework that autonomously controls the full humanoid body based on egocentric vision. Our visuomotor policy successfully demonstrates whole-body dexterous manipulation and dynamic kicking tasks. The entire system is fully reproducible and open-sourced at https://yanjieze.com/TWIST2 . Our collected dataset is also open-sourced at https://twist-data.github.io .

## 参考
- http://arxiv.org/abs/2511.02832v1

