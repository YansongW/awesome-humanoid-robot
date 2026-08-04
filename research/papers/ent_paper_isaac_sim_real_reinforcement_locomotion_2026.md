---
$id: ent_paper_isaac_sim_real_reinforcement_locomotion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds'
  zh: 'Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds'
  ko: 'Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds'
summary:
  en: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex
    legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion,
    often utilizes a high-performance simulation tool, providing a controlled and efficient training and development environment.
    However, policies that perform.
  zh: 本文提出一个基于Nvidia Isaac Sim平台的强化学习四足运动控制框架，通过域随机化、执行器建模和奖励塑形实现零样本sim-to-real迁移，并在Unitree Go1上验证。核心贡献在于不依赖预获取数据或teacher-student架构，仅通过仿真训练即可获得与集成控制器相当的速度跟踪性能和更强的扰动恢复能力。
  ko: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex
    legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion,
    often utilizes a high-performance simulation tool, providing a controlled and efficient training and development environment.
    However, policies that perform.
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
- isaac
- sim
- real
- reinforcement
- locomotion
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.18135 Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds'
  url: https://arxiv.org/abs/2607.18135
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一个基于Nvidia Isaac Sim平台的强化学习四足运动控制框架，通过域随机化、执行器建模和奖励塑形实现零样本sim-to-real迁移，并在Unitree Go1上验证。核心贡献在于不依赖预获取数据或teacher-student架构，仅通过仿真训练即可获得与集成控制器相当的速度跟踪性能和更强的扰动恢复能力。

## 它改变了什么

传统RL运动策略要么作为高层控制器输出参考轨迹，要么依赖teacher-student框架中的预训练模型，这限制了策略的泛化性和部署便捷性。本文改变了这一范式：直接以关节位置为动作空间，通过精心设计的奖励塑形让策略自主涌现自然步态，而非显式指定步态模式。这种"奖励驱动"方法在Isaac Sim平台上证明了可行性，且训练成本极低（单张RTX 3090、3小时），使得RL运动控制从研究原型走向工程可复现。

更重要的是，作者将执行器建模（actuator-net）作为sim-to-real成功的关键前置条件，而非事后补偿。这一决策改变了传统"先训练策略再处理域差异"的流程，将硬件特性嵌入仿真环境，使得零样本迁移成为可能。同时，作者在推理端将策略频率从训练时的50Hz提升至100Hz，并发现性能显著提升，这挑战了"训练与推理频率必须一致"的常见假设。

## 方法拆解

### 问题建模
- 使用MDP (𝒮, 𝒜, 𝒫, ℛ, γ) 定义运动控制问题，策略 π(𝒜|𝒮) 输出12维关节位置动作（Unitree Go1的12个驱动关节）。
- 动作空间：关节位置乘以缩放因子0.2，加上标称配置偏移；观测空间为48维向量，包含线速度、角速度、投影重力、用户命令、关节位置/速度、上一动作。

### 域随机化
- 并行训练4096个环境（RTX 3090），随机化范围覆盖足部摩擦(0.4, 1.1)、质心偏移(±0.025)、连杆质量(0.8-1.3倍)、身体速度/位置/姿态、关节位置/速度等。
- 地形课程逐步增加高度和粗糙度；每10-15秒施加随机推动（线速度[-1.0, 1.0] m/s）。
- 命令速度采样：x方向[-2, 3] m/s，y方向[-1.5, 1.5] m/s，角速度[-1.5, 1.5] rad/s，采样间隔0.3-10秒。

### 执行器建模
- 使用3层MLP（每层64神经元，soft-sign激活）的actuator-net捕捉非线性执行器动力学，kp=20，kd=0.5。
- 训练数据来自部署期间记录的关节位置/速度历史与力矩输出；作者强调集成actuator-net前策略在sim-to-real上遭遇显著挑战。

### 奖励塑形
- 步态奖励（权重10.0）通过同步/异步足部接触产生自然步态；足部离地间隙(5.0)和空中时间(5.0)权重较大。
- 安全惩罚：关节位置限制(-100.0)、关节速度限制(-10.0)、大腿接触(-10.0)、小腿接触(-1.0)。
- 动作平滑性(-1.5)和关节偏差(-0.75)权重高于同类工作，提升高命令速度下的表现；足部受力惩罚(-0.00002)实现柔和接触。

