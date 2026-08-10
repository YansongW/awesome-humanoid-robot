---
$id: ent_paper_towards_spatial_trace_with_rea_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
  zh: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
  ko: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
summary:
  en: 'arXiv:2512.13660v4 Announce Type: replace Abstract: Spatial tracing, as a fundamental embodied interaction ability
    for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial
    referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this
    end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal
    spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover,
    RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process
    rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training,
    we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting
    complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the
    gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding,
    measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench
    by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control
    policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes.
    Please see the project page at https://zhoues.github.io/RoboTracer.'
  zh: RoboTracer 是一个面向机器人空间追踪能力的 3D 感知视觉语言模型，由研究团队提出。其核心贡献在于通过通用空间编码器与回归监督解码器实现 3D 空间指代与测量，并利用基于度量敏感过程奖励的强化微调（RFT）推进多步度量推理。该模型在
    TraceSpatial-Bench 基准上以 79.1% 的平均成功率超越 Gemini-2.5-Pro 达 36% 的准确率提升。
  ko: 'arXiv:2512.13660v4 Announce Type: replace Abstract: Spatial tracing, as a fundamental embodied interaction ability
    for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial
    referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this
    end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal
    spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover,
    RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process
    rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training,
    we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting
    complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the
    gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding,
    measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench
    by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control
    policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes.
    Please see the project page at https://zhoues.github.io/RoboTracer.'
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
- robotics
- towards_spatial_trace_with_rea
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13660v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (965 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics (arXiv)
  url: https://arxiv.org/abs/2512.13660
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
RoboTracer 针对机器人空间追踪这一需要多步度量推理与复杂空间指代结合的挑战性任务，提出了一种 3D 感知视觉语言模型。该模型通过监督微调（SFT）阶段引入通用空间编码器和回归监督解码器，增强了尺度感知能力；同时采用基于度量敏感过程奖励的强化微调（RFT）方法，监督关键中间感知线索以生成精确的空间轨迹。为支持训练，团队构建了包含 3000 万问答对的大规模数据集 TraceSpatial，覆盖室外、室内和桌面场景，并支持最多 9 步的复杂推理过程。实验表明，RoboTracer 在空间理解、测量和指代任务上均超越基线，并在 TraceSpatial-Bench 上以显著优势达到最优性能。

## 核心内容
### 方法架构
- **3D 感知视觉语言模型**：RoboTracer 采用通用空间编码器（universal spatial encoder）将 3D 空间信息编码为视觉特征，并通过回归监督解码器（regression-supervised decoder）直接输出度量值，从而在 SFT 阶段增强模型的尺度感知能力。
- **多步度量推理**：通过强化微调（RFT）引入度量敏感过程奖励（metric-sensitive process rewards），对关键中间感知线索（如物体位置、距离估计）进行监督，引导模型逐步生成准确的空间轨迹。

### 训练数据与基准
- **TraceSpatial 数据集**：包含 3000 万问答对，覆盖室外、室内和桌面场景，支持最多 9 步的复杂推理过程，用于 SFT 和 RFT 训练。
- **TraceSpatial-Bench 基准**：专门用于评估空间追踪能力的挑战性基准，填补了该领域的评估空白。

### 实验设置与结果
- **性能对比**：RoboTracer 在空间理解、测量和指代任务上均超越基线，平均成功率达 79.1%。在 TraceSpatial-Bench 上，其准确率超过 Gemini-2.5-Pro 达 36%，以显著优势达到最优性能（SOTA）。
- **实际部署**：RoboTracer 可与多种控制策略集成，在杂乱的真实场景中执行长时域、动态任务，已成功部署于 UR5 和 G1 人形机器人等不同平台。

## Overview
Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer.

## 参考
- http://arxiv.org/abs/2512.13660v4

## 개요
RoboTracer는 다단계 측정 추론과 복잡한 공간 지시를 결합해야 하는 도전적인 작업인 로봇 공간 추적을 위해 3D 인식 비전-언어 모델을 제안합니다. 이 모델은 지도 미세 조정(SFT) 단계에서 범용 공간 인코더와 회귀 감독 디코더를 도입하여 스케일 인식 능력을 강화합니다. 동시에 측정 민감 프로세스 보상 기반의 강화 미세 조정(RFT) 방법을 채택하여 핵심 중간 인식 단서를 감독하여 정밀한 공간 궤적을 생성합니다. 훈련을 지원하기 위해 팀은 3천만 개의 질의응답 쌍을 포함하는 대규모 데이터셋 TraceSpatial을 구축했으며, 실외, 실내, 데스크톱 장면을 포괄하고 최대 9단계의 복잡한 추론 과정을 지원합니다. 실험 결과 RoboTracer는 공간 이해, 측정 및 지시 작업에서 기준선을 능가하며, TraceSpatial-Bench에서 현저한 우위로 최적 성능을 달성했습니다.

## 핵심 내용
### 방법 아키텍처
- **3D 인식 비전-언어 모델**: RoboTracer는 범용 공간 인코더(universal spatial encoder)를 사용하여 3D 공간 정보를 시각적 특징으로 인코딩하고, 회귀 감독 디코더(regression-supervised decoder)를 통해 측정 값을 직접 출력하여 SFT 단계에서 모델의 스케일 인식 능력을 강화합니다.
- **다단계 측정 추론**: 강화 미세 조정(RFT)을 통해 측정 민감 프로세스 보상(metric-sensitive process rewards)을 도입하여 핵심 중간 인식 단서(예: 객체 위치, 거리 추정)를 감독하고, 모델이 단계적으로 정확한 공간 궤적을 생성하도록 유도합니다.

### 훈련 데이터 및 벤치마크
- **TraceSpatial 데이터셋**: 3천만 개의 질의응답 쌍을 포함하며, 실외, 실내, 데스크톱 장면을 포괄하고 최대 9단계의 복잡한 추론 과정을 지원하여 SFT 및 RFT 훈련에 사용됩니다.
- **TraceSpatial-Bench 벤치마크**: 공간 추적 능력을 평가하기 위한 도전적인 벤치마크로, 해당 분야의 평가 공백을 메웁니다.

### 실험 설정 및 결과
- **성능 비교**: RoboTracer는 공간 이해, 측정 및 지시 작업에서 기준선을 능가하며 평균 성공률 79.1%를 달성합니다. TraceSpatial-Bench에서 Gemini-2.5-Pro보다 정확도가 36% 높아 현저한 우위로 최적 성능(SOTA)을 달성합니다.
- **실제 배포**: RoboTracer는 다양한 제어 전략과 통합될 수 있으며, 복잡한 실제 장면에서 장시간 동적 작업을 수행할 수 있습니다. UR5 및 G1 휴머노이드 로봇과 같은 다양한 플랫폼에 성공적으로 배포되었습니다.
