---
$id: ent_paper_ge_sim_2_0_roadmap_comprehensive_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation'
  zh: 'GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation'
  ko: 'GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation'
summary:
  en: We introduce GE-Sim 2.0 (Genie Envisioner World Simulator 2.0), a closed-loop video world simulator for robotic manipulation.
    Building on the action-conditioned video generation framework of Genie Envisioner, GE-Sim 2.0 is re-trained on thousands
    of hours of real-world robot data spanning teleoperation, contact-rich interaction, and on-robot policy deployment, substantially
    improving action-following fidelity and tra
  zh: GE-Sim 2.0 是一个面向机器人操作的闭环视频世界模拟器，由 Genie Envisioner 团队开发。其核心贡献在于通过三个新模块（状态专家、世界裁判、加速框架）将视频模拟与策略学习闭环连接，仅用 2B 参数即登顶 WorldArena
    排行榜，并实现真实世界策略性能提升。
  ko: We introduce GE-Sim 2.0 (Genie Envisioner World Simulator 2.0), a closed-loop video world simulator for robotic manipulation.
    Building on the action-conditioned video generation framework of Genie Envisioner, GE-Sim 2.0 is re-trained on thousands
    of hours of real-world robot data spanning teleoperation, contact-rich interaction, and on-robot policy deployment, substantially
    improving action-following fidelity and tra
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
- ge
- sim
- '2'
- '0'
- roadmap
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 372 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2605.27491v1); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.27491 GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation'
  url: https://arxiv.org/abs/2605.27491
  accessed_at: '2026-07-31'
  date: '2026-05-26'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

GE-Sim 2.0 基于 Genie Envisioner 的动作条件视频生成框架，在数千小时真实机器人数据（涵盖遥操作、接触密集交互及策略部署）上重新训练，显著提升了动作跟随精度与轨迹覆盖。在此基础上，新增三个模块：状态专家从视频潜变量解码本体感知状态，支持下游 VLA 策略的下一块预测；世界裁判根据任务指令对生成轨迹评分，提供机器可验证的成功信号与奖励；加速框架在单块 H100 上 2.3 秒生成 25 帧，推理时可跳过最多 4 帧以支持长时评估。该模型以 2B 参数超越专用机器人世界模型与闭源通用视频生成器，其训练的策略在真实场景中取得可量化增益。

## 核心内容
### 方法架构
GE-Sim 2.0 延续 Genie Envisioner 的动作条件视频生成范式，但重新训练于大规模真实机器人数据，包括遥操作、接触密集交互及策略部署场景，从而提升动作跟随保真度与轨迹多样性。其闭环系统由三个核心模块构成：
- **状态专家（State Expert）**：从视频潜变量中解码本体感知状态（如关节角度、末端执行器位姿），使下游 VLA 策略能够基于模拟视频进行下一块预测（next-chunk prediction）。
- **世界裁判（World Judge）**：对生成的视频轨迹进行任务指令对齐评分，输出机器可验证的成功信号与奖励，替代人工检查。
- **加速框架**：在单块 H100 GPU 上，25 帧生成仅需 2.3 秒；推理时支持最多 4 倍帧跳过（frame skipping），适用于长时评估。

### 实验设置与关键数字
- **基准测试**：在公开的 WorldArena 排行榜上，GE-Sim 2.0 以 2B 参数取得榜首，超越专用机器人世界模型（如 RoboGen）及闭源通用视频生成器（如 Sora）。
- **性能指标**：动作跟随精度与轨迹覆盖相比 Genie Envisioner 基线提升显著；加速框架使 25 帧生成延迟降至 2.3 秒。
- **策略学习**：基于 GE-Sim 2.0 生成的轨迹与奖励训练的策略，在真实机器人操作任务中取得可量化的性能提升，验证了闭环模拟到策略学习的有效性。

### 结论
GE-Sim 2.0 通过状态专家、世界裁判与加速框架，将视频世界模拟从开环生成推进至闭环策略学习平台。其轻量级参数（2B）与高效推理能力，为大规模机器人操作策略的评估与闭环训练提供了实用方案。

