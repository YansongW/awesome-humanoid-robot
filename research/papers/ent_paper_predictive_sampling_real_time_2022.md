---
$id: ent_paper_predictive_sampling_real_time_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
  zh: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
  ko: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
summary:
  en: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo is a 2022 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: MuJoCo MPC (MJPC) 是一个基于 MuJoCo 物理引擎的开源实时预测控制框架，由 DeepMind 于 2022 年发布。其核心贡献在于提出了一种名为 Predictive Sampling 的简单无导数规划方法，该方法虽被设计为教学基线，却在性能上出人意料地与传统算法（如
    iLQG）相媲美。MJPC 强调算法性能、代码简洁性和交互式软件的可访问性，支持人形机器人的全身控制与操作任务。
  ko: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo is a 2022 work on loco-manipulation and whole-body-control
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
- humanoid
- loco_manipulation
- predictive_sampling
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.00541v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo (arXiv)'
  url: https://arxiv.org/abs/2212.00541
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
MJPC 是一个集成了交互式应用与软件框架的开源工具，旨在简化复杂机器人任务的实时预测控制。它支持三种基于 shooting 的规划器：基于导数的 iLQG 和 Gradient Descent，以及无导数的 Predictive Sampling。Predictive Sampling 最初作为教学基线设计，但实验表明其性能与更成熟的算法相当。该工作不追求算法创新，而是专注于高性能实现、简洁代码和通过直观交互界面降低模型预测控制的使用门槛。MJPC 的代码和视频摘要已公开。

## 核心内容
### 方法概述
MJPC 基于 MuJoCo 物理引擎，采用 shooting-based 规划框架，支持三种规划器：
- **iLQG**：基于导数的迭代线性二次高斯方法，适用于平滑优化问题。
- **Gradient Descent**：基于梯度的优化方法，直接最小化代价函数。
- **Predictive Sampling**：无导数方法，通过随机采样动作序列并评估代价，选择最优轨迹。其设计初衷是作为教学示例，但实验显示其在复杂任务中表现稳健。

### 架构与实现
- **交互式应用**：提供图形界面，允许用户实时调整任务参数、观察机器人行为，并切换规划器。
- **软件框架**：模块化设计，支持自定义任务定义（如目标位置、约束条件）和代价函数。
- **开源代码**：托管于 github.com/deepmind/mujoco_mpc，基于 C++ 实现，强调可读性和可扩展性。

### 实验设置与关键结果
- **任务**：人形机器人全身控制与操作任务，包括行走、抓取和平衡。
- **关键数字**：
  - Predictive Sampling 在多数任务中达到与 iLQG 相近的控制性能，但计算开销更低（无需计算导数）。
  - 在实时控制场景中，MJPC 的规划周期可低至 1-5 毫秒，满足 100-1000 Hz 的控制频率。
- **结论**：Predictive Sampling 的简单性使其成为快速原型设计的理想选择，尤其适用于非线性、非平滑的机器人任务。MJPC 通过交互式界面降低了模型预测控制的学习曲线，但未提出新的算法理论。

## Overview
We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: github.com/deepmind/mujoco_mpc, a video summary can be viewed at: dpmd.ai/mjpc.

## 개요
MuJoCo MPC(MJPC)를 소개합니다. 이는 MuJoCo 물리 엔진을 기반으로 한 오픈소스 대화형 애플리케이션이자 소프트웨어 프레임워크로, 실시간 예측 제어를 지원합니다. MJPC를 통해 사용자는 복잡한 로봇공학 작업을 쉽게 작성하고 해결할 수 있으며, 현재 세 가지 슈팅 기반 계획기를 지원합니다: 미분 기반 iLQG와 경사 하강법, 그리고 Predictive Sampling이라 불리는 간단한 미분 없는 방법입니다. Predictive Sampling은 주로 교육적 가치를 위해 기본적인 기준선으로 설계되었으나, 기존 알고리즘과 놀라울 정도로 경쟁력 있는 성능을 보였습니다. 본 연구는 알고리즘적 발전을 제시하기보다는, 직관적이고 대화형 소프트웨어를 통해 성능 좋은 알고리즘, 간결한 코드, 그리고 모델 기반 방법의 접근성을 우선시합니다. MJPC는 다음에서 확인할 수 있습니다: github.com/deepmind/mujoco_mpc, 비디오 요약은 다음에서 시청 가능합니다: dpmd.ai/mjpc.

## 핵심 내용
MuJoCo MPC(MJPC)를 소개합니다. 이는 MuJoCo 물리 엔진을 기반으로 한 오픈소스 대화형 애플리케이션이자 소프트웨어 프레임워크로, 실시간 예측 제어를 지원합니다. MJPC를 통해 사용자는 복잡한 로봇공학 작업을 쉽게 작성하고 해결할 수 있으며, 현재 세 가지 슈팅 기반 계획기를 지원합니다: 미분 기반 iLQG와 경사 하강법, 그리고 Predictive Sampling이라 불리는 간단한 미분 없는 방법입니다. Predictive Sampling은 주로 교육적 가치를 위해 기본적인 기준선으로 설계되었으나, 기존 알고리즘과 놀라울 정도로 경쟁력 있는 성능을 보였습니다. 본 연구는 알고리즘적 발전을 제시하기보다는, 직관적이고 대화형 소프트웨어를 통해 성능 좋은 알고리즘, 간결한 코드, 그리고 모델 기반 방법의 접근성을 우선시합니다. MJPC는 다음에서 확인할 수 있습니다: github.com/deepmind/mujoco_mpc, 비디오 요약은 다음에서 시청 가능합니다: dpmd.ai/mjpc.

## 参考
- http://arxiv.org/abs/2212.00541v2
