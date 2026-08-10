---
$id: ent_paper_hermite_curves_trajectory_priors_vision_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hermite Curves as Trajectory Priors for Vision-Language-Action Models
  zh: Hermite Curves as Trajectory Priors for Vision-Language-Action Models
  ko: Hermite Curves as Trajectory Priors for Vision-Language-Action Models
summary:
  en: Despite recent progress in Vision-Language-Action (VLA) models for robotic manipulation, the action chunk remains a
    weakly structured interface. Existing work typically flatten each chunk into per-timestep controls, relying on implicit
    data learning that manifests as jagged motion and boundary discontinuities during physical execution. To address these
    limitations, we introduce Hermite trajectory.
  zh: 本文提出用分段三次 Hermite 样条作为视觉-语言-动作模型（VLA）的轨迹先验，将动作块显式参数化为端点位置与速度，并通过三个集成变体（离散 DH、连续 CH、正则化 Reg）验证其效果。核心贡献在于证明轨迹平滑度作为学习阶段的归纳偏置（而非推理约束）能显著提升任务成功率与轨迹质量，其中
    Hermite-VLA Reg 以零推理开销取得最佳性能。
  ko: Despite recent progress in Vision-Language-Action (VLA) models for robotic manipulation, the action chunk remains a
    weakly structured interface. Existing work typically flatten each chunk into per-timestep controls, relying on implicit
    data learning that manifests as jagged motion and boundary discontinuities during physical execution. To address these
    limitations, we introduce Hermite trajectory.
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
- hermite
- curves
- trajectory
- priors
- vision
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. [2026-08-05] guardrail fix: unverifiable numbers corrected to
    full-text-verbatim or marked as computed/未提取 (catchup sweep audit). 深读+数字白名单复核通过 2026-08-10（补网）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: arXiv:2608.01265 Hermite Curves as Trajectory Priors for Vision-Language-Action Models
  url: https://arxiv.org/abs/2608.01265
  date: '2026-08-02'
  accessed_at: '2026-08-05'
---

## 概述

本文提出用分段三次 Hermite 样条作为视觉-语言-动作模型（VLA）的轨迹先验，将动作块显式参数化为端点位置与速度，并通过三个集成变体（离散 DH、连续 CH、正则化 Reg）验证其效果。核心贡献在于证明轨迹平滑度作为学习阶段的归纳偏置（而非推理约束）能显著提升任务成功率与轨迹质量，其中 Hermite-VLA Reg 以零推理开销取得最佳性能。

## 它改变了什么

VLA 动作生成长期面临一个被忽视的结构性缺陷：动作块被建模为扁平离散序列，块内平滑性与块间连续性完全依赖隐式学习，而跨块接缝处的速度是跨块有限差分，不属于任何单个参数集，因此在标准逐块行为克隆目标下不受直接监督。这导致长时程闭环操作中轨迹粗糙、接缝瞬态尖峰明显，物理控制不稳定且策略漂移累积。作者真正改变的是将动作块从"坐标序列"重新定义为"边界状态（位置+速度）的 Hermite 插值"，使平滑性成为可显式监督、可理论分析的结构属性，而非事后滤波或正则化的副产品。

更关键的是，这项工作改变了"平滑度提升"的归因逻辑。作者通过控制实验（对比成功与失败轨迹的 jerk）排除了幸存者偏差——平滑度提升并非仅由更高成功率造成，而是先验本身带来的独立效应。这为轨迹级归纳偏置在 VLA 中的价值提供了因果性证据，而非相关性证据。

## 方法拆解

### 核心算子：分段三次 Hermite 插值
- 动作块 a^c ∈ ℝ^{T×D_c} 被参数化为 K 段 Hermite 样条，每段由端点位置 (p_s, p_e) 与速度 (v_s, v_e) 定义，共 4K 个边界坐标 θ ∈ ℝ^{4K×D_c}
- 线性算子 H ∈ ℝ^{T×4K} 将边界坐标映射到轨迹空间：a^c = Hθ，H 由 Hermite 基函数 h₀₀, h₁₀, h₀₁, h₁₁ 构成，预计算并缓存在加速器上

