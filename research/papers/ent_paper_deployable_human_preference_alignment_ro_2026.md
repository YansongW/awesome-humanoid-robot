---
$id: ent_paper_deployable_human_preference_alignment_ro_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Deployable Human Preference Alignment in Robotics: Learning Representative Rewards from Diverse Human Preferences'
  zh: 'Deployable Human Preference Alignment in Robotics: Learning Representative Rewards from Diverse Human Preferences'
  ko: 'Deployable Human Preference Alignment in Robotics: Learning Representative Rewards from Diverse Human Preferences'
summary:
  en: Aligning robot policies with human preferences is essential for deployment to diverse end users. In per-user alignment
    approach, preference feedback is often sparse, so learning becomes unstable and vulnerable to human preference noise,
    and a growing number of individualized policies makes validation difficult before deployment. A single shared policy approach
    to user alignment avoids this cost.
  zh: 本文提出 PREC（Preference-based Reward Clustering）框架，面向机器人部署中多样化终端用户的偏好对齐问题。PREC 通过自预测表示（SPR）预训练共享轨迹编码器，再以泄漏 EM 算法联合聚类用户并学习每簇代表性奖励模型，最终为每簇训练一个策略。核心贡献在于以少量可验证的策略集合，在稀疏、嘈杂偏好反馈下逼近个体化对齐的社会福利水平。
  ko: Aligning robot policies with human preferences is essential for deployment to diverse end users. In per-user alignment
    approach, preference feedback is often sparse, so learning becomes unstable and vulnerable to human preference noise,
    and a growing number of individualized policies makes validation difficult before deployment. A single shared policy approach
    to user alignment avoids this cost.
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
- deployable
- human
- preference
- alignment
- ro
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
  title: 'arXiv:2607.12466 Deployable Human Preference Alignment in Robotics: Learning Representative Rewar'
  url: https://arxiv.org/abs/2607.12466
  date: '2026-07-14'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 PREC（Preference-based Reward Clustering）框架，面向机器人部署中多样化终端用户的偏好对齐问题。PREC 通过自预测表示（SPR）预训练共享轨迹编码器，再以泄漏 EM 算法联合聚类用户并学习每簇代表性奖励模型，最终为每簇训练一个策略。核心贡献在于以少量可验证的策略集合，在稀疏、嘈杂偏好反馈下逼近个体化对齐的社会福利水平。

## 它改变了什么

机器人偏好对齐长期在两条路线间摇摆：每用户独立建模能捕捉异质偏好，但稀疏反馈下学习不稳、易受噪声干扰，且大量个性化策略在监管严格领域（如 FDA 将医用外骨骼列为 II 类器械）几乎无法逐一验证；单一共享策略虽部署简单，却必然牺牲少数群体偏好。PREC 真正改变的是将“对齐”从个体粒度重构为“亚种群粒度”——用 K 个代表性奖励模型覆盖连续偏好空间，使部署者只需验证 K 个策略而非 N 个用户策略，同时保留比单一策略高得多的偏好保真度。

这一转变的深层动机在于：机器人领域的用户反馈远比 NLP 或推荐系统稀疏（每用户仅数十条标签），且噪声类型复杂（随机、短视、错误、跳过、相等）。PREC 的假设是，用户偏好虽各异，但可聚类为有限个稳定模式；通过跨用户共享表示学习与聚类，能有效弥补单用户数据不足，将验证负担从 O(N) 降至 O(K)。

## 方法拆解

PREC 分三阶段，核心在于将表示学习与噪声标签解耦，并将聚类与奖励学习联合优化。

### 阶段一：种群级表示学习（SPR 预训练）
- 搁置所有偏好标签，跨用户聚合轨迹，训练编码器 \( f_{\psi^{enc}}(s,a) \) 预测一步状态差 \( s_{t+1} - s_t \)。
- 理由：利用比任何单个用户更广泛的状态-动作观测，避免在表示学习阶段直接依赖稀疏且有噪声的标签。
- 实现：MLP 将状态-动作对映射到 **128** 维潜在表示，两个隐藏层宽度 **256**，ReLU，dropout；AdamW 优化 **20** epoch，批大小 **1024**，学习率 **3×10⁻⁴**，权重衰减 **10⁻⁴**。预训练后丢弃预测器，编码器冻结。

