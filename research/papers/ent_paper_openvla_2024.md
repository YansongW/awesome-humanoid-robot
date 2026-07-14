---
$id: ent_paper_openvla_2024
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OpenVLA: An Open-Source Vision-Language-Action Model'
  zh: OpenVLA：一个开源的视觉-语言-动作模型
  ko: 'OpenVLA: 오픈소스 비전-언어-액션 모델'
summary:
  en: A 7B-parameter open-source VLA pretrained on 970k real-world robot demonstrations from the Open X-Embodiment dataset,
    combining Llama 2, DINOv2, and SigLIP for generalist manipulation.
  zh: 一个 70 亿参数的开源 VLA 模型，基于 Open X-Embodiment 数据集的 97 万条真实机器人演示进行预训练，融合 Llama 2、DINOv2 和 SigLIP 以实现通用操作。
  ko: Open X-Embodiment 데이터셋의 97만 개 실제 로봇 데모로 사전 학습된 70억 개 매개변수의 오픈소스 VLA 모델로, Llama 2, DINOv2, SigLIP을 결합하여 범용 조작을 수행함.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- open_source
- open_x_embodiment
- manipulation
- llama2
- dinov2
- siglip
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.09246v3.
sources:
- id: src_paper_openvla_2024
  type: paper
  title: 'OpenVLA: An Open-Source Vision-Language-Action Model'
  url: https://arxiv.org/abs/2406.09246
  date: '2024-06-13'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: is_based_on
  description:
    en: OpenVLA is pretrained on 970k real-world robot demonstrations from the Open X-Embodiment dataset.
    zh: OpenVLA 基于 Open X-Embodiment 数据集的 97 万条真实机器人演示进行预训练。
    ko: OpenVLA는 Open X-Embodiment 데이터셋의 97만 개 실제 로봇 데모로 사전 학습되었음.
- id: ent_dataset_droid
  relationship: cites
  description:
    en: The OpenVLA paper discusses DROID as part of the diverse robot demonstration data used for pretraining.
    zh: OpenVLA 论文将 DROID 作为预训练所使用的多样化机器人演示数据的一部分进行讨论。
    ko: OpenVLA 논문은 사전 학습에 사용된 다양한 로봇 데모 데이터의 일부로 DROID를 다룸.
theoretical_depth:
- system
---
## 概述
Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from scratch, we can fine-tune such vision-language-action (VLA) models to obtain robust, generalizable policies for visuomotor control. Yet, widespread adoption of VLAs for robotics has been challenging as 1) existing VLAs are largely closed and inaccessible to the public, and 2) prior work fails to explore methods for efficiently fine-tuning VLAs for new tasks, a key component for adoption. Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. As a product of the added data diversity and new model components, OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters. We further show that we can effectively fine-tune OpenVLA for new settings, with especially strong generalization results in multi-task environments involving multiple objects and strong language grounding abilities, and outperform expressive from-scratch imitation learning methods such as Diffusion Policy by 20.4%. We also explore compute efficiency; as a separate contribution, we show that OpenVLA can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization without a hit to downstream success rate. Finally, we release model checkpoints, fine-tuning notebooks, and our PyTorch codebase with built-in support for training VLAs at scale on Open X-Embodiment datasets.

## 核心内容
Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from scratch, we can fine-tune such vision-language-action (VLA) models to obtain robust, generalizable policies for visuomotor control. Yet, widespread adoption of VLAs for robotics has been challenging as 1) existing VLAs are largely closed and inaccessible to the public, and 2) prior work fails to explore methods for efficiently fine-tuning VLAs for new tasks, a key component for adoption. Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. As a product of the added data diversity and new model components, OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters. We further show that we can effectively fine-tune OpenVLA for new settings, with especially strong generalization results in multi-task environments involving multiple objects and strong language grounding abilities, and outperform expressive from-scratch imitation learning methods such as Diffusion Policy by 20.4%. We also explore compute efficiency; as a separate contribution, we show that OpenVLA can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization without a hit to downstream success rate. Finally, we release model checkpoints, fine-tuning notebooks, and our PyTorch codebase with built-in support for training VLAs at scale on Open X-Embodiment datasets.

## 参考
- http://arxiv.org/abs/2406.09246v3

