---
$id: ent_paper_unveiling_the_impact_of_data_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots
  zh: 揭示数据和模型扩展对人形机器人高级控制的影响
  ko: Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots
summary:
  en: Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion
    data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to
    the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video,
    extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this,
    we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours
    of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset
    can be further expanded via the same pipeline. Building on this data resource
  zh: 这篇工作先从人类视频/动捕轨迹恢复场景、目标或运动表征，再用扩散策略/流匹配生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: 这篇工作先从人类视频/动捕轨迹恢复场景、目标或运动表征，再用扩散策略/流匹配生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generative_motion
- language_control
- motion_generation
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Unveiling the Impact of
    Data and Model Scaling on High-Level Control for Humanoid Robots.'
sources:
- id: src_001
  type: website
  title: 揭示数据和模型扩展对人形机器人高级控制的影响 project page
  url: https://vfishc.github.io/schur/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video, extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this, we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset can be further expanded via the same pipeline. Building on this data resource, we propose SCHUR, a scalable learning framework designed to explore the impact of large-scale data on high-level control in humanoid robots. Experimental results demonstrate that SCHUR achieves high robot motion generation quality and strong text-motion alignment under data and model scaling, with 37\% reconstruction improvement under MPJPE and 25\% alignment improvement under FID comparing with previous methods. Its effectiveness is further validated through deployment in real-world humanoid robot.

## 核心内容
Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video, extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this, we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset can be further expanded via the same pipeline. Building on this data resource, we propose SCHUR, a scalable learning framework designed to explore the impact of large-scale data on high-level control in humanoid robots. Experimental results demonstrate that SCHUR achieves high robot motion generation quality and strong text-motion alignment under data and model scaling, with 37\% reconstruction improvement under MPJPE and 25\% alignment improvement under FID comparing with previous methods. Its effectiveness is further validated through deployment in real-world humanoid robot.

## 参考
- Semantic Scholar search: Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots

## Overview
Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video, extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this, we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset can be further expanded via the same pipeline. Building on this data resource, we propose SCHUR, a scalable learning framework designed to explore the impact of large-scale data on high-level control in humanoid robots. Experimental results demonstrate that SCHUR achieves high robot motion generation quality and strong text-motion alignment under data and model scaling, with 37\% reconstruction improvement under MPJPE and 25\% alignment improvement under FID comparing with previous methods. Its effectiveness is further validated through deployment in real-world humanoid robot.

## Content
Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video, extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this, we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset can be further expanded via the same pipeline. Building on this data resource, we propose SCHUR, a scalable learning framework designed to explore the impact of large-scale data on high-level control in humanoid robots. Experimental results demonstrate that SCHUR achieves high robot motion generation quality and strong text-motion alignment under data and model scaling, with 37\% reconstruction improvement under MPJPE and 25\% alignment improvement under FID comparing with previous methods. Its effectiveness is further validated through deployment in real-world humanoid robot.

## 개요
데이터 스케일링은 오랫동안 로봇 학습에서 중요한 병목 현상으로 남아 있었습니다. 휴머노이드 로봇의 경우, 인간의 비디오와 모션 데이터는 풍부하고 널리 이용 가능하여 무료이면서 대규모 데이터 소스를 제공합니다. 또한, 모션과 관련된 의미 정보는 모달리티 정렬 및 고수준 로봇 제어 학습을 가능하게 합니다. 그러나 원시 비디오를 효과적으로 마이닝하고, 로봇이 학습 가능한 표현을 추출하며, 이를 확장 가능한 학습에 활용하는 방법은 여전히 해결되지 않은 문제입니다. 이를 해결하기 위해, 우리는 자율 파이프라인을 통해 생성된 대규모 데이터셋인 Humanoid-Union을 소개합니다. 이 데이터셋은 인간 모션 비디오에서 추출된 의미 주석과 함께 260시간 이상의 다양하고 고품질의 휴머노이드 로봇 모션 데이터로 구성됩니다. 동일한 파이프라인을 통해 데이터셋을 더 확장할 수 있습니다. 이 데이터 자원을 기반으로, 우리는 휴머노이드 로봇의 고수준 제어에 대한 대규모 데이터의 영향을 탐구하도록 설계된 확장 가능한 학습 프레임워크인 SCHUR을 제안합니다. 실험 결과는 SCHUR이 데이터 및 모델 스케일링 하에서 높은 로봇 모션 생성 품질과 강력한 텍스트-모션 정렬을 달성하며, 이전 방법과 비교하여 MPJPE에서 37%의 재구성 개선 및 FID에서 25%의 정렬 개선을 보여줍니다. 그 효과성은 실제 휴머노이드 로봇에 배치하여 추가로 검증되었습니다.

## 핵심 내용
데이터 스케일링은 오랫동안 로봇 학습에서 중요한 병목 현상으로 남아 있었습니다. 휴머노이드 로봇의 경우, 인간의 비디오와 모션 데이터는 풍부하고 널리 이용 가능하여 무료이면서 대규모 데이터 소스를 제공합니다. 또한, 모션과 관련된 의미 정보는 모달리티 정렬 및 고수준 로봇 제어 학습을 가능하게 합니다. 그러나 원시 비디오를 효과적으로 마이닝하고, 로봇이 학습 가능한 표현을 추출하며, 이를 확장 가능한 학습에 활용하는 방법은 여전히 해결되지 않은 문제입니다. 이를 해결하기 위해, 우리는 자율 파이프라인을 통해 생성된 대규모 데이터셋인 Humanoid-Union을 소개합니다. 이 데이터셋은 인간 모션 비디오에서 추출된 의미 주석과 함께 260시간 이상의 다양하고 고품질의 휴머노이드 로봇 모션 데이터로 구성됩니다. 동일한 파이프라인을 통해 데이터셋을 더 확장할 수 있습니다. 이 데이터 자원을 기반으로, 우리는 휴머노이드 로봇의 고수준 제어에 대한 대규모 데이터의 영향을 탐구하도록 설계된 확장 가능한 학습 프레임워크인 SCHUR을 제안합니다. 실험 결과는 SCHUR이 데이터 및 모델 스케일링 하에서 높은 로봇 모션 생성 품질과 강력한 텍스트-모션 정렬을 달성하며, 이전 방법과 비교하여 MPJPE에서 37%의 재구성 개선 및 FID에서 25%의 정렬 개선을 보여줍니다. 그 효과성은 실제 휴머노이드 로봇에 배치하여 추가로 검증되었습니다.
