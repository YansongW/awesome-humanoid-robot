---
$id: ent_paper_wcm_world_critic_model_vision_language_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning'
  zh: 'WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning'
  ko: 'WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning'
summary:
  en: Reinforcement learning (RL) post-training of Vision-Language-Action (VLA) models has shown strong promise for robotic
    manipulation. Among RL methods, critic-based approaches rely on a value estimator that predominantly operates on single-frame
    observations or single-frame VLM backbone latents, which is a fundamental mismatch with the partially observable nature
    of robot control. A naive approach.
  zh: WCM（World Critic Model）是一种面向视觉-语言-动作（VLA）强化学习的评论家模型，由作者提出，旨在解决现有评论家基于单帧观测导致的部分可观测性（POMDP）不匹配问题。其核心贡献是引入轻量级 LeJEPA 架构，联合预测未来潜在状态与估计价值，使评论家表示显式捕捉时间动态，从而显著提升仿真与真实世界的任务成功率与分布外（OOD）泛化能力。
  ko: Reinforcement learning (RL) post-training of Vision-Language-Action (VLA) models has shown strong promise for robotic
    manipulation. Among RL methods, critic-based approaches rely on a value estimator that predominantly operates on single-frame
    observations or single-frame VLM backbone latents, which is a fundamental mismatch with the partially observable nature
    of robot control. A naive approach.
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
- wcm
- world
- critic
- model
- vision
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
  title: 'arXiv:2607.29613 WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning'
  url: https://arxiv.org/abs/2607.29613
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

WCM（World Critic Model）是一种面向视觉-语言-动作（VLA）强化学习的评论家模型，由作者提出，旨在解决现有评论家基于单帧观测导致的部分可观测性（POMDP）不匹配问题。其核心贡献是引入轻量级 LeJEPA 架构，联合预测未来潜在状态与估计价值，使评论家表示显式捕捉时间动态，从而显著提升仿真与真实世界的任务成功率与分布外（OOD）泛化能力。

## 它改变了什么

现有 VLA-RL 方法的价值估计器大多基于单帧观测或单帧 VLM 骨干潜在表示，这与机器人控制固有的部分可观测性（POMDP）本质相悖。简单地将观测历史拼接进评论家输入，会遭遇高维视觉空间下的指数级复杂度，且纯标量回报回归提供的监督信号过于稀疏，不足以引导评论家学习跨时间步的动态结构。根本问题在于状态近似：缺乏显式世界建模目标时，评论家的潜在表示无法编码价值估计所需的时序信息，导致其在真实世界动态任务（如变形物体操作）中产生错误的价值判断，甚至驱动机械臂撞向桌面。

WCM 真正改变的是评论家的学习目标与表示空间。它不再将评论家视为一个单纯的标量回报回归器，而是将其训练为一个联合的世界模型与价值估计器。通过显式预测未来潜在状态，评论家的表示被强制编码时间动态结构，从而在价值估计时能利用历史上下文区分“正在接近成功”与“即将发生碰撞”等物理状态。这一转变直接回应了单帧 critic 在真实世界任务中因缺乏历史信息而导致的失败模式，将评论家的角色从“回报预测器”升级为“状态动力学理解器”。

## 方法拆解

WCM 基于轻量级 LeJEPA 架构，由四个核心组件构成：观测编码器、世界预测器、价值解码头与动作条件潜在动态分支。其处理流程如下：

### 观测编码与指令注入
- 给定时间步 t-K+1 到 t 的观测历史（K 为历史长度），观测编码器（ViT 或 VLA 策略的 VLM 骨干）独立处理每帧，得到潜在嵌入：z_{t-k} = enc_ε(o_{t-k})。
- 语言指令由 CLIP 编码，经学习的适配器 A_lang 映射到 WCM 潜在空间：u_ℓ = A_lang(CLIP(ℓ))。

### 历史主干与交叉注意力
- 编码的视觉历史先与指令 token 进行交叉注意力，再由因果 Transformer 历史主干（世界预测器）处理：h_t = Tr_φ(XAttn(z_{t-K+1:t}, u_ℓ))。
- 隐藏表示 h_t 输入两个独立解码头。

### 价值与动态预测
- 价值解码头 D_value 输出回报估计：V̂_t = D_value(h_t)。
- 动作条件潜在动态分支使用残差更新预测下一潜在状态：ẑ_{t+1} = D_world(h_t, a_t, z_t)，其中 D_world 由动作编码器和门控 FiLM 残差块实现。

