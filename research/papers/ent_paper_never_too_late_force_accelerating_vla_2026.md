---
$id: ent_paper_never_too_late_force_accelerating_vla_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection'
  zh: 'Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection'
  ko: 'Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection'
summary:
  en: Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they
    remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth
    is ambiguous, or small force errors push execution off the offline demonstration distribution. We present LIFT (Late Reactive
    Injection of Force for VLA.
  zh: LIFT（Late Reactive Injection of Force）是一种面向视觉-语言-动作（VLA）策略后训练的力注入框架，由研究团队在Flexiv Rizon 4S机器人上针对毛巾折叠、书本插入和汉诺塔环放置三个接触密集任务验证。其核心贡献在于将高频6D力信号以因果、延迟对齐的方式注入一个与预训练动作专家输出等价的反应式专家，在不破坏预训练先验的前提下加速后训练收敛并提升峰值性能。
  ko: Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they
    remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth
    is ambiguous, or small force errors push execution off the offline demonstration distribution. We present LIFT (Late Reactive
    Injection of Force for VLA.
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
- never
- too
- late
- force
- accelerating
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.14236 Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Inj'
  url: https://arxiv.org/abs/2607.14236
  date: '2026-07-15'
  accessed_at: '2026-08-05'
---

## 概述

LIFT（Late Reactive Injection of Force）是一种面向视觉-语言-动作（VLA）策略后训练的力注入框架，由研究团队在Flexiv Rizon 4S机器人上针对毛巾折叠、书本插入和汉诺塔环放置三个接触密集任务验证。其核心贡献在于将高频6D力信号以因果、延迟对齐的方式注入一个与预训练动作专家输出等价的反应式专家，在不破坏预训练先验的前提下加速后训练收敛并提升峰值性能。

## 它改变了什么

预训练VLA策略在接触状态下表现不佳的根本原因在于视觉模态的固有缺陷：遮挡、深度模糊以及微小力误差导致的执行偏移，这些都无法通过视觉单独解决。力/力矩数据之所以在预训练阶段被排除，并非其不重要，而是采集成本高、硬件依赖强、跨设置差异大，这使得后训练阶段成为注入力的唯一现实窗口。作者真正改变的是对“力参与”的定位——不是简单地增加一个输入模态，而是将其视为一种能够加速后训练过程、而非拖累其收敛的机制。

这一转变的关键在于识别出力的两个独特属性：高频（10 Hz）与低维（6D），以及其与接触动力学的紧密耦合。传统做法要么将力作为单帧特征拼接，要么在预训练阶段就引入力模态，前者无法应对瞬态接触的误导，后者则受限于数据可得性。LIFT通过将力注入设计为与预训练动作专家输出等价的反应式路径，使得力信息能够在不干扰既有先验的前提下，以逐动作刷新的方式参与决策，从而真正实现了“力加速后训练”这一假设。

## 方法拆解

### 两阶段训练流程
- **Stage 1**：使用手持数据采集设备（iPhone + ARKit SLAM）收集纯视觉任务对齐数据集 D_v = {(ℓ, I, a)}，训练纯视觉策略 π^V(a|ℓ, I)，学习粗略操作知识。
- **Stage 2**：切换到配备6D末端力传感器的Flexiv Rizon 4S机器人，通过在线DAgger收集纠正数据 D_f^(k) = {(ℓ, I, F, a*)}，在在线序列与静态视觉集上联合后训练。

### 反应式动作专家（O1.1）
在原始动作专家旁实例化一个反应式专家，要求其块内动作解码是因果的，使反应式流能随新接触逐动作刷新块。原始专家保持全注意力（每个基础动作 token a_i 可关注所有动作 token a_0:H-1），反应式专家采用移位因果注意力：r_i 看到视觉-语言前缀、后续基础动作 token a_(i+1):H-1、因果反应式前缀 r_0:i，同时屏蔽基础动作 token a_0:i 和后续反应式 token r_(i+1):H-1。

### 因果力注入交叉注意力（O1.2）
近期6D末端力块 F_(t:t+H) ∈ R^(H×6) 由单层因果GRU后接线性投影编码：m_(t:t+H) = Linear_dm(GRU_dh(F_(t:t+H))) ∈ R^(H×dm)，其中 d_h = 512，d_m = 1024。每个反应式查询 q_i 通过力注入交叉注意力关注完整力记忆序列，延迟对齐因果掩码移除不应可用的力 token：b_ij^(L) = {0, j ≤ i−L; −∞, j > i−L}，L 为匹配网络推理延迟的延迟对齐偏移（设为3）。

### 缓存视觉-语言慢上下文（O1.3）
部署时先计算一次视觉-语言前缀并存储KV缓存，块内反复编码最新延迟对齐力历史并针对缓存前缀重新评估动作专家，无需完整视觉-语言前向传播。

### 输出等价初始化（O2.1）
从预训练 π_0.5 复制原始动作专家权重到反应式专家。初始化时，复制的权重和对齐的位置使 r_0:i 等价于基础动作表示 a_0:i，移位上下文提供 a_(i+1):H-1，因此 r_i 接收与原始全注意力动作专家中 a_i 相同的上下文，实现初始化等价。

### 零初始化交叉注意力输出（O2.2）
零初始化交叉注意力块的输出投影，使力注入更新在步骤0时恰好为零，力不能改变预训练动作输出，直到后训练学到非零残差。

### 加性流匹配目标（O3.1）
对两个数据源联合训练原始和反应式动作流。采样独立噪声 ε, ε^r ~ N(0, I) 和同时间插值 x_τ, x_τ^r，最小化 L(θ) = ||v_θ(x_τ, τ, o) − u||²₂ + ||v_θ^r(x_τ^r, τ, o, m_(t:t+H)) − u^r||²₂。两个损失在同一前向传播中计算，梯度累积，共享参数联合更新。

### 选择性力掩码（O3.2）与异构数据均衡采样（O3.3）
纯视觉批次使用零力占位符并掩码编码后的力记忆，阻断梯度流向力编码器和力注入注意力；在线纠正批次保持实测力记忆激活。遵循RLPD对称采样策略，以 1:1 混合离线任务对齐批次和在线纠正批次。

## 关键创新

1. **延迟对齐的因果力记忆**：这是对力信号时间特性的根本性重新思考。力不是静态特征，而是与动作执行同步演化的动态信号。通过延迟对齐因果掩码（L=3），每个反应式动作只使用推理完成时可用的最新力测量，避免了瞬态接触脉冲（如初始碰触杆子）对策略的误导，这是单帧力注入基线不稳定的根源。

2. **输出等价初始化机制**：通过移位因果注意力设计，使得反应式专家在初始化时与原始动作专家输出严格等价，配合零初始化交叉注意力输出投影，力注入在步骤0时恰好为零。这保证了预训练先验在初始化阶段完全不受干扰，后训练过程只需学习力的非零残差，而非重新学习整个动作分布。

3. **双流联合训练与选择性力掩码**：加性流匹配目标让原始和反应式动作流在同一前向传播中联合优化，共享参数更新。选择性力掩码确保纯视觉批次不会污染力编码器，而在线纠正批次则激活力记忆，实现了异构数据源的无缝混合训练，这是力数据稀缺条件下保持训练稳定的关键。

## 实验与结果

实验在三个真实机器人任务上对比了五个变体：π_0.5 w/ Online DAgger（无力的在线DAgger）、LIFT w/o Reactive Force Injection（单帧力输入）、LIFT w/o Online DAgger（无重复在线更新）、π_0.5 w/ Offline Handheld Data（仅离线手持数据）、LIFT（完整方法）。每个检查点用十次自主rollout评估。

| 任务 | 指标 | π_0.5 w/ Online DAgger | LIFT w/o Reactive Force | LIFT（完整） |
|------|------|------------------------|------------------------|-------------|
| 毛巾折叠 | 峰值分数 | 0.725 (#3.1K) | 0.95 (#2.8K) | 0.825 (#2.8K) |
| 毛巾折叠 | 达到0.65样本数 | #3.1K | #2.4K | #2.3K |
| 书本插入 | 峰值分数 | 0.4 (#5.6K) | 0.4 (#5.0K/#5.3K) | 0.6 (#4.6K) |
| 汉诺塔环 | 峰值分数 | 0.3 (#1.4K) | 0.5 (#0.7K) | 0.6 (#1.7K) |
| 汉诺塔环 | 最终分数 | 0.2 (#1.6K) | 0.1 (#1.7K) | 0.6 (#2.0K) |

关键发现：LIFT在书本插入和汉诺塔任务上显著优于无力的在线DAgger基线（0.6 vs 0.4、0.6 vs 0.3），且收敛更快。毛巾折叠任务中，LIFT w/o Reactive Force Injection达到最高峰值0.95，但LIFT以更少样本（#2.3K vs #3.1K）达到0.65，说明反应式力注入主要加速收敛而非提升绝对峰值。汉诺塔任务中，单帧力注入基线在#0.7K达到0.5后急剧下降至0.1，而LIFT保持稳定0.6，验证了延迟对齐因果掩码对瞬态接触鲁棒性的关键作用。LIFT w/o Online DAgger在所有任务上表现不佳（书本插入降至零），证明在线纠正数据不可或缺。

## 边界与局限

LIFT仍依赖在线DAgger期间的人类纠正，限制了数据吞吐量，这是作者明确承认的瓶颈。评估仅限于单臂操作，未涉及双臂协作或更复杂的多接触场景。所有任务使用单相机设置，未验证多相机输入下的表现。论文未明确在仿真环境中的验证，也未讨论力传感器噪声或漂移对性能的影响。泛化实验仅改变物体、桌布和光照，未测试不同机器人平台或末端执行器下的迁移能力。此外，延迟对齐偏移L=3是针对当前系统推理延迟调参的结果，在其他硬件配置下可能需要重新调整。

## 工程启示

复现LIFT时，最先需要核对的是延迟对齐偏移量L=3与自身系统推理延迟的匹配关系——这是反应式力注入稳定性的核心超参数，若推理管线延迟不同，直接沿用该值可能导致力信息错位。其次，输出等价初始化依赖移位因果注意力的精确实现，务必验证初始化时反应式专家输出与原始专家严格一致（误差应为零），否则预训练先验会被破坏。训练配置中，1:1的离线/在线数据混合比例（RLPD对称采样）和选择性力掩码是联合训练稳定的关键，纯视觉批次必须阻断力编码器梯度。在线DAgger的检查点同步频率（每100训练步推送）直接影响数据新鲜度，建议根据训练吞吐量调整。部署时，缓存视觉-语言KV前缀并仅刷新力历史是达到10 Hz执行频率的前提，若计算资源不足可考虑降低力编码器宽度（d_m=1024）或GRU隐藏宽度（512）。最后，所有动作均为相对动作并填充到32维共享输出维度，数据预处理时需严格对齐这一格式，否则会导致训练不收敛。

## Overview
Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth is ambiguous, or small force errors push execution off the offline demonstration distribution. We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-training framework that adds contact reactivity to a pretrained VLA policy while preserving its general manipulation knowledge. LIFT grafts a reactive action expert beside the original action expert, initializes it from pretrained action weights, and injects recent 6D end-effector force through causal force memory and zero-initialized cross attention, enabling actions to be refreshed during execution. To address the policy-dependent distribution shift of contact feedback, LIFT further couples reactive force injection with an online DAgger loop that trains on a mixture of offline task-alignment data and human-corrected online rollouts. Across towel folding, book insertion, and Hanoi ring placement, LIFT learns faster and reaches higher performance than vision-only post-training, while ablations show that reactive force memory and online corrective data are both important for robust contact-rich manipulation. Our code and data will be publicly available.

## 参考
- https://arxiv.org/abs/2607.14236

## 개요

LIFT(Late Reactive Injection of Force)는 시각-언어-동작(VLA) 정책의 후훈련(post-training)을 위한 힘 주입 프레임워크로, 연구팀이 Flexiv Rizon 4S 로봇에서 수건 접기, 책 삽입, 하노이 탑 링 배치라는 세 가지 접촉 집약적 작업을 통해 검증했다. 핵심 기여는 고주파 6D 힘 신호를 인과적(causal)이고 지연 정렬된 방식으로, 사전 훈련된 동작 전문가 출력과 동등한 반응형 전문가(reactive expert)에 주입하여 사전 훈련 사전 지식을 손상시키지 않으면서 후훈련 수렴을 가속화하고 최고 성능을 향상시키는 데 있다.

## 무엇을 바꾸었는가

사전 훈련된 VLA 정책이 접촉 상태에서 성능이 저조한 근본 원인은 시각 양식의 고유한 결함에 있다: 가림, 깊이 흐림, 그리고 미세한 힘 오차로 인한 실행 편향은 시각만으로는 해결할 수 없다. 힘/토크 데이터가 사전 훈련 단계에서 제외된 이유는 중요하지 않아서가 아니라, 수집 비용이 높고 하드웨어 의존성이 강하며 설정 간 차이가 크기 때문이며, 이로 인해 후훈련 단계가 힘 주입의 유일한 현실적 창구가 된다. 저자가 실제로 바꾼 것은 "힘 참여"의 위치이다 — 단순히 입력 양식을 추가하는 것이 아니라, 후훈련 과정을 지연시키지 않고 오히려 가속화할 수 있는 메커니즘으로 간주한 것이다.

이 전환의 핵심은 힘의 두 가지 독특한 속성, 즉 고주파(10 Hz)와 저차원(6D), 그리고 접촉 역학과의 긴밀한 결합을 식별한 데 있다. 전통적 접근 방식은 힘을 단일 프레임 특징으로 연결하거나 사전 훈련 단계에서 힘 양식을 도입하는데, 전자는 과도 접촉의 오도를 처리할 수 없고 후자는 데이터 가용성에 제약을 받는다. LIFT는 힘 주입을 사전 훈련된 동작 전문가 출력과 동등한 반응형 경로로 설계함으로써, 힘 정보가 기존 사전 지식을 방해하지 않으면서 동작별 갱신 방식으로 의사 결정에 참여할 수 있게 하여 "힘이 후훈련을 가속화한다"는 가설을 실제로 구현했다.

## 방법 분해

### 2단계 훈련 흐름
- **Stage 1**: 휴대용 데이터 수집 장치(iPhone + ARKit SLAM)를 사용하여 순수 시각 작업 정렬 데이터셋 D_v = {(ℓ, I, a)}를 수집하고, 순수 시각 정책 π^V(a|ℓ, I)를 훈련하여 대략적인 조작 지식을 학습한다.
- **Stage 2**: 6D 말단 힘 센서가 장착된 Flexiv Rizon 4S 로봇으로 전환하고, 온라인 DAgger를 통해 교정 데이터 D_f^(k) = {(ℓ, I, F, a*)}를 수집하여 온라인 시퀀스와 정적 시각 데이터셋에서 공동 후훈련한다.

### 반응형 동작 전문가 (O1.1)
원래 동작 전문가 옆에 반응형 전문가를 인스턴스화하고, 블록 내 동작 디코딩이 인과적이도록 요구하여 반응형 흐름이 새로운 접촉에 따라 동작별로 블록을 갱신할 수 있게 한다. 원래 전문가는 전체 어텐션(각 기본 동작 토큰 a_i가 모든 동작 토큰 a_0:H-1을 볼 수 있음)을 유지하고, 반응형 전문가는 이동 인과 어텐션(shifted causal attention)을 사용한다: r_i는 시각-언어 접두사, 후속 기본 동작 토큰 a_(i+1):H-1, 인과적 반응형 접두사 r_0:i를 보지만 기본 동작 토큰 a_0:i와 후속 반응형 토큰 r_(i+1):H-1은 차단한다.

### 인과적 힘 주입 교차 어텐션 (O1.2)
최근 6D 말단 힘 블록 F_(t:t+H) ∈ R^(H×6)은 단일 레이어 인과 GRU 후 선형 투영으로 인코딩된다: m_(t:t+H) = Linear_dm(GRU_dh(F_(t:t+H))) ∈ R^(H×dm), 여기서 d_h = 512, d_m = 1024. 각 반응형 쿼리 q_i는 힘 주입 교차 어텐션을 통해 전체 힘 메모리 시퀀스를 주목하며, 지연 정렬 인과 마스크는 사용할 수 없는 힘 토큰을 제거한다: b_ij^(L) = {0, j ≤ i−L; −∞, j > i−L}, L은 네트워크 추론 지연과 일치하는 지연 정렬 오프셋(3으로 설정).

### 캐시된 시각-언어 느린 컨텍스트 (O1.3)
배포 시 시각-언어 접두사를 한 번 계산하고 KV 캐시를 저장한 후, 블록 내에서 최신 지연 정렬 힘 이력을 반복적으로 인코딩하고 캐시된 접두사에 대해 동작 전문가를 재평가하며, 전체 시각-언어 순방향 전파가 필요 없다.

### 출력 등가 초기화 (O2.1)
사전 훈련된 π_0.5에서 원래 동작 전문가 가중치를 반응형 전문가로 복사한다. 초기화 시 복사된 가중치와 정렬된 위치로 인해 r_0:i는 기본 동작 표현 a_0:i와 동등하며, 이동 컨텍스트가 a_(i+1):H-1을 제공하므로 r_i는 원래 전체 어텐션 동작 전문가에서 a_i가 받는 것과 동일한 컨텍스트를 받아 초기화 등가를 구현한다.

### 교차 어텐션 출력의 제로 초기화 (O2.2)
교차 어텐션 블록의 출력 투영을 제로 초기화하여 힘 주입 갱신이 단계 0에서 정확히 0이 되도록 하며, 후훈련이 비제로 잔차를 학습할 때까지 힘이 사전 훈련된 동작 출력을 변경할 수 없다.

### 가산적 흐름 매칭 목표 (O3.1)
두 데이터 소스에 대해 원래 및 반응형 동작 흐름을 공동 훈련한다. 독립 노이즈 ε, ε^r ~ N(0, I)와 동일 시간 보간 x_τ, x_τ^r을 샘플링하고, L(θ) = ||v_θ(x_τ, τ, o) − u||²₂ + ||v_θ^r(x_τ^r, τ, o, m_(t:t+H)) − u^r||²₂를 최소화한다. 두 손실은 동일한 순방향 전파에서 계산되고, 기울기가 누적되며, 공유 파라미터가 공동으로 갱신된다.

### 선택적 힘 마스크 (O3.2) 및 이종 데이터 균형 샘플링 (O3.3)
순수 시각 배치는 제로 힘 플레이스홀더를 사용하고 인코딩된 힘 메모리를 마스킹하여 힘 인코더와 힘 주입 어텐션으로의 기울기 흐름을 차단한다; 온라인 교정 배치는 실제 측정된 힘 메모리를 활성화 상태로 유지한다. RLPD 대칭 샘플링 전략을 따라 오프라인 작업 정렬 배치와 온라인 교정 배치를 1:1로 혼합한다.

## 핵심 혁신

1. **지연 정렬된 인과적 힘 메모리**: 이는 힘 신호의 시간적 특성에 대한 근본적인 재고이다. 힘은 정적 특징이 아니라 동작 실행과 동기화되어 진화하는 동적 신호이다. 지연 정렬 인과 마스크(L=3)를 통해 각 반응형 동작은 추론 완료 시 사용 가능한 최신 힘 측정만 사용하므로, 과도 접촉 펄스(예: 초기 막대 접촉)가 정책을 오도하는 것을 방지하며, 이는 단일 프레임 힘 주입 기준선이 불안정한 근본 원인이다.

2. **출력 등가 초기화 메커니즘**: 이동 인과 어텐션 설계를 통해 반응형 전문가가 초기화 시 원래 동작 전문가 출력과 엄격히 동등하도록 하고, 교차 어텐션 출력 투영의 제로 초기화와 결합하여 힘 주입이 단계 0에서 정확히 0이 되도록 보장한다. 이는 사전 훈련 사전 지식이 초기화 단계에서 완전히 방해받지 않도록 하며, 후훈련 과정은 전체 동작 분포를 다시 학습하는 대신 힘의 비제로 잔차만 학습하면 된다.

3. **이중 흐름 공동 훈련 및 선택적 힘 마스크**: 가산적 흐름 매칭 목표는 원래 및 반응형 동작 흐름이 동일한 순방향 전파에서 공동 최적화되고 공유 파라미터가 갱신되도록 한다. 선택적 힘 마스크는 순수 시각 배치가 힘 인코더를 오염시키지 않도록 보장하고, 온라인 교정 배치는 힘 메모리를 활성화하여 이종 데이터 소스의 원활한 혼합 훈련을 구현하며, 이는 힘 데이터가 부족한 조건에서 훈련 안정성을 유지하는 핵심이다.

## 실험 및 결과

실험은 세 가지 실제 로봇 작업에서 다섯 가지 변형을 비교했다: π_0.5 w/ Online DAgger(힘 없는 온라인 DAgger), LIFT w/o Reactive Force Injection(단일 프레임 힘 입력), LIFT w/o Online DAgger(반복 온라인 갱신 없음), π_0.5 w/ Offline Handheld Data(오프라인 휴대 데이터만), LIFT(전체 방법). 각 체크포인트는 10회 자율 롤아웃으로 평가되었다.

| 작업 | 지표 | π_0.5 w/ Online DAgger | LIFT w/o Reactive Force | LIFT(전체) |
|------|------|------------------------|------------------------|-------------|
| 수건 접기 | 최고 점수 | 0.725 (#3.1K) | 0.95 (#2.8K) | 0.825 (#2.8K) |
| 수건 접기 | 0.65 도달 샘플 수 | #3.1K | #2.4K | #2.3K |
| 책 삽입 | 최고 점수 | 0.4 (#5.6K) | 0.4 (#5.0K/#5.3K) | 0.6 (#4.6K) |
| 하노이 탑 링 | 최고 점수 | 0.3 (#1.4K) | 0.5 (#0.7K) | 0.6 (#1.7K) |
| 하노이 탑 링 | 최종 점수 | 0.2 (#1.6K) | 0.1 (#1.7K) | 0.6 (#2.0K) |

핵심 발견: LIFT는 책 삽입 및 하노이 탑 작업에서 힘 없는 온라인 DAgger 기준선보다 크게 우수하며(0.6 vs 0.4, 0.6 vs 0.3), 수렴도 더 빠르다. 수건 접기 작업에서 LIFT w/o Reactive Force Injection은 최고 0.95에 도달했지만, LIFT는 더 적은 샘플(#2.3K vs #3.1K)로 0.65에 도달하여 반응형 힘 주입이 주로 수렴을 가속화하고 절대 최고점을 높이는 것이 아님을 보여준다. 하노이 탑 작업에서 단일 프레임 힘 주입 기준선은 #0.7K에서 0.5에 도달한 후 급격히 0.1로 하락한 반면, LIFT는 안정적인 0.6을 유지하여 지연 정렬 인과 마스크가 과도 접촉에 대한 견고성에 핵심적인 역할을 한다는 것을 검증한다. LIFT w/o Online DAgger는 모든 작업에서 성능이 저조했으며(책 삽입은 0으로 하락), 온라인 교정 데이터가 필수적임을 증명한다.

## 경계 및 한계

LIFT는 여전히 온라인 DAgger 동안 인간 교정에 의존하므로 데이터 처리량이 제한되며, 이는 저자가 명시적으로 인정한 병목이다. 평가는 단일 팔 조작에만 국한되었고, 양팔 협업이나 더 복잡한 다중 접촉 시나리오는 다루지 않았다. 모든 작업은 단일 카메라 설정을 사용했으며, 다중 카메라 입력에서의 성능은 검증되지 않았다. 논문은 시뮬레이션 환경에서의 검증을 명시하지 않았고, 힘 센서 노이즈나 드리프트가 성능에 미치는 영향도 논의하지 않았다. 일반화 실험은 물체, 테이블보, 조명만 변경했으며, 다른 로봇 플랫폼이나 말단 효과기에서의 전이 능력은 테스트하지 않았다. 또한 지연 정렬 오프셋 L=3은 현재 시스템 추론 지연에 맞춰 조정된 결과이므로, 다른 하드웨어 구성에서는 재조정이 필요할 수 있다.

## 공학적 시사점

LIFT를 재현할 때 가장 먼저 확인해야 할 것은 지연 정렬 오프셋 L=3과 자체 시스템 추론 지연의 일치 관계이다 — 이는 반응형 힘 주입 안정성의 핵심 하이퍼파라미터이며, 추론 파이프라인 지연이 다르면 이 값을 그대로 사용할 경우 힘 정보가 어긋날 수 있다. 둘째, 출력 등가 초기화는 이동 인과 어텐션의 정확한 구현에 의존하므로, 초기화 시 반응형 전문가 출력이 원래 전문가와 엄격히 일치하는지(오차가 0이어야 함) 반드시 검증해야 하며, 그렇지 않으면 사전 훈련 사전 지식이 손상된다. 훈련 구성에서 1:1 오프라인/온라인 데이터 혼합 비율(RLPD 대칭 샘플링)과 선택적 힘 마스크는 공동 훈련 안정성의 핵심이며, 순수 시각 배치는 힘 인코더 기울기를 반드시 차단해야 한다. 온라인 DAgger의 체크포인트 동기화 빈도(100 훈련 단계마다 푸시)는 데이터 신선도에 직접 영향을 미치므로 훈련 처리량에 따라 조정하는 것이 좋다. 배포 시 시각-언어 KV 접두사를 캐시하고 힘 이력만 갱신하는 것이 10 Hz 실행 빈도를 달성하는 전제 조건이며, 계산 자원이 부족하면 힘 인코더 너비(d_m=1024)나 GRU 숨김 너비(512)를 줄이는 것을 고려할 수 있다. 마지막으로 모든 동작은 상대 동작이며 32차원 공유 출력 차원으로 패딩되므로, 데이터 전처리 시 이 형식을 엄격히 정렬해야 하며 그렇지 않으면 훈련이 수렴하지 않는다.
