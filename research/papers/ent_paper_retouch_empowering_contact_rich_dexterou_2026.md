---
$id: ent_paper_retouch_empowering_contact_rich_dexterou_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction'
  zh: 'ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction'
  ko: 'ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction'
summary:
  en: Fusing tactile signals has proven effective for contact-rich manipulation, enabling robots to perceive contact states
    and adapt to rapidly changing physical interactions. Yet effectively integrating tactile feedback into dexterous manipulation
    remains underexplored. In this work, we introduce ReTouch, a vision-language-action model (VLA) that supports contact-rich
    dexterous manipulation through.
  zh: ReTouch 是一个面向接触丰富灵巧操作的触觉-视觉-语言-动作（VLA）策略框架，由研究团队在 XHand–UR7e 平台上提出。其核心贡献在于通过结构化触觉补丁编码、未来触觉潜在预测与递归在线精化，解决了触觉时序预测与动作生成之间的对齐问题，在标准与挑战性设置下分别超越最强基线
    18.4 和 23.8 个百分点。
  ko: Fusing tactile signals has proven effective for contact-rich manipulation, enabling robots to perceive contact states
    and adapt to rapidly changing physical interactions. Yet effectively integrating tactile feedback into dexterous manipulation
    remains underexplored. In this work, we introduce ReTouch, a vision-language-action model (VLA) that supports contact-rich
    dexterous manipulation through.
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
- retouch
- empowering
- contact
- rich
- dexterou
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. 深读+数字白名单复核通过 2026-08-10（补网）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.01824 ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tact'
  url: https://arxiv.org/abs/2608.01824
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---

## 概述

ReTouch 是一个面向接触丰富灵巧操作的触觉-视觉-语言-动作（VLA）策略框架，由研究团队在 XHand–UR7e 平台上提出。其核心贡献在于通过结构化触觉补丁编码、未来触觉潜在预测与递归在线精化，解决了触觉时序预测与动作生成之间的对齐问题，在标准与挑战性设置下分别超越最强基线 18.4 和 23.8 个百分点。

## 它改变了什么

这个工作的真正改变在于，它把触觉预测从“一次性预报”重新定义为“由执行反馈持续更新的控制状态”。现有方法（如 Tactile-VLA、TaF-VLA）虽然引入了触觉，但要么将触觉展平为通用 token 模糊了手指级空间结构，要么在动作块执行过程中让预测的触觉状态逐渐过时，导致后续动作修正被误导。ReTouch 直击这两个痛点：一是保留接触拓扑的触觉表示，二是让未来触觉预测在块内以 36 Hz 高频被递归精化。

另一个关键改变是架构层面的解耦。它不再让 VLM 以单一频率处理所有模态，而是将低频视觉-语言推理（9 Hz）与高频触觉-动作更新（36 Hz）分离。这种多速率异步设计更符合真实物理交互的时序需求——视觉场景变化慢，而接触状态（滑动、位移）变化快。这不仅是工程优化，更是对“预测-反应”范式的重新思考：预测不是终点，而是需要被反馈持续修正的中间状态。

## 方法拆解

### 整体架构与多速率调度
- 低频 VLM 以 9 Hz 缓存语义上下文 c_k，与块起始状态 s_k 一起条件化高频控制。
- 高频 FAE（Foresight Action Expert）以 36 Hz 运行，每次调用重新生成 16 步动作块 Â_t，但仅应用偏移 o ∈ {4, 8, 12} 后的未执行后缀。

### Tactile-Patch Encoder（TPE）
- 每指 120 个 3D taxel 划分为 5 个功能补丁（tip、center、base、left、right）。
- 补丁聚合统计量：接触门控平均力 f̄_p、分量级最大绝对值 m_p、接触比例 a_p、最大 L2 范数 q_p。
- 软接触权重：w_j = σ(‖f_j‖₂ − θ_c)/γ_c，θ_c 在预训练（0.5）与策略训练（1.0）间切换。
- 精确补丁池化：e_p = g(SiLU(h_p)) + log(a_p + ε)，α_p = softmax，z = LN(Σ α_p h_p)。
- 历史 9 帧按手指用学习标量权重池化，当前帧 token 保留并带独立类型嵌入，共 10 个输入 token。

