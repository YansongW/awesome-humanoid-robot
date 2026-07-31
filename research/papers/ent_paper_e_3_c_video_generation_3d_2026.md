---
$id: ent_paper_e_3_c_video_generation_3d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control'
  zh: 'E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control'
  ko: 'E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control'
summary:
  en: 'Controllable and physically grounded egocentric video generation is essential for embodied agents to reason about how
    their own and others'' actions manifest and change the world. Institutions per source list: Meta Reality Labs、University
    of Toronto.'
  zh: E$^3$C 是一个可控的自我中心视频生成框架，由研究团队提出，用于具身智能体推理自身及他人动作如何改变世界。其核心贡献在于构建了基于半稠密点云的 3D 环境记忆，并分离了场景结构与人类动态控制，同时支持自我中心（ego）和外部（exo）人体姿态控制。在
    Nymeria 数据集上的实验表明，E$^3$C 在视觉保真度、相机运动准确性、物体一致性及人体控制方面均优于强基线方法。
  ko: 'Controllable and physically grounded egocentric video generation is essential for embodied agents to reason about how
    their own and others'' actions manifest and change the world. Institutions per source list: Meta Reality Labs、University
    of Toronto.'
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
- e
- '3'
- c
- video
- generation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 281 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2605.26316 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.26316v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.26316 E$^3$C: Video Generation with 3D Environmental Memory and Ego-Exo Human Pose Control'
  url: https://arxiv.org/abs/2605.26316
  accessed_at: '2026-07-31'
  date: '2026-05-25'
- id: src_002
  type: website
  title: Project page
  url: https://e3c-videogen.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 机器人下一代数据入口，可能就是Ego：9篇论文讲透第一视角技术路线
  url: https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA
  accessed_at: '2026-07-31'
---

## 概述

E$^3$C 通过构建结构化且紧凑的条件，将持久的场景结构与人类驱动的动态分离开来。它从上下文帧中构建基于半稠密点云的 3D 环境记忆，并为每个点附加来自 video-VAE 特征的外观描述符，渲染到目标视角后生成与目标帧对齐的条件。人类动态被单独建模：场景中观察到的人由骨架渲染（外部人体控制）控制，而相机佩戴者则由其 3D 身体关节和 6DoF 手腕运动（自我中心人体控制）指定。为解决佩戴者身体部位不可见时自我中心控制的保持问题，E$^3$C 引入了自我运动编码器，生成持久的交叉注意力标记。

## 核心内容
### 方法
E$^3$C 是一个可控的视频扩散框架，其核心在于构建结构化且紧凑的条件，以分离持久的场景结构与人类驱动的动态。

- **3D 环境记忆**：从上下文帧中构建一个半稠密点云，并为每个点附加来自 video-VAE 特征的外观描述符。将此记忆渲染到目标视角，产生与目标帧对齐的条件。
- **人体动态建模**：场景中观察到的人由骨架渲染（外部人体控制）控制；相机佩戴者由 3D 身体关节和 6DoF 手腕运动（自我中心人体控制）指定。
- **自我运动编码器**：当佩戴者身体部位不可见时，该编码器生成持久的交叉注意力标记，以保持自我中心人体控制。

### 实验设置
- **数据集**：在 Nymeria 数据集上进行评估。
- **基线**：与强基线方法进行比较，包括视觉保真度、相机运动准确性、物体一致性以及自我中心和外部人体控制。

### 关键结果
- E$^3$C 在视觉保真度、相机运动准确性、物体一致性以及自我中心和外部人体控制方面均优于强基线方法。
- 该框架还支持直观的场景编辑功能。

### 结论
E$^3$C 通过分离场景结构与人类动态，并引入自我运动编码器，有效解决了自我中心视频生成中的挑战，如快速视角变化和频繁自遮挡。实验验证了其在多个指标上的优越性，并展示了场景编辑的潜力。

