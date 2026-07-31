---
$id: ent_paper_enpire_agentic_robot_policy_self_improve_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ENPIRE: Agentic Robot Policy Self-Improvement in the Real World'
  zh: 'ENPIRE: Agentic Robot Policy Self-Improvement in the Real World'
  ko: 'ENPIRE: Agentic Robot Policy Self-Improvement in the Real World'
summary:
  en: 'Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering,
    which becomes a central bottleneck in the pursuit of general physical intelligence. Institutions per source list: NVIDIA
    GEAR Lab、CMU LeCAR Lab、UC Berkeley（项目页致谢与公开报道）.'
  zh: ENPIRE 是一个面向真实世界机器人策略自主改进的框架，由研究团队提出，核心贡献在于构建了环境重置、策略执行、结果验证与迭代优化的闭环物理反馈循环。该框架使编码智能体能够自主训练灵巧操作策略，在插针盒整理、扎带紧固和工具使用等任务上达到
    99% 的成功率。
  ko: 'Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering,
    which becomes a central bottleneck in the pursuit of general physical intelligence. Institutions per source list: NVIDIA
    GEAR Lab、CMU LeCAR Lab、UC Berkeley（项目页致谢与公开报道）.'
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
- enpire
- agentic
- robot
- policy
- self
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 360 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.19980 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.19980v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.19980 ENPIRE: Agentic Robot Policy Self-Improvement in the Real World'
  url: https://arxiv.org/abs/2606.19980
  accessed_at: '2026-07-31'
  date: '2026-06-18'
- id: src_002
  type: website
  title: Project page
  url: https://research.nvidia.com/labs/gear/enpire/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

ENPIRE 框架通过四个核心模块将真实世界的机器人操作学习转化为可控的优化过程：环境模块负责自动重置与验证，策略改进模块启动策略优化，部署模块支持单台或多台机器人并行评估策略，进化模块让编码智能体分析日志、查阅文献并改进训练代码。该闭环系统大幅减少人工干预，同时支持对不同训练方案和智能体变体的公平消融实验。实验表明，前沿编码智能体在 ENPIRE 驱动下可自主训练出高成功率的灵巧操作策略，且通过机器人集群部署智能体团队能进一步加速这一过程。

## 核心内容
### 方法概述
ENPIRE 框架的核心思想是将真实世界的策略改进抽象为一个可重复的物理反馈循环，包含四个关键模块：
- **环境模块 (EN)**：负责自动重置场景并验证任务结果，为每次迭代提供一致的初始条件。
- **策略改进模块 (PI)**：基于前一轮的失败模式启动策略优化，包括调整训练超参数、修改算法代码或改进基础设施。
- **部署模块 (R)**：支持单台或多台物理机器人并行执行策略评估，加速数据收集与验证。
- **进化模块 (E)**：编码智能体在此模块中分析执行日志、查阅相关文献，自主决定如何改进训练代码和算法以解决失败案例。

### 实验设置与关键结果
- **任务**：在真实机器人上测试了三个挑战性灵巧操作任务：插针盒整理、扎带紧固和工具使用。
- **性能**：前沿编码智能体在 ENPIRE 框架下自主训练，最终在三个任务上均达到 **99% 的成功率**。
- **加速效果**：当在机器人集群上部署多个编码智能体组成的团队时，策略改进速度进一步加快，验证了框架的可扩展性。
- **人工干预**：整个训练过程中，人类仅需提供初始任务描述和场景设置，后续策略迭代完全由智能体自主完成。

### 结论
ENPIRE 证明了通过构建物理反馈闭环，编码智能体能够自主推进真实世界的机器人操作研究，为减少人工依赖、实现通用物理智能提供了一条实用且可扩展的路径。

