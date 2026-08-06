---
$id: ent_paper_ur_vc_unsupervised_robotic_value_correct_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies'
  zh: 'UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies'
  ko: 'UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies'
summary:
  en: 'Modern robot learning systems increasingly rely on dense progress or value signals to evaluate intermediate states,
    guide policy learning, and detect task completion, making the quality of these signals critical. Since such dense labels
    are rarely available at scale, normalized time within a demonstration is often used as a scalable substitute: later frames
    are treated as higher progress..'
  zh: UR-VC 是一种离线、免训练的标签修正方法，用于修正机器人演示数据中由归一化时间派生的有噪进度代理。它利用跨独立片段的视觉状态匹配来估计更准确的物理进度，并在真实双臂布料操作任务中显著提升了优势条件 VLA 策略的成功率。核心贡献在于将标签修正从学习过程中解耦，直接作用于监督信号本身。
  ko: 'Modern robot learning systems increasingly rely on dense progress or value signals to evaluate intermediate states,
    guide policy learning, and detect task completion, making the quality of these signals critical. Since such dense labels
    are rarely available at scale, normalized time within a demonstration is often used as a scalable substitute: later frames
    are treated as higher progress..'
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
- ur
- vc
- unsupervised
- robotic
- value
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
  title: 'arXiv:2607.12892 UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies'
  url: https://arxiv.org/abs/2607.12892
  date: '2026-07-14'
  accessed_at: '2026-08-05'
---

## 概述

UR-VC 是一种离线、免训练的标签修正方法，用于修正机器人演示数据中由归一化时间派生的有噪进度代理。它利用跨独立片段的视觉状态匹配来估计更准确的物理进度，并在真实双臂布料操作任务中显著提升了优势条件 VLA 策略的成功率。核心贡献在于将标签修正从学习过程中解耦，直接作用于监督信号本身。

## 它改变了什么

现有机器人学习系统普遍依赖密集的进度或价值信号来指导策略学习与任务完成检测。由于真实物理进度难以大规模标注，归一化时间成为最常用的替代品，但其单调递增的假设与接触丰富操作中常见的倒退、停滞现象严重不符。这种系统性偏差会被下游学习器继承，导致策略无法区分有效动作与破坏性动作，甚至利用外观、速度等偶然线索进行错误建模。

UR-VC 真正改变的是问题定义：它不再试图训练一个更鲁棒的进度估计器来对抗有噪标签，而是直接修正标签本身。这一视角转换将标签修正从学习过程中解耦，使得任何下游算法——无论是优势条件策略还是独立价值模型——都能受益于更准确的监督信号，而无需修改其训练目标或架构。

## 方法拆解

UR-VC 的核心假设是：跨独立片段的状态匹配能提供减少时间扭曲的锚点，因为相似物理状态在不同片段中对应的时间戳各不相同，平均这些时间戳可抵消轨迹特定的噪声。

### 标签修正流程
1. **嵌入计算**：使用 SigLIP-2 视觉编码器计算每帧的 L2 归一化嵌入，以余弦相似度度量状态相似性。
2. **候选集构建**：对查询帧 i，在每个其他片段 e 中，选取时间带 τ=0.3 内的帧作为候选：C_{i,e} = {j : ep(j)=e, |g_j - g_i| ≤ τ}。
3. **最佳代表选择**：从每个片段的候选中仅保留与查询帧最相似的帧：j*_{i,e} = argmax_{j∈C_{i,e}} f_i^T f_j。
4. **相似度过滤**：若最佳代表相似度低于阈值 ρ=0.90，则丢弃该片段贡献。
5. **片段平衡平均**：剩余片段代表构成集合 M_i，修正估计为 ĝ_i = (1/|M_i|) Σ_{e∈M_i} g_{j*_{i,e}}；若无代表存活，保持原值。

### 关键设计决策
- **每片段仅贡献一个匹配**：避免过度加权时间相邻帧，因为同一片段内误差相关，而跨片段平均才能减少独立噪声。
- **时间带 τ 约束修正幅度**：所有被平均的标签满足 |g_j - g_i| ≤ τ，因此修正有界 |ĝ_i - g_i| ≤ τ，防止异常跳跃。
- **相似度阈值 ρ 保守过滤**：确保只有足够相似的状态才参与估计，避免引入不相关片段的噪声。

