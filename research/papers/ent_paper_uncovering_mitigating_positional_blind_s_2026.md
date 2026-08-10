---
$id: ent_paper_uncovering_mitigating_positional_blind_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Uncovering and Mitigating Positional Blind Spots in Vision-Language-Action Models
  zh: Uncovering and Mitigating Positional Blind Spots in Vision-Language-Action Models
  ko: Uncovering and Mitigating Positional Blind Spots in Vision-Language-Action Models
summary:
  en: 'Recent Vision-Language-Action (VLA) models achieve promising performance in robotic manipulation, typically measured
    by success rates aggregated over predefined object configurations, an evaluation that implicitly assumes spatially uniform
    competence across the workspace. However, this assumption does not hold: even with the instruction and every other scene
    factor held fixed, merely relocating a.'
  zh: 本文提出并系统研究了视觉-语言-动作模型（VLA）中的位置性盲区（Positional Blind Spots, PBS）现象，即模型在连续工作空间中特定局部区域表现出的系统性失败。作者设计了一个两阶段黑盒框架，先通过离散化网格与似然比检验高效定位PBS，再利用定位结果引导LoRA微调进行针对性缓解，在五个VLA模型和两个基准上验证了方法的有效性与泛化性。
  ko: 'Recent Vision-Language-Action (VLA) models achieve promising performance in robotic manipulation, typically measured
    by success rates aggregated over predefined object configurations, an evaluation that implicitly assumes spatially uniform
    competence across the workspace. However, this assumption does not hold: even with the instruction and every other scene
    factor held fixed, merely relocating a.'
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
- uncovering
- mitigating
- positional
- blind
- s
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
  title: arXiv:2608.01573 Uncovering and Mitigating Positional Blind Spots in Vision-Language-Action Model
  url: https://arxiv.org/abs/2608.01573
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---

## 概述

本文提出并系统研究了视觉-语言-动作模型（VLA）中的位置性盲区（Positional Blind Spots, PBS）现象，即模型在连续工作空间中特定局部区域表现出的系统性失败。作者设计了一个两阶段黑盒框架，先通过离散化网格与似然比检验高效定位PBS，再利用定位结果引导LoRA微调进行针对性缓解，在五个VLA模型和两个基准上验证了方法的有效性与泛化性。

## 它改变了什么

现有VLA评估范式存在一个根本性盲区：默认模型能力在工作空间内空间均匀，因此仅报告预定义对象配置上的平均成功率。本文揭示这一假设在具身任务中不成立——仅移动任务无关干扰物，就能在局部空间连贯区域内显著提高失败概率，且该现象在五个主流VLA模型中普遍存在（穷举评估显示所有策略失败率范围为0.15至0.58）。这一发现将评估粒度从“任务级平均”推进到“空间单元级”，改变了我们对VLA鲁棒性来源的理解：失败并非随机噪声，而是具有空间结构、可预测、可干预的系统性缺陷。

更重要的是，本文改变了“发现问题”与“解决问题”之间的连接方式。以往鲁棒性研究多停留在诊断层面，或依赖随机数据增强进行隐式缓解。本文证明，通过主动搜索定位高风险区域，并用极小量（980次策略执行）的定向演示数据进行LoRA微调，即可将位置脆弱性指标（LLR）降低92.61%–99.93%，同时保持策略原生训练目标与超参数不变。这为VLA部署前的空间安全审计提供了可操作范式。

## 方法拆解

### 阶段一：PBS发现（黑盒搜索）
- 将可行干扰物放置区域 Ω ⊂ ℝ² 离散化为 N×N 均匀网格，共 N² 个单元 {gᵢ}。
- 每个单元 gᵢ 均匀采样 K 个有效位置，每个位置执行一次完整rollout，总预算 Q = N²K（默认 N=7, K=20, Q=980）。
- 记录每单元失败数 cᵢ，计算经验失败概率 p̂ᵢ = cᵢ/K。
- 对每单元计算 **Log-Likelihood Ratio (LLR) 分数**：零假设为单元失败概率等于其余工作空间；备择假设为单元内失败概率更高。当单元内经验失败概率不超过其余工作空间时，LLR 设为零。
- 按 LLR 降序排列，保留得分最高的 M 个单元作为预测 PBS 集合 B̂；相邻选中单元合并为同一盲区。

