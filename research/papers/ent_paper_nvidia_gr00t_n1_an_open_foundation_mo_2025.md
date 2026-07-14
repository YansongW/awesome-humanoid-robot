---
$id: ent_paper_nvidia_gr00t_n1_an_open_foundation_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'
  zh: GR00T N1：面向通用人形机器人的开放基础模型
  ko: 'GR00T N1: 범용 휴머노이드 로봇을 위한 오픈 파운데이션 모델'
summary:
  en: GR00T N1 is a dual-system Vision-Language-Action (VLA) foundation model for humanoid robots, combining an Eagle-2 vision-language
    reasoning module with a flow-matching Diffusion Transformer for real-time motor action generation, and is trained end-to-end
    on a heterogeneous mixture of real-robot trajectories, human videos, and synthetic data.
  zh: GR00T N1 是一个面向人形机器人的双系统视觉-语言-动作（VLA）基础模型，结合 Eagle-2 视觉-语言推理模块与流匹配扩散 Transformer 实现实时运动动作生成，并以真实机器人轨迹、人类视频与合成数据的异构混合进行端到端训练。
  ko: GR00T N1은 휴머노이드 로봇을 위한 이중 시스템 비전-언어-행동(VLA) 파운데이션 모델로, Eagle-2 비전-언어 추론 모듈과 실시간 모터 행동 생성을 위한 플로우 매칭 디퓨전 트랜스포머를 결합하며
    실제 로봇 궤적, 인간 비디오 및 합성 데이터의 이종 혼합물로 종단간 학습된다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- vla
- foundation_model
- humanoid_manipulation
- diffusion_transformer
- cross_embodiment
- bimanual_manipulation
- imitation_learning
- fourier_gr1
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.14734v2.
sources:
- id: src_001
  type: paper
  title: 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'
  url: https://arxiv.org/abs/2503.14734
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: uses
  description:
    en: GR00T N1 training data includes the Open X-Embodiment dataset as part of its heterogeneous data pyramid.
    zh: GR00T N1 的训练数据包含 Open X-Embodiment 数据集，作为其异构数据金字塔的一部分。
    ko: GR00T N1의 학습 데이터는 이종 데이터 피라미드의 일환으로 Open X-Embodiment 데이터셋을 포함한다.
---
## 概述
General-purpose robots need a versatile body and an intelligent mind. Recent advancements in humanoid robots have shown great promise as a hardware platform for building generalist autonomy in the human world. A robot foundation model, trained on massive and diverse data sources, is essential for enabling the robots to reason about novel situations, robustly handle real-world variability, and rapidly learn new tasks. To this end, we introduce GR00T N1, an open foundation model for humanoid robots. GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture. The vision-language module (System 2) interprets the environment through vision and language instructions. The subsequent diffusion transformer module (System 1) generates fluid motor actions in real time. Both modules are tightly coupled and jointly trained end-to-end. We train GR00T N1 with a heterogeneous mixture of real-robot trajectories, human videos, and synthetically generated datasets. We show that our generalist robot model GR00T N1 outperforms the state-of-the-art imitation learning baselines on standard simulation benchmarks across multiple robot embodiments. Furthermore, we deploy our model on the Fourier GR-1 humanoid robot for language-conditioned bimanual manipulation tasks, achieving strong performance with high data efficiency.

## 核心内容
General-purpose robots need a versatile body and an intelligent mind. Recent advancements in humanoid robots have shown great promise as a hardware platform for building generalist autonomy in the human world. A robot foundation model, trained on massive and diverse data sources, is essential for enabling the robots to reason about novel situations, robustly handle real-world variability, and rapidly learn new tasks. To this end, we introduce GR00T N1, an open foundation model for humanoid robots. GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture. The vision-language module (System 2) interprets the environment through vision and language instructions. The subsequent diffusion transformer module (System 1) generates fluid motor actions in real time. Both modules are tightly coupled and jointly trained end-to-end. We train GR00T N1 with a heterogeneous mixture of real-robot trajectories, human videos, and synthetically generated datasets. We show that our generalist robot model GR00T N1 outperforms the state-of-the-art imitation learning baselines on standard simulation benchmarks across multiple robot embodiments. Furthermore, we deploy our model on the Fourier GR-1 humanoid robot for language-conditioned bimanual manipulation tasks, achieving strong performance with high data efficiency.

## 参考
- http://arxiv.org/abs/2503.14734v2

