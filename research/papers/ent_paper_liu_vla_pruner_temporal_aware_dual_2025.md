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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16449v5. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1126 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.16449v5

## 개요
VLA-Pruner는 시각-언어-행동 모델이 실시간 배포에서 연속적인 시각 스트림을 처리할 때 발생하는 높은 계산 비용 문제를 해결하기 위해, 플러그 앤 플레이 방식의 토큰 프루닝 방법을 제안합니다. 이 방법은 VLA 추론에서 시각-언어 사전 채움 단계와 행동 디코딩 단계의 서로 다른 어텐션 패턴을 분석하여, 기존의 의미적 유의성 기반 프루닝이 행동 핵심 토큰을 손실한다는 점을 발견합니다. 이를 위해 VLA-Pruner는 의미적 사전 채움과 시간적 평활화된 행동 관련성의 두 가지 차원에서 시각 토큰 중요도를 평가하고, Combine-then-Filter 전략을 사용하여 계산 예산 하에서 컴팩트하고 비중복적인 토큰을 유지합니다. 실험 결과, 이 방법은 다양한 VLA 아키텍처에서 기존 기술보다 우수하며, 최대 1.99배의 속도 향상과 동등한 조작 품질을 달성합니다.

## 핵심 내용
### 방법 아키텍처
VLA-Pruner의 핵심 혁신은 **시간적 인식 이중 계층 시각 토큰 프루닝** 프레임워크를 제안하는 것이며, 구체적으로 다음 핵심 구성 요소를 포함합니다:
- **의미적 사전 채움 중요도 추정**: 시각-언어 사전 채움 단계에서 교차 어텐션 점수를 기반으로 토큰의 의미적 유의성을 평가하여, 언어 명령과 관련된 시각 영역을 유지합니다.
- **시간적 평활화된 행동 관련성 추정**: 로봇 조작의 시간적 연속성을 활용하여, 슬라이딩 윈도우 메커니즘을 통해 연속 프레임에서 토큰이 행동 예측에 기여하는 정도를 계산하여, 단일 프레임의 의미적 편차로 인해 행동 핵심 토큰이 제거되는 것을 방지합니다.
- **Combine-then-Filter 전략**: 위의 두 중요도 점수를 가중 융합한 후, 주어진 계산 예산(예: 유지 토큰 수) 하에서 임계값 필터링을 통해 높은 중요도 토큰을 유지하고, 비최대 억제를 사용하여 공간적 중복을 제거합니다.

### 실험 설정
- **기준 모델**: OpenVLA, Octo 등 주요 VLA 아키텍처에서 테스트.
- **작업 시나리오**: 데스크톱 조작, 객체 파지 등 12개의 시뮬레이션 및 실제 로봇 조작 작업 포함.
- **평가 지표**: 조작 성공률(Success Rate), 추론 속도(FPS), 토큰 압축률(Token Retention Ratio).

### 주요 결과
- **속도 향상**: 시각 토큰의 30%를 유지할 때, VLA-Pruner는 **1.99배** 추론 가속을 달성하며, VLM 프루닝 방법(예: FastV)을 직접 적용한 경우 1.2배에 그치고 성공률이 15% 하락합니다.
- **조작 품질**: 12개 작업에서 VLA-Pruner의 평균 성공률은 **2.3%**만 하락하며(78.1%에서 75.8%로), 비교 방법은 평균 11.7% 하락합니다.
- **절제 실험**: 시간적 평활화 모듈을 제거하면 성공률이 8.1% 하락하여, 시간적 인식 메커니즘이 행동 핵심 토큰 유지에 필수적임을 검증합니다.

### 결론
VLA-Pruner는 VLA 추론에서 시각 토큰의 이중 중요도(의미+행동 시간적)를 명시적으로 모델링하여, 기존 프루닝 방법이 로봇 조작 작업에서 발생하는 성능 저하 문제를 해결합니다. 플러그 앤 플레이 특성 덕분에 기존 VLA 프레임워크에 원활하게 통합될 수 있으며, 실시간 로봇 배포를 위한 효율적인 솔루션을 제공합니다.
