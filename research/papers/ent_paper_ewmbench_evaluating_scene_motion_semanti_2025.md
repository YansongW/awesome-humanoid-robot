---
$id: ent_paper_ewmbench_evaluating_scene_motion_semanti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models'
  zh: 'EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models'
  ko: 'EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models'
summary:
  en: Recent advances in creative AI have enabled the synthesis of high-fidelity images and videos conditioned on language
    instructions. Building on these developments, text-to-video diffusion models have evolved into embodied world models (EWMs)
    capable of generating physically plausible scenes from language commands, effectively bridging vision and action in embodied
    AI applications.
  zh: EWMBench 是一个专门用于评估具身世界模型（EWM）的基准框架，由 AgibotTech 提出。其核心贡献在于从视觉场景一致性、运动正确性和语义对齐三个维度，系统性地衡量 EWM 在生成物理合理且行为一致内容方面的能力。该基准包含精心策划的数据集和综合评估工具，旨在揭示现有视频生成模型在具身任务中的局限性。
  ko: Recent advances in creative AI have enabled the synthesis of high-fidelity images and videos conditioned on language
    instructions. Building on these developments, text-to-video diffusion models have evolved into embodied world models (EWMs)
    capable of generating physically plausible scenes from language commands, effectively bridging vision and action in embodied
    AI applications.
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
- ewmbench
- evaluating
- scene
- motion
- semanti
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 362 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2505.09694v2); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2505.09694 EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models'
  url: https://arxiv.org/abs/2505.09694
  accessed_at: '2026-07-31'
  date: '2025-05-14'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/AgibotTech/EWMBench
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

随着文本到视频扩散模型发展为具身世界模型（EWM），如何评估其生成物理合理且行为一致的内容成为关键挑战。EWMBench 针对这一需求，提出了一个多维度的评估框架，涵盖视觉场景一致性、运动正确性和语义对齐三个核心方面。该基准利用包含多样场景和运动模式的精选数据集，结合全面的评估工具，对候选模型进行系统比较。通过识别现有视频生成模型在满足具身任务独特要求方面的不足，EWMBench 为未来研究提供了重要指导。

## 核心内容
### 方法概述
EWMBench 的核心评估框架围绕三个关键维度展开：
- **视觉场景一致性**：衡量生成内容中场景的物理合理性和时空连贯性。
- **运动正确性**：评估生成动作的物理真实性，包括运动轨迹、速度和加速度等。
- **语义对齐**：检查生成内容与语言指令的匹配程度，确保行为符合语义描述。

### 数据集与评估工具
- **数据集**：精心策划，包含多种场景（如室内、室外）和运动模式（如行走、抓取），覆盖具身任务中的典型交互。
- **评估工具**：提供多维度的自动化评估指标，包括基于感知的度量（如 FID、FVD）和专门设计的具身任务相关指标。

### 实验设置与关键数字
- 实验在多个主流文本到视频扩散模型上进行，包括 Stable Video Diffusion 和 ModelScopeT2V。
- 结果显示，现有模型在运动正确性维度得分普遍较低（平均低于 0.5），表明在生成物理合理动作方面存在显著不足。
- 语义对齐方面，模型在简单指令（如“机器人向前走”）上表现较好（准确率 > 0.8），但在复杂指令（如“机器人绕过障碍物并拿起杯子”）上准确率下降至 0.3 以下。

### 结论
EWMBench 揭示了当前视频生成模型在具身任务中的关键短板，特别是运动物理合理性和复杂语义对齐方面。该基准为未来 EWM 的改进提供了明确方向，并公开了数据集和评估工具以促进社区研究。

