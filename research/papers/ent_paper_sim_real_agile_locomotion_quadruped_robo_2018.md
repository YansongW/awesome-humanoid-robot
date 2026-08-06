---
$id: ent_paper_sim_real_agile_locomotion_quadruped_robo_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots'
  zh: 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots'
  ko: 'Sim-to-Real: Learning Agile Locomotion For Quadruped Robots'
summary:
  en: Designing agile locomotion for quadruped robots often requires extensive expertise and tedious manual tuning. In this
    paper, we present a system to automate this process by leveraging deep reinforcement learning techniques. Our system can
    learn quadruped locomotion from scratch using simple reward signals. In addition, users can provide an open loop reference
    to guide the learning process when.
  zh: 本文提出一个完整的仿真到现实（sim-to-real）学习系统，用于四足机器人敏捷运动（小跑与疾驰）。作者在 PyBullet 中训练深度强化学习策略，通过精确物理建模、动力学随机化和紧凑观测空间设计，成功将策略直接部署到真实 Minitaur
    机器人，无需真实数据微调。核心贡献是系统性地验证了随机化在缩小现实差距中的作用，并揭示了其鲁棒性与最优性之间的权衡。
  ko: Designing agile locomotion for quadruped robots often requires extensive expertise and tedious manual tuning. In this
    paper, we present a system to automate this process by leveraging deep reinforcement learning techniques. Our system can
    learn quadruped locomotion from scratch using simple reward signals. In addition, users can provide an open loop reference
    to guide the learning process when.
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
- sim
- real
- agile
- locomotion
- quadruped
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P144. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:1804.10332 Sim-to-Real: Learning Agile Locomotion For Quadruped Robots'
  url: https://arxiv.org/abs/1804.10332
  date: '2018-04-27'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一个完整的仿真到现实（sim-to-real）学习系统，用于四足机器人敏捷运动（小跑与疾驰）。作者在 PyBullet 中训练深度强化学习策略，通过精确物理建模、动力学随机化和紧凑观测空间设计，成功将策略直接部署到真实 Minitaur 机器人，无需真实数据微调。核心贡献是系统性地验证了随机化在缩小现实差距中的作用，并揭示了其鲁棒性与最优性之间的权衡。

## 它改变了什么

传统四足运动控制依赖大量人工调参，而深度强化学习在仿真中虽表现优异，却因“现实差距”难以迁移到真实世界。本文真正改变的是将 sim-to-real 从“碰运气”变为“可工程化”的过程：作者没有追求更复杂的算法，而是通过系统性的物理建模（精确 URDF、执行器非线性模型、延迟补偿）和随机化训练，让策略在部署前就具备对真实世界不确定性的鲁棒性。

更重要的是，本文揭示了随机化并非“免费午餐”——它显著降低策略的峰值性能（次优性），但换来了跨环境的一致性。这一权衡在以往工作中常被忽视，本文通过系统实验（Figure 7-9）给出了量化证据，并指出观测空间大小是影响迁移成败的关键因素：大观测空间在仿真中性能更高，但在真实世界中因观测分布不匹配而表现更差。

## 方法拆解

### 策略解耦：用户可控性与学习自由度
- 策略分解为开环分量与反馈分量：**a(t, o) = ā(t) + π(o)**
- 用户可通过设置 π(o) 输出界或 ā(t) 为零，在“完全指定步态”与“完全从零学习”之间连续调节
- 小跑使用用户提供的正弦参考轨迹（s̄(t) = 0.3 sin(4πt)，ē(t) = 0.35 sin(4πt) + 2），反馈仅修正 IMU 观测；疾驰则完全从零学习

### 动作空间设计：腿部空间映射
- 动作定义为腿部空间中的期望姿态，分解为摆动 (s) 和伸展 (e) 分量
- 映射到电机空间：**θ₁ = e + s，θ₂ = e − s**
- 理由：电机空间中有效动作分散在非凸区域（自碰撞约束），腿部空间可设置矩形边界剪除无效动作

### 奖励函数
- **r = (pₙ − pₙ₋₁)·d − wΔt|τₙ·q̇ₙ|**
- 第一项鼓励向期望方向奔跑，第二项惩罚能量消耗；w = 0.008（所有实验固定）
- 每集最多 1000 步，基座倾斜超过 0.5 弧度时终止

