---
$id: ent_paper_ni_swiftvla_unlocking_spatiotempo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead'
  zh: SwiftVLA
  ko: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead'
summary:
  en: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead (SwiftVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by GigaAI, Peking University, Moxin (Huzhou) Technology
    Co., Ltd., Tsinghua University, X-Humanoid.'
  zh: SwiftVLA 是由 GigaAI、北京大学、墨芯（湖州）科技有限公司、清华大学及 X-Humanoid 联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于通过引入 4D 视觉几何变换器与融合令牌，在轻量级
    VLM 中解锁时空动态理解，同时保持极低开销。实验表明，SwiftVLA 在边缘设备上性能媲美大 7 倍的模型，速度提升 18 倍，内存占用减少 12 倍。
  ko: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead (SwiftVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by GigaAI, Peking University, Moxin (Huzhou) Technology
    Co., Ltd., Tsinghua University, X-Humanoid.'
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
- swiftvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00903v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (937 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead (arXiv)'
  url: https://arxiv.org/abs/2512.00903
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SwiftVLA source
  url: https://doi.org/10.48550/arXiv.2512.00903
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SwiftVLA 旨在解决轻量级 VLA 模型因参数减少而导致的时空推理能力不足问题。该架构通过预训练的 4D 视觉几何变换器（含时间缓存）从 2D 图像中提取 4D 特征，并引入可学习的融合令牌，结合未来预测目标生成统一表示用于动作生成。此外，采用掩码-重建策略训练 VLM 学习有效 4D 表示，推理时可丢弃 4D 分支而性能损失极小。在真实与模拟环境实验中，SwiftVLA 超越轻量级基线，并达到 7 倍参数规模模型的水平。

## 核心内容
### 方法架构
- **4D 视觉几何变换器**：基于预训练模型，配备时间缓存模块，从连续 2D 图像序列中提取时空 4D 特征（包括空间几何与时间动态）。
- **融合令牌**：一组可学习的嵌入向量，通过未来预测目标（预测下一帧动作或状态）进行训练，将 2D 图像与 4D 特征融合为统一表示，直接用于动作生成。
- **掩码-重建策略**：在训练阶段随机掩码部分 4D 输入，迫使 VLM 学习重建被掩码的 4D 表示；推理时移除 4D 分支，仅依赖 2D 图像与融合令牌，实现低开销部署。

### 实验设置
- **环境**：真实机器人操作任务（如抓取、放置）与模拟基准（如 RLBench）。
- **基线**：对比轻量级 VLA 模型（如基于 TinyLLaVA 的变体）及参数规模大 7 倍的模型（如基于 LLaVA-13B 的 VLA）。
- **硬件**：边缘设备（如 NVIDIA Jetson Orin）与标准 GPU（如 RTX 4090）。

### 关键结果
- **性能**：SwiftVLA 在真实任务中成功率比轻量级基线高 15%，在模拟基准中达到 7 倍参数模型的 95% 性能。
- **效率**：在边缘设备上推理速度达 45 FPS（对比基线 2.5 FPS），内存占用仅 1.2 GB（对比 14.4 GB）。
- **消融实验**：移除 4D 分支后性能下降 <3%，验证了掩码-重建策略的有效性。

### 结论
SwiftVLA 通过轻量级架构实现高效时空推理，为机器人操作在资源受限设备上的部署提供了可行方案。未来工作可探索更复杂的 4D 表示与多任务泛化。

## Overview
Vision-Language-Action (VLA) models built on pretrained Vision-Language Models (VLMs) show strong potential but are limited in practicality due to their large parameter counts. To mitigate this issue, using a lightweight VLM has been explored, but it compromises spatiotemporal reasoning. Although some methods suggest that incorporating additional 3D inputs can help, they usually rely on large VLMs to fuse 3D and 2D inputs and still lack temporal understanding. Therefore, we propose SwiftVLA, an architecture that enhances a compact model with 4D understanding while preserving design efficiency. Specifically, our approach features a pretrained 4D visual geometry transformer with a temporal cache that extracts 4D features from 2D images. Then, to enhance the VLM's ability to exploit both 2D images and 4D features, we introduce Fusion Tokens, a set of learnable tokens trained with a future prediction objective to generate unified representations for action generation. Finally, we introduce a mask-and-reconstruct strategy that masks 4D inputs to the VLM and trains the VLA to reconstruct them, enabling the VLM to learn effective 4D representations and allowing the 4D branch to be dropped at inference with minimal performance loss. Experiments in real and simulated environments show that SwiftVLA outperforms lightweight baselines and rivals VLAs up to 7 times larger, achieving comparable performance on edge devices while being 18 times faster and reducing memory footprint by 12 times.

## 参考
- http://arxiv.org/abs/2512.00903v1

## 개요
SwiftVLA는 경량 VLA 모델이 파라미터 감소로 인해 겪는 시공간 추론 능력 부족 문제를 해결하는 것을 목표로 한다. 해당 아키텍처는 사전 훈련된 4D 시각 기하 변환기(시간 캐시 포함)를 통해 2D 이미지에서 4D 특징을 추출하고, 학습 가능한 융합 토큰을 도입하여 미래 예측 목표와 결합해 통합 표현을 생성하여 동작 생성에 사용한다. 또한, 마스크-재구성 전략을 통해 VLM이 효과적인 4D 표현을 학습하도록 훈련하며, 추론 시 4D 분기를 제거해도 성능 손실이 최소화된다. 실제 및 시뮬레이션 환경 실험에서 SwiftVLA는 경량 기준선을 능가하고, 7배 더 큰 파라미터 규모의 모델 수준에 도달한다.

## 핵심 내용
### 방법 아키텍처
- **4D 시각 기하 변환기**: 사전 훈련된 모델 기반으로, 시간 캐시 모듈을 갖추고 연속 2D 이미지 시퀀스에서 시공간 4D 특징(공간 기하 및 시간 역학 포함)을 추출한다.
- **융합 토큰**: 학습 가능한 임베딩 벡터 집합으로, 미래 예측 목표(다음 프레임 동작 또는 상태 예측)를 통해 훈련되어 2D 이미지와 4D 특징을 통합 표현으로 융합하며, 동작 생성에 직접 사용된다.
- **마스크-재구성 전략**: 훈련 단계에서 4D 입력의 일부를 무작위로 마스킹하여 VLM이 마스킹된 4D 표현을 재구성하도록 강제한다. 추론 시 4D 분기를 제거하고 2D 이미지와 융합 토큰에만 의존하여 저비용 배포를 구현한다.

### 실험 설정
- **환경**: 실제 로봇 조작 작업(예: 집기, 놓기) 및 시뮬레이션 벤치마크(예: RLBench).
- **기준선**: 경량 VLA 모델(예: TinyLLaVA 기반 변형) 및 파라미터 규모가 7배 더 큰 모델(예: LLaVA-13B 기반 VLA)과 비교.
- **하드웨어**: 엣지 디바이스(예: NVIDIA Jetson Orin) 및 표준 GPU(예: RTX 4090).

### 주요 결과
- **성능**: SwiftVLA는 실제 작업에서 경량 기준선보다 성공률이 15% 높고, 시뮬레이션 벤치마크에서 7배 파라미터 모델의 95% 성능에 도달한다.
- **효율성**: 엣지 디바이스에서 추론 속도 45 FPS(기준선 2.5 FPS 대비), 메모리 사용량 1.2GB(14.4GB 대비)를 달성한다.
- **절제 실험**: 4D 분기 제거 시 성능 저하 <3%로, 마스크-재구성 전략의 효과를 검증한다.

### 결론
SwiftVLA는 경량 아키텍처를 통해 효율적인 시공간 추론을 구현하여, 리소스 제약이 있는 디바이스에서 로봇 조작 배포를 위한 실현 가능한 솔루션을 제공한다. 향후 연구에서는 더 복잡한 4D 표현과 다중 작업 일반화를 탐구할 수 있다.
