---
$id: ent_paper_li_towards_deploying_vla_without_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary
    Diffusion'
  zh: VLA-Pilot
  ko: 'Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary
    Diffusion'
summary:
  en: 'Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary
    Diffusion (VLA-Pilot), is a 2025 large vision-language-action model for robotic manipulation, introduced by The Chinese
    University of Hong Kong, T-Stone Robotics Institute, Hong Kong Center for Logistics Robotics, Department of Advanced Robotics,
    Istituto Italiano di Tecnologia.'
  zh: VLA-Pilot 是由香港中文大学、T-Stone 机器人研究所、香港物流机器人中心及意大利技术研究院联合提出的即插即用推理时策略引导方法，用于零样本部署预训练 VLA 模型。其核心贡献在于无需微调或额外数据收集，通过具身进化扩散机制提升下游操作任务的成功率。
  ko: 'Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary
    Diffusion (VLA-Pilot), is a 2025 large vision-language-action model for robotic manipulation, introduced by The Chinese
    University of Hong Kong, T-Stone Robotics Institute, Hong Kong Center for Logistics Robotics, Department of Advanced Robotics,
    Istituto Italiano di Tecnologia.'
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
- vla_pilot
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14178v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (783 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary
    Diffusion (arXiv)'
  url: https://arxiv.org/abs/2511.14178
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Pilot source
  url: https://doi.org/10.48550/arXiv.2511.14178
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA-Pilot 针对预训练 VLA 模型在下游部署中性能显著下降的问题，提出了一种无需微调的推理时策略引导方案。该方法通过具身进化扩散机制，在零样本场景下直接调整预训练模型的输出行为，避免了传统微调所需的高成本演示数据采集和密集计算。在六项真实世界下游操作任务（涵盖分布内与分布外场景）及两种不同机器人本体上的实验表明，VLA-Pilot 能显著提升现成预训练 VLA 策略的成功率，实现鲁棒的零样本泛化。

## 核心内容
### 方法概述
VLA-Pilot 的核心是一种即插即用的推理时策略引导框架，无需修改预训练 VLA 模型的权重或收集新数据。它通过具身进化扩散（Embodied Evolutionary Diffusion）机制，在推理阶段动态优化动作输出，使预训练策略能适应未见过的任务和机器人本体。

### 实验设置
- **任务与场景**：在六项真实世界下游操作任务上评估，涵盖分布内（in-distribution）和分布外（out-of-distribution）场景。
- **机器人本体**：使用两种不同的机器人平台，验证方法的跨本体泛化能力。
- **基线对比**：直接使用未经微调的现成预训练 VLA 策略作为基线。

### 关键结果
- **性能提升**：VLA-Pilot 在所有六项任务上均显著提高了成功率，尤其在分布外场景中，提升幅度更为明显。
- **零样本泛化**：无需任何微调或额外数据，即可实现对新任务和新本体的鲁棒适应。
- **即插即用特性**：方法可直接集成到现有预训练 VLA 策略中，无需修改模型架构或训练流程。

### 结论
VLA-Pilot 为预训练 VLA 模型的实际部署提供了一种高效、低成本的解决方案，通过推理时引导克服了微调依赖数据与计算资源的瓶颈。实验代码和视频已开源。

## Overview
Vision-Language-Action (VLA) models have demonstrated significant potential in real-world robotic manipulation. However, pre-trained VLA policies still suffer from substantial performance degradation during downstream deployment. Although fine-tuning can mitigate this issue, its reliance on costly demonstration collection and intensive computation makes it impractical in real-world settings. In this work, we introduce VLA-Pilot, a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection. We evaluate VLA-Pilot on six real-world downstream manipulation tasks across two distinct robotic embodiments, encompassing both in-distribution and out-of-distribution scenarios. Experimental results demonstrate that VLA-Pilot substantially boosts the success rates of off-the-shelf pre-trained VLA policies, enabling robust zero-shot generalization to diverse tasks and embodiments. Experimental videos and code are available at: https://rip4kobe.github.io/vla-pilot/.

## 参考
- http://arxiv.org/abs/2511.14178v2

## 개요
VLA-Pilot은 사전 훈련된 VLA 모델이 다운스트림 배포에서 성능이 현저히 저하되는 문제를 해결하기 위해, 미세 조정 없이 추론 시점에 정책을 안내하는 방안을 제시합니다. 이 방법은 구현된 진화 확산 메커니즘을 통해 제로샷 시나리오에서 사전 훈련된 모델의 출력 동작을 직접 조정하여, 전통적인 미세 조정에 필요한 고비용의 시연 데이터 수집과 집중적인 계산을 피합니다. 여섯 가지 실제 세계 다운스트림 조작 작업(분포 내 및 분포 외 시나리오 포함)과 두 가지 서로 다른 로봇 플랫폼에서의 실험은 VLA-Pilot이 기성 사전 훈련된 VLA 정책의 성공률을 크게 향상시키고, 강력한 제로샷 일반화를 달성함을 보여줍니다.

## 핵심 내용
### 방법 개요
VLA-Pilot의 핵심은 사전 훈련된 VLA 모델의 가중치를 수정하거나 새로운 데이터를 수집할 필요 없이, 플러그 앤 플레이 방식의 추론 시점 정책 안내 프레임워크입니다. 구현된 진화 확산(Embodied Evolutionary Diffusion) 메커니즘을 통해 추론 단계에서 동작 출력을 동적으로 최적화하여, 사전 훈련된 정책이 보지 못한 작업과 로봇 플랫폼에 적응할 수 있게 합니다.

### 실험 설정
- **작업 및 시나리오**: 여섯 가지 실제 세계 다운스트림 조작 작업에서 평가하며, 분포 내(in-distribution) 및 분포 외(out-of-distribution) 시나리오를 포함합니다.
- **로봇 플랫폼**: 두 가지 서로 다른 로봇 플랫폼을 사용하여 방법의 교차 플랫폼 일반화 능력을 검증합니다.
- **기준 비교**: 미세 조정 없이 기성 사전 훈련된 VLA 정책을 직접 사용하는 것을 기준선으로 삼습니다.

### 주요 결과
- **성능 향상**: VLA-Pilot은 모든 여섯 가지 작업에서 성공률을 크게 향상시켰으며, 특히 분포 외 시나리오에서 향상 폭이 더 두드러집니다.
- **제로샷 일반화**: 미세 조정이나 추가 데이터 없이도 새로운 작업과 플랫폼에 대한 강력한 적응을 달성합니다.
- **플러그 앤 플레이 특성**: 이 방법은 기존 사전 훈련된 VLA 정책에 직접 통합할 수 있으며, 모델 아키텍처나 훈련 프로세스를 수정할 필요가 없습니다.

### 결론
VLA-Pilot은 사전 훈련된 VLA 모델의 실제 배포를 위한 효율적이고 저비용의 솔루션을 제공하며, 추론 시점 안내를 통해 미세 조정이 데이터와 계산 자원에 의존하는 병목 현상을 극복합니다. 실험 코드와 비디오는 오픈소스로 공개되었습니다.