### 三个集成变体
- **Hermite-VLA DH（离散）**：替换 π₀-FAST 分词器，将每个 Hermite 坐标量化为 256 个 bin，实现离散 token 化
- **Hermite-VLA CH（显式通道）**：流匹配头的干净预测重构为"样条骨架 + 逐时间步残差"：â_clean = Hθ + r，推理时先估计 θ 再叠加残差，Hermite 先验在每个去噪步骤主动条件化生成轨迹
- **Hermite-VLA Reg（正则化）**：附加辅助头 MLP_aux 将时间平均特征映射到 θ，通过 L_aux = ‖Hθ_aux − a_gt^c‖₂² 监督，总损失 L_Reg = L_flow + λ·L_aux，推理时完全丢弃辅助头，零额外开销

### 关键设计决策
- **轨迹空间监督而非 θ 空间监督**：轨迹空间损失在 H^T H 度量下加权每个边界坐标，速度列严格有界（max|h₁₀| = max|h₁₁| = 4/27），避免 θ 空间单位度量损失不成比例惩罚速度误差
- **软先验而非硬约束**：保留策略表达力，以绝对连续性换取灵活性
- **单侧有限差分编码器**：v_s = s(F(1/s) − F(0))，引入 O(s²) 收敛率（而非精确切线的 O(s⁴)），但避免了对未知真值导数的依赖

### 理论保证
- **命题 3.1**：轨迹空间损失与 θ 空间损失监督相同最小二乘目标，但度量不同
- **命题 3.2**：近似误差以 K⁻² 衰减，容许 jerk 上限以 K³ 增长，预示 K 存在内部最优（经验最优 K=2）
- **命题 3.3**：接缝位置不连续由轨迹空间残差直接控制（无需 σ_min(H)），速度不连续需经过坐标空间并受 1/σ_min(H) 放大

## 关键创新

1. **接缝位置与速度的解耦控制**：命题 3.3 证明位置接缝由轨迹空间残差直接界定（式 23，无 σ_min(H) 因子），而速度接缝需经过坐标空间（式 24，受 1/σ_min(H) 放大）。这一区分解释了为何位置连续性易得而速度连续性难保，为后续优化提供了精确靶点。

2. **可辨识性上限的发现**：T=10 时 K=3 导致 H 列秩亏缺（σ_min = 0），边界坐标从解码轨迹不可辨识。这为 K 消融实验中的退化现象提供了与偏差-保真度权衡互补的解释，且是首个将轨迹参数化可辨识性与 VLA 性能直接关联的理论结果。

3. **零开销正则化范式**：Hermite-VLA Reg 将先验严格作为辅助训练目标，推理时完全移除，在取得最佳性能（LIBERO 98.7%）的同时保持与基线完全相同的推理延迟（48.6 ms vs 48.4 ms）。这证明了轨迹平滑性作为学习阶段归纳偏置的价值，而非推理阶段约束。

## 实验与结果


### 仿真基准（LIBERO 成功率 %）

| 方法 | LIBERO | LIBERO-plus |
|------|--------|-------------|
| π₀.₅ | 95.9 | 85.7 |
| Hermite-VLA CH | 97.7 | 85.0 |
| Hermite-VLA Reg | **98.7** | **90.9** |
| Hermite-VLA DH | 95.4 | 69.4 |
| Spline Policy（并行工作） | 原文为表格图，数值未提取 | — |

### 真实机器人（平均成功率 %，15 次 rollout/任务）

| 方法 | Task 1 | Task 2 | Task 3 | Task 4 | Avg |
|------|--------|--------|--------|--------|-----|
| π₀.₅ | 86.7 | 26.7 | 46.7 | 93.3 | 63.4 |
| Hermite-VLA CH | 86.7 | 60.0 | 80.0 | 100.0 | 81.7 |
| Hermite-VLA Reg | **100.0** | **66.7** | **93.3** | **100.0** | **90.0** |

### 关键消融
- **λ 注入强度**：λ=10 最优（98.7%），λ=0 时 95.9%，λ=20 退化至 97.5%
- **K 段数**：K=2 最优（98.7%），K=1 为 93.7%，K=3 降至 96.6%，K=4 降至 95.8%
- **监督空间**：θ 空间+最小二乘目标仅 91.5%，轨迹空间+残差（完整 CH）达 97.7%
- **边界基**：Hermite（98.7%）优于 B-spline（97.6%）、Bernstein（96.9%）、Polynomial（96.7%）

