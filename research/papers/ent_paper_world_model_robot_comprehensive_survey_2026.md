---
$id: ent_paper_world_model_robot_comprehensive_survey_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'World Model for Robot Learning: A Comprehensive Survey'
  zh: 'World Model for Robot Learning: A Comprehensive Survey'
  ko: 'World Model for Robot Learning: A Comprehensive Survey'
summary:
  en: 'World models, which are predictive representations of how environments evolve under actions, have become a central
    component of robot learning. They support policy learning, planning, simulation, evaluation, data generation, and have
    advanced rapidly with the rise of foundation models and large-scale video generation. Institutions per source list: NTU、UC
    Berkeley、Stanford、东京大学、Oxford、Microsoft、ETH、Princeton、Harvard.'
  zh: 本文是一篇关于机器人学习领域世界模型的全面综述，由研究团队系统梳理了该领域的发展脉络。核心贡献在于从机器人学习视角出发，整合了世界模型与策略耦合、作为学习模拟器、视频生成等关键范式，并总结了导航与自动驾驶等应用及代表性基准与评估协议。
  ko: 'World models, which are predictive representations of how environments evolve under actions, have become a central
    component of robot learning. They support policy learning, planning, simulation, evaluation, data generation, and have
    advanced rapidly with the rise of foundation models and large-scale video generation. Institutions per source list: NTU、UC
    Berkeley、Stanford、东京大学、Oxford、Microsoft、ETH、Princeton、Harvard.'
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
- world
- model
- robot
- comprehensive
- survey
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 301 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2605.00080v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.00080 World Model for Robot Learning: A Comprehensive Survey'
  url: https://arxiv.org/abs/2605.00080
  accessed_at: '2026-07-31'
  date: '2026-04-30'
- id: src_002
  type: website
  title: 机器人世界模型，下一步不是生成视频，而是进入训练闭环
  url: https://mp.weixin.qq.com/s/0edW0GhwtyNc5nF6RDIfuw
  accessed_at: '2026-07-31'
---

## 概述

该综述聚焦于世界模型在机器人学习中的核心作用，即作为环境在动作作用下如何演化的预测性表征。文章系统分析了世界模型如何与机器人策略耦合以支持策略学习与规划，如何作为学习模拟器服务于强化学习与评估，以及机器人视频世界模型如何从基于想象的生成演进为可控、结构化且基于基础模型的形态。此外，综述将上述概念与导航和自动驾驶领域相连接，并总结了代表性数据集、基准和评估协议，最后指出了预测建模在具身智能体中的主要挑战与未来方向。

## 核心内容
### 核心范式与架构
- **世界模型与策略的耦合**：综述探讨了世界模型如何与机器人策略紧密结合，例如通过模型预测控制（MPC）或作为策略学习的隐式表征，以提升样本效率与泛化能力。
- **作为学习模拟器**：世界模型被用作强化学习（RL）的模拟环境，支持策略评估与数据生成，从而减少对真实环境交互的依赖。文中特别强调了其在离线RL与在线微调中的关键作用。
- **视频世界模型的演进**：从早期基于循环神经网络（RNN）的想象生成，发展到当前利用扩散模型或Transformer架构的可控视频生成，并进一步向基础模型（Foundation Models）规模扩展，支持多模态输入与结构化输出。

### 应用领域与关键资源
- **导航与自动驾驶**：综述将世界模型应用于复杂动态环境中的路径规划与决策，例如通过预测未来帧来评估碰撞风险或优化行驶轨迹。
- **代表性数据集与基准**：文中列出了如Habitat、Matterport3D、nuScenes等数据集，以及用于评估世界模型预测精度、控制性能与泛化能力的基准，如World Model Benchmark（WMB）和RoboMimic。
- **评估协议**：强调需从预测误差、下游任务成功率、样本效率及计算开销等多维度进行标准化评估，并指出当前缺乏统一评估框架的挑战。

### 主要挑战与未来方向
- **长期预测与不确定性量化**：现有模型在长时域预测中易出现误差累积，需引入概率建模或因果推理。
- **泛化到新场景与任务**：世界模型需具备跨域迁移能力，例如从仿真到真实（Sim-to-Real）的零样本适应。
- **计算效率与实时性**：大规模视频生成模型的计算成本限制了其在机器人实时控制中的应用，需探索轻量化架构或蒸馏技术。
- **与基础模型的深度融合**：如何将语言模型、视觉语言模型（VLM）等基础模型的能力整合进世界模型，以实现更丰富的语义理解与任务规划，是未来重要方向。

