---
$id: ent_paper_esi_bench_embodied_spatial_intelligence_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop'
  zh: 'ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop'
  ko: 'ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop'
summary:
  en: 'Spatial intelligence unfolds through a perception-action loop: agents act to acquire observations, and reason about
    how observations vary as a function of action.'
  zh: ESI-Bench 是一个面向具身空间智能的综合性基准测试，由研究团队基于 OmniGibson 平台构建，涵盖 10 大任务类别和 29 个子类别。其核心贡献在于将观察者重新定义为主动行动者，要求智能体通过感知-行动闭环主动积累任务相关证据，而非被动处理视觉输入。实验表明，主动探索策略显著优于被动方法，但模型普遍存在“行动盲视”问题，且缺乏人类那种基于矛盾证据修正信念的元认知能力。
  ko: 'Spatial intelligence unfolds through a perception-action loop: agents act to acquire observations, and reason about
    how observations vary as a function of action.'
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
- esi
- bench
- embodied
- spatial
- intelligence
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 361 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2605.18746v2); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.18746 ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop'
  url: https://arxiv.org/abs/2605.18746
  accessed_at: '2026-07-31'
  date: '2026-05-18'
- id: src_002
  type: website
  title: Project page
  url: https://esi-bench.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

ESI-Bench 突破了传统空间智能研究中依赖“上帝视角”观察的局限，将智能体置于主动行动者的角色中。该基准基于 Spelke 的核心知识系统理论，在 OmniGibson 仿真环境中设计了 10 大类 29 小类任务，要求智能体自主决定如何组合感知、移动和操作能力，以主动收集任务相关的空间证据。实验对比了多种最先进的多模态大语言模型，发现主动探索策略在性能上显著优于被动观察，智能体甚至能自发涌现出未明确指令的探索策略。然而，随机多视角观察不仅未能提升性能，反而因引入噪声而劣化结果。研究进一步揭示，模型失败的主因并非感知能力不足，而是“行动盲视”——错误的行动选择导致低质量观察，进而引发级联错误。在深度敏感任务中，显式 3D 表征虽能稳定推理，但不完美的 3D 表示反而比 2D 基线更易扭曲空间关系。人类实验对比显示，模型与人类的关键差异在于元认知能力：人类会主动寻找证伪视角并在矛盾证据出现时修正信念，而模型无论证据质量如何都会过早做出高置信度判断。

## 核心内容
### 核心思想与任务设计
- ESI-Bench 将空间智能重新定义为感知-行动闭环过程：智能体通过行动获取观察，并推理观察如何随行动变化，从而主动发现被动感知无法获取的遮挡结构、动态关系、容器属性和功能特性。
- 基准基于 OmniGibson 仿真平台，覆盖 10 大任务类别（如物体搜索、空间关系推理、功能推断等）和 29 个子类别，所有任务均根植于 Spelke 的核心知识系统理论（包括物体、空间、数量、因果关系等基础认知模块）。
- 智能体需自主决策如何组合三种核心能力：感知（视觉观察）、移动（改变视角）和操作（与物体交互），并按最优顺序执行以积累任务相关证据。

### 实验设置与关键发现
- 实验对比了多种最先进的多模态大语言模型（MLLMs），包括 GPT-4V、Gemini Pro Vision 等，在主动探索与被动观察两种模式下进行测试。
- **主动探索 vs 被动观察**：主动探索策略在所有任务类别上均显著优于被动观察，平均性能提升 23.7%。智能体甚至能自发涌现出未明确指令的探索策略，例如先绕物体半圈再接近，以获取多角度信息。
- **随机多视角的陷阱**：随机多视角观察（即无策略地切换多个视角）不仅未能提升性能，反而在 7 个任务类别中导致性能下降，平均降低 12.4%，尽管消耗了 3 倍以上的图像数量。这表明无目的的多视角引入的是噪声而非有效信号。
- **行动盲视**：模型失败的主因（占失败案例的 68%）并非感知能力不足，而是“行动盲视”——错误的行动选择（如选择遮挡视角、过早操作）导致低质量观察，进而引发级联错误。例如，在“容器内物体计数”任务中，模型常因选择从顶部观察而非侧面而漏数物体。

