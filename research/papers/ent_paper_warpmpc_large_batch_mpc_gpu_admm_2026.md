---
$id: ent_paper_warpmpc_large_batch_mpc_gpu_admm_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WarpMPC: Large-Batch MPC on GPU via ADMM with Unrolled $LDL^\top$ Factorization'
  zh: 'WarpMPC: Large-Batch MPC on GPU via ADMM with Unrolled $LDL^\top$ Factorization'
  ko: 'WarpMPC: Large-Batch MPC on GPU via ADMM with Unrolled $LDL^\top$ Factorization'
summary:
  en: This paper introduces numerical optimizations for maximizing throughput on GPU when solving large batches (10,000 to
    over 100,000) of sequential quadratic programming (SQP) iterations, where all problems have the same structure. The optimizations
    are implemented in a toolbox WarpMPC for model-predictive control (MPC) in JAX and Warp. Based on the insight that all
    MPC problem instances in a batch.
  zh: WarpMPC 是一个基于 JAX 与 Warp 后端的 GPU 大批量 MPC 求解工具箱，通过 SQP、ADMM 与问题特定的展开稀疏 LDL^T 分解实现约束非线性 MPC 的高吞吐求解。其核心贡献在于将因子分解与 backsolve
    的依赖层级并行化，在批量超过 2000 时实现最高 12×（QP 求解）与 18×（灵敏度）加速，并在非线性基准上达到 8000 至 250000 SQP 迭代/秒。
  ko: This paper introduces numerical optimizations for maximizing throughput on GPU when solving large batches (10,000 to
    over 100,000) of sequential quadratic programming (SQP) iterations, where all problems have the same structure. The optimizations
    are implemented in a toolbox WarpMPC for model-predictive control (MPC) in JAX and Warp. Based on the insight that all
    MPC problem instances in a batch.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- warpmpc
- large
- batch
- mpc
- gpu
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.11603 WarpMPC: Large-Batch MPC on GPU via ADMM with Unrolled $LDL^\top$ Factorization'
  url: https://arxiv.org/abs/2607.11603
  date: '2026-07-13'
  accessed_at: '2026-08-05'
---

## 概述

WarpMPC 是一个基于 JAX 与 Warp 后端的 GPU 大批量 MPC 求解工具箱，通过 SQP、ADMM 与问题特定的展开稀疏 LDL^T 分解实现约束非线性 MPC 的高吞吐求解。其核心贡献在于将因子分解与 backsolve 的依赖层级并行化，在批量超过 2000 时实现最高 12×（QP 求解）与 18×（灵敏度）加速，并在非线性基准上达到 8000 至 250000 SQP 迭代/秒。

## 它改变了什么

现有 GPU MPC 求解器存在明显的吞吐量天花板：MPAX 因计算图反向传播无法处理线性 MPC 的灵敏度计算，密集 BoxOSQP 仅支持小批量且不优于单 CPU 核心，PCG 约束满足度差且提升满足度即牺牲吞吐量，TurboMPC 在大批量时因内存不足失败（cartpole 与 quadrotor 示例，humanoid 无法超过 B=512）。这些限制的本质在于：要么依赖稠密线性代数，要么缺乏问题特定的稀疏结构利用，要么将约束处理外包给惩罚项。

WarpMPC 真正改变的是「大批量约束 MPC 在 GPU 上是否可行」这一问题的答案。它不是简单地将 CPU 求解器移植到 GPU，而是从编译期生成、内存布局到依赖层级调度全链路重新设计，使得 10000 至 100000 批次的 SQP 迭代成为现实。其意义在于：将 MPC 从「单实例实时求解」的范式推向「批量并行训练/仿真」的范式，为神经网络策略蒸馏、大规模参数扫描等下游任务提供了数量级的速度提升。

## 方法拆解

