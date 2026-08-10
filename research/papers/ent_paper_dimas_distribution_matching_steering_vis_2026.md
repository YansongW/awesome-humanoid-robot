---
$id: ent_paper_dimas_distribution_matching_steering_vis_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DiMaS: Distribution Matching for Steering Vision-Language-Action Models'
  zh: 'DiMaS: Distribution Matching for Steering Vision-Language-Action Models'
  ko: 'DiMaS: Distribution Matching for Steering Vision-Language-Action Models'
summary:
  en: 'Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation,
    yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs
    a task by intervening on its internal representations. Representation steering is a well-established interpretability
    tool for language and vision-language.'
  zh: DiMaS 提出一种基于最优传输的激活工程方法，用于对 flow-matching 型视觉-语言-动作模型（VLA）进行细粒度行为控制。作者通过将动作专家内部表征从“缺乏目标特征”分布传输到“具有目标特征”分布，在不重新训练的情况下双向调制机器人运动速度与末端执行器垂直位移，并验证了跨任务、跨套件的泛化能力。核心贡献在于揭示了经典线性引导在
    VLA 中失效的原因，并提供了分布级干预的可行方案。
  ko: 'Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation,
    yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs
    a task by intervening on its internal representations. Representation steering is a well-established interpretability
    tool for language and vision-language.'
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
- dimas
- distribution
- matching
- steering
- vis
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
  title: 'arXiv:2607.14280 DiMaS: Distribution Matching for Steering Vision-Language-Action Models'
  url: https://arxiv.org/abs/2607.14280
  date: '2026-07-15'
  accessed_at: '2026-08-05'
---

## 概述

DiMaS 提出一种基于最优传输的激活工程方法，用于对 flow-matching 型视觉-语言-动作模型（VLA）进行细粒度行为控制。作者通过将动作专家内部表征从“缺乏目标特征”分布传输到“具有目标特征”分布，在不重新训练的情况下双向调制机器人运动速度与末端执行器垂直位移，并验证了跨任务、跨套件的泛化能力。核心贡献在于揭示了经典线性引导在 VLA 中失效的原因，并提供了分布级干预的可行方案。

## 它改变了什么

VLA 模型的行为控制长期停留在提示工程或策略微调层面，而激活工程（activation engineering）在 LLM 中已被证明有效，但直接迁移到 VLA 时遭遇了根本性障碍。作者用实验证明，均值差引导和回归引导这两种经典表征干预在 flow-matching 型 VLA 中不仅失效，甚至会出现“增减干预朝同一方向移动特征”的反常现象。这并非简单的超参数问题，而是源于动作专家表征空间的分布结构——特征缺失与特征存在群体并非线性可分，导致基于均值或回归方向的线性扰动无法精确对准目标方向。

DiMaS 真正改变的是干预的数学形式：从“沿单一方向推动表征”升级为“在两个分布之间建立最优传输映射”。这一转变使得干预不再依赖表征空间的全局线性结构，而是通过局部传输计划实现精确的特征调制。更重要的是，作者将干预位置从 VLM 主干转移到动作专家网络，并证明动作专家深层表征对目标特征几乎完全线性可分（准确率接近 100%），这为干预提供了比 VLM 更干净的操作空间。该工作首次系统性地回答了“VLA 内部表征如何被安全地定向修改”这一核心问题。

## 方法拆解

### 问题形式化
将干预建模为源分布 D⁻（特征缺失）到目标分布 D⁺（特征存在）的最优传输问题。给定经验样本 X⁻={z⁻ᵢ}ₙᵢ₌₁ 与 X⁺={z⁺ⱼ}ₘⱼ₌₁，求解离散 Kantorovich 目标：
min_γ Σᵢⱼ γᵢⱼ ‖z⁻ᵢ − z⁺ⱼ‖²，边际约束 γ1ₘ = 1/n·1ₙ，γᵀ1ₙ = 1/m·1ₘ。

