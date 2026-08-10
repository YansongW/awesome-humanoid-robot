---
$id: ent_paper_latent_dynamics_planning_pixels_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Latent Dynamics for Planning from Pixels
  zh: Learning Latent Dynamics for Planning from Pixels
  ko: Learning Latent Dynamics for Planning from Pixels
summary:
  en: Planning has been very successful for control tasks with known environment dynamics. To leverage planning in unknown
    environments, the agent needs to learn the dynamics from interactions with the world. However, learning dynamics models
    that are accurate enough for planning has been a long-standing challenge, especially in image-based domains. We propose
    the Deep Planning Network (PlaNet), a.
  zh: PlaNet 是一个纯模型驱动的强化学习智能体，从像素观测中学习循环状态空间模型（RSSM），并在潜在空间中用交叉熵方法（CEM）进行规划。它在 DeepMind Control Suite 的六个连续控制任务上，以 1000 个回合的样本量达到或超过无模型基线（D4PG）在
    100000 个回合下的性能，数据效率提升 40 至 500 倍以上。核心贡献在于证明了随机与确定性混合的潜在动力学模型结合在线规划，是样本高效控制的一条可行路径。
  ko: Planning has been very successful for control tasks with known environment dynamics. To leverage planning in unknown
    environments, the agent needs to learn the dynamics from interactions with the world. However, learning dynamics models
    that are accurate enough for planning has been a long-standing challenge, especially in image-based domains. We propose
    the Deep Planning Network (PlaNet), a.
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
- latent
- dynamics
- planning
- pixels
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P063. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: arXiv:1811.04551 Learning Latent Dynamics for Planning from Pixels
  url: https://arxiv.org/abs/1811.04551
  date: '2018-11-12'
  accessed_at: '2026-08-05'
---

## 概述

PlaNet 是一个纯模型驱动的强化学习智能体，从像素观测中学习循环状态空间模型（RSSM），并在潜在空间中用交叉熵方法（CEM）进行规划。它在 DeepMind Control Suite 的六个连续控制任务上，以 1000 个回合的样本量达到或超过无模型基线（D4PG）在 100000 个回合下的性能，数据效率提升 40 至 500 倍以上。核心贡献在于证明了随机与确定性混合的潜在动力学模型结合在线规划，是样本高效控制的一条可行路径。

## 它改变了什么

在 PlaNet 之前，从像素直接做模型预测控制（MPC）几乎不可行：视频预测模型要么是确定性的（无法处理多模态未来），要么是纯随机的（训练不稳定、长期预测坍缩）。强化学习社区的主流共识是，模型误差会在多步规划中累积，因此不如直接学策略或价值函数。PlaNet 真正改变的是这个前提——它用 RSSM 的确定性路径承载跨时间步的记忆，用随机路径捕捉观测中的不确定性，从而让潜在空间中的 12 步规划（H=12）变得足够可靠，甚至能超越用真实模拟器状态做 CEM 规划的性能（如 cheetah 662 vs 656，walker 951 vs 994 接近）。

另一个被改变的认知是“规划必须用真实状态”。PlaNet 证明，从 64×64 像素、5 位深度（bit depth 降至 5）的观测中学习到的 30 维潜在状态，足以支撑开环 50 步的像素级预测（图 9），并且潜在空间中的状态估计（位置、速度）在远超规划视界的距离上仍然可预测（图 10）。这意味着，模型学习的不是简单的帧间插值，而是底层物理量的压缩表征。此外，PlaNet 的多任务实验（单个智能体不被告知任务身份，同时学习六个任务）也挑战了“每个任务需要单独建模”的默认假设，尽管学习速度会变慢。

## 方法拆解

### 模型架构：RSSM（Recurrent State-Space Model）
- 由两条路径组成：
  - **确定性路径**：GRU（200 个单元）接收上一时刻的确定性状态 h_{t-1} 和随机状态 s_{t-1}，输出 h_t。这允许模型跨时间步记住信息，避免纯随机模型的信息丢失。
  - **随机路径**：从 30 维对角高斯分布中采样 s_t，均值和标准差由 h_t 和观测编码预测。随机性对学习至关重要，因为任务从智能体视角看是部分可观测的（初始状态未知），且噪声为规划目标增加安全边际，产生更鲁棒的动作序列。
