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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00200v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (961 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2503.00200v3

## 개요
UVA는 비디오 생성과 동작 예측을 효과적으로 결합하기 어려운 문제를 해결하는 것을 목표로 한다. 기존의 비디오 생성 기반 방법은 동작 정확도와 추론 속도에서 종종 직접적인 정책 학습보다 떨어진다. UVA는 비디오와 동작 예측을 공동으로 최적화하여 시각 영역과 동작 영역을 연결하는 공동 잠재 표현을 학습하고, 두 개의 경량 확산 헤드를 사용하여 분리된 디코딩을 구현함으로써 추론 시 비디오 생성 과정을 우회하여 고속 동작 추론을 가능하게 한다. 또한, 마스크 입력 훈련을 통해 단일 모델이 정책 학습, 정/역동역학 모델링, 비디오 생성 등 다양한 작업을 유연하게 처리할 수 있으며, 성능은 전용 방법에 뒤지지 않는다.

## 핵심 내용
### 방법 아키텍처
UVA의 핵심 설계는 두 가지 주요 구성 요소를 포함한다:
- **공동 비디오-동작 잠재 표현**: 이 표현은 시각 영역과 동작 영역을 연결하여 비디오 시퀀스와 동작 시퀀스 간의 연관성을 효과적으로 모델링한다. 공동 인코딩을 통해 모델은 장면 정보와 동적 정보의 상호작용을 포착할 수 있다.
- **분리된 비디오-동작 디코딩**: 두 개의 경량 확산 헤드를 사용하여 비디오와 동작을 각각 디코딩한다. 추론 단계에서 동작 디코딩 헤드는 공동 잠재 표현에서 직접 동작을 생성할 수 있으며, 비디오를 먼저 생성할 필요가 없어 추론 속도를 크게 향상시킨다.

### 훈련 및 기능
- **마스크 입력 훈련**: 동작 또는 비디오 입력을 선택적으로 마스킹함으로써 단일 모델이 다양한 작업에 적응할 수 있다. 예를 들어:
  - 정책 학습: 비디오를 입력으로 받아 동작을 예측.
  - 정동역학 모델링: 동작을 입력으로 받아 다음 비디오 프레임을 예측.
  - 역동역학 모델링: 비디오를 입력으로 받아 동작 시퀀스를 예측.
  - 비디오 생성: 동작을 입력으로 받아 해당 비디오를 생성.
- **실험 설정**: 휴머노이드 로봇 조작 작업을 포함한 여러 로봇 조작 벤치마크에서 평가된다. 주요 지표는 동작 예측 정확도(예: 성공률)와 추론 속도(예: 초당 프레임 수)이다.

### 주요 결과
- **성능 비교**: UVA는 정책 학습 작업에서 직접 정책 학습(예: 행동 클로닝)과 동등한 동작 정확도를 달성하면서, 비디오 생성 기반 방법(예: Video Diffusion Policy)보다 추론 속도가 현저히 빠르다.
- **다기능성**: 정/역동역학 모델링 및 비디오 생성 작업에서 UVA의 성능은 전용 모델(예: Dynamics Model 또는 Video Generation Model)과 동등하거나 더 우수하다.
- **속도 이점**: 추론 시 비디오 생성이 필요 없으므로 UVA의 동작 추론 지연 시간은 밀리초 수준으로 줄어들어 실시간 로봇 제어에 적합하다.

### 결론
UVA는 공동 비디오-동작 잠재 표현과 분리된 디코딩을 통해 고정밀도, 고효율의 범용 로봇 작업 솔루션을 구현한다. 통합 프레임워크는 다양한 작업을 위해 여러 모델을 훈련할 필요를 없애면서도 성능 경쟁력을 유지한다. 더 많은 시각화 결과는 프로젝트 웹사이트에서 확인할 수 있다.