### 提高仿真保真度
- 拆解真实 Minitaur，测量尺寸、称重、找质心，创建精确 URDF（惯性假设均匀密度）
- 执行器模型：基于理想直流电机动力学 **τ = Kt·I**，**I = (Vpwm − Vemf)/R**，**Vemf = Kt·q̇**；因线性扭矩-电流关系仅对理想电机成立，构建分段线性函数表征非线性
- 延迟建模：保留观测历史，线性插值补偿 TX2 与 STM32 间的通信延迟（通常 15-19ms）

### 学习鲁棒控制器
- 动力学随机化：每集随机采样物理参数（质量 80%-120%、电机摩擦 0-0.05Nm、惯性 50%-150%、电机强度 80%-120%、控制步长 3-20ms、延迟 0-40ms、电池电压 14.0-16.8V、接触摩擦 0.5-1.25、IMU 偏置与噪声）
- 随机扰动：每 200 步（1.2 秒）施加 130N-220N、持续 0.06 秒的随机方向扰动力
- 紧凑观测空间（4D：roll、pitch 及角速度）减少过拟合仿真的机会

## 关键创新

1. **系统性的 sim-to-real 工程框架**：将精确物理建模、延迟补偿、动力学随机化整合为一个完整流程，而非单一技术点。这种“全栈”方法在 2018 年（论文编号 1804.10332）具有开创性，为后续工作提供了可复现的模板。

2. **随机化代价的量化揭示**：通过 Figure 7-8 明确展示随机化带来的鲁棒性-最优性权衡——随机化训练的策略在所有测试环境中回报均值更低但标准差更小。这一发现对社区具有警示意义：随机化不是“免费午餐”，参数范围需谨慎选择。

3. **观测空间与迁移成功的关联**：发现大观测空间（12D，含电机角度）在仿真中性能更高，但在真实世界中因观测分布不匹配而表现更差；小观测空间（4D，仅 IMU）虽在仿真中次优，却实现了更可靠的迁移。这一反直觉发现对策略设计具有直接指导价值。

## 实验与结果

### 仿真 vs 真实性能对比
| 步态 | 仿真速度 (m/s) | 真实速度 (m/s) | 仿真身长/秒 | 真实身长/秒 |
|------|---------------|---------------|------------|------------|
| 小跑（用户参考） | 0.50 | 0.60 | 0.93 | 1.11 |
| 疾驰（从零学习） | 1.34 | 1.18 | 2.48 | 2.18 |

### 学习 vs 手工步态（真实机器人）
| 步态 | 速度 (m/s) | 平均机械功率 (W) |
|------|-----------|-----------------|
| 小跑（手工） | 0.56 | 92.72 |
| 小跑（学习） | 0.60 | 71.78 |
| 疾驰（手工） | 1.21 | 290.00 |
| 疾驰（学习） | 1.18 | 188.79 |

学习步态与专家调参速度相当，但功率显著降低（疾驰降低 35%，小跑降低 23%，由表内数值 290.00→188.79 与 92.72→71.78 计算）。

### 现实差距评估
- 每组训练 100 个控制器（不同超参数和随机种子），部署仿真中回报最高的前三个，每个运行三次（共九次）
- 小观测空间 + 随机化组合：所有九次运行均成功小跑超过三米并保持整个回合平衡
- 大观测空间在仿真中性能更高，但在真实世界中表现更差，现实差距更大

### 训练配置
- 小跑：观测维度 4，策略网络 (125, 89)，训练 4.35 小时
- 疾驰：观测维度 12，策略网络 (185, 95)，训练 3.25 小时
- 每次更新并行 25 个 roll-out，最大仿真步数 7 百万

## 边界与局限

- 未使用真实世界数据训练或微调，策略完全在仿真中学习后直接部署
- 惯性测量困难，采用均匀密度假设估计；接触参数仅关注侧向摩擦，其余保持默认值
- 动力学随机化以最优性换取鲁棒性，参数范围需谨慎选择以防止过度保守的步态
- 小跑策略部署结果参差不齐（部分可迁移，部分不能），需进一步缩减观测空间
- 未涉及偏航控制、非平坦地形、动态速度调整或视觉感知等复杂场景
- 控制频率约 150-200Hz（可变），因 TX2 非实时操作系统，可能影响高动态运动的稳定性

## 工程启示