### 训练目标
总目标为 L = L_value + λ·L_pred + η·L_SIGReg，所有组件端到端训练：
- 预测损失：L_pred = ||ẑ_{t+1} - z_{t+1}||_2^2（教师强制）。
- SIGReg 损失：防止潜在空间特征坍缩，鼓励匹配各向同性高斯分布（仅在离线策略管线中使用）。
- 价值损失：L_value = ||V̂_t - G_t||_2^2。

### 奖励与回报定义
- 奖励：成功 r_t=0，失败 r_t=-C_fail（C_fail=300），否则 r_t=-1。
- 回报：G_t = Σ γ^{t'-t} r_{t'}，并最小-最大归一化到 [-1,1]。

### 策略更新管线
- 在线策略（仿真）：AR 模型（OpenVLA-OFT）用 PPO，流匹配模型（π_0、π_0.5）用 Flow-SDE。
- 离线策略（真实世界）：AR 模型用 AWR，流匹配模型用 RECAP。两种离线方法均使用在线 rollout 数据补充缓冲区，而非纯离线数据。

## 关键创新

1. **联合世界预测与价值估计的评论家架构**：WCM 首次将未来潜在状态预测作为辅助任务引入评论家训练，使价值表示显式编码时间动态。这一设计直接解决了单帧 critic 在 POMDP 下的状态近似缺陷，且通过轻量级 LeJEPA 架构避免了高维视觉历史输入的指数级复杂度。

2. **历史观测的因果 Transformer 处理**：通过交叉注意力将语言指令注入视觉历史，再由因果 Transformer 主干处理，WCM 能以线性复杂度整合 K 帧历史（实验表明 K=3 最优），捕捉速度与加速度等一阶、二阶动态信息，而无需显式建模完整状态转移。

3. **跨算法与跨策略的通用性**：WCM 被设计为即插即用组件，可替换 PPO、Flow-SDE、AWR、RECAP 等不同 RL 算法中的原始 critic。在仿真与真实世界共 149 个任务上验证，均带来一致且显著的性能提升，表明其作为评论家基础架构的通用价值。

## 实验与结果

实验覆盖 4 个仿真基准（ManiSkill、MetaWorld、CALVIN、LIBERO-Plus）与真实世界 WidowX-250S 上的 7 个任务。关键结果如下：

### ManiSkill 主结果（Table 1）
| 策略 | 方法 | IND 成功率 | OOD 成功率 |
|------|------|-----------|-----------|
| π_0 | SFT | 38.4 | 18.1 |
| π_0 | +WCM | 84.4 ± 1.2 (+46.0) | 51.5 ± 1.5 (+33.4) |
| π_0.5 | SFT | 47.0 | 26.4 |
| π_0.5 | +WCM | 91.9 ± 0.4 (+44.9) | 64.4 ± 1.4 (+38.0) |
| OpenVLA-OFT | SFT | 28.1 | 18.3 |
| OpenVLA-OFT | +WCM | 99.0 ± 0.4 (+70.9) | 77.9 ± 0.8 (+59.6) |
| Zero-Shot | +WCM | 98.7 ± 0.3 (+97.9) | 73.5 ± 1.8 (+72.7) |

OpenVLA-OFT 从 0.78% 初始性能提升 12,551%（由表内数值 0.78%→98.7 计算），从弱 SFT 基线提升 252%。

### LIBERO-Plus（Table 2）
| 策略 | One-SFT | +WCM | Δ |
|------|---------|------|---|
| π_0 | 39.1 ± 2.1 | 72.8 ± 1.9 | +33.7 |
| π_0.5 | 38.0 ± 1.6 | 73.7 ± 1.4 | +35.7 |
| OpenVLA-OFT | 29.3 ± 1.5 | 74.0 ± 1.8 | +44.7 |

从 one-shot SFT 出发约 250 步 RL 后超过 full-shot SFT（20k 轨迹）。

### 真实世界（Table 3，成功率 /50）
| 任务 | OpenVLA-OFT +WCM | π_0.5 +WCM |
|------|-----------------|------------|
| Carrot | 32/50 | 44/50 |
| Banana | 26/50 | 38/50 |
| Pepper | 26/50 | 43/50 |
| Cloth Folding | 38/50 | 38/50 |
| Towel Folding | 40/50 | 35/50 |
| Stovetop Cleaning | 15/50 | 33/50 |
| Conveyor Belt Sushi | 22/50 | 24/50 |

