---
$id: ent_paper_human_like_physical_intelligence_lifelon_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learning for Robotic Manipulation'
  zh: 'Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learning for Robotic Manipulation'
  ko: 'Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learning for Robotic Manipulation'
summary:
  en: Similar to the natural capabilities of humans to sequentially learn new tasks, robots with Vision-Language-Action (VLA)
    models should possess lifelong learning ability to learn a new task when deployed in open-world environments. However,
    most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high
    accuracy on previous tasks (stability),.
  zh: LifelongVLA 提出一种面向机器人操作的双时间尺度 LoRA 门控与缓存高效随机重放框架，在冻结 PaliGemma 骨干上实现终身视觉-语言-动作学习。该方法通过短期/长期适配器分离可塑性与稳定性，以紧凑前缀缓存替代全轨迹重放，在
    LIBERO 基准上达到 83.2% 平均成功率与 11.4% 平均遗忘率，并完成 xArm 真实机器人五任务验证。
  ko: Similar to the natural capabilities of humans to sequentially learn new tasks, robots with Vision-Language-Action (VLA)
    models should possess lifelong learning ability to learn a new task when deployed in open-world environments. However,
    most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high
    accuracy on previous tasks (stability),.
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
- human
- like
- physical
- intelligence
- lifelon
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.14852 Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learni'
  url: https://arxiv.org/abs/2607.14852
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

LifelongVLA 提出一种面向机器人操作的双时间尺度 LoRA 门控与缓存高效随机重放框架，在冻结 PaliGemma 骨干上实现终身视觉-语言-动作学习。该方法通过短期/长期适配器分离可塑性与稳定性，以紧凑前缀缓存替代全轨迹重放，在 LIBERO 基准上达到 83.2% 平均成功率与 11.4% 平均遗忘率，并完成 xArm 真实机器人五任务验证。

## 它改变了什么

静态离线训练的 VLA 范式在真实部署中面临根本性失效：新物体、新指令、新布局持续出现，而模型权重一旦固定便无法适应。直接顺序微调导致灾难性遗忘，保留全部历史数据重训则内存与计算开销不可承受。现有增量方法——重放缓冲、架构扩展、参数隔离——均未真正解决可塑性-稳定性困境：简单经验重放对 VLA 有效但需存储图像丰富片段并反复重新编码，架构扩展则引入路由成本与推理延迟。

LifelongVLA 改变了这一格局的核心在于：它不再将终身学习视为"如何存储更多旧数据"或"如何扩展更多参数"，而是重新思考 VLA 适配器内部的信息流。通过将单一 LoRA 路径拆分为双时间尺度更新，它让可塑性与稳定性成为可独立控制的变量；通过缓存冻结前缀而非原始轨迹，它将重放成本从"重新编码整个观测"降为"仅重计算轻量后缀"。这使终身学习从"昂贵的必要之恶"变为"近乎免费的能力扩展"。

## 方法拆解

### 双时间尺度 LoRA 门控
- 短期适配器 `ψ_sh` 仅由当前任务损失更新：`ψ_sh,t ← ψ_sh,t − η_sh ∇ψ_sh L_new`
- 长期适配器 `ψ_lg` 仅由重放与蒸馏信号更新：`ψ_lg,t ← ψ_lg,t − η_lg ∇ψ_lg (λ L_rep + β L_dist)`
- 设置 `η_lg < η_sh`，长期路径演化更慢，形成"快速学习新技能、慢速巩固旧记忆"的时间尺度分离
- 门控上下文 `c = Pool(stopgrad(E_pre(u; Θ_0)))` 从冻结前缀特征计算，避免门控依赖自身控制的权重造成循环
- 权重级组合：`ΔŴ_t^ℓ(c) = (1−α_t^ℓ(c)) ΔW_sh,t^ℓ + α_t^ℓ(c) ΔW_lg,t^ℓ`，`α_t^ℓ(c) = σ(W_g^ℓ φ^ℓ(c) + b_g^ℓ)`
- 关键设计：权重级组合保证推理仅需单次前向传播，无需两次前向或修改骨干