- 观测编码器/解码器：卷积/反卷积网络（来自 Ha & Schmidhuber 2018），其他函数为两个全连接层（大小 200，ReLU 激活）。

### 训练目标
- 联合优化重建损失（图像重建）和 KL 散度（正则化潜在分布）。KL 项不相对重建项缩放，但将散度损失裁剪到 3 个自由 nats 以下。
- 关键设计：**latent overshooting**（潜在过冲）作为多步预测的正则化器，在训练时对潜在状态进行多步展开并计算 KL。但最终 agent 未使用它，因为 RSSM 本身已足够好（消融显示它略微降低 RSSM 性能，但显著提升纯随机 DRNN）。

### 规划算法：CEM（交叉熵方法）
- 参数：规划视界 H=12、优化迭代 I=10、候选样本 J=1000、拟合最优 K=100。
- 流程：
  1. 从因子化信念 q(a_{t:t+H}) ← Normal(0, I) 初始化。
  2. 迭代 I 次：采样 J 个动作序列，用学习到的奖励模型评估期望回报，取 K 个最优序列重新拟合高斯分布（更新均值和标准差）。
  3. 返回第一个动作均值 μ_t 作为执行动作。
- 动作噪声 ε ~ Normal(0, 0.3) 用于数据收集，每 C=100 个更新步收集一个额外回合，从 S=5 个随机动作种子回合开始。

### 多任务学习
- 单个智能体在所有六个任务上训练，不被告知任务身份，需从图像观测推断。动作空间用未使用元素填充以兼容，算法调整为每 C 个更新步收集每个任务的一个回合，使用与主实验相同的超参数。

## 关键创新

1. **随机与确定性的混合状态空间**：这是 RSSM 的核心创新。纯随机模型（stochastic-only）无法解决任何任务，纯确定性模型（deterministic-only）在大多数任务上表现更差。RSSM 的确定性路径提供长期记忆，随机路径处理观测不确定性，两者结合使得潜在动力学既稳定又具有表达力。这一设计直接解决了视频预测中“确定性模型无法生成多模态未来，随机模型难以训练”的两难。

2. **潜在空间中的在线规划（latent planning）**：PlaNet 不学习策略或价值函数，而是用 CEM 在潜在空间中搜索动作序列。与随机射击（random shooting，从 1000 个序列中选最优）相比，CEM 的迭代优化（I=10）在所有任务上提升性能。与随机收集数据（random collection）相比，在线规划驱动的数据收集对所有任务有帮助，对 cartpole、finger 和 walker 任务是必要的。这表明，规划不仅用于决策，还用于引导数据分布，形成“探索-建模-规划”的正反馈。

3. **数据效率的跨越式提升**：PlaNet 用 1000 个回合达到 D4PG 用 100000 个回合的性能，数据效率提升 40（reacher）到 500+（cheetah）倍。这一数量级的差距不是渐进改进，而是改变了“从像素学习控制需要多少数据”的预期，为真实机器人应用（数据获取成本高）打开了可能性。

## 实验与结果

### 任务与基线
- 任务：Cartpole Swing Up、Reacher Easy、Cheetah Run、Finger Spin、Cup Catch、Walker Walk。
- 基线：A3C（本体感觉模态，100000 回合）、D4PG（像素模态，100000 回合）、PlaNet（像素模态，1000 回合）、CEM + 真实模拟器（模拟器状态，0 回合，作为性能上界估计）。

### 关键结果（表 1，5 个种子和 10 条轨迹的平均最终性能）

