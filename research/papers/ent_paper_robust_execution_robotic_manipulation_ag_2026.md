---
$id: ent_paper_robust_execution_robotic_manipulation_ag_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning
  zh: Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning
  ko: Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning
summary:
  en: Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon execution, and compounding errors,
    which can easily destabilize execution and lead to task failure. Although recent vision-language-action (VLA) models exhibit
    strong generalization, they typically lack explicit mechanisms to assess execution stability and to recover when execution
    deviates from its nominal.
  zh: 本文提出一种名为智能体强化学习（Agentic Reinforcement Learning）的框架，通过冻结底层操作策略、训练一个高层智能体策略来选择执行模式（Execute/Retry/Repair/Reset），从而在不修改或重训底层策略的前提下提升机器人操作在扰动下的鲁棒性。核心贡献在于将执行鲁棒性问题从策略学习层面转移到执行管理层面，并设计了基于本体感觉与动作历史的局部/全局执行质量评估机制。
  ko: Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon execution, and compounding errors,
    which can easily destabilize execution and lead to task failure. Although recent vision-language-action (VLA) models exhibit
    strong generalization, they typically lack explicit mechanisms to assess execution stability and to recover when execution
    deviates from its nominal.
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
- robust
- execution
- robotic
- manipulation
- ag
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
  title: arXiv:2607.13818 Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Lea
  url: https://arxiv.org/abs/2607.13818
  date: '2026-07-15'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一种名为智能体强化学习（Agentic Reinforcement Learning）的框架，通过冻结底层操作策略、训练一个高层智能体策略来选择执行模式（Execute/Retry/Repair/Reset），从而在不修改或重训底层策略的前提下提升机器人操作在扰动下的鲁棒性。核心贡献在于将执行鲁棒性问题从策略学习层面转移到执行管理层面，并设计了基于本体感觉与动作历史的局部/全局执行质量评估机制。

## 它改变了什么

现有VLA与模仿学习策略的失败模式并非总是源于感知或规划错误，更多时候是执行过程中累积的微小偏差（如接触力异常、轨迹漂移）导致任务不可逆地失败。作者敏锐地指出，单纯扩大数据规模或引入VLM进行重规划，要么成本高昂且受长尾分布限制，要么引入额外延迟与指令分布偏移敏感性。本文真正改变的是将“鲁棒执行”从底层策略的泛化能力问题，重构为一个独立的、可学习的执行管理问题——即“何时继续、何时回退、何时重来”的决策问题。这一视角切换使得鲁棒性提升不再依赖底层策略的容量或数据覆盖，而是通过一个轻量级高层策略在推理时动态调控执行过程，从而在冻结底层策略的情况下获得显著的性能增益。

## 方法拆解

### 问题形式化
将执行过程建模为部分可观测马尔可夫决策过程（POMDP），元组为 ℳ = ⟨𝒮, 𝒜, P, R, γ⟩。智能体策略不直接生成控制命令，而是在离散动作空间 𝒜 = {Execute, Retry, Repair, Reset}（编码为 {0, 1, 2, 3}）中选择如何应用底层策略。

### 执行质量评估
- **局部质量**：基于滑动窗口 W 的末端执行器位置与动作，计算运动有效性 E = ‖p_t − p_{t−W+1}‖ / (1/W ∑‖â_k‖ + ε)，经饱和变换 E_norm = E/(E+c) 映射到 [0,1]；运动平滑度 S = 1/(1 + σ_v²/(μ_v² + ε))。聚合为 q_local(t) = β·q_local(t−1) + (1−β)·σ(k·(w₁E_norm + w₂S − b))，初始化为 1.0。
- **全局质量**：部署前为每任务收集 N = 50 条成功轨迹，按进度 t/T 归一化并离散化为 B = 10 个bin，构建阶段感知参考库。执行时与对应bin中 k = 5 个最近邻比较，q_global(t) = β·q_global(t−1) + (1−β)·exp(−α·d_t)，初始化为 1.0。
- **聚合**：q_agg(t) = λ·q_local(t) + (1−λ)·q_global(t)。