### 平滑度与因果性
- π₀.₅ 失败轨迹 jerk（0.00070）显著高于成功轨迹（0.00046），而 Hermite-VLA Reg 失败轨迹 jerk（0.00048）接近其成功轨迹（0.00040），证明平滑度提升非幸存者偏差
- 真实机器人接缝不连续性：Hermite-VLA Reg 相对 π₀.₅ 降至 0.48×（Task 3），加速度与 jerk RMS 均显著更低（p < 10⁻⁴）

### 推理成本（单 H100，1000 次平均）

| 方法 | 延迟 (ms) | FPS | 峰值显存 (GB) |
|------|-----------|-----|---------------|
| π₀-FAST | 238.2 | 4.2 | 7.57 |
| Hermite-VLA DH | 28.9 | 34.6 | 6.66 |
| π₀.₅ | 48.4 | 20.7 | 6.63 |
| Hermite-VLA CH | 49.4 | 20.2 | 6.64 |
| Hermite-VLA Reg | 48.6 | 20.6 | 6.85 |

## 边界与局限

- **软先验的固有边界**：接缝尖峰被缩小但未完全消除，速度连续性保证在仿真时域（T=10）比真实机器人时域（T=50）更宽松（1/σ_min 分别为 53.0 vs 9.5）
- **单侧差分编码器的代价**：端点速度估计引入 O(s²) 收敛率，若用精确导数可恢复 O(s⁴)，但需未知真值信息
- **离散通道未建模**：夹爪等非平滑通道被排除在 Hermite 先验之外，仅连续子空间受约束
- **K 值未在 T=50 扫描**：真实机器人时域的最优 K 未经验证，仅依赖仿真结论
- **因果方向性未完全解决**：平滑度与成功率之间的因果机制仍部分依赖外部引用，本文控制实验提供了证据但未完全闭合
- **泛化范围有限**：未验证精细装配、高动态接触等复杂操作场景

## 工程启示

- **优先复现 Hermite-VLA Reg**：零推理开销且性能最佳，实现最简单（仅训练时附加辅助头），是工程性价比最高的变体
- **核对 H 矩阵条件数**：T=10 时 K 必须 ≤ 2，否则 σ_min = 0 导致速度保证退化；T=50 时 K ≤ 12 均安全，但 K=2 仍是经验最优
- **注意监督空间选择**：务必在轨迹空间（‖Hθ − a‖₂²）而非 θ 空间施加损失，否则速度误差会被不成比例惩罚（强度至少 6.75 倍）
- **接缝位置与速度分开评估**：位置接缝由轨迹残差直接控制，速度接缝受 1/σ_min 放大，调试时若速度尖峰明显应先检查 σ_min 而非残差
- **λ 与 K 需重新调优**：λ=10、K=2 在 LIBERO 最优，但换基准或本体后需重新扫描，λ 在 5–20 区间、K 在 2–5 区间内性能相对平坦
- **最容易踩坑**：四舍五入网格下 T=10、K=2 时 i₁=4，LIBERO 窗口 W=5 恰好节点对齐（W−1=4），真实机器人 W=20 则非对齐——评估接缝指标时需区分这两种情况

## 参考
- https://arxiv.org/abs/2608.01265

## Overview

This paper proposes using piecewise cubic Hermite splines as trajectory priors for Vision-Language-Action models (VLA), explicitly parameterizing action chunks as endpoint positions and velocities, and validating their effectiveness through three integration variants (discrete DH, continuous CH, regularized Reg). The core contribution lies in demonstrating that trajectory smoothness as an inductive bias during the learning phase (rather than an inference constraint) significantly improves task success rates and trajectory quality, with Hermite-VLA Reg achieving the best performance at zero inference overhead.

## What It Changes

VLA action generation has long faced an overlooked structural flaw: action chunks are modeled as flat discrete sequences, with intra-chunk smoothness and inter-chunk continuity relying entirely on implicit learning, while the velocity at cross-chunk seams is a cross-chunk finite difference that does not belong to any single parameter set and thus receives no direct supervision under standard per-chunk behavior cloning objectives. This leads to rough trajectories, pronounced seam transient spikes, unstable physical control, and accumulating policy drift in long-horizon closed-loop manipulation. What the authors truly change is redefining action chunks from "coordinate sequences" to "Hermite interpolations of boundary states (position + velocity)," making smoothness a structural property that can be explicitly supervised and theoretically analyzed, rather than a byproduct of post-hoc filtering or regularization.

