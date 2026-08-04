---
$id: ent_paper_direct_dynamic_retargeting_humanoid_imit_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos
  zh: Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos
  ko: Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos
summary:
  en: Imitation Learning from monocular video demonstrations provides a scalable approach for teaching complex skills to humanoid
    robots. However, translating human motion to humanoids requires overcoming significant morphological mismatches. Standard
    approaches rely on Geometric Retargeting or Indirect Dynamic Retargeting pipelines. We identify that these intermediate
    kinematic projections introduce a.
  zh: 本文提出 Direct Dynamic Retargeting (DDR)，一种直接从单目视频中生成人形机器人动态可行轨迹的单阶段框架，由法国团队完成。DDR 绕过传统几何重定向的中间步骤，在任务空间用基于采样的 MPC 求解器直接优化，并在
    Unitree H1-2 上实现零样本 sim-to-real 迁移，显著提升下游模仿学习的成功率与效率。
  ko: Imitation Learning from monocular video demonstrations provides a scalable approach for teaching complex skills to humanoid
    robots. However, translating human motion to humanoids requires overcoming significant morphological mismatches. Standard
    approaches rely on Geometric Retargeting or Indirect Dynamic Retargeting pipelines. We identify that these intermediate
    kinematic projections introduce a.
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
- direct
- dynamic
- retargeting
- humanoid
- imit
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): xiaoze_P122. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: arXiv:2605.23762 Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos
  url: https://arxiv.org/abs/2605.23762
  date: '2026-05-22'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Direct Dynamic Retargeting (DDR)，一种直接从单目视频中生成人形机器人动态可行轨迹的单阶段框架，由法国团队完成。DDR 绕过传统几何重定向的中间步骤，在任务空间用基于采样的 MPC 求解器直接优化，并在 Unitree H1-2 上实现零样本 sim-to-real 迁移，显著提升下游模仿学习的成功率与效率。

## 它改变了什么

传统的人形机器人模仿学习 pipeline 是"视频→SMPL→几何重定向→动力学优化→RL 训练"，其中几何重定向 (GR) 和间接动态重定向 (IDR) 都依赖一个中间运动学投影步骤。作者的核心判断是：这个中间步骤不是无害的"格式转换"，而是引入了几何偏差——它把人体运动硬性映射到机器人运动学上，却丢失了接触序列和动力学可行性信息，等于在优化之前就人为缩小了搜索空间。DDR 真正改变的是这个 pipeline 的拓扑结构：不再先求一个"看起来像"的中间轨迹，再费力把它变成"能执行"的轨迹，而是直接在任务空间里搜索"能执行且最接近演示"的轨迹。这个改变的意义在于，它把"几何相似性"和"动力学可行性"从串行变成了并行约束，让优化器自己发现接触序列，而不是依赖人工标注或启发式规则。

## 方法拆解

### 问题形式化
DDR 最小化参考演示与动态可行集 𝔽_q0 中轨迹的 FK 投影距离：min_{U∈𝕌} d(FK(S_q0(U)), x_ref)，其中 S_q0 是模拟器 rollout 函数，FK 是扩展前向运动学，U 是控制序列。

### 求解器选择：CEM 而非梯度法
- 使用交叉熵方法 (CEM) 作为 MPC 求解器，而非 Crocoddyl 等梯度求解器
- 关键理由：CEM 的采样方式能内在处理从噪声视频数据中识别接触序列的歧义，无需预定义接触序列——梯度法需要接触序列作为输入，而 CEM 通过随机采样隐式探索接触模式

### 距离度量：增强距离
- 空间跟踪项 E_p：欧氏距离，惩罚关键点位置偏差
- 相对形状匹配项 E_l：使用拉普拉斯矩阵 L 惩罚相邻关键点间的结构变形，对全局平移和旋转不变——这保证了在整体位姿有偏差时，肢体相对结构仍被约束

### MPC 方案
- 滚动时域控制，可求解任意时间范围，计算负担小
- 框架模块化，可替换其他随机优化器

