---
$id: ent_paper_teleopbench_a_simulator_centri_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation'
  zh: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation'
  ko: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation'
summary:
  en: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation is a 2025 work on teleoperation for
    humanoid robots.'
  zh: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation is a 2025 work on teleoperation for
    humanoid robots.'
  ko: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation is a 2025 work on teleoperation for
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
- humanoid
- teleopbench
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12748v2.
sources:
- id: src_001
  type: paper
  title: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2505.12748
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation project page'
  url: https://gorgeous2002.github.io/TeleOpBench/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Teleoperation is a cornerstone of embodied-robot learning, and bimanual dexterous teleoperation in particular provides rich demonstrations that are difficult to obtain with fully autonomous systems. While recent studies have proposed diverse hardware pipelines-ranging from inertial motion-capture gloves to exoskeletons and vision-based interfaces-there is still no unified benchmark that enables fair, reproducible comparison of these systems. In this paper, we introduce TeleOpBench, a simulator-centric benchmark tailored to bimanual dexterous teleoperation. TeleOpBench contains 30 high-fidelity task environments that span pick-and-place, tool use, and collaborative manipulation, covering a broad spectrum of kinematic and force-interaction difficulty. Within this benchmark we implement four representative teleoperation modalities-(i) MoCap, (ii) VR device, (iii) arm-hand exoskeletons, and (iv) monocular vision tracking-and evaluate them with a common protocol and metric suite. To validate that performance in simulation is predictive of real-world behavior, we conduct mirrored experiments on a physical dual-arm platform equipped with two 6-DoF dexterous hands. Across 10 held-out tasks we observe a strong correlation between simulator and hardware performance, confirming the external validity of TeleOpBench. TeleOpBench establishes a common yardstick for teleoperation research and provides an extensible platform for future algorithmic and hardware innovation. Codes is now available at https://github.com/cyjdlhy/TeleOpBench .

## 核心内容
Teleoperation is a cornerstone of embodied-robot learning, and bimanual dexterous teleoperation in particular provides rich demonstrations that are difficult to obtain with fully autonomous systems. While recent studies have proposed diverse hardware pipelines-ranging from inertial motion-capture gloves to exoskeletons and vision-based interfaces-there is still no unified benchmark that enables fair, reproducible comparison of these systems. In this paper, we introduce TeleOpBench, a simulator-centric benchmark tailored to bimanual dexterous teleoperation. TeleOpBench contains 30 high-fidelity task environments that span pick-and-place, tool use, and collaborative manipulation, covering a broad spectrum of kinematic and force-interaction difficulty. Within this benchmark we implement four representative teleoperation modalities-(i) MoCap, (ii) VR device, (iii) arm-hand exoskeletons, and (iv) monocular vision tracking-and evaluate them with a common protocol and metric suite. To validate that performance in simulation is predictive of real-world behavior, we conduct mirrored experiments on a physical dual-arm platform equipped with two 6-DoF dexterous hands. Across 10 held-out tasks we observe a strong correlation between simulator and hardware performance, confirming the external validity of TeleOpBench. TeleOpBench establishes a common yardstick for teleoperation research and provides an extensible platform for future algorithmic and hardware innovation. Codes is now available at https://github.com/cyjdlhy/TeleOpBench .

## 参考
- http://arxiv.org/abs/2505.12748v2

