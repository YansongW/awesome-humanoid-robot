---
$id: ent_paper_when_does_legacy_data_start_help_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Robot Learning
  zh: When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Robot Learning
  ko: When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Robot Learning
summary:
  en: 'Robotic hardware evolves over time, but demonstration data is often tied to a specific sensor and actuator configuration.
    This raises a practical and underexplored question: when does legacy data begin to benefit an upgraded robot? We study
    this question on a wheeled humanoid platform across two hardware generations, where both the camera and gripper are changed
    while the overall morphology.'
  zh: 本文研究机器人硬件迭代后，旧代（legacy）演示数据何时开始对新一代（Gen-2）策略产生正向迁移收益。作者在轮式人形平台上通过真实实验发现，协同训练增益与独立任务成功率呈倒 U 型关系，并据此提出三阶段模型与任务依赖的迁移阈值判据，用于指导数据采集策略。
  ko: 'Robotic hardware evolves over time, but demonstration data is often tied to a specific sensor and actuator configuration.
    This raises a practical and underexplored question: when does legacy data begin to benefit an upgraded robot? We study
    this question on a wheeled humanoid platform across two hardware generations, where both the camera and gripper are changed
    while the overall morphology.'
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
- when
- does
- legacy
- data
- start
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
  title: arXiv:2607.25593 When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Ro
  url: https://arxiv.org/abs/2607.25593
  date: '2026-07-28'
  accessed_at: '2026-08-05'
---

## 概述

本文研究机器人硬件迭代后，旧代（legacy）演示数据何时开始对新一代（Gen-2）策略产生正向迁移收益。作者在轮式人形平台上通过真实实验发现，协同训练增益与独立任务成功率呈倒 U 型关系，并据此提出三阶段模型与任务依赖的迁移阈值判据，用于指导数据采集策略。

## 它改变了什么

该工作真正改变的是对“跨配置数据复用”这一工程常识的认知。此前领域内普遍假设“更多跨配置数据总是有帮助”，但本文用真实机器人实验证明，在目标硬件策略能力极低时（如花插入独立成功率 10.0%），旧数据协同训练不仅无益，甚至可能完全无效（10.0% → 10.0%）。这推翻了数据量至上主义，将问题从“是否该用旧数据”精确转化为“在什么能力门槛下旧数据才开始产生正收益”。

更关键的是，作者没有停留在现象描述，而是给出了一个可操作的工程判据：通过任务复杂度估计（视界长度与空间容差）预测迁移阈值，再以新硬件独立成功率作为代理指标，决定何时停止采集新数据、何时启动旧数据协同训练。这使得硬件迭代中的数据管理从经验试错变为有理论支撑的决策流程。

## 方法拆解

### 三阶段模型
协同训练增益 ΔSR 与独立成功率 SR 呈倒 U 型关系：
- **Phase I（SR < 15–20%）**：旧数据无可测收益，机制为“表征真空”——策略内部表征尚无法解码任务阶段，旧数据梯度与目标梯度期望对齐非正。
- **Phase II（SR 20–75%）**：收益大幅上升（+15 到 +63 个百分点），机制为“协同绽放”——阶段可解码性提升使旧数据提供有效监督。
- **Phase III（SR > 75%）**：收益递减（+0 到 +15），机制为“饱和递减”——配置冲突成本 δ(SR) 随饱和增加。

### 核心理论定义
- **迁移阈值**：τ(T) = inf{SR : E[ΔSR | SR] > 0}，即使旧数据产生正期望增益的最小独立成功率。
- **阶段可解码性**：ρ_c(T;θ) = max_g Pr_{(s,o)}[g(φ_θ(s,o)) = z(s,o)]，衡量内部表征 φ_θ 对真实任务阶段 z 的可解码程度。
- **倒 U 增益律**（Theorem 2）：E[ΔSR | SR] = [κ(1 − SR) − δ(SR)] × 𝟙[SR > τ(T)]，其中 κ > 0 为任务相关参数，δ(SR) 为配置冲突成本。
- **信息量公式**：I_legacy = ρ·H̄_within − ε_dom，其中 H̄_within = η(1 − SR) 为剩余阶段内策略不确定性，ε_dom 为不可约配置不匹配。

