---
$id: ent_paper_anybody_free_form_whole_body_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AnyBody: Free-Form Whole-Body Humanoid Control from Arbitrary Keypoint Guidance'
  zh: 'AnyBody: Free-Form Whole-Body Humanoid Control from Arbitrary Keypoint Guidance'
  ko: 'AnyBody: Free-Form Whole-Body Humanoid Control from Arbitrary Keypoint Guidance'
summary:
  en: We present AnyBody, a unified whole-body humanoid controller driven by an arbitrary subset of body keypoints chosen
    at deploy time. Prior physics-based trackers either rely on expensive full-body motion capture and error-prone trajectory
    retargeting, which bottleneck scalable data collection and policy learning, or decompose upper- and lower-body control
    into separate hierarchical.
  zh: AnyBody 是一个由部署时任意身体关键点子集驱动的统一全身人形控制器，由研究团队提出。其核心贡献在于学习一个共享的球形潜在运动表示，将稀疏关键点条件与全身控制统一到单一框架中，并支持通过潜在空间残差强化学习进行下游任务微调。该方法在
    Unitree G1 人形上实现了从单腕到全身多种关键点配置的零样本追踪，并显著提升了障碍物到达和腕部书写等下游任务的成功率。
  ko: We present AnyBody, a unified whole-body humanoid controller driven by an arbitrary subset of body keypoints chosen
    at deploy time. Prior physics-based trackers either rely on expensive full-body motion capture and error-prone trajectory
    retargeting, which bottleneck scalable data collection and policy learning, or decompose upper- and lower-body control
    into separate hierarchical.
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
- anybody
- free
- form
- whole
- body
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P039. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.29209 AnyBody: Free-Form Whole-Body Humanoid Control from Arbitrary Keypoint Guidance'
  url: https://arxiv.org/abs/2606.29209
  date: '2026-06-28'
  accessed_at: '2026-08-05'
---

## 概述

AnyBody 是一个由部署时任意身体关键点子集驱动的统一全身人形控制器，由研究团队提出。其核心贡献在于学习一个共享的球形潜在运动表示，将稀疏关键点条件与全身控制统一到单一框架中，并支持通过潜在空间残差强化学习进行下游任务微调。该方法在 Unitree G1 人形上实现了从单腕到全身多种关键点配置的零样本追踪，并显著提升了障碍物到达和腕部书写等下游任务的成功率。

## 它改变了什么

现有物理追踪器面临两难：要么依赖昂贵的全身动捕与易错的重定向流程，限制了数据规模与策略学习；要么将上下肢控制拆分为分离的层次结构，牺牲了全身协调。AnyBody 真正改变的是将“控制条件”从固定关节轨迹或完整骨架降维为“任意关键点子集”，从而绕过了重定向环节，让操作者能按任务与部署环境灵活选择控制点（从单腕到全身），同时保持全身行为的协调性。这实质上是把“跟随什么”与“如何协调全身”解耦，前者由用户在线指定，后者由预训练的运动先验承担。

## 方法拆解

### 三阶段训练框架
- **Stage 1（运动先验学习）**：在约 140 小时过滤后的 Bones-Seed 数据上训练特权教师追踪器，并在线蒸馏为确定性编码器-解码器。潜在变量 z 投影到单位球面 𝕊^{d_z−1}（d_z = 16），解码器 D 作为动力学感知的运动先验。损失 ℒ₁ = ‖D_ϕ(z, s^p) − π^T(s)‖²₂ + λ_sm(1 − cos(z_t, z_{t−1}))，其中 λ_sm = 0.1。
- **Stage 2（关键点条件化）**：冻结解码器 D，训练基于自注意力 transformer 的关键点编码器 E^kp。每个关键点 token 堆叠 0.5 秒窗口（15 帧，对称对数间隔）的历史与未来信息，缺失关键点通过注意力掩码 m 丢弃。损失 ℒ₂ = (1 − cos(ẑ^kp, sg[ẑ])) + λ_a‖D(ẑ^kp, s^p) − sg[D(ẑ, s^p)]‖²₂，λ_a = 0.05。掩码课程从全可见退火到 p_see = 0.4，并混合语义部署模式（仅躯干、仅手腕、仅脚踝等）。
- **Stage 3（下游微调）**：冻结编码器与解码器，学习浅层残差校正器 g_ξ（1 层 transformer，d_model = 64）。策略均值 ẑ_policy = norm(ẑ_enc + α·g_ξ(·))，α = 1.0。输出投影以 gain 0.01 的 Xavier 初始化，使 Δz ≈ 0 在 step 0，从而精确复现蒸馏行为，避免随机潜在探索导致的奖励崩溃。

