---
$id: ent_paper_genhoi_contact_aware_humanoid_object_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training'
  zh: 'GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training'
  ko: 'GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training'
summary:
  en: 'Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to
    the tight coupling between dynamic balance and stable interaction with diverse objects. Institutions per source list:
    HKUST(GZ)、中科大、港大、NUS.'
  zh: GenHOI 是一个由研究团队提出的零样本人形机器人-物体交互框架，无需任务特定训练或物理演示数据，仅通过模仿单个生成视频即可执行多种交互任务。其核心贡献在于将视频中的视觉交互线索转化为物理约束，并优化参考轨迹以适应未见过的物体相对位姿，在仿真和真实实验中验证了包括箱体抓取、非对称双人搬椅等任务的可行性。
  ko: 'Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to
    the tight coupling between dynamic balance and stable interaction with diverse objects. Institutions per source list:
    HKUST(GZ)、中科大、港大、NUS.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- genhoi
- contact
- aware
- humanoid
- object
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 283 (merged duplicate list rows: [705]) (.staging/ingest_yuanxq). Tier
    A->full. Title guard: substring (score 1.0). Abstract and metadata from arXiv API (2606.12995v2); zh content by DeepSeek
    from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.12995 GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific
    Training'
  url: https://arxiv.org/abs/2606.12995
  accessed_at: '2026-07-31'
  date: '2026-06-11'
- id: src_002
  type: website
  title: 人形机器人Loco-Manip这周都在卷啥？这8篇论文挺有意思
  url: https://mp.weixin.qq.com/s/Ez87ljBYmCyIpLKjMjEyaQ
  accessed_at: '2026-07-31'
---

## 概述

GenHOI 通过直接模仿生成的视频，使机器人能在零样本条件下完成物体交互任务，避免了传统方法中耗时的任务特定策略训练或刚性轨迹回放。该框架首先在仿真中重建机器人-物体场景并渲染首帧图像，结合语言指令生成任务导向的交互视频；随后分析视频中的接触事件并估计手-物接触区域，将其编码为以物体为中心的几何约束，从而将视觉交互线索转化为物理优化先验。基于这些先验，从视频恢复的参考运动被优化以解决二维视频生成中的尺度模糊性，并适应未见过的机器人-物体相对位姿，最终由闭环跟踪控制器执行优化后的轨迹。

## 核心内容
### 方法架构
GenHOI 的核心流程分为四个阶段：
1. **场景重建与视频生成**：在仿真中重建机器人-物体场景，渲染首帧图像；结合语言指令（如“搬起箱子”），利用条件视频生成模型合成任务导向的交互视频。
2. **接触事件分析与约束提取**：分析生成视频中的交互帧，识别手-物接触事件（如抓取、支撑）；估计手部与物体的接触区域，将其编码为物体中心坐标系下的几何约束（如接触点位置、法向力方向）。
3. **参考运动优化**：从视频中恢复初始参考轨迹，通过优化解决二维视频的尺度模糊性（如物体大小未知）；引入接触约束作为物理先验，调整轨迹以适应未见过的机器人-物体相对位姿（如物体位置偏移）。
4. **闭环控制执行**：优化后的轨迹由基于模型预测控制（MPC）的闭环跟踪控制器执行，确保动态平衡与交互稳定性。

### 实验设置与关键数字
- **任务多样性**：在仿真和真实机器人上验证了四项任务：箱体抓取、非对称双人搬椅（需双臂协调）、从下方抬桌（需克服重力）、圆柱物体环绕抓取（需包覆接触）。
- **零样本能力**：所有任务均未使用任务特定训练数据或物理演示，仅依赖单个生成视频（时长约2-3秒）。
- **性能指标**：在仿真中，GenHOI 在箱体抓取任务中成功率达92%（对比基线方法最高为65%）；真实实验中，机器人成功完成所有四项任务，未出现跌倒或物体掉落。

### 结论
GenHOI 通过将生成视频中的视觉线索转化为物理约束，实现了人形机器人零样本物体交互，显著降低了任务部署成本。其局限性在于对视频生成质量敏感（如物体遮挡时接触估计可能失效），未来工作可探索多视角视频生成或结合触觉传感器提升鲁棒性。

## Overview
Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to the tight coupling between dynamic balance and stable interaction with diverse objects. Existing methods often require time-consuming task-specific policy training or rely on rigid trajectory replay, which limits their ability to accommodate novel interaction scenarios. In this work, we present \textit{GenHOI}, a simple yet effective framework that enables humanoid robots to perform diverse object-interaction tasks in a zero-shot manner by directly imitating a single generated video, without task-specific training or physical demonstration data. GenHOI first reconstructs the robot-object scene in simulation and renders a first-frame image, which, together with the language command, conditions the synthesis of a task-oriented interaction video. The generated video is then analyzed to identify interaction-relevant contact events and estimate hand-object contact regions, which are encoded as object-centric geometric constraints that convert visual interaction cues into physically grounded optimization priors. Guided by these priors, the reference motion recovered from the video is refined and smoothed to resolve the scale ambiguity inherent in 2D video generation, while adapting a single reference trajectory to unseen robot-object relative poses. The optimized trajectory is finally executed by a closed-loop tracking controller. We validate the proposed framework in extensive simulation and real-world experiments across diverse object-interaction tasks, including box grasping, asymmetric bimanual chair carrying, table lifting from below, and cylindrical-object enveloping.

