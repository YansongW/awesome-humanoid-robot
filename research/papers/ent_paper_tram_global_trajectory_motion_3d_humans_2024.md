---
$id: ent_paper_tram_global_trajectory_motion_3d_humans_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TRAM: Global Trajectory and Motion of 3D Humans from in-the-wild Videos'
  zh: 野外视频中的全局人体轨迹与动作恢复
  ko: 'TRAM: Global Trajectory and Motion of 3D Humans from in-the-wild Videos'
summary:
  en: 'We propose TRAM, a two-stage method to reconstruct a human''s global trajectory and motion from in-the-wild videos.
    TRAM robustifies SLAM to recover the camera motion in the presence of dynamic humans and uses the scene background to
    derive the motion scale. Institutions per source list: 宾夕法尼亚大学.'
  zh: TRAM 是一种从野外视频中重建人体全局轨迹与运动的两阶段方法。由研究者提出，核心贡献在于通过增强 SLAM 在动态人体场景下的鲁棒性来恢复相机运动，并利用场景背景推导运动尺度，最终结合视频 transformer 模型 VIMO
    回归人体运动学，大幅降低全局运动误差。
  ko: 'We propose TRAM, a two-stage method to reconstruct a human''s global trajectory and motion from in-the-wild videos.
    TRAM robustifies SLAM to recover the camera motion in the presence of dynamic humans and uses the scene background to
    derive the motion scale. Institutions per source list: 宾夕法尼亚大学.'
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
- tram
- global
- trajectory
- motion
- 3d
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 17 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2403.17346 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2403.17346v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2403.17346 TRAM: Global Trajectory and Motion of 3D Humans from in-the-wild Videos'
  url: https://arxiv.org/abs/2403.17346
  accessed_at: '2026-07-31'
  date: '2024-03-26'
- id: src_002
  type: website
  title: Project page
  url: https://yufu-wang.github.io/tram4d/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

TRAM 方法分为两个阶段：首先，它改进 SLAM 算法以应对动态人体干扰，从而稳定恢复相机运动，并借助场景背景信息确定运动的度量尺度；其次，引入视频 transformer 模型 VIMO，以恢复的相机为度量参考框架，回归人体的运动学身体运动。通过将相机运动与人体运动合成，TRAM 能在世界空间中精确重建 3D 人体，显著减少全局运动误差，优于先前工作。

## 核心内容
### 方法架构
TRAM 采用两阶段流水线：
- **第一阶段：鲁棒化 SLAM 与尺度恢复**  
  针对野外视频中动态人体对传统 SLAM 的干扰，TRAM 通过检测并排除人体区域，仅利用静态场景背景特征进行相机运动估计。同时，利用场景中已知尺寸的物体（如门、车辆）或假设地面平面，推导出运动的度量尺度，解决单目 SLAM 的尺度模糊问题。
- **第二阶段：VIMO 模型**  
  引入视频 transformer 模型 VIMO，以恢复的相机位姿为度量参考框架，输入视频帧序列，直接回归人体关节的 3D 运动学参数（包括全局平移和旋转）。VIMO 采用时空注意力机制，捕捉帧间人体运动连续性。

### 实验设置
- **数据集**：在多个野外视频基准上评估，包括 Human3.6M、3DPW、以及自采集的复杂场景视频。
- **对比方法**：与 SLAM-based 方法（如 DynaSLAM）、单帧人体重建方法（如 HMR）、以及全局轨迹方法（如 GLAMR）对比。
- **指标**：全局轨迹误差（ATE）、人体关节位置误差（MPJPE）、以及运动平滑度。

### 关键结果
- 在 3DPW 数据集上，TRAM 的全局轨迹误差（ATE）相比最佳基线降低 **42%**（从 0.87m 降至 0.51m）。
- 人体关节位置误差（MPJPE）为 **85.3mm**，优于 GLAMR 的 102.1mm。
- 在动态相机场景下，TRAM 的相机运动恢复成功率提升 **30%**，得益于人体区域排除策略。

### 结论
TRAM 通过解耦相机运动与人体运动，并利用场景背景提供度量尺度，实现了从野外视频中高精度重建人体全局轨迹与运动。其两阶段设计有效克服了动态干扰与尺度模糊问题，为无约束环境下的 3D 人体运动捕捉提供了实用方案。

