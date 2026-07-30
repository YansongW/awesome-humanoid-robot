---
$id: ent_paper_zhang_ta_vla_elucidating_the_design_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models'
  zh: TA-VLA
  ko: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models'
summary:
  en: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (TA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Academy of Artificial Intelligence, BAAI, Institute for AI Industry
    Research (AIR), Tsinghua Univeristy, Nanyang Technological University, and published at CoRL25.'
  zh: TA-VLA 是由北京人工智能研究院（BAAI）、清华大学 AIR、南洋理工大学等机构在 CoRL25 上发表的 2025 年大型视觉-语言-动作模型，专注于机器人操作。其核心贡献是系统探索了将扭矩信号融入 VLA 模型的设计空间，并提出在解码器中引入扭矩适配器以及将扭矩预测作为辅助输出，显著提升了接触丰富操作任务的性能。
  ko: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (TA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Academy of Artificial Intelligence, BAAI, Institute for AI Industry
    Research (AIR), Tsinghua Univeristy, Nanyang Technological University, and published at CoRL25.'
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
- robotic_manipulation
- ta_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.07962v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2509.07962
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TA-VLA source
  url: https://doi.org/10.48550/arXiv.2509.07962
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前视觉-语言-动作（VLA）模型缺乏整合扭矩等力信号的能力，而这对于闭环控制和任务完成评估至关重要。TA-VLA 通过系统研究设计空间，发现将扭矩适配器插入解码器比插入编码器效果更好，并且受自动驾驶中联合预测与规划范式的启发，提出将扭矩预测作为辅助输出，从而鼓励模型建立物理交互的内部表征。大量定量与定性实验在接触丰富操作基准上验证了这些发现。

## 核心内容
### 方法
TA-VLA 旨在将扭矩信号融入现有 VLA 架构，其设计空间探索聚焦于两个关键策略：
- **扭矩适配器位置**：比较了将扭矩适配器插入编码器与解码器的效果，发现解码器端插入始终更优。
- **辅助输出预测**：借鉴自动驾驶中的联合预测与规划范式，将扭矩预测作为辅助任务，这促使模型学习更物理化的交互动力学内部表征。

### 实验设置
- **基准**：在接触丰富的操作基准上进行评估，包括定量和定性实验。
- **对比**：系统比较了不同扭矩集成策略，验证了上述两个关键发现的有效性。

### 关键结果
- 解码器中的扭矩适配器显著优于编码器中的适配器。
- 辅助扭矩预测进一步提升了性能，表明其有助于模型建立物理交互的隐式理解。
- 实验覆盖了多种接触丰富任务，结果一致支持所提出的设计选择。

### 结论
TA-VLA 通过系统设计空间探索，证明了扭矩感知对 VLA 模型在接触丰富操作中的重要性，并提供了有效的集成策略，为未来机器人操作中的物理反馈融合奠定了基础。

## Overview
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder.Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## Overview
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder. Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## Content
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder. Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## 개요
많은 로봇 조작 작업은 작업이 성공적으로 완료되었는지 평가하고 폐쇄 루프 제어를 가능하게 하기 위해 토크와 같은 힘 신호를 감지하고 반응해야 합니다. 그러나 현재의 Vision-Language-Action(VLA) 모델은 이러한 미묘한 물리적 피드백을 통합하는 능력이 부족합니다. 본 연구에서는 Torque-aware VLA 모델을 탐구하며, 기존 VLA 아키텍처에 토크 신호를 통합하기 위한 설계 공간을 체계적으로 연구하여 이러한 격차를 해소하고자 합니다. 우리는 여러 전략을 식별하고 평가하여 세 가지 주요 발견을 도출했습니다. 첫째, 디코더에 토크 어댑터를 도입하는 것이 인코더에 삽입하는 것보다 일관되게 더 나은 성능을 보였습니다. 셋째, 자율 주행에서의 공동 예측 및 계획 패러다임에서 영감을 받아, 우리는 보조 출력으로 토크를 예측하는 것을 제안하며, 이는 성능을 더욱 향상시킵니다. 이 전략은 모델이 상호작용 역학에 대한 물리적으로 기반한 내부 표현을 구축하도록 장려합니다. 접촉이 많은 조작 벤치마크에 걸친 광범위한 정량적 및 정성적 실험을 통해 우리의 발견을 검증했습니다.

## 핵심 내용
많은 로봇 조작 작업은 작업이 성공적으로 완료되었는지 평가하고 폐쇄 루프 제어를 가능하게 하기 위해 토크와 같은 힘 신호를 감지하고 반응해야 합니다. 그러나 현재의 Vision-Language-Action(VLA) 모델은 이러한 미묘한 물리적 피드백을 통합하는 능력이 부족합니다. 본 연구에서는 Torque-aware VLA 모델을 탐구하며, 기존 VLA 아키텍처에 토크 신호를 통합하기 위한 설계 공간을 체계적으로 연구하여 이러한 격차를 해소하고자 합니다. 우리는 여러 전략을 식별하고 평가하여 세 가지 주요 발견을 도출했습니다. 첫째, 디코더에 토크 어댑터를 도입하는 것이 인코더에 삽입하는 것보다 일관되게 더 나은 성능을 보였습니다. 셋째, 자율 주행에서의 공동 예측 및 계획 패러다임에서 영감을 받아, 우리는 보조 출력으로 토크를 예측하는 것을 제안하며, 이는 성능을 더욱 향상시킵니다. 이 전략은 모델이 상호작용 역학에 대한 물리적으로 기반한 내부 표현을 구축하도록 장려합니다. 접촉이 많은 조작 벤치마크에 걸친 광범위한 정량적 및 정성적 실험을 통해 우리의 발견을 검증했습니다.

## 参考
- http://arxiv.org/abs/2509.07962v1
