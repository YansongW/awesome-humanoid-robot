---
$id: ent_paper_agenticfocus_object_preserving_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning'
  zh: 'AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning'
  ko: 'AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning'
summary:
  en: 'arXiv:2607.08857v1 Announce Type: new Abstract: Human egocentric video is a scalable supervision source for humanoid
    policy learning, but current pipelines struggle with hand-object occlusion, oversimplified motion, or specialized capture
    hardware. We introduce AgenticFocus, a Mixed Reality synthesis pipeline that converts ordinary first-person-view human
    videos into robot-trainable demonstrations by restoring occluded object geometry, reconstructing full-hand motion, and
    retargeting it to a humanoid embodiment through camera-relative alignment and layered compositing. The resulting dataset
    pairs focused visual observations with synchronized robot actions and states. AgenticFocus achieves lower trajectory error
    and smoother wrist motion than cross-embodiment baselines, with SPARC scores of -5.18 versus -5.56 and -6.05.'
  zh: AgenticFocus 是一个混合现实合成管线，能将普通人类第一人称视角视频转化为机器人可训练的演示。它通过恢复被遮挡的物体几何、重建完整手部运动，并利用相机相对对齐与分层合成将动作重定向到人形机器人上。该管线在轨迹误差和手腕运动平滑度上优于跨实体基线，SPARC
    得分达到 -5.18，对比基线的 -5.56 和 -6.05。
  ko: 'arXiv:2607.08857v1 Announce Type: new Abstract: Human egocentric video is a scalable supervision source for humanoid
    policy learning, but current pipelines struggle with hand-object occlusion, oversimplified motion, or specialized capture
    hardware. We introduce AgenticFocus, a Mixed Reality synthesis pipeline that converts ordinary first-person-view human
    videos into robot-trainable demonstrations by restoring occluded object geometry, reconstructing full-hand motion, and
    retargeting it to a humanoid embodiment through camera-relative alignment and layered compositing. The resulting dataset
    pairs focused visual observations with synchronized robot actions and states. AgenticFocus achieves lower trajectory error
    and smoother wrist motion than cross-embodiment baselines, with SPARC scores of -5.18 versus -5.56 and -6.05.'
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
- agenticfocus
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.08857v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning (arXiv)'
  url: https://arxiv.org/abs/2607.08857
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
AgenticFocus 由研究团队提出，旨在解决人类第一人称视频在机器人策略学习中的手-物遮挡、运动简化及专用硬件依赖问题。该管线通过恢复被遮挡物体几何、重建完整手部运动，并采用相机相对对齐与分层合成技术，将普通人类第一人称视角视频转化为机器人可训练的演示。生成的配对数据集包含聚焦的视觉观察与同步的机器人动作和状态。实验表明，AgenticFocus 在轨迹误差和手腕运动平滑度上优于跨实体基线，SPARC 得分达到 -5.18，对比基线的 -5.56 和 -6.05。

## 核心内容
### 方法
AgenticFocus 是一个混合现实合成管线，核心步骤包括：
- **物体几何恢复**：从被遮挡的视角中重建被手遮挡的物体完整几何形状。
- **手部运动重建**：恢复完整的手部运动，包括手指关节和手腕姿态。
- **重定向与合成**：通过相机相对对齐和分层合成，将人类手部运动重定向到人形机器人实体上，生成机器人可执行的演示。

### 实验设置
- **数据来源**：使用普通人类第一人称视角视频，无需专用捕捉硬件。
- **基线对比**：与跨实体基线方法进行对比，包括 SPARC 得分评估。
- **评估指标**：轨迹误差（Trajectory Error）和手腕运动平滑度（Wrist Motion Smoothness），以及 SPARC 得分。

### 关键结果
- **SPARC 得分**：AgenticFocus 达到 -5.18，优于基线的 -5.56 和 -6.05。
- **轨迹误差**：AgenticFocus 实现更低的轨迹误差。
- **手腕运动**：手腕运动更平滑，减少抖动。

### 结论
AgenticFocus 通过混合现实合成，有效将人类第一人称视频转化为机器人可训练的演示，解决了手-物遮挡和运动简化问题，无需专用硬件。其生成的配对数据集支持更精准的机器人策略学习，在轨迹误差和运动平滑度上显著优于现有跨实体基线方法。

## Overview
Human egocentric video is a scalable supervision source for humanoid policy learning, but current pipelines struggle with hand-object occlusion, oversimplified motion, or specialized capture hardware. We introduce AgenticFocus, a Mixed Reality synthesis pipeline that converts ordinary first-person-view human videos into robot-trainable demonstrations by restoring occluded object geometry, reconstructing full-hand motion, and retargeting it to a humanoid embodiment through camera-relative alignment and layered compositing. The resulting dataset pairs focused visual observations with synchronized robot actions and states. AgenticFocus achieves lower trajectory error and smoother wrist motion than cross-embodiment baselines, with SPARC scores of -5.18 versus -5.56 and -6.05.

## 개요
인간의 자기중심적 비디오는 휴머노이드 정책 학습을 위한 확장 가능한 감독 소스이지만, 현재 파이프라인은 손-물체 가림, 지나치게 단순화된 동작 또는 특수 촬영 하드웨어로 인해 어려움을 겪고 있습니다. 우리는 AgenticFocus를 소개합니다. 이는 혼합 현실 합성 파이프라인으로, 일반적인 1인칭 시점 인간 비디오를 로봇 학습 가능한 시연으로 변환합니다. 가려진 물체 형상을 복원하고, 전체 손 동작을 재구성하며, 카메라 상대 정렬 및 계층적 합성을 통해 휴머노이드 체형에 재타겟팅합니다. 결과 데이터셋은 집중된 시각적 관찰과 동기화된 로봇 동작 및 상태를 쌍으로 제공합니다. AgenticFocus는 교차 체형 기준선보다 낮은 궤적 오차와 더 부드러운 손목 동작을 달성하며, SPARC 점수는 -5.18 대 -5.56 및 -6.05입니다.

## 핵심 내용
인간의 자기중심적 비디오는 휴머노이드 정책 학습을 위한 확장 가능한 감독 소스이지만, 현재 파이프라인은 손-물체 가림, 지나치게 단순화된 동작 또는 특수 촬영 하드웨어로 인해 어려움을 겪고 있습니다. 우리는 AgenticFocus를 소개합니다. 이는 혼합 현실 합성 파이프라인으로, 일반적인 1인칭 시점 인간 비디오를 로봇 학습 가능한 시연으로 변환합니다. 가려진 물체 형상을 복원하고, 전체 손 동작을 재구성하며, 카메라 상대 정렬 및 계층적 합성을 통해 휴머노이드 체형에 재타겟팅합니다. 결과 데이터셋은 집중된 시각적 관찰과 동기화된 로봇 동작 및 상태를 쌍으로 제공합니다. AgenticFocus는 교차 체형 기준선보다 낮은 궤적 오차와 더 부드러운 손목 동작을 달성하며, SPARC 점수는 -5.18 대 -5.56 및 -6.05입니다.

## 参考
- http://arxiv.org/abs/2607.08857v2