### 消融（Figure 5）
- 历史长度 K=3 表现最佳。
- λ 最佳范围 [0.3, 0.5]；λ 变化导致 OOD 波动 10.6 个百分点，IND 仅 2.7 个百分点，表明 OOD 对 λ 更敏感。

### 仿真到真实迁移（Table 4）
- 仿真 SFT 在真实世界 0/25 成功率；仿真 RL 后 7/25、7/25、6/25。
- Real SFT + sim RL 模拟 IND 73.5，真实 11/25、8/25、9/25。

## 边界与局限

- 更长观测历史并非总是有益，超过最优长度（K=3）后收益有限，一阶和二阶动态信息（速度、加速度）已足够描述所需动态特征。
- λ 控制世界预测与价值学习间的权衡，过大或过小均非最优，且 OOD 性能对 λ 更敏感。
- 仿真数据与真实机器人数据存在本质差异：仿真环境完全理想化，即使引入基于规则的扰动也难以获得类似真实环境的噪声或干扰。仿真 SFT 模型在真实世界完全无法成功抓取任何物体。
- 作者明确声明不声称 WCM 完全免疫过拟合，仅在 500 步内未观察到过拟合现象。
- SIGReg 未在在线策略管线中采用，因约束 VLM 潜变量会引入不必要的计算开销，其在线场景下的效果论文未明确。

## 工程启示

- **复现核对顺序**：先确认历史长度 K=3 与 λ∈[0.3, 0.5] 的设置，这是消融实验验证的最优区间。其次核对奖励定义（C_fail=300）与回报归一化到 [-1,1] 的细节，这两处直接影响价值损失的量纲与训练稳定性。
- **最易踩坑点**：λ 的取值对 OOD 性能影响显著（波动 10.6 个百分点），调参时应以 OOD 指标为准而非仅看 IND。此外，SIGReg 仅在离线策略管线中使用，在线策略中强行加入会引入不必要的计算开销且效果未验证。
- **真实世界部署**：仿真 SFT 模型直接部署到真实机器人会完全失败（0/25），必须经过真实数据 RL 微调。建议先收集每任务 100 条真实轨迹做 SFT，再以 8 轮 RL 迭代（每轮 50 条 rollout）微调，训练时间可控制在 1 小时内。
- **下游团队选型**：若已有 VLA 策略（π_0、π_0.5、OpenVLA-OFT）且面临动态操作任务（变形物体、传送带），WCM 可作为 critic 的即插即用替换。其 107.2M 可学习参数在 8×H100 上训练开销可控，推理可在 RTX5090 本地工作站实时运行（10 Hz 控制频率）。

## Overview
Reinforcement learning (RL) post-training of Vision-Language-Action (VLA) models has shown strong promise for robotic manipulation. Among RL methods, critic-based approaches rely on a value estimator that predominantly operates on single-frame observations or single-frame VLM backbone latents, which is a fundamental mismatch with the partially observable nature of robot control. A naive approach to incorporate observation history into the critic incurs exponential complexity with high-dimensional visual space, and still fails because pure scalar-return regression provides insufficient supervision for learning cross-temporal dynamics. We identify the root cause as a state approximation problem: without an explicit world modeling objective, the critic's representation cannot capture the temporal structure needed for accurate value estimation. To address this, we propose the World Critic Model (WCM), built on a lightweight LeJEPA architecture; WCM jointly predicts future latent state and estimates values, such that the critic's representation is explicitly trained to capture temporal dynamics rather than merely regress scalar returns. WCM integrates seamlessly into both on-policy and off-policy training pipelines and is compatible with state-of-the-art VLA backbones including Pi0, Pi0.5, and OpenVLA-OFT. Extensive experiments on 149 tasks across four benchmarks demonstrate that WCM consistently achieves state-of-the-art performance in both in-distribution and out-of-distribution settings, with particularly strong generalization gains. We further validate WCM on seven real-world manipulation tasks using OpenVLA-OFT and Pi0.5 with off-policy RL, confirming stable deployment across diverse settings.

## 参考
- https://arxiv.org/abs/2607.29613

## 개요