### 缓存高效随机重放
- 每任务随机选择技能级子集 `R_t ⊆ Ω_t`，`|R_t| = min(c_t, |Ω_t|)`
- 重放缓冲仅存储 stop-gradient 前缀 token 与紧凑状态-动作监督：`B_t = Reservoir_M(B_{t−1} ∪ {(h̄_i,t^pre, s_i^t, y_i^t) : i ∈ R_t})`
- 不存储原始图像、语言 token、后缀 token、扩散时间步或扩散噪声
- 重放时重新采样扩散变量：`τ_j' ~ p(τ)`，`ϵ_j' ~ N(0, I)`，`ỹ_τ_j'^rep = q_τ_j'(y_j, ϵ_j')`
- 缓存前缀与当前模型重计算的后缀 token 组合，每次重放重新采样 τ 和 ϵ，使每个缓存前缀可生成多个随机重放实例

### 掩码新-重放目标
- 当前样本与重放样本在同一 mini-batch 拼接并打乱，用掩码 `m_i ∈ {0,1}` 区分
- 当前损失：`L_new = (1/|M_new|) Σ_{i∈M} (1−m_i) ℓ(η̂_i, η_i*)`
- 重放损失：`L_rep = (1/|M_rep|) Σ_{i∈M} m_i ℓ(η̂_i, η_i*)`
- 蒸馏损失：`L_dist = (1/|M_rep|) Σ_{i∈M} m_i ‖η̂_i − stopgrad(η̂_i^old)‖_2^2`，教师为任务 t−1 的分离模型快照
- 最终目标：`L_t = L_new + λ L_rep + β L_dist`，当前项与重放项分别归一化防止某一来源主导

## 关键创新

**双时间尺度 LoRA 门控**是核心创新。以往单 LoRA 适配器用同一更新路径同时追求可塑性与稳定性，导致两者纠缠难以控制。分解为双路径后，短期路径快速吸收新任务分布，长期路径通过重放与蒸馏缓慢巩固，门控根据冻结前缀特征动态决定每条路径的贡献权重。这一设计使"学新"与"保旧"成为可独立调节的变量，而非相互妥协的折中。

**缓存高效随机重放**解决了 VLA 终身学习的存储瓶颈。全轨迹重放需存储图像丰富片段并反复重新编码旧观测，而该方法仅缓存冻结前缀 token 与紧凑监督信号，重放时重新采样扩散变量并重计算后缀。这不仅将内存从 167.62 MiB/task 降至 95.70 MiB/task（由表内数值计算），还通过每次重放生成多样化实例增强了保留信号的丰富性。前缀作为旧技能记忆锚点，重计算后缀则消除缓存与当前表示之间的陈旧不匹配。

**掩码新-重放目标**的分别归一化设计看似简单却至关重要。当前样本与重放样本在同一 mini-batch 中拼接打乱，若不做分别归一化，相对批大小差异会导致某一来源主导梯度。这一细节保证了双路径更新信号的均衡性，是双时间尺度机制稳定工作的前提。

## 实验与结果

LIBERO 基准 10 任务增量学习，冻结 PaliGemma 骨干 + Gemma 2B + Gemma 300M 连续动作解码器，终身方法每任务 10000 步，联合训练 40000 步。超参数 r=16，γ=16，M=500，c_t=50，λ=1.0，β=0.1。

| 方法 | 平均 SR (%) | 平均 FOR (%) |
|---|---|---|
| Joint（上界） | 89.6 | — |
| SFT | 7.8 | 76.8 |
| LwF-LoRA | 7.8 | 72.6 |
| ER | 70.2 | 19.6 |
| Info-VLA | 28.6 | 21.2 |
| AtomicVLA | 28.6 | 39.2 |
| **Ours** | **83.2** | **11.4** |