### 恢复机制
- **Retry**：回滚到最近 M = 15 步中 q_agg 最高的状态。
- **Repair**：回滚到最近 N = 30 步中无接触状态（MuJoCo 接触力阈值 τ = 5 N）里 q_agg 最高的状态。
- **Reset**：终止当前回合并从初始配置重新开始。
- 回滚使用操作空间控制器（OSC）驱动，夹爪保持张开，跟踪增量末端执行器位姿命令。恢复阶段信息不记录到执行历史，防止污染后续决策。

### 奖励与优化
任务成功 +1.0，失败 −1.0，时间惩罚 −0.02/步，Retry/Repair/Reset 成本分别为 −0.1/−0.3/−0.5。使用 PPO 优化，学习率 1×10⁻⁴，折扣 γ = 0.99，clip = 0.2，value coef = 0.1，entropy coef = 0.01。决策间隔 K = 5，历史长度 L = 20。Critic 可访问特权全局状态，actor 仅依赖本体感觉与底层动作。

## 关键创新

1. **执行模式抽象**：将鲁棒执行问题分解为“执行质量评估”与“恢复策略选择”两个子问题，通过离散动作空间 {Execute, Retry, Repair, Reset} 实现，避免了直接修改底层策略或引入外部重规划器。这一抽象使得方法可以即插即用地应用于任何冻结的底层策略（OpenVLA、π₀、Diffusion Policy 等）。
2. **无视觉、无特权的执行质量信号**：仅使用本体感觉与底层动作构造局部（运动有效性+平滑度）与全局（阶段感知参考库）质量分数，不依赖原始视觉或模拟器特权信息，显著降低了 sim-to-real 迁移难度，同时避免了视觉特征在扰动下的脆弱性。
3. **恢复机制设计**：Retry/Repair 不生成新动作，而是将机器人恢复到先前访问过的标称状态，从而“重新激活”底层策略的有效性。这种设计避免了生成式恢复带来的分布外动作风险，且通过固定回滚范围（M = 15、N = 30）保证了训练稳定性。

## 实验与结果

在 LIBERO 四个子集上，以 OpenVLA、π₀、π₀.₅、Diffusion Policy 为冻结底层策略，每回合注入一次持续 5 步的随机噪声扰动（δ = 3.0）。标准评估下，平均成功率提升最高达 13.7%（LIBERO-Long）；扰动评估下，平均成功率提升最高达 39.2%（LIBERO-Long）。具体关键数字如下：

| 评估模式 | 子集 | 最佳基线（w/o→w/） | 平均提升 |
|----------|------|---------------------|----------|
| 标准 | Spatial | π₀.₅: 97.4→96.6 | +5.1 |
| 标准 | Object | π₀.₅: 97.4→98.2 | +5.4 |
| 标准 | Goal | π₀.₅: 98.0→97.4 | +6.6 |
| 标准 | Long | π₀.₅: 92.4→95.2 | +13.7 |
| 扰动 | Spatial | π₀.₅: 80.0→90.4 | +25.7 |
| 扰动 | Object | π₀.₅: 64.0→92.8 | +27.4 |
| 扰动 | Goal | π₀.₅: 67.2→88.8 | +28.3 |
| 扰动 | Long | π₀.₅: 40.2→87.2 | +39.2 |

事件条件化分析显示，Reset 决策后 q_local 提升 +0.20 ± 0.08、q_global 提升 +0.22 ± 0.07，且 P(Δq_global > 0) = 0.95，验证了质量信号的有效性。恢复成本方面，Diffusion Policy 恢复次数增加最多（+2.1 ± 0.7），回合长度增加 15%；π₀.₅ 增加最少（+0.9 ± 0.3），回合长度增加 5%。

## 边界与局限

作者明确承认对更严重的执行退化和分布外场景恢复能力有限，且未在真实世界环境中验证。方法不处理底层策略本身的失败模式（如感知错误或规划错误），仅针对执行偏差。回滚范围 M 和 N 为固定值（15 和 30），学习这些参数会降低训练稳定性。智能体策略仅使用本体感觉与动作历史，未利用视觉信息，这可能限制了在需要视觉反馈才能判断恢复时机场景下的表现。论文未明确在极端扰动（如持续多回合扰动或 δ > 3.0）下的性能边界。

## 工程启示