### 阶段二：PBS引导的缓解
- 从 B̂ 中采样 N_demo 个有效干扰物位置 zⱼ，人类专家遥操作收集成功演示轨迹 τⱼ(zⱼ)。
- 使用策略原生训练目标 L_native，通过 **LoRA** 优化可训练参数 φ：
  φ* = argmin_φ (1/N_demo) Σⱼ L_native(π_{θ,φ}; τⱼ)
- 保留原始观测空间、动作表示、优化目标和训练超参数，仅更新 LoRA 引入的参数。

### 关键设计决策
- **均匀分配rollout**：使各单元失败风险估计可比，避免采样偏差。
- **LLR而非经验失败概率**：经验失败概率无法区分局部位置脆弱性与策略整体失败率（单元可能因任务本身困难而失败率高）。
- **黑盒设置**：策略仅通过完整rollout查询，仅观察二元成功/失败结果，无需访问策略内部，适用于任何不可微或闭源策略。

## 关键创新

1. **首次形式化定义并量化VLA的位置性盲区**：通过LLR与Global Moran's I两个指标，将“空间非均匀失败”从定性观察转化为可量化、可比较的工程指标。表I显示所有模型在缓解前均表现出显著空间聚集性（Moran's I 0.49–0.86），证实PBS是跨架构的普遍现象而非个别模型缺陷。

2. **黑盒、预算受限的PBS定位算法**：在无梯度、无置信度、仅二元反馈的约束下，用LLR排序替代简单失败率排序，在980次执行（仅为穷举评估十分之一）内实现平均F1-score 0.678，较随机搜索提升0.268、较自适应采样提升0.178。LLR的关键创新在于通过对比单元内与其余工作空间的失败率，消除了任务固有难度对定位的干扰。

3. **“定位-缓解”闭环**：将PBS发现结果直接转化为LoRA微调数据，形成从诊断到修复的完整链路。缓解后LLR降低92.61%–99.93%，且跨基准泛化实验（表VI）显示微调后模型在未见基准上成功率从0.04提升至0.14，证明针对PBS的定向数据比随机数据更有效地提升空间鲁棒性。

## 实验与结果

### 表I：位置脆弱性量化（Pre-Mitigation vs Post-Mitigation）

| 模型 | 基准 | LLR ↓ (前→后) | Moran's I ↓ (前→后) | FR ↓ (前→后) |
|---|---|---|---|---|
| π₀ | LIBERO | 644.03→0.43 | 0.70→0.24 | 0.27→0.04 |
| π₀.₅ | LIBERO | 950.42→8.17 | 0.86→0.28 | 0.31→0.16 |
| OpenVLA-OFT | LIBERO | 1954.03→80.59 | 0.75→0.31 | 0.33→0.11 |
| UniVLA | LIBERO | 445.10→1.25 | 0.49→0.29 | 0.15→0.09 |
| VLA-Adapter | LIBERO | 776.31→8.58 | 0.55→0.22 | 0.36→0.15 |
| π₀ | VLA-Arena | 491.05→7.32 | 0.61→0.29 | 0.49→0.16 |
| π₀.₅ | VLA-Arena | 55.51→4.10 | 0.21→0.24 | 0.36→0.10 |
| OpenVLA-OFT | VLA-Arena | 631.02→5.95 | 0.66→0.27 | 0.58→0.26 |
| UniVLA | VLA-Arena | 969.56→6.74 | 0.45→0.21 | 0.24→0.07 |

### 表II：PBS发现性能（平均）

| 方法 | Prec. ↑ | Rec. ↑ | F1 ↑ | IoU ↑ |
|---|---|---|---|---|
| Random | 0.366 | 0.490 | 0.410 | 0.270 |
| Adaptive | 0.456 | 0.598 | 0.500 | 0.352 |
| Ours | 0.636 | 0.824 | 0.678 | 0.528 |

### 表III：搜索粒度消融（N ∈ {4,5,6,7,8}, K=20）

| 指标 / N | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|
| F1-score ↑ | 0.52 | 0.62 | 0.69 | 0.84 | 0.58 |
| IoU ↑ | 0.35 | 0.45 | 0.53 | 0.72 | 0.41 |

### 表IV：缓解轮次消融（π₀.₅, LIBERO）

| 指标 / r | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| LLR ↓ | 950.42 | 8.17 | 3.47 | 2.64 |
| FR ↓ | 0.31 | 0.16 | 0.08 | 0.10 |