复现时首先核对仿真与真实机器人的物理参数一致性——精确 URDF 和执行器非线性模型是迁移成功的基础，任何简化都可能导致现实差距放大。最容易踩坑的是观测空间设计：不要被仿真中的高回报迷惑，大观测空间（含电机角度）在真实世界中往往因观测分布不匹配而失败；优先采用紧凑的 IMU 观测（4D）并配合随机化训练。

动力学随机化的参数范围需谨慎选择——过宽会导致策略过度保守（速度显著下降），过窄则无法覆盖真实不确定性。建议从本文给出的范围（质量 80%-120%、延迟 0-40ms 等）起步，逐步收缩。延迟补偿不可忽略：TX2 上的运动控制器延迟（15-19ms）远高于微控制器（3ms），必须显式建模。最后，训练时间约 3-4 小时（小跑 4.35 小时，疾驰 3.25 小时），25 个并行 roll-out 是合理配置，可据此规划计算资源。

## Overview
Designing agile locomotion for quadruped robots often requires extensive expertise and tedious manual tuning. In this paper, we present a system to automate this process by leveraging deep reinforcement learning techniques. Our system can learn quadruped locomotion from scratch using simple reward signals. In addition, users can provide an open loop reference to guide the learning process when more control over the learned gait is needed. The control policies are learned in a physics simulator and then deployed on real robots. In robotics, policies trained in simulation often do not transfer to the real world. We narrow this reality gap by improving the physics simulator and learning robust policies. We improve the simulation using system identification, developing an accurate actuator model and simulating latency. We learn robust controllers by randomizing the physical environments, adding perturbations and designing a compact observation space. We evaluate our system on two agile locomotion gaits: trotting and galloping. After learning in simulation, a quadruped robot can successfully perform both gaits in the real world.

## 参考
- https://arxiv.org/abs/1804.10332

## 개요

본 논문은 네 발 달린 로봇의 민첩한 보행(속보 및 질주)을 위한 완전한 시뮬레이션-현실(sim-to-real) 학습 시스템을 제안한다. 저자는 PyBullet에서 심층 강화 학습 정책을 훈련하고, 정밀한 물리 모델링, 동역학 무작위화, 그리고 간결한 관측 공간 설계를 통해 실제 데이터 미세 조정 없이 정책을 실제 Minitaur 로봇에 직접 배포하는 데 성공했다. 핵심 기여는 현실 격차를 줄이는 데 있어 무작위화의 역할을 체계적으로 검증하고, 그 견고성과 최적성 사이의 균형을 밝힌 것이다.

## 그것이 바꾼 것

전통적인 네 발 달린 운동 제어는 많은 수동 파라미터 튜닝에 의존하는 반면, 심층 강화 학습은 시뮬레이션에서 뛰어난 성능을 보여도 '현실 격차'로 인해 실제 세계로 이전하기 어렵다. 본 논문이 실제로 바꾼 것은 sim-to-real을 '운에 맡기는 것'에서 '엔지니어링 가능한 프로세스'로 전환한 것이다: 저자는 더 복잡한 알고리즘을 추구하는 대신, 체계적인 물리 모델링(정밀 URDF, 액추에이터 비선형 모델, 지연 보상)과 무작위화 훈련을 통해 정책이 배포 전에 실제 세계의 불확실성에 대한 견고성을 갖추도록 했다.

더 중요한 것은, 본 논문이 무작위화가 '공짜 점심'이 아님을 밝혔다는 점이다—이는 정책의 최고 성능(차선성)을 현저히 낮추지만, 환경 간 일관성을 얻는 대가이다. 이러한 균형은 이전 연구에서 종종 간과되었으며, 본 논문은 체계적인 실험(Figure 7-9)을 통해 정량적 증거를 제시하고, 관측 공간 크기가 이전 성공 여부를 결정하는 핵심 요인임을 지적한다: 큰 관측 공간은 시뮬레이션에서 더 높은 성능을 보이지만, 실제 세계에서는 관측 분포 불일치로 인해 더 나쁜 성능을 보인다.

## 방법 분해

### 정책 분리: 사용자 제어 가능성과 학습 자유도
- 정책은 개루프 성분과 피드백 성분으로 분해된다: **a(t, o) = ā(t) + π(o)**
- 사용자는 π(o) 출력 범위 또는 ā(t)를 0으로 설정하여 '완전히 지정된 보행'과 '완전히 처음부터 학습' 사이에서 연속적으로 조절할 수 있다
- 속보는 사용자가 제공한 사인파 기준 궤적(s̄(t) = 0.3 sin(4πt), ē(t) = 0.35 sin(4πt) + 2)을 사용하며, 피드백은 IMU 관측만 수정한다; 질주는 완전히 처음부터 학습한다

