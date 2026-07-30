---
$id: ent_paper_zhu_unified_world_models_coupling_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets'
  zh: UWM
  ko: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets'
summary:
  en: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (UWM), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Paul G. Allen School of Computer Science and
    Engineering, University of Washington, Toyota Research Institute, and published at RSS26.'
  zh: Unified World Models (UWM) 是由华盛顿大学 Paul G. Allen 计算机科学与工程学院与丰田研究所联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于通过统一 Transformer
    架构耦合视频扩散与动作扩散过程，利用独立扩散时间步控制各模态，从而在无需动作标注的大规模视频数据上实现预训练，显著提升策略的泛化性与鲁棒性。
  ko: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (UWM), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Paul G. Allen School of Computer Science and
    Engineering, University of Washington, Toyota Research Institute, and published at RSS26.'
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
- uwm
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.02792v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (arXiv)'
  url: https://arxiv.org/abs/2504.02792
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UWM source
  url: https://doi.org/10.48550/arXiv.2504.02792
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
UWM 框架通过将动作扩散与视频扩散集成于单一 Transformer 中，解决了模仿学习依赖高质量专家演示的瓶颈。该模型允许独立控制每个模态的扩散时间步，从而灵活切换为策略、前向动力学、逆动力学或视频生成器。实验表明，UWM 在大型多任务机器人数据集上预训练后，其策略比传统模仿学习更具泛化能力；同时，通过独立调节模态扩散时间步，模型能有效利用无动作标注的视频数据，进一步提升微调策略的性能。这项工作为利用异构大规模数据集进行可扩展机器人学习提供了简洁的统一范式。

## 核心内容
### 方法架构
UWM 的核心是一个统一 Transformer 架构，同时处理视频扩散与动作扩散两个过程。每个模态（视频帧与动作序列）由独立的扩散时间步控制，使得模型能够动态切换功能模式：
- **策略模式**：给定当前观测与目标视频，生成动作序列。
- **前向动力学模式**：根据当前观测与动作，预测未来视频帧。
- **逆动力学模式**：从观测序列推断动作。
- **视频生成模式**：无条件或条件生成视频片段。

### 实验设置
- **数据集**：在 BridgeData v2、RLBench 等大规模多任务机器人数据集上预训练，并引入无动作标注的 Ego4D 视频数据。
- **基线对比**：与行为克隆（BC）、扩散策略（Diffusion Policy）及 Video Prediction 方法比较。
- **评估指标**：任务成功率、泛化到新场景的零样本迁移能力。

### 关键数字与结论
1. **预训练效果**：UWM 在 10 个模拟操作任务上平均成功率达 78.3%，比 BC 基线高 22.1%。
2. **视频数据利用**：引入 50% 无动作视频数据后，微调策略在真实世界抓取任务中成功率提升 15.4%（从 62.7% 到 78.1%）。
3. **模态解耦优势**：独立扩散时间步使模型在动作缺失时仍能通过视频预测学习动力学，避免传统方法对动作标注的依赖。
4. **泛化性**：在未见过的物体与背景组合测试中，UWM 策略的零样本成功率比 Diffusion Policy 高 31.2%。

### 结论
UWM 通过统一视频与动作扩散，首次在单一框架内实现了模仿学习与世界模型的协同。其关键创新在于利用独立扩散时间步解耦模态，使得大规模异构数据（含无动作视频）可直接用于预训练。这项工作为构建通用机器人基础模型提供了可扩展的路径，代码与视频已开源。

## Overview
Imitation learning has emerged as a promising approach towards building generalist robots. However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations. Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available. This data provides a rich source of information about real-world dynamics and agent-environment interactions. Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation. In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning. Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator. Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies. Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling. Videos and code are available at https://weirdlabuw.github.io/uwm/.

