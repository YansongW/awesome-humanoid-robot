---
$id: ent_paper_jia_video2act_a_dual_system_video_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling'
  zh: Video2Act
  ko: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling'
summary:
  en: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (Video2Act), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Sun Yat-sen University, Wuhan University, Hong Kong University
    of Science and Technology.'
  zh: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (Video2Act), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Sun Yat-sen University, Wuhan University, Hong Kong University
    of Science and Technology.'
  ko: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (Video2Act), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Sun Yat-sen University, Wuhan University, Hong Kong University
    of Science and Technology.'
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
- video2act
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.03044v3.
sources:
- id: src_001
  type: paper
  title: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (arXiv)'
  url: https://arxiv.org/abs/2512.03044
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Video2Act source
  url: https://doi.org/10.48550/arXiv.2512.03044
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robust perception and dynamics modeling are fundamental to real-world robotic policy learning. Recent methods employ video diffusion models (VDMs) to enhance robotic policies, improving their understanding and modeling of the physical world. However, existing approaches overlook the coherent and physically consistent motion representations inherently encoded across frames in VDMs. To this end, we propose Video2Act, a framework that efficiently guides robotic action learning by explicitly integrating spatial and motion-aware representations. Building on the inherent representations of VDMs, we extract foreground boundaries and inter-frame motion variations while filtering out background noise and task-irrelevant biases. These refined representations are then used as additional conditioning inputs to a diffusion transformer (DiT) action head, enabling it to reason about what to manipulate and how to move. To mitigate inference inefficiency, we propose an asynchronous dual-system design, where the VDM functions as the slow System 2 and the DiT head as the fast System 1, working collaboratively to generate adaptive actions. By providing motion-aware conditions to System 1, Video2Act maintains stable manipulation even with low-frequency updates from the VDM. For evaluation, Video2Act surpasses previous state-of-the-art VLA methods by 7.7% in simulation and 21.7% in real-world tasks in terms of average success rate, further exhibiting strong generalization capabilities.

## 核心内容
Robust perception and dynamics modeling are fundamental to real-world robotic policy learning. Recent methods employ video diffusion models (VDMs) to enhance robotic policies, improving their understanding and modeling of the physical world. However, existing approaches overlook the coherent and physically consistent motion representations inherently encoded across frames in VDMs. To this end, we propose Video2Act, a framework that efficiently guides robotic action learning by explicitly integrating spatial and motion-aware representations. Building on the inherent representations of VDMs, we extract foreground boundaries and inter-frame motion variations while filtering out background noise and task-irrelevant biases. These refined representations are then used as additional conditioning inputs to a diffusion transformer (DiT) action head, enabling it to reason about what to manipulate and how to move. To mitigate inference inefficiency, we propose an asynchronous dual-system design, where the VDM functions as the slow System 2 and the DiT head as the fast System 1, working collaboratively to generate adaptive actions. By providing motion-aware conditions to System 1, Video2Act maintains stable manipulation even with low-frequency updates from the VDM. For evaluation, Video2Act surpasses previous state-of-the-art VLA methods by 7.7% in simulation and 21.7% in real-world tasks in terms of average success rate, further exhibiting strong generalization capabilities.

## 参考
- http://arxiv.org/abs/2512.03044v3

