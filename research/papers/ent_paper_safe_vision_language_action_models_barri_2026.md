---
$id: ent_paper_safe_vision_language_action_models_barri_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Safe Vision Language Action Models via Barrier Enhanced Flow Matching
  zh: Safe Vision Language Action Models via Barrier Enhanced Flow Matching
  ko: Safe Vision Language Action Models via Barrier Enhanced Flow Matching
summary:
  en: This article presents a modular inference framework that integrates Flow Matching generative models with formal Control
    Barrier Function (CBF) safety guarantees. Unlike existing methods that apply external safety filters to a model's final
    output, our approach modifies the Flow Matching denoising process within the model to inherently generate safe trajectories.
    By employing a smooth.
  zh: 本文提出 barrier-enhanced flow matching（CBF-FM）框架，将控制屏障函数（CBF）安全保证直接集成到流匹配（Flow Matching）生成式视觉-语言-动作（VLA）模型的去噪过程中，而非事后过滤。该方法通过
    Log-Sum-Exp 平滑聚合屏障函数与解析可解的 CBF-QP 修正项，在不重训练、无需安全数据集的前提下，同时提升轨迹安全性、平滑性与计算效率，并在仿真与两类硬件平台上验证。
  ko: This article presents a modular inference framework that integrates Flow Matching generative models with formal Control
    Barrier Function (CBF) safety guarantees. Unlike existing methods that apply external safety filters to a model's final
    output, our approach modifies the Flow Matching denoising process within the model to inherently generate safe trajectories.
    By employing a smooth.
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
- safe
- vision
- language
- action
- models
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
  title: arXiv:2607.29569 Safe Vision Language Action Models via Barrier Enhanced Flow Matching
  url: https://arxiv.org/abs/2607.29569
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 barrier-enhanced flow matching（CBF-FM）框架，将控制屏障函数（CBF）安全保证直接集成到流匹配（Flow Matching）生成式视觉-语言-动作（VLA）模型的去噪过程中，而非事后过滤。该方法通过 Log-Sum-Exp 平滑聚合屏障函数与解析可解的 CBF-QP 修正项，在不重训练、无需安全数据集的前提下，同时提升轨迹安全性、平滑性与计算效率，并在仿真与两类硬件平台上验证。

## 它改变了什么

现有生成式安全滤波器（如 SafeDiffuser、SafeFM）在 VLA 动作块上存在根本性缺陷：SafeDiffuser 因在去噪全程施加硬约束导致 69% 的“陷阱”失败率（轨迹卡死），SafeFM 虽部分缓解但计算时间高达 14.14 秒且轨迹曲率与加速度惩罚显著。这些方法本质上是“事后打补丁”——在完整生成轨迹后过滤，既破坏流匹配的分布一致性，又引入分布外样本。本文真正改变的是安全干预的时机与粒度：将 CBF 约束嵌入去噪 ODE 的每一步，使安全成为生成过程的固有属性而非外部附加条件。这意味着安全保证不再依赖对最终输出的修正，而是从噪声到轨迹的演化路径上逐点满足屏障条件，从而在数学上保证终端状态的安全性（定理 4），同时保持预训练模型的语义意图不变。

## 方法拆解

### 核心机制：去噪过程中的 CBF 修正
- 在流匹配 ODE（公式 11）中引入修正项 δ_s，构建 CBF-QP（公式 12），其解析解为：
  δ_s = ReLU(-αh(z) - ∇_z h(z) v_θ(τ,z)) / ||∇_z h||² ∇_z h
  其中 h 为屏障函数，α 为衰减率，v_θ 为预训练速度场，τ 为去噪时间步。

### 平滑聚合：Log-Sum-Exp 替代 min 算子
- 对动作块内多状态屏障值，用 LSE 聚合（公式 8）替代非光滑 min 算子，近似误差有界（定理 2）：
  min_i h(q_i) - ln(H)/κ ≤ h(z˘) ≤ min_i h(q_i)
  其中 H 为状态数，κ 为平滑参数。这保证 QP 可微且梯度信息完整。

### 阶段式干预：仅后期去噪
- 仅在 τ ∈ [τ_s, 1] 施加安全过滤，因早期中间状态类似无结构噪声，缺乏物理意义。安全保证（定理 4）：
  若 τ_s ≤ h_0/M（h_0 初始屏障值，M 最坏衰减率），则 h(ψ(z,1.0)) ≥ (h_0 - Mτ_s)e^{-α(1-τ_s)} > 0。

