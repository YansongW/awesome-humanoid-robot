---
$id: ent_paper_universal_humanoid_motion_representation_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Universal Humanoid Motion Representations for Physics-Based Control
  zh: Universal Humanoid Motion Representations for Physics-Based Control
  ko: Universal Humanoid Motion Representations for Physics-Based Control
summary:
  en: We present a universal motion representation that encompasses a comprehensive range of motor skills for physics-based
    humanoid control. Due to the high dimensionality of humanoids and the inherent difficulties in reinforcement learning,
    prior methods have focused on learning skill embeddings for a narrow range of movement styles (e.g. locomotion, game characters)
    from specialized motion datasets..
  zh: PULSE 提出一种基于物理的人形全身运动通用表示：先用 PHC+ 模仿器覆盖 40 小时 AMASS 数据，再通过条件变分信息瓶颈蒸馏出 32 维潜在动作空间，供下游生成与跟踪任务直接复用。核心贡献在于用在线蒸馏替代对抗学习，使大规模非结构化
    MoCap 数据成为可扩展的运动先验。
  ko: We present a universal motion representation that encompasses a comprehensive range of motor skills for physics-based
    humanoid control. Due to the high dimensionality of humanoids and the inherent difficulties in reinforcement learning,
    prior methods have focused on learning skill embeddings for a narrow range of movement styles (e.g. locomotion, game characters)
    from specialized motion datasets..
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
- universal
- humanoid
- motion
- representation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P027. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: arXiv:2310.04582 Universal Humanoid Motion Representations for Physics-Based Control
  url: https://arxiv.org/abs/2310.04582
  date: '2023-10-06'
  accessed_at: '2026-08-05'
---

## 概述

PULSE 提出一种基于物理的人形全身运动通用表示：先用 PHC+ 模仿器覆盖 40 小时 AMASS 数据，再通过条件变分信息瓶颈蒸馏出 32 维潜在动作空间，供下游生成与跟踪任务直接复用。核心贡献在于用在线蒸馏替代对抗学习，使大规模非结构化 MoCap 数据成为可扩展的运动先验。

## 它改变了什么

现有物理人形运动表示（ASE、CALM）依赖判别器或对抗目标，只能在专门数据集（locomotion、boxing、dancing）上形成狭窄潜在空间，无法覆盖多样技能；而运动学潜在空间（HuMoR）随机采样易产生不合理运动。PULSE 真正改变的是：把“模仿器 + 蒸馏”从专用 pipeline 提升为通用基础设施——下游任务（速度、打击、地形穿越、VR 跟踪）无需重新设计表示，直接以冻结解码器为动作空间即可训练。

更关键的是，作者放弃对抗奖励，仅靠预学习先验采样产生类人运动。这验证了一个假设：物理约束下，类人技能比非自然运动更容易被采样到，从而简化了任务设计（如 VR 跟踪无需 PACER 的额外对抗项）。

## 方法拆解

### 两阶段训练
1. **PHC+ 模仿器**：基于 PHC（Luo et al., 2023），采用渐进式训练——先训练原始策略 𝓟(0) 覆盖全数据集，失败序列构成硬负样本集，再训练 𝓟(1) 学习这些样本，直至无运动可学；额外训练恢复策略 𝓟(F) 处理跌倒，组合器 𝓒 动态切换冻结策略。关键修改：移除严重穿透/不连续序列；实例化新策略前先让旧策略专注自身硬负样本；激活从 ReLU 改 SiLU 并扩大网络（6 层 MLP，单元 [2048, 1536, 1024, 1024, 512, 512]），仅用三个原始策略达到 100% 成功率。

