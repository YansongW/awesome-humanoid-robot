---
$id: ent_paper_cross_embodiment_transfer_behavior_align_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Cross-Embodiment Transfer via Behavior-Aligned Representations
  zh: Cross-Embodiment Transfer via Behavior-Aligned Representations
  ko: Cross-Embodiment Transfer via Behavior-Aligned Representations
summary:
  en: Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across
    a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging.
    In this work, we study the role of using behavior-aligned representations (e.g., object bounding boxes, language motions,
    end-effector traces of robot motion).
  zh: 本文提出通过行为对齐表示（behavior-aligned representations）隐式对齐异构机器人数据集，以提升跨本体迁移性能。作者在 RoboCasa-X 模拟基准和真实机器人上验证了该方法，发现组合表示（如边界框、语言运动、末端执行器轨迹）能显著提升迁移效果，且推理时无需预测表示。核心贡献在于提供了一种无需显式对齐观测或动作空间的可扩展跨本体迁移方案。
  ko: Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across
    a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging.
    In this work, we study the role of using behavior-aligned representations (e.g., object bounding boxes, language motions,
    end-effector traces of robot motion).
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
- cross
- embodiment
- transfer
- behavior
- align
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
  title: arXiv:2607.27549 Cross-Embodiment Transfer via Behavior-Aligned Representations
  url: https://arxiv.org/abs/2607.27549
  date: '2026-07-30'
  accessed_at: '2026-08-05'
---

## 概述

本文提出通过行为对齐表示（behavior-aligned representations）隐式对齐异构机器人数据集，以提升跨本体迁移性能。作者在 RoboCasa-X 模拟基准和真实机器人上验证了该方法，发现组合表示（如边界框、语言运动、末端执行器轨迹）能显著提升迁移效果，且推理时无需预测表示。核心贡献在于提供了一种无需显式对齐观测或动作空间的可扩展跨本体迁移方案。

## 它改变了什么

跨本体迁移的核心障碍在于不同机器人本体的观测空间和动作空间存在本质差异，且数据覆盖不足。现有方法要么需要大量人工对齐工作（如相机位姿），要么在训练时依赖部署机器人的先验信息，难以规模化。本文真正改变的是：将跨本体对齐从显式的空间对齐转变为隐式的行为对齐——通过预测与本体无关的中间表示（如边界框、语言运动、末端执行器轨迹）来桥接异构数据，从而避免了繁琐的人工标注和先验依赖。这一转变使得跨本体迁移可以更自然地扩展到新本体，且无需在训练时知道部署机器人的具体信息。

## 方法拆解

### 形式化框架
- 定义机器人本体空间 ℛ，每个本体 r 有观测空间 𝒪^r 和动作空间 𝒜^r，不假设空间间对齐。
- 学习策略 π_θ(a|o,l)，将观测 o 和语言指令 l 映射到动作 a。
- 行为克隆损失：ℒ_BC(θ) = 𝔼_{(o,a,l)∼𝒟}[ℓ(π_θ(·|o,l), a)]。
- 每个观测 o_i 标注表示元组 z_i = (z_i^(1), …, z_i^(K))，策略条件于表示子集 z̃ ⊆ {z^(1), …, z^(K)}。
- 总损失：ℒ_total(θ) = 𝔼_{(o,z,a,l)∼𝒟, z̃∼p_rep(z)}[ℓ(π_θ(·|o,l,z̃), a) + ℓ_aux]，其中 ℓ_aux = Σ_{k=1}^K λ_k ℓ_rep^(k)(π_θ(·|o,l), z^(k))。

### 表示选择
- **边界框（Bounding Boxes）**：当前图像中应操作对象的边界框，用 VLM 场景描述和 Grounding DINO 标注。
- **语言运动（Language Motions）**：描述机器人下一步动作的语言，如“向左下移动”，通过阈值化本体感知状态变化获得。
- **末端执行器轨迹（End Effector Traces）**：未来运动中末端执行器在图像中的 2D 位置序列，用预训练模型检测。

### 架构与训练
- 使用 MiniVLA 架构，从预训练 VLM 开始，无机器人预训练。
- 观测空间为单个第三人称相机视图，所有损失权重 λ_k = 1。
- 表示集成方式：No Reps（仅动作）、Single Rep（单个表示）、ECoT（顺序预测所有表示）、Joint Reps（单模型训练所有表示）。
- 推理时仅预测动作（不预测表示），以加速推理且不显著影响性能。
- 动作空间统一为 delta 笛卡尔末端执行器位姿控制，所有模拟机器人共享同一控制器。

## 关键创新