### 扩展约束：速度限制与平滑性
- QP（公式 19）加入稀疏矩阵 D 表示的速度限制（盒约束 ±0.1 rad/s）与加权平滑项（参数 λ），确保实时可解（使用 qpth 求解器）。

### 屏障函数实例
- 墙屏障：基于平面法向量 n 和偏移 d（公式 20-21）；球形屏障：基于中心 p_center 和半径 r（公式 22-23）。均为纯运动学函数，无需动力学模型。

## 关键创新

1. **生成过程内嵌安全而非后置过滤**：现有方法在完整轨迹上施加约束，本文在 ODE 积分过程中逐点修正，从根源避免分布外样本。这是安全性与生成质量解耦的关键——安全修正不改变流匹配的边缘分布，仅调整采样路径。
2. **LSE 平滑聚合 + 解析 QP 解**：用 LSE 替代 min 算子使屏障函数全局光滑，且 QP 具有闭式解（公式 13），避免了 SafeDiffuser 的迭代优化陷阱（69% 失败率）和 SafeFM 的额外引导需求，计算时间从 14.41 秒降至 10.65 秒。
3. **理论完备的安全保证**：定理 4 给出终端屏障值的指数衰减下界，推论 1 证明在良态屏障与紧致配置空间下 2-Wasserstein 距离有界。这为安全关键部署提供了可验证的数学承诺，而非仅凭实验观察。

## 实验与结果

### Maze2D 仿真（100 次试验，qpth 求解器）
| 方法 | BS1 (≥0) | BS2 (≥0) | Trap (%) ↓ | Time (s) ↓ | κ ↓ | Accel. ↓ |
|---|---|---|---|---|---|---|
| FM (no safety) | -0.762 | -0.938 | 0 | 1.38 | 97.7 ± 1.5 | 151.3 ± 4.8 |
| SafeDiffuser | -0.003 | -0.003 | 69 | 14.41 | 68.2 ± 90.3 | 124.5 ± 34.2 |
| SafeFM | -0.3031 | 0.003 | 12 | 14.14 | 75.9 ± 2.9 | 195.9 ± 22.0 |
| CBF-FM (Ours) | 0.109 | 0.046 | 0 | 10.65 | 7.2 ± 0.4 | 3.3 ± 0.1 |

CBF-FM 是唯一同时满足 BS1、BS2 非负的方法，且 Trap 率为 0，曲率与加速度比 SafeFM 降低一个数量级（由表内数值 75.9→7.2、195.9→3.3 计算）。

### 硬件操作实验（每种方法 ≥20 次）
| 平台 | 方法 | Safety (%) | Success (%) |
|---|---|---|---|
| SO-101 (5-DoF) | No Filter | 15.0 | 75.0 |
| SO-101 | E2E-CBF | 68.2 | 68.2 |
| SO-101 | CBF-FM | 100.0 | 77.4 |
| QArm (4-DoF) | No Filter | 0.00 | 100.0 |
| QArm | E2E-CBF | 70.0 | 75.0 |
| QArm | CBF-FM | 100.0 | 100.0 |

CBF-FM 在两类平台上均实现 100% 安全率，且成功率不低于无过滤基线（SO-101 上 77.4% vs 75.0%，QArm 上 100% vs 100%）。注意成功判定不惩罚碰撞（Remark 4），故安全率与成功率独立。

## 边界与局限

- 未处理高度动态障碍物（列为未来工作），当前屏障函数为静态或准静态场景设计。
- 未覆盖超越空间碰撞的抽象安全描述（如语义安全、任务级约束）。
- 屏障函数虽为运动学形式，但定理 4 的保证依赖最坏衰减率 M 的估计，实际中 M 需人工设定，过保守或过激进均影响性能。
- 推论 1 的分布偏移分析依赖“屏障函数良态、配置空间紧致且远离奇异”假设，硬件实验中通过将物体严格置于无奇异灵巧工作空间来满足，但真实场景未必可保证。
- 计算开销仅声称“实时可解”，未提供具体量化数字（论文未明确）。

## 工程启示

