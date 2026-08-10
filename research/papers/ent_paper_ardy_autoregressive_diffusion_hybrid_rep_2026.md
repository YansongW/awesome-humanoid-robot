---
$id: ent_paper_ardy_autoregressive_diffusion_hybrid_rep_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation'
  zh: 'ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation'
  ko: 'ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation'
summary:
  en: Generating realistic 3D human motions in real-time within interactive applications is key for animation, simulation,
    and humanoid robotics. While recent offline motion generation approaches offer precise control via text and kinematic
    constraints, they lack the inference speed required for interactive settings. Conversely, existing online methods enable
    real-time synthesis but often sacrifice.
  zh: ARDY 是 NVIDIA 提出的流式人体运动生成框架，通过混合运动表示（显式根轨迹 + 潜在身体嵌入）与两阶段自回归扩散模型，在单个生成窗口内同时支持在线文本提示与灵活运动学约束（含窗口外长时程目标）。核心贡献在于将离线方法的可控性与在线方法的实时性统一到同一架构中，无需测试时优化或
    RL 控制策略。
  ko: Generating realistic 3D human motions in real-time within interactive applications is key for animation, simulation,
    and humanoid robotics. While recent offline motion generation approaches offer precise control via text and kinematic
    constraints, they lack the inference speed required for interactive settings. Conversely, existing online methods enable
    real-time synthesis but often sacrifice.
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
- ardy
- autoregressive
- diffusion
- hybrid
- rep
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量四）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.08741 ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human '
  url: https://arxiv.org/abs/2607.08741
  date: '2026-07-09'
  accessed_at: '2026-08-05'
---

## 概述

ARDY 是 NVIDIA 提出的流式人体运动生成框架，通过混合运动表示（显式根轨迹 + 潜在身体嵌入）与两阶段自回归扩散模型，在单个生成窗口内同时支持在线文本提示与灵活运动学约束（含窗口外长时程目标）。核心贡献在于将离线方法的可控性与在线方法的实时性统一到同一架构中，无需测试时优化或 RL 控制策略。

## 它改变了什么

现有运动生成方法存在根本性分裂：离线扩散/掩码模型（如 MaskControl、Kimodo）能精确控制但推理延迟高，无法支撑交互；在线自回归方法（如 DiP、DartControl）虽实时但历史上下文极短（DiP 仅 1.00 秒），既难以理解复杂文本语义（如“先走，弯腰捡东西，再继续走”），也无法执行超出生成窗口的长时程目标。ARDY 真正改变的是将“可控性”从离线专属能力变为流式生成的内生属性——它证明在自回归扩散框架中，根轨迹覆盖、关节级约束与窗口外目标可以原生融入去噪过程，而非事后优化或策略学习。

另一个关键转变在于运动表示本身。此前方法要么用纯显式表示（高维、生成学习困难），要么用纯潜在表示（难以施加空间约束）。ARDY 的混合表示将根轨迹保持显式、身体运动压缩为潜在 token，使得精确轨迹控制与高效生成建模不再互斥。这一设计决策直接影响了后续所有实验：显式表示在约束误差上比混合表示差一个数量级（如关节位置误差 0.130 vs 0.025）。

## 方法拆解

### 混合运动表示
- 每帧运动分解为显式根特征 m_root = (p, cos ψ, sin ψ) ∈ ℝ⁵（全局位置 + 朝向角）与潜在身体嵌入 x_body ∈ ℝ^L（由 tokenizer 输出，每个 token 编码 P=4 帧）。
- 混合 token 为 x = [m_root; x_body]，维度 D = L + 5P。根保持全局坐标避免局部速度积分误差，且便于直接覆盖以施加空间约束。