复现时首先核对全局质量参考库的构建：需为每个任务收集 N = 50 条成功轨迹，且按进度 t/T 归一化并离散化为 B = 10 个bin，这一步骤对 q_global 的有效性至关重要，若成功轨迹数量不足或分布不均，可能导致全局质量信号失真。最容易踩坑的地方是恢复阶段信息污染：恢复过程中产生的状态与动作必须从执行历史中排除，否则会误导后续决策。建议在实现时显式维护一个“恢复标志”，在回滚期间暂停历史记录更新。另外，PPO 训练时 Critic 可访问特权状态而 actor 不能，这一不对称设计是价值估计稳定的关键，但需确保测试时 actor 完全脱离特权信息。对于下游团队，若底层策略更换，需重新收集成功轨迹构建参考库，且建议先在小规模任务上验证质量信号（q_local 与 q_global）的区分度，再投入完整训练。

## Overview
Robotic manipulation poses fundamental challenges due to uncertainty, long-horizon execution, and compounding errors, which can easily destabilize execution and lead to task failure. Although recent vision-language-action (VLA) models exhibit strong generalization, they typically lack explicit mechanisms to assess execution stability and to recover when execution deviates from its nominal behavior. In this paper, we propose: (1) two complementary metrics to assess execution quality at runtime, and (2) an agentic reinforcement learning framework that learns to restore effective execution through high-level decision-making rather than directly learning low-level actions. In this framework, an agentic policy reasons over recent execution history and selects among a small set of execution modes to regulate the execution process. Under execution degradation, it triggers appropriate recovery mechanisms to restore the robot to previously visited nominal states, enabling the task to continue. We evaluate the proposed method on the LIBERO benchmark, achieving up to a 13.7% improvement in success rate under standard settings and up to a 39.2% improvement under disturbance settings, demonstrating substantially enhanced execution robustness.

## 参考
- https://arxiv.org/abs/2607.13818

## 개요

본 논문은 에이전트 강화 학습(Agentic Reinforcement Learning)이라는 프레임워크를 제안한다. 이는 하위 수준의 조작 정책을 동결하고, 상위 수준의 에이전트 정책을 훈련하여 실행 모드(Execute/Retry/Repair/Reset)를 선택함으로써, 하위 정책을 수정하거나 재훈련하지 않고도 교란 하에서 로봇 조작의 견고성을 향상시킨다. 핵심 기여는 실행 견고성 문제를 정책 학습 수준에서 실행 관리 수준으로 전환하고, 고유 감각 및 동작 이력에 기반한 국소/전역 실행 품질 평가 메커니즘을 설계한 것이다.

## 그것이 바꾸는 것

기존 VLA 및 모방 학습 정책의 실패 모드는 항상 인식이나 계획 오류에서 비롯되는 것이 아니라, 실행 과정에서 누적되는 미세한 편차(예: 접촉력 이상, 궤적 드리프트)로 인해 작업이 되돌릴 수 없게 실패하는 경우가 더 많다. 저자들은 단순히 데이터 규모를 확대하거나 VLM을 도입하여 재계획하는 것이 비용이 높고 긴 꼬리 분포의 제한을 받거나, 추가 지연 시간과 명령 분포 이동에 대한 민감성을 유발한다는 점을 예리하게 지적한다. 본 논문이 실제로 바꾸는 것은 '견고한 실행'을 하위 정책의 일반화 능력 문제에서 독립적이고 학습 가능한 실행 관리 문제, 즉 '언제 계속할지, 언제 되돌릴지, 언제 다시 시작할지'의 의사 결정 문제로 재구성한 것이다. 이러한 관점의 전환은 견고성 향상이 더 이상 하위 정책의 용량이나 데이터 커버리지에 의존하지 않고, 경량 상위 정책이 추론 시 실행 과정을 동적으로 조절함으로써 하위 정책을 동결한 상태에서도 상당한 성능 향상을 얻을 수 있게 한다.

## 방법 분해

### 문제 정식화
실행 과정을 부분 관측 마르코프 결정 과정(POMDP)으로 모델링하며, 튜플은 ℳ = ⟨𝒮, 𝒜, P, R, γ⟩이다. 에이전트 정책은 제어 명령을 직접 생성하지 않고, 이산 행동 공간 𝒜 = {Execute, Retry, Repair, Reset}({0, 1, 2, 3}으로 인코딩)에서 하위 정책을 어떻게 적용할지 선택한다.

