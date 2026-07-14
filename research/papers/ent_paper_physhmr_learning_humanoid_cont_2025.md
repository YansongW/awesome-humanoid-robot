---
$id: ent_paper_physhmr_learning_humanoid_cont_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction'
  zh: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction'
  ko: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction'
summary:
  en: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction is a 2025
    work on physics-based character animation for humanoid robots.'
  zh: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction is a 2025
    work on physics-based character animation for humanoid robots.'
  ko: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction is a 2025
    work on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physhmr
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.02566v1.
sources:
- id: src_001
  type: paper
  title: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction (arXiv)'
  url: https://arxiv.org/abs/2510.02566
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reconstructing physically plausible human motion from monocular videos remains a challenging problem in computer vision and graphics. Existing methods primarily focus on kinematics-based pose estimation, often leading to unrealistic results due to the lack of physical constraints. To address such artifacts, prior methods have typically relied on physics-based post-processing following the initial kinematics-based motion estimation. However, this two-stage design introduces error accumulation, ultimately limiting the overall reconstruction quality. In this paper, we present PhysHMR, a unified framework that directly learns a visual-to-action policy for humanoid control in a physics-based simulator, enabling motion reconstruction that is both physically grounded and visually aligned with the input video. A key component of our approach is the pixel-as-ray strategy, which lifts 2D keypoints into 3D spatial rays and transforms them into global space. These rays are incorporated as policy inputs, providing robust global pose guidance without depending on noisy 3D root predictions. This soft global grounding, combined with local visual features from a pretrained encoder, allows the policy to reason over both detailed pose and global positioning. To overcome the sample inefficiency of reinforcement learning, we further introduce a distillation scheme that transfers motion knowledge from a mocap-trained expert to the vision-conditioned policy, which is then refined using physically motivated reinforcement learning rewards. Extensive experiments demonstrate that PhysHMR produces high-fidelity, physically plausible motion across diverse scenarios, outperforming prior approaches in both visual accuracy and physical realism.

## 核心内容
Reconstructing physically plausible human motion from monocular videos remains a challenging problem in computer vision and graphics. Existing methods primarily focus on kinematics-based pose estimation, often leading to unrealistic results due to the lack of physical constraints. To address such artifacts, prior methods have typically relied on physics-based post-processing following the initial kinematics-based motion estimation. However, this two-stage design introduces error accumulation, ultimately limiting the overall reconstruction quality. In this paper, we present PhysHMR, a unified framework that directly learns a visual-to-action policy for humanoid control in a physics-based simulator, enabling motion reconstruction that is both physically grounded and visually aligned with the input video. A key component of our approach is the pixel-as-ray strategy, which lifts 2D keypoints into 3D spatial rays and transforms them into global space. These rays are incorporated as policy inputs, providing robust global pose guidance without depending on noisy 3D root predictions. This soft global grounding, combined with local visual features from a pretrained encoder, allows the policy to reason over both detailed pose and global positioning. To overcome the sample inefficiency of reinforcement learning, we further introduce a distillation scheme that transfers motion knowledge from a mocap-trained expert to the vision-conditioned policy, which is then refined using physically motivated reinforcement learning rewards. Extensive experiments demonstrate that PhysHMR produces high-fidelity, physically plausible motion across diverse scenarios, outperforming prior approaches in both visual accuracy and physical realism.

## 参考
- http://arxiv.org/abs/2510.02566v1