### 关键设计决策
- 球形潜在空间（单位范数）提供有界且平滑的运动流形，便于余弦对齐与残差校正。
- 冻结解码器作为运动先验，确保任何关键点配置下的动作都符合物理可信的运动模式。
- 小增益初始化是 Stage 3 安全微调的核心，它保证了初始策略与预训练行为完全一致，再通过 PPO 逐步偏离。

## 关键创新

1. **统一任意关键点条件**：首次将稀疏关键点（1 到 5 个）与全身控制统一到单一潜在空间，无需重定向或任务特定分支。这使得从单腕遥操作到全身追踪的连续谱系成为可能，且部署时无需重新训练。
2. **三阶段蒸馏与残差微调范式**：将“运动先验学习”与“任务条件化”分离，再通过潜在空间残差 RL 微调。这种范式避免了直接在冻结解码器上随机探索导致的奖励崩溃，为预训练运动模型的安全下游适配提供了新思路。
3. **掩码课程与语义模式采样**：通过从全可见到稀疏掩码的渐进训练，并显式采样部署相关的关键点组合（如仅脚踝），使编码器学会从任意子集推断全身状态，而非记忆特定配置。

## 实验与结果

### 定量追踪性能（表 1）
| 命令模式 | # 点 | SR (%) ↑ | POI 位置误差 (cm) ↓ | POI 速度误差 ↓ |
|---|---|---|---|---|
| 全身 | 5 | 97.6 | 10.90 | 0.301 |
| 上肢（腕+躯干） | 3 | 94.8 | 9.48 | 0.284 |
| 仅腕 | 2 | 94.3 | 10.41 | 0.325 |
| 单腕（左/右） | 1 | 93.7 | 10.79 | 0.335 |
| 仅躯干 | 1 | 94.3 | 8.34 | 0.216 |
| 仅踝 | 2 | 95.4 | 13.39 | 0.351 |
| 关节命令（特权信息） | – | 99.3 | 8.31 | 0.225 |
| 关节命令（无特权信息） | – | 99.1 | 16.98 | 0.378 |

单腕追踪成功率高于 93%，平均 POI 位置误差在大多数掩码模式下保持约 10 cm。仅躯干模式误差最低（8.34 cm），表明躯干作为全局锚点对稳定性至关重要。

### 下游任务成功率（表 2）
| 任务 | 无 RL 微调成功率 | 有 RL 微调成功率 |
|---|---|---|
| 障碍物到达 - 开放 | 54.68% | 97.09% |
| 障碍物到达 - 屏障 | 10.49% | 96.04% |
| 障碍物到达 - 低净空 | 44.36% | 99.47% |
| 障碍物到达 - 容器 | 3.04% | 95.56% |
| 腕部书写 | 0.00% | 97.87% |

RL 微调带来显著提升，尤其在容器任务（3.04% → 95.56%）和腕部书写（0.00% → 97.87%）上，验证了残差微调对分布外命令轨迹的修复能力。

## 边界与局限

论文未明确列出所有局限，但可推断：控制器在训练语料覆盖不足的边缘运动（如极低到达、大规模空中手写）上仍会失败，需依赖下游 RL 微调修复。当前平台不包括灵巧手控制，无法执行精细操作。扩展到配备灵巧手的人形是未来方向。此外，所有实验均在 Unitree G1 上完成，跨平台泛化性未验证；真实世界长期稳定性与磨损未讨论。

