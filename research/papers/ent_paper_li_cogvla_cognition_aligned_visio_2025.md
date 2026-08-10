---
$id: ent_paper_li_cogvla_cognition_aligned_visio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification'
  zh: CogVLA
  ko: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification'
summary:
  en: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification (CogVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Computer Science and Technology,
    Harbin Institute of Technology, Harbin Institute of Technology, and published at NIPS25.'
  zh: CogVLA 是哈尔滨工业大学于 2025 年提出的认知对齐视觉-语言-动作模型，通过指令驱动的路由与稀疏化机制提升机器人操作效率。该模型在 LIBERO 基准上达到 97.4% 的成功率，训练成本降低 2.5 倍，推理延迟减少 2.8
    倍。
  ko: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification (CogVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Computer Science and Technology,
    Harbin Institute of Technology, Harbin Institute of Technology, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cogvla
- large_vla_model
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.21046v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (775 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification (arXiv)'
  url: https://arxiv.org/abs/2508.21046
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CogVLA source
  url: https://doi.org/10.48550/arXiv.2508.21046
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
CogVLA 针对现有 VLA 模型后训练计算开销大的问题，提出三阶段渐进式架构。其核心创新包括：EFA-Routing 通过 FiLM 机制将指令注入视觉编码器以压缩双流视觉令牌；LFP-Routing 利用 LLM 剪枝与指令无关的视觉令牌实现稀疏化；CAtten 结合因果视觉-语言注意力与双向动作并行解码。实验表明，该模型在 LIBERO 基准和真实机器人任务中均取得最优性能。

## 核心内容
### 方法架构
CogVLA 采用三阶段渐进式设计：
- **EFA-Routing**：基于 FiLM 的编码器聚合路由，将指令信息注入视觉编码器，选择性聚合并压缩双流视觉令牌，形成指令感知的隐式表征。
- **LFP-Routing**：基于 LLM 的剪枝路由，通过引入动作意图，剪枝与指令无关的视觉令牌，实现令牌级稀疏化。
- **CAtten**：V-L-A 耦合注意力机制，结合因果视觉-语言注意力与双向动作并行解码，确保压缩后的感知输入仍能生成准确连贯的动作。

### 实验设置
- **基准测试**：在 LIBERO 基准上进行评估，包含多种机器人操作任务。
- **真实场景**：在真实机器人任务中验证泛化能力。
- **对比基线**：与 OpenVLA 等模型进行效率与性能对比。

### 关键结果
- **成功率**：LIBERO 基准达 97.4%，真实任务达 70.0%。
- **效率提升**：训练成本降低 2.5 倍，推理延迟减少 2.8 倍。
- **开源**：代码与模型公开于 https://github.com/JiuTian-VL/CogVLA。

### 结论
CogVLA 通过指令驱动的路由与稀疏化，在保持高性能的同时显著降低计算开销，为 VLA 模型的可扩展部署提供了有效方案。

## Overview
Recent Vision-Language-Action (VLA) models built on pre-trained Vision-Language Models (VLMs) require extensive post-training, resulting in high computational overhead that limits scalability and deployment.We propose CogVLA, a Cognition-Aligned Vision-Language-Action framework that leverages instruction-driven routing and sparsification to improve both efficiency and performance. CogVLA draws inspiration from human multimodal coordination and introduces a 3-stage progressive architecture. 1) Encoder-FiLM based Aggregation Routing (EFA-Routing) injects instruction information into the vision encoder to selectively aggregate and compress dual-stream visual tokens, forming a instruction-aware latent representation. 2) Building upon this compact visual encoding, LLM-FiLM based Pruning Routing (LFP-Routing) introduces action intent into the language model by pruning instruction-irrelevant visually grounded tokens, thereby achieving token-level sparsity. 3) To ensure that compressed perception inputs can still support accurate and coherent action generation, we introduce V-L-A Coupled Attention (CAtten), which combines causal vision-language attention with bidirectional action parallel decoding. Extensive experiments on the LIBERO benchmark and real-world robotic tasks demonstrate that CogVLA achieves state-of-the-art performance with success rates of 97.4% and 70.0%, respectively, while reducing training costs by 2.5-fold and decreasing inference latency by 2.8-fold compared to OpenVLA. CogVLA is open-sourced and publicly available at https://github.com/JiuTian-VL/CogVLA.

