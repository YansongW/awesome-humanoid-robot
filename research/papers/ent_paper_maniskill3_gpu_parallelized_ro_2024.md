---
$id: ent_paper_maniskill3_gpu_parallelized_ro_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI'
  zh: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI'
  ko: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI'
summary:
  en: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
  zh: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
  ko: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- maniskill3
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.00425v2.
sources:
- id: src_001
  type: paper
  title: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI (arXiv)'
  url: https://arxiv.org/abs/2410.00425
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI project page'
  url: https://www.maniskill.ai/home
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Simulation has enabled unprecedented compute-scalable approaches to robot learning. However, many existing simulation frameworks typically support a narrow range of scenes/tasks and lack features critical for scaling generalizable robotics and sim2real. We introduce and open source ManiSkill3, the fastest state-visual GPU parallelized robotics simulator with contact-rich physics targeting generalizable manipulation. ManiSkill3 supports GPU parallelization of many aspects including simulation+rendering, heterogeneous simulation, pointclouds/voxels visual input, and more. Simulation with rendering on ManiSkill3 can run 10-1000x faster with 2-3x less GPU memory usage than other platforms, achieving up to 30,000+ FPS in benchmarked environments due to minimal python/pytorch overhead in the system, simulation on the GPU, and the use of the SAPIEN parallel rendering system. Tasks that used to take hours to train can now take minutes. We further provide the most comprehensive range of GPU parallelized environments/tasks spanning 12 distinct domains including but not limited to mobile manipulation for tasks such as drawing, humanoids, and dextrous manipulation in realistic scenes designed by artists or real-world digital twins. In addition, millions of demonstration frames are provided from motion planning, RL, and teleoperation. ManiSkill3 also provides a comprehensive set of baselines that span popular RL and learning-from-demonstrations algorithms.

## 核心内容
Simulation has enabled unprecedented compute-scalable approaches to robot learning. However, many existing simulation frameworks typically support a narrow range of scenes/tasks and lack features critical for scaling generalizable robotics and sim2real. We introduce and open source ManiSkill3, the fastest state-visual GPU parallelized robotics simulator with contact-rich physics targeting generalizable manipulation. ManiSkill3 supports GPU parallelization of many aspects including simulation+rendering, heterogeneous simulation, pointclouds/voxels visual input, and more. Simulation with rendering on ManiSkill3 can run 10-1000x faster with 2-3x less GPU memory usage than other platforms, achieving up to 30,000+ FPS in benchmarked environments due to minimal python/pytorch overhead in the system, simulation on the GPU, and the use of the SAPIEN parallel rendering system. Tasks that used to take hours to train can now take minutes. We further provide the most comprehensive range of GPU parallelized environments/tasks spanning 12 distinct domains including but not limited to mobile manipulation for tasks such as drawing, humanoids, and dextrous manipulation in realistic scenes designed by artists or real-world digital twins. In addition, millions of demonstration frames are provided from motion planning, RL, and teleoperation. ManiSkill3 also provides a comprehensive set of baselines that span popular RL and learning-from-demonstrations algorithms.

## 参考
- http://arxiv.org/abs/2410.00425v2

