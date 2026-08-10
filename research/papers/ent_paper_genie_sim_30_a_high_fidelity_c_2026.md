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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.02078v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP1 dedup merge 2026-08-06: merged
    ent_paper_genie_sim_30_a_high_fidelity_c_2026 into this card (rules: suffix_reingest). Backup+manifest: .staging/cleanup_wp12/.
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (824 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot (arXiv)'
  url: https://arxiv.org/abs/2601.02078
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Genie Sim 3.0: A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot'
  url: ''
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

## 参考
- http://arxiv.org/abs/2601.02078v3

## 개요
Genie Sim 3.0은 로봇 학습 분야에서 데이터 수집 비용이 높고, 시뮬레이션 벤치마크가 파편화되어 있으며, 충실도가 부족한 등의 핵심 문제를 해결하는 것을 목표로 합니다. 이 플랫폼은 Genie Sim Generator 도구를 통해 대규모 언어 모델(LLM)을 활용하여 자연어 지시를 고충실도 장면으로 변환하고, 빠른 다차원 일반화를 지원하여 다양한 환경 합성을 촉진합니다. 또한, 플랫폼은 처음으로 LLM 기반 자동 평가 벤치마크를 도입하고, 비전-언어 모델(VLM)을 결합하여 평가 파이프라인을 구축합니다. 연구팀은 또한 200개 이상의 작업을 포괄하는 10,000시간 이상의 합성 데이터셋을 오픈소스로 공개했으며, 체계적인 실험을 통해 제로샷 sim-to-real 전이에서의 견고성을 검증했습니다.

## 핵심 내용
### 핵심 아키텍처 및 방법
- **Genie Sim Generator**: 자연어 지시에서 고충실도 장면을 자동으로 구축할 수 있는 대규모 언어 모델(LLM) 기반 도구입니다. 핵심 장점은 빠른 다차원 일반화를 구현하고 다양한 환경 합성을 지원하여 확장 가능한 데이터 수집과 견고한 정책 평가의 기반을 제공한다는 점입니다.
- **자동 평가 벤치마크**: 처음으로 LLM을 자동 평가에 적용하여, LLM이 평가 장면을 대량 생성하고, 비전-언어 모델(VLM)을 활용하여 자동 평가 파이프라인을 구축함으로써 기존의 수동 평가가 비효율적이고 적용 범위가 제한적이던 문제를 해결합니다.

### 데이터셋 및 실험 설정
- **오픈소스 데이터셋**: 200개 이상의 작업을 포괄하는 10,000시간 이상의 합성 데이터를 포함합니다. 데이터는 Genie Sim Generator를 통해 생성되며, 정책 훈련을 위한 대규모의 다양한 훈련 샘플을 제공하는 것을 목표로 합니다.
- **실험 검증**: 체계적인 실험을 통해 제로샷 sim-to-real 전이 능력을 평가합니다. 결과는 통제된 조건에서 합성 데이터가 실제 데이터를 효과적으로 대체할 수 있고, 확장 가능한 정책 훈련을 지원하며, 플랫폼의 실용성과 충실도를 검증함을 보여줍니다.

### 결론 및 리소스
- Genie Sim 3.0은 통합 시뮬레이션 플랫폼, LLM 기반 장면 생성 및 평가, 그리고 대규모 오픈소스 데이터셋을 통해 로봇 조작 작업을 위한 고충실도, 확장 가능한 솔루션을 제공합니다.
- 코드와 데이터셋은 오픈소스로 공개되었으며, 접속 주소: https://github.com/AgibotTech/genie_sim.
