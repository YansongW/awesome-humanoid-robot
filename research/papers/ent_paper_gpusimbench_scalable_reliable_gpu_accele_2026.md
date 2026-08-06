---
$id: ent_paper_gpusimbench_scalable_reliable_gpu_accele_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI'
  zh: 'GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI'
  ko: 'GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI'
summary:
  en: Data-driven embodied AI is rapidly transitioning into a paradigm that scales training through massively parallel simulation,
    where GPU-accelerated simulators serve as the foundational data infrastructure. However, as computational throughput scales,
    the underlying trade-offs between parallel efficiency, physical fidelity, and execution determinism remain largely unexamined,
    hindering the.
  zh: GPUSimBench 是一个面向具身智能 GPU 加速模拟器的标准化基准，由作者团队提出，用于系统评估主流模拟器（Isaac Lab、Genesis、Madrona、ManiSkill、MJX、MuJoCo Warp、Playground）在并行可扩展性、物理一致性和计算确定性三个维度的表现。核心贡献在于首次将“并行变异性”与“运行间变异性”作为独立指标引入模拟器评估，并揭示了不同编程抽象（数组式、内核式、任务中心、ECS）对仿真可靠性的根本性影响。
  ko: Data-driven embodied AI is rapidly transitioning into a paradigm that scales training through massively parallel simulation,
    where GPU-accelerated simulators serve as the foundational data infrastructure. However, as computational throughput scales,
    the underlying trade-offs between parallel efficiency, physical fidelity, and execution determinism remain largely unexamined,
    hindering the.
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
- gpusimbench
- scalable
- reliable
- gpu
- accele
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
  title: 'arXiv:2607.13059 GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodie'
  url: https://arxiv.org/abs/2607.13059
  date: '2026-07-06'
  accessed_at: '2026-08-05'
---

## 概述

GPUSimBench 是一个面向具身智能 GPU 加速模拟器的标准化基准，由作者团队提出，用于系统评估主流模拟器（Isaac Lab、Genesis、Madrona、ManiSkill、MJX、MuJoCo Warp、Playground）在并行可扩展性、物理一致性和计算确定性三个维度的表现。核心贡献在于首次将“并行变异性”与“运行间变异性”作为独立指标引入模拟器评估，并揭示了不同编程抽象（数组式、内核式、任务中心、ECS）对仿真可靠性的根本性影响。

## 它改变了什么

过去对 GPU 模拟器的评价几乎完全聚焦于任务级成功率或峰值吞吐量，默认并行执行只是“更快的顺序模拟”。GPUSimBench 改变了这一认知框架：它证明 GPU 批量执行并非透明加速层，而是会引入两类独立的非确定性——同一批次内不同环境间的结果发散（并行变异性），以及相同种子下多次运行的分布漂移（运行间变异性）。这两类变异性的组合直接决定了模拟器能否用于需要严格可复现的科学实验或策略评估。

更关键的是，该基准将“物理一致性”从定性讨论变为可量化指标：通过受控斜面碰撞任务，用物理单位（厘米）的推土机距离（EMD）度量模拟分布与真实世界分布的偏差。这迫使模拟器开发者直面一个此前被回避的问题——并行化带来的数值扰动并非随机噪声，而是系统性地改变了接触动力学行为，例如 Madrona 因 XPBD 求解器摩擦力不足导致 EMD 高达 211.60±2.22cm，而 ManiSkill 仅 2.520±0.000cm，两者相差两个数量级。

## 方法拆解