- **复现核对点**：先确认屏障函数梯度 ∇_z h 在配置空间内非零（推论 1 前提），否则 QP 解退化。硬件实验中所有物体需严格置于机械臂无奇异工作空间内。
- **参数敏感性**：τ_s（后期去噪起始点）与 α（衰减率）是核心超参。τ_s 过大则安全保证减弱（定理 4 中 h_0/M 约束），过小则早期噪声阶段被过度约束。建议从 τ_s = 0.5 起步，α 按屏障值衰减速度调节。
- **最易踩坑处**：LSE 平滑参数 κ 影响近似误差界（ln(H)/κ），κ 过小导致屏障函数过平滑、安全裕度虚高；速度限制的盒约束（±0.1 rad/s）需与 VLA 帧率匹配，Δt 与物理采样时间不一致会导致约束失效。
- **下游集成**：推理滤波器基于开源 π₀ 模型（LeRobot/PyTorch）实现，修改去噪循环即可，无需重训练。若下游任务需多障碍或动态障碍，需自行扩展屏障函数组合（当前仅支持墙与球）。
- **性能预期**：仿真中计算时间 10.65 秒仍高于无过滤基线（1.38 秒），若部署在实时控制回路需进一步优化 QP 求解或降低过滤频率。

## Overview
This article presents a modular inference framework that integrates Flow Matching generative models with formal Control Barrier Function (CBF) safety guarantees. Unlike existing methods that apply external safety filters to a model's final output, our approach modifies the Flow Matching denoising process within the model to inherently generate safe trajectories. By employing a smooth Log-Sum-Exponential aggregate barrier, we enforce safety over entire action chunks. This aggregate barrier ensures a minimal increase in computational overhead and does not alter the semantic intent of the model. We show that, within the proposed framework, the 2-Wasserstein distance between the generated distribution and the target distribution remains bounded. Our method eliminates the need for safety-specific datasets or costly model retraining, providing a versatile solution for safe inference. We validate the approach on two robotic manipulation platforms and a 2D navigation benchmark, verifying that our framework achieves reliable safety without degrading the success rate of the model.

## 参考
- https://arxiv.org/abs/2607.29569

## 개요

본 논문은 barrier-enhanced flow matching(CBF-FM) 프레임워크를 제안하며, 제어 장벽 함수(CBF) 안전 보장을 사후 필터링이 아닌 플로우 매칭(Flow Matching) 기반 생성형 비전-언어-행동(VLA) 모델의 디노이징 과정에 직접 통합한다. 이 방법은 Log-Sum-Exp 평활 집계와 해석적으로 풀 수 있는 CBF-QP 수정항을 통해, 재학습이나 안전 데이터셋 없이도 궤적 안전성, 평활성, 계산 효율성을 동시에 향상시키며, 시뮬레이션과 두 가지 하드웨어 플랫폼에서 검증한다.

## 무엇을 바꾸는가

기존 생성형 안전 필터(예: SafeDiffuser, SafeFM)는 VLA 행동 블록에서 근본적인 결함을 가진다: SafeDiffuser는 디노이징 전 과정에 경성 제약을 가해 69%의 "트랩" 실패율(궤적 정체)을 유발하며, SafeFM은 부분적으로 완화하지만 계산 시간이 14.14초에 달하고 궤적 곡률과 가속도 패널티가 크다. 이러한 방법들은 본질적으로 "사후 패치" 방식이다—완전히 생성된 궤적을 필터링하여 플로우 매칭의 분포 일관성을 파괴하고 분포 외 샘플을 유발한다. 본 논문이 실제로 바꾸는 것은 안전 개입의 시점과 세분성이다: CBF 제약을 디노이징 ODE의 각 단계에 내장하여 안전을 생성 과정의 고유 속성으로 만들고 외부 부가 조건이 아닌 것으로 만든다. 이는 안전 보장이 최종 출력 수정에 의존하지 않고, 노이즈에서 궤적으로의 진화 경로상 각 지점에서 장벽 조건을 충족함을 의미하며, 수학적으로 종단 상태의 안전성을 보장하고(정리 4), 사전 훈련된 모델의 의미적 의도를 유지한다.

## 방법 분해

