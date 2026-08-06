---
$id: ent_paper_courteous_anticipation_improving_long_li_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Courteous Anticipation: Improving Long-Lived Task Planning in Persistent Shared Environments'
  zh: 'Courteous Anticipation: Improving Long-Lived Task Planning in Persistent Shared Environments'
  ko: 'Courteous Anticipation: Improving Long-Lived Task Planning in Persistent Shared Environments'
summary:
  en: We consider a task planning scenario in which robots sharing a persistent environment are assigned tasks one at a time
    from a held-out sequence. Standard task planners, lacking foresight of future tasks and inconsiderate of others' constraints,
    solve each task in isolation, leaving terminal states that increase future cost for all, side effects that compound over
    lengthy task sequences. To reduce.
  zh: 本文提出“礼貌预期规划”（courteous anticipatory planning），针对共享持久环境中多机器人长序列任务分配问题，通过联合最小化当前任务成本与所有机器人聚合预期未来成本，改善长期规划效率。作者来自学术机构，核心贡献在于将“对他人预见”引入符号规划，并验证其在家庭与餐厅模拟环境中的显著收益。
  ko: We consider a task planning scenario in which robots sharing a persistent environment are assigned tasks one at a time
    from a held-out sequence. Standard task planners, lacking foresight of future tasks and inconsiderate of others' constraints,
    solve each task in isolation, leaving terminal states that increase future cost for all, side effects that compound over
    lengthy task sequences. To reduce.
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
- courteous
- anticipation
- improving
- long
- li
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
  title: 'arXiv:2607.20289 Courteous Anticipation: Improving Long-Lived Task Planning in Persistent Shared '
  url: https://arxiv.org/abs/2607.20289
  date: '2026-07-22'
  accessed_at: '2026-08-05'
---

## 概述

本文提出“礼貌预期规划”（courteous anticipatory planning），针对共享持久环境中多机器人长序列任务分配问题，通过联合最小化当前任务成本与所有机器人聚合预期未来成本，改善长期规划效率。作者来自学术机构，核心贡献在于将“对他人预见”引入符号规划，并验证其在家庭与餐厅模拟环境中的显著收益。

## 它改变了什么

标准任务规划器在共享环境中孤立求解每个任务，忽视终端状态对其他机器人未来任务的副作用，这些副作用在长序列中累积，导致整体成本上升。现有预期规划方法仅考虑单机器人自身未来任务，即“自私预期”，仍可能留下对其他机器人昂贵的终端状态。本文真正改变的是将规划目标从“自我中心”扩展为“社会性”，即规划时显式纳入共享空间中所有机器人的能力与责任，使当前决策主动降低他人未来成本，而非仅优化自身。这一转变将问题从单智能体优化重构为多智能体符号规划行为问题，而非协调或通信问题。

## 方法拆解

