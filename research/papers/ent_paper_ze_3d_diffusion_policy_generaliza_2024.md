---
$id: ent_paper_ze_3d_diffusion_policy_generaliza_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'
  zh: DP3
  ko: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'
summary:
  en: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (DP3), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Shanghai Jiao Tong University,
    Tsinghua University, IIIS, Shanghai AI Lab, and published at Robotics - Science and Systems 2024.'
  zh: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (DP3), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Shanghai Jiao Tong University,
    Tsinghua University, IIIS, Shanghai AI Lab, and published at Robotics - Science and Systems 2024.'
  ko: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (DP3), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Shanghai Jiao Tong University,
    Tsinghua University, IIIS, Shanghai AI Lab, and published at Robotics - Science and Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dp3
- generalist_policy
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.03954v7.
sources:
- id: src_001
  type: website
  title: DP3 source
  url: https://doi.org/10.15607/RSS.2024.XX.067
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizablely usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## 核心内容
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizablely usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## 参考
- http://arxiv.org/abs/2403.03954v7

