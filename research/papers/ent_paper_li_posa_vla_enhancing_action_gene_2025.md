---
$id: ent_paper_li_posa_vla_enhancing_action_gene_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention'
  zh: PosA-VLA
  ko: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention'
summary:
  en: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention (PosA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney.'
  zh: PosA-VLA 是悉尼大学于 2025 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过姿态条件锚点注意力机制，解决现有 VLA 模型因空间均匀感知场导致的冗余动作问题，从而提升动作生成的精确性与效率。
  ko: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention (PosA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- posa_vla
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.03724v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (592 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention (arXiv)'
  url: https://arxiv.org/abs/2512.03724
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PosA-VLA source
  url: https://doi.org/10.48550/arXiv.2512.03724
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前视觉-语言-动作模型在具身任务中表现优异，但在复杂环境下常因目标无关物体的干扰而产生冗余或不稳定的动作轨迹。PosA-VLA 框架通过姿态条件监督来锚定视觉注意力，使模型持续聚焦于任务相关区域，从而更好地将指令语义与可操作的视觉线索对齐。该框架采用轻量级架构，无需额外的感知模块（如分割或接地网络），保证了高效的推理能力。实验表明，该方法在多种机器人操作基准上实现了精确且省时的行为，并在多种挑战性环境中展现出稳健的泛化能力。

## 核心内容
### 问题背景
- 现有 VLA 模型在具身任务中表现良好，但常生成沿轨迹的冗余或不稳定动作，限制了其在时间敏感场景中的应用。
- 作者将冗余动作归因于现有 VLA 的空间均匀感知场：模型在复杂环境中易被目标无关物体分散注意力。

### 方法架构
- **PosA-VLA 框架**：通过姿态条件监督锚定视觉注意力，持续引导模型感知任务相关区域。
- **姿态条件锚点注意力机制**：使模型更好地对齐指令语义与可操作的视觉线索，提升动作生成的精确性与效率。
- **轻量级架构**：无需辅助感知模块（如分割网络或接地网络），确保高效推理。

### 实验设置与结果
- 在多种机器人操作基准上进行实验，验证了方法在具身任务中的精确且省时行为。
- 在多种挑战性环境中展现出稳健的泛化能力，未提供具体数字但强调性能提升。

## Overview
The Vision-Language-Action (VLA) models have demonstrated remarkable performance on embodied tasks and shown promising potential for real-world applications. However, current VLAs still struggle to produce consistent and precise target-oriented actions, as they often generate redundant or unstable motions along trajectories, limiting their applicability in time-sensitive scenarios.In this work, we attribute these redundant actions to the spatially uniform perception field of existing VLAs, which causes them to be distracted by target-irrelevant objects, especially in complex environments.To address this issue, we propose an efficient PosA-VLA framework that anchors visual attention via pose-conditioned supervision, consistently guiding the model's perception toward task-relevant regions. The pose-conditioned anchor attention mechanism enables the model to better align instruction semantics with actionable visual cues, thereby improving action generation precision and efficiency. Moreover, our framework adopts a lightweight architecture and requires no auxiliary perception modules (e.g., segmentation or grounding networks), ensuring efficient inference. Extensive experiments verify that our method executes embodied tasks with precise and time-efficient behavior across diverse robotic manipulation benchmarks and shows robust generalization in a variety of challenging environments.

## Overview
The Vision-Language-Action (VLA) models have demonstrated remarkable performance on embodied tasks and shown promising potential for real-world applications. However, current VLAs still struggle to produce consistent and precise target-oriented actions, as they often generate redundant or unstable motions along trajectories, limiting their applicability in time-sensitive scenarios. In this work, we attribute these redundant actions to the spatially uniform perception field of existing VLAs, which causes them to be distracted by target-irrelevant objects, especially in complex environments. To address this issue, we propose an efficient PosA-VLA framework that anchors visual attention via pose-conditioned supervision, consistently guiding the model's perception toward task-relevant regions. The pose-conditioned anchor attention mechanism enables the model to better align instruction semantics with actionable visual cues, thereby improving action generation precision and efficiency. Moreover, our framework adopts a lightweight architecture and requires no auxiliary perception modules (e.g., segmentation or grounding networks), ensuring efficient inference. Extensive experiments verify that our method executes embodied tasks with precise and time-efficient behavior across diverse robotic manipulation benchmarks and shows robust generalization in a variety of challenging environments.

## Content
The Vision-Language-Action (VLA) models have demonstrated remarkable performance on embodied tasks and shown promising potential for real-world applications. However, current VLAs still struggle to produce consistent and precise target-oriented actions, as they often generate redundant or unstable motions along trajectories, limiting their applicability in time-sensitive scenarios. In this work, we attribute these redundant actions to the spatially uniform perception field of existing VLAs, which causes them to be distracted by target-irrelevant objects, especially in complex environments. To address this issue, we propose an efficient PosA-VLA framework that anchors visual attention via pose-conditioned supervision, consistently guiding the model's perception toward task-relevant regions. The pose-conditioned anchor attention mechanism enables the model to better align instruction semantics with actionable visual cues, thereby improving action generation precision and efficiency. Moreover, our framework adopts a lightweight architecture and requires no auxiliary perception modules (e.g., segmentation or grounding networks), ensuring efficient inference. Extensive experiments verify that our method executes embodied tasks with precise and time-efficient behavior across diverse robotic manipulation benchmarks and shows robust generalization in a variety of challenging environments.

## 参考
- http://arxiv.org/abs/2512.03724v2

## 개요
현재 비전-언어-행동 모델은 구현 작업에서 우수한 성능을 보이지만, 복잡한 환경에서는 목표와 무관한 객체의 간섭으로 인해 중복되거나 불안정한 행동 궤적이 발생하는 경우가 많습니다. PosA-VLA 프레임워크는 자세 조건 감독을 통해 시각적 주의를 고정시켜 모델이 작업 관련 영역에 지속적으로 집중하도록 하여, 명령 의미론과 실행 가능한 시각적 단서를 더 잘 정렬합니다. 이 프레임워크는 경량 아키텍처를 채택하여 추가적인 인식 모듈(예: 분할 또는 접지 네트워크) 없이도 효율적인 추론 능력을 보장합니다. 실험 결과, 이 방법은 다양한 로봇 조작 벤치마크에서 정밀하고 시간 효율적인 행동을 구현했으며, 여러 도전적인 환경에서 강건한 일반화 능력을 보여주었습니다.

## 핵심 내용
### 문제 배경
- 기존 VLA 모델은 구현 작업에서 우수한 성능을 보이지만, 궤적을 따라 중복되거나 불안정한 행동을 생성하는 경우가 많아 시간에 민감한 시나리오에서의 적용이 제한됩니다.
- 저자는 중복 행동을 기존 VLA의 공간적으로 균일한 인식 필드에 기인한다고 보았습니다. 즉, 모델이 복잡한 환경에서 목표와 무관한 객체에 쉽게 주의가 분산된다는 것입니다.

### 방법 아키텍처
- **PosA-VLA 프레임워크**: 자세 조건 감독을 통해 시각적 주의를 고정시켜 모델이 작업 관련 영역을 지속적으로 인식하도록 유도합니다.
- **자세 조건 앵커 주의 메커니즘**: 모델이 명령 의미론과 실행 가능한 시각적 단서를 더 잘 정렬하여 행동 생성의 정밀성과 효율성을 향상시킵니다.
- **경량 아키텍처**: 보조 인식 모듈(예: 분할 네트워크 또는 접지 네트워크) 없이도 효율적인 추론을 보장합니다.

### 실험 설정 및 결과
- 다양한 로봇 조작 벤치마크에서 실험을 수행하여 구현 작업에서의 정밀하고 시간 효율적인 행동을 검증했습니다.
- 여러 도전적인 환경에서 강건한 일반화 능력을 보여주었으며, 구체적인 수치는 제공되지 않았지만 성능 향상을 강조했습니다.