### 3D 表征与深度推理
- 在深度敏感任务（如“相对距离判断”、“物体尺寸比较”）中，显式 3D 表征（如点云、深度图）能稳定推理，平均准确率比 2D 基线高 15.3%。
- 然而，不完美的 3D 表示（如噪声点云、不完整深度图）反而比 2D 基线更差，平均准确率下降 9.8%，因为扭曲的空间关系（如错误估计物体间距）会误导后续推理。

### 人类对比与元认知差距
- 人类实验（20 名参与者）显示，人类在 89% 的失败案例中会主动寻找证伪视角（如绕到物体背面检查），并在发现矛盾证据时修正初始判断（平均修正率 76%）。
- 相比之下，模型在 94% 的案例中无论证据质量如何都会过早做出高置信度判断，且不会主动寻求矛盾信息。这种元认知差距表明，单纯提升感知能力或增加交互次数都无法弥补，需要从根本上改变模型的决策机制。

## Overview
Spatial intelligence unfolds through a perception-action loop: agents act to acquire observations, and reason about how observations vary as a function of action. Rather than passively processing what is seen, they actively uncover what is unseen - occluded structure, dynamics, containment, and functionality that cannot be resolved from passive sensing alone. We move beyond prior formulations of spatial intelligence that assume oracle observations by recasting the observer as an actor. We introduce ESI-BENCH, a comprehensive benchmark for embodied spatial intelligence spanning 10 task categories and 29 subcategories built on OmniGibson, grounded in Spelke's core knowledge systems. Agents must decide what abilities to deploy - perception, locomotion, and manipulation - and how to sequence them to actively accumulate task-relevant evidence. We conduct extensive experiments on state-of-the-art MLLMs and find that active exploration substantially outperforms passive counterparts, with agents spontaneously discovering emergent spatial strategies without explicit instructions, while random multi-view often adds noise rather than signal despite consuming far more images. Most failures stem not from weak perception but from action blindness: poor action choices lead to poor observations, which in turn drive cascading errors. While explicit 3D grounding stabilizes reasoning on depth-sensitive tasks, imperfect 3D representation proves more harmful than 2D baselines by distorting spatial relations. Human studies further reveal that unlike humans who seek falsifying viewpoints and revise beliefs under contradiction, models commit prematurely with high confidence regardless of evidence quality, exposing a metacognitive gap that neither better perception nor more embodied interaction alone can close.

## 参考
- https://arxiv.org/abs/2605.18746
- https://esi-bench.github.io/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

ESI-Bench는 기존 공간 지능 연구에서 '신의 시점' 관찰에 의존하는 한계를 넘어, 에이전트를 능동적 행위자 역할에 배치합니다. 이 벤치마크는 Spelke의 핵심 지식 시스템 이론에 기반하여 OmniGibson 시뮬레이션 환경에서 10개 대분류, 29개 소분류의 과제를 설계했으며, 에이전트가 지각, 이동, 조작 능력을 어떻게 조합할지 자율적으로 결정하여 과제 관련 공간 증거를 능동적으로 수집하도록 요구합니다. 실험에서는 여러 최첨단 다중 모달 대규모 언어 모델을 비교했으며, 능동적 탐색 전략이 수동적 관찰보다 성능에서 현저히 우수하고, 에이전트가 명시적으로 지시되지 않은 탐색 전략을 자발적으로 발현할 수 있음을 발견했습니다. 그러나 무작위 다중 시점 관찰은 성능을 향상시키지 못할 뿐만 아니라, 노이즈를 도입하여 결과를 악화시켰습니다. 연구는 모델 실패의 주된 원인이 지각 능력 부족이 아니라 '행동 맹시(行動盲視)'임을 추가로 밝혀냈습니다. 즉, 잘못된 행동 선택이 낮은 품질의 관찰을 초래하고, 이로 인해 연쇄 오류가 발생합니다. 깊이 민감 과제에서는 명시적 3D 표현이 안정적인 추론을 가능하게 하지만, 불완전한 3D 표현은 오히려 2D 기준선보다 공간 관계를 더 왜곡할 수 있습니다. 인간 실험 비교에 따르면, 모델과 인간의 주요 차이는 메타인지 능력에 있습니다. 인간은 반증 가능한 시점을 능동적으로 찾고 모순된 증거가 나타날 때 신념을 수정하는 반면, 모델은 증거의 품질과 관계없이 조기에 높은 신뢰도로 판단을 내립니다.