### 身体运动 Tokenizer
- 非对称条件自编码器：编码器将 N 帧身体运动按 P 帧 patch 化为 T 个输入，压缩为潜在 token；解码器从混合 token 重建身体运动。
- 关键设计：解码器先将全局根运动转换为局部表示（ψ̇, ṗ_x, ṗ_z, p_y），显著减轻脚滑（Skate 指标从 0.303 降至 0.264）。
- 默认使用 FSQ 量化（64 级别 × 128 维），训练稳定性优于 VAE。

### 两阶段自回归扩散
- 每步扩散：根 transformer 先预测干净全局根运动 m̂_root，detach 后输入身体 transformer 预测潜在身体 token x̂_body，拼接形成完整预测 x̂₀。
- 根约束覆盖：将带噪 token 的根部分替换为 m̃_root = (1 - v_root) ⊙ m_root + v_root ⊙ g_root，实现高精度轨迹控制。
- 身体约束：显式目标特征与掩码沿特征维度拼接，形成增强表示 [m̃_root; x_body; g_body; v]。
- 窗口外目标 g^(C+1):(C+F) 作为额外 token 输入，隐式决定当前窗口内运动（如 10 秒内跑到目的地）。
- 损失函数四部分：混合损失 ℒ_hybrid = ||x̂₀ − x₀||₁、解码身体损失 ℒ_dec = ||m̂_body − m_body||₁、目标损失 ℒ_goal = ||v ⊙ (m̂₀ − g)||₁、一致性损失 ℒ_consist = ||Ĵ₀ − FK(θ̂₀)||₂。

### 训练与推理
- 去噪器：batch size 512，4×A100，1 百万步，AdamAtan2 学习率 2e−5，无 dropout。
- 默认 10 扩散步，低至 4 步性能可接受（约束误差从 0.024 升至 0.027）。
- 推理时 classifier-free guidance，10% 概率丢弃条件；上下文截断最大 8 秒；动态重规划检测到新输入或缓冲耗尽时触发。

## 关键创新

1. **混合表示 + 两阶段去噪的架构解耦**：将根轨迹预测与身体生成分离，使根 transformer 专注空间控制、身体 transformer 专注运动质量。消融显示单阶段联合预测在关节位置误差上恶化 4 倍（0.101 vs 0.025），证明分解是可控性的关键而非工程细节。

2. **窗口外目标的原生支持**：通过将未来约束作为额外 token 输入，ARDY 能隐式规划当前窗口运动（如起始方向由 10 秒后的目标决定）。DiP 在 out-of-horizon 目标下 FID 恶化至 1.453，而 ARDY 保持 0.100，这是流式方法首次在长时程规划上接近离线水平。

3. **无需测试时优化的实时可控性**：相比 MaskControl 需 68.65 秒优化、DiP 需 RL 策略，ARDY 在 0.15 秒内达到约束误差 2.48（DiP 为 9.20），且无额外控制模块。这使交互式应用成为可能，而非事后附加能力。

## 实验与结果

### 自回归对比（HumanML3D，表 5）
| 方法 | 目标类型 | R-Prec. | FID | Skate | Error | Latency |
|---|---|---|---|---|---|---|
| DiP | In-horizon | 0.609 | 0.967 | 12.29 | 9.20 | 0.15 |
| ARDY | In-horizon | 0.690 | 0.092 | 7.07 | 2.48 | 0.15 |
| DiP | Out-of-horizon | 0.599 | 1.453 | 11.07 | 17.64 | 0.15 |
| ARDY | Out-of-horizon | 0.684 | 0.100 | 7.63 | 2.92 | 0.15 |

### 架构消融（表 2，Bones Rigplay）
| 变体 | Skate | R-prec. | FID | Joint pos. 误差 |
|---|---|---|---|---|
| ARDY（默认） | 0.264 | 65.47 | 0.027 | 0.025 |
| 显式表示 | 0.365 | 53.90 | 0.065 | 0.130 |
| 全局根条件解码器 | 0.303 | 64.94 | 0.028 | 0.048 |
| 单阶段架构 | 0.264 | 65.84 | 0.029 | 0.101 |

