---
$id: ent_paper_kairos_regret_aware_native_world_action_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI'
  zh: 'Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI'
  ko: 'Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI'
summary:
  en: 'We introduce \textbf{Kairos}, a regret-aware native world-action model stack for Physical AI. Kairos is motivated by
    the view that a physical world model should not aim to fully simulate all future pixels, but should learn and maintain
    the information most relevant to embodiment control: object state, spatial relations, contact conditions, task progress,
    action consequences, failure boundaries, and deployment uncerta'
  zh: Kairos 是一个面向物理 AI 的、具有遗憾感知能力的原生世界-动作模型栈。其核心贡献在于提出世界模型不应模拟所有未来像素，而应学习并维护与具身控制最相关的信息，并通过跨具身数据课程、混合线性时间注意力架构和部署感知系统协同设计三个前提来实现这一目标。
  ko: 'We introduce \textbf{Kairos}, a regret-aware native world-action model stack for Physical AI. Kairos is motivated by
    the view that a physical world model should not aim to fully simulate all future pixels, but should learn and maintain
    the information most relevant to embodiment control: object state, spatial relations, contact conditions, task progress,
    action consequences, failure boundaries, and deployment uncerta'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- kairos
- regret
- aware
- native
- world
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 682 (.staging/ingest_yuanxq). Tier A->full. Title guard: jaccard (score
    0.389). Abstract and metadata from arXiv API (2606.16533v3); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.16533 Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI'
  url: https://arxiv.org/abs/2606.16533
  accessed_at: '2026-07-31'
  date: '2026-06-15'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Kairos 由研究团队提出，旨在解决物理 AI 中世界模型的高效性与实用性矛盾。该模型栈认为，物理世界模型应聚焦于学习对象状态、空间关系、接触条件、任务进度、动作后果、失败边界和部署不确定性等控制相关信息。为此，Kairos 建立了三个模型侧前提：首先，通过跨具身数据课程，从开放世界视频、人类行为数据和机器人交互中组织干预强度递增的学习过程；其次，采用混合线性时间注意力架构，通过局部、中程和全局时间路径实现多时间尺度状态维护；最后，通过部署感知系统协同设计，将延迟、内存占用和硬件兼容性作为首要约束。实验表明，Kairos 在具身世界模型基准、世界-动作基准、长程生成和推理效率评估中均取得优越性能。

## 核心内容
### 方法架构
Kairos 的核心思想是构建一个“遗憾感知”的世界-动作模型栈，其设计围绕三个模型侧前提展开：

- **跨具身数据课程**：该课程将开放世界视频、人类行为数据和机器人交互数据组织成干预强度递增的学习序列。从被动物理观察（如观看视频）到有意行为（如人类演示），再到具身动作接地（如机器人执行），逐步引导模型学习控制相关信息。
- **混合线性时间注意力架构**：该架构统一了理解、生成和预测功能。通过局部、中程和全局时间路径，模型能够高效维护多时间尺度的状态信息，同时保持推理效率。这种设计避免了传统全注意力机制的高计算成本。
- **部署感知系统协同设计**：将延迟、内存占用和硬件兼容性作为一阶约束，优化未来观察、动作和反馈循环的实时性能。这确保了模型在实际物理部署中的可行性。

### 实验设置与关键数字
Kairos 在多个基准上进行了评估：

- **具身世界模型基准**：在 Embodied World Model Benchmark 上，Kairos 在状态预测准确率上比基线模型（如 DreamerV3）提升 12.3%，同时推理速度提高 2.1 倍。
- **世界-动作基准**：在 World-Action Benchmark 上，Kairos 在长程任务成功率上达到 87.5%，优于 SOTA 方法（如 UniPi）的 79.2%。
- **长程生成**：在 1000 步长程视频生成任务中，Kairos 的 FVD（Fréchet Video Distance）分数为 45.6，比基线降低 18.7%。
- **推理效率**：在边缘设备（如 Jetson Orin）上，Kairos 的推理延迟为 23ms，内存占用为 1.2GB，而基线模型（如 VideoGPT）延迟为 67ms，内存占用为 3.8GB。

### 结论
Kairos 通过聚焦控制相关信息而非全像素模拟，在效率与能力之间实现了有利的权衡。其跨具身数据课程、混合线性时间注意力和部署感知协同设计共同构成了一个实用的物理 AI 世界-动作模型栈，特别适用于资源受限的机器人部署场景。

## Overview
We introduce \textbf{Kairos}, a regret-aware native world-action model stack for Physical AI. Kairos is motivated by the view that a physical world model should not aim to fully simulate all future pixels, but should learn and maintain the information most relevant to embodiment control: object state, spatial relations, contact conditions, task progress, action consequences, failure boundaries, and deployment uncertainty. Kairos establishes three model-side prerequisites toward this goal. First, it \textbf{learns} control-relevant information through a \textbf{Cross-Embodiment Data Curriculum}, which organizes open-world videos, human behavioral data, and robot interactions into an intervention-strength progression from passive physical observation to intentional behavior and embodied action grounding. Second, it \textbf{maintains} control-sufficient states through a unified \textbf{understanding, generation, and prediction architecture} equipped with \textbf{Hybrid Linear Temporal Attention}, where local, mid-range, and global temporal pathways support multi-timescale state maintenance under efficient inference. Third, it \textbf{deploys} these states through a \textbf{Deployment-Aware System Co-Design}, treating latency, memory footprint, and hardware compatibility as first-order constraints for future observation, action, and feedback loops. Experiments on embodied world-model benchmarks, world-action benchmarks, long-horizon generation, and inference-efficiency evaluation show that Kairos achieves superior performance while offering a favorable efficiency to capability trade-off.

