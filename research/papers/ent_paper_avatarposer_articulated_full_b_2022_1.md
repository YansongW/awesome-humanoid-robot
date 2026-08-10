---
$id: ent_paper_avatarposer_articulated_full_b_2022_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
  zh: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
  ko: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing'
summary:
  en: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing is a 2022 work on human motion analysis
    and synthesis for humanoid robots, with open-source code available.'
  zh: AvatarPoser 是2022年提出的一种基于学习的全身姿态追踪方法，由研究团队开发，仅通过用户头部和手部的稀疏运动输入预测完整人体姿态。其核心贡献在于首次利用Transformer编码器从稀疏信号中解耦全局运动与局部关节方向，并结合逆运动学优化实现高精度实时追踪，在AMASS数据集上达到当时最优性能。
  ko: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing is a 2022 work on human motion analysis
    and synthesis for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- avatarposer
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2207.13784v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP1 dedup merge 2026-08-06: merged
    ent_paper_avatarposer_articulated_full_b_2022_1 into this card (rules: same_arxiv). Backup+manifest: .staging/cleanup_wp12/.
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (846 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing (arXiv)'
  url: https://arxiv.org/abs/2207.13784
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing project page'
  url: https://siplab.org/projects/AvatarPoser
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
现有混合现实头显仅追踪用户头部和手部姿态，导致虚拟化身只能呈现上半身，在协作场景中局限性明显。AvatarPoser通过Transformer编码器从头部和手部运动信号中提取深层特征，将全局运动与局部关节方向分离以指导姿态估计，再通过逆运动学优化手臂关节位置以匹配原始追踪输入。该方法在AMASS数据集上取得当时最优结果，且推理速度支持实时运行，为元宇宙应用中的全身化身控制提供了实用方案。

## 核心内容
### 方法架构
- **输入**：仅使用用户头部和双手的6D姿态（位置+旋转）作为稀疏运动信号。
- **核心模块**：基于Transformer编码器提取输入信号的深层特征，通过解耦全局运动（身体平移和旋转）与局部关节方向（各关节相对旋转）来构建姿态估计框架。
- **优化环节**：采用逆运动学（Inverse Kinematics）优化手臂关节位置，使输出姿态与原始追踪输入严格对齐，从而生成类似动作捕捉动画的精确全身运动。

### 实验设置
- **数据集**：在大型动作捕捉数据集AMASS上进行训练与评估，该数据集包含多种人体运动类型。
- **对比基准**：与使用额外传感器（如腰部或下肢追踪器）的现有方法进行对比。

### 关键结果
- **精度**：在AMASS数据集上达到当时最优（state-of-the-art）的全身姿态估计精度，具体指标包括关节位置误差和旋转误差。
- **实时性**：推理速度满足实时运行需求（未明确给出具体帧率，但强调支持实时交互）。
- **应用价值**：无需额外硬件（如腰部追踪器），仅依赖头显和手柄的现有追踪数据，显著降低部署复杂度，适用于移动端和Metaverse场景。

### 结论
AvatarPoser首次证明了仅通过头部和手部稀疏输入即可实现高精度实时全身姿态追踪，通过Transformer与逆运动学结合的设计，在精度和实用性上超越了依赖额外传感器的传统方法，为虚拟化身控制提供了轻量化解决方案。

## Overview
Today's Mixed Reality head-mounted displays track the user's head pose in world space as well as the user's hands for interaction in both Augmented Reality and Virtual Reality scenarios. While this is adequate to support user input, it unfortunately limits users' virtual representations to just their upper bodies. Current systems thus resort to floating avatars, whose limitation is particularly evident in collaborative settings. To estimate full-body poses from the sparse input sources, prior work has incorporated additional trackers and sensors at the pelvis or lower body, which increases setup complexity and limits practical application in mobile settings. In this paper, we present AvatarPoser, the first learning-based method that predicts full-body poses in world coordinates using only motion input from the user's head and hands. Our method builds on a Transformer encoder to extract deep features from the input signals and decouples global motion from the learned local joint orientations to guide pose estimation. To obtain accurate full-body motions that resemble motion capture animations, we refine the arm joints' positions using an optimization routine with inverse kinematics to match the original tracking input. In our evaluation, AvatarPoser achieved new state-of-the-art results in evaluations on large motion capture datasets (AMASS). At the same time, our method's inference speed supports real-time operation, providing a practical interface to support holistic avatar control and representation for Metaverse applications.

## 参考
- http://arxiv.org/abs/2207.13784v1

## 개요
기존 혼합현실 헤드셋은 사용자의 머리와 손姿态만 추적하여 가상 아바타가 상반신만 표현할 수밖에 없어 협업 환경에서 한계가 뚜렷하다. AvatarPoser는 Transformer 인코더를 통해 머리와 손의 운동 신호에서 심층 특징을 추출하고, 전역 운동과 국부 관절 방향을 분리하여 자세 추정을 유도한 후, 역운동학(Inverse Kinematics)을 통해 팔 관절 위치를 최적화하여 원래 추적 입력과 정합시킨다. 이 방법은 AMASS 데이터셋에서 당시 최고 성능을 달성했으며, 추론 속도가 실시간 실행을 지원하여 메타버스 응용에서 전신 아바타 제어를 위한 실용적인 솔루션을 제공한다.

## 핵심 내용
### 방법 구조
- **입력**: 사용자의 머리와 양손의 6D 자세(위치+회전)만 희소 운동 신호로 사용.
- **핵심 모듈**: Transformer 인코더 기반으로 입력 신호의 심층 특징을 추출하고, 전역 운동(신체 이동 및 회전)과 국부 관절 방향(각 관절의 상대 회전)을 분리하여 자세 추정 프레임워크를 구축.
- **최적화 단계**: 역운동학(Inverse Kinematics)을 사용하여 팔 관절 위치를 최적화함으로써 출력 자세가 원래 추적 입력과 엄격히 정렬되도록 하여, 모션 캡처 애니메이션과 유사한 정밀한 전신 운동을 생성.

### 실험 설정
- **데이터셋**: 대규모 모션 캡처 데이터셋 AMASS에서 훈련 및 평가를 수행하며, 해당 데이터셋은 다양한 인간 운동 유형을 포함.
- **비교 기준**: 추가 센서(예: 허리 또는 하체 추적기)를 사용하는 기존 방법과 비교.

### 주요 결과
- **정밀도**: AMASS 데이터셋에서 당시 최고 수준(state-of-the-art)의 전신 자세 추정 정밀도를 달성했으며, 구체적 지표로 관절 위치 오류 및 회전 오류를 포함.
- **실시간성**: 추론 속도가 실시간 실행 요구를 충족(구체적 프레임률은 명시되지 않았지만 실시간 상호작용 지원을 강조).
- **응용 가치**: 추가 하드웨어(예: 허리 추적기) 없이 헤드셋과 컨트롤러의 기존 추적 데이터만으로 배포 복잡성을 크게 낮추며, 모바일 및 메타버스 환경에 적합.

### 결론
AvatarPoser는 머리와 손의 희소 입력만으로도 고정밀 실시간 전신 자세 추적이 가능함을 처음으로 입증했다. Transformer와 역운동학의 결합 설계를 통해 추가 센서에 의존하는 기존 방법보다 정밀도와 실용성에서 우수하며, 가상 아바타 제어를 위한 경량화 솔루션을 제공한다.
