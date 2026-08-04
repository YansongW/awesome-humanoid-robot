---
$id: ent_paper_wristmimic_full_body_humanoid_control_wr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WristMimic: Full-Body Humanoid Control with Wrist-Guided Manipulation'
  zh: 'WristMimic: Full-Body Humanoid Control with Wrist-Guided Manipulation'
  ko: 'WristMimic: Full-Body Humanoid Control with Wrist-Guided Manipulation'
summary:
  en: Retargeting human object interaction demonstrations to physics based simulation requires reproducing not only body motion
    but also the object motion and contacts that make manipulation succeed. However, position only hand trajectories do not
    specify the contact forces needed to manipulate objects, and directly tracking them can overconstrain contact rich finger
    behavior. We introduce WristMimic,.
  zh: WristMimic 是一个腕部引导的全身人形控制框架，由韩国研究团队提出，旨在将人体-物体交互演示重定向到物理仿真中。其核心贡献在于解耦无接触身体运动与接触丰富的手部操作，通过腕部作为桥梁，让手指行为由物体和接触动力学隐式引导，而非显式监督，从而在
    ParaHome 和 OMOMO 数据集上显著超越现有方法。
  ko: Retargeting human object interaction demonstrations to physics based simulation requires reproducing not only body motion
    but also the object motion and contacts that make manipulation succeed. However, position only hand trajectories do not
    specify the contact forces needed to manipulate objects, and directly tracking them can overconstrain contact rich finger
    behavior. We introduce WristMimic,.
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
- wristmimic
- full
- body
- humanoid
- control
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
  title: 'arXiv:2607.06438 WristMimic: Full-Body Humanoid Control with Wrist-Guided Manipulation'
  url: https://arxiv.org/abs/2607.06438
  date: '2026-07-07'
  accessed_at: '2026-08-05'
---

## 概述

WristMimic 是一个腕部引导的全身人形控制框架，由韩国研究团队提出，旨在将人体-物体交互演示重定向到物理仿真中。其核心贡献在于解耦无接触身体运动与接触丰富的手部操作，通过腕部作为桥梁，让手指行为由物体和接触动力学隐式引导，而非显式监督，从而在 ParaHome 和 OMOMO 数据集上显著超越现有方法。

## 它改变了什么

现有的人-物交互重定向方法陷入了一个误区：试图通过越来越密集的手指运动学监督来复现操作细节。但问题在于，仅基于位置的手部轨迹无法指定操作物体所需的接触力，直接跟踪这些轨迹会过度约束接触丰富的指尖行为，导致仿真中的物体滑落或姿态不自然。作者质疑了这种“跟踪一切”的范式，提出一个更本质的问题：与其让手指服从运动学目标，不如让手部由物体和接触动力学来引导。

WristMimic 真正改变的是监督信号的分配逻辑。它不再将人体视为一个需要全自由度跟踪的整体，而是将问题分解为两个机制：无接触的身体运动（可运动学跟踪）和接触丰富的手部操作（需动力学引导）。腕部作为这两个机制的天然桥梁——它基本无接触，可被精确跟踪，同时决定了手的全局配置并将手指置于可及的抓取范围内。这一改变使得策略无需任何手指姿态监督即可学习操作，且能适应不同手部形态，从根本上降低了对密集手指动捕数据的依赖。

## 方法拆解

### 监督解耦
- 策略网络输出所有 51 个关节的动作（19 身体 + 2 腕部 + 30 手指），动作从高斯分布采样，通过 PD 控制器转为力矩。
- 目标状态仅对无接触关节（19 身体 + 2 腕部）分配运动学姿态目标，**排除所有 30 个手指关节**。手指行为通过物体姿态目标和接触对齐奖励间接优化。

