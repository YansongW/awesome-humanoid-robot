---
$id: ent_paper_developing_combined_manipulation_locomot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill Composition
  zh: Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill Composition
  ko: Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill Composition
summary:
  en: This paper addresses how to enable a humanoid robot to learn motion policies based on developmental principles and combine
    policies to create more sophisticated and useful behaviors. Specifically, we present an approach to (1) learning a whole-body
    reaching and grasping policy and (2) combining it and a standing-up and walking policy to compose a more complex policy
    of manipulation and.
  zh: 本文提出一套基于发展心理学原理的类人机器人操作与移动技能学习框架，核心贡献包括：立方谐波加权空间卷积（CHWSC）与反比例缩放距离场（ISDF）构成的手-物交互紧凑表征、受发展原则启发的成就触发奖励图与渐进式手指关节解耦，以及跨具身策略组合方法。作者在Isaac
    Gym中训练72-DoF类人机器人完成“伸手抓取→站立→行走”的复合任务，零样本抓取未见物体成功率最高达98%。
  ko: This paper addresses how to enable a humanoid robot to learn motion policies based on developmental principles and combine
    policies to create more sophisticated and useful behaviors. Specifically, we present an approach to (1) learning a whole-body
    reaching and grasping policy and (2) combining it and a standing-up and walking policy to compose a more complex policy
    of manipulation and.
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
- developing
- combined
- manipulation
- locomot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: arXiv:2608.00208 Developing Combined Manipulation and Locomotion Skills with Interaction Represen
  url: https://arxiv.org/abs/2608.00208
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一套基于发展心理学原理的类人机器人操作与移动技能学习框架，核心贡献包括：立方谐波加权空间卷积（CHWSC）与反比例缩放距离场（ISDF）构成的手-物交互紧凑表征、受发展原则启发的成就触发奖励图与渐进式手指关节解耦，以及跨具身策略组合方法。作者在Isaac Gym中训练72-DoF类人机器人完成“伸手抓取→站立→行走”的复合任务，零样本抓取未见物体成功率最高达98%。

## 它改变了什么

这项工作的真正改变在于：它把“操作技能学习”从依赖大规模人类演示或预训练视觉-语言模型的范式，拉回到“紧凑几何表征+结构化奖励塑形”的经典RL路线，同时证明了这种路线在类人机器人全身控制上的可行性。作者没有追逐端到端大模型潮流，而是用距离场和立方谐波这种低维、可解释的几何特征，让策略在4096并行环境下仅用PPO就能学会精细抓取——这对资源受限的机器人实验室有直接吸引力。

更关键的是，它直面了“技能组合”这个被多数工作回避的工程难题：独立训练的技能如何在推理时无缝拼接。作者用“在完整身体上训练”这一反直觉的结论（无手指机器人上训练的站立策略迁移到有手指机器人时成功率从100%暴跌至31%），揭示了具身不匹配对即插即用组合的致命影响。这改变了人们对“技能模块化”的乐观假设——模块化不是免费的，它需要训练时就在目标具身上进行。

## 方法拆解

### 问题形式化与架构无关性
- 使用PPO训练策略，输入观测向量（含肢体姿态、关节力等），输出关节力矩命令。
- 方法仅涉及预计算观测、预处理动作、设计奖励，不绑定特定RL算法或网络结构。

### 手-物交互表征
- **ISDF**：\( I(i) = \min(1, \exp(-\alpha \cdot S(i))) \)，\(\alpha\)为固定正超参数；负距离（穿透）截断为1。
- **CHWSC**：\( \text{CHWSC}(l) = \sum_{\ell=0}^{l} \sum_j I(f_j) \cdot K_\ell^m(f_j/\|f_j\|) \)，用立方谐波作为权重与各手指段到物体的ISDF卷积；排除数值不稳定的不对称谐波（\(K_2^{-1}, K_4^{-4}, K_4^{-2}, K_6^{-6}, K_6^{-3}\)）。