### 基准架构
GPUSimBench 将评估拆解为三个正交维度，每个维度有独立协议：
- **可扩展性**：在自由落体立方体阵列（3×3×3）和 Franka 机械臂随机动作（含自碰撞）两个场景下，测量不同并行环境数 N_env 的吞吐量（FPS = (N_env × N_step) / T_step）和峰值内存增量（M_usage = M_peak − M_base）。
- **物理一致性**：设计斜面碰撞任务（斜面角度 20°，立方体边长 0.02m，质量 0.005kg），在 N_env=16 并行环境和 K=16 次真实试验中，记录 t_s=5.0s 时所有立方体的 xy 位置，用六边形分箱和对数密度映射（D_b = log10(max(c_b, 1))）可视化分布。
- **确定性**：通过 R=10 次独立运行，区分四种随机性类型（Type 1–4），由并行变异性（W̄1^parallel）和运行间变异性（W̄1^run-to-run）的有无组合定义。

### 关键度量公式
- **并行变异性**：基于分配的 EMD，W1(e,e') = min_{π∈S_n} (1/n) Σ ||x_{e,i} − x_{e',π(i)}||_2，汇总为平均成对 EMD W̄1^parallel。
- **真实世界对齐**：模拟与真实分布的物理单位 EMD，d_EMD,phys^sim = W1^phys(X^sim, X^real)，位置以 cm 计。
- **运行间变异性**：R 次独立运行的聚合分布间平均成对 EMD W̄1^run-to-run。

### 实验控制
统一仿真时间步长 Δt=0.01s，100 步预热（JIT 编译或场景初始化），1000 步内测量 FPS 和内存。固定随机种子并禁用任务级随机化，以隔离数值和执行级效应。物理参数（摩擦系数、恢复系数）通过专业实验室设施识别，例如地面静摩擦 0.65、动摩擦 0.45、恢复系数 0.40；斜面静摩擦 0.35、动摩擦 0.25、恢复系数 0.40。

## 关键创新

1. **将确定性从“全有或全无”细化为四类机制**：此前模拟器要么被简单标记为“确定”或“不确定”，GPUSimBench 通过并行变异性与运行间变异性的组合，区分出 Type 1（两者皆无，如 Isaac Lab、ManiSkill）、Type 2（仅并行变异，如 Genesis、MJX）、Type 3（两者皆有，如 Madrona、MuJoCo Warp）、Type 4（仅运行间变异，如 Playground）。这种分类直接对应底层执行模型——例如 MJX 的 XLA 编译保证了批内一致性但跨运行有 JIT 重编译差异，而 Madrona 的 ECS 架构在批内就存在线程调度非确定性。

2. **物理一致性以厘米级 EMD 量化**：首次将模拟与真实世界的分布对齐用物理单位（cm）的 EMD 度量，而非任务成功率或轨迹误差。这使得不同模拟器之间的物理保真度可以直接比较，且结果可解释——例如 Madrona 的 211.60±2.22cm 意味着立方体在木板上无法可靠减速，产生大平面漂移，这是 XPBD 求解器摩擦力建模不足的直接后果。

3. **跨模拟器分类的评估框架**：将模拟器按编程抽象分为四类（数组+XLA、高级内核、任务中心、ECS），并揭示抽象选择与确定性/物理保真度的关联。例如数组式（MJX、Playground）倾向于低并行变异性但可能有运行间差异，而任务中心（Isaac Lab、ManiSkill）在物理一致性上表现最优（EMD 分别为 5.400±0.000cm 和 2.520±0.000cm）。

## 实验与结果

实验在单一硬件平台（13th Gen Intel i5-13400F CPU, 32 GB RAM, NVIDIA GeForce RTX 5070 GPU with 12 GB memory）上进行，评估 7 个模拟器。并行能力基准每个模拟器重复十次独立运行，斜面碰撞基准报告十次独立运行的均值±标准差。

**并行能力关键结果**（自由落体场景，N_env^max 为最大并行环境数）：

| 模拟器 | N_env^max | FPS (×10^4) | 内存 (GB) |
|--------|-----------|-------------|-----------|
| Genesis | 2^11 | 2.233712 | 7.75 |
| Isaac Lab | 2^12 | 47.189328 | 3.34 |
| Madrona | 2^18 | 48.107876 | 9.53 |
| ManiSkill | 2^12 | 7.374857 | 8.34 |
| MJX | 2^9 | 0.534038 | 10.61 |
| MuJoCo Warp | 2^11 | 16.600347 | 5.87 |
| Playground | 2^8 | 0.003472 | 8.89 |