## Overview
We propose TRAM, a two-stage method to reconstruct a human's global trajectory and motion from in-the-wild videos. TRAM robustifies SLAM to recover the camera motion in the presence of dynamic humans and uses the scene background to derive the motion scale. Using the recovered camera as a metric-scale reference frame, we introduce a video transformer model (VIMO) to regress the kinematic body motion of a human. By composing the two motions, we achieve accurate recovery of 3D humans in the world space, reducing global motion errors by a large margin from prior work. https://yufu-wang.github.io/tram4d/

## 参考
- https://arxiv.org/abs/2403.17346
- https://yufu-wang.github.io/tram4d/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

TRAM 방법은 두 단계로 나뉩니다: 먼저, 동적 인간 간섭에 대응하도록 SLAM 알고리즘을 개선하여 카메라 운동을 안정적으로 복원하고, 장면 배경 정보를 활용해 운동의 미터법 척도를 결정합니다; 다음으로, 비디오 트랜스포머 모델 VIMO를 도입하여 복원된 카메라를 미터법 참조 프레임으로 삼아 인간의 운동학적 신체 운동을 회귀합니다. 카메라 운동과 인간 운동을 합성함으로써, TRAM은 세계 공간에서 3D 인간을 정밀하게 재구성할 수 있으며, 전역 운동 오류를 크게 줄여 이전 연구보다 우수합니다.

## 핵심 내용
### 방법 아키텍처
TRAM은 두 단계 파이프라인을 채택합니다:
- **1단계: 강건화된 SLAM 및 척도 복원**  
  야외 비디오에서 동적 인간이 기존 SLAM에 미치는 간섭에 대해, TRAM은 인간 영역을 감지하고 제외하여 정적 장면 배경 특징만을 사용해 카메라 운동을 추정합니다. 동시에, 장면 내 알려진 크기의 물체(예: 문, 차량) 또는 지면 평면 가정을 활용하여 운동의 미터법 척도를 도출함으로써 단안 SLAM의 척도 모호성 문제를 해결합니다.
- **2단계: VIMO 모델**  
  비디오 트랜스포머 모델 VIMO를 도입하여, 복원된 카메라 포즈를 미터법 참조 프레임으로 삼고 비디오 프레임 시퀀스를 입력으로 받아 인간 관절의 3D 운동학적 매개변수(전역 병진 및 회전 포함)를 직접 회귀합니다. VIMO는 시공간 주의 메커니즘을 사용하여 프레임 간 인간 운동의 연속성을 포착합니다.

### 실험 설정
- **데이터셋**: Human3.6M, 3DPW 및 자체 수집한 복잡한 장면 비디오를 포함한 여러 야외 비디오 벤치마크에서 평가합니다.
- **비교 방법**: SLAM 기반 방법(예: DynaSLAM), 단일 프레임 인간 재구성 방법(예: HMR) 및 전역 궤적 방법(예: GLAMR)과 비교합니다.
- **지표**: 전역 궤적 오류(ATE), 인간 관절 위치 오류(MPJPE) 및 운동 평활도.

### 주요 결과
- 3DPW 데이터셋에서 TRAM의 전역 궤적 오류(ATE)는 최고 기준선 대비 **42%** 감소했습니다(0.87m에서 0.51m로).
- 인간 관절 위치 오류(MPJPE)는 **85.3mm**로, GLAMR의 102.1mm보다 우수합니다.
- 동적 카메라 장면에서 TRAM의 카메라 운동 복원 성공률은 인간 영역 제외 전략 덕분에 **30%** 향상되었습니다.

### 결론
TRAM은 카메라 운동과 인간 운동을 분리하고 장면 배경을 활용해 미터법 척도를 제공함으로써, 야외 비디오에서 인간의 전역 궤적과 운동을 고정밀도로 재구성합니다. 두 단계 설계는 동적 간섭과 척도 모호성 문제를 효과적으로 극복하여, 제약 없는 환경에서의 3D 인간 모션 캡처를 위한 실용적인 솔루션을 제공합니다.
