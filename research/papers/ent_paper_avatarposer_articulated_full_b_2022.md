---
$id: ent_paper_avatarposer_articulated_full_b_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
  zh: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
  ko: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
summary:
  en: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing is a 2022 work on teleoperation for humanoid
    robots, with open-source code available.'
  zh: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing is a 2022 work on teleoperation for humanoid
    robots, with open-source code available.'
  ko: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing is a 2022 work on teleoperation for humanoid
    robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- avatarposer
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2207.13784v1.
sources:
- id: src_001
  type: paper
  title: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing (arXiv)'
  url: https://arxiv.org/abs/2207.13784
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing project page'
  url: https://siplab.org/projects/AvatarPoser
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Today's Mixed Reality head-mounted displays track the user's head pose in world space as well as the user's hands for interaction in both Augmented Reality and Virtual Reality scenarios. While this is adequate to support user input, it unfortunately limits users' virtual representations to just their upper bodies. Current systems thus resort to floating avatars, whose limitation is particularly evident in collaborative settings. To estimate full-body poses from the sparse input sources, prior work has incorporated additional trackers and sensors at the pelvis or lower body, which increases setup complexity and limits practical application in mobile settings. In this paper, we present AvatarPoser, the first learning-based method that predicts full-body poses in world coordinates using only motion input from the user's head and hands. Our method builds on a Transformer encoder to extract deep features from the input signals and decouples global motion from the learned local joint orientations to guide pose estimation. To obtain accurate full-body motions that resemble motion capture animations, we refine the arm joints' positions using an optimization routine with inverse kinematics to match the original tracking input. In our evaluation, AvatarPoser achieved new state-of-the-art results in evaluations on large motion capture datasets (AMASS). At the same time, our method's inference speed supports real-time operation, providing a practical interface to support holistic avatar control and representation for Metaverse applications.

## 核心内容
Today's Mixed Reality head-mounted displays track the user's head pose in world space as well as the user's hands for interaction in both Augmented Reality and Virtual Reality scenarios. While this is adequate to support user input, it unfortunately limits users' virtual representations to just their upper bodies. Current systems thus resort to floating avatars, whose limitation is particularly evident in collaborative settings. To estimate full-body poses from the sparse input sources, prior work has incorporated additional trackers and sensors at the pelvis or lower body, which increases setup complexity and limits practical application in mobile settings. In this paper, we present AvatarPoser, the first learning-based method that predicts full-body poses in world coordinates using only motion input from the user's head and hands. Our method builds on a Transformer encoder to extract deep features from the input signals and decouples global motion from the learned local joint orientations to guide pose estimation. To obtain accurate full-body motions that resemble motion capture animations, we refine the arm joints' positions using an optimization routine with inverse kinematics to match the original tracking input. In our evaluation, AvatarPoser achieved new state-of-the-art results in evaluations on large motion capture datasets (AMASS). At the same time, our method's inference speed supports real-time operation, providing a practical interface to support holistic avatar control and representation for Metaverse applications.

## 参考
- http://arxiv.org/abs/2207.13784v1

## Overview
Today's Mixed Reality head-mounted displays track the user's head pose in world space as well as the user's hands for interaction in both Augmented Reality and Virtual Reality scenarios. While this is adequate to support user input, it unfortunately limits users' virtual representations to just their upper bodies. Current systems thus resort to floating avatars, whose limitation is particularly evident in collaborative settings. To estimate full-body poses from the sparse input sources, prior work has incorporated additional trackers and sensors at the pelvis or lower body, which increases setup complexity and limits practical application in mobile settings. In this paper, we present AvatarPoser, the first learning-based method that predicts full-body poses in world coordinates using only motion input from the user's head and hands. Our method builds on a Transformer encoder to extract deep features from the input signals and decouples global motion from the learned local joint orientations to guide pose estimation. To obtain accurate full-body motions that resemble motion capture animations, we refine the arm joints' positions using an optimization routine with inverse kinematics to match the original tracking input. In our evaluation, AvatarPoser achieved new state-of-the-art results in evaluations on large motion capture datasets (AMASS). At the same time, our method's inference speed supports real-time operation, providing a practical interface to support holistic avatar control and representation for Metaverse applications.