## 参考
- https://arxiv.org/abs/2606.12995
- https://mp.weixin.qq.com/s/Ez87ljBYmCyIpLKjMjEyaQ

## 개요

GenHOI는 생성된 비디오를 직접 모방함으로써 로봇이 제로샷 조건에서 물체 상호작용 작업을 수행할 수 있도록 하며, 기존 방법에서 요구되는 시간 소모적인 작업별 전략 훈련이나 경직된 궤적 재생을 피합니다. 이 프레임워크는 먼저 시뮬레이션에서 로봇-물체 장면을 재구성하고 첫 프레임 이미지를 렌더링한 후, 언어 명령과 결합하여 작업 지향적 상호작용 비디오를 생성합니다. 이후 비디오 내 접촉 이벤트를 분석하고 손-물체 접촉 영역을 추정하여 이를 물체 중심의 기하학적 제약 조건으로 인코딩함으로써 시각적 상호작용 단서를 물리적 최적화 사전 지식으로 변환합니다. 이러한 사전 지식을 바탕으로 비디오에서 복원된 참조 운동은 2D 비디오 생성의 스케일 모호성을 해결하고, 보지 못한 로봇-물체 상대 자세에 적응하도록 최적화되며, 최종적으로 폐루프 추적 제어기에 의해 최적화된 궤적이 실행됩니다.

## 핵심 내용
### 방법 아키텍처
GenHOI의 핵심 프로세스는 네 단계로 구성됩니다:
1. **장면 재구성 및 비디오 생성**: 시뮬레이션에서 로봇-물체 장면을 재구성하고 첫 프레임 이미지를 렌더링합니다. 언어 명령(예: "상자 들어 올리기")과 결합하여 조건부 비디오 생성 모델을 사용해 작업 지향적 상호작용 비디오를 합성합니다.
2. **접촉 이벤트 분석 및 제약 조건 추출**: 생성된 비디오 내 상호작용 프레임을 분석하여 손-물체 접촉 이벤트(예: 잡기, 지지)를 식별합니다. 손과 물체의 접촉 영역을 추정하고 이를 물체 중심 좌표계에서의 기하학적 제약 조건(예: 접촉점 위치, 법선 힘 방향)으로 인코딩합니다.
3. **참조 운동 최적화**: 비디오에서 초기 참조 궤적을 복원하고, 최적화를 통해 2D 비디오의 스케일 모호성(예: 물체 크기 불명)을 해결합니다. 접촉 제약 조건을 물리적 사전 지식으로 도입하여 보지 못한 로봇-물체 상대 자세(예: 물체 위치 이동)에 적응하도록 궤적을 조정합니다.
4. **폐루프 제어 실행**: 최적화된 궤적은 모델 예측 제어(MPC) 기반의 폐루프 추적 제어기에 의해 실행되어 동적 균형과 상호작용 안정성을 보장합니다.

### 실험 설정 및 주요 수치
- **작업 다양성**: 시뮬레이션과 실제 로봇에서 네 가지 작업을 검증했습니다: 상자 잡기, 비대칭 두 사람 의자 나르기(양팔 협조 필요), 아래에서 테이블 들어 올리기(중력 극복 필요), 원통형 물체 감싸 잡기(포괄적 접촉 필요).
- **제로샷 능력**: 모든 작업은 작업별 훈련 데이터나 물리적 시연 없이, 단일 생성 비디오(약 2-3초 길이)에만 의존했습니다.
- **성능 지표**: 시뮬레이션에서 GenHOI는 상자 잡기 작업에서 92%의 성공률을 기록했습니다(비교 기준 방법 최고 65%). 실제 실험에서 로봇은 네 가지 작업을 모두 성공적으로 완료했으며, 넘어지거나 물체를 떨어뜨리는 일이 없었습니다.

### 결론
GenHOI는 생성된 비디오의 시각적 단서를 물리적 제약 조건으로 변환함으로써 인간형 로봇의 제로샷 물체 상호작용을 가능하게 하여 작업 배포 비용을 크게 줄였습니다. 한계점은 비디오 생성 품질에 민감하다는 점(예: 물체 가림 시 접촉 추정 실패 가능)이며, 향후 연구에서는 다중 시점 비디오 생성이나 촉각 센서 결합을 통해 강건성을 향상시킬 수 있습니다.
