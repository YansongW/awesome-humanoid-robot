---
$id: ent_paper_wang_vla_survey_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines'
  zh: 机器人视觉-语言-动作：数据集、基准与数据引擎综述
  ko: '로보틱스에서의 비전-언어-액션: 데이터셋, 벤치마크 및 데이터 엔진에 대한 서베이'
summary:
  en: A 2026 survey arguing that VLA progress now depends more on data infrastructure and evaluation co-design than on model
    architecture, organized around datasets, benchmarks, and data engines.
  zh: 本文是2026年关于视觉-语言-动作（VLA）模型的综述，指出VLA进展的关键瓶颈已从模型架构转向数据基础设施与评估协同设计。研究围绕数据集、基准测试和数据引擎三大支柱展开系统分析，揭示了数据保真度与成本之间的根本性权衡，以及现有评估协议在组合泛化和长程推理方面的结构性缺陷。
  ko: 2026년 서베이로, VLA의 발전은 모델 아키텍처보다 데이터 인프라와 평가 공동 설계에 더 많이 의존하고 있으며, 데이터셋, 벤치마크, 데이터 엔진 세 축으로 구성됨.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- survey
- datasets
- benchmarks
- data_engines
- sim_to_real
- embodied_ai
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.23001v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_paper_wang_vla_survey_2026
  type: paper
  title: 'Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines'
  url: https://arxiv.org/abs/2604.23001
  date: '2026-04-24'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: cites
  description:
    en: The survey cites Open X-Embodiment as a widely used cross-embodiment pretraining dataset.
    zh: 该综述引用 Open X-Embodiment 作为常用的跨具身预训练数据集。
    ko: 해당 서베이는 Open X-Embodiment를 널리 사용되는 cross-embodiment 사전 학습 데이터셋으로 인용함.
- id: ent_dataset_droid
  relationship: cites
  description:
    en: The survey cites DROID as a distributed real-world dataset emphasizing visual and environmental variation.
    zh: 该综述引用 DROID 作为强调视觉与环境变化的分布式真实世界数据集。
    ko: 해당 서베이는 DROID를 시각 및 환경 변화를 강조하는 분산 실제 데이터셋으로 인용함.
- id: ent_benchmark_humanoidbench
  relationship: cites
  description:
    en: The survey discusses HumanoidBench as a simulation benchmark for whole-body locomotion and manipulation.
    zh: 该综述讨论 HumanoidBench 作为全身运动与操作的仿真基准。
    ko: 해당 서베이는 HumanoidBench를 전신 로코모션 및 조작을 위한 시뮬레이션 벤치마크로 논의함.
- id: ent_benchmark_libero
  relationship: cites
  description:
    en: The survey cites LIBERO as a representative short-horizon table-top VLA benchmark.
    zh: 该综述引用 LIBERO 作为代表性短程桌面 VLA 基准。
    ko: 해당 서베이는 LIBERO를 대표적인 단기 테이블탑 VLA 벤치마크로 인용함.
- id: ent_tech_mimicgen
  relationship: cites
  description:
    en: The survey discusses MimicGen as a demonstration augmentation method that scales simulator data.
    zh: 该综述讨论 MimicGen 作为扩展仿真器数据的演示增强方法。
    ko: 해당 서베이는 MimicGen을 시뮬레이터 데이터를 확장하는 데모 증강 방법으로 논의함.
- id: ent_tech_robogen
  relationship: cites
  description:
    en: The survey discusses RoboGen as an LLM-driven automatic task-generation framework for simulation.
    zh: 该综述讨论 RoboGen 作为由大语言模型驱动的仿真自动任务生成框架。
    ko: 해당 서베이는 RoboGen을 LLM 기반 시뮬레이션 자동 작업 생성 프레임워크로 논의함.
theoretical_depth:
- system
---
## 概述
这篇2026年的综述论文提出，视觉-语言-动作（VLA）模型的未来发展将更多依赖于高保真数据引擎与结构化评估协议的协同设计，而非模型架构本身。作者从数据集、基准测试和数据引擎三个维度进行了数据驱动的系统分析：在数据集方面，按实体多样性、模态组成和动作空间公式对真实世界与合成语料库进行分类，揭示了制约大规模数据收集的保真度-成本权衡；在基准测试方面，联合分析任务复杂度和环境结构，指出现有协议在组合泛化和长程推理评估中的结构性空白；在数据引擎方面，审视了基于仿真、视频重建和自动任务生成的范式，识别出它们在物理基础与仿真到现实迁移中的共同局限。

## 核心内容
### 核心论点
- VLA进展的瓶颈已从模型架构转向数据基础设施与评估的协同设计
- 数据基础设施应被视为第一类研究问题，而非背景性事务

### 数据集分析
- 对真实世界与合成语料库按三个维度分类：实体多样性、模态组成、动作空间公式
- 揭示保真度-成本权衡：高保真真实数据采集成本高昂，合成数据虽成本低但存在物理保真度不足问题
- 该权衡从根本上制约了大规模数据收集

### 基准测试分析
- 联合分析任务复杂度与环境结构
- 发现现有评估协议存在两大结构性空白：
  - 组合泛化评估不足
  - 长程推理评估缺失