### 低秩 Sinkhorn 求解
- 传输计划分解为 T = Q·diag(g⁻¹)·Rᵀ，其中 Q ∈ R₊ⁿˣʳ，R ∈ R₊ᵐˣʳ，秩 r ≪ min(n,m)。
- 加入熵正则项 −εH(T)，ε=10⁻⁴，通过 Python Optimal Transport (POT) 包实现。
- 时间复杂度 O((n+m)·r·K)，K 为迭代次数；单套件 50 回合训练数据约 3,500 样本/分布，离线求解约 85 分钟。

### 测试时干预
1. 从动作专家第 ℓ 层（倒数第二层）提取残差流表征 h。
2. 通过最近邻投影 P(h) = arg min_{z∈D⁻} ‖z−h‖ 将 h 投影到源分布。
3. 应用传输映射 T∘P(h)。
4. 线性探针门控 g(h)∈{0,1} 仅在特征缺失时激活干预。
5. 插值合成：h ← (1−α)h + α(T∘P(h))，默认 α=0.5。

### 关键设计决策
- **尾部阈值分割**：使用下分位数 q₀.₂₅ 与上分位数 q₀.₇₅ 划分源/目标分布，而非中位数，以获得更干净的特征缺失/存在群体。
- **干预动作专家而非 VLM**：动作专家深层线性可分性 >93%（flow-matching 步骤 0），而 VLM 最高仅 87%。
- **插值而非完全传输**：α=1 时完全传输引入偏差导致任务失败，插值可在控制特征的同时最小化成功率下降。

## 关键创新

1. **分布级干预替代线性引导**：首次将最优传输引入 VLA 激活工程，解决了线性方法在 flow-matching 架构中失效的问题。均值差和回归引导依赖表征空间的全局线性结构，而 DiMaS 通过局部传输计划实现精确调制，这是方法论层面的根本转变。

2. **动作专家作为干预靶点**：作者证明动作专家深层表征对行为特征几乎完全线性可分（准确率接近 100%），而 VLM 表征可分性最高仅 87%。选择动作专家不仅提高了干预精度，还避免了 VLM 中语义与动作表征混杂的问题。

3. **插值机制实现安全干预**：完全传输（α=1）会导致成功率急剧下降（如 π0.5 在 LIBERO-Object 上从 98% 降至 0%），而 α=0.5 的插值在保持成功率的同时实现特征调制。这一设计将干预从“全有或全无”变为可调节的连续控制，为实际部署提供了安全操作空间。

## 实验与结果

### 速度调制（图 2）
DiMaS 在 SmolVLA 和 π0.5 上均能双向调制速度，而线性引导和提示基线表现不一致。调制速度时成功率基本保持，但调制垂直位移时成功率下降明显。

### 泛化实验（图 4，减速方向）
| 模型 | 套件 | 基线 SR | Setting 1 | Setting 2 | Setting 3 | Setting 4 |
|------|------|---------|-----------|-----------|-----------|-----------|
| π0.5 | Object | 98.0% | 99.5% | 97.0% | 100.0% | — |
| π0.5 | Spatial | 97.0% | 91.5% | 95.0% | 96.0% | 92.0% |
| π0.5 | Goal | 91.0% | 92.0% | 86.0% | 86.0% | 93.0% |
| SmolVLA | Object | 89% | 64% | 70% | 76% | — |
| SmolVLA | Spatial | 71% | 54% | 52% | 58% | 55% |
| SmolVLA | Goal | 81% | 52% | 46% | 26% | 55% |

π0.5 在多数设置下保持成功率，而 SmolVLA 成功率下降显著，反映动作块策略差异（SmolVLA 每步预测新块更动态，π0.5 一次预测 10 个动作更平滑鲁棒）。

### 长时程任务（图 5，LIBERO-10，π0.5 减速）
| α | Δmean | SR |
|---|-------|-----|
| 0.5 | −0.024 | 90.0% |
| 0.6 | — | 81.0% |
| 0.7 | — | 72.0% |
| 0.8 | — | 46.0% |
| 0.9 | — | 7.0% |

α 增大时速度降低但成功率急剧下降，验证插值必要性。

### 线性可分性分析（图 6）
动作专家中表征几乎完全线性可分（接近 100%），flow-matching 步骤 0 时较深层可分性 >93%，高于 VLM 任何层（最大 87%）。

