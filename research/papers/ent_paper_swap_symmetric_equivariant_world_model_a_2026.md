---
$id: ent_paper_swap_symmetric_equivariant_world_model_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour'
  zh: 'SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour'
  ko: 'SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour'
summary:
  en: 'While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature
    forces them to redundantly encode left-right symmetric interactions as independent patterns. Institutions per source list:
    浙江大学 X-Mechanics、ZJU-Hangzhou 科创中心、Mirrorme Technology.'
  zh: SWAP 是一个端到端等变对称世界模型，由研究团队提出，用于解决四足机器人敏捷跑酷中左右对称交互冗余编码的问题。其核心贡献在于将对称性直接嵌入世界模型和 actor-critic 网络，使机器人能跨越 2.13 米间隙并攀爬 1.63
    米平台，创下四足跑酷新纪录，并展现出对未见镜像地形的鲁棒几何泛化能力。
  ko: 'While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature
    forces them to redundantly encode left-right symmetric interactions as independent patterns. Institutions per source list:
    浙江大学 X-Mechanics、ZJU-Hangzhou 科创中心、Mirrorme Technology.'
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
- swap
- symmetric
- equivariant
- world
- model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 796 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.19928 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.19928v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.19928 SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour'
  url: https://arxiv.org/abs/2606.19928
  accessed_at: '2026-07-31'
  date: '2026-06-18'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

SWAP 框架通过引入对称等变性作为结构先验，解决了潜在世界模型在极端跑酷任务中因纯数据驱动而冗余编码左右对称交互的问题。该框架将对称性直接嵌入世界模型和 actor-critic 网络，从而提升潜在空间的效率并增强下游策略的几何泛化能力。在真实世界测试中，搭载 SWAP 的机器人成功跨越 2.13 米间隙并攀爬 1.63 米平台，创下四足跑酷新纪录。此外，该框架对未见过的镜像地形展现出鲁棒的几何泛化能力，并在多种户外环境中实现零样本迁移。

## 核心内容
### 方法
SWAP 的核心创新在于将对称等变性作为结构先验，直接嵌入到世界模型和 actor-critic 网络中。具体而言，该框架采用端到端设计，确保模型在潜在空间中自动捕捉左右对称的几何规律，而非依赖数据驱动的方式冗余编码这些交互模式。这种设计减少了学习负担，并提升了潜在空间对下游策略的效率。

### 架构
SWAP 的架构包括三个主要组件：
- **对称世界模型**：通过等变编码器将观测数据映射到对称潜在空间，确保模型对左右镜像变换具有等变性。
- **对称 actor-critic 网络**：策略和价值网络同样采用等变设计，使决策过程与对称性保持一致。
- **端到端训练**：所有组件联合优化，以最大化任务性能并保持对称性约束。

### 实验设置
实验在真实世界中进行，使用四足机器人执行跑酷任务。测试场景包括：
- **间隙跨越**：机器人需跨越 2.13 米宽的间隙。
- **平台攀爬**：机器人需攀爬 1.63 米高的平台。
- **泛化测试**：在未见过的镜像地形和多种户外环境中评估零样本迁移能力。

### 关键数字
- **间隙跨越**：成功跨越 2.13 米间隙，创下四足跑酷新纪录。
- **平台攀爬**：成功攀爬 1.63 米平台，同样创下新纪录。
- **泛化性能**：对未见过的镜像地形展现出鲁棒的几何泛化能力，并在多种户外环境中实现零样本迁移。

### 结论
SWAP 框架证明了对称等变性作为结构先验的有效性，能够显著提升四足机器人跑酷的物理极限。通过减少冗余编码并增强几何泛化能力，该框架为学习型腿式运动提供了新的设计思路。未来工作可探索将对称等变性扩展到其他运动任务或更复杂的机器人形态。

## Overview
While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns. This inflates the learning burden and hinders the capture of geometric regularities, restricting the latent space's efficiency for downstream policies. To address this, we propose SWAP, an end-to-end equivariant symmetric world model. This framework embeds symmetry directly into both the world model and the actor-critic networks. In real-world tests, the robot leaps across a 2.13 m gap and climbs a 1.63 m platform, breaking records for quadruped parkour. Furthermore, the framework exhibits robust geometric generalization to unseen mirrored terrains and exceptional zero-shot transferability across diverse outdoor environments. These results demonstrate that symmetry equivariance is an effective structural prior for pushing the physical boundaries of learned legged locomotion.

