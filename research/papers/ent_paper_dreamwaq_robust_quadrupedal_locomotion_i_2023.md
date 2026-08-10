---
$id: ent_paper_dreamwaq_robust_quadrupedal_locomotion_i_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning'
  zh: 'DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning'
  ko: 'DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning'
summary:
  en: Quadrupedal robots resemble the physical ability of legged animals to walk through unstructured terrains. However, designing
    a controller for quadrupedal robots poses a significant challenge due to their functional complexity and requires adaptation
    to various terrains. Recently, deep reinforcement learning, inspired by how legged animals learn to walk from their experiences,
    has been utilized to.
  zh: DreamWaQ 提出一种仅依赖本体感觉的四足机器人鲁棒运动控制器，通过非对称演员-评论家架构与隐式地形想象（CENet 联合估计速度与潜在上下文）实现无视觉感知的复杂地形行走。核心贡献在于将地形表征学习与策略优化端到端联合训练，并引入自适应引导机制（AdaBoot）提升域随机化下的鲁棒性，在真实
    Unitree A1 上验证了长距离行走能力。
  ko: Quadrupedal robots resemble the physical ability of legged animals to walk through unstructured terrains. However, designing
    a controller for quadrupedal robots poses a significant challenge due to their functional complexity and requires adaptation
    to various terrains. Recently, deep reinforcement learning, inspired by how legged animals learn to walk from their experiences,
    has been utilized to.
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
- dreamwaq
- robust
- quadrupedal
- locomotion
- i
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P125. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2301.10602 DreamWaQ: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imaginati'
  url: https://arxiv.org/abs/2301.10602
  date: '2023-01-25'
  accessed_at: '2026-08-05'
---

## 概述

DreamWaQ 提出一种仅依赖本体感觉的四足机器人鲁棒运动控制器，通过非对称演员-评论家架构与隐式地形想象（CENet 联合估计速度与潜在上下文）实现无视觉感知的复杂地形行走。核心贡献在于将地形表征学习与策略优化端到端联合训练，并引入自适应引导机制（AdaBoot）提升域随机化下的鲁棒性，在真实 Unitree A1 上验证了长距离行走能力。

## 它改变了什么

现有四足控制器要么依赖相机/LiDAR 等外感受感知，在恶劣天气或光照下脆弱易失效；要么纯靠本体感觉但受限于表示学习瓶颈，无法在长距离多变地形中保持稳定。DreamWaQ 真正改变的是将“地形想象”从显式建图或监督预训练中解放出来——它不再试图重建地形几何，而是通过潜在上下文 z_t 隐式编码地形特征，让策略在接触前就能“预判”地面性质。这打破了感知-控制两阶段流水线的传统范式，使地形适应成为策略优化的一部分而非前置模块。

另一个关键转变在于训练策略：作者放弃行为克隆（BC）对学生策略的约束，改用非对称 actor-critic 直接联合优化，让评论家看到完整状态（含扰动力和高度图）而演员只看到部分观测。这解决了此前方法中“学生策略性能受限于教师”的根本问题，同时通过 CENet 的 β-VAE 结构让潜在上下文具备可解释的物理意义（速度估计与地形表征共享编码器），而非黑箱特征。

## 方法拆解

### 架构总览
- 非对称 actor-critic：actor 接收部分时序观测 o_t^H（H=5），critic 接收完整状态 s_t（含扰动力、高度图）
- 策略输入：本体感觉 o_t（角速度、重力向量、速度指令、关节角、关节角速度、上一动作）+ 估计速度 v_t + 潜在上下文 z_t
- 动作空间：12 维期望关节角，围绕站立姿态偏移，由 PD 控制器跟踪（Kp=28、Kd=0.7，200 Hz）

### CENet（Context Estimation Network）
- 共享编码器 + 多头解码器，联合估计身体速度 v_t 和潜在上下文 z_t
- 损失函数：MSE 速度估计损失 + VAE 重建/KL 损失（β-VAE 结构）
- 关键设计：速度估计作为辅助任务，强制编码器提取与运动相关的物理量，使 z_t 不退化