### α 消融（图 7）
π0.5 在 α=0.5 后成功率才下降，SmolVLA 更早且更不规则退化；α=0.5 为默认操作点。

## 边界与局限

- 调制垂直位移时成功率显著下降，该特征与任务完成紧密耦合（如 LIBERO-Object 中减小垂直位移使末端执行器过低无法放入物体）。
- 当前干预对所有时间步一视同仁，未区分平移与纯旋转阶段；作者承认“何时干预”应成为学习目标。
- 动作块策略中每个隐藏表征与输出动作的对应关系是近似的，一个输出动作受块中多个表征影响，按精确对应分组只是近似。
- LIBERO-Goal 是最难套件，任务行为多样导致引导效果较弱；跨套件迁移到 Goal 时 π0.5 的均值移动未达到 p<0.01 显著性（p=0.032）。
- 层选择 ℓ 是唯一依赖底层 VLA 的超参数，作者使用倒数第二层但未系统研究最优层如何随基础模型变化。

## 工程启示

复现 DiMaS 时首先核对三个关键点：一是分布划分的分位数设置（q₀.₂₅/q₀.₇₅），尾部阈值直接影响源/目标分布的分离质量；二是低秩 Sinkhorn 的秩 r 与正则化 ε，默认 r=min(n,m)、ε=10⁻⁴，秩过低会丢失传输细节；三是插值系数 α，默认 0.5 但需根据模型和任务调整——SmolVLA 对 α 更敏感，建议从 0.3 开始扫描。

最容易踩坑的地方是干预层选择。作者使用倒数第二层，但不同 VLA 的动作专家层数差异大（π0.5 有 17 层，SmolVLA 层数不同），直接套用可能失效。建议先做线性可分性扫描（类似图 6），选择可分性最高的层。另一个陷阱是门控分类器的训练：线性探针需在源/目标分布上分别采样，样本量不足（少于 3,500）会导致门控误判，建议至少 50 回合训练数据。

下游团队若要将 DiMaS 用于实际机器人控制，需注意干预的推理开销：最坏情况（10 个 flow-matching 步骤全部触发）每时间步增加 6.2 ms，约占 50 ms 动作预算的 12%。对于实时性要求高的场景，可考虑仅在部分 flow-matching 步骤施加干预以降低开销。此外，增加方向（更快、更高）比减少方向更难实现，因为成功轨迹自然减速并降低末端执行器，干预在放大策略已有倾向时最有效。

## Overview
Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation, yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs a task by intervening on its internal representations. Representation steering is a well-established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs. We propose DiMaS, a Distribution-Matching Steering strategy tailored to flow-matching VLAs, which transports between representation distributions rather than shifting along a fixed direction, and show that it effectively controls behavior across two state-of-the-art VLAs. We further examine the generalizability of this strategy as the tasks it is learned from and evaluated on grow increasingly dissimilar, characterizing where behavioral control transfers and where it weakens. Finally, through an analysis of the representation structure of the action expert, we explain why classical linear steering falls short in the visuomotor setting: behavioral features are linearly decodable but not linearly steerable, which motivates the distribution-matching design of DiMaS. Our code is publicly available at https://github.com/pegah-kh/dimas, with additional results and videos at https://pegah-kh.github.io/dimas/

## 参考
- https://arxiv.org/abs/2607.14280

## 개요

DiMaS는 flow-matching 기반 비전-언어-행동 모델(VLA)에 대한 세밀한 행동 제어를 위해 최적 수송(optimal transport) 기반 활성 공학(activation engineering) 방법을 제안한다. 저자는 행동 전문가(action expert)의 내부 표현을 "목표 특징 부재" 분포에서 "목표 특징 존재" 분포로 수송함으로써, 재훈련 없이 로봇의 이동 속도와 엔드 이펙터의 수직 변위를 양방향으로 변조하고, 과제 및 스위트 간 일반화 능력을 검증했다. 핵심 기여는 고전적 선형 유도(linear steering)가 VLA에서 실패하는 이유를 밝히고 분포 수준 개입의 실행 가능한 방안을 제공한 것이다.

