---
$id: ent_paper_genie_sim_30_a_high_fidelity_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot'
  zh: 'Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot'
  ko: 'Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot'
summary:
  en: 'Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot is a 2026 work on manipulation
    for humanoid robots.'
  zh: Genie Sim 3.0 是 AgibotTech 于 2026 年提出的面向人形机器人的高保真综合仿真平台。其核心贡献包括：基于 LLM 的 Genie Sim Generator 实现自然语言驱动的场景生成、首个利用 LLM
    进行自动化评估的基准，以及包含超过 200 个任务、10,000 小时合成数据的开源数据集。实验验证了该平台在零样本 sim-to-real 迁移中的有效性，表明合成数据可在受控条件下替代真实数据用于可扩展策略训练。
  ko: 'Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot is a 2026 work on manipulation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- genie_sim_30
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.02078v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot (arXiv)'
  url: https://arxiv.org/abs/2601.02078
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Genie Sim 3.0 旨在解决机器人学习领域数据采集成本高、仿真基准碎片化及保真度不足等关键问题。该平台通过 Genie Sim Generator 工具，利用大语言模型将自然语言指令转化为高保真场景，支持快速多维度的泛化，从而促进多样化环境的合成。平台还首次引入基于 LLM 的自动化评估基准，结合视觉语言模型构建评估流水线。此外，研究团队开源了超过 10,000 小时的合成数据集，覆盖 200 余项任务，并通过系统实验验证了其在零样本 sim-to-real 迁移中的鲁棒性。

## 核心内容
### 核心架构与方法
- **Genie Sim Generator**：基于大语言模型（LLM）的工具，能够从自然语言指令自动构建高保真场景。其核心优势在于快速实现多维度泛化，支持合成多样化环境，从而为可扩展数据收集和鲁棒策略评估提供基础。
- **自动化评估基准**：首次将 LLM 应用于自动化评估，通过 LLM 批量生成评估场景，并利用视觉语言模型（VLM）构建自动化评估流水线，解决了传统人工评估效率低、覆盖范围有限的问题。

### 数据集与实验设置
- **开源数据集**：包含超过 10,000 小时的合成数据，覆盖 200 余项任务。数据通过 Genie Sim Generator 生成，旨在为策略训练提供大规模、多样化的训练样本。
- **实验验证**：通过系统实验评估零样本 sim-to-real 迁移能力。结果表明，在受控条件下，合成数据可有效替代真实数据，支持可扩展的策略训练，验证了平台的实用性与保真度。

### 结论与资源
- Genie Sim 3.0 通过统一仿真平台、LLM 驱动的场景生成与评估、以及大规模开源数据集，为机器人操作任务提供了高保真、可扩展的解决方案。
- 代码与数据集已开源，访问地址：https://github.com/AgibotTech/genie_sim。

## Overview
The development of robust and generalizable robot learning models is critically contingent upon the availability of large-scale, diverse training data and reliable evaluation benchmarks. Collecting data in the physical world poses prohibitive costs and scalability challenges, and prevailing simulation benchmarks frequently suffer from fragmentation, narrow scope, or insufficient fidelity to enable effective sim-to-real transfer. To address these challenges, we introduce Genie Sim 3.0, a unified simulation platform for robotic manipulation. We present Genie Sim Generator, a large language model (LLM)-powered tool that constructs high-fidelity scenes from natural language instructions. Its principal strength resides in rapid and multi-dimensional generalization, facilitating the synthesis of diverse environments to support scalable data collection and robust policy evaluation. We introduce the first benchmark that pioneers the application of LLM for automated evaluation. It leverages LLM to mass-generate evaluation scenarios and employs Vision-Language Model (VLM) to establish an automated assessment pipeline. We also release an open-source dataset comprising more than 10,000 hours of synthetic data across over 200 tasks. Through systematic experimentation, we validate the robust zero-shot sim-to-real transfer capability of our open-source dataset, demonstrating that synthetic data can server as an effective substitute for real-world data under controlled conditions for scalable policy training. For code and dataset details, please refer to: https://github.com/AgibotTech/genie_sim.

## Overview
The development of robust and generalizable robot learning models is critically contingent upon the availability of large-scale, diverse training data and reliable evaluation benchmarks. Collecting data in the physical world poses prohibitive costs and scalability challenges, and prevailing simulation benchmarks frequently suffer from fragmentation, narrow scope, or insufficient fidelity to enable effective sim-to-real transfer. To address these challenges, we introduce Genie Sim 3.0, a unified simulation platform for robotic manipulation. We present Genie Sim Generator, a large language model (LLM)-powered tool that constructs high-fidelity scenes from natural language instructions. Its principal strength resides in rapid and multi-dimensional generalization, facilitating the synthesis of diverse environments to support scalable data collection and robust policy evaluation. We introduce the first benchmark that pioneers the application of LLM for automated evaluation. It leverages LLM to mass-generate evaluation scenarios and employs Vision-Language Model (VLM) to establish an automated assessment pipeline. We also release an open-source dataset comprising more than 10,000 hours of synthetic data across over 200 tasks. Through systematic experimentation, we validate the robust zero-shot sim-to-real transfer capability of our open-source dataset, demonstrating that synthetic data can serve as an effective substitute for real-world data under controlled conditions for scalable policy training. For code and dataset details, please refer to: https://github.com/AgibotTech/genie_sim.