WCM(World Critic Model)은 비전-언어-행동(VLA) 강화학습을 위한 비평가 모델로, 저자가 제안한 것으로, 기존 비평가가 단일 프레임 관측에 기반하여 발생하는 부분 관측 가능성(POMDP) 불일치 문제를 해결하는 것을 목표로 합니다. 핵심 기여는 경량 LeJEPA 아키텍처를 도입하여 미래 잠재 상태 예측과 가치 추정을 결합하고, 비평가 표현이 시간적 역학을 명시적으로 포착하도록 하여 시뮬레이션 및 실제 세계에서의 작업 성공률과 분포 외(OOD) 일반화 능력을 크게 향상시킨 것입니다.

## 무엇을 바꾸었는가

기존 VLA-RL 방법의 가치 추정기는 대부분 단일 프레임 관측 또는 단일 프레임 VLM 백본 잠재 표현에 기반하며, 이는 로봇 제어에 내재된 부분 관측 가능성(POMDP) 본질과 상충됩니다. 단순히 관측 이력을 비평가 입력에 연결하면 고차원 시각 공간에서 지수적 복잡도가 발생하고, 순수 스칼라 보상 회귀가 제공하는 감독 신호는 너무 희소하여 비평가가 시간 단계에 걸친 동적 구조를 학습하도록 유도하기에 충분하지 않습니다. 근본적인 문제는 상태 근사에 있습니다: 명시적 세계 모델링 목표가 없을 때 비평가의 잠재 표현은 가치 추정에 필요한 시간적 정보를 인코딩할 수 없으며, 이로 인해 실제 세계의 동적 작업(예: 변형 물체 조작)에서 잘못된 가치 판단을 내리고 심지어 로봇 팔을 테이블에 부딪히게 만들 수 있습니다.

WCM이 실제로 바꾸는 것은 비평가의 학습 목표와 표현 공간입니다. 더 이상 비평가를 단순한 스칼라 보상 회귀기로 보지 않고, 세계 모델과 가치 추정기를 결합한 형태로 훈련합니다. 미래 잠재 상태를 명시적으로 예측함으로써 비평가의 표현은 시간적 동적 구조를 강제로 인코딩하게 되며, 가치 추정 시 역사적 맥락을 활용하여 "성공에 접근 중"과 "충돌 임박"과 같은 물리적 상태를 구분할 수 있습니다. 이러한 전환은 단일 프레임 비평가가 실제 세계 작업에서 역사적 정보 부족으로 실패하는 패턴에 직접 대응하며, 비평가의 역할을 "보상 예측기"에서 "상태 역학 이해기"로 승격시킵니다.

## 방법 분해

WCM은 경량 LeJEPA 아키텍처를 기반으로 하며, 네 가지 핵심 구성 요소로 이루어져 있습니다: 관측 인코더, 세계 예측기, 가치 디코더 헤드, 행동 조건 잠재 동적 분기. 처리 흐름은 다음과 같습니다:

### 관측 인코딩 및 명령 주입
- 시간 단계 t-K+1부터 t까지의 관측 이력(K는 이력 길이)이 주어지면, 관측 인코더(ViT 또는 VLA 정책의 VLM 백본)가 각 프레임을 독립적으로 처리하여 잠재 임베딩을 얻습니다: z_{t-k} = enc_ε(o_{t-k}).
- 언어 명령은 CLIP으로 인코딩되고, 학습된 어댑터 A_lang을 통해 WCM 잠재 공간에 매핑됩니다: u_ℓ = A_lang(CLIP(ℓ)).

### 이력 백본 및 교차 주의
- 인코딩된 시각 이력은 먼저 명령 토큰과 교차 주의를 수행한 후, 인과 Transformer 이력 백본(세계 예측기)이 처리합니다: h_t = Tr_φ(XAttn(z_{t-K+1:t}, u_ℓ)).
- 숨겨진 표현 h_t는 두 개의 독립적인 디코더 헤드에 입력됩니다.

### 가치 및 동적 예측
- 가치 디코더 헤드 D_value는 보상 추정을 출력합니다: V̂_t = D_value(h_t).
- 행동 조건 잠재 동적 분기는 잔차 업데이트를 사용하여 다음 잠재 상태를 예측합니다: ẑ_{t+1} = D_world(h_t, a_t, z_t), 여기서 D_world는 행동 인코더와 게이티드 FiLM 잔차 블록으로 구현됩니다.