More critically, this work changes the attribution logic of "smoothness improvement." Through controlled experiments (comparing jerk of successful vs. failed trajectories), the authors rule out survivorship bias—the smoothness improvement is not merely caused by higher success rates but is an independent effect brought by the prior itself. This provides causal, rather than correlational, evidence for the value of trajectory-level inductive biases in VLAs.

## Method Breakdown

### Core Operator: Piecewise Cubic Hermite Interpolation
- Action chunk a^c ∈ ℝ^{T×D_c} is parameterized as K segments of Hermite splines, each defined by endpoint positions (p_s, p_e) and velocities (v_s, v_e), totaling 4K boundary coordinates θ ∈ ℝ^{4K×D_c}
- Linear operator H ∈ ℝ^{T×4K} maps boundary coordinates to trajectory space: a^c = Hθ, where H is composed of Hermite basis functions h₀₀, h₁₀, h₀₁, h₁₁, precomputed and cached on the accelerator

### Three Integration Variants
- **Hermite-VLA DH (discrete)**: Replaces the π₀-FAST tokenizer, quantizing each Hermite coordinate into 256 bins for discrete tokenization
- **Hermite-VLA CH (explicit channel)**: The clean prediction of the flow matching head is reconstructed as "spline skeleton + per-timestep residual": â_clean = Hθ + r. At inference, θ is estimated first, then residuals are added; the Hermite prior actively conditions trajectory generation at every denoising step
- **Hermite-VLA Reg (regularization)**: An auxiliary head MLP_aux maps time-averaged features to θ, supervised by L_aux = ‖Hθ_aux − a_gt^c‖₂², with total loss L_Reg = L_flow + λ·L_aux. The auxiliary head is completely discarded at inference, incurring zero extra overhead

### Key Design Decisions
- **Trajectory-space supervision rather than θ-space supervision**: Trajectory-space loss weights each boundary coordinate under the H^T H metric, with velocity columns strictly bounded (max|h₁₀| = max|h₁₁| = 4/27), avoiding disproportionate penalization of velocity errors under the unit metric in θ space
- **Soft prior rather than hard constraint**: Preserves policy expressiveness, trading absolute continuity for flexibility
- **One-sided finite difference encoder**: v_s = s(F(1/s) − F(0)), introducing O(s²) convergence rate (rather than O(s⁴) for exact tangents), but avoiding dependence on unknown ground-truth derivatives

### Theoretical Guarantees
- **Proposition 3.1**: Trajectory-space loss and θ-space loss supervise the same least-squares objective but with different metrics
- **Proposition 3.2**: Approximation error decays at K⁻², while the admissible jerk upper bound grows at K³, suggesting an internal optimum for K (empirically optimal K=2)
- **Proposition 3.3**: Position discontinuity at seams is directly controlled by trajectory-space residuals (without σ_min(H)), while velocity discontinuity must pass through coordinate space and is amplified by 1/σ_min(H)

## Key Innovations

1. **Decoupled control of seam position and velocity**: Proposition 3.3 proves that position seams are directly bounded by trajectory-space residuals (Eq. 23, without σ_min(H) factor), while velocity seams must pass through coordinate space (Eq. 24, amplified by 1/σ_min(H)). This distinction explains why position continuity is easy to achieve while velocity continuity is difficult, providing precise targets for subsequent optimization.

2. **Discovery of identifiability upper bound**: At T=10, K=3 causes H to become column-rank-deficient (σ_min = 0), making boundary coordinates unidentifiable from decoded trajectories. This provides a complementary explanation to the bias-fidelity tradeoff for the degradation observed in K ablation experiments, and is the first theoretical result directly linking trajectory parameterization identifiability to VLA performance.

3. **Zero-overhead regularization paradigm**: Hermite-VLA Reg applies the prior strictly as an auxiliary training objective, completely removed at inference, achieving the best performance (LIBERO 98.7%) while maintaining identical inference latency to the baseline (48.6 ms vs 48.4 ms). This demonstrates the value of trajectory smoothness as a learning-phase inductive bias rather than an inference-phase constraint.

## Experiments and Results

### Simulation Benchmarks (LIBERO Success Rate %)

| Method | LIBERO | LIBERO-plus |
|--------|--------|-------------|
| π₀.₅ | 95.9 | 85.7 |
| Hermite-VLA CH | 97.7 | 85.0 |
| Hermite-VLA Reg | **98.7** | **90.9** |
| Hermite-VLA DH | 95.4 | 69.4 |
| Spline Policy (parallel work) | Original was a table figure, values not extracted | — |