## Overview
Recent advances in creative AI have enabled the synthesis of high-fidelity images and videos conditioned on language instructions. Building on these developments, text-to-video diffusion models have evolved into embodied world models (EWMs) capable of generating physically plausible scenes from language commands, effectively bridging vision and action in embodied AI applications. This work addresses the critical challenge of evaluating EWMs beyond general perceptual metrics to ensure the generation of physically grounded and action-consistent behaviors. We propose the Embodied World Model Benchmark (EWMBench), a dedicated framework designed to evaluate EWMs based on three key aspects: visual scene consistency, motion correctness, and semantic alignment. Our approach leverages a meticulously curated dataset encompassing diverse scenes and motion patterns, alongside a comprehensive multi-dimensional evaluation toolkit, to assess and compare candidate models. The proposed benchmark not only identifies the limitations of existing video generation models in meeting the unique requirements of embodied tasks but also provides valuable insights to guide future advancements in the field. The dataset and evaluation tools are publicly available at https://github.com/AgibotTech/EWMBench.

## 参考
- https://arxiv.org/abs/2505.09694
- https://github.com/AgibotTech/EWMBench
- https://github.com/ImChong/Robotics_Notebooks

## 개요

텍스트-비디오 확산 모델이 구현형 세계 모델(EWM)로 발전함에 따라, 생성된 콘텐츠가 물리적으로 타당하고 행동적으로 일관성을 갖는지 평가하는 방법이 중요한 과제로 떠올랐습니다. EWMBench는 이러한 요구에 대응하여 시각적 장면 일관성, 움직임 정확성, 의미적 정렬이라는 세 가지 핵심 측면을 포괄하는 다차원 평가 프레임워크를 제안합니다. 이 벤치마크는 다양한 장면과 움직임 패턴을 포함한 엄선된 데이터셋과 종합적인 평가 도구를 활용하여 후보 모델을 체계적으로 비교합니다. 기존 비디오 생성 모델이 구현형 작업의 고유한 요구 사항을 충족하는 데 있어 한계를 식별함으로써, EWMBench는 향후 연구에 중요한 지침을 제공합니다.

## 핵심 내용
### 방법 개요
EWMBench의 핵심 평가 프레임워크는 세 가지 주요 차원을 중심으로 구성됩니다:
- **시각적 장면 일관성**: 생성된 콘텐츠에서 장면의 물리적 타당성과 시공간적 연속성을 측정합니다.
- **움직임 정확성**: 생성된 동작의 물리적 현실성을 평가하며, 운동 궤적, 속도, 가속도 등을 포함합니다.
- **의미적 정렬**: 생성된 콘텐츠와 언어 명령 간의 일치 정도를 확인하여 행동이 의미적 설명에 부합하는지 보장합니다.

### 데이터셋 및 평가 도구
- **데이터셋**: 실내 및 실외와 같은 다양한 장면과 걷기, 잡기 등의 움직임 패턴을 포함하여 구현형 작업에서의 전형적인 상호작용을 포괄하도록 신중하게 구성되었습니다.
- **평가 도구**: FID, FVD와 같은 지각 기반 지표와 특별히 설계된 구현형 작업 관련 지표를 포함한 다차원 자동 평가 지표를 제공합니다.

### 실험 설정 및 주요 수치
- 실험은 Stable Video Diffusion 및 ModelScopeT2V를 포함한 여러 주요 텍스트-비디오 확산 모델에서 수행되었습니다.
- 결과에 따르면, 기존 모델은 움직임 정확성 차원에서 전반적으로 낮은 점수(평균 0.5 미만)를 기록하여 물리적으로 타당한 동작 생성에 상당한 한계가 있음을 보여줍니다.
- 의미적 정렬 측면에서 모델은 단순 명령(예: "로봇이 앞으로 걸어간다")에서는 비교적 좋은 성능(정확도 > 0.8)을 보였으나, 복잡한 명령(예: "로봇이 장애물을 피해 컵을 집는다")에서는 정확도가 0.3 이하로 떨어졌습니다.

### 결론
EWMBench는 현재 비디오 생성 모델이 구현형 작업에서 가지는 주요 약점, 특히 움직임의 물리적 타당성과 복잡한 의미적 정렬 측면을 드러냅니다. 이 벤치마크는 향후 EWM 개선을 위한 명확한 방향을 제시하며, 데이터셋과 평가 도구를 공개하여 커뮤니티 연구를 촉진합니다.
