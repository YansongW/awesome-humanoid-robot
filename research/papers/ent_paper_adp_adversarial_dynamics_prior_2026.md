---
$id: ent_paper_adp_adversarial_dynamics_prior_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion'
  zh: 'ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion'
  ko: 'ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion'
summary:
  en: 'arXiv:2607.03454v1 Announce Type: new Abstract: In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient
    humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion
    features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces,
    and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features
    extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization
    to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent
    with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close
    to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline
    in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged
    recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.'
  zh: 本文提出对抗性动力学先验（ADP），用于抗扰动的仿人机器人行走控制。该方法用轨迹优化构建参考数据集，通过判别器正则化动力学特征（如质心运动、接触力等），替代传统运动学特征模仿。实验表明，ADP在抗冲击能力、恢复时间和速度跟踪误差上显著优于现有最强基线AMP。
  ko: 'arXiv:2607.03454v1 Announce Type: new Abstract: In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient
    humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion
    features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces,
    and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features
    extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization
    to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent
    with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close
    to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline
    in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged
    recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.'
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
- adp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03454v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2607.03454
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有基于运动先验的方法通过模仿运动学特征来生成自然步态，但未能直接约束动力学特征（如质心运动、接触力等）。ADP从行走轨迹中提取选定的动力学特征作为对抗正则化的目标，利用轨迹优化生成参考数据集，并训练判别器评估策略生成的时序窗口是否与参考分布一致。该方法无需显式运动跟踪，即使受到扰动也能使策略输出贴近参考支撑域。在仿人机器人实验中，ADP将80%成功抗冲击阈值（J80）提升16.7%，方向平均恢复时间减少47.9%，速度跟踪误差降低35.4%。

## 核心内容
### 方法核心
- **问题定位**：现有运动先验方法（如AMP）仅模仿运动学特征（关节角度、速度等），未直接约束动力学特征（质心运动、质心动量、接触力、接触状态），导致抗扰动能力不足。
- **ADP框架**：
  - **参考数据集构建**：使用轨迹优化生成包含动力学特征的行走轨迹，作为参考分布。
  - **判别器设计**：训练一个判别器，评估策略生成的时序窗口（temporal windows）是否与参考分布一致，替代传统运动学特征对抗正则化。
  - **策略优化**：无需显式运动跟踪，通过对抗训练鼓励策略输出贴近参考支撑域，即使受到外部扰动也能保持鲁棒性。

### 实验设置
- **平台**：仿人机器人（具体型号未在摘要中说明）。
- **基线**：与AMP（Adversarial Motion Priors）对比，AMP被评估为最强基线。
- **评估指标**：
  - 80%成功抗冲击阈值（J80）：衡量抗扰动能力。
  - 方向平均恢复时间：扰动后恢复稳定行走所需时间。
  - 速度跟踪误差：实际速度与目标速度的偏差。

### 关键结果
- **抗冲击能力**：ADP的J80比AMP提升16.7%。
- **恢复时间**：方向平均恢复时间减少47.9%。
- **速度跟踪**：速度跟踪误差降低35.4%。

### 结论
ADP通过直接正则化动力学特征，显著提升了仿人机器人行走控制的抗扰动鲁棒性，在关键指标上全面超越现有运动先验方法。

## Overview
In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.

## Overview
In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states. To address this limitation, we replace kinematic motion-style features with selected dynamics features extracted from locomotion trajectories as the target of adversarial regularization. To this end, we use trajectory optimization to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent with the resulting reference distribution. Without explicit motion tracking, ADP encourages policy rollouts to remain close to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.

## Content
In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states. To address this limitation, we replace kinematic motion-style features with selected dynamics features extracted from locomotion trajectories as the target of adversarial regularization. To this end, we use trajectory optimization to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent with the resulting reference distribution. Without explicit motion tracking, ADP encourages policy rollouts to remain close to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.

## 개요
본 논문에서는 외란에 강건한 휴머노이드 보행 제어를 위한 적대적 동역학 사전(ADP)을 제안합니다. 기존의 동작 사전 기반 방법은 운동학적 동작 특징을 모방하여 자연스러운 동작 스타일을 유도하지만, CoM 운동, 중심 운동량, 접촉력 및 접촉 상태와 같은 동역학 특징을 직접적으로 정규화하지는 않습니다. 이러한 한계를 해결하기 위해, 우리는 운동학적 동작 스타일 특징을 보행 궤적에서 추출한 선택된 동역학 특징으로 대체하여 적대적 정규화의 대상으로 삼습니다. 이를 위해 궤적 최적화를 사용하여 참조 데이터셋을 구축하고, 정책이 유도하는 시간 창이 결과 참조 분포와 일관성이 있는지 평가하는 판별기를 훈련합니다. 명시적인 동작 추적 없이도 ADP는 정책 롤아웃이 외란 이후에도 참조 지지 영역에 가깝게 유지되도록 장려합니다. 실험 결과, 평가에서 가장 강력한 기준선인 AMP와 비교하여 ADP는 $80\%$ 성공 임펄스 임계값($J_{80}$)을 $16.7\%$ 향상시키고, 방향 평균 회복 시간과 속도 추적 오차를 각각 $47.9\%$ 및 $35.4\%$ 감소시킵니다.

## 핵심 내용
본 논문에서는 외란에 강건한 휴머노이드 보행 제어를 위한 적대적 동역학 사전(ADP)을 제안합니다. 기존의 동작 사전 기반 방법은 운동학적 동작 특징을 모방하여 자연스러운 동작 스타일을 유도하지만, CoM 운동, 중심 운동량, 접촉력 및 접촉 상태와 같은 동역학 특징을 직접적으로 정규화하지는 않습니다. 이러한 한계를 해결하기 위해, 우리는 운동학적 동작 스타일 특징을 보행 궤적에서 추출한 선택된 동역학 특징으로 대체하여 적대적 정규화의 대상으로 삼습니다. 이를 위해 궤적 최적화를 사용하여 참조 데이터셋을 구축하고, 정책이 유도하는 시간 창이 결과 참조 분포와 일관성이 있는지 평가하는 판별기를 훈련합니다. 명시적인 동작 추적 없이도 ADP는 정책 롤아웃이 외란 이후에도 참조 지지 영역에 가깝게 유지되도록 장려합니다. 실험 결과, 평가에서 가장 강력한 기준선인 AMP와 비교하여 ADP는 $80\%$ 성공 임펄스 임계값($J_{80}$)을 $16.7\%$ 향상시키고, 방향 평균 회복 시간과 속도 추적 오차를 각각 $47.9\%$ 및 $35.4\%$ 감소시킵니다.

## 参考
- http://arxiv.org/abs/2607.03454v1
