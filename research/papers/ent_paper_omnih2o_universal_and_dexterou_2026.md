---
$id: ent_paper_omnih2o_universal_and_dexterou_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning'
  zh: 把遥操作升级成通用身体接口
  ko: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning'
summary:
  en: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning is a knowledge node related
    to paper in the humanoid robot value chain.'
  zh: We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
    Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized
    humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB
    camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models
    such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation
    or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop
    an RL-based sim-to-real pipeline, which involves large-scale retargeting a
  ko: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning is a knowledge node related
    to paper in the humanoid robot value chain.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.08858v1.
sources:
- id: src_001
  type: paper
  title: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning (arXiv)'
  url: https://arxiv.org/abs/2406.08858
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 把遥操作升级成通用身体接口 project page
  url: https://omni.human2humanoid.com/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy. Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a privileged teacher policy, and reward designs to enhance robustness and stability. We release the first humanoid whole-body control dataset, OmniH2O-6, containing six everyday tasks, and demonstrate humanoid whole-body skill learning from teleoperated datasets.

## 核心内容
We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy. Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a privileged teacher policy, and reward designs to enhance robustness and stability. We release the first humanoid whole-body control dataset, OmniH2O-6, containing six everyday tasks, and demonstrate humanoid whole-body skill learning from teleoperated datasets.

## 参考
- http://arxiv.org/abs/2406.08858v1