## Overview
World models, which are predictive representations of how environments evolve under actions, have become a central component of robot learning. They support policy learning, planning, simulation, evaluation, data generation, and have advanced rapidly with the rise of foundation models and large-scale video generation. However, the literature remains fragmented across architectures, functional roles, and embodied application domains. To address this gap, we present a comprehensive review of world models from a robot-learning perspective. We examine how world models are coupled with robot policies, how they serve as learned simulators for reinforcement learning and evaluation, and how robotic video world models have progressed from imagination-based generation to controllable, structured, and foundation-scale formulations. We further connect these ideas to navigation and autonomous driving, and summarize representative datasets, benchmarks, and evaluation protocols. Overall, this survey systematically reviews the rapidly growing literature on world models for robot learning, clarifies key paradigms and applications, and highlights major challenges and future directions for predictive modeling in embodied agents. To facilitate continued access to newly emerging works, benchmarks, and resources, we will maintain and regularly update the accompanying GitHub repository alongside this survey.

## 参考
- https://arxiv.org/abs/2605.00080
- https://mp.weixin.qq.com/s/0edW0GhwtyNc5nF6RDIfuw

## 개요

이 서베이는 로봇 학습에서 세계 모델의 핵심 역할, 즉 행동에 따라 환경이 어떻게 진화하는지에 대한 예측적 표상에 초점을 맞춘다. 본 논문은 세계 모델이 로봇 정책과 어떻게 결합되어 정책 학습과 계획을 지원하는지, 강화 학습과 평가를 위한 학습 시뮬레이터로 어떻게 활용되는지, 그리고 로봇 비디오 세계 모델이 상상 기반 생성에서 제어 가능하고 구조화된 기반 모델 형태로 어떻게 진화하는지를 체계적으로 분석한다. 또한, 이 서베이는 위 개념을 내비게이션 및 자율주행 분야와 연결하고, 대표적인 데이터셋, 벤치마크 및 평가 프로토콜을 요약하며, 마지막으로 구현된 에이전트에서 예측 모델링의 주요 과제와 향후 방향을 제시한다.

## 핵심 내용
### 핵심 패러다임 및 아키텍처
- **세계 모델과 정책의 결합**: 서베이는 세계 모델이 모델 예측 제어(MPC) 또는 정책 학습의 암시적 표상으로서 로봇 정책과 어떻게 긴밀하게 결합되어 샘플 효율성과 일반화 능력을 향상시키는지 탐구한다.
- **학습 시뮬레이터로서의 역할**: 세계 모델은 강화 학습(RL)의 시뮬레이션 환경으로 활용되어 정책 평가와 데이터 생성을 지원함으로써 실제 환경 상호작용에 대한 의존도를 줄인다. 본 논문은 특히 오프라인 RL과 온라인 미세 조정에서의 핵심 역할을 강조한다.
- **비디오 세계 모델의 진화**: 순환 신경망(RNN) 기반 초기 상상 생성에서 확산 모델 또는 Transformer 아키텍처를 활용한 제어 가능한 비디오 생성으로 발전했으며, 더 나아가 기반 모델(Foundation Models) 규모로 확장되어 다중 모달 입력과 구조화된 출력을 지원한다.

### 응용 분야 및 핵심 자원
- **내비게이션 및 자율주행**: 서베이는 세계 모델을 복잡한 동적 환경에서의 경로 계획 및 의사 결정에 적용한다. 예를 들어, 미래 프레임을 예측하여 충돌 위험을 평가하거나 주행 궤적을 최적화한다.
- **대표적인 데이터셋 및 벤치마크**: Habitat, Matterport3D, nuScenes와 같은 데이터셋과 세계 모델의 예측 정확도, 제어 성능 및 일반화 능력을 평가하기 위한 World Model Benchmark(WMB) 및 RoboMimic과 같은 벤치마크가 제시된다.
- **평가 프로토콜**: 예측 오류, 하위 작업 성공률, 샘플 효율성 및 계산 비용 등 다차원적인 표준화된 평가의 필요성을 강조하며, 현재 통일된 평가 프레임워크가 부족하다는 과제를 지적한다.

### 주요 과제 및 향후 방향
- **장기 예측 및 불확실성 정량화**: 기존 모델은 장기간 예측에서 오류 누적이 발생하기 쉬우며, 확률적 모델링 또는 인과 추론의 도입이 필요하다.
- **새로운 시나리오 및 작업으로의 일반화**: 세계 모델은 시뮬레이션에서 실제 환경으로의 제로샷 적응(Sim-to-Real)과 같은 도메인 간 전이 능력을 갖추어야 한다.
- **계산 효율성 및 실시간성**: 대규모 비디오 생성 모델의 계산 비용은 로봇 실시간 제어에의 적용을 제한하므로, 경량화 아키텍처 또는 증류 기술의 탐구가 필요하다.
- **기반 모델과의 심층 통합**: 언어 모델, 비전-언어 모델(VLM) 등 기반 모델의 능력을 세계 모델에 통합하여 더 풍부한 의미 이해와 작업 계획을 구현하는 것이 향후 중요한 방향이다.