### 手-物交互评分（5个指标）
1. 手-物接近度：\(I(h)\)
2. 内法线对齐：\(-n_f \cdot n_\Omega\)
3. 手指-物体接近度：\(\text{avg}_j(I(f_j))\)
4. 物体-手指接近度：\(\text{avg}_k(\exp(-\alpha \cdot \min_j\|f_j - \Omega_k\|))\)，按曲率匹配采样
5. 包裹度：\(\exp(-\alpha\|c_{obj} - c_{fingers}\|)\)

### 手指关节解耦
- 每集开始所有手指关节接收平均力矩命令；训练中按近端到远端顺序逐步解耦。
- **个体解耦**：每100步解耦一次，t=800后开始。
- **分组解耦**：每500步解耦一次，同类型关节一起解耦。

### 成就触发奖励
- 里程碑组织为有向无环图，含强制/非强制两种成就分数：
  - 强制：\(A_{i,j,t}^E = r_{i,t} - p_{i,j}\)（用瞬时奖励）
  - 非强制：\(A_{i,j,t}^N = \max_{t^* \le t}\{r_{i,t^*}\} - p_{i,j}\)（用历史最大奖励）
- 总奖励：\( r_t = \sum_j \text{pow}(L_j, w) \cdot \sum_i \max(0, A_{i,j,t}) \cdot r_{j,t} \)，\(w=2\)。

### 策略组合
- 多策略RL播放器，统一观测向量通过索引提取各子任务独立观测。
- 抓取策略控制所有关节；物体被抓取后（通过“手指段接触百分比”里程碑），站立策略接管除手指外的身体关节。

## 关键创新

1. **CHWSC+ISDF的几何表征**：首次将立方谐波（源自原子轨道形状）用于手-物交互的空间卷积，在物体参考系中同时捕捉距离场的径向分量和手指环绕的角度分布。相比原始距离场或原始点云，这种低维嵌入（44×2）让策略在未见物体上零样本泛化（球体98%、长方体94%），且消融显示CHWSC阶数从6降到0时成功率从93%归零——证明角度信息是抓取成功的关键。

2. **成就触发奖励图**：将任务分解为带通过阈值的里程碑DAG，用“历史最大奖励”的非强制分数处理可牺牲的前置条件，用“瞬时奖励”的强制分数处理必须保持的状态（如预抓取）。这种设计避免了稀疏奖励下的探索困难，且不依赖任何奖励塑形先验，是纯结构化的课程学习替代方案。

3. **跨具身策略组合的实证发现**：作者用实验证明“在完整身体上训练”是即插即用组合的必要条件——无手指机器人上训练的站立策略迁移到有手指机器人时成功率仅31%（76%站起但45%摔倒），而完整72-DoF训练的站立策略组合成功率达100%。这一反直觉结论对多技能模块化架构的设计有直接指导意义。

## 实验与结果

### 零样本抓取未见物体成功率（表IV）
| 物体 | 成功率 |
|------|--------|
| 球体 | 98% |
| 长方体 | 94% |
| 圆柱体 | 93% |
| 四面体 | 94% |
| 八面体 | 93% |
| 二十面体 | 94% |

### 站立行走成功率（表V，与72-DoF抓取策略组合）
| 站立策略训练具身 | 成功率 |
|------------------|--------|
| 同一机器人72 DoF | 100% |
| 同一机器人非驱动手指32 DoF | 96% |
| 无手指机器人32 DoF | 31%（76%站起但45%摔倒） |

### 消融实验关键数据（表VI，CHWSC阶数与解耦方式）
| 配置 | 手指-物体接近 | 物体-手指接近 | 包裹度 | 成功率 | 总奖励 | 训练epochs |
|------|--------------|--------------|--------|--------|--------|-----------|
| CHWSC(6), D(1) | 97% | 98% | 97% | **93%** | 414,376 | 23,907 |
| CHWSC(3), D(1) | 86% | 56% | 23% | 8% | 221,712 | 11,344 |
| CHWSC(0), D(1) | 24% | 26% | 10% | 0% | 116,098 | 8,344 |
| CHWSC(6), D(5) | 99% | 99% | 86% | 73% | 434,384 | 35,719 |
| CHWSC(6), 无解耦 | 52% | 81% | 64% | 7% | 259,932 | 39,750 |
| 两者皆无 | 3% | 14% | 3% | 0% | 161,759 | 7,407 |

