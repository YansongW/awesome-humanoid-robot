---
$id: ent_paper_chi_impromptu_vla_open_weights_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models'
  zh: Impromptu VLA
  ko: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models'
summary:
  en: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
  zh: Impromptu VLA 是由清华大学、Bosch Research 等机构在 NIPS25 提出的开源视觉-语言-动作模型，专为自动驾驶非结构化场景设计。其核心贡献是构建了包含 8 万+高质量视频片段的 Impromptu VLA
    Dataset，基于四类非结构化场景分类法，并配备规划导向的问答标注与动作轨迹。实验表明，该数据集显著提升了 VLA 模型在闭环 NeuroNCAP 和开环 nuScenes 轨迹预测上的性能。
  ko: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- impromptu_vla
- large_vla_model
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23757v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (815 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2505.23757
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Impromptu VLA source
  url: https://doi.org/10.48550/arXiv.2505.23757
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 Vision-Language-Action 模型在自动驾驶中面临非结构化边缘场景的挑战，主要原因是缺乏针对性基准。Impromptu VLA 通过构建全新数据集解决了这一问题：从 8 个开源数据集的 200 万+源片段中蒸馏出 8 万+精心筛选的视频片段，并基于四类非结构化场景分类法进行标注。该数据集包含丰富的规划导向问答对和动作轨迹，训练后的 VLA 模型在闭环 NeuroNCAP 评分和碰撞率上取得显著提升，在开环 nuScenes 轨迹预测中达到接近最优的 L2 精度。此外，问答套件还能有效诊断 VLM 在感知、预测和规划方面的能力。

## 核心内容
### 方法概述
Impromptu VLA 的核心创新在于数据驱动的方法，而非模型架构本身。研究团队首先提出了一种针对自动驾驶非结构化场景的四类分类法，涵盖：
- 罕见物体与事件
- 复杂交互行为
- 极端环境条件
- 违反常规的交通模式

### 数据集构建
- **数据来源**：从 8 个开源大规模数据集中收集超过 200 万个原始视频片段
- **筛选过程**：通过自动化管道和人工验证，最终保留 80,000+ 高质量片段
- **标注内容**：每个片段包含规划导向的问答对（Q&A）和精确的动作轨迹

### 实验设置与结果
- **闭环评估**：在 NeuroNCAP 基准上，使用 Impromptu VLA 数据集训练的模型在评分和碰撞率指标上均取得显著提升
- **开环评估**：在 nuScenes 轨迹预测任务中，L2 精度达到接近当前最优水平
- **诊断能力**：问答套件可有效揭示 VLM 在感知、预测和规划三个子任务中的具体表现，帮助定位模型弱点

### 开源资源
代码、数据和模型权重已在 GitHub 上完全开源，地址为 https://github.com/ahydchh/Impromptu-VLA。

## Overview
Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

## 参考
- http://arxiv.org/abs/2505.23757v1

## 개요
기존 Vision-Language-Action 모델은 자율주행에서 비구조적 엣지 시나리오에 직면할 때 어려움을 겪으며, 주요 원인은 맞춤형 벤치마크 부족이다. Impromptu VLA는 새로운 데이터셋 구축을 통해 이 문제를 해결한다: 8개 오픈소스 데이터셋의 200만+ 소스 클립에서 8만+ 정제된 비디오 클립을 추출하고, 네 가지 비구조적 시나리오 분류 체계를 기반으로 주석을 달았다. 이 데이터셋은 풍부한 계획 지향 질의응답 쌍과 행동 궤적을 포함하며, 훈련된 VLA 모델은 폐루프 NeuroNCAP 점수와 충돌률에서 현저한 개선을 보였고, 개루프 nuScenes 궤적 예측에서 최적에 근접한 L2 정밀도를 달성했다. 또한, 질의응답 스위트는 VLM의 인식, 예측, 계획 능력을 효과적으로 진단할 수 있다.

## 핵심 내용
### 방법 개요
Impromptu VLA의 핵심 혁신은 모델 아키텍처가 아닌 데이터 중심 접근 방식에 있다. 연구팀은 먼저 자율주행 비구조적 시나리오를 위한 네 가지 분류 체계를 제안했으며, 이는 다음을 포함한다:
- 희귀 객체 및 이벤트
- 복잡한 상호작용 행동
- 극한 환경 조건
- 일반적 교통 패턴 위반

### 데이터셋 구축
- **데이터 출처**: 8개 오픈소스 대규모 데이터셋에서 200만 개 이상의 원본 비디오 클립 수집
- **선별 과정**: 자동화 파이프라인과 수동 검증을 통해 최종적으로 80,000+ 고품질 클립 유지
- **주석 내용**: 각 클립은 계획 지향 질의응답 쌍(Q&A)과 정밀한 행동 궤적 포함

### 실험 설정 및 결과
- **폐루프 평가**: NeuroNCAP 벤치마크에서 Impromptu VLA 데이터셋으로 훈련된 모델은 점수와 충돌률 지표 모두에서 현저한 개선을 보임
- **개루프 평가**: nuScenes 궤적 예측 작업에서 L2 정밀도가 현재 최적 수준에 근접
- **진단 능력**: 질의응답 스위트는 VLM의 인식, 예측, 계획 세 가지 하위 작업에서의 구체적 성능을 효과적으로 드러내며 모델 약점 파악에 도움

### 오픈소스 리소스
코드, 데이터, 모델 가중치는 GitHub에서 완전히 오픈소스로 제공되며, 주소는 https://github.com/ahydchh/Impromptu-VLA 이다.
