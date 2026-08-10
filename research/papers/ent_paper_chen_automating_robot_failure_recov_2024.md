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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.03966v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (868 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2409.03966v1

## 개요
현재 로봇 자율 시스템은 사전에 정의된 운영 설계 영역을 벗어날 때 쉽게 실패하며, 기존 복구 방법은 수동 개입이나 모든 고장 사례를 나열하는 방식에 의존하여 비용이 높습니다. 본 논문은 기초 비전-언어 모델의 상식 추론 능력을 활용하여, 시각 프롬프트의 핵심 요소를 최적화하고, 텍스트 프롬프트에서 이러한 요소를 강조하며, 고장 감지와 제어 생성을 위한 추론 과정을 분해함으로써 VLM의 공간 추론 한계를 극복합니다. 실험 결과, 최적화된 프롬프트는 최적화되지 않은 VLM보다 현저히 우수할 뿐만 아니라, 사전 훈련된 비전-언어-행동 모델을 능가하며, Lego 조립과 같은 복잡한 작업에서 알려지지 않은 고장을 효과적으로 처리합니다.

## 핵심 내용
### 방법
- **프롬프트 최적화 전략**: 먼저 시각 프롬프트에서 핵심 시각 요소(예: 객체 위치, 자세)를 식별한 다음, 텍스트 프롬프트에서 이러한 요소를 명확히 설명하여 쿼리를 안내하고, 마지막으로 고장 감지와 제어 생성을 위한 추론 과정을 여러 하위 단계로 분해합니다.
- **블랙박스 컨트롤러**: VLM을 운동 수준 위치 보정 및 작업 수준 복구를 위한 컨트롤러로 사용하며, 모델을 재훈련할 필요 없이 입력 프롬프트 최적화만으로 공간 추론 능력을 향상시킵니다.

### 실험 설정
- **작업**: 운동 수준 위치 보정(로봇 팔 엔드 이펙터의 위치 오류 수정) 및 작업 수준 고장 복구(Lego 조립 중 알려지지 않은 오류, 예: 부품 정렬 불량, 누락).
- **비교 기준**: 최적화되지 않은 VLM, 사전 훈련된 Vision-Language-Action Model(예: RT-2).
- **평가 지표**: 운동 수준 작업은 위치 보정 정확도를 사용하고, 작업 수준 작업은 고장 감지율, 문제 분석 정확도, 복구 계획 성공률을 사용합니다.

### 주요 결과
- **운동 수준 위치 보정**: 최적화된 프롬프트의 VLM 정확도는 최적화되지 않은 VLM보다 65.78% 향상되었으며, 사전 훈련된 VLA 모델보다 현저히 우수합니다.
- **작업 수준 고장 복구**: Lego 조립 작업에서 최적화된 프롬프트는 VLM의 고장 감지 성공률을 5.8%, 문제 분석 성공률을 5.8%, 복구 계획 생성 성공률을 7.5% 향상시킵니다.
- **일반화**: 최적화된 프롬프트는 다양한 알려지지 않은 고장 시나리오에서 효과적이며, 각 고장 유형에 대해 개별 복구 전략을 설계할 필요가 없습니다.

### 결론
본 논문은 정교하게 설계된 시각 및 텍스트 프롬프트 최적화를 통해 VLM의 로봇 고장 복구에서의 공간 추론 능력을 현저히 강화할 수 있음을 증명하며, 자동화된 복구를 위한 저비용, 높은 일반화 솔루션을 제공합니다. 향후 연구는 더 복잡한 프롬프트 최적화 전략이나 다른 지각 양식의 통합을 탐구할 수 있습니다.