**关键结论**：CHWSC阶数从6降到0，成功率从93%降至0%；无关节解耦时仅7%成功；两者皆无时策略在7,407 epochs即停止学习。分组解耦在接近度指标上更优（99%/99%），但包裹度（86% vs 97%）和总成功率（73% vs 93%）劣于个体解耦。

## 边界与局限

- 训练抓取策略时未显式使用物体形状，实际部署依赖多视角感知近似，精度损失未量化。
- 未将更多物体类型纳入训练课程以增强泛化（作者自认）。
- 手-物交互评分不区分左右手，特定手或双手操作任务需重新定义（未做）。
- 策略组合模块不处理站立接管后物体掉落的情况，作者提出可用大语言模型选择策略但未实现。
- 论文未提及真实机器人实验、计算时间、内存占用、训练总时长（墙钟时间）、GPU型号与数量。

## 工程启示

1. **复现优先核对**：先确认CHWSC阶数≥5（CHWSC(5)成功率89%，CHWSC(4)骤降至41%），这是成功率的分水岭；同时确保手指关节解耦启用（无解耦仅7%成功）。建议直接采用个体解耦（D(1)）而非分组解耦（D(5)），后者虽接近度更高但包裹度和成功率明显下降。

2. **最容易踩坑的环节**：跨具身迁移。若你计划在简化模型（如无手指）上训练再迁移到完整机器人，成功率会从100%暴跌至31%——务必在目标具身上训练所有技能。域随机化无法弥补具身不匹配，这是架构层面的约束而非调参问题。

3. **奖励设计参考**：成就触发奖励图的里程碑阈值（如手-物接近85%、包裹度40%）可直接复用，但需注意强制/非强制分数的选择——预抓取等必须保持的状态用强制分数，可牺牲的中间状态用非强制分数。总奖励公式中的\(L_j\)（跳数）和\(w=2\)的指数设计值得保留。

4. **观测向量维度注意**：完整72-DoF操作策略的观测向量含CHWSC(6) 44×2维，而移动策略不含；32-DoF无手指机器人无手指接触力项。组合时需确保统一观测向量的索引映射正确，这是多策略播放器最容易出bug的地方。

## Overview
This paper addresses how to enable a humanoid robot to learn motion policies based on developmental principles and combine policies to create more sophisticated and useful behaviors. Specifically, we present an approach to (1) learning a whole-body reaching and grasping policy and (2) combining it and a standing-up and walking policy to compose a more complex policy of manipulation and locomotion: grasping, standing up, and walking. In (1), our method draws inspiration from harmonic analysis and adopts cubic harmonics as weights to represent the hand-object spatial relationship via spatial convolution. Utilizing an intra-episode finger joint decoupling curriculum based on developmental principles, a robot can autonomously learn a generalizable grasping policy without relying on external datasets or pretrained models. In (2), our method combines the grasping policy with a separately learned getting-up policy by providing both policies with their respective observation vectors and using hand-object interaction scores to determine when each policy should control which robot joints. Our results show a 93% zero-shot success rate for grasping unseen objects and a 96-100% success rate for standing up while holding the object. Our work also demonstrates that combining different policies is only effective if each policy learning happens on the same whole humanoid body even if a policy (such as for locomotion) does not seem to need all the body parts (such as fingers).

## 参考
- https://arxiv.org/abs/2608.00208

## 개요

본 논문은 발달 심리학 원리에 기반한 휴머노이드 로봇 조작 및 이동 기술 학습 프레임워크를 제안한다. 핵심 기여는 다음과 같다: 입방 조화 가중 공간 컨볼루션(CHWSC)과 역비례 스케일링 거리장(ISDF)으로 구성된 손-물체 상호작용의 컴팩트 표현, 발달 원리에서 영감을 받은 성취 트리거 보상 그래프와 점진적 손가락 관절 분리, 그리고 교차-구현 정책 조합 방법. 저자는 Isaac Gym에서 72-DoF 휴머노이드 로봇을 훈련하여 "손을 뻗어 잡기→서기→걷기" 복합 작업을 완료했으며, 보지 못한 물체에 대한 제로샷 잡기 성공률은 최대 98%에 달한다.

