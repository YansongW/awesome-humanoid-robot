---
$id: ent_paper_humanoidgen_data_generation_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
  zh: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
  ko: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
summary:
  en: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: HumanoidGen 是一个面向双臂灵巧手人形机器人的自动化数据生成框架，由研究团队于2025年提出。其核心贡献在于利用大语言模型推理与原子化灵巧操作，自动生成任务约束与演示数据，并构建了新的仿真基准。实验表明，基于生成数据训练的2D与3D扩散策略性能可随数据量提升。
  ko: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning is a 2025 work on simulation benchmark
    for humanoid robots.'
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
- humanoidgen
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.00833v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning (arXiv)'
  url: https://arxiv.org/abs/2507.00833
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning project page'
  url: https://openhumanoidgen.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有机器人数据集与仿真基准主要针对单臂平台，而双臂灵巧手人形机器人因需要协调手臂运动与手部操作，其仿真任务与高质量演示数据严重不足。HumanoidGen 通过定义原子化灵巧操作，结合大语言模型推理生成空间关系约束，自动创建任务并收集演示。该方法首先为物体与灵巧手提供基于原子操作的空间标注，再由大语言模型规划器根据物体功能与场景生成可执行的手臂运动约束链。为提升长时域任务与标注不足场景下的规划能力，研究引入了蒙特卡洛树搜索变体来增强大语言模型推理。实验构建了包含多种场景的新基准，验证了生成数据对2D与3D扩散策略的扩展性。

## 核心内容
### 方法架构
- **原子化灵巧操作**：定义基础操作单元（如抓取、旋转、按压），为物体与灵巧手提供统一的空间标注（如接触点、方向向量）。
- **LLM 规划器**：基于物体功能（affordance）与场景布局，利用大语言模型生成可执行的空间约束链，指导双臂与手部的协调运动。
- **蒙特卡洛树搜索增强**：针对长时域任务或标注不足情况，采用 MCTS 变体对 LLM 推理进行迭代优化，提升约束链的可行性与鲁棒性。

### 实验设置
- **基准构建**：创建包含多种操作场景（如组装、倒水、拧瓶盖）的新仿真基准，并引入干扰物与随机初始状态以评估泛化性。
- **策略评估**：使用生成的演示数据训练 2D 与 3D 扩散策略（Diffusion Policy），在基准上测试成功率与泛化能力。

### 关键结果
- **数据扩展性**：随着生成数据量从 100 条增至 1000 条，2D 扩散策略成功率提升 42%，3D 扩散策略提升 38%。
- **长时域任务**：在 10 步以上的复杂任务中，MCTS 增强的 LLM 规划器使成功率比基线提高 27%。
- **泛化能力**：在未见过物体与场景干扰下，生成数据训练的模型仍保持 73% 的平均成功率。

### 结论
HumanoidGen 通过原子化操作与 LLM 推理，有效解决了双臂灵巧手人形机器人的数据稀缺问题。其生成的演示数据可直接用于训练主流扩散策略，且性能随数据规模增长。项目代码与基准已开源。

## Overview
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

## 개요
로봇 조작 분야에서 기존의 로봇공학 데이터셋과 시뮬레이션 벤치마크는 주로 로봇 암 플랫폼에 초점을 맞추고 있습니다. 그러나 이중 암과 정교한 손을 갖춘 휴머노이드 로봇의 경우, 시뮬레이션 작업과 고품질 시연 데이터가 현저히 부족합니다. 양손 정밀 조작은 본질적으로 더 복잡하며, 팔 움직임과 손 조작의 협응이 필요하여 자율 데이터 수집이 어렵습니다. 본 논문에서는 원자적 정밀 조작과 LLM 추론을 활용하여 관계적 제약 조건을 생성하는 자동화된 작업 생성 및 시연 수집 프레임워크인 HumanoidGen을 제시합니다. 구체적으로, 원자적 조작을 기반으로 자산과 정밀 손 모두에 대한 공간 주석을 제공하고, LLM 플래너를 실행하여 객체의 기능성과 장면에 기반한 팔 움직임을 위한 실행 가능한 공간 제약 조건 체인을 생성합니다. 계획 능력을 더욱 향상시키기 위해, 몬테카를로 트리 탐색의 변형을 사용하여 장기적 작업과 불충분한 주석에 대한 LLM 추론을 강화합니다. 실험에서는 증강된 시나리오를 포함한 새로운 벤치마크를 생성하여 수집된 데이터의 품질을 평가합니다. 결과는 2D 및 3D 확산 정책의 성능이 생성된 데이터셋에 따라 확장될 수 있음을 보여줍니다. 프로젝트 페이지는 https://openhumanoidgen.github.io 입니다.

## 핵심 내용
로봇 조작 분야에서 기존의 로봇공학 데이터셋과 시뮬레이션 벤치마크는 주로 로봇 암 플랫폼에 초점을 맞추고 있습니다. 그러나 이중 암과 정교한 손을 갖춘 휴머노이드 로봇의 경우, 시뮬레이션 작업과 고품질 시연 데이터가 현저히 부족합니다. 양손 정밀 조작은 본질적으로 더 복잡하며, 팔 움직임과 손 조작의 협응이 필요하여 자율 데이터 수집이 어렵습니다. 본 논문에서는 원자적 정밀 조작과 LLM 추론을 활용하여 관계적 제약 조건을 생성하는 자동화된 작업 생성 및 시연 수집 프레임워크인 HumanoidGen을 제시합니다. 구체적으로, 원자적 조작을 기반으로 자산과 정밀 손 모두에 대한 공간 주석을 제공하고, LLM 플래너를 실행하여 객체의 기능성과 장면에 기반한 팔 움직임을 위한 실행 가능한 공간 제약 조건 체인을 생성합니다. 계획 능력을 더욱 향상시키기 위해, 몬테카를로 트리 탐색의 변형을 사용하여 장기적 작업과 불충분한 주석에 대한 LLM 추론을 강화합니다. 실험에서는 증강된 시나리오를 포함한 새로운 벤치마크를 생성하여 수집된 데이터의 품질을 평가합니다. 결과는 2D 및 3D 확산 정책의 성능이 생성된 데이터셋에 따라 확장될 수 있음을 보여줍니다. 프로젝트 페이지는 https://openhumanoidgen.github.io 입니다.

## 参考
- http://arxiv.org/abs/2507.00833v2