### Real Robot (Average Success Rate %, 15 rollouts/task)

| Method | Task 1 | Task 2 | Task 3 | Task 4 | Avg |
|--------|--------|--------|--------|--------|-----|
| π₀.₅ | 86.7 | 26.7 | 46.7 | 93.3 | 63.4 |
| Hermite-VLA CH | 86.7 | 60.0 | 80.0 | 100.0 | 81.7 |
| Hermite-VLA Reg | **100.0** | **66.7** | **93.3** | **100.0** | **90.0** |

### Key Ablations
- **λ injection strength**: λ=10 optimal (98.7%), λ=0 gives 95.9%, λ=20 degrades to 97.5%
- **K segment count**: K=2 optimal (98.7%), K=1 gives 93.7%, K=3 drops to 96.6%, K=4 drops to 95.8%
- **Supervision space**: θ-space with least-squares objective only 91.5%, trajectory-space with residual (full CH) reaches 97.7%
- **Boundary basis**: Hermite (98.7%) outperforms B-spline (97.6%), Bernstein (96.9%), Polynomial (96.7%)

### Smoothness and Causality
- π₀.₅ failed trajectories have significantly higher jerk (0.00070) than successful ones (0.00046), while Hermite-VLA Reg failed trajectories have jerk (0.00048) close to its successful ones (0.00040), proving the smoothness improvement is not survivorship bias
- Real robot seam discontinuity: Hermite-VLA Reg reduced to 0.48× relative to π₀.₅ (Task 3), with both acceleration and jerk RMS significantly lower (p < 10⁻⁴)

### Inference Cost (Single H100, 1000-run average)

| Method | Latency (ms) | FPS | Peak Memory (GB) |
|--------|--------------|-----|------------------|
| π₀-FAST | 238.2 | 4.2 | 7.57 |
| Hermite-VLA DH | 28.9 | 34.6 | 6.66 |
| π₀.₅ | 48.4 | 20.7 | 6.63 |
| Hermite-VLA CH | 49.4 | 20.2 | 6.64 |
| Hermite-VLA Reg | 48.6 | 20.6 | 6.85 |

## Boundaries and Limitations

- **Inherent boundary of soft prior**: Seam spikes are reduced but not fully eliminated; velocity continuity guarantees are looser in the simulation horizon (T=10) than the real robot horizon (T=50) (1/σ_min of 53.0 vs 9.5, respectively)
- **Cost of one-sided difference encoder**: Endpoint velocity estimation introduces O(s²) convergence rate; exact derivatives could restore O(s⁴) but require unknown ground-truth information
- **Discrete channels not modeled**: Non-smooth channels such as grippers are excluded from the Hermite prior; only the continuous subspace is constrained
- **K not swept at T=50**: The optimal K for the real robot horizon is not validated, relying only on simulation conclusions
- **Causal directionality not fully resolved**: The causal mechanism between smoothness and success rate still partially relies on external references; this paper's controlled experiments provide evidence but do not fully close the loop
- **Limited generalization scope**: Complex manipulation scenarios such as fine assembly and high-dynamic contact are not validated

## Engineering Insights

- **Prioritize reproducing Hermite-VLA Reg**: Zero inference overhead with the best performance, simplest implementation (only an auxiliary head during training), making it the most cost-effective variant
- **Check H matrix condition number**: At T=10, K must be ≤ 2, otherwise σ_min = 0 causes degraded velocity guarantees; at T=50, K ≤ 12 is safe, but K=2 remains empirically optimal
- **Pay attention to supervision space selection**: Always apply the loss in trajectory space (‖Hθ − a‖₂²) rather than θ space, otherwise velocity errors are disproportionately penalized (by at least 6.75×)
- **Evaluate seam position and velocity separately**: Position seams are directly controlled by trajectory residuals, while velocity seams are amplified by 1/σ_min; when debugging, if velocity spikes are prominent, check σ_min first rather than residuals
- **λ and K need re-tuning**: λ=10, K=2 are optimal on LIBERO, but re-scanning is required when changing benchmarks or embodiments; performance is relatively flat for λ in the 5–20 range and K in the 2–5 range
- **Most common pitfall**: Under the rounding grid, at T=10 and K=2, i₁=4; the LIBERO window W=5 happens to align with nodes (W−1=4), while the real robot window W=20 is non-aligned—seam metrics must distinguish between these two cases when evaluated

