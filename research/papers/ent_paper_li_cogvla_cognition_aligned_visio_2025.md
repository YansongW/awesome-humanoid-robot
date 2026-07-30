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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.21046v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
최근 사전 훈련된 Vision-Language Models(VLM)을 기반으로 구축된 Vision-Language-Action(VLA) 모델은 광범위한 사후 훈련이 필요하여 높은 계산 오버헤드를 초래하며 확장성과 배포에 제약을 줍니다. 본 논문에서는 명령 기반 라우팅과 희소화를 활용하여 효율성과 성능을 모두 개선하는 인지 정렬 Vision-Language-Action 프레임워크인 CogVLA를 제안합니다. CogVLA는 인간의 다중 모달 협력에서 영감을 받아 3단계 점진적 아키텍처를 도입합니다. 1) Encoder-FiLM 기반 집계 라우팅(EFA-Routing)은 명령 정보를 비전 인코더에 주입하여 이중 스트림 시각 토큰을 선택적으로 집계 및 압축하고 명령 인식 잠재 표현을 형성합니다. 2) 이 컴팩트한 시각적 인코딩을 기반으로 LLM-FiLM 기반 가지치기 라우팅(LFP-Routing)은 명령과 무관한 시각적 기반 토큰을 가지치기하여 언어 모델에 행동 의도를 도입함으로써 토큰 수준의 희소성을 달성합니다. 3) 압축된 인식 입력이 여전히 정확하고 일관된 행동 생성을 지원할 수 있도록 하기 위해 인과적 시각-언어 주의와 양방향 행동 병렬 디코딩을 결합한 V-L-A 결합 주의(CAtten)를 도입합니다. LIBERO 벤치마크 및 실제 로봇 작업에 대한 광범위한 실험을 통해 CogVLA는 각각 97.4%와 70.0%의 성공률로 최첨단 성능을 달성하면서도 OpenVLA 대비 훈련 비용을 2.5배 절감하고 추론 지연 시간을 2.8배 감소시킵니다. CogVLA는 오픈소스로 제공되며 https://github.com/JiuTian-VL/CogVLA에서 공개적으로 이용 가능합니다.

## 핵심 내용
최근 사전 훈련된 Vision-Language Models(VLM)을 기반으로 구축된 Vision-Language-Action(VLA) 모델은 광범위한 사후 훈련이 필요하여 높은 계산 오버헤드를 초래하며 확장성과 배포에 제약을 줍니다. 본 논문에서는 명령 기반 라우팅과 희소화를 활용하여 효율성과 성능을 모두 개선하는 인지 정렬 Vision-Language-Action 프레임워크인 CogVLA를 제안합니다. CogVLA는 인간의 다중 모달 협력에서 영감을 받아 3단계 점진적 아키텍처를 도입합니다. 1) Encoder-FiLM 기반 집계 라우팅(EFA-Routing)은 명령 정보를 비전 인코더에 주입하여 이중 스트림 시각 토큰을 선택적으로 집계 및 압축하고 명령 인식 잠재 표현을 형성합니다. 2) 이 컴팩트한 시각적 인코딩을 기반으로 LLM-FiLM 기반 가지치기 라우팅(LFP-Routing)은 명령과 무관한 시각적 기반 토큰을 가지치기하여 언어 모델에 행동 의도를 도입함으로써 토큰 수준의 희소성을 달성합니다. 3) 압축된 인식 입력이 여전히 정확하고 일관된 행동 생성을 지원할 수 있도록 하기 위해 인과적 시각-언어 주의와 양방향 행동 병렬 디코딩을 결합한 V-L-A 결합 주의(CAtten)를 도입합니다. LIBERO 벤치마크 및 실제 로봇 작업에 대한 광범위한 실험을 통해 CogVLA는 각각 97.4%와 70.0%의 성공률로 최첨단 성능을 달성하면서도 OpenVLA 대비 훈련 비용을 2.5배 절감하고 추론 지연 시간을 2.8배 감소시킵니다. CogVLA는 오픈소스로 제공되며 https://github.com/JiuTian-VL/CogVLA에서 공개적으로 이용 가능합니다.

## 参考
- http://arxiv.org/abs/2508.21046v3