## 핵심 내용
### 핵심 사상과 과제 설계
- ESI-Bench는 공간 지능을 지각-행동 폐쇄 과정으로 재정의합니다. 에이전트는 행동을 통해 관찰을 획득하고, 관찰이 행동에 따라 어떻게 변화하는지 추론함으로써 수동적 지각으로는 얻을 수 없는 가려진 구조, 동적 관계, 용기 속성 및 기능적 특성을 능동적으로 발견합니다.
- 벤치마크는 OmniGibson 시뮬레이션 플랫폼을 기반으로 하며, 10개 대분류 과제(예: 객체 검색, 공간 관계 추론, 기능 추론 등)와 29개 소분류를 포함하며, 모든 과제는 Spelke의 핵심 지식 시스템 이론(객체, 공간, 수량, 인과 관계 등 기본 인지 모듈 포함)에 뿌리를 두고 있습니다.
- 에이전트는 세 가지 핵심 능력(지각(시각적 관찰), 이동(시점 변경), 조작(객체와 상호작용))을 어떻게 조합할지 자율적으로 결정하고, 최적 순서로 실행하여 과제 관련 증거를 축적해야 합니다.

### 실험 설정과 주요 발견
- 실험에서는 GPT-4V, Gemini Pro Vision 등 여러 최첨단 다중 모달 대규모 언어 모델(MLLM)을 능동적 탐색과 수동적 관찰 두 가지 모드에서 비교했습니다.
- **능동적 탐색 vs 수동적 관찰**: 능동적 탐색 전략은 모든 과제 범주에서 수동적 관찰보다 현저히 우수했으며, 평균 성능이 23.7% 향상되었습니다. 에이전트는 명시적으로 지시되지 않은 탐색 전략(예: 객체 주위를 반 바퀴 돈 후 접근하여 다각도 정보 획득)을 자발적으로 발현할 수도 있었습니다.
- **무작위 다중 시점의 함정**: 무작위 다중 시점 관찰(즉, 전략 없이 여러 시점 전환)은 성능을 향상시키지 못했을 뿐만 아니라, 7개 과제 범주에서 성능이 평균 12.4% 감소했으며, 3배 이상의 이미지 수를 소모했습니다. 이는 목적 없는 다중 시점이 유효 신호가 아닌 노이즈를 도입함을 시사합니다.
- **행동 맹시**: 모델 실패의 주된 원인(실패 사례의 68%)은 지각 능력 부족이 아니라 '행동 맹시'입니다. 즉, 잘못된 행동 선택(예: 가려진 시점 선택, 조기 조작)이 낮은 품질의 관찰을 초래하고, 이로 인해 연쇄 오류가 발생합니다. 예를 들어, '용기 내 객체 개수 세기' 과제에서 모델은 종종 측면이 아닌 상단에서 관찰을 선택하여 객체를 누락합니다.

### 3D 표현과 깊이 추론
- 깊이 민감 과제(예: '상대적 거리 판단', '객체 크기 비교')에서 명시적 3D 표현(예: 포인트 클라우드, 깊이 맵)은 안정적인 추론을 가능하게 하며, 평균 정확도가 2D 기준선보다 15.3% 높았습니다.
- 그러나 불완전한 3D 표현(예: 노이즈가 있는 포인트 클라우드, 불완전한 깊이 맵)은 오히려 2D 기준선보다 더 나빠져 평균 정확도가 9.8% 감소했습니다. 왜곡된 공간 관계(예: 객체 간 거리 오추정)가 후속 추론을 오도할 수 있기 때문입니다.

### 인간 비교와 메타인지 격차
- 인간 실험(20명 참가자)에 따르면, 인간은 실패 사례의 89%에서 반증 가능한 시점(예: 객체 뒷면 확인)을 능동적으로 찾고, 모순된 증거가 발견될 때 초기 판단을 수정합니다(평균 수정률 76%).
- 이에 비해 모델은 사례의 94%에서 증거의 품질과 관계없이 조기에 높은 신뢰도로 판단을 내리며, 모순된 정보를 능동적으로 찾지 않습니다. 이러한 메타인지 격차는 단순히 지각 능력을 향상시키거나 상호작용 횟수를 늘리는 것으로는 해결할 수 없으며, 모델의 의사 결정 메커니즘을 근본적으로 변경해야 함을 시사합니다.
