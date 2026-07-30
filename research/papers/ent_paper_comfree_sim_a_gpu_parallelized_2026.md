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
  zh: ComFree-Sim 是一个基于 GPU 并行化的解析接触物理引擎，由研究团队于 2026 年提出，旨在解决高密度接触场景下机器人仿真的计算瓶颈。其核心贡献在于采用无互补约束的接触建模方法，通过闭式解计算接触冲量，实现了与接触数量近线性的运行时间缩放，并在密集接触场景中达到
    MuJoCo Warp 2-3 倍的吞吐量。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12185v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
传统接触仿真引擎因依赖互补约束或约束优化，其计算成本随接触密度超线性增长，成为接触丰富型机器人仿真的主要瓶颈。ComFree-Sim 通过阻抗式预测-校正更新在库仑摩擦对偶锥中直接计算接触冲量，避免了迭代求解。该引擎将接触计算解耦为独立接触对，并进一步分解至锥面，从而天然适配 GPU 内核并行化。实验表明，ComFree-Sim 在保持与 MuJoCo Warp 相当物理精度的同时，实现了近线性的运行时间缩放，并在密集接触场景中吞吐量提升 2-3 倍。该引擎已成功应用于真实世界多指 LEAP 手的实时模型预测控制与动力学感知运动重定向任务。

## 核心内容
### 方法架构
- **无互补约束建模**：ComFree-Sim 摒弃了传统引擎中强制非穿透与库仑摩擦的互补约束或约束优化方法，转而采用解析形式计算接触冲量。
- **闭式解计算**：通过阻抗式预测-校正更新，在库仑摩擦的对偶锥中直接求解接触冲量，避免了每步迭代求解。
- **GPU 并行化**：接触计算在接触对之间解耦，并进一步分解至摩擦锥的各个锥面，这种结构天然映射到 GPU 内核，实现了与接触数量近线性的运行时间缩放。
- **统一 6D 接触模型**：扩展了传统模型，同时捕捉切向、扭转和滚动摩擦，并引入实用的对偶锥阻抗启发式方法。

### 实现与接口
- **实现框架**：基于 Warp 实现，并通过与 MuJoCo 兼容的接口暴露，可作为 MuJoCo Warp (MJWarp) 的即插即用后端替代方案。

### 实验设置与关键结果
- **基准测试**：针对穿透、摩擦行为、稳定性和仿真运行时间缩放，与 MJWarp 进行了对比。
- **性能数据**：在密集接触场景中，ComFree-Sim 展现出近线性的运行时间缩放，吞吐量是 MJWarp 的 2-3 倍，同时保持了可比的物理保真度。
- **实际部署**：
  - **实时 MPC**：在真实世界多指 LEAP 手上进行手内灵巧操作，低延迟仿真带来了更高的闭环成功率。
  - **运动重定向**：在动力学感知运动重定向任务中，实现了实用的高频控制。

### 结论
ComFree-Sim 通过解析计算与 GPU 并行化，有效解决了接触丰富型机器人仿真中的计算瓶颈，在保持物理精度的同时大幅提升了密集接触场景的仿真速度，并已在真实机器人控制任务中验证了其实用价值。

## Overview
Physics simulation for contact-rich robotics is often bottlenecked by contact resolution: mainstream engines enforce non-penetration and Coulomb friction via complementarity constraints or constrained optimization, requiring per-step iterative solves whose cost grows superlinearly with contact density. We present ComFree-Sim, a GPU-parallelized analytical contact physics engine built on complementarity-free contact modeling. ComFree-Sim computes contact impulses in closed form via an impedance-style prediction--correction update in the dual cone of Coulomb friction. Contact computation decouples across contact pairs and becomes separable across cone facets, mapping naturally to GPU kernels and yielding near-linear runtime scaling with the number of contacts. We further extend the formulation to a unified 6D contact model capturing tangential, torsional, and rolling friction, and introduce a practical dual-cone impedance heuristic. ComFree-Sim is implemented in Warp and exposed through a MuJoCo-compatible interface as a drop-in backend alternative to MuJoCo Warp (MJWarp). Experiments benchmark penetration, friction behaviors, stability, and simulation runtime scaling against MJWarp, demonstrating near-linear scaling and 2--3 times higher throughput in dense contact scenes with comparable physical fidelity. We deploy ComFree-Sim in real-time MPC for in-hand dexterous manipulation on a real-world multi-fingered LEAP hand and in dynamics-aware motion retargeting, demonstrating that low-latency simulation yields higher closed-loop success rates and enables practical high-frequency control in contact-rich tasks.