2. **在线蒸馏**：编码器 𝓔(𝒛_t | 𝒔_t^p, 𝒔_t^g-mimic) 与解码器 𝓓(𝒂_t | 𝒔_t^p, 𝒛_t) 建模动作分布，目标函数为 ELBO：
   log P(𝒂_t | ·) ≥ E_𝓔[log 𝓓(𝒂_t | 𝒔_t^p, 𝒛_t)] - D_KL(𝓔 || 𝓡)
   其中先验 𝓡(𝒛_t | 𝒔_t^p) 为学习到的条件高斯（非零均值），理由：站立与空中翻转的动作分布差异显著。损失 ℒ = ℒ_action + αℒ_regu + βℒ_KL，ℒ_regu = ‖𝝁_t^e - 𝝁_{t-1}^e‖²₂ 惩罚连续潜码偏差（类似 NPMP 的 AR(1) 先验），β 从 0.01 退火至 0.001（2.5×10⁹ 至 5×10⁹ 样本）。

### 下游使用
冻结 𝓓 与 𝓡，高层策略 π_task 输出相对先验均值 𝝁_t^p 的残差动作：𝒂_t^task = 𝓓(π_task(𝒛_t | 𝒔_t^p, 𝒔_t^g) + 𝝁_t^p)。RL 探索用固定方差 0.22（而非 𝝈_t^p，因其偏小），且不监督 π_task 分布用先验，避免坏潜码导致状态恶化形成反馈循环。

## 关键创新

1. **在线蒸馏替代对抗学习**：直接查询 π_PHC+ 获得 (𝒔_t^p, 𝒔_t^g-mimic, 𝒂_t, 𝒂_t^PHC+) 对训练潜空间，无需判别器。消融显示无蒸馏时训练 1×10¹⁰ 样本仍不收敛（Train Succ 72.0% vs 有蒸馏 99.8%），证明蒸馏对大规模数据可扩展性至关重要。

2. **条件先验 + 残差动作**：学习先验 𝓡(𝒛_t | 𝒔_t^p) 而非零均值高斯，适应不同姿态的动作分布差异；残差动作（式 4）对探索至关重要——消融 R5 vs R6 显示无残差时 Succ 从 93.4% 暴跌至 18.1%。

3. **ℒ_regu 平滑正则**：惩罚连续潜码偏差，提供更紧凑连续的潜在空间。消融 R1 vs R2 显示加入后 Succ 从 36.9% 升至 45.6%，且 E_g-mpjpe 下降。

## 实验与结果

**运动模仿（AMASS）**：PHC+ 达到 100% Train Succ，PULSE 略降至 99.8%，但 Test Succ 97.1% 与 PHC 持平，E_g-mpjpe 54.1mm 略高于 PHC+ 的 36.1mm（信息瓶颈的有损代价）。

**VR 控制器跟踪**：PULSE 在真实世界 14/14 序列成功，与从零训练（Scratch）持平，远超 ASE-30Hz（7/14）、CALM-30Hz（2/14）。但 E_g-mhpe 68.4mm 高于 Scratch 的 43.3mm，说明通用先验仍不如任务专用策略精确。

| 方法 | Train Succ | Test Succ | Real Succ | E_g-mhpe (mm) |
|---|---|---|---|---|
| ASE-30Hz | 79.8% | 37.6% | 7/14 | 99.0 |
| CALM-30Hz | 16.6% | 10.1% | 2/14 | 206.9 |
| Scratch | 98.8% | 93.4% | 14/14 | 43.3 |
| Ours | 99.5% | 93.4% | 14/14 | 68.4 |

**消融（VR 跟踪）**：完整模型（R6）Succ 93.4%；去掉 ℒ_regu（R3）降至 60.8%；去掉残差动作（R5）仅 18.1%；去掉 RL 仅监督（R4）71.0%——证明混合 RL 与在线监督蒸馏有负面效果（R4 vs R6）。

## 边界与局限

- π_PULSE 未达 100% 模仿成功率，信息瓶颈是有损压缩；无变分瓶颈的在线蒸馏可达 100%。
- 变分公式引入额外优化挑战（β 退火调度敏感）。
- VR 跟踪等任务性能仍落后于从零训练（E_g-mhpe 68.4 vs 43.3mm）。
- 人形可能卡在跌倒或站立状态，增加系统噪声可缓解但未完全解决。
- 未考虑形状变化、人-人交互、物体操作及关节手指（论文未明确）。