### 下游 RL 蒸馏
- 将离线生成的 DDR 轨迹蒸馏为闭环策略
- 使用 Constraints-as-Terminations 框架 + PPO（skrl 实现，IsaacLab 环境）
- 每个动作训练一个策略，5 个随机种子
- 观测：关节位置/速度、先前动作、基座线/角速度、基座高度、投影重力、相位变量 φ_t ∈ [0,1]
- 动作：a_t ∈ R^21，期望关节位置经 PD 控制器跟踪
- 奖励：deepMimic 风格，含跟踪项（关节位置/速度、根姿态/速度、末端执行器位置）和惩罚项（关节加速度/扭矩、动作速率、脚滑）

## 关键创新

1. **单阶段动态重定向**：首次将"几何投影"和"动力学优化"合并为一步，直接在任务空间搜索动态可行轨迹。这消除了中间几何步骤带来的偏差累积，让优化器在完整动力学约束下自由探索接触序列——这是对传统 GR→IDR 两级 pipeline 的结构性简化。

2. **CEM 作为接触序列隐式发现器**：用采样方法替代梯度优化，看似是"退而求其次"，实则是针对视频噪声数据的刻意设计。梯度法需要接触序列先验，而 CEM 通过随机采样天然处理接触歧义，避免了人工标注接触模式的瓶颈。

3. **拉普拉斯形状匹配项**：在任务空间距离中引入对全局平移/旋转不变的相对结构约束，解决了纯欧氏距离对整体位姿偏差过度敏感的问题，使得优化器能容忍全局偏移而保持肢体结构一致——这是保证动态可行性与参考相似性平衡的关键设计。

## 实验与结果

### 可行性（表 II，物理不可行段百分比，越低越好）
| 动作 | GR | IDR | DDR |
|------|-----|-----|-----|
| Squat | 21.74% | 0.00% | 0.00% |
| Kung fu | 15.81% | 0.00% | 0.00% |
| One-foot Balance | 28.38% | 2.86% | 3.36% |
| Pistol Squat | 18.16% | 1.06% | 0.00% |
| Balancing Stick | 3.08% | 1.02% | 0.20% |

### 接触序列误差率（表 III，与手动标注真值不匹配，越低越好）
| 动作 | GR | IDR | DDR |
|------|-----|-----|-----|
| Squat | 32.12% | 0.00% | 0.00% |
| Kung fu | 10.53% | 13.03% | 4.23% |
| One-foot Balance | 21.37% | 24.72% | 13.71% |
| Pistol Squat | 15.00% | 9.13% | 5.35% |
| Balancing Stick | 8.19% | 20.73% | 7.86% |

### 下游 RL 成功率（表 IV，5 个随机种子，失败判据：骨盆偏差>50cm）
| 动作 | IDR | DDR |
|------|-----|-----|
| Squat | 100.00% | 100.00% |
| Kung fu | 66.67% | 100.00% |
| One-foot Balance | 13.33% | 46.67% |
| Pistol Squat | 40.00% | 80.00% |
| Balancing Stick | 0.00% | 66.67% |

### RL 学习效率（表 VI，90% 为达到平台期 90% 所需环境步数，越低越好）
| 动作 | GR 90% | IDR 90% | DDR 90% |
|------|--------|---------|---------|
| Squat | 41.3k | 38.2k | 21.1k |
| Kung fu | 91.1k | 95.6k | 71.6k |
| One-foot Bal. | 219.9k | 57.3k | 76.3k |
| Pistol Squat | 128.4k | 93.5k | 79.6k |
| Bal. Stick | 103.2k | - | 78.9k |

### 策略参考跟踪（表 VII，关节 RMSE [rad]，越低越好）
| 动作 | GR | IDR | DDR |
|------|-----|-----|-----|
| Squat | 0.916 | 0.806 | 0.750 |
| Kung fu | 0.735 | 0.672 | 0.627 |
| One-foot balance | 0.848 | 0.657 | 0.713 |
| Pistol Squat | 0.976 | 0.807 | 0.729 |
| Balancing Stick | 1.021 | - | 0.667 |