**斜面碰撞物理一致性结果**（d_EMD,phys^sim 为模拟与真实分布 EMD，单位 cm）：

| 模拟器 | d_EMD,phys^sim | W̄1^parallel | W̄1^run-to-run | 类型 |
|--------|----------------|-------------|---------------|------|
| Isaac Lab | 5.400±0.000 | 4.21±0.00 | 0.00±0.00 | Type 1 |
| ManiSkill | 2.520±0.000 | 4.76±0.00 | 0.00±0.00 | Type 1 |
| Genesis | 4.780±0.000 | 0.00±0.00 | 0.00±0.00 | Type 2 |
| MJX | 3.970±0.000 | 0.00±0.00 | 0.00±0.00 | Type 2 |
| Madrona | 211.60±2.22 | 32.53±1.86 | 11.47±1.40 | Type 3 |
| MuJoCo Warp | 4.230±0.740 | 4.55±1.39 | 2.15±0.82 | Type 3 |
| Playground | 3.380±0.110 | 0.00±0.00 | 1.39±0.47 | Type 4 |

结果含义：ManiSkill 和 MJX 达到最低 EMD（2.520±0.000cm 和 3.970±0.000cm），表明在尽力参数匹配下与真实物理分布对齐最佳。Madrona 的 EMD 异常高（211.60±2.22cm），且并行变异性（32.53±1.86cm）和运行间变异性（11.47±1.40cm）均显著，说明其求解器在接触建模上存在系统性缺陷。Isaac Lab 虽然物理一致性中等（5.400±0.000cm），但并行变异性（4.21±0.00cm）表明批内环境间存在数值发散，尽管运行间完全确定。

## 边界与局限

论文结论部分（VII Conclusion and Limitation）被截断，完整局限描述未提供。从上下文推断的边界包括：未考虑仅支持 CPU 并行或仅部分使用 GPU 加速的模拟器（如 Gazebo、PyBullet）；未包含所有可能的真实到仿真分布实验（如骰子投掷关节姿态分布和高斯球投掷分布实验因空间限制被省略，将在项目网站发布）；物理参数（摩擦系数、恢复系数）是通过专业实验室设施识别得到的近似值，EMD 值应解释为在尽力参数匹配下与测量参考的分布级一致性。此外，基准仅覆盖两个可扩展性场景和一个接触丰富的真实世界匹配实验，且全部在单一硬件和软件栈上进行，报告的性能和变异性可能因不同 GPU、驱动程序和模拟器版本而变化。当前基准未涵盖可变形体动力学、流体仿真、感知和传感器渲染的影响。

## 工程启示

复现 GPUSimBench 时，首先核对模拟器版本与硬件配置——论文使用 ManiSkill v3.0.0b22、Genesis v0.3.11、MJX (MuJoCo v3.4.0)、MujocoPlayground v0.1.0、IsaacLab v2.2.1，均从各自仓库主分支获取，版本差异可能显著改变结果。最容易踩坑的是预热步数：必须严格执行 100 步预热（用于 JIT 编译或场景初始化），否则 MJX 和 Playground 这类依赖 XLA 编译的模拟器会在测量窗口内包含编译开销，导致 FPS 严重低估。

对于下游团队选型，建议根据任务需求权衡：若需要严格可复现的科学实验（如策略评估对比），优先选择 Type 1 模拟器（Isaac Lab、ManiSkill），它们运行间变异性为 0.00±0.00cm；若追求最大并行吞吐量且可接受批内发散，Madrona 在自由落体场景达到 N_env^max=2^18 和 FPS=48.107876×10^4，但需注意其物理一致性缺陷（EMD 211.60±2.22cm）。对于接触丰富的操作任务，ManiSkill 的物理一致性（2.520±0.000cm）和确定性组合最优，但并行扩展上限（2^12）低于 Madrona。若需在物理保真与并行能力间平衡，MuJoCo Warp 提供中等 EMD（4.230±0.740cm）和较高并行上限（2^11），但需接受两类变异性均存在。

