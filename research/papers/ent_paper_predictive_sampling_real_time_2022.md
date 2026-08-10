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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.00541v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (946 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2212.00541v2

## 개요
MJPC는 대화형 애플리케이션과 소프트웨어 프레임워크를 통합한 오픈소스 도구로, 복잡한 로봇 작업의 실시간 예측 제어를 단순화하기 위해 설계되었습니다. 이는 shooting 기반의 세 가지 플래너를 지원합니다: 도함수 기반의 iLQG 및 Gradient Descent, 그리고 무도함수 기반의 Predictive Sampling입니다. Predictive Sampling은 처음에는 교육용 기준선으로 설계되었지만, 실험 결과 더 성숙된 알고리즘과 견줄 만한 성능을 보였습니다. 이 작업은 알고리즘 혁신을 추구하지 않고, 고성능 구현, 간결한 코드, 직관적인 상호작용 인터페이스를 통해 모델 예측 제어의 사용 장벽을 낮추는 데 집중합니다. MJPC의 코드와 비디오 요약은 공개되었습니다.

## 핵심 내용
### 방법 개요
MJPC는 MuJoCo 물리 엔진을 기반으로 하며, shooting 기반 계획 프레임워크를 채택하여 세 가지 플래너를 지원합니다:
- **iLQG**: 도함수 기반의 반복 선형 이차 가우시안 방법으로, 매끄러운 최적화 문제에 적합합니다.
- **Gradient Descent**: 기울기 기반 최적화 방법으로, 비용 함수를 직접 최소화합니다.
- **Predictive Sampling**: 무도함수 방법으로, 행동 시퀀스를 무작위로 샘플링하고 비용을 평가하여 최적 궤적을 선택합니다. 이는 처음에는 교육용 예시로 설계되었지만, 실험 결과 복잡한 작업에서 견고한 성능을 보였습니다.

### 아키텍처 및 구현
- **대화형 애플리케이션**: 그래픽 인터페이스를 제공하여 사용자가 작업 매개변수를 실시간으로 조정하고, 로봇 행동을 관찰하며, 플래너를 전환할 수 있습니다.
- **소프트웨어 프레임워크**: 모듈식 설계로, 사용자 정의 작업 정의(예: 목표 위치, 제약 조건)와 비용 함수를 지원합니다.
- **오픈소스 코드**: github.com/deepmind/mujoco_mpc에 호스팅되며, C++로 구현되어 가독성과 확장성을 강조합니다.

### 실험 설정 및 주요 결과
- **작업**: 휴머노이드 로봇의 전신 제어 및 조작 작업으로, 걷기, 잡기, 균형 유지가 포함됩니다.
- **주요 수치**:
  - Predictive Sampling은 대부분의 작업에서 iLQG와 유사한 제어 성능을 달성하지만, 계산 비용이 더 낮습니다(도함수 계산 불필요).
  - 실시간 제어 시나리오에서 MJPC의 계획 주기는 1-5밀리초까지 낮출 수 있어, 100-1000Hz의 제어 주파수를 충족합니다.
- **결론**: Predictive Sampling의 단순성은 빠른 프로토타입 설계에 이상적인 선택이 되며, 특히 비선형적이고 비매끄러운 로봇 작업에 적합합니다. MJPC는 대화형 인터페이스를 통해 모델 예측 제어의 학습 곡선을 낮추지만, 새로운 알고리즘 이론을 제시하지는 않습니다.
