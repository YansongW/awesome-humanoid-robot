---
$id: ent_paper_sds_see_it_do_it_sorted_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SDS -- See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration'
  zh: 'SDS -- See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration'
  ko: 'SDS -- See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration'
summary:
  en: 'Imagine a robot learning locomotion skills from any single video, without labels or reward engineering. We introduce
    SDS ("See it. Institutions per source list: Robot Perception Lab、UCL（Maria Stamatopoulou、Jeffrey Li、Dimitrios Kanoulas）.'
  zh: SDS（"See it. Do it. Sorted."）是由UCL团队提出的四足机器人技能合成自动化流水线，能从单段无标签视频中学习运动技能。其核心创新在于利用GPT-4o结合时空网格视觉编码（$G_{v}$）与结构化输入分解（SUS）生成可执行奖励函数，并通过闭环进化优化PPO策略，在Unitree
    Go1和ANYmal上实现四种步态100%匹配精度与零失败率。
  ko: 'Imagine a robot learning locomotion skills from any single video, without labels or reward engineering. We introduce
    SDS ("See it. Institutions per source list: Robot Perception Lab、UCL（Maria Stamatopoulou、Jeffrey Li、Dimitrios Kanoulas）.'
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
- sds
- see
- it
- do
- it
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 764 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2410.11571v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2410.11571 SDS -- See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration'
  url: https://arxiv.org/abs/2410.11571
  accessed_at: '2026-07-31'
  date: '2024-10-15'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

SDS通过GPT-4o的视觉理解能力，将单段非结构化演示视频转化为机器人可执行的奖励函数。该方法采用时空网格视觉编码（$G_{v}$）对视频帧进行结构化分解，再通过结构化输入分解（SUS）生成奖励函数，随后利用PPO算法训练策略，并通过闭环进化机制（以训练录像和性能指标为自监督信号）持续优化奖励函数。实验表明，SDS在Unitree Go1上成功学习trot、bound、pace、hop四种步态，实现100%步态匹配精度、DTW距离低至$10^{-6}$量级，且仿真与真实环境中均无失败案例。该方法还能泛化至形态不同的ANYmal机器人，在数据效率、训练时间和工程投入上均优于先前工作。

## 核心内容
### 方法架构
SDS流水线包含三个核心阶段：
1. **视觉编码与分解**：使用GPT-4o对输入视频进行时空网格视觉编码（$G_{v}$），将连续帧分解为结构化时空单元；再通过结构化输入分解（SUS）提取关键运动特征。
2. **奖励函数生成**：基于SUS输出，GPT-4o自动生成可执行的奖励函数（RF），无需人工设计或标签。
3. **策略优化**：使用PPO算法训练策略，并通过闭环进化机制迭代优化RF——利用训练过程中的录像和性能指标（如步态匹配度、稳定性）作为自监督信号，自动调整RF参数。

### 实验设置
- **机器人平台**：Unitree Go1（四足）和ANYmal（不同形态四足）
- **学习目标**：四种步态——trot（小跑）、bound（跳跃）、pace（踱步）、hop（单足跳）
- **训练环境**：仿真环境（Isaac Gym）与真实世界部署
- **对比基线**：与先前基于视频的机器人学习方法（如模仿学习、逆强化学习）对比

### 关键结果
- **步态匹配**：四种步态均实现100%匹配精度（gait matching fidelity）
- **轨迹相似度**：Dynamic Time Warping (DTW) 距离达到$10^{-6}$量级，表明学习到的运动轨迹与演示视频高度一致
- **稳定性**：仿真与真实环境中均实现零失败（zero failures），包括复杂地形下的稳定行走
- **泛化能力**：在形态不同的ANYmal上同样成功学习步态，无需调整流水线参数
- **效率优势**：相比先前工作，数据需求降低（仅需单段视频）、训练时间缩短（PPO收敛更快）、工程投入减少（无需手动设计奖励或标注）

### 结论
SDS证明了通过大语言模型（GPT-4o）的视觉推理能力，可以从单段无标签视频中自动合成四足机器人运动技能。其闭环进化机制有效解决了奖励函数自动生成中的优化问题，且方法具有跨形态泛化能力。开源代码和补充材料已发布。

## Overview
Imagine a robot learning locomotion skills from any single video, without labels or reward engineering. We introduce SDS ("See it. Do it. Sorted."), an automated pipeline for skill acquisition from unstructured demonstrations. Using GPT-4o, SDS applies novel prompting techniques, in the form of spatio-temporal grid-based visual encoding ($G_{v}$) and structured input decomposition (SUS). These produce executable reward functions (RF) from the raw input videos. The RFs are used to train PPO policies and are optimized through closed-loop evolution, using training footage and performance metrics as self-supervised signals. SDS allows quadrupeds (e.g. Unitree Go1) to learn four gaits -- trot, bound, pace, and hop -- achieving 100% gait matching fidelity, Dynamic Time Warping (DTW) distance in the order of $10^{-6}$, and stable locomotion with zero failures, both in simulation and the real world. SDS generalizes to morphologically different quadrupeds (e.g. ANYmal) and outperforms prior work in data efficiency, training time and engineering effort. Further materials and the code are open-source under: https://rpl-cs-ucl.github.io/SDSweb/.

## 参考
- https://arxiv.org/abs/2410.11571
- https://github.com/ImChong/Robotics_Notebooks

## 개요

SDS는 GPT-4o의 시각적 이해 능력을 활용하여 단일 비정형 시연 영상을 로봇이 실행 가능한 보상 함수로 변환합니다. 이 방법은 시공간 그리드 시각적 인코딩($G_{v}$)을 통해 비디오 프레임을 구조적으로 분해하고, 구조화된 입력 분해(SUS)를 통해 보상 함수를 생성한 후, PPO 알고리즘을 사용하여 정책을 훈련하고, 폐쇄 루프 진화 메커니즘(훈련 영상 및 성능 지표를 자기 지도 신호로 활용)을 통해 보상 함수를 지속적으로 최적화합니다. 실험 결과, SDS는 Unitree Go1에서 trot, bound, pace, hop 네 가지 보행을 성공적으로 학습하여 100%의 보행 일치 정확도와 $10^{-6}$ 수준의 DTW 거리를 달성했으며, 시뮬레이션 및 실제 환경 모두에서 실패 사례가 없었습니다. 이 방법은 형태가 다른 ANYmal 로봇에도 일반화 가능하며, 데이터 효율성, 훈련 시간 및 엔지니어링 투입 측면에서 이전 연구보다 우수합니다.

## 핵심 내용
### 방법 아키텍처
SDS 파이프라인은 세 가지 핵심 단계로 구성됩니다:
1. **시각적 인코딩 및 분해**: GPT-4o를 사용하여 입력 영상에 대해 시공간 그리드 시각적 인코딩($G_{v}$)을 수행하고, 연속 프레임을 구조화된 시공간 단위로 분해한 후, 구조화된 입력 분해(SUS)를 통해 주요 운동 특징을 추출합니다.
2. **보상 함수 생성**: SUS 출력을 기반으로 GPT-4o가 자동으로 실행 가능한 보상 함수(RF)를 생성하며, 수동 설계나 레이블이 필요하지 않습니다.
3. **정책 최적화**: PPO 알고리즘을 사용하여 정책을 훈련하고, 폐쇄 루프 진화 메커니즘을 통해 RF를 반복적으로 최적화합니다. 훈련 과정의 영상 및 성능 지표(예: 보행 일치도, 안정성)를 자기 지도 신호로 활용하여 RF 매개변수를 자동으로 조정합니다.

### 실험 설정
- **로봇 플랫폼**: Unitree Go1(사족) 및 ANYmal(다른 형태의 사족)
- **학습 목표**: 네 가지 보행 – trot(속보), bound(도약), pace(측보), hop(외다리 뛰기)
- **훈련 환경**: 시뮬레이션 환경(Isaac Gym) 및 실제 세계 배치
- **비교 기준**: 이전의 영상 기반 로봇 학습 방법(예: 모방 학습, 역강화 학습)과 비교

### 주요 결과
- **보행 일치**: 네 가지 보행 모두 100%의 일치 정확도(gait matching fidelity) 달성
- **궤적 유사도**: Dynamic Time Warping(DTW) 거리가 $10^{-6}$ 수준으로, 학습된 운동 궤적이 시연 영상과 매우 일치함을 나타냄
- **안정성**: 시뮬레이션 및 실제 환경 모두에서 제로 실패(zero failures) 달성, 복잡한 지형에서의 안정적인 보행 포함
- **일반화 능력**: 형태가 다른 ANYmal에서도 파이프라인 매개변수 조정 없이 보행 학습 성공
- **효율성 우위**: 이전 연구 대비 데이터 요구량 감소(단일 영상만 필요), 훈련 시간 단축(PPO 수렴 속도 향상), 엔지니어링 투입 감소(수동 보상 설계나 레이블링 불필요)

### 결론
SDS는 대규모 언어 모델(GPT-4o)의 시각적 추론 능력을 통해 단일 레이블 없는 영상에서 사족 로봇의 운동 기술을 자동으로 합성할 수 있음을 입증했습니다. 폐쇄 루프 진화 메커니즘은 보상 함수 자동 생성에서의 최적화 문제를 효과적으로 해결하며, 이 방법은 형태 간 일반화 능력을 갖추고 있습니다. 오픈 소스 코드 및 추가 자료가 공개되었습니다.
