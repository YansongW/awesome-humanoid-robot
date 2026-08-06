---
$id: ent_paper_user_driven_demonstration_trajectory_imp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'User-Driven Learning from Demonstration: A Trajectory and Impedance Learning Method'
  zh: 'User-Driven Learning from Demonstration: A Trajectory and Impedance Learning Method'
  ko: 'User-Driven Learning from Demonstration: A Trajectory and Impedance Learning Method'
summary:
  en: This paper presents a method for user-driven robot Learning from Demonstration (LfD) that reduces user effort while
    ensuring compliant and precise reproduction. The method eliminates repeated teaching for the same task and enables real-time
    learning from a single demonstration. Demonstrated motions are reproduced with high precision, while impedance variations
    are learned in real time to provide.
  zh: 本文提出一种单次示教（single-shot）的机器人学习从示教（LfD）框架，由作者 Yang 与 Kermani 开发，同时从机器人本体感觉传感器学习轨迹与阻抗轮廓。核心贡献在于将 3D 快速微分同胚匹配（FDM）与扩展卡尔曼滤波（EKF）速度修正、在线阻抗参数化及表面接触保持策略结合，实现高保真路径复现与扰动恢复。
  ko: This paper presents a method for user-driven robot Learning from Demonstration (LfD) that reduces user effort while
    ensuring compliant and precise reproduction. The method eliminates repeated teaching for the same task and enables real-time
    learning from a single demonstration. Demonstrated motions are reproduced with high precision, while impedance variations
    are learned in real time to provide.
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
- user
- driven
- demonstration
- trajectory
- imp
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.16998 User-Driven Learning from Demonstration: A Trajectory and Impedance Learning Met'
  url: https://arxiv.org/abs/2607.16998
  date: '2026-07-18'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一种单次示教（single-shot）的机器人学习从示教（LfD）框架，由作者 Yang 与 Kermani 开发，同时从机器人本体感觉传感器学习轨迹与阻抗轮廓。核心贡献在于将 3D 快速微分同胚匹配（FDM）与扩展卡尔曼滤波（EKF）速度修正、在线阻抗参数化及表面接触保持策略结合，实现高保真路径复现与扰动恢复。

## 它改变了什么

传统 LfD 方法长期受困于两个相互纠缠的痛点：一是多示教需求带来的用户负担，二是轨迹表示对时间索引的依赖，导致复现时无法适应新轨迹或外部扰动。尽管 DMPs 解决了时间不变性与目标收敛，但其多示教需求与时间依赖问题依旧存在。更关键的是，现有力/阻抗学习方法通常依赖传感器反馈或简化环境接触模型，与路径复现独立记录，无法直接从人类示教中学习柔顺行为。

本文真正改变的是将“轨迹学习”与“阻抗学习”从分离的两条技术路线合并为单一、在线、本体感觉驱动的过程。它不再将偏离任务参考视为需要抑制的扰动，而是通过 EKF 在线估计速度偏置，将扰动视为可修正的系统状态。同时，它利用示教阶段人类操作者保持末端执行器与表面连续接触的隐含假设，将表面几何信息编码进动力学系统（DS）中，从而无需外部接触或视觉传感器即可实现表面接触保持。这实质上是把“示教什么”从单纯的位置路径扩展到了“如何与环境交互”的层面。

## 方法拆解

### 整体架构（Fig. 1）
框架由四个模块组成：(i) 3D FDM 算法将线性 DS 匹配到示教轨迹，生成基础速度场；(ii) EKF 修正基础速度以细化轨迹复现并实现扰动恢复；(iii) 复现过程中在线学习阻抗参数；(iv) 可选模块用于表面接触保持。

### 3D FDM 算法（Algorithm 1）
- 将 2D FDM 扩展至 3D，计算微分同胚 Φ 将点集 X 映射到 Y。
- 局部加权平移：ŷᵢ = xᵢ + k_ρⱼ vⱼ，其中 k_ρⱼ = e^(−ρⱼ²‖xᵢ−cⱼ‖²) 为高斯 RBF 核。
- 优化 ρⱼ 以最小化 ‖φ(X)−Y‖²/N，ρ_max = e^(1/4)/(√2‖v‖)。
- 每次迭代选择 X 中距目标最远的点，方向 vⱼ = β(qⱼ−cⱼ)，0 < μ < 1 为安全裕度，0 < β ≤ 1 为学习率，K = 120–200 为用户选择的局部加权平移总数。
- 最终 Ŷ = Φ(X^(K)) = (φ_ρ₁ ∘ φ_ρ₂ ∘ ⋯ ∘ φ_ρK)(X)。