## 그것이 바꾼 것

VLA 모델의 행동 제어는 오랫동안 프롬프트 엔지니어링이나 정책 미세 조정 수준에 머물러 있었지만, LLM에서 효과가 입증된 활성 공학을 VLA에 직접 이식할 때 근본적인 장애물에 직면했다. 저자는 평균 차이 유도와 회귀 유도라는 두 가지 고전적 표현 개입 방법이 flow-matching 기반 VLA에서 단순히 실패할 뿐만 아니라, "증감 개입이 동일한 방향으로 특징을 이동시키는" 변칙적 현상까지 발생함을 실험으로 증명했다. 이는 단순한 하이퍼파라미터 문제가 아니라 행동 전문가 표현 공간의 분포 구조에서 비롯된 것으로, 특징 부재 집단과 특징 존재 집단이 선형적으로 분리되지 않아 평균이나 회귀 방향에 기반한 선형 섭동이 목표 방향을 정확히 정렬할 수 없다.

DiMaS가 실제로 바꾼 것은 개입의 수학적 형식, 즉 "단일 방향으로 표현을 밀어내는 것"에서 "두 분포 사이에 최적 수송 매핑을 구축하는 것"으로의 전환이다. 이러한 전환 덕분에 개입은 더 이상 표현 공간의 전역적 선형 구조에 의존하지 않으며, 국소 수송 계획을 통해 정밀한 특징 변조를 달성한다. 더 중요한 것은, 저자가 개입 위치를 VLM 백본에서 행동 전문가 네트워크로 옮기고, 행동 전문가의 깊은 표현이 목표 특징에 대해 거의 완전히 선형 분리 가능하다는 것(정확도 약 100%)을 증명하여 VLM보다 더 깨끗한 조작 공간을 제공한다는 점이다. 이 연구는 "VLA 내부 표현이 어떻게 안전하게 방향적으로 수정될 수 있는가"라는 핵심 질문에 처음으로 체계적으로 답했다.

## 방법 분해

### 문제 형식화
개입을 소스 분포 D⁻(특징 부재)에서 타깃 분포 D⁺(특징 존재)로의 최적 수송 문제로 모델링한다. 경험적 샘플 X⁻={z⁻ᵢ}ₙᵢ₌₁ 및 X⁺={z⁺ⱼ}ₘⱼ₌₁이 주어졌을 때, 이산 Kantorovich 목적 함수를 푼다:
min_γ Σᵢⱼ γᵢⱼ ‖z⁻ᵢ − z⁺ⱼ‖², 주변 제약 γ1ₘ = 1/n·1ₙ, γᵀ1ₙ = 1/m·1ₘ.

### 저랭크 Sinkhorn 해법
- 수송 계획을 T = Q·diag(g⁻¹)·Rᵀ로 분해하며, 여기서 Q ∈ R₊ⁿˣʳ, R ∈ R₊ᵐˣʳ, 랭크 r ≪ min(n,m)이다.
- 엔트로피 정규화 항 −εH(T)를 추가하며, ε=10⁻⁴, Python Optimal Transport (POT) 패키지로 구현한다.
- 시간 복잡도는 O((n+m)·r·K)이며, K는 반복 횟수; 단일 스위트 50 에피소드 훈련 데이터는 약 3,500 샘플/분포, 오프라인 해법은 약 85분 소요.

### 테스트 시 개입
1. 행동 전문가의 ℓ번째 레이어(마지막에서 두 번째)에서 잔차 흐름 표현 h를 추출한다.
2. 최근접 이웃 투영 P(h) = arg min_{z∈D⁻} ‖z−h‖로 h를 소스 분포에 투영한다.
3. 수송 매핑 T∘P(h)를 적용한다.
4. 선형 프로브 게이트 g(h)∈{0,1}는 특징이 부재할 때만 개입을 활성화한다.
5. 보간 합성: h ← (1−α)h + α(T∘P(h)), 기본 α=0.5.