### AdaBoot（Adaptive Bootstrapping）
- 自适应引导概率：p_boot = 1 - tanh(CV(R))
- CV(R) 为 m 个域随机化环境的奖励变异系数
- 动态调整：当域随机化导致奖励方差大时降低 p_boot，稳定时提高，平衡探索与利用

### 课程学习与训练
- 地形：平滑、粗糙、离散化、楼梯，倾角范围 [0°, 22°]，十级梯度
- 网格自适应课程：针对低速转向性能优化
- PPO 超参：裁剪 0.2，GAE 0.95，折扣 0.99，Adam 学习率 10^{-3}
- 训练：Isaac Gym，4,096 并行域随机化智能体，1,000 次迭代，约 1 小时（相当于 46 天真实数据）

### 域随机化范围
| 参数 | 范围 |
|------|------|
| 载荷 | [-1, 2] kg |
| Kp 因子 | [0.9, 1.1] Nm/rad |
| Kd 因子 | [0.9, 1.1] Nms/rad |
| 电机强度 | [0.9, 1.1] Nm |
| 质心偏移 | [-50, 50] mm |
| 摩擦系数 | [0.2, 1.25] |
| 系统延迟 | [0.0, 15.0] ms |

## 关键创新

1. **隐式地形想象（Implicit Terrain Imagination）**：不显式重建地形，而是通过潜在上下文 z_t 在接触前编码地形特征。这是首次将地形表征作为可学习的隐变量与策略联合优化，避免了传统感知框架的脆弱性和显式建图的复杂度。

2. **非对称 actor-critic 与 CENet 的协同设计**：评论家访问完整状态（含扰动力和高度图）提供密集学习信号，演员仅依赖本体感觉+潜在上下文。CENet 的速度估计辅助任务确保 z_t 包含运动相关信息，而非纯粹的自监督噪声——这是此前方法未解决的表示学习瓶颈。

3. **AdaBoot 自适应引导**：基于奖励变异系数动态调整引导概率，在域随机化环境中自动平衡“跟随教师”与“自主探索”。相比固定引导概率，这种方法在训练初期（高方差）更保守，后期（低方差）更激进，显著提升最终鲁棒性（表 III 中最大推力从 1.015 提升至 1.121 m/s）。

## 实验与结果

### 鲁棒性测试（表 III，Gazebo 仿真，随机命令 [-1.0, 1.0]，10 分钟，5 次随机种子，配对 t 检验 p<10^{-4}）

| 方法 | 最大推力 (m/s) | 存活率 (%) |
|------|---------------|-----------|
| Baseline | 0.511 ± 0.053 | 20.51 ± 6.44 |
| AdaptationNet | 0.714 ± 0.096 | 82.37 ± 2.49 |
| EstimatorNet | 0.871 ± 0.124 | 80.92 ± 5.73 |
| DreamWaQ w/o AdaBoot | 1.015 ± 0.121 | 90.71 ± 1.25 |
| DreamWaQ w/ AdaBoot | 1.121 ± 0.164 | 95.23 ± 1.61 |

结果解读：DreamWaQ 在最大推力上比最强基线（EstimatorNet）提升 28.7%（由表内数值 0.871→1.121 计算），存活率提升 14.31 个百分点（由表内数值 80.92→95.23 计算）。AdaBoot 的贡献显著：最大推力 +10.4%（由表内数值 1.015→1.121 计算），存活率 +4.52 个百分点（由表内数值 90.71→95.23 计算）。

### 真实世界验证
- Unitree A1，Intel NUC，额外载荷约 500 g，策略与 CENet 同步 50 Hz
- Course A（校园庭院）430 m，Course B（校园山丘）465 m，海拔增益最高 22 m，RTK-GPS 10 Hz
- Course B 在 10 分钟内完成，验证长距离、多变地形下的稳定性

## 边界与局限

- **接触前规划缺失**：DreamWaQ 的适应机制需先以腿部接触障碍物才能更新潜在上下文，对于高楼梯等需要提前规划步态的结构无法处理。作者明确表示集成外感受感知（如视觉）以在接触前规划是未来工作。
- **速度估计依赖**：CENet 的速度估计质量直接影响策略性能，论文未明确在极端打滑或足部完全离地场景下的退化表现。
- **训练计算成本**：4,096 并行智能体 + 1,000 次迭代在 RTX 3060Ti 上需约 1 小时，虽相对高效，但未提供扩展到更复杂地形（如连续楼梯）时的收敛性分析。
- **真实实验规模**：仅 2 条路线（430 m、465 m），未覆盖雨雪、泥泞等极端天气，而这是论文动机中强调的感知失效场景。

