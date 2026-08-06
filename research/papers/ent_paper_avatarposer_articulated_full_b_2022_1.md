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
    ent_paper_avatarposer_articulated_full_b_2022_1 into this card (rules: same_arxiv). Backup+manifest: .staging/cleanup_wp12/.'
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

## 개요
오늘날의 혼합 현실 헤드 마운트 디스플레이는 증강 현실과 가상 현실 시나리오 모두에서 사용자의 머리 자세를 월드 공간에서 추적하고, 사용자의 손을 추적하여 상호작용을 지원합니다. 이는 사용자 입력을 지원하기에 충분하지만, 불행히도 사용자의 가상 표현을 상체로만 제한합니다. 따라서 현재 시스템은 떠다니는 아바타에 의존하게 되며, 이러한 한계는 협업 환경에서 특히 두드러집니다. 희소한 입력 소스로부터 전신 자세를 추정하기 위해, 이전 연구에서는 골반이나 하체에 추가 트래커와 센서를 통합했지만, 이는 설정 복잡성을 증가시키고 모바일 환경에서의 실용적 적용을 제한합니다. 본 논문에서는 사용자의 머리와 손의 모션 입력만을 사용하여 월드 좌표에서 전신 자세를 예측하는 최초의 학습 기반 방법인 AvatarPoser를 제시합니다. 우리의 방법은 Transformer 인코더를 기반으로 입력 신호에서 심층 특징을 추출하고, 학습된 로컬 관절 방향에서 전역 모션을 분리하여 자세 추정을 안내합니다. 모션 캡처 애니메이션과 유사한 정확한 전신 동작을 얻기 위해, 역운동학을 사용한 최적화 루틴을 통해 팔 관절 위치를 정제하여 원래 추적 입력과 일치시킵니다. 평가에서 AvatarPoser는 대규모 모션 캡처 데이터셋(AMASS)에서 최신 기술 수준의 결과를 달성했습니다. 동시에, 우리 방법의 추론 속도는 실시간 작동을 지원하여 메타버스 애플리케이션을 위한 전체적인 아바타 제어 및 표현을 지원하는 실용적인 인터페이스를 제공합니다.

## 핵심 내용
오늘날의 혼합 현실 헤드 마운트 디스플레이는 증강 현실과 가상 현실 시나리오 모두에서 사용자의 머리 자세를 월드 공간에서 추적하고, 사용자의 손을 추적하여 상호작용을 지원합니다. 이는 사용자 입력을 지원하기에 충분하지만, 불행히도 사용자의 가상 표현을 상체로만 제한합니다. 따라서 현재 시스템은 떠다니는 아바타에 의존하게 되며, 이러한 한계는 협업 환경에서 특히 두드러집니다. 희소한 입력 소스로부터 전신 자세를 추정하기 위해, 이전 연구에서는 골반이나 하체에 추가 트래커와 센서를 통합했지만, 이는 설정 복잡성을 증가시키고 모바일 환경에서의 실용적 적용을 제한합니다. 본 논문에서는 사용자의 머리와 손의 모션 입력만을 사용하여 월드 좌표에서 전신 자세를 예측하는 최초의 학습 기반 방법인 AvatarPoser를 제시합니다. 우리의 방법은 Transformer 인코더를 기반으로 입력 신호에서 심층 특징을 추출하고, 학습된 로컬 관절 방향에서 전역 모션을 분리하여 자세 추정을 안내합니다. 모션 캡처 애니메이션과 유사한 정확한 전신 동작을 얻기 위해, 역운동학을 사용한 최적화 루틴을 통해 팔 관절 위치를 정제하여 원래 추적 입력과 일치시킵니다. 평가에서 AvatarPoser는 대규모 모션 캡처 데이터셋(AMASS)에서 최신 기술 수준의 결과를 달성했습니다. 동시에, 우리 방법의 추론 속도는 실시간 작동을 지원하여 메타버스 애플리케이션을 위한 전체적인 아바타 제어 및 표현을 지원하는 실용적인 인터페이스를 제공합니다.

## 参考
- http://arxiv.org/abs/2207.13784v1