## 개요

본 논문은 3차 Hermite 스플라인을 시각-언어-행동 모델(VLA)의 궤적 사전으로 사용하여, 행동 블록을 끝점 위치와 속도로 명시적으로 파라미터화하고, 세 가지 통합 변형(이산 DH, 연속 CH, 정규화 Reg)을 통해 그 효과를 검증한다. 핵심 기여는 궤적 평활도가 추론 제약이 아닌 학습 단계의 귀납적 편향으로 작용할 때 작업 성공률과 궤적 품질을 크게 향상시킬 수 있음을 증명한 것이며, Hermite-VLA Reg는 추론 오버헤드 없이 최고 성능을 달성한다.

## 무엇을 바꾸었는가

VLA 행동 생성은 오랫동안 간과된 구조적 결함을 안고 있었다: 행동 블록이 평평한 이산 시퀀스로 모델링되어, 블록 내 평활성과 블록 간 연속성은 전적으로 암묵적 학습에 의존하며, 블록 경계에서의 속도는 블록 간 유한 차분으로 계산되어 어떤 단일 파라미터 집합에도 속하지 않는다. 따라서 표준 블록별 행동 클로닝 목표 하에서 직접적인 감독을 받지 못한다. 이로 인해 장시간 폐루프 조작에서 궤적이 거칠어지고, 경계에서 과도 스파이크가 뚜렷해지며, 물리적 제어가 불안정해지고 정책 드리프트가 누적된다. 저자가 실제로 바꾼 것은 행동 블록을 "좌표 시퀀스"에서 "경계 상태(위치+속도)의 Hermite 보간"으로 재정의하여, 평활성을 사후 필터링이나 정규화의 부산물이 아닌 명시적으로 감독 가능하고 이론적으로 분석 가능한 구조적 속성으로 만든 것이다.

더욱 중요한 것은, 이 연구가 "평활도 향상"의 귀인 논리를 바꾸었다는 점이다. 저자는 대조 실험(성공 및 실패 궤적의 jerk 비교)을 통해 생존자 편향을 배제했다—평활도 향상은 단순히 더 높은 성공률에 의한 것이 아니라, 사전 자체가 가져오는 독립적 효과이다. 이는 VLA에서 궤적 수준 귀납적 편향의 가치에 대해 상관관계가 아닌 인과적 증거를 제공한다.

## 방법 분해

### 핵심 연산자: 조각별 3차 Hermite 보간
- 행동 블록 a^c ∈ ℝ^{T×D_c}는 K개의 Hermite 스플라인 세그먼트로 파라미터화되며, 각 세그먼트는 끝점 위치 (p_s, p_e)와 속도 (v_s, v_e)로 정의되어 총 4K개의 경계 좌표 θ ∈ ℝ^{4K×D_c}를 가진다
- 선형 연산자 H ∈ ℝ^{T×4K}는 경계 좌표를 궤적 공간으로 매핑한다: a^c = Hθ, H는 Hermite 기저 함수 h₀₀, h₁₀, h₀₁, h₁₁로 구성되며, 사전 계산되어 가속기에서 캐시된다

### 세 가지 통합 변형
- **Hermite-VLA DH(이산)**: π₀-FAST 토크나이저를 대체하여 각 Hermite 좌표를 256개 빈으로 양자화하여 이산 토큰화를 구현
- **Hermite-VLA CH(명시적 채널)**: 흐름 매칭 헤드의 깨끗한 예측을 "스플라인 골격 + 시간 단계별 잔차"로 재구성: â_clean = Hθ + r, 추론 시 θ를 먼저 추정한 후 잔차를 중첩하며, Hermite 사전은 각 노이즈 제거 단계에서 생성 궤적을 능동적으로 조건화
- **Hermite-VLA Reg(정규화)**: 추가 보조 헤드 MLP_aux가 시간 평균 특징을 θ로 매핑하고, L_aux = ‖Hθ_aux − a_gt^c‖₂²로 감독하며, 총 손실 L_Reg = L_flow + λ·L_aux, 추론 시 보조 헤드를 완전히 제거하여 추가 오버헤드가 없다

