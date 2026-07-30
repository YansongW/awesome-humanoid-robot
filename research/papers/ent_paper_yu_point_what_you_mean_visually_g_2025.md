---
$id: ent_paper_yu_point_what_you_mean_visually_g_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Point What You Mean: Visually Grounded Instruction Policy'
  zh: Point-VLA
  ko: 'Point What You Mean: Visually Grounded Instruction Policy'
summary:
  en: 'Point What You Mean: Visually Grounded Instruction Policy (Point-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Tongji University, Shanghai Jiao Tong University, Spirit AI, Tsinghua University.'
  zh: Point-VLA 是由同济大学、上海交通大学、Spirit AI 和清华大学联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于通过引入显式视觉线索（如边界框）增强语言指令，解决物体指代歧义，并在杂乱或未见场景中实现更鲁棒的泛化能力。
  ko: 'Point What You Mean: Visually Grounded Instruction Policy (Point-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Tongji University, Shanghai Jiao Tong University, Spirit AI, Tsinghua University.'
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
- point_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18933v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Point What You Mean: Visually Grounded Instruction Policy (arXiv)'
  url: https://arxiv.org/abs/2512.18933
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Point-VLA source
  url: https://doi.org/10.48550/arXiv.2512.18933
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Point-VLA 是一种即插即用的策略，通过将像素级视觉线索（如边界框）与语言指令结合，显著提升了视觉-语言-动作模型在物体指代任务中的准确性。研究团队还开发了自动化数据标注流程，以最小化人工成本高效扩展视觉接地数据集。在真实世界的指代任务评估中，Point-VLA 在杂乱场景和未见物体场景下均持续优于纯文本指令的 VLA 模型，展现出强大的泛化能力。

## 核心内容
### 方法
- **核心问题**：传统 VLA 模型仅依赖文本提示时，在杂乱或分布外场景中物体指代能力有限。
- **Point-VLA 架构**：采用即插即用策略，在语言指令中嵌入显式视觉线索（如边界框），实现像素级物体接地，消除指代歧义。
- **数据标注**：开发自动化标注流程，通过最小化人工干预高效生成视觉接地数据集，支持大规模训练。

### 实验设置
- **任务**：在多样化真实世界指代任务上评估，包括杂乱场景和未见物体场景。
- **对比基线**：与纯文本指令的 VLA 模型进行对比。

### 关键结果
- **性能提升**：Point-VLA 在所有测试任务中均表现更强，尤其在杂乱场景和未见物体场景中优势显著。
- **泛化能力**：通过像素级视觉接地，模型在分布外场景中仍保持鲁棒泛化，验证了其解决物体指代歧义的有效性。

### 结论
Point-VLA 通过显式视觉线索增强语言指令，成功提升了 VLA 模型在复杂环境中的物体指代精度和泛化能力，为机器人操作提供了更可靠的接地策略。

## Overview
Vision-Language-Action (VLA) models align vision and language with embodied control, but their object referring ability remains limited when relying solely on text prompt, especially in cluttered or out-of-distribution (OOD) scenes. In this study, we introduce the Point-VLA, a plug-and-play policy that augments language instructions with explicit visual cues (e.g., bounding boxes) to resolve referential ambiguity and enable precise object-level grounding. To efficiently scale visually grounded datasets, we further develop an automatic data annotation pipeline requiring minimal human effort. We evaluate Point-VLA on diverse real-world referring tasks and observe consistently stronger performance than text-only instruction VLAs, particularly in cluttered or unseen-object scenarios, with robust generalization. These results demonstrate that Point-VLA effectively resolves object referring ambiguity through pixel-level visual grounding, achieving more generalizable embodied control.

## 개요
Vision-Language-Action (VLA) 모델은 시각 및 언어를 임베디드 제어와 정렬하지만, 텍스트 프롬프트에만 의존할 경우 객체 참조 능력이 제한적이며, 특히 복잡하거나 분포 외(OOD) 장면에서 그러합니다. 본 연구에서는 Point-VLA를 소개합니다. 이는 플러그 앤 플레이 정책으로, 명시적 시각적 단서(예: 경계 상자)를 언어 명령에 추가하여 참조 모호성을 해결하고 정밀한 객체 수준의 근거를 가능하게 합니다. 시각적으로 근거된 데이터셋을 효율적으로 확장하기 위해, 최소한의 인간 노력만 필요한 자동 데이터 주석 파이프라인을 추가로 개발했습니다. 다양한 실제 참조 작업에서 Point-VLA를 평가한 결과, 텍스트 전용 명령 VLA보다 일관되게 더 강력한 성능을 관찰했으며, 특히 복잡하거나 보지 못한 객체 시나리오에서 강력한 일반화를 보였습니다. 이러한 결과는 Point-VLA가 픽셀 수준의 시각적 근거를 통해 객체 참조 모호성을 효과적으로 해결하여 더 일반화 가능한 임베디드 제어를 달성함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각 및 언어를 임베디드 제어와 정렬하지만, 텍스트 프롬프트에만 의존할 경우 객체 참조 능력이 제한적이며, 특히 복잡하거나 분포 외(OOD) 장면에서 그러합니다. 본 연구에서는 Point-VLA를 소개합니다. 이는 플러그 앤 플레이 정책으로, 명시적 시각적 단서(예: 경계 상자)를 언어 명령에 추가하여 참조 모호성을 해결하고 정밀한 객체 수준의 근거를 가능하게 합니다. 시각적으로 근거된 데이터셋을 효율적으로 확장하기 위해, 최소한의 인간 노력만 필요한 자동 데이터 주석 파이프라인을 추가로 개발했습니다. 다양한 실제 참조 작업에서 Point-VLA를 평가한 결과, 텍스트 전용 명령 VLA보다 일관되게 더 강력한 성능을 관찰했으며, 특히 복잡하거나 보지 못한 객체 시나리오에서 강력한 일반화를 보였습니다. 이러한 결과는 Point-VLA가 픽셀 수준의 시각적 근거를 통해 객체 참조 모호성을 효과적으로 해결하여 더 일반화 가능한 임베디드 제어를 달성함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2512.18933v2
