---
$id: ent_paper_simfoundry_modular_and_automat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation'
  zh: 'SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation'
  ko: 'SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation'
summary:
  en: 'arXiv:2606.28276v2 Announce Type: replace Abstract: Training and evaluating robot policies in the real world is costly
    and difficult to scale. We introduce SimFoundry, a modular and automated system for zero-shot real-to-sim scene construction
    from a video. SimFoundry generates sim-ready digital twins and supports object, scene, and task editing, enabling the
    automated generation of diverse digital cousins: affordance-preserving variations of reconstructed real-world scenes.
    Policies trained on SimFoundry data transfer zero-shot to challenging real tasks involving multi-step manipulation, articulated
    object interaction, and bimanual interaction, and its digital cousins (variations of the original scene, objects, and
    tasks) facilitate generalization to new real-world conditions. Across 7 manipulation tasks and 5 policy architectures,
    SimFoundry simulation evaluations strongly predict real-world performance, with mean Pearson correlation 0.911 and mean
    maximum ranking violation 0.018. When evaluating sim-trained policies zero-shot in the real world, policies trained with
    object, scene, and task cousins in simulation show average task success rate improvements of 17%, 21%, and 40%, respectively.
    Additional details at https://research.nvidia.com/labs/gear/simfoundry/ .'
  zh: SimFoundry 是 NVIDIA 研究团队提出的模块化自动化系统，能从视频零样本构建仿真场景。其核心贡献在于生成保真数字孪生体并支持对象、场景与任务编辑，自动创建多样化的“数字表亲”变体。实验表明，SimFoundry 训练的机器人策略在零样本真实任务中成功率提升显著，且仿真评估与真实性能高度相关（平均
    Pearson 相关系数 0.911）。
  ko: 'arXiv:2606.28276v2 Announce Type: replace Abstract: Training and evaluating robot policies in the real world is costly
    and difficult to scale. We introduce SimFoundry, a modular and automated system for zero-shot real-to-sim scene construction
    from a video. SimFoundry generates sim-ready digital twins and supports object, scene, and task editing, enabling the
    automated generation of diverse digital cousins: affordance-preserving variations of reconstructed real-world scenes.
    Policies trained on SimFoundry data transfer zero-shot to challenging real tasks involving multi-step manipulation, articulated
    object interaction, and bimanual interaction, and its digital cousins (variations of the original scene, objects, and
    tasks) facilitate generalization to new real-world conditions. Across 7 manipulation tasks and 5 policy architectures,
    SimFoundry simulation evaluations strongly predict real-world performance, with mean Pearson correlation 0.911 and mean
    maximum ranking violation 0.018. When evaluating sim-trained policies zero-shot in the real world, policies trained with
    object, scene, and task cousins in simulation show average task success rate improvements of 17%, 21%, and 40%, respectively.
    Additional details at https://research.nvidia.com/labs/gear/simfoundry/ .'
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
- robotics
- simfoundry
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.28276v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (975 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation (arXiv)'
  url: https://arxiv.org/abs/2606.28276
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
SimFoundry 通过视频输入自动构建仿真就绪的数字孪生场景，并支持对物体、场景和任务进行灵活编辑，从而生成保留原始功能属性的多样化变体（即“数字表亲”）。该系统在 7 个操作任务和 5 种策略架构上验证了有效性：仿真评估结果与真实世界性能高度一致（平均 Pearson 相关系数 0.911，最大排名违反率仅 0.018）。零样本迁移测试中，使用物体、场景和任务变体训练的仿真策略，在真实世界的平均任务成功率分别提升 17%、21% 和 40%。

## 核心内容
### 方法架构
SimFoundry 采用模块化流水线设计，核心步骤包括：
- **零样本真实到仿真场景构建**：从单段视频自动生成仿真就绪的数字孪生体，无需人工标注或预训练模型。
- **编辑与变体生成**：支持对物体属性、场景布局和任务参数进行编辑，自动创建“数字表亲”——即保留原始功能（如可抓取性、可开合性）的多样化变体。

### 实验设置
- **任务与策略**：涵盖 7 个操作任务，包括多步操作、铰接物体交互和双臂协作；测试了 5 种策略架构（如行为克隆、扩散策略等）。
- **评估指标**：仿真与真实性能的相关性通过 Pearson 相关系数和最大排名违反率（Maximum Ranking Violation）衡量。

### 关键数字与结论
- **仿真-真实一致性**：平均 Pearson 相关系数达 0.911，最大排名违反率仅 0.018，表明 SimFoundry 的仿真评估可可靠预测真实世界表现。
- **零样本迁移效果**：
  - 使用物体变体训练：成功率提升 17%
  - 使用场景变体训练：成功率提升 21%
  - 使用任务变体训练：成功率提升 40%
- **泛化能力**：数字表亲策略在未见过的新场景、新物体配置和新任务变体中均表现出显著泛化优势。

### 结论
SimFoundry 通过自动化仿真场景生成与多样化变体编辑，有效降低了真实世界策略训练的成本与难度，同时为策略评估提供了高保真度的仿真环境。其零样本迁移能力与强仿真-真实相关性，为机器人学习领域提供了一种可扩展的解决方案。更多细节见项目主页：https://research.nvidia.com/labs/gear/simfoundry/。

## Overview
Training and evaluating robot policies in the real world is costly and difficult to scale. We introduce SimFoundry, a modular and automated system for zero-shot real-to-sim scene construction from a video. SimFoundry generates sim-ready digital twins and supports object, scene, and task editing, enabling the automated generation of diverse digital cousins: affordance-preserving variations of reconstructed real-world scenes. Policies trained on SimFoundry data transfer zero-shot to challenging real tasks involving multi-step manipulation, articulated object interaction, and bimanual interaction, and its digital cousins (variations of the original scene, objects, and tasks) facilitate generalization to new real-world conditions. Across 7 manipulation tasks and 5 policy architectures, SimFoundry simulation evaluations strongly predict real-world performance, with mean Pearson correlation 0.911 and mean maximum ranking violation 0.018. When evaluating sim-trained policies zero-shot in the real world, policies trained with object, scene, and task cousins in simulation show average task success rate improvements of 17%, 21%, and 40%, respectively. Additional details at https://research.nvidia.com/labs/gear/simfoundry/ .

## 参考
- http://arxiv.org/abs/2606.28276v2

## 개요
SimFoundry는 비디오 입력을 통해 시뮬레이션 준비가 완료된 디지털 트윈 장면을 자동으로 구축하고, 객체, 장면 및 작업에 대한 유연한 편집을 지원하여 원래 기능 속성을 유지하는 다양한 변형(즉, "디지털 사촌")을 생성합니다. 이 시스템은 7가지 조작 작업과 5가지 정책 아키텍처에서 유효성을 검증했습니다: 시뮬레이션 평가 결과는 실제 세계 성능과 높은 일치도를 보였습니다(평균 Pearson 상관 계수 0.911, 최대 순위 위반율 0.018에 불과). 제로샷 전이 테스트에서 객체, 장면 및 작업 변형으로 훈련된 시뮬레이션 정책은 실제 세계에서 평균 작업 성공률이 각각 17%, 21%, 40% 향상되었습니다.

## 핵심 내용
### 방법 아키텍처
SimFoundry는 모듈식 파이프라인 설계를 채택하며, 핵심 단계는 다음과 같습니다:
- **제로샷 실제-시뮬레이션 장면 구축**: 단일 비디오에서 시뮬레이션 준비가 완료된 디지털 트윈을 자동 생성하며, 수동 주석이나 사전 훈련된 모델이 필요 없습니다.
- **편집 및 변형 생성**: 객체 속성, 장면 레이아웃 및 작업 매개변수 편집을 지원하며, 원래 기능(예: 파지 가능성, 개폐 가능성)을 유지하는 다양한 "디지털 사촌"을 자동으로 생성합니다.

### 실험 설정
- **작업 및 정책**: 다단계 조작, 관절 객체 상호작용 및 양팔 협력을 포함한 7가지 조작 작업을 다루며, 5가지 정책 아키텍처(예: 행동 복제, 확산 정책 등)를 테스트했습니다.
- **평가 지표**: 시뮬레이션과 실제 성능 간의 상관 관계는 Pearson 상관 계수와 최대 순위 위반율(Maximum Ranking Violation)로 측정되었습니다.

### 핵심 수치 및 결론
- **시뮬레이션-실제 일치도**: 평균 Pearson 상관 계수 0.911, 최대 순위 위반율 0.018에 불과하여 SimFoundry의 시뮬레이션 평가가 실제 세계 성능을 신뢰성 있게 예측할 수 있음을 나타냅니다.
- **제로샷 전이 효과**:
  - 객체 변형으로 훈련: 성공률 17% 향상
  - 장면 변형으로 훈련: 성공률 21% 향상
  - 작업 변형으로 훈련: 성공률 40% 향상
- **일반화 능력**: 디지털 사촌 정책은 보지 못한 새로운 장면, 새로운 객체 구성 및 새로운 작업 변형에서 모두 유의미한 일반화 이점을 보였습니다.

### 결론
SimFoundry는 자동화된 시뮬레이션 장면 생성과 다양한 변형 편집을 통해 실제 세계 정책 훈련의 비용과 난이도를 효과적으로 낮추면서, 정책 평가를 위한 고충실도 시뮬레이션 환경을 제공합니다. 제로샷 전이 능력과 강력한 시뮬레이션-실제 상관 관계는 로봇 학습 분야에 확장 가능한 솔루션을 제공합니다. 자세한 내용은 프로젝트 페이지를 참조하세요: https://research.nvidia.com/labs/gear/simfoundry/.
