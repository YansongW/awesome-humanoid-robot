---
$id: ent_paper_monocular_vision_based_control_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Monocular Vision Based Control Framework for Grasping
  zh: Monocular Vision Based Control Framework for Grasping
  ko: ''
summary:
  en: "arXiv:2607.07897v1 Announce Type: new \nAbstract: Grasping in unstructured\
    \ environments requires handling objects with widely different mechanical properties,\
    \ from soft and deformable items to rigid everyday objects. Most existing approaches\
    \ address these categories separately and often rely on tactile sensing, object-specific\
    \ models, or specialized grippers. In this paper, we present a unified monocular\
    \ vision-based grasping framework that targets both soft and rigid objects within\
    \ a single control pipeline, using only RGB input and a position-controlled gripper.\
    \ The proposed system combines open-vocabulary object detection, image segmentation,\
    \ boundary-aware point assignment, real-time point tracking, and monocular depth\
    \ estimation to recover object motion and geometry from visual observations. A\
    \ key component of the framework is a language-based stiffness estimation model\
    \ that infers an object's expected compliance from its semantic description and\
    \ provides an object-level prior for selecting the grasping strategy before contact.\
    \ For deformable objects, grasp adaptation is governed by a Procrustes-based dissimilarity\
    \ measure computed from tracked keypoints, which acts as a visual proxy for deformation.\
    \ For rigid objects, the gripper width is regulated through the scaling of tracked\
    \ point distances. We validate the proposed method in real-world pick-and-place\
    \ experiments on a Franka Emika Research 3 arm using objects with substantially\
    \ different mechanical properties, including lettuce, fresh mozzarella cheese,\
    \ croissants, paper towels, and hard plastic bottles. Results demonstrate that\
    \ the framework achieves stable grasping across both soft and rigid objects using\
    \ visual feedback alone, highlighting a practical, sensor-efficient, and generalizable\
    \ approach for food handling and household manipulation."
  zh: "arXiv:2607.07897v1 Announce Type: new \nAbstract: Grasping in unstructured\
    \ environments requires handling objects with widely different mechanical properties,\
    \ from soft and deformable items to rigid everyday objects. Most existing approaches\
    \ address these categories separately and often rely on tactile sensing, object-specific\
    \ models, or specialized grippers. In this paper, we present a unified monocular\
    \ vision-based grasping framework that targets both soft and rigid objects within\
    \ a single control pipeline, using only RGB input and a position-controlled gripper.\
    \ The proposed system combines open-vocabulary object detection, image segmentation,\
    \ boundary-aware point assignment, real-time point tracking, and monocular depth\
    \ estimation to recover object motion and geometry from visual observations. A\
    \ key component of the framework is a language-based stiffness estimation model\
    \ that infers an object's expected compliance from its semantic description and\
    \ provides an object-level prior for selecting the grasping strategy before contact.\
    \ For deformable objects, grasp adaptation is governed by a Procrustes-based dissimilarity\
    \ measure computed from tracked keypoints, which acts as a visual proxy for deformation.\
    \ For rigid objects, the gripper width is regulated through the scaling of tracked\
    \ point distances. We validate the proposed method in real-world pick-and-place\
    \ experiments on a Franka Emika Research 3 arm using objects with substantially\
    \ different mechanical properties, including lettuce, fresh mozzarella cheese,\
    \ croissants, paper towels, and hard plastic bottles. Results demonstrate that\
    \ the framework achieves stable grasping across both soft and rigid objects using\
    \ visual feedback alone, highlighting a practical, sensor-efficient, and generalizable\
    \ approach for food handling and household manipulation."
  ko: ''
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
- monocular_vision_based_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-11'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Monocular Vision Based Control Framework for Grasping (arXiv)
  url: https://arxiv.org/abs/2607.07897
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.07897v1 Announce Type: new 
Abstract: Grasping in unstructured environments requires handling objects with widely different mechanical properties, from soft and deformable items to rigid everyday objects. Most existing approaches address these categories separately and often rely on tactile sensing, object-specific models, or specialized grippers. In this paper, we present a unified monocular vision-based grasping framework that targets both soft and rigid objects within a single control pipeline, using only RGB input and a position-controlled gripper. The proposed system combines open-vocabulary object detection, image segmentation, boundary-aware point assignment, real-time point tracking, and monocular depth estimation to recover object motion and geometry from visual observations. A key component of the framework is a language-based stiffness estimation model that infers an object's expected compliance from its semantic description and provides an object-level prior for selecting the grasping strategy before contact. For deformable objects, grasp adaptation is governed by a Procrustes-based dissimilarity measure computed from tracked keypoints, which acts as a visual proxy for deformation. For rigid objects, the gripper width is regulated through the scaling of tracked point distances. We validate the proposed method in real-world pick-and-place experiments on a Franka Emika Research 3 arm using objects with substantially different mechanical properties, including lettuce, fresh mozzarella cheese, croissants, paper towels, and hard plastic bottles. Results demonstrate that the framework achieves stable grasping across both soft and rigid objects using visual feedback alone, highlighting a practical, sensor-efficient, and generalizable approach for food handling and household manipulation.