### 乘法奖励结构
奖励采用乘法形式 `r = exp(−λE)`，包含五个部分：
- 关节位置跟踪（仅无接触关节）
- 关节旋转跟踪（仅无接触关节）
- 物体位置跟踪
- 物体旋转跟踪
- 接触对齐（23 个接触元素：21 非手指刚体 + 2 手级指示器）

### 优先级对齐策略
- 定义以首次接触帧为中心的接触窗口（`t_b=10` 帧前，`t_a=15` 帧后）。
- 窗口内：抓取手肩肘关节权重置 0，腕部权重保持 1，其余无接触身体关节权重降为 `w_red`（<1）。
- 阶段特定重置阈值：接触窗口分为接近、抓取、稳定三阶段。抓取阶段严格（位置 7cm，方向 0.2 rad），接近和稳定阶段宽松（15cm，0.5 rad）。

### 训练配置
- PPO 算法，2048 并行环境，minibatch 8192，horizon 32，控制频率 30Hz，单张 RTX 3090。
- Isaac Gym + PhysX（TGS 求解器，子步 2），位置迭代 10（默认 4）防穿透，接触偏移 0.002m。

## 关键创新

1. **腕部引导的监督解耦**：这是首个明确将腕部作为无接触身体与接触丰富手部之间桥梁的全身控制框架。腕部既提供强结构信号（决定手的全局构型），又避免直接跟踪手指带来的过约束问题。这一设计使得策略能通过交互动力学适应不同手部几何，而非依赖运动学监督。

2. **手指无关（finger-agnostic）的公式化**：通过排除所有手指关节的运动学目标，策略可在不同手部形态间迁移（如 InterMimic 手、OmniGrasp 手），无需为每种手重新采集手指数据。这打破了现有方法对手指动捕数据的刚性依赖。

3. **接触窗口内的优先级调制**：在接触发生的关键帧附近，动态调整奖励权重——降低身体监督、置零上臂关节、保持腕部恒定。这种时间上的非均匀监督策略，让策略在接触瞬间专注于动力学而非姿态复现，是成功率大幅提升的关键设计。

## 实验与结果

### 主结果（表 1）
| 数据集 | 方法 | 成功率 (%) | 位置误差 (cm) | 旋转误差 (°) |
|--------|------|------------|---------------|--------------|
| OMOMO | WristMimic | **98.9** | **7.3** | **12.2** |
| OMOMO | InterMimic | 86.6 | 14.2 | 22.2 |
| ParaHome | WristMimic | **83.3** | **15.3** | **33.9** |
| ParaHome | InterMimic | 0.1 | 83.5 | 73.3 |
| ParaHome | SkillMimicV2 | 1.3 | 72.1 | 80.3 |
| 平均 | WristMimic | **91.1** | **11.3** | **23.1** |
| 平均 | InterMimic | 43.3 | 48.8 | 47.7 |

### 消融研究（表 2，ParaHome）
| 变体 | 成功率 (%) | 位置误差 (cm) | 旋转误差 (°) |
|------|------------|---------------|--------------|
| 无腕部约束（解耦） | 0.0 | 56.4 | 49.7 |
| 仅奖励权重调制 | 0.0 | 50.3 | 43.6 |
| 仅阶段特定重置 | 67.5 | 28.8 | 56.9 |
| WristMimic（完整） | **86.5** | **9.9** | **36.0** |

### 重置阈值消融（Tab. 4.4）
| 阈值 | 成功率 (%) | 位置误差 (cm) | 旋转误差 (°) |
|------|------------|---------------|--------------|
| 3.5cm/0.1rad（tight） | 0.0 | 99.8 | 86.8 |
| 15cm/0.5rad（loose） | 17.5 | 78.3 | 72.3 |
| 7cm/0.2rad（默认） | **96.3** | **9.5** | **18.1** |

### 手部形态泛化（Tab. 5，ParaHome 10 序列）
| 手型 | 成功率 (%) | 位置误差 (cm) | 旋转误差 (°) |
|------|------------|---------------|--------------|
| ParaHome 场景特定手 | 75.8 | 20.1 | 39.6 |
| InterMimic 手 | **95.2** | **10.8** | **28.1** |
| OmniGrasp 手 | 76.4 | 16.9 | 27.1 |