### 핵심 메커니즘: 디노이징 과정에서의 CBF 수정
- 플로우 매칭 ODE(식 11)에 수정항 δ_s를 도입하여 CBF-QP(식 12)를 구성하며, 그 해석적 해는 다음과 같다:
  δ_s = ReLU(-αh(z) - ∇_z h(z) v_θ(τ,z)) / ||∇_z h||² ∇_z h
  여기서 h는 장벽 함수, α는 감쇠율, v_θ는 사전 훈련된 속도장, τ는 디노이징 시간 단계이다.

### 평활 집계: Log-Sum-Exp로 min 연산자 대체
- 행동 블록 내 다중 상태 장벽 값에 대해 LSE 집계(식 8)를 사용하여 비평활 min 연산자를 대체하며, 근사 오차는 유계이다(정리 2):
  min_i h(q_i) - ln(H)/κ ≤ h(z˘) ≤ min_i h(q_i)
  여기서 H는 상태 수, κ는 평활 파라미터이다. 이는 QP가 미분 가능하고 기울기 정보가 완전함을 보장한다.

### 단계적 개입: 후기 디노이징만 적용
- τ ∈ [τ_s, 1]에서만 안전 필터링을 적용하는데, 초기 중간 상태는 구조 없는 노이즈와 유사하여 물리적 의미가 부족하기 때문이다. 안전 보장(정리 4):
  τ_s ≤ h_0/M(h_0 초기 장벽 값, M 최악 감쇠율)이면, h(ψ(z,1.0)) ≥ (h_0 - Mτ_s)e^{-α(1-τ_s)} > 0.

### 확장 제약: 속도 제한 및 평활성
- QP(식 19)에 희소 행렬 D로 표현된 속도 제한(박스 제약 ±0.1 rad/s)과 가중 평활 항(파라미터 λ)을 추가하여 실시간 해석 가능성을 보장한다(qpth 솔버 사용).

### 장벽 함수 예시
- 벽 장벽: 평면 법선 벡터 n과 오프셋 d 기반(식 20-21); 구형 장벽: 중심 p_center와 반경 r 기반(식 22-23). 모두 순수 운동학적 함수로 동역학 모델이 필요 없다.

## 핵심 혁신

1. **생성 과정 내장 안전이 아닌 사후 필터링**: 기존 방법은 완전한 궤적에 제약을 가하지만, 본 논문은 ODE 적분 과정에서 각 지점을 수정하여 분포 외 샘플을 원천적으로 방지한다. 이는 안전성과 생성 품질의 분리를 가능하게 하는 핵심이다—안전 수정은 플로우 매칭의 주변 분포를 변경하지 않고 샘플링 경로만 조정한다.
2. **LSE 평활 집계 + 해석적 QP 해**: LSE로 min 연산자를 대체하여 장벽 함수를 전역적으로 평활하게 만들고, QP는 폐쇄형 해(식 13)를 가지므로 SafeDiffuser의 반복 최적화 트랩(69% 실패율)과 SafeFM의 추가 유도 요구를 피하며, 계산 시간이 14.41초에서 10.65초로 단축된다.
3. **이론적으로 완전한 안전 보장**: 정리 4는 종단 장벽 값의 지수 감쇠 하한을 제공하고, 추론 1은 양호한 장벽 함수와 컴팩트 구성 공간에서 2-Wasserstein 거리가 유계임을 증명한다. 이는 실험 관찰에만 의존하지 않고 검증 가능한 수학적 약속을 안전 중요 배포에 제공한다.

## 실험 및 결과

### Maze2D 시뮬레이션(100회 시행, qpth 솔버)
| 방법 | BS1 (≥0) | BS2 (≥0) | Trap (%) ↓ | Time (s) ↓ | κ ↓ | Accel. ↓ |
|---|---|---|---|---|---|---|
| FM (안전 없음) | -0.762 | -0.938 | 0 | 1.38 | 97.7 ± 1.5 | 151.3 ± 4.8 |
| SafeDiffuser | -0.003 | -0.003 | 69 | 14.41 | 68.2 ± 90.3 | 124.5 ± 34.2 |
| SafeFM | -0.3031 | 0.003 | 12 | 14.14 | 75.9 ± 2.9 | 195.9 ± 22.0 |
| CBF-FM (Ours) | 0.109 | 0.046 | 0 | 10.65 | 7.2 ± 0.4 | 3.3 ± 0.1 |