### 훈련 목표
총 목표는 L = L_value + λ·L_pred + η·L_SIGReg이며, 모든 구성 요소가 엔드투엔드로 훈련됩니다:
- 예측 손실: L_pred = ||ẑ_{t+1} - z_{t+1}||_2^2(교사 강제).
- SIGReg 손실: 잠재 공간 특징 붕괴를 방지하고 등방성 가우시안 분포 일치를 장려합니다(오프라인 정책 파이프라인에서만 사용).
- 가치 손실: L_value = ||V̂_t - G_t||_2^2.

### 보상 및 수익 정의
- 보상: 성공 r_t=0, 실패 r_t=-C_fail(C_fail=300), 그 외 r_t=-1.
- 수익: G_t = Σ γ^{t'-t} r_{t'}, 최소-최대 정규화를 통해 [-1,1] 범위로 조정.

### 정책 업데이트 파이프라인
- 온라인 정책(시뮬레이션): AR 모델(OpenVLA-OFT)은 PPO 사용, 플로우 매칭 모델(π_0, π_0.5)은 Flow-SDE 사용.
- 오프라인 정책(실제 세계): AR 모델은 AWR 사용, 플로우 매칭 모델은 RECAP 사용. 두 오프라인 방법 모두 순수 오프라인 데이터가 아닌 온라인 롤아웃 데이터로 버퍼를 보충합니다.

## 핵심 혁신

1. **세계 예측과 가치 추정을 결합한 비평가 아키텍처**: WCM은 처음으로 미래 잠재 상태 예측을 보조 작업으로 비평가 훈련에 도입하여 가치 표현이 시간적 역학을 명시적으로 인코딩하도록 합니다. 이 설계는 POMDP 하에서 단일 프레임 비평가의 상태 근사 결함을 직접 해결하며, 경량 LeJEPA 아키텍처를 통해 고차원 시각 이력 입력의 지수적 복잡도를 피합니다.

2. **이력 관측의 인과 Transformer 처리**: 교차 주의를 통해 언어 명령을 시각 이력에 주입한 후 인과 Transformer 백본이 처리함으로써, WCM은 선형 복잡도로 K 프레임 이력(실험에서 K=3이 최적)을 통합하여 속도와 가속도와 같은 1차 및 2차 동적 정보를 포착할 수 있으며, 완전한 상태 전이를 명시적으로 모델링할 필요가 없습니다.

3. **알고리즘 및 정책 전반에 걸친 범용성**: WCM은 플러그 앤 플레이 구성 요소로 설계되어 PPO, Flow-SDE, AWR, RECAP 등 다양한 RL 알고리즘의 원래 비평가를 대체할 수 있습니다. 시뮬레이션과 실제 세계의 총 149개 작업에서 검증되었으며, 일관되고 유의미한 성능 향상을 보여 비평가 기본 아키텍처로서의 범용 가치를 입증합니다.

## 실험 및 결과

실험은 4개의 시뮬레이션 벤치마크(ManiSkill, MetaWorld, CALVIN, LIBERO-Plus)와 실제 세계 WidowX-250S의 7개 작업을 포함합니다. 주요 결과는 다음과 같습니다:

### ManiSkill 주요 결과(Table 1)
| 정책 | 방법 | IND 성공률 | OOD 성공률 |
|------|------|-----------|-----------|
| π_0 | SFT | 38.4 | 18.1 |
| π_0 | +WCM | 84.4 ± 1.2 (+46.0) | 51.5 ± 1.5 (+33.4) |
| π_0.5 | SFT | 47.0 | 26.4 |
| π_0.5 | +WCM | 91.9 ± 0.4 (+44.9) | 64.4 ± 1.4 (+38.0) |
| OpenVLA-OFT | SFT | 28.1 | 18.3 |
| OpenVLA-OFT | +WCM | 99.0 ± 0.4 (+70.9) | 77.9 ± 0.8 (+59.6) |
| Zero-Shot | +WCM | 98.7 ± 0.3 (+97.9) | 73.5 ± 1.8 (+72.7) |

OpenVLA-OFT는 초기 성능 0.78%에서 12,551% 향상(표 내 값 0.78%→98.7 계산), 약한 SFT 기준선 대비 252% 향상.