结果含义：腕部约束是成功的关键（无它则完全失败）；阶段特定重置比权重调制更重要；InterMimic 手因关节范围受限（防物理不合理姿态）表现最佳，验证了“让动力学引导手指”而非强制跟踪的设计。

## 边界与局限

- 方法聚焦于感知抓取和物体操作，**不适用于需要精细手指姿态控制的精确手内操作（in-hand manipulation）**，如手指内重定位或物体在手内重新定向。
- 当前框架训练**场景特定策略**，每个场景需单独训练，与 OmniGrasp、InterMimic、MaskedManipulator 等跨场景泛化方法形成对比。
- 在 Move Book 场景中，策略会因抓取稳定性而用双手支撑书本，与人类演示（单手举起）有偏差——这是设计选择（优先稳定操作而非严格模仿），但可能不适用于需要精确姿态复现的应用。
- 论文未明确评估对未见物体类别或未见交互模式的泛化能力。

## 工程启示

- **先核对腕部重置阈值**：这是成功率的分水岭。7cm/0.2rad 是经过消融验证的最优平衡点，过紧（3.5cm/0.1rad）导致探索不足完全失败，过松（15cm/0.5rad）破坏接触稳定性。复现时务必严格按此设置。
- **位置迭代次数必须调高**：从默认 4 增至 10 是防止抓取过程中物体穿透的关键，对接触丰富的稳定操作至关重要。若使用其他物理引擎，需找到等效的防穿透配置。
- **最容易踩坑的是奖励权重调制**：接触窗口内身体权重降低（gbp: 30→10, gbr: 2.5→1）、上臂关节置零、腕部权重恒定（gwp=10, gwr=1）——这三者缺一不可。消融显示仅权重调制而无腕部约束仍会完全失败。
- **手部关节范围设置影响巨大**：InterMimic 手因限制关节范围（而非 [−π, π]）而表现最佳。复现时若使用其他手型，务必限制关节范围以排除物理不合理姿态，否则性能会显著下降（如 ParaHome 特定手 75.8% vs InterMimic 手 95.2%）。
- **训练成本可控**：单张 RTX 3090、2048 并行环境即可训练，但每场景需单独训练。若需跨场景泛化，需在保留腕部中心交互结构的前提下扩展框架，这是当前未解决的方向。

## Overview
Retargeting human object interaction demonstrations to physics based simulation requires reproducing not only body motion but also the object motion and contacts that make manipulation succeed. However, position only hand trajectories do not specify the contact forces needed to manipulate objects, and directly tracking them can overconstrain contact rich finger behavior. We introduce WristMimic, a wrist guided whole body control framework that explicitly separates contact free body motion from contact rich hand manipulation. The contact free body and wrist are guided by kinematic pose targets, whereas the fingers are not directly supervised by human hand pose. Instead, they learn grasping and manipulation behaviors from object tracking and contact outcomes. Our key insight is that the wrist is the natural gate between these two regimes. It is largely free from contact and can be tracked kinematically, yet it determines the global hand configuration and places the fingers within reachable grasp affordances. To ensure reliable wrist placement during interaction, we introduce wrist specific reset constraints and reward prioritization. Experiments show that WristMimic matches or surpasses methods using full finger pose supervision while enabling finger agnostic retargeting across diverse hand embodiments.

## 参考
- https://arxiv.org/abs/2607.06438

## 개요

