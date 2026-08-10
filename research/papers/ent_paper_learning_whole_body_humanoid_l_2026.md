---
$id: ent_paper_learning_whole_body_humanoid_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking
  zh: 复杂地形里，参考动作要在线生成
  ko: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking
summary:
  en: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking is a knowledge node related to paper
    in the humanoid robot value chain.
  zh: 本文提出一种结合运动生成与运动跟踪的全身人形机器人运动框架，由研究团队基于Unitree G1机器人实现。核心贡献在于通过扩散模型实时生成地形感知的参考运动，并利用强化学习训练全身跟踪器，最终通过闭环微调提升鲁棒性，成功实现多种复杂地形的穿越。
  ko: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking is a knowledge node related to paper
    in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- task_interface
- visual_closed_loop
- vla
- whole_body_control
- world_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.17335v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (590 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking (arXiv)
  url: https://arxiv.org/abs/2604.17335
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 复杂地形里，参考动作要在线生成 project page
  url: https://wholebodylocomotion.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
针对人形机器人全身运动控制中高维控制、形态不稳定及实时地形适应等挑战，本文提出一种融合运动生成与运动跟踪的框架。首先，基于重定向的人类运动数据训练扩散模型，用于实时预测地形感知的参考运动；同时，利用强化学习训练全身参考跟踪器。为应对生成参考不完美的情况，进一步在闭环设置中微调跟踪器。该系统支持基于方向的目标到达控制，并成功部署于Unitree G1机器人，在箱子、障碍物、楼梯及混合地形上完成实验验证。

## 核心内容
### 方法架构
- **运动生成**：使用扩散模型（diffusion model）对重定向的人类运动数据进行训练，实现实时预测地形感知的参考运动。
- **运动跟踪**：通过强化学习（RL）训练全身参考跟踪器，利用生成的运动数据学习协调的全身技能。
- **闭环微调**：在冻结运动生成器的闭环设置中进一步微调跟踪器，以提升对不完美生成参考的鲁棒性。

### 实验设置
- **硬件平台**：Unitree G1人形机器人，配备机载感知与计算模块。
- **地形测试**：包括箱子（boxes）、障碍物（hurdles）、楼梯（stairs）及混合地形组合。

### 关键结果
- **硬件实验**：成功穿越所有测试地形，验证了系统的实际部署能力。
- **定量分析**：结果表明，结合在线运动生成与跟踪器微调显著提升了泛化性与鲁棒性。

## Overview
Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions. Concurrently, we train a whole-body reference tracker with RL using this motion data. To improve robustness under imperfectly generated references, we further fine-tune the tracker with a frozen motion generator in a closed-loop setting. The resulting system supports directional goal-reaching control with terrain-aware whole-body adaptation, and can be deployed on a Unitree G1 humanoid robot with onboard perception and computation. The hardware experiments demonstrate successful traversal over boxes, hurdles, stairs, and mixed terrain combinations. Quantitative results further show the benefits of incorporating online motion generation and fine-tuning the motion tracker for improved generalization and robustness.

## 参考
- http://arxiv.org/abs/2604.17335v2

## 개요
인간형 로봇의 전신 운동 제어에서 발생하는 고차원 제어, 형태 불안정성 및 실시간 지형 적응과 같은 과제를 해결하기 위해, 본 논문은 운동 생성과 운동 추적을 융합한 프레임워크를 제안한다. 먼저, 리타게팅된 인간 운동 데이터를 기반으로 확산 모델을 훈련하여 지형 인식 참조 운동을 실시간으로 예측한다. 동시에 강화 학습을 사용하여 전신 참조 추적기를 훈련한다. 생성된 참조가 불완전한 경우를 대비하여, 폐루프 설정에서 추적기를 추가로 미세 조정한다. 이 시스템은 방향 기반 목표 도달 제어를 지원하며, Unitree G1 로봇에 성공적으로 배포되어 상자, 장애물, 계단 및 혼합 지형에서 실험 검증을 완료했다.

## 핵심 내용
### 방법 아키텍처
- **운동 생성**: 확산 모델(diffusion model)을 사용하여 리타게팅된 인간 운동 데이터를 훈련하고, 지형 인식 참조 운동을 실시간으로 예측한다.
- **운동 추적**: 강화 학습(RL)을 통해 전신 참조 추적기를 훈련하며, 생성된 운동 데이터를 활용하여 조화로운 전신 기술을 학습한다.
- **폐루프 미세 조정**: 운동 생성기를 고정한 폐루프 설정에서 추적기를 추가로 미세 조정하여, 불완전한 생성 참조에 대한 강건성을 향상시킨다.

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 인간형 로봇으로, 온보드 인식 및 계산 모듈을 갖추고 있다.
- **지형 테스트**: 상자(boxes), 장애물(hurdles), 계단(stairs) 및 혼합 지형 조합을 포함한다.

### 주요 결과
- **하드웨어 실험**: 모든 테스트 지형을 성공적으로 통과하여 시스템의 실제 배포 능력을 검증했다.
- **정량 분석**: 결과는 온라인 운동 생성과 추적기 미세 조정의 결합이 일반화 성능과 강건성을 크게 향상시킴을 보여준다.