**结果含义**：DDR 在可行性上几乎完全消除不可行段（除 One-foot Balance 的 3.36%），在接触序列识别上显著优于 IDR（尤其 One-foot Balance 从 24.72% 降至 13.71%），在下游 RL 成功率上全面碾压 IDR（尤其 Balancing Stick 从 0% 到 66.67%），且学习效率普遍提升。实机实验在 Unitree H1-2 上零样本迁移成功执行全部 5 种动作，手枪深蹲中甚至出现单脚恢复跳跃行为。

## 边界与局限

- 目标函数纯粹定义在任务空间，可能导致病态解或收敛较慢——作者明确承认这一点
- 性能对任务空间权重和初始化敏感，目前需要手动调参，缺乏自适应机制
- 未扩展到大规模、多样化的网络视频动作集（列为未来工作）
- IDR 和 DDR 中仍存在小部分不可行段（如 One-foot Balance 的 3.36%），归因于 Mujoco 与 Pinocchio 模拟差异
- 论文未明确推理频率、训练时长、数据量对性能的敏感性分析

## 工程启示

- **复现优先核对**：CEM 的采样数、迭代次数、任务空间权重（E_p 与 E_l 的相对权重）是影响性能的关键超参，论文未给出具体数值，需自行调参——这是最可能踩坑的地方
- **接触判定阈值**：脚与地面距离小于 2 cm 视为接触，这个阈值直接影响接触序列误差率的计算，复现时需严格对齐
- **模拟器差异**：Mujoco（参考轨迹）与 Pinocchio（可行性评估）的动力学差异会导致不可行段残留，复现时需注意两个模拟器的摩擦系数、接触模型设置
- **RL 蒸馏注意**：DDR 轨迹是离线生成的，蒸馏为闭环策略时需使用参考状态初始化和早期终止技术（deepMimic 方法），否则学习效率会显著下降
- **下游团队选型**：如果你的任务涉及动态平衡（如单脚站立、高难度姿势），DDR 的优势最明显（成功率从 0-40% 提升到 47-80%）；如果任务本身静态且简单（如 Squat），IDR 已足够，DDR 的收益有限
- **实机部署**：Unitree H1-2 上零样本迁移成功，但需注意硬件安全约束（限制最大关节位置、速度和扭矩），且实机使用机载本体感觉和 Mocap 系统——Mocap 依赖可能限制实际部署场景

## Overview
Imitation Learning from monocular video demonstrations provides a scalable approach for teaching complex skills to humanoid robots. However, translating human motion to humanoids requires overcoming significant morphological mismatches. Standard approaches rely on Geometric Retargeting or Indirect Dynamic Retargeting pipelines. We identify that these intermediate kinematic projections introduce a geometric bias, restricting the search space and yielding suboptimal dynamic behaviors. In this paper, we propose Direct Dynamic Retargeting (DDR), a novel single-stage framework that generates high-fidelity, dynamically feasible trajectories directly from expert videos. By formulating the problem in the task space and leveraging a sampling-based Model Predictive Control solver within a physics simulator, DDR natively optimizes over complex contact sequences while mitigating input drift. Our experiments demonstrate that bypassing the geometric bias allows DDR to outperform state-of-the-art baselines in demonstration tracking accuracy. Furthermore, we establish that providing such physically viable references to RL agents accelerates training convergence and enhances the final execution of agile and balancing behaviors. Source code will be made publicly available.

## 参考
- https://arxiv.org/abs/2605.23762

## 개요

본 논문은 프랑스 팀이 제안한 Direct Dynamic Retargeting (DDR)을 소개합니다. DDR은 단안 비디오에서 직접 휴머노이드 로봇의 동적 실행 가능 궤적을 생성하는 단일 단계 프레임워크입니다. DDR은 전통적인 기하학적 리타겟팅의 중간 단계를 우회하여, 작업 공간에서 샘플링 기반 MPC 솔버로 직접 최적화하며, Unitree H1-2에서 제로샷 sim-to-real 전이를 구현하여 하위 모방 학습의 성공률과 효율성을 크게 향상시킵니다.

