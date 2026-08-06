---
$id: ent_paper_crocoddyl_efficient_versatile_framework_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control'
  zh: 'Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control'
  ko: 'Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control'
summary:
  en: We introduce Crocoddyl (Contact RObot COntrol by Differential DYnamic Library), an open-source framework tailored for
    efficient multi-contact optimal control. Crocoddyl efficiently computes the state trajectory and the control policy for
    a given predefined sequence of contacts. Its efficiency is due to the use of sparse analytical derivatives, exploitation
    of the problem structure, and data.
  zh: Crocoddyl 是法国 LAAS-CNRS 团队提出的多接触最优控制框架，核心贡献在于将接触序列显式建模为切换动力学，并用稀疏性感知的 Riccati 递归实现高效求解。它面向四足与双足机器人，在统一权重与代价函数下覆盖多种步态，显著降低了多接触轨迹优化的计算门槛。
  ko: We introduce Crocoddyl (Contact RObot COntrol by Differential DYnamic Library), an open-source framework tailored for
    efficient multi-contact optimal control. Crocoddyl efficiently computes the state trajectory and the control policy for
    a given predefined sequence of contacts. Its efficiency is due to the use of sparse analytical derivatives, exploitation
    of the problem structure, and data.
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
- crocoddyl
- efficient
- versatile
- framework
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P006. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:1909.04947 Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Contro'
  url: https://arxiv.org/abs/1909.04947
  date: '2019-09-11'
  accessed_at: '2026-08-05'
---

## 概述

Crocoddyl 是法国 LAAS-CNRS 团队提出的多接触最优控制框架，核心贡献在于将接触序列显式建模为切换动力学，并用稀疏性感知的 Riccati 递归实现高效求解。它面向四足与双足机器人，在统一权重与代价函数下覆盖多种步态，显著降低了多接触轨迹优化的计算门槛。

## 它改变了什么

多接触最优控制长期受困于两个痛点：一是接触事件（如脚落地）带来的动力学不连续，传统方法要么忽略冲击要么用软约束近似，导致轨迹在切换瞬间物理不一致；二是全维状态-控制空间的优化规模随接触数量爆炸，通用求解器难以在机器人在线周期内收敛。Crocoddyl 改变了这一局面——它把接触序列当作一阶离散变量显式纳入问题结构，而非事后修正，从而让求解器能利用稀疏性做针对性加速。这不仅是算法层面的改进，更意味着多足机器人的全身轨迹优化从“离线离线调参”走向“可重复、可泛化”的工程实践。

## 方法拆解

### 问题形式化
将多接触最优控制建模为有限时域离散最优控制问题，状态为广义坐标与速度，控制为关节力矩。接触序列被划分为若干“切换阶段”（switching phases），每个阶段内接触状态恒定，阶段间发生接触增益变化。

### 冲击动力学处理
在每个切换阶段，用冲量动力学（impulse dynamics）计算碰撞后的速度，保证轨迹在接触切换瞬间满足动量守恒与非穿透约束。这是保证物理一致性的关键步骤，避免了软约束近似带来的漂移。

### 代价函数设计
代价函数由三部分构成：质心（CoM）跟踪、落脚点（foot placement）跟踪，以及状态与控制的正则化项。摆动脚参考轨迹用分段线性函数描述，并对落脚点偏离参考位置施加强惩罚。四足所有步态共用同一组权重与代价函数，双足行走使用相近权重，体现了框架的通用性。

### 热启动策略
状态热启动 𝐗₀ 通过对接触配置序列的标称身体姿态做线性插值得到，同时给出标称关节姿态；控制热启动 𝐔₀ 则基于准静态假设（quasi-static assumption）计算——以参考姿态为平衡点，通过 Newton 步数值求解准静态力矩。这一策略显著加速了收敛。

### 求解器核心
采用稀疏性感知的 Riccati 递归，利用接触约束带来的块稀疏结构，将复杂度从全维 O(n³) 降至与接触数相关的近线性规模。这是实现实时性的根本原因。

## 关键创新