| 任务 | A3C | D4PG | PlaNet (ours) | CEM + true simulator | 数据效率增益（PlaNet vs D4PG） |
|------|-----|------|---------------|----------------------|-------------------------------|
| Cartpole Swing Up | 558 | 862 | 821 | 850 | 250 |
| Reacher Easy | 285 | 967 | 832 | 964 | 40 |
| Cheetah Run | 214 | 524 | 662 | 656 | 500+ |
| Finger Spin | 129 | 985 | 700 | 825 | 300 |
| Cup Catch | 105 | 980 | 930 | 993 | 100 |
| Walker Walk | 311 | 968 | 951 | 994 | 90 |

- PlaNet 在 cheetah 上超过 D4PG（662 vs 524），在 walker 上接近（951 vs 968），在 cup 上接近（930 vs 980）。在 finger 上落后（700 vs 985），但数据效率增益仍达 300 倍。
- 与 CEM + true simulator 对比：PlaNet 在 cheetah 上超过（662 vs 656），在 walker 上接近（951 vs 994），说明潜在模型的质量已接近真实模拟器。

### 消融实验
- **模型组件**：纯随机模型无法解决任何任务；纯确定性模型在大多数任务上更差；RSSM 在所有任务上最佳（finger 任务上确定性模型略好）。
- **规划设计**：PlaNet 优于随机收集（random collection）和随机射击（random shooting），证明在线规划和 CEM 迭代优化的必要性。
- **潜在过冲**：显著提升 DRNN 性能，但略微降低 RSSM 性能（图 7）。
- **激活函数**：ELU 帮助纯随机模型，但 RSSM 对激活函数选择鲁棒（图 8）。
- **规划视界**：视界长度 6 不够，过长则因搜索空间增大而性能下降；cheetah 环境最佳视界接近 8 步（图 11，规划性能范围 132 到 837）。

### 多任务学习
- 单个智能体解决所有任务，但学习速度比单独训练的智能体慢（图 5、图 6）。

## 边界与局限

- **未使用 latent overshooting**：最终 agent 未使用该正则化器，作者认为它可能对其他模型架构更有益，但未验证。
- **固定规划视界**：H=12 对所有任务固定，不根据任务或状态自适应。图 11 显示 cheetah 最佳视界接近 8 步，说明固定视界并非最优。
- **固定动作重复**：每个任务的动作重复 R 是预设的（cartpole R=8、reacher R=4、cheetah R=4、finger R=2、cup R=4、walker R=2），未学习调整。
- **无迁移学习**：未考虑任务间或环境间的迁移。
- **探索策略简单**：仅使用高斯噪声（ε ~ Normal(0, 0.3)），未探索更复杂的探索方法。
- **未在真实机器人上验证**：所有实验在模拟环境（DeepMind Control Suite）中完成。
- **未解决高视觉多样性任务**：未处理视觉更复杂的场景。
- **未使用梯度规划或价值函数**：规划视界之外的奖励总和未通过价值函数近似，计算效率有提升空间。

## 工程启示

- **复现时先核对超参数**：最重要的超参数是动作重复（R）、KL 散度尺度 β、学习率。动作重复直接影响数据收集的粒度，KL 裁剪到 3 个自由 nats 是关键细节，缺失会导致训练不稳定。
- **RSSM 的随机路径不能省**：纯确定性模型在大多数任务上性能下降，纯随机模型完全失败。如果下游任务需要长期记忆，确定性路径的 GRU 单元数（200）和潜在维度（30）是合理的起点，但建议先做激活函数敏感性测试（RSSM 对 ELU/ReLU 鲁棒，但纯随机模型对 ELU 敏感）。
- **CEM 参数是性能杠杆**：J=1000、I=10、K=100 是默认值，但图 11 显示规划视界长度对性能影响最大（6 步不足，过长反而有害）。对具体任务，建议先扫描 H 在 6-12 之间的值，再调整 J 和 I。
- **多任务训练会变慢**：如果目标是单任务，不要直接复用多任务配置；多任务时每 C=100 步收集每个任务的一个回合，但学习速度会下降，需要更多总更新步。
- **最容易踩坑的地方**：数据收集阶段的前 S=5 个随机回合质量至关重要，如果初始数据分布太差，模型可能无法收敛；另外，图像预处理（位深度降至 5 位）和批次大小 B=50、序列块长度 L=50 必须保持一致，否则重建损失和 KL 平衡会偏移。