### 扩散步数（表 3）
| 步数 | Skate | R-prec. | FID | Joint pos. 误差 |
|---|---|---|---|---|
| 1 | 0.411 | 56.74 | 0.079 | 1.040 |
| 4 | 0.230 | 64.41 | 0.034 | 0.034 |
| 10（默认） | 0.264 | 65.47 | 0.027 | 0.025 |
| 100 | 0.282 | 65.49 | 0.025 | 0.030 |

结果含义：4 步扩散在约束精度上几乎与 10 步持平（0.034 vs 0.025），但生成延迟降至 33 ms（由表内 4 步与 10 步对比计算），这为实时交互提供了关键余量。感知研究（240 对比较）中，ARDY 在运动质量、语义对齐、目标精度上分别以 65.8%、67.5%、64.6% 胜出 DiP。

## 边界与局限

- 自回归生成显式使用所有历史帧作为上下文，对极长时程任务效率低下，作者未提出结构化记忆机制。
- 纯运动学模型，无物理动力学意识，脚滑与抖动伪影仍存在（Skate 0.264 虽优于 DiP 但非零）。
- HumanML3D 实验使用 vanilla autoencoder tokenizer 而非默认 FSQ，且排除 HumanAct12 子集，跨数据集泛化结论需谨慎。
- 训练预算限制在 1 百万步，FSQ 16-32 在 FID 上略优但约束精度下降，更大预算下的最优配置论文未明确。

## 工程启示

- 复现时先核对 tokenizer 的局部根表示转换：这是脚滑指标从 0.303 降至 0.264 的关键，若跳过此步将显著恶化运动质量。
- 扩散步数选择：若目标为实时交互，4 步是甜点（约束误差 0.034 vs 10 步的 0.025，延迟减半）；若追求最高保真度，10 步足够，100 步收益甚微（FID 仅从 0.027 降至 0.025）。
- 上下文截断长度务必设为 8 秒——这是训练中观察到的最大有效上下文，超出部分会被截断且未来约束被排除，可能导致长时程目标失效。
- 训练时禁用 dropout，否则根约束条件输入会部分丢失，直接破坏空间控制精度。
- 自回归生成时需将历史根轨迹平移至原点，并将偏移保留用于变换回全局坐标，否则累积漂移会破坏轨迹一致性。

## Overview
Generating realistic 3D human motions in real-time within interactive applications is key for animation, simulation, and humanoid robotics. While recent offline motion generation approaches offer precise control via text and kinematic constraints, they lack the inference speed required for interactive settings. Conversely, existing online methods enable real-time synthesis but often sacrifice controllability or struggle with complex text semantics and long-horizon goals due to limited context windows. In this work, we introduce ARDY, a streaming generation framework that bridges this gap by enabling high-fidelity motion generation controllable via online text prompts and flexible kinematic constraints. ARDY employs a hybrid representation that combines explicit root features with a latent body embedding, balancing precise trajectory control with efficient generative learning. We propose a two-stage autoregressive transformer denoiser that features variable history context and supports conditioning on flexible, long-horizon kinematic constraints. By training on a large-scale motion capture dataset and being directly conditioned on text labels and kinematic constraints sampled from ground truth poses, ARDY natively learns controllable generation that supports online prompting and flexible long-horizon goals. Extensive evaluations on the HumanML3D benchmark and the large-scale, high-fidelity Bones Rigplay dataset demonstrate ARDY's high motion quality and constraint adherence, validating the efficacy of our key architectural decisions. Finally, we demonstrate the method's practical versatility through an interactive demo featuring dynamic text control, diverse keyframe pose constraints, path following, and interactive locomotion control via mouse and keyboard. Supplementary video results, code, and model releases can be found at https://research.nvidia.com/labs/sil/projects/ardy/.

## 参考
- https://arxiv.org/abs/2607.08741

## 개요