1. **接触序列的一阶显式建模**：将接触增益作为离散变量纳入优化，而非用连续松弛近似，使得冲击动力学可以被精确处理，轨迹在切换瞬间物理自洽。这是与以往“软接触”方法最本质的区别。
2. **统一权重下的多步态泛化**：四足所有步态共用同一组代价权重，双足仅需微调，说明框架对接触模式变化具有内在鲁棒性，而非为每种步态手工调参。这大幅降低了部署成本。
3. **稀疏性感知的求解架构**：将 Riccati 递归与接触结构的稀疏性结合，使计算复杂度随接触规模近线性增长，这是从“能算”到“算得快”的跨越，为在线重规划铺平了道路。

## 实验与结果

论文在四足与双足平台上验证了框架的通用性与效率，但原文事实要点未给出具体对照实验的数值细节。可确认的是：所有四足步态共用同一权重与代价函数，双足行走使用相近权重；热启动采用线性插值加准静态假设；冲击动力学在每个切换阶段被显式计算。关键数字汇总如下：

| 项目 | 数值 | 说明 |
|------|------|------|
| 四足步态权重 | 统一 | 所有步态共用 |
| 双足权重 | 相近 | 与四足相似 |
| 摆动脚参考 | 分段线性 | 描述参考轨迹 |
| 落脚点惩罚 | 强 | 偏离参考即重罚 |
| 热启动状态 | 线性插值 | 标称姿态间插值 |
| 热启动控制 | 准静态 | Newton 步求平衡力矩 |

论文未明确给出求解时间、收敛迭代次数或与基线方法的对比数字，因此无法量化其加速比；但“同一权重覆盖多步态”这一事实本身已说明框架的泛化能力。

## 边界与局限

论文未明确讨论以下边界：一是接触序列本身仍由用户预设，框架优化的是给定接触时序下的轨迹，而非自动发现接触模式；二是准静态热启动假设在高速动态或大扰动场景下可能失效，此时 Newton 步求得的力矩未必是好的初始猜测；三是冲击动力学处理依赖接触点位置与摩擦锥模型的准确性，对地面参数敏感；四是实验平台与负载范围未在事实要点中说明，框架对高动态跳跃或非结构化地形的适用性未知。

## 工程启示

复现或采用 Crocoddyl 时，优先核对三件事：**接触序列的定义方式**——确保切换阶段的划分与真实足底事件一致，否则冲击动力学计算会引入虚假动量；**热启动的质量**——准静态假设在低速或准静态步态下表现良好，但若目标轨迹含明显动态（如快走或跑），建议改用上一时域解或仿真数据做热启动，否则收敛可能陷入局部极小；**权重标定**——虽然四足共用权重，但双足仍需“相近”而非“相同”的调整，落地时先复现论文的步态再改参数，避免一步到位。最容易踩坑的是落脚点强惩罚与摆动脚分段线性参考的配合——若参考轨迹不平滑，强惩罚会放大抖动，建议先检查参考轨迹的连续性再调惩罚系数。

## Overview
We introduce Crocoddyl (Contact RObot COntrol by Differential DYnamic Library), an open-source framework tailored for efficient multi-contact optimal control. Crocoddyl efficiently computes the state trajectory and the control policy for a given predefined sequence of contacts. Its efficiency is due to the use of sparse analytical derivatives, exploitation of the problem structure, and data sharing. It employs differential geometry to properly describe the state of any geometrical system, e.g. floating-base systems. Additionally, we propose a novel optimal control algorithm called Feasibility-driven Differential Dynamic Programming (FDDP). Our method does not add extra decision variables which often increases the computation time per iteration due to factorization. FDDP shows a greater globalization strategy compared to classical Differential Dynamic Programming (DDP) algorithms. Concretely, we propose two modifications to the classical DDP algorithm. First, the backward pass accepts infeasible state-control trajectories. Second, the rollout keeps the gaps open during the early "exploratory" iterations (as expected in multiple-shooting methods with only equality constraints). We showcase the performance of our framework using different tasks. With our method, we can compute highly-dynamic maneuvers (e.g. jumping, front-flip) within few milliseconds.

## 参考
- https://arxiv.org/abs/1909.04947

## 개요

Crocoddyl은 프랑스 LAAS-CNRS 팀이 제안한 다접촉 최적 제어 프레임워크로, 핵심 기여는 접촉 시퀀스를 스위칭 동역학으로 명시적으로 모델링하고 희소성 인지 Riccati 재귀를 통해 효율적으로 해를 구하는 데 있다. 이는 사족 및 이족 로봇을 대상으로 하며, 통합된 가중치와 비용 함수 아래에서 다양한 보행을 포괄하여 다접촉 궤적 최적화의 계산 장벽을 크게 낮췄다.