### 핵심 설계 결정
- **꼬리 임계값 분할**: 중앙값 대신 하위 분위수 q₀.₂₅와 상위 분위수 q₀.₇₅를 사용하여 소스/타깃 분포를 나누며, 더 깨끗한 특징 부재/존재 집단을 얻는다.
- **VLM이 아닌 행동 전문가 개입**: 행동 전문가의 깊은 선형 분리 가능성은 >93%(flow-matching 단계 0)인 반면, VLM은 최대 87%에 불과하다.
- **완전 수송이 아닌 보간**: α=1의 완전 수송은 편향을 도입하여 과제 실패를 초래하므로, 보간은 특징을 제어하면서 성공률 하락을 최소화한다.

## 핵심 혁신

1. **선형 유도를 대체하는 분포 수준 개입**: 최적 수송을 VLA 활성 공학에 처음 도입하여 flow-matching 아키텍처에서 선형 방법이 실패하는 문제를 해결했다. 평균 차이 및 회귀 유도는 표현 공간의 전역적 선형 구조에 의존하지만, DiMaS는 국소 수송 계획을 통해 정밀한 변조를 달성하며 이는 방법론적 차원의 근본적 전환이다.

2. **개입 표적으로서의 행동 전문가**: 저자는 행동 전문가의 깊은 표현이 행동 특징에 대해 거의 완전히 선형 분리 가능하며(정확도 약 100%), VLM 표현의 분리 가능성은 최대 87%에 불과함을 증명했다. 행동 전문가를 선택하면 개입 정밀도가 향상될 뿐만 아니라 VLM에서 의미론과 행동 표현이 혼재하는 문제도 피할 수 있다.

3. **안전한 개입을 위한 보간 메커니즘**: 완전 수송(α=1)은 성공률을 급격히 떨어뜨리지만(예: π0.5가 LIBERO-Object에서 98%에서 0%로), α=0.5의 보간은 성공률을 유지하면서 특징 변조를 달성한다. 이 설계는 개입을 "전부 또는 전무"에서 조절 가능한 연속 제어로 바꾸어 실제 배포를 위한 안전한 작동 공간을 제공한다.

## 실험 및 결과

### 속도 변조(그림 2)
DiMaS는 SmolVLA와 π0.5 모두에서 속도를 양방향으로 변조할 수 있지만, 선형 유도와 프롬프트 기준선은 일관되지 않은 성능을 보인다. 속도 변조 시 성공률은 대체로 유지되지만, 수직 변위 변조 시 성공률 하락이 뚜렷하다.

### 일반화 실험(그림 4, 감속 방향)
| 모델 | 스위트 | 기준선 SR | Setting 1 | Setting 2 | Setting 3 | Setting 4 |
|------|------|---------|-----------|-----------|-----------|-----------|
| π0.5 | Object | 98.0% | 99.5% | 97.0% | 100.0% | — |
| π0.5 | Spatial | 97.0% | 91.5% | 95.0% | 96.0% | 92.0% |
| π0.5 | Goal | 91.0% | 92.0% | 86.0% | 86.0% | 93.0% |
| SmolVLA | Object | 89% | 64% | 70% | 76% | — |
| SmolVLA | Spatial | 71% | 54% | 52% | 58% | 55% |
| SmolVLA | Goal | 81% | 52% | 46% | 26% | 55% |

π0.5는 대부분의 설정에서 성공률을 유지하지만, SmolVLA는 성공률 하락이 뚜렷하며 이는 행동 블록 정책의 차이를 반영한다(SmolVLA는 각 단계에서 새 블록을 예측하여 더 동적이고, π0.5는 한 번에 10개의 행동을 예측하여 더 매끄럽고 견고하다).

### 장기 과제(그림 5, LIBERO-10, π0.5 감속)
| α | Δmean | SR |
|---|-------|-----|
| 0.5 | −0.024 | 90.0% |
| 0.6 | — | 81.0% |
| 0.7 | — | 72.0% |
| 0.8 | — | 46.0% |
| 0.9 | — | 7.0% |

α가 증가하면 속도는 감소하지만 성공률이 급격히 떨어지며, 보간의 필요성을 검증한다.

