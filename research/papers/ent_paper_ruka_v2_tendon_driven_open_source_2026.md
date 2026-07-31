---
$id: ent_paper_ruka_v2_tendon_driven_open_source_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning'
  zh: 'Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning'
  ko: 'Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning'
summary:
  en: 'Lack of accessible and dexterous robot hardware has been a significant bottleneck to achieving human-level dexterity
    in robots. Last year, we released Ruka, a fully open-sourced, tendon-driven humanoid hand with 11 degrees of freedom -
    2 per finger and 3 at the thumb - buildable for under $1,300. Institutions per source list: New York University、New York
    University Shanghai.'
  zh: Ruka-v2 是一款完全开源、肌腱驱动的人形灵巧手，由前代 Ruka 升级而来，新增了解耦的 2 自由度平行腕关节和手指外展/内收功能。通过遥操作用户研究，Ruka-v2 在任务完成时间上降低 51.3%，成功率提升 21.2%，并支持双臂和单臂遥操作及自主策略学习。
  ko: 'Lack of accessible and dexterous robot hardware has been a significant bottleneck to achieving human-level dexterity
    in robots. Last year, we released Ruka, a fully open-sourced, tendon-driven humanoid hand with 11 degrees of freedom -
    2 per finger and 3 at the thumb - buildable for under $1,300. Institutions per source list: New York University、New York
    University Shanghai.'
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
- ruka
- v2
- tendon
- driven
- open
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 759 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2603.26660v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.26660 Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning'
  url: https://arxiv.org/abs/2603.26660
  accessed_at: '2026-07-31'
  date: '2026-03-27'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Ruka-v2 由团队在 Ruka 基础上开发，旨在解决前代缺乏腕部灵活性和手指外展/内收的问题。其平行腕关节提供独立的屈伸和桡尺偏运动，使机械手能在狭窄空间（如橱柜）中操作；手指外展/内收则支持抓取薄物体、手内旋转和书法等精细动作。通过遥操作用户研究，Ruka-v2 相比 Ruka 在任务完成时间上降低 51.3%，成功率提升 21.2%。该手部完全开源，所有 3D 打印文件、组装说明、控制器软件和视频均已公开。

## 核心内容
### 设计与架构
- **自由度**：Ruka-v2 在 Ruka 的 11 自由度（每指 2 自由度，拇指 3 自由度）基础上，新增了 2 自由度平行腕关节和手指外展/内收功能，总自由度提升。
- **平行腕关节**：采用解耦设计，实现独立的屈伸（flexion/extension）和桡尺偏（radial/ulnar deviation），运动平滑，适合在受限环境（如橱柜）中操作。
- **手指外展/内收**：允许手指横向运动，支持抓取薄物体、手内旋转和书法等任务。

### 实验设置与关键数字
- **用户研究**：通过遥操作任务对比 Ruka-v2 与 Ruka，发现：
  - 任务完成时间降低 51.3%
  - 成功率提升 21.2%
- **应用范围**：覆盖 13 项灵巧任务的单臂和双臂遥操作，以及 3 项任务的自主策略学习。

### 结论
Ruka-v2 通过新增腕部和手指外展/内收功能，显著提升了灵巧操作能力，并验证了其在机器人学习中的实用性。所有资源已开源，便于复现和扩展。

## Overview
Lack of accessible and dexterous robot hardware has been a significant bottleneck to achieving human-level dexterity in robots. Last year, we released Ruka, a fully open-sourced, tendon-driven humanoid hand with 11 degrees of freedom - 2 per finger and 3 at the thumb - buildable for under $1,300. It was one of the first fully open-sourced humanoid hands, and introduced a novel data-driven approach to finger control that captures tendon dynamics within the control system. Despite these contributions, Ruka lacked two degrees of freedom essential for closely imitating human behavior: wrist mobility and finger adduction/abduction. In this paper, we introduce Ruka-v2: a fully open-sourced, tendon-driven humanoid hand featuring a decoupled 2-DOF parallel wrist and abduction/adduction at the fingers. The parallel wrist adds smooth, independent flexion/extension and radial/ulnar deviation, enabling manipulation in confined environments such as cabinets. Abduction enables motions such as grasping thin objects, in-hand rotation, and calligraphy. We present the design of Ruka-v2 and evaluate it against Ruka through user studies on teleoperated tasks, finding a 51.3% reduction in completion time and a 21.2% increase in success rate. We further demonstrate its full range of applications for robot learning: bimanual and single-arm teleoperation across 13 dexterous tasks, and autonomous policy learning on 3 tasks. All 3D print files, assembly instructions, controller software, and videos are available at https://ruka-hand-v2.github.io/ .

## 参考
- https://arxiv.org/abs/2603.26660
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Ruka-v2는 팀이 Ruka를 기반으로 개발한 것으로, 이전 모델의 손목 유연성 부족과 손가락 외전/내전 문제를 해결하기 위해 설계되었습니다. 평행 손목 관절은 독립적인 굴곡/신전 및 요측/척측 편위 운동을 제공하여 로봇 손이 좁은 공간(예: 캐비닛)에서도 조작할 수 있게 합니다. 손가락 외전/내전은 얇은 물체 잡기, 손 내부 회전 및 서예와 같은 정밀 작업을 지원합니다. 원격 조작 사용자 연구 결과, Ruka-v2는 Ruka에 비해 작업 완료 시간이 51.3% 감소하고 성공률이 21.2% 향상되었습니다. 이 로봇 손은 완전히 오픈소스로, 모든 3D 프린팅 파일, 조립 설명서, 컨트롤러 소프트웨어 및 비디오가 공개되었습니다.

## 핵심 내용
### 설계 및 아키텍처
- **자유도**: Ruka-v2는 Ruka의 11자유도(각 손가락 2자유도, 엄지 3자유도)를 기반으로 2자유도 평행 손목 관절과 손가락 외전/내전 기능을 추가하여 총 자유도를 향상시켰습니다.
- **평행 손목 관절**: 분리 설계를 채택하여 독립적인 굴곡/신전 및 요측/척측 편위 운동을 구현하며, 움직임이 부드럽고 제한된 환경(예: 캐비닛)에서의 조작에 적합합니다.
- **손가락 외전/내전**: 손가락의 측면 움직임을 허용하여 얇은 물체 잡기, 손 내부 회전 및 서예와 같은 작업을 지원합니다.

### 실험 설정 및 주요 수치
- **사용자 연구**: 원격 조작 작업을 통해 Ruka-v2와 Ruka를 비교한 결과:
  - 작업 완료 시간 51.3% 감소
  - 성공률 21.2% 향상
- **적용 범위**: 13가지 정밀 작업의 단일 팔 및 양팔 원격 조작과 3가지 작업의 자율 정책 학습을 포함합니다.

### 결론
Ruka-v2는 손목 및 손가락 외전/내전 기능을 추가하여 정밀 조작 능력을 크게 향상시켰으며, 로봇 학습에서의 실용성을 입증했습니다. 모든 리소스는 오픈소스로 제공되어 재현 및 확장이 용이합니다.