### 阶段感知数据采集规则
1. 估计任务难度 H(T) = L(T)·log(1/ε(T))，据此预测迁移阈值 τ̂(T)。
2. 在新硬件数据上训练独立策略，测量成功率 SR₂(T)。
3. 若 SR₂(T) < τ̂(T)，继续采集新硬件数据；否则，用旧数据协同训练。

### 关键设计决策
- 协同训练等概率采样 Gen-1 与 Gen-2 数据（非按小时比例），以控制数据量比例变量。
- 策略不接收硬件代次标签，强制学习跨配置共享表征。
- 两代硬件使用相同归一化手臂动作表示，夹爪差异由配置特定底层控制器处理。

## 关键创新

1. **首次给出跨配置迁移的“阈值”而非“趋势”**：现有工作（如 Open X-Embodiment）只证明旧数据“可以”有用，本文用定理形式定义了迁移阈值 τ(T)，并证明在阈值以下期望梯度对齐非正、以上为正。这是从定性观察到定量判据的跃迁。

2. **倒 U 型增益律的统一解释框架**：将 Phase I 的表征真空、Phase II 的协同绽放、Phase III 的饱和递减纳入单一公式 E[ΔSR | SR] = [κ(1 − SR) − δ(SR)] × 𝟙[SR > τ(T)]，并用阶段可解码性作为底层机制。这为后续研究提供了可检验的理论预测。

3. **双向迁移的实证发现**：协同训练不仅提升 Gen-2 性能，还反向提升 Gen-1 花插入（50.0% → 78.3%）。这表明跨配置协同不是单向“源到目标”迁移，而是共享表征的互惠增强，对多代硬件共存的部署场景有直接指导意义。

## 实验与结果

实验在轮式人形平台（26 DoF）上进行，对比 Gen-1（单目相机 640×480，位置控制夹爪）与 Gen-2（鱼眼相机 1920×1536，混合力/位置夹爪）两代硬件。策略为 π_0.5 VLA 骨干的行为克隆微调，每条件 n = 60 次真实试验。

**表 2（Phase I，early Gen-2 数据）**：花插入 Gen-2 单训 10.0%，协同后仍为 10.0%（Δ = 0，p = n.s.），证实低基线时旧数据无收益；而同一任务 Gen-1 单训 50.0%，协同后 78.3%（Δ = +28.3，p = 0.002），展示双向迁移。

**表 3（Phase II，quality-refined Gen-2 数据）**：花插入单训 23.3%，协同 86.7%（Δ = +63.4 个百分点）；笔插入单训 71.7%，协同 98.3%（Δ = +26.6）。

**表 7（饱和效应）**：笔插入在 71.7% 基线时增益 +26.6，加入更多 Gen-2 数据达到 85.0% 独立基线后，同一任务仅增益 +8.3。

**表 5（held-out 移动浇水任务）**：0.5 h 新数据时 Δ = 0.0；1.5 h 时 Pick kettle Δ = +40.0（p = 1.5×10⁻⁶）、Water plant Δ = +38.3（p = 3.5×10⁻⁵）；8 h 时 Δ 降至 −1.7 与 +3.3（均不显著）。

| 任务 | 数据条件 | 单训 SR | 协同 SR | ΔSR | p 值 |
|------|----------|---------|---------|-----|------|
| 花插入 | early 4.3 h | 10.0% | 10.0% | 0.0 | n.s. |
| 花插入 | refined 15.6 h | 23.3% | 86.7% | +63.4 | 1.8×10⁻¹² |
| 笔插入 | refined 13.58 h | 71.7% | 98.3% | +26.6 | 4.0×10⁻⁵ |
| 笔插入 | early+refined 32.21 h | 85.0% | 93.3% | +8.3 | — |
| 浇水 Pick | 1.5 h | 51.7% | 91.7% | +40.0 | 1.5×10⁻⁶ |
| 浇水 Water | 1.5 h | 40.0% | 78.3% | +38.3 | 3.5×10⁻⁵ |