1. **隐式行为对齐替代显式空间对齐**：通过预测与本体无关的中间表示，避免了显式对齐观测或动作空间所需的大量人工努力，使得跨本体迁移更可扩展。
2. **表示的可组合性与灵活性**：支持多种表示（边界框、语言运动、末端执行器轨迹）的单独或组合使用，且推理时无需预测表示，兼顾性能与效率。
3. **无动作预训练的有效性**：仅预训练表示预测（无动作）也能带来迁移提升，表明行为对齐表示本身携带跨本体可迁移的信息，而非仅依赖动作预测。

## 实验与结果

### 模拟基准 RoboCasa-X
- 源机器人：IIWA、Kinova3、UR5e；目标机器人：Panda、Jaco、Panda-OG。
- 数据集：XP-900（每任务 900 演示）和 XP-3K（每任务 3000 演示）；目标机器人每任务 50 个人类演示。
- 评估：每次 100 次 rollout，报告三个检查点中的最高成功率。

### 关键结果
| 实验设置 | 结果 |
|---------|------|
| 表示集成（Q1） | 每个表示单独使用均提升迁移；末端执行器轨迹最有效；组合表示在 Panda 和 Jaco 上优于单独使用，但 Panda-OG 上不如仅用轨迹 |
| 跨本体扩展（Q2） | 表示在仅目标数据时 +5%，XP-900 时 +15%，XP-3K 时 +19%（除 Turn On Sink Faucet 外） |
| Turn On Sink Faucet 例外 | 仅目标数据 +22%，XP-900 时 +4%，XP-3K 时 +1% |
| 无动作迁移（Q4） | 无动作预训练加表示总体提升 14%，比完整先前数据（含动作但无表示）提升 11% |
| 真实世界 | Joint Reps 总体增加 28%；含跨本体数据时比仅目标数据帮助更大（+8%）；无表示时跨本体数据仅 +7% |

### 结果含义
- 行为对齐表示在跨本体数据规模增大时提升更显著，表明其能有效利用异构数据。
- 例外任务（Turn On Sink Faucet）表明表示的效果可能受任务类型影响。
- 真实世界验证了模拟结论，但提升幅度受任务变化减少影响。

## 边界与局限

- 设置涉及本体间显著对齐（模拟中每个本体有相同相机位姿、场景和任务分布），隔离了跨本体迁移问题，但使研究的表示更对齐；未来可研究更少结构化、更大错位的迁移。
- 研究的表示并非穷尽，且偏向对象中心操作任务；其他行为对齐表示可能对特定任务和本体更有益。
- 未研究不同错位水平对表示促进迁移能力的影响；未探索更广泛的行为对齐表示。
- 论文未明确：真实世界实验的任务变化减少对结果的影响程度，以及不同控制频率对迁移的具体影响。

## 工程启示

- **复现核对**：先确认模拟环境中的相机位姿、场景和任务分布是否与原文一致（RoboCasa-X 中每个本体相同），这直接影响表示对齐的有效性。
- **表示选择**：末端执行器轨迹是最有效的单一表示，但若目标本体末端执行器在先前数据中未见（如 Panda-OG），组合表示可能不如单独使用轨迹，需根据目标本体特性调整。
- **推理效率**：推理时仅预测动作（不预测表示）可显著加速且不显著影响性能，工程实现时应默认采用此策略。
- **数据规模**：跨本体数据规模从 XP-900 增至 XP-3K 时，表示带来的提升从 +15% 增至 +19%，建议优先扩充跨本体数据而非仅依赖目标数据。
- **易踩坑**：Turn On Sink Faucet 任务中表示提升有限（+1%），表明表示对涉及精细操作或非对象中心任务可能效果不佳，需评估任务类型与表示的匹配度。

## Overview
Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging. In this work, we study the role of using behavior-aligned representations (e.g., object bounding boxes, language motions, end-effector traces of robot motion) in vision-language-action (VLA) models to promote cross-embodiment transfer. We hypothesize that by possessing invariances across embodiments while being predictive of robot actions, these representations can help unify large-scale cross-embodiment data to enhance transfer. To assess our hypothesis, we develop a simulation-based benchmark designed to assess transfer with diverse cross-embodiment data to new embodiments. Using this benchmark, we compare different representations and ways of incorporating them. We identify that end-effector traces can be particularly beneficial for transfer, representations are generally more useful with larger prior datasets, and can be used to benefit from action-free data. We also demonstrate that they can enhance sim-to-real cross-embodiment transfer, improving task completion progress of real robot policies pre-trained on simulation data by 28%. We provide videos of our evaluations at our website: https://ajaysridhar.com/barx/.

## 参考
- https://arxiv.org/abs/2607.27549

## 개요