## Overview
Data-driven embodied AI is rapidly transitioning into a paradigm that scales training through massively parallel simulation, where GPU-accelerated simulators serve as the foundational data infrastructure. However, as computational throughput scales, the underlying trade-offs between parallel efficiency, physical fidelity, and execution determinism remain largely unexamined, hindering the development of reliable robot learning. In this paper, we expose the hidden limits of mainstream GPU-based robotic simulators (e.g., Isaac Lab, Genesis) by introducing GPUSimBench, which focuses on scalability, physical consistency, and computational determinism. First, GPUSimBench establishes a physical grounding evaluation with a controlled inclined-plane task, quantifying the distributional alignment between simulated dynamics and their real-world counterparts. Second, we benchmark parallel scalability by measuring throughput and memory footprints across scaling environment counts. Crucially, beyond standard performance metrics, we unveil and quantify the inherent non-determinism introduced by GPU-batched execution, characterized by significant run-to-run and inter-environment variability even under identical initial conditions. Finally, we identify four empirical regimes of stochasticity within current simulator stacks, highlighting that unbounded scaling can compromise reproducibility without explicit constraints.

## 参考
- https://arxiv.org/abs/2607.13059

## 개요

GPUSimBench는 저자 팀이 제안한, 임베디드 인텔리전스 GPU 가속 시뮬레이터를 위한 표준화된 벤치마크로, 주요 시뮬레이터(Isaac Lab, Genesis, Madrona, ManiSkill, MJX, MuJoCo Warp, Playground)를 병렬 확장성, 물리 일관성, 계산 결정성의 세 가지 차원에서 체계적으로 평가합니다. 핵심 기여는 '병렬 변동성'과 '실행 간 변동성'을 시뮬레이터 평가의 독립 지표로 처음 도입하고, 서로 다른 프로그래밍 추상화(배열형, 커널형, 태스크 중심, ECS)가 시뮬레이션 신뢰성에 미치는 근본적 영향을 밝힌 것입니다.

## 무엇을 바꾸었는가

과거 GPU 시뮬레이터 평가는 거의 전적으로 태스크 수준 성공률이나 최대 처리량에 집중했으며, 병렬 실행은 단지 '더 빠른 순차 시뮬레이션'일 뿐이라고 기본적으로 가정했습니다. GPUSimBench는 이러한 인식 체계를 바꿉니다. GPU 배치 실행이 투명한 가속 계층이 아니라 두 가지 독립적인 비결정성을 도입한다는 것을 증명합니다. 즉, 동일 배치 내 서로 다른 환경 간 결과 발산(병렬 변동성)과 동일 시드 하에서 여러 번 실행할 때의 분포 이동(실행 간 변동성)입니다. 이 두 변동성의 조합은 시뮬레이터가 엄격한 재현성을 요구하는 과학 실험이나 정책 평가에 사용될 수 있는지를 직접 결정합니다.

