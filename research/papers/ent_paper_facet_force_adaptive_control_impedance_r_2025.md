---
$id: ent_paper_facet_force_adaptive_control_impedance_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots'
  zh: 'FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots'
  ko: 'FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots'
summary:
  en: Reinforcement learning (RL) has made significant strides in legged robot control, enabling locomotion across diverse
    terrains and complex loco-manipulation capabilities. However, the commonly used position or velocity tracking-based objectives
    are agnostic to forces experienced by the robot, leading to stiff and potentially dangerous behaviors and poor control
    during forceful interactions. To.
  zh: FACET 提出一种基于阻抗参考跟踪的力自适应控制框架，用于腿式机器人。它通过虚拟质量-弹簧-阻尼模型定义参考动力学，并利用强化学习训练策略跟踪该参考，从而将外力响应从隐式、僵硬的行为转变为显式、可调节的顺应性。核心贡献在于提供了一种原理性的力控制接口，并在仿真和真实机器人上验证了其鲁棒性和可调节性。
  ko: Reinforcement learning (RL) has made significant strides in legged robot control, enabling locomotion across diverse
    terrains and complex loco-manipulation capabilities. However, the commonly used position or velocity tracking-based objectives
    are agnostic to forces experienced by the robot, leading to stiff and potentially dangerous behaviors and poor control
    during forceful interactions. To.
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
- facet
- force
- adaptive
- control
- impedance
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P084. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2505.06883 FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots'
  url: https://arxiv.org/abs/2505.06883
  date: '2025-05-11'
  accessed_at: '2026-08-05'
---

## 概述

FACET 提出一种基于阻抗参考跟踪的力自适应控制框架，用于腿式机器人。它通过虚拟质量-弹簧-阻尼模型定义参考动力学，并利用强化学习训练策略跟踪该参考，从而将外力响应从隐式、僵硬的行为转变为显式、可调节的顺应性。核心贡献在于提供了一种原理性的力控制接口，并在仿真和真实机器人上验证了其鲁棒性和可调节性。

## 它改变了什么

现有基于 RL 的腿式机器人控制器，无论是速度跟踪还是操作任务，其奖励函数都未明确指定对外力的响应。速度跟踪策略会本能地拒绝一切外力，导致运动僵硬；操作策略则假设力可忽略，在真实交互中行为未定义。这从根本上限制了机器人在人类密集环境中的安全性和可用性。FACET 改变了这一范式：它不再将外力视为需要抑制的干扰，而是将其作为参考动力学的一部分，通过阻抗参数显式地“设计”机器人的外力响应。这使得力交互行为从不可控的副作用，转变为可调节、可预测的核心功能。

## 方法拆解

### 核心架构
FACET 采用教师-学生框架，学生策略仅依赖可部署的观测（命令、关节状态、IMU），教师策略额外使用特权信息（线速度、外力、接触状态等）。学生策略以教师参数初始化，并用 PPO 继续训练，而非单纯模仿。

### 参考模型
机器人行为由虚拟质量-弹簧-阻尼系统定义，其动力学为：
`m * ẍ_ref = K_p(x_des - x_ref) + K_d(ẋ_des - ẋ_ref) + f_ext`
其中 `u = (x_des, K_p, K_d, m)` 是策略输入，`f_ext` 是外部力。策略的目标是让机器人实际状态 `x_sim` 跟踪 `x_ref`，损失函数为 `L_track = ||x_sim - x_ref||² + ||ẋ_sim - ẋ_ref||²`。

### 时间平滑
为避免参考轨迹的噪声和不连续性，使用从不同历史时间步 `t' ∈ {t-8Δt, t-16Δt, t-32Δt}` 积分得到的混合目标，`Δt = 0.02s`。奖励函数为 `r_t = (1/M) Σ exp(-||x_sim - x_ref^{t'}||²) + exp(-||ẋ_sim - ẋ_ref^{t'}||²)`。

### 力接口
通过设置阻抗参数实现不同力行为：`K_p=0` 时完全柔顺，可被外力引导；增大 `K_p` 则刚度增加。对于移动操作器，为基座和末端执行器分别定义参考模型，参数 `a ∈ [0,1]` 控制末端力是否传递到基座。

## 关键创新