WristMimic은 한국 연구팀이 제안한 손목 기반 전신 휴머노이드 제어 프레임워크로, 인간-물체 상호작용 데모를 물리 시뮬레이션으로 리타게팅하는 것을 목표로 합니다. 핵심 기여는 비접촉 신체 운동과 접촉이 풍부한 손 조작을 분리하고, 손목을 브리지로 활용하여 손가락 동작이 명시적 감독이 아닌 물체 및 접촉 역학에 의해 암시적으로 유도되도록 한 점입니다. 이를 통해 ParaHome 및 OMOMO 데이터셋에서 기존 방법들을 크게 능가하는 성능을 달성했습니다.

## 무엇을 바꾸었는가

기존의 인간-물체 상호작용 리타게팅 방법은 점점 더 조밀한 손가락 운동학적 감독을 통해 조작 세부 사항을 재현하려는 오류에 빠져 있었습니다. 그러나 문제는 위치 기반 손 궤적만으로는 물체를 조작하는 데 필요한 접촉 힘을 지정할 수 없으며, 이러한 궤적을 직접 추적하면 접촉이 풍부한 손끝 동작이 과도하게 제약되어 시뮬레이션에서 물체가 미끄러지거나 자세가 부자연스러워진다는 점입니다. 저자들은 이러한 "모든 것을 추적"하는 패러다임에 의문을 제기하며, 손가락이 운동학적 목표를 따르게 하는 대신 손이 물체 및 접촉 역학에 의해 유도되도록 하는 것이 더 근본적인 질문이라고 제안합니다.

WristMimic이 실제로 바꾼 것은 감독 신호의 할당 논리입니다. 더 이상 인체를 전체 자유도를 추적해야 하는 하나의 덩어리로 보지 않고, 비접촉 신체 운동(운동학적으로 추적 가능)과 접촉이 풍부한 손 조작(역학적 유도 필요)이라는 두 가지 메커니즘으로 문제를 분해합니다. 손목은 이 두 메커니즘의 자연스러운 브리지 역할을 합니다—기본적으로 비접촉이므로 정밀하게 추적할 수 있으며, 동시에 손의 전체 구성을 결정하고 손가락을 파지 가능한 범위 내에 위치시킵니다. 이러한 변화 덕분에 정책은 손가락 자세 감독 없이도 조작을 학습할 수 있고, 다양한 손 형태에 적응할 수 있어 조밀한 손가락 모션 캡처 데이터에 대한 의존도를 근본적으로 낮춥니다.

## 방법 분석

### 감독 분리
- 정책 네트워크는 51개 관절 모두의 동작(19 신체 + 2 손목 + 30 손가락)을 출력하며, 동작은 가우시안 분포에서 샘플링되어 PD 컨트롤러를 통해 토크로 변환됩니다.
- 목표 상태는 비접촉 관절(19 신체 + 2 손목)에만 운동학적 자세 목표를 할당하며, **30개 손가락 관절은 모두 제외**합니다. 손가락 동작은 물체 자세 목표와 접촉 정렬 보상을 통해 간접적으로 최적화됩니다.

### 곱셈 보상 구조
보상은 곱셈 형태 `r = exp(−λE)`를 사용하며, 다섯 가지 구성 요소를 포함합니다:
- 관절 위치 추적(비접촉 관절만)
- 관절 회전 추적(비접촉 관절만)
- 물체 위치 추적
- 물체 회전 추적
- 접촉 정렬(23개 접촉 요소: 21 비손가락 강체 + 2 손 수준 표시기)

### 우선순위 정렬 전략
- 첫 접촉 프레임을 중심으로 한 접촉 창(`t_b=10` 프레임 전, `t_a=15` 프레임 후)을 정의합니다.
- 창 내에서: 파지 손의 어깨-팔꿈치 관절 가중치는 0으로 설정, 손목 가중치는 1 유지, 나머지 비접촉 신체 관절 가중치는 `w_red`(<1)로 감소.
- 단계별 리셋 임계값: 접촉 창은 접근, 파지, 안정의 세 단계로 구분됩니다. 파지 단계는 엄격(위치 7cm, 방향 0.2 rad), 접근 및 안정 단계는 완화(15cm, 0.5 rad).

