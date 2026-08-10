---
$id: ent_paper_armada_augmented_reality_for_r_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition'
  zh: 'ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition'
  ko: 'ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition'
summary:
  en: 'ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition is a 2024 work on manipulation for
    humanoid robots.'
  zh: ARMADA 是 2024 年提出的一种增强现实系统，通过 Apple Vision Pro 提供实时虚拟机器人反馈，让用户无需物理机器人即可收集高质量的操作数据。该系统在 15 名参与者的用户研究中验证了三种任务下的数据质量，并成功在真实机器人上复现轨迹，为可扩展的机器人学习数据采集开辟了新途径。
  ko: 'ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition is a 2024 work on manipulation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- armada
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.10631v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (669 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition (arXiv)'
  url: https://arxiv.org/abs/2412.10631
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition project page'
  url: https://nataliya.dev/armada
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
ARMADA 的核心创新在于利用增强现实技术，在 Apple Vision Pro 上叠加虚拟机器人模型，实时映射用户的手部动作到机器人运动。这使得操作者能够直观理解自身动作与机器人约束的对应关系，从而在无物理机器人环境下采集自然、兼容的裸手操作数据。研究通过 15 名参与者完成三种任务，对比三种反馈条件，证明实时虚拟反馈显著提升了数据质量，最终轨迹可直接在真实机器人上执行。

## 核心内容
### 方法
- **系统架构**：基于 Apple Vision Pro 构建增强现实环境，实时渲染虚拟机器人模型，并同步映射用户裸手动作到机器人关节空间。
- **数据采集**：用户通过视觉反馈理解动作与机器人运动的关系，采集自然手势数据，避免物理机器人硬件限制。

### 实验设置
- **参与者**：15 名用户，每人完成 3 种不同任务（如抓取、放置、组装）。
- **反馈条件**：每种任务在 3 种条件下执行——无反馈、静态反馈、实时虚拟机器人反馈。
- **验证**：采集的轨迹直接回放到真实物理机器人硬件上，评估执行成功率与精度。

### 关键结果
- 实时虚拟机器人反馈显著提升了数据质量，轨迹在真实机器人上的成功率远高于无反馈或静态反馈条件。
- 用户无需接触物理机器人即可生成兼容硬件约束的操作数据，为大规模数据采集提供了可扩展方案。

### 结论
ARMADA 证明了增强现实在机器人学习数据采集中的潜力，通过消除对物理机器人的依赖，降低了数据获取门槛。未来可进一步优化反馈延迟与多任务泛化能力。

## Overview
Teleoperation for robot imitation learning is bottlenecked by hardware availability. Can high-quality robot data be collected without a physical robot? We present a system for augmenting Apple Vision Pro with real-time virtual robot feedback. By providing users with an intuitive understanding of how their actions translate to robot motions, we enable the collection of natural barehanded human data that is compatible with the limitations of physical robot hardware. We conducted a user study with 15 participants demonstrating 3 different tasks each under 3 different feedback conditions and directly replayed the collected trajectories on physical robot hardware. Results suggest live robot feedback dramatically improves the quality of the collected data, suggesting a new avenue for scalable human data collection without access to robot hardware. Videos and more are available at https://nataliya.dev/armada.

## 参考
- http://arxiv.org/abs/2412.10631v1

## 개요
ARMADA의 핵심 혁신은 증강 현실 기술을 활용하여 Apple Vision Pro 위에 가상 로봇 모델을 오버레이하고, 사용자의 손 동작을 로봇 운동에 실시간으로 매핑하는 데 있습니다. 이를 통해 조작자는 자신의 동작과 로봇 제약 조건 간의 대응 관계를 직관적으로 이해할 수 있으며, 물리적 로봇 환경 없이 자연스럽고 호환 가능한 맨손 조작 데이터를 수집할 수 있습니다. 연구는 15명의 참가자가 세 가지 작업을 수행하고 세 가지 피드백 조건을 비교하여, 실시간 가상 피드백이 데이터 품질을 크게 향상시키며 최종 궤적이 실제 로봇에서 직접 실행될 수 있음을 입증했습니다.

## 핵심 내용
### 방법
- **시스템 아키텍처**: Apple Vision Pro 기반의 증강 현실 환경을 구축하여 가상 로봇 모델을 실시간으로 렌더링하고, 사용자의 맨손 동작을 로봇 관절 공간에 동기화하여 매핑합니다.
- **데이터 수집**: 사용자는 시각적 피드백을 통해 동작과 로봇 운동의 관계를 이해하며 자연스러운 손동작 데이터를 수집하고, 물리적 로봇 하드웨어의 제약을 피합니다.

### 실험 설정
- **참가자**: 15명의 사용자가 각각 3가지 다른 작업(예: 잡기, 놓기, 조립)을 수행합니다.
- **피드백 조건**: 각 작업은 3가지 조건에서 실행됩니다—피드백 없음, 정적 피드백, 실시간 가상 로봇 피드백.
- **검증**: 수집된 궤적은 실제 물리적 로봇 하드웨어에 직접 재생되어 실행 성공률과 정밀도를 평가합니다.

### 주요 결과
- 실시간 가상 로봇 피드백은 데이터 품질을 크게 향상시켰으며, 실제 로봇에서의 궤적 성공률은 피드백 없음 또는 정적 피드백 조건보다 훨씬 높았습니다.
- 사용자는 물리적 로봇에 접촉하지 않고도 하드웨어 제약 조건과 호환되는 조작 데이터를 생성할 수 있어, 대규모 데이터 수집을 위한 확장 가능한 솔루션을 제공합니다.

### 결론
ARMADA는 로봇 학습 데이터 수집에서 증강 현실의 잠재력을 입증하며, 물리적 로봇에 대한 의존성을 제거하여 데이터 획득의 장벽을 낮췄습니다. 향후 피드백 지연 시간과 다중 작업 일반화 능력을 더욱 최적화할 수 있습니다.
