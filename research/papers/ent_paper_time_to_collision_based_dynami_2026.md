---
$id: ent_paper_time_to_collision_based_dynami_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Time-to-Collision Based Dynamic Obstacle Avoidance Using Pretrained Vision Models
    for Robots in Unstructured Environments
  zh: Time-to-Collision Based Dynamic Obstacle Avoidance Using Pretrained Vision Models
    for Robots in Unstructured Environments
  ko: ''
summary:
  en: "arXiv:2607.07885v1 Announce Type: new \nAbstract: Dynamic obstacle avoidance\
    \ in unstructured outdoor environments remains a critical challenge for autonomous\
    \ mobile robots, particularly when large-scale robot-specific training data and\
    \ simulation-based policies are impractical. We present a data-efficient, interpretable\
    \ method for vision-based dynamic obstacle avoidance that operates entirely on\
    \ real-world data, avoiding the sim-to-real transfer problem inherent in simulation-trained\
    \ policies. Our approach leverages UniDepth, a large pretrained monocular depth\
    \ estimation model, to produce dense depth maps from RGB video without requiring\
    \ stereo cameras or LiDAR at inference time. Dynamic obstacle avoidance is achieved\
    \ by extending the SuperPoint and SuperGlue feature correspondence pipeline to\
    \ track keypoints across long frame sequences, projecting their 2D pixel-space\
    \ positions into 3D using camera intrinsics and predicted depth, running bundle\
    \ adjustment initialized from these 3D keypoints, and computing per-keypoint time-to-collision\
    \ (TTC). A 2D motion primitive in the ground plane is then selected to move the\
    \ robot away from the closest point of approach of the minimum-TTC keypoint. Evaluated\
    \ on real-world data from the M3ED dataset, our pipeline achieves a precision\
    \ of 0.49 and a recall of 0.38 in identifying frames with a ground truth TTC below\
    \ 1 second, and correctly generates the evasive motion direction in 84\\% of true\
    \ positive detections. Crucially, it detects at least one frame with TTC less\
    \ than 1 second for 20 out of 22 unique physical obstacles present in our test\
    \ sequences. Unlike end-to-end learned methods that demand thousands of hours\
    \ of robot-specific training data, our approach eliminates model training entirely,\
    \ requiring only 74 seconds of data for hyperparameter tuning. This demonstrates\
    \ exceptional data efficiency while preserving interpretable and generalizable\
    \ behavior across diverse obstacle types."
  zh: "arXiv:2607.07885v1 Announce Type: new \nAbstract: Dynamic obstacle avoidance\
    \ in unstructured outdoor environments remains a critical challenge for autonomous\
    \ mobile robots, particularly when large-scale robot-specific training data and\
    \ simulation-based policies are impractical. We present a data-efficient, interpretable\
    \ method for vision-based dynamic obstacle avoidance that operates entirely on\
    \ real-world data, avoiding the sim-to-real transfer problem inherent in simulation-trained\
    \ policies. Our approach leverages UniDepth, a large pretrained monocular depth\
    \ estimation model, to produce dense depth maps from RGB video without requiring\
    \ stereo cameras or LiDAR at inference time. Dynamic obstacle avoidance is achieved\
    \ by extending the SuperPoint and SuperGlue feature correspondence pipeline to\
    \ track keypoints across long frame sequences, projecting their 2D pixel-space\
    \ positions into 3D using camera intrinsics and predicted depth, running bundle\
    \ adjustment initialized from these 3D keypoints, and computing per-keypoint time-to-collision\
    \ (TTC). A 2D motion primitive in the ground plane is then selected to move the\
    \ robot away from the closest point of approach of the minimum-TTC keypoint. Evaluated\
    \ on real-world data from the M3ED dataset, our pipeline achieves a precision\
    \ of 0.49 and a recall of 0.38 in identifying frames with a ground truth TTC below\
    \ 1 second, and correctly generates the evasive motion direction in 84\\% of true\
    \ positive detections. Crucially, it detects at least one frame with TTC less\
    \ than 1 second for 20 out of 22 unique physical obstacles present in our test\
    \ sequences. Unlike end-to-end learned methods that demand thousands of hours\
    \ of robot-specific training data, our approach eliminates model training entirely,\
    \ requiring only 74 seconds of data for hyperparameter tuning. This demonstrates\
    \ exceptional data efficiency while preserving interpretable and generalizable\
    \ behavior across diverse obstacle types."
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
- time_to_collision_based_dynami
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
  title: Time-to-Collision Based Dynamic Obstacle Avoidance Using Pretrained Vision
    Models for Robots in Unstructured Environments (arXiv)
  url: https://arxiv.org/abs/2607.07885
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.07885v1 Announce Type: new 
Abstract: Dynamic obstacle avoidance in unstructured outdoor environments remains a critical challenge for autonomous mobile robots, particularly when large-scale robot-specific training data and simulation-based policies are impractical. We present a data-efficient, interpretable method for vision-based dynamic obstacle avoidance that operates entirely on real-world data, avoiding the sim-to-real transfer problem inherent in simulation-trained policies. Our approach leverages UniDepth, a large pretrained monocular depth estimation model, to produce dense depth maps from RGB video without requiring stereo cameras or LiDAR at inference time. Dynamic obstacle avoidance is achieved by extending the SuperPoint and SuperGlue feature correspondence pipeline to track keypoints across long frame sequences, projecting their 2D pixel-space positions into 3D using camera intrinsics and predicted depth, running bundle adjustment initialized from these 3D keypoints, and computing per-keypoint time-to-collision (TTC). A 2D motion primitive in the ground plane is then selected to move the robot away from the closest point of approach of the minimum-TTC keypoint. Evaluated on real-world data from the M3ED dataset, our pipeline achieves a precision of 0.49 and a recall of 0.38 in identifying frames with a ground truth TTC below 1 second, and correctly generates the evasive motion direction in 84\% of true positive detections. Crucially, it detects at least one frame with TTC less than 1 second for 20 out of 22 unique physical obstacles present in our test sequences. Unlike end-to-end learned methods that demand thousands of hours of robot-specific training data, our approach eliminates model training entirely, requiring only 74 seconds of data for hyperparameter tuning. This demonstrates exceptional data efficiency while preserving interpretable and generalizable behavior across diverse obstacle types.
