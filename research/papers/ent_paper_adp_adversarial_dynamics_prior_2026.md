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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03454v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (879 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.03454v1

## 개요
기존의 운동 사전 기반 방법은 운동학적 특징을 모방하여 자연스러운 보행을 생성하지만, 동역학적 특징(예: 질량 중심 운동, 접촉력 등)을 직접적으로 제약하지는 못합니다. ADP는 보행 궤적에서 선택된 동역학적 특징을 적대적 정규화의 목표로 추출하고, 궤적 최적화를 활용해 참조 데이터셋을 생성하며, 판별기를 훈련시켜 정책이 생성한 시계열 창이 참조 분포와 일치하는지 평가합니다. 이 방법은 명시적인 운동 추적 없이도 외란을 받더라도 정책 출력이 참조 지지 영역에 가깝게 유지되도록 합니다. 휴머노이드 로봇 실험에서 ADP는 80% 성공 충격 저항 임계값(J80)을 16.7% 향상시키고, 방향 평균 회복 시간을 47.9% 줄였으며, 속도 추적 오차를 35.4% 감소시켰습니다.

## 핵심 내용
### 방법 핵심
- **문제 정의**: 기존 운동 사전 방법(예: AMP)은 운동학적 특징(관절 각도, 속도 등)만 모방하고 동역학적 특징(질량 중심 운동, 질량 중심 운동량, 접촉력, 접촉 상태)을 직접 제약하지 않아 외란 저항 능력이 부족합니다.
- **ADP 프레임워크**:
  - **참조 데이터셋 구축**: 궤적 최적화를 사용해 동역학적 특징을 포함한 보행 궤적을 생성하여 참조 분포로 사용합니다.
  - **판별기 설계**: 판별기를 훈련시켜 정책이 생성한 시계열 창이 참조 분포와 일치하는지 평가하며, 기존의 운동학적 특징 적대적 정규화를 대체합니다.
  - **정책 최적화**: 명시적인 운동 추적 없이 적대적 훈련을 통해 정책 출력이 참조 지지 영역에 가깝게 유지되도록 장려하며, 외부 외란에도 강건성을 유지합니다.

### 실험 설정
- **플랫폼**: 휴머노이드 로봇(구체적인 모델은 초록에 명시되지 않음).
- **기준선**: AMP(Adversarial Motion Priors)와 비교하며, AMP는 가장 강력한 기준선으로 평가됩니다.
- **평가 지표**:
  - 80% 성공 충격 저항 임계값(J80): 외란 저항 능력 측정.
  - 방향 평균 회복 시간: 외란 후 안정적인 보행 복귀에 필요한 시간.
  - 속도 추적 오차: 실제 속도와 목표 속도의 편차.

### 주요 결과
- **충격 저항 능력**: ADP의 J80은 AMP보다 16.7% 향상.
- **회복 시간**: 방향 평균 회복 시간이 47.9% 감소.
- **속도 추적**: 속도 추적 오차가 35.4% 감소.

### 결론
ADP는 동역학적 특징을 직접 정규화함으로써 휴머노이드 로봇 보행 제어의 외란 저항 강건성을 크게 향상시키며, 핵심 지표에서 기존 운동 사전 방법을 전반적으로 능가합니다.