**关键结论**：缓解后LLR降低92.61%–99.93%，FR降低40.00%–85.19%（由表内数值计算）。搜索策略平均F1-score 0.678，优于随机搜索0.268、优于自适应采样0.178。搜索预算980次仅为穷举评估执行次数的十分之一。N=7为最优搜索粒度，第一轮缓解贡献主要改善，后续轮次改善有限且非单调。

## 边界与局限

- **残余空间相关性**：π₀.₅在VLA-Arena上缓解后Moran's I从0.21略增至0.24，表明少量残余失败仍局部相关，LLR与FR的降低并未完全消除空间聚集性。
- **缓解轮次的非单调性**：表IV显示第二轮后FR从0.08回升至0.10，说明过度微调可能引入新的脆弱性，作者默认采用一轮缓解作为鲁棒性与适配成本之间的实际权衡。
- **基准覆盖不全**：VLA-Adapter未在VLA-Arena上评估（无公开适配检查点），跨基准泛化实验仅针对π₀.₅，其他模型的跨基准表现论文未明确。
- **搜索空间假设**：方法假设PBS存在于干扰物放置的二维平面内，未考虑物体姿态、光照、背景纹理等其他空间因素；对三维空间或更高维配置空间的适用性论文未明确。
- **演示数据依赖**：缓解阶段依赖人类专家遥操作收集成功演示，在复杂长程任务中演示成本可能显著上升，论文未明确演示数量N_demo的具体取值。

## 工程启示

- **复现时先核对搜索网格与预算**：默认配置为N=7、K=20、Q=980，表III显示N=7为最优（F1=0.84），N=8时性能骤降（F1=0.58），说明网格过密导致每单元样本不足，复现时应严格保持N与K的比例关系。
- **LLR实现细节是关键**：LLR分数在单元内经验失败概率不超过其余工作空间时设为零，这一截断操作直接影响PBS集合的排序与召回率，实现时务必确认零假设的对比基准是“其余所有单元”而非“全局平均”。
- **缓解阶段最容易踩坑的是LoRA超参数**：作者强调保留原始观测空间、动作表示、优化目标和训练超参数，仅更新LoRA参数。若在微调时改动学习率或优化器，可能破坏策略原有行为，导致缓解后FR不降反升（如表IV第二轮所示）。
- **下游团队部署前应执行空间审计**：即使模型在基准上平均成功率达标，仍可能存在局部盲区。建议用本文框架以980次rollout预算（约数小时机器人时间）完成空间风险测绘，优先对高风险区域补充演示数据。
- **跨基准泛化需单独验证**：表VI显示微调后模型在VLABench上成功率仍为0.00，说明PBS缓解可能不迁移到分布差异较大的场景，跨基准部署前应重新执行PBS发现流程。

## Overview
Recent Vision-Language-Action (VLA) models achieve promising performance in robotic manipulation, typically measured by success rates aggregated over predefined object configurations, an evaluation that implicitly assumes spatially uniform competence across the workspace. However, this assumption does not hold: even with the instruction and every other scene factor held fixed, merely relocating a task-irrelevant distractor can sharply raise the failure probability within localized, spatially coherent regions, which we term Positional Blind Spots (PBS). In this paper, we propose a two-stage black-box framework to uncover and mitigate PBS. During the uncovering stage, we grid the workspace and apply a one-sided log-likelihood-ratio test to localize PBS cells with significantly elevated risk. During the mitigation stage, we fine-tune the policy via LoRA on demonstrations collected from these PBS regions, improving competence there while largely preserving performance across the rest of the workspace. We evaluate our framework on five state-of-the-art VLA policies across two benchmarks, and find that PBS are pervasive and spatially concentrated in all of them, with failure rates up to 0.58. Our search strategy achieves an average F1-score of 0.678, outperforming random search and adaptive sampling baselines by 0.268 and 0.178, respectively. Guided by the discovered regions, targeted fine-tuning reduces the overall failure rate by 40.00%--85.19%.

## 参考
- https://arxiv.org/abs/2608.01573

## 개요

본 논문은 비전-언어-행동 모델(VLA)에서의 위치적 맹점(Positional Blind Spots, PBS) 현상, 즉 모델이 연속 작업 공간의 특정 국소 영역에서 보이는 체계적 실패를 제안하고 체계적으로 연구한다. 저자들은 두 단계 블랙박스 프레임워크를 설계하여, 먼저 이산화된 그리드와 우도비 검정을 통해 PBS를 효율적으로 위치 파악하고, 이후 위치 파악 결과를 활용해 LoRA 미세 조정을 유도하여 표적화된 완화를 수행한다. 다섯 개의 VLA 모델과 두 개의 벤치마크에서 방법의 효율성과 일반화를 검증한다.