## Content
The development of robust and generalizable robot learning models is critically contingent upon the availability of large-scale, diverse training data and reliable evaluation benchmarks. Collecting data in the physical world poses prohibitive costs and scalability challenges, and prevailing simulation benchmarks frequently suffer from fragmentation, narrow scope, or insufficient fidelity to enable effective sim-to-real transfer. To address these challenges, we introduce Genie Sim 3.0, a unified simulation platform for robotic manipulation. We present Genie Sim Generator, a large language model (LLM)-powered tool that constructs high-fidelity scenes from natural language instructions. Its principal strength resides in rapid and multi-dimensional generalization, facilitating the synthesis of diverse environments to support scalable data collection and robust policy evaluation. We introduce the first benchmark that pioneers the application of LLM for automated evaluation. It leverages LLM to mass-generate evaluation scenarios and employs Vision-Language Model (VLM) to establish an automated assessment pipeline. We also release an open-source dataset comprising more than 10,000 hours of synthetic data across over 200 tasks. Through systematic experimentation, we validate the robust zero-shot sim-to-real transfer capability of our open-source dataset, demonstrating that synthetic data can serve as an effective substitute for real-world data under controlled conditions for scalable policy training. For code and dataset details, please refer to: https://github.com/AgibotTech/genie_sim.

## 개요
강건하고 일반화 가능한 로봇 학습 모델의 개발은 대규모의 다양한 훈련 데이터와 신뢰할 수 있는 평가 벤치마크의 가용성에 결정적으로 의존합니다. 물리적 세계에서 데이터를 수집하는 것은 엄청난 비용과 확장성 문제를 야기하며, 기존의 시뮬레이션 벤치마크는 종종 단편화, 좁은 범위, 또는 효과적인 시뮬레이션-실제 전환을 가능하게 할 충분한 충실도 부족으로 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 로봇 조작을 위한 통합 시뮬레이션 플랫폼인 Genie Sim 3.0을 소개합니다. 우리는 자연어 명령어로부터 고충실도 장면을 구축하는 대규모 언어 모델(LLM) 기반 도구인 Genie Sim Generator를 제시합니다. 그 주요 강점은 빠르고 다차원적인 일반화에 있으며, 확장 가능한 데이터 수집과 강건한 정책 평가를 지원하기 위해 다양한 환경을 합성하는 것을 용이하게 합니다. 우리는 LLM을 자동 평가에 적용한 최초의 벤치마크를 소개합니다. 이는 LLM을 활용하여 평가 시나리오를 대량 생성하고, 비전-언어 모델(VLM)을 사용하여 자동 평가 파이프라인을 구축합니다. 또한 200개 이상의 작업에 걸쳐 10,000시간 이상의 합성 데이터를 포함하는 오픈소스 데이터셋을 공개합니다. 체계적인 실험을 통해, 우리는 오픈소스 데이터셋의 강건한 제로샷 시뮬레이션-실제 전환 능력을 검증하며, 합성 데이터가 통제된 조건에서 확장 가능한 정책 훈련을 위한 실제 데이터의 효과적인 대체재 역할을 할 수 있음을 보여줍니다. 코드 및 데이터셋에 대한 자세한 내용은 다음을 참조하십시오: https://github.com/AgibotTech/genie_sim.

## 핵심 내용
강건하고 일반화 가능한 로봇 학습 모델의 개발은 대규모의 다양한 훈련 데이터와 신뢰할 수 있는 평가 벤치마크의 가용성에 결정적으로 의존합니다. 물리적 세계에서 데이터를 수집하는 것은 엄청난 비용과 확장성 문제를 야기하며, 기존의 시뮬레이션 벤치마크는 종종 단편화, 좁은 범위, 또는 효과적인 시뮬레이션-실제 전환을 가능하게 할 충분한 충실도 부족으로 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 로봇 조작을 위한 통합 시뮬레이션 플랫폼인 Genie Sim 3.0을 소개합니다. 우리는 자연어 명령어로부터 고충실도 장면을 구축하는 대규모 언어 모델(LLM) 기반 도구인 Genie Sim Generator를 제시합니다. 그 주요 강점은 빠르고 다차원적인 일반화에 있으며, 확장 가능한 데이터 수집과 강건한 정책 평가를 지원하기 위해 다양한 환경을 합성하는 것을 용이하게 합니다. 우리는 LLM을 자동 평가에 적용한 최초의 벤치마크를 소개합니다. 이는 LLM을 활용하여 평가 시나리오를 대량 생성하고, 비전-언어 모델(VLM)을 사용하여 자동 평가 파이프라인을 구축합니다. 또한 200개 이상의 작업에 걸쳐 10,000시간 이상의 합성 데이터를 포함하는 오픈소스 데이터셋을 공개합니다. 체계적인 실험을 통해, 우리는 오픈소스 데이터셋의 강건한 제로샷 시뮬레이션-실제 전환 능력을 검증하며, 합성 데이터가 통제된 조건에서 확장 가능한 정책 훈련을 위한 실제 데이터의 효과적인 대체재 역할을 할 수 있음을 보여줍니다. 코드 및 데이터셋에 대한 자세한 내용은 다음을 참조하십시오: https://github.com/AgibotTech/genie_sim.

## 参考
- http://arxiv.org/abs/2601.02078v3