## 工程启示

复现时优先核对 Stage 2 的掩码课程参数（p_see 从 1.0 退火到 0.4）与 Stage 3 的小增益初始化（gain 0.01），这两处是方法有效性的关键。最容易踩坑的是 Stage 3 的奖励设计：若未使用任务特定的非对称评论家或未设置成功阈值提前截断（如腕部书写 0.5 m 误差终止），训练可能不稳定。下游团队应首先验证预训练追踪器在目标关键点配置下的基线成功率，再决定是否需要 RL 微调；对于分布外命令（如空中书写），直接微调比调整追踪器更高效。硬件部署时注意控制频率 50 Hz 与仿真步长 0.005 s 的匹配，以及域随机化参数（摩擦 0.3–1.6、推力脉冲 ±0.5 m/s）对 sim-to-real 迁移的影响。

## Overview
We present AnyBody, a unified whole-body humanoid controller driven by an arbitrary subset of body keypoints chosen at deploy time. Prior physics-based trackers either rely on expensive full-body motion capture and error-prone trajectory retargeting, which bottleneck scalable data collection and policy learning, or decompose upper- and lower-body control into separate hierarchical representations, sacrificing the coordinated whole-body motions that loco-manipulation requires. We close this gap by learning a single latent motion representation that any keypoint subset can address. To achieve this, we first train a privileged teacher tracker on a large unstructured motion corpus and distill it online into a deterministic encoder-decoder student whose latent space is a unit sphere. We then train a transformer keypoint encoder that admits any subset of body keypoints through masked self-attention, aligning it to the privileged latent. Additionally, we treat the frozen decoder as a motor prior and specialize downstream tasks with a lightweight residual corrector in the latent space. We demonstrate the effectiveness of AnyBody by tracking large-scale human motions from arbitrary keypoint subsets, free-form control, flexibly teleoperating, and learning downstream behaviors including locomotion, in-air writing, and obstacle-reach.

## 参考
- https://arxiv.org/abs/2606.29209

## 개요

AnyBody는 연구팀이 제안한, 배포 시 임의의 신체 키포인트 부분집합에 의해 구동되는 통합 전신 휴머노이드 컨트롤러입니다. 핵심 기여는 공유된 구형 잠재 운동 표현을 학습하여 희소 키포인트 조건과 전신 제어를 단일 프레임워크로 통합하고, 잠재 공간 잔차 강화 학습을 통한 하위 작업 미세 조정을 지원한다는 점입니다. 이 방법은 Unitree G1 휴머노이드에서 단일 손목부터 전신까지 다양한 키포인트 구성의 제로샷 추적을 구현했으며, 장애물 도달 및 손목 쓰기와 같은 하위 작업의 성공률을 크게 향상시켰습니다.

## 무엇을 바꾸었는가

기존 물리 추적기는 두 가지 난관에 직면해 있습니다: 고가의 전신 모션 캡처와 오류가 쉬운 리타게팅 파이프라인에 의존하여 데이터 규모와 정책 학습을 제한하거나, 상·하지 제어를 분리된 계층 구조로 분할하여 전신 협응을 희생합니다. AnyBody가 실제로 바꾼 것은 "제어 조건"을 고정 관절 궤적이나 완전한 골격에서 "임의의 키포인트 부분집합"으로 축소하여 리타게팅 과정을 우회하고, 작업자(operators)가 작업과 배포 환경에 따라 제어 지점(단일 손목부터 전신까지)을 유연하게 선택하면서도 전신 행동의 협응을 유지할 수 있게 한 점입니다. 이는 본질적으로 "무엇을 따라갈 것인가"와 "전신을 어떻게 협응시킬 것인가"를 분리한 것으로, 전자는 사용자가 온라인으로 지정하고 후자는 사전 훈련된 운동 사전(motion prior)이 담당합니다.

## 방법 분해

