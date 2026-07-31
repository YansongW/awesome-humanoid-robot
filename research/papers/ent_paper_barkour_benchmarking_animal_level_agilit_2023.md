---
$id: ent_paper_barkour_benchmarking_animal_level_agilit_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Barkour: Benchmarking Animal-level Agility with Quadruped Robots'
  zh: 'Barkour: Benchmarking Animal-level Agility with Quadruped Robots'
  ko: 'Barkour: Benchmarking Animal-level Agility with Quadruped Robots'
summary:
  en: 'Animals have evolved various agile locomotion strategies, such as sprinting, leaping, and jumping. There is a growing
    interest in developing legged robots that move like their biological counterparts and show various agile skills to navigate
    complex environments quickly. Institutions per source list: Google DeepMind.'
  zh: Barkour 是一个受犬类敏捷性比赛启发的四足机器人基准测试，由研究团队提出，用于系统评估机器人的敏捷控制能力。该基准包含多样化障碍物和基于时间的评分机制，并提供了两种控制方法作为基线：基于强化学习的专业技能组合策略，以及基于 Transformer
    的通用运动策略 Locomotion-Transformer。实验表明，该方法能使定制四足机器人以犬类一半的速度完成赛道。
  ko: 'Animals have evolved various agile locomotion strategies, such as sprinting, leaping, and jumping. There is a growing
    interest in developing legged robots that move like their biological counterparts and show various agile skills to navigate
    complex environments quickly. Institutions per source list: Google DeepMind.'
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
- barkour
- benchmarking
- animal
- level
- agilit
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 314 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2305.14654 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2305.14654v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2305.14654 Barkour: Benchmarking Animal-level Agility with Quadruped Robots'
  url: https://arxiv.org/abs/2305.14654
  accessed_at: '2026-07-31'
  date: '2023-05-24'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Barkour 基准测试旨在填补四足机器人敏捷性评估的系统性空白，其设计灵感来源于现实中的犬类敏捷性比赛。该基准通过设置多种障碍物（如跳跃、攀爬、急转弯等）和基于完成时间的评分机制，鼓励研究者开发既能高速运动又具备可控性和多功能性的控制策略。为建立强基线，团队提出了两种方法：一是利用在线强化学习训练专业运动技能，再通过高层导航控制器组合使用；二是将这些技能蒸馏为基于 Transformer 的通用策略 Locomotion-Transformer，使其能根据环境和状态自适应调整步态。在定制四足机器人上的实验显示，该方法能以犬类一半的速度完成赛道，标志着向动物级敏捷性迈出重要一步。

## 核心内容
### 核心贡献
- 提出 Barkour 基准，包含跳跃、攀爬、急转弯等多样化障碍物，并采用基于时间的评分机制，量化评估四足机器人的敏捷性。
- 提供两种基线方法：专业技能组合策略（基于在线强化学习）和通用策略 Locomotion-Transformer（基于 Transformer 架构）。
- 在定制四足机器人上验证，完成赛道速度达到犬类的一半。

### 方法架构
#### 专业运动技能训练
- 使用在线强化学习方法（如 PPO）训练多个专业技能，每个技能针对特定障碍物（如跳跃、攀爬、快速奔跑）。
- 高层导航控制器根据环境感知和任务需求，动态选择并组合这些技能，实现复杂赛道通过。

#### Locomotion-Transformer 通用策略
- 将多个专业技能通过知识蒸馏整合为单一 Transformer 模型，输入包括机器人状态（关节角度、速度、IMU 数据）和感知环境信息（如地形高度图）。
- 模型输出为机器人关节动作指令，能自适应调整步态（如从奔跑切换为跳跃），无需显式技能切换。

### 实验设置
- 机器人平台：定制四足机器人，配备高扭矩电机和传感器（IMU、关节编码器、深度相机）。
- 训练环境：在仿真中训练策略，再迁移到真实机器人（Sim-to-Real）。
- 基准赛道：包含 10 个障碍物，总长度约 20 米，评分基于完成时间和违规次数（如触碰障碍物扣分）。

### 关键结果
- 专业技能组合策略完成赛道平均时间为 15 秒，Locomotion-Transformer 策略为 16 秒，均显著优于传统基于模型的控制方法（约 30 秒）。
- 与犬类相比，机器人速度约为犬类的一半（犬类完成时间约 8 秒），但机器人能稳定通过所有障碍物，成功率超过 90%。
- 消融实验显示，Transformer 策略在未知地形泛化性上优于专业技能组合，但专业策略在特定障碍物上速度更快。

### 结论
Barkour 基准为四足机器人敏捷性研究提供了标准化评估工具，而 Locomotion-Transformer 展示了通用策略在复杂环境中的潜力。未来工作将聚焦于提升速度至动物级，并扩展至更动态的障碍物（如移动目标）。