### 改进的 DS（mDS）运动生成器（式 6）
- 原始 FDM 变换 DS 在 3D 和复杂运动情况下泛化能力下降，作者提出 mDS：ẏ_mDS = −ζ J_Φ x̂。
- ζ = ζ + ηΔζ 为速度调制项，Δζ = (·)ᵀe_v/(‖(·)ᵀe_v‖+ε)，e_v 为示教速度与 mDS 生成速度之间的误差，η 为适应率，ε 为阈值。
- Δζ 经移动平均滤波并施加钳位。

### 逆微分同胚（Algorithm 2）
- 通过反转位移求解 X̂ = Φ⁻¹(Y)，使用 Newton–Raphson 方法求解自引用方程 rⱼ(k) = e^(−ρⱼ²‖oⱼ+kⱼvⱼ⁻‖²)。
- 停止阈值 ε = 10⁻⁶，最大迭代次数 20–50。

### Jacobian 矩阵（式 16–17）
- 使用 Sherman–Morrison 公式 J_φⱼ = I₃ + 2ρⱼ²kⱼvⱼ⁻(X̂−cⱼ)ᵀ，完整 Jacobian J_Φ = ∏ⱼ₌K→1 J_φⱼ。

### EKF 速度修正模块（式 18–22）
- 修正速度：ẏ_ekf = ẏ_mDS + b，b 为在线估计的速度偏置项。
- EKF 状态 sᵢ = [yᵢ, bᵢ]ᵀ ∈ ℝ⁶。
- 过程模型包含偏置衰减项 e^(−λ_b Δt)，λ_b > 0 为偏置衰减率。
- 状态转移 Jacobian 中 F_y 用前向有限差分近似，时间间隔 10⁻³。
- 测量矩阵 H = [I₃ 0₃]，R 为用户定义测量噪声协方差。

### 阻抗参数化（式 23–25）
- 速度跟踪控制器：F_c = D(⋄)ṗ_c，其中 ṗ_c = ẏ_msr − ẏ_ekf。
- D(⋄) = U(⋄)ΛU(⋄)ᵀ，U 包含估计的正交主轴，ê₁ 指向期望运动方向。
- Λ = diag(λ₁, λ₂, λ₃) 为用户定义对角矩阵，元素非负（通常 10–100）。
- 设置 λ₁ = 0 且其余 > 0 可抵抗导致偏离路径跟踪的外力。

### 表面接触保持策略（式 26）
- 利用示教阶段人类操作者保持 EE 工具与目标表面连续接触的假设，表面局部几何隐含编码在 DS 中，无需外部接触或视觉传感器。
- 第三列 ê₃ 与外表面法线重合，提供实时表面法线估计。
- 最终速度：ẏ_d = ẏ_mDS + g_c(·) + b，其中 g_c(·) = α_c ê₃ 产生指向表面的可调速度；高 α_c 强制紧密接触，α_c = 0 表示无接触力跟踪。

## 关键创新

1. **单次示教同时学习轨迹与阻抗**：这是对传统 LfD 范式的实质性突破。以往方法要么只学轨迹（如 DMPs、GMM），要么依赖传感器反馈单独学习力/阻抗，本文首次将两者统一在本体感觉驱动的单一框架内，显著降低用户示教负担。
2. **mDS 与 EKF 的协同设计**：mDS 解决了原始 FDM 在 3D 复杂运动下的泛化退化问题，而 EKF 在线估计速度偏置 b 则赋予系统扰动恢复能力。这一组合的关键在于：EKF 不是简单地滤波，而是将“偏离参考”重新解释为可估计、可修正的系统状态，而非需要抑制的噪声。
3. **表面接触保持的无传感器策略**：利用示教阶段隐含的表面几何信息，通过 DS 编码与第三主轴 ê₃ 对齐表面法线，实现无需外部接触或视觉传感器的接触保持。这一设计将“示教”的语义从路径跟踪扩展到了交互任务本身，对 HRI 安全性具有直接意义。