## 그것이 바꾸는 것

전통적인 휴머노이드 모방 학습 파이프라인은 "비디오→SMPL→기하학적 리타겟팅→동역학 최적화→RL 훈련"이며, 여기서 기하학적 리타겟팅(GR)과 간접 동적 리타겟팅(IDR)은 모두 중간 운동학적 투영 단계에 의존합니다. 저자들의 핵심 판단은 이 중간 단계가 무해한 "형식 변환"이 아니라 기하학적 편향을 도입한다는 것입니다. 즉, 인간의 움직임을 로봇 운동학에 강제로 매핑하면서 접촉 시퀀스와 동역학적 실행 가능성 정보를 잃어버려, 최적화 전에 탐색 공간을 인위적으로 축소시키는 것입니다. DDR이 진정으로 바꾸는 것은 이 파이프라인의 토폴로지 구조입니다. 더 이상 "비슷해 보이는" 중간 궤적을 먼저 구한 다음 그것을 "실행 가능한" 궤적으로 변환하는 데 힘쓰지 않고, 작업 공간에서 직접 "실행 가능하면서 데모에 가장 가까운" 궤적을 탐색합니다. 이 변화의 의미는 "기하학적 유사성"과 "동역학적 실행 가능성"을 직렬에서 병렬 제약 조건으로 전환하여, 최적화기가 수동 주석이나 휴리스틱 규칙에 의존하지 않고 접촉 시퀀스를 스스로 발견하게 한다는 점입니다.

## 방법 분석

### 문제 정식화
DDR은 참조 데모와 동적 실행 가능 집합 𝔽_q0 내 궤적의 FK 투영 거리를 최소화합니다: min_{U∈𝕌} d(FK(S_q0(U)), x_ref). 여기서 S_q0는 시뮬레이터 rollout 함수, FK는 확장 전방 운동학, U는 제어 시퀀스입니다.

### 솔버 선택: CEM vs 그래디언트 방법
- Crocoddyl과 같은 그래디언트 솔버 대신 교차 엔트로피 방법(CEM)을 MPC 솔버로 사용
- 핵심 이유: CEM의 샘플링 방식은 노이즈가 있는 비디오 데이터에서 접촉 시퀀스를 식별하는 모호성을 내재적으로 처리하며, 사전 정의된 접촉 시퀀스가 필요 없음——그래디언트 방법은 접촉 시퀀스를 입력으로 필요로 하지만, CEM은 무작위 샘플링을 통해 접촉 패턴을 암시적으로 탐색

### 거리 측정: 강화 거리
- 공간 추적 항 E_p: 유클리드 거리, 키포인트 위치 편차 페널티
- 상대 형상 매칭 항 E_l: 라플라시안 행렬 L을 사용하여 인접 키포인트 간 구조 변형 페널티, 전역 병진 및 회전에 불변——이는 전체 자세에 편차가 있을 때 팔다리 상대 구조가 여전히 제약되도록 보장

### MPC 방식
- 롤링 호라이즌 제어, 임의 시간 범위 해결 가능, 계산 부담 적음
- 프레임워크 모듈식, 다른 무작위 최적화기로 교체 가능

### 하위 RL 증류
- 오프라인에서 생성된 DDR 궤적을 폐루프 정책으로 증류
- Constraints-as-Terminations 프레임워크 + PPO 사용 (skrl 구현, IsaacLab 환경)
- 각 동작마다 하나의 정책 훈련, 5개 무작위 시드
- 관측: 관절 위치/속도, 이전 동작, 베이스 선형/각속도, 베이스 높이, 투영 중력, 위상 변수 φ_t ∈ [0,1]
- 동작: a_t ∈ R^21, 원하는 관절 위치를 PD 컨트롤러로 추적
- 보상: deepMimic 스타일, 추적 항(관절 위치/속도, 루트 자세/속도, 말단 효과기 위치) 및 페널티 항(관절 가속도/토크, 동작 속도, 발 미끄러짐) 포함