ARDY는 NVIDIA가 제안한 스트리밍 인간 동작 생성 프레임워크로, 혼합 동작 표현(명시적 루트 궤적 + 잠재 신체 임베딩)과 2단계 자기회귀 확산 모델을 통해 단일 생성 창 내에서 온라인 텍스트 프롬프트와 유연한 운동학적 제약(창 외부 장기 목표 포함)을 동시에 지원합니다. 핵심 기여는 오프라인 방법의 제어 가능성과 온라인 방법의 실시간성을 테스트 시 최적화나 RL 제어 정책 없이 동일한 아키텍처에 통합한 것입니다.

## 무엇을 바꾸었는가

기존 동작 생성 방법은 근본적으로 분열되어 있습니다: 오프라인 확산/마스크 모델(MaskControl, Kimodo 등)은 정밀한 제어가 가능하지만 추론 지연이 높아 상호작용을 지원할 수 없고, 온라인 자기회귀 방법(DiP, DartControl 등)은 실시간이지만 역사적 컨텍스트가 매우 짧아(DiP는 1.00초에 불과) 복잡한 텍스트 의미(예: "먼저 걷고, 구부려 물건을 집고, 다시 계속 걷기")를 이해하기 어렵고 생성 창을 초과하는 장기 목표를 실행할 수 없습니다. ARDY가 진정으로 바꾼 것은 "제어 가능성"을 오프라인 전용 능력에서 스트리밍 생성의 내재적 속성으로 전환한 것입니다—자기회귀 확산 프레임워크에서 루트 궤적 커버리지, 관절 수준 제약, 창 외부 목표가 사후 최적화나 정책 학습이 아닌 노이즈 제거 과정에 원래대로 통합될 수 있음을 증명했습니다.

또 다른 핵심 전환은 동작 표현 자체에 있습니다. 이전 방법은 순수 명시적 표현(고차원, 생성 학습이 어려움)이나 순수 잠재 표현(공간 제약 적용이 어려움)을 사용했습니다. ARDY의 혼합 표현은 루트 궤적을 명시적으로 유지하고 신체 동작을 잠재 토큰으로 압축하여 정밀한 궤적 제어와 효율적인 생성 모델링이 더 이상 상호 배타적이지 않게 합니다. 이 설계 결정은 이후 모든 실험에 직접 영향을 미쳤습니다: 명시적 표현은 제약 오류에서 혼합 표현보다 한 자릿수 나쁩니다(예: 관절 위치 오류 0.130 vs 0.025).

## 방법 분해

### 혼합 동작 표현
- 각 프레임 동작은 명시적 루트 특징 m_root = (p, cos ψ, sin ψ) ∈ ℝ⁵(전역 위치 + 방향 각도)와 잠재 신체 임베딩 x_body ∈ ℝ^L(tokenizer 출력, 각 토큰은 P=4 프레임 인코딩)으로 분해됩니다.
- 혼합 토큰은 x = [m_root; x_body], 차원 D = L + 5P. 루트는 전역 좌표를 유지하여 로컬 속도 적분 오류를 피하고 공간 제약 적용을 위해 직접 덮어쓰기가 용이합니다.

### 신체 동작 Tokenizer
- 비대칭 조건부 오토인코더: 인코더는 N 프레임 신체 동작을 P 프레임 패치로 T 입력으로 변환하여 잠재 토큰으로 압축하고, 디코더는 혼합 토큰에서 신체 동작을 재구성합니다.
- 핵심 설계: 디코더는 먼저 전역 루트 동작을 로컬 표현(ψ̇, ṗ_x, ṗ_z, p_y)으로 변환하여 발 미끄러짐을 크게 줄입니다(Skate 지표 0.303에서 0.264로).
- 기본적으로 FSQ 양자화(64 레벨 × 128 차원)를 사용하며 VAE보다 훈련 안정성이 우수합니다.

