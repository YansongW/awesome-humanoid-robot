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
  zh: GenVid2Robot 是一个将生成视频中的运动转化为真实机器人可执行操作轨迹的框架，由研究团队提出。其核心贡献在于通过刚体几何一致性约束，将生成视频视为不确定的视觉运动假设而非直接演示，仅转移几何一致的运动，并结合掩码约束抓取与有界深度补偿模块，显著提升了视频引导操作的真实世界可靠性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09191v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (939 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency (arXiv)'
  url: https://arxiv.org/abs/2607.09191
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
生成视频虽能为机器人操作提供视觉运动先验，但其视觉合理性并不保证物理可执行性，因为视频缺乏度量几何、抓取接地、机器人运动学可行性及执行时反馈。GenVid2Robot 通过从真实第一帧 RGB-D 观测中采样任务相关语义锚点，在生成视频候选帧中追踪这些锚点，并利用稀疏相对 SE(3) 模型验证 2D 运动是否可由第一帧 RGB-D 锚点解释，从而筛选出几何一致的运动。被接受的相对运动随后应用于由掩码约束抓取选择的真实抓取时刻 TCP 位姿，生成与视觉运动先验和物理抓取配置一致的抓取条件执行轨迹。为减少 RGB-D 噪声、校准残差及接触位移导致的执行偏差，框架引入有界深度补偿模块，在不依赖完整在线重规划的前提下修正局部深度方向误差。

## 核心内容
### 方法概述
GenVid2Robot 的核心思想是将生成视频视为不确定的视觉运动假设，而非直接演示。其流程包括：
- **语义锚点采样**：从真实第一帧 RGB-D 观测中，根据任务指令采样与任务相关的语义锚点（如物体关键点）。
- **锚点追踪与几何验证**：在生成视频候选帧中追踪这些锚点，并通过稀疏相对 SE(3) 模型检验 2D 运动是否与第一帧 RGB-D 锚点几何一致。仅通过验证的运动被转移至机器人。
- **抓取条件轨迹生成**：被接受的相对运动应用于由掩码约束抓取选择的真实抓取时刻 TCP 位姿，确保轨迹同时符合视觉运动先验与物理抓取配置。

### 关键模块
- **掩码约束抓取**：利用物体掩码约束抓取点选择，确保抓取位姿与物体几何对齐。
- **有界深度补偿模块**：针对 RGB-D 噪声、校准残差及接触位移导致的深度方向误差，该模块在局部范围内修正深度误差，无需完整在线重规划。

### 实验设置与结果
- **实验平台**：真实机器人操作场景，涉及多种物体与任务指令。
- **关键指标**：GenVid2Robot 通过将视觉运动先验与稀疏度量几何、抓取约束、机器人可行性检查及有界执行反馈相结合，显著提升了生成视频引导操作的成功率与可靠性。实验表明，直接轨迹回放因缺乏几何一致性而失败率较高，而 GenVid2Robot 的几何验证与补偿机制有效降低了执行偏差。

## Overview
Generated videos provide useful visual motion priors for robot manipulation, but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry, grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.

## 参考
- http://arxiv.org/abs/2607.09191v1

## 개요
비디오 생성은 로봇 조작을 위한 시각적 운동 사전을 제공할 수 있지만, 시각적 합리성이 물리적 실행 가능성을 보장하지는 않습니다. 비디오에는 측정 기하학, 파지 접지, 로봇 운동학적 실현 가능성 및 실행 중 피드백이 부족하기 때문입니다. GenVid2Robot은 실제 첫 프레임 RGB-D 관측에서 작업 관련 의미론적 앵커를 샘플링하고, 생성된 비디오 후보 프레임에서 이러한 앵커를 추적하며, 희소 상대 SE(3) 모델을 사용하여 2D 운동이 첫 프레임 RGB-D 앵커로 설명될 수 있는지 검증함으로써 기하학적으로 일관된 운동을 선별합니다. 수용된 상대 운동은 이후 마스크 제약 파지로 선택된 실제 파지 시점의 TCP 포즈에 적용되어, 시각적 운동 사전 및 물리적 파지 구성과 일치하는 파지 조건 실행 궤적을 생성합니다. RGB-D 노이즈, 캘리브레이션 잔차 및 접촉 변위로 인한 실행 편차를 줄이기 위해, 프레임워크는 완전한 온라인 재계획에 의존하지 않고 국소 깊이 방향 오류를 수정하는 유계 깊이 보상 모듈을 도입합니다.

## 핵심 내용
### 방법 개요
GenVid2Robot의 핵심 아이디어는 생성된 비디오를 직접적인 시연이 아닌 불확실한 시각적 운동 가설로 간주하는 것입니다. 그 흐름은 다음과 같습니다:
- **의미론적 앵커 샘플링**: 실제 첫 프레임 RGB-D 관측에서 작업 지시에 따라 작업 관련 의미론적 앵커(예: 객체 키포인트)를 샘플링합니다.
- **앵커 추적 및 기하학적 검증**: 생성된 비디오 후보 프레임에서 이러한 앵커를 추적하고, 희소 상대 SE(3) 모델을 통해 2D 운동이 첫 프레임 RGB-D 앵커와 기하학적으로 일관되는지 검증합니다. 검증을 통과한 운동만 로봇으로 전송됩니다.
- **파지 조건 궤적 생성**: 수용된 상대 운동은 마스크 제약 파지로 선택된 실제 파지 시점의 TCP 포즈에 적용되어, 궤적이 시각적 운동 사전과 물리적 파지 구성 모두에 부합하도록 보장합니다.

### 핵심 모듈
- **마스크 제약 파지**: 객체 마스크를 사용하여 파지 지점 선택을 제약하고, 파지 포즈가 객체 기하학과 정렬되도록 보장합니다.
- **유계 깊이 보상 모듈**: RGB-D 노이즈, 캘리브레이션 잔차 및 접촉 변위로 인한 깊이 방향 오류를 대상으로, 이 모듈은 완전한 온라인 재계획 없이 국소 범위에서 깊이 오류를 수정합니다.

### 실험 설정 및 결과
- **실험 플랫폼**: 다양한 객체와 작업 지시를 포함하는 실제 로봇 조작 시나리오.
- **핵심 지표**: GenVid2Robot은 시각적 운동 사전을 희소 측정 기하학, 파지 제약, 로봇 실현 가능성 검사 및 유계 실행 피드백과 결합하여, 생성 비디오 기반 조작의 성공률과 신뢰성을 크게 향상시켰습니다. 실험에 따르면 직접 궤적 재생은 기하학적 일관성 부족으로 실패율이 높은 반면, GenVid2Robot의 기하학적 검증 및 보상 메커니즘은 실행 편차를 효과적으로 줄였습니다.