## 무엇을 바꾸었는가

다접촉 최적 제어는 오랫동안 두 가지 문제점에 시달려 왔다. 첫째, 접촉 이벤트(예: 발 착지)로 인한 동역학 불연속성으로, 기존 방법은 충격을 무시하거나 소프트 제약으로 근사하여 스위칭 순간에 궤적이 물리적으로 불일치했다. 둘째, 전차원 상태-제어 공간의 최적화 규모가 접촉 수에 따라 폭발적으로 증가하여 범용 솔버가 로봇 온라인 주기 내에 수렴하기 어려웠다. Crocoddyl은 이러한 상황을 바꾸었다—접촉 시퀀스를 사후 수정이 아닌 1차 이산 변수로 문제 구조에 명시적으로 포함시켜, 솔버가 희소성을 활용해 맞춤형 가속을 할 수 있게 했다. 이는 단순한 알고리즘 개선에 그치지 않고, 다족 로봇의 전신 궤적 최적화가 "오프라인 파라미터 튜닝"에서 "반복 가능하고 일반화 가능한" 엔지니어링 실천으로 나아갔음을 의미한다.

## 방법 분석

### 문제 정식화
다접촉 최적 제어를 유한 시간 영역 이산 최적 제어 문제로 모델링하며, 상태는 일반화 좌표와 속도, 제어는 관절 토크로 정의한다. 접촉 시퀀스는 여러 "스위칭 단계"(switching phases)로 나뉘며, 각 단계 내에서는 접촉 상태가 일정하고 단계 사이에 접촉 증분 변화가 발생한다.

### 충격 동역학 처리
각 스위칭 단계에서 충격량 동역학(impulse dynamics)을 사용하여 충돌 후 속도를 계산하고, 접촉 스위칭 순간에 운동량 보존과 비관통 제약을 만족하도록 보장한다. 이는 물리적 일관성을 확보하는 핵심 단계로, 소프트 제약 근사로 인한 드리프트를 피한다.

### 비용 함수 설계
비용 함수는 세 부분으로 구성된다: 질량 중심(CoM) 추적, 착지점(foot placement) 추적, 그리고 상태 및 제어의 정규화 항. 스윙 발 참조 궤적은 구간 선형 함수로 표현되며, 착지점이 참조 위치에서 벗어나면 강한 페널티를 부과한다. 사족의 모든 보행은 동일한 가중치와 비용 함수를 공유하고, 이족 보행은 유사한 가중치를 사용하여 프레임워크의 범용성을 보여준다.

### 웜 스타트 전략
상태 웜 스타트 𝐗₀는 접촉 구성 시퀀스의 공칭 신체 자세를 선형 보간하여 얻고, 동시에 공칭 관절 자세를 제공한다. 제어 웜 스타트 𝐔₀는 준정적 가정(quasi-static assumption)에 기반하여 계산된다—참조 자세를 평형점으로 삼고 Newton 단계를 통해 준정적 토크를 수치적으로 푼다. 이 전략은 수렴을 크게 가속화한다.

### 솔버 핵심
희소성 인지 Riccati 재귀를 채택하여 접촉 제약에서 발생하는 블록 희소 구조를 활용하고, 복잡도를 전차원 O(n³)에서 접촉 수와 관련된 준선형 규모로 낮춘다. 이것이 실시간성을 달성하는 근본 이유다.

## 핵심 혁신

1. **접촉 시퀀스의 1차 명시적 모델링**: 접촉 증분을 연속 완화 근사가 아닌 이산 변수로 최적화에 포함시켜, 충격 동역학을 정확히 처리할 수 있고 스위칭 순간에 궤적이 물리적으로 자기 일관성을 갖는다. 이는 기존 "소프트 접촉" 방법과 가장 본질적인 차이다.
2. **통합 가중치 아래의 다보행 일반화**: 사족의 모든 보행이 동일한 비용 가중치를 공유하고, 이족은 미세 조정만 필요하므로 프레임워크가 접촉 패턴 변화에 내재적 강건성을 가짐을 의미하며, 각 보행마다 수동 튜닝이 필요 없다. 이는 배포 비용을 크게 낮춘다.
3. **희소성 인지 솔버 아키텍처**: Riccati 재귀와 접촉 구조의 희소성을 결합하여 계산 복잡도가 접촉 규모에 따라 준선형으로 증가하게 하며, 이는 "계산 가능"에서 "빠르게 계산"으로의 도약으로 온라인 재계획의 길을 열었다.