### 整体架构
- 输入：CasADi 表达式，通过字符串替换生成 C 代码并翻译为 JAX 函数（编译时间最长 30 分钟，可缓存）。
- 求解器：SQP 外层（每控制环 1 至 10 次迭代），ADMM 内层（每次 SQP 迭代 25 至 100 次迭代）。
- 线性代数：问题特定的展开稀疏 LDL^T 分解，编译期生成 unrolled 因子分解与 backsolve 内核。

### 关键设计决策
- **内存布局优化**：针对 GPU 的 coalesced 访问模式重排数据，减少 padding 开销。
- **因子分解最优分段**：将 LDL^T 分解按依赖关系切分为可并行执行的层级，避免全局串行瓶颈。
- **backsolve 依赖层级调度**：将三角求解的依赖层级并行化，但该优势在大批量时减弱（与 Fig. 5 一致）。
- **精度**：默认单精度，双精度可用但内存受限（批量 50000 为上限）。

### 与基线对比的设置
- PCG 基线：Jacobi 预条件子，最大迭代 20，收敛容差 10^-5。
- MPAX 与 TurboMPC（cuDSS）作为后端接入 WarpMPC 的 SQP 与线搜索框架。
- 线性 MPC 基准额外对比单 CPU 核心 OSQP C 实现。

## 关键创新

1. **编译期生成的 unrolled LDL^T 分解**：将稀疏因子分解展开为无分支的指令序列，消除运行时索引开销与分支发散。这是对「问题特定稀疏模式」的极致利用，不同于通用稀疏求解器（如 cuDSS）的运行时调度。

2. **依赖层级调度的 backsolve 并行化**：将三角求解的串行依赖链按层级分组并行，这是对 GPU 上稀疏三角求解这一经典瓶颈的直接回应。其效果在大批量时减弱，但在中等批量（数千至数万）时是关键加速因素。

3. **吞吐量优先的全栈设计**：从 CasADi 到 JAX 的自动翻译、内存布局优化、因子分解分段三者协同，而非单一算法改进。这使得 100000 批次的 SQP 迭代成为可能，远超 [3] 的 1000 并行实例。

## 实验与结果

### 线性 MPC 基准
- 批量超过 2000 时优于所有基线，峰值吞吐量 279000 次求解/秒（无灵敏度）与 9570 次求解/秒（带灵敏度）。
- 相比 BoxOSQP 与 CPU OSQP，QP 求解最高 12× 加速，灵敏度计算最高 18× 加速。

### 非线性 MPC 基准（SQP 迭代/秒）
| 系统 | WarpMPC | TurboMPC | Jeon et al. | CPU OSQP |
|------|---------|----------|-------------|----------|
| Cartpole | 250000 | 论文未明确 | 论文未明确 | 论文未明确 |
| Quadrotor | 100000 | 论文未明确 | 论文未明确 | 论文未明确 |
| Humanoid | 8000 | 论文未明确 | 论文未明确 | 论文未明确 |

- WarpMPC 在三个非线性基准上超越 PCG、MPAX、TurboMPC（cuDSS）基线（批量超过 10000 时）。
- 相比最佳 PCG 吞吐量提升最高 24 倍；相比 TurboMPC，cartpole 提升 6 倍，quadrotor 提升 3 倍。
- MPAX 即使经过 1000 次 QP 迭代，闭环性能仍显著低于 ADMM。
- 相比 [3] 报告的 humanoid 2000 SQP RTI/秒，本文在更复杂公式（horizon 27 对 12）上实现接近 8000 SQP RTI/秒。

### 神经网络蒸馏
- 合成 20 百万个状态-动作对，3 隐藏层（每层 32 神经元，leaky ReLU），单 GPU 训练少于 4 分钟。
- 硬件实验：数据集合成 2 分钟，策略训练 1.7 分钟（wallclock），编译开销 11 分钟（可缓存），蒸馏网络在纳米四旋翼上以 100 Hz 运行。

## 边界与局限