## Overview
We introduce GE-Sim 2.0 (Genie Envisioner World Simulator 2.0), a closed-loop video world simulator for robotic manipulation. Building on the action-conditioned video generation framework of Genie Envisioner, GE-Sim 2.0 is re-trained on thousands of hours of real-world robot data spanning teleoperation, contact-rich interaction, and on-robot policy deployment, substantially improving action-following fidelity and trajectory coverage. On top of this foundation, three new modules close the loop from video simulation to policy learning: a state expert that decodes proprioceptive state from video latents to support next-chunk prediction by downstream VLA policies; a world judge that scores generated rollouts against task instructions, yielding machine-verifiable success signals and rewards in place of manual inspection; and an acceleration framework that delivers a 25-frame rollout in 2.3 seconds on a single H100, with up to 4* frame skipping at inference for long-horizon evaluation. GE-Sim 2.0 tops the public WorldArena leaderboard at only 2B parameters, outperforming both dedicated robotic world models and closed-source general video generators, and policies trained against its rollouts and rewards translate into measurable real-world gains, establishing GE-Sim 2.0 as a practical platform for scalable evaluation and closed-loop learning of manipulation policies.

## 参考
- https://arxiv.org/abs/2605.27491
- https://github.com/ImChong/Robotics_Notebooks

## 개요

GE-Sim 2.0은 Genie Envisioner의 동작 조건 비디오 생성 프레임워크를 기반으로, 수천 시간의 실제 로봇 데이터(원격 조작, 접촉 밀집 상호작용 및 정책 배포 포함)에서 재학습되어 동작 추종 정밀도와 궤적 커버리지를 크게 향상시켰습니다. 이를 바탕으로 세 가지 모듈이 추가되었습니다: 상태 전문가는 비디오 잠재 변수에서 고유 인식 상태를 디코딩하여 하위 VLA 정책의 다음 블록 예측을 지원합니다. 세계 심판은 작업 명령에 따라 생성된 궤적을 평가하여 기계가 검증 가능한 성공 신호와 보상을 제공합니다. 가속 프레임워크는 단일 H100에서 2.3초 만에 25프레임을 생성하며, 추론 시 최대 4프레임을 건너뛰어 장기 평가를 지원합니다. 이 모델은 2B 파라미터로 전용 로봇 세계 모델과 폐쇄형 범용 비디오 생성기를 능가하며, 학습된 정책은 실제 환경에서 정량적 이점을 얻습니다.

## 핵심 내용
### 방법 아키텍처
GE-Sim 2.0은 Genie Envisioner의 동작 조건 비디오 생성 패러다임을 계승하지만, 원격 조작, 접촉 밀집 상호작용 및 정책 배포 시나리오를 포함한 대규모 실제 로봇 데이터에서 재학습되어 동작 추종 충실도와 궤적 다양성을 향상시킵니다. 폐쇄 루프 시스템은 세 가지 핵심 모듈로 구성됩니다:
- **상태 전문가(State Expert)**: 비디오 잠재 변수에서 고유 인식 상태(관절 각도, 엔드 이펙터 자세 등)를 디코딩하여 하위 VLA 정책이 시뮬레이션 비디오를 기반으로 다음 블록 예측(next-chunk prediction)을 수행할 수 있도록 합니다.
- **세계 심판(World Judge)**: 생성된 비디오 궤적을 작업 명령 정렬에 따라 평가하여 기계가 검증 가능한 성공 신호와 보상을 출력하며, 수동 검사를 대체합니다.
- **가속 프레임워크**: 단일 H100 GPU에서 25프레임 생성에 2.3초만 소요되며, 추론 시 최대 4배 프레임 건너뛰기(frame skipping)를 지원하여 장기 평가에 적합합니다.

### 실험 설정 및 주요 수치
- **벤치마크 테스트**: 공개된 WorldArena 순위에서 GE-Sim 2.0은 2B 파라미터로 1위를 차지하며, 전용 로봇 세계 모델(RoboGen 등) 및 폐쇄형 범용 비디오 생성기(Sora 등)를 능가합니다.
- **성능 지표**: 동작 추종 정밀도와 궤적 커버리지가 Genie Envisioner 기준선 대비 크게 향상되었으며, 가속 프레임워크로 25프레임 생성 지연 시간이 2.3초로 단축되었습니다.
- **정책 학습**: GE-Sim 2.0에서 생성된 궤적과 보상을 기반으로 학습된 정책은 실제 로봇 조작 작업에서 정량적 성능 향상을 보여주며, 폐쇄 루프 시뮬레이션에서 정책 학습으로의 효과성을 입증합니다.

### 결론
GE-Sim 2.0은 상태 전문가, 세계 심판 및 가속 프레임워크를 통해 비디오 세계 시뮬레이션을 개방형 생성에서 폐쇄 루프 정책 학습 플랫폼으로 발전시켰습니다. 경량 파라미터(2B)와 효율적인 추론 능력은 대규모 로봇 조작 정책의 평가와 폐쇄 루프 학습에 실용적인 솔루션을 제공합니다.