### 阶段二：亚种群级解码器学习（泄漏 EM）
- 冻结编码器，联合推断用户簇分配与每簇奖励解码器 \( h_{\psi_k^{dec}} \)。
- 奖励模型分解：\( \hat{r}_{\psi_k}(s,a) = h_{\psi_k^{dec}}(f_{\psi^{enc*}}(s,a)) \)。
- 标签似然：簇 k 下标签 \( y_{i,m} \) 的似然为 \( P(y_{i,m} \mid \tau_{i,m}, Z_i=k, \psi_k) = \sigma(\hat{R}_{\psi_k}(\tau_{i,m}))^{y_{i,m}}(1-\sigma(\hat{R}_{\psi_k}(\tau_{i,m})))^{1-y_{i,m}} \)。
- **E-step**：计算后验责任 \( \gamma_{ik} = \frac{\rho_k \mathcal{L}_{ik}}{\sum_{k'=1}^{K}\rho_{k'} \mathcal{L}_{ik'}} \)，转为硬分配 \( \hat{z}_i = \arg\max_k \gamma_{ik} \)。
- **泄漏 M-step**：权重 \( \omega_{ik} = \max(\mathbf{1}[\hat{z}_i = k], \nu) \)，\( \nu=0.05 \)；解码器最小化加权 BCE：\( \psi_k^{dec} \leftarrow \arg\min_{\psi_k^{dec}} \sum_{i=1}^{N} \omega_{ik} \sum_{m=1}^{M_i} \mathrm{BCE}(\sigma(\hat{R}_{\psi_k}(\tau_{i,m})), y_{i,m}) \)。
- 设计理由：硬更新在簇内用户少时过拟合，完全软更新模糊簇边界，泄漏系数 \( \nu \) 在特化与稳定间平衡。EM 运行 **8** 次迭代，头初始化训练 **6** epoch，每次 E-step 后额外训练 **3** epoch。
- 理论保证：定理 1 证明固定簇先验下，泄漏 EM 单调改进受限变分族的泄漏 ELBO 并收敛到有限极限；\( \nu=0 \) 时退化为硬 EM。

### 阶段三：簇级策略优化
- 使用学习到的奖励模型，通过隐式 Q 学习（IQL）为每个簇训练策略。IQL 配置：梯度步数 **100,000**，批大小 **256**，学习率 **3×10⁻⁴**，折扣 **0.99**，expectile **0.7**，AWR 温度 **3.0**。

## 关键创新

1. **表示学习与偏好监督解耦**：SPR 预训练完全忽略标签，仅利用状态转移预测。这是反直觉的——传统方法直接以偏好标签训练表示，但 PREC 证明在标签稀疏且噪声高时，无监督的动力学预测能学到更稳健的共享表示，为后续聚类提供干净特征空间。
2. **泄漏 EM 的联合聚类-奖励学习**：不同于先独立聚类用户再训练奖励（如 K-Means 基线），PREC 将聚类与奖励学习置于同一目标下交替优化。泄漏系数 \( \nu \) 是关键设计——它既避免硬 EM 在小簇上的过拟合，又防止软 EM 的簇边界模糊，且定理 1 保证了收敛性。
3. **部署友好的策略集合**：最终产出 K 个策略而非 N 个，直接回应监管验证需求。实验表明 K=3 或 K=5 时，PREC 在功利、平等、纳什三种社会福利指标上均接近甚至超越个体化模型（Indiv），而验证成本仅为后者的 K/N。

## 实验与结果

实验在四个 D4RL MuJoCo 环境（HalfCheetah、Ant、Hopper、Walker2d）上进行，轨迹池由 random、medium、expert 数据按 **1:2:2** 混合，轨迹段长度 **50**。共 **30** 个用户，每用户 **50** 或 **100** 条标签，噪声注入强度 **16%** 与 **28%**。

### 聚类质量（表 4，稀疏反馈下）
| 环境 | K | PREC SH | PREC CH | K-Means SH | K-Means CH |
|---|---|---|---|---|---|
| HalfCheetah | 2 | **0.605** | **296.2** | 未明确 | 未明确 |
| Ant | 3 | **0.616** | **478.5** | 未明确 | 未明确 |
| Walker2d | 5 | **0.365** | **300.6** | 未明确 | 未明确 |
| Hopper | 3 | **0.666** | **491.6** | 未明确 | 未明确 |

PREC 在所有环境与 K 值下 SH 与 CH 均优于 K-Means 与 W-K-Means 基线，且优势随 K 增大而扩大（K=5 时 PREC SH=**0.54** vs K-Means **0.23**，由表 1 数值）。

### 社会福利（表 2，PREC 组件消融）
| 环境 | 指标 | PREC | PREC (w/o SPR, leaky EM) |
|---|---|---|---|
| HalfCheetah | Util | **0.798** | 0.786 |
| Ant | Egal | **0.165** | 0.132 |
| Hopper | Nash | **0.753** | 0.672 |
| Walker2d | Egal | **0.481** | 0.188 |

完整 PREC 在所有环境-指标组合上最佳，移除 SPR 与泄漏 EM 后性能显著下降，尤其 Walker2d 平等福利从 **0.481** 跌至 **0.188**（由表内数值计算）。

### 反馈预算实验
- 每用户 **10** 至 **50** 标签时，PREC 大幅优于 Pooled 与 Indiv。
- 每用户 **500** 标签时，Indiv 在功利与 Nash 福利上超越 PREC；Pooled 在标签从 **100** 增至 **500** 时性能急剧下降。

## 边界与局限

- 仅在模拟连续控制基准（D4RL MuJoCo）上验证，未在真实机器人或真实人类用户上测试；脚本化标注器虽注入噪声，但与真实反馈仍有差距。
- 定理 1 仅覆盖解码器参数，簇先验 \( \rho_k \) 固定；任何修改先验的稳定器（如 Dirichlet 平滑）不在收敛性论证范围内。
- 当每用户反馈充足（如 **500** 标签）时，个体化模型 Indiv 在功利与 Nash 福利上超越 PREC，表明 PREC 的优势主要在稀疏反馈场景。
- 未探索除 IQL 外的下游离线 RL 算法；未处理非马尔可夫奖励（作者指出可与 Preference Transformer 结合，但未实验）。

## 工程启示

复现 PREC 时，最关键的核对点是 SPR 预训练与泄漏 EM 的衔接：编码器必须完全冻结后再进入聚类阶段，任何微调都会破坏表示与标签的解耦。泄漏系数 \( \nu=0.05 \) 是敏感超参——过小退化为硬 EM 导致小簇过拟合，过大则簇边界模糊；建议在目标环境的用户数（如 **30**）下先扫描 \( \nu \in [0.01, 0.1] \)。另一个易踩坑处是噪声注入的实现：五种噪声类型（stochastic、myopic、mistake、skip、equal）需按均匀随机采样混合，且阈值 \( \eta=0.5 \) 与强度（**16%**、**28%**）必须严格复现，否则聚类质量对比会失真。对于下游团队，若反馈预算充足（>500 标签/用户），应直接考虑 Indiv 而非 PREC；若预算稀疏且需监管验证，PREC(3) 或 PREC(5) 是验证成本与福利保真的最佳折中。所有实验可在 CPU 上运行（Intel Xeon Gold 5320，**4** 核 **24** GB 内存），无需 GPU，但 **30** 用户 × **50** 标签 × **8** 次 EM 迭代的完整流程预计耗时较长，建议先以 K=2 跑通 pipeline 再扩展。

## Overview
Aligning robot policies with human preferences is essential for deployment to diverse end users. In per-user alignment approach, preference feedback is often sparse, so learning becomes unstable and vulnerable to human preference noise, and a growing number of individualized policies makes validation difficult before deployment. A single shared policy approach to user alignment avoids this cost but fails to capture heterogeneous preferences and often neglects minority preferences. To address these challenges, we introduce Preference-based REward Clustering (PREC), a novel framework that learns a compact set of policies from binary preference labels provided by diverse users. From a dataset of user trajectories and their preference labels, PREC first sets the labels aside and aggregates trajectories across users to learn a population-level shared trajectory encoder, alleviating limited per-user coverage and avoiding label noise during representation learning. Using this representation, PREC jointly assigns users to preference-coherent clusters and learns a representative reward model per cluster using preference labels, from which a policy is optimized for each cluster. Clustering similar users compensates for the limited number of labels available from each user and mitigates the effect of label noise. At the same time, maintaining a manageable number of reward models reduces the validation burden at deployment. Experiments across diverse simulated locomotion environments show that PREC groups users who label different trajectory subsets into preference-coherent clusters more accurately than baseline methods. Under sparse and noisy feedback, policies trained with PREC improve all three social welfare metrics over an existing single shared-policy user-alignment approach and even outperform per-user alignment approaches.

## 参考
- https://arxiv.org/abs/2607.12466

## 개요

본 논문은 로봇 배포 환경에서 다양한 최종 사용자의 선호 정렬 문제를 해결하기 위해 PREC(Preference-based Reward Clustering) 프레임워크를 제안한다. PREC는 자기 예측 표현(SPR) 사전 학습을 통해 공유 궤적 인코더를 학습하고, 누출 EM 알고리즘을 사용하여 사용자를 클러스터링하고 각 클러스터의 대표 보상 모델을 공동으로 학습한 후, 각 클러스터에 대한 정책을 학습한다. 핵심 기여는 적은 수의 검증 가능한 정책 세트를 통해 희소하고 잡음이 많은 선호 피드백 하에서 개인화 정렬의 사회 복지 수준에 근접하는 것이다.

## 무엇을 변화시키는가

로봇 선호 정렬은 오랫동안 두 가지 접근 방식 사이에서 흔들려 왔다: 사용자별 개별 모델링은 이질적 선호를 포착할 수 있지만, 희소 피드백 하에서 학습이 불안정하고 잡음에 취약하며, 규제가 엄격한 분야(예: FDA가 의료용 외골격을 II등급 의료기기로 분류)에서는 수많은 개인화 정책을 하나씩 검증하는 것이 거의 불가능하다. 단일 공유 정책은 배포가 간단하지만 소수 집단의 선호를 반드시 희생한다. PREC가 진정으로 변화시키는 것은 "정렬"을 개인 단위에서 "하위 집단 단위"로 재구성하는 것이다 — K개의 대표 보상 모델로 연속적 선호 공간을 커버하여, 배포자는 N개의 사용자 정책이 아닌 K개의 정책만 검증하면 되며, 동시에 단일 정책보다 훨씬 높은 선호 충실도를 유지한다.

이러한 전환의 근본적 동기는 로봇 분야의 사용자 피드백이 NLP나 추천 시스템보다 훨씬 희소하고(사용자당 수십 개의 레이블에 불과), 잡음 유형이 복잡하다는 점(무작위, 근시안적, 오류, 건너뛰기, 동일)에 있다. PREC의 가정은 사용자 선호가 다양하지만 유한한 안정적 패턴으로 클러스터링될 수 있다는 것이다. 사용자 간 공유 표현 학습과 클러스터링을 통해 단일 사용자 데이터 부족을 보완하고, 검증 부담을 O(N)에서 O(K)로 줄일 수 있다.

## 방법 분석

PREC는 세 단계로 구성되며, 핵심은 표현 학습과 잡음 레이블의 분리, 그리고 클러스터링과 보상 학습의 공동 최적화에 있다.

### 1단계: 집단 수준 표현 학습(SPR 사전 학습)
- 모든 선호 레이블을 보류하고, 사용자 간 궤적을 집계하여 인코더 \( f_{\psi^{enc}}(s,a) \)가 한 단계 상태 차이 \( s_{t+1} - s_t \)를 예측하도록 학습한다.
- 근거: 단일 사용자보다 훨씬 광범위한 상태-행동 관측을 활용하여, 표현 학습 단계에서 희소하고 잡음이 많은 레이블에 직접 의존하는 것을 피한다.
- 구현: MLP가 상태-행동 쌍을 **128**차원 잠재 표현으로 매핑하며, 두 개의 은닉층 너비 **256**, ReLU, dropout 사용. AdamW 최적화 **20** epoch, 배치 크기 **1024**, 학습률 **3×10⁻⁴**, 가중치 감쇠 **10⁻⁴**. 사전 학습 후 예측기는 폐기되고 인코더는 동결된다.

### 2단계: 하위 집단 수준 디코더 학습(누출 EM)
- 인코더를 동결하고, 사용자 클러스터 할당과 각 클러스터의 보상 디코더 \( h_{\psi_k^{dec}} \)를 공동으로 추론한다.
- 보상 모델 분해: \( \hat{r}_{\psi_k}(s,a) = h_{\psi_k^{dec}}(f_{\psi^{enc*}}(s,a)) \).
- 레이블 우도: 클러스터 k에서 레이블 \( y_{i,m} \)의 우도는 \( P(y_{i,m} \mid \tau_{i,m}, Z_i=k, \psi_k) = \sigma(\hat{R}_{\psi_k}(\tau_{i,m}))^{y_{i,m}}(1-\sigma(\hat{R}_{\psi_k}(\tau_{i,m})))^{1-y_{i,m}} \).
- **E-step**: 사후 책임 \( \gamma_{ik} = \frac{\rho_k \mathcal{L}_{ik}}{\sum_{k'=1}^{K}\rho_{k'} \mathcal{L}_{ik'}} \)을 계산하고, 하드 할당 \( \hat{z}_i = \arg\max_k \gamma_{ik} \)으로 변환한다.
- **누출 M-step**: 가중치 \( \omega_{ik} = \max(\mathbf{1}[\hat{z}_i = k], \nu) \), \( \nu=0.05 \). 디코더는 가중 BCE를 최소화한다: \( \psi_k^{dec} \leftarrow \arg\min_{\psi_k^{dec}} \sum_{i=1}^{N} \omega_{ik} \sum_{m=1}^{M_i} \mathrm{BCE}(\sigma(\hat{R}_{\psi_k}(\tau_{i,m})), y_{i,m}) \).
- 설계 근거: 하드 업데이트는 클러스터 내 사용자가 적을 때 과적합되고, 완전 소프트 업데이트는 클러스터 경계를 흐리게 만든다. 누출 계수 \( \nu \)는 특수화와 안정성 사이의 균형을 맞춘다. EM은 **8**회 반복, 헤드 초기화 학습 **6** epoch, 각 E-step 후 추가 **3** epoch 학습.
- 이론적 보장: 정리 1은 고정 클러스터 사전 하에서 누출 EM이 제한된 변분 패밀리의 누출 ELBO를 단조 개선하고 유한 극한으로 수렴함을 증명한다. \( \nu=0 \)일 때 하드 EM으로 축소된다.

### 3단계: 클러스터 수준 정책 최적화
- 학습된 보상 모델을 사용하여 암시적 Q 학습(IQL)으로 각 클러스터에 대한 정책을 학습한다. IQL 구성: 그래디언트 스텝 **100,000**, 배치 크기 **256**, 학습률 **3×10⁻⁴**, 할인율 **0.99**, expectile **0.7**, AWR 온도 **3.0**.

## 핵심 혁신

1. **표현 학습과 선호 감독의 분리**: SPR 사전 학습은 레이블을 완전히 무시하고 상태 전이 예측만 활용한다. 이는 반직관적이다 — 전통적 방법은 선호 레이블로 직접 표현을 학습하지만, PREC는 레이블이 희소하고 잡음이 높을 때 비지도 역학 예측이 더 견고한 공유 표현을 학습하여 이후 클러스터링에 깨끗한 특징 공간을 제공함을 증명한다.
2. **누출 EM의 공동 클러스터링-보상 학습**: 사용자를 먼저 독립적으로 클러스터링한 후 보상을 학습하는 방식(예: K-Means 기준선)과 달리, PREC는 클러스터링과 보상 학습을 동일한 목표 하에 교대로 최적화한다. 누출 계수 \( \nu \)는 핵심 설계 요소이다 — 하드 EM의 소규모 클러스터 과적합을 방지하면서 소프트 EM의 클러스터 경계 모호함을 막고, 정리 1이 수렴성을 보장한다.
3. **배포 친화적 정책 세트**: 최종 산출물은 N개가 아닌 K개의 정책으로, 규제 검증 요구에 직접 대응한다. 실험 결과 K=3 또는 K=5일 때 PREC는 공리주의, 평등주의, 내시의 세 가지 사회 복지 지표에서 개별 모델(Indiv)에 근접하거나 능가하며, 검증 비용은 후자의 K/N에 불과하다.

## 실험 및 결과

실험은 네 개의 D4RL MuJoCo 환경(HalfCheetah, Ant, Hopper, Walker2d)에서 수행되었으며, 궤적 풀은 random, medium, expert 데이터를 **1:2:2** 비율로 혼합하고 궤적 세그먼트 길이는 **50**이다. 총 **30**명의 사용자, 사용자당 **50** 또는 **100**개의 레이블, 잡음 주입 강도 **16%** 및 **28%**.

### 클러스터링 품질(표 4, 희소 피드백 하)
| 환경 | K | PREC SH | PREC CH | K-Means SH | K-Means CH |
|---|---|---|---|---|---|
| HalfCheetah | 2 | **0.605** | **296.2** | 명시되지 않음 | 명시되지 않음 |
| Ant | 3 | **0.616** | **478.5** | 명시되지 않음 | 명시되지 않음 |
| Walker2d | 5 | **0.365** | **300.6** | 명시되지 않음 | 명시되지 않음 |
| Hopper | 3 | **0.666** | **491.6** | 명시되지 않음 | 명시되지 않음 |

PREC는 모든 환경과 K 값에서 SH 및 CH 지표가 K-Means 및 W-K-Means 기준선보다 우수하며, K가 증가할수록 그 격차가 커진다(K=5에서 PREC SH=**0.54** vs K-Means **0.23**, 표 1 수치 기준).

### 사회 복지(표 2, PREC 구성 요소 제거 실험)
| 환경 | 지표 | PREC | PREC (SPR, 누출 EM 제거) |
|---|---|---|---|
| HalfCheetah | Util | **0.798** | 0.786 |
| Ant | Egal | **0.165** | 0.132 |
| Hopper | Nash | **0.753** | 0.672 |
| Walker2d | Egal | **0.481** | 0.188 |

완전한 PREC는 모든 환경-지표 조합에서 최상의 성능을 보이며, SPR과 누출 EM을 제거하면 성능이 크게 하락한다. 특히 Walker2d의 평등 복지는 **0.481**에서 **0.188**로 급락한다(표 내 수치 계산 기준).

### 피드백 예산 실험
- 사용자당 **10**~**50**개 레이블일 때, PREC는 Pooled 및 Indiv보다 크게 우수하다.
- 사용자당 **500**개 레이블일 때, Indiv가 공리주의 및 내시 복지에서 PREC를 능가한다. Pooled는 레이블이 **100**개에서 **500**개로 증가할 때 성능이 급격히 하락한다.

## 경계 및 한계

- D4RL MuJoCo 시뮬레이션 연속 제어 벤치마크에서만 검증되었으며, 실제 로봇이나 실제 인간 사용자에서는 테스트되지 않았다. 스크립트 기반 주석기는 잡음을 주입하지만 실제 피드백과는 여전히 차이가 있다.
- 정리 1은 디코더 매개변수만 다루며, 클러스터 사전 \( \rho_k \)는 고정되어 있다. 사전을 수정하는 안정화 장치(예: Dirichlet 평활화)는 수렴성 논증 범위에 포함되지 않는다.
- 사용자당 피드백이 충분할 때(예: **500**개 레이블), 개별 모델 Indiv가 공리주의 및 내시 복지에서 PREC를 능가하며, 이는 PREC의 장점이 주로 희소 피드백 시나리오에 있음을 시사한다.
- IQL 외의 하류 오프라인 RL 알고리즘은 탐색되지 않았다. 비마르코프 보상은 처리되지 않았다(저자는 Preference Transformer와 결합할 수 있다고 언급했지만 실험하지 않았다).

## 엔지니어링 시사점

PREC를 재현할 때 가장 중요한 확인 지점은 SPR 사전 학습과 누출 EM의 연결이다: 인코더는 클러스터링 단계에 들어가기 전에 완전히 동결되어야 하며, 어떤 미세 조정도 표현과 레이블의 분리를 깨뜨린다. 누출 계수 \( \nu=0.05 \)는 민감한 하이퍼파라미터이다 — 너무 작으면 하드 EM으로 퇴화하여 소규모 클러스터가 과적합되고, 너무 크면 클러스터 경계가 모호해진다. 목표 환경의 사용자 수(예: **30**)에서 \( \nu \in [0.01, 0.1] \) 범위를 먼저 스캔할 것을 권장한다. 또 다른 함정은 잡음 주입 구현이다: 다섯 가지 잡음 유형(stochastic, myopic, mistake, skip, equal)은 균일 무작위 샘플링으로 혼합해야 하며, 임계값 \( \eta=0.5 \)와 강도(**16%**, **28%**)를 엄격히 재현해야 한다. 그렇지 않으면 클러스터링 품질 비교가 왜곡된다. 하류 팀의 경우, 피드백 예산이 충분하다면(사용자당 >500개 레이블) PREC 대신 Indiv를 직접 고려해야 한다. 예산이 희소하고 규제 검증이 필요하다면 PREC(3) 또는 PREC(5)가 검증 비용과 복지 충실도 사이의 최상의 절충안이다. 모든 실험은 CPU(Intel Xeon Gold 5320, **4**코어 **24**GB 메모리)에서 실행 가능하며 GPU가 필요하지 않지만, **30**명의 사용자 × **50**개 레이블 × **8**회 EM 반복의 전체 프로세스는 시간이 오래 걸릴 것으로 예상되므로, 먼저 K=2로 파이프라인을 실행한 후 확장할 것을 권장한다.