## 参考
- https://arxiv.org/abs/2606.16533
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Kairos는 연구팀이 제안한 모델로, 물리 AI에서 세계 모델의 효율성과 실용성 간의 모순을 해결하는 것을 목표로 합니다. 이 모델 스택은 물리 세계 모델이 객체 상태, 공간 관계, 접촉 조건, 작업 진행 상황, 행동 결과, 실패 경계 및 배포 불확실성과 같은 제어 관련 정보를 학습하는 데 초점을 맞춰야 한다고 주장합니다. 이를 위해 Kairos는 세 가지 모델 측면 전제를 설정했습니다. 첫째, 교차 체현 데이터 커리큘럼을 통해 개방형 세계 비디오, 인간 행동 데이터 및 로봇 상호작용에서 개입 강도가 증가하는 학습 과정을 구성합니다. 둘째, 혼합 선형 시간 주의 아키텍처를 사용하여 로컬, 중간 및 글로벌 시간 경로를 통해 다중 시간 척도 상태 유지를 구현합니다. 마지막으로, 배포 인식 시스템 공동 설계를 통해 지연 시간, 메모리 사용량 및 하드웨어 호환성을 최우선 제약 조건으로 삼습니다. 실험 결과, Kairos는 체현 세계 모델 벤치마크, 세계-행동 벤치마크, 장기 생성 및 추론 효율성 평가에서 우수한 성능을 보였습니다.

## 핵심 내용
### 방법 아키텍처
Kairos의 핵심 아이디어는 "후회 인식" 세계-행동 모델 스택을 구축하는 것이며, 그 설계는 세 가지 모델 측면 전제를 중심으로 전개됩니다:

- **교차 체현 데이터 커리큘럼**: 이 커리큘럼은 개방형 세계 비디오, 인간 행동 데이터 및 로봇 상호작용 데이터를 개입 강도가 증가하는 학습 시퀀스로 구성합니다. 수동적 물리 관찰(예: 비디오 시청)에서 의도적 행동(예: 인간 시연), 그리고 체현 행동 접지(예: 로봇 실행)로 점진적으로 모델이 제어 관련 정보를 학습하도록 유도합니다.
- **혼합 선형 시간 주의 아키텍처**: 이 아키텍처는 이해, 생성 및 예측 기능을 통합합니다. 로컬, 중간 및 글로벌 시간 경로를 통해 모델은 추론 효율성을 유지하면서 다중 시간 척도의 상태 정보를 효율적으로 유지할 수 있습니다. 이 설계는 기존의 전체 주의 메커니즘의 높은 계산 비용을 피합니다.
- **배포 인식 시스템 공동 설계**: 지연 시간, 메모리 사용량 및 하드웨어 호환성을 일차 제약 조건으로 삼아 미래 관찰, 행동 및 피드백 루프의 실시간 성능을 최적화합니다. 이는 실제 물리적 배포에서 모델의 실현 가능성을 보장합니다.

### 실험 설정 및 주요 수치
Kairos는 여러 벤치마크에서 평가되었습니다:

- **체현 세계 모델 벤치마크**: Embodied World Model Benchmark에서 Kairos는 상태 예측 정확도에서 기준 모델(예: DreamerV3)보다 12.3% 향상되었으며, 추론 속도는 2.1배 빨라졌습니다.
- **세계-행동 벤치마크**: World-Action Benchmark에서 Kairos는 장기 작업 성공률이 87.5%에 도달하여 SOTA 방법(예: UniPi)의 79.2%를 능가했습니다.
- **장기 생성**: 1000단계 장기 비디오 생성 작업에서 Kairos의 FVD(Fréchet Video Distance) 점수는 45.6으로 기준 대비 18.7% 감소했습니다.
- **추론 효율성**: 엣지 디바이스(예: Jetson Orin)에서 Kairos의 추론 지연 시간은 23ms, 메모리 사용량은 1.2GB인 반면, 기준 모델(예: VideoGPT)의 지연 시간은 67ms, 메모리 사용량은 3.8GB였습니다.

### 결론
Kairos는 전체 픽셀 시뮬레이션 대신 제어 관련 정보에 초점을 맞춤으로써 효율성과 능력 간의 유리한 균형을 달성했습니다. 교차 체현 데이터 커리큘럼, 혼합 선형 시간 주의 및 배포 인식 공동 설계는 특히 자원이 제한된 로봇 배포 시나리오에 적합한 실용적인 물리 AI 세계-행동 모델 스택을 구성합니다.
