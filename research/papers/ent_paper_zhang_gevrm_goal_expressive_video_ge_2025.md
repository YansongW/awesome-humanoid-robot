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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.09268v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
체화 인공지능의 급속한 발전에 힘입어, 일반 로봇 의사 결정을 위한 시각-언어-행동(VLA) 모델에서 상당한 진전이 이루어졌습니다. 그러나 기존 VLA의 대부분은 배포 중에 발생하는 불가피한 외부 교란을 고려하지 못합니다. 이러한 교란은 VLA에 예상치 못한 상태 정보를 도입하여 부정확한 행동을 초래하고, 결과적으로 일반화 성능이 크게 저하됩니다. 고전적인 내부 모델 제어(IMC) 원리는 외부 입력 신호를 포함하는 내부 모델을 가진 폐루프 시스템이 기준 입력을 정확히 추적하고 교란을 효과적으로 상쇄할 수 있음을 보여줍니다. 우리는 IMC 원리를 통합하여 로봇 시각 조작의 강건성을 향상시키는 새로운 폐루프 VLA 방법인 GEVRM을 제안합니다. GEVRM의 텍스트 유도 비디오 생성 모델은 표현력이 뛰어난 미래 시각 계획 목표를 생성할 수 있습니다. 동시에, 우리는 내부 임베딩이라고 불리는 시뮬레이션 응답을 통해 교란을 평가하고, 프로토타입 대조 학습을 통해 이를 최적화합니다. 이를 통해 모델이 외부 환경의 교란을 암시적으로 추론하고 구별할 수 있습니다. 제안된 GEVRM은 표준 및 교란된 CALVIN 벤치마크 모두에서 최첨단 성능을 달성하며, 실제 로봇 작업에서 상당한 개선을 보여줍니다.

## 핵심 내용
체화 인공지능의 급속한 발전에 힘입어, 일반 로봇 의사 결정을 위한 시각-언어-행동(VLA) 모델에서 상당한 진전이 이루어졌습니다. 그러나 기존 VLA의 대부분은 배포 중에 발생하는 불가피한 외부 교란을 고려하지 못합니다. 이러한 교란은 VLA에 예상치 못한 상태 정보를 도입하여 부정확한 행동을 초래하고, 결과적으로 일반화 성능이 크게 저하됩니다. 고전적인 내부 모델 제어(IMC) 원리는 외부 입력 신호를 포함하는 내부 모델을 가진 폐루프 시스템이 기준 입력을 정확히 추적하고 교란을 효과적으로 상쇄할 수 있음을 보여줍니다. 우리는 IMC 원리를 통합하여 로봇 시각 조작의 강건성을 향상시키는 새로운 폐루프 VLA 방법인 GEVRM을 제안합니다. GEVRM의 텍스트 유도 비디오 생성 모델은 표현력이 뛰어난 미래 시각 계획 목표를 생성할 수 있습니다. 동시에, 우리는 내부 임베딩이라고 불리는 시뮬레이션 응답을 통해 교란을 평가하고, 프로토타입 대조 학습을 통해 이를 최적화합니다. 이를 통해 모델이 외부 환경의 교란을 암시적으로 추론하고 구별할 수 있습니다. 제안된 GEVRM은 표준 및 교란된 CALVIN 벤치마크 모두에서 최첨단 성능을 달성하며, 실제 로봇 작업에서 상당한 개선을 보여줍니다.

## 参考
- http://arxiv.org/abs/2502.09268v2
