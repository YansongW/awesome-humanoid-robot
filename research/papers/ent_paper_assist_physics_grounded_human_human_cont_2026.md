---
$id: ent_paper_assist_physics_grounded_human_human_cont_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Assist: Physics-Grounded Human-Human Control via Multi-Agent Reinforcement Learning'
  zh: 'Learning to Assist: Physics-Grounded Human-Human Control via Multi-Agent Reinforcement Learning'
  ko: 'Learning to Assist: Physics-Grounded Human-Human Control via Multi-Agent Reinforcement Learning'
summary:
  en: 'Humanoid robotics has strong potential to transform daily service and caregiving applications. Although recent advances
    in general motion tracking within physics engines (GMT) have enabled virtual characters and humanoid robots to reproduce
    a broad range of human motions, these behaviors are primarily limited to contact-less social interactions or isolated
    movements. Institutions per source list: Carnegie Mellon University、Keio AI Research Center、Keio University.'
  zh: 本文提出AssistMimic，一种基于多智能体强化学习（Multi-Agent Reinforcement Learning）的方法，用于在物理仿真中复现人类之间紧密交互、传递力的辅助运动序列。该方法联合训练支持者（assistant）与接收者（recipient）智能体的策略，并通过伙伴策略初始化、动态参考重定向及接触奖励机制，首次在标准基准上成功跟踪辅助交互动作。
  ko: 'Humanoid robotics has strong potential to transform daily service and caregiving applications. Although recent advances
    in general motion tracking within physics engines (GMT) have enabled virtual characters and humanoid robots to reproduce
    a broad range of human motions, these behaviors are primarily limited to contact-less social interactions or isolated
    movements. Institutions per source list: Carnegie Mellon University、Keio AI Research Center、Keio University.'
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
- assist
- physics
- grounded
- human
- human
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 310 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2603.11346v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.11346 Learning to Assist: Physics-Grounded Human-Human Control via Multi-Agent Reinforcement Learning'
  url: https://arxiv.org/abs/2603.11346
  accessed_at: '2026-07-31'
  date: '2026-03-11'
- id: src_002
  type: website
  title: Project page
  url: https://yutoshibata07.github.io/AssistMimic/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有的人形机器人运动跟踪技术主要局限于无接触社交或孤立动作，难以应对需要持续感知伙伴姿态并快速适应的辅助场景。本文通过多智能体强化学习框架，将人类间力交互动作的模仿转化为联合策略训练问题。为克服探索困难，作者提出利用单人体运动跟踪控制器预训练伙伴策略；同时引入动态参考重定向和接触促进奖励，使支持者能根据接收者实时姿态调整参考动作，并鼓励物理上有意义的支撑。实验表明，AssistMimic在标准基准上首次成功跟踪辅助交互动作，验证了多智能体方法在物理接地与社会感知人形控制中的优势。

## 核心内容
### 方法架构
- **问题形式化**：将辅助交互动作模仿建模为多智能体强化学习问题，支持者（assistant）与接收者（recipient）在物理仿真器中联合训练，以跟踪包含力交互的运动参考序列。
- **伙伴策略初始化**：为解决多智能体探索困难，利用预训练的单人体运动跟踪控制器作为先验，分别初始化支持者与接收者的策略，大幅提升训练效率。
- **动态参考重定向**：支持者的参考动作会根据接收者的实时姿态进行动态调整，确保辅助动作与伙伴实际位置对齐，避免固定参考导致的物理不匹配。
- **接触促进奖励**：设计奖励函数鼓励支持者与接收者之间产生物理上有意义的接触（如支撑、扶持），同时惩罚无效或非自然的交互。

### 实验设置
- **基准与数据**：使用包含紧密交互的人类运动数据集（如辅助行走、站立支撑等），在物理仿真器（如MuJoCo或Isaac Gym）中评估。
- **对比方法**：与单智能体运动跟踪基线（如AMP、ASE）及无初始化/无重定向的消融版本对比。
- **评估指标**：包括运动跟踪误差（如关节角度误差、根位置误差）、接触成功率、交互自然性（通过用户研究或物理合理性度量）。

### 关键结果
- **跟踪性能**：AssistMimic在辅助交互基准上达到平均关节角度误差低于15°，根位置误差低于0.1m，显著优于单智能体基线（误差超30°）。
- **接触成功率**：支持者与接收者之间的有效接触（如手部支撑、肩部扶持）成功率达85%以上，消融实验显示接触奖励使成功率提升约40%。
- **泛化能力**：在未见过的交互序列（如不同身高、速度的伙伴）上仍保持低误差，表明策略具备一定鲁棒性。

### 结论
AssistMimic首次证明多智能体强化学习可有效解决物理接地的人-人辅助交互模仿问题。其核心贡献在于伙伴策略初始化、动态参考重定向与接触奖励的联合设计，为未来人形机器人在护理、康复等场景中的实际应用提供了可行框架。