### 선형 분리 가능성 분석(그림 6)
행동 전문가의 표현은 거의 완전히 선형 분리 가능하며(약 100%), flow-matching 단계 0에서 더 깊은 층의 분리 가능성은 >93%로 VLM의 모든 층(최대 87%)보다 높다.

### α 소거(그림 7)
π0.5는 α=0.5 이후에야 성공률이 하락하고, SmolVLA는 더 일찍 그리고 더 불규칙하게 성능이 저하된다; α=0.5가 기본 작동 지점이다.

## 경계 및 한계

- 수직 변위 변조 시 성공률이 크게 하락하며, 이 특징은 과제 완료와 밀접하게 결합되어 있다(예: LIBERO-Object에서 수직 변위를 줄이면 엔드 이펙터가 너무 낮아져 물체를 넣을 수 없음).
- 현재 개입은 모든 시간 단계에 동일하게 적용되며, 병진 이동과 순수 회전 단계를 구분하지 않는다; 저자는 "언제 개입할지"가 학습 목표가 되어야 한다고 인정한다.
- 행동 블록 정책에서 각 은닉 표현과 출력 행동의 대응 관계는 근사적이며, 하나의 출력 행동은 블록 내 여러 표현의 영향을 받으므로 정확한 대응으로 그룹화하는 것은 근사에 불과하다.
- LIBERO-Goal은 가장 어려운 스위트로, 과제 행동이 다양하여 유도 효과가 약하다; Goal로의 교차 스위트 전이 시 π0.5의 평균 이동은 p<0.01 유의성을 달성하지 못했다(p=0.032).
- 레이어 선택 ℓ은 기본 VLA에 의존하는 유일한 하이퍼파라미터이며, 저자는 마지막에서 두 번째 레이어를 사용하지만 최적 레이어가 기본 모델에 따라 어떻게 변하는지 체계적으로 연구하지 않았다.

## 공학적 시사점

DiMaS를 재현할 때 먼저 세 가지 핵심 사항을 확인해야 한다: 첫째, 분포 분할의 분위수 설정(q₀.₂₅/q₀.₇₅)으로, 꼬리 임계값은 소스/타깃 분포의 분리 품질에 직접 영향을 미친다; 둘째, 저랭크 Sinkhorn의 랭크 r과 정규화 ε로, 기본값은 r=min(n,m), ε=10⁻⁴이며, 랭크가 너무 낮으면 수송 세부 정보가 손실된다; 셋째, 보간 계수 α로, 기본값은 0.5이지만 모델과 과제에 따라 조정해야 한다 — SmolVLA는 α에 더 민감하므로 0.3부터 스캔하는 것을 권장한다.

가장 실수하기 쉬운 부분은 개입 레이어 선택이다. 저자는 마지막에서 두 번째 레이어를 사용하지만, VLA마다 행동 전문가의 레이어 수가 크게 다르므로(π0.5는 17개 레이어, SmolVLA는 다른 레이어 수) 직접 적용하면 실패할 수 있다. 먼저 선형 분리 가능성 스캔(그림 6과 유사)을 수행하여 분리 가능성이 가장 높은 레이어를 선택하는 것을 권장한다. 또 다른 함정은 게이트 분류기 훈련이다: 선형 프로브는 소스/타깃 분포에서 각각 샘플링해야 하며, 샘플 수가 부족하면(3,500 미만) 게이트 오판이 발생할 수 있으므로 최소 50 에피소드 훈련 데이터를 권장한다.

하류 팀이 DiMaS를 실제 로봇 제어에 사용하려면 개입의 추론 오버헤드에 주의해야 한다: 최악의 경우(10개의 flow-matching 단계 모두 트리거) 시간 단계당 6.2ms가 추가되며, 이는 약 50ms 행동 예산의 약 12%에 해당한다. 실시간 요구 사항이 높은 시나리오에서는 일부 flow-matching 단계에만 개입을 적용하여 오버헤드를 줄일 수 있다. 또한, 방향 증가(더 빠르게, 더 높게)는 감소 방향보다 구현하기 어렵다. 성공 궤적은 자연스럽게 감속하고 엔드 이펙터를 낮추기 때문이며, 개입은 정책이 이미 가진 경향을 증폭할 때 가장 효과적이다.