### 网络与训练
- Actor-critic架构，MLP均为3层(512, 256, 128)，ELU激活；PPO算法，熵系数0.0025，目标KL 0.01，γ=0.99，λ=0.95，学习率0.001。
- 训练5000次迭代约3小时；物理仿真Δt=0.002s，策略Δt=0.02s（50Hz）。

### 推理优化
- 策略编译为ONNX格式，运行于Jetson Nano（Docker容器），无需GPU加速即可达400Hz。
- 卡尔曼滤波器完全用C++实现（Pybind11编译），使状态估计延迟降低至支持400Hz循环率。

## 关键创新

1. **零样本sim-to-real的完整工程闭环**：不依赖任何真实机器人数据或预训练模型，仅通过域随机化+执行器建模+奖励塑形，在Isaac Sim上训练的策略可直接部署到Unitree Go1。这验证了Isaac Sim作为RL训练平台的可靠性，为其他机器人平台提供了可复制的范式。

2. **执行器建模作为前置条件**：作者明确将actuator-net集成作为sim-to-real成功的关键，而非事后补偿。这一设计决策将硬件非线性动力学嵌入仿真环境，使得策略在训练阶段就适应真实执行器特性，显著缩小域差距。

3. **推理频率提升的意外收益**：将策略循环率从训练时的50Hz提升至100Hz，性能反而提升（更敏捷、更稳定）。这挑战了"训练-推理频率必须一致"的常见做法，暗示更高控制频率可部分补偿策略的模型误差，为部署优化提供了新思路。

## 实验与结果

### 速度跟踪
- 策略达到线速度2.0 m/s，角速度1.8 rad/s；35秒正弦命令跟踪中，性能与Unitree集成控制器相似，仅存在小幅相位滞后。
- 高频率高振幅命令下出现足部打滑，因此降低了最大/最小速度限制。

### 扰动抑制
- 三次连续踢击（力度递增），策略均成功恢复，仅出现踉跄，从未完全摔倒；原始数据25Hz记录，策略100Hz运行。

### 地形验证
- 在砾石、沙地、上坡/下坡平原等崎岖地形上行走成功，包括陡峭斜坡托盘（图1）。

### 关键数字汇总
| 指标 | 数值 |
|------|------|
| 训练时间 | ~3小时（5000次迭代） |
| 并行环境数 | 4096 |
| 最大线速度 | 2.0 m/s |
| 最大角速度 | 1.8 rad/s |
| 推理频率 | 400 Hz（ONNX, Jetson Nano） |
| 训练频率 | 50 Hz |
| 部署频率 | 100 Hz（性能提升） |
| 扰动恢复 | 3/3次成功 |

### 对比基线
- 仅与Unitree集成控制器（默认步态）对比，未与其他RL方法进行定量比较。

## 边界与局限

- 论文未设独立局限性章节，从事实要点推断：未使用预获取数据（非teacher-student框架），未在真实机器人上训练或微调（纯仿真+零样本迁移）。
- 未与其他RL基线（如SAC、TD3或其他四足RL方法）进行定量对比，仅与Unitree集成控制器比较，缺乏相对优势的量化证据。
- 扰动测试中踢击力仅为近似估计（通过线速度推算），非精确测量，恢复能力的边界条件不明确。
- 未提及策略在极端地形（如楼梯、冰面）或长时间运行下的退化情况；域随机化范围有限，可能无法覆盖所有真实环境变化。

## 工程启示

