---
$id: ent_paper_qian_wristworld_generating_wrist_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation'
  zh: WristWorld
  ko: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation'
summary:
  en: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation (WristWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Hong Kong University of Science and Technology, National
    University of Singapore, Beijing Innovation Center of Humanoid Robotics.'
  zh: WristWorld 是由北京大学、香港科技大学、新加坡国立大学和北京人形机器人创新中心联合提出的首个4D世界模型，能够仅从锚定视角生成腕部视角视频。其核心贡献在于通过两阶段架构（重建与生成）弥合锚定视角与腕部视角之间的数据鸿沟，并在Droid、Calvin和Franka
    Panda基准上实现了最先进的视频生成效果，同时将Calvin任务平均完成长度提升3.81%，缩小了42.4%的视角差距。
  ko: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation (WristWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Hong Kong University of Science and Technology, National
    University of Singapore, Beijing Innovation Center of Humanoid Robotics.'
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
- wristworld
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07313v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2510.07313
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WristWorld source
  url: https://doi.org/10.48550/arXiv.2510.07313
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
腕部视角观测对于视觉-语言-动作模型至关重要，因为它能捕捉手-物体交互的精细细节，直接提升操作性能。然而大规模数据集极少包含此类记录，导致丰富的锚定视角与稀缺的腕部视角之间存在显著差距。现有世界模型无法弥合这一鸿沟，因为它们需要腕部视角的首帧作为输入。WristWorld 利用VGGT等视觉几何模型的几何与跨视角先验，通过两阶段流程解决极端视角变换问题：首先在重建阶段扩展VGGT并引入空间投影一致性损失，以估计几何一致的腕部视角姿态和4D点云；随后在生成阶段使用视频生成模型合成时间连贯的腕部视角视频。实验表明该方法在空间一致性上超越现有技术，并有效提升了VLA模型性能。

## 核心内容
### 方法架构
WristWorld 采用两阶段流水线：
- **重建阶段**：基于VGGT扩展，提出**空间投影一致性损失**，通过约束多视角投影的几何一致性，从锚定视角估计腕部视角的相机姿态和4D点云。
- **生成阶段**：利用视频生成模型，从重建的视角参数出发，合成时间上连贯的腕部视角视频，无需任何腕部视角首帧作为条件。

### 实验设置与关键结果
- **基准测试**：在Droid、Calvin和Franka Panda三个机器人操作数据集上评估。
- **视频生成性能**：在空间一致性指标上达到最先进水平，显著优于现有世界模型。
- **VLA性能提升**：在Calvin基准上，将任务平均完成长度提升3.81%，并缩小了锚定视角与腕部视角之间42.4%的性能差距。

### 结论
WristWorld 首次实现了仅从锚定视角生成腕部视角视频，有效解决了机器人操作中腕部数据稀缺的问题，为VLA模型提供了关键的细粒度交互信息。

## Overview
Wrist-view observations are crucial for VLA models as they capture fine-grained hand-object interactions that directly enhance manipulation performance. Yet large-scale datasets rarely include such recordings, resulting in a substantial gap between abundant anchor views and scarce wrist views. Existing world models cannot bridge this gap, as they require a wrist-view first frame and thus fail to generate wrist-view videos from anchor views alone. Amid this gap, recent visual geometry models such as VGGT emerge with geometric and cross-view priors that make it possible to address extreme viewpoint shifts. Inspired by these insights, we propose WristWorld, the first 4D world model that generates wrist-view videos solely from anchor views. WristWorld operates in two stages: (i) Reconstruction, which extends VGGT and incorporates our Spatial Projection Consistency (SPC) Loss to estimate geometrically consistent wrist-view poses and 4D point clouds; (ii) Generation, which employs our video generation model to synthesize temporally coherent wrist-view videos from the reconstructed perspective. Experiments on Droid, Calvin, and Franka Panda demonstrate state-of-the-art video generation with superior spatial consistency, while also improving VLA performance, raising the average task completion length on Calvin by 3.81% and closing 42.4% of the anchor-wrist view gap.

## 개요
손목 시점 관찰은 VLA 모델에 매우 중요합니다. 이는 미세한 손-물체 상호작용을 포착하여 조작 성능을 직접적으로 향상시키기 때문입니다. 그러나 대규모 데이터셋에는 이러한 기록이 거의 포함되지 않아, 풍부한 앵커 뷰와 부족한 손목 뷰 사이에 상당한 격차가 발생합니다. 기존의 세계 모델은 이 격차를 해소할 수 없는데, 이는 손목 뷰의 첫 프레임을 필요로 하여 앵커 뷰만으로는 손목 뷰 비디오를 생성할 수 없기 때문입니다. 이러한 격차 속에서 VGGT와 같은 최근의 시각 기하학 모델은 기하학적 및 교차 뷰 사전 정보를 제공하여 극단적인 시점 변화를 처리할 수 있게 합니다. 이러한 통찰에서 영감을 받아, 우리는 앵커 뷰만으로 손목 뷰 비디오를 생성하는 최초의 4D 세계 모델인 WristWorld를 제안합니다. WristWorld는 두 단계로 작동합니다: (i) 재구성 단계에서는 VGGT를 확장하고 우리의 공간 투영 일관성(SPC) 손실을 통합하여 기하학적으로 일관된 손목 뷰 포즈와 4D 포인트 클라우드를 추정합니다; (ii) 생성 단계에서는 우리의 비디오 생성 모델을 사용하여 재구성된 시점에서 시간적으로 일관된 손목 뷰 비디오를 합성합니다. Droid, Calvin, Franka Panda에 대한 실험은 우수한 공간 일관성을 가진 최첨단 비디오 생성을 입증했으며, VLA 성능도 향상시켜 Calvin에서 평균 작업 완료 길이를 3.81% 증가시키고 앵커-손목 뷰 격차의 42.4%를 좁혔습니다.

## 핵심 내용
손목 시점 관찰은 VLA 모델에 매우 중요합니다. 이는 미세한 손-물체 상호작용을 포착하여 조작 성능을 직접적으로 향상시키기 때문입니다. 그러나 대규모 데이터셋에는 이러한 기록이 거의 포함되지 않아, 풍부한 앵커 뷰와 부족한 손목 뷰 사이에 상당한 격차가 발생합니다. 기존의 세계 모델은 이 격차를 해소할 수 없는데, 이는 손목 뷰의 첫 프레임을 필요로 하여 앵커 뷰만으로는 손목 뷰 비디오를 생성할 수 없기 때문입니다. 이러한 격차 속에서 VGGT와 같은 최근의 시각 기하학 모델은 기하학적 및 교차 뷰 사전 정보를 제공하여 극단적인 시점 변화를 처리할 수 있게 합니다. 이러한 통찰에서 영감을 받아, 우리는 앵커 뷰만으로 손목 뷰 비디오를 생성하는 최초의 4D 세계 모델인 WristWorld를 제안합니다. WristWorld는 두 단계로 작동합니다: (i) 재구성 단계에서는 VGGT를 확장하고 우리의 공간 투영 일관성(SPC) 손실을 통합하여 기하학적으로 일관된 손목 뷰 포즈와 4D 포인트 클라우드를 추정합니다; (ii) 생성 단계에서는 우리의 비디오 생성 모델을 사용하여 재구성된 시점에서 시간적으로 일관된 손목 뷰 비디오를 합성합니다. Droid, Calvin, Franka Panda에 대한 실험은 우수한 공간 일관성을 가진 최첨단 비디오 생성을 입증했으며, VLA 성능도 향상시켜 Calvin에서 평균 작업 완료 길이를 3.81% 증가시키고 앵커-손목 뷰 격차의 42.4%를 좁혔습니다.

## 参考
- http://arxiv.org/abs/2510.07313v1