1.  **原理性力响应设计**：与现有方法要么忽略外力、要么需要显式切换力/位置模式不同，FACET 通过阻抗参数连续调节顺应性，提供了一个统一的、可微调的力控制接口。这是首次将阻抗控制思想与 RL 训练目标深度耦合。
2.  **间接力命令**：策略不直接输出力或速度，而是输出阻抗参数 `u`。这允许用户通过直观的物理量（如刚度、阻尼、虚拟质量）指定期望行为，例如设置 `K_p=0` 即可让机器人被绳子轻松拉动。
3.  **时间平滑的参考跟踪**：通过混合多个历史时间步的参考目标，解决了 RL 训练中参考轨迹噪声大、难以精确跟踪的问题，显著提升了训练的稳定性和最终策略的平滑性。

## 实验与结果

### 仿真实验
- **大扰动鲁棒性**：在 `1.5 m/s` 前进时施加横向冲量，FACET 成功率显著高于速度跟踪和随机扰动基线。
- **软碰撞**：机器人以 `1.5 m/s` 走入虚拟墙，FACET 的碰撞冲量显著更低，且可通过调节 `K_p` 控制。
- **消融研究**：比较平滑、开环、闭环、加速度四种教师策略及对应学生策略。

| 策略 | 位置误差 | 速度误差 | 成功率 |
|------|---------|---------|-------|
| 平滑教师 | 1.00 | 1.00 | 0.98 |
| 开环教师 | 0.72 | 0.92 | 0.97 |
| 闭环教师 | 17.71 | 2.04 | 0.96 |
| 加速度教师 | 70.51 | 6.64 | 0.97 |
| 平滑学生 | 5.18 | 1.85 | 0.97 |
| 开环学生 | 10.31 | 2.07 | 0.98 |
| 并发基线 | 26.23 | 3.53 | 0.92 |

平滑教师误差最小，开环学生优于闭环学生，确认了时间平滑和积分目标的重要性。

### 真实世界实验
- **柔顺跟随**：设置 `K_p=0, K_d=4`，机器人可被细绳轻拉或指尖推动启停，无显式速度指令时平滑跟随力方向。
- **大力拉拽**：内置控制器成功拉动至 `2.5 kg`，鲁棒策略超过 `5 kg` 失败，FACET 可靠拉动至 `10 kg` 无失败。

## 边界与局限

论文未明确提及所有局限，但基于事实要点可推断：直接测量身体速度和外部力在现实中不可用，参考模型在现实中也不可用。可靠感知 `f_ext` 不可行，因大多数机器人缺乏力传感器。实现式2的动力学需要控制机器人通过脚接触产生 `f_grf` 以匹配虚拟弹簧力，但因复杂接触动力学而具有挑战性。多体设置下，机械约束未考虑，末端执行器参考目标可能不可达。此外，使用预定义频率的振荡器控制步态，可能限制基于目标加速度和速度调整立足点的能力。

## 工程启示

复现时需注意：策略在 IsaacLab 中用 PPO 训练，控制间隔 `Δt = 0.02s`，时间平滑使用 `t' ∈ {t-8Δt, t-16Δt, t-32Δt}`。训练期间采样各种命令和外部力分布，并应用域随机化。最关键的工程细节是时间平滑的实现，它直接决定了训练稳定性。部署时，由于多数情况无明确定义的世界系，需在机器人系中按固定目标速度模式或完全柔顺模式指定 `x_des`。大力拉拽实验中，逐渐增大 `K_p` 和设定点位移，使 `K_p(x_ref-x)` 增至 `100 N`。最容易踩坑的地方是奖励函数中 `exp(-||ẋ-ẋ_ref||²)` 形式在早期误差大时可能饱和，需添加二次成本项 `-||ẋ-ẋ_ref||²` 解决。

## Overview
Reinforcement learning (RL) has made significant strides in legged robot control, enabling locomotion across diverse terrains and complex loco-manipulation capabilities. However, the commonly used position or velocity tracking-based objectives are agnostic to forces experienced by the robot, leading to stiff and potentially dangerous behaviors and poor control during forceful interactions. To address this limitation, we present \emph{Force-Adaptive Control via Impedance Reference Tracking} (FACET). Inspired by impedance control, we use RL to train a control policy to imitate a virtual mass-spring-damper system, allowing fine-grained control under external forces by manipulating the virtual spring. In simulation, we demonstrate that our quadruped robot achieves improved robustness to large impulses (up to 200 Ns) and exhibits controllable compliance, achieving an 80% reduction in collision impulse. The policy is deployed to a physical robot to showcase both compliance and the ability to engage with large forces by kinesthetic control and pulling payloads up to 2/3 of its weight. Further extension to a legged loco-manipulator and a humanoid shows the applicability of our method to more complex settings to enable whole-body compliance control. Project Website: https://facet.pages.dev/

## 参考
- https://arxiv.org/abs/2505.06883