### 优势标签构造
对从帧 i 开始、视界 H 的动作块，优势标签为 r_i = ĝ_{i+H} - ĝ_i；片段末尾附近则按视界速率重新缩放：r_i = (H/(T_e - i))(ĝ_{T_e} - ĝ_i)。按 r_i 排序后，标记 top 20% 为正优势示例，训练时附加文本后缀 "…, advantage: positive"。

## 关键创新

1. **免训练的标签修正范式**：UR-VC 无需训练任何模型、无需在线 rollout、无需手动标注，仅通过离线语料库上的矩阵运算即可完成修正。这使其可作为即插即用模块，直接替换现有流程中的时间派生标签。

2. **片段平衡的跨片段匹配**：不同于简单的最近邻检索，UR-VC 强制每个片段最多贡献一个匹配标签，这一设计在统计上更合理——跨独立片段的平均能减少轨迹特定噪声，而同一片段内相邻帧的误差高度相关，不应重复加权。

3. **非单调进度的显式建模**：通过允许修正后的标签出现负优势（实验中 13.4% 的帧获得负视界优势），UR-VC 首次在无监督条件下捕捉了物理进度倒退现象，这是时间派生标签完全无法表达的信息。

## 实验与结果

实验在真实双臂布料展平-折叠任务上进行，主要评估集为 150 个真实机器人片段，训练混合包含 5700 个展平-折叠演示与 1795 个恢复演示。

### 覆盖率与修正质量
| 指标 | 150 片段 | 10^4 片段 |
|------|----------|-----------|
| 覆盖率（相似度 ≥ 0.90） | 98% | 99.9% |
| 覆盖率（相似度 ≥ 0.955） | 69.9% | 90.4% |
| 修正估计粗糙度（mean \|Δ²ĝ_t\|） | 基准 | 下降约三分之一 |

修正估计与归一化时间整体相关性高达 0.98，但 13.4% 的帧获得负视界优势（视界为片段长度的 5%，约 1.7 秒），表明非单调进度被有效捕捉。

### 下游真实机器人评估
| 桌面条件 | Baseline | UR-VC |
|----------|----------|-------|
| Bare table | 0.90 | 0.97 |
| Beige cloth | 0.70 | 0.73 |
| Blue-gray cloth | 0.50 | 0.43 |
| Light-yellow cloth | 0.63 | 0.90 |
| Light-gray cloth | 0.77 | 0.80 |
| Khaki cloth | 0.87 | 0.90 |
| **Average** | **0.728** | **0.789** |

UR-VC 在 6 种条件中的 5 种中成功率更高，平均成功率从 0.728（131/180）提升至 0.789（142/180），提升幅度约 6.1 个百分点（由表内数值 0.728→0.789 计算）。唯一表现下降的条件是 Blue-gray cloth，可能与该背景下的视觉检索质量有关。

## 边界与局限

UR-VC 的核心假设是视觉相似即物理进度相似，但当相似视觉状态出现在不同任务阶段或不同动作历史之后，其潜在进度可能模糊，这一假设可能失效。片段平衡平均能减少轨迹特定噪声，但无法修正系统性的检索错误——如果检索池本身存在偏差，修正结果也会继承该偏差。论文未明确 UR-VC 在非布料操作（如刚性物体装配）或更复杂多阶段任务中的表现，也未探讨超参数 τ 与 ρ 的敏感性。作者明确不声称访问真实物理进度的 ground-truth，因此修正质量的评估仅依赖下游任务成功率这一间接指标。

## 工程启示

复现 UR-VC 时，首先核对嵌入模型的选择——SigLIP-2 的视觉特征质量直接决定检索可靠性，更换编码器需重新验证覆盖率。时间带 τ=0.3 与相似度阈值 ρ=0.90 是针对布料操作调优的，迁移到其他任务时应先绘制覆盖率-阈值曲线，确保至少 90% 的帧有匹配代表。最容易踩坑的是索引约定：论文使用 1 起始索引（o_1^(e), …, o_{T_e}^(e)），若实现采用 0 起始索引，片段末尾的视界缩放公式分母需相应调整。对于下游团队，建议先在小规模检索池（如 50 片段）上验证修正标签的粗糙度下降趋势，再扩展到全量数据；若发现覆盖率不足，优先增加检索池规模而非降低阈值，因为 10^4 片段规模下覆盖率可提升至 99.9%。部署时，正优势后缀的构造需与训练完全一致，否则策略可能无法正确理解查询语义。

