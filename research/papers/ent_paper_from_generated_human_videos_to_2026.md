---
$id: ent_paper_from_generated_human_videos_to_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: From Generated Human Videos to Physically Plausible Robot Trajectories
  zh: 生成视频不能直接给机器人用
  ko: From Generated Human Videos to Physically Plausible Robot Trajectories
summary:
  en: From Generated Human Videos to Physically Plausible Robot Trajectories is a knowledge node related to paper in the humanoid
    robot value chain.
  zh: 'Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding
    the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research
    question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This
    challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation
    difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into
    a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic-a physics-aware reinforcement
    learning policy conditioned on 3D keypoints, and trained with symmetry reg'
  ko: From Generated Human Videos to Physically Plausible Robot Trajectories is a knowledge node related to paper in the humanoid
    robot value chain.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- data_collection
- human_demonstration
- human_video
- interaction_fidelity
- motion_retargeting
- teleoperation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05094v2.
sources:
- id: src_001
  type: paper
  title: From Generated Human Videos to Physically Plausible Robot Trajectories (arXiv)
  url: https://arxiv.org/abs/2512.05094
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 生成视频不能直接给机器人用 project page
  url: https://genmimic.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic-a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## 核心内容
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic-a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## 参考
- http://arxiv.org/abs/2512.05094v2

