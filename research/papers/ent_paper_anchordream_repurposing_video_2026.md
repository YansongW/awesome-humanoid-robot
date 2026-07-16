---
$id: ent_paper_anchordream_repurposing_video_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
  zh: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
  ko: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
summary:
  en: 'arXiv:2512.11797v2 Announce Type: replace Abstract: The collection of large-scale and diverse robot demonstrations
    remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited
    diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing
    methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies
    that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model
    that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process
    on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments
    consistent with the robot''s kinematics. Starting from only a handful of human teleoperation demonstrations, our method
    scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show
    that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in
    simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative
    world models in robot motion provides a practical path toward scaling imitation learning.'
  zh: 'arXiv:2512.11797v2 Announce Type: replace Abstract: The collection of large-scale and diverse robot demonstrations
    remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited
    diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing
    methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies
    that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model
    that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process
    on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments
    consistent with the robot''s kinematics. Starting from only a handful of human teleoperation demonstrations, our method
    scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show
    that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in
    simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative
    world models in robot motion provides a practical path toward scaling imitation learning.'
  ko: 'arXiv:2512.11797v2 Announce Type: replace Abstract: The collection of large-scale and diverse robot demonstrations
    remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited
    diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing
    methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies
    that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model
    that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process
    on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments
    consistent with the robot''s kinematics. Starting from only a handful of human teleoperation demonstrations, our method
    scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show
    that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in
    simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative
    world models in robot motion provides a practical path toward scaling imitation learning.'
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
- anchordream
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11797v2.
sources:
- id: src_001
  type: paper
  title: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis (arXiv)'
  url: https://arxiv.org/abs/2512.11797
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

## 核心内容
The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

## 参考
- http://arxiv.org/abs/2512.11797v2

## Overview
The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

## Content
The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

## 개요
대규모의 다양한 로봇 시연 데이터 수집은 모방 학습의 주요 병목 현상으로 남아 있습니다. 실제 데이터 획득은 비용이 많이 들고, 시뮬레이터는 제한된 다양성과 정확성을 제공하며 시뮬레이션-실제 간 차이가 두드러지기 때문입니다. 생성 모델이 매력적인 해결책을 제시하지만, 기존 방법은 종종 새로운 행동을 생성하지 않고 시각적 외관만 변경하거나, 신체적 불일치로 인해 비현실적인 움직임을 초래합니다. 이러한 한계를 극복하기 위해, 우리는 AnchorDream을 소개합니다. 이는 사전 훈련된 비디오 확산 모델을 로봇 데이터 합성에 재활용하는 신체 인식 세계 모델입니다. AnchorDream은 로봇 동작 렌더링에 확산 과정을 조건화하여, 로봇의 운동학과 일치하는 객체와 환경을 합성하면서 환각을 방지하기 위해 신체를 고정합니다. 소수의 인간 원격 조작 시연만으로 시작하여, 명시적인 환경 모델링 없이도 이를 대규모의 다양하고 고품질의 데이터셋으로 확장합니다. 실험 결과, 생성된 데이터는 하위 정책 학습에서 일관된 개선을 가져오며, 시뮬레이터 벤치마크에서 36.4%의 상대적 향상과 실제 연구에서 거의 두 배의 성능을 보였습니다. 이러한 결과는 생성적 세계 모델을 로봇 동작에 기반하는 것이 모방 학습 확장을 위한 실용적인 경로를 제공함을 시사합니다.

## 핵심 내용
대규모의 다양한 로봇 시연 데이터 수집은 모방 학습의 주요 병목 현상으로 남아 있습니다. 실제 데이터 획득은 비용이 많이 들고, 시뮬레이터는 제한된 다양성과 정확성을 제공하며 시뮬레이션-실제 간 차이가 두드러지기 때문입니다. 생성 모델이 매력적인 해결책을 제시하지만, 기존 방법은 종종 새로운 행동을 생성하지 않고 시각적 외관만 변경하거나, 신체적 불일치로 인해 비현실적인 움직임을 초래합니다. 이러한 한계를 극복하기 위해, 우리는 AnchorDream을 소개합니다. 이는 사전 훈련된 비디오 확산 모델을 로봇 데이터 합성에 재활용하는 신체 인식 세계 모델입니다. AnchorDream은 로봇 동작 렌더링에 확산 과정을 조건화하여, 로봇의 운동학과 일치하는 객체와 환경을 합성하면서 환각을 방지하기 위해 신체를 고정합니다. 소수의 인간 원격 조작 시연만으로 시작하여, 명시적인 환경 모델링 없이도 이를 대규모의 다양하고 고품질의 데이터셋으로 확장합니다. 실험 결과, 생성된 데이터는 하위 정책 학습에서 일관된 개선을 가져오며, 시뮬레이터 벤치마크에서 36.4%의 상대적 향상과 실제 연구에서 거의 두 배의 성능을 보였습니다. 이러한 결과는 생성적 세계 모델을 로봇 동작에 기반하는 것이 모방 학습 확장을 위한 실용적인 경로를 제공함을 시사합니다.