## Overview
Modern robot learning systems increasingly rely on dense progress or value signals to evaluate intermediate states, guide policy learning, and detect task completion, making the quality of these signals critical. Since such dense labels are rarely available at scale, normalized time within a demonstration is often used as a scalable substitute: later frames are treated as higher progress. However, this time-derived label is only a noisy proxy for physical task progress. In contact-rich manipulation, a robot may make progress and then lose it through slips, failed grasps, or partial undoing, while the time-derived label continues to increase monotonically. We introduce Unsupervised Robotic Value Correction (UR-VC), an offline, training-free method for correcting time-derived progress labels. UR-VC exploits a simple regularity in demonstration data: similar states often recur across different episodes, but at different timestamps. Instead of trusting the timestamp from a single trajectory, UR-VC retrieves similar states from other episodes and aggregates their time-derived labels to obtain a corrected progress estimate. UR-VC requires no manual progress labels, reward annotations, or additional value model. We evaluate UR-VC on real bimanual cloth flatten-and-fold data, a long-horizon deformable-object manipulation task with visible intermediate progress. The corrected labels capture local regressions and non-uniform progress that normalized time cannot represent, while preserving the overall task trend. We further use the corrected signal to construct advantage labels for VLA training, following recent advantage-conditioned policy learning. UR-VC shows a positive trend in real-robot task success under matched data, model, and training settings.

## 参考
- https://arxiv.org/abs/2607.12892

## 개요

UR-VC는 로봇 시연 데이터에서 정규화된 시간에서 파생된 노이즈가 있는 진행 프록시를 수정하기 위한 오프라인, 훈련 불필요 라벨 수정 방법입니다. 이는 독립적인 세그먼트 간의 시각적 상태 매칭을 활용하여 더 정확한 물리적 진행도를 추정하며, 실제 양팔 직물 조작 작업에서 어드밴티지 조건부 VLA 정책의 성공률을 크게 향상시킵니다. 핵심 기여는 라벨 수정을 학습 과정에서 분리하여 감독 신호 자체에 직접 작용한다는 점입니다.

## 그것이 바꾸는 것

기존 로봇 학습 시스템은 정책 학습과 작업 완료 감지를 안내하기 위해 조밀한 진행도 또는 가치 신호에 광범위하게 의존합니다. 실제 물리적 진행도는 대규모로 라벨링하기 어렵기 때문에 정규화된 시간이 가장 일반적인 대체재가 되지만, 단조 증가 가정은 접촉이 많은 조작에서 흔한 후퇴, 정체 현상과 심각하게 불일치합니다. 이러한 체계적 편향은 하위 학습기에 상속되어 정책이 유효한 동작과 파괴적 동작을 구분하지 못하게 하고, 심지어 외관, 속도와 같은 우연한 단서를 활용하여 잘못된 모델링을 하게 만듭니다.

UR-VC가 실제로 바꾸는 것은 문제 정의입니다. 더 강건한 진행도 추정기를 훈련하여 노이즈가 있는 라벨에 대항하는 대신, 라벨 자체를 직접 수정합니다. 이러한 관점 전환은 라벨 수정을 학습 과정에서 분리하여 어드밴티지 조건부 정책이든 독립적 가치 모델이든 어떤 하위 알고리즘도 훈련 목표나 아키텍처를 수정하지 않고 더 정확한 감독 신호의 혜택을 받을 수 있게 합니다.

## 방법 분해

UR-VC의 핵심 가정은 독립적인 세그먼트 간의 상태 매칭이 시간 왜곡을 줄이는 앵커를 제공한다는 것입니다. 유사한 물리적 상태는 다른 세그먼트에서 서로 다른 타임스탬프에 해당하며, 이러한 타임스탬프를 평균화하면 궤적 특정 노이즈를 상쇄할 수 있기 때문입니다.