### 数据引擎范式
- 三种主要范式：基于仿真、视频重建、自动任务生成
- 共同局限：物理基础不足、仿真到现实迁移困难

### 四大开放挑战
1. 表示对齐（representation alignment）
2. 多模态监督（multimodal supervision）
3. 推理评估（reasoning assessment）
4. 可扩展数据生成（scalable data generation）

## Overview
Despite remarkable progress in Vision--Language--Action (VLA) models, a central bottleneck remains underexamined: the data infrastructure that underlies embodied learning. In this survey, we argue that future advances in VLA will depend less on model architecture and more on the co-design of high-fidelity data engines and structured evaluation protocols. To this end, we present a systematic, data-centric analysis of VLA research organized around three pillars: datasets, benchmarks, and data engines. For datasets, we categorize real-world and synthetic corpora along embodiment diversity, modality composition, and action space formulation, revealing a persistent fidelity-cost trade-off that fundamentally constrains large-scale collection. For benchmarks, we analyze task complexity and environment structure jointly, exposing structural gaps in compositional generalization and long-horizon reasoning evaluation that existing protocols fail to address. For data engines, we examine simulation-based, video-reconstruction, and automated task-generation paradigms, identifying their shared limitations in physical grounding and sim-to-real transfer. Synthesizing these analyses, we distill four open challenges: representation alignment, multimodal supervision, reasoning assessment, and scalable data generation. Addressing them, we argue, requires treating data infrastructure as a first-class research problem rather than a background concern.

## 개요
비전-언어-행동(VLA) 모델의 놀라운 발전에도 불구하고, 체화된 학습의 기반이 되는 데이터 인프라는 여전히 충분히 검토되지 않은 핵심 병목 현상으로 남아 있습니다. 본 서베이에서는 VLA의 미래 발전이 모델 아키텍처보다는 고충실도 데이터 엔진과 구조화된 평가 프로토콜의 공동 설계에 더 크게 의존할 것이라고 주장합니다. 이를 위해 데이터셋, 벤치마크, 데이터 엔진이라는 세 가지 축을 중심으로 체계적이고 데이터 중심적인 VLA 연구 분석을 제시합니다. 데이터셋의 경우, 실제 및 합성 코퍼스를 체화 다양성, 모달리티 구성, 행동 공간 공식화에 따라 분류하여 대규모 수집을 근본적으로 제약하는 지속적인 충실도-비용 트레이드오프를 드러냅니다. 벤치마크의 경우, 작업 복잡성과 환경 구조를 함께 분석하여 기존 프로토콜이 해결하지 못하는 구성적 일반화 및 장기 추론 평가의 구조적 격차를 노출합니다. 데이터 엔진의 경우, 시뮬레이션 기반, 비디오 재구성, 자동 작업 생성 패러다임을 검토하여 물리적 기반 및 시뮬레이션-실제 전환에서의 공통된 한계를 식별합니다. 이러한 분석을 종합하여 표현 정렬, 다중 모달 감독, 추론 평가, 확장 가능한 데이터 생성이라는 네 가지 공개 과제를 도출합니다. 이를 해결하기 위해서는 데이터 인프라를 배경 문제가 아닌 일급 연구 문제로 취급해야 한다고 주장합니다.

## 핵심 내용
비전-언어-행동(VLA) 모델의 놀라운 발전에도 불구하고, 체화된 학습의 기반이 되는 데이터 인프라는 여전히 충분히 검토되지 않은 핵심 병목 현상으로 남아 있습니다. 본 서베이에서는 VLA의 미래 발전이 모델 아키텍처보다는 고충실도 데이터 엔진과 구조화된 평가 프로토콜의 공동 설계에 더 크게 의존할 것이라고 주장합니다. 이를 위해 데이터셋, 벤치마크, 데이터 엔진이라는 세 가지 축을 중심으로 체계적이고 데이터 중심적인 VLA 연구 분석을 제시합니다. 데이터셋의 경우, 실제 및 합성 코퍼스를 체화 다양성, 모달리티 구성, 행동 공간 공식화에 따라 분류하여 대규모 수집을 근본적으로 제약하는 지속적인 충실도-비용 트레이드오프를 드러냅니다. 벤치마크의 경우, 작업 복잡성과 환경 구조를 함께 분석하여 기존 프로토콜이 해결하지 못하는 구성적 일반화 및 장기 추론 평가의 구조적 격차를 노출합니다. 데이터 엔진의 경우, 시뮬레이션 기반, 비디오 재구성, 자동 작업 생성 패러다임을 검토하여 물리적 기반 및 시뮬레이션-실제 전환에서의 공통된 한계를 식별합니다. 이러한 분석을 종합하여 표현 정렬, 다중 모달 감독, 추론 평가, 확장 가능한 데이터 생성이라는 네 가지 공개 과제를 도출합니다. 이를 해결하기 위해서는 데이터 인프라를 배경 문제가 아닌 일급 연구 문제로 취급해야 한다고 주장합니다.

## 参考
- http://arxiv.org/abs/2604.23001v1
