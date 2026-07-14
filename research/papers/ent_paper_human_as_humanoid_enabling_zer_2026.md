---
$id: ent_paper_human_as_humanoid_enabling_zer_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments'
  zh: 'Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments'
  ko: 'Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments'
summary:
  en: "arXiv:2606.32009v1 Announce Type: new \nAbstract: Vision-language-action (VLA) models across robot embodiments require\
    \ high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains\
    \ difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric\
    \ videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid,\
    \ a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human\
    \ demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup,\
    \ and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses\
    \ synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets\
    \ the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and\
    \ trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry.\
    \ This converts large-scale human demonstrations from visual observations into executable observation--action supervision\
    \ for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot\
    \ deployment levels. Human-as-Humanoid yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation\
    \ in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human\
    \ labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is\
    \ available at https://zgc-embodyai.github.io/Human-as-Humanoid."
  zh: "arXiv:2606.32009v1 Announce Type: new \nAbstract: Vision-language-action (VLA) models across robot embodiments require\
    \ high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains\
    \ difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric\
    \ videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid,\
    \ a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human\
    \ demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup,\
    \ and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses\
    \ synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets\
    \ the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and\
    \ trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry.\
    \ This converts large-scale human demonstrations from visual observations into executable observation--action supervision\
    \ for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot\
    \ deployment levels. Human-as-Humanoid yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation\
    \ in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human\
    \ labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is\
    \ available at https://zgc-embodyai.github.io/Human-as-Humanoid."
  ko: "arXiv:2606.32009v1 Announce Type: new \nAbstract: Vision-language-action (VLA) models across robot embodiments require\
    \ high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains\
    \ difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric\
    \ videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid,\
    \ a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human\
    \ demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup,\
    \ and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses\
    \ synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets\
    \ the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and\
    \ trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry.\
    \ This converts large-scale human demonstrations from visual observations into executable observation--action supervision\
    \ for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot\
    \ deployment levels. Human-as-Humanoid yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation\
    \ in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human\
    \ labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is\
    \ available at https://zgc-embodyai.github.io/Human-as-Humanoid."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_as_humanoid
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.32009v1.
sources:
- id: src_001
  type: paper
  title: 'Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments'
  url: https://arxiv.org/abs/2606.32009
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models across robot embodiments require high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid, a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup, and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry. This converts large-scale human demonstrations from visual observations into executable observation--action supervision for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot deployment levels. Human-as-Humanoid yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is available at https://zgc-embodyai.github.io/Human-as-Humanoid.

## 核心内容
Vision-language-action (VLA) models across robot embodiments require high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid, a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup, and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry. This converts large-scale human demonstrations from visual observations into executable observation--action supervision for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot deployment levels. Human-as-Humanoid yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is available at https://zgc-embodyai.github.io/Human-as-Humanoid.

## 参考
- http://arxiv.org/abs/2606.32009v1