## 개요
접촉이 많은 로봇 공학을 위한 물리 시뮬레이션은 종종 접촉 해석에 의해 병목 현상이 발생합니다. 주류 엔진은 상보성 제약 조건 또는 제약 최적화를 통해 비관통 및 쿨롱 마찰을 강제하며, 접촉 밀도에 따라 비용이 초선형적으로 증가하는 반복적 해법을 각 단계마다 필요로 합니다. 우리는 상보성 없는 접촉 모델링을 기반으로 구축된 GPU 병렬화 분석 접촉 물리 엔진인 ComFree-Sim을 제시합니다. ComFree-Sim은 쿨롱 마찰의 이중 원뿔에서 임피던스 스타일의 예측-보정 업데이트를 통해 폐쇄형으로 접촉 임펄스를 계산합니다. 접촉 계산은 접촉 쌍 간에 분리되고 원뿔 면에 걸쳐 분리 가능해져 GPU 커널에 자연스럽게 매핑되며, 접촉 수에 따라 거의 선형적인 런타임 확장성을 제공합니다. 우리는 또한 접선, 비틀림 및 구름 마찰을 포착하는 통합 6D 접촉 모델로 공식을 확장하고, 실용적인 이중 원뿔 임피던스 휴리스틱을 도입합니다. ComFree-Sim은 Warp로 구현되었으며 MuJoCo 호환 인터페이스를 통해 MuJoCo Warp(MJWarp)의 드롭인 백엔드 대안으로 제공됩니다. 실험은 MJWarp와 비교하여 관통, 마찰 거동, 안정성 및 시뮬레이션 런타임 확장성을 벤치마킹하며, 비슷한 물리적 충실도로 밀집 접촉 장면에서 거의 선형적인 확장성과 2~3배 높은 처리량을 보여줍니다. 우리는 실제 다지 LEAP 핸드를 사용한 손 안의 정밀 조작을 위한 실시간 MPC와 동역학 인식 모션 리타겟팅에 ComFree-Sim을 배포하여, 저지연 시뮬레이션이 더 높은 폐쇄 루프 성공률을 제공하고 접촉이 많은 작업에서 실용적인 고주파 제어를 가능하게 함을 입증합니다.

## 핵심 내용
접촉이 많은 로봇 공학을 위한 물리 시뮬레이션은 종종 접촉 해석에 의해 병목 현상이 발생합니다. 주류 엔진은 상보성 제약 조건 또는 제약 최적화를 통해 비관통 및 쿨롱 마찰을 강제하며, 접촉 밀도에 따라 비용이 초선형적으로 증가하는 반복적 해법을 각 단계마다 필요로 합니다. 우리는 상보성 없는 접촉 모델링을 기반으로 구축된 GPU 병렬화 분석 접촉 물리 엔진인 ComFree-Sim을 제시합니다. ComFree-Sim은 쿨롱 마찰의 이중 원뿔에서 임피던스 스타일의 예측-보정 업데이트를 통해 폐쇄형으로 접촉 임펄스를 계산합니다. 접촉 계산은 접촉 쌍 간에 분리되고 원뿔 면에 걸쳐 분리 가능해져 GPU 커널에 자연스럽게 매핑되며, 접촉 수에 따라 거의 선형적인 런타임 확장성을 제공합니다. 우리는 또한 접선, 비틀림 및 구름 마찰을 포착하는 통합 6D 접촉 모델로 공식을 확장하고, 실용적인 이중 원뿔 임피던스 휴리스틱을 도입합니다. ComFree-Sim은 Warp로 구현되었으며 MuJoCo 호환 인터페이스를 통해 MuJoCo Warp(MJWarp)의 드롭인 백엔드 대안으로 제공됩니다. 실험은 MJWarp와 비교하여 관통, 마찰 거동, 안정성 및 시뮬레이션 런타임 확장성을 벤치마킹하며, 비슷한 물리적 충실도로 밀집 접촉 장면에서 거의 선형적인 확장성과 2~3배 높은 처리량을 보여줍니다. 우리는 실제 다지 LEAP 핸드를 사용한 손 안의 정밀 조작을 위한 실시간 MPC와 동역학 인식 모션 리타겟팅에 ComFree-Sim을 배포하여, 저지연 시뮬레이션이 더 높은 폐쇄 루프 성공률을 제공하고 접촉이 많은 작업에서 실용적인 고주파 제어를 가능하게 함을 입증합니다.

## 参考
- http://arxiv.org/abs/2603.12185v2
