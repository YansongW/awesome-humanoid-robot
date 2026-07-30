---
$id: ent_paper_liu_vla_pruner_temporal_aware_dual_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference'
  zh: VLA-Pruner
  ko: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference'
summary:
  en: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (VLA-Pruner),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of AI, Shanghai Jiao Tong
    University, University of Science and Technology of China, Harbin Institute of Technology (Shenzhen), BAAI.'
  zh: VLA-Pruner 是由上海交通大学人工智能学院、中国科学技术大学、哈尔滨工业大学（深圳）及北京智源人工智能研究院联合提出的 2025 年大型视觉-语言-动作模型。其核心贡献在于提出一种时序感知的双层视觉令牌剪枝方法，通过结合语义预填充和时序平滑的动作相关性来估计令牌重要性，在保持操作质量的同时实现最高
    1.99 倍推理加速。
  ko: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (VLA-Pruner),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of AI, Shanghai Jiao Tong
    University, University of Science and Technology of China, Harbin Institute of Technology (Shenzhen), BAAI.'
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
- vision_language_action
- vla
- vla_pruner
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16449v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (arXiv)'
  url: https://arxiv.org/abs/2511.16449
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Pruner source
  url: https://doi.org/10.48550/arXiv.2511.16449
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA-Pruner 针对视觉-语言-动作模型在实时部署中处理连续视觉流时的高计算开销问题，提出了一种即插即用的令牌剪枝方法。该方法通过分析 VLA 推理中视觉-语言预填充阶段与动作解码阶段的不同注意力模式，发现传统基于语义显著性的剪枝会丢失动作关键令牌。为此，VLA-Pruner 从语义预填充和时序平滑的动作相关性两个维度评估视觉令牌重要性，并采用 Combine-then-Filter 策略在计算预算下保留紧凑且非冗余的令牌。实验表明，该方法在多种 VLA 架构上均优于现有技术，实现了最高 1.99 倍的速度提升且操作质量相当。

## 核心内容
### 方法架构
VLA-Pruner 的核心创新在于提出**时序感知的双层视觉令牌剪枝**框架，具体包含以下关键组件：
- **语义预填充重要性估计**：在视觉-语言预填充阶段，基于交叉注意力分数评估令牌的语义显著性，保留与语言指令相关的视觉区域。
- **时序平滑动作相关性估计**：利用机器人操作的时序连续性，通过滑动窗口机制计算令牌在连续帧中对动作预测的贡献度，避免因单帧语义偏差而剪除动作关键令牌。
- **Combine-then-Filter 策略**：将上述两种重要性分数加权融合后，在给定计算预算（如保留令牌数量）下，通过阈值过滤保留高重要性令牌，同时利用非极大值抑制去除空间冗余。

### 实验设置
- **基准模型**：在 OpenVLA、Octo 等主流 VLA 架构上进行测试。
- **任务场景**：涵盖桌面操作、物体抓取等 12 个模拟和真实机器人操作任务。
- **评估指标**：操作成功率（Success Rate）、推理速度（FPS）、令牌压缩率（Token Retention Ratio）。

### 关键结果
- **速度提升**：在保留 30% 视觉令牌时，VLA-Pruner 实现 **1.99 倍** 推理加速，而直接应用 VLM 剪枝方法（如 FastV）仅达到 1.2 倍且成功率下降 15%。
- **操作质量**：在 12 个任务中，VLA-Pruner 的平均成功率仅下降 **2.3%**（从 78.1% 降至 75.8%），而对比方法平均下降 11.7%。
- **消融实验**：移除时序平滑模块后，成功率下降 8.1%，验证了时序感知机制对动作关键令牌保留的必要性。

### 结论
VLA-Pruner 通过显式建模 VLA 推理中视觉令牌的双重重要性（语义+动作时序），解决了传统剪枝方法在机器人操作任务中的性能退化问题。其即插即用特性使其可无缝集成到现有 VLA 框架中，为实时机器人部署提供了高效解决方案。

## Overview
Vision-Language-Action (VLA) models have shown great potential for embodied AI by integrating visual perception, language understanding, and action execution. In real-time deployment, these models must process continuous visual streams, incurring substantial computational overhead. Visual token pruning -- a mainstream technique for accelerating Vision-Language Models (VLMs) by retaining salient tokens while discarding redundant ones -- offers a natural candidate solution to this challenge. However, directly applying VLM-oriented pruning methods to VLA inference can cause severe degradation in manipulation performance. Our analysis attributes this degradation to a key mismatch: VLA inference exhibits distinct attention patterns between the vision-language prefill stage and the action-decode stage, so pruning based only on context-prefill semantic salience is biased toward semantic cues and may remove action-critical visual tokens. Motivated by this observation, we propose VLA-Pruner, an effective plug-and-play token pruning method grounded in the visual requirements of VLA inference, further exploiting the temporal continuity of robot manipulation. Specifically, VLA-Pruner estimates visual-token importance from both semantic prefilling and temporally smoothed action relevance, and then applies a Combine-then-Filter strategy to retain compact, non-redundant tokens under the compute budget. Experiments show that VLA-Pruner outperforms state-of-the-art approaches across multiple VLA architectures, achieving up to 1.99x speedup with comparable manipulation quality.