## 工程启示

- **复现优先级**：先核对 CENet 的 β-VAE 损失权重和速度估计损失的相对比例——这是影响 z_t 质量的关键超参，论文未明确给出具体权重值，需自行调参。
- **AdaBoot 的 CV 计算窗口**：m 个域随机化环境的奖励变异系数计算方式未详细说明，建议先固定 m=10 左右，观察训练曲线中 p_boot 的变化是否平滑，避免震荡。
- **PD 增益匹配**：真实实验中 Kp=28、Kd=0.7 是针对 Unitree A1 调优的，迁移到其他平台需重新标定，且动作空间（12 维期望关节角）的偏移量需与站立姿态对齐。
- **最易踩坑点**：域随机化中系统延迟 [0.0, 15.0] ms 对策略稳定性影响极大，建议先固定延迟为 0 训练，再逐步引入；直接全范围随机化可能导致训练不收敛。
- **下游团队注意**：策略与 CENet 同步运行于 50 Hz，但 PD 控制器需 200 Hz——这意味着推理管线必须异步设计，否则实时性不足。

## Overview
Quadrupedal robots resemble the physical ability of legged animals to walk through unstructured terrains. However, designing a controller for quadrupedal robots poses a significant challenge due to their functional complexity and requires adaptation to various terrains. Recently, deep reinforcement learning, inspired by how legged animals learn to walk from their experiences, has been utilized to synthesize natural quadrupedal locomotion. However, state-of-the-art methods strongly depend on a complex and reliable sensing framework. Furthermore, prior works that rely only on proprioception have shown a limited demonstration for overcoming challenging terrains, especially for a long distance. This work proposes a novel quadrupedal locomotion learning framework that allows quadrupedal robots to walk through challenging terrains, even with limited sensing modalities. The proposed framework was validated in real-world outdoor environments with varying conditions within a single run for a long distance.

## 参考
- https://arxiv.org/abs/2301.10602

## 개요

DreamWaQ는 고유 감각(proprioception)만을 활용하는 네 발 달린 로봇의 강건한 운동 제어기를 제안하며, 비대칭 액터-크리틱 아키텍처와 암묵적 지형 상상(CENet이 속도와 잠재 컨텍스트를 공동 추정)을 통해 시각적 인식 없이 복잡한 지형을 보행합니다. 핵심 기여는 지형 표현 학습과 정책 최적화를 엔드투엔드로 공동 훈련하고, 적응형 유도 메커니즘(AdaBoot)을 도입하여 도메인 무작위화 하에서 강건성을 향상시킨 점이며, 실제 Unitree A1에서 장거리 보행 능력을 검증했습니다.

## 무엇을 바꾸었는가

기존 네 발 달린 제어기는 카메라/LiDAR 같은 외감각 인식에 의존하여 악천후나 조명 조건에서 취약하거나, 순수 고유 감각에 의존하지만 표현 학습의 병목으로 장거리 다변 지형에서 안정성을 유지하지 못했습니다. DreamWaQ가 실제로 바꾼 것은 '지형 상상'을 명시적 매핑이나 지도 사전 훈련에서 해방시킨 것입니다. 더 이상 지형 기하학을 재구성하려 하지 않고, 잠재 컨텍스트 z_t를 통해 지형 특징을 암묵적으로 인코딩하여 정책이 접촉 전에 지면 특성을 '예측'할 수 있게 합니다. 이는 인식-제어 2단계 파이프라인의 전통적 패러다임을 깨고, 지형 적응을 전처리 모듈이 아닌 정책 최적화의 일부로 만듭니다.

