---
$id: ent_paper_learning_with_pycub_a_simulati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics'
  zh: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics'
  ko: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics'
summary:
  en: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics is a 2025 work on simulation benchmark
    for humanoid robots.'
  ko: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics is a 2025 work on simulation benchmark
    for humanoid robots.'
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
- learning_with_pycub
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01756v3.
sources:
- id: src_001
  type: paper
  title: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics (arXiv)'
  url: https://arxiv.org/abs/2506.01756
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present pyCub, an open-source physics-based simulation of the humanoid robot iCub, along with exercises to teach students the basics of humanoid robotics. Compared to existing iCub simulators (iCub SIM, iCub Gazebo), which require C++ code and YARP as middleware, pyCub works without YARP and with Python code. The complete robot with all articulations has been simulated, with two cameras in the eyes and the unique sensitive skin of the iCub comprising 4000 receptors on its body surface. The exercises range from basic control of the robot in velocity, joint, and Cartesian space to more complex tasks like gazing, grasping, or reactive control. The whole framework is written and controlled with Python, thus allowing to be used even by people with small or almost no programming practice. The exercises can be scaled to different difficulty levels. We tested the framework in two runs of a course on humanoid robotics. The simulation, exercises, documentation, Docker images, and example videos are publicly available at https://rustlluk.github.io/pyCub.

## 核心内容
We present pyCub, an open-source physics-based simulation of the humanoid robot iCub, along with exercises to teach students the basics of humanoid robotics. Compared to existing iCub simulators (iCub SIM, iCub Gazebo), which require C++ code and YARP as middleware, pyCub works without YARP and with Python code. The complete robot with all articulations has been simulated, with two cameras in the eyes and the unique sensitive skin of the iCub comprising 4000 receptors on its body surface. The exercises range from basic control of the robot in velocity, joint, and Cartesian space to more complex tasks like gazing, grasping, or reactive control. The whole framework is written and controlled with Python, thus allowing to be used even by people with small or almost no programming practice. The exercises can be scaled to different difficulty levels. We tested the framework in two runs of a course on humanoid robotics. The simulation, exercises, documentation, Docker images, and example videos are publicly available at https://rustlluk.github.io/pyCub.

## 参考
- http://arxiv.org/abs/2506.01756v3

