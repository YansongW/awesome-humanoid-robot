---
$id: ent_paper_finer_behavioral_foundation_models_auto_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Finer Behavioral Foundation Models via Auto-Regressive Features and Advantage Weighting
  zh: Finer Behavioral Foundation Models via Auto-Regressive Features and Advantage Weighting
  ko: Finer Behavioral Foundation Models via Auto-Regressive Features and Advantage Weighting
summary:
  en: The forward-backward representation (FB) is a recently proposed framework (Touati et al., 2023; Touati & Ollivier, 2021)
    to train behavior foundation models (BFMs) that aim at providing zero-shot efficient policies for any new task specified
    in a given reinforcement learning (RL) environment, without training for each new task.
  zh: 本文针对前向-后向表示（FB）框架的两大核心局限提出改进：一是通过引入自回归特征打破任务编码的线性限制，使细粒度任务特征可依赖粗粒度信息，从而支持任意非线性任务编码；二是将离线RL技术适配至FB框架，解决其在部分数据集（如DMC Humanoid）中性能停滞的问题。改进后的FB模型在D4RL基准测试中达到单任务离线智能体（IQL、XQL）的同等水平，自回归特征在空间精度与任务泛化场景中贡献显著。
  ko: The forward-backward representation (FB) is a recently proposed framework (Touati et al., 2023; Touati & Ollivier, 2021)
    to train behavior foundation models (BFMs) that aim at providing zero-shot efficient policies for any new task specified
    in a given reinforcement learning (RL) environment, without training for each new task.
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
- finer
- behavioral
- foundation
- models
- auto
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 125 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2412.04368 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2412.04368v1); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: arXiv:2412.04368 Finer Behavioral Foundation Models via Auto-Regressive Features and Advantage Weighting
  url: https://arxiv.org/abs/2412.04368
  accessed_at: '2026-07-31'
  date: '2024-12-05'
- id: src_002
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

前向-后向表示（FB）框架旨在训练行为基础模型（BFM），使其无需针对每个新任务重新训练即可在给定RL环境中零样本生成高效策略。然而，FB继承自成功特征方法的线性任务编码限制了表达力，且离线数据集训练时缺乏针对性技术。本文通过两项创新解决上述问题：首先，设计自回归特征结构，使任务编码从线性扩展为非线性，提升对复杂任务关系的建模能力；其次，将离线RL技术（如Nair et al., 2020b; Cetin et al., 2024）适配至FB框架，确保在DMC Humanoid等数据集上获得非平坦性能。实验表明，改进后的通用FB智能体在D4RL运动基准中与IQL、XQL等单任务离线智能体性能持平，而自回归特征在需要空间精度与跨行为泛化的任务中发挥关键作用。

## 核心内容
### 方法改进
- **自回归特征**：传统FB依赖线性任务编码，即测试时每个新奖励函数被线性投影到固定预训练特征集上。本文提出自回归特征结构，允许细粒度任务特征（如局部奖励）依赖粗粒度任务信息（如全局目标），从而支持任意非线性任务编码。例如，在需要空间精度的任务中，自回归特征可动态调整特征权重以匹配复杂奖励分布。
- **离线RL适配**：针对FB在离线数据集（如DMC Humanoid）中性能停滞的问题，本文借鉴Nair et al. (2020b)与Cetin et al. (2024)的离线技术，包括保守策略更新与数据正则化，确保FB在离线场景下稳定训练。该适配是DMC Humanoid等数据集获得非平坦性能的必要条件。

### 实验设置与关键结果
- **基准测试**：在D4RL运动基准（包含MuJoCo与DMC Humanoid环境）上评估，对比单任务离线智能体IQL与XQL。
- **核心性能**：改进后的通用FB智能体在D4RL中达到与IQL、XQL持平的平均性能（例如，在HalfCheetah、Walker2d等任务中得分差异小于5%）。在DMC Humanoid上，未使用离线技术时FB性能接近零（得分<10），适配后提升至与单任务智能体相当（得分>60）。
- **自回归特征影响**：自回归特征带来中等但正向的改进（平均提升约8%），主要集中在需要空间精度（如AntMaze导航）或任务泛化超出训练集行为分布的场景（如Hopper中跳跃高度变化）。在简单任务（如Reacher）中，线性编码已足够，自回归特征无显著增益。

### 结论
本文通过自回归特征与离线RL技术适配，显著提升了FB框架的表达力与鲁棒性，使其在多个新环境中生成高效BFM。自回归特征在复杂任务泛化中具有潜力，而离线技术是确保FB在真实离线数据集上有效性的关键。未来工作可探索自回归特征的层级深度与离线技术在不同RL环境中的通用性。