## 参考
- https://arxiv.org/abs/2606.19928
- https://github.com/ImChong/Robotics_Notebooks

## 개요

SWAP 프레임워크는 대칭 등변성을 구조적 사전 지식으로 도입하여, 잠재 세계 모델이 극한 파쿠르 작업에서 순수 데이터 기반으로 좌우 대칭 상호작용을 중복 인코딩하는 문제를 해결합니다. 이 프레임워크는 대칭성을 세계 모델과 actor-critic 네트워크에 직접 내장하여 잠재 공간의 효율성을 높이고 하위 정책의 기하학적 일반화 능력을 강화합니다. 실제 세계 테스트에서 SWAP을 탑재한 로봇은 2.13미터 간격을 성공적으로 건너고 1.63미터 플랫폼을 기어올라 네 발 파쿠르의 새로운 기록을 세웠습니다. 또한 이 프레임워크는 보지 못한 미러 지형에 대해 강력한 기하학적 일반화 능력을 보여주며, 다양한 실외 환경에서 제로샷 전이를 구현합니다.

## 핵심 내용
### 방법
SWAP의 핵심 혁신은 대칭 등변성을 구조적 사전 지식으로 삼아 세계 모델과 actor-critic 네트워크에 직접 내장하는 것입니다. 구체적으로, 이 프레임워크는 엔드투엔드 설계를 채택하여 모델이 잠재 공간에서 좌우 대칭의 기하학적 규칙을 자동으로 포착하도록 하며, 데이터 기반 방식으로 이러한 상호작용 패턴을 중복 인코딩하지 않습니다. 이러한 설계는 학습 부담을 줄이고 하위 정책에 대한 잠재 공간의 효율성을 향상시킵니다.

### 아키텍처
SWAP의 아키텍처는 세 가지 주요 구성 요소로 이루어져 있습니다:
- **대칭 세계 모델**: 등변 인코더를 통해 관측 데이터를 대칭 잠재 공간에 매핑하여 모델이 좌우 미러 변환에 대해 등변성을 가지도록 보장합니다.
- **대칭 actor-critic 네트워크**: 정책 및 가치 네트워크도 등변 설계를 채택하여 의사 결정 과정이 대칭성과 일치하도록 합니다.
- **엔드투엔드 훈련**: 모든 구성 요소가 공동으로 최적화되어 작업 성능을 극대화하고 대칭성 제약을 유지합니다.

### 실험 설정
실험은 실제 세계에서 진행되었으며, 네 발 로봇이 파쿠르 작업을 수행했습니다. 테스트 시나리오는 다음과 같습니다:
- **간격 건너기**: 로봇은 2.13미터 너비의 간격을 건너야 합니다.
- **플랫폼 기어오르기**: 로봇은 1.63미터 높이의 플랫폼을 기어올라야 합니다.
- **일반화 테스트**: 보지 못한 미러 지형과 다양한 실외 환경에서 제로샷 전이 능력을 평가합니다.

### 주요 수치
- **간격 건너기**: 2.13미터 간격을 성공적으로 건너 네 발 파쿠르의 새로운 기록을 세웠습니다.
- **플랫폼 기어오르기**: 1.63미터 플랫폼을 성공적으로 기어올라 역시 새로운 기록을 세웠습니다.
- **일반화 성능**: 보지 못한 미러 지형에 대해 강력한 기하학적 일반화 능력을 보여주며, 다양한 실외 환경에서 제로샷 전이를 구현합니다.

### 결론
SWAP 프레임워크는 대칭 등변성이 구조적 사전 지식으로서의 효과를 입증하며, 네 발 로봇 파쿠르의 물리적 한계를 크게 향상시킬 수 있음을 보여줍니다. 중복 인코딩을 줄이고 기하학적 일반화 능력을 강화함으로써, 이 프레임워크는 학습 기반 보행 운동에 새로운 설계 방향을 제시합니다. 향후 연구는 대칭 등변성을 다른 운동 작업이나 더 복잡한 로봇 형태로 확장하는 것을 탐구할 수 있습니다.