## Overview
Planning has been very successful for control tasks with known environment dynamics. To leverage planning in unknown environments, the agent needs to learn the dynamics from interactions with the world. However, learning dynamics models that are accurate enough for planning has been a long-standing challenge, especially in image-based domains. We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning in latent space. To achieve high performance, the dynamics model must accurately predict the rewards ahead for multiple time steps. We approach this using a latent dynamics model with both deterministic and stochastic transition components. Moreover, we propose a multi-step variational inference objective that we name latent overshooting. Using only pixel observations, our agent solves continuous control tasks with contact dynamics, partial observability, and sparse rewards, which exceed the difficulty of tasks that were previously solved by planning with learned models. PlaNet uses substantially fewer episodes and reaches final performance close to and sometimes higher than strong model-free algorithms.

## 参考
- https://arxiv.org/abs/1811.04551

## 개요

PlaNet은 픽셀 관측에서 순환 상태 공간 모델(RSSM)을 학습하고 잠재 공간에서 교차 엔트로피 방법(CEM)으로 계획하는 순수 모델 기반 강화 학습 에이전트입니다. DeepMind Control Suite의 여섯 가지 연속 제어 작업에서 1000개의 에피소드 샘플로 무모델 기준선(D4PG)이 100000개의 에피소드에서 달성한 성능에 도달하거나 능가하여 데이터 효율성을 40배에서 500배 이상 향상시켰습니다. 핵심 기여는 무작위성과 결정론이 혼합된 잠재 역학 모델과 온라인 계획의 결합이 샘플 효율적인 제어의 실행 가능한 경로임을 입증한 것입니다.

## 그것이 바꾼 것

PlaNet 이전에는 픽셀에서 직접 모델 예측 제어(MPC)를 수행하는 것이 거의 불가능했습니다. 비디오 예측 모델은 결정론적(다중 모드 미래를 처리할 수 없음)이거나 순수 무작위(훈련이 불안정하고 장기 예측이 붕괴됨)였기 때문입니다. 강화 학습 커뮤니티의 주류 합의는 모델 오류가 다단계 계획에서 누적되므로 정책이나 가치 함수를 직접 학습하는 것이 더 낫다는 것이었습니다. PlaNet이 실제로 바꾼 것은 이 전제입니다. RSSM의 결정론적 경로가 시간 단계 간 메모리를 담당하고 무작위 경로가 관측의 불확실성을 포착하여 잠재 공간에서의 12단계 계획(H=12)이 충분히 신뢰할 수 있게 만들었고, 실제 시뮬레이터 상태로 CEM 계획을 수행하는 성능(예: cheetah 662 vs 656, walker 951 vs 994 근접)을 능가하기도 했습니다.

또 다른 바뀐 인식은 "계획은 실제 상태를 사용해야 한다"는 것입니다. PlaNet은 64×64 픽셀, 5비트 깊이(비트 깊이를 5로 낮춤)의 관측에서 학습된 30차원 잠재 상태가 개루프 50단계의 픽셀 수준 예측(그림 9)을 지원할 수 있고, 잠재 공간의 상태 추정(위치, 속도)이 계획 시야를 훨씬 넘어서는 거리에서도 예측 가능함(그림 10)을 증명했습니다. 이는 모델이 단순한 프레임 간 보간이 아니라 기본 물리량의 압축 표현을 학습한다는 것을 의미합니다. 또한 PlaNet의 다중 작업 실험(단일 에이전트가 작업 정체를 알지 못한 채 여섯 가지 작업을 동시에 학습)은 "각 작업에 별도의 모델링이 필요하다"는 기본 가정에 도전했지만, 학습 속도는 느려졌습니다.

## 방법 분해