## Overview
Controllable and physically grounded egocentric video generation is essential for embodied agents to reason about how their own and others' actions manifest and change the world. Compared to generic video synthesis, egocentric generation is especially challenging: the camera is tightly coupled to the actor, leading to rapid viewpoint changes and frequent self-occlusions; the underlying actions are subtle, articulated, and often only partially visible; and both the people and the scene state must evolve consistently with the specified controls. We present E$^3$C, a controllable video diffusion framework for egocentric generation that builds structured and compact conditions disentangling persistent scene structure from human-driven dynamics. From context frames, E$^3$C constructs a semi-dense point cloud-based 3D memory and augments each point with appearance descriptors from video-VAE features. Rendering this memory into target viewpoints produces conditioning aligned with the target frames. Human dynamics are modeled separately. The observed people in the scene are controlled by skeleton renderings (exo human control), while the camera wearer is specified by their 3D body joints and 6DoF wrist motion (ego human control). To preserve ego human control when the wearer's body parts are invisible, we introduce an ego motion encoder that produces persistent cross-attention tokens. Experiments on Nymeria show that E$^3$C improves visual fidelity, camera-motion accuracy, object consistency, and ego & exo human control over strong baselines, while also enabling intuitive scene editing.

## 参考
- https://arxiv.org/abs/2605.26316
- https://e3c-videogen.github.io/
- https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA

## 개요

E$^3$C는 구조화되고 간결한 조건을 구축하여 지속적인 장면 구조와 인간 주도 동적 요소를 분리합니다. 컨텍스트 프레임에서 반밀집 점군 기반의 3D 환경 메모리를 구성하고, 각 점에 video-VAE 특징에서 추출한 외관 설명자를 첨부한 후, 목표 시점으로 렌더링하여 목표 프레임과 정렬된 조건을 생성합니다. 인간 동적 요소는 별도로 모델링됩니다. 장면에서 관찰된 사람은 골격 렌더링(외부 인간 제어)으로 제어되며, 카메라 착용자는 3D 신체 관절과 6DoF 손목 움직임(자기중심 인간 제어)으로 지정됩니다. 착용자의 신체 부위가 보이지 않을 때 자기중심 제어를 유지하는 문제를 해결하기 위해, E$^3$C는 자기 운동 인코더를 도입하여 지속적인 교차 주의 토큰을 생성합니다.

## 핵심 내용
### 방법
E$^3$C는 제어 가능한 비디오 확산 프레임워크로, 구조화되고 간결한 조건을 구축하여 지속적인 장면 구조와 인간 주도 동적 요소를 분리하는 데 중점을 둡니다.

- **3D 환경 메모리**: 컨텍스트 프레임에서 반밀집 점군을 구성하고, 각 점에 video-VAE 특징에서 추출한 외관 설명자를 첨부합니다. 이 메모리를 목표 시점으로 렌더링하여 목표 프레임과 정렬된 조건을 생성합니다.
- **인간 동적 모델링**: 장면에서 관찰된 사람은 골격 렌더링(외부 인간 제어)으로 제어되며, 카메라 착용자는 3D 신체 관절과 6DoF 손목 움직임(자기중심 인간 제어)으로 지정됩니다.
- **자기 운동 인코더**: 착용자의 신체 부위가 보이지 않을 때, 이 인코더는 지속적인 교차 주의 토큰을 생성하여 자기중심 인간 제어를 유지합니다.

### 실험 설정
- **데이터셋**: Nymeria 데이터셋에서 평가를 수행합니다.
- **기준선**: 시각적 충실도, 카메라 움직임 정확성, 객체 일관성, 자기중심 및 외부 인간 제어를 포함한 강력한 기준선 방법과 비교합니다.

### 주요 결과
- E$^3$C는 시각적 충실도, 카메라 움직임 정확성, 객체 일관성, 자기중심 및 외부 인간 제어에서 강력한 기준선 방법보다 우수합니다.
- 이 프레임워크는 직관적인 장면 편집 기능도 지원합니다.

### 결론
E$^3$C는 장면 구조와 인간 동적 요소를 분리하고 자기 운동 인코더를 도입함으로써, 빠른 시점 변화와 빈번한 자체 폐색과 같은 자기중심 비디오 생성의 도전 과제를 효과적으로 해결합니다. 실험을 통해 여러 지표에서 우수성을 입증하고 장면 편집의 잠재력을 보여줍니다.