## 그것이 바꾸는 것

기존 VLA 평가 패러다임에는 근본적인 맹점이 있다: 모델 능력이 작업 공간 내에서 공간적으로 균일하다는 기본 가정으로, 따라서 사전 정의된 객체 구성에서의 평균 성공률만 보고한다. 본 논문은 이 가정이 구현 작업에서 성립하지 않음을 밝힌다—작업과 무관한 방해물을 이동시키기만 해도 국소 공간의 연결된 영역에서 실패 확률이 유의미하게 증가하며, 이 현상은 다섯 개의 주류 VLA 모델에서 보편적으로 존재한다(완전 평가 결과 모든 정책의 실패율 범위는 0.15~0.58). 이 발견은 평가의 세분성을 "작업 수준 평균"에서 "공간 단위 수준"으로 전환하여 VLA 견고성의 원천에 대한 우리의 이해를 바꾼다: 실패는 무작위 잡음이 아니라 공간 구조를 가지며 예측 가능하고 개입 가능한 체계적 결함이다.

더 중요하게, 본 논문은 "문제 발견"과 "문제 해결" 사이의 연결 방식을 바꾼다. 기존 견고성 연구는 주로 진단 수준에 머물거나 무작위 데이터 증강을 통한 암시적 완화에 의존했다. 본 논문은 능동적 탐색으로 고위험 영역을 위치 파악하고 극소량(980회 정책 실행)의 표적화된 시연 데이터로 LoRA 미세 조정을 수행하면 위치 취약성 지표(LLR)를 92.61%–99.93% 감소시키면서 정책의 원래 훈련 목표와 하이퍼파라미터를 유지할 수 있음을 증명한다. 이는 VLA 배포 전 공간 안전 감사를 위한 실행 가능한 패러다임을 제공한다.

## 방법 분해

### 1단계: PBS 발견(블랙박스 탐색)
- 가능한 방해물 배치 영역 Ω ⊂ ℝ²를 N×N 균일 그리드로 이산화하여 총 N²개의 셀 {gᵢ}를 생성한다.
- 각 셀 gᵢ에서 K개의 유효 위치를 균일하게 샘플링하고, 각 위치에서 전체 롤아웃을 한 번 실행하며, 총 예산은 Q = N²K(기본값 N=7, K=20, Q=980)이다.
- 각 셀의 실패 수 cᵢ를 기록하고 경험적 실패 확률 p̂ᵢ = cᵢ/K를 계산한다.
- 각 셀에 대해 **로그 우도비(LLR) 점수**를 계산한다: 귀무가설은 셀의 실패 확률이 나머지 작업 공간과 동일하다는 것이고, 대립가설은 셀 내 실패 확률이 더 높다는 것이다. 셀 내 경험적 실패 확률이 나머지 작업 공간을 초과하지 않으면 LLR은 0으로 설정된다.
- LLR 내림차순으로 정렬하고, 점수가 가장 높은 M개의 셀을 예측 PBS 집합 B̂로 유지한다; 인접한 선택된 셀은 동일한 맹점으로 병합된다.

### 2단계: PBS 유도 완화
- B̂에서 N_demo개의 유효 방해물 위치 zⱼ를 샘플링하고, 인간 전문가가 원격 조작으로 성공적인 시연 궤적 τⱼ(zⱼ)를 수집한다.
- 정책의 원래 훈련 목표 L_native를 사용하여 **LoRA**로 훈련 가능한 매개변수 φ를 최적화한다:
  φ* = argmin_φ (1/N_demo) Σⱼ L_native(π_{θ,φ}; τⱼ)
- 원래 관측 공간, 행동 표현, 최적화 목표 및 훈련 하이퍼파라미터를 유지하고 LoRA로 도입된 매개변수만 업데이트한다.

### 핵심 설계 결정
- **롤아웃 균등 배분**: 각 셀의 실패 위험 추정을 비교 가능하게 하여 샘플링 편향을 방지한다.
- **경험적 실패 확률 대신 LLR**: 경험적 실패 확률은 국소 위치 취약성과 정책의 전체 실패율을 구분할 수 없다(셀은 작업 자체가 어려워 실패율이 높을 수 있음).
- **블랙박스 설정**: 정책은 전체 롤아웃을 통해서만 쿼리되며 이진 성공/실패 결과만 관찰되고 정책 내부에 접근할 필요가 없으므로 미분 불가능하거나 폐쇄된 정책에 적용 가능하다.