### 모델 아키텍처: RSSM(Recurrent State-Space Model)
- 두 가지 경로로 구성:
  - **결정론적 경로**: GRU(200개 유닛)가 이전 시간 단계의 결정론적 상태 h_{t-1}와 무작위 상태 s_{t-1}를 받아 h_t를 출력합니다. 이를 통해 모델이 시간 단계 간 정보를 기억할 수 있어 순수 무작위 모델의 정보 손실을 피할 수 있습니다.
  - **무작위 경로**: 30차원 대각 가우시안 분포에서 s_t를 샘플링하며, 평균과 표준편차는 h_t와 관측 인코더로 예측됩니다. 무작위성은 학습에 중요합니다. 작업이 에이전트 관점에서 부분적으로 관측 가능하고(초기 상태 불명), 노이즈가 계획 목표에 안전 마진을 추가하여 더 견고한 행동 시퀀스를 생성하기 때문입니다.
- 관측 인코더/디코더: 합성곱/역합성곱 네트워크(Ha & Schmidhuber 2018), 기타 함수는 두 개의 완전 연결 계층(크기 200, ReLU 활성화).

### 훈련 목표
- 재구성 손실(이미지 재구성)과 KL 발산(잠재 분포 정규화)을 공동 최적화합니다. KL 항은 재구성 항에 대해 스케일링되지 않지만, 발산 손실은 3 자유 nats 미만으로 클리핑됩니다.
- 핵심 설계: **latent overshooting**(잠재 오버슈팅)이 다단계 예측의 정규화기로 사용되며, 훈련 중 잠재 상태를 다단계로 전개하고 KL을 계산합니다. 그러나 최종 에이전트는 이를 사용하지 않았습니다. RSSM 자체가 충분히 좋았기 때문입니다(절제 실험에서 RSSM 성능을 약간 낮추지만 순수 무작위 DRNN을 크게 향상시킴).

### 계획 알고리즘: CEM(교차 엔트로피 방법)
- 매개변수: 계획 시야 H=12, 최적화 반복 I=10, 후보 샘플 J=1000, 최적 적합 K=100.
- 절차:
  1. 인수분해된 신념 q(a_{t:t+H}) ← Normal(0, I)에서 초기화.
  2. I번 반복: J개의 행동 시퀀스를 샘플링하고, 학습된 보상 모델로 기대 보상을 평가한 후, K개의 최적 시퀀스로 가우시안 분포를 재적합(평균과 표준편차 업데이트).
  3. 첫 번째 행동 평균 μ_t를 실행 행동으로 반환.
- 행동 노이즈 ε ~ Normal(0, 0.3)는 데이터 수집에 사용되며, C=100 업데이트 단계마다 추가 에피소드를 수집하고 S=5개의 무작위 행동 시드 에피소드에서 시작합니다.

### 다중 작업 학습
- 단일 에이전트가 여섯 가지 작업 모두에서 훈련되며 작업 정체를 알지 못하고 이미지 관측에서 추론해야 합니다. 행동 공간은 호환성을 위해 사용되지 않는 요소로 채워지고, 알고리즘은 C 업데이트 단계마다 각 작업의 에피소드를 수집하도록 조정되며, 주 실험과 동일한 하이퍼파라미터를 사용합니다.

## 핵심 혁신

1. **무작위성과 결정론의 혼합 상태 공간**: 이것이 RSSM의 핵심 혁신입니다. 순수 무작위 모델(stochastic-only)은 어떤 작업도 해결할 수 없고, 순수 결정론적 모델(deterministic-only)은 대부분의 작업에서 더 나쁜 성능을 보입니다. RSSM의 결정론적 경로는 장기 메모리를 제공하고 무작위 경로는 관측 불확실성을 처리하여, 두 경로의 결합이 잠재 역학을 안정적이면서도 표현력 있게 만듭니다. 이 설계는 비디오 예측에서 "결정론적 모델은 다중 모드 미래를 생성할 수 없고, 무작위 모델은 훈련이 어렵다"는 딜레마를 직접 해결합니다.