### 双专家潜在对齐
- HAE（Hindsight Action Expert）：特权分支，访问真实未来触觉 τ_{t:t+H}^+，提取目标表示 Z_{t,ℓ}^{+,hid}。
- FAE（Foresight Action Expert）：可部署分支，用可学习查询 Q^fore 推断未来触觉潜在 Ẑ_{t,ℓ}^+。
- 对齐损失：L_align = d_cos(g_ψ(Ẑ_{t,ℓ}^+), sg(Z_{t,ℓ}^{+,hid}))，在 18 层 Transformer 的第 12 层对齐，权重 0.1。

### 在线触觉预测精化
- 每次高频调用构造查询：Q̃_t^fore = M_t ⊙ sg(Ẑ_{t-1}^+) + (1-M_t) ⊙ Q^fore，M_t 选择已流逝部分的潜在前缀。
- 方向性注意力掩码：触觉查询可关注上下文但不能关注动作 token；动作 token 可关注更新的触觉潜在，防止信息泄漏。
- 训练时从 {4, 8, 12} 随机采样偏移，部署时以高频控制率重复调用。

### 动作流匹配
- 采样 ε∼N(0,I)，t = 0.001 + 0.999·t̃，t̃∼Beta(1.5,1)；x_t = tε + (1−t)a，u = ε − a。
- 推理用 10 步显式 Euler 从 t=1 到 0，同一块内所有精化调用复用初始动作噪声样本。

## 关键创新

1. **递归触觉潜在精化机制**：这是最核心的创新。它不是简单地“预测未来触觉”，而是让预测结果在动作块执行过程中被高频（36 Hz）重新估计和修正。离线诊断显示，接触中阶段潜在余弦相似度提升 0.908%，动作后缀 MSE 降低 2.139%。这直接解决了多指操作中接触状态快速变化导致预测过时的问题。

2. **结构化触觉补丁编码器（TPE）**：与将触觉展平为通用 token 的做法不同，TPE 保留手指级空间拓扑（5 指 × 5 补丁），并引入软接触权重和精确池化。预训练诊断显示，平衡三头损失将接触 F1 从 0.9980 提升至 0.9999，规范补丁分布 KL 从 0.1648 降至 0.0048，活动力方向余弦从 0.4089 提升至 0.8071。这证明结构化表示对局部接触变化的敏感性远优于扁平化方法。

3. **HAE-FAE 双专家对齐训练**：通过特权分支（HAE）提供动作相关的未来触觉目标，让可部署分支（FAE）在无真实未来信息时也能逼近特权表示。这种“教师-学生”式对齐避免了直接回归原始触觉信号的冗余，而是聚焦于动作相关的潜在空间。

## 实验与结果

### 标准设置平均成功率（Table 1）
| 方法 | 成功率 (%) |
|------|-----------|
| **ReTouch** | **83.6** |
| Tactile-VLA | 65.2 |
| π0.5+tactile | 53.1 |
| π0.5 | 51.5 |
| π0+tactile | 43.8 |
| π0 | 45.6 |
| ViTacFormer | 33.1 |
| RDP | 31.6 |

### 挑战设置平均成功率（Table 2）
| 方法 | 成功率 (%) |
|------|-----------|
| **ReTouch** | **73.1** |
| π0.5+tactile | 49.3 |
| π0.5 | 47.1 |
| Tactile-VLA | 35.0 |
| RDP | 10.0 |
| ViTacFormer | 7.8 |

### 消融研究（Table 3）
| 变体 | 成功率 (%) | 差值 |
|------|-----------|------|
| Full ReTouch | 83.6 | — |
| w/o intra-chunk refinement | 60.0 | -23.6 |
| w/o tactile-prediction refinement | 68.4 | -15.2 |
| w/o future tactile prediction | 67.6 | -16.0 |
| non-blocking joint refinement | 75.8 | -7.8 |
| w/o Tactile-Patch Encoder | 69.1 | -14.5 |

### 关键结果解读
- 最大任务增益：Sponge Wipe 超越最强基线 25.0 个百分点，Liquid Transfer 超越 19.0 个百分点。
- 拉动干扰（Pull Bottle）增益最大：ReTouch 85.0% vs 最强基线 30.0%，差距 30.0 个百分点。
- 光照变化（Lighting Liquid）超越最强基线 20.0 个百分点。
- 触觉预测细化诊断（100 条测试轨迹）：接触后潜在余弦 +0.908%，动作误差 -2.139%。
- 例外：Cabinet Retrieval 中 ReTouch 62.5% 低于 ViTacFormer 67.5%。

## 边界与局限

- **Cabinet Retrieval 例外**：ReTouch 在视觉遮挡任务中低于 ViTacFormer（62.5% vs 67.5%），说明触觉精化在需要长时序视觉推理的任务中可能不是主导因素。
- **编码器预训练诊断的局限**：作者明确承认预训练诊断仅评估编码器质量，不单独证明下游操作增益。
- **未明确项**：论文未提及模型参数量、训练时间、泛化到未见任务/物体的能力、触觉传感器磨损或校准漂移的影响、多平台迁移、安全性分析、失败案例分析、长期稳定性测试。
- **扩展性未验证**：对触觉预测细化机制在更长动作块或更复杂多阶段任务上的扩展性分析未提及。

## 工程启示

- **先核对触觉表示的结构保真度**：如果你的触觉传感器是阵列式（如 taxel），不要直接展平。ReTouch 的补丁划分（tip/center/base/left/right）和软接触权重（θ_c 从 0.5 到 1.0 的切换）是经过预训练验证的关键设计，直接复现可省去大量调参。
- **最容易踩坑的地方是训练-部署不一致**：ReTouch 在训练时随机采样偏移 {4, 8, 12} 构造监督，部署时以 36 Hz 高频调用。如果只训练单次预测而部署时做多次精化，性能会显著下降（消融显示 w/o intra-chunk refinement 掉 23.6 个百分点）。务必在训练中模拟多偏移场景。
- **注意动作噪声的复用**：同一块内所有精化调用复用初始动作噪声样本，这是流匹配稳定性的关键。如果每次精化重新采样噪声，动作输出会抖动。
- **对下游团队的指导**：如果目标是接触丰富任务（如抓取、按压、擦拭），ReTouch 的架构值得参考；但如果是视觉遮挡主导的任务（如 Cabinet Retrieval），可能需要更强的视觉推理而非触觉精化。建议先评估任务中接触状态变化的频率——变化越快，递归精化的收益越大。
- **硬件门槛**：推理延迟在 RTX 5090 上为 52.25 ms（初始）+ 19.54 ms（精化），对应 9 Hz/36 Hz。部署时需确保 GPU 能支撑双频率异步调度，否则需降低 VLM 频率或减少触觉历史窗口。

## Overview
Fusing tactile signals has proven effective for contact-rich manipulation, enabling robots to perceive contact states and adapt to rapidly changing physical interactions. Yet effectively integrating tactile feedback into dexterous manipulation remains underexplored. In this work, we introduce ReTouch, a vision-language-action model (VLA) that supports contact-rich dexterous manipulation through tactile predictions continually refined online using execution-time feedback. ReTouch builds on two main innovations for tactile representation and closed-loop action generation. First, its Tactile-Patch Encoder represents tactile observations as structured tactile patch features that preserve finger identity and local contact structure, providing contact cues for fine-grained dexterous control. Second, its high-frequency action module jointly predicts future tactile states and action chunks and refines both using incoming tactile feedback during execution. This closed-loop refinement keeps tactile predictions aligned with evolving physical interactions, enabling responsive action correction and improving robustness to contact changes and execution errors. We further introduce XHT-Dataset, comprising 900 real-world demonstrations across seven contact-rich tasks collected on an XHand--UR7e platform, and evaluate ReTouch through closed-loop real-robot experiments. ReTouch surpasses the strongest baseline by 18.4 and 23.8 percentage points in average success rate under standard and challenging conditions, respectively, demonstrating its effectiveness and robustness.

## 参考
- https://arxiv.org/abs/2608.01824

## 개요

ReTouch는 XHand–UR7e 플랫폼에서 연구팀이 제안한 접촉이 풍부한 정밀 조작을 위한 촉각-시각-언어-행동(VLA) 정책 프레임워크입니다. 핵심 기여는 구조화된 촉각 패치 인코딩, 미래 촉각 잠재 예측, 재귀적 온라인 정밀화를 통해 촉각 시계열 예측과 행동 생성 간의 정렬 문제를 해결한 것이며, 표준 및 도전적 설정에서 각각 최강 기준선을 18.4 및 23.8퍼센트 포인트 초과 달성했습니다.

## 무엇을 바꾸었는가

이 작업의 진정한 변화는 촉각 예측을 "일회성 예보"에서 "실행 피드백에 의해 지속적으로 갱신되는 제어 상태"로 재정의한 것입니다. 기존 방법(Tactile-VLA, TaF-VLA 등)은 촉각을 도입했지만, 촉각을 일반 토큰으로 평탄화하여 손가락 수준의 공간 구조를 모호하게 만들거나, 행동 블록 실행 중에 예측된 촉각 상태가 점차 낡아져 후속 행동 수정을 오도했습니다. ReTouch는 이 두 가지 문제점을 직접 공략합니다. 첫째, 접촉 토폴로지를 보존하는 촉각 표현을 유지하고, 둘째, 미래 촉각 예측이 블록 내에서 36Hz 고주파로 재귀적으로 정밀화되도록 합니다.

또 다른 핵심 변화는 아키텍처 수준의 분리입니다. VLM이 단일 주파수로 모든 모달리티를 처리하도록 하지 않고, 저주파 시각-언어 추론(9Hz)과 고주파 촉각-행동 갱신(36Hz)을 분리합니다. 이러한 다중 속도 비동기 설계는 실제 물리적 상호작용의 시간적 요구(시각 장면은 느리게 변하지만 접촉 상태(슬립, 변위)는 빠르게 변함)에 더 부합합니다. 이는 단순한 엔지니어링 최적화가 아니라 "예측-반응" 패러다임에 대한 재고입니다. 예측은 종착점이 아니라 피드백에 의해 지속적으로 수정되어야 하는 중간 상태입니다.

## 방법 분해

### 전체 아키텍처 및 다중 속도 스케줄링
- 저주파 VLM은 9Hz로 의미론적 컨텍스트 c_k를 캐시하고, 블록 시작 상태 s_k와 함께 고주파 제어를 조건화합니다.
- 고주파 FAE(Foresight Action Expert)는 36Hz로 실행되며, 호출 시마다 16단계 행동 블록 Â_t를 재생성하지만 오프셋 o ∈ {4, 8, 12} 이후의 미실행 접미사만 적용합니다.

### 이중 전문가 잠재 정렬
- HAE(Hindsight Action Expert): 특권 분기로, 실제 미래 촉각 τ_{t:t+H}^+에 접근하여 목표 표현 Z_{t,ℓ}^{+,hid}를 추출합니다.
- FAE(Foresight Action Expert): 배포 가능한 분기로, 학습 가능한 쿼리 Q^fore를 사용하여 미래 촉각 잠재 Ẑ_{t,ℓ}^+를 추론합니다.
- 정렬 손실: L_align = d_cos(g_ψ(Ẑ_{t,ℓ}^+), sg(Z_{t,ℓ}^{+,hid})), 18층 Transformer의 12층에서 정렬, 가중치 0.1.

### 온라인 촉각 예측 정밀화
- 각 고주파 호출 시 쿼리 구성: Q̃_t^fore = M_t ⊙ sg(Ẑ_{t-1}^+) + (1-M_t) ⊙ Q^fore, M_t는 경과 부분의 잠재 접두사를 선택합니다.
- 방향성 어텐션 마스크: 촉각 쿼리는 컨텍스트를 볼 수 있지만 행동 토큰은 볼 수 없습니다. 행동 토큰은 갱신된 촉각 잠재를 볼 수 있어 정보 누출을 방지합니다.
- 훈련 시 {4, 8, 12}에서 오프셋을 무작위 샘플링하고, 배포 시 고주파 제어율로 반복 호출합니다.