## 핵심 혁신

1. **VLA의 위치적 맹점을 최초로 공식적으로 정의하고 정량화**: LLR과 Global Moran's I 두 지표를 통해 "공간적 비균일 실패"를 정성적 관찰에서 정량적이고 비교 가능한 엔지니어링 지표로 전환한다. 표 I은 모든 모델이 완화 전 유의미한 공간 집적성을 보임을 보여주며(Moran's I 0.49–0.86), PBS가 개별 모델의 결함이 아닌 아키텍처 전반의 보편적 현상임을 확인한다.

2. **블랙박스, 예산 제한 PBS 위치 파악 알고리즘**: 기울기 없음, 신뢰도 없음, 이진 피드백만 있는 제약 하에서 단순 실패율 정렬 대신 LLR 정렬을 사용하여 980회 실행(완전 평가의 10분의 1) 내에 평균 F1-score 0.678을 달성하며, 무작위 탐색 대비 0.268, 적응형 샘플링 대비 0.178 향상된다. LLR의 핵심 혁신은 셀 내부와 나머지 작업 공간의 실패율을 대조하여 작업 고유의 난이도가 위치 파악에 미치는 간섭을 제거하는 것이다.

3. **"위치 파악-완화" 폐루프**: PBS 발견 결과를 직접 LoRA 미세 조정 데이터로 변환하여 진단에서 수리까지의 완전한 체인을 형성한다. 완화 후 LLR은 92.61%–99.93% 감소하며, 교차 벤치마크 일반화 실험(표 VI)은 미세 조정된 모델이 보지 못한 벤치마크에서 성공률이 0.04에서 0.14로 향상됨을 보여준다. 이는 PBS를 대상으로 한 표적 데이터가 무작위 데이터보다 공간 견고성을 더 효과적으로 향상시킴을 증명한다.

## 실험 및 결과

### 표 I: 위치 취약성 정량화(완화 전 vs 완화 후)

| 모델 | 벤치마크 | LLR ↓ (전→후) | Moran's I ↓ (전→후) | FR ↓ (전→후) |
|---|---|---|---|---|
| π₀ | LIBERO | 644.03→0.43 | 0.70→0.24 | 0.27→0.04 |
| π₀.₅ | LIBERO | 950.42→8.17 | 0.86→0.28 | 0.31→0.16 |
| OpenVLA-OFT | LIBERO | 1954.03→80.59 | 0.75→0.31 | 0.33→0.11 |
| UniVLA | LIBERO | 445.10→1.25 | 0.49→0.29 | 0.15→0.09 |
| VLA-Adapter | LIBERO | 776.31→8.58 | 0.55→0.22 | 0.36→0.15 |
| π₀ | VLA-Arena | 491.05→7.32 | 0.61→0.29 | 0.49→0.16 |
| π₀.₅ | VLA-Arena | 55.51→4.10 | 0.21→0.24 | 0.36→0.10 |
| OpenVLA-OFT | VLA-Arena | 631.02→5.95 | 0.66→0.27 | 0.58→0.26 |
| UniVLA | VLA-Arena | 969.56→6.74 | 0.45→0.21 | 0.24→0.07 |

### 표 II: PBS 발견 성능(평균)

| 방법 | Prec. ↑ | Rec. ↑ | F1 ↑ | IoU ↑ |
|---|---|---|---|---|
| Random | 0.366 | 0.490 | 0.410 | 0.270 |
| Adaptive | 0.456 | 0.598 | 0.500 | 0.352 |
| Ours | 0.636 | 0.824 | 0.678 | 0.528 |

### 표 III: 탐색 세분성 소거(N ∈ {4,5,6,7,8}, K=20)

| 지표 / N | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|
| F1-score ↑ | 0.52 | 0.62 | 0.69 | 0.84 | 0.58 |
| IoU ↑ | 0.35 | 0.45 | 0.53 | 0.72 | 0.41 |

### 표 IV: 완화 라운드 소거(π₀.₅, LIBERO)

| 지표 / r | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| LLR ↓ | 950.42 | 8.17 | 3.47 | 2.64 |
| FR ↓ | 0.31 | 0.16 | 0.08 | 0.10 |