## 무엇을 바꾸었는가

이 작업의 진정한 변화는 "조작 기술 학습"을 대규모 인간 시연이나 사전 훈련된 비전-언어 모델에 의존하는 패러다임에서 "컴팩트 기하학적 표현 + 구조화된 보상 형성"의 고전적 RL 경로로 되돌려 놓았고, 이 경로가 휴머노이드 전신 제어에서 실현 가능함을 입증했다는 점이다. 저자는 엔드투엔드 대형 모델 트렌드를 추구하지 않고, 거리장과 입방 조화와 같은 저차원의 해석 가능한 기하학적 특징을 사용하여 4096 병렬 환경에서 PPO만으로도 정밀한 잡기를 학습할 수 있게 했다—이는 자원이 제한된 로봇 연구실에 직접적인 매력을 제공한다.

더 중요하게는, 대부분의 연구가 회피하는 엔지니어링 난제인 "기술 조합"을 정면으로 다루었다: 독립적으로 훈련된 기술을 추론 시 매끄럽게 연결하는 방법. 저자는 "전신에서 훈련"이라는 반직관적 결론(손가락 없는 로봇에서 훈련된 서기 정책을 손가락 있는 로봇으로 전이하면 성공률이 100%에서 31%로 급락)을 통해 구현 불일치가 플러그앤플레이 조합에 미치는 치명적 영향을 밝혔다. 이는 "기술 모듈화"에 대한 낙관적 가정을 바꾼다—모듈화는 공짜가 아니며, 훈련 시점에 목표 구현에서 이루어져야 한다.

## 방법 분해

### 문제 정식화 및 아키텍처 독립성
- PPO로 정책을 훈련하며, 입력 관측 벡터(신체 자세, 관절 힘 등 포함)를 받아 관절 토크 명령을 출력한다.
- 이 방법은 사전 계산된 관측, 사전 처리된 행동, 보상 설계만 포함하며 특정 RL 알고리즘이나 네트워크 구조에 묶이지 않는다.

### 손-물체 상호작용 표현
- **ISDF**: \( I(i) = \min(1, \exp(-\alpha \cdot S(i))) \), \(\alpha\)는 고정 양의 하이퍼파라미터; 음의 거리(관통)는 1로 잘린다.
- **CHWSC**: \( \text{CHWSC}(l) = \sum_{\ell=0}^{l} \sum_j I(f_j) \cdot K_\ell^m(f_j/\|f_j\|) \), 입방 조화를 가중치로 사용하여 각 손가락 마디에서 물체까지의 ISDF와 컨볼루션; 수치적으로 불안정한 비대칭 조화(\(K_2^{-1}, K_4^{-4}, K_4^{-2}, K_6^{-6}, K_6^{-3}\))는 제외한다.

### 손-물체 상호작용 점수(5개 지표)
1. 손-물체 근접도: \(I(h)\)
2. 내부 법선 정렬: \(-n_f \cdot n_\Omega\)
3. 손가락-물체 근접도: \(\text{avg}_j(I(f_j))\)
4. 물체-손가락 근접도: \(\text{avg}_k(\exp(-\alpha \cdot \min_j\|f_j - \Omega_k\|))\), 곡률 매칭에 따라 샘플링
5. 감싸기 정도: \(\exp(-\alpha\|c_{obj} - c_{fingers}\|)\)

### 손가락 관절 분리
- 각 에피소드 시작 시 모든 손가락 관절은 평균 토크 명령을 받는다; 훈련 중 근위에서 원위 순서로 점진적으로 분리된다.
- **개별 분리**: 100스텝마다 한 번 분리, t=800 이후 시작.
- **그룹 분리**: 500스텝마다 한 번 분리, 동일 유형의 관절이 함께 분리.