본 논문은 행동 정렬 표현(behavior-aligned representations)을 통해 이기종 로봇 데이터셋을 암시적으로 정렬하여 교차 본체 전이 성능을 향상시키는 방법을 제안한다. 저자는 RoboCasa-X 시뮬레이션 벤치마크와 실제 로봇에서 이 방법을 검증했으며, 결합 표현(경계 상자, 언어 운동, 말단 실행기 궤적 등)이 전이 효과를 크게 향상시키고 추론 시 표현 예측이 필요 없음을 발견했다. 핵심 기여는 관측 또는 행동 공간의 명시적 정렬 없이 확장 가능한 교차 본체 전이 방식을 제공한 것이다.

## 무엇을 바꾸었는가

교차 본체 전이의 핵심 장애물은 서로 다른 로봇 본체의 관측 공간과 행동 공간이 본질적으로 다르고 데이터 커버리지가 부족하다는 점이다. 기존 방법은 많은 수동 정렬 작업(예: 카메라 포즈)이 필요하거나 훈련 시 배포 로봇의 사전 정보에 의존하여 확장이 어렵다. 본 논문이 실제로 바꾼 것은 교차 본체 정렬을 명시적 공간 정렬에서 암시적 행동 정렬로 전환한 것이다—본체와 무관한 중간 표현(경계 상자, 언어 운동, 말단 실행기 궤적 등)을 예측하여 이기종 데이터를 연결함으로써 번거로운 수동 주석과 사전 의존을 피했다. 이러한 전환은 교차 본체 전이가 새 본체로 더 자연스럽게 확장될 수 있게 하며, 훈련 시 배포 로봇의 구체적 정보를 알 필요가 없다.

## 방법 분해

### 형식적 프레임워크
- 로봇 본체 공간 ℛ을 정의하고, 각 본체 r은 관측 공간 𝒪^r과 행동 공간 𝒜^r을 가지며 공간 간 정렬을 가정하지 않는다.
- 정책 π_θ(a|o,l)을 학습하여 관측 o와 언어 명령 l을 행동 a에 매핑한다.
- 행동 복제 손실: ℒ_BC(θ) = 𝔼_{(o,a,l)∼𝒟}[ℓ(π_θ(·|o,l), a)].
- 각 관측 o_i는 표현 튜플 z_i = (z_i^(1), …, z_i^(K))로 주석되며, 정책은 표현 부분집합 z̃ ⊆ {z^(1), …, z^(K)}에 조건화된다.
- 총 손실: ℒ_total(θ) = 𝔼_{(o,z,a,l)∼𝒟, z̃∼p_rep(z)}[ℓ(π_θ(·|o,l,z̃), a) + ℓ_aux], 여기서 ℓ_aux = Σ_{k=1}^K λ_k ℓ_rep^(k)(π_θ(·|o,l), z^(k)).

### 표현 선택
- **경계 상자(Bounding Boxes)**: 현재 이미지에서 조작 대상 객체의 경계 상자. VLM 장면 설명과 Grounding DINO로 주석.
- **언어 운동(Language Motions)**: 로봇의 다음 동작을 설명하는 언어(예: "왼쪽 아래로 이동"). 본체 인식 상태 변화를 임계값 처리하여 획득.
- **말단 실행기 궤적(End Effector Traces)**: 향후 운동에서 말단 실행기의 이미지 내 2D 위치 시퀀스. 사전 훈련된 모델로 감지.

### 아키텍처 및 훈련
- MiniVLA 아키텍처 사용, 사전 훈련된 VLM에서 시작하며 로봇 사전 훈련 없음.
- 관측 공간은 단일 3인칭 카메라 뷰이며 모든 손실 가중치 λ_k = 1.
- 표현 통합 방식: No Reps(행동만), Single Rep(단일 표현), ECoT(모든 표현 순차 예측), Joint Reps(단일 모델로 모든 표현 훈련).
- 추론 시 행동만 예측(표현 미예측)하여 추론을 가속화하고 성능에 큰 영향을 주지 않음.
- 행동 공간은 델타 데카르트 말단 실행기 포즈 제어로 통일되며 모든 시뮬레이션 로봇이 동일한 컨트롤러를 공유.

## 핵심 혁신

1. **명시적 공간 정렬 대신 암시적 행동 정렬**: 본체와 무관한 중간 표현을 예측함으로써 관측 또는 행동 공간의 명시적 정렬에 필요한 대규모 수동 작업을 피하고 교차 본체 전이를 더 확장 가능하게 만든다.
2. **표현의 조합성과 유연성**: 여러 표현(경계 상자, 언어 운동, 말단 실행기 궤적)을 단독 또는 조합으로 지원하며 추론 시 표현 예측이 필요 없어 성능과 효율을 모두 고려한다.
3. **행동 없는 사전 훈련의 효과성**: 표현 예측만 사전 훈련(행동 없음)해도 전이 향상이 나타나며, 이는 행동 정렬 표현 자체가 교차 본체 전이 가능한 정보를 담고 있음을 시사한다.

