---
$id: ent_paper_shen_videovla_video_generators_can_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators'
  zh: VideoVLA
  ko: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators'
summary:
  en: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators (VideoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by IAIR, Xi’an Jiaotong University, Microsoft Research Asia, Fudan University,
    and published at NIPS25.'
  zh: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators (VideoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by IAIR, Xi’an Jiaotong University, Microsoft Research Asia, Fudan University,
    and published at NIPS25.'
  ko: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators (VideoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by IAIR, Xi’an Jiaotong University, Microsoft Research Asia, Fudan University,
    and published at NIPS25.'
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
- videovla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.06963v1.
sources:
- id: src_001
  type: paper
  title: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators (arXiv)'
  url: https://arxiv.org/abs/2512.06963
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VideoVLA source
  url: https://doi.org/10.48550/arXiv.2512.06963
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalization in robot manipulation is essential for deploying robots in open-world environments and advancing toward artificial general intelligence. While recent Vision-Language-Action (VLA) models leverage large pre-trained understanding models for perception and instruction following, their ability to generalize to novel tasks, objects, and settings remains limited. In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators. Given a language instruction and an image, VideoVLA predicts an action sequence as well as the future visual outcomes. Built on a multi-modal Diffusion Transformer, VideoVLA jointly models video, language, and action modalities, using pre-trained video generative models for joint visual and action forecasting. Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation. VideoVLA demonstrates strong generalization, including imitating other embodiments' skills and handling novel objects. This dual-prediction strategy - forecasting both actions and their visual consequences - explores a paradigm shift in robot learning and unlocks generalization capabilities in manipulation systems.

## 核心内容
Generalization in robot manipulation is essential for deploying robots in open-world environments and advancing toward artificial general intelligence. While recent Vision-Language-Action (VLA) models leverage large pre-trained understanding models for perception and instruction following, their ability to generalize to novel tasks, objects, and settings remains limited. In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators. Given a language instruction and an image, VideoVLA predicts an action sequence as well as the future visual outcomes. Built on a multi-modal Diffusion Transformer, VideoVLA jointly models video, language, and action modalities, using pre-trained video generative models for joint visual and action forecasting. Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation. VideoVLA demonstrates strong generalization, including imitating other embodiments' skills and handling novel objects. This dual-prediction strategy - forecasting both actions and their visual consequences - explores a paradigm shift in robot learning and unlocks generalization capabilities in manipulation systems.

## 参考
- http://arxiv.org/abs/2512.06963v1