### 성취 트리거 보상
- 마일스톤은 방향성 비순환 그래프(DAG)로 구성되며, 강제/비강제 두 가지 성취 점수를 포함:
  - 강제: \(A_{i,j,t}^E = r_{i,t} - p_{i,j}\) (순간 보상 사용)
  - 비강제: \(A_{i,j,t}^N = \max_{t^* \le t}\{r_{i,t^*}\} - p_{i,j}\) (역사적 최대 보상 사용)
- 총 보상: \( r_t = \sum_j \text{pow}(L_j, w) \cdot \sum_i \max(0, A_{i,j,t}) \cdot r_{j,t} \), \(w=2\).

### 정책 조합
- 다중 정책 RL 플레이어, 통합 관측 벡터에서 인덱스를 통해 각 하위 작업의 독립 관측을 추출한다.
- 잡기 정책은 모든 관절을 제어; 물체가 잡힌 후("손가락 마디 접촉 비율" 마일스톤 통해) 서기 정책이 손가락을 제외한 신체 관절을接管한다.

## 핵심 혁신

1. **CHWSC+ISDF 기하학적 표현**: 원자 궤도 형태에서 유래한 입방 조화를 손-물체 상호작용의 공간 컨볼루션에 처음으로 사용하여, 물체 참조 프레임에서 거리장의 방사형 성분과 손가락 감싸기의 각도 분포를 동시에 포착한다. 원시 거리장이나 원시 포인트 클라우드에 비해, 이 저차원 임베딩(44×2)은 보지 못한 물체에 대한 제로샷 일반화(구체 98%, 직육면체 94%)를 가능하게 하며, 절제 실험에서 CHWSC 차수를 6에서 0으로 낮추면 성공률이 93%에서 0으로 떨어짐을 보여준다—각도 정보가 잡기 성공의 핵심임을 증명한다.

2. **성취 트리거 보상 그래프**: 작업을 통과 임계값이 있는 마일스톤 DAG로 분해하고, "역사적 최대 보상"의 비강제 점수로 희생 가능한 전제 조건을 처리하며, "순간 보상"의 강제 점수로 유지해야 하는 상태(예: 사전 잡기)를 처리한다. 이 설계는 희소 보상 하의 탐색 어려움을 피하면서도 보상 형성 사전 지식에 의존하지 않는 순수 구조화된 커리큘럼 학습 대안이다.

3. **교차-구현 정책 조합의 실증적 발견**: 저자는 실험을 통해 "전신에서 훈련"이 플러그앤플레이 조합의 필요 조건임을 증명한다—손가락 없는 로봇에서 훈련된 서기 정책을 손가락 있는 로봇으로 전이하면 성공률이 31%에 불과하며(76%는 일어서지만 45%는 넘어짐), 완전한 72-DoF 훈련 서기 정책 조합의 성공률은 100%에 달한다. 이 반직관적 결론은 다중 기술 모듈형 아키텍처 설계에 직접적인 지침을 제공한다.

## 실험 및 결과

### 보지 못한 물체 제로샷 잡기 성공률(표 IV)
| 물체 | 성공률 |
|------|--------|
| 구체 | 98% |
| 직육면체 | 94% |
| 원기둥 | 93% |
| 사면체 | 94% |
| 팔면체 | 93% |
| 이십면체 | 94% |

### 서기-걷기 성공률(표 V, 72-DoF 잡기 정책과 조합)
| 서기 정책 훈련 구현 | 성공률 |
|------------------|--------|
| 동일 로봇 72 DoF | 100% |
| 동일 로봇 비구동 손가락 32 DoF | 96% |
| 손가락 없는 로봇 32 DoF | 31%(76% 일어서지만 45% 넘어짐) |

