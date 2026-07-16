---
$id: ent_paper_wei_hmc_learning_heterogeneous_met_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation'
  zh: HMC：面向接触密集型移动操作任务的异构元控制学习
  ko: 'HMC: 접촉이 풍부한 로코 매니퓰레이션을 위한 이종 메타 제어 학습'
summary:
  en: HMC introduces a torque-space meta-controller that continuously blends position, impedance, and hybrid force-position
    actions, learned by a heterogeneous Mixture-of-Experts policy and validated on a Unitree G1 humanoid for contact-rich
    loco-manipulation.
  zh: HMC 提出一种在力矩空间连续融合位置、阻抗和力/位混合控制的异构元控制框架，通过异构混合专家策略学习，并在 Unitree G1 人形机器人上验证了接触密集型移动操作任务。
  ko: HMC는 토크 공간에서 위치, 임피던스, 힘-위치 혼합 제어를 연속적으로 혼합하는 이종 메타 제어 프레임워크를 제안하며, 이종 혼합 전문가 정책으로 학습하고 Unitree G1 휴머노이드에서 접촉이 풍부한 로코
    매니퓰레이션을 검증했다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- loco_manipulation
- contact_rich_manipulation
- force_control
- impedance_control
- hybrid_force_position_control
- mixture_of_experts
- meta_control
- teleoperation
- unitree_g1
- real_world_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14756v1.
sources:
- id: src_001
  type: paper
  title: 'HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation'
  url: https://arxiv.org/abs/2511.14756
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: The paper evaluates the HMC framework on a real Unitree G1 humanoid robot.
    zh: 该论文在真实的 Unitree G1 人形机器人上验证了 HMC 框架。
    ko: 해당 논문은 실제 Unitree G1 휴머노이드 로봇에서 HMC 프레임워크를 평가했다.
---
## 概述
Learning from real-world robot demonstrations holds promise for interacting with complex real-world environments. However, the complexity and variability of interaction dynamics often cause purely positional controllers to struggle with contacts or varying payloads. To address this, we propose a Heterogeneous Meta-Control (HMC) framework for Loco-Manipulation that adaptively stitches multiple control modalities: position, impedance, and hybrid force-position. We first introduce an interface, HMC-Controller, for blending actions from different control profiles continuously in the torque space. HMC-Controller facilitates both teleoperation and policy deployment. Then, to learn a robust force-aware policy, we propose HMC-Policy to unify different controllers into a heterogeneous architecture. We adopt a mixture-of-experts style routing to learn from large-scale position-only data and fine-grained force-aware demonstrations. Experiments on a real humanoid robot show over 50% relative improvement vs. baselines on challenging tasks such as compliant table wiping and drawer opening, demonstrating the efficacy of HMC.

## 核心内容
Learning from real-world robot demonstrations holds promise for interacting with complex real-world environments. However, the complexity and variability of interaction dynamics often cause purely positional controllers to struggle with contacts or varying payloads. To address this, we propose a Heterogeneous Meta-Control (HMC) framework for Loco-Manipulation that adaptively stitches multiple control modalities: position, impedance, and hybrid force-position. We first introduce an interface, HMC-Controller, for blending actions from different control profiles continuously in the torque space. HMC-Controller facilitates both teleoperation and policy deployment. Then, to learn a robust force-aware policy, we propose HMC-Policy to unify different controllers into a heterogeneous architecture. We adopt a mixture-of-experts style routing to learn from large-scale position-only data and fine-grained force-aware demonstrations. Experiments on a real humanoid robot show over 50% relative improvement vs. baselines on challenging tasks such as compliant table wiping and drawer opening, demonstrating the efficacy of HMC.

## 参考
- http://arxiv.org/abs/2511.14756v1

## Overview
Learning from real-world robot demonstrations holds promise for interacting with complex real-world environments. However, the complexity and variability of interaction dynamics often cause purely positional controllers to struggle with contacts or varying payloads. To address this, we propose a Heterogeneous Meta-Control (HMC) framework for Loco-Manipulation that adaptively stitches multiple control modalities: position, impedance, and hybrid force-position. We first introduce an interface, HMC-Controller, for blending actions from different control profiles continuously in the torque space. HMC-Controller facilitates both teleoperation and policy deployment. Then, to learn a robust force-aware policy, we propose HMC-Policy to unify different controllers into a heterogeneous architecture. We adopt a mixture-of-experts style routing to learn from large-scale position-only data and fine-grained force-aware demonstrations. Experiments on a real humanoid robot show over 50% relative improvement vs. baselines on challenging tasks such as compliant table wiping and drawer opening, demonstrating the efficacy of HMC.