## 개요

FACET는 다리형 로봇을 위한 임피던스 기준 추적 기반 힘 적응 제어 프레임워크를 제안한다. 가상 질량-스프링-댐퍼 모델로 기준 동역학을 정의하고, 강화 학습으로 해당 기준을 추적하는 정책을 훈련시켜 외부 힘에 대한 반응을 암시적이고 경직된 행동에서 명시적이고 조절 가능한 순응성으로 전환한다. 핵심 기여는 원리 기반의 힘 제어 인터페이스를 제공하고, 시뮬레이션과 실제 로봇에서 견고성과 조절 가능성을 검증한 것이다.

## 무엇을 바꾸었는가

기존 RL 기반 다리형 로봇 제어기는 속도 추적이든 조작 작업이든 보상 함수가 외부 힘에 대한 반응을 명시적으로 지정하지 않았다. 속도 추적 정책은 모든 외부 힘을 본능적으로 거부하여 움직임이 경직되고, 조작 정책은 힘이 무시 가능하다고 가정하여 실제 상호작용에서 행동이 정의되지 않는다. 이는 인간 밀집 환경에서 로봇의 안전성과 유용성을 근본적으로 제한한다. FACET는 이러한 패러다임을 바꾼다: 외부 힘을 억제해야 할 교란으로 보지 않고, 기준 동역학의 일부로 간주하여 임피던스 파라미터를 통해 로봇의 외부 힘 반응을 명시적으로 "설계"한다. 이를 통해 힘 상호작용 행동이 통제 불가능한 부작용에서 조절 가능하고 예측 가능한 핵심 기능으로 전환된다.

## 방법 분해

### 핵심 아키텍처
FACET는 교사-학생 프레임워크를 사용하며, 학생 정책은 배포 가능한 관측(명령, 관절 상태, IMU)만 사용하고, 교사 정책은 추가로 특권 정보(선속도, 외부 힘, 접촉 상태 등)를 사용한다. 학생 정책은 교사 파라미터로 초기화되고 단순 모방이 아닌 PPO로 계속 훈련된다.

### 기준 모델
로봇 행동은 가상 질량-스프링-댐퍼 시스템으로 정의되며, 그 동역학은 다음과 같다:
`m * ẍ_ref = K_p(x_des - x_ref) + K_d(ẋ_des - ẋ_ref) + f_ext`
여기서 `u = (x_des, K_p, K_d, m)`는 정책 입력이고, `f_ext`는 외부 힘이다. 정책의 목표는 로봇의 실제 상태 `x_sim`이 `x_ref`를 추적하도록 하는 것이며, 손실 함수는 `L_track = ||x_sim - x_ref||² + ||ẋ_sim - ẋ_ref||²`이다.

### 시간 평활화
기준 궤적의 노이즈와 불연속성을 피하기 위해, 서로 다른 과거 시간 스텝 `t' ∈ {t-8Δt, t-16Δt, t-32Δt}`에서 적분된 혼합 목표를 사용하며, `Δt = 0.02s`이다. 보상 함수는 `r_t = (1/M) Σ exp(-||x_sim - x_ref^{t'}||²) + exp(-||ẋ_sim - ẋ_ref^{t'}||²)`이다.

### 힘 인터페이스
임피던스 파라미터 설정을 통해 다양한 힘 행동을 구현한다: `K_p=0`일 때 완전 순응하여 외부 힘에 의해 유도될 수 있고, `K_p`를 증가시키면 강성이 증가한다. 이동 조작기의 경우 베이스와 엔드 이펙터 각각에 대해 기준 모델을 정의하며, 파라미터 `a ∈ [0,1]`는 엔드 이펙터 힘이 베이스로 전달되는지 여부를 제어한다.

## 핵심 혁신

1.  **원리 기반 힘 응답 설계**: 기존 방법이 외부 힘을 무시하거나 힘/위치 모드를 명시적으로 전환해야 하는 것과 달리, FACET는 임피던스 파라미터를 통해 순응성을 연속적으로 조절하여 통합적이고 미세 조정 가능한 힘 제어 인터페이스를 제공한다. 임피던스 제어 개념을 RL 훈련 목표와 깊게 결합한 최초의 사례이다.
2.  **간접 힘 명령**: 정책은 힘이나 속도를 직접 출력하지 않고 임피던스 파라미터 `u`를 출력한다. 이를 통해 사용자는 강성, 댐핑, 가상 질량과 같은 직관적인 물리량으로 원하는 행동을 지정할 수 있다. 예를 들어 `K_p=0`으로 설정하면 로봇이 줄에 의해 쉽게 끌려갈 수 있다.
3.  **시간 평활화된 기준 추적**: 여러 과거 시간 스텝의 기준 목표를 혼합함으로써 RL 훈련에서 기준 궤적의 노이즈가 크고 정밀 추적이 어려운 문제를 해결하여 훈련 안정성과 최종 정책의 평활성을 크게 향상시킨다.

