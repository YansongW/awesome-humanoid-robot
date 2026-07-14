---
$id: ent_paper_comfree_sim_a_gpu_parallelized_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and
    Control'
  zh: 'ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and
    Control'
  ko: 'ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and
    Control'
summary:
  en: 'ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and
    Control is a 2026 work on simulation benchmark for humanoid robots.'
  zh: 'ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and
    Control is a 2026 work on simulation benchmark for humanoid robots.'
  ko: 'ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and
    Control is a 2026 work on simulation benchmark for humanoid robots.'
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
- comfree_sim
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12185v2.
sources:
- id: src_001
  type: paper
  title: 'ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation
    and Control (arXiv)'
  url: https://arxiv.org/abs/2603.12185
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation
    and Control project page'
  url: https://irislab.tech/comfree-sim/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Physics simulation for contact-rich robotics is often bottlenecked by contact resolution: mainstream engines enforce non-penetration and Coulomb friction via complementarity constraints or constrained optimization, requiring per-step iterative solves whose cost grows superlinearly with contact density. We present ComFree-Sim, a GPU-parallelized analytical contact physics engine built on complementarity-free contact modeling. ComFree-Sim computes contact impulses in closed form via an impedance-style prediction--correction update in the dual cone of Coulomb friction. Contact computation decouples across contact pairs and becomes separable across cone facets, mapping naturally to GPU kernels and yielding near-linear runtime scaling with the number of contacts. We further extend the formulation to a unified 6D contact model capturing tangential, torsional, and rolling friction, and introduce a practical dual-cone impedance heuristic. ComFree-Sim is implemented in Warp and exposed through a MuJoCo-compatible interface as a drop-in backend alternative to MuJoCo Warp (MJWarp). Experiments benchmark penetration, friction behaviors, stability, and simulation runtime scaling against MJWarp, demonstrating near-linear scaling and 2--3 times higher throughput in dense contact scenes with comparable physical fidelity. We deploy ComFree-Sim in real-time MPC for in-hand dexterous manipulation on a real-world multi-fingered LEAP hand and in dynamics-aware motion retargeting, demonstrating that low-latency simulation yields higher closed-loop success rates and enables practical high-frequency control in contact-rich tasks.

## 核心内容
Physics simulation for contact-rich robotics is often bottlenecked by contact resolution: mainstream engines enforce non-penetration and Coulomb friction via complementarity constraints or constrained optimization, requiring per-step iterative solves whose cost grows superlinearly with contact density. We present ComFree-Sim, a GPU-parallelized analytical contact physics engine built on complementarity-free contact modeling. ComFree-Sim computes contact impulses in closed form via an impedance-style prediction--correction update in the dual cone of Coulomb friction. Contact computation decouples across contact pairs and becomes separable across cone facets, mapping naturally to GPU kernels and yielding near-linear runtime scaling with the number of contacts. We further extend the formulation to a unified 6D contact model capturing tangential, torsional, and rolling friction, and introduce a practical dual-cone impedance heuristic. ComFree-Sim is implemented in Warp and exposed through a MuJoCo-compatible interface as a drop-in backend alternative to MuJoCo Warp (MJWarp). Experiments benchmark penetration, friction behaviors, stability, and simulation runtime scaling against MJWarp, demonstrating near-linear scaling and 2--3 times higher throughput in dense contact scenes with comparable physical fidelity. We deploy ComFree-Sim in real-time MPC for in-hand dexterous manipulation on a real-world multi-fingered LEAP hand and in dynamics-aware motion retargeting, demonstrating that low-latency simulation yields higher closed-loop success rates and enables practical high-frequency control in contact-rich tasks.

## 参考
- http://arxiv.org/abs/2603.12185v2

