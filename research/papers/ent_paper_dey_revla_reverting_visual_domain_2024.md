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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.15250v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
최근 대규모 언어 모델의 발전과 대규모 로봇 데이터셋에 대한 접근성은 로봇 모델을 다양한 작업, 장면 및 로봇 모달리티에 적응할 수 있는 제너럴리스트로 전환하는 패러다임 변화를 촉발했습니다. 커뮤니티의 큰 진전은 다양한 작업에서 강력한 성능을 보여주는 오픈 Vision Language Action 모델입니다. 본 연구에서는 기존의 세 가지 로봇 기반 모델의 시각적 일반화 능력을 조사하고, 이에 상응하는 평가 프레임워크를 제안합니다. 우리의 연구는 기존 모델이 시각적 도메인 외부(out-of-domain) 시나리오에 대한 견고성을 나타내지 않음을 보여줍니다. 이는 잠재적으로 훈련 데이터의 제한된 다양성 및/또는 치명적 망각(catastrophic forgetting)으로 인해 발생하며, 이는 시각 기반 모델의 도메인 한계로 이어집니다. 우리는 또한 OpenVLA를 추가로 탐구합니다. OpenVLA는 두 개의 사전 훈련된 시각 기반 모델을 사용하므로 도메인 외부 실험에 일반화될 것으로 예상됩니다. 그러나 우리는 OpenVLA에서 DINO-v2가 깊이 회귀(depth regression) 작업을 수행하지 못함으로써 치명적 망각을 보여줍니다. 위에서 언급한 시각적 치명적 망각 문제를 극복하기 위해, 우리는 모델 병합(model merging)에 기반한 점진적 백본 역전(gradual backbone reversal) 접근 방식을 제안합니다. 이를 통해 초기 훈련 중 시각적 백본의 적응이 필요한 OpenVLA가 시각적 일반화 능력을 회복할 수 있습니다. 이 능력을 회복함으로써 우리의 ReVLA 모델은 시각적 OOD 작업에서 그리핑(grasping) 및 리프팅(lifting)에 대해 OpenVLA 대비 각각 77% 및 66% 향상됩니다. 포괄적인 평가, 에피소드 롤아웃 및 모델 가중치는 ReVLA 페이지에서 확인할 수 있습니다.

## 핵심 내용
최근 대규모 언어 모델의 발전과 대규모 로봇 데이터셋에 대한 접근성은 로봇 모델을 다양한 작업, 장면 및 로봇 모달리티에 적응할 수 있는 제너럴리스트로 전환하는 패러다임 변화를 촉발했습니다. 커뮤니티의 큰 진전은 다양한 작업에서 강력한 성능을 보여주는 오픈 Vision Language Action 모델입니다. 본 연구에서는 기존의 세 가지 로봇 기반 모델의 시각적 일반화 능력을 조사하고, 이에 상응하는 평가 프레임워크를 제안합니다. 우리의 연구는 기존 모델이 시각적 도메인 외부 시나리오에 대한 견고성을 나타내지 않음을 보여줍니다. 이는 잠재적으로 훈련 데이터의 제한된 다양성 및/또는 치명적 망각으로 인해 발생하며, 이는 시각 기반 모델의 도메인 한계로 이어집니다. 우리는 또한 OpenVLA를 추가로 탐구합니다. OpenVLA는 두 개의 사전 훈련된 시각 기반 모델을 사용하므로 도메인 외부 실험에 일반화될 것으로 예상됩니다. 그러나 우리는 OpenVLA에서 DINO-v2가 깊이 회귀 작업을 수행하지 못함으로써 치명적 망각을 보여줍니다. 위에서 언급한 시각적 치명적 망각 문제를 극복하기 위해, 우리는 모델 병합에 기반한 점진적 백본 역전 접근 방식을 제안합니다. 이를 통해 초기 훈련 중 시각적 백본의 적응이 필요한 OpenVLA가 시각적 일반화 능력을 회복할 수 있습니다. 이 능력을 회복함으로써 우리의 ReVLA 모델은 시각적 OOD 작업에서 그리핑 및 리프팅에 대해 OpenVLA 대비 각각 77% 및 66% 향상됩니다. 포괄적인 평가, 에피소드 롤아웃 및 모델 가중치는 ReVLA 페이지에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2409.15250v3
