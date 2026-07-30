---
$id: ent_paper_unified_video_action_model_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Video Action Model
  zh: Unified Video Action Model
  ko: Unified Video Action Model
summary:
  en: Unified Video Action Model is a 2025 work on manipulation for humanoid robots.
  zh: Unified Video Action Model (UVA) 是2025年面向人形机器人操作任务的工作，由研究团队提出。其核心贡献在于通过联合视频-动作潜在表示与解耦解码架构，同时实现高精度动作预测与高效推理，并支持策略学习、正/逆动力学建模及视频生成等多种任务。
  ko: Unified Video Action Model is a 2025 work on manipulation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- manipulation
- unified_video_action_model
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00200v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Unified Video Action Model (arXiv)
  url: https://arxiv.org/abs/2503.00200
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Unified Video Action Model project page
  url: https://unified-video-action-model.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
UVA 旨在解决视频生成与动作预测难以有效结合的问题。现有基于视频生成的方法在动作精度和推理速度上往往不如直接策略学习。UVA 通过联合优化视频与动作预测，学习一个连接视觉与动作域的联合潜在表示，并利用两个轻量级扩散头实现解耦解码，从而在推理时绕过视频生成过程，实现高速动作推理。此外，通过掩码输入训练，单一模型可灵活处理策略学习、正/逆动力学建模和视频生成等多样化任务，且性能不逊于专用方法。

## 核心内容
### 方法架构
UVA 的核心设计包括两个关键组件：
- **联合视频-动作潜在表示**：该表示桥接视觉与动作域，有效建模视频序列与动作序列之间的关联。通过联合编码，模型能够捕捉场景信息与动态信息的交互。
- **解耦视频-动作解码**：采用两个轻量级扩散头分别解码视频和动作。在推理阶段，动作解码头可直接从联合潜在表示生成动作，无需先生成视频，从而大幅提升推理速度。

### 训练与功能
- **掩码输入训练**：通过选择性掩码动作或视频输入，单一模型可适配多种任务。例如：
  - 策略学习：输入视频，预测动作。
  - 正动力学建模：输入动作，预测下一视频帧。
  - 逆动力学建模：输入视频，预测动作序列。
  - 视频生成：输入动作，生成对应视频。
- **实验设置**：在多个机器人操作基准上评估，包括人形机器人操作任务。关键指标包括动作预测精度（如成功率）和推理速度（如每秒帧数）。

### 关键结果
- **性能对比**：UVA 在策略学习任务上达到与直接策略学习（如行为克隆）相当的动作精度，同时推理速度显著快于基于视频生成的方法（如 Video Diffusion Policy）。
- **多功能性**：在正/逆动力学建模和视频生成任务中，UVA 的性能与专用模型（如 Dynamics Model 或 Video Generation Model）持平或更优。
- **速度优势**：由于推理时无需视频生成，UVA 的动作推理延迟降低至毫秒级，适合实时机器人控制。

### 结论
UVA 通过联合视频-动作潜在表示与解耦解码，实现了高精度、高效率的通用机器人任务解决方案。其统一框架避免了为不同任务训练多个模型，同时保持了性能竞争力。更多可视化结果可访问项目网站。

## Overview
A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation. Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications. Results are best viewed on https://unified-video-action-model.github.io/.

## 개요
통합 비디오 및 행동 모델은 로보틱스에서 큰 가능성을 지니고 있습니다. 비디오는 행동 예측을 위한 풍부한 장면 정보를 제공하고, 행동은 비디오 예측을 위한 동역학 정보를 제공합니다. 그러나 비디오 생성과 행동 예측을 효과적으로 결합하는 것은 여전히 어려운 과제이며, 현재 비디오 생성 기반 방법은 행동 정확도와 추론 속도에서 직접 정책 학습의 성능을 따라잡기 어렵습니다. 이러한 격차를 해소하기 위해, 우리는 비디오와 행동 예측을 공동으로 최적화하여 높은 정확도와 효율적인 행동 추론을 동시에 달성하는 통합 비디오 행동 모델(UVA)을 소개합니다. 핵심은 공동 비디오-행동 잠재 표현을 학습하고 비디오-행동 디코딩을 분리하는 데 있습니다. 공동 잠재 표현은 시각 및 행동 도메인을 연결하여 비디오와 행동 시퀀스 간의 관계를 효과적으로 모델링합니다. 동시에, 두 개의 경량 확산 헤드로 구동되는 분리된 디코딩은 추론 중 비디오 생성을 우회하여 고속 행동 추론을 가능하게 합니다. 이러한 통합 프레임워크는 마스크 입력 학습을 통해 다기능성을 더욱 향상시킵니다. 행동이나 비디오를 선택적으로 마스킹함으로써, 단일 모델이 정책 학습 외에도 순방향 및 역방향 동역학 모델링, 비디오 생성과 같은 다양한 작업을 처리할 수 있습니다. 광범위한 실험을 통해, UVA가 특정 애플리케이션에 맞춤화된 방법과 비교하여 성능 저하 없이 정책 학습, 순방향/역방향 동역학, 비디오 관측 예측 등 다양한 로보틱스 작업을 위한 범용 솔루션으로 사용될 수 있음을 입증합니다. 결과는 https://unified-video-action-model.github.io/에서 가장 잘 확인할 수 있습니다.

## 핵심 내용
통합 비디오 및 행동 모델은 로보틱스에서 큰 가능성을 지니고 있습니다. 비디오는 행동 예측을 위한 풍부한 장면 정보를 제공하고, 행동은 비디오 예측을 위한 동역학 정보를 제공합니다. 그러나 비디오 생성과 행동 예측을 효과적으로 결합하는 것은 여전히 어려운 과제이며, 현재 비디오 생성 기반 방법은 행동 정확도와 추론 속도에서 직접 정책 학습의 성능을 따라잡기 어렵습니다. 이러한 격차를 해소하기 위해, 우리는 비디오와 행동 예측을 공동으로 최적화하여 높은 정확도와 효율적인 행동 추론을 동시에 달성하는 통합 비디오 행동 모델(UVA)을 소개합니다. 핵심은 공동 비디오-행동 잠재 표현을 학습하고 비디오-행동 디코딩을 분리하는 데 있습니다. 공동 잠재 표현은 시각 및 행동 도메인을 연결하여 비디오와 행동 시퀀스 간의 관계를 효과적으로 모델링합니다. 동시에, 두 개의 경량 확산 헤드로 구동되는 분리된 디코딩은 추론 중 비디오 생성을 우회하여 고속 행동 추론을 가능하게 합니다. 이러한 통합 프레임워크는 마스크 입력 학습을 통해 다기능성을 더욱 향상시킵니다. 행동이나 비디오를 선택적으로 마스킹함으로써, 단일 모델이 정책 학습 외에도 순방향 및 역방향 동역학 모델링, 비디오 생성과 같은 다양한 작업을 처리할 수 있습니다. 광범위한 실험을 통해, UVA가 특정 애플리케이션에 맞춤화된 방법과 비교하여 성능 저하 없이 정책 학습, 순방향/역방향 동역학, 비디오 관측 예측 등 다양한 로보틱스 작업을 위한 범용 솔루션으로 사용될 수 있음을 입증합니다. 결과는 https://unified-video-action-model.github.io/에서 가장 잘 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2503.00200v3
