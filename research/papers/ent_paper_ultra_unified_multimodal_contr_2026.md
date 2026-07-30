---
$id: ent_paper_ultra_unified_multimodal_contr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation'
  zh: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation'
  ko: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation'
summary:
  en: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: ULTRA 是一个面向人形机器人全身移动操作任务的统一多模态控制框架，由研究团队于 2026 年提出。其核心贡献在于提出物理驱动的神经重定向算法，将大规模动作捕捉数据转化为物理合理的人形机器人运动，并训练统一多模态控制器，支持从精确状态到嘈杂视觉输入的多传感模式，最终实现从稀疏任务意图直接生成全身行为，无需测试时的参考运动。
  ko: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- loco_manipulation
- ultra
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.03279v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation (arXiv)'
  url: https://arxiv.org/abs/2603.03279
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation project page'
  url: https://ultra-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有的人形机器人全身移动操作研究受限于数据稀缺、技能规模难以扩展以及依赖预定义运动参考等问题。ULTRA 框架通过两个关键组件解决这些挑战：一是物理驱动的神经重定向算法，用于将大规模动作捕捉数据转化为物理合理的人形机器人运动，尤其适用于接触丰富的交互场景；二是统一多模态控制器，该控制器通过蒸馏通用跟踪策略、将运动技能压缩至紧凑潜在空间，并利用强化学习微调来提升覆盖范围与鲁棒性。ULTRA 在仿真与真实 Unitree G1 人形机器人上进行了评估，结果表明其能够从自我中心感知出发，泛化至自主、目标导向的全身移动操作任务，性能持续优于仅依赖有限技能的跟踪基线。

## 核心内容
### 方法架构
ULTRA 框架包含两个核心组件：
- **物理驱动的神经重定向算法**：将大规模动作捕捉数据转换为适用于人形机器人本体的运动，通过物理约束确保接触丰富的交互场景中的运动合理性。
- **统一多模态控制器**：支持从精确的运动捕捉状态到嘈杂的自我中心视觉输入等多种传感模式，同时兼容密集参考信号与稀疏任务规格。

### 训练流程
1. **蒸馏通用跟踪策略**：将跟踪策略的知识迁移至统一控制器。
2. **压缩运动技能**：将多种运动技能编码至紧凑的潜在空间。
3. **强化学习微调**：扩展技能覆盖范围，提升在分布外场景下的鲁棒性。

### 实验设置与结果
- **平台**：仿真环境与真实 Unitree G1 人形机器人。
- **任务**：自主、目标导向的全身移动操作，基于自我中心感知。
- **关键发现**：ULTRA 能够从稀疏意图直接生成协调的全身行为，无需测试时的参考运动。在多种场景下，其性能显著优于仅依赖有限技能的跟踪基线方法。

## Overview
Achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful. Yet existing approaches are fundamentally constrained: retargeted data are often scarce or low-quality; methods struggle to scale to large skill repertoires; and, most importantly, they rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications. To address these limitations, we propose ULTRA, a unified framework with two key components. First, we introduce a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions. Second, we learn a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. We distill a universal tracking policy into this controller, compress motor skills into a compact latent space, and apply reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios. This enables coordinated whole-body behavior from sparse intent without test-time reference motions. We evaluate ULTRA in simulation and on a real Unitree G1 humanoid. Results show that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

## 개요
인간형 로봇을 실용적으로 만드는 데 있어 자율적이고 다재다능한 전신 이동-조작 능력을 달성하는 것은 여전히 핵심적인 장벽으로 남아 있습니다. 그러나 기존 접근 방식은 근본적인 한계를 가지고 있습니다. 리타겟팅된 데이터는 종종 부족하거나 품질이 낮으며, 방법론은 다양한 기술 레퍼토리로 확장하는 데 어려움을 겪고, 가장 중요하게는 인식 및 고수준 작업 사양에서 행동을 생성하는 대신 미리 정의된 동작 참조를 추적하는 데 의존합니다. 이러한 한계를 해결하기 위해 우리는 두 가지 핵심 구성 요소를 가진 통합 프레임워크인 ULTRA를 제안합니다. 첫째, 접촉이 많은 상호작용에서 물리적 타당성을 유지하면서 대규모 모션 캡처를 인간형 로봇 구현체로 변환하는 물리 기반 신경 리타겟팅 알고리즘을 소개합니다. 둘째, 정확한 모션 캡처 상태에서 노이즈가 있는 자기중심적 시각 입력에 이르는 감각 하에서 밀집 참조와 희소 작업 사양을 모두 지원하는 통합 다중 모드 컨트롤러를 학습합니다. 우리는 이 컨트롤러에 보편적 추적 정책을 증류하고, 모터 기술을 컴팩트한 잠재 공간으로 압축하며, 강화 학습 미세 조정을 적용하여 적용 범위를 확장하고 분포 외 시나리오에서의 견고성을 향상시킵니다. 이를 통해 테스트 시 참조 동작 없이 희소 의도로부터 조정된 전신 행동이 가능해집니다. 우리는 시뮬레이션과 실제 Unitree G1 인간형 로봇에서 ULTRA를 평가합니다. 결과는 ULTRA가 자기중심적 인식으로부터 자율적이고 목표 조건화된 전신 이동-조작으로 일반화되며, 제한된 기술을 가진 추적 전용 기준선을 일관되게 능가함을 보여줍니다.

## 핵심 내용
인간형 로봇을 실용적으로 만드는 데 있어 자율적이고 다재다능한 전신 이동-조작 능력을 달성하는 것은 여전히 핵심적인 장벽으로 남아 있습니다. 그러나 기존 접근 방식은 근본적인 한계를 가지고 있습니다. 리타겟팅된 데이터는 종종 부족하거나 품질이 낮으며, 방법론은 다양한 기술 레퍼토리로 확장하는 데 어려움을 겪고, 가장 중요하게는 인식 및 고수준 작업 사양에서 행동을 생성하는 대신 미리 정의된 동작 참조를 추적하는 데 의존합니다. 이러한 한계를 해결하기 위해 우리는 두 가지 핵심 구성 요소를 가진 통합 프레임워크인 ULTRA를 제안합니다. 첫째, 접촉이 많은 상호작용에서 물리적 타당성을 유지하면서 대규모 모션 캡처를 인간형 로봇 구현체로 변환하는 물리 기반 신경 리타겟팅 알고리즘을 소개합니다. 둘째, 정확한 모션 캡처 상태에서 노이즈가 있는 자기중심적 시각 입력에 이르는 감각 하에서 밀집 참조와 희소 작업 사양을 모두 지원하는 통합 다중 모드 컨트롤러를 학습합니다. 우리는 이 컨트롤러에 보편적 추적 정책을 증류하고, 모터 기술을 컴팩트한 잠재 공간으로 압축하며, 강화 학습 미세 조정을 적용하여 적용 범위를 확장하고 분포 외 시나리오에서의 견고성을 향상시킵니다. 이를 통해 테스트 시 참조 동작 없이 희소 의도로부터 조정된 전신 행동이 가능해집니다. 우리는 시뮬레이션과 실제 Unitree G1 인간형 로봇에서 ULTRA를 평가합니다. 결과는 ULTRA가 자기중심적 인식으로부터 자율적이고 목표 조건화된 전신 이동-조작으로 일반화되며, 제한된 기술을 가진 추적 전용 기준선을 일관되게 능가함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2603.03279v1
