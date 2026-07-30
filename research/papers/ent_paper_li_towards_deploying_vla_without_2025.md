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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14178v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-Language-Action (VLA) 모델은 실제 로봇 조작 분야에서 상당한 잠재력을 입증했습니다. 그러나 사전 훈련된 VLA 정책은 다운스트림 배포 시 여전히 상당한 성능 저하를 겪습니다. 파인튜닝이 이 문제를 완화할 수 있지만, 고비용의 시연 수집과 집중적인 계산에 의존하기 때문에 실제 환경에서는 실용적이지 않습니다. 본 연구에서는 추가적인 파인튜닝이나 데이터 수집 없이 사전 훈련된 VLA의 제로샷 배포를 위한 플러그 앤 플레이 방식의 추론 시간 정책 조정 방법인 VLA-Pilot을 소개합니다. 우리는 두 가지 서로 다른 로봇 체계에 걸쳐 여섯 가지 실제 다운스트림 조작 작업에서 VLA-Pilot을 평가했으며, 이는 분포 내 및 분포 외 시나리오를 모두 포함합니다. 실험 결과는 VLA-Pilot이 기성 사전 훈련된 VLA 정책의 성공률을 크게 향상시켜 다양한 작업과 체계에 대한 강력한 제로샷 일반화를 가능하게 함을 보여줍니다. 실험 비디오와 코드는 다음에서 확인할 수 있습니다: https://rip4kobe.github.io/vla-pilot/.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 실제 로봇 조작 분야에서 상당한 잠재력을 입증했습니다. 그러나 사전 훈련된 VLA 정책은 다운스트림 배포 시 여전히 상당한 성능 저하를 겪습니다. 파인튜닝이 이 문제를 완화할 수 있지만, 고비용의 시연 수집과 집중적인 계산에 의존하기 때문에 실제 환경에서는 실용적이지 않습니다. 본 연구에서는 추가적인 파인튜닝이나 데이터 수집 없이 사전 훈련된 VLA의 제로샷 배포를 위한 플러그 앤 플레이 방식의 추론 시간 정책 조정 방법인 VLA-Pilot을 소개합니다. 우리는 두 가지 서로 다른 로봇 체계에 걸쳐 여섯 가지 실제 다운스트림 조작 작업에서 VLA-Pilot을 평가했으며, 이는 분포 내 및 분포 외 시나리오를 모두 포함합니다. 실험 결과는 VLA-Pilot이 기성 사전 훈련된 VLA 정책의 성공률을 크게 향상시켜 다양한 작업과 체계에 대한 강력한 제로샷 일반화를 가능하게 함을 보여줍니다. 실험 비디오와 코드는 다음에서 확인할 수 있습니다: https://rip4kobe.github.io/vla-pilot/.

## 参考
- http://arxiv.org/abs/2511.14178v2