CBF-FM은 BS1, BS2를 동시에 비음수로 만족하는 유일한 방법이며, Trap 비율이 0이고 곡률과 가속도가 SafeFM보다 한 자릿수 낮다(표 값 75.9→7.2, 195.9→3.3으로 계산).

### 하드웨어 조작 실험(각 방법 ≥20회)
| 플랫폼 | 방법 | Safety (%) | Success (%) |
|---|---|---|---|
| SO-101 (5-DoF) | 필터 없음 | 15.0 | 75.0 |
| SO-101 | E2E-CBF | 68.2 | 68.2 |
| SO-101 | CBF-FM | 100.0 | 77.4 |
| QArm (4-DoF) | 필터 없음 | 0.00 | 100.0 |
| QArm | E2E-CBF | 70.0 | 75.0 |
| QArm | CBF-FM | 100.0 | 100.0 |

CBF-FM은 두 플랫폼 모두에서 100% 안전율을 달성하며, 성공률은 필터 없는 기준선 이상이다(SO-101에서 77.4% vs 75.0%, QArm에서 100% vs 100%). 성공 판정은 충돌을 처벌하지 않으므로(Remark 4), 안전율과 성공률은 독립적이다.

## 경계 및 한계

- 고도로 동적인 장애물은 처리하지 않음(향후 작업으로 분류), 현재 장벽 함수는 정적 또는 준정적 시나리오용으로 설계됨.
- 공간 충돌을 넘어서는 추상적 안전 설명(예: 의미적 안전, 작업 수준 제약)은 다루지 않음.
- 장벽 함수는 운동학적 형태이지만, 정리 4의 보장은 최악 감쇠율 M의 추정에 의존하며, 실제로 M은 수동 설정이 필요하고 과보수적이거나 과격하면 성능에 영향을 미친다.
- 추론 1의 분포 이동 분석은 "장벽 함수가 양호하고, 구성 공간이 컴팩트하며, 특이점에서 멀다"는 가정에 의존하며, 하드웨어 실험에서는 물체를 특이점 없는 영리한 작업 공간에 엄격히 배치하여 충족하지만, 실제 시나리오에서는 보장할 수 없다.
- 계산 오버헤드는 "실시간 해석 가능"이라고만 주장하며 구체적인 수치를 제공하지 않는다(논문에 명시되지 않음).

## 공학적 시사점

- **재현 체크포인트**: 먼저 장벽 함수 기울기 ∇_z h가 구성 공간에서 0이 아닌지 확인(추론 1 전제), 그렇지 않으면 QP 해가 퇴화한다. 하드웨어 실험에서 모든 물체는 로봇 팔의 특이점 없는 작업 공간에 엄격히 배치해야 한다.
- **파라미터 민감도**: τ_s(후기 디노이징 시작점)와 α(감쇠율)는 핵심 하이퍼파라미터이다. τ_s가 너무 크면 안전 보장이 약해지고(정리 4의 h_0/M 제약), 너무 작으면 초기 노이즈 단계가 과도하게 제약된다. τ_s = 0.5에서 시작하고 α는 장벽 값 감쇠 속도에 따라 조정할 것을 권장한다.
- **가장 함정에 빠지기 쉬운 부분**: LSE 평활 파라미터 κ는 근사 오차 경계(ln(H)/κ)에 영향을 미치며, κ가 너무 작으면 장벽 함수가 과평활되어 안전 마진이 허위로 높아진다; 속도 제한의 박스 제약(±0.1 rad/s)은 VLA 프레임 속도와 일치해야 하며, Δt와 물리적 샘플링 시간이 불일치하면 제약이 무효화된다.
- **하위 통합**: 추론 필터는 오픈소스 π₀ 모델(LeRobot/PyTorch) 기반으로 구현되며, 디노이징 루프만 수정하면 되고 재학습이 필요 없다. 하위 작업에 다중 장애물이나 동적 장애물이 필요하면 장벽 함수 조합을 직접 확장해야 한다(현재는 벽과 구만 지원).
- **성능 기대**: 시뮬레이션에서 계산 시간 10.65초는 여전히 필터 없는 기준선(1.38초)보다 높으며, 실시간 제어 루프에 배포하려면 QP 해석을 더 최적화하거나 필터링 빈도를 낮춰야 한다.