2. **잠재 공간에서의 온라인 계획(latent planning)**: PlaNet은 정책이나 가치 함수를 학습하지 않고 CEM으로 잠재 공간에서 행동 시퀀스를 탐색합니다. 무작위 사격(random shooting, 1000개 시퀀스에서 최적 선택)과 비교하여 CEM의 반복 최적화(I=10)는 모든 작업에서 성능을 향상시킵니다. 무작위 데이터 수집(random collection)과 비교하여 온라인 계획 기반 데이터 수집은 모든 작업에 도움이 되며, cartpole, finger, walker 작업에는 필수적입니다. 이는 계획이 의사 결정뿐만 아니라 데이터 분포를 유도하여 "탐색-모델링-계획"의 긍정적 피드백을 형성함을 보여줍니다.

3. **데이터 효율성의 비약적 향상**: PlaNet은 1000개의 에피소드로 D4PG가 100000개의 에피소드에서 달성한 성능에 도달하여 데이터 효율성을 40(reacher)에서 500+(cheetah)배 향상시킵니다. 이 규모의 차이는 점진적 개선이 아니라 "픽셀에서 제어를 학습하는 데 필요한 데이터 양"에 대한 기대를 바꾸어, 데이터 획득 비용이 높은 실제 로봇 응용에 가능성을 열어줍니다.

## 실험과 결과

### 작업과 기준선
- 작업: Cartpole Swing Up, Reacher Easy, Cheetah Run, Finger Spin, Cup Catch, Walker Walk.
- 기준선: A3C(고유 감각 모달리티, 100000 에피소드), D4PG(픽셀 모달리티, 100000 에피소드), PlaNet(픽셀 모달리티, 1000 에피소드), CEM + 실제 시뮬레이터(시뮬레이터 상태, 0 에피소드, 성능 상한 추정).

### 핵심 결과(표 1, 5개 시드와 10개 궤적의 평균 최종 성능)

| 작업 | A3C | D4PG | PlaNet (ours) | CEM + true simulator | 데이터 효율성 이득(PlaNet vs D4PG) |
|------|-----|------|---------------|----------------------|-------------------------------|
| Cartpole Swing Up | 558 | 862 | 821 | 850 | 250 |
| Reacher Easy | 285 | 967 | 832 | 964 | 40 |
| Cheetah Run | 214 | 524 | 662 | 656 | 500+ |
| Finger Spin | 129 | 985 | 700 | 825 | 300 |
| Cup Catch | 105 | 980 | 930 | 993 | 100 |
| Walker Walk | 311 | 968 | 951 | 994 | 90 |

- PlaNet은 cheetah에서 D4PG를 능가(662 vs 524)하고, walker에서 근접(951 vs 968), cup에서 근접(930 vs 980)합니다. finger에서는 뒤처지지만(700 vs 985), 데이터 효율성 이득은 여전히 300배입니다.
- CEM + true simulator와 비교: PlaNet은 cheetah에서 능가(662 vs 656)하고 walker에서 근접(951 vs 994)하여 잠재 모델의 품질이 실제 시뮬레이터에 근접함을 보여줍니다.

### 절제 실험
- **모델 구성 요소**: 순수 무작위 모델은 어떤 작업도 해결할 수 없고, 순수 결정론적 모델은 대부분의 작업에서 더 나쁩니다. RSSM은 모든 작업에서 최적입니다(finger 작업에서는 결정론적 모델이 약간 더 좋음).
- **계획 설계**: PlaNet은 무작위 수집(random collection)과 무작위 사격(random shooting)보다 우수하여 온라인 계획과 CEM 반복 최적화의 필요성을 입증합니다.
- **잠재 오버슈팅**: DRNN 성능을 크게 향상시키지만 RSSM 성능을 약간 낮춥니다(그림 7).
- **활성화 함수**: ELU는 순수 무작위 모델에 도움이 되지만 RSSM은 활성화 함수 선택에 강건합니다(그림 8).
- **계획 시야**: 시야 길이 6은 충분하지 않고, 너무 길면 탐색 공간 증가로 성능이 저하됩니다. cheetah 환경의 최적 시야는 약 8단계입니다(그림 11, 계획 성능 범위 132~837).

