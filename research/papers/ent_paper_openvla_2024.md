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
  zh: OpenVLA 是一个 7B 参数的开源视觉-语言-动作模型，由团队基于 Open X-Embodiment 数据集的 97 万条真实机器人演示训练而成。它融合了 Llama 2、DINOv2 和 SigLIP，在通用操作任务上超越闭源模型
    RT-2-X（55B）16.5%，且参数量仅为后者的 1/7。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.09246v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
OpenVLA 旨在解决现有视觉-语言-动作模型（VLA）闭源且难以微调的问题。该模型以 Llama 2 为语言主干，结合 DINOv2 与 SigLIP 的融合视觉编码器，在 29 项任务及多种机器人平台上取得了 16.5% 的绝对成功率提升。研究还展示了通过低秩适配方法在消费级 GPU 上高效微调的能力，并验证了量化部署不影响下游性能。

## 核心内容
### 模型架构
- **语言模型**：基于 Llama 2（7B 参数）作为核心推理引擎。
- **视觉编码器**：融合 DINOv2 与 SigLIP 的预训练特征，增强对视觉语义与细节的捕捉能力。
- **动作输出**：直接生成连续动作指令，实现端到端的视觉-语言-动作映射。

### 训练数据
- 使用 Open X-Embodiment 数据集中的 97 万条真实机器人演示，涵盖多种操作场景与机械臂形态。
- 数据多样性是模型泛化能力的关键，使其能处理多物体、多任务环境。

### 实验设置与关键结果
- **通用操作性能**：在 29 项任务上，OpenVLA 绝对任务成功率达 16.5%，超越 RT-2-X（55B）7 倍参数量的模型。
- **微调与泛化**：通过低秩适配（LoRA）在消费级 GPU 上微调，多任务环境中成功率比从头训练的 Diffusion Policy 高 20.4%。
- **部署效率**：量化后模型推理速度提升，且下游任务成功率无显著下降。

### 结论
OpenVLA 作为首个开源 7B 级 VLA 模型，证明了大规模预训练与高效微调的结合可显著降低机器人技能获取门槛。研究团队已公开模型权重、微调代码及 PyTorch 训练框架，支持在 Open X-Embodiment 数据集上扩展训练。

## Overview
Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from scratch, we can fine-tune such vision-language-action (VLA) models to obtain robust, generalizable policies for visuomotor control. Yet, widespread adoption of VLAs for robotics has been challenging as 1) existing VLAs are largely closed and inaccessible to the public, and 2) prior work fails to explore methods for efficiently fine-tuning VLAs for new tasks, a key component for adoption. Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. As a product of the added data diversity and new model components, OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters. We further show that we can effectively fine-tune OpenVLA for new settings, with especially strong generalization results in multi-task environments involving multiple objects and strong language grounding abilities, and outperform expressive from-scratch imitation learning methods such as Diffusion Policy by 20.4%. We also explore compute efficiency; as a separate contribution, we show that OpenVLA can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization without a hit to downstream success rate. Finally, we release model checkpoints, fine-tuning notebooks, and our PyTorch codebase with built-in support for training VLAs at scale on Open X-Embodiment datasets.

