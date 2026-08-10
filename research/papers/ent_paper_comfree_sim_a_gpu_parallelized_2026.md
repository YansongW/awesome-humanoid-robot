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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12185v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1018 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2603.12185v2

## 개요
전통적인 접촉 시뮬레이션 엔진은 상보성 제약 또는 제약 최적화에 의존하기 때문에 계산 비용이 접촉 밀도에 따라 초선형적으로 증가하여, 접촉이 빈번한 로봇 시뮬레이션의 주요 병목 현상이 되었습니다. ComFree-Sim은 임피던스 기반 예측-수정 업데이트를 통해 쿨롱 마찰의 쌍대 원뿔에서 접촉 충격량을 직접 계산하여 반복 해법을 피합니다. 이 엔진은 접촉 계산을 독립적인 접촉 쌍으로 분리하고, 이를 다시 원뿔 면으로 분해하여 GPU 커널 병렬화에 자연스럽게 적합합니다. 실험 결과, ComFree-Sim은 MuJoCo Warp와 동등한 물리적 정확도를 유지하면서도 거의 선형적인 실행 시간 확장을 달성했으며, 밀집 접촉 시나리오에서 처리량이 2-3배 향상되었습니다. 이 엔진은 실제 세계의 다지 LEAP 손을 위한 실시간 모델 예측 제어 및 동역학 인식 동작 재타겟팅 작업에 성공적으로 적용되었습니다.

## 핵심 내용
### 방법 아키텍처
- **상보성 제약 없는 모델링**: ComFree-Sim은 전통적인 엔진에서 강제하는 비관통 및 쿨롱 마찰의 상보성 제약 또는 제약 최적화 방식을 버리고, 대신 해석적 형태로 접촉 충격량을 계산합니다.
- **폐쇄형 해 계산**: 임피던스 기반 예측-수정 업데이트를 통해 쿨롱 마찰의 쌍대 원뿔에서 접촉 충격량을 직접 해결하여, 각 단계의 반복 해법을 피합니다.
- **GPU 병렬화**: 접촉 계산이 접촉 쌍 간에 분리되고, 다시 마찰 원뿔의 각 원뿔 면으로 분해됩니다. 이러한 구조는 GPU 커널에 자연스럽게 매핑되어 접촉 수에 따른 거의 선형적인 실행 시간 확장을 구현합니다.
- **통합 6D 접촉 모델**: 전통적인 모델을 확장하여 접선, 비틀림 및 구름 마찰을 동시에 포착하고, 실용적인 쌍대 원뿔 임피던스 휴리스틱을 도입합니다.

### 구현 및 인터페이스
- **구현 프레임워크**: Warp 기반으로 구현되었으며, MuJoCo 호환 인터페이스를 통해 노출되어 MuJoCo Warp (MJWarp)의 플러그 앤 플레이 백엔드 대체 옵션으로 사용될 수 있습니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 관통, 마찰 거동, 안정성 및 시뮬레이션 실행 시간 확장 측면에서 MJWarp와 비교되었습니다.
- **성능 데이터**: 밀집 접촉 시나리오에서 ComFree-Sim은 거의 선형적인 실행 시간 확장을 보여주었으며, 처리량은 MJWarp의 2-3배이면서도 비교 가능한 물리적 충실도를 유지했습니다.
- **실제 배포**:
  - **실시간 MPC**: 실제 세계의 다지 LEAP 손에서 손 안의 정밀 조작을 수행하며, 낮은 지연 시간 시뮬레이션이 더 높은 폐루프 성공률을 가져왔습니다.
  - **동작 재타겟팅**: 동역학 인식 동작 재타겟팅 작업에서 실용적인 고주파 제어를 구현했습니다.

### 결론
ComFree-Sim은 해석적 계산과 GPU 병렬화를 통해 접촉이 빈번한 로봇 시뮬레이션의 계산 병목 현상을 효과적으로 해결하며, 물리적 정확도를 유지하면서 밀집 접촉 시나리오의 시뮬레이션 속도를 크게 향상시켰습니다. 또한 실제 로봇 제어 작업에서 그 실용적 가치를 검증했습니다.