## 실험 및 결과

### 시뮬레이션 벤치마크 RoboCasa-X
- 소스 로봇: IIWA, Kinova3, UR5e; 타겟 로봇: Panda, Jaco, Panda-OG.
- 데이터셋: XP-900(작업당 900 데모) 및 XP-3K(작업당 3000 데모); 타겟 로봇은 작업당 50개의 인간 데모.
- 평가: 각 100회 롤아웃, 세 체크포인트 중 최고 성공률 보고.

### 핵심 결과
| 실험 설정 | 결과 |
|---------|------|
| 표현 통합(Q1) | 각 표현 단독 사용 모두 전이 향상; 말단 실행기 궤적이 가장 효과적; 결합 표현은 Panda와 Jaco에서 단독보다 우수하지만 Panda-OG에서는 궤적 단독보다 낮음 |
| 교차 본체 확장(Q2) | 표현은 타겟 데이터만 있을 때 +5%, XP-900에서 +15%, XP-3K에서 +19%(Turn On Sink Faucet 제외) |
| Turn On Sink Faucet 예외 | 타겟 데이터만 +22%, XP-900에서 +4%, XP-3K에서 +1% |
| 행동 없는 전이(Q4) | 행동 없는 사전 훈련과 표현이 전체적으로 14% 향상, 완전한 이전 데이터(행동 포함, 표현 없음)보다 11% 더 높음 |
| 실제 세계 | Joint Reps가 전체적으로 28% 증가; 교차 본체 데이터 포함 시 타겟 데이터만보다 더 큰 도움(+8%); 표현 없이 교차 본체 데이터는 +7%에 불과 |

### 결과 의미
- 행동 정렬 표현은 교차 본체 데이터 규모가 커질수록 향상이 더 두드러지며 이기종 데이터를 효과적으로 활용할 수 있음을 보여준다.
- 예외 작업(Turn On Sink Faucet)은 표현 효과가 작업 유형에 따라 달라질 수 있음을 시사한다.
- 실제 세계에서 시뮬레이션 결론을 검증했지만 향상 폭은 작업 변화 감소의 영향을 받는다.

## 경계 및 한계

- 설정은 본체 간 상당한 정렬을 포함한다(시뮬레이션에서 각 본체가 동일한 카메라 포즈, 장면, 작업 분포를 가짐). 이는 교차 본체 전이 문제를 분리하지만 연구된 표현이 더 정렬되게 만든다; 향후 덜 구조화되고 더 큰 정렬 오차가 있는 전이를 연구할 수 있다.
- 연구된 표현은 완전하지 않으며 객체 중심 조작 작업에 치우쳐 있다; 다른 행동 정렬 표현이 특정 작업과 본체에 더 유용할 수 있다.
- 서로 다른 정렬 오차 수준이 표현의 전이 촉진 능력에 미치는 영향은 연구되지 않았다; 더 넓은 행동 정렬 표현도 탐구되지 않았다.
- 논문은 실제 세계 실험에서 작업 변화 감소가 결과에 미치는 영향 정도와 서로 다른 제어 주파수가 전이에 미치는 구체적 영향을 명확히 하지 않았다.

## 공학적 시사점

- **재현 확인**: 먼저 시뮬레이션 환경의 카메라 포즈, 장면, 작업 분포가 원문과 일치하는지 확인해야 한다(RoboCasa-X에서 각 본체가 동일). 이는 표현 정렬의 효과에 직접적인 영향을 미친다.
- **표현 선택**: 말단 실행기 궤적이 가장 효과적인 단일 표현이지만, 타겟 본체의 말단 실행기가 이전 데이터에 없으면(예: Panda-OG) 결합 표현이 궤적 단독보다 나을 수 없으므로 타겟 본체 특성에 따라 조정해야 한다.
- **추론 효율**: 추론 시 행동만 예측(표현 미예측)하면 크게 가속화되고 성능에 큰 영향을 주지 않으므로 공학 구현 시 기본적으로 이 전략을 채택해야 한다.
- **데이터 규모**: 교차 본체 데이터 규모가 XP-900에서 XP-3K로 증가할 때 표현의 향상이 +15%에서 +19%로 증가하므로 타겟 데이터에만 의존하기보다 교차 본체 데이터 확장을 우선 권장한다.
- **주의할 점**: Turn On Sink Faucet 작업에서 표현 향상이 제한적(+1%)이며, 이는 표현이 정밀 조작이나 비객체 중심 작업에서 효과가 낮을 수 있음을 나타내므로 작업 유형과 표현의 적합성을 평가해야 한다.