1. **复现优先核对**：执行器建模（actuator-net）是sim-to-real成功的关键，务必先采集真实执行器数据训练该网络，再训练策略。跳过此步骤将导致显著的域差距。
2. **奖励权重敏感**：关节位置限制惩罚(-100.0)和步态奖励(10.0)权重极高，调整时需谨慎；动作平滑性(-1.5)和关节偏差(-0.75)高于常规设置，对高命令速度表现至关重要。
3. **推理频率优化**：部署时尝试将策略频率从训练值提升（如50Hz→100Hz），可能带来性能提升；但需确保状态估计（如卡尔曼滤波器）延迟足够低，建议用C++实现关键组件。
4. **域随机化范围**：足部摩擦(0.4, 1.1)和连杆质量(0.8-1.3)是主要随机化维度，若目标地形差异大，需扩展范围或增加地形课程复杂度。
5. **易踩坑点**：观测空间未缩放（与其他研究不同），若修改需重新调参；命令速度采样间隔(0.3-10秒)影响策略对指令变化的响应，需根据实际任务调整。

## Overview
Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development environment. However, policies that perform well in simulation frequently encounter unexpected challenges when deployed on a physical system, known as the sim-to-real gap. This work presents a robust RL locomotion framework capable of whole-body control. The proposed RL framework utilizes Nvidia's new set of simulation tools, Isaac Sim, and its companion RL framework, Isaac Lab, for training, achieving a zero-shot sim-to-real policy. The performance of our policy is validated on physical hardware using the Unitree Go1, with experimental results showing similar velocity tracking performance to the quadruped's integrated controller, with a greater ability to recover from large disturbances, and achieve linear velocities of 2.0 m/s and angular velocities of 1.8 rad/s.

## 参考
- https://arxiv.org/abs/2607.18135

## 개요

본 논문은 Nvidia Isaac Sim 플랫폼 기반 강화학습 사족 보행 제어 프레임워크를 제안하며, 도메인 무작위화, 액추에이터 모델링 및 보상 형상을 통해 제로샷 sim-to-real 전이를 구현하고 Unitree Go1에서 검증한다. 핵심 기여는 사전 수집 데이터나 teacher-student 아키텍처에 의존하지 않고, 시뮬레이션 훈련만으로 통합 컨트롤러와 유사한 속도 추적 성능과 더 강력한 외란 회복 능력을 얻을 수 있다는 점이다.

## 무엇을 바꾸었는가

기존 RL 운동 정책은 고수준 컨트롤러로서 참조 궤적을 출력하거나 teacher-student 프레임워크의 사전 훈련 모델에 의존하여, 정책의 일반화 성능과 배포 편의성을 제한했다. 본 논문은 이러한 패러다임을 변경한다: 관절 위치를 직접 행동 공간으로 사용하고, 정교하게 설계된 보상 형상을 통해 명시적 보행 패턴 지정 없이 정책이 자연스러운 보행을 자율적으로 창발하게 한다. 이러한 "보상 기반" 접근 방식은 Isaac Sim 플랫폼에서 실현 가능함을 입증했으며, 훈련 비용이 매우 낮아(단일 RTX 3090, 3시간) RL 운동 제어를 연구 프로토타입에서 공학적으로 재현 가능한 수준으로 끌어올렸다.

더 중요하게, 저자는 액추에이터 모델링(actuator-net)을 사후 보상이 아닌 sim-to-real 성공의 핵심 선행 조건으로 간주한다. 이 결정은 "정책을 먼저 훈련하고 도메인 차이를 처리하는" 기존 프로세스를 변경하여 하드웨어 특성을 시뮬레이션 환경에 내장함으로써 제로샷 전이를 가능하게 한다. 또한, 저자는 추론 단계에서 정책 주파수를 훈련 시 50Hz에서 100Hz로 높였을 때 성능이 현저히 향상됨을 발견했으며, 이는 "훈련과 추론 주파수가 일치해야 한다"는 일반적인 가정에 도전한다.

## 방법 분해

### 문제 모델링
- MDP (𝒮, 𝒜, 𝒫, ℛ, γ)로 운동 제어 문제를 정의하고, 정책 π(𝒜|𝒮)는 12차원 관절 위치 행동(Unitree Go1의 12개 구동 관절)을 출력한다.
- 행동 공간: 관절 위치에 스케일 팩터 0.2를 곱하고 공칭 구성 오프셋을 더함; 관측 공간은 48차원 벡터로 선속도, 각속도, 투영 중력, 사용자 명령, 관절 위치/속도, 이전 행동을 포함한다.