### 실행 품질 평가
- **국소 품질**: 슬라이딩 윈도우 W의 말단 효과기 위치와 동작을 기반으로 운동 효율성 E = ‖p_t − p_{t−W+1}‖ / (1/W ∑‖â_k‖ + ε)을 계산하고, 포화 변환 E_norm = E/(E+c)을 통해 [0,1]로 매핑한다. 운동 평활도 S = 1/(1 + σ_v²/(μ_v² + ε))이다. 이를 q_local(t) = β·q_local(t−1) + (1−β)·σ(k·(w₁E_norm + w₂S − b))로 집계하며, 초기값은 1.0이다.
- **전역 품질**: 배포 전 각 작업에 대해 N = 50개의 성공 궤적을 수집하고, 진행률 t/T로 정규화한 후 B = 10개의 bin으로 이산화하여 단계 인식 참조 라이브러리를 구축한다. 실행 시 해당 bin의 k = 5개의 최근접 이웃과 비교하여 q_global(t) = β·q_global(t−1) + (1−β)·exp(−α·d_t)를 계산하며, 초기값은 1.0이다.
- **집계**: q_agg(t) = λ·q_local(t) + (1−λ)·q_global(t).

### 복구 메커니즘
- **Retry**: 최근 M = 15단계 중 q_agg가 가장 높은 상태로 롤백한다.
- **Repair**: 최근 N = 30단계 중 무접촉 상태(MuJoCo 접촉력 임계값 τ = 5 N)에서 q_agg가 가장 높은 상태로 롤백한다.
- **Reset**: 현재 에피소드를 종료하고 초기 구성에서 다시 시작한다.
- 롤백은 운영 공간 제어기(OSC)로 구동되며, 그리퍼는 벌린 상태를 유지하고 증분 말단 효과기 자세 명령을 추적한다. 복구 단계 정보는 실행 이력에 기록되지 않아 이후 의사 결정을 오염시키지 않는다.

### 보상 및 최적화
작업 성공 시 +1.0, 실패 시 −1.0, 시간 패널티 −0.02/단계, Retry/Repair/Reset 비용은 각각 −0.1/−0.3/−0.5이다. PPO로 최적화하며, 학습률 1×10⁻⁴, 할인 γ = 0.99, clip = 0.2, value coef = 0.1, entropy coef = 0.01이다. 결정 간격 K = 5, 이력 길이 L = 20이다. Critic은 특권 전역 상태에 접근할 수 있지만, actor는 고유 감각과 하위 동작에만 의존한다.

## 핵심 혁신

1. **실행 모드 추상화**: 견고한 실행 문제를 '실행 품질 평가'와 '복구 정책 선택'이라는 두 하위 문제로 분해하고, 이산 행동 공간 {Execute, Retry, Repair, Reset}을 통해 구현하여 하위 정책을 직접 수정하거나 외부 재계획기를 도입하지 않아도 된다. 이러한 추상화는 방법을 동결된 모든 하위 정책(OpenVLA, π₀, Diffusion Policy 등)에 플러그 앤 플레이 방식으로 적용할 수 있게 한다.
2. **비전 및 특권 정보가 없는 실행 품질 신호**: 고유 감각과 하위 동작만을 사용하여 국소(운동 효율성+평활도) 및 전역(단계 인식 참조 라이브러리) 품질 점수를 구성하며, 원시 비전이나 시뮬레이터 특권 정보에 의존하지 않아 sim-to-real 전환 난이도를 크게 낮추고 교란 하에서 시각적 특징의 취약성을 피한다.
3. **복구 메커니즘 설계**: Retry/Repair는 새로운 동작을 생성하지 않고 로봇을 이전에 방문했던 명목 상태로 복원하여 하위 정책의 유효성을 '재활성화'한다. 이러한 설계는 생성적 복구가 가져오는 분포 외 동작 위험을 피하고, 고정된 롤백 범위(M = 15, N = 30)를 통해 훈련 안정성을 보장한다.

## 실험 및 결과

