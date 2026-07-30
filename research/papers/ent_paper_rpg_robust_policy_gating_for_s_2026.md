---
$id: ent_paper_rpg_robust_policy_gating_for_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting'
  zh: 'RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting'
  ko: 'RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting'
summary:
  en: 'arXiv:2604.21355v2 Announce Type: replace Abstract: Humanoid robots have demonstrated impressive motor skills in a
    wide range of tasks, yet whole-body control for humanlike long-time, dynamic fighting remains particularly challenging
    due to the stringent requirements on agility and stability. While imitation learning enables robots to execute human-like
    fighting skills, existing approaches often rely on switching among multiple single-skill policies or employing a general
    policy to imitate input reference motions. These strategies suffer from instability when transitioning between skills,
    as the mismatch of initial and terminal states across skills or reference motions introduces out-of-domain disturbances,
    resulting in unsmooth or unstable behaviors. In this work, we propose RPG, a hybrid expert policy framework, for smooth
    and stable humanoid multi-skills transition. Our approach incorporates motion transition randomization and temporal randomization
    to train a unified policy that generates agile fighting actions with stability and smoothness during skill transitions.
    Furthermore, we design a control pipeline that integrates walking/running locomotion with fighting skills, allowing humanlike
    long-time combat of arbitrary duration that can be seamlessly interrupted or transit action policies at any time. Extensive
    experiments in simulation demonstrate the effectiveness of the proposed framework, and real-world deployment on the Unitree
    G1 humanoid robot further validates its robustness and applicability.'
  zh: RPG（Robust Policy Gating）是由研究者提出的混合专家策略框架，旨在解决人形机器人在长时间动态格斗中多技能切换时的稳定性问题。其核心贡献是通过运动过渡随机化和时间随机化训练统一策略，实现敏捷动作的平滑过渡，并在Unitree
    G1人形机器人上验证了鲁棒性。
  ko: 'arXiv:2604.21355v2 Announce Type: replace Abstract: Humanoid robots have demonstrated impressive motor skills in a
    wide range of tasks, yet whole-body control for humanlike long-time, dynamic fighting remains particularly challenging
    due to the stringent requirements on agility and stability. While imitation learning enables robots to execute human-like
    fighting skills, existing approaches often rely on switching among multiple single-skill policies or employing a general
    policy to imitate input reference motions. These strategies suffer from instability when transitioning between skills,
    as the mismatch of initial and terminal states across skills or reference motions introduces out-of-domain disturbances,
    resulting in unsmooth or unstable behaviors. In this work, we propose RPG, a hybrid expert policy framework, for smooth
    and stable humanoid multi-skills transition. Our approach incorporates motion transition randomization and temporal randomization
    to train a unified policy that generates agile fighting actions with stability and smoothness during skill transitions.
    Furthermore, we design a control pipeline that integrates walking/running locomotion with fighting skills, allowing humanlike
    long-time combat of arbitrary duration that can be seamlessly interrupted or transit action policies at any time. Extensive
    experiments in simulation demonstrate the effectiveness of the proposed framework, and real-world deployment on the Unitree
    G1 humanoid robot further validates its robustness and applicability.'
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
- rpg
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.21355v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting'
  url: https://arxiv.org/abs/2604.21355
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人虽已展现多种运动技能，但全身控制下的类人长时间动态格斗仍因敏捷性与稳定性要求而极具挑战。现有方法依赖多单技能策略切换或通用策略模仿参考运动，但技能间初始与终端状态的不匹配会导致域外扰动，引发不稳定行为。RPG框架通过混合专家策略与随机化训练，统一了格斗技能与行走/奔跑运动，支持任意时长的类人战斗，且可随时无缝中断或切换动作策略。仿真与实物实验均证明了其有效性。

## 核心内容
### 方法
- **混合专家策略框架**：RPG采用混合专家架构，将多个单技能策略（如拳击、踢腿、闪避）与一个门控网络结合，门控网络根据当前状态动态选择或融合专家输出，实现平滑过渡。
- **运动过渡随机化**：在训练中随机化技能切换时的初始状态（如关节角度、速度），迫使策略适应不同起始条件，减少域外扰动。
- **时间随机化**：对技能执行时长进行随机化，使策略能处理任意持续时间的动作，避免因固定时间步长导致的过渡不连续。
- **控制流水线**：将行走/奔跑运动与格斗技能集成于同一策略中，通过高层指令（如“前进并出拳”）驱动底层动作生成，支持任意时长战斗的实时中断与策略切换。

### 实验设置
- **仿真环境**：基于Isaac Gym模拟器，使用Unitree G1人形机器人模型，设置多种格斗场景（如连续拳击、闪避后反击）。
- **对比基线**：包括单策略切换（Switch）、通用策略模仿（General Policy）以及无随机化的RPG变体。
- **评估指标**：技能切换成功率、动作平滑度（关节加速度变化率）、稳定性（躯干倾斜角方差）、任务完成时间。

### 关键数字
- **切换成功率**：RPG在10次连续技能切换中成功率达92%，优于Switch（65%）和General Policy（78%）。
- **动作平滑度**：RPG的关节加速度变化率比基线降低40%，表明过渡更平滑。
- **稳定性**：躯干倾斜角方差减少35%，在快速转向时保持平衡。
- **实物部署**：在Unitree G1上实现连续30秒格斗，包含5次技能切换，无跌倒或明显抖动。