더 중요하게, 이 벤치마크는 '물리 일관성'을 정성적 논의에서 정량적 지표로 전환합니다. 통제된 경사면 충돌 태스크를 통해 물리 단위(센티미터)의 EMD(earth mover's distance)로 시뮬레이션 분포와 실제 세계 분포의 편차를 측정합니다. 이는 시뮬레이터 개발자가 이전에 회피했던 문제, 즉 병렬화로 인한 수치적 섭동이 단순한 무작위 노이즈가 아니라 접촉 역학 거동을 체계적으로 변화시킨다는 사실을 직면하게 만듭니다. 예를 들어 Madrona는 XPBD 솔버의 마찰력 부족으로 EMD가 211.60±2.22cm에 달하는 반면, ManiSkill은 2.520±0.000cm에 불과하여 두 시뮬레이터 간에 두 자릿수 차이가 발생합니다.

## 방법 분석

### 벤치마크 아키텍처
GPUSimBench는 평가를 세 개의 직교 차원으로 분해하며, 각 차원에는 독립적인 프로토콜이 있습니다:
- **확장성**: 자유 낙하 큐브 배열(3×3×3)과 Franka 로봇 팔 무작위 동작(자체 충돌 포함) 두 시나리오에서 서로 다른 병렬 환경 수 N_env에 따른 처리량(FPS = (N_env × N_step) / T_step)과 최대 메모리 증가량(M_usage = M_peak − M_base)을 측정합니다.
- **물리 일관성**: 경사면 충돌 태스크(경사각 20°, 큐브 모서리 길이 0.02m, 질량 0.005kg)를 설계하고, N_env=16 병렬 환경과 K=16회 실제 실험에서 t_s=5.0s 시점의 모든 큐브 xy 위치를 기록하고, 육각형 빈과 로그 밀도 매핑(D_b = log10(max(c_b, 1)))으로 분포를 시각화합니다.
- **결정성**: R=10회 독립 실행을 통해 네 가지 무작위성 유형(Type 1–4)을 구분하며, 병렬 변동성(W̄1^parallel)과 실행 간 변동성(W̄1^run-to-run)의 유무 조합으로 정의됩니다.

### 핵심 측정 공식
- **병렬 변동성**: 할당 기반 EMD, W1(e,e') = min_{π∈S_n} (1/n) Σ ||x_{e,i} − x_{e',π(i)}||_2, 평균 쌍별 EMD W̄1^parallel로 요약됩니다.
- **실제 세계 정렬**: 시뮬레이션과 실제 분포 간 물리 단위 EMD, d_EMD,phys^sim = W1^phys(X^sim, X^real), 위치는 cm 단위입니다.
- **실행 간 변동성**: R회 독립 실행의 집계 분포 간 평균 쌍별 EMD W̄1^run-to-run.

### 실험 통제
통일된 시뮬레이션 시간 간격 Δt=0.01s, 100스텝 워밍업(JIT 컴파일 또는 시나리오 초기화), 1000스텝 내에서 FPS와 메모리를 측정합니다. 고정된 무작위 시드를 사용하고 태스크 수준 무작위화를 비활성화하여 수치 및 실행 수준 효과를 분리합니다. 물리 파라미터(마찰 계수, 반발 계수)는 전문 실험실 시설을 통해 식별됩니다. 예를 들어 지면 정지 마찰 0.65, 동적 마찰 0.45, 반발 계수 0.40; 경사면 정지 마찰 0.35, 동적 마찰 0.25, 반발 계수 0.40입니다.

## 핵심 혁신

1. **결정성을 '전부 또는 전무'에서 네 가지 메커니즘으로 세분화**: 이전에는 시뮬레이터가 단순히 '결정적' 또는 '비결정적'으로 표시되었지만, GPUSimBench는 병렬 변동성과 실행 간 변동성의 조합을 통해 Type 1(둘 다 없음, Isaac Lab, ManiSkill), Type 2(병렬 변동성만 있음, Genesis, MJX), Type 3(둘 다 있음, Madrona, MuJoCo Warp), Type 4(실행 간 변동성만 있음, Playground)를 구분합니다. 이 분류는 기본 실행 모델과 직접적으로 대응합니다. 예를 들어 MJX의 XLA 컴파일은 배치 내 일관성을 보장하지만 실행 간 JIT 재컴파일 차이가 있고, Madrona의 ECS 아키텍처는 배치 내에서도 스레드 스케줄링 비결정성이 존재합니다.

2. **물리 일관성을 센티미터 단위 EMD로 정량화**: 시뮬레이션과 실제 세계의 분포 정렬을 태스크 성공률이나 궤적 오류가 아닌 물리 단위(cm)의 EMD로 처음 측정합니다. 이를 통해 서로 다른 시뮬레이터 간 물리 충실도를 직접 비교할 수 있고 결과를 해석할 수 있습니다. 예를 들어 Madrona의 211.60±2.22cm는 큐브가 나무 판에서 안정적으로 감속하지 못해 큰 평면 드리프트가 발생함을 의미하며, 이는 XPBD 솔버의 마찰력 모델링 부족의 직접적인 결과입니다.

3. **시뮬레이터 간 분류 평가 프레임워크**: 시뮬레이터를 프로그래밍 추상화에 따라 네 가지 유형(배열+XLA, 고급 커널, 태스크 중심, ECS)으로 분류하고, 추상화 선택과 결정성/물리 충실도 간의 연관성을 밝힙니다. 예를 들어 배열형(MJX, Playground)은 낮은 병렬 변동성을 보이는 경향이 있지만 실행 간 차이가 있을 수 있고, 태스크 중심(Isaac Lab, ManiSkill)은 물리 일관성에서 최상의 성능을 보입니다(EMD 각각 5.400±0.000cm 및 2.520±0.000cm).

## 실험 및 결과

실험은 단일 하드웨어 플랫폼(13th Gen Intel i5-13400F CPU, 32 GB RAM, NVIDIA GeForce RTX 5070 GPU with 12 GB memory)에서 7개 시뮬레이터를 평가했습니다. 병렬 능력 벤치마크는 각 시뮬레이터에 대해 10회 독립 실행을 반복했고, 경사면 충돌 벤치마크는 10회 독립 실행의 평균±표준편차를 보고했습니다.

**병렬 능력 핵심 결과**(자유 낙하 시나리오, N_env^max는 최대 병렬 환경 수):

| 시뮬레이터 | N_env^max | FPS (×10^4) | 메모리 (GB) |
|--------|-----------|-------------|-----------|
| Genesis | 2^11 | 2.233712 | 7.75 |
| Isaac Lab | 2^12 | 47.189328 | 3.34 |
| Madrona | 2^18 | 48.107876 | 9.53 |
| ManiSkill | 2^12 | 7.374857 | 8.34 |
| MJX | 2^9 | 0.534038 | 10.61 |
| MuJoCo Warp | 2^11 | 16.600347 | 5.87 |
| Playground | 2^8 | 0.003472 | 8.89 |

**경사면 충돌 물리 일관성 결과**(d_EMD,phys^sim는 시뮬레이션과 실제 분포 간 EMD, 단위 cm):

| 시뮬레이터 | d_EMD,phys^sim | W̄1^parallel | W̄1^run-to-run | 유형 |
|--------|----------------|-------------|---------------|------|
| Isaac Lab | 5.400±0.000 | 4.21±0.00 | 0.00±0.00 | Type 1 |
| ManiSkill | 2.520±0.000 | 4.76±0.00 | 0.00±0.00 | Type 1 |
| Genesis | 4.780±0.000 | 0.00±0.00 | 0.00±0.00 | Type 2 |
| MJX | 3.970±0.000 | 0.00±0.00 | 0.00±0.00 | Type 2 |
| Madrona | 211.60±2.22 | 32.53±1.86 | 11.47±1.40 | Type 3 |
| MuJoCo Warp | 4.230±0.740 | 4.55±1.39 | 2.15±0.82 | Type 3 |
| Playground | 3.380±0.110 | 0.00±0.00 | 1.39±0.47 | Type 4 |

결과 의미: ManiSkill과 MJX는 가장 낮은 EMD(2.520±0.000cm 및 3.970±0.000cm)를 달성하여 최선의 파라미터 매칭 하에서 실제 물리 분포와 가장 잘 정렬됨을 보여줍니다. Madrona의 EMD는 비정상적으로 높고(211.60±2.22cm), 병렬 변동성(32.53±1.86cm)과 실행 간 변동성(11.47±1.40cm) 모두 유의미하여 솔버의 접촉 모델링에 체계적 결함이 있음을 시사합니다. Isaac Lab은 물리 일관성이 중간 수준(5.400±0.000cm)이지만, 병렬 변동성(4.21±0.00cm)은 배치 내 환경 간 수치 발산이 있음을 나타내며, 실행 간에는 완전히 결정적입니다.

## 경계 및 한계

논문 결론 부분(VII Conclusion and Limitation)은 잘려 있어 완전한 한계 설명은 제공되지 않았습니다. 문맥에서 추론할 수 있는 경계는 다음과 같습니다: CPU 병렬만 지원하거나 GPU 가속을 부분적으로만 사용하는 시뮬레이터(예: Gazebo, PyBullet)는 고려하지 않았습니다. 모든 가능한 실제-시뮬레이션 분포 실험을 포함하지 않았습니다(예: 주사위 던지기 관절 자세 분포와 가우스 구 던지기 분포 실험은 공간 제약으로 생략되었으며 프로젝트 웹사이트에 게시될 예정). 물리 파라미터(마찰 계수, 반발 계수)는 전문 실험실 시설을 통해 식별된 근사값이며, EMD 값은 최선의 파라미터 매칭 하에서 측정 기준과의 분포 수준 일관성으로 해석되어야 합니다. 또한 벤치마크는 두 개의 확장성 시나리오와 하나의 접촉이 풍부한 실제 세계 매칭 실험만을 다루며, 모두 단일 하드웨어 및 소프트웨어 스택에서 수행되어 보고된 성능과 변동성은 GPU, 드라이버, 시뮬레이터 버전에 따라 달라질 수 있습니다. 현재 벤치마크는 변형체 역학, 유체 시뮬레이션, 인식 및 센서 렌더링의 영향을 포함하지 않습니다.

## 엔지니어링 시사점

GPUSimBench를 재현할 때 먼저 시뮬레이터 버전과 하드웨어 구성을 확인하십시오. 논문은 ManiSkill v3.0.0b22, Genesis v0.3.11, MJX (MuJoCo v3.4.0), MujocoPlayground v0.1.0, IsaacLab v2.2.1을 사용했으며, 모두 각 저장소의 메인 브랜치에서 가져왔습니다. 버전 차이는 결과를 크게 바꿀 수 있습니다. 가장 흔한 함정은 워밍업 스텝 수입니다. 100스텝 워밍업(JIT 컴파일 또는 시나리오 초기화용)을 엄격히 수행해야 합니다. 그렇지 않으면 MJX 및 Playground와 같은 XLA 컴파일 의존 시뮬레이터가 측정 창에 컴파일 오버헤드를 포함하여 FPS가 심각하게 과소평가됩니다.

다운스트림 팀의 선택을 위해 태스크 요구 사항에 따라权衡하는 것이 좋습니다: 엄격한 재현성을 요구하는 과학 실험(예: 정책 평가 비교)이 필요하면 Type 1 시뮬레이터(Isaac Lab, ManiSkill)를 우선 선택하십시오. 실행 간 변동성이 0.00±0.00cm입니다. 최대 병렬 처리량을 추구하고 배치 내 발산을 수용할 수 있다면 Madrona는 자유 낙하 시나리오에서 N_env^max=2^18 및 FPS=48.107876×10^4를 달성하지만 물리 일관성 결함(EMD 211.60±2.22cm)에 주의해야 합니다. 접촉이 풍부한 조작 태스크의 경우 ManiSkill의 물리 일관성(2.520±0.000cm)과 결정성 조합이 최적이지만 병렬 확장 상한(2^12)은 Madrona보다 낮습니다. 물리 충실도와 병렬 능력 간 균형이 필요하면 MuJoCo Warp는 중간 EMD(4.230±0.740cm)와 높은 병렬 상한(2^11)을 제공하지만 두 유형의 변동성이 모두 존재함을 수용해야 합니다.
