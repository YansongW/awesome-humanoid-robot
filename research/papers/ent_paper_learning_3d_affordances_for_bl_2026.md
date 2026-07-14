---
$id: ent_paper_learning_3d_affordances_for_bl_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning 3D Affordances for Blade Insertion in Cluttered Stowing
  zh: Learning 3D Affordances for Blade Insertion in Cluttered Stowing
  ko: Learning 3D Affordances for Blade Insertion in Cluttered Stowing
summary:
  en: "arXiv:2607.02549v1 Announce Type: cross \nAbstract: Many manipulation tasks require reasoning about free-space affordances:\
    \ discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for\
    \ grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins\
    \ to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with\
    \ unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel\
    \ keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene\
    \ geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade\
    \ affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure\
    \ for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching\
    \ faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives.\
    \ Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89\
    \ versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs.\
    \ 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose\
    \ trajectories at https://www.armbench.com/blade_insertion. html."
  zh: "arXiv:2607.02549v1 Announce Type: cross \nAbstract: Many manipulation tasks require reasoning about free-space affordances:\
    \ discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for\
    \ grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins\
    \ to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with\
    \ unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel\
    \ keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene\
    \ geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade\
    \ affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure\
    \ for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching\
    \ faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives.\
    \ Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89\
    \ versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs.\
    \ 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose\
    \ trajectories at https://www.armbench.com/blade_insertion. html."
  ko: "arXiv:2607.02549v1 Announce Type: cross \nAbstract: Many manipulation tasks require reasoning about free-space affordances:\
    \ discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for\
    \ grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins\
    \ to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with\
    \ unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel\
    \ keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene\
    \ geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade\
    \ affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure\
    \ for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching\
    \ faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives.\
    \ Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89\
    \ versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs.\
    \ 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose\
    \ trajectories at https://www.armbench.com/blade_insertion. html."
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
- learning_3d_affordances_for_bl
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02549v1.
sources:
- id: src_001
  type: paper
  title: Learning 3D Affordances for Blade Insertion in Cluttered Stowing (arXiv)
  url: https://arxiv.org/abs/2607.02549
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Many manipulation tasks require reasoning about free-space affordances: discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at https://www.armbench.com/blade_insertion. html.

## 核心内容
Many manipulation tasks require reasoning about free-space affordances: discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at https://www.armbench.com/blade_insertion. html.

## 参考
- http://arxiv.org/abs/2607.02549v1