### 도메인 무작위화
- 4096개 환경을 병렬 훈련(RTX 3090)하며, 무작위화 범위는 발 마찰(0.4, 1.1), 질량 중심 오프셋(±0.025), 링크 질량(0.8-1.3배), 몸체 속도/위치/자세, 관절 위치/속도 등을 포함한다.
- 지형 커리큘럼은 높이와 거칠기를 점진적으로 증가시킨다; 10-15초마다 무작위 밀기(선속도 [-1.0, 1.0] m/s)를 적용한다.
- 명령 속도 샘플링: x 방향 [-2, 3] m/s, y 방향 [-1.5, 1.5] m/s, 각속도 [-1.5, 1.5] rad/s, 샘플링 간격 0.3-10초.

### 액추에이터 모델링
- 3층 MLP(각 층 64 뉴런, soft-sign 활성화)의 actuator-net으로 비선형 액추에이터 동역학을 포착하며, kp=20, kd=0.5.
- 훈련 데이터는 배포 중 기록된 관절 위치/속도 이력과 토크 출력에서 얻는다; 저자는 actuator-net 통합 전 정책이 sim-to-real에서 상당한 어려움을 겪었음을 강조한다.

### 보상 형상
- 보행 보상(가중치 10.0)은 동기/비동기 발 접촉을 통해 자연스러운 보행을 생성한다; 발 이격 간격(5.0)과 공중 시간(5.0) 가중치가 크다.
- 안전 패널티: 관절 위치 제한(-100.0), 관절 속도 제한(-10.0), 대퇴부 접촉(-10.0), 하퇴부 접촉(-1.0).
- 행동 평활성(-1.5)과 관절 편차(-0.75) 가중치는 유사 연구보다 높아 높은 명령 속도에서 성능을 향상시킨다; 발 힘 패널티(-0.00002)는 부드러운 접촉을 구현한다.

### 네트워크 및 훈련
- Actor-critic 아키텍처, MLP 모두 3층(512, 256, 128), ELU 활성화; PPO 알고리즘, 엔트로피 계수 0.0025, 목표 KL 0.01, γ=0.99, λ=0.95, 학습률 0.001.
- 훈련 5000회 반복 약 3시간; 물리 시뮬레이션 Δt=0.002s, 정책 Δt=0.02s(50Hz).

### 추론 최적화
- 정책을 ONNX 형식으로 컴파일하여 Jetson Nano(Docker 컨테이너)에서 실행하며, GPU 가속 없이 400Hz 달성.
- 칼만 필터를 완전히 C++로 구현(Pybind11 컴파일)하여 상태 추정 지연을 400Hz 루프 속도를 지원할 수준으로 낮춘다.

## 핵심 혁신

1. **제로샷 sim-to-real의 완전한 엔지니어링 폐루프**: 실제 로봇 데이터나 사전 훈련 모델에 의존하지 않고, 도메인 무작위화 + 액추에이터 모델링 + 보상 형상만으로 Isaac Sim에서 훈련된 정책을 Unitree Go1에 직접 배포할 수 있다. 이는 Isaac Sim의 RL 훈련 플랫폼으로서의 신뢰성을 검증하며, 다른 로봇 플랫폼에 재현 가능한 패러다임을 제공한다.

2. **액추에이터 모델링을 선행 조건으로**: 저자는 actuator-net 통합을 sim-to-real 성공의 핵심으로 명시하며, 사후 보상이 아닌 것으로 간주한다. 이 설계 결정은 하드웨어 비선형 동역학을 시뮬레이션 환경에 내장하여 정책이 훈련 단계에서 실제 액추에이터 특성에 적응하게 하여 도메인 격차를 현저히 줄인다.

3. **추론 주파수 향상의 예상 외 이점**: 정책 루프 속도를 훈련 시 50Hz에서 100Hz로 높였을 때 오히려 성능이 향상된다(더 민첩하고 안정적). 이는 "훈련-추론 주파수 일치"의 일반적 관행에 도전하며, 더 높은 제어 주파수가 정책의 모델 오차를 부분적으로 보상할 수 있음을 시사하여 배포 최적화에 새로운 방향을 제시한다.

## 실험 및 결과