## 实验与结果

实验在 7-DOF KUKA LWR IV+ 机器人上进行，远程 Ubuntu PC 通过 ROS 与 UDP 通信，使用 FRI 接口，采样率 200 Hz。控制模式为关节阻抗模式，仅控制扭矩输入，刚度和阻尼接口被禁用，摩擦与重力扭矩得到补偿。数据集采用 LASA Handwriting 数据集的 2D 参考轨迹，扩展至 3D 笛卡尔空间，轨迹类型包括 'S' 形、近 'O' 形、梯形、'W' 形路径。

| 指标 | 数值 | 说明 |
|------|------|------|
| FDM 变换估计误差 | 低于 0.3 cm | subfigures ii |
| 修正后复现误差 | 一般在 2 cm 以下 | 绿色虚线紧密跟随示教（红色） |
| 基线（DS 速度生成）复现误差 | 明显更大 | 随路径复杂度增加而恶化，扰动下无法恢复 |

结果以图形形式呈现（Fig. 3 和 Fig. 4），论文未包含数字表格。关键含义：mDS+EKF 组合在复现精度上显著优于纯 DS 基线，且具备扰动恢复能力；阻抗参数化与表面接触保持策略在保持接触的同时不牺牲路径跟踪精度。

## 边界与局限

论文未明确讨论多任务泛化、不同用户示教风格差异、以及该方法在其他机器人平台上的可迁移性。原始 FDM 变换 DS 在 3D 和更复杂运动情况下泛化能力下降的问题虽由 mDS 缓解，但作者未提及对非常复杂或高度动态任务的适用性边界。计算复杂度在更大规模数据集上的表现也未讨论。实验仅在单一平台（KUKA LWR IV+）上验证，且轨迹类型有限（'S'、'O'、梯形、'W'），对非结构化环境或动态接触任务的泛化能力论文未明确。

## 工程启示

复现时首先核对 FDM 参数设置：K = 120–200 的局部加权平移总数、0 < μ < 1 的安全裕度、0 < β ≤ 1 的学习率，这些参数直接影响微分同胚的质量与计算开销。EKF 模块中，F_y 的前向有限差分时间间隔 10⁻³ 与偏置衰减率 λ_b > 0 需要根据实际采样率（200 Hz）与任务动态调整，否则可能导致速度估计滞后或过度平滑。阻抗参数 Λ 对角元素（通常 10–100）的选择需权衡柔顺性与跟踪精度，λ₁ = 0 的设置对抵抗偏离路径的外力至关重要。最容易踩坑的地方在于逆微分同胚的 Newton–Raphson 求解：停止阈值 ε = 10⁻⁶ 与最大迭代次数 20–50 在复杂轨迹上可能不收敛，建议先在小规模点集上验证逆变换精度。表面接触保持策略依赖示教阶段人类操作者保持连续接触的假设，若示教时接触不连续，第三主轴 ê₃ 与表面法线的对齐将失效，需在示教阶段严格规范操作者行为。

## Overview
This paper presents a method for user-driven robot Learning from Demonstration (LfD) that reduces user effort while ensuring compliant and precise reproduction. The method eliminates repeated teaching for the same task and enables real-time learning from a single demonstration. Demonstrated motions are reproduced with high precision, while impedance variations are learned in real time to provide both compliance and robustness against perturbations. This mitigates potential safety issues in Human-Robot Interaction (HRI) that arise from conventional time-indexed trajectories lacking compliance. The proposed approach integrates a three-dimensional (3D) Fast Diffeomorphic Matching (FDM) algorithm with a Dynamical System (DS)-based motion generator to achieve real-time single-shot demonstration learning and reproduction. An Extended Kalman Filter (EKF) framework compensates for reproduction errors and recovers from external interactions. Furthermore, an impedance parameterization function is incorporated to learn impedance variations from demonstrations and maintain surface contact for specific applications. The proposed approach is validated through comprehensive experiments on a 7 Degree-of-Freedom (DOF) KUKA LWR IV+ robot.

## 参考
- https://arxiv.org/abs/2607.16998

## 개요