## 개요
인터넷 규모의 시각-언어 데이터와 다양한 로봇 시연 데이터를 결합하여 사전 학습된 대규모 정책은 로봇에게 새로운 기술을 가르치는 방식을 바꿀 잠재력을 지니고 있습니다. 즉, 새로운 행동을 처음부터 훈련하는 대신, 이러한 시각-언어-행동(VLA) 모델을 미세 조정하여 시각-운동 제어를 위한 강력하고 일반화 가능한 정책을 얻을 수 있습니다. 그러나 로봇 공학에서 VLA의 광범위한 채택은 1) 기존 VLA가 대부분 폐쇄적이고 대중이 접근하기 어렵다는 점, 2) 선행 연구가 새로운 작업을 위한 VLA의 효율적인 미세 조정 방법(채택의 핵심 요소)을 탐구하지 못했다는 점에서 어려움을 겪고 있습니다. 이러한 문제를 해결하기 위해 우리는 970k개의 실제 로봇 시연 데이터로 구성된 다양한 컬렉션에서 훈련된 7B 파라미터 오픈소스 VLA인 OpenVLA를 소개합니다. OpenVLA는 DINOv2와 SigLIP의 사전 학습된 특징을 융합하는 시각 인코더와 결합된 Llama 2 언어 모델을 기반으로 합니다. 추가된 데이터 다양성과 새로운 모델 구성 요소의 결과로, OpenVLA는 일반화된 조작에서 강력한 결과를 보여주며, 29개 작업과 여러 로봇 구현체에서 절대 작업 성공률 기준으로 RT-2-X(55B)와 같은 폐쇄형 모델을 16.5% 능가하고, 파라미터는 7배 적습니다. 또한 OpenVLA를 새로운 환경에 효과적으로 미세 조정할 수 있음을 보여주며, 특히 여러 객체와 강력한 언어 기반 능력을 포함하는 다중 작업 환경에서 뛰어난 일반화 결과를 보여주고, Diffusion Policy와 같은 처음부터 학습하는 표현적 모방 학습 방법을 20.4% 능가합니다. 또한 계산 효율성을 탐구합니다. 별도의 기여로, 최신 저랭크 적응 방법을 통해 소비자용 GPU에서 OpenVLA를 미세 조정하고, 양자화를 통해 다운스트림 성공률 저하 없이 효율적으로 서비스할 수 있음을 보여줍니다. 마지막으로, 모델 체크포인트, 미세 조정 노트북, 그리고 Open X-Embodiment 데이터셋에서 대규모 VLA 훈련을 지원하는 PyTorch 코드베이스를 공개합니다.

## 핵심 내용
인터넷 규모의 시각-언어 데이터와 다양한 로봇 시연 데이터를 결합하여 사전 학습된 대규모 정책은 로봇에게 새로운 기술을 가르치는 방식을 바꿀 잠재력을 지니고 있습니다. 즉, 새로운 행동을 처음부터 훈련하는 대신, 이러한 시각-언어-행동(VLA) 모델을 미세 조정하여 시각-운동 제어를 위한 강력하고 일반화 가능한 정책을 얻을 수 있습니다. 그러나 로봇 공학에서 VLA의 광범위한 채택은 1) 기존 VLA가 대부분 폐쇄적이고 대중이 접근하기 어렵다는 점, 2) 선행 연구가 새로운 작업을 위한 VLA의 효율적인 미세 조정 방법(채택의 핵심 요소)을 탐구하지 못했다는 점에서 어려움을 겪고 있습니다. 이러한 문제를 해결하기 위해 우리는 970k개의 실제 로봇 시연 데이터로 구성된 다양한 컬렉션에서 훈련된 7B 파라미터 오픈소스 VLA인 OpenVLA를 소개합니다. OpenVLA는 DINOv2와 SigLIP의 사전 학습된 특징을 융합하는 시각 인코더와 결합된 Llama 2 언어 모델을 기반으로 합니다. 추가된 데이터 다양성과 새로운 모델 구성 요소의 결과로, OpenVLA는 일반화된 조작에서 강력한 결과를 보여주며, 29개 작업과 여러 로봇 구현체에서 절대 작업 성공률 기준으로 RT-2-X(55B)와 같은 폐쇄형 모델을 16.5% 능가하고, 파라미터는 7배 적습니다. 또한 OpenVLA를 새로운 환경에 효과적으로 미세 조정할 수 있음을 보여주며, 특히 여러 객체와 강력한 언어 기반 능력을 포함하는 다중 작업 환경에서 뛰어난 일반화 결과를 보여주고, Diffusion Policy와 같은 처음부터 학습하는 표현적 모방 학습 방법을 20.4% 능가합니다. 또한 계산 효율성을 탐구합니다. 별도의 기여로, 최신 저랭크 적응 방법을 통해 소비자용 GPU에서 OpenVLA를 미세 조정하고, 양자화를 통해 다운스트림 성공률 저하 없이 효율적으로 서비스할 수 있음을 보여줍니다. 마지막으로, 모델 체크포인트, 미세 조정 노트북, 그리고 Open X-Embodiment 데이터셋에서 대규모 VLA 훈련을 지원하는 PyTorch 코드베이스를 공개합니다.

## 参考
- http://arxiv.org/abs/2406.09246v3