结果验证了三阶段模型：低基线无收益、中基线高增益、高基线收益递减。浇水任务复杂度估计 H(T) ≈ 44（接近笔插入的 42），预测约 1–2 小时新数据即可进入高增益区间，实际 1.5 h 数据验证了该预测。

## 边界与局限

- 实验仅覆盖单一轮式人形平台、两代硬件、一个 VLA 骨干（π_0.5）与有限操作任务，结论向其他形态（如四足、人形双臂）或模型家族的推广性未验证。
- τ(T) ≈ α + β·H(T) 的关系被作者明确视为“有初步证据支持的理论预测”，而非经验验证的缩放定律。
- 训练期间未直接记录逐源梯度对齐，图 4 的损失轨迹仅作为间接诊断，理论机制（梯度对齐解释）未被直接确立。
- 未测试除 π_0.5 之外的其他 VLA 骨干，也未覆盖移动底座之外的硬件配置差异类型（如自由度数量变化）。

## 工程启示

1. **先核对基线成功率**：在决定是否复用旧数据前，务必先在新硬件上训练独立策略并测量成功率。若低于 15–20%，旧数据协同训练大概率无效，应优先采集新数据；若在 20–75% 区间，旧数据收益最大；若高于 75%，收益有限且可能引入噪声级负迁移。

2. **任务复杂度是阈值预测的关键**：用 H(T) = L(T)·log(1/ε(T)) 估计任务难度（浇水任务 H ≈ 44，笔插入 H ≈ 42），可提前预判所需新数据量。浇水任务从 8 小时降至 1.5 小时的案例表明，该规则能显著节省采集成本。

3. **最容易踩坑的点**：数据质量不能绕过阈值——early 数据（4.3 h）即使协同训练也无收益，而 refined 数据（15.6 h）在相同任务上带来 +63.4 点增益。质量过滤（更严格操作员训练、逐轨迹过滤、更紧位姿容差）是进入 Phase II 的必要条件，而非充分条件。

4. **采样比例与标签设计**：等概率采样两代数据（而非按小时比例）且不给策略代次标签，是实现有效协同的关键设计。复现时应严格遵循，否则可能引入配置特定捷径。

5. **统计严谨性**：负 ΔSR 仅在统计显著时才视为负迁移证据（本文主实验中所有负增益均不显著）。评估时使用双侧 Fisher 精确检验与 Wilson 95% 置信区间，n = 60 次试验是获得可靠结论的最低要求。

## Overview
Robotic hardware evolves over time, but demonstration data is often tied to a specific sensor and actuator configuration. This raises a practical and underexplored question: when does legacy data begin to benefit an upgraded robot? We study this question on a wheeled humanoid platform across two hardware generations, where both the camera and gripper are changed while the overall morphology remains fixed. Contrary to the common assumption that more cross-configuration data is always helpful, we observe a grokking-like transition: legacy data remains ineffective until the upgraded configuration acquires a minimum level of task competence, after which co-training gains rise sharply before diminishing near saturation. We hypothesize that this task-dependent transition is governed by a transfer threshold and characterize the resulting three-phase pattern. Across real-robot manipulation tasks, we observe all three phases: no measurable benefit at low competence ($10.0\% \rightarrow 10.0\%$), a sharp gain after crossing the threshold ($23.3\% \rightarrow 86.7\%$ on flower insertion), and diminishing returns at high competence ($85.0\% \rightarrow 93.3\%$ on pen insertion). We provide a theoretical account based on gradient alignment and residual policy uncertainty, and derive a phase-aware rule for deciding when to collect more new-hardware data and when to reuse legacy demonstrations. We further validate this three-phase pattern on a mobile dual-arm watering task, with results consistent with our predictions.

## 参考
- https://arxiv.org/abs/2607.25593

## 개요

본 논문은 로봇 하드웨어 반복 이후, 구세대(legacy) 데모 데이터가 언제부터 신세대(Gen-2) 정책에 긍정적 전이 이득을 발생시키는지 연구한다. 저자는 휠형 휴머노이드 플랫폼에서 실제 실험을 통해 공동 훈련 이득과 단독 작업 성공률이 역 U자형 관계를 보인다는 것을 발견하고, 이를 바탕으로 3단계 모델과 작업 의존적 전이 임계값 판별 기준을 제안하여 데이터 수집 전략을 안내한다.