### 目标函数
礼貌预期规划选择终端状态 \( s'_g \) 最小化：
\[
s^*_g = \arg\min_{s'_g \in G_\tau} \left[ V^*_{s'_g}(s_0) + \sum_{r \in R} V^r_{\text{A.P.}}(s'_g) \right]
\]
其中 \( V^*_{s'_g}(s_0) \) 为当前任务即时成本，\( V^r_{\text{A.P.}}(s'_g) \) 为机器人 \( r \) 从该终端状态完成其后续任务的预期成本。

### 分解策略
- 将聚合预期未来成本分解为独立的每机器人估计器，避免组合联合回滚。
- 每个估计器独立训练于单个机器人的责任，隐式捕获其结构约束。
- 模块化部署：新增机器人仅需训练其自身估计器，无需重训现有估计器。

### 候选计划生成
- 采用聚焦采样程序，选择性增强任务与放置谓词、对象状态谓词，生成结构不同的候选计划。
- 拒绝未能完成原始任务的计划。
- 使用 FastDownward 与 ff-astar 求解每个代理任务。

### 预期成本估计器
- 图神经网络（GNN），四个 GINConv 层，后接批归一化与 leaky ReLU。
- 节点特征通过均值与求和池化聚合为图级表示，最终线性层输出成本估计。
- 训练数据从保留的训练时环境离线生成，使用规划器求解并计算计划成本。

## 关键创新

1. **对他人预见**：首次将“礼貌”概念形式化为规划目标，显式聚合所有机器人的预期未来成本，区别于仅考虑自身的自私预期，这是符号规划行为层面的新问题定义。
2. **分解式估计器**：将联合预期成本分解为独立每机器人估计器，避免组合爆炸，同时支持模块化扩展，新增机器人无需重训，工程上可扩展。
3. **离线训练、在线查询**：训练时用昂贵计算近似预期成本，部署时仅查询学习估计器，避免回滚，实现实时决策。

## 实验与结果

实验在家庭（ProcTHOR）与餐厅两个模拟环境进行，对比短视（myopic）、自私预期（selfish anticipatory）与礼貌预期（courteous）三种规划器。

| 环境/设置 | Myopic 成本 | Self. A.P. 成本 | Courteous 成本 | vs Myopic | vs Self. A.P. |
|---|---|---|---|---|---|
| 家庭（两机器人，100序列×20任务） | — | — | — | 10.4% | 4.0% |
| 餐厅（三机器人，200序列×30任务） | 873 | 831 | 721 | 17.41% | 13.24% |
| 餐厅（两机器人平均） | — | — | — | 6.7% | 5.5% |
| 餐厅（Cook+Cleaner） | 917 | 901 | 838 | 8.62% | 7.01% |
| 餐厅（Cleaner+Server） | 812 | 796 | 778 | 4.18% | 2.26% |
| 餐厅（Cook+Server） | 1052 | 1046 | 976 | 7.22% | 6.69% |

主动性实验：在 Cook-Server 设置中，空闲 Cleaning 机器人每两任务获 100 秒预算，将成本从 976 降至 670，改进 31.4%。单机器人设置中，Courteous 与 Selfish 结果相同（标注 *），因无其他代理可礼貌对待。定性示例显示，礼貌规划器将垃圾直接放入垃圾桶、将脏锅放在餐车上，而短视规划器留下阻塞表面等副作用。

## 边界与局限

论文未明确完整局限列表，但作者承认：方法假设任务顺序到达且环境在任务间持续存在，未覆盖并发场景（多机器人同时行动、任务并发到达、环境中途变化），此类场景需时间规划。未考虑任务时间到达的在线规划，未在单任务设置中建模未来任务序列或不同能力。实验仅在模拟环境验证，未涉及真实机器人部署。

## 工程启示

复现时先核对候选计划生成器的采样密度与多样性，这直接影响终端状态覆盖质量。估计器训练数据需覆盖足够多样的终端状态，否则部署时对未见状态预测偏差大。模块化设计使新增机器人仅需训练自身估计器，但需注意各估计器输入特征对齐。最易踩坑处：单机器人设置中礼貌与自私结果相同，验证算法收益必须使用多机器人异构责任设置；主动性实验依赖预算分配策略，需仔细调参。下游团队应优先在异构机器人、责任差异大的场景评估，收益最显著。

## Overview
We consider a task planning scenario in which robots sharing a persistent environment are assigned tasks one at a time from a held-out sequence. Standard task planners, lacking foresight of future tasks and inconsiderate of others' constraints, solve each task in isolation, leaving terminal states that increase future cost for all, side effects that compound over lengthy task sequences. To reduce cost over the sequence, a robot must anticipate how its actions now may impact performance on future tasks for all robots sharing the environment. Therefore, we present courteous anticipatory planning, wherein a model-based planner proposes candidate plans and selects the one that jointly minimizes immediate cost and aggregated expected future cost across all robots, estimated via independent per-robot learned estimators. This factored formulation avoids combinatorial joint rollouts and supports modular deployment: adding a robot requires only training its own estimator. We evaluate in two persistent PDDL domains, a home environment with robots that have similar capabilities but different responsibilities, and a restaurant environment where robots' distinct capabilities create states that other robots lack the capability to resolve. During lengthy task sequences, our planner reduces total cost by 10.43% versus myopic and 4.03% versus selfish anticipatory planning in a two-robot home environment and by 17.41% and 13.24%, respectively, in a three-robot restaurant.

## 参考
- https://arxiv.org/abs/2607.20289

## 개요

본 논문은 "공손한 예측 계획"(courteous anticipatory planning)을 제안하며, 공유 지속 환경에서 다중 로봇 장기 작업 할당 문제를 위해 현재 작업 비용과 모든 로봇의 통합 예측 미래 비용을 공동으로 최소화하여 장기 계획 효율성을 개선한다. 저자는 학술 기관 소속이며, 핵심 기여는 "타인에 대한 예견"을 기호 계획에 도입하고 가정 및 레스토랑 시뮬레이션 환경에서 상당한 이점을 검증한 것이다.

## 그것이 바꾸는 것

표준 작업 계획기는 공유 환경에서 각 작업을 고립적으로 해결하며, 종료 상태가 다른 로봇의 미래 작업에 미치는 부작용을 무시한다. 이러한 부작용은 장기 시퀀스에서 누적되어 전체 비용을 증가시킨다. 기존 예측 계획 방법은 단일 로봇 자신의 미래 작업만 고려하는 "이기적 예측"에 그쳐, 다른 로봇에게 비용이 많이 드는 종료 상태를 남길 수 있다. 본 논문이 실제로 바꾸는 것은 계획 목표를 "자아 중심"에서 "사회적"으로 확장한 점이다. 즉, 계획 시 공유 공간에 있는 모든 로봇의 능력과 책임을 명시적으로 포함하여, 현재 결정이 타인의 미래 비용을 능동적으로 낮추도록 하며, 단지 자신만 최적화하지 않는다. 이러한 전환은 문제를 단일 에이전트 최적화에서 다중 에이전트 기호 계획 행동 문제로 재구성하며, 조정이나 통신 문제가 아니다.

## 방법 분해

### 목적 함수
공손한 예측 계획은 종료 상태 \( s'_g \)를 선택하여 다음을 최소화한다:
\[
s^*_g = \arg\min_{s'_g \in G_\tau} \left[ V^*_{s'_g}(s_0) + \sum_{r \in R} V^r_{\text{A.P.}}(s'_g) \right]
\]
여기서 \( V^*_{s'_g}(s_0) \)는 현재 작업의 즉시 비용이고, \( V^r_{\text{A.P.}}(s'_g) \)는 로봇 \( r \)이 해당 종료 상태에서 후속 작업을 완료하는 예측 비용이다.

### 분해 전략
- 통합 예측 미래 비용을 독립적인 로봇별 추정기로 분해하여 결합 롤백을 피한다.
- 각 추정기는 단일 로봇의 책임에 대해 독립적으로 훈련되며, 구조적 제약을 암시적으로 포착한다.
- 모듈식 배포: 새 로봇은 자체 추정기만 훈련하면 되며, 기존 추정기를 재훈련할 필요가 없다.

### 후보 계획 생성
- 초점 샘플링 절차를 사용하여 작업 및 배치 술어, 객체 상태 술어를 선택적으로 강화하여 구조적으로 다른 후보 계획을 생성한다.
- 원래 작업을 완료하지 못하는 계획은 거부한다.
- 각 에이전트 작업을 해결하기 위해 FastDownward 및 ff-astar를 사용한다.

### 예측 비용 추정기
- 그래프 신경망(GNN), 4개의 GINConv 레이어, 배치 정규화 및 leaky ReLU를 사용한다.
- 노드 특징은 평균 및 합계 풀링을 통해 그래프 수준 표현으로 집계되고, 최종 선형 레이어가 비용 추정을 출력한다.
- 훈련 데이터는 유보된 훈련 환경에서 오프라인으로 생성되며, 계획기로 해결하고 계획 비용을 계산한다.

## 핵심 혁신

1. **타인에 대한 예견**: "공손함" 개념을 계획 목표로 공식화한 최초의 사례로, 모든 로봇의 예측 미래 비용을 명시적으로 통합하며, 자신만 고려하는 이기적 예측과 구별된다. 이는 기호 계획 행동 수준의 새로운 문제 정의이다.
2. **분해형 추정기**: 결합 예측 비용을 독립적인 로봇별 추정기로 분해하여 조합 폭발을 피하고, 모듈식 확장을 지원하여 새 로봇 추가 시 재훈련이 필요 없어 엔지니어링 확장성이 뛰어나다.
3. **오프라인 훈련, 온라인 쿼리**: 훈련 시에는 고비용 계산으로 예측 비용을 근사하고, 배포 시에는 학습된 추정기만 쿼리하여 롤백을 피하고 실시간 결정을 구현한다.

## 실험 및 결과

실험은 가정(ProcTHOR) 및 레스토랑 두 시뮬레이션 환경에서 수행되었으며, 근시안적(myopic), 이기적 예측(selfish anticipatory), 공손한 예측(courteous) 세 가지 계획기를 비교했다.

| 환경/설정 | Myopic 비용 | Self. A.P. 비용 | Courteous 비용 | vs Myopic | vs Self. A.P. |
|---|---|---|---|---|---|
| 가정(로봇 2대, 100시퀀스×20작업) | — | — | — | 10.4% | 4.0% |
| 레스토랑(로봇 3대, 200시퀀스×30작업) | 873 | 831 | 721 | 17.41% | 13.24% |
| 레스토랑(로봇 2대 평균) | — | — | — | 6.7% | 5.5% |
| 레스토랑(Cook+Cleaner) | 917 | 901 | 838 | 8.62% | 7.01% |
| 레스토랑(Cleaner+Server) | 812 | 796 | 778 | 4.18% | 2.26% |
| 레스토랑(Cook+Server) | 1052 | 1046 | 976 | 7.22% | 6.69% |

능동성 실험: Cook-Server 설정에서 유휴 Cleaning 로봇이 작업 2개마다 100초 예산을 받아 비용을 976에서 670으로 낮추어 31.4% 개선했다. 단일 로봇 설정에서는 Courteous와 Selfish 결과가 동일하며(* 표시), 공손하게 대할 다른 에이전트가 없기 때문이다. 정성적 예시에서 공손한 계획기는 쓰레기를 쓰레기통에 직접 넣고 더러운 냄비를 서빙 카트에 두는 반면, 근시안적 계획기는 표면을 막는 부작용을 남긴다.

## 경계 및 한계

논문은 완전한 한계 목록을 명시하지 않았지만, 저자는 다음을 인정한다: 이 방법은 작업이 순차적으로 도착하고 환경이 작업 간 지속된다고 가정하며, 동시 시나리오(여러 로봇이 동시에 행동, 작업 동시 도착, 환경 중간 변경)를 다루지 않으며, 이러한 시나리오는 시간 계획이 필요하다. 작업 시간 도착의 온라인 계획을 고려하지 않았고, 단일 작업 설정에서 미래 작업 시퀀스나 다양한 능력을 모델링하지 않았다. 실험은 시뮬레이션 환경에서만 검증되었으며 실제 로봇 배포는 다루지 않았다.

## 엔지니어링 시사점

재현 시 후보 계획 생성기의 샘플링 밀도와 다양성을 먼저 확인해야 하며, 이는 종료 상태 커버리지 품질에 직접 영향을 미친다. 추정기 훈련 데이터는 충분히 다양한 종료 상태를 포함해야 하며, 그렇지 않으면 배포 시 보지 못한 상태에 대한 예측 편차가 크다. 모듈식 설계로 새 로봇은 자체 추정기만 훈련하면 되지만, 각 추정기의 입력 특징 정렬에 주의해야 한다. 가장 쉽게 실수하는 지점: 단일 로봇 설정에서는 공손함과 이기적 결과가 동일하므로, 알고리즘 이점을 검증하려면 다중 로봇 이기종 책임 설정을 사용해야 한다. 능동성 실험은 예산 할당 전략에 의존하므로 세심한 파라미터 튜닝이 필요하다. 하류 팀은 이기종 로봇, 책임 차이가 큰 시나리오에서 우선 평가해야 하며, 이점이 가장 두드러진다.