또 다른 핵심 전환은 훈련 전략에 있습니다. 저자들은 행동 복제(BC)가 학생 정책에 부과하던 제약을 포기하고, 비대칭 액터-크리틱을 직접 공동 최적화하여 크리틱은 완전한 상태(교란력과 높이 맵 포함)를 보고 액터는 부분 관측만 보도록 합니다. 이는 기존 방법에서 '학생 정책 성능이 교사에 의해 제한되는' 근본 문제를 해결하며, CENet의 β-VAE 구조를 통해 잠재 컨텍스트가 해석 가능한 물리적 의미(속도 추정과 지형 표현이 인코더를 공유)를 갖도록 합니다. 블랙박스 특징이 아닙니다.

## 방법 분해

### 아키텍처 개요
- 비대칭 액터-크리틱: 액터는 부분 시계열 관측 o_t^H(H=5)를 수신하고, 크리틱은 완전한 상태 s_t(교란력, 높이 맵 포함)를 수신
- 정책 입력: 고유 감각 o_t(각속도, 중력 벡터, 속도 명령, 관절 각도, 관절 각속도, 이전 동작) + 추정 속도 v_t + 잠재 컨텍스트 z_t
- 동작 공간: 12차원 기대 관절 각도, 서 있는 자세 오프셋을 중심으로 PD 제어기로 추적(Kp=28, Kd=0.7, 200 Hz)

### 커리큘럼 학습 및 훈련
- 지형: 평탄, 거친, 불연속, 계단, 경사 범위 [0°, 22°], 10단계 그라데이션
- 그리드 적응형 커리큘럼: 저속 선회 성능 최적화
- PPO 하이퍼파라미터: 클리핑 0.2, GAE 0.95, 할인 0.99, Adam 학습률 10^{-3}
- 훈련: Isaac Gym, 4,096 병렬 도메인 무작위화 에이전트, 1,000회 반복, 약 1시간(실제 데이터 46일 상당)

### 도메인 무작위화 범위
| 파라미터 | 범위 |
|------|------|
| 하중 | [-1, 2] kg |
| Kp 계수 | [0.9, 1.1] Nm/rad |
| Kd 계수 | [0.9, 1.1] Nms/rad |
| 모터 강도 | [0.9, 1.1] Nm |
| 질량 중심 오프셋 | [-50, 50] mm |
| 마찰 계수 | [0.2, 1.25] |
| 시스템 지연 | [0.0, 15.0] ms |

## 핵심 혁신

1. **암묵적 지형 상상(Implicit Terrain Imagination)**: 지형을 명시적으로 재구성하지 않고, 잠재 컨텍스트 z_t를 통해 접촉 전에 지형 특징을 인코딩합니다. 지형 표현을 학습 가능한 잠재 변수로 정책과 공동 최적화한 최초의 사례로, 전통적 인식 프레임워크의 취약성과 명시적 매핑의 복잡성을 피합니다.

2. **비대칭 액터-크리틱과 CENet의 협력 설계**: 크리틱은 완전한 상태(교란력과 높이 맵 포함)에 접근하여 밀집 학습 신호를 제공하고, 액터는 고유 감각+잠재 컨텍스트에만 의존합니다. CENet의 속도 추정 보조 작업은 z_t가 순수 자기 지도 노이즈가 아닌 운동 관련 정보를 포함하도록 보장합니다. 이는 기존 방법이 해결하지 못한 표현 학습 병목입니다.

3. **AdaBoot 적응형 유도**: 보상 변동 계수를 기반으로 유도 확률을 동적으로 조정하여, 도메인 무작위화 환경에서 '교사 따르기'와 '자율 탐험' 사이의 균형을 자동으로 맞춥니다. 고정 유도 확률과 비교하여 이 방법은 훈련 초기(고분산)에는 더 보수적이고, 후기(저분산)에는 더 공격적이어서 최종 강건성을 크게 향상시킵니다(표 III에서 최대 추력이 1.015에서 1.121 m/s로 증가).

## 실험 및 결과

### 강건성 테스트(표 III, Gazebo 시뮬레이션, 무작위 명령 [-1.0, 1.0], 10분, 5회 무작위 시드, 대응 t-검정 p<10^{-4})

| 방법 | 최대 추력 (m/s) | 생존율 (%) |
|------|---------------|-----------|
| Baseline | 0.511 ± 0.053 | 20.51 ± 6.44 |
| AdaptationNet | 0.714 ± 0.096 | 82.37 ± 2.49 |
| EstimatorNet | 0.871 ± 0.124 | 80.92 ± 5.73 |
| DreamWaQ w/o AdaBoot | 1.015 ± 0.121 | 90.71 ± 1.25 |
| DreamWaQ w/ AdaBoot | 1.121 ± 0.164 | 95.23 ± 1.61 |