相比最强基线 ER，SR 提升 13.0 个百分点、FOR 降低 8.2 个百分点（由表内数值计算）。任务级表现突出：任务 5 达 96%、任务 9 达 98%、任务 10 达 96%，任务 9 的 FOR 为 0。消融显示：潜在重放将内存从 167.62 MiB/task 降至 95.70 MiB/task（相同 49.99M 可训练参数），SR 相当且 FOR 更低；双 LoRA 相比单 LoRA 提升 SR 并降低 FOR，可训练参数增至 99.97M 但仍远小于 AtomicVLA 的 226.49M 参数和 452.98 MiB/task 内存。真实机器人 xArm 五任务流，每任务 50 个训练片段，学习完所有任务后每任务成功率均高于 80%。

## 边界与局限

当前评估在任务规模与多样性上有限。真实世界终身学习可能涉及更长任务流、更多样物体类别、更丰富场景布局，以及长时间部署中收集的非均匀数据。论文未评估更长和更多异构任务序列，未随机化任务顺序，未跨多个流报告均值和方差。实验使用清晰语言指令，真实用户可能提供更多样、模糊或对话式命令（省略、共指、上下文依赖），论文未引入释义、对话式和上下文相关指令来评估语言鲁棒性，也未使用语言增强或指令改写提升模型处理多样用户表达的能力。测试时任务身份不可用，但任务顺序固定，顺序敏感性未验证。

## 工程启示

复现时先核对门控上下文的 stop-gradient 实现——这是避免循环依赖的关键，若去掉会导致训练不稳定。双时间尺度更新中 `η_lg < η_sh` 的比例需要仔细调参，论文未明确具体数值，建议从 10:1 起步。重放缓存仅存前缀 token 与紧凑监督，实现时需确保前缀确实来自冻结骨干且不参与梯度。掩码新-重放目标中分别归一化是必须的，否则相对批大小差异会破坏双路径均衡。蒸馏损失中教师快照需在任务切换时分离保存，stop-gradient 位置错误会导致梯度泄漏。真实机器人部署时注意每任务 50 个训练片段的数据量级，若数据更少可能需要调整 `c_t` 配额。最易踩坑处：扩散变量 τ 和 ϵ 的重新采样逻辑——若沿用原始时间步与噪声，缓存前缀将无法生成多样化重放实例，丧失随机重放的核心优势。

## Overview
Similar to the natural capabilities of humans to sequentially learn new tasks, robots with Vision-Language-Action (VLA) models should possess lifelong learning ability to learn a new task when deployed in open-world environments. However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation models. To address this fundamental challenge, we propose a cache-efficient lifelong Vision-Language-Action learning framework for robotic manipulation (i.e., LifelongVLA), which alleviates the plasticity-stability trade-off with a dual-timescale adaptation mechanism while achieving low-cost robotic deployment with a cache-efficient replay strategy. More concretely, we propose a dual-timescale LoRA gating module to decompose VLA adaptation into two lightweight pathways: a short-term adapter for plasticity and a long-term adapter for stable consolidation. These pathways are integrated via a task-aware gate, enabling explicit control of the plasticity-stability trade-off. In the skill replay phase, a cache-efficient stochastic replay strategy is proposed to preserve more balanced retention signals without full-trajectory storage. Finally, experiments show that LifelongVLA outperforms existing baselines, demonstrating efficient skill expansion, robust retention of learned manipulation behaviors, and reduced reliance on retraining for real-world deployment on an xArm robot.

## 参考
- https://arxiv.org/abs/2607.14852

## 개요

LifelongVLA는 로봇 조작을 위한 이중 시간 척도 LoRA 게이팅과 캐시 효율적 무작위 리플레이 프레임워크를 제안하며, 동결된 PaliGemma 백본에서 평생 비전-언어-행동 학습을 구현한다. 이 방법은 단기/장기 어댑터를 통해 가소성과 안정성을 분리하고, 전체 궤적 리플레이 대신 컴팩트한 프리픽스 캐시를 사용하여 LIBERO 벤치마크에서 83.2% 평균 성공률과 11.4% 평균 망각률을 달성하며, xArm 실제 로봇 5개 작업 검증을 완료한다.

