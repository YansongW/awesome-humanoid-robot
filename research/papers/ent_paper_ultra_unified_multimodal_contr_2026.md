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
  zh: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.03279v1.
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
Achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful. Yet existing approaches are fundamentally constrained: retargeted data are often scarce or low-quality; methods struggle to scale to large skill repertoires; and, most importantly, they rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications. To address these limitations, we propose ULTRA, a unified framework with two key components. First, we introduce a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions. Second, we learn a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. We distill a universal tracking policy into this controller, compress motor skills into a compact latent space, and apply reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios. This enables coordinated whole-body behavior from sparse intent without test-time reference motions. We evaluate ULTRA in simulation and on a real Unitree G1 humanoid. Results show that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

## 核心内容
Achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful. Yet existing approaches are fundamentally constrained: retargeted data are often scarce or low-quality; methods struggle to scale to large skill repertoires; and, most importantly, they rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications. To address these limitations, we propose ULTRA, a unified framework with two key components. First, we introduce a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions. Second, we learn a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. We distill a universal tracking policy into this controller, compress motor skills into a compact latent space, and apply reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios. This enables coordinated whole-body behavior from sparse intent without test-time reference motions. We evaluate ULTRA in simulation and on a real Unitree G1 humanoid. Results show that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

## 参考
- http://arxiv.org/abs/2603.03279v1

## Overview
Achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful. Yet existing approaches are fundamentally constrained: retargeted data are often scarce or low-quality; methods struggle to scale to large skill repertoires; and, most importantly, they rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications. To address these limitations, we propose ULTRA, a unified framework with two key components. First, we introduce a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions. Second, we learn a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. We distill a universal tracking policy into this controller, compress motor skills into a compact latent space, and apply reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios. This enables coordinated whole-body behavior from sparse intent without test-time reference motions. We evaluate ULTRA in simulation and on a real Unitree G1 humanoid. Results show that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

## Content
Achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful. Yet existing approaches are fundamentally constrained: retargeted data are often scarce or low-quality; methods struggle to scale to large skill repertoires; and, most importantly, they rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications. To address these limitations, we propose ULTRA, a unified framework with two key components. First, we introduce a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions. Second, we learn a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. We distill a universal tracking policy into this controller, compress motor skills into a compact latent space, and apply reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios. This enables coordinated whole-body behavior from sparse intent without test-time reference motions. We evaluate ULTRA in simulation and on a real Unitree G1 humanoid. Results show that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

## 개요
인간형 로봇을 실용적으로 만드는 데 있어 자율적이고 다재다능한 전신 이동-조작 능력을 달성하는 것은 여전히 핵심적인 장벽으로 남아 있습니다. 그러나 기존 접근 방식은 근본적인 한계를 가지고 있습니다. 리타겟팅된 데이터는 종종 부족하거나 품질이 낮으며, 방법론은 다양한 기술 레퍼토리로 확장하는 데 어려움을 겪고, 가장 중요하게는 인식 및 고수준 작업 사양에서 행동을 생성하는 대신 미리 정의된 동작 참조를 추적하는 데 의존합니다. 이러한 한계를 해결하기 위해 우리는 두 가지 핵심 구성 요소를 가진 통합 프레임워크인 ULTRA를 제안합니다. 첫째, 접촉이 많은 상호작용에서 물리적 타당성을 유지하면서 대규모 모션 캡처를 인간형 로봇 구현체로 변환하는 물리 기반 신경 리타겟팅 알고리즘을 소개합니다. 둘째, 정확한 모션 캡처 상태에서 노이즈가 있는 자기중심적 시각 입력에 이르는 감각 하에서 밀집 참조와 희소 작업 사양을 모두 지원하는 통합 다중 모드 컨트롤러를 학습합니다. 우리는 이 컨트롤러에 보편적 추적 정책을 증류하고, 모터 기술을 컴팩트한 잠재 공간으로 압축하며, 강화 학습 미세 조정을 적용하여 적용 범위를 확장하고 분포 외 시나리오에서의 견고성을 향상시킵니다. 이를 통해 테스트 시 참조 동작 없이 희소 의도로부터 조정된 전신 행동이 가능해집니다. 우리는 시뮬레이션과 실제 Unitree G1 인간형 로봇에서 ULTRA를 평가합니다. 결과는 ULTRA가 자기중심적 인식으로부터 자율적이고 목표 조건화된 전신 이동-조작으로 일반화되며, 제한된 기술을 가진 추적 전용 기준선을 일관되게 능가함을 보여줍니다.

## 핵심 내용
인간형 로봇을 실용적으로 만드는 데 있어 자율적이고 다재다능한 전신 이동-조작 능력을 달성하는 것은 여전히 핵심적인 장벽으로 남아 있습니다. 그러나 기존 접근 방식은 근본적인 한계를 가지고 있습니다. 리타겟팅된 데이터는 종종 부족하거나 품질이 낮으며, 방법론은 다양한 기술 레퍼토리로 확장하는 데 어려움을 겪고, 가장 중요하게는 인식 및 고수준 작업 사양에서 행동을 생성하는 대신 미리 정의된 동작 참조를 추적하는 데 의존합니다. 이러한 한계를 해결하기 위해 우리는 두 가지 핵심 구성 요소를 가진 통합 프레임워크인 ULTRA를 제안합니다. 첫째, 접촉이 많은 상호작용에서 물리적 타당성을 유지하면서 대규모 모션 캡처를 인간형 로봇 구현체로 변환하는 물리 기반 신경 리타겟팅 알고리즘을 소개합니다. 둘째, 정확한 모션 캡처 상태에서 노이즈가 있는 자기중심적 시각 입력에 이르는 감각 하에서 밀집 참조와 희소 작업 사양을 모두 지원하는 통합 다중 모드 컨트롤러를 학습합니다. 우리는 이 컨트롤러에 보편적 추적 정책을 증류하고, 모터 기술을 컴팩트한 잠재 공간으로 압축하며, 강화 학습 미세 조정을 적용하여 적용 범위를 확장하고 분포 외 시나리오에서의 견고성을 향상시킵니다. 이를 통해 테스트 시 참조 동작 없이 희소 의도로부터 조정된 전신 행동이 가능해집니다. 우리는 시뮬레이션과 실제 Unitree G1 인간형 로봇에서 ULTRA를 평가합니다. 결과는 ULTRA가 자기중심적 인식으로부터 자율적이고 목표 조건화된 전신 이동-조작으로 일반화되며, 제한된 기술을 가진 추적 전용 기준선을 일관되게 능가함을 보여줍니다.
