---
$id: ent_paper_genvid2robot_from_video_genera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency'
  zh: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency'
  ko: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency'
summary:
  en: "arXiv:2607.09191v1 Announce Type: new \nAbstract: Generated videos provide useful visual motion priors for robot manipulation,\
    \ but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry,\
    \ grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable\
    \ in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts\
    \ generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and\
    \ a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors\
    \ through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D\
    \ anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion\
    \ hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot.\
    \ The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping,\
    \ producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical\
    \ grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced\
    \ displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online\
    \ replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided\
    \ manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking,\
    \ and bounded execution feedback."
  zh: "arXiv:2607.09191v1 Announce Type: new \nAbstract: Generated videos provide useful visual motion priors for robot manipulation,\
    \ but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry,\
    \ grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable\
    \ in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts\
    \ generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and\
    \ a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors\
    \ through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D\
    \ anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion\
    \ hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot.\
    \ The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping,\
    \ producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical\
    \ grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced\
    \ displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online\
    \ replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided\
    \ manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking,\
    \ and bounded execution feedback."
  ko: "arXiv:2607.09191v1 Announce Type: new \nAbstract: Generated videos provide useful visual motion priors for robot manipulation,\
    \ but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry,\
    \ grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable\
    \ in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts\
    \ generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and\
    \ a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors\
    \ through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D\
    \ anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion\
    \ hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot.\
    \ The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping,\
    \ producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical\
    \ grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced\
    \ displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online\
    \ replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided\
    \ manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking,\
    \ and bounded execution feedback."
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
- genvid2robot
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09191v1.
sources:
- id: src_001
  type: paper
  title: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency (arXiv)'
  url: https://arxiv.org/abs/2607.09191
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Generated videos provide useful visual motion priors for robot manipulation, but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry, grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.

## 核心内容
Generated videos provide useful visual motion priors for robot manipulation, but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry, grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.

## 参考
- http://arxiv.org/abs/2607.09191v1