### 3단계 훈련 프레임워크
- **Stage 1 (운동 사전 학습)**: 약 140시간의 필터링된 Bones-Seed 데이터에서 특권(privileged) 교사 추적기를 훈련하고, 온라인 증류를 통해 결정적 인코더-디코더로 변환합니다. 잠재 변수 z는 단위 구면 𝕊^{d_z−1} (d_z = 16)에 투영되며, 디코더 D는 역학 인지 운동 사전 역할을 합니다. 손실 ℒ₁ = ‖D_ϕ(z, s^p) − π^T(s)‖²₂ + λ_sm(1 − cos(z_t, z_{t−1})), 여기서 λ_sm = 0.1입니다.
- **Stage 2 (키포인트 조건화)**: 디코더 D를 동결하고, 자기 주의(self-attention) 트랜스포머 기반 키포인트 인코더 E^kp를 훈련합니다. 각 키포인트 토큰은 0.5초 창(15프레임, 대칭 로그 간격)의 과거 및 미래 정보를 쌓으며, 누락된 키포인트는 주의 마스크 m을 통해 버려집니다. 손실 ℒ₂ = (1 − cos(ẑ^kp, sg[ẑ])) + λ_a‖D(ẑ^kp, s^p) − sg[D(ẑ, s^p)]‖²₂, λ_a = 0.05. 마스크 커리큘럼은 전체 가시에서 p_see = 0.4로 어닐링되며, 의미론적 배포 모드(몸통만, 손목만, 발목만 등)를 혼합합니다.
- **Stage 3 (하위 작업 미세 조정)**: 인코더와 디코더를 동결하고, 얕은 잔차 보정기 g_ξ(1계층 트랜스포머, d_model = 64)를 학습합니다. 정책 평균 ẑ_policy = norm(ẑ_enc + α·g_ξ(·)), α = 1.0. 출력 투영은 gain 0.01의 Xavier 초기화를 사용하여 step 0에서 Δz ≈ 0이 되도록 하여 증류된 동작을 정확히 재현하고, 무작위 잠재 탐색으로 인한 보상 붕괴를 방지합니다.

### 핵심 설계 결정
- 구형 잠재 공간(단위 노름)은 경계가 있고 매끄러운 운동 다양체를 제공하여 코사인 정렬과 잔차 보정을 용이하게 합니다.
- 디코더를 운동 사전으로 동결하면 어떤 키포인트 구성에서도 동작이 물리적으로 타당한 운동 패턴을 따르도록 보장합니다.
- 작은 게인 초기화는 Stage 3 안전 미세 조정의 핵심으로, 초기 정책이 사전 훈련된 동작과 완전히 일치하도록 보장한 후 PPO를 통해 점진적으로 이탈합니다.

## 핵심 혁신

1. **임의 키포인트 조건의 통합**: 처음으로 희소 키포인트(1~5개)와 전신 제어를 단일 잠재 공간으로 통합하여 리타게팅이나 작업별 분기가 필요 없습니다. 이를 통해 단일 손목 원격 조작부터 전신 추적까지의 연속적인 스펙트럼이 가능해지며, 배포 시 재훈련이 필요 없습니다.
2. **3단계 증류 및 잔차 미세 조정 패러다임**: "운동 사전 학습"과 "작업 조건화"를 분리한 후, 잠재 공간 잔차 RL 미세 조정을 수행합니다. 이 패러다임은 동결된 디코더에서 직접 무작위 탐색으로 인한 보상 붕괴를 피하며, 사전 훈련된 운동 모델의 안전한 하위 작업 적응에 대한 새로운 접근을 제시합니다.
3. **마스크 커리큘럼 및 의미론적 모드 샘플링**: 전체 가시에서 희소 마스크로의 점진적 훈련과 배포 관련 키포인트 조합(예: 발목만)의 명시적 샘플링을 통해, 인코더가 특정 구성을 암기하는 대신 임의의 부분집합에서 전신 상태를 추론하는 법을 학습하게 합니다.

## 실험 및 결과

