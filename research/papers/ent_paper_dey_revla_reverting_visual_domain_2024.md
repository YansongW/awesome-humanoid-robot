---
$id: ent_paper_dey_revla_reverting_visual_domain_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models'
  zh: ReVLA
  ko: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models'
summary:
  en: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models (ReVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, and published at ICRA 2024.'
  zh: ReVLA 是 INSAIT 与索非亚大学于 ICRA 2024 提出的视觉-语言-动作模型，旨在解决机器人基础模型在视觉域外场景中的泛化失效问题。其核心贡献在于通过模型合并的渐进式骨干网络逆转方法，恢复 OpenVLA 中因微调而遗忘的视觉能力，在抓取与提升任务上分别提升
    77% 与 66%。
  ko: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models (ReVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, and published at ICRA 2024.'
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
- revla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.15250v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (987 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: ReVLA source
  url: https://doi.org/10.1109/ICRA55743.2025.11128823
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该研究首先系统评估了三种现有机器人基础模型在视觉域外场景下的表现，发现它们均因训练数据多样性不足或灾难性遗忘而缺乏鲁棒性。针对 OpenVLA 中 DINO-v2 视觉骨干在深度回归任务上的完全失效，作者提出一种基于模型合并的渐进式骨干逆转策略，在不破坏动作学习能力的前提下恢复预训练视觉特征。最终得到的 ReVLA 模型在视觉域外抓取与提升任务中显著超越原版 OpenVLA，验证了该方法对视觉域限制的有效逆转。

## 核心内容
### 研究动机与问题
- 现有机器人基础模型（如 RT-2、Octo、OpenVLA）在训练数据覆盖的视觉场景中表现优异，但面对光照、背景、物体纹理等域外变化时性能骤降。
- 分析指出，视觉域限制源于两方面：训练数据中视觉变化不足，以及微调过程中预训练视觉骨干（如 DINO-v2）发生灾难性遗忘。

### 方法：渐进式骨干逆转（Gradual Backbone Reversal）
- 核心思想：通过模型合并技术，在保持 OpenVLA 已习得的动作能力的同时，逐步恢复其视觉骨干的原始泛化能力。
- 具体实现：
  - 将 OpenVLA 的视觉编码器（SigLIP + DINO-v2）与原始预训练权重进行线性插值。
  - 插值系数从 0（完全使用微调后权重）逐渐过渡到 1（完全使用预训练权重），形成一系列中间模型。
  - 在验证集上选择最佳插值系数，平衡视觉泛化与动作精度。

### 实验设置与关键结果
- 评估基准：自定义视觉域外测试集，包含不同光照、背景、物体颜色与纹理的抓取（grasping）与提升（lifting）任务。
- 对比模型：OpenVLA（基线）、RT-2、Octo。
- 关键数字：
  - ReVLA 在视觉域外抓取任务上比 OpenVLA 提升 77%，在提升任务上提升 66%。
  - 在域内任务中，ReVLA 性能与 OpenVLA 持平，未出现退化。
  - 消融实验表明，渐进式逆转（多步插值）优于直接使用预训练权重（一步逆转），后者会导致动作能力崩溃。

### 结论
- 视觉灾难性遗忘是限制机器人基础模型域外泛化的关键瓶颈。
- 基于模型合并的渐进式骨干逆转是一种轻量级、无需额外训练的有效解决方案。
- 模型权重与完整评估视频已开源，详见 ReVLA 项目页面。

## Overview
Recent progress in large language models and access to large-scale robotic datasets has sparked a paradigm shift in robotics models transforming them into generalists able to adapt to various tasks, scenes, and robot modalities. A large step for the community are open Vision Language Action models which showcase strong performance in a wide variety of tasks. In this work, we study the visual generalization capabilities of three existing robotic foundation models, and propose a corresponding evaluation framework. Our study shows that the existing models do not exhibit robustness to visual out-of-domain scenarios. This is potentially caused by limited variations in the training data and/or catastrophic forgetting, leading to domain limitations in the vision foundation models. We further explore OpenVLA, which uses two pre-trained vision foundation models and is, therefore, expected to generalize to out-of-domain experiments. However, we showcase catastrophic forgetting by DINO-v2 in OpenVLA through its failure to fulfill the task of depth regression. To overcome the aforementioned issue of visual catastrophic forgetting, we propose a gradual backbone reversal approach founded on model merging. This enables OpenVLA -- which requires the adaptation of the visual backbones during initial training -- to regain its visual generalization ability. Regaining this capability enables our ReVLA model to improve over OpenVLA by a factor of 77\% and 66\% for grasping and lifting in visual OOD tasks. Comprehensive evaluations, episode rollouts and model weights are available on the ReVLA Page

## Overview
Recent progress in large language models and access to large-scale robotic datasets has sparked a paradigm shift in robotics models, transforming them into generalists able to adapt to various tasks, scenes, and robot modalities. A major step for the community is the emergence of open Vision-Language-Action models, which demonstrate strong performance across a wide variety of tasks. In this work, we study the visual generalization capabilities of three existing robotic foundation models and propose a corresponding evaluation framework. Our study shows that these existing models do not exhibit robustness to visual out-of-domain scenarios. This is potentially caused by limited variations in the training data and/or catastrophic forgetting, leading to domain limitations in the vision foundation models. We further explore OpenVLA, which uses two pre-trained vision foundation models and is therefore expected to generalize to out-of-domain experiments. However, we demonstrate catastrophic forgetting by DINO-v2 in OpenVLA through its failure to perform depth regression. To address the aforementioned issue of visual catastrophic forgetting, we propose a gradual backbone reversal approach based on model merging. This enables OpenVLA—which requires adaptation of the visual backbones during initial training—to regain its visual generalization ability. Regaining this capability allows our ReVLA model to improve over OpenVLA by 77% and 66% for grasping and lifting in visual OOD tasks. Comprehensive evaluations, episode rollouts, and model weights are available on the ReVLA Page.

## Content
Recent progress in large language models and access to large-scale robotic datasets has sparked a paradigm shift in robotics models, transforming them into generalists able to adapt to various tasks, scenes, and robot modalities. A major step for the community is the emergence of open Vision-Language-Action models, which demonstrate strong performance across a wide variety of tasks. In this work, we study the visual generalization capabilities of three existing robotic foundation models and propose a corresponding evaluation framework. Our study shows that these existing models do not exhibit robustness to visual out-of-domain scenarios. This is potentially caused by limited variations in the training data and/or catastrophic forgetting, leading to domain limitations in the vision foundation models. We further explore OpenVLA, which uses two pre-trained vision foundation models and is therefore expected to generalize to out-of-domain experiments. However, we demonstrate catastrophic forgetting by DINO-v2 in OpenVLA through its failure to perform depth regression. To address the aforementioned issue of visual catastrophic forgetting, we propose a gradual backbone reversal approach based on model merging. This enables OpenVLA—which requires adaptation of the visual backbones during initial training—to regain its visual generalization ability. Regaining this capability allows our ReVLA model to improve over OpenVLA by 77% and 66% for grasping and lifting in visual OOD tasks. Comprehensive evaluations, episode rollouts, and model weights are available on the ReVLA Page.

## 参考
- http://arxiv.org/abs/2409.15250v3

## 개요
이 연구는 먼저 세 가지 기존 로봇 기반 모델의 시각적 도메인 외부(out-of-domain) 시나리오에서의 성능을 체계적으로 평가했으며, 훈련 데이터 다양성 부족이나 파괴적 망각(catastrophic forgetting)으로 인해 모두 견고성이 부족함을 발견했습니다. OpenVLA의 DINO-v2 시각 백본(visual backbone)이 깊이 회귀 작업에서 완전히 실패하는 문제를 해결하기 위해, 저자들은 모델 병합(model merging) 기반의 점진적 백본 역전(gradual backbone reversal) 전략을 제안하여, 행동 학습 능력을 손상시키지 않으면서 사전 훈련된 시각 특징을 복원합니다. 최종적으로 얻어진 ReVLA 모델은 시각적 도메인 외부 파지(grasping) 및 들어올리기(lifting) 작업에서 원본 OpenVLA를 크게 능가하며, 이 방법이 시각적 도메인 제한을 효과적으로 역전시킬 수 있음을 검증했습니다.

## 핵심 내용
### 연구 동기와 문제
- 기존 로봇 기반 모델(예: RT-2, Octo, OpenVLA)은 훈련 데이터가 포함된 시각적 장면에서 우수한 성능을 보이지만, 조명, 배경, 객체 질감 등의 도메인 외부 변화에 직면하면 성능이 급격히 저하됩니다.
- 분석에 따르면 시각적 도메인 제한은 두 가지 요인에서 비롯됩니다: 훈련 데이터의 시각적 변화 부족, 그리고 미세 조정 과정에서 사전 훈련된 시각 백본(예: DINO-v2)의 파괴적 망각입니다.

### 방법: 점진적 백본 역전(Gradual Backbone Reversal)
- 핵심 아이디어: 모델 병합 기술을 통해 OpenVLA가 학습한 행동 능력을 유지하면서, 시각 백본의 원래 일반화 능력을 점진적으로 복원합니다.
- 구체적 구현:
  - OpenVLA의 시각 인코더(SigLIP + DINO-v2)를 원래 사전 훈련 가중치와 선형 보간(linear interpolation)합니다.
  - 보간 계수는 0(완전히 미세 조정된 가중치 사용)에서 1(완전히 사전 훈련 가중치 사용)로 점진적으로 전환되며, 일련의 중간 모델을 생성합니다.
  - 검증 세트에서 최적의 보간 계수를 선택하여 시각적 일반화와 행동 정밀도의 균형을 맞춥니다.

### 실험 설정 및 주요 결과
- 평가 기준: 사용자 정의 시각적 도메인 외부 테스트 세트로, 다양한 조명, 배경, 객체 색상 및 질감의 파지(grasping) 및 들어올리기(lifting) 작업을 포함합니다.
- 비교 모델: OpenVLA(기준선), RT-2, Octo.
- 주요 수치:
  - ReVLA는 시각적 도메인 외부 파지 작업에서 OpenVLA보다 77% 향상, 들어올리기 작업에서 66% 향상.
  - 도메인 내 작업에서 ReVLA 성능은 OpenVLA와 동등하며, 성능 저하가 없음.
  - 절제 실험은 점진적 역전(다단계 보간)이 사전 훈련 가중치를 직접 사용하는 것(단계적 역전)보다 우수하며, 후자는 행동 능력 붕괴를 초래함을 보여줍니다.

### 결론
- 시각적 파괴적 망각은 로봇 기반 모델의 도메인 외부 일반화를 제한하는 핵심 병목입니다.
- 모델 병합 기반의 점진적 백본 역전은 추가 훈련 없이도 효과적인 경량 솔루션입니다.
- 모델 가중치와 전체 평가 비디오는 오픈소스로 공개되었으며, 자세한 내용은 ReVLA 프로젝트 페이지에서 확인할 수 있습니다.
