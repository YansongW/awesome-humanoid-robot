---
$id: ent_paper_physics_models_for_sim_to_real_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
  zh: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
  ko: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
summary:
  en: 'arXiv:2606.28805v2 Announce Type: replace Abstract: At competitive speeds and spins, a table tennis ball follows complex,
    counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement
    learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity
    simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures
    real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling
    inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses
    on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level
    play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact.
    that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we
    model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations.
    For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals
    into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component
    to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping.
    Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces
    prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL
    policies for the first real-world robot table tennis AI agent capable of competing against professional players.'
  zh: 'arXiv:2606.28805v2 Announce Type: replace Abstract: At competitive speeds and spins, a table tennis ball follows complex,
    counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement
    learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity
    simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures
    real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling
    inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses
    on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level
    play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact.
    that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we
    model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations.
    For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals
    into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component
    to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping.
    Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces
    prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL
    policies for the first real-world robot table tennis AI agent capable of competing against professional players.'
  ko: 'arXiv:2606.28805v2 Announce Type: replace Abstract: At competitive speeds and spins, a table tennis ball follows complex,
    counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement
    learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity
    simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures
    real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling
    inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses
    on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level
    play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact.
    that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we
    model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations.
    For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals
    into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component
    to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping.
    Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces
    prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL
    policies for the first real-world robot table tennis AI agent capable of competing against professional players.'
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
- physics_models_for_sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.28805v2.
sources:
- id: src_001
  type: paper
  title: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis (arXiv)
  url: https://arxiv.org/abs/2606.28805
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## 核心内容
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## 参考
- http://arxiv.org/abs/2606.28805v2

## Overview
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model, we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduce prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## Content
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model, we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduce prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## 개요
경쟁적인 속도와 회전에서 탁구공은 복잡하고 직관에 반하는 궤적을 따르며, 로봇은 이를 추적하고 1초 미만의 시간 내에 정밀하게 대응해야 합니다. 이러한 기술을 갖춘 강화 학습 정책을 훈련하는 것은 실제 환경에서 엄청난 비용과 위험이 따르므로, 고충실도 시뮬레이션이 필수적입니다. 그러나 이러한 정책의 전이 가능성은 시뮬레이션이 실제 세계의 역학을 얼마나 충실히 포착하는지에 결정적으로 의존합니다. 이는 게임의 적대적 특성으로 인해 더욱 엄격해지는 요구 사항으로, 모델링의 부정확성은 상대방이 악용할 수 있는 약점이 됩니다. 기존의 로봇 탁구 최신 기술은 일반적으로 제한된 속도와 회전 범위에 초점을 맞추며, 프로 수준의 플레이에서 나타나는 공의 다양한 행동을 포착하지 못합니다. 본 연구에서는 공기 역학적 비행, 공-테이블 접촉, 공-라켓 접촉에 대한 물리 모델을 제시하여, 게임과 관련된 광범위한 속도와 회전 범위에서 공의 행동을 정확히 포착합니다. 구체적으로, 공기 역학 방정식에서 항력 및 마그누스 힘 계수를 레이놀즈 수와 회전 비율의 함수로 모델링합니다. 테이블 접촉 모델의 경우, 공의 좌굴 효과가 반발 계수에 미치는 영향을 모델링하고 잔차를 순간 점 접촉 모델에 통합합니다. 라켓 접촉 모델의 경우, 잔차 신경망 구성 요소를 도입하여 법선 및 접선 반발 계수와 비틀림 회전 감쇠 관련 계수를 보완합니다. 전례 없는 규모의 경기 데이터 세트(277경기)에서 평가된 제안된 모델은 예측 오류를 크게 줄입니다(예: 중간 착지 위치 오류 59% 감소). 결과 모델은 프로 선수와 경쟁할 수 있는 최초의 실제 로봇 탁구 AI 에이전트를 위한 RL 정책을 훈련하는 데 사용되었습니다.

## 핵심 내용
경쟁적인 속도와 회전에서 탁구공은 복잡하고 직관에 반하는 궤적을 따르며, 로봇은 이를 추적하고 1초 미만의 시간 내에 정밀하게 대응해야 합니다. 이러한 기술을 갖춘 강화 학습 정책을 훈련하는 것은 실제 환경에서 엄청난 비용과 위험이 따르므로, 고충실도 시뮬레이션이 필수적입니다. 그러나 이러한 정책의 전이 가능성은 시뮬레이션이 실제 세계의 역학을 얼마나 충실히 포착하는지에 결정적으로 의존합니다. 이는 게임의 적대적 특성으로 인해 더욱 엄격해지는 요구 사항으로, 모델링의 부정확성은 상대방이 악용할 수 있는 약점이 됩니다. 기존의 로봇 탁구 최신 기술은 일반적으로 제한된 속도와 회전 범위에 초점을 맞추며, 프로 수준의 플레이에서 나타나는 공의 다양한 행동을 포착하지 못합니다. 본 연구에서는 공기 역학적 비행, 공-테이블 접촉, 공-라켓 접촉에 대한 물리 모델을 제시하여, 게임과 관련된 광범위한 속도와 회전 범위에서 공의 행동을 정확히 포착합니다. 구체적으로, 공기 역학 방정식에서 항력 및 마그누스 힘 계수를 레이놀즈 수와 회전 비율의 함수로 모델링합니다. 테이블 접촉 모델의 경우, 공의 좌굴 효과가 반발 계수에 미치는 영향을 모델링하고 잔차를 순간 점 접촉 모델에 통합합니다. 라켓 접촉 모델의 경우, 잔차 신경망 구성 요소를 도입하여 법선 및 접선 반발 계수와 비틀림 회전 감쇠 관련 계수를 보완합니다. 전례 없는 규모의 경기 데이터 세트(277경기)에서 평가된 제안된 모델은 예측 오류를 크게 줄입니다(예: 중간 착지 위치 오류 59% 감소). 결과 모델은 프로 선수와 경쟁할 수 있는 최초의 실제 로봇 탁구 AI 에이전트를 위한 RL 정책을 훈련하는 데 사용되었습니다.