### 훈련 구성
- PPO 알고리즘, 2048 병렬 환경, 미니배치 8192, horizon 32, 제어 주파수 30Hz, 단일 RTX 3090.
- Isaac Gym + PhysX(TGS 솔버, 서브스텝 2), 위치 반복 10회(기본 4)로 관통 방지, 접촉 오프셋 0.002m.

## 핵심 혁신

1. **손목 기반 감독 분리**: 손목을 비접촉 신체와 접촉이 풍부한 손 사이의 브리지로 명시적으로 활용한 최초의 전신 제어 프레임워크입니다. 손목은 강력한 구조적 신호(손의 전체 구성을 결정)를 제공하면서도 손가락 직접 추적의 과도한 제약 문제를 피합니다. 이 설계 덕분에 정책은 운동학적 감독이 아닌 상호작용 역학을 통해 다양한 손 기하학에 적응할 수 있습니다.

2. **손가락 무관(finger-agnostic) 공식화**: 모든 손가락 관절의 운동학적 목표를 제외함으로써, 정책은 다른 손 형태 간에 전이될 수 있으며(예: InterMimic 손, OmniGrasp 손), 각 손에 대한 손가락 데이터를 다시 수집할 필요가 없습니다. 이는 기존 방법의 손가락 모션 캡처 데이터에 대한 경직된 의존성을 깨뜨립니다.

3. **접촉 창 내 우선순위 변조**: 접촉이 발생하는 중요한 프레임 주변에서 보상 가중치를 동적으로 조정합니다—신체 감독 감소, 상완 관절 제로화, 손목 가중치 일정 유지. 이러한 시간적 비균일 감독 전략은 정책이 접촉 순간에 자세 재현이 아닌 역학에 집중하도록 하여, 성공률을 크게 향상시키는 핵심 설계입니다.

## 실험 및 결과

### 주요 결과 (표 1)
| 데이터셋 | 방법 | 성공률 (%) | 위치 오차 (cm) | 회전 오차 (°) |
|--------|------|------------|---------------|--------------|
| OMOMO | WristMimic | **98.9** | **7.3** | **12.2** |
| OMOMO | InterMimic | 86.6 | 14.2 | 22.2 |
| ParaHome | WristMimic | **83.3** | **15.3** | **33.9** |
| ParaHome | InterMimic | 0.1 | 83.5 | 73.3 |
| ParaHome | SkillMimicV2 | 1.3 | 72.1 | 80.3 |
| 평균 | WristMimic | **91.1** | **11.3** | **23.1** |
| 평균 | InterMimic | 43.3 | 48.8 | 47.7 |

### 절제 연구 (표 2, ParaHome)
| 변형 | 성공률 (%) | 위치 오차 (cm) | 회전 오차 (°) |
|------|------------|---------------|--------------|
| 손목 제약 없음(분리) | 0.0 | 56.4 | 49.7 |
| 보상 가중치 변조만 | 0.0 | 50.3 | 43.6 |
| 단계별 리셋만 | 67.5 | 28.8 | 56.9 |
| WristMimic(전체) | **86.5** | **9.9** | **36.0** |

### 리셋 임계값 절제 (Tab. 4.4)
| 임계값 | 성공률 (%) | 위치 오차 (cm) | 회전 오차 (°) |
|------|------------|---------------|--------------|
| 3.5cm/0.1rad(엄격) | 0.0 | 99.8 | 86.8 |
| 15cm/0.5rad(완화) | 17.5 | 78.3 | 72.3 |
| 7cm/0.2rad(기본) | **96.3** | **9.5** | **18.1** |

### 손 형태 일반화 (Tab. 5, ParaHome 10 시퀀스)
| 손 유형 | 성공률 (%) | 위치 오차 (cm) | 회전 오차 (°) |
|------|------------|---------------|--------------|
| ParaHome 시나리오 특정 손 | 75.8 | 20.1 | 39.6 |
| InterMimic 손 | **95.2** | **10.8** | **28.1** |
| OmniGrasp 손 | 76.4 | 16.9 | 27.1 |

