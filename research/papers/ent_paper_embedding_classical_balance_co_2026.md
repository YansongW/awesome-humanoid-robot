---
$id: ent_paper_embedding_classical_balance_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
  zh: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
  ko: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
summary:
  en: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: 本文提出一种将经典平衡控制指标嵌入强化学习框架的统一策略，用于人形机器人的自主恢复。该工作由研究团队于2026年发表，核心贡献在于通过捕获点、质心状态和质心动量作为特权评论家输入与塑形奖励，使单一策略覆盖从踝关节策略到多触点站立的完整恢复谱系，在Unitree
    H1-2上达到93.4%恢复率。
  ko: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embedding_classical_balance_co
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.08619v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1004 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery (arXiv)
  url: https://arxiv.org/abs/2603.08619
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有强化学习方法将人形机器人恢复视为纯任务奖励问题，缺乏对平衡状态的显式表征。本文通过嵌入经典平衡指标（捕获点、质心状态、质心动量）作为特权评论家输入，并直接围绕这些量设计塑形奖励，使演员网络仅依赖本体感觉即可实现零样本硬件迁移。该策略无需参考轨迹或脚本化接触，即可处理小扰动下的踝/髋关节策略、大推力下的补偿步态，以及利用手肘膝盖的多触点倒地站立。在Isaac Lab中训练的Unitree H1-2策略，在随机初始姿态和未脚本化倒地配置下达到93.4%恢复率。消融实验表明移除平衡信息结构会导致站立学习完全失败，证实这些指标提供了有意义的训练信号而非偶然结构。

## 核心内容
### 方法架构
- **平衡指标嵌入**：将捕获点（Capture Point）、质心状态（CoM state）和质心动量（Centroidal Momentum）作为特权信息输入评论家网络，同时基于这些量设计塑形奖励函数
- **演员-评论家框架**：演员网络仅使用本体感觉（关节位置/速度、IMU数据）进行零样本硬件迁移，评论家网络在训练时获取特权平衡指标
- **无参考轨迹设计**：不依赖任何预设运动轨迹或脚本化接触序列，完全通过强化学习自主发现恢复策略

### 实验设置
- **训练环境**：Isaac Lab仿真平台，使用Unitree H1-2人形机器人模型
- **测试配置**：包含随机初始姿态（不同倒地角度/方向）和未脚本化倒地场景（模拟真实跌倒动力学）
- **迁移验证**：Sim-to-sim迁移至MuJoCo环境，以及初步硬件实验

### 关键结果
- **恢复性能**：在随机初始姿态和未脚本化倒地配置下达到93.4%恢复率
- **策略多样性**：单一策略自动涌现出踝关节策略（小扰动）、髋关节策略（中等扰动）、补偿步态（大推力）、多触点站立（利用手肘膝盖）
- **消融实验**：移除平衡信息结构后，站立学习完全失败（0%恢复率），证明这些指标提供了关键学习信号
- **泛化能力**：成功迁移至MuJoCo仿真环境，初步硬件实验验证了跨环境泛化性

### 结论
嵌入可解释的平衡结构显著减少了人形机器人处于失败状态的时间，将自主恢复的能力边界从单一站立任务扩展至包含倒地、补偿步态和多触点站立的完整恢复谱系。该方法为将经典控制理论融入现代强化学习框架提供了有效范式。

## Overview
Humanoid robots remain vulnerable to falls and unrecoverable failure states, limiting their practical utility in unstructured environments. While reinforcement learning has demonstrated stand-up behaviors, existing approaches treat recovery as a pure task-reward problem without an explicit representation of the balance state. We present a unified RL policy that addresses this limitation by embedding classical balance metrics: capture point, center-of-mass state, and centroidal momentum, as privileged critic inputs and shaping rewards directly around these quantities during training, while the actor relies solely on proprioception for zero-shot hardware transfer. Without reference trajectories or scripted contacts, a single policy spans the full recovery spectrum: ankle and hip strategies for small disturbances, corrective stepping under large pushes, and compliant falling with multi-contact stand-up using the hands, elbows, and knees. Trained on the Unitree H1-2 in Isaac Lab, the policy achieves a 93.4% recovery rate across randomized initial poses and unscripted fall configurations. An ablation study shows that removing the balance-informed structure causes stand-up learning to fail entirely, confirming that these metrics provide a meaningful learning signal rather than incidental structure. Sim-to-sim transfer to MuJoCo and preliminary hardware experiments further demonstrate cross-environment generalization. These results show that embedding interpretable balance structure into the learning framework substantially reduces time spent in failure states and broadens the envelope of autonomous recovery.

