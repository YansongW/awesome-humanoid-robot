---
$id: ent_paper_kim_fine_tuning_vision_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'
  zh: OpenVLA-OFT
  ko: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'
summary:
  en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University, and published at RSS 2025.'
  zh: OpenVLA-OFT 是斯坦福大学在 RSS 2025 上提出的一种针对视觉-语言-动作模型（VLA）的优化微调方法。其核心贡献在于通过整合并行解码、动作分块、连续动作表示和 L1 回归损失函数，将 OpenVLA 在 LIBERO
    基准上的平均成功率从 76.5% 提升至 97.1%，同时将动作生成吞吐量提高 26 倍。该方法在真实机器人任务中，使双机械臂 ALOHA 机器人成功执行灵巧高频控制，并超越其他 VLA 模型和从零训练的模仿学习策略。
  ko: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University, and published at RSS 2025.'
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
- openvla_oft
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.19645v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (arXiv)'
  url: https://arxiv.org/abs/2502.19645
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OpenVLA-OFT source
  url: https://doi.org/10.48550/arXiv.2502.19645
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型（VLA）虽在语义泛化上表现优异，但面对新机器人设置时仍需微调，而微调策略的选择尚不明确。本研究以 OpenVLA 为基座模型，系统分析了动作解码方案、动作表示和学习目标等关键设计选择。基于实证分析，作者提出优化微调（OFT）方案，整合并行解码、动作分块、连续动作表示和 L1 回归损失，显著提升推理效率、策略性能和输入输出灵活性。该方案在 LIBERO 模拟基准上创下新纪录，并在真实世界评估中使双机械臂 ALOHA 机器人成功执行灵巧高频控制任务，平均成功率比 π₀ 和 RDT-1B 等 VLA 模型高出 15%。

## 核心内容
### 方法概述
- **基座模型**：采用 OpenVLA 作为代表性 VLA 模型，其基于预训练的视觉-语言模型，利用多样化机器人数据集训练。
- **关键设计选择**：
  - **动作解码方案**：从自回归解码改为并行解码，显著提升推理速度。
  - **动作表示**：采用连续动作表示（而非离散化），保留动作精度。
  - **学习目标**：使用简单的 L1 回归损失替代复杂的损失函数，简化训练过程。
  - **动作分块**：引入动作分块（action chunking），允许模型一次性预测多个时间步的动作，提升控制稳定性。

### 实验设置
- **模拟基准**：在 LIBERO 基准的四个任务套件（LIBERO-Spatial、LIBERO-Object、LIBERO-Goal、LIBERO-Long）上进行评估。
- **真实世界评估**：在双机械臂 ALOHA 机器人上执行灵巧高频控制任务，对比模型包括 π₀、RDT-1B、Diffusion Policy 和 ACT。

### 关键结果
- **LIBERO 基准**：
  - OpenVLA-OFT 平均成功率从 76.5% 提升至 97.1%。
  - 动作生成吞吐量提高 26 倍（从 1.5 Hz 到 39 Hz）。
- **真实世界评估**：
  - 在双机械臂 ALOHA 机器人上，OpenVLA-OFT 成功执行灵巧高频控制任务。
  - 平均成功率比 π₀ 和 RDT-1B（使用默认微调方案）高出 15%。
  - 比从零训练的 Diffusion Policy 和 ACT 高出 15%（绝对成功率）。

### 结论
OpenVLA-OFT 通过优化微调策略，在模拟和真实环境中均实现了显著的性能提升和效率改进。代码和预训练模型已开源。

## Overview
Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.