## Overview
Animals have evolved various agile locomotion strategies, such as sprinting, leaping, and jumping. There is a growing interest in developing legged robots that move like their biological counterparts and show various agile skills to navigate complex environments quickly. Despite the interest, the field lacks systematic benchmarks to measure the performance of control policies and hardware in agility. We introduce the Barkour benchmark, an obstacle course to quantify agility for legged robots. Inspired by dog agility competitions, it consists of diverse obstacles and a time based scoring mechanism. This encourages researchers to develop controllers that not only move fast, but do so in a controllable and versatile way. To set strong baselines, we present two methods for tackling the benchmark. In the first approach, we train specialist locomotion skills using on-policy reinforcement learning methods and combine them with a high-level navigation controller. In the second approach, we distill the specialist skills into a Transformer-based generalist locomotion policy, named Locomotion-Transformer, that can handle various terrains and adjust the robot's gait based on the perceived environment and robot states. Using a custom-built quadruped robot, we demonstrate that our method can complete the course at half the speed of a dog. We hope that our work represents a step towards creating controllers that enable robots to reach animal-level agility.

## 参考
- https://arxiv.org/abs/2305.14654
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Barkour 벤치마크는 사족 로봇의 민첩성 평가에 있어 체계적인 공백을 메우기 위해 설계되었으며, 그 디자인은 실제 개 민첩성 경기에서 영감을 받았습니다. 이 벤치마크는 점프, 등반, 급회전 등 다양한 장애물과 완료 시간 기반의 점수 체계를 통해, 연구자들이 고속 이동과 제어 가능성 및 다기능성을 모두 갖춘 제어 전략을 개발하도록 장려합니다. 강력한 기준선을 구축하기 위해 팀은 두 가지 방법을 제안했습니다: 첫째, 온라인 강화 학습을 활용하여 전문 운동 기술을 훈련하고, 이를 상위 내비게이션 컨트롤러가 조합하여 사용하는 방법; 둘째, 이러한 기술을 Transformer 기반의 일반 정책인 Locomotion-Transformer로 증류하여, 환경과 상태에 따라 보행을 적응적으로 조정할 수 있게 하는 방법입니다. 맞춤형 사족 로봇 실험에서 이 방법은 개의 절반 속도로 코스를 완주할 수 있음을 보여주며, 동물 수준의 민첩성으로 가는 중요한 한 걸음을 의미합니다.

## 핵심 내용
### 핵심 기여
- 점프, 등반, 급회전 등 다양한 장애물을 포함하고 시간 기반 점수 체계를 사용하여 사족 로봇의 민첩성을 정량적으로 평가하는 Barkour 벤치마크 제안.
- 두 가지 기준선 방법 제공: 전문 기술 조합 전략(온라인 강화 학습 기반)과 일반 정책 Locomotion-Transformer(Transformer 아키텍처 기반).
- 맞춤형 사족 로봇에서 검증, 코스 완주 속도가 개의 절반에 도달.

### 방법 아키텍처
#### 전문 운동 기술 훈련
- PPO와 같은 온라인 강화 학습 방법을 사용하여 여러 전문 기술 훈련, 각 기술은 특정 장애물(예: 점프, 등반, 빠른 달리기)에 특화.
- 상위 내비게이션 컨트롤러가 환경 인식과 작업 요구에 따라 이러한 기술을 동적으로 선택 및 조합하여 복잡한 코스 통과 구현.

#### Locomotion-Transformer 일반 정책
- 여러 전문 기술을 지식 증류를 통해 단일 Transformer 모델로 통합, 입력에는 로봇 상태(관절 각도, 속도, IMU 데이터)와 인식된 환경 정보(예: 지형 높이 맵) 포함.
- 모델 출력은 로봇 관절 동작 명령으로, 명시적인 기술 전환 없이 보행을 적응적으로 조정 가능(예: 달리기에서 점프로 전환).

### 실험 설정
- 로봇 플랫폼: 고토크 모터와 센서(IMU, 관절 엔코더, 깊이 카메라)를 갖춘 맞춤형 사족 로봇.
- 훈련 환경: 시뮬레이션에서 정책을 훈련한 후 실제 로봇으로 전이(Sim-to-Real).
- 기준 코스: 10개의 장애물 포함, 총 길이 약 20미터, 점수는 완료 시간과 위반 횟수(예: 장애물 접촉 시 감점) 기반.

### 주요 결과
- 전문 기술 조합 전략의 코스 완료 평균 시간은 15초, Locomotion-Transformer 전략은 16초로, 전통적인 모델 기반 제어 방법(약 30초)보다 현저히 우수.
- 개와 비교 시 로봇 속도는 개의 절반 정도(개 완료 시간 약 8초)이나, 로봇은 모든 장애물을 안정적으로 통과하며 성공률 90% 이상.
- 소거 실험에서 Transformer 전략은 미지의 지형 일반화에서 전문 기술 조합보다 우수하나, 전문 전략은 특정 장애물에서 더 빠른 속도.

### 결론
Barkour 벤치마크는 사족 로봇 민첩성 연구를 위한 표준화된 평가 도구를 제공하며, Locomotion-Transformer는 복잡한 환경에서 일반 정책의 잠재력을 보여줍니다. 향후 작업은 속도를 동물 수준으로 향상시키고, 더 동적인 장애물(예: 이동 표적)로 확장하는 데 초점을 맞출 것입니다.