### 핵심 설계 결정
- **θ 공간 감독이 아닌 궤적 공간 감독**: 궤적 공간 손실은 H^T H 메트릭 하에서 각 경계 좌표에 가중치를 부여하며, 속도 열은 엄격히 유계(max|h₁₀| = max|h₁₁| = 4/27)이므로 θ 공간 단위 메트릭 손실이 속도 오차를 불균형적으로 처벌하는 것을 방지
- **하드 제약이 아닌 소프트 사전**: 정책의 표현력을 유지하고, 절대적 연속성을 유연성과 교환
- **단측 유한 차분 인코더**: v_s = s(F(1/s) − F(0)), O(s²) 수렴률(정확한 접선의 O(s⁴) 대신)을 도입하지만, 알 수 없는 참값 도함수에 대한 의존성을 피한다

### 이론적 보장
- **명제 3.1**: 궤적 공간 손실과 θ 공간 손실은 동일한 최소 제곱 목표를 감독하지만 메트릭이 다르다
- **명제 3.2**: 근사 오차는 K⁻²로 감쇠하고, 허용 jerk 상한은 K³으로 증가하여 K에 내부 최적값이 존재함을 시사(경험적 최적 K=2)
- **명제 3.3**: 경계 위치 불연속성은 궤적 공간 잔차에 의해 직접 제어되며(σ_min(H) 불필요), 속도 불연속성은 좌표 공간을 거쳐야 하며 1/σ_min(H)에 의해 증폭된다

## 핵심 혁신

1. **경계 위치와 속도의 분리 제어**: 명제 3.3은 위치 경계가 궤적 공간 잔차에 의해 직접 경계가 정해지고(식 23, σ_min(H) 인자 없음), 속도 경계는 좌표 공간을 거쳐야 하며(식 24, 1/σ_min(H)에 의해 증폭) 이를 증명한다. 이 구분은 위치 연속성이 쉽게 얻어지고 속도 연속성이 어려운 이유를 설명하며, 후속 최적화에 정확한 표적을 제공한다.

2. **식별 가능성 상한의 발견**: T=10에서 K=3은 H 열 랭크 결핍(σ_min = 0)을 초래하여 경계 좌표가 디코딩된 궤적에서 식별 불가능해진다. 이는 K 소거 실험의 퇴화 현상에 대해 편향-충실도 트레이드오프를 보완하는 설명을 제공하며, 궤적 파라미터화 식별 가능성과 VLA 성능을 직접 연결하는 최초의 이론적 결과이다.

3. **제로 오버헤드 정규화 패러다임**: Hermite-VLA Reg는 사전을 엄격히 보조 훈련 목표로 사용하고 추론 시 완전히 제거하여, 최고 성능(LIBERO 98.7%)을 달성하면서도 기준선과 동일한 추론 지연 시간(48.6 ms vs 48.4 ms)을 유지한다. 이는 궤적 평활도가 추론 단계 제약이 아닌 학습 단계 귀납적 편향으로서의 가치를 증명한다.

## 실험 및 결과

### 시뮬레이션 벤치마크(LIBERO 성공률 %)

| 방법 | LIBERO | LIBERO-plus |
|------|--------|-------------|
| π₀.₅ | 95.9 | 85.7 |
| Hermite-VLA CH | 97.7 | 85.0 |
| Hermite-VLA Reg | **98.7** | **90.9** |
| Hermite-VLA DH | 95.4 | 69.4 |
| Spline Policy(병행 연구) | 원문은 표 그림으로 수치 미추출 | — |

### 실제 로봇(평균 성공률 %, 작업당 15회 롤아웃)

| 방법 | 작업 1 | 작업 2 | 작업 3 | 작업 4 | 평균 |
|------|--------|--------|--------|--------|-----|
| π₀.₅ | 86.7 | 26.7 | 46.7 | 93.3 | 63.4 |
| Hermite-VLA CH | 86.7 | 60.0 | 80.0 | 100.0 | 81.7 |
| Hermite-VLA Reg | **100.0** | **66.7** | **93.3** | **100.0** | **90.0** |

### 핵심 소거
- **λ 주입 강도**: λ=10 최적(98.7%), λ=0일 때 95.9%, λ=20에서 97.5%로 퇴화
- **K 세그먼트 수**: K=2 최적(98.7%), K=1은 93.7%, K=3은 96.6%로 감소, K=4는 95.8%로 감소
- **감독 공간**: θ 공간+최소 제곱 목표는 91.5%에 불과, 궤적 공간+잔차(전체 CH)는 97.7% 달성
- **경계 기저**: Hermite(98.7%)가 B-spline(97.6%), Bernstein(96.9%), Polynomial(96.7%)보다 우수

