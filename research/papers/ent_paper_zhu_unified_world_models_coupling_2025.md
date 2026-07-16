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
  zh: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (UWM), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Paul G. Allen School of Computer Science and
    Engineering, University of Washington, Toyota Research Institute, and published at RSS26.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.02792v3.
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
Imitation learning has emerged as a promising approach towards building generalist robots. However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations. Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available. This data provides a rich source of information about real-world dynamics and agent-environment interactions. Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation. In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning. Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator. Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies. Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling. Videos and code are available at https://weirdlabuw.github.io/uwm/.

## 核心内容
Imitation learning has emerged as a promising approach towards building generalist robots. However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations. Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available. This data provides a rich source of information about real-world dynamics and agent-environment interactions. Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation. In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning. Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator. Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies. Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling. Videos and code are available at https://weirdlabuw.github.io/uwm/.

## 参考
- http://arxiv.org/abs/2504.02792v3

## Overview
Imitation learning has emerged as a promising approach towards building generalist robots. However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations. Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available. This data provides a rich source of information about real-world dynamics and agent-environment interactions. Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation. In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning. Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator. Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies. Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling. Videos and code are available at https://weirdlabuw.github.io/uwm/.

## Content
Imitation learning has emerged as a promising approach towards building generalist robots. However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations. Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available. This data provides a rich source of information about real-world dynamics and agent-environment interactions. Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation. In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning. Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator. Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies. Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling. Videos and code are available at https://weirdlabuw.github.io/uwm/.

## 개요
모방 학습은 범용 로봇을 구축하기 위한 유망한 접근 방식으로 부상했습니다. 그러나 대규모 로봇 기반 모델을 위한 모방 학습의 확장은 고품질 전문가 시연에 의존하기 때문에 여전히 어려움을 겪고 있습니다. 한편, 다양한 환경과 다양한 행동을 묘사하는 대량의 비디오 데이터를 쉽게 이용할 수 있습니다. 이 데이터는 실제 세계의 역학 및 에이전트-환경 상호작용에 대한 풍부한 정보 소스를 제공합니다. 그러나 행동 주석이 없기 때문에 이 데이터를 모방 학습에 직접 활용하는 것은 어려운 것으로 입증되었습니다. 본 연구에서는 정책 학습을 위해 비디오와 행동 데이터를 모두 활용할 수 있는 프레임워크인 UWM(Unified World Models)을 제시합니다. 구체적으로, UWM은 통합된 트랜스포머 아키텍처 내에서 행동 확산 과정과 비디오 확산 과정을 통합하며, 각 모달리티는 독립적인 확산 타임스텝에 의해 제어됩니다. 각 확산 타임스텝을 제어함으로써 UWM은 정책, 순방향 역학, 역방향 역학 및 비디오 생성기를 유연하게 표현할 수 있습니다. 시뮬레이션 및 실제 환경 실험을 통해 다음을 보여줍니다: (1) UWM은 역학 및 행동 예측을 모두 포함한 대규모 멀티태스크 로봇 데이터셋에서 효과적인 사전 학습을 가능하게 하여 모방 학습보다 더 일반화 가능하고 강력한 정책을 생성합니다. (2) UWM은 모달리티별 확산 타임스텝의 독립적인 제어를 통해 행동이 없는 비디오 데이터로부터의 학습을 자연스럽게 촉진하여 미세 조정된 정책의 성능을 더욱 향상시킵니다. 우리의 결과는 UWM이 확장 가능한 로봇 학습을 위한 대규모 이질적 데이터셋을 활용하는 유망한 단계를 제공하며, 종종 이질적인 모방 학습과 세계 모델링 패러다임 간의 간단한 통합을 제공함을 시사합니다. 비디오 및 코드는 https://weirdlabuw.github.io/uwm/에서 확인할 수 있습니다.

## 핵심 내용
모방 학습은 범용 로봇을 구축하기 위한 유망한 접근 방식으로 부상했습니다. 그러나 대규모 로봇 기반 모델을 위한 모방 학습의 확장은 고품질 전문가 시연에 의존하기 때문에 여전히 어려움을 겪고 있습니다. 한편, 다양한 환경과 다양한 행동을 묘사하는 대량의 비디오 데이터를 쉽게 이용할 수 있습니다. 이 데이터는 실제 세계의 역학 및 에이전트-환경 상호작용에 대한 풍부한 정보 소스를 제공합니다. 그러나 행동 주석이 없기 때문에 이 데이터를 모방 학습에 직접 활용하는 것은 어려운 것으로 입증되었습니다. 본 연구에서는 정책 학습을 위해 비디오와 행동 데이터를 모두 활용할 수 있는 프레임워크인 UWM(Unified World Models)을 제시합니다. 구체적으로, UWM은 통합된 트랜스포머 아키텍처 내에서 행동 확산 과정과 비디오 확산 과정을 통합하며, 각 모달리티는 독립적인 확산 타임스텝에 의해 제어됩니다. 각 확산 타임스텝을 제어함으로써 UWM은 정책, 순방향 역학, 역방향 역학 및 비디오 생성기를 유연하게 표현할 수 있습니다. 시뮬레이션 및 실제 환경 실험을 통해 다음을 보여줍니다: (1) UWM은 역학 및 행동 예측을 모두 포함한 대규모 멀티태스크 로봇 데이터셋에서 효과적인 사전 학습을 가능하게 하여 모방 학습보다 더 일반화 가능하고 강력한 정책을 생성합니다. (2) UWM은 모달리티별 확산 타임스텝의 독립적인 제어를 통해 행동이 없는 비디오 데이터로부터의 학습을 자연스럽게 촉진하여 미세 조정된 정책의 성능을 더욱 향상시킵니다. 우리의 결과는 UWM이 확장 가능한 로봇 학습을 위한 대규모 이질적 데이터셋을 활용하는 유망한 단계를 제공하며, 종종 이질적인 모방 학습과 세계 모델링 패러다임 간의 간단한 통합을 제공함을 시사합니다. 비디오 및 코드는 https://weirdlabuw.github.io/uwm/에서 확인할 수 있습니다.
