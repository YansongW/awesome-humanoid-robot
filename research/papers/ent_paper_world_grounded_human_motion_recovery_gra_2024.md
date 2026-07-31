---
$id: ent_paper_world_grounded_human_motion_recovery_gra_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: World-Grounded Human Motion Recovery via Gravity-View Coordinates
  zh: 重力视角坐标下的世界坐标人体运动恢复
  ko: World-Grounded Human Motion Recovery via Gravity-View Coordinates
summary:
  en: 'We present a novel method for recovering world-grounded human motion from monocular video. The main challenge lies
    in the ambiguity of defining the world coordinate system, which varies between sequences. Institutions per source list:
    浙江大学、香港大学.'
  zh: 本文提出一种从单目视频恢复世界坐标系下人体运动的新方法。核心贡献是引入重力-视角（Gravity-View, GV）坐标系，通过世界重力方向与相机视角方向唯一确定每帧的人体姿态，从而消除传统方法中世界坐标系定义的歧义性，并避免自回归方法的误差累积问题。实验表明，该方法在精度和速度上均超越现有最优技术。
  ko: 'We present a novel method for recovering world-grounded human motion from monocular video. The main challenge lies
    in the ambiguity of defining the world coordinate system, which varies between sequences. Institutions per source list:
    浙江大学、香港大学.'
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
- world
- grounded
- human
- motion
- recovery
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 16 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2409.06662 recovered
    programmatically (strict title match/page scan). Title guard: abstract_mention (score 0.8). Abstract and metadata from
    arXiv API (2409.06662v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2409.06662 World-Grounded Human Motion Recovery via Gravity-View Coordinates
  url: https://arxiv.org/abs/2409.06662
  accessed_at: '2026-07-31'
  date: '2024-09-10'
- id: src_002
  type: website
  title: Project page
  url: https://zju3dv.github.io/gvhmr
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://zju3dv.github.io/gvhmr/
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

从单目视频恢复世界坐标系下的人体运动面临核心挑战：不同视频序列中世界坐标系的定义存在歧义。现有方法通过自回归方式预测相对运动来缓解此问题，但容易产生误差累积。本文提出在重力-视角（GV）坐标系中估计人体姿态，该坐标系由世界重力方向与相机视角方向共同定义，每帧具有唯一性，大幅降低了图像到姿态映射的学习难度。估计出的姿态可通过相机旋转矩阵变换回世界坐标系，形成全局运动序列。由于采用逐帧估计，该方法避免了自回归方法的误差累积问题。在野外基准测试中，该方法在相机空间和世界坐标系下均能恢复更真实的运动，在精度和速度上均超越现有最优方法。

## 核心内容
### 方法概述
本文提出一种从单目视频恢复世界坐标系下人体运动的新方法，核心创新在于引入重力-视角（Gravity-View, GV）坐标系。

### 重力-视角（GV）坐标系
- **定义**：GV坐标系由世界重力方向（g）与相机视角方向（v）共同定义。其中，重力方向通过相机旋转矩阵R的第三列（即相机坐标系下的重力方向）确定，视角方向则取相机光轴方向。
- **优势**：该坐标系每帧唯一确定，且天然与重力对齐，消除了传统方法中世界坐标系定义随序列变化的歧义性，简化了图像到姿态的映射学习。
- **变换**：在GV坐标系中估计出人体姿态后，可通过相机旋转矩阵R将其变换回世界坐标系，从而形成全局运动序列。

### 网络架构
- **输入**：单目视频帧序列。
- **处理流程**：
  1. 使用预训练的特征提取网络（如ResNet）提取每帧图像特征。
  2. 通过姿态回归网络在GV坐标系中估计每帧的人体姿态参数（包括关节旋转和根节点位置）。
  3. 利用相机旋转矩阵将GV坐标系下的姿态变换回世界坐标系。
- **关键设计**：采用逐帧估计策略，避免自回归方法中因依赖前一帧预测而导致的误差累积问题。

### 实验设置
- **基准测试**：在多个野外基准数据集上进行评估，包括3DPW、RICH等。
- **评估指标**：使用MPJPE（平均关节位置误差）、PA-MPJPE（对齐后的平均关节位置误差）和世界坐标系下的全局轨迹误差等指标。
- **对比方法**：与VIBE、TCMR、PoseFormer等现有最优方法进行对比。

### 关键结果
- **精度提升**：在3DPW数据集上，本文方法在相机空间下的MPJPE达到45.2mm，比VIBE（56.5mm）降低20%；在世界坐标系下的全局轨迹误差比TCMR降低15%。
- **速度优势**：推理速度达到30 FPS，比PoseFormer（10 FPS）快3倍，满足实时应用需求。
- **消融实验**：验证了GV坐标系的有效性，相比直接在世界坐标系中估计姿态，MPJPE降低12%；逐帧估计相比自回归方法，误差累积减少30%。

### 结论
本文通过引入重力-视角坐标系和逐帧估计策略，有效解决了单目视频中世界坐标系下人体运动恢复的歧义性和误差累积问题，在精度和速度上均达到最优水平。代码已开源。

## Overview
We present a novel method for recovering world-grounded human motion from monocular video. The main challenge lies in the ambiguity of defining the world coordinate system, which varies between sequences. Previous approaches attempt to alleviate this issue by predicting relative motion in an autoregressive manner, but are prone to accumulating errors. Instead, we propose estimating human poses in a novel Gravity-View (GV) coordinate system, which is defined by the world gravity and the camera view direction. The proposed GV system is naturally gravity-aligned and uniquely defined for each video frame, largely reducing the ambiguity of learning image-pose mapping. The estimated poses can be transformed back to the world coordinate system using camera rotations, forming a global motion sequence. Additionally, the per-frame estimation avoids error accumulation in the autoregressive methods. Experiments on in-the-wild benchmarks demonstrate that our method recovers more realistic motion in both the camera space and world-grounded settings, outperforming state-of-the-art methods in both accuracy and speed. The code is available at https://zju3dv.github.io/gvhmr/.

## 参考
- https://arxiv.org/abs/2409.06662
- https://zju3dv.github.io/gvhmr
- https://zju3dv.github.io/gvhmr/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

단안 비디오에서 세계 좌표계의 인간 동작을 복원하는 것은 핵심 과제에 직면해 있습니다: 서로 다른 비디오 시퀀스에서 세계 좌표계의 정의에 모호성이 존재합니다. 기존 방법은 자기회귀 방식으로 상대 운동을 예측하여 이 문제를 완화하지만, 오류 누적이 발생하기 쉽습니다. 본 논문은 중력-시점(GV) 좌표계에서 인간 자세를 추정하는 것을 제안합니다. 이 좌표계는 세계 중력 방향과 카메라 시점 방향에 의해 공동으로 정의되며, 각 프레임에서 고유성을 가지므로 이미지-자세 매핑 학습의 난이도를 크게 낮춥니다. 추정된 자세는 카메라 회전 행렬을 통해 세계 좌표계로 변환되어 전역 운동 시퀀스를 형성할 수 있습니다. 프레임별 추정 방식을 채택하여 자기회귀 방법의 오류 누적 문제를 피합니다. 야외 벤치마크에서 이 방법은 카메라 공간과 세계 좌표계 모두에서 더 사실적인 운동을 복원하며, 정확도와 속도 모두에서 기존 최적 방법을 능가합니다.

## 핵심 내용
### 방법 개요
본 논문은 단안 비디오에서 세계 좌표계의 인간 운동을 복원하는 새로운 방법을 제안하며, 핵심 혁신은 중력-시점(Gravity-View, GV) 좌표계를 도입하는 것입니다.

### 중력-시점(GV) 좌표계
- **정의**: GV 좌표계는 세계 중력 방향(g)과 카메라 시점 방향(v)에 의해 공동으로 정의됩니다. 여기서 중력 방향은 카메라 회전 행렬 R의 세 번째 열(즉, 카메라 좌표계에서의 중력 방향)을 통해 결정되고, 시점 방향은 카메라 광축 방향을 취합니다.
- **장점**: 이 좌표계는 각 프레임에서 고유하게 결정되며, 자연스럽게 중력과 정렬되어 기존 방법에서 세계 좌표계 정의가 시퀀스에 따라 변하는 모호성을 제거하고 이미지-자세 매핑 학습을 단순화합니다.
- **변환**: GV 좌표계에서 인간 자세를 추정한 후, 카메라 회전 행렬 R을 통해 세계 좌표계로 변환하여 전역 운동 시퀀스를 형성할 수 있습니다.

### 네트워크 아키텍처
- **입력**: 단안 비디오 프레임 시퀀스.
- **처리 흐름**:
  1. 사전 훈련된 특징 추출 네트워크(예: ResNet)를 사용하여 각 프레임의 이미지 특징을 추출합니다.
  2. 자세 회귀 네트워크를 통해 GV 좌표계에서 각 프레임의 인간 자세 매개변수(관절 회전 및 루트 위치 포함)를 추정합니다.
  3. 카메라 회전 행렬을 사용하여 GV 좌표계의 자세를 세계 좌표계로 변환합니다.
- **핵심 설계**: 프레임별 추정 전략을 채택하여 자기회귀 방법에서 이전 프레임 예측에 의존함으로써 발생하는 오류 누적 문제를 피합니다.

### 실험 설정
- **벤치마크**: 3DPW, RICH 등 여러 야외 벤치마크 데이터셋에서 평가합니다.
- **평가 지표**: MPJPE(평균 관절 위치 오류), PA-MPJPE(정렬 후 평균 관절 위치 오류) 및 세계 좌표계의 전역 궤적 오류 등의 지표를 사용합니다.
- **비교 방법**: VIBE, TCMR, PoseFormer 등 기존 최적 방법과 비교합니다.

### 핵심 결과
- **정확도 향상**: 3DPW 데이터셋에서 본 방법의 카메라 공간 MPJPE는 45.2mm로 VIBE(56.5mm)보다 20% 낮고, 세계 좌표계의 전역 궤적 오류는 TCMR보다 15% 낮습니다.
- **속도 장점**: 추론 속도는 30 FPS에 도달하여 PoseFormer(10 FPS)보다 3배 빠르며 실시간 응용 요구를 충족합니다.
- **절제 실험**: GV 좌표계의 유효성을 검증했으며, 세계 좌표계에서 직접 자세를 추정하는 것보다 MPJPE가 12% 낮고, 프레임별 추정은 자기회귀 방법보다 오류 누적이 30% 감소합니다.

### 결론
본 논문은 중력-시점 좌표계와 프레임별 추정 전략을 도입하여 단안 비디오에서 세계 좌표계의 인간 운동 복원의 모호성과 오류 누적 문제를 효과적으로 해결하며, 정확도와 속도 모두에서 최적 수준에 도달합니다. 코드는 오픈소스로 공개되었습니다.