## 그것이 바꾸는 것

정적 오프라인 훈련 VLA 패러다임은 실제 배포에서 근본적으로失效한다: 새로운 객체, 새로운 지시, 새로운 레이아웃이 지속적으로 등장하지만 모델 가중치가 한번 고정되면 적응할 수 없다. 직접 순차 미세 조정은 치명적 망각을 초래하고, 전체 과거 데이터를 유지하며 재훈련하면 메모리와 계산 비용이 감당할 수 없게 된다. 기존 증분 방법(리플레이 버퍼, 아키텍처 확장, 파라미터 격리)은 모두 가소성-안정성 딜레마를 진정으로 해결하지 못한다: 단순 경험 리플레이는 VLA에 효과적이지만 이미지가 풍부한 에피소드를 저장하고 반복적으로 재인코딩해야 하며, 아키텍처 확장은 라우팅 비용과 추론 지연을 도입한다.

LifelongVLA가 이 구도를 바꾸는 핵심은: 평생 학습을 "더 많은 과거 데이터를 저장하는 방법"이나 "더 많은 파라미터를 확장하는 방법"으로 보지 않고, VLA 어댑터 내부의 정보 흐름을 재고하는 것이다. 단일 LoRA 경로를 이중 시간 척도 업데이트로 분할함으로써 가소성과 안정성을 독립적으로 제어 가능한 변수로 만들고, 원시 궤적 대신 동결된 프리픽스를 캐시함으로써 리플레이 비용을 "전체 관측 재인코딩"에서 "경량 접미사만 재계산"으로 낮춘다. 이로써 평생 학습은 "비싼 필요악"에서 "거의 무료의 능력 확장"이 된다.

## 방법 분해

### 이중 시간 척도 LoRA 게이팅
- 단기 어댑터 `ψ_sh`는 현재 작업 손실로만 업데이트: `ψ_sh,t ← ψ_sh,t − η_sh ∇ψ_sh L_new`
- 장기 어댑터 `ψ_lg`는 리플레이와 증류 신호로만 업데이트: `ψ_lg,t ← ψ_lg,t − η_lg ∇ψ_lg (λ L_rep + β L_dist)`
- `η_lg < η_sh`로 설정하여 장기 경로가 더 느리게 진화하며 "새 기술 빠르게 학습, 오래된 기억 천천히 강화"의 시간 척도 분리를 형성
- 게이팅 컨텍스트 `c = Pool(stopgrad(E_pre(u; Θ_0)))`는 동결된 프리픽스 특징에서 계산되어 게이팅이 자신이 제어하는 가중치에 의존하는 순환을 방지
- 가중치 수준 결합: `ΔŴ_t^ℓ(c) = (1−α_t^ℓ(c)) ΔW_sh,t^ℓ + α_t^ℓ(c) ΔW_lg,t^ℓ`, `α_t^ℓ(c) = σ(W_g^ℓ φ^ℓ(c) + b_g^ℓ)`
- 핵심 설계: 가중치 수준 결합은 추론 시 단일 순방향 전파만 필요하며, 두 번의 순방향이나 백본 수정이 필요 없음

### 캐시 효율적 무작위 리플레이
- 각 작업에서 기술 수준 하위 집합 `R_t ⊆ Ω_t`을 무작위 선택, `|R_t| = min(c_t, |Ω_t|)`
- 리플레이 버퍼는 stop-gradient 프리픽스 토큰과 컴팩트 상태-행동 감독만 저장: `B_t = Reservoir_M(B_{t−1} ∪ {(h̄_i,t^pre, s_i^t, y_i^t) : i ∈ R_t})`
- 원시 이미지, 언어 토큰, 접미사 토큰, 확산 시간 단계, 확산 노이즈는 저장하지 않음
- 리플레이 시 확산 변수 재샘플링: `τ_j' ~ p(τ)`, `ϵ_j' ~ N(0, I)`, `ỹ_τ_j'^rep = q_τ_j'(y_j, ϵ_j')`
- 캐시된 프리픽스와 현재 모델이 재계산한 접미사 토큰을 결합하고, 각 리플레이마다 τ와 ϵ을 재샘플링하여 각 캐시 프리픽스가 여러 무작위 리플레이 인스턴스를 생성할 수 있게 함

