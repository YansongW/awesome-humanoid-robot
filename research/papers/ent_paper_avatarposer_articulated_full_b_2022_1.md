---
$id: ent_paper_avatarposer_articulated_full_b_2022_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
  zh: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
  ko: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
summary:
  en: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing is a 2022 work on human motion analysis
    and synthesis for humanoid robots, with open-source code available.'
  zh: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing is a 2022 work on human motion analysis
    and synthesis for humanoid robots, with open-source code available.'
  ko: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing is a 2022 work on human motion analysis
    and synthesis for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- avatarposer
- humanoid
- motion_analysis
- motion_synthesis
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