**핵심 결론**: 완화 후 LLR은 92.61%–99.93% 감소하고 FR은 40.00%–85.19% 감소한다(표 내 수치로 계산). 탐색 전략의 평균 F1-score는 0.678로 무작위 탐색보다 0.268, 적응형 샘플링보다 0.178 우수하다. 탐색 예산 980회는 완전 평가 실행 횟수의 10분의 1에 불과하다. N=7이 최적 탐색 세분성이며, 첫 번째 완화 라운드가 주요 개선을 기여하고 이후 라운드의 개선은 제한적이고 비단조적이다.

## 경계 및 한계

- **잔여 공간 상관성**: π₀.₅는 VLA-Arena에서 완화 후 Moran's I가 0.21에서 0.24로 약간 증가하여 소량의 잔여 실패가 여전히 국소적으로 상관되어 있음을 보여준다. LLR과 FR의 감소가 공간 집적성을 완전히 제거하지는 못한다.
- **완화 라운드의 비단조성**: 표 IV는 두 번째 라운드 후 FR이 0.08에서 0.10으로 회복됨을 보여주며, 과도한 미세 조정이 새로운 취약성을 도입할 수 있음을 시사한다. 저자는 기본적으로 견고성과 적응 비용 사이의 실용적 절충으로 한 라운드 완화를 채택한다.
- **벤치마크 커버리지 불완전**: VLA-Adapter는 VLA-Arena에서 평가되지 않았으며(공개 적응 체크포인트 없음), 교차 벤치마크 일반화 실험은 π₀.₅에만 국한되고 다른 모델의 교차 벤치마크 성능은 논문에 명시되지 않았다.
- **탐색 공간 가정**: 방법은 PBS가 방해물 배치의 2차원 평면에 존재한다고 가정하며, 객체 자세, 조명, 배경 질감 등 다른 공간 요인을 고려하지 않는다; 3차원 공간 또는 더 높은 차원 구성 공간에 대한 적용 가능성은 논문에 명시되지 않았다.
- **시연 데이터 의존성**: 완화 단계는 인간 전문가의 원격 조작으로 성공적인 시연을 수집하는 데 의존하며, 복잡한 장기 작업에서는 시연 비용이 크게 증가할 수 있다. 논문은 N_demo의 구체적인 값을 명시하지 않았다.

## 공학적 시사점

- **재현 시 탐색 그리드와 예산을 먼저 확인**: 기본 구성은 N=7, K=20, Q=980이며, 표 III은 N=7이 최적(F1=0.84)이고 N=8에서 성능이 급락(F1=0.58)함을 보여준다. 이는 그리드가 너무 조밀하면 셀당 샘플이 부족해짐을 의미하므로, 재현 시 N과 K의 비율 관계를 엄격히 유지해야 한다.
- **LLR 구현 세부 사항이 핵심**: LLR 점수는 셀 내 경험적 실패 확률이 나머지 작업 공간을 초과하지 않을 때 0으로 설정된다. 이 절단 연산은 PBS 집합의 정렬과 재현율에 직접 영향을 미치므로, 구현 시 귀무가설의 비교 기준이 "전체 평균"이 아닌 "나머지 모든 셀"임을 반드시 확인해야 한다.
- **완화 단계에서 가장 함정이 많은 부분은 LoRA 하이퍼파라미터**: 저자는 원래 관측 공간, 행동 표현, 최적화 목표 및 훈련 하이퍼파라미터를 유지하고 LoRA 매개변수만 업데이트할 것을 강조한다. 미세 조정 시 학습률이나 옵티마이저를 변경하면 정책의 원래 행동을 파괴하여 완화 후 FR이 오히려 증가할 수 있다(표 IV 두 번째 라운드 참조).
- **하위 팀은 배포 전 공간 감사를 수행해야 함**: 모델이 벤치마크에서 평균 성공률 기준을 충족하더라도 국소 맹점이 존재할 수 있다. 본 프레임워크로 980회 롤아웃 예산(약 수 시간의 로봇 시간)으로 공간 위험 매핑을 완료하고 고위험 영역에 우선적으로 시연 데이터를 보충할 것을 권장한다.
- **교차 벤치마크 일반화는 별도 검증 필요**: 표 VI는 미세 조정된 모델이 VLABench에서 성공률이 여전히 0.00임을 보여주며, PBS 완화가 분포 차이가 큰 시나리오로 전이되지 않을 수 있음을 시사한다. 교차 벤치마크 배포 전에 PBS 발견 프로세스를 다시 실행해야 한다.