### 다중 작업 학습
- 단일 에이전트가 모든 작업을 해결하지만, 개별 훈련 에이전트보다 학습 속도가 느립니다(그림 5, 그림 6).

## 경계와 한계

- **latent overshooting 미사용**: 최종 에이전트는 이 정규화기를 사용하지 않았으며, 저자는 다른 모델 아키텍처에 더 유용할 수 있다고 생각하지만 검증하지 않았습니다.
- **고정 계획 시야**: H=12가 모든 작업에 고정되어 있으며 작업이나 상태에 따라 적응하지 않습니다. 그림 11은 cheetah의 최적 시야가 약 8단계임을 보여주어 고정 시야가 최적이 아님을 시사합니다.
- **고정 행동 반복**: 각 작업의 행동 반복 R은 사전 설정됩니다(cartpole R=8, reacher R=4, cheetah R=4, finger R=2, cup R=4, walker R=2), 학습으로 조정되지 않습니다.
- **전이 학습 없음**: 작업 간 또는 환경 간 전이를 고려하지 않습니다.
- **단순한 탐색 전략**: 가우시안 노이즈(ε ~ Normal(0, 0.3))만 사용하며 더 복잡한 탐색 방법을 탐구하지 않습니다.
- **실제 로봇 검증 없음**: 모든 실험은 시뮬레이션 환경(DeepMind Control Suite)에서 수행됩니다.
- **높은 시각적 다양성 작업 미해결**: 시각적으로 더 복잡한 장면을 처리하지 않습니다.
- **그래디언트 계획 또는 가치 함수 미사용**: 계획 시야를 넘어서는 보상 합계를 가치 함수로 근사하지 않아 계산 효율성에 개선 여지가 있습니다.

## 공학적 시사점

- **재현 시 하이퍼파라미터 먼저 확인**: 가장 중요한 하이퍼파라미터는 행동 반복(R), KL 발산 스케일 β, 학습률입니다. 행동 반복은 데이터 수집의 세분성에 직접 영향을 미치고, KL 클리핑을 3 자유 nats로 하는 것은 핵심 세부 사항으로 누락 시 훈련이 불안정해집니다.
- **RSSM의 무작위 경로는 생략 불가**: 순수 결정론적 모델은 대부분의 작업에서 성능이 저하되고, 순수 무작위 모델은 완전히 실패합니다. 하류 작업에 장기 메모리가 필요하면 결정론적 경로의 GRU 유닛 수(200)와 잠재 차원(30)이 합리적인 시작점이지만, 먼저 활성화 함수 민감도 테스트를 권장합니다(RSSM은 ELU/ReLU에 강건하지만 순수 무작위 모델은 ELU에 민감).
- **CEM 매개변수는 성능 레버**: J=1000, I=10, K=100이 기본값이지만, 그림 11은 계획 시야 길이가 성능에 가장 큰 영향을 미침을 보여줍니다(6단계는 부족, 너무 길면 오히려 해로움). 특정 작업에 대해 H를 6~12 사이에서 먼저 스캔한 후 J와 I를 조정하는 것을 권장합니다.
- **다중 작업 훈련은 느려짐**: 목표가 단일 작업이라면 다중 작업 구성을 직접 재사용하지 마십시오. 다중 작업 시 C=100 단계마다 각 작업의 에피소드를 수집하지만 학습 속도가 감소하므로 더 많은 총 업데이트 단계가 필요합니다.
- **가장 쉽게 함정에 빠지는 부분**: 데이터 수집 단계의 처음 S=5개 무작위 에피소드 품질이 매우 중요합니다. 초기 데이터 분포가 너무 나쁘면 모델이 수렴하지 않을 수 있습니다. 또한 이미지 전처리(비트 깊이를 5비트로 낮춤)와 배치 크기 B=50, 시퀀스 블록 길이 L=50을 일관되게 유지해야 합니다. 그렇지 않으면 재구성 손실과 KL 균형이 어긋납니다.
