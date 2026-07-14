---
$id: ent_paper_dai_rover_robot_reward_model_as_te_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model'
  zh: RoVer
  ko: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model'
summary:
  en: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model (RoVer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences,
    Peng Cheng Laboratory, School of Computer Science and Engineering, Sun Yat-sen University, College of Computing and Data
    Science, Nanyang Technological University, Shanghai AI Laboratory, University of Chinese Academy of Sciences, X-Era AI
    Lab.'
  zh: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model (RoVer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences,
    Peng Cheng Laboratory, School of Computer Science and Engineering, Sun Yat-sen University, College of Computing and Data
    Science, Nanyang Technological University, Shanghai AI Laboratory, University of Chinese Academy of Sciences, X-Era AI
    Lab.'
  ko: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model (RoVer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences,
    Peng Cheng Laboratory, School of Computer Science and Engineering, Sun Yat-sen University, College of Computing and Data
    Science, Nanyang Technological University, Shanghai AI Laboratory, University of Chinese Academy of Sciences, X-Era AI
    Lab.'
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
- rover
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10975v2.
sources:
- id: src_001
  type: paper
  title: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2510.10975
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoVer source
  url: https://doi.org/10.48550/arXiv.2510.10975
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have become a prominent paradigm for embodied intelligence, yet further performance improvements typically rely on scaling up training data and model size -- an approach that is prohibitively expensive for robotics and fundamentally limited by data collection costs. We address this limitation with $\mathbf{RoVer}$, an embodied test-time scaling framework that uses a $\mathbf{Ro}$bot Process Reward Model (PRM) as a Test-Time $\mathbf{Ver}$ifier to enhance the capabilities of existing VLA models without modifying their architectures or weights. Specifically, RoVer (i) assigns scalar-based process rewards to evaluate the reliability of candidate actions, and (ii) predicts an action-space direction for candidate expansion/refinement. During inference, RoVer generates multiple candidate actions concurrently from the base policy, expands them along PRM-predicted directions, and then scores all candidates with PRM to select the optimal action for execution. Notably, by caching shared perception features, it can amortize perception cost and evaluate more candidates under the same test-time computational budget. Essentially, our approach effectively transforms available computing resources into better action decision-making, realizing the benefits of test-time scaling without extra training overhead. Our contributions are threefold: (1) a general, plug-and-play test-time scaling framework for VLAs; (2) a PRM that jointly provides scalar process rewards and an action-space direction to guide exploration; and (3) an efficient direction-guided sampling strategy that leverages a shared perception cache to enable scalable candidate generation and selection during inference.

## 核心内容
Vision-Language-Action (VLA) models have become a prominent paradigm for embodied intelligence, yet further performance improvements typically rely on scaling up training data and model size -- an approach that is prohibitively expensive for robotics and fundamentally limited by data collection costs. We address this limitation with $\mathbf{RoVer}$, an embodied test-time scaling framework that uses a $\mathbf{Ro}$bot Process Reward Model (PRM) as a Test-Time $\mathbf{Ver}$ifier to enhance the capabilities of existing VLA models without modifying their architectures or weights. Specifically, RoVer (i) assigns scalar-based process rewards to evaluate the reliability of candidate actions, and (ii) predicts an action-space direction for candidate expansion/refinement. During inference, RoVer generates multiple candidate actions concurrently from the base policy, expands them along PRM-predicted directions, and then scores all candidates with PRM to select the optimal action for execution. Notably, by caching shared perception features, it can amortize perception cost and evaluate more candidates under the same test-time computational budget. Essentially, our approach effectively transforms available computing resources into better action decision-making, realizing the benefits of test-time scaling without extra training overhead. Our contributions are threefold: (1) a general, plug-and-play test-time scaling framework for VLAs; (2) a PRM that jointly provides scalar process rewards and an action-space direction to guide exploration; and (3) an efficient direction-guided sampling strategy that leverages a shared perception cache to enable scalable candidate generation and selection during inference.

## 参考
- http://arxiv.org/abs/2510.10975v2