## 핵심 혁신

1. **단일 단계 동적 리타겟팅**: "기하학적 투영"과 "동역학 최적화"를 하나의 단계로 처음 통합하여 작업 공간에서 직접 동적 실행 가능 궤적을 탐색합니다. 이는 중간 기하학적 단계로 인한 편향 누적을 제거하고, 최적화기가 완전한 동역학 제약 하에서 접촉 시퀀스를 자유롭게 탐색하게 합니다——이는 전통적인 GR→IDR 2단계 파이프라인의 구조적 단순화입니다.

2. **CEM을 접촉 시퀀스 암시적 발견기로 사용**: 샘플링 방법으로 그래디언트 최적화를 대체하는 것은 겉보기에는 "차선책"처럼 보이지만, 실제로는 노이즈가 있는 비디오 데이터를 위한 의도적인 설계입니다. 그래디언트 방법은 접촉 시퀀스 사전 지식이 필요하지만, CEM은 무작위 샘플링을 통해 접촉 모호성을 자연스럽게 처리하여 수동 주석 접촉 패턴의 병목을 피합니다.

3. **라플라시안 형상 매칭 항**: 작업 공간 거리에 전역 병진/회전에 불변한 상대 구조 제약을 도입하여, 순수 유클리드 거리가 전체 자세 편차에 과도하게 민감한 문제를 해결합니다. 이를 통해 최적화기가 전역 오프셋을 허용하면서 팔다리 구조 일관성을 유지할 수 있습니다——이는 동적 실행 가능성과 참조 유사성의 균형을 보장하는 핵심 설계입니다.

## 실험 및 결과

### 실행 가능성 (표 II, 물리적으로 실행 불가능한 구간 비율, 낮을수록 좋음)
| 동작 | GR | IDR | DDR |
|------|-----|-----|-----|
| Squat | 21.74% | 0.00% | 0.00% |
| Kung fu | 15.81% | 0.00% | 0.00% |
| One-foot Balance | 28.38% | 2.86% | 3.36% |
| Pistol Squat | 18.16% | 1.06% | 0.00% |
| Balancing Stick | 3.08% | 1.02% | 0.20% |

### 접촉 시퀀스 오류율 (표 III, 수동 주석 진실값과 불일치, 낮을수록 좋음)
| 동작 | GR | IDR | DDR |
|------|-----|-----|-----|
| Squat | 32.12% | 0.00% | 0.00% |
| Kung fu | 10.53% | 13.03% | 4.23% |
| One-foot Balance | 21.37% | 24.72% | 13.71% |
| Pistol Squat | 15.00% | 9.13% | 5.35% |
| Balancing Stick | 8.19% | 20.73% | 7.86% |

### 하위 RL 성공률 (표 IV, 5개 무작위 시드, 실패 기준: 골반 편차>50cm)
| 동작 | IDR | DDR |
|------|-----|-----|
| Squat | 100.00% | 100.00% |
| Kung fu | 66.67% | 100.00% |
| One-foot Balance | 13.33% | 46.67% |
| Pistol Squat | 40.00% | 80.00% |
| Balancing Stick | 0.00% | 66.67% |

### RL 학습 효율 (표 VI, 90%는 플랫폼 90% 도달에 필요한 환경 스텝 수, 낮을수록 좋음)
| 동작 | GR 90% | IDR 90% | DDR 90% |
|------|--------|---------|---------|
| Squat | 41.3k | 38.2k | 21.1k |
| Kung fu | 91.1k | 95.6k | 71.6k |
| One-foot Bal. | 219.9k | 57.3k | 76.3k |
| Pistol Squat | 128.4k | 93.5k | 79.6k |
| Bal. Stick | 103.2k | - | 78.9k |