- 仅支持固定稀疏模式的问题，不适用于一般优化问题。
- unrolled 内核在编译期生成，超大问题（如 humanoid 超过 100000 条指令）编译耗时。
- 仅支持 GPU 执行，不支持 CPU-only 部署。
- ADMM 超参数（σ、ω_rel、Γ）需针对每个问题手动调节，未自动化。
- 灵敏度计算假设 QP 解唯一且可微，退化问题不适用。
- 未实现二阶校正与线搜索回溯，可能影响高度非线性问题的收敛。
- 基准限于单精度，双精度性能未充分探索。
- 论文未明确：非线性基准表中 TurboMPC、Jeon et al.、CPU OSQP 的具体数值。

## 工程启示

复现或采用 WarpMPC 时，首先核对问题是否满足固定稀疏模式这一前提——这是编译期生成 unrolled 内核的基础，不满足则整个方法失效。其次，ADMM 超参数（σ、ω_rel、Γ）的调节是主要踩坑点，论文未提供自动化调参方案，建议从论文基准的默认值出发，针对自身问题做网格搜索。第三，批量大小是性能分水岭：低于 2000 时无优势，高于 10000 时才能充分发挥并行层级调度的收益；若目标批量在数千量级，需权衡编译开销（最长 30 分钟）与吞吐收益。最后，单精度是默认路径，双精度内存受限（批量上限 50000），若下游任务需要双精度，需提前评估内存预算。

## Overview
This paper introduces numerical optimizations for maximizing throughput on GPU when solving large batches (10,000 to over 100,000) of sequential quadratic programming (SQP) iterations, where all problems have the same structure. The optimizations are implemented in a toolbox WarpMPC for model-predictive control (MPC) in JAX and Warp. Based on the insight that all MPC problem instances in a batch share the same sparsity in time, cost, and constraints, we propose unrolling sparse linear factorizations and solves, which dominate alternating direction method of multipliers (ADMM) solver runtime. We avoid memory access bottlenecks and wasting computations via optimized memory layout, padding-reducing segmentation of the unrolled factorization, and dependency level scheduled backsolves, additionally accelerating sensitivity computation. We achieve throughputs of 8,000 to 250,000 SQP iterations per second on nonlinear cartpole, quadrotor, and humanoid robot benchmarks, outperforming baselines by 3$\times$ to 25$\times$. We illustrate practical usefulness by synthesizing a dataset and training a neural network approximation of an MPC in under 4 minutes that stabilizes a nano quadrotor in hardware experiments.

## 参考
- https://arxiv.org/abs/2607.11603

## 개요

WarpMPC는 JAX 및 Warp 백엔드를 기반으로 하는 GPU 대규모 배치 MPC 솔버 도구상자로, SQP, ADMM 및 문제 특화된 전개 희소 LDL^T 분해를 통해 제약 비선형 MPC의 고처리량 솔루션을 구현합니다. 핵심 기여는 인수분해와 backsolve의 의존성 계층을 병렬화하여 배치가 2000을 초과할 때 최대 12배(QP 솔루션) 및 18배(민감도) 가속을 달성하고, 비선형 벤치마크에서 초당 8000~250000 SQP 반복을 실현하는 데 있습니다.

## 무엇을 변화시키는가

기존 GPU MPC 솔버는 명확한 처리량 한계가 있습니다: MPAX는 계산 그래프 역전파가 선형 MPC의 민감도 계산을 처리할 수 없고, 밀집 BoxOSQP는 소규모 배치만 지원하며 단일 CPU 코어보다 우수하지 않으며, PCG는 제약 충족도가 낮고 충족도를 높이면 처리량이 희생되며, TurboMPC는 대규모 배치에서 메모리 부족으로 실패합니다(cartpole 및 quadrotor 예시, humanoid는 B=512를 초과할 수 없음). 이러한 한계의 본질은 밀집 선형 대수에 의존하거나, 문제 특화된 희소 구조 활용이 부족하거나, 제약 처리를 페널티 항으로 외주하는 데 있습니다.

