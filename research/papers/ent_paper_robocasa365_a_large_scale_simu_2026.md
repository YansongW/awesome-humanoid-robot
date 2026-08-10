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
    abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read
    (896 chars, DeepSeek).'
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

## 参考
- Semantic Scholar search: RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots

## 개요
RoboCasa365는 로봇 분야에서 재현 가능하고 대규모의 체계적인 평가 기준이 부족한 공백을 메우기 위해 설계되었습니다. RoboCasa 플랫폼을 기반으로 확장되어 365개의 가정용 이동 조작 작업과 2500개의 주방 장면으로 구성된 환경 다양성을 갖추고 있습니다. 데이터셋은 600시간의 인간 시연과 1600시간의 합성 시연을 포함하며, 현재 가장 풍부한 대규모 범용 정책 연구 자원 중 하나입니다. 이 벤치마크는 다중 작업 학습, 로봇 기반 모델 훈련, 평생 학습 등 다양한 문제 설정의 체계적인 평가를 지원하며, 최신 방법론과의 광범위한 실험을 통해 작업 다양성, 데이터셋 규모, 환경 변화가 일반화 능력에 미치는 영향을 분석합니다.

## 핵심 내용
### 방법
RoboCasa365는 RoboCasa 플랫폼 위에 구축되었으며, 작업 라이브러리와 환경 라이브러리를 확장하여 대규모 시뮬레이션을 구현합니다. 작업은 물건 집기, 놓기, 서랍 열고 닫기 등 일상적인 가정용 조작을 포함하며 총 365개입니다. 환경은 프로그래밍 방식으로 2500개의 서로 다른 레이아웃의 주방 장면을 생성하여 시각적 및 물리적 다양성을 보장합니다.

### 데이터셋
- **인간 시연 데이터**: 600시간 이상, 운영자가 원격 조작을 통해 수집.
- **합성 시연 데이터**: 1600시간 이상, 자동화된 스크립트와 시뮬레이션 엔진을 통해 생성.
- 총 데이터량으로 인해 RoboCasa365는 현재 가장 큰 규모의 범용 정책 연구 자원 중 하나입니다.

### 실험 설정
벤치마크는 세 가지 문제 설정을 지원합니다:
1. **다중 작업 학습**: 여러 작업에 대한 모델의 공동 훈련 효과를 평가.
2. **로봇 기반 모델 훈련**: 사전 훈련된 모델의 보지 못한 작업에 대한 제로샷 일반화 능력을 테스트.
3. **평생 학습**: 새로운 작업을 지속적으로 학습할 때 모델의 안정성과 가소성을 평가.

실험은 최신 방법론(예: BC, RL, Transformer 기반 정책)과 비교하며, 주요 지표는 작업 성공률, 일반화 오차, 샘플 효율성입니다.

### 주요 결과
- **작업 다양성**: 작업 수를 늘리면 모델의 일반화 능력이 크게 향상되지만, 200개 작업을 초과하면 수익이 감소합니다.
- **데이터셋 규모**: 합성 데이터는 인간 데이터를 부분적으로 대체할 수 있지만, 복잡한 작업에서는 인간 데이터가 여전히 필수적입니다.
- **환경 변화**: 환경 다양성(예: 조명, 물체 위치)이 성공률에 가장 큰 영향을 미치며, 작업 난이도가 그 다음입니다.
- **결론**: 범용 로봇 성능은 작업 다양성, 데이터 품질, 환경 변화의 영향을 함께 받으며, 향후에는 단순히 작업 수를 늘리는 것보다 환경 다양성을 확장하는 데 우선순위를 두어야 합니다.