### 행동 흐름 매칭
- ε∼N(0,I) 샘플링, t = 0.001 + 0.999·t̃, t̃∼Beta(1.5,1); x_t = tε + (1−t)a, u = ε − a.
- 추론은 t=1에서 0까지 10단계 명시적 Euler를 사용하며, 동일 블록 내 모든 정밀화 호출은 초기 행동 노이즈 샘플을 재사용합니다.

## 핵심 혁신

1. **재귀적 촉각 잠재 정밀화 메커니즘**: 가장 핵심적인 혁신입니다. 단순히 "미래 촉각을 예측"하는 것이 아니라, 예측 결과가 행동 블록 실행 중에 고주파(36Hz)로 재추정되고 수정되도록 합니다. 오프라인 진단에 따르면 접촉 중 단계의 잠재 코사인 유사도가 0.908% 향상되고, 행동 접미사 MSE가 2.139% 감소했습니다. 이는 다중 손가락 조작에서 접촉 상태가 빠르게 변하여 예측이 낡아지는 문제를 직접 해결합니다.

2. **구조화된 촉각 패치 인코더(TPE)**: 촉각을 일반 토큰으로 평탄화하는 방식과 달리, TPE는 손가락 수준의 공간 토폴로지(5손가락 × 5패치)를 보존하고 소프트 접촉 가중치와 정밀 풀링을 도입합니다. 사전 훈련 진단에 따르면 균형 잡힌 삼중 손실이 접촉 F1을 0.9980에서 0.9999로 향상시키고, 패치 분포 KL을 0.1648에서 0.0048로 낮추며, 활동력 방향 코사인을 0.4089에서 0.8071로 향상시킵니다. 이는 구조화된 표현이 국소 접촉 변화에 대한 민감도가 평탄화 방법보다 훨씬 우수함을 증명합니다.

3. **HAE-FAE 이중 전문가 정렬 훈련**: 특권 분기(HAE)가 행동 관련 미래 촉각 목표를 제공하여, 배포 가능한 분기(FAE)가 실제 미래 정보 없이도 특권 표현에 근접할 수 있게 합니다. 이러한 "교사-학생"식 정렬은 원시 촉각 신호의 중복 회귀를 피하고 행동 관련 잠재 공간에 집중합니다.

## 실험 및 결과

### 표준 설정 평균 성공률 (Table 1)
| 방법 | 성공률 (%) |
|------|-----------|
| **ReTouch** | **83.6** |
| Tactile-VLA | 65.2 |
| π0.5+tactile | 53.1 |
| π0.5 | 51.5 |
| π0+tactile | 43.8 |
| π0 | 45.6 |
| ViTacFormer | 33.1 |
| RDP | 31.6 |

### 도전적 설정 평균 성공률 (Table 2)
| 방법 | 성공률 (%) |
|------|-----------|
| **ReTouch** | **73.1** |
| π0.5+tactile | 49.3 |
| π0.5 | 47.1 |
| Tactile-VLA | 35.0 |
| RDP | 10.0 |
| ViTacFormer | 7.8 |

### 절제 연구 (Table 3)
| 변형 | 성공률 (%) | 차이 |
|------|-----------|------|
| Full ReTouch | 83.6 | — |
| w/o intra-chunk refinement | 60.0 | -23.6 |
| w/o tactile-prediction refinement | 68.4 | -15.2 |
| w/o future tactile prediction | 67.6 | -16.0 |
| non-blocking joint refinement | 75.8 | -7.8 |
| w/o Tactile-Patch Encoder | 69.1 | -14.5 |