### 라벨 수정 프로세스
1. **임베딩 계산**: SigLIP-2 비전 인코더를 사용하여 각 프레임의 L2 정규화 임베딩을 계산하고, 코사인 유사도로 상태 유사성을 측정합니다.
2. **후보 집합 구축**: 쿼리 프레임 i에 대해, 다른 각 세그먼트 e에서 시간 대역 τ=0.3 내의 프레임을 후보로 선택합니다: C_{i,e} = {j : ep(j)=e, |g_j - g_i| ≤ τ}.
3. **최적 대표 선택**: 각 세그먼트의 후보 중 쿼리 프레임과 가장 유사한 프레임만 유지합니다: j*_{i,e} = argmax_{j∈C_{i,e}} f_i^T f_j.
4. **유사도 필터링**: 최적 대표 유사도가 임계값 ρ=0.90보다 낮으면 해당 세그먼트 기여를 폐기합니다.
5. **세그먼트 균형 평균**: 남은 세그먼트 대표가 집합 M_i를 구성하고, 수정 추정치는 ĝ_i = (1/|M_i|) Σ_{e∈M_i} g_{j*_{i,e}}입니다. 대표가 없으면 원래 값을 유지합니다.

### 핵심 설계 결정
- **세그먼트당 하나의 매칭만 기여**: 시간적으로 인접한 프레임의 과도한 가중치를 방지합니다. 동일 세그먼트 내 오류는 상관되어 있고, 교차 세그먼트 평균만이 독립적 노이즈를 줄일 수 있기 때문입니다.
- **시간 대역 τ가 수정 범위 제한**: 평균화되는 모든 라벨이 |g_j - g_i| ≤ τ를 만족하므로 수정은 |ĝ_i - g_i| ≤ τ로 제한되어 비정상적 점프를 방지합니다.
- **유사도 임계값 ρ의 보수적 필터링**: 충분히 유사한 상태만 추정에 참여하도록 보장하여 관련 없는 세그먼트의 노이즈 유입을 방지합니다.

### 어드밴티지 라벨 구성
프레임 i에서 시작하는 시야 H의 액션 블록에 대해, 어드밴티지 라벨은 r_i = ĝ_{i+H} - ĝ_i입니다. 세그먼트 끝 근처에서는 시야 비율로 재조정됩니다: r_i = (H/(T_e - i))(ĝ_{T_e} - ĝ_i). r_i로 정렬한 후 상위 20%를 양성 어드밴티지 예시로 표시하고, 훈련 시 텍스트 접미사 "…, advantage: positive"를 추가합니다.

## 핵심 혁신

1. **훈련 불필요 라벨 수정 패러다임**: UR-VC는 모델 훈련, 온라인 롤아웃, 수동 라벨링이 전혀 필요 없으며, 오프라인 코퍼스에서의 행렬 연산만으로 수정을 완료합니다. 따라서 기존 파이프라인의 시간 파생 라벨을 직접 대체하는 플러그 앤 플레이 모듈로 사용할 수 있습니다.

2. **세그먼트 균형 교차 세그먼트 매칭**: 단순한 최근접 이웃 검색과 달리, UR-VC는 각 세그먼트가 최대 하나의 매칭 라벨만 기여하도록 강제합니다. 이 설계는 통계적으로 더 합리적입니다. 독립 세그먼트 간의 평균은 궤적 특정 노이즈를 줄일 수 있지만, 동일 세그먼트 내 인접 프레임의 오류는 높은 상관관계가 있어 반복적으로 가중치를 부여해서는 안 되기 때문입니다.

3. **비단조 진행도의 명시적 모델링**: 수정된 라벨이 음의 어드밴티지를 갖도록 허용함으로써(실험에서 13.4%의 프레임이 음의 시야 어드밴티지 획득), UR-VC는 무감독 조건에서 물리적 진행도 후퇴 현상을 처음으로 포착합니다. 이는 시간 파생 라벨로는 전혀 표현할 수 없는 정보입니다.

## 실험 및 결과

실험은 실제 양팔 직물 펼치기-접기 작업에서 수행되었으며, 주요 평가 세트는 150개의 실제 로봇 세그먼트이고, 훈련 혼합은 5700개의 펼치기-접기 시연과 1795개의 복구 시연을 포함합니다.