## Content
Today's Mixed Reality head-mounted displays track the user's head pose in world space as well as the user's hands for interaction in both Augmented Reality and Virtual Reality scenarios. While this is adequate to support user input, it unfortunately limits users' virtual representations to just their upper bodies. Current systems thus resort to floating avatars, whose limitation is particularly evident in collaborative settings. To estimate full-body poses from the sparse input sources, prior work has incorporated additional trackers and sensors at the pelvis or lower body, which increases setup complexity and limits practical application in mobile settings. In this paper, we present AvatarPoser, the first learning-based method that predicts full-body poses in world coordinates using only motion input from the user's head and hands. Our method builds on a Transformer encoder to extract deep features from the input signals and decouples global motion from the learned local joint orientations to guide pose estimation. To obtain accurate full-body motions that resemble motion capture animations, we refine the arm joints' positions using an optimization routine with inverse kinematics to match the original tracking input. In our evaluation, AvatarPoser achieved new state-of-the-art results in evaluations on large motion capture datasets (AMASS). At the same time, our method's inference speed supports real-time operation, providing a practical interface to support holistic avatar control and representation for Metaverse applications.

## 개요
오늘날의 혼합 현실 헤드 마운트 디스플레이는 증강 현실과 가상 현실 시나리오 모두에서 사용자의 머리 자세를 세계 좌표계로 추적하고, 상호작용을 위해 사용자의 손을 추적합니다. 이는 사용자 입력을 지원하기에 충분하지만, 불행히도 사용자의 가상 표현을 상체로만 제한합니다. 따라서 현재 시스템은 떠 있는 아바타에 의존하며, 이러한 한계는 협업 환경에서 특히 두드러집니다. 희소한 입력 소스로부터 전신 자세를 추정하기 위해, 이전 연구에서는 골반이나 하체에 추가 트래커와 센서를 통합했지만, 이는 설정 복잡성을 증가시키고 모바일 환경에서의 실용적 적용을 제한합니다. 본 논문에서는 사용자의 머리와 손의 모션 입력만을 사용하여 세계 좌표계에서 전신 자세를 예측하는 최초의 학습 기반 방법인 AvatarPoser를 제시합니다. 우리의 방법은 Transformer 인코더를 기반으로 입력 신호에서 심층 특징을 추출하고, 학습된 국소 관절 방향에서 전역 모션을 분리하여 자세 추정을 안내합니다. 모션 캡처 애니메이션과 유사한 정확한 전신 모션을 얻기 위해, 역운동학을 사용한 최적화 루틴으로 팔 관절 위치를 정제하여 원래 추적 입력과 일치시킵니다. 평가에서 AvatarPoser는 대규모 모션 캡처 데이터셋(AMASS)에서 새로운 최첨단 결과를 달성했습니다. 동시에, 우리 방법의 추론 속도는 실시간 작동을 지원하여 메타버스 애플리케이션을 위한 전체적인 아바타 제어 및 표현을 지원하는 실용적인 인터페이스를 제공합니다.

## 핵심 내용
오늘날의 혼합 현실 헤드 마운트 디스플레이는 증강 현실과 가상 현실 시나리오 모두에서 사용자의 머리 자세를 세계 좌표계로 추적하고, 상호작용을 위해 사용자의 손을 추적합니다. 이는 사용자 입력을 지원하기에 충분하지만, 불행히도 사용자의 가상 표현을 상체로만 제한합니다. 따라서 현재 시스템은 떠 있는 아바타에 의존하며, 이러한 한계는 협업 환경에서 특히 두드러집니다. 희소한 입력 소스로부터 전신 자세를 추정하기 위해, 이전 연구에서는 골반이나 하체에 추가 트래커와 센서를 통합했지만, 이는 설정 복잡성을 증가시키고 모바일 환경에서의 실용적 적용을 제한합니다. 본 논문에서는 사용자의 머리와 손의 모션 입력만을 사용하여 세계 좌표계에서 전신 자세를 예측하는 최초의 학습 기반 방법인 AvatarPoser를 제시합니다. 우리의 방법은 Transformer 인코더를 기반으로 입력 신호에서 심층 특징을 추출하고, 학습된 국소 관절 방향에서 전역 모션을 분리하여 자세 추정을 안내합니다. 모션 캡처 애니메이션과 유사한 정확한 전신 모션을 얻기 위해, 역운동학을 사용한 최적화 루틴으로 팔 관절 위치를 정제하여 원래 추적 입력과 일치시킵니다. 평가에서 AvatarPoser는 대규모 모션 캡처 데이터셋(AMASS)에서 새로운 최첨단 결과를 달성했습니다. 동시에, 우리 방법의 추론 속도는 실시간 작동을 지원하여 메타버스 애플리케이션을 위한 전체적인 아바타 제어 및 표현을 지원하는 실용적인 인터페이스를 제공합니다.
