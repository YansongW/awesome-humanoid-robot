---
$id: ent_paper_koo_retovla_reusing_register_token_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models'
  zh: RetoVLA
  ko: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models'
summary:
  en: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (RetoVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by School of Computing, Gachon University.'
  zh: RetoVLA 是韩国嘉泉大学计算机学院于 2025 年提出的大型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于复用 Vision Transformer 中的 Register Tokens（原本用于缓解注意力伪影的可学习参数）来保持轻量级模型的空间感知能力，无需增加参数量即可恢复全局空间上下文。
  ko: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (RetoVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by School of Computing, Gachon University.'
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
- retovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21243v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2509.21243
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RetoVLA source
  url: https://doi.org/10.48550/arXiv.2509.21243
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型虽在机器人任务中表现优异，但高内存与计算需求限制了其实时部署。传统模型压缩方法虽能减少参数量，却常导致 3D 空间推理与场景布局理解能力下降。RetoVLA 通过将原本被丢弃的 Register Tokens 重新利用，将其密集的全局空间上下文表征直接注入动作规划模块，设计了一条专用的空间上下文注入路径。该方法在不增加总参数量的前提下恢复了全局上下文，在 7 自由度机械臂的真实实验中，平均成功率相比基线提升了 17.1 个百分点。

## 核心内容
### 方法架构
- **核心思想**：复用 Vision Transformer 中的 Register Tokens（一种可学习参数，最初用于减少注意力伪影），将其从“一次性使用”转变为“空间上下文载体”。
- **空间上下文注入路径**：将回收的 Register Tokens 通过专用路径直接馈入动作规划模块，使轻量级模型也能保持对场景布局的全局理解。
- **参数效率**：整个设计不增加模型总参数量，仅通过重新利用已有 token 实现空间感知能力的恢复。

### 实验设置
- **硬件平台**：7 自由度机械臂，用于真实世界操作任务。
- **基线对比**：与未使用 Register Tokens 的轻量级 VLA 模型进行对比。
- **评估指标**：任务平均成功率。

### 关键结果
- **性能提升**：RetoVLA 在真实实验中平均成功率比基线高出 17.1 个百分点（绝对提升）。
- **结论**：复用内部 Register Tokens 是开发高效且具备空间感知能力的机器人智能体的有效机制。

### 附加资源
- 视频演示：https://youtu.be/2CseBR-snZg

## Overview
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens-learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg

## 개요
Vision-Language-Action (VLA) 모델은 다양한 로봇 작업에서 강력한 성능을 입증했습니다. 그러나 높은 메모리 및 계산 요구로 인해 실시간 배포가 제한되는 경우가 많습니다. 기존 모델 압축 기술은 파라미터 크기를 줄이지만, 3D 공간 추론 및 장면 레이아웃 이해에서 성능 저하가 자주 발생합니다. 본 연구는 Register Tokens(비전 트랜스포머에서 주의 아티팩트를 완화하기 위해 도입된 학습 가능한 파라미터)을 재활용하여 경량 모델에서 공간 인식을 유지하도록 설계된 아키텍처인 RetoVLA를 소개합니다. 이러한 토큰은 일반적으로 사용 후 폐기되지만, 우리는 이를 전역 공간 컨텍스트의 밀집 표현을 위해 재활용합니다. RetoVLA는 전용 공간 컨텍스트 주입 경로를 통해 이러한 재활용 토큰을 행동 계획 모듈에 직접 통합합니다. 제안된 설계는 총 파라미터 수를 증가시키지 않으면서 전역 컨텍스트를 복구할 수 있게 합니다. 7-DOF 매니퓰레이터를 사용한 실제 실험에서 기준선 대비 평균 성공률이 17.1%p 향상되었습니다. 본 결과는 내부 레지스터 토큰을 활용하는 것이 효율적이고 공간 인식이 가능한 로봇 에이전트를 개발하는 데 매우 효과적인 메커니즘을 제공함을 보여줍니다. 비디오 데모는 다음에서 확인할 수 있습니다: https://youtu.be/2CseBR-snZg

## 핵심 내용
Vision-Language-Action (VLA) 모델은 다양한 로봇 작업에서 강력한 성능을 입증했습니다. 그러나 높은 메모리 및 계산 요구로 인해 실시간 배포가 제한되는 경우가 많습니다. 기존 모델 압축 기술은 파라미터 크기를 줄이지만, 3D 공간 추론 및 장면 레이아웃 이해에서 성능 저하가 자주 발생합니다. 본 연구는 Register Tokens(비전 트랜스포머에서 주의 아티팩트를 완화하기 위해 도입된 학습 가능한 파라미터)을 재활용하여 경량 모델에서 공간 인식을 유지하도록 설계된 아키텍처인 RetoVLA를 소개합니다. 이러한 토큰은 일반적으로 사용 후 폐기되지만, 우리는 이를 전역 공간 컨텍스트의 밀집 표현을 위해 재활용합니다. RetoVLA는 전용 공간 컨텍스트 주입 경로를 통해 이러한 재활용 토큰을 행동 계획 모듈에 직접 통합합니다. 제안된 설계는 총 파라미터 수를 증가시키지 않으면서 전역 컨텍스트를 복구할 수 있게 합니다. 7-DOF 매니퓰레이터를 사용한 실제 실험에서 기준선 대비 평균 성공률이 17.1%p 향상되었습니다. 본 결과는 내부 레지스터 토큰을 활용하는 것이 효율적이고 공간 인식이 가능한 로봇 에이전트를 개발하는 데 매우 효과적인 메커니즘을 제공함을 보여줍니다. 비디오 데모는 다음에서 확인할 수 있습니다: https://youtu.be/2CseBR-snZg

## Overview
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens—learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg

## Content
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens—learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg

## 参考
- http://arxiv.org/abs/2509.21243v2