## 실험 및 결과

논문은 사족 및 이족 플랫폼에서 프레임워크의 범용성과 효율성을 검증했지만, 원문 사실 요점에는 구체적인 대조 실험의 수치 세부 사항이 제공되지 않았다. 확인 가능한 사실은 다음과 같다: 모든 사족 보행이 동일한 가중치와 비용 함수를 공유하고, 이족 보행은 유사한 가중치를 사용한다; 웜 스타트는 선형 보간과 준정적 가정을 사용한다; 충격 동역학은 각 스위칭 단계에서 명시적으로 계산된다. 핵심 수치 요약은 다음과 같다:

| 항목 | 값 | 설명 |
|------|------|------|
| 사족 보행 가중치 | 통일 | 모든 보행 공유 |
| 이족 가중치 | 유사 | 사족과 유사 |
| 스윙 발 참조 | 구간 선형 | 참조 궤적 기술 |
| 착지점 페널티 | 강함 | 기준 이탈 시 중벌 |
| 웜 스타트 상태 | 선형 보간 | 공칭 자세 간 보간 |
| 웜 스타트 제어 | 준정적 | Newton 단계로 평형 토크 계산 |

논문은 해석 시간, 수렴 반복 횟수 또는 기준 방법과의 비교 수치를 명시하지 않아 가속 비율을 정량화할 수 없지만, "동일 가중치로 다보행 커버"라는 사실 자체가 프레임워크의 일반화 능력을 보여준다.

## 경계와 한계

논문은 다음 경계를 명시적으로 논의하지 않았다: 첫째, 접촉 시퀀스 자체는 여전히 사용자가 사전 설정하며, 프레임워크는 주어진 접촉 타이밍 하의 궤적을 최적화할 뿐 접촉 패턴을 자동 발견하지 않는다; 둘째, 준정적 웜 스타트 가정은 고속 동적 또는 큰 교란 시나리오에서 실패할 수 있으며, 이때 Newton 단계로 얻은 토크가 좋은 초기 추측이 아닐 수 있다; 셋째, 충격 동역학 처리는 접촉점 위치와 마찰 원뿔 모델의 정확성에 의존하므로 지면 파라미터에 민감하다; 넷째, 실험 플랫폼과 부하 범위가 사실 요점에 명시되지 않아 고동적 점프나 비구조화 지형에 대한 프레임워크의 적용 가능성은 알 수 없다.

## 엔지니어링 시사점

Crocoddyl을 재현하거나 채택할 때 세 가지를 우선 확인해야 한다: **접촉 시퀀스 정의 방식**—스위칭 단계의 구분이 실제 발바닥 이벤트와 일치하는지 확인해야 하며, 그렇지 않으면 충격 동역학 계산이 허위 운동량을 유발할 수 있다; **웜 스타트 품질**—준정적 가정은 저속 또는 준정적 보행에서 잘 작동하지만, 목표 궤적에 명확한 동적 요소(예: 빠른 걷기 또는 달리기)가 포함된 경우 이전 시간 영역 해나 시뮬레이션 데이터를 웜 스타트로 사용하는 것이 좋으며, 그렇지 않으면 수렴이 국소 최소값에 빠질 수 있다; **가중치 보정**—사족이 가중치를 공유하지만 이족은 여전히 "동일"이 아닌 "유사"한 조정이 필요하므로, 착지 시 논문의 보행을 먼저 재현한 후 파라미터를 변경하는 것이 좋다. 가장 쉽게 함정에 빠지는 부분은 착지점 강한 페널티와 스윙 발 구간 선형 참조의 조합이다—참조 궤적이 매끄럽지 않으면 강한 페널티가 진동을 증폭시킬 수 있으므로, 먼저 참조 궤적의 연속성을 확인한 후 페널티 계수를 조정하는 것이 좋다.