## 参考
- http://arxiv.org/abs/2603.08619v1

## 개요
기존 강화학습 방법은 휴머노이드 로봇 복구를 순수 작업 보상 문제로 간주하여 균형 상태에 대한 명시적 표현이 부족하다. 본 논문은 고전적 균형 지표(캡처 포인트, 질량 중심 상태, 질량 중심 운동량)를 특권 비평가 입력으로 임베딩하고, 이러한 양을 중심으로 직접 형상 보상을 설계하여 행위자 네트워크가 고유 감각만으로 제로샷 하드웨어 전이를 달성할 수 있게 한다. 이 전략은 참조 궤적이나 스크립트화된 접촉 없이도 작은 교란에서의 발목/고관절 전략, 큰 추력에서의 보상 보행, 팔꿈치와 무릎을 활용한 다중 접촉 쓰러짐 후 기립을 처리할 수 있다. Isaac Lab에서 훈련된 Unitree H1-2 전략은 무작위 초기 자세와 비스크립트화된 쓰러짐 구성에서 93.4%의 복구율을 달성했다. 절제 실험에서 균형 정보 구조를 제거하면 기립 학습이 완전히 실패함을 보여주며, 이러한 지표가 우연한 구조가 아닌 의미 있는 훈련 신호를 제공함을 확인했다.

## 핵심 내용
### 방법 아키텍처
- **균형 지표 임베딩**: 캡처 포인트(Capture Point), 질량 중심 상태(CoM state), 질량 중심 운동량(Centroidal Momentum)을 특권 정보로 비평가 네트워크에 입력하고, 이러한 양을 기반으로 형상 보상 함수를 설계
- **행위자-비평가 프레임워크**: 행위자 네트워크는 고유 감각(관절 위치/속도, IMU 데이터)만 사용하여 제로샷 하드웨어 전이를 수행하고, 비평가 네트워크는 훈련 중 특권 균형 지표를 획득
- **참조 궤적 없는 설계**: 사전 정의된 운동 궤적이나 스크립트화된 접촉 시퀀스에 의존하지 않으며, 완전히 강화학습을 통해 복구 전략을 자율적으로 발견

### 실험 설정
- **훈련 환경**: Isaac Lab 시뮬레이션 플랫폼, Unitree H1-2 휴머노이드 로봇 모델 사용
- **테스트 구성**: 무작위 초기 자세(다양한 쓰러짐 각도/방향) 및 비스크립트화된 쓰러짐 시나리오(실제 낙하 역학 시뮬레이션) 포함
- **전이 검증**: MuJoCo 환경으로의 Sim-to-sim 전이 및 초기 하드웨어 실험

### 주요 결과
- **복구 성능**: 무작위 초기 자세 및 비스크립트화된 쓰러짐 구성에서 93.4%의 복구율 달성
- **전략 다양성**: 단일 전략에서 발목 관절 전략(작은 교란), 고관절 전략(중간 교란), 보상 보행(큰 추력), 다중 접촉 기립(팔꿈치와 무릎 활용)이 자율적으로 출현
- **절제 실험**: 균형 정보 구조를 제거하면 기립 학습이 완전히 실패(0% 복구율)하여, 이러한 지표가 핵심 학습 신호를 제공함을 입증
- **일반화 능력**: MuJoCo 시뮬레이션 환경으로 성공적으로 전이되었으며, 초기 하드웨어 실험에서 교차 환경 일반화를 검증

### 결론
해석 가능한 균형 구조를 임베딩함으로써 휴머노이드 로봇이 실패 상태에 머무는 시간을 크게 줄이고, 자율 복구 능력의 경계를 단일 기립 작업에서 쓰러짐, 보상 보행, 다중 접촉 기립을 포함한 완전한 복구 스펙트럼으로 확장했다. 본 방법은 고전 제어 이론을 현대 강화학습 프레임워크에 통합하는 효과적인 패러다임을 제공한다.