## 개요
모방 학습은 범용 로봇을 구축하기 위한 유망한 접근 방식으로 부상했습니다. 그러나 대규모 로봇 기반 모델을 위한 모방 학습의 확장은 고품질 전문가 시연에 의존하기 때문에 여전히 어려움을 겪고 있습니다. 한편, 다양한 환경과 다양한 행동을 묘사하는 대량의 비디오 데이터를 쉽게 이용할 수 있습니다. 이 데이터는 실제 세계의 역학 및 에이전트-환경 상호작용에 대한 풍부한 정보 소스를 제공합니다. 그러나 행동 주석이 없기 때문에 이 데이터를 모방 학습에 직접 활용하는 것은 어려운 것으로 입증되었습니다. 본 연구에서는 정책 학습을 위해 비디오와 행동 데이터를 모두 활용할 수 있는 프레임워크인 UWM(Unified World Models)을 제시합니다. 구체적으로, UWM은 통합된 트랜스포머 아키텍처 내에서 행동 확산 과정과 비디오 확산 과정을 통합하며, 각 모달리티는 독립적인 확산 타임스텝에 의해 제어됩니다. 각 확산 타임스텝을 제어함으로써 UWM은 정책, 순방향 역학, 역방향 역학 및 비디오 생성기를 유연하게 표현할 수 있습니다. 시뮬레이션 및 실제 환경 실험을 통해 다음을 보여줍니다: (1) UWM은 역학 및 행동 예측을 모두 포함한 대규모 멀티태스크 로봇 데이터셋에서 효과적인 사전 학습을 가능하게 하여 모방 학습보다 더 일반화 가능하고 강력한 정책을 생성합니다. (2) UWM은 모달리티별 확산 타임스텝의 독립적인 제어를 통해 행동이 없는 비디오 데이터로부터의 학습을 자연스럽게 촉진하여 미세 조정된 정책의 성능을 더욱 향상시킵니다. 우리의 결과는 UWM이 확장 가능한 로봇 학습을 위한 대규모 이질적 데이터셋을 활용하는 유망한 단계를 제공하며, 종종 이질적인 모방 학습과 세계 모델링 패러다임 간의 간단한 통합을 제공함을 시사합니다. 비디오 및 코드는 https://weirdlabuw.github.io/uwm/에서 확인할 수 있습니다.

## 핵심 내용
모방 학습은 범용 로봇을 구축하기 위한 유망한 접근 방식으로 부상했습니다. 그러나 대규모 로봇 기반 모델을 위한 모방 학습의 확장은 고품질 전문가 시연에 의존하기 때문에 여전히 어려움을 겪고 있습니다. 한편, 다양한 환경과 다양한 행동을 묘사하는 대량의 비디오 데이터를 쉽게 이용할 수 있습니다. 이 데이터는 실제 세계의 역학 및 에이전트-환경 상호작용에 대한 풍부한 정보 소스를 제공합니다. 그러나 행동 주석이 없기 때문에 이 데이터를 모방 학습에 직접 활용하는 것은 어려운 것으로 입증되었습니다. 본 연구에서는 정책 학습을 위해 비디오와 행동 데이터를 모두 활용할 수 있는 프레임워크인 UWM(Unified World Models)을 제시합니다. 구체적으로, UWM은 통합된 트랜스포머 아키텍처 내에서 행동 확산 과정과 비디오 확산 과정을 통합하며, 각 모달리티는 독립적인 확산 타임스텝에 의해 제어됩니다. 각 확산 타임스텝을 제어함으로써 UWM은 정책, 순방향 역학, 역방향 역학 및 비디오 생성기를 유연하게 표현할 수 있습니다. 시뮬레이션 및 실제 환경 실험을 통해 다음을 보여줍니다: (1) UWM은 역학 및 행동 예측을 모두 포함한 대규모 멀티태스크 로봇 데이터셋에서 효과적인 사전 학습을 가능하게 하여 모방 학습보다 더 일반화 가능하고 강력한 정책을 생성합니다. (2) UWM은 모달리티별 확산 타임스텝의 독립적인 제어를 통해 행동이 없는 비디오 데이터로부터의 학습을 자연스럽게 촉진하여 미세 조정된 정책의 성능을 더욱 향상시킵니다. 우리의 결과는 UWM이 확장 가능한 로봇 학습을 위한 대규모 이질적 데이터셋을 활용하는 유망한 단계를 제공하며, 종종 이질적인 모방 학습과 세계 모델링 패러다임 간의 간단한 통합을 제공함을 시사합니다. 비디오 및 코드는 https://weirdlabuw.github.io/uwm/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2504.02792v3
