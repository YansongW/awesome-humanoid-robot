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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18933v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (653 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.18933v2

## 개요
Point-VLA는 픽셀 수준의 시각적 단서(예: 경계 상자)를 언어 지시와 결합하여 시각-언어-행동 모델의 객체 지시 작업 정확도를 크게 향상시키는 플러그 앤 플레이 정책입니다. 연구팀은 또한 인적 비용을 최소화하면서 시각적 접지 데이터 세트를 효율적으로 확장할 수 있는 자동 데이터 주석 파이프라인을 개발했습니다. 실제 세계 지시 작업 평가에서 Point-VLA는 혼잡한 장면과 미지의 객체 장면 모두에서 텍스트 지시만 사용하는 VLA 모델보다 지속적으로 우수한 성능을 보이며 강력한 일반화 능력을 입증했습니다.

## 핵심 내용
### 방법
- **핵심 문제**: 기존 VLA 모델은 텍스트 프롬프트에만 의존할 때 혼잡하거나 분포 외 장면에서 객체 지시 능력이 제한적입니다.
- **Point-VLA 아키텍처**: 언어 지시에 명시적 시각적 단서(예: 경계 상자)를 포함시키는 플러그 앤 플레이 전략을 채택하여 픽셀 수준의 객체 접지를 실현하고 지시 모호성을 제거합니다.
- **데이터 주석**: 자동 주석 파이프라인을 개발하여 인적 개입을 최소화하면서 시각적 접지 데이터 세트를 효율적으로 생성하고 대규모 훈련을 지원합니다.

### 실험 설정
- **작업**: 혼잡한 장면과 미지의 객체 장면을 포함한 다양한 실제 세계 지시 작업에서 평가합니다.
- **비교 기준**: 텍스트 지시만 사용하는 VLA 모델과 비교합니다.

### 주요 결과
- **성능 향상**: Point-VLA는 모든 테스트 작업에서 더 강력한 성능을 보였으며, 특히 혼잡한 장면과 미지의 객체 장면에서 두드러진 우위를 보였습니다.
- **일반화 능력**: 픽셀 수준의 시각적 접지를 통해 모델은 분포 외 장면에서도 견고한 일반화를 유지하여 객체 지시 모호성 해결의 효과성을 검증했습니다.

### 결론
Point-VLA는 명시적 시각적 단서를 통해 언어 지시를 강화함으로써 복잡한 환경에서 VLA 모델의 객체 지시 정확도와 일반화 능력을 성공적으로 향상시켰으며, 로봇 조작을 위한 더 신뢰할 수 있는 접지 전략을 제공합니다.