### 속도 추적
- 정책은 선속도 2.0 m/s, 각속도 1.8 rad/s에 도달; 35초 사인파 명령 추적에서 Unitree 통합 컨트롤러와 유사한 성능을 보이며, 약간의 위상 지연만 존재한다.
- 고주파 고진폭 명령에서 발 미끄러짐이 발생하여 최대/최소 속도 제한을 낮췄다.

### 외란 억제
- 세 번의 연속 발차기(힘 증가)에서 정책은 모두 성공적으로 회복하며, 비틀거림만 발생하고 완전히 넘어지지 않았다; 원본 데이터는 25Hz 기록, 정책은 100Hz 실행.

### 지형 검증
- 자갈, 모래, 오르막/내리막 평지 등 거친 지형에서 성공적으로 보행하며, 가파른 경사 팔레트(그림 1)도 포함한다.

### 핵심 수치 요약
| 지표 | 값 |
|------|------|
| 훈련 시간 | ~3시간(5000회 반복) |
| 병렬 환경 수 | 4096 |
| 최대 선속도 | 2.0 m/s |
| 최대 각속도 | 1.8 rad/s |
| 추론 주파수 | 400 Hz(ONNX, Jetson Nano) |
| 훈련 주파수 | 50 Hz |
| 배포 주파수 | 100 Hz(성능 향상) |
| 외란 회복 | 3/3회 성공 |

### 비교 기준
- Unitree 통합 컨트롤러(기본 보행)와만 비교했으며, 다른 RL 방법과의 정량적 비교는 없다.

## 경계 및 한계

- 논문은 별도의 한계 섹션을 두지 않았으며, 사실적 요점에서 추론: 사전 수집 데이터를 사용하지 않았고(비 teacher-student 프레임워크), 실제 로봇에서 훈련이나 미세 조정을 하지 않았다(순수 시뮬레이션 + 제로샷 전이).
- 다른 RL 기준(SAC, TD3 또는 다른 사족 RL 방법)과의 정량적 비교가 없으며, Unitree 통합 컨트롤러와만 비교하여 상대적 우위의 정량적 증거가 부족하다.
- 외란 테스트의 발차기 힘은 근사 추정(선속도로 환산)일 뿐 정밀 측정이 아니며, 회복 능력의 경계 조건이 명확하지 않다.
- 극단적 지형(계단, 빙판)이나 장시간 운용에서의 정책 저하에 대한 언급이 없다; 도메인 무작위화 범위가 제한적이어서 모든 실제 환경 변화를 포괄하지 못할 수 있다.

## 엔지니어링 시사점

1. **재현 시 우선 확인 사항**: 액추에이터 모델링(actuator-net)은 sim-to-real 성공의 핵심이므로, 먼저 실제 액추에이터 데이터를 수집하여 해당 네트워크를 훈련한 후 정책을 훈련해야 한다. 이 단계를 건너뛰면 상당한 도메인 격차가 발생한다.
2. **보상 가중치 민감성**: 관절 위치 제한 패널티(-100.0)와 보행 보상(10.0) 가중치가 매우 높아 조정 시 주의가 필요하다; 행동 평활성(-1.5)과 관절 편차(-0.75)는 일반 설정보다 높아 높은 명령 속도 성능에 중요하다.
3. **추론 주파수 최적화**: 배포 시 정책 주파수를 훈련 값에서 높이는 것(예: 50Hz→100Hz)이 성능 향상을 가져올 수 있다; 단, 상태 추정(예: 칼만 필터) 지연이 충분히 낮아야 하며, 핵심 구성 요소는 C++로 구현하는 것이 좋다.
4. **도메인 무작위화 범위**: 발 마찰(0.4, 1.1)과 링크 질량(0.8-1.3)이 주요 무작위화 차원이며, 목표 지형 차이가 크면 범위를 확장하거나 지형 커리큘럼 복잡도를 높여야 한다.
5. **주의할 함정**: 관측 공간이 스케일링되지 않았으며(다른 연구와 다름), 수정 시 재조정이 필요하다; 명령 속도 샘플링 간격(0.3-10초)은 정책의 명령 변화 응답에 영향을 미치므로 실제 작업에 따라 조정해야 한다.
