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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.08857v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (846 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.08857v2

## Overview
AgenticFocus, proposed by the research team, aims to address the challenges of hand-object occlusion, motion simplification, and reliance on specialized hardware in robot policy learning from human first-person videos. This pipeline recovers the geometry of occluded objects, reconstructs complete hand motion, and employs camera-relative alignment with layered synthesis to transform ordinary human first-person perspective videos into robot-trainable demonstrations. The generated paired dataset includes focused visual observations alongside synchronized robot actions and states. Experiments show that AgenticFocus outperforms cross-embodiment baselines in trajectory error and wrist motion smoothness, achieving a SPARC score of -5.18 compared to the baselines' -5.56 and -6.05.

## Content
### Method
AgenticFocus is a mixed-reality synthesis pipeline, with core steps including:
- **Object Geometry Recovery**: Reconstructs the complete geometry of objects occluded by hands from partially obscured viewpoints.
- **Hand Motion Reconstruction**: Recovers full hand motion, including finger joints and wrist pose.
- **Retargeting and Synthesis**: Retargets human hand motion to a humanoid robot embodiment through camera-relative alignment and layered synthesis, generating executable robot demonstrations.

### Experimental Setup
- **Data Source**: Uses ordinary human first-person perspective videos without requiring specialized capture hardware.
- **Baseline Comparison**: Compared against cross-embodiment baseline methods, including SPARC score evaluation.
- **Evaluation Metrics**: Trajectory Error and Wrist Motion Smoothness, along with the SPARC score.

### Key Results
- **SPARC Score**: AgenticFocus achieves -5.18, outperforming the baselines' -5.56 and -6.05.
- **Trajectory Error**: AgenticFocus achieves lower trajectory error.
- **Wrist Motion**: Wrist motion is smoother with reduced jitter.

### Conclusion
AgenticFocus effectively transforms human first-person videos into robot-trainable demonstrations through mixed-reality synthesis, addressing hand-object occlusion and motion simplification without requiring specialized hardware. The generated paired dataset supports more precise robot policy learning, significantly outperforming existing cross-embodiment baseline methods in trajectory error and motion smoothness.

## 개요
AgenticFocus는 연구팀이 제안한 것으로, 인간 일인칭 비디오를 로봇 정책 학습에 활용할 때 발생하는 손-물체 가림, 운동 단순화, 전용 하드웨어 의존 문제를 해결하기 위해 설계되었습니다. 이 파이프라인은 가려진 물체의 기하학을 복원하고, 완전한 손 운동을 재구성하며, 카메라 상대 정렬 및 계층적 합성 기술을 적용하여 일반적인 인간 일인칭 시점 비디오를 로봇이 훈련 가능한 시연으로 변환합니다. 생성된 쌍 데이터셋은 초점이 맞춰진 시각적 관찰과 동기화된 로봇 동작 및 상태를 포함합니다. 실험 결과, AgenticFocus는 궤적 오류와 손목 운동 평활도에서 교차 실체 기준선보다 우수하며, SPARC 점수는 -5.18로 기준선의 -5.56 및 -6.05보다 높습니다.

## 핵심 내용
### 방법
AgenticFocus는 혼합 현실 합성 파이프라인으로, 핵심 단계는 다음과 같습니다:
- **물체 기하학 복원**: 가려진 시점에서 손에 의해 가려진 물체의 완전한 기하학적 형태를 재구성합니다.
- **손 운동 재구성**: 손가락 관절과 손목 자세를 포함한 완전한 손 운동을 복원합니다.
- **리타겟팅 및 합성**: 카메라 상대 정렬과 계층적 합성을 통해 인간의 손 운동을 휴머노이드 로봇 실체로 리타겟팅하여 로봇이 실행 가능한 시연을 생성합니다.

### 실험 설정
- **데이터 소스**: 전용 캡처 하드웨어 없이 일반적인 인간 일인칭 시점 비디오를 사용합니다.
- **기준선 비교**: SPARC 점수 평가를 포함한 교차 실체 기준선 방법과 비교합니다.
- **평가 지표**: 궤적 오류(Trajectory Error)와 손목 운동 평활도(Wrist Motion Smoothness), 그리고 SPARC 점수입니다.

### 주요 결과
- **SPARC 점수**: AgenticFocus는 -5.18로 기준선의 -5.56 및 -6.05보다 우수합니다.
- **궤적 오류**: AgenticFocus는 더 낮은 궤적 오류를 달성합니다.
- **손목 운동**: 손목 운동이 더 평활하며, 떨림이 줄어듭니다.

### 결론
AgenticFocus는 혼합 현실 합성을 통해 인간 일인칭 비디오를 로봇이 훈련 가능한 시연으로 효과적으로 변환하여, 손-물체 가림과 운동 단순화 문제를 해결하고 전용 하드웨어가 필요 없습니다. 생성된 쌍 데이터셋은 더 정밀한 로봇 정책 학습을 지원하며, 궤적 오류와 운동 평활도에서 기존 교차 실체 기준선 방법보다 현저히 우수합니다.