## 그것이 바꾼 것

이 작업이 실제로 바꾼 것은 "교차 구성 데이터 재사용"이라는 공학적 상식에 대한 인식이다. 이전에는 "더 많은 교차 구성 데이터가 항상 도움이 된다"는 가정이 업계에 널리 퍼져 있었지만, 본 논문은 실제 로봇 실험을 통해 목표 하드웨어 정책의 능력이 극도로 낮을 때(예: 꽃 삽입 단독 성공률 10.0%), 구세대 데이터 공동 훈련이 무익할 뿐만 아니라 완전히 무효할 수도 있음을 증명한다(10.0% → 10.0%). 이는 데이터 양 만능주의를 뒤집고, 문제를 "구세대 데이터를 사용할지 여부"에서 "어떤 능력 문턱에서 구세대 데이터가 긍정적 수익을 발생하기 시작하는가"로 정밀하게 전환한다.

더욱 중요한 것은 저자가 현상 설명에 머물지 않고 실행 가능한 공학적 판별 기준을 제시했다는 점이다: 작업 복잡도 추정(시야 길이와 공간 허용 오차)을 통해 전이 임계값을 예측하고, 신형 하드웨어 단독 성공률을 대리 지표로 사용하여 언제 새 데이터 수집을 중단하고 언제 구세대 데이터 공동 훈련을 시작할지 결정한다. 이로써 하드웨어 반복 시 데이터 관리는 경험적 시행착오에서 이론적 뒷받침이 있는 의사 결정 프로세스로 변화한다.

## 방법 분해

### 3단계 모델
공동 훈련 이득 ΔSR과 단독 성공률 SR은 역 U자형 관계를 보인다:
- **Phase I (SR < 15–20%)**: 구세대 데이터의 측정 가능한 이득 없음, 메커니즘은 "표현 진공" — 정책 내부 표현이 아직 작업 단계를 디코딩할 수 없으며, 구세대 데이터 기울기와 목표 기울기의 기대 정렬이 비양수.
- **Phase II (SR 20–75%)**: 이득이 크게 상승(+15 ~ +63 퍼센트 포인트), 메커니즘은 "협력 발현" — 단계 디코딩 가능성 향상으로 구세대 데이터가 효과적 감독 제공.
- **Phase III (SR > 75%)**: 이득 감소(+0 ~ +15), 메커니즘은 "포화 감소" — 구성 충돌 비용 δ(SR)이 포화에 따라 증가.

### 핵심 이론 정의
- **전이 임계값**: τ(T) = inf{SR : E[ΔSR | SR] > 0}, 즉 구세대 데이터가 양의 기대 이득을 발생시키는 최소 단독 성공률.
- **단계 디코딩 가능성**: ρ_c(T;θ) = max_g Pr_{(s,o)}[g(φ_θ(s,o)) = z(s,o)], 내부 표현 φ_θ가 실제 작업 단계 z를 디코딩할 수 있는 정도를 측정.
- **역 U자 이득 법칙** (Theorem 2): E[ΔSR | SR] = [κ(1 − SR) − δ(SR)] × 𝟙[SR > τ(T)], 여기서 κ > 0는 작업 관련 매개변수, δ(SR)는 구성 충돌 비용.
- **정보량 공식**: I_legacy = ρ·H̄_within − ε_dom, 여기서 H̄_within = η(1 − SR)는 잔여 단계 내 정책 불확실성, ε_dom은 환원 불가능한 구성 불일치.

### 단계 인식 데이터 수집 규칙
1. 작업 난이도 H(T) = L(T)·log(1/ε(T)) 추정, 이를 통해 전이 임계값 τ̂(T) 예측.
2. 신형 하드웨어 데이터로 단독 정책 훈련, 성공률 SR₂(T) 측정.
3. SR₂(T) < τ̂(T)이면 신형 하드웨어 데이터 계속 수집; 그렇지 않으면 구세대 데이터 공동 훈련 시작.