## 실험 및 결과

### 시뮬레이션 실험
- **대형 교란 견고성**: `1.5 m/s` 전진 시 횡방향 충격량을 가했을 때, FACET의 성공률이 속도 추적 및 무작위 교란 기준선보다 유의미하게 높았다.
- **연성 충돌**: 로봇이 `1.5 m/s`로 가상 벽에 들어갈 때, FACET의 충돌 충격량이 유의미하게 낮았고, `K_p` 조절로 제어 가능했다.
- **절제 연구**: 평활화, 개루프, 폐루프, 가속도 네 가지 교사 정책 및 해당 학생 정책을 비교했다.

| 정책 | 위치 오차 | 속도 오차 | 성공률 |
|------|---------|---------|-------|
| 평활화 교사 | 1.00 | 1.00 | 0.98 |
| 개루프 교사 | 0.72 | 0.92 | 0.97 |
| 폐루프 교사 | 17.71 | 2.04 | 0.96 |
| 가속도 교사 | 70.51 | 6.64 | 0.97 |
| 평활화 학생 | 5.18 | 1.85 | 0.97 |
| 개루프 학생 | 10.31 | 2.07 | 0.98 |
| 동시 기준선 | 26.23 | 3.53 | 0.92 |

평활화 교사가 오차가 가장 작았고, 개루프 학생이 폐루프 학생보다 우수하여 시간 평활화와 적분 목표의 중요성을 확인했다.

### 실제 세계 실험
- **순응 추종**: `K_p=0, K_d=4`로 설정하면 로봇이 가는 줄로 가볍게 당기거나 손끝으로 밀어서 시작/정지할 수 있으며, 명시적 속도 명령 없이 힘 방향을 따라 부드럽게 움직인다.
- **강한 당김**: 내장 제어기는 `2.5 kg`까지 성공적으로 당겼고, 견고한 정책은 `5 kg` 초과 시 실패했으며, FACET는 `10 kg`까지 안정적으로 당겼다.

## 경계 및 한계

논문은 모든 한계를 명시적으로 언급하지 않았지만, 사실적 요점을 기반으로 추론할 수 있다: 신체 속도와 외부 힘의 직접 측정은 현실에서 사용 불가능하며, 기준 모델도 현실에서 사용 불가능하다. `f_ext`의 신뢰할 수 있는 인식은 대부분의 로봇에 힘 센서가 없어 불가능하다. 식 2의 동역학을 구현하려면 로봇이 발 접촉을 통해 `f_grf`를 생성하여 가상 스프링 힘을 일치시켜야 하지만, 복잡한 접촉 동역학으로 인해 어렵다. 다물체 설정에서는 기계적 구속이 고려되지 않아 엔드 이펙터 기준 목표가 도달 불가능할 수 있다. 또한, 사전 정의된 주파수의 발진기로 보행을 제어하여 목표 가속도와 속도에 기반한 발 디딤 위치 조정 능력을 제한할 수 있다.

## 공학적 시사점

재현 시 주의할 점: 정책은 IsaacLab에서 PPO로 훈련되고, 제어 간격은 `Δt = 0.02s`, 시간 평활화는 `t' ∈ {t-8Δt, t-16Δt, t-32Δt}`를 사용한다. 훈련 중 다양한 명령과 외부 힘 분포를 샘플링하고 도메인 무작위화를 적용한다. 가장 중요한 공학적 세부 사항은 시간 평활화의 구현으로, 훈련 안정성을 직접 결정한다. 배포 시 대부분의 경우 명확히 정의된 세계 좌표계가 없으므로, 로봇 좌표계에서 고정 목표 속도 모드 또는 완전 순응 모드로 `x_des`를 지정해야 한다. 강한 당김 실험에서는 `K_p`와 설정점 변위를 점진적으로 증가시켜 `K_p(x_ref-x)`가 `100 N`까지 도달하게 한다. 가장 함정에 빠지기 쉬운 부분은 보상 함수의 `exp(-||ẋ-ẋ_ref||²)` 형태가 초기 오차가 클 때 포화될 수 있다는 점으로, 이차 비용 항 `-||ẋ-ẋ_ref||²`을 추가하여 해결해야 한다.