### 핵심 결과 해석
- 최대 작업 이득: Sponge Wipe가 최강 기준선을 25.0퍼센트 포인트 초과, Liquid Transfer가 19.0퍼센트 포인트 초과.
- 외란 견인(Pull Bottle) 이득 최대: ReTouch 85.0% vs 최강 기준선 30.0%, 격차 30.0퍼센트 포인트.
- 조명 변화(Lighting Liquid) 최강 기준선을 20.0퍼센트 포인트 초과.
- 촉각 예측 정밀화 진단(100개 테스트 궤적): 접촉 후 잠재 코사인 +0.908%, 행동 오류 -2.139%.
- 예외: Cabinet Retrieval에서 ReTouch 62.5%가 ViTacFormer 67.5%보다 낮음.

## 경계 및 한계

- **Cabinet Retrieval 예외**: ReTouch는 시각적 폐색 작업에서 ViTacFormer보다 낮음(62.5% vs 67.5%). 이는 긴 시계열 시각 추론이 필요한 작업에서 촉각 정밀화가 지배적 요소가 아닐 수 있음을 시사합니다.
- **인코더 사전 훈련 진단의 한계**: 저자들은 사전 훈련 진단이 인코더 품질만 평가하며, 하류 조작 이득을 단독으로 증명하지 않는다고 명시적으로 인정했습니다.
- **명시되지 않은 항목**: 논문은 모델 파라미터 수, 훈련 시간, 미지 작업/객체로의 일반화, 촉각 센서 마모 또는 캘리브레이션 드리프트 영향, 다중 플랫폼 이전, 안전성 분석, 실패 사례 분석, 장기 안정성 테스트를 언급하지 않았습니다.
- **확장성 미검증**: 더 긴 행동 블록이나 더 복잡한 다단계 작업에서 촉각 예측 정밀화 메커니즘의 확장성 분석은 언급되지 않았습니다.

## 엔지니어링 시사점

- **먼저 촉각 표현의 구조적 충실도를 확인하세요**: 촉각 센서가 배열형(예: taxel)이라면 직접 평탄화하지 마세요. ReTouch의 패치 분할(tip/center/base/left/right)과 소프트 접촉 가중치(θ_c 0.5에서 1.0으로 전환)는 사전 훈련으로 검증된 핵심 설계로, 직접 재현하면 많은 하이퍼파라미터 튜닝을 절약할 수 있습니다.
- **가장 함정에 빠지기 쉬운 곳은 훈련-배포 불일치입니다**: ReTouch는 훈련 시 오프셋 {4, 8, 12}를 무작위 샘플링하여 감독을 구성하고, 배포 시 36Hz 고주파로 호출합니다. 단일 예측만 훈련하고 배포 시 여러 번 정밀화하면 성능이 크게 저하됩니다(절제 연구에서 w/o intra-chunk refinement가 23.6퍼센트 포인트 하락). 훈련에서 다중 오프셋 시나리오를 반드시 시뮬레이션하세요.
- **행동 노이즈 재사용에 주의하세요**: 동일 블록 내 모든 정밀화 호출은 초기 행동 노이즈 샘플을 재사용합니다. 이는 흐름 매칭 안정성의 핵심입니다. 매 정밀화마다 노이즈를 재샘플링하면 행동 출력이 떨립니다.
- **하류 팀에 대한 지침**: 목표가 접촉이 풍부한 작업(예: 파지, 누르기, 닦기)이라면 ReTouch의 아키텍처를 참고할 가치가 있습니다. 그러나 시각적 폐색이 지배적인 작업(예: Cabinet Retrieval)이라면 촉각 정밀화보다 더 강력한 시각 추론이 필요할 수 있습니다. 먼저 작업에서 접촉 상태 변화의 빈도를 평가하세요. 변화가 빠를수록 재귀적 정밀화의 이득이 커집니다.
- **하드웨어 요구 사항**: 추론 지연 시간은 RTX 5090에서 52.25ms(초기) + 19.54ms(정밀화)로, 9Hz/36Hz에 해당합니다. 배포 시 GPU가 이중 주파수 비동기 스케줄링을 지원할 수 있는지 확인해야 하며, 그렇지 않으면 VLM 주파수를 낮추거나 촉각 히스토리 창을 줄여야 합니다.