### 커버리지 및 수정 품질
| 지표 | 150 세그먼트 | 10^4 세그먼트 |
|------|----------|-----------|
| 커버리지(유사도 ≥ 0.90) | 98% | 99.9% |
| 커버리지(유사도 ≥ 0.955) | 69.9% | 90.4% |
| 수정 추정치 거칠기(mean \|Δ²ĝ_t\|) | 기준 | 약 1/3 감소 |

수정 추정치와 정규화된 시간의 전체 상관관계는 0.98로 높지만, 13.4%의 프레임이 음의 시야 어드밴티지(시야는 세그먼트 길이의 5%, 약 1.7초)를 획득하여 비단조 진행도가 효과적으로 포착되었음을 보여줍니다.

### 하위 실제 로봇 평가
| 테이블 조건 | Baseline | UR-VC |
|----------|----------|-------|
| Bare table | 0.90 | 0.97 |
| Beige cloth | 0.70 | 0.73 |
| Blue-gray cloth | 0.50 | 0.43 |
| Light-yellow cloth | 0.63 | 0.90 |
| Light-gray cloth | 0.77 | 0.80 |
| Khaki cloth | 0.87 | 0.90 |
| **평균** | **0.728** | **0.789** |

UR-VC는 6가지 조건 중 5가지에서 성공률이 더 높았으며, 평균 성공률은 0.728(131/180)에서 0.789(142/180)로 약 6.1% 포인트(표 내 값 0.728→0.789로 계산) 향상되었습니다. 유일하게 성능이 하락한 조건은 Blue-gray cloth로, 해당 배경에서의 시각적 검색 품질과 관련이 있을 수 있습니다.

## 경계 및 한계

UR-VC의 핵심 가정은 시각적 유사성이 물리적 진행도 유사성과 같다는 것이지만, 유사한 시각적 상태가 다른 작업 단계나 다른 동작 이력 이후에 나타날 때 잠재적 진행도가 모호해질 수 있어 이 가정이 실패할 수 있습니다. 세그먼트 균형 평균은 궤적 특정 노이즈를 줄일 수 있지만 체계적 검색 오류는 수정할 수 없습니다. 검색 풀 자체에 편향이 있으면 수정 결과도 해당 편향을 상속받습니다. 논문은 UR-VC가 비직물 조작(예: 강체 조립)이나 더 복잡한 다단계 작업에서의 성능을 명시하지 않았으며, 하이퍼파라미터 τ와 ρ의 민감도도 탐구하지 않았습니다. 저자는 실제 물리적 진행도의 ground-truth에 접근한다고 명시적으로 주장하지 않으므로, 수정 품질 평가는 하위 작업 성공률이라는 간접 지표에만 의존합니다.

## 엔지니어링 시사점

UR-VC를 재현할 때 먼저 임베딩 모델 선택을 확인하십시오. SigLIP-2의 시각적 특징 품질이 검색 신뢰성을 직접 결정하므로, 인코더를 교체하면 커버리지를 다시 검증해야 합니다. 시간 대역 τ=0.3과 유사도 임계값 ρ=0.90은 직물 조작에 맞게 튜닝된 것이므로, 다른 작업으로 전환할 때 먼저 커버리지-임계값 곡선을 그려 최소 90%의 프레임이 매칭 대표를 갖도록 해야 합니다. 가장 실수하기 쉬운 부분은 인덱스 규칙입니다. 논문은 1-시작 인덱스(o_1^(e), …, o_{T_e}^(e))를 사용하므로, 구현에서 0-시작 인덱스를 사용하면 세그먼트 끝의 시야 비율 공식 분모를 조정해야 합니다. 하위 팀의 경우, 먼저 소규모 검색 풀(예: 50 세그먼트)에서 수정 라벨의 거칠기 감소 추세를 검증한 다음 전체 데이터로 확장하는 것이 좋습니다. 커버리지가 부족하면 임계값을 낮추기보다 검색 풀 크기를 늘리는 것이 우선입니다. 10^4 세그먼트 규모에서 커버리지는 99.9%까지 향상될 수 있기 때문입니다. 배포 시 양성 어드밴티지 접미사 구성은 훈련과 완전히 일치해야 합니다. 그렇지 않으면 정책이 쿼리 의미를 올바르게 이해하지 못할 수 있습니다.