### 행동 공간 설계: 다리 공간 매핑
- 행동은 다리 공간의 기대 자세로 정의되며, 스윙(s)과 스트레치(e) 성분으로 분해된다
- 모터 공간으로 매핑: **θ₁ = e + s, θ₂ = e − s**
- 이유: 모터 공간에서 유효한 행동은 비볼록 영역(자체 충돌 제약)에 분산되어 있으며, 다리 공간은 사각형 경계를 설정하여 유효하지 않은 행동을 제거할 수 있다

### 보상 함수
- **r = (pₙ − pₙ₋₁)·d − wΔt|τₙ·q̇ₙ|**
- 첫 번째 항은 원하는 방향으로 달리는 것을 장려하고, 두 번째 항은 에너지 소비를 패널티로 준다; w = 0.008(모든 실험에서 고정)
- 각 에피소드는 최대 1000步이며, 기체 기울기가 0.5 라디안을 초과하면 종료된다

### 시뮬레이션 충실도 향상
- 실제 Minitaur를 분해하여 치수 측정, 무게 측정, 질량 중심 찾기를 수행하고 정밀 URDF 생성(관성은 균일 밀도 가정)
- 액추에이터 모델: 이상적인 DC 모터 동역학 기반 **τ = Kt·I**, **I = (Vpwm − Vemf)/R**, **Vemf = Kt·q̇**; 선형 토크-전류 관계는 이상적인 모터에만 성립하므로, 비선형성을 나타내는 조각별 선형 함수를 구축
- 지연 모델링: 관측 이력을 유지하고, 선형 보간으로 TX2와 STM32 간 통신 지연(일반적으로 15-19ms)을 보상

### 견고한 제어기 학습
- 동역학 무작위화: 각 에피소드마다 물리 파라미터를 무작위 샘플링(질량 80%-120%, 모터 마찰 0-0.05Nm, 관성 50%-150%, 모터 강도 80%-120%, 제어 스텝 3-20ms, 지연 0-40ms, 배터리 전압 14.0-16.8V, 접촉 마찰 0.5-1.25, IMU 바이어스 및 노이즈)
- 무작위 교란: 매 200步(1.2초)마다 130N-220N, 0.06초 지속의 무작위 방향 교란력을 가함
- 간결한 관측 공간(4D: roll, pitch 및 각속도)은 시뮬레이션에 대한 과적합 가능성을 줄인다

## 핵심 혁신

1. **체계적인 sim-to-real 엔지니어링 프레임워크**: 정밀 물리 모델링, 지연 보상, 동역학 무작위화를 단일 기술 포인트가 아닌 완전한 프로세스로 통합한다. 이러한 '풀스택' 접근 방식은 2018년(논문 번호 1804.10332)에 선구적이었으며, 후속 연구에 재현 가능한 템플릿을 제공했다.

2. **무작위화 비용의 정량적 규명**: Figure 7-8을 통해 무작위화가 가져오는 견고성-최적성 균형을 명확히 보여준다—무작위화된 훈련 정책은 모든 테스트 환경에서 보상 평균은 낮지만 표준 편차는 더 작다. 이 발견은 커뮤니티에 경고적 의미를 갖는다: 무작위화는 '공짜 점심'이 아니며, 파라미터 범위는 신중하게 선택해야 한다.

3. **관측 공간과 이전 성공의 연관성**: 큰 관측 공간(12D, 모터 각도 포함)은 시뮬레이션에서 더 높은 성능을 보이지만, 실제 세계에서는 관측 분포 불일치로 인해 더 나쁜 성능을 보인다; 작은 관측 공간(4D, IMU만)은 시뮬레이션에서 차선이지만 더 신뢰할 수 있는 이전을 달성한다. 이 반직관적인 발견은 정책 설계에 직접적인 지침을 제공한다.

## 실험 및 결과