## 工程启示

- **复现先核对数据清洗**：移除穿透/不连续序列是 PHC+ 达 100% 的前提；AMASS 过滤后 11313 训练 / 138 测试序列。
- **蒸馏是成败关键**：无蒸馏训练 1×10¹⁰ 样本仍不收敛，务必实现在线查询 π_PHC+ 的 pipeline。
- **β 退火需精细调度**：从 0.01 退火至 0.001（2.5×10⁹ 至 5×10⁹ 样本），过早退火会牺牲重建精度，过晚则 KL 项失控。
- **残差动作不可省**：下游策略输出相对先验均值的残差，否则探索效率崩溃（Succ 18.1% vs 93.4%）。
- **RL 探索方差固定 0.22**：用 𝝈_t^p 会因方差过小导致探索不足。
- **最易踩坑**：混合 RL 与在线监督蒸馏会污染潜空间（R4 vs R6），务必分离两阶段训练。

## Overview
We present a universal motion representation that encompasses a comprehensive range of motor skills for physics-based humanoid control. Due to the high dimensionality of humanoids and the inherent difficulties in reinforcement learning, prior methods have focused on learning skill embeddings for a narrow range of movement styles (e.g. locomotion, game characters) from specialized motion datasets. This limited scope hampers their applicability in complex tasks. We close this gap by significantly increasing the coverage of our motion representation space. To achieve this, we first learn a motion imitator that can imitate all of human motion from a large, unstructured motion dataset. We then create our motion representation by distilling skills directly from the imitator. This is achieved by using an encoder-decoder structure with a variational information bottleneck. Additionally, we jointly learn a prior conditioned on proprioception (humanoid's own pose and velocities) to improve model expressiveness and sampling efficiency for downstream tasks. By sampling from the prior, we can generate long, stable, and diverse human motions. Using this latent space for hierarchical RL, we show that our policies solve tasks using human-like behavior. We demonstrate the effectiveness of our motion representation by solving generative tasks (e.g. strike, terrain traversal) and motion tracking using VR controllers.

## 参考
- https://arxiv.org/abs/2310.04582

## 개요

PULSE는 물리 기반 휴머노이드 전신 운동의 범용 표현을 제안한다. 먼저 PHC+ 모방기로 40시간 분량의 AMASS 데이터를 커버한 뒤, 조건부 변분 정보 병목을 통해 32차원 잠재 동작 공간을 증류하여 하위 생성 및 추적 작업에 직접 재사용할 수 있게 한다. 핵심 기여는 적대적 학습을 온라인 증류로 대체하여 대규모 비정형 MoCap 데이터를 확장 가능한 운동 사전 지식으로 만든 것이다.

## 무엇을 바꾸었는가

기존 물리 휴머노이드 운동 표현(ASE, CALM)은 판별기나 적대적 목표에 의존하여 특수 데이터셋(보행, 복싱, 춤)에서만 좁은 잠재 공간을 형성하고 다양한 기술을 포괄하지 못한다. 반면 운동학적 잠재 공간(HuMoR)은 무작위 샘플링 시 부자연스러운 운동을 생성하기 쉽다. PULSE가 실제로 바꾼 것은 "모방기 + 증류"를 전용 파이프라인에서 범용 인프라로 승격시킨 점이다. 하위 작업(속도, 타격, 지형 횡단, VR 추적)은 표현을 재설계할 필요 없이 동결된 디코더를 동작 공간으로 바로 사용하여 훈련할 수 있다.

더 중요하게, 저자들은 적대적 보상을 포기하고 사전 학습된 사전 지식 샘플링만으로 인간형 운동을 생성한다. 이는 물리적 제약 하에서 비자연적 운동보다 인간형 기술이 샘플링되기 더 쉽다는 가설을 검증하며, 이로써 작업 설계가 단순화된다(예: VR 추적에 PACER의 추가 적대 항이 필요 없음).

## 방법 분해

### 2단계 훈련
1. **PHC+ 모방기**: PHC(Luo et al., 2023) 기반, 점진적 훈련 사용 — 먼저 원시 정책 𝓟(0)을 훈련하여 전체 데이터셋을 커버하고, 실패 시퀀스는 하드 네거티브 샘플 세트를 구성하며, 이후 𝓟(1)을 훈련하여 이러한 샘플을 학습하고 더 이상 배울 운동이 없을 때까지 반복한다. 추가로 낙상을 처리하기 위한 복구 정책 𝓟(F)을 훈련하고, 컴바이너 𝓒가 동결 정책을 동적으로 전환한다. 핵심 수정 사항: 심각한 관통/불연속 시퀀스 제거, 새 정책을 인스턴스화하기 전에 이전 정책이 자체 하드 네거티브에 집중하도록 함, 활성화 함수를 ReLU에서 SiLU로 변경하고 네트워크 확장(6층 MLP, 유닛 [2048, 1536, 1024, 1024, 512, 512]), 세 개의 원시 정책만으로 100% 성공률 달성.

2. **온라인 증류**: 인코더 𝓔(𝒛_t | 𝒔_t^p, 𝒔_t^g-mimic)와 디코더 𝓓(𝒂_t | 𝒔_t^p, 𝒛_t)가 동작 분포를 모델링하며, 목표 함수는 ELBO:
   log P(𝒂_t | ·) ≥ E_𝓔[log 𝓓(𝒂_t | 𝒔_t^p, 𝒛_t)] - D_KL(𝓔 || 𝓡)
   여기서 사전 𝓡(𝒛_t | 𝒔_t^p)는 학습된 조건부 가우시안(비영평균)이다. 이유: 서 있는 상태와 공중 뒤집기의 동작 분포는 크게 다르다. 손실 ℒ = ℒ_action + αℒ_regu + βℒ_KL, ℒ_regu = ‖𝝁_t^e - 𝝁_{t-1}^e‖²₂는 연속 잠재 코드 편차를 페널티한다(NPMP의 AR(1) 사전과 유사), β는 0.01에서 0.001로 어닐링(2.5×10⁹ ~ 5×10⁹ 샘플).

### 하위 사용
𝓓와 𝓡을 동결하고, 상위 정책 π_task는 사전 평균 𝝁_t^p에 대한 잔차 동작을 출력한다: 𝒂_t^task = 𝓓(π_task(𝒛_t | 𝒔_t^p, 𝒔_t^g) + 𝝁_t^p). RL 탐색은 고정 분산 0.22를 사용하며(𝝈_t^p는 너무 작아서), π_task 분포를 사전으로 감독하지 않아 나쁜 잠재 코드로 인한 상태 악화 피드백 루프를 방지한다.

## 핵심 혁신

1. **온라인 증류로 적대적 학습 대체**: π_PHC+를 직접 쿼리하여 (𝒔_t^p, 𝒔_t^g-mimic, 𝒂_t, 𝒂_t^PHC+) 쌍을 얻어 잠재 공간을 훈련하며 판별기가 필요 없다. 소거 실험에서 증류 없이는 1×10¹⁰ 샘플 훈련에도 수렴하지 않았고(Train Succ 72.0% vs 증류 포함 99.8%), 이는 증류가 대규모 데이터 확장성에 필수적임을 증명한다.

2. **조건부 사전 + 잔차 동작**: 영평균 가우시안 대신 학습된 사전 𝓡(𝒛_t | 𝒔_t^p)을 사용하여 다양한 자세의 동작 분포 차이에 적응한다. 잔차 동작(식 4)은 탐색에 필수적이다 — 소거 R5 vs R6에서 잔차 없이 Succ가 93.4%에서 18.1%로 급락.

3. **ℒ_regu 평활 정규화**: 연속 잠재 코드 편차를 페널티하여 더 컴팩트하고 연속적인 잠재 공간을 제공한다. 소거 R1 vs R2에서 추가 시 Succ가 36.9%에서 45.6%로 상승하고 E_g-mpjpe가 감소.

## 실험 및 결과

**운동 모방(AMASS)**: PHC+는 100% Train Succ에 도달, PULSE는 99.8%로 약간 감소하지만 Test Succ 97.1%로 PHC와 동등, E_g-mpjpe 54.1mm는 PHC+의 36.1mm보다 약간 높음(정보 병목의 손실 비용).

**VR 컨트롤러 추적**: PULSE는 실제 세계 14/14 시퀀스에서 성공, 처음부터 훈련(Scratch)과 동등하며 ASE-30Hz(7/14), CALM-30Hz(2/14)를 크게 능가. 그러나 E_g-mhpe 68.4mm는 Scratch의 43.3mm보다 높아 범용 사전이 여전히 작업 전용 정책보다 정확도가 낮음을 시사.

| 방법 | Train Succ | Test Succ | Real Succ | E_g-mhpe (mm) |
|---|---|---|---|---|
| ASE-30Hz | 79.8% | 37.6% | 7/14 | 99.0 |
| CALM-30Hz | 16.6% | 10.1% | 2/14 | 206.9 |
| Scratch | 98.8% | 93.4% | 14/14 | 43.3 |
| Ours | 99.5% | 93.4% | 14/14 | 68.4 |

**소거(VR 추적)**: 전체 모델(R6) Succ 93.4%; ℒ_regu 제거(R3) 시 60.8%로 하락; 잔차 동작 제거(R5) 시 18.1%에 불과; RL 전용 감독 제거(R4) 시 71.0% — RL과 온라인 감독 증류의 혼합이 부정적 효과를 가짐을 증명(R4 vs R6).

## 경계 및 한계

- π_PULSE는 100% 모방 성공률에 도달하지 못함, 정보 병목은 손실 압축; 변분 병목 없는 온라인 증류는 100% 도달 가능.
- 변분 공식은 추가 최적화 과제 도입(β 어닐링 스케줄에 민감).
- VR 추적 등 작업 성능은 여전히 처음부터 훈련보다 뒤처짐(E_g-mhpe 68.4 vs 43.3mm).
- 휴머노이드가 낙상 또는 기립 상태에 갇힐 수 있으며, 시스템 노이즈 증가로 완화 가능하지만 완전히 해결되지는 않음.
- 형상 변화, 사람-사람 상호작용, 물체 조작 및 관절 손가락은 고려하지 않음(논문에 명시되지 않음).

## 엔지니어링 시사점

- **재현 시 데이터 정제 먼저 확인**: 관통/불연속 시퀀스 제거는 PHC+가 100%에 도달하기 위한 전제 조건; AMASS 필터링 후 11313 훈련 / 138 테스트 시퀀스.
- **증류가 성패를 좌우**: 증류 없이는 1×10¹⁰ 샘플 훈련에도 수렴하지 않으므로 π_PHC+를 온라인으로 쿼리하는 파이프라인을 반드시 구현.
- **β 어닐링 세밀한 스케줄 필요**: 0.01에서 0.001로 어닐링(2.5×10⁹ ~ 5×10⁹ 샘플), 너무 이른 어닐링은 재구성 정밀도를 희생하고 너무 늦으면 KL 항이 통제 불능.
- **잔차 동작 생략 불가**: 하위 정책은 사전 평균에 대한 잔차를 출력해야 하며, 그렇지 않으면 탐색 효율이 붕괴(Succ 18.1% vs 93.4%).
- **RL 탐색 분산 고정 0.22**: 𝝈_t^p를 사용하면 분산이 너무 작아 탐색 부족 발생.
- **가장 흔한 함정**: RL과 온라인 감독 증류를 혼합하면 잠재 공간이 오염됨(R4 vs R6), 반드시 두 단계 훈련을 분리.
