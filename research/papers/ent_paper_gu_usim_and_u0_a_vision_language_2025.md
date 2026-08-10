---
$id: ent_paper_gu_usim_and_u0_a_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots'
  zh: USIM & U0
  ko: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots'
summary:
  en: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (USIM & U0), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences,
    Key Laboratory of Cognition and Decision Intelligence for Complex Systems.'
  zh: 中国科学院自动化研究所与复杂系统认知与决策重点实验室于2025年提出USIM & U0，这是一个面向通用水下机器人的视觉-语言-动作（VLA）数据集与模型。核心贡献包括：构建了包含90.5万帧、2275条轨迹的仿真数据集USIM，以及提出具备卷积-注意力感知模块的U0模型，在导航与三维移动操作任务上实现SOTA性能，在线成功率较基线提升5.5%。
  ko: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (USIM & U0), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences,
    Key Laboratory of Cognition and Decision Intelligence for Complex Systems.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- usim_u0
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07869v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (822 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (arXiv)'
  url: https://arxiv.org/abs/2510.07869
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: USIM & U0 source
  url: https://doi.org/10.48550/arXiv.2510.07869
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对水下机器人多任务通用智能研究匮乏的现状，该工作提出了统一框架，通过语言指令驱动感知与动作的整合。研究团队首先开发数据合成流水线，基于BlueROV2平台构建了约25小时交互数据的USIM仿真数据集。在此基础上提出的U0模型采用卷积-注意力感知（CAP）模块，将目标位姿估计作为辅助任务以增强空间感知能力。实验建立了包含离线指标与在线任务执行的系统评估框架，结果显示USIM数据集能有效提升现有VLA模型的水下适应能力，而U0模型在导航任务中达到87.5%的成功率。

## 核心内容
### 方法架构
- **数据合成流水线**：基于BlueROV2水下机器人平台，通过仿真环境生成多任务交互数据，包含避障导航与三维移动操作等场景
- **U0模型设计**：
  - 采用卷积-注意力感知（CAP）模块，融合CNN与Transformer架构
  - 引入目标位姿估计作为辅助学习任务，显式增强模型的空间位置感知能力
  - 输入为视觉观测与语言指令，输出为连续动作指令

### 实验设置
- **数据集规模**：USIM包含905,000+帧图像，覆盖2275条不同轨迹，总时长约25小时
- **评估体系**：
  - 离线评估：计算动作预测均方误差（MSE）
  - 在线评估：在仿真环境中执行完整任务链，统计成功率
- **基线对比**：与现有VLA模型（成功率低于37.6%）进行公平比较

### 关键结果
- **离线性能**：U0模型将平均动作预测误差降至0.0359
- **在线成功率**：
  - 综合任务成功率43.1%，较最佳基线（37.6%）提升5.5%
  - 导航子任务成功率高达87.5%
- **数据集有效性**：USIM预训练使现有VLA模型在水下场景的适应能力显著提升

### 结论
该工作验证了通用智能在水下机器人领域的可行性，为大规模数据集合成与水下具身智能体研究提供了基础框架。

## Overview
Underwater environments pose unique challenges for robotic navigation and manipulation. While existing research has primarily focused on task-specific methods, studies on general-purpose intelligence for multi-task execution remain scarce. To address this gap, we propose a unified framework for general-purpose underwater robots that integrates perception and action driven by language instructions. First, we develop a data synthesis pipeline to construct USIM, a simulation-based dataset which comprises over 905K frames from 2275 trajectories, totaling approximately 25 hours of BlueROV2 interactions. Furthermore, we propose U0, a vision-language-action (VLA) model capable of executing various tasks from obstacle-avoidance navigation to three-dimensional mobile manipulation. The model features a convolution-attention-based perception (CAP) module, which incorporates target pose estimation as an auxiliary task to explicitly bolster the model's spatial awareness. For evaluation, we establish a systematic assessment framework and an automated pipeline encompassing both offline metrics and online task execution. Experimental results demonstrate that the USIM dataset significantly empowers existing VLA models to adapt to underwater scenarios. Notably, our U0 model achieves state-of-the-art performance: it reduces the offline mean action prediction error to 0.0359 and achieves an overall online success rate of 43.1%, marking a 5.5% improvement over existing competitive baselines (below 37.6%), with navigation tasks reaching as high as 87.5%. These results validate the feasibility of general-purpose intelligence in underwater robotics, providing a foundation for scalable dataset synthesis and aquatic embodied agents.

## 参考
- http://arxiv.org/abs/2510.07869v4

## 개요
수중 로봇의 다중 작업 범용 지능 연구가 부족한 현황에 대응하여, 본 연구는 언어 명령을 통해 인식과 행동의 통합을 구동하는 통합 프레임워크를 제안한다. 연구팀은 먼저 데이터 합성 파이프라인을 개발하여 BlueROV2 플랫폼 기반으로 약 25시간의 상호작용 데이터를 포함하는 USIM 시뮬레이션 데이터셋을 구축했다. 이를 바탕으로 제안된 U0 모델은 컨볼루션-어텐션 인식(CAP) 모듈을 채택하고, 목표 자세 추정을 보조 작업으로 활용하여 공간 인식 능력을 강화한다. 실험은 오프라인 지표와 온라인 작업 실행을 포함한 체계적 평가 프레임워크를 구축했으며, USIM 데이터셋이 기존 VLA 모델의 수중 적응 능력을 효과적으로 향상시키고, U0 모델은 내비게이션 작업에서 87.5%의 성공률을 달성함을 보여주었다.

## 핵심 내용
### 방법 아키텍처
- **데이터 합성 파이프라인**: BlueROV2 수중 로봇 플랫폼 기반으로 시뮬레이션 환경에서 다중 작업 상호작용 데이터를 생성하며, 장애물 회피 내비게이션 및 3차원 이동 조작 등의 시나리오를 포함
- **U0 모델 설계**:
  - 컨볼루션-어텐션 인식(CAP) 모듈을 채택하여 CNN과 Transformer 아키텍처를 융합
  - 목표 자세 추정을 보조 학습 작업으로 도입하여 모델의 공간 위치 인식 능력을 명시적으로 강화
  - 입력은 시각 관측과 언어 명령, 출력은 연속 동작 명령

### 실험 설정
- **데이터셋 규모**: USIM은 905,000+ 프레임의 이미지를 포함하며, 2,275개의 서로 다른 궤적을 커버하고 총 길이는 약 25시간
- **평가 체계**:
  - 오프라인 평가: 동작 예측 평균 제곱 오차(MSE) 계산
  - 온라인 평가: 시뮬레이션 환경에서 전체 작업 체인을 실행하여 성공률 통계
- **기준선 비교**: 기존 VLA 모델(성공률 37.6% 미만)과 공정한 비교 수행

### 핵심 결과
- **오프라인 성능**: U0 모델은 평균 동작 예측 오차를 0.0359로 감소
- **온라인 성공률**:
  - 종합 작업 성공률 43.1%로 최고 기준선(37.6%) 대비 5.5% 향상
  - 내비게이션 하위 작업 성공률은 87.5%에 달함
- **데이터셋 유효성**: USIM 사전 학습을 통해 기존 VLA 모델의 수중 시나리오 적응 능력이 크게 향상

### 결론
본 연구는 수중 로봇 분야에서 범용 지능의 실현 가능성을 검증했으며, 대규모 데이터셋 합성 및 수중 임베디드 에이전트 연구를 위한 기반 프레임워크를 제공한다.