### 실제 세계(Table 3, 성공률 /50)
| 작업 | OpenVLA-OFT +WCM | π_0.5 +WCM |
|------|-----------------|------------|
| Carrot | 32/50 | 44/50 |
| Banana | 26/50 | 38/50 |
| Pepper | 26/50 | 43/50 |
| Cloth Folding | 38/50 | 38/50 |
| Towel Folding | 40/50 | 35/50 |
| Stovetop Cleaning | 15/50 | 33/50 |
| Conveyor Belt Sushi | 22/50 | 24/50 |

### 소거(Figure 5)
- 이력 길이 K=3이 가장 우수한 성능.
- λ 최적 범위 [0.3, 0.5]; λ 변화로 OOD 변동 10.6% 포인트, IND는 2.7% 포인트에 불과하여 OOD가 λ에 더 민감함을 시사.

### 시뮬레이션-실제 전이(Table 4)
- 시뮬레이션 SFT는 실제 세계에서 0/25 성공률; 시뮬레이션 RL 후 7/25, 7/25, 6/25.
- Real SFT + sim RL 시뮬레이션 IND 73.5, 실제 11/25, 8/25, 9/25.

## 경계 및 한계

- 더 긴 관측 이력이 항상 유익한 것은 아니며, 최적 길이(K=3)를 초과하면 이득이 제한적입니다. 1차 및 2차 동적 정보(속도, 가속도)가 필요한 동적 특징을 설명하기에 충분합니다.
- λ는 세계 예측과 가치 학습 간의 균형을 제어하며, 너무 크거나 작으면 최적이 아니며 OOD 성능이 λ에 더 민감합니다.
- 시뮬레이션 데이터와 실제 로봇 데이터 간에는 본질적 차이가 있습니다: 시뮬레이션 환경은 완전히 이상적이며, 규칙 기반 교란을 도입하더라도 실제 환경과 유사한 노이즈나 간섭을 얻기 어렵습니다. 시뮬레이션 SFT 모델은 실제 세계에서 어떤 물체도 성공적으로 잡을 수 없습니다.
- 저자는 WCM이 과적합에 완전히 면역이라고 주장하지 않으며, 500단계 내에서 과적합 현상이 관찰되지 않았을 뿐입니다.
- SIGReg는 온라인 정책 파이프라인에서 채택되지 않았으며, VLM 잠재 변수를 제약하면 불필요한 계산 오버헤드가 발생하고 온라인 시나리오에서의 효과는 논문에서 명확히 밝히지 않았습니다.

## 공학적 시사점

- **재현 검증 순서**: 먼저 이력 길이 K=3과 λ∈[0.3, 0.5] 설정을 확인하세요. 이는 소거 실험에서 검증된 최적 구간입니다. 다음으로 보상 정의(C_fail=300)와 수익 정규화 [-1,1] 세부 사항을 확인하세요. 이 두 가지는 가치 손실의 차원과 훈련 안정성에 직접 영향을 미칩니다.
- **가장 실수하기 쉬운 지점**: λ 값은 OOD 성능에 유의미한 영향을 미치며(10.6% 포인트 변동), 하이퍼파라미터 튜닝 시 IND가 아닌 OOD 지표를 기준으로 해야 합니다. 또한 SIGReg는 오프라인 정책 파이프라인에서만 사용되며, 온라인 정책에서 강제로 추가하면 불필요한 계산 오버헤드가 발생하고 효과가 검증되지 않았습니다.
- **실제 세계 배포**: 시뮬레이션 SFT 모델을 실제 로봇에 직접 배포하면 완전히 실패하며(0/25), 반드시 실제 데이터 RL 미세 조정이 필요합니다. 작업당 100개의 실제 궤적을 수집하여 SFT를 수행한 후, 8라운드 RL 반복(라운드당 50개 롤아웃)으로 미세 조정하는 것을 권장하며, 훈련 시간은 1시간 이내로 제어할 수 있습니다.
- **하류 팀 선택**: 이미 VLA 정책(π_0, π_0.5, OpenVLA-OFT)이 있고 동적 조작 작업(변형 물체, 컨베이어 벨트)에 직면한 경우, WCM을 비평가의 플러그 앤 플레이 대체로 사용할 수 있습니다. 107.2M 학습 가능한 파라미터는 8×H100에서 훈련 오버헤드가 관리 가능하며, 추론은 RTX5090 로컬 워크스테이션에서 실시간(10 Hz 제어 주파수)으로 실행할 수 있습니다.