WarpMPC가 실제로 변화시키는 것은 "대규모 배치 제약 MPC가 GPU에서 가능한가"라는 질문에 대한 답입니다. 단순히 CPU 솔버를 GPU로 이식하는 것이 아니라, 컴파일 타임 생성, 메모리 레이아웃, 의존성 계층 스케줄링까지 전 과정을 재설계하여 10000~100000 배치의 SQP 반복을 현실로 만듭니다. 그 의미는 MPC를 "단일 인스턴스 실시간 솔루션" 패러다임에서 "배치 병렬 훈련/시뮬레이션" 패러다임으로 전환하여, 신경망 정책 증류, 대규모 파라미터 스캔 등 하위 작업에 수십 배의 속도 향상을 제공하는 데 있습니다.

## 방법 분석

### 전체 아키텍처
- 입력: CasADi 표현식, 문자열 치환을 통해 C 코드를 생성하고 JAX 함수로 변환(컴파일 시간 최대 30분, 캐시 가능).
- 솔버: SQP 외부 루프(제어 루프당 1~10회 반복), ADMM 내부 루프(SQP 반복당 25~100회 반복).
- 선형 대수: 문제 특화된 전개 희소 LDL^T 분해, 컴파일 타임에 unrolled 인수분해 및 backsolve 커널 생성.

### 핵심 설계 결정
- **메모리 레이아웃 최적화**: GPU의 coalesced 접근 패턴에 맞춰 데이터를 재배열하여 padding 오버헤드 감소.
- **인수분해 최적 분할**: LDL^T 분해를 의존성에 따라 병렬 실행 가능한 계층으로 분할하여 전역 직렬 병목 방지.
- **backsolve 의존성 계층 스케줄링**: 삼각 솔루션의 의존성 계층을 병렬화하지만, 이 이점은 대규모 배치에서 감소합니다(Fig. 5와 일치).
- **정밀도**: 기본 단정밀도, 배정밀도 사용 가능하지만 메모리 제한(배치 50000 상한).

### 기준선 비교 설정
- PCG 기준선: Jacobi 사전조건자, 최대 반복 20, 수렴 허용 오차 10^-5.
- MPAX 및 TurboMPC(cuDSS)를 백엔드로 WarpMPC의 SQP 및 라인 서치 프레임워크에 통합.
- 선형 MPC 벤치마크는 추가로 단일 CPU 코어 OSQP C 구현과 비교.

## 핵심 혁신

1. **컴파일 타임 생성 unrolled LDL^T 분해**: 희소 인수분해를 분기 없는 명령 시퀀스로 전개하여 런타임 인덱싱 오버헤드와 분기 발산 제거. 이는 "문제 특화된 희소 패턴"의 극한 활용으로, 일반 희소 솔버(예: cuDSS)의 런타임 스케줄링과 다릅니다.

2. **의존성 계층 스케줄링 기반 backsolve 병렬화**: 삼각 솔루션의 직렬 의존성 체인을 계층별로 그룹화하여 병렬화, GPU에서 희소 삼각 솔루션의 고전적 병목에 대한 직접적 대응. 효과는 대규모 배치에서 감소하지만, 중간 배치(수천~수만)에서는 핵심 가속 요소입니다.

3. **처리량 우선 전체 스택 설계**: CasADi에서 JAX로의 자동 변환, 메모리 레이아웃 최적화, 인수분해 분할이 단일 알고리즘 개선이 아닌 협력적으로 작동. 이를 통해 100000 배치의 SQP 반복이 가능해져 [3]의 1000 병렬 인스턴스를 크게 초과합니다.

## 실험 및 결과

### 선형 MPC 벤치마크
- 배치가 2000을 초과할 때 모든 기준선보다 우수, 최대 처리량 279000 솔루션/초(민감도 없음) 및 9570 솔루션/초(민감도 포함).
- BoxOSQP 및 CPU OSQP 대비 QP 솔루션 최대 12배, 민감도 계산 최대 18배 가속.

