---
$id: ent_tech_robogen
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: technology
names:
  en: RoboGen
  zh: RoboGen
  ko: RoboGen
summary:
  en: An LLM-driven automatic task-generation framework for robotics that proposes tasks and generates simulation code to
    expand synthetic training data diversity.
  zh: 一种由大语言模型驱动的机器人自动任务生成框架，提出任务并生成仿真代码以扩展合成训练数据的多样性。
  ko: 작업을 제안하고 시뮬레이션 코드를 생성하여 합성 학습 데이터 다양성을 확장하는 LLM 기반 로봇 자동 작업 생성 프레임워크.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
layers:
- intelligence
functional_roles:
- intelligence
- tool_equipment
tags:
- data_engine
- llm
- automatic_task_generation
- simulation
- synthetic_data
- vla
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: high
  notes: Scope confirmed by original NeurIPS 2023 paper and Wang et al. 2026 VLA survey. Body backfilled from entity metadata
    by scripts/backfill_critical_entities.py.
sources:
- id: src_robogen_paper
  type: paper
  title: 'RoboGen: Towards Universal Humanoid Control via Diffusion Transformer'
  url: https://arxiv.org/abs/2311.01455
  date: '2023-11-02'
  accessed_at: '2026-06-22'
- id: src_robogen_code
  type: website
  title: RoboGen Project Page
  url: https://robogen-ai.github.io/
  date: '2023-11-02'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_paper_wang_vla_survey_2026
  relationship: cites
  description:
    en: Wang et al. 2026 survey discusses RoboGen as an LLM-driven automatic task-generation framework for simulation.
    zh: Wang 等人 2026 综述将 RoboGen 作为由 LLM 驱动的仿真自动任务生成框架进行讨论。
    ko: Wang et al. 2026 서베이는 RoboGen을 LLM 기반 시뮬레이션 자동 작업 생성 프레임워크로 논의함.
theoretical_depth:
- method
---
## 概述
一种由大语言模型驱动的机器人自动任务生成框架，提出任务并生成仿真代码以扩展合成训练数据的多样性。

## 核心内容
### RoboGen的定义与定位
RoboGen属于 **technology** 类型。 所属领域包括：07_ai_models_algorithms, 08_software_middleware, 09_data_datasets。 价值链层级：intelligence。 一种由大语言模型驱动的机器人自动任务生成框架，提出任务并生成仿真代码以扩展合成训练数据的多样性。 英文名称为 *RoboGen*。 韩文名称为 *RoboGen*。

### RoboGen的工作原理与技术架构
RoboGen的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用RoboGen需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
RoboGen已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- data_engine
- llm
- automatic_task_generation
- simulation
- synthetic_data
- vla

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键technology之一，RoboGen在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [RoboGen: Towards Universal Humanoid Control via Diffusion Transformer](https://arxiv.org/abs/2311.01455)
- [RoboGen Project Page](https://robogen-ai.github.io/)