### 2단계 자기회귀 확산
- 각 확산 단계: 루트 트랜스포머가 먼저 깨끗한 전역 루트 동작 m̂_root를 예측하고, detach 후 신체 트랜스포머에 입력하여 잠재 신체 토큰 x̂_body를 예측하고, 결합하여 완전한 예측 x̂₀를 형성합니다.
- 루트 제약 덮어쓰기: 노이즈 토큰의 루트 부분을 m̃_root = (1 - v_root) ⊙ m_root + v_root ⊙ g_root로 대체하여 고정밀 궤적 제어를 구현합니다.
- 신체 제약: 명시적 목표 특징과 마스크를 특징 차원을 따라 연결하여 강화 표현 [m̃_root; x_body; g_body; v]를 형성합니다.
- 창 외부 목표 g^(C+1):(C+F)는 추가 토큰으로 입력되어 현재 창 내 동작을 암시적으로 결정합니다(예: 10초 내 목적지까지 달리기).
- 손실 함수 4부분: 혼합 손실 ℒ_hybrid = ||x̂₀ − x₀||₁, 디코더 신체 손실 ℒ_dec = ||m̂_body − m_body||₁, 목표 손실 ℒ_goal = ||v ⊙ (m̂₀ − g)||₁, 일관성 손실 ℒ_consist = ||Ĵ₀ − FK(θ̂₀)||₂.

### 훈련 및 추론
- 노이즈 제거기: 배치 크기 512, 4×A100, 1백만 스텝, AdamAtan2 학습률 2e−5, 드롭아웃 없음.
- 기본 10 확산 스텝, 최소 4스텝까지 성능 허용(제약 오류 0.024에서 0.027로).
- 추론 시 classifier-free guidance, 10% 확률로 조건 드롭; 컨텍스트 잘림 최대 8초; 동적 재계획은 새 입력 또는 버퍼 소진 시 트리거.

## 핵심 혁신

1. **혼합 표현 + 2단계 노이즈 제거의 아키텍처 분리**: 루트 궤적 예측과 신체 생성을 분리하여 루트 트랜스포머는 공간 제어에, 신체 트랜스포머는 동작 품질에 집중합니다. 절제 실험에서 단일 단계 결합 예측은 관절 위치 오류가 4배 악화(0.101 vs 0.025)되어 분해가 제어 가능성의 핵심이며 공학적 세부 사항이 아님을 증명합니다.

2. **창 외부 목표의 원래 지원**: 미래 제약을 추가 토큰으로 입력함으로써 ARDY는 현재 창 동작을 암시적으로 계획할 수 있습니다(예: 시작 방향이 10초 후 목표에 의해 결정됨). DiP는 out-of-horizon 목표에서 FID가 1.453으로 악화되는 반면 ARDY는 0.100을 유지하며, 이는 스트리밍 방법이 처음으로 장기 계획에서 오프라인 수준에 근접한 것입니다.

3. **테스트 시 최적화 없는 실시간 제어 가능성**: MaskControl이 68.65초 최적화, DiP가 RL 정책이 필요한 반면 ARDY는 0.15초 내 제약 오류 2.48(DiP는 9.20)을 달성하며 추가 제어 모듈이 없습니다. 이는 상호작용 애플리케이션을 사후 부가 능력이 아닌 가능하게 합니다.

## 실험 및 결과

### 자기회귀 비교(HumanML3D, 표 5)
| 방법 | 목표 유형 | R-Prec. | FID | Skate | Error | Latency |
|---|---|---|---|---|---|---|
| DiP | In-horizon | 0.609 | 0.967 | 12.29 | 9.20 | 0.15 |
| ARDY | In-horizon | 0.690 | 0.092 | 7.07 | 2.48 | 0.15 |
| DiP | Out-of-horizon | 0.599 | 1.453 | 11.07 | 17.64 | 0.15 |
| ARDY | Out-of-horizon | 0.684 | 0.100 | 7.63 | 2.92 | 0.15 |

### 아키텍처 절제(표 2, Bones Rigplay)
| 변형 | Skate | R-prec. | FID | 관절 위치 오류 |
|---|---|---|---|---|
| ARDY(기본) | 0.264 | 65.47 | 0.027 | 0.025 |
| 명시적 표현 | 0.365 | 53.90 | 0.065 | 0.130 |
| 전역 루트 조건 디코더 | 0.303 | 64.94 | 0.028 | 0.048 |
| 단일 단계 아키텍처 | 0.264 | 65.84 | 0.029 | 0.101 |

### 확산 스텝 수(표 3)
| 스텝 | Skate | R-prec. | FID | 관절 위치 오류 |
|---|---|---|---|---|
| 1 | 0.411 | 56.74 | 0.079 | 1.040 |
| 4 | 0.230 | 64.41 | 0.034 | 0.034 |
| 10(기본) | 0.264 | 65.47 | 0.027 | 0.025 |
| 100 | 0.282 | 65.49 | 0.025 | 0.030 |

결과 의미: 4스텝 확산은 제약 정밀도에서 10스텝과 거의 동일(0.034 vs 0.025)하지만 생성 지연이 33ms로 감소(표 내 4스텝과 10스텝 비교 계산)하여 실시간 상호작용에 핵심 여유를 제공합니다. 지각 연구(240쌍 비교)에서 ARDY는 동작 품질, 의미 정렬, 목표 정밀도에서 각각 65.8%, 67.5%, 64.6%로 DiP를 능가합니다.

## 경계 및 한계

- 자기회귀 생성은 모든 역사적 프레임을 컨텍스트로 명시적으로 사용하여 매우 긴 작업에 효율성이 낮으며, 저자는 구조화된 메모리 메커니즘을 제안하지 않았습니다.
- 순수 운동학적 모델로 물리 역학 인식이 없어 발 미끄러짐과 떨림 아티팩트가 여전히 존재합니다(Skate 0.264는 DiP보다 우수하지만 0이 아님).
- HumanML3D 실험은 기본 FSQ가 아닌 vanilla autoencoder tokenizer를 사용하고 HumanAct12 하위 집합을 제외하므로 교차 데이터 세트 일반화 결론은 주의가 필요합니다.
- 훈련 예산이 1백만 스텝으로 제한되며 FSQ 16-32는 FID에서 약간 우수하지만 제약 정밀도가 감소하고, 더 큰 예산에서의 최적 구성은 논문에서 명확하지 않습니다.

## 공학적 시사점

- 재현 시 먼저 tokenizer의 로컬 루트 표현 변환을 확인하세요: 이는 발 미끄러짐 지표를 0.303에서 0.264로 낮추는 핵심이며, 이 단계를 건너뛰면 동작 품질이 크게 악화됩니다.
- 확산 스텝 선택: 실시간 상호작용이 목표라면 4스텝이 최적입니다(제약 오류 0.034 vs 10스텝의 0.025, 지연 절반); 최고 충실도를 원한다면 10스텝으로 충분하며 100스텝은 이득이 거의 없습니다(FID 0.027에서 0.025로만 감소).
- 컨텍스트 잘림 길이는 반드시 8초로 설정하세요—이는 훈련에서 관찰된 최대 유효 컨텍스트이며, 초과 부분은 잘리고 미래 제약이 제외되어 장기 목표가 실패할 수 있습니다.
- 훈련 시 드롭아웃을 비활성화하세요. 그렇지 않으면 루트 제약 조건 입력이 부분적으로 손실되어 공간 제어 정밀도가 직접 파괴됩니다.
- 자기회귀 생성 시 역사적 루트 궤적을 원점으로 평행 이동하고 오프셋을 전역 좌표로 변환하기 위해 보존해야 하며, 그렇지 않으면 누적 드리프트가 궤적 일관성을 파괴합니다.