### 평활도 및 인과성
- π₀.₅ 실패 궤적 jerk(0.00070)가 성공 궤적(0.00046)보다 유의하게 높은 반면, Hermite-VLA Reg 실패 궤적 jerk(0.00048)는 성공 궤적(0.00040)에 근접하여 평활도 향상이 생존자 편향이 아님을 증명
- 실제 로봇 경계 불연속성: Hermite-VLA Reg는 π₀.₅ 대비 0.48배로 감소(작업 3), 가속도와 jerk RMS 모두 유의하게 낮음(p < 10⁻⁴)

### 추론 비용(단일 H100, 1000회 평균)

| 방법 | 지연 시간 (ms) | FPS | 최대 메모리 (GB) |
|------|-----------|-----|---------------|
| π₀-FAST | 238.2 | 4.2 | 7.57 |
| Hermite-VLA DH | 28.9 | 34.6 | 6.66 |
| π₀.₅ | 48.4 | 20.7 | 6.63 |
| Hermite-VLA CH | 49.4 | 20.2 | 6.64 |
| Hermite-VLA Reg | 48.6 | 20.6 | 6.85 |

## 경계 및 한계

- **소프트 사전의 고유 경계**: 경계 스파이크가 축소되지만 완전히 제거되지는 않으며, 속도 연속성 보장은 시뮬레이션 시간 영역(T=10)에서 실제 로봇 시간 영역(T=50)보다 더 완화됨(1/σ_min 각각 53.0 vs 9.5)
- **단측 차분 인코더의 비용**: 끝점 속도 추정이 O(s²) 수렴률을 도입하며, 정확한 도함수를 사용하면 O(s⁴)를 회복할 수 있지만 알 수 없는 참값 정보가 필요
- **이산 채널 미모델링**: 그리퍼 등 비평활 채널은 Hermite 사전에서 제외되며, 연속 부분 공간만 제약됨
- **K 값이 T=50에서 스캔되지 않음**: 실제 로봇 시간 영역의 최적 K는 검증되지 않았으며, 시뮬레이션 결론에만 의존
- **인과 방향성이 완전히 해결되지 않음**: 평활도와 성공률 간의 인과 메커니즘은 여전히 부분적으로 외부 참조에 의존하며, 본 논문의 대조 실험은 증거를 제공하지만 완전히 닫지는 못함
- **일반화 범위 제한**: 정밀 조립, 고동적 접촉 등 복잡한 조작 시나리오는 검증되지 않음

## 공학적 시사점

- **Hermite-VLA Reg 우선 재현**: 제로 추론 오버헤드와 최고 성능, 가장 간단한 구현(훈련 시 보조 헤드만 추가)으로 공학적 비용 효율이 가장 높은 변형
- **H 행렬 조건수 확인**: T=10에서 K는 반드시 ≤ 2여야 하며, 그렇지 않으면 σ_min = 0으로 속도 보장이 퇴화됨; T=50에서 K ≤ 12는 모두 안전하지만 K=2가 여전히 경험적 최적
- **감독 공간 선택 주의**: 반드시 궤적 공간(‖Hθ − a‖₂²)에서 손실을 적용해야 하며, θ 공간에서 적용하면 속도 오차가 불균형적으로 처벌됨(최소 6.75배 강도)
- **경계 위치와 속도 별도 평가**: 위치 경계는 궤적 잔차에 의해 직접 제어되고, 속도 경계는 1/σ_min에 의해 증폭되므로, 디버깅 시 속도 스파이크가 뚜렷하면 잔차보다 σ_min을 먼저 확인해야 함
- **λ와 K 재튜닝 필요**: λ=10, K=2가 LIBERO에서 최적이지만, 벤치마크나 플랫폼이 바뀌면 재스캔이 필요하며, λ는 5–20 구간, K는 2–5 구간에서 성능이 상대적으로 평탄함
- **가장 흔한 함정**: 반올림 그리드에서 T=10, K=2일 때 i₁=4, LIBERO 창 W=5는 정확히 노드 정렬(W−1=4)되지만, 실제 로봇 W=20은 비정렬—경계 지표 평가 시 이 두 경우를 구분해야 함