### 핵심 설계 결정
- 공동 훈련 시 Gen-1과 Gen-2 데이터를 등확률 샘플링(시간 비율 아님)하여 데이터량 비율 변수를 통제.
- 정책은 하드웨어 세대 레이블을 받지 않아 교차 구성 공유 표현 학습을 강제.
- 두 세대 하드웨어는 동일한 정규화된 팔 동작 표현을 사용하며, 그리퍼 차이는 구성 특정 하위 수준 컨트롤러가 처리.

## 핵심 혁신

1. **교차 구성 전이의 "추세"가 아닌 "임계값"을 최초로 제시**: 기존 연구(예: Open X-Embodiment)는 구세대 데이터가 "유용할 수 있다"는 것만 증명했지만, 본 논문은 정리 형태로 전이 임계값 τ(T)를 정의하고 임계값 이하에서는 기대 기울기 정렬이 비양수, 이상에서는 양수임을 증명한다. 이는 정성적 관찰에서 정량적 판별 기준으로의 도약이다.

2. **역 U자 이득 법칙의 통일된 설명 프레임워크**: Phase I의 표현 진공, Phase II의 협력 발현, Phase III의 포화 감소를 단일 공식 E[ΔSR | SR] = [κ(1 − SR) − δ(SR)] × 𝟙[SR > τ(T)]에 통합하고, 단계 디코딩 가능성을 하위 메커니즘으로 사용한다. 이는 후속 연구에 검증 가능한 이론적 예측을 제공한다.

3. **양방향 전이의 실증 발견**: 공동 훈련은 Gen-2 성능을 향상시킬 뿐만 아니라 Gen-1 꽃 삽입도 역방향으로 향상시킨다(50.0% → 78.3%). 이는 교차 구성 협력이 단방향 "소스에서 타깃으로" 전이가 아니라 공유 표현의 상호 이익 강화임을 시사하며, 다세대 하드웨어 공존 배포 시나리오에 직접적 지침을 제공한다.

## 실험 및 결과

실험은 휠형 휴머노이드 플랫폼(26 DoF)에서 수행되었으며, Gen-1(단안 카메라 640×480, 위치 제어 그리퍼)과 Gen-2(어안 카메라 1920×1536, 혼합 힘/위치 그리퍼) 두 세대 하드웨어를 비교한다. 정책은 π_0.5 VLA 백본의 행동 클로닝 미세 조정이며, 각 조건당 n = 60회 실제 시행.

**표 2 (Phase I, 초기 Gen-2 데이터)**: 꽃 삽입 Gen-2 단독 훈련 10.0%, 공동 훈련 후에도 10.0% (Δ = 0, p = n.s.), 낮은 기준선에서 구세대 데이터 무수익 확인; 동일 작업 Gen-1 단독 훈련 50.0%, 공동 훈련 후 78.3% (Δ = +28.3, p = 0.002), 양방향 전이 입증.

**표 3 (Phase II, 품질 개선 Gen-2 데이터)**: 꽃 삽입 단독 훈련 23.3%, 공동 훈련 86.7% (Δ = +63.4 퍼센트 포인트); 펜 삽입 단독 훈련 71.7%, 공동 훈련 98.3% (Δ = +26.6).

**표 7 (포화 효과)**: 펜 삽입 71.7% 기준선에서 이득 +26.6, 더 많은 Gen-2 데이터 추가로 85.0% 단독 기준선 도달 후 동일 작업 이득은 +8.3에 불과.

**표 5 (보류 이동 물주기 작업)**: 0.5 h 새 데이터 시 Δ = 0.0; 1.5 h 시 Pick kettle Δ = +40.0 (p = 1.5×10⁻⁶), Water plant Δ = +38.3 (p = 3.5×10⁻⁵); 8 h 시 Δ는 −1.7 및 +3.3으로 감소(모두 유의하지 않음).

| 작업 | 데이터 조건 | 단독 훈련 SR | 공동 훈련 SR | ΔSR | p 값 |
|------|----------|---------|---------|-----|------|
| 꽃 삽입 | 초기 4.3 h | 10.0% | 10.0% | 0.0 | n.s. |
| 꽃 삽입 | 개선 15.6 h | 23.3% | 86.7% | +63.4 | 1.8×10⁻¹² |
| 펜 삽입 | 개선 13.58 h | 71.7% | 98.3% | +26.6 | 4.0×10⁻⁵ |
| 펜 삽입 | 초기+개선 32.21 h | 85.0% | 93.3% | +8.3 | — |
| 물주기 Pick | 1.5 h | 51.7% | 91.7% | +40.0 | 1.5×10⁻⁶ |
| 물주기 Water | 1.5 h | 40.0% | 78.3% | +38.3 | 3.5×10⁻⁵ |

