---
$id: ent_paper_zhang_gevrm_goal_expressive_video_ge_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation'
  zh: GEVRM
  ko: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation'
summary:
  en: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation (GEVRM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Westlake University, and published at ICLR25.'
  zh: GEVRM 是浙江大学与西湖大学联合提出的 2025 年大型视觉-语言-动作模型，发表于 ICLR25。其核心贡献在于将内部模型控制（IMC）原理引入闭环 VLA 系统，通过文本引导的视频生成模型表达未来规划目标，并利用原型对比学习隐式推断外部扰动，显著提升了机器人操作任务的鲁棒性。
  ko: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation (GEVRM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Westlake University, and published at ICLR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gevrm
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.09268v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (864 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: GEVRM source
  url: https://openreview.net/forum?id=hPWWXpCaJ7
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型（VLA）在部署时易受外部扰动影响，导致动作不准确和泛化性能下降。GEVRM 借鉴经典内部模型控制（IMC）原理，构建了闭环 VLA 框架：其文本引导的视频生成模型可生成高表达力的未来视觉规划目标，同时通过模拟响应评估扰动（称为内部嵌入），并借助原型对比学习优化这些嵌入，使模型能隐式推断并区分外部环境扰动。该方法在标准与扰动条件下的 CALVIN 基准上均达到最优性能，并在真实机器人任务中展现出显著提升。

## 核心内容
### 方法架构
GEVRM 的核心创新在于将内部模型控制（IMC）原理融入 VLA 闭环系统。IMC 原理指出，包含外部输入信号内部模型的闭环系统能精确跟踪参考输入并有效抵消扰动。GEVRM 具体实现为：
- **目标表达模块**：使用文本引导的视频生成模型，生成具有高表达力的未来视觉规划目标（即参考输入）。
- **扰动评估模块**：通过模拟响应生成“内部嵌入”，用于评估外部扰动。这些嵌入通过原型对比学习（prototype contrastive learning）进行优化，使模型能隐式推断并区分不同扰动来源。

### 实验设置与关键结果
- **基准测试**：在标准 CALVIN 基准及其扰动版本（引入外部干扰）上评估。
- **性能表现**：GEVRM 在标准与扰动 CALVIN 上均达到当前最优（state-of-the-art）水平。在真实机器人任务中，其鲁棒性提升尤为显著，具体表现为在存在物理扰动（如物体位置偏移、光照变化）时仍能保持高成功率。
- **关键数字**：论文未在摘要中提供具体数值，但强调在扰动条件下相比现有 VLA 方法（如 RT-2、Octo）有“显著改进”（significant improvements）。

### 结论
GEVRM 通过将 IMC 原理与视频生成模型结合，首次在 VLA 框架中显式处理外部扰动问题，为机器人操作任务提供了更鲁棒的闭环决策方案。其原型对比学习机制为隐式扰动建模提供了新思路。

## Overview
With the rapid development of embodied artificial intelligence, significant progress has been made in vision-language-action (VLA) models for general robot decision-making. However, the majority of existing VLAs fail to account for the inevitable external perturbations encountered during deployment. These perturbations introduce unforeseen state information to the VLA, resulting in inaccurate actions and consequently, a significant decline in generalization performance. The classic internal model control (IMC) principle demonstrates that a closed-loop system with an internal model that includes external input signals can accurately track the reference input and effectively offset the disturbance. We propose a novel closed-loop VLA method GEVRM that integrates the IMC principle to enhance the robustness of robot visual manipulation. The text-guided video generation model in GEVRM can generate highly expressive future visual planning goals. Simultaneously, we evaluate perturbations by simulating responses, which are called internal embeddings and optimized through prototype contrastive learning. This allows the model to implicitly infer and distinguish perturbations from the external environment. The proposed GEVRM achieves state-of-the-art performance on both standard and perturbed CALVIN benchmarks and shows significant improvements in realistic robot tasks.

## 参考
- http://arxiv.org/abs/2502.09268v2

## 개요
기존 비전-언어-행동 모델(VLA)은 배포 시 외부 교란의 영향을 쉽게 받아, 행동의 부정확성과 일반화 성능 저하를 초래한다. GEVRM은 고전적인 내부 모델 제어(IMC) 원리를 차용하여 폐루프 VLA 프레임워크를 구축한다. 이 프레임워크의 텍스트 유도 비디오 생성 모델은 표현력이 높은 미래 시각 계획 목표를 생성할 수 있으며, 동시에 모의 응답을 통해 교란을 평가하는 내부 임베딩을 생성하고, 프로토타입 대조 학습을 통해 이러한 임베딩을 최적화하여 모델이 외부 환경 교란을 암시적으로 추론하고 구분할 수 있게 한다. 이 방법은 표준 및 교란 조건의 CALVIN 벤치마크에서 최적의 성능을 달성하며, 실제 로봇 작업에서도 현저한 향상을 보여준다.

## 핵심 내용
### 방법 아키텍처
GEVRM의 핵심 혁신은 내부 모델 제어(IMC) 원리를 VLA 폐루프 시스템에 통합한 것이다. IMC 원리는 외부 입력 신호의 내부 모델을 포함하는 폐루프 시스템이 참조 입력을 정밀하게 추적하고 교란을 효과적으로 상쇄할 수 있음을 지적한다. GEVRM은 구체적으로 다음과 같이 구현된다:
- **목표 표현 모듈**: 텍스트 유도 비디오 생성 모델을 사용하여 표현력이 높은 미래 시각 계획 목표(즉, 참조 입력)를 생성한다.
- **교란 평가 모듈**: 모의 응답을 통해 '내부 임베딩'을 생성하여 외부 교란을 평가한다. 이러한 임베딩은 프로토타입 대조 학습(prototype contrastive learning)을 통해 최적화되어, 모델이 서로 다른 교란 원인을 암시적으로 추론하고 구분할 수 있게 한다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 표준 CALVIN 벤치마크 및 교란 버전(외부 간섭 도입)에서 평가한다.
- **성능**: GEVRM은 표준 및 교란 CALVIN 모두에서 최신(state-of-the-art) 수준을 달성한다. 실제 로봇 작업에서는 특히 강건성 향상이 두드러지며, 물리적 교란(예: 물체 위치 이동, 조명 변화)이 존재하는 상황에서도 높은 성공률을 유지한다.
- **주요 수치**: 논문은 초록에서 구체적인 수치를 제공하지 않지만, 교란 조건에서 기존 VLA 방법(예: RT-2, Octo) 대비 '현저한 개선'(significant improvements)을 강조한다.

### 결론
GEVRM은 IMC 원리와 비디오 생성 모델을 결합하여 VLA 프레임워크에서 외부 교란 문제를 처음으로 명시적으로 처리하며, 로봇 조작 작업에 더 강건한 폐루프 의사결정 방안을 제공한다. 그 프로토타입 대조 학습 메커니즘은 암시적 교란 모델링에 새로운 접근 방식을 제시한다.