본 논문은 Yang과 Kermani가 개발한 단일 시연(single-shot) 로봇 학습 기반 시연(LfD) 프레임워크를 제안하며, 로봇 고유수용감각 센서로부터 궤적과 임피던스 프로파일을 동시에 학습한다. 핵심 기여는 3D 고속 미분동형 정합(FDM)과 확장 칼만 필터(EKF) 속도 보정, 온라인 임피던스 파라미터화, 표면 접촉 유지 전략을 결합하여 고충실도 경로 재현과 외란 복구를 달성하는 것이다.

## 그것이 바꾸는 것

기존 LfD 방법은 오랫동안 두 가지 상호 얽힌 문제점에 시달려 왔다: 첫째는 다중 시연 요구로 인한 사용자 부담, 둘째는 시간 인덱스에 의존하는 궤적 표현으로 인해 재현 시 새로운 궤적이나 외부 외란에 적응할 수 없는 점이다. DMP가 시간 불변성과 목표 수렴을 해결했지만, 다중 시연 요구와 시간 의존성 문제는 여전히 존재한다. 더욱 중요하게는, 기존 힘/임피던스 학습 방법은 일반적으로 센서 피드백이나 단순화된 환경 접촉 모델에 의존하며 경로 재현과 별도로 기록되어 인간 시연으로부터 순응 동작을 직접 학습할 수 없다.

본 논문이 실제로 바꾸는 것은 "궤적 학습"과 "임피던스 학습"을 분리된 두 기술 경로에서 단일하고 온라인이며 고유수용감각 기반의 프로세스로 통합한 것이다. 이는 작업 참조에서의 이탈을 억제해야 할 외란으로 간주하지 않고, EKF를 통해 속도 바이어스를 온라인으로 추정하여 외란을 수정 가능한 시스템 상태로 간주한다. 동시에, 시연 단계에서 인간 조작자가 엔드 이펙터와 표면의 연속 접촉을 유지한다는 암묵적 가정을 활용하여 표면 기하 정보를 동역학 시스템(DS)에 인코딩함으로써 외부 접촉 또는 비전 센서 없이 표면 접촉 유지를 달성한다. 이는 본질적으로 "무엇을 시연하는가"를 단순한 위치 경로에서 "환경과 상호작용하는 방법"의 수준으로 확장한 것이다.

## 방법 분해

### 전체 아키텍처 (Fig. 1)
프레임워크는 네 가지 모듈로 구성된다: (i) 3D FDM 알고리즘이 선형 DS를 시연 궤적에 정합하여 기본 속도장을 생성; (ii) EKF가 기본 속도를 보정하여 궤적 재현을 정밀화하고 외란 복구를 달성; (iii) 재현 과정에서 임피던스 파라미터를 온라인으로 학습; (iv) 표면 접촉 유지를 위한 선택적 모듈.

### 3D FDM 알고리즘 (Algorithm 1)
- 2D FDM을 3D로 확장하여 점 집합 X를 Y로 매핑하는 미분동형 Φ를 계산.
- 국소 가중 평행 이동: ŷᵢ = xᵢ + k_ρⱼ vⱼ, 여기서 k_ρⱼ = e^(−ρⱼ²‖xᵢ−cⱼ‖²)는 가우시안 RBF 커널.
- ‖φ(X)−Y‖²/N을 최소화하도록 ρⱼ를 최적화, ρ_max = e^(1/4)/(√2‖v‖).
- 각 반복에서 X 내 목표로부터 가장 먼 점을 선택하고, 방향 vⱼ = β(qⱼ−cⱼ), 0 < μ < 1은 안전 여유, 0 < β ≤ 1은 학습률, K = 120–200은 사용자가 선택한 국소 가중 평행 이동 총 수.
- 최종 Ŷ = Φ(X^(K)) = (φ_ρ₁ ∘ φ_ρ₂ ∘ ⋯ ∘ φ_ρK)(X).

### 개선된 DS (mDS) 운동 생성기 (식 6)
- 원래 FDM 변환 DS는 3D 및 복잡한 운동에서 일반화 능력이 저하되며, 저자는 mDS를 제안: ẏ_mDS = −ζ J_Φ x̂.
- ζ = ζ + ηΔζ는 속도 변조 항, Δζ = (·)ᵀe_v/(‖(·)ᵀe_v‖+ε), e_v는 시연 속도와 mDS 생성 속도 간 오차, η는 적응률, ε는 임계값.
- Δζ는 이동 평균 필터를 거치고 클램프가 적용됨.