## Overview
Recent Vision-Language-Action (VLA) models built on pre-trained Vision-Language Models (VLMs) require extensive post-training, resulting in high computational overhead that limits scalability and deployment. We propose CogVLA, a Cognition-Aligned Vision-Language-Action framework that leverages instruction-driven routing and sparsification to improve both efficiency and performance. CogVLA draws inspiration from human multimodal coordination and introduces a 3-stage progressive architecture. 1) Encoder-FiLM based Aggregation Routing (EFA-Routing) injects instruction information into the vision encoder to selectively aggregate and compress dual-stream visual tokens, forming an instruction-aware latent representation. 2) Building upon this compact visual encoding, LLM-FiLM based Pruning Routing (LFP-Routing) introduces action intent into the language model by pruning instruction-irrelevant visually grounded tokens, thereby achieving token-level sparsity. 3) To ensure that compressed perception inputs can still support accurate and coherent action generation, we introduce V-L-A Coupled Attention (CAtten), which combines causal vision-language attention with bidirectional action parallel decoding. Extensive experiments on the LIBERO benchmark and real-world robotic tasks demonstrate that CogVLA achieves state-of-the-art performance with success rates of 97.4% and 70.0%, respectively, while reducing training costs by 2.5-fold and decreasing inference latency by 2.8-fold compared to OpenVLA. CogVLA is open-sourced and publicly available at https://github.com/JiuTian-VL/CogVLA.

## Content
Recent Vision-Language-Action (VLA) models built on pre-trained Vision-Language Models (VLMs) require extensive post-training, resulting in high computational overhead that limits scalability and deployment. We propose CogVLA, a Cognition-Aligned Vision-Language-Action framework that leverages instruction-driven routing and sparsification to improve both efficiency and performance. CogVLA draws inspiration from human multimodal coordination and introduces a 3-stage progressive architecture. 1) Encoder-FiLM based Aggregation Routing (EFA-Routing) injects instruction information into the vision encoder to selectively aggregate and compress dual-stream visual tokens, forming an instruction-aware latent representation. 2) Building upon this compact visual encoding, LLM-FiLM based Pruning Routing (LFP-Routing) introduces action intent into the language model by pruning instruction-irrelevant visually grounded tokens, thereby achieving token-level sparsity. 3) To ensure that compressed perception inputs can still support accurate and coherent action generation, we introduce V-L-A Coupled Attention (CAtten), which combines causal vision-language attention with bidirectional action parallel decoding. Extensive experiments on the LIBERO benchmark and real-world robotic tasks demonstrate that CogVLA achieves state-of-the-art performance with success rates of 97.4% and 70.0%, respectively, while reducing training costs by 2.5-fold and decreasing inference latency by 2.8-fold compared to OpenVLA. CogVLA is open-sourced and publicly available at https://github.com/JiuTian-VL/CogVLA.

## 参考
- http://arxiv.org/abs/2508.21046v3

## 개요
CogVLA는 기존 VLA 모델의 후훈련(post-training) 계산 비용이 큰 문제를 해결하기 위해 3단계 점진적 아키텍처를 제안한다. 핵심 혁신은 다음과 같다: EFA-Routing은 FiLM 메커니즘을 통해 명령을 시각 인코더에 주입하여 이중 스트림 시각 토큰을 압축한다; LFP-Routing은 LLM 가지치기를 활용해 명령과 무관한 시각 토큰을 제거하여 희소화를 구현한다; CAtten은 인과적 시각-언어 어텐션과 양방향 동작 병렬 디코딩을 결합한다. 실험 결과, 이 모델은 LIBERO 벤치마크와 실제 로봇 작업에서 모두 최적의 성능을 달성했다.

## 핵심 내용
### 방법 아키텍처
CogVLA는 3단계 점진적 설계를 채택한다:
- **EFA-Routing**: FiLM 기반 인코더 집계 라우팅으로, 명령 정보를 시각 인코더에 주입하고 이중 스트림 시각 토큰을 선택적으로 집계 및 압축하여 명령 인지적 암시적 표현을 형성한다.
- **LFP-Routing**: LLM 기반 가지치기 라우팅으로, 동작 의도를 도입하여 명령과 무관한 시각 토큰을 가지치기하고 토큰 수준 희소화를 구현한다.
- **CAtten**: V-L-A 결합 어텐션 메커니즘으로, 인과적 시각-언어 어텐션과 양방향 동작 병렬 디코딩을 결합하여 압축된 인식 입력에서도 정확하고 일관된 동작을 생성할 수 있도록 보장한다.

### 실험 설정
- **벤치마크 테스트**: LIBERO 벤치마크에서 평가하며, 다양한 로봇 조작 작업을 포함한다.
- **실제 시나리오**: 실제 로봇 작업에서 일반화 능력을 검증한다.
- **비교 기준선**: OpenVLA 등 모델과 효율성 및 성능을 비교한다.

### 주요 결과
- **성공률**: LIBERO 벤치마크에서 97.4%, 실제 작업에서 70.0%를 달성.
- **효율성 향상**: 훈련 비용 2.5배 절감, 추론 지연 시간 2.8배 감소.
- **오픈소스**: 코드와 모델은 https://github.com/JiuTian-VL/CogVLA에서 공개.

### 결론
CogVLA는 명령 기반 라우팅과 희소화를 통해 높은 성능을 유지하면서 계산 비용을 크게 줄여 VLA 모델의 확장 가능한 배포에 효과적인 솔루션을 제공한다.