## Content
Learning from real-world robot demonstrations holds promise for interacting with complex real-world environments. However, the complexity and variability of interaction dynamics often cause purely positional controllers to struggle with contacts or varying payloads. To address this, we propose a Heterogeneous Meta-Control (HMC) framework for Loco-Manipulation that adaptively stitches multiple control modalities: position, impedance, and hybrid force-position. We first introduce an interface, HMC-Controller, for blending actions from different control profiles continuously in the torque space. HMC-Controller facilitates both teleoperation and policy deployment. Then, to learn a robust force-aware policy, we propose HMC-Policy to unify different controllers into a heterogeneous architecture. We adopt a mixture-of-experts style routing to learn from large-scale position-only data and fine-grained force-aware demonstrations. Experiments on a real humanoid robot show over 50% relative improvement vs. baselines on challenging tasks such as compliant table wiping and drawer opening, demonstrating the efficacy of HMC.

## 개요
실제 로봇 시연으로부터 학습하는 것은 복잡한 실제 환경과 상호작용하는 데 유망한 접근 방식입니다. 그러나 상호작용 동역학의 복잡성과 가변성으로 인해 순수 위치 기반 제어기는 접촉이나 다양한 페이로드 상황에서 어려움을 겪는 경우가 많습니다. 이를 해결하기 위해, 우리는 위치, 임피던스, 하이브리드 힘-위치 등 여러 제어 방식을 적응적으로 결합하는 Loco-Manipulation을 위한 이종 메타 제어(HMC) 프레임워크를 제안합니다. 먼저, 다양한 제어 프로파일의 동작을 토크 공간에서 연속적으로 혼합하는 인터페이스인 HMC-Controller를 소개합니다. HMC-Controller는 원격 조작과 정책 배포를 모두 용이하게 합니다. 다음으로, 강건한 힘 인식 정책을 학습하기 위해, 서로 다른 제어기를 이종 아키텍처로 통합하는 HMC-Policy를 제안합니다. 우리는 대규모 위치 전용 데이터와 세밀한 힘 인식 시연으로부터 학습하기 위해 전문가 혼합 스타일의 라우팅을 채택합니다. 실제 휴머노이드 로봇 실험에서, 순응적인 테이블 닦기와 서랍 열기와 같은 까다로운 작업에서 기준선 대비 50% 이상의 상대적 개선을 보여주며 HMC의 효용성을 입증했습니다.

## 핵심 내용
실제 로봇 시연으로부터 학습하는 것은 복잡한 실제 환경과 상호작용하는 데 유망한 접근 방식입니다. 그러나 상호작용 동역학의 복잡성과 가변성으로 인해 순수 위치 기반 제어기는 접촉이나 다양한 페이로드 상황에서 어려움을 겪는 경우가 많습니다. 이를 해결하기 위해, 우리는 위치, 임피던스, 하이브리드 힘-위치 등 여러 제어 방식을 적응적으로 결합하는 Loco-Manipulation을 위한 이종 메타 제어(HMC) 프레임워크를 제안합니다. 먼저, 다양한 제어 프로파일의 동작을 토크 공간에서 연속적으로 혼합하는 인터페이스인 HMC-Controller를 소개합니다. HMC-Controller는 원격 조작과 정책 배포를 모두 용이하게 합니다. 다음으로, 강건한 힘 인식 정책을 학습하기 위해, 서로 다른 제어기를 이종 아키텍처로 통합하는 HMC-Policy를 제안합니다. 우리는 대규모 위치 전용 데이터와 세밀한 힘 인식 시연으로부터 학습하기 위해 전문가 혼합 스타일의 라우팅을 채택합니다. 실제 휴머노이드 로봇 실험에서, 순응적인 테이블 닦기와 서랍 열기와 같은 까다로운 작업에서 기준선 대비 50% 이상의 상대적 개선을 보여주며 HMC의 효용성을 입증했습니다.