### 역 미분동형 (Algorithm 2)
- 변위를 반전하여 X̂ = Φ⁻¹(Y)를 풀며, Newton–Raphson 방법으로 자기 참조 방정식 rⱼ(k) = e^(−ρⱼ²‖oⱼ+kⱼvⱼ⁻‖²)를 해결.
- 중지 임계값 ε = 10⁻⁶, 최대 반복 횟수 20–50.

### Jacobian 행렬 (식 16–17)
- Sherman–Morrison 공식을 사용하여 J_φⱼ = I₃ + 2ρⱼ²kⱼvⱼ⁻(X̂−cⱼ)ᵀ, 전체 Jacobian J_Φ = ∏ⱼ₌K→1 J_φⱼ.

### EKF 속도 보정 모듈 (식 18–22)
- 보정 속도: ẏ_ekf = ẏ_mDS + b, b는 온라인으로 추정되는 속도 바이어스 항.
- EKF 상태 sᵢ = [yᵢ, bᵢ]ᵀ ∈ ℝ⁶.
- 프로세스 모델에는 바이어스 감쇠 항 e^(−λ_b Δt)가 포함되며, λ_b > 0은 바이어스 감쇠율.
- 상태 전이 Jacobian에서 F_y는 전방 유한 차분으로 근사, 시간 간격 10⁻³.
- 측정 행렬 H = [I₃ 0₃], R은 사용자 정의 측정 노이즈 공분산.

### 임피던스 파라미터화 (식 23–25)
- 속도 추적 제어기: F_c = D(⋄)ṗ_c, 여기서 ṗ_c = ẏ_msr − ẏ_ekf.
- D(⋄) = U(⋄)ΛU(⋄)ᵀ, U는 추정된 직교 주축을 포함하며, ê₁은 원하는 운동 방향을 가리킴.
- Λ = diag(λ₁, λ₂, λ₃)는 사용자 정의 대각 행렬, 요소는 비음수 (일반적으로 10–100).
- λ₁ = 0으로 설정하고 나머지 > 0으로 설정하면 경로 추적에서 이탈을 유발하는 외력을 저항할 수 있음.

### 표면 접촉 유지 전략 (식 26)
- 시연 단계에서 인간 조작자가 EE 도구와 대상 표면의 연속 접촉을 유지한다는 가정을 활용하여, 표면 국소 기하가 DS에 암묵적으로 인코딩되므로 외부 접촉 또는 비전 센서가 필요 없음.
- 세 번째 열 ê₃는 외부 표면 법선과 일치하여 실시간 표면 법선 추정을 제공.
- 최종 속도: ẏ_d = ẏ_mDS + g_c(·) + b, 여기서 g_c(·) = α_c ê₃는 표면을 향한 조정 가능한 속도를 생성; 높은 α_c는 긴밀한 접촉을 강제하고, α_c = 0은 접촉력 없는 추적을 의미.

## 핵심 혁신

1. **단일 시연으로 궤적과 임피던스를 동시에 학습**: 이는 기존 LfD 패러다임에 대한 실질적 돌파구이다. 기존 방법은 궤적만 학습하거나(DMP, GMM 등), 센서 피드백에 의존하여 힘/임피던스를 별도로 학습했지만, 본 논문은 처음으로 둘을 고유수용감각 기반의 단일 프레임워크로 통합하여 사용자 시연 부담을 크게 줄였다.
2. **mDS와 EKF의 협력 설계**: mDS는 원래 FDM이 3D 복잡 운동에서 겪는 일반화 저하 문제를 해결하고, EKF가 속도 바이어스 b를 온라인으로 추정하여 시스템에 외란 복구 능력을 부여한다. 이 조합의 핵심은 EKF가 단순히 필터링하는 것이 아니라 "참조 이탈"을 억제해야 할 노이즈가 아닌 추정 및 수정 가능한 시스템 상태로 재해석한다는 점이다.
3. **센서 없는 표면 접촉 유지 전략**: 시연 단계의 암묵적 표면 기하 정보를 활용하여 DS 인코딩과 세 번째 주축 ê₃를 표면 법선에 정렬함으로써 외부 접촉 또는 비전 센서 없이 접촉 유지를 달성한다. 이 설계는 "시연"의 의미를 경로 추적에서 상호작용 작업 자체로 확장하며, HRI 안전성에 직접적인 의미를 가진다.