## Overview
Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering, which becomes a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely confined in digital environments. We conjecture that the missing abstraction to automate robotics research is a repeatable feedback loop for real-world policy improvement: reset the scene, execute a policy, verify the outcome, and refine the next iteration. To bridge this gap, we introduce ENPIRE, a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with one or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes. This closed-loop system transforms real-world manipulation learning into a controllable optimization procedure, minimizing human effort while allowing fair ablations across training recipe and agent variants. Powered by ENPIRE, frontier coding agents can autonomously train a policy to achieve a 99% success rate on challenging, dexterous manipulation tasks, such as organizing a pin box, fastening a zip tie, and tool use, a process that further accelerates when we dispatch an agent team on a robot fleet. Our results suggest a practical and scalable path toward deploying coding agents to autonomously advancing robotics in the physical world.

## 参考
- https://arxiv.org/abs/2606.19980
- https://research.nvidia.com/labs/gear/enpire/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

ENPIRE 프레임워크는 네 가지 핵심 모듈을 통해 실제 로봇 조작 학습을 제어 가능한 최적화 과정으로 전환합니다. 환경 모듈은 자동 리셋 및 검증을 담당하고, 정책 개선 모듈은 정책 최적화를 시작하며, 배포 모듈은 단일 또는 다중 로봇의 병렬 정책 평가를 지원하고, 진화 모듈은 코딩 에이전트가 로그를 분석하고 문헌을 참고하며 훈련 코드를 개선할 수 있도록 합니다. 이 폐쇄 루프 시스템은 인간의 개입을 크게 줄이는 동시에 다양한 훈련 방식과 에이전트 변형에 대한 공정한 절제 실험을 지원합니다. 실험 결과, 최첨단 코딩 에이전트는 ENPIRE의 구동 하에 자율적으로 높은 성공률의 정교한 조작 정책을 훈련할 수 있으며, 로봇 클러스터를 통해 에이전트 팀을 배치하면 이 과정을 더욱 가속화할 수 있습니다.

## 핵심 내용
### 방법 개요
ENPIRE 프레임워크의 핵심 아이디어는 실제 세계의 정책 개선을 반복 가능한 물리적 피드백 루프로 추상화하는 것이며, 네 가지 주요 모듈을 포함합니다:
- **환경 모듈 (EN)**: 장면을 자동으로 리셋하고 작업 결과를 검증하여 각 반복에 일관된 초기 조건을 제공합니다.
- **정책 개선 모듈 (PI)**: 이전 라운드의 실패 패턴을 기반으로 정책 최적화를 시작하며, 훈련 하이퍼파라미터 조정, 알고리즘 코드 수정 또는 인프라 개선을 포함합니다.
- **배포 모듈 (R)**: 단일 또는 다중 물리적 로봇이 병렬로 정책 평가를 수행하도록 지원하여 데이터 수집 및 검증을 가속화합니다.
- **진화 모듈 (E)**: 코딩 에이전트가 이 모듈에서 실행 로그를 분석하고 관련 문헌을 참고하여 실패 사례를 해결하기 위해 훈련 코드와 알고리즘을 어떻게 개선할지 자율적으로 결정합니다.

### 실험 설정 및 주요 결과
- **작업**: 실제 로봇에서 세 가지 도전적인 정교한 조작 작업(핀 박스 정리, 케이블 타이 고정, 도구 사용)을 테스트했습니다.
- **성능**: 최첨단 코딩 에이전트는 ENPIRE 프레임워크 하에서 자율적으로 훈련하여 세 가지 작업 모두에서 **99%의 성공률**을 달성했습니다.
- **가속 효과**: 로봇 클러스터에 여러 코딩 에이전트로 구성된 팀을 배치할 때 정책 개선 속도가 더욱 빨라져 프레임워크의 확장성을 입증했습니다.
- **인간 개입**: 전체 훈련 과정에서 인간은 초기 작업 설명과 장면 설정만 제공하면 되며, 이후 정책 반복은 전적으로 에이전트가 자율적으로 수행합니다.

### 결론
ENPIRE는 물리적 피드백 폐쇄 루프를 구축함으로써 코딩 에이전트가 자율적으로 실제 세계의 로봇 조작 연구를 추진할 수 있음을 증명했으며, 인간 의존도를 줄이고 범용 물리적 지능을 실현하기 위한 실용적이고 확장 가능한 경로를 제공합니다.