### 절제 실험 핵심 데이터(표 VI, CHWSC 차수 및 분리 방식)
| 구성 | 손가락-물체 근접 | 물체-손가락 근접 | 감싸기 정도 | 성공률 | 총 보상 | 훈련 epochs |
|------|--------------|--------------|--------|--------|--------|-----------|
| CHWSC(6), D(1) | 97% | 98% | 97% | **93%** | 414,376 | 23,907 |
| CHWSC(3), D(1) | 86% | 56% | 23% | 8% | 221,712 | 11,344 |
| CHWSC(0), D(1) | 24% | 26% | 10% | 0% | 116,098 | 8,344 |
| CHWSC(6), D(5) | 99% | 99% | 86% | 73% | 434,384 | 35,719 |
| CHWSC(6), 분리 없음 | 52% | 81% | 64% | 7% | 259,932 | 39,750 |
| 둘 다 없음 | 3% | 14% | 3% | 0% | 161,759 | 7,407 |

**핵심 결론**: CHWSC 차수를 6에서 0으로 낮추면 성공률이 93%에서 0%로 감소; 관절 분리가 없으면 7%만 성공; 둘 다 없으면 정책이 7,407 epochs에서 학습을 중단한다. 그룹 분리는 근접도 지표에서 더 우수하지만(99%/99%), 감싸기 정도(86% vs 97%)와 총 성공률(73% vs 93%)에서 개별 분리보다 열등하다.

## 경계 및 한계

- 잡기 정책 훈련 시 물체 모양을 명시적으로 사용하지 않았으며, 실제 배포는 다중 시점 인식 근사에 의존하지만 정밀도 손실은 정량화되지 않았다.
- 더 많은 물체 유형을 훈련 커리큘럼에 포함하여 일반화를 강화하지 않았다(저자 자인).
- 손-물체 상호작용 점수는 좌우 손을 구분하지 않으며, 특정 손 또는 양손 조작 작업은 재정의가 필요하다(미수행).
- 정책 조합 모듈은 서기接管 후 물체 낙하를 처리하지 않으며, 저자는 대형 언어 모델로 정책 선택을 제안했지만 구현하지 않았다.
- 논문은 실제 로봇 실험, 계산 시간, 메모리 사용량, 총 훈련 시간(벽시계 시간), GPU 모델 및 수량을 언급하지 않았다.

## 공학적 시사점

1. **재현 시 우선 확인 사항**: 먼저 CHWSC 차수가 ≥5인지 확인하라(CHWSC(5) 성공률 89%, CHWSC(4)는 41%로 급락)—이는 성공률의 분기점이다; 동시에 손가락 관절 분리가 활성화되었는지 확인하라(분리 없음은 7%만 성공). 개별 분리(D(1))를 직접 채택하는 것이 좋으며, 그룹 분리(D(5))는 근접도가 더 높지만 감싸기 정도와 성공률이 현저히 떨어진다.

2. **가장 함정에 빠지기 쉬운 부분**: 교차-구현 전이. 단순화된 모델(예: 손가락 없음)에서 훈련한 후 완전한 로봇으로 전이할 계획이라면 성공률이 100%에서 31%로 급락한다—반드시 목표 구현에서 모든 기술을 훈련하라. 도메인 무작위화는 구현 불일치를 보완할 수 없으며, 이는 파라미터 튜닝 문제가 아닌 아키텍처 수준의 제약이다.

3. **보상 설계 참고**: 성취 트리거 보상 그래프의 마일스톤 임계값(예: 손-물체 근접 85%, 감싸기 정도 40%)은 직접 재사용할 수 있지만, 강제/비강제 점수 선택에 주의하라—사전 잡기와 같이 유지해야 하는 상태는 강제 점수, 희생 가능한 중간 상태는 비강제 점수를 사용한다. 총 보상 공식의 \(L_j\)(점프 수)와 \(w=2\) 지수 설계는 유지할 가치가 있다.

4. **관측 벡터 차원 주의**: 완전한 72-DoF 조작 정책의 관측 벡터는 CHWSC(6) 44×2 차원을 포함하지만 이동 정책은 포함하지 않는다; 32-DoF 손가락 없는 로봇은 손가락 접촉 힘 항이 없다. 조합 시 통합 관측 벡터의 인덱스 매핑이 올바른지 확인해야 하며, 이는 다중 정책 플레이어에서 가장 버그가 발생하기 쉬운 부분이다.