### 정책 참조 추적 (표 VII, 관절 RMSE [rad], 낮을수록 좋음)
| 동작 | GR | IDR | DDR |
|------|-----|-----|-----|
| Squat | 0.916 | 0.806 | 0.750 |
| Kung fu | 0.735 | 0.672 | 0.627 |
| One-foot balance | 0.848 | 0.657 | 0.713 |
| Pistol Squat | 0.976 | 0.807 | 0.729 |
| Balancing Stick | 1.021 | - | 0.667 |

**결과 의미**: DDR은 실행 가능성에서 거의 모든 실행 불가능 구간을 제거하고(One-foot Balance의 3.36% 제외), 접촉 시퀀스 식별에서 IDR보다 크게 우수하며(특히 One-foot Balance가 24.72%에서 13.71%로 감소), 하위 RL 성공률에서 IDR을 전반적으로 압도하고(특히 Balancing Stick이 0%에서 66.67%로), 학습 효율도 전반적으로 향상됩니다. 실물 실험은 Unitree H1-2에서 제로샷 전이로 5가지 동작을 모두 성공적으로 실행했으며, 권총 스쿼트에서는 한 발로 회복 점프하는 행동까지 나타났습니다.

## 경계 및 한계

- 목적 함수가 순수하게 작업 공간에 정의되어 있어 병리적 해나 수렴 속도 저하를 초래할 수 있음——저자들이 명시적으로 인정
- 성능이 작업 공간 가중치와 초기화에 민감하며, 현재 수동 튜닝이 필요하고 적응 메커니즘이 부족
- 대규모, 다양한 웹 비디오 동작 세트로 확장되지 않음(향후 작업으로 명시)
- IDR과 DDR 모두 여전히 소량의 실행 불가능 구간이 존재(예: One-foot Balance의 3.36%), Mujoco와 Pinocchio 시뮬레이션 차이로 인한 것으로 귀속
- 논문은 추론 빈도, 훈련 시간, 데이터 양에 따른 성능 민감도 분석을 명시하지 않음

## 공학적 시사점

- **재현 시 우선 확인 사항**: CEM의 샘플 수, 반복 횟수, 작업 공간 가중치(E_p와 E_l의 상대 가중치)는 성능에 영향을 미치는 핵심 하이퍼파라미터이며, 논문에 구체적인 수치가 없어 직접 튜닝해야 함——가장 함정에 빠지기 쉬운 부분
- **접촉 판정 임계값**: 발과 지면 사이 거리가 2cm 미만이면 접촉으로 간주하며, 이 임계값은 접촉 시퀀스 오류율 계산에 직접 영향을 미치므로 재현 시 엄격히 일치시켜야 함
- **시뮬레이터 차이**: Mujoco(참조 궤적)와 Pinocchio(실행 가능성 평가)의 동역학 차이는 실행 불가능 구간 잔존을 초래할 수 있으므로, 재현 시 두 시뮬레이터의 마찰 계수, 접촉 모델 설정에 주의해야 함
- **RL 증류 주의사항**: DDR 궤적은 오프라인에서 생성되므로, 폐루프 정책으로 증류할 때 참조 상태 초기화 및 조기 종료 기술(deepMimic 방법)을 사용해야 하며, 그렇지 않으면 학습 효율이 크게 저하됨
- **하위 팀 선택**: 작업이 동적 균형(예: 한 발 서기, 고난도 자세)을 포함한다면 DDR의 이점이 가장 두드러짐(성공률 0-40%에서 47-80%로 향상); 작업 자체가 정적이고 단순하다면(예: Squat) IDR로 충분하며 DDR의 이점은 제한적
- **실물 배포**: Unitree H1-2에서 제로샷 전이가 성공했지만, 하드웨어 안전 제약(최대 관절 위치, 속도, 토크 제한)에 주의해야 하며, 실물은 기내 고유 감각과 Mocap 시스템을 사용——Mocap 의존성은 실제 배포 시나리오를 제한할 수 있음