## 개요
최근 비전-언어-행동 모델(VLA)은 사전 훈련된 비전-언어 모델을 기반으로 다양한 로봇 데이터셋을 활용하여 강력한 작업 실행, 언어 명령 수행 능력 및 의미적 일반화를 입증했습니다. 이러한 성공에도 불구하고 VLA는 새로운 로봇 설정에 어려움을 겪으며 좋은 성능을 달성하기 위해 미세 조정이 필요하지만, 다양한 가능한 전략이 존재하는 가운데 가장 효과적인 미세 조정 방법은 불분명합니다. 본 연구에서는 OpenVLA를 대표적인 기본 모델로 사용하여 다양한 행동 디코딩 방식, 행동 표현 및 미세 조정을 위한 학습 목표와 같은 주요 VLA 적응 설계 선택지를 연구합니다. 실증 분석을 통해 병렬 디코딩, 행동 청킹, 연속 행동 표현 및 간단한 L1 회귀 기반 학습 목표를 통합하여 추론 효율성, 정책 성능 및 모델의 입출력 사양 유연성을 모두 개선하는 최적화된 미세 조정(OFT) 레시피를 도출했습니다. 이 레시피의 구현체인 OpenVLA-OFT를 제안하며, 이는 LIBERO 시뮬레이션 벤치마크에서 새로운 최첨단 성능을 달성하여 네 가지 작업 제품군에서 OpenVLA의 평균 성공률을 76.5%에서 97.1%로 크게 향상시키고 행동 생성 처리량을 26배 증가시킵니다. 실제 환경 평가에서, 당사의 미세 조정 레시피는 OpenVLA가 양팔 ALOHA 로봇에서 정밀하고 고주파 제어 작업을 성공적으로 실행할 수 있게 하며, 기본 레시피로 미세 조정된 다른 VLA($π_0$ 및 RDT-1B)와 처음부터 훈련된 강력한 모방 학습 정책(Diffusion Policy 및 ACT)을 평균 성공률에서 최대 15%(절대값)까지 능가합니다. OFT 코드와 사전 훈련된 모델 체크포인트를 https://openvla-oft.github.io/에서 공개합니다.

## 핵심 내용
최근 비전-언어-행동 모델(VLA)은 사전 훈련된 비전-언어 모델을 기반으로 다양한 로봇 데이터셋을 활용하여 강력한 작업 실행, 언어 명령 수행 능력 및 의미적 일반화를 입증했습니다. 이러한 성공에도 불구하고 VLA는 새로운 로봇 설정에 어려움을 겪으며 좋은 성능을 달성하기 위해 미세 조정이 필요하지만, 다양한 가능한 전략이 존재하는 가운데 가장 효과적인 미세 조정 방법은 불분명합니다. 본 연구에서는 OpenVLA를 대표적인 기본 모델로 사용하여 다양한 행동 디코딩 방식, 행동 표현 및 미세 조정을 위한 학습 목표와 같은 주요 VLA 적응 설계 선택지를 연구합니다. 실증 분석을 통해 병렬 디코딩, 행동 청킹, 연속 행동 표현 및 간단한 L1 회귀 기반 학습 목표를 통합하여 추론 효율성, 정책 성능 및 모델의 입출력 사양 유연성을 모두 개선하는 최적화된 미세 조정(OFT) 레시피를 도출했습니다. 이 레시피의 구현체인 OpenVLA-OFT를 제안하며, 이는 LIBERO 시뮬레이션 벤치마크에서 새로운 최첨단 성능을 달성하여 네 가지 작업 제품군에서 OpenVLA의 평균 성공률을 76.5%에서 97.1%로 크게 향상시키고 행동 생성 처리량을 26배 증가시킵니다. 실제 환경 평가에서, 당사의 미세 조정 레시피는 OpenVLA가 양팔 ALOHA 로봇에서 정밀하고 고주파 제어 작업을 성공적으로 실행할 수 있게 하며, 기본 레시피로 미세 조정된 다른 VLA($π_0$ 및 RDT-1B)와 처음부터 훈련된 강력한 모방 학습 정책(Diffusion Policy 및 ACT)을 평균 성공률에서 최대 15%(절대값)까지 능가합니다. OFT 코드와 사전 훈련된 모델 체크포인트를 https://openvla-oft.github.io/에서 공개합니다.

## 参考
- http://arxiv.org/abs/2502.19645v2
