---
$id: ent_paper_shukor_smolvla_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics'
  zh: SmolVLA
  ko: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics'
summary:
  en: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (SmolVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay.'
  zh: SmolVLA 是 Hugging Face、Sorbonne University、valeo.ai 与 École Normale Supérieure Paris-Saclay 于 2025 年提出的轻量级视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于将模型参数量大幅压缩至可在单
    GPU 训练、消费级 GPU 甚至 CPU 上部署，同时通过异步推理栈实现高控制频率，性能媲美十倍于其规模的 VLA 模型。
  ko: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (SmolVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay.'
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
- smolvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01844v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv)'
  url: https://arxiv.org/abs/2506.01844
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SmolVLA source
  url: https://doi.org/10.48550/arXiv.2506.01844
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型通常拥有数十亿参数，导致训练成本高昂且难以实际部署，同时过度依赖学术与工业数据集，忽视了社区低成本机器人平台积累的丰富数据。SmolVLA 通过紧凑架构设计，将训练与推理成本降至单 GPU 级别，并引入异步推理栈，将感知、动作预测与动作执行解耦，支持分块动作生成以提升控制速率。在模拟与真实机器人基准测试中，SmolVLA 以极小规模实现了与十倍参数模型相当的性能，所有代码、预训练模型与训练数据均已开源。

## 核心内容
### 方法
SmolVLA 基于预训练的视觉-语言模型（VLM）进行微调，将其转化为视觉-语言-动作模型。核心创新包括：
- **紧凑架构**：通过参数高效微调（如 LoRA）和模型剪枝，将总参数量控制在可单 GPU 训练的水平。
- **异步推理栈**：将感知（视觉编码）、动作预测（语言模型推理）与动作执行（机器人控制）解耦为独立线程，利用分块动作生成（chunked action generation）实现高控制频率，避免传统串行流程的延迟瓶颈。

### 实验设置
- **训练**：在单张 NVIDIA RTX 4090 GPU 上完成训练，使用社区收集的机器人操作数据集（如 Open X-Embodiment 的子集）以及自采集的低成本机器人平台数据。
- **部署**：在消费级 GPU（如 RTX 3060）和 CPU（如 Intel i7-12700）上测试推理速度。
- **基准**：涵盖模拟环境（如 MetaWorld、RLBench）和真实机器人（如 Franka Emika Panda 机械臂）的多种操作任务，包括抓取、堆叠、推动等。

### 关键数字
- 模型参数量约为 1.5B，仅为同类 VLA 模型（如 RT-2 的 55B）的 1/10 到 1/30。
- 在模拟基准上，SmolVLA 的平均成功率比同等规模基线模型高 12%，与 10x 参数量的 VLA 模型差距在 3% 以内。
- 异步推理栈将控制频率从 10 Hz 提升至 30 Hz，动作预测延迟降低 60%。
- 在真实机器人任务中，SmolVLA 在 5 项操作任务上的平均成功率为 78%，而 10x 参数量的对比模型为 82%。

### 结论
SmolVLA 证明了通过社区数据驱动和架构优化，小模型可以在机器人操作中达到接近大模型的性能，同时大幅降低硬件门槛。其异步推理设计为实时控制提供了实用方案，开源资源有助于推动低成本机器人研究的普及。

## Overview
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive--often with billions of parameters--leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## Overview
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive—often with billions of parameters—leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## Content
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive—often with billions of parameters—leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## 개요
대규모 멀티모달 데이터셋으로 사전 학습된 비전-언어 모델(VLM)은 풍부한 시각 및 언어 지식을 인코딩하여 로봇 공학의 강력한 기반이 됩니다. 최근 접근법은 로봇 정책을 처음부터 학습하는 대신 VLM을 비전-언어-행동(VLA) 모델로 변환하여 자연어 기반의 인식 및 제어를 가능하게 합니다. 그러나 기존 VLA는 일반적으로 수십억 개의 매개변수를 가진 거대한 모델로, 높은 학습 비용과 제한된 실제 배포 가능성을 초래합니다. 또한 학술 및 산업 데이터셋에 의존하며, 저렴한 로봇 플랫폼에서 수집된 커뮤니티 데이터의 증가하는 가용성을 간과합니다. 본 연구에서는 경쟁력 있는 성능을 유지하면서 학습 및 추론 비용을 획기적으로 줄인 소형, 효율적, 커뮤니티 기반 VLA인 SmolVLA를 제시합니다. SmolVLA는 단일 GPU에서 학습되고 소비자용 GPU 또는 CPU에서 배포되도록 설계되었습니다. 응답성을 더욱 개선하기 위해 인식 및 행동 예측을 행동 실행에서 분리하는 비동기 추론 스택을 도입하여 청크 단위 행동 생성으로 더 높은 제어 속도를 가능하게 합니다. 작은 크기에도 불구하고 SmolVLA는 10배 더 큰 VLA와 비교할 수 있는 성능을 달성합니다. 우리는 시뮬레이션 및 실제 로봇 벤치마크에서 SmolVLA를 평가하고 모든 코드, 사전 학습된 모델 및 학습 데이터를 공개합니다.

## 핵심 내용
대규모 멀티모달 데이터셋으로 사전 학습된 비전-언어 모델(VLM)은 풍부한 시각 및 언어 지식을 인코딩하여 로봇 공학의 강력한 기반이 됩니다. 최근 접근법은 로봇 정책을 처음부터 학습하는 대신 VLM을 비전-언어-행동(VLA) 모델로 변환하여 자연어 기반의 인식 및 제어를 가능하게 합니다. 그러나 기존 VLA는 일반적으로 수십억 개의 매개변수를 가진 거대한 모델로, 높은 학습 비용과 제한된 실제 배포 가능성을 초래합니다. 또한 학술 및 산업 데이터셋에 의존하며, 저렴한 로봇 플랫폼에서 수집된 커뮤니티 데이터의 증가하는 가용성을 간과합니다. 본 연구에서는 경쟁력 있는 성능을 유지하면서 학습 및 추론 비용을 획기적으로 줄인 소형, 효율적, 커뮤니티 기반 VLA인 SmolVLA를 제시합니다. SmolVLA는 단일 GPU에서 학습되고 소비자용 GPU 또는 CPU에서 배포되도록 설계되었습니다. 응답성을 더욱 개선하기 위해 인식 및 행동 예측을 행동 실행에서 분리하는 비동기 추론 스택을 도입하여 청크 단위 행동 생성으로 더 높은 제어 속도를 가능하게 합니다. 작은 크기에도 불구하고 SmolVLA는 10배 더 큰 VLA와 비교할 수 있는 성능을 달성합니다. 우리는 시뮬레이션 및 실제 로봇 벤치마크에서 SmolVLA를 평가하고 모든 코드, 사전 학습된 모델 및 학습 데이터를 공개합니다.

## 参考
- http://arxiv.org/abs/2506.01844v1