LIBERO의 네 하위 집합에서 OpenVLA, π₀, π₀.₅, Diffusion Policy를 동결 하위 정책으로 사용하고, 각 에피소드마다 5단계 동안 지속되는 무작위 잡음 교란(δ = 3.0)을 한 번 주입했다. 표준 평가에서 평균 성공률 향상은 최대 13.7%(LIBERO-Long)였고, 교란 평가에서 평균 성공률 향상은 최대 39.2%(LIBERO-Long)였다. 구체적인 핵심 수치는 다음과 같다:

| 평가 모드 | 하위 집합 | 최고 기준선(w/o→w/) | 평균 향상 |
|----------|------|---------------------|----------|
| 표준 | Spatial | π₀.₅: 97.4→96.6 | +5.1 |
| 표준 | Object | π₀.₅: 97.4→98.2 | +5.4 |
| 표준 | Goal | π₀.₅: 98.0→97.4 | +6.6 |
| 표준 | Long | π₀.₅: 92.4→95.2 | +13.7 |
| 교란 | Spatial | π₀.₅: 80.0→90.4 | +25.7 |
| 교란 | Object | π₀.₅: 64.0→92.8 | +27.4 |
| 교란 | Goal | π₀.₅: 67.2→88.8 | +28.3 |
| 교란 | Long | π₀.₅: 40.2→87.2 | +39.2 |

이벤트 조건 분석에 따르면 Reset 결정 후 q_local은 +0.20 ± 0.08, q_global은 +0.22 ± 0.07 향상되었고, P(Δq_global > 0) = 0.95로 품질 신호의 유효성이 검증되었다. 복구 비용 측면에서 Diffusion Policy의 복구 횟수 증가가 가장 컸고(+2.1 ± 0.7), 에피소드 길이는 15% 증가했다. π₀.₅는 증가가 가장 적었으며(+0.9 ± 0.3), 에피소드 길이는 5% 증가했다.

## 경계 및 한계

저자들은 더 심각한 실행 저하 및 분포 외 시나리오에 대한 복구 능력이 제한적이며 실제 환경에서 검증되지 않았음을 명시적으로 인정한다. 이 방법은 하위 정책 자체의 실패 모드(예: 인식 오류 또는 계획 오류)를 처리하지 않으며 실행 편차만 대상으로 한다. 롤백 범위 M과 N은 고정값(15 및 30)이며, 이러한 매개변수를 학습하면 훈련 안정성이 낮아진다. 에이전트 정책은 고유 감각과 동작 이력만 사용하고 시각 정보를 활용하지 않아, 복구 시점 판단에 시각적 피드백이 필요한 시나리오에서는 성능이 제한될 수 있다. 논문은 극단적 교란(예: 연속 다회 교란 또는 δ > 3.0) 하에서의 성능 경계를 명확히 제시하지 않는다.

## 공학적 시사점

재현 시 먼저 전역 품질 참조 라이브러리 구축을 확인해야 한다. 각 작업에 대해 N = 50개의 성공 궤적을 수집하고 진행률 t/T로 정규화한 후 B = 10개의 bin으로 이산화해야 하며, 이 단계는 q_global의 유효성에至关重要하다. 성공 궤적 수가 부족하거나 분포가 고르지 않으면 전역 품질 신호가 왜곡될 수 있다. 가장 함정에 빠지기 쉬운 부분은 복구 단계 정보 오염이다. 복구 과정에서 생성된 상태와 동작은 실행 이력에서 제외해야 하며, 그렇지 않으면 이후 의사 결정을 오도할 수 있다. 구현 시 '복구 플래그'를 명시적으로 유지하고 롤백 중 이력 기록 업데이트를 일시 중지하는 것을 권장한다. 또한 PPO 훈련 시 Critic은 특권 상태에 접근할 수 있지만 actor는 접근할 수 없는 비대칭 설계가 가치 추정 안정성의 핵심이지만, 테스트 시 actor가 특권 정보에서 완전히 분리되도록 해야 한다. 하위 팀의 경우 하위 정책을 교체하면 성공 궤적을 다시 수집하여 참조 라이브러리를 구축해야 하며, 먼저 소규모 작업에서 품질 신호(q_local 및 q_global)의 변별력을 검증한 후 전체 훈련에 투입하는 것이 좋다.