### 정량적 추적 성능 (표 1)
| 명령 모드 | # 포인트 | SR (%) ↑ | POI 위치 오차 (cm) ↓ | POI 속도 오차 ↓ |
|---|---|---|---|---|
| 전신 | 5 | 97.6 | 10.90 | 0.301 |
| 상지(손목+몸통) | 3 | 94.8 | 9.48 | 0.284 |
| 손목만 | 2 | 94.3 | 10.41 | 0.325 |
| 단일 손목(좌/우) | 1 | 93.7 | 10.79 | 0.335 |
| 몸통만 | 1 | 94.3 | 8.34 | 0.216 |
| 발목만 | 2 | 95.4 | 13.39 | 0.351 |
| 관절 명령(특권 정보) | – | 99.3 | 8.31 | 0.225 |
| 관절 명령(비특권 정보) | – | 99.1 | 16.98 | 0.378 |

단일 손목 추적 성공률은 93% 이상이며, 평균 POI 위치 오차는 대부분의 마스크 모드에서 약 10cm를 유지합니다. 몸통만 모드가 가장 낮은 오차(8.34cm)를 보여, 몸통이 전역 앵커로서 안정성에 중요함을 시사합니다.

### 하위 작업 성공률 (표 2)
| 작업 | RL 미세 조정 없음 성공률 | RL 미세 조정 있음 성공률 |
|---|---|---|
| 장애물 도달 - 개방 | 54.68% | 97.09% |
| 장애물 도달 - 장벽 | 10.49% | 96.04% |
| 장애물 도달 - 낮은 간격 | 44.36% | 99.47% |
| 장애물 도달 - 용기 | 3.04% | 95.56% |
| 손목 쓰기 | 0.00% | 97.87% |

RL 미세 조정은 특히 용기 작업(3.04% → 95.56%)과 손목 쓰기(0.00% → 97.87%)에서 큰 향상을 가져왔으며, 잔차 미세 조정이 분포 외 명령 궤적을 복구하는 능력을 검증합니다.

## 경계 및 한계

논문은 모든 한계를 명시적으로 나열하지는 않았지만, 훈련 말뭉치가 충분히 다루지 못하는 가장자리 운동(예: 매우 낮은 도달, 대규모 공중 손글씨)에서는 컨트롤러가 여전히 실패할 수 있으며, 하위 작업 RL 미세 조정에 의존해야 합니다. 현재 플랫폼은 정교한 손(덱스트러스 핸드) 제어를 포함하지 않아 정밀 조작을 수행할 수 없습니다. 정교한 손을 갖춘 휴머노이드로의 확장이 향후 방향입니다. 또한 모든 실험은 Unitree G1에서 수행되었으며, 교차 플랫폼 일반화는 검증되지 않았습니다. 실제 세계의 장기 안정성과 마모는 논의되지 않았습니다.

## 엔지니어링 시사점

재현 시 Stage 2의 마스크 커리큘럼 매개변수(p_see를 1.0에서 0.4로 어닐링)와 Stage 3의 작은 게인 초기화(gain 0.01)를 우선적으로 확인해야 하며, 이 두 곳이 방법의 유효성을 결정하는 핵심입니다. 가장 실수하기 쉬운 부분은 Stage 3의 보상 설계입니다: 작업별 비대칭 비평가(asymmetric critic)를 사용하지 않거나 성공 임계값에 의한 조기 종료(예: 손목 쓰기 0.5m 오차 종료)를 설정하지 않으면 훈련이 불안정해질 수 있습니다. 하위 작업 팀은 먼저 사전 훈련된 추적기가 목표 키포인트 구성에서의 기준 성공률을 검증한 후 RL 미세 조정 여부를 결정해야 합니다. 분포 외 명령(예: 공중 쓰기)의 경우 추적기를 조정하는 것보다 직접 미세 조정하는 것이 더 효율적입니다. 하드웨어 배포 시 제어 주파수 50Hz와 시뮬레이션 스텝 크기 0.005s의 일치, 그리고 도메인 무작위화 매개변수(마찰 0.3–1.6, 추력 펄스 ±0.5 m/s)가 sim-to-real 전이에 미치는 영향을 확인해야 합니다.