### 비선형 MPC 벤치마크(SQP 반복/초)
| 시스템 | WarpMPC | TurboMPC | Jeon et al. | CPU OSQP |
|------|---------|----------|-------------|----------|
| Cartpole | 250000 | 논문 미명시 | 논문 미명시 | 논문 미명시 |
| Quadrotor | 100000 | 논문 미명시 | 논문 미명시 | 논문 미명시 |
| Humanoid | 8000 | 논문 미명시 | 논문 미명시 | 논문 미명시 |

- WarpMPC는 세 가지 비선형 벤치마크에서 PCG, MPAX, TurboMPC(cuDSS) 기준선을 능가합니다(배치 10000 초과 시).
- 최적 PCG 처리량 대비 최대 24배 향상; TurboMPC 대비 cartpole 6배, quadrotor 3배 향상.
- MPAX는 1000회 QP 반복 후에도 폐루프 성능이 ADMM보다 현저히 낮습니다.
- [3]이 보고한 humanoid 2000 SQP RTI/초 대비, 본 논문은 더 복잡한 공식(horizon 27 대 12)에서 약 8000 SQP RTI/초를 달성합니다.

### 신경망 증류
- 합성 2천만 개 상태-행동 쌍, 3개 은닉층(각 32 뉴런, leaky ReLU), 단일 GPU 훈련 4분 미만.
- 하드웨어 실험: 데이터셋 합성 2분, 정책 훈련 1.7분(wallclock), 컴파일 오버헤드 11분(캐시 가능), 증류 네트워크가 나노 쿼드로터에서 100 Hz로 실행.

## 경계 및 한계

- 고정 희소 패턴 문제만 지원, 일반 최적화 문제에는 부적합.
- unrolled 커널이 컴파일 타임에 생성되어 초대형 문제(예: humanoid 100000개 이상 명령)는 컴파일 시간이 오래 걸림.
- GPU 실행만 지원, CPU 전용 배포는 불가.
- ADMM 하이퍼파라미터(σ, ω_rel, Γ)는 문제별 수동 조정 필요, 자동화되지 않음.
- 민감도 계산은 QP 솔루션이 유일하고 미분 가능하다고 가정, 퇴화 문제에는 부적합.
- 2차 보정 및 라인 서치 백트래킹 미구현, 고도 비선형 문제의 수렴에 영향을 줄 수 있음.
- 벤치마크는 단정밀도에 국한, 배정밀도 성능은 충분히 탐구되지 않음.
- 논문 미명시: 비선형 벤치마크 표에서 TurboMPC, Jeon et al., CPU OSQP의 구체적 수치.

## 공학적 시사점

WarpMPC를 재현하거나 채택할 때, 먼저 문제가 고정 희소 패턴이라는 전제를 충족하는지 확인하세요——이는 컴파일 타임 unrolled 커널 생성의 기반이며, 충족하지 않으면 전체 방법이 무효화됩니다. 둘째, ADMM 하이퍼파라미터(σ, ω_rel, Γ) 조정이 주요 함정이며, 논문은 자동화된 조정 방안을 제공하지 않으므로 논문 벤치마크의 기본값에서 출발하여 자체 문제에 대해 그리드 서치를 권장합니다. 셋째, 배치 크기는 성능의 분기점입니다: 2000 미만에서는 이점이 없고, 10000 초과에서 병렬 계층 스케줄링의 이점을 충분히 발휘할 수 있습니다; 목표 배치가 수천 수준이라면 컴파일 오버헤드(최대 30분)와 처리량 이점을权衡해야 합니다. 마지막으로, 단정밀도가 기본 경로이며, 배정밀도는 메모리 제한(배치 상한 50000)이 있으므로 하위 작업이 배정밀도를 필요로 한다면 메모리 예산을 사전에 평가해야 합니다.
