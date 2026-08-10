---
$id: ent_paper_pakdamansavoji_improving_robotic_manipulation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Robotic Manipulation Robustness via NICE Scene Surgery
  zh: NICE
  ko: Improving Robotic Manipulation Robustness via NICE Scene Surgery
summary:
  en: Improving Robotic Manipulation Robustness via NICE Scene Surgery (NICE), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Huawei Canada.
  zh: NICE（Naturalistic Inpainting for Context Enhancement）是华为加拿大团队于2025年提出的大型视觉-语言-动作模型，用于提升机器人操作鲁棒性。其核心贡献是通过图像生成和大型语言模型对现有演示数据进行三种编辑操作（物体替换、风格重绘、干扰物移除），在不需额外数据收集或模型训练的情况下，缩小模仿学习中的分布外差距，使操作成功率平均提升11%。
  ko: Improving Robotic Manipulation Robustness via NICE Scene Surgery (NICE), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Huawei Canada.
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
- nice
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22777v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (881 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Improving Robotic Manipulation Robustness via NICE Scene Surgery (arXiv)
  url: https://arxiv.org/abs/2511.22777
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: NICE source
  url: https://doi.org/10.48550/arXiv.2511.22777
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
NICE框架通过利用图像生成模型和大型语言模型，对机器人演示场景进行自然化修补，以增强视觉多样性。它执行三种编辑操作：替换物体、重绘风格和移除干扰物，这些操作保持空间关系不变且不遮挡目标物体，同时确保动作标签一致性。与以往方法不同，NICE无需额外机器人数据收集、模拟器访问或自定义模型训练，可直接应用于现有数据集。在真实场景测试中，NICE将高度杂乱场景中的空间关联预测准确率提升超过20%，在存在不同数量干扰物的环境中，操作任务成功率平均提高11%，同时目标混淆率降低6%，碰撞率降低7%。

## 核心内容
### 方法概述
NICE框架的核心在于利用现有演示数据，通过图像生成和大型语言模型自动生成多样化的场景变体，从而增强训练数据的视觉丰富度。具体操作包括：
- **物体替换**：将场景中的非目标物体替换为其他物体，保持空间布局不变。
- **风格重绘**：改变场景的视觉风格（如纹理、光照），但不影响物体位置和动作标签。
- **干扰物移除**：去除可能分散注意力的非目标物体，减少视觉噪声。

这些操作通过预训练的生成模型和LLM自动执行，无需人工标注或额外数据采集。

### 实验设置
- **下游任务**：使用NICE增强数据微调两个模型：
  - 视觉-语言模型（VLM）用于空间关联预测（affordance prediction）。
  - 视觉-语言-动作模型（VLA）用于物体操作。
- **测试环境**：真实场景，包含不同数量的干扰物（distractors），以评估鲁棒性。

### 关键结果
- **空间关联预测**：在高度杂乱场景中，NICE将预测准确率提升超过20%。
- **操作任务**：在存在干扰物的环境中，成功率平均提高11%。
- **鲁棒性与安全性**：
  - 目标混淆率降低6%。
  - 碰撞率降低7%。

### 结论
NICE通过低成本的数据增强策略，有效缩小了模仿学习中的分布外差距，显著提升了机器人操作在真实复杂环境中的鲁棒性和安全性，且无需额外数据或模型训练，具有高度可扩展性。

## Overview
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets.   Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## Overview
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets. Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## Content
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets. Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## 参考
- http://arxiv.org/abs/2511.22777v1

## 개요
NICE 프레임워크는 이미지 생성 모델과 대규모 언어 모델을 활용하여 로봇 시연 장면을 자연스럽게 패치함으로써 시각적 다양성을 향상시킵니다. 이는 객체 교체, 스타일 재구성, 방해물 제거의 세 가지 편집 작업을 수행하며, 이러한 작업은 공간 관계를 유지하고 대상 객체를 가리지 않으면서 동작 라벨의 일관성을 보장합니다. 기존 방법과 달리 NICE는 추가 로봇 데이터 수집, 시뮬레이터 접근 또는 맞춤형 모델 훈련이 필요 없이 기존 데이터셋에 직접 적용할 수 있습니다. 실제 장면 테스트에서 NICE는 높은 혼잡도 환경에서 공간 연관 예측 정확도를 20% 이상 향상시켰으며, 다양한 수의 방해물이 존재하는 환경에서 조작 작업 성공률을 평균 11% 향상시키고, 대상 객체 혼동률을 6% 낮추고, 충돌률을 7% 낮췄습니다.

## 핵심 내용
### 방법 개요
NICE 프레임워크의 핵심은 기존 시연 데이터를 활용하여 이미지 생성과 대규모 언어 모델을 통해 다양한 장면 변형을 자동으로 생성함으로써 훈련 데이터의 시각적 풍부함을 향상시키는 것입니다. 구체적인 작업은 다음과 같습니다:
- **객체 교체**: 장면 내 비대상 객체를 다른 객체로 교체하며 공간 배치를 유지합니다.
- **스타일 재구성**: 장면의 시각적 스타일(예: 질감, 조명)을 변경하지만 객체 위치와 동작 라벨에는 영향을 미치지 않습니다.
- **방해물 제거**: 주의를 분산시킬 수 있는 비대상 객체를 제거하여 시각적 노이즈를 줄입니다.

이러한 작업은 사전 훈련된 생성 모델과 LLM을 통해 자동으로 실행되며, 수동 주석이나 추가 데이터 수집이 필요 없습니다.

### 실험 설정
- **하위 작업**: NICE 강화 데이터로 두 모델을 미세 조정합니다:
  - 시각-언어 모델(VLM)은 공간 연관 예측(affordance prediction)에 사용됩니다.
  - 시각-언어-행동 모델(VLA)은 객체 조작에 사용됩니다.
- **테스트 환경**: 다양한 수의 방해물(distractors)이 포함된 실제 장면으로, 견고성을 평가합니다.

### 주요 결과
- **공간 연관 예측**: 높은 혼잡도 환경에서 NICE는 예측 정확도를 20% 이상 향상시킵니다.
- **조작 작업**: 방해물이 존재하는 환경에서 성공률이 평균 11% 향상됩니다.
- **견고성 및 안전성**:
  - 대상 객체 혼동률이 6% 감소합니다.
  - 충돌률이 7% 감소합니다.

### 결론
NICE는 저비용 데이터 증강 전략을 통해 모방 학습에서의 분포 외 차이를 효과적으로 줄이며, 추가 데이터나 모델 훈련 없이도 실제 복잡한 환경에서 로봇 조작의 견고성과 안전성을 크게 향상시키며, 높은 확장성을 제공합니다.