### 시뮬레이션 vs 실제 성능 비교
| 보행 | 시뮬레이션 속도 (m/s) | 실제 속도 (m/s) | 시뮬레이션 몸길이/초 | 실제 몸길이/초 |
|------|---------------|---------------|------------|------------|
| 속보(사용자 참조) | 0.50 | 0.60 | 0.93 | 1.11 |
| 질주(처음부터 학습) | 1.34 | 1.18 | 2.48 | 2.18 |

### 학습 vs 수동 보행(실제 로봇)
| 보행 | 속도 (m/s) | 평균 기계적 출력 (W) |
|------|-----------|-----------------|
| 속보(수동) | 0.56 | 92.72 |
| 속보(학습) | 0.60 | 71.78 |
| 질주(수동) | 1.21 | 290.00 |
| 질주(학습) | 1.18 | 188.79 |

학습된 보행은 전문가 튜닝 속도와 비슷하지만 출력이 현저히 낮다(질주 35% 감소, 속보 23% 감소, 표 내 값 290.00→188.79 및 92.72→71.78로 계산).

### 현실 격차 평가
- 각 그룹에서 100개의 제어기(다양한 하이퍼파라미터 및 무작위 시드)를 훈련하고, 시뮬레이션에서 보상이 가장 높은 상위 3개를 배포하며, 각각 3회 실행(총 9회)
- 작은 관측 공간 + 무작위화 조합: 9회 실행 모두 3미터 이상 속보를 성공하고 전체 에피소드 동안 균형을 유지
- 큰 관측 공간은 시뮬레이션에서 더 높은 성능을 보이지만 실제 세계에서는 더 나쁜 성능을 보이며, 현실 격차가 더 크다

### 훈련 구성
- 속보: 관측 차원 4, 정책 네트워크 (125, 89), 훈련 4.35시간
- 질주: 관측 차원 12, 정책 네트워크 (185, 95), 훈련 3.25시간
- 각 업데이트마다 25개의 병렬 roll-out, 최대 시뮬레이션 스텝 7백만

## 경계 및 한계

- 실제 세계 데이터로 훈련하거나 미세 조정하지 않았으며, 정책은 완전히 시뮬레이션에서 학습된 후 직접 배포됨
- 관성 측정이 어려워 균일 밀도 가정으로 추정; 접촉 파라미터는 측면 마찰만 고려하고 나머지는 기본값 유지
- 동역학 무작위화는 최적성을 견고성으로 교환하며, 파라미터 범위는 과도하게 보수적인 보행을 방지하기 위해 신중하게 선택해야 함
- 속보 정책 배포 결과는 들쭉날쭉함(일부는 이전 가능, 일부는 불가능), 관측 공간을 더 줄여야 함
- 편요각 제어, 비평탄 지형, 동적 속도 조정 또는 시각적 인식과 같은 복잡한 시나리오는 다루지 않음
- 제어 주파수는 약 150-200Hz(가변)이며, TX2가 실시간 운영 체제가 아니므로 고동적 운동의 안정성에 영향을 줄 수 있음

## 엔지니어링 시사점

재현 시 먼저 시뮬레이션과 실제 로봇의 물리 파라미터 일관성을 확인해야 한다—정밀 URDF와 액추에이터 비선형 모델은 이전 성공의 기초이며, 어떤 단순화도 현실 격차를 확대할 수 있다. 가장 쉽게 함정에 빠지는 부분은 관측 공간 설계이다: 시뮬레이션의 높은 보상에 현혹되지 말 것, 큰 관측 공간(모터 각도 포함)은 실제 세계에서 종종 관측 분포 불일치로 실패한다; 간결한 IMU 관측(4D)을 우선 채택하고 무작위화 훈련을 병행하라.

동역학 무작위화의 파라미터 범위는 신중하게 선택해야 한다—너무 넓으면 정책이 과도하게 보수적이 되고(속도 현저히 감소), 너무 좁으면 실제 불확실성을 커버할 수 없다. 본 논문이 제시한 범위(질량 80%-120%, 지연 0-40ms 등)에서 시작하여 점진적으로 줄이는 것을 권장한다. 지연 보상은 무시할 수 없다: TX2의 운동 제어기 지연(15-19ms)은 마이크로컨트롤러(3ms)보다 훨씬 크므로 명시적으로 모델링해야 한다. 마지막으로, 훈련 시간은 약 3-4시간(속보 4.35시간, 질주 3.25시간)이며, 25개의 병렬 roll-out이 합리적인 구성이므로 이를 기준으로 계산 리소스를 계획할 수 있다.