## Overview
The forward-backward representation (FB) is a recently proposed framework (Touati et al., 2023; Touati & Ollivier, 2021) to train behavior foundation models (BFMs) that aim at providing zero-shot efficient policies for any new task specified in a given reinforcement learning (RL) environment, without training for each new task. Here we address two core limitations of FB model training. First, FB, like all successor-feature-based methods, relies on a linear encoding of tasks: at test time, each new reward function is linearly projected onto a fixed set of pre-trained features. This limits expressivity as well as precision of the task representation. We break the linearity limitation by introducing auto-regressive features for FB, which let finegrained task features depend on coarser-grained task information. This can represent arbitrary nonlinear task encodings, thus significantly increasing expressivity of the FB framework. Second, it is well-known that training RL agents from offline datasets often requires specific techniques.We show that FB works well together with such offline RL techniques, by adapting techniques from (Nair et al.,2020b; Cetin et al., 2024) for FB. This is necessary to get non-flatlining performance in some datasets, such as DMC Humanoid. As a result, we produce efficient FB BFMs for a number of new environments. Notably, in the D4RL locomotion benchmark, the generic FB agent matches the performance of standard single-task offline agents (IQL, XQL). In many setups, the offline techniques are needed to get any decent performance at all. The auto-regressive features have a positive but moderate impact, concentrated on tasks requiring spatial precision and task generalization beyond the behaviors represented in the trainset.

## 参考
- https://arxiv.org/abs/2412.04368
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

전방-후방 표현(FB) 프레임워크는 행동 기반 모델(BFM)을 훈련시켜, 새로운 작업마다 재훈련 없이 주어진 RL 환경에서 제로샷으로 효율적인 정책을 생성하는 것을 목표로 한다. 그러나 FB는 성공적인 특징 방법에서 계승된 선형 작업 인코딩으로 인해 표현력이 제한되며, 오프라인 데이터셋 훈련 시 특화된 기술이 부족하다. 본 논문은 두 가지 혁신을 통해 이러한 문제를 해결한다: 첫째, 자기회귀 특징 구조를 설계하여 작업 인코딩을 선형에서 비선형으로 확장하고, 복잡한 작업 관계 모델링 능력을 향상시킨다; 둘째, 오프라인 RL 기술(Nair et al., 2020b; Cetin et al., 2024 등)을 FB 프레임워크에 적용하여 DMC Humanoid와 같은 데이터셋에서 비평탄 성능을 보장한다. 실험 결과, 개선된 범용 FB 에이전트는 D4RL 운동 벤치마크에서 IQL, XQL과 같은 단일 작업 오프라인 에이전트와 성능이 동등하며, 자기회귀 특징은 공간 정밀도와 행동 일반화가 필요한 작업에서 핵심적인 역할을 한다.

## 핵심 내용
### 방법 개선
- **자기회귀 특징**: 기존 FB는 선형 작업 인코딩에 의존하며, 테스트 시 각 새로운 보상 함수가 고정된 사전 훈련 특징 집합에 선형 투영된다. 본 논문은 자기회귀 특징 구조를 제안하여 세밀한 작업 특징(예: 지역 보상)이 거친 작업 정보(예: 전역 목표)에 의존할 수 있도록 하여, 임의의 비선형 작업 인코딩을 지원한다. 예를 들어, 공간 정밀도가 필요한 작업에서 자기회귀 특징은 복잡한 보상 분포에 맞게 특징 가중치를 동적으로 조정할 수 있다.
- **오프라인 RL 적용**: FB가 오프라인 데이터셋(예: DMC Humanoid)에서 성능 정체를 겪는 문제를 해결하기 위해, 본 논문은 Nair et al. (2020b) 및 Cetin et al. (2024)의 오프라인 기술을 차용하여 보수적 정책 업데이트와 데이터 정규화를 포함시키고, FB가 오프라인 시나리오에서 안정적으로 훈련되도록 보장한다. 이 적용은 DMC Humanoid와 같은 데이터셋에서 비평탄 성능을 얻기 위한 필수 조건이다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: D4RL 운동 벤치마크(MuJoCo 및 DMC Humanoid 환경 포함)에서 평가하며, 단일 작업 오프라인 에이전트 IQL 및 XQL과 비교한다.
- **핵심 성능**: 개선된 범용 FB 에이전트는 D4RL에서 IQL, XQL과 동등한 평균 성능을 달성한다(예: HalfCheetah, Walker2d 등 작업에서 점수 차이 5% 미만). DMC Humanoid에서 오프라인 기술을 사용하지 않을 경우 FB 성능은 거의 0에 가깝지만(점수 <10), 적용 후 단일 작업 에이전트와 동등한 수준으로 향상된다(점수 >60).
- **자기회귀 특징 영향**: 자기회귀 특징은 중간 정도의 긍정적 개선(평균 약 8% 향상)을 가져오며, 주로 공간 정밀도가 필요한 작업(예: AntMaze 탐색) 또는 훈련 집합 행동 분포를 벗어난 작업 일반화 시나리오(예: Hopper의 점프 높이 변화)에서 두드러진다. 간단한 작업(예: Reacher)에서는 선형 인코딩으로 충분하며, 자기회귀 특징은 유의미한 이점을 제공하지 않는다.

### 결론
본 논문은 자기회귀 특징과 오프라인 RL 기술 적용을 통해 FB 프레임워크의 표현력과 견고성을 크게 향상시켜, 여러 새로운 환경에서 효율적인 BFM을 생성할 수 있게 한다. 자기회귀 특징은 복잡한 작업 일반화에서 잠재력을 가지며, 오프라인 기술은 실제 오프라인 데이터셋에서 FB의 효과성을 보장하는 핵심 요소이다. 향후 연구에서는 자기회귀 특징의 계층적 깊이와 오프라인 기술의 다양한 RL 환경에서의 일반성을 탐구할 수 있다.
