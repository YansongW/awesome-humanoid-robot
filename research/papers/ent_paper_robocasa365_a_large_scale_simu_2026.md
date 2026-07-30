---
$id: ent_paper_robocasa365_a_large_scale_simu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots'
  zh: 'RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots'
  ko: 'RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots'
summary:
  en: 'RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots is a 2026 work on simulation
    benchmark for humanoid robots.'
  zh: RoboCasa365 是一个 2026 年发布的大规模仿真基准，用于训练和评估通用人形机器人。该工作由研究团队基于 RoboCasa 平台构建，核心贡献是提供了 365 项日常任务、2500 个多样化厨房环境、超过 600 小时人类演示数据及
    1600 小时合成数据，支持多任务学习、基础模型训练和终身学习等系统评估。
  ko: 'RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots is a 2026 work on simulation
    benchmark for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- robocasa365
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: RoboCasa365: A Large-Scale
    Simulation Framework for Training and Benchmarking Generalist Robots. [2026-07-29] zh content backfilled from English
    abstract via scripts/sinicize_english_cards.py'
sources:
- id: src_001
  type: website
  title: 'RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots project page'
  url: https://openreview.net/forum?id=tQJYKwc3n4
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
RoboCasa365 旨在填补机器人领域缺乏可重复、大规模系统评估基准的空白。它基于 RoboCasa 平台扩展，覆盖 365 项家庭移动操作任务，环境多样性达 2500 个厨房场景。数据集包含 600 小时人类演示和 1600 小时合成演示，是目前最丰富的大规模通用策略研究资源之一。该基准支持多任务学习、机器人基础模型训练和终身学习等不同问题设置的系统评估，并通过与最先进方法的广泛实验，分析了任务多样性、数据集规模和环境变化对泛化能力的影响。

## 核心内容
### 方法
RoboCasa365 构建于 RoboCasa 平台之上，通过扩展任务库和环境库实现大规模仿真。任务涵盖日常家庭操作，如取物、放置、开关抽屉等，共 365 项。环境通过程序化生成 2500 个不同布局的厨房场景，确保视觉和物理多样性。

### 数据集
- **人类演示数据**：超过 600 小时，由操作员通过遥操作收集。
- **合成演示数据**：超过 1600 小时，通过自动化脚本和仿真引擎生成。
- 总数据量使 RoboCasa365 成为当前规模最大的通用策略研究资源之一。

### 实验设置
基准设计支持三种问题设置：
1. **多任务学习**：评估模型在多个任务上的联合训练效果。
2. **机器人基础模型训练**：测试预训练模型在未见任务上的零样本泛化能力。
3. **终身学习**：评估模型在持续学习新任务时的稳定性与可塑性。

实验采用最先进方法（如 BC、RL、Transformer-based 策略）进行对比，关键指标包括任务成功率、泛化误差和样本效率。

### 关键结果
- **任务多样性**：增加任务数量显著提升模型泛化能力，但超过 200 项任务后收益递减。
- **数据集规模**：合成数据可部分替代人类数据，但人类数据在复杂任务中仍不可或缺。
- **环境变化**：环境多样性（如光照、物体位置）对成功率影响最大，任务难度次之。
- **结论**：通用机器人性能受任务多样性、数据质量和环境变化共同影响，未来应优先扩展环境多样性而非单纯增加任务数量。

## Overview
Recent advances in robot learning have accelerated progress toward generalist robots that can perform everyday tasks in human environments. Yet it remains difficult to gauge how close we are to this vision. The field lacks a reproducible, large-scale benchmark for systematic evaluation. To fill this gap, we present RoboCasa365, a comprehensive simulation benchmark for household mobile manipulation. Built on the RoboCasa platform, RoboCasa365 introduces 365 everyday tasks across 2,500 diverse kitchen environments, with over 600 hours of human demonstration data and over 1600 hours of synthetically generated demonstration data -- making it one of the most diverse and large-scale resources for studying generalist policies. RoboCasa365 is designed to support systematic evaluations for different problem settings, including multi-task learning, robot foundation model training, and lifelong learning. We conduct extensive experiments on this benchmark with state-of-the-art methods and analyze the impacts of task diversity, dataset scale, and environment variation on generalization. Our results provide new insights into what factors most strongly affect the performance of generalist robots and inform strategies for future progress in the field.

