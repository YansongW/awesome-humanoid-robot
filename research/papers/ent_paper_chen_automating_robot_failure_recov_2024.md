---
$id: ent_paper_chen_automating_robot_failure_recov_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts
  zh: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts
  ko: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts
summary:
  en: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts (Automating Robot Failure Recovery
    Using Vision-Language Models With Optimized Prompts), is a 2024 large vision-language-action model for robotic manipulation.
  zh: 《Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts》是2024年提出的大型视觉-语言-动作模型，用于机器人操作中的故障恢复。该研究通过优化视觉和文本提示，增强视觉语言模型的空间推理能力，使其能作为黑箱控制器处理运动级位置修正和任务级未知故障。实验表明，优化提示在运动级错误修正中准确率提升65.78%，在Lego组装任务中故障检测、分析和恢复计划成功率分别提高5.8%、5.8%和7.5%。
  ko: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts (Automating Robot Failure Recovery
    Using Vision-Language Models With Optimized Prompts), is a 2024 large vision-language-action model for robotic manipulation.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- automating_robot_failure_recov
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.03966v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts (arXiv)
  url: https://arxiv.org/abs/2409.03966
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts source
  url: https://doi.org/10.48550/arXiv.2409.03966
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
当前机器人自主系统在超出预设运行设计域时容易失效，而传统恢复方法依赖人工干预或穷举故障案例，成本高昂。本文利用基础视觉语言模型的常识推理能力，通过优化视觉提示中的关键元素、在文本提示中突出这些元素，并分解故障检测与控制生成的推理过程，来克服VLM在空间推理上的局限。实验证明，优化后的提示不仅显著优于未优化的VLM，还超越了预训练的视觉-语言-动作模型，在Lego组装等复杂任务中有效处理未知故障。

## 核心内容
### 方法
- **提示优化策略**：首先识别视觉提示中的关键视觉元素（如物体位置、姿态），然后在文本提示中明确描述这些元素以引导查询，最后将故障检测与控制生成的推理过程分解为多个子步骤。
- **黑箱控制器**：将VLM作为运动级位置修正和任务级恢复的控制器，无需重新训练模型，仅通过优化输入提示来提升空间推理能力。

### 实验设置
- **任务**：运动级位置修正（纠正机械臂末端执行器的位置误差）和任务级故障恢复（Lego组装中的未知错误，如零件错位、缺失）。
- **对比基准**：未优化的VLM、预训练的Vision-Language-Action Model（如RT-2）。
- **评估指标**：运动级任务使用位置修正准确率；任务级任务使用故障检测率、问题分析准确率和恢复计划成功率。

### 关键结果
- **运动级位置修正**：优化提示的VLM准确率比未优化VLM提升65.78%，且显著优于预训练的VLA模型。
- **任务级故障恢复**：在Lego组装任务中，优化提示使VLM的故障检测成功率提升5.8%，问题分析成功率提升5.8%，恢复计划生成成功率提升7.5%。
- **泛化性**：优化提示在多种未知故障场景中均有效，无需针对每种故障单独设计恢复策略。

### 结论
本文证明，通过精心设计的视觉和文本提示优化，可以显著增强VLM在机器人故障恢复中的空间推理能力，为自动化恢复提供了一种低成本、高泛化性的解决方案。未来工作可探索更复杂的提示优化策略或结合其他感知模态。

## Overview
Current robot autonomy struggles to operate beyond the assumed Operational Design Domain (ODD), the specific set of conditions and environments in which the system is designed to function, while the real-world is rife with uncertainties that may lead to failures. Automating recovery remains a significant challenge. Traditional methods often rely on human intervention to manually address failures or require exhaustive enumeration of failure cases and the design of specific recovery policies for each scenario, both of which are labor-intensive. Foundational Vision-Language Models (VLMs), which demonstrate remarkable common-sense generalization and reasoning capabilities, have broader, potentially unbounded ODDs. However, limitations in spatial reasoning continue to be a common challenge for many VLMs when applied to robot control and motion-level error recovery. In this paper, we investigate how optimizing visual and text prompts can enhance the spatial reasoning of VLMs, enabling them to function effectively as black-box controllers for both motion-level position correction and task-level recovery from unknown failures. Specifically, the optimizations include identifying key visual elements in visual prompts, highlighting these elements in text prompts for querying, and decomposing the reasoning process for failure detection and control generation. In experiments, prompt optimizations significantly outperform pre-trained Vision-Language-Action Models in correcting motion-level position errors and improve accuracy by 65.78% compared to VLMs with unoptimized prompts. Additionally, for task-level failures, optimized prompts enhanced the success rate by 5.8%, 5.8%, and 7.5% in VLMs' abilities to detect failures, analyze issues, and generate recovery plans, respectively, across a wide range of unknown errors in Lego assembly.