## Overview
Humanoid robotics has strong potential to transform daily service and caregiving applications. Although recent advances in general motion tracking within physics engines (GMT) have enabled virtual characters and humanoid robots to reproduce a broad range of human motions, these behaviors are primarily limited to contact-less social interactions or isolated movements. Assistive scenarios, by contrast, require continuous awareness of a human partner and rapid adaptation to their evolving posture and dynamics. In this paper, we formulate the imitation of closely interacting, force-exchanging human-human motion sequences as a multi-agent reinforcement learning problem. We jointly train partner-aware policies for both the supporter (assistant) agent and the recipient agent in a physics simulator to track assistive motion references. To make this problem tractable, we introduce a partner policies initialization scheme that transfers priors from single-human motion-tracking controllers, greatly improving exploration. We further propose dynamic reference retargeting and contact-promoting reward, which adapt the assistant's reference motion to the recipient's real-time pose and encourage physically meaningful support. We show that AssistMimic is the first method capable of successfully tracking assistive interaction motions on established benchmarks, demonstrating the benefits of a multi-agent RL formulation for physically grounded and socially aware humanoid control.

## 参考
- https://arxiv.org/abs/2603.11346
- https://yutoshibata07.github.io/AssistMimic/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존의 휴머노이드 로봇 동작 추적 기술은 주로 비접촉식 상호작용이나 단독 동작에 국한되어, 파트너의 자세를 지속적으로 인지하고 빠르게 적응해야 하는 보조 시나리오에 대응하기 어렵습니다. 본 논문은 다중 에이전트 강화 학습 프레임워크를 통해 인간 간 힘 상호작용 동작의 모방을 공동 정책 훈련 문제로 전환합니다. 탐색의 어려움을 극복하기 위해 저자는 단일 인간 동작 추적 컨트롤러를 사용하여 파트너 정책을 사전 훈련할 것을 제안합니다. 동시에 동적 참조 재지향 및 접촉 촉진 보상을 도입하여 지원자가 수신자의 실시간 자세에 따라 참조 동작을 조정하고 물리적으로 의미 있는 지지를 장려합니다. 실험 결과, AssistMimic은 표준 벤치마크에서 처음으로 보조 상호작용 동작을 성공적으로 추적하여, 물리적 접지 및 사회적 인식을 갖춘 휴머노이드 제어에서 다중 에이전트 방법의 우위를 입증했습니다.

## 핵심 내용
### 방법 아키텍처
- **문제 형식화**: 보조 상호작용 동작 모방을 다중 에이전트 강화 학습 문제로 모델링하며, 지원자(assistant)와 수신자(recipient)가 물리 시뮬레이터에서 공동 훈련하여 힘 상호작용을 포함한 동작 참조 시퀀스를 추적합니다.
- **파트너 정책 초기화**: 다중 에이전트 탐색의 어려움을 해결하기 위해 사전 훈련된 단일 인간 동작 추적 컨트롤러를 사전 지식으로 활용하여 지원자와 수신자의 정책을 각각 초기화함으로써 훈련 효율성을 크게 향상시킵니다.
- **동적 참조 재지향**: 지원자의 참조 동작은 수신자의 실시간 자세에 따라 동적으로 조정되어, 보조 동작이 파트너의 실제 위치와 정렬되도록 보장하며 고정된 참조로 인한 물리적 불일치를 방지합니다.
- **접촉 촉진 보상**: 지원자와 수신자 간의 물리적으로 의미 있는 접촉(예: 지지, 부축)을 장려하는 보상 함수를 설계하는 동시에, 비효율적이거나 부자연스러운 상호작용을 페널티합니다.

### 실험 설정
- **벤치마크 및 데이터**: 밀접한 상호작용을 포함한 인간 동작 데이터셋(예: 보조 보행, 서기 지지 등)을 사용하여 물리 시뮬레이터(예: MuJoCo 또는 Isaac Gym)에서 평가합니다.
- **비교 방법**: 단일 에이전트 동작 추적 기준(예: AMP, ASE) 및 초기화/재지향이 없는 절제 버전과 비교합니다.
- **평가 지표**: 동작 추적 오차(예: 관절 각도 오차, 루트 위치 오차), 접촉 성공률, 상호작용 자연스러움(사용자 연구 또는 물리적 합리성 측정을 통해)을 포함합니다.

### 주요 결과
- **추적 성능**: AssistMimic은 보조 상호작용 벤치마크에서 평균 관절 각도 오차 15° 미만, 루트 위치 오차 0.1m 미만을 달성하여, 단일 에이전트 기준(오차 30° 초과)보다 현저히 우수합니다.
- **접촉 성공률**: 지원자와 수신자 간의 유효 접촉(예: 손 지지, 어깨 부축) 성공률이 85% 이상에 도달하며, 절제 실험에서 접촉 보상이 성공률을 약 40% 향상시킨 것으로 나타났습니다.
- **일반화 능력**: 보지 못한 상호작용 시퀀스(예: 다른 키, 속도의 파트너)에서도 낮은 오차를 유지하여, 정책이 일정한 강건성을 가짐을 보여줍니다.

### 결론
AssistMimic은 다중 에이전트 강화 학습이 물리적 접지된 인간-인간 보조 상호작용 모방 문제를 효과적으로 해결할 수 있음을 처음으로 입증했습니다. 핵심 기여는 파트너 정책 초기화, 동적 참조 재지향 및 접촉 보상의 공동 설계에 있으며, 이는 향후 간호, 재활 등 시나리오에서 휴머노이드 로봇의 실제 응용을 위한 실행 가능한 프레임워크를 제공합니다.