### 마스크된 신규-리플레이 목표
- 현재 샘플과 리플레이 샘플을 동일한 미니배치에 연결하고 섞으며, 마스크 `m_i ∈ {0,1}`로 구분
- 현재 손실: `L_new = (1/|M_new|) Σ_{i∈M} (1−m_i) ℓ(η̂_i, η_i*)`
- 리플레이 손실: `L_rep = (1/|M_rep|) Σ_{i∈M} m_i ℓ(η̂_i, η_i*)`
- 증류 손실: `L_dist = (1/|M_rep|) Σ_{i∈M} m_i ‖η̂_i − stopgrad(η̂_i^old)‖_2^2`, 교사는 작업 t−1의 분리된 모델 스냅샷
- 최종 목표: `L_t = L_new + λ L_rep + β L_dist`, 현재 항과 리플레이 항을 각각 정규화하여 한 소스가 지배하지 않도록 함

## 핵심 혁신

**이중 시간 척도 LoRA 게이팅**은 핵심 혁신이다. 기존 단일 LoRA 어댑터는 동일한 업데이트 경로로 가소성과 안정성을 동시에 추구하여 둘이 얽혀 제어하기 어려웠다. 이중 경로로 분해한 후, 단기 경로는 새 작업 분포를 빠르게 흡수하고 장기 경로는 리플레이와 증류를 통해 천천히 강화하며, 게이팅은 동결된 프리픽스 특징에 따라 각 경로의 기여 가중치를 동적으로 결정한다. 이 설계는 "새것 학습"과 "옛것 유지"를 서로 타협하는 절충이 아닌 독립적으로 조절 가능한 변수로 만든다.

**캐시 효율적 무작위 리플레이**는 VLA 평생 학습의 저장 병목을 해결한다. 전체 궤적 리플레이는 이미지가 풍부한 에피소드를 저장하고 오래된 관측을 반복적으로 재인코딩해야 하지만, 이 방법은 동결된 프리픽스 토큰과 컴팩트 감독 신호만 캐시하고 리플레이 시 확산 변수를 재샘플링하며 접미사를 재계산한다. 이는 메모리를 167.62 MiB/작업에서 95.70 MiB/작업으로 줄일 뿐만 아니라(표 내 수치로 계산), 각 리플레이마다 다양한 인스턴스를 생성하여 유지 신호의 풍부성을 강화한다. 프리픽스는 오래된 기술의 기억 앵커 역할을 하고, 접미사 재계산은 캐시와 현재 표현 사이의 낡은 불일치를 제거한다.

**마스크된 신규-리플레이 목표**의 개별 정규화 설계는 단순해 보이지만 결정적이다. 현재 샘플과 리플레이 샘플이 동일한 미니배치에 연결되어 섞이므로, 개별 정규화를 하지 않으면 상대적 배치 크기 차이로 한 소스가 그라디언트를 지배하게 된다. 이 세부 사항은 이중 경로 업데이트 신호의 균형을 보장하며, 이중 시간 척도 메커니즘이 안정적으로 작동하는 전제 조건이다.

## 실험 및 결과

LIBERO 벤치마크 10개 작업 증분 학습, 동결된 PaliGemma 백본 + Gemma 2B + Gemma 300M 연속 행동 디코더, 평생 방법은 작업당 10000 스텝, 공동 훈련은 40000 스텝. 하이퍼파라미터 r=16, γ=16, M=500, c_t=50, λ=1.0, β=0.1.