결과 의미: 손목 제약은 성공의 핵심(없으면 완전 실패); 단계별 리셋이 가중치 변조보다 더 중요; InterMimic 손은 관절 범위 제한(물리적으로 비합리적인 자세 방지)으로 최고 성능을 보여, "손가락을 강제 추적"하는 대신 "역학이 손가락을 유도하도록" 하는 설계를 검증합니다.

## 경계 및 한계

- 이 방법은 지각적 파지와 물체 조작에 초점을 맞추며, **정밀한 손가락 자세 제어가 필요한 정교한 손 안 조작(in-hand manipulation)** 에는 적합하지 않습니다(예: 손가락 내 재배치 또는 손 안에서 물체 재방향 설정).
- 현재 프레임워크는 **시나리오별 정책**을 훈련하며, 각 시나리오마다 별도 훈련이 필요합니다. 이는 OmniGrasp, InterMimic, MaskedManipulator 등의 교차 시나리오 일반화 방법과 대조적입니다.
- Move Book 시나리오에서 정책은 파지 안정성을 위해 양손으로 책을 지지하며, 인간 데모(한 손으로 들어 올리기)와 차이가 있습니다—이는 설계 선택(엄격한 모방보다 안정적 조작 우선)이지만, 정확한 자세 재현이 필요한 응용에는 적합하지 않을 수 있습니다.
- 논문은 보이지 않는 물체 범주나 보이지 않는 상호작용 패턴에 대한 일반화 능력을 명시적으로 평가하지 않았습니다.

## 공학적 시사점

- **손목 리셋 임계값을 먼저 확인하세요**: 이것이 성공률의 분기점입니다. 7cm/0.2rad는 절제 연구를 통해 검증된 최적 균형점이며, 너무 엄격하면(3.5cm/0.1rad) 탐색 부족으로 완전 실패, 너무 완화하면(15cm/0.5rad) 접촉 안정성이 파괴됩니다. 재현 시 반드시 이 설정을 엄격히 따르세요.
- **위치 반복 횟수를 반드시 높여야 합니다**: 기본 4에서 10으로 증가시키는 것은 파지 과정에서 물체 관통을 방지하는 핵심이며, 접촉이 풍부한 안정적 조작에 필수적입니다. 다른 물리 엔진을 사용하는 경우, 동등한 관통 방지 구성을 찾아야 합니다.
- **가장 함정에 빠지기 쉬운 것은 보상 가중치 변조입니다**: 접촉 창 내 신체 가중치 감소(gbp: 30→10, gbr: 2.5→1), 상완 관절 제로화, 손목 가중치 일정(gwp=10, gwr=1)—이 세 가지가 모두 필요합니다. 절제 연구에 따르면 손목 제약 없이 가중치 변조만으로는 여전히 완전 실패합니다.
- **손 관절 범위 설정의 영향이 큽니다**: InterMimic 손은 관절 범위를 제한( [−π, π] 대신)하여 최고 성능을 보입니다. 재현 시 다른 손 유형을 사용한다면, 물리적으로 비합리적인 자세를 배제하기 위해 관절 범위를 반드시 제한해야 합니다. 그렇지 않으면 성능이 크게 저하됩니다(예: ParaHome 특정 손 75.8% vs InterMimic 손 95.2%).
- **훈련 비용은 관리 가능합니다**: 단일 RTX 3090, 2048 병렬 환경으로 훈련 가능하지만, 각 시나리오마다 별도 훈련이 필요합니다. 교차 시나리오 일반화가 필요하다면, 손목 중심 상호작용 구조를 유지하면서 프레임워크를 확장해야 하며, 이는 현재 해결되지 않은 방향입니다.