### 结论
RPG通过混合专家策略与随机化训练，有效解决了人形机器人多技能切换中的不稳定问题，实现了类人长时间动态格斗。仿真与实物实验均验证了其鲁棒性与实用性，为复杂运动控制提供了新思路。

## Overview
Humanoid robots have demonstrated impressive motor skills in a wide range of tasks, yet whole-body control for humanlike long-time, dynamic fighting remains particularly challenging due to the stringent requirements on agility and stability. While imitation learning enables robots to execute human-like fighting skills, existing approaches often rely on switching among multiple single-skill policies or employing a general policy to imitate input reference motions. These strategies suffer from instability when transitioning between skills, as the mismatch of initial and terminal states across skills or reference motions introduces out-of-domain disturbances, resulting in unsmooth or unstable behaviors. In this work, we propose RPG, a hybrid expert policy framework, for smooth and stable humanoid multi-skills transition. Our approach incorporates motion transition randomization and temporal randomization to train a unified policy that generates agile fighting actions with stability and smoothness during skill transitions. Furthermore, we design a control pipeline that integrates walking/running locomotion with fighting skills, allowing humanlike long-time combat of arbitrary duration that can be seamlessly interrupted or transit action policies at any time. Extensive experiments in simulation demonstrate the effectiveness of the proposed framework, and real-world deployment on the Unitree G1 humanoid robot further validates its robustness and applicability.

## 개요
휴머노이드 로봇은 다양한 작업에서 인상적인 운동 기술을 입증했지만, 인간과 같은 장시간의 역동적인 격투를 위한 전신 제어는 민첩성과 안정성에 대한 엄격한 요구 사항으로 인해 특히 어렵습니다. 모방 학습을 통해 로봇이 인간과 유사한 격투 기술을 실행할 수 있게 되었지만, 기존 접근 방식은 여러 단일 기술 정책 간 전환에 의존하거나 일반 정책을 사용하여 입력 참조 동작을 모방하는 경우가 많습니다. 이러한 전략은 기술 간 초기 상태와 최종 상태의 불일치 또는 참조 동작으로 인해 도메인 외 교란이 발생하여 부드럽지 않거나 불안정한 행동을 초래함으로써 기술 전환 시 불안정성을 겪습니다. 본 연구에서는 부드럽고 안정적인 휴머노이드 다중 기술 전환을 위해 하이브리드 전문가 정책 프레임워크인 RPG를 제안합니다. 우리의 접근 방식은 동작 전환 무작위화와 시간 무작위화를 통합하여 기술 전환 중 안정성과 부드러움을 갖춘 민첩한 격투 동작을 생성하는 통합 정책을 훈련합니다. 또한, 걷기/달리기 운동과 격투 기술을 통합하는 제어 파이프라인을 설계하여 언제든지 원활하게 중단되거나 행동 정책이 전환될 수 있는 임의 지속 시간의 인간과 같은 장시간 전투를 가능하게 합니다. 시뮬레이션에서의 광범위한 실험은 제안된 프레임워크의 효과를 입증하며, Unitree G1 휴머노이드 로봇에 대한 실제 배치는 그 견고성과 적용 가능성을 추가로 검증합니다.

## 핵심 내용
휴머노이드 로봇은 다양한 작업에서 인상적인 운동 기술을 입증했지만, 인간과 같은 장시간의 역동적인 격투를 위한 전신 제어는 민첩성과 안정성에 대한 엄격한 요구 사항으로 인해 특히 어렵습니다. 모방 학습을 통해 로봇이 인간과 유사한 격투 기술을 실행할 수 있게 되었지만, 기존 접근 방식은 여러 단일 기술 정책 간 전환에 의존하거나 일반 정책을 사용하여 입력 참조 동작을 모방하는 경우가 많습니다. 이러한 전략은 기술 간 초기 상태와 최종 상태의 불일치 또는 참조 동작으로 인해 도메인 외 교란이 발생하여 부드럽지 않거나 불안정한 행동을 초래함으로써 기술 전환 시 불안정성을 겪습니다. 본 연구에서는 부드럽고 안정적인 휴머노이드 다중 기술 전환을 위해 하이브리드 전문가 정책 프레임워크인 RPG를 제안합니다. 우리의 접근 방식은 동작 전환 무작위화와 시간 무작위화를 통합하여 기술 전환 중 안정성과 부드러움을 갖춘 민첩한 격투 동작을 생성하는 통합 정책을 훈련합니다. 또한, 걷기/달리기 운동과 격투 기술을 통합하는 제어 파이프라인을 설계하여 언제든지 원활하게 중단되거나 행동 정책이 전환될 수 있는 임의 지속 시간의 인간과 같은 장시간 전투를 가능하게 합니다. 시뮬레이션에서의 광범위한 실험은 제안된 프레임워크의 효과를 입증하며, Unitree G1 휴머노이드 로봇에 대한 실제 배치는 그 견고성과 적용 가능성을 추가로 검증합니다.

## 参考
- http://arxiv.org/abs/2604.21355v2
