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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.07962v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (636 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.07962v1

## 개요
현재 비전-언어-동작(VLA) 모델은 토크와 같은 힘 신호를 통합하는 능력이 부족하며, 이는 폐루프 제어와 작업 완료 평가에 중요합니다. TA-VLA는 설계 공간을 체계적으로 연구하여 토크 어댑터를 인코더보다 디코더에 삽입하는 것이 더 효과적임을 발견했으며, 자율주행의 결합 예측 및 계획 패러다임에서 영감을 얻어 토크 예측을 보조 출력으로 제안함으로써 모델이 물리적 상호작용의 내부 표현을 구축하도록 장려합니다. 광범위한 정량적 및 정성적 실험이 접촉이 많은 조작 벤치마크에서 이러한 발견을 검증합니다.

## 핵심 내용
### 방법
TA-VLA는 기존 VLA 아키텍처에 토크 신호를 통합하는 것을 목표로 하며, 설계 공간 탐색은 두 가지 핵심 전략에 초점을 맞춥니다:
- **토크 어댑터 위치**: 토크 어댑터를 인코더에 삽입하는 것과 디코더에 삽입하는 효과를 비교했으며, 디코더 측 삽입이 항상 더 우수함을 발견했습니다.
- **보조 출력 예측**: 자율주행의 결합 예측 및 계획 패러다임에서 차용하여 토크 예측을 보조 작업으로 사용하며, 이는 모델이 더 물리적인 상호작용 역학의 내부 표현을 학습하도록 유도합니다.

### 실험 설정
- **벤치마크**: 접촉이 많은 조작 벤치마크에서 평가되었으며, 정량적 및 정성적 실험을 포함합니다.
- **비교**: 다양한 토크 통합 전략을 체계적으로 비교하여 위의 두 가지 핵심 발견의 유효성을 검증했습니다.

### 주요 결과
- 디코더의 토크 어댑터가 인코더의 어댑터보다 현저히 우수합니다.
- 보조 토크 예측이 성능을 추가로 향상시켜, 모델이 물리적 상호작용의 암묵적 이해를 구축하는 데 도움이 됨을 시사합니다.
- 실험은 다양한 접촉이 많은 작업을 포괄하며, 결과는 제안된 설계 선택을 일관되게 지지합니다.

### 결론
TA-VLA는 체계적인 설계 공간 탐색을 통해 접촉이 많은 조작에서 VLA 모델에 대한 토크 인식의 중요성을 입증하고, 효과적인 통합 전략을 제공하여 미래 로봇 조작에서 물리적 피드백 융합의 기반을 마련합니다.