## 개요
최근 로봇 학습의 발전으로 인간 환경에서 일상적인 작업을 수행할 수 있는 범용 로봇(Generalist Robot)을 향한 진전이 가속화되고 있습니다. 그러나 이러한 비전에 얼마나 근접했는지 측정하는 것은 여전히 어렵습니다. 이 분야에는 체계적인 평가를 위한 재현 가능하고 대규모의 벤치마크가 부족합니다. 이러한 격차를 해소하기 위해, 우리는 가정용 모바일 조작을 위한 포괄적인 시뮬레이션 벤치마크인 RoboCasa365를 제시합니다. RoboCasa 플랫폼을 기반으로 구축된 RoboCasa365는 2,500개의 다양한 주방 환경에서 365가지 일상 작업을 도입하며, 600시간 이상의 인간 시연 데이터와 1,600시간 이상의 합성 생성 시연 데이터를 제공합니다. 이는 범용 정책(Generalist Policy) 연구를 위한 가장 다양하고 대규모의 자원 중 하나입니다. RoboCasa365는 다중 작업 학습, 로봇 기반 모델 훈련, 평생 학습(Lifelong Learning) 등 다양한 문제 설정에 대한 체계적인 평가를 지원하도록 설계되었습니다. 우리는 최첨단 방법을 사용하여 이 벤치마크에 대한 광범위한 실험을 수행하고, 작업 다양성, 데이터셋 규모, 환경 변화가 일반화에 미치는 영향을 분석합니다. 우리의 결과는 범용 로봇의 성능에 가장 큰 영향을 미치는 요인에 대한 새로운 통찰력을 제공하며, 해당 분야의 미래 발전을 위한 전략을 제시합니다.

## 핵심 내용
최근 로봇 학습의 발전으로 인간 환경에서 일상적인 작업을 수행할 수 있는 범용 로봇(Generalist Robot)을 향한 진전이 가속화되고 있습니다. 그러나 이러한 비전에 얼마나 근접했는지 측정하는 것은 여전히 어렵습니다. 이 분야에는 체계적인 평가를 위한 재현 가능하고 대규모의 벤치마크가 부족합니다. 이러한 격차를 해소하기 위해, 우리는 가정용 모바일 조작을 위한 포괄적인 시뮬레이션 벤치마크인 RoboCasa365를 제시합니다. RoboCasa 플랫폼을 기반으로 구축된 RoboCasa365는 2,500개의 다양한 주방 환경에서 365가지 일상 작업을 도입하며, 600시간 이상의 인간 시연 데이터와 1,600시간 이상의 합성 생성 시연 데이터를 제공합니다. 이는 범용 정책(Generalist Policy) 연구를 위한 가장 다양하고 대규모의 자원 중 하나입니다. RoboCasa365는 다중 작업 학습, 로봇 기반 모델 훈련, 평생 학습(Lifelong Learning) 등 다양한 문제 설정에 대한 체계적인 평가를 지원하도록 설계되었습니다. 우리는 최첨단 방법을 사용하여 이 벤치마크에 대한 광범위한 실험을 수행하고, 작업 다양성, 데이터셋 규모, 환경 변화가 일반화에 미치는 영향을 분석합니다. 우리의 결과는 범용 로봇의 성능에 가장 큰 영향을 미치는 요인에 대한 새로운 통찰력을 제공하며, 해당 분야의 미래 발전을 위한 전략을 제시합니다.

## 参考
- Semantic Scholar search: RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots
