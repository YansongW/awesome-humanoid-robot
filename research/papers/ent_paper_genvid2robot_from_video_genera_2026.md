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
  en: 'arXiv:2607.09191v1 Announce Type: new Abstract: Generated videos provide useful visual motion priors for robot manipulation,
    but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry,
    grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable
    in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated
    video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction,
    GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated
    video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse
    relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct
    robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is
    then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution
    trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution
    mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation
    module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate
    that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with
    sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.'
  zh: 'arXiv:2607.09191v1 Announce Type: new Abstract: Generated videos provide useful visual motion priors for robot manipulation,
    but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry,
    grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable
    in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated
    video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction,
    GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated
    video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse
    relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct
    robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is
    then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution
    trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution
    mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation
    module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate
    that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with
    sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.'
  ko: 'arXiv:2607.09191v1 Announce Type: new Abstract: Generated videos provide useful visual motion priors for robot manipulation,
    but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry,
    grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable
    in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated
    video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction,
    GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated
    video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse
    relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct
    robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is
    then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution
    trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution
    mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation
    module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate
    that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with
    sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.'
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

## Overview
Generated videos provide useful visual motion priors for robot manipulation, but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry, grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.

## Content
Generated videos provide useful visual motion priors for robot manipulation, but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry, grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.

## 개요
생성된 비디오는 로봇 조작을 위한 유용한 시각적 움직임 사전 정보를 제공하지만, 시각적 그럴듯함이 물리적 실행 가능성을 의미하지는 않습니다. 생성된 비디오는 일반적으로 미터법 기하학, 그립 기반, 로봇 운동학적 실행 가능성 및 실행 시간 피드백이 부족하여 실제 조작에서 직접적인 궤적 재생이 신뢰할 수 없습니다. 본 논문은 생성된 비디오 움직임을 실행 가능한 실제 로봇 조작 궤적으로 변환하는 강체-기하학적 일관성 프레임워크인 GenVid2Robot을 제시합니다. 초기 RGB-D 관찰과 작업 명령이 주어지면, GenVid2Robot은 실제 첫 번째 프레임에서 작업 관련 의미론적 앵커를 샘플링하고, 생성된 비디오 후보를 통해 이러한 앵커를 추적하며, 결과 2D 움직임이 희소 상대 $SE(3)$ 모델 하에서 첫 번째 프레임 RGB-D 앵커로 설명될 수 있는지 검증합니다. 이러한 방식으로 생성된 비디오는 직접적인 로봇 시연이 아닌 불확실한 시각적 움직임 가설로 취급됩니다. 기하학적으로 일관된 움직임만 로봇으로 전송됩니다. 허용된 상대 움직임은 마스크 제약 그립에 의해 선택된 실제 그립 시간 TCP 포즈에 적용되어 시각적 움직임 사전 정보와 물리적 그립 구성 모두와 일관된 그립 조건 실행 궤적을 생성합니다. RGB-D 노이즈, 캘리브레이션 잔차 및 작은 접촉 유발 변위로 인한 실행 불일치를 줄이기 위해, 제한된 깊이 보상 모듈이 전체 온라인 재계획을 가정하지 않고 로컬 깊이 방향 오류를 수정합니다. 실제 로봇 실험은 GenVid2Robot이 희소 미터법 기하학, 그립 제약, 로봇 실행 가능성 검사 및 제한된 실행 피드백으로 시각적 움직임 사전 정보를 기반으로 하여 생성된 비디오 유도 조작의 신뢰성을 향상시킴을 보여줍니다.

## 핵심 내용
생성된 비디오는 로봇 조작을 위한 유용한 시각적 움직임 사전 정보를 제공하지만, 시각적 그럴듯함이 물리적 실행 가능성을 의미하지는 않습니다. 생성된 비디오는 일반적으로 미터법 기하학, 그립 기반, 로봇 운동학적 실행 가능성 및 실행 시간 피드백이 부족하여 실제 조작에서 직접적인 궤적 재생이 신뢰할 수 없습니다. 본 논문은 생성된 비디오 움직임을 실행 가능한 실제 로봇 조작 궤적으로 변환하는 강체-기하학적 일관성 프레임워크인 GenVid2Robot을 제시합니다. 초기 RGB-D 관찰과 작업 명령이 주어지면, GenVid2Robot은 실제 첫 번째 프레임에서 작업 관련 의미론적 앵커를 샘플링하고, 생성된 비디오 후보를 통해 이러한 앵커를 추적하며, 결과 2D 움직임이 희소 상대 $SE(3)$ 모델 하에서 첫 번째 프레임 RGB-D 앵커로 설명될 수 있는지 검증합니다. 이러한 방식으로 생성된 비디오는 직접적인 로봇 시연이 아닌 불확실한 시각적 움직임 가설로 취급됩니다. 기하학적으로 일관된 움직임만 로봇으로 전송됩니다. 허용된 상대 움직임은 마스크 제약 그립에 의해 선택된 실제 그립 시간 TCP 포즈에 적용되어 시각적 움직임 사전 정보와 물리적 그립 구성 모두와 일관된 그립 조건 실행 궤적을 생성합니다. RGB-D 노이즈, 캘리브레이션 잔차 및 작은 접촉 유발 변위로 인한 실행 불일치를 줄이기 위해, 제한된 깊이 보상 모듈이 전체 온라인 재계획을 가정하지 않고 로컬 깊이 방향 오류를 수정합니다. 실제 로봇 실험은 GenVid2Robot이 희소 미터법 기하학, 그립 제약, 로봇 실행 가능성 검사 및 제한된 실행 피드백으로 시각적 움직임 사전 정보를 기반으로 하여 생성된 비디오 유도 조작의 신뢰성을 향상시킴을 보여줍니다.