| 방법 | 평균 SR (%) | 평균 FOR (%) |
|---|---|---|
| Joint (상한) | 89.6 | — |
| SFT | 7.8 | 76.8 |
| LwF-LoRA | 7.8 | 72.6 |
| ER | 70.2 | 19.6 |
| Info-VLA | 28.6 | 21.2 |
| AtomicVLA | 28.6 | 39.2 |
| **Ours** | **83.2** | **11.4** |

가장 강한 베이스라인 ER 대비 SR 13.0% 포인트 향상, FOR 8.2% 포인트 감소(표 내 수치로 계산). 작업 수준 성능이 두드러짐: 작업 5는 96%, 작업 9는 98%, 작업 10은 96%, 작업 9의 FOR는 0. 절제 실험: 잠재 리플레이는 메모리를 167.62 MiB/작업에서 95.70 MiB/작업으로 줄이고(동일한 49.99M 훈련 가능 파라미터), SR은 동등하며 FOR는 더 낮음; 이중 LoRA는 단일 LoRA 대비 SR을 높이고 FOR를 낮추며, 훈련 가능 파라미터는 99.97M으로 증가하지만 AtomicVLA의 226.49M 파라미터와 452.98 MiB/작업 메모리보다 훨씬 작음. 실제 로봇 xArm 5개 작업 스트림, 작업당 50개 훈련 에피소드, 모든 작업 학습 후 각 작업 성공률이 80% 이상.

## 경계와 한계

현재 평가는 작업 규모와 다양성에서 제한적이다. 실제 세계 평생 학습은 더 긴 작업 스트림, 더 다양한 객체 범주, 더 풍부한 장면 레이아웃, 장기 배포에서 수집된 비균일 데이터를 포함할 수 있다. 논문은 더 길고 이질적인 작업 시퀀스를 평가하지 않았고, 작업 순서를 무작위화하지 않았으며, 여러 스트림에 걸친 평균과 분산을 보고하지 않았다. 실험은 명확한 언어 지시를 사용했지만, 실제 사용자는 더 다양하고 모호하거나 대화형 명령(생략, 공지시, 맥락 의존)을 제공할 수 있으며, 논문은 의역, 대화형 및 맥락 관련 지시를 도입하여 언어 견고성을 평가하지 않았고, 언어 증강이나 지시 재작성을 통해 다양한 사용자 표현을 처리하는 모델 능력을 향상시키지 않았다. 테스트 시 작업 정체성은 사용할 수 없지만 작업 순서는 고정되어 있어 순서 민감성은 검증되지 않았다.

## 엔지니어링 시사점

재현 시 먼저 게이팅 컨텍스트의 stop-gradient 구현을 확인하라 — 이는 순환 의존성을 피하는 핵심이며, 제거하면 훈련이 불안정해진다. 이중 시간 척도 업데이트에서 `η_lg < η_sh` 비율은 신중한 튜닝이 필요하며, 논문은 구체적인 값을 명시하지 않았으므로 10:1에서 시작하는 것을 권장한다. 리플레이 캐시는 프리픽스 토큰과 컴팩트 감독만 저장하므로, 구현 시 프리픽스가 실제로 동결된 백본에서 나오고 그라디언트에 참여하지 않는지 확인해야 한다. 마스크된 신규-리플레이 목표에서 개별 정규화는 필수이며, 그렇지 않으면 상대적 배치 크기 차이가 이중 경로 균형을 깨뜨린다. 증류 손실에서 교사 스냅샷은 작업 전환 시 분리 저장해야 하며, stop-gradient 위치 오류는 그라디언트 누출을 초래한다. 실제 로봇 배포 시 작업당 50개 훈련 에피소드의 데이터 규모에 주의하고, 데이터가 더 적으면 `c_t` 할당량을 조정해야 할 수 있다. 가장 함정에 빠지기 쉬운 지점: 확산 변수 τ와 ϵ의 재샘플링 로직 — 원래 시간 단계와 노이즈를 그대로 사용하면 캐시된 프리픽스가 다양한 리플레이 인스턴스를 생성할 수 없어 무작위 리플레이의 핵심 이점을 잃게 된다.