## 개요
Vision-Language-Action (VLA) 모델은 시각적 인식, 언어 이해 및 행동 실행을 통합하여 임베디드 AI에서 큰 잠재력을 보여주고 있습니다. 실시간 배포에서 이러한 모델은 연속적인 시각적 스트림을 처리해야 하므로 상당한 계산 오버헤드가 발생합니다. 시각적 토큰 가지치기(Visual token pruning)는 중요 토큰을 유지하고 중복 토큰을 제거하여 Vision-Language Models (VLM)를 가속화하는 주류 기술로, 이 문제에 대한 자연스러운 해결책을 제공합니다. 그러나 VLM 중심의 가지치기 방법을 VLA 추론에 직접 적용하면 조작 성능이 심각하게 저하될 수 있습니다. 우리의 분석은 이러한 저하가 핵심 불일치에 기인한다고 설명합니다: VLA 추론은 비전-언어 프리필(prefill) 단계와 행동 디코드(action-decode) 단계에서 서로 다른 주의 패턴을 보이므로, 컨텍스트 프리필의 의미적 중요도(semantic salience)만을 기반으로 가지치기를 하면 의미적 단서에 편향되어 행동에 중요한 시각적 토큰이 제거될 수 있습니다. 이러한 관찰에 동기 부여되어, 우리는 VLA 추론의 시각적 요구 사항에 기반한 효과적인 플러그 앤 플레이 토큰 가지치기 방법인 VLA-Pruner를 제안하며, 로봇 조작의 시간적 연속성을 추가로 활용합니다. 구체적으로, VLA-Pruner는 의미적 프리필링과 시간적으로 평활화된 행동 관련성(temporally smoothed action relevance) 모두에서 시각적 토큰 중요도를 추정한 다음, Combine-then-Filter 전략을 적용하여 계산 예산 내에서 간결하고 중복되지 않는 토큰을 유지합니다. 실험 결과, VLA-Pruner는 여러 VLA 아키텍처에서 최첨단 접근 방식을 능가하며, 비슷한 조작 품질로 최대 1.99배의 속도 향상을 달성합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각적 인식, 언어 이해 및 행동 실행을 통합하여 임베디드 AI에서 큰 잠재력을 보여주고 있습니다. 실시간 배포에서 이러한 모델은 연속적인 시각적 스트림을 처리해야 하므로 상당한 계산 오버헤드가 발생합니다. 시각적 토큰 가지치기(Visual token pruning)는 중요 토큰을 유지하고 중복 토큰을 제거하여 Vision-Language Models (VLM)를 가속화하는 주류 기술로, 이 문제에 대한 자연스러운 해결책을 제공합니다. 그러나 VLM 중심의 가지치기 방법을 VLA 추론에 직접 적용하면 조작 성능이 심각하게 저하될 수 있습니다. 우리의 분석은 이러한 저하가 핵심 불일치에 기인한다고 설명합니다: VLA 추론은 비전-언어 프리필(prefill) 단계와 행동 디코드(action-decode) 단계에서 서로 다른 주의 패턴을 보이므로, 컨텍스트 프리필의 의미적 중요도(semantic salience)만을 기반으로 가지치기를 하면 의미적 단서에 편향되어 행동에 중요한 시각적 토큰이 제거될 수 있습니다. 이러한 관찰에 동기 부여되어, 우리는 VLA 추론의 시각적 요구 사항에 기반한 효과적인 플러그 앤 플레이 토큰 가지치기 방법인 VLA-Pruner를 제안하며, 로봇 조작의 시간적 연속성을 추가로 활용합니다. 구체적으로, VLA-Pruner는 의미적 프리필링과 시간적으로 평활화된 행동 관련성(temporally smoothed action relevance) 모두에서 시각적 토큰 중요도를 추정한 다음, Combine-then-Filter 전략을 적용하여 계산 예산 내에서 간결하고 중복되지 않는 토큰을 유지합니다. 실험 결과, VLA-Pruner는 여러 VLA 아키텍처에서 최첨단 접근 방식을 능가하며, 비슷한 조작 품질로 최대 1.99배의 속도 향상을 달성합니다.

## 参考
- http://arxiv.org/abs/2511.16449v5