## 개요
현재 로봇 자율성은 시스템이 작동하도록 설계된 특정 조건 및 환경 집합인 가정된 운용 설계 영역(ODD)을 벗어나 작동하는 데 어려움을 겪고 있으며, 실제 세계는 실패로 이어질 수 있는 불확실성으로 가득 차 있습니다. 복구 자동화는 여전히 중요한 과제로 남아 있습니다. 전통적인 방법은 종종 인간의 개입에 의존하여 수동으로 실패를 처리하거나, 실패 사례를 철저히 열거하고 각 시나리오에 대한 특정 복구 정책을 설계해야 하며, 이 두 가지 모두 노동 집약적입니다. 놀라운 상식 일반화 및 추론 능력을 보여주는 기초 시각-언어 모델(VLM)은 더 넓고 잠재적으로 무한한 ODD를 가지고 있습니다. 그러나 공간 추론의 한계는 로봇 제어 및 동작 수준 오류 복구에 적용될 때 많은 VLM에서 여전히 공통적인 과제로 남아 있습니다. 본 논문에서는 시각 및 텍스트 프롬프트를 최적화하여 VLM의 공간 추론을 향상시키고, 이를 통해 동작 수준 위치 보정과 알려지지 않은 실패로부터의 작업 수준 복구 모두에서 블랙박스 컨트롤러로 효과적으로 기능할 수 있도록 하는 방법을 조사합니다. 구체적으로, 최적화에는 시각 프롬프트에서 핵심 시각 요소 식별, 쿼리를 위해 텍스트 프롬프트에서 이러한 요소 강조, 그리고 실패 감지 및 제어 생성을 위한 추론 과정 분해가 포함됩니다. 실험에서 프롬프트 최적화는 동작 수준 위치 오류 보정에서 사전 훈련된 시각-언어-행동 모델을 크게 능가하며, 최적화되지 않은 프롬프트를 사용한 VLM에 비해 정확도를 65.78% 향상시켰습니다. 또한, 작업 수준 실패의 경우, 최적화된 프롬프트는 레고 조립의 다양한 알려지지 않은 오류에 걸쳐 VLM의 실패 감지, 문제 분석 및 복구 계획 생성 능력에서 각각 5.8%, 5.8% 및 7.5%의 성공률 향상을 보였습니다.

## 핵심 내용
현재 로봇 자율성은 시스템이 작동하도록 설계된 특정 조건 및 환경 집합인 가정된 운용 설계 영역(ODD)을 벗어나 작동하는 데 어려움을 겪고 있으며, 실제 세계는 실패로 이어질 수 있는 불확실성으로 가득 차 있습니다. 복구 자동화는 여전히 중요한 과제로 남아 있습니다. 전통적인 방법은 종종 인간의 개입에 의존하여 수동으로 실패를 처리하거나, 실패 사례를 철저히 열거하고 각 시나리오에 대한 특정 복구 정책을 설계해야 하며, 이 두 가지 모두 노동 집약적입니다. 놀라운 상식 일반화 및 추론 능력을 보여주는 기초 시각-언어 모델(VLM)은 더 넓고 잠재적으로 무한한 ODD를 가지고 있습니다. 그러나 공간 추론의 한계는 로봇 제어 및 동작 수준 오류 복구에 적용될 때 많은 VLM에서 여전히 공통적인 과제로 남아 있습니다. 본 논문에서는 시각 및 텍스트 프롬프트를 최적화하여 VLM의 공간 추론을 향상시키고, 이를 통해 동작 수준 위치 보정과 알려지지 않은 실패로부터의 작업 수준 복구 모두에서 블랙박스 컨트롤러로 효과적으로 기능할 수 있도록 하는 방법을 조사합니다. 구체적으로, 최적화에는 시각 프롬프트에서 핵심 시각 요소 식별, 쿼리를 위해 텍스트 프롬프트에서 이러한 요소 강조, 그리고 실패 감지 및 제어 생성을 위한 추론 과정 분해가 포함됩니다. 실험에서 프롬프트 최적화는 동작 수준 위치 오류 보정에서 사전 훈련된 시각-언어-행동 모델을 크게 능가하며, 최적화되지 않은 프롬프트를 사용한 VLM에 비해 정확도를 65.78% 향상시켰습니다. 또한, 작업 수준 실패의 경우, 최적화된 프롬프트는 레고 조립의 다양한 알려지지 않은 오류에 걸쳐 VLM의 실패 감지, 문제 분석 및 복구 계획 생성 능력에서 각각 5.8%, 5.8% 및 7.5%의 성공률 향상을 보였습니다.

## 参考
- http://arxiv.org/abs/2409.03966v1