## 실험 및 결과

실험은 7-DOF KUKA LWR IV+ 로봇에서 수행되었으며, 원격 Ubuntu PC가 ROS와 UDP를 통해 통신하고 FRI 인터페이스를 사용하며 샘플링 속도는 200 Hz이다. 제어 모드는 관절 임피던스 모드로 토크 입력만 제어하며, 강성 및 댐핑 인터페이스는 비활성화되고 마찰 및 중력 토크는 보상되었다. 데이터셋은 LASA Handwriting 데이터셋의 2D 참조 궤적을 사용하여 3D 데카르트 공간으로 확장했으며, 궤적 유형에는 'S'자형, 근접 'O'자형, 사다리꼴, 'W'자형 경로가 포함된다.

| 지표 | 값 | 설명 |
|------|------|------|
| FDM 변환 추정 오차 | 0.3 cm 미만 | subfigures ii |
| 보정 후 재현 오차 | 일반적으로 2 cm 이하 | 녹색 점선이 시연(빨간색)을 밀접하게 추종 |
| 기준선(DS 속도 생성) 재현 오차 | 명확히 더 큼 | 경로 복잡도가 증가함에 따라 악화되며 외란 하에서 복구 불가 |

결과는 그래픽 형태로 제시되며(Fig. 3 및 Fig. 4), 논문에는 숫자 표가 포함되지 않았다. 핵심 의미: mDS+EKF 조합은 재현 정밀도에서 순수 DS 기준선보다 현저히 우수하며 외란 복구 능력을 갖추고, 임피던스 파라미터화와 표면 접촉 유지 전략은 접촉을 유지하면서도 경로 추적 정밀도를 희생하지 않는다.

## 경계 및 한계

논문은 다중 작업 일반화, 서로 다른 사용자 시연 스타일 차이, 그리고 다른 로봇 플랫폼에서의 이식성을 명시적으로 논의하지 않았다. 원래 FDM 변환 DS가 3D 및 더 복잡한 운동에서 겪는 일반화 저하 문제는 mDS로 완화되었지만, 저자는 매우 복잡하거나 고도로 동적인 작업에 대한 적용 가능성 경계를 언급하지 않았다. 더 큰 규모의 데이터셋에서의 계산 복잡도 성능도 논의되지 않았다. 실험은 단일 플랫폼(KUKA LWR IV+)에서만 검증되었고 궤적 유형도 제한적이며('S', 'O', 사다리꼴, 'W'), 비구조화 환경이나 동적 접촉 작업에 대한 일반화 능력은 논문에서 명확히 다루지 않았다.

## 공학적 시사점

재현 시 먼저 FDM 파라미터 설정을 확인해야 한다: K = 120–200의 국소 가중 평행 이동 총 수, 0 < μ < 1의 안전 여유, 0 < β ≤ 1의 학습률. 이러한 파라미터는 미분동형 품질과 계산 비용에 직접적인 영향을 미친다. EKF 모듈에서 F_y의 전방 유한 차분 시간 간격 10⁻³과 바이어스 감쇠율 λ_b > 0은 실제 샘플링 속도(200 Hz)와 작업 동역학에 따라 조정해야 하며, 그렇지 않으면 속도 추정 지연이나 과도한 평활화가 발생할 수 있다. 임피던스 파라미터 Λ의 대각 요소(일반적으로 10–100) 선택은 순응성과 추적 정밀도 간의 균형을 고려해야 하며, λ₁ = 0 설정은 경로 이탈을 유발하는 외력에 저항하는 데 중요하다. 가장 함정에 빠지기 쉬운 부분은 역 미분동형의 Newton–Raphson 해법이다: 중지 임계값 ε = 10⁻⁶과 최대 반복 횟수 20–50은 복잡한 궤적에서 수렴하지 않을 수 있으므로, 먼저 소규모 점 집합에서 역변환 정밀도를 검증하는 것이 좋다. 표면 접촉 유지 전략은 시연 단계에서 인간 조작자가 연속 접촉을 유지한다는 가정에 의존하므로, 시연 중 접촉이 불연속적이면 세 번째 주축 ê₃와 표면 법선의 정렬이 실패할 수 있으며, 시연 단계에서 조작자 행동을 엄격히 규범화해야 한다.
