---
$id: ent_paper_yin_mivla_towards_generalizable_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training'
  zh: MiVLA
  ko: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training'
summary:
  en: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training (MiVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of Electronic
    Science and Technology of China.'
  zh: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training (MiVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of Electronic
    Science and Technology of China.'
  ko: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training (MiVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of Electronic
    Science and Technology of China.'
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
- mivla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15411v2.
sources:
- id: src_001
  type: paper
  title: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training (arXiv)'
  url: https://arxiv.org/abs/2512.15411
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MiVLA source
  url: https://doi.org/10.48550/arXiv.2512.15411
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

## 核心内容
While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

## 参考
- http://arxiv.org/abs/2512.15411v2

## Overview
While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbol\pi_{0}$, $\boldsymbol\pi_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

## Content
While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbol\pi_{0}$, $\boldsymbol\pi_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

## 개요
풍부한 인간 비디오와 시뮬레이션 로봇 데이터를 활용하는 것은 실제 로봇 데이터 부족 문제에 대한 확장 가능한 해결책을 제시하지만, 기존의 시각-언어-행동 모델(VLA)의 일반화 능력은 카메라 시점, 시각적 외관, 구현체 형태의 불일치로 인해 여전히 제한적입니다. 이러한 한계를 극복하기 위해, 우리는 인간-로봇 상호 모방 사전 학습을 기반으로 하는 일반화 가능한 VLA인 MiVLA를 제안합니다. 이는 인간 손과 로봇 팔 사이의 본질적인 행동 유사성을 활용하여 인간 행동과 로봇 제어 모두에 강력한 행동 사전 지식의 기반을 구축합니다. 구체적으로, 우리의 방법은 왼손/오른손 좌표계를 사용한 운동학적 규칙을 활용하여 인간과 로봇의 행동 공간 간 양방향 정렬을 수행합니다. 인간 또는 시뮬레이션 로봇 시연이 주어지면, MiVLA는 한 구현체의 행동 궤적을 예측하고 시연에서 보지 못한 다른 구현체의 행동을 모방하도록 훈련됩니다. 이러한 상호 모방을 기반으로, 실제 인간 데이터의 행동 충실도와 시뮬레이션 로봇 데이터의 조작 다양성을 통합 모델에 결합하여 하위 작업에 대한 일반화 능력을 향상시킵니다. 세 가지 로봇(ARX, PiPer, LocoMan)을 사용한 시뮬레이션 및 실제 플랫폼에서의 광범위한 실험을 통해, MiVLA는 강력한 향상된 일반화 능력을 달성하며, 최첨단 VLA(예: $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$, H-RDT)를 시뮬레이션에서 25%, 실제 로봇 제어 작업에서 14% 능가함을 입증했습니다.

## 핵심 내용
풍부한 인간 비디오와 시뮬레이션 로봇 데이터를 활용하는 것은 실제 로봇 데이터 부족 문제에 대한 확장 가능한 해결책을 제시하지만, 기존의 시각-언어-행동 모델(VLA)의 일반화 능력은 카메라 시점, 시각적 외관, 구현체 형태의 불일치로 인해 여전히 제한적입니다. 이러한 한계를 극복하기 위해, 우리는 인간-로봇 상호 모방 사전 학습을 기반으로 하는 일반화 가능한 VLA인 MiVLA를 제안합니다. 이는 인간 손과 로봇 팔 사이의 본질적인 행동 유사성을 활용하여 인간 행동과 로봇 제어 모두에 강력한 행동 사전 지식의 기반을 구축합니다. 구체적으로, 우리의 방법은 왼손/오른손 좌표계를 사용한 운동학적 규칙을 활용하여 인간과 로봇의 행동 공간 간 양방향 정렬을 수행합니다. 인간 또는 시뮬레이션 로봇 시연이 주어지면, MiVLA는 한 구현체의 행동 궤적을 예측하고 시연에서 보지 못한 다른 구현체의 행동을 모방하도록 훈련됩니다. 이러한 상호 모방을 기반으로, 실제 인간 데이터의 행동 충실도와 시뮬레이션 로봇 데이터의 조작 다양성을 통합 모델에 결합하여 하위 작업에 대한 일반화 능력을 향상시킵니다. 세 가지 로봇(ARX, PiPer, LocoMan)을 사용한 시뮬레이션 및 실제 플랫폼에서의 광범위한 실험을 통해, MiVLA는 강력한 향상된 일반화 능력을 달성하며, 최첨단 VLA(예: $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$, H-RDT)를 시뮬레이션에서 25%, 실제 로봇 제어 작업에서 14% 능가함을 입증했습니다.
