---
$id: ent_paper_bfm_zero_a_promptable_behavior_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
  zh: BFM-Zero｜使用无监督强化学习的人形控制的即时行为基础模型
  ko: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
summary:
  en: Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under
    a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid
    characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective
    shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to
    be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile
    and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot
    motion tracking, goal reaching, and reward optimization, and few-sho
  zh: BFM-Zero 是一个面向人形机器人控制的提示式行为基础模型框架，由研究团队提出。其核心贡献在于通过无监督强化学习学习共享潜在表示，将运动、目标和奖励嵌入同一空间，使单一策略无需重新训练即可执行多种下游任务。该模型在 Unitree
    G1 人形机器人上实现了零样本运动跟踪、目标到达和奖励优化等真实世界全身技能。
  ko: BFM-Zero 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、分层技能/专家策略、闭环纠错/人类干预训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- balance
- behavioral_foundation_model
- bfm_zero
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: BFM-Zero: A Promptable
    Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning. [2026-07-29] zh content backfilled
    from English abstract via scripts/sinicize_english_cards.py | WP1 dedup merge 2026-08-06: merged ent_paper_bfm_zero_a_promptable_behavior_2025
    into this card (rules: same_title_same_year). Backup+manifest: .staging/cleanup_wp12/. | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (992 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: BFM-Zero project page
  url: https://lecar-lab.github.io/BFM-Zero/
  date: '2025'
  accessed_at: '2026-06-26'
- id: src_002
  type: paper
  title: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
  url: https://arxiv.org/abs/2511.04131
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
现有的人形机器人行为基础模型要么仅部署于仿真环境，要么局限于特定任务如跟踪。BFM-Zero 通过无监督强化学习和 Forward-Backward (FB) 模型构建了一个目标导向、可解释且平滑的潜在表示空间，从而支持多种推理方法。该框架结合了奖励塑形、域随机化和历史依赖的非对称学习等关键设计，有效缩小了仿真到现实的差距。在 Unitree G1 人形机器人上的真实世界实验中，BFM-Zero 展示了零样本运动跟踪、目标到达和奖励优化等多样化能力，并通过少量样本的优化实现自适应。

## 核心内容
### 方法架构
BFM-Zero 的核心是学习一个共享潜在表示空间，该空间通过无监督强化学习将运动、目标和奖励嵌入统一表征。具体而言，框架基于 Forward-Backward (FB) 模型，该模型提供目标导向、可解释且平滑的全身运动潜在表示。与传统的基于策略的强化学习框架不同，BFM-Zero 利用无监督 RL 的最新进展，避免了手动设计奖励函数的繁琐过程。

### 关键设计
- **奖励塑形**：通过精心设计的奖励函数引导策略学习，提升任务性能。
- **域随机化**：在仿真环境中引入随机化参数（如物理属性、传感器噪声），增强策略对真实世界变化的鲁棒性。
- **历史依赖的非对称学习**：利用历史观测信息进行非对称训练，进一步缩小仿真到现实的差距。

### 实验设置
- **硬件平台**：Unitree G1 人形机器人。
- **推理方法**：支持零样本运动跟踪、目标到达、奖励优化，以及基于少量样本的优化自适应。
- **消融实验**：在仿真环境中对关键设计选择（如奖励塑形、域随机化）进行定量消融分析，验证其有效性。

### 关键结果
- BFM-Zero 在真实世界 Unitree G1 人形机器人上成功实现了多种全身技能，包括零样本运动跟踪（如行走、跑步）、目标到达（如抓取指定位置）和奖励优化（如平衡控制）。
- 通过少量样本的优化自适应，策略能够快速适应新任务或环境变化。
- 消融实验表明，奖励塑形和域随机化对策略的鲁棒性和泛化能力至关重要。

### 结论
BFM-Zero 是首个可提示的行为基础模型，为人形机器人全身控制提供了可扩展的解决方案。其共享潜在表示和多样化的推理方法为未来通用人形机器人策略的发展奠定了基础。

## Overview
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 参考
- Semantic Scholar search: BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning

## 개요
기존의 휴머노이드 로봇 행동 기반 모델은 시뮬레이션 환경에만 배포되거나 추적과 같은 특정 작업에 국한되어 있습니다. BFM-Zero는 비지도 강화 학습과 Forward-Backward (FB) 모델을 통해 목표 지향적이고 해석 가능하며 매끄러운 잠재 표현 공간을 구축하여 다양한 추론 방법을 지원합니다. 이 프레임워크는 보상 형성, 도메인 무작위화, 기록 의존적 비대칭 학습과 같은 핵심 설계를 결합하여 시뮬레이션-실제 격차를 효과적으로 줄입니다. Unitree G1 휴머노이드 로봇에서의 실제 세계 실험에서 BFM-Zero는 제로샷 운동 추적, 목표 도달, 보상 최적화와 같은 다양한 능력을 입증했으며, 소량 샘플 최적화를 통한 적응도 가능합니다.

## 핵심 내용
### 방법 아키텍처
BFM-Zero의 핵심은 비지도 강화 학습을 통해 운동, 목표, 보상을 통합 표현으로 임베딩하는 공유 잠재 표현 공간을 학습하는 것입니다. 구체적으로, 프레임워크는 목표 지향적이고 해석 가능하며 매끄러운 전신 운동 잠재 표현을 제공하는 Forward-Backward (FB) 모델을 기반으로 합니다. 전통적인 정책 기반 강화 학습 프레임워크와 달리 BFM-Zero는 비지도 RL의 최신 발전을 활용하여 수동 보상 함수 설계의 번거로운 과정을 피합니다.

### 핵심 설계
- **보상 형성**: 정교하게 설계된 보상 함수를 통해 정책 학습을 유도하여 작업 성능을 향상시킵니다.
- **도메인 무작위화**: 시뮬레이션 환경에 무작위화 매개변수(예: 물리 속성, 센서 노이즈)를 도입하여 실제 세계 변화에 대한 정책의 견고성을 강화합니다.
- **기록 의존적 비대칭 학습**: 과거 관측 정보를 활용한 비대칭 훈련을 통해 시뮬레이션-실제 격차를 더욱 줄입니다.

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇.
- **추론 방법**: 제로샷 운동 추적, 목표 도달, 보상 최적화, 소량 샘플 기반 최적화 적응을 지원합니다.
- **소거 실험**: 시뮬레이션 환경에서 보상 형성, 도메인 무작위화와 같은 핵심 설계 선택에 대한 정량적 소거 분석을 수행하여 유효성을 검증합니다.

### 핵심 결과
- BFM-Zero는 실제 세계 Unitree G1 휴머노이드 로봇에서 제로샷 운동 추적(예: 걷기, 달리기), 목표 도달(예: 지정된 위치 잡기), 보상 최적화(예: 균형 제어)를 포함한 다양한 전신 기술을 성공적으로 구현했습니다.
- 소량 샘플 최적화 적응을 통해 정책은 새로운 작업이나 환경 변화에 빠르게 적응할 수 있습니다.
- 소거 실험은 보상 형성과 도메인 무작위화가 정책의 견고성과 일반화 능력에 중요함을 보여줍니다.

### 결론
BFM-Zero는 최초의 프롬프트 가능한 행동 기반 모델로, 휴머노이드 로봇 전신 제어를 위한 확장 가능한 솔루션을 제공합니다. 공유 잠재 표현과 다양한 추론 방법은 미래의 범용 휴머노이드 로봇 정책 개발의 기반을 마련합니다.