결과는 3단계 모델을 검증한다: 낮은 기준선에서는 무수익, 중간 기준선에서는 높은 이득, 높은 기준선에서는 이득 감소. 물주기 작업 복잡도 추정 H(T) ≈ 44(펜 삽입의 42에 근접)로, 약 1–2시간 새 데이터면 고이득 구간에 진입할 것으로 예측되었고, 실제 1.5 h 데이터가 이 예측을 검증했다.

## 경계 및 한계

- 실험은 단일 휠형 휴머노이드 플랫폼, 두 세대 하드웨어, 하나의 VLA 백본(π_0.5) 및 제한된 조작 작업만을 다루며, 다른 형태(예: 사족, 휴머노이드 양팔)나 모델 계열로의 일반화는 검증되지 않음.
- τ(T) ≈ α + β·H(T) 관계는 저자가 명시적으로 "초기 증거가 있는 이론적 예측"으로 간주하며, 경험적으로 검증된 스케일링 법칙이 아님.
- 훈련 중 소스별 기울기 정렬을 직접 기록하지 않았으며, 그림 4의 손실 궤적은 간접 진단으로만 사용되어 이론적 메커니즘(기울기 정렬 설명)이 직접 확립되지 않음.
- π_0.5 외 다른 VLA 백본을 테스트하지 않았으며, 이동 베이스 외 하드웨어 구성 차이 유형(예: 자유도 수 변화)도 다루지 않음.

## 공학적 시사점

1. **먼저 기준선 성공률 확인**: 구세대 데이터 재사용 여부를 결정하기 전에 반드시 신형 하드웨어에서 단독 정책을 훈련하고 성공률을 측정하라. 15–20% 미만이면 구세대 데이터 공동 훈련은 대체로 무효하므로 새 데이터 수집을 우선시해야 함; 20–75% 구간이면 구세대 데이터 이득이 최대; 75% 이상이면 이득이 제한적이고 노이즈 수준의 음성 전이가 발생할 수 있음.

2. **작업 복잡도가 임계값 예측의 핵심**: H(T) = L(T)·log(1/ε(T))로 작업 난이도를 추정(물주기 작업 H ≈ 44, 펜 삽입 H ≈ 42)하면 필요한 새 데이터량을 사전에 예측할 수 있음. 물주기 작업이 8시간에서 1.5시간으로 단축된 사례는 이 규칙이 수집 비용을 크게 절감할 수 있음을 보여줌.

3. **가장 함정에 빠지기 쉬운 지점**: 데이터 품질은 임계값을 우회할 수 없음 — 초기 데이터(4.3 h)는 공동 훈련에도 무수익이지만, 개선 데이터(15.6 h)는 동일 작업에서 +63.4 포인트 이득을 제공. 품질 필터링(더 엄격한 운영자 훈련, 궤적별 필터링, 더 좁은 포즈 허용 오차)은 Phase II 진입의 필요 조건이지 충분 조건이 아님.

4. **샘플링 비율 및 레이블 설계**: 두 세대 데이터를 등확률 샘플링(시간 비율 아님)하고 정책에 세대 레이블을 부여하지 않는 것이 효과적 협력의 핵심 설계. 재현 시 이를 엄격히 준수해야 하며, 그렇지 않으면 구성 특정 지름길이 유발될 수 있음.

5. **통계적 엄밀성**: 음의 ΔSR은 통계적으로 유의할 때만 음성 전이 증거로 간주(본 논문의 주요 실험에서 모든 음의 이득은 유의하지 않음). 평가 시 양측 Fisher 정확 검정과 Wilson 95% 신뢰 구간을 사용하며, n = 60회 시행은 신뢰할 수 있는 결론을 위한 최소 요건임.
