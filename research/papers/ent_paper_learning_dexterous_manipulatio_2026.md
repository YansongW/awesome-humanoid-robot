---
$id: ent_paper_learning_dexterous_manipulatio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration
  zh: Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration
  ko: Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration
summary:
  en: 'arXiv:2607.00033v1 Announce Type: new Abstract: Dexterous robot manipulation can benefit from the abundance of human
    demonstrations, but transferring such demonstrations to robot policies remains challenging. We present Contact Wrench
    Guidance from Human Demonstration in Robotic Dexterous Manipulation (CHORD), a framework for long-horizon manipulation
    of rigid and articulated objects with reinforcement learning. The key idea is object-centric contact wrench space guidance:
    we represent human and robot motions by the forces and torques they can induce on the object, enabling similarity to be
    measured by the induced instantaneous motions. This guidance makes reinforcement learning more scalable for contact-rich
    dexterous manipulation. We further introduce a large-scale simulation benchmark with 4,739 bimanual dexterous manipulation
    tasks, constructed from motion-capture datasets and reconstructed in-house videos. Evaluated on 1,831 benchmark tasks,
    CHORD achieves an average success rate of 82.12%, demonstrating strong scalability. CHORD also generalizes to whole-body
    manipulation from hand-only and third-person demonstrations, achieving a 90.77% success rate, and the learned policies
    transfer to the real world in both open-loop and closed-loop settings.'
  zh: CHORD 是一个利用人类演示中的接触力/力矩信息来引导机器人灵巧操作的强化学习框架。其核心创新在于以物体为中心的接触力空间引导，通过比较人类与机器人对物体施加的瞬时力/力矩来度量动作相似性。该框架在包含 4,739 个双手灵巧操作任务的大规模仿真基准上平均成功率达
    82.12%，并能迁移到真实世界。
  ko: 'arXiv:2607.00033v1 Announce Type: new Abstract: Dexterous robot manipulation can benefit from the abundance of human
    demonstrations, but transferring such demonstrations to robot policies remains challenging. We present Contact Wrench
    Guidance from Human Demonstration in Robotic Dexterous Manipulation (CHORD), a framework for long-horizon manipulation
    of rigid and articulated objects with reinforcement learning. The key idea is object-centric contact wrench space guidance:
    we represent human and robot motions by the forces and torques they can induce on the object, enabling similarity to be
    measured by the induced instantaneous motions. This guidance makes reinforcement learning more scalable for contact-rich
    dexterous manipulation. We further introduce a large-scale simulation benchmark with 4,739 bimanual dexterous manipulation
    tasks, constructed from motion-capture datasets and reconstructed in-house videos. Evaluated on 1,831 benchmark tasks,
    CHORD achieves an average success rate of 82.12%, demonstrating strong scalability. CHORD also generalizes to whole-body
    manipulation from hand-only and third-person demonstrations, achieving a 90.77% success rate, and the learned policies
    transfer to the real world in both open-loop and closed-loop settings.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- learning_dexterous_manipulatio
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00033v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (917 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration (arXiv)
  url: https://arxiv.org/abs/2607.00033
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
CHORD 框架解决了将人类演示迁移到机器人灵巧操作策略中的核心难题。它提出了一种以物体为中心的接触力空间引导方法，将人类和机器人的运动都表示为它们对物体施加的力和力矩，从而通过物体受到的瞬时运动来度量两者的相似性。这种引导方式使得强化学习在处理接触丰富的灵巧操作任务时更具可扩展性。为了验证方法，研究者构建了一个包含 4,739 个双手灵巧操作任务的大规模仿真基准，并基于 1,831 个任务进行了评估，平均成功率达到 82.12%。此外，CHORD 还能从仅手部或第三人称视角的演示中泛化到全身操作，成功率达 90.77%，且学到的策略在开环和闭环设置下均能成功迁移到真实世界。

## 核心内容
### 方法核心
- **接触力空间引导**：CHORD 的核心思想是“以物体为中心的接触力空间引导”。它将人类和机器人的操作动作统一表示为它们对物体施加的接触力与力矩（即接触力/力矩），通过比较这些力/力矩引起的物体瞬时运动来评估动作相似性，从而绕开了直接匹配人体关节角度或末端轨迹的难题。
- **强化学习框架**：该引导信号被集成到强化学习奖励函数中，指导机器人策略学习。这种基于物理交互的引导方式，使得强化学习在接触频繁、高维动作空间的灵巧操作任务中更易收敛和扩展。

### 实验设置与基准
- **大规模基准**：研究者构建了一个包含 **4,739 个双手灵巧操作任务** 的仿真基准。这些任务数据来源于公开的动作捕捉数据集以及内部重建的视频，涵盖了刚体和铰接物体的长时域操作。
- **评估规模**：在其中的 **1,831 个任务** 上进行了系统评估。

### 关键结果
- **主实验结果**：CHORD 在 1,831 个基准任务上的平均成功率达到 **82.12%**，展示了其强大的可扩展性。
- **泛化能力**：
  - 从仅手部演示或第三人称视角演示中，CHORD 能成功泛化到全身操作任务，成功率达 **90.77%**。
- **真实世界迁移**：学到的策略在真实机器人上进行了验证，在开环（open-loop）和闭环（closed-loop）两种控制设置下均能成功执行操作任务。

## Overview
Dexterous robot manipulation can benefit from the abundance of human demonstrations, but transferring such demonstrations to robot policies remains challenging. We present Contact Wrench Guidance from Human Demonstration in Robotic Dexterous Manipulation (CHORD), a framework for long-horizon manipulation of rigid and articulated objects with reinforcement learning. The key idea is object-centric contact wrench space guidance: we represent human and robot motions by the forces and torques they can induce on the object, enabling similarity to be measured by the induced instantaneous motions. This guidance makes reinforcement learning more scalable for contact-rich dexterous manipulation. We further introduce a large-scale simulation benchmark with 4,739 bimanual dexterous manipulation tasks, constructed from motion-capture datasets and reconstructed in-house videos. Evaluated on 1,831 benchmark tasks, CHORD achieves an average success rate of 82.12%, demonstrating strong scalability. CHORD also generalizes to whole-body manipulation from hand-only and third-person demonstrations, achieving a 90.77% success rate, and the learned policies transfer to the real world in both open-loop and closed-loop settings.

## 参考
- http://arxiv.org/abs/2607.00033v1

## 개요
CHORD 프레임워크는 인간 시연을 로봇 손재주 조작 정책으로 이전하는 핵심 난제를 해결합니다. 이는 객체 중심의 접촉 힘 공간 안내 방법을 제안하여, 인간과 로봇의 움직임을 모두 객체에 가하는 힘과 토크로 표현함으로써 객체가 받는 순간 운동을 통해 둘의 유사성을 측정합니다. 이러한 안내 방식은 강화 학습이 접촉이 빈번한 손재주 조작 작업에서 더 확장 가능하게 만듭니다. 방법을 검증하기 위해 연구자들은 **4,739개의 양손 손재주 조작 작업**을 포함하는 대규모 시뮬레이션 벤치마크를 구축하고, **1,831개의 작업**을 기반으로 평가하여 평균 성공률 **82.12%**를 달성했습니다. 또한 CHORD는 손만 또는 3인칭 시점의 시연에서 전신 조작으로 일반화할 수 있으며, 성공률은 **90.77%**에 달합니다. 학습된 정책은 개루프 및 폐루프 설정 모두에서 실제 세계로 성공적으로 이전됩니다.

## 핵심 내용
### 방법 핵심
- **접촉 힘 공간 안내**: CHORD의 핵심 아이디어는 '객체 중심의 접촉 힘 공간 안내'입니다. 이는 인간과 로봇의 조작 동작을 객체에 가하는 접촉 힘과 토크(즉, 접촉 힘/토크)로 통일하여 표현하고, 이러한 힘/토크가 유발하는 객체의 순간 운동을 비교하여 동작 유사성을 평가함으로써 인간 관절 각도나 말단 궤적을 직접 매칭하는 어려움을 우회합니다.
- **강화 학습 프레임워크**: 이 안내 신호는 강화 학습 보상 함수에 통합되어 로봇 정책 학습을 안내합니다. 이러한 물리적 상호작용 기반의 안내 방식은 접촉이 빈번하고 고차원 동작 공간을 가진 손재주 조작 작업에서 강화 학습이 더 쉽게 수렴하고 확장되도록 합니다.

### 실험 설정 및 벤치마크
- **대규모 벤치마크**: 연구자들은 **4,739개의 양손 손재주 조작 작업**을 포함하는 시뮬레이션 벤치마크를 구축했습니다. 이 작업 데이터는 공개 모션 캡처 데이터셋과 내부 재구성 비디오에서 비롯되었으며, 강체 및 관절 객체의 장시간 조작을 포함합니다.
- **평가 규모**: 그중 **1,831개의 작업**에서 체계적인 평가를 수행했습니다.

### 핵심 결과
- **주요 실험 결과**: CHORD는 1,831개의 벤치마크 작업에서 평균 성공률 **82.12%**를 달성하여 강력한 확장성을 보여줍니다.
- **일반화 능력**:
  - 손만 시연 또는 3인칭 시점 시연에서 CHORD는 전신 조작 작업으로 성공적으로 일반화하며, 성공률은 **90.77%**입니다.
- **실제 세계 이전**: 학습된 정책은 실제 로봇에서 검증되었으며, 개루프(open-loop) 및 폐루프(closed-loop) 두 제어 설정 모두에서 조작 작업을 성공적으로 수행합니다.