결과 해석: DreamWaQ는 최대 추력에서 가장 강한 기준선(EstimatorNet)보다 28.7% 향상(표 내 수치 0.871→1.121로 계산), 생존율은 14.31% 포인트 향상(표 내 수치 80.92→95.23으로 계산). AdaBoot의 기여는 유의미합니다: 최대 추력 +10.4%(표 내 수치 1.015→1.121로 계산), 생존율 +4.52% 포인트(표 내 수치 90.71→95.23으로 계산).

### 실제 세계 검증
- Unitree A1, Intel NUC, 추가 하중 약 500 g, 정책과 CENet 동기화 50 Hz
- Course A(캠퍼스 안뜰) 430 m, Course B(캠퍼스 언덕) 465 m, 고도 상승 최대 22 m, RTK-GPS 10 Hz
- Course B는 10분 내 완료, 장거리·다변 지형에서의 안정성 검증

## 경계 및 한계

- **접촉 전 계획 부재**: DreamWaQ의 적응 메커니즘은 다리가 장애물에 접촉한 후에야 잠재 컨텍스트를 업데이트할 수 있어, 높은 계단처럼 보행 패턴을 사전에 계획해야 하는 구조는 처리할 수 없습니다. 저자들은 접촉 전 계획을 위해 외감각 인식(예: 시각)을 통합하는 것을 향후 작업으로 명시했습니다.
- **속도 추정 의존성**: CENet의 속도 추정 품질이 정책 성능에 직접 영향을 미치며, 극단적 미끄러짐이나 발이 완전히 지면에서 떨어진 시나리오에서의 성능 저하에 대해서는 논문에서 명확히 다루지 않았습니다.
- **훈련 계산 비용**: 4,096 병렬 에이전트 + 1,000회 반복은 RTX 3060Ti에서 약 1시간이 소요되지만, 상대적으로 효율적임에도 불구하고 연속 계단 같은 더 복잡한 지형으로 확장할 때의 수렴성 분석은 제공되지 않았습니다.
- **실제 실험 규모**: 2개 경로(430 m, 465 m)에 불과하며, 논문의 동기에서 강조한 인식 실패 시나리오인 비·눈·진흙 같은 극한 기상 조건을 포함하지 않았습니다.

## 공학적 시사점

- **재현 우선순위**: 먼저 CENet의 β-VAE 손실 가중치와 속도 추정 손실의 상대적 비율을 확인하세요. 이는 z_t 품질에 영향을 주는 핵심 하이퍼파라미터로, 논문에서 구체적인 가중치 값을 명시하지 않아 자체 튜닝이 필요합니다.
- **AdaBoot의 CV 계산 창**: m개 도메인 무작위화 환경의 보상 변동 계수 계산 방식이 자세히 설명되지 않았으므로, 먼저 m=10 정도로 고정하고 훈련 곡선에서 p_boot 변화가 매끄러운지 확인하여 진동을 피하는 것이 좋습니다.
- **PD 게인 매칭**: 실제 실험에서 Kp=28, Kd=0.7은 Unitree A1에 맞게 튜닝된 값으로, 다른 플랫폼으로 이식하려면 재보정이 필요하며, 동작 공간(12차원 기대 관절 각도)의 오프셋도 서 있는 자세와 정렬해야 합니다.
- **가장 흔한 함정**: 도메인 무작위화의 시스템 지연 [0.0, 15.0] ms는 정책 안정성에 큰 영향을 미치므로, 먼저 지연을 0으로 고정하고 훈련한 후 점진적으로 도입하는 것이 좋습니다. 전체 범위를 바로 무작위화하면 훈련이 수렴하지 않을 수 있습니다.
- **하위 팀 주의**: 정책과 CENet은 50 Hz로 동기화되지만, PD 제어기는 200 Hz가 필요합니다. 즉, 추론 파이프라인은 비동기적으로 설계해야 하며, 그렇지 않으면 실시간성이 부족합니다.
