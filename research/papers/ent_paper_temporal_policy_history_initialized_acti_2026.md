---
$id: ent_paper_temporal_policy_history_initialized_acti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Temporal Policy: History-Initialized Action Generation for Robotic Learning from Demonstration'
  zh: 'Temporal Policy: History-Initialized Action Generation for Robotic Learning from Demonstration'
  ko: 'Temporal Policy: History-Initialized Action Generation for Robotic Learning from Demonstration'
summary:
  en: By relying on independent couplings from uninformative Gaussian priors, standard diffusion and flow matching models
    are forced to learn complex, high-cost vector fields to reach the physical action space. Generative models excel at capturing
    multimodal behaviors for robotic Learning from Demonstration (LfD), but often suffer from high inference cost. This paper
    introduces Temporal Policy, a.
  zh: Temporal Policy 将机器人动作生成从“无信息高斯噪声初始化”重构为“历史状态初始化”的点对分布传输问题，基于随机插值理论实现时间耦合的动作生成。该方法在保持任务成功率的同时，将推理延迟降至 19.1 ms（较 Diffusion
    Policy 的 615.6 ms 降低约 32 倍），并以 17M 参数紧凑架构在 Robomimic 基准和真实遥操作平台上验证了高频闭环控制的可行性。
  ko: By relying on independent couplings from uninformative Gaussian priors, standard diffusion and flow matching models
    are forced to learn complex, high-cost vector fields to reach the physical action space. Generative models excel at capturing
    multimodal behaviors for robotic Learning from Demonstration (LfD), but often suffer from high inference cost. This paper
    introduces Temporal Policy, a.
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
- temporal
- policy
- history
- initialized
- acti
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量四）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.29482 Temporal Policy: History-Initialized Action Generation for Robotic Learning from'
  url: https://arxiv.org/abs/2607.29482
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

Temporal Policy 将机器人动作生成从“无信息高斯噪声初始化”重构为“历史状态初始化”的点对分布传输问题，基于随机插值理论实现时间耦合的动作生成。该方法在保持任务成功率的同时，将推理延迟降至 19.1 ms（较 Diffusion Policy 的 615.6 ms 降低约 32 倍），并以 17M 参数紧凑架构在 Robomimic 基准和真实遥操作平台上验证了高频闭环控制的可行性。

## 它改变了什么

扩散模型和流匹配在机器人动作生成中的根本瓶颈，在于它们从高熵高斯先验出发，被迫学习一条长且高曲率的传输路径才能抵达物理可行的动作空间。这种“从噪声到动作”的映射不仅计算昂贵，而且忽略了机器人控制中一个明确已知的关键先验——智能体的当前物理状态。现有框架将动作生成视为独立同分布噪声到动作的映射，本质上是在为一个本可更简单的问题支付不必要的传输成本。

Temporal Policy 真正改变的是问题的几何结构：它把动作生成从“无信息先验到目标分布”的远距离传输，转化为“近期状态历史到未来动作块”的短距离、时间耦合传输。由于专家演示的平滑性，源与目标之间存在强正相关，这使得传输路径更直、向量场更简单。这一重构不仅降低了推理延迟，还使得单步采样即可产生有效动作——这是噪声初始化方法在 32 NFE 以下无法做到的。

## 方法拆解

### 问题形式化
- 要求状态空间 𝒮 与动作空间 𝒜 同构（𝒮 ≅ 𝒜 ≅ ℝ^D），即状态与动作共享相同表示（如关节位置或笛卡尔位姿）。
- 在时刻 t，源定义为状态历史 𝐱₀ = s_{t-H+1:t}，目标为未来动作块 𝐱₁ = s_{t-H+1+d:t+d}，其中 d 为时间偏移（1 ≤ d ≤ H）。序列重叠（d < H）用于减少动作块间的不连续性。

### 随机插值框架
- 插值路径（公式 1）：𝐱_λ = (1−λ)𝐱₀ + λ𝐱₁ + ε(1−λ)𝐰_λ，其中 λ ∈ [0,1]，ε ≥ 0 为噪声尺度，𝐰_λ 为标准维纳过程。线性插值方案旨在鼓励直线向量场。
- SDE 形式（公式 2）：d𝐱_λ = [(𝐱₁−𝐱₀) − ε𝐰_λ]dλ + ε(1−λ)d𝐰_λ，漂移目标为 u_λ = (𝐱₁−𝐱₀) − ε𝐰_λ。
- 训练损失（公式 3）：ℒ(θ) = 𝔼[||b_θ − (𝐱₁−𝐱₀−ε√λ z)||²₂]，通过平方损失回归学习漂移 b_θ(𝐱_λ, 𝐱₀, λ, c)。

### 网络架构
- 1D U-Net 骨干网络，在动作块的时间维度上操作。
- 视觉观测经 ResNet-18 编码，Spatial Softmax 投影为 2D 特征点。
- 特征与插值时间 λ 的正弦嵌入拼接形成条件向量 c，通过 FiLM 层调制 U-Net 特征图。作者强调该公式是架构无关的。

### 推理策略
- 解析分数恢复（公式 4、5）：分数 ∇_𝐱 log p_λ(𝐱|𝐱₀) 可从漂移 u_λ 和插值系数 α_λ = 1−λ、β_λ = λ、γ_λ = ε(1−λ) 解析恢复，无需重新训练即可调整噪声调度。
- 推理 SDE（公式 6）支持确定性采样（g_λ = 0，单路径、少步骤）与随机采样（g_λ > 0，注入噪声探索多模态）。
- 采用滚动时域控制，仅执行动作块的前 K 步（K < H）后重新查询网络。

## 关键创新

1. **时间耦合传输问题的新形式化**：将动作生成从“噪声到动作”的独立耦合重构为“历史到未来”的时间耦合。这一形式化利用了机器人控制中状态已知的先验，从数学上降低了传输成本（J_temporal < J_indep），并简化了向量场几何。这是对现有流匹配框架在机器人应用中的根本性重新定位。

2. **解析分数恢复与推理时噪声调度调整**：利用随机插值性质，无需重新训练即可在推理时切换确定性/随机采样范式。这一设计解耦了训练与推理的噪声策略，为部署时的灵活性提供了理论支撑。

3. **紧凑架构的高效性**：Temporal Policy 以 17M 参数（基线为 255M）实现相当或更优的性能，且单步采样即可产生有效动作。这表明传输问题的简化直接转化为模型容量需求和计算成本的降低，而非依赖更大的网络来弥补先验选择的低效。

## 实验与结果

### 仿真基准（Robomimic）
- 五个任务（Lift、Can、Square、Transport、Tool Hang），使用 proficient-human (ph) 和 multi-human (mh) 数据集。
- 基线为 Diffusion Policy 和 CFM（均为噪声初始化）。
- 训练配置：batch size 128，1500 epochs，单张 NVIDIA A100 GPU；推理在 RTX 4080 上测量。

| 任务 | Diffusion Policy (Max/Avg) | CFM (Max/Avg) | Temporal Policy (Max/Avg) |
|---|---|---|---|
| Lift ph | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 |
| Can mh | 0.99 / 0.96 | 0.99 / 0.95 | 1.00 / 0.98 |
| Square ph | 0.98 / 0.91 | 0.97 / 0.91 | 0.99 / 0.96 |
| Transport mh | 0.82 / 0.73 | 0.67 / 0.54 | 0.85 / 0.76 |
| Tool Hang ph | 0.87 / 0.71 | 0.79 / 0.70 | 0.81 / 0.69 |

### 推理效率
- NFE：Diffusion Policy 100，CFM 10，Temporal Policy 10。
- 推理延迟：Diffusion Policy 615.6 ms，CFM 63.5 ms，Temporal Policy 19.1 ms。
- 参数量：基线 255M，Temporal Policy 17M。

### 传输指标（Square ph，50 episodes 平均）
| 模型 | Transport | Straightness |
|---|---|---|
| Diffusion Policy | 189.99 | 20.61 |
| CFM | 10.00 | 1.08 |
| Temporal Policy | 1.21 | 1.02 |

Straightness 比率（公式 8）≈1 表示沿直线移动：Temporal Policy 为 1.02，Diffusion Policy 为 20.61，CFM 为 1.08。

### 消融与真实世界
- NFE 消融：标准扩散在 32 NFE 以下无法产生有效动作；Temporal Policy 单步采样即可达到相对较高成功率。
- SDE 噪声调度（Tool Hang ph）：确定性 ODE（ε = 0.0）在 2 至 4 步内达到较高成功率；完全随机（ε = 1.0）需 8 至 16 步。
- 真实世界（mug-hanging）：20 次试验整体成功率 50%（10/20），抓取阶段成功率 95%（19/20）；主要失败模式为对齐阶段末端执行器系统性欠冲。

## 边界与局限

- 点对分布公式对初始化质量敏感：源状态的显著噪声可能使生成轨迹产生偏差，论文未明确量化该敏感性的阈值。
- 未探究历史初始化是否主要消除表观多模态性，以及是否保留演示中观察到的全部有效行为范围。
- 真实世界实验仅验证单一任务（mug-hanging），且成功率 50% 表明对齐阶段存在系统性缺陷，论文未明确该缺陷是否源于传输公式本身或工程实现细节。
- 状态-动作同构要求（𝒮 ≅ 𝒜）限制了该方法对非欧氏表示（如力/力矩控制）的直接适用性。

## 工程启示

- **复现优先核对**：确认状态与动作表示严格同构（关节位置或笛卡尔位姿），否则公式 1 的插值路径在几何上无意义。真实世界实验中状态-动作耦合为从端关节位置和夹爪速度，重叠 d = 2，观测窗口 2，预测 16 步执行 8 步，确定性采样 10 个 Euler 步——这些超参数是复现的关键起点。
- **最容易踩坑**：模型容量选择。作者发现 255M 参数模型对 Temporal Policy 导致过拟合，需使用 17M 紧凑架构。若直接沿用 Diffusion Policy 的超参数配置，可能因过拟合而性能退化。
- **推理策略**：确定性 ODE（ε = 0.0）是效率最优选择（2 至 4 步即可），随机采样（ε = 1.0）虽可探索多模态但需 8 至 16 步。若下游任务需要高频控制，优先确定性采样；若任务存在显著多模态动作，需权衡延迟与探索能力。
- **数据效率**：Temporal Policy 在所有数据规模下持续优于 Diffusion Policy（Square ph 任务），对数据稀缺的机器人场景更具吸引力。下游团队可考虑在演示数据有限时优先采用该方法。

## Overview
By relying on independent couplings from uninformative Gaussian priors, standard diffusion and flow matching models are forced to learn complex, high-cost vector fields to reach the physical action space. Generative models excel at capturing multimodal behaviors for robotic Learning from Demonstration (LfD), but often suffer from high inference cost. This paper introduces Temporal Policy, a generative framework based on stochastic interpolants that formulates action generation as a temporally coupled transport problem. By initializing the generative flow at the robot's recent history, we explicitly couple past states to future action sequences. This data-dependent coupling reduces transport cost and produces straight vector fields. We validate Temporal Policy across visuomotor simulation benchmarks and on a physical Barrett WAM 2x 7DoF teleoperation platform. Our approach reduces transport costs by nearly an order of magnitude compared to noise-initialized baselines, achieving a 19.1 ms inference latency on a single NVIDIA RTX 4080. Crucially, these geometric and computational efficiencies are achieved while matching the success rates of state-of-the-art baselines. This simplified transport geometry bypasses the computational bottleneck of independent Gaussian priors, helping enable high-frequency, closed-loop control. The code is publicly available at https://github.com/dmiller12/TemporalPolicy.

## 参考
- https://arxiv.org/abs/2607.29482

## 개요

Temporal Policy는 로봇 동작 생성을 "무정보 가우시안 노이즈 초기화"에서 "상태 이력 초기화"로 재구성한 점-대-분포 전송 문제로, 확률적 보간 이론을 기반으로 시간적으로 결합된 동작 생성을 구현한다. 이 방법은 작업 성공률을 유지하면서 추론 지연 시간을 19.1ms로 낮추었으며(Diffusion Policy의 615.6ms 대비 약 32배 감소), 1,700만 개의 파라미터로 구성된 컴팩트한 아키텍처로 Robomimic 벤치마크와 실제 원격 조작 플랫폼에서 고주파 폐루프 제어의 실현 가능성을 검증했다.

## 무엇을 바꾸었는가

확산 모델과 플로우 매칭이 로봇 동작 생성에서 겪는 근본적인 병목은 높은 엔트로피의 가우시안 사전 분포에서 출발하여, 물리적으로 실행 가능한 동작 공간에 도달하기 위해 길고 곡률이 높은 전송 경로를 학습해야 한다는 점이다. 이러한 "노이즈에서 동작으로"의 매핑은 계산 비용이 높을 뿐만 아니라, 로봇 제어에서 명확히 알려진 핵심 사전 정보, 즉 에이전트의 현재 물리적 상태를 무시한다. 기존 프레임워크는 동작 생성을 독립적이고 동일한 분포의 노이즈에서 동작으로의 매핑으로 간주하여, 본질적으로 더 단순할 수 있는 문제에 불필요한 전송 비용을 지불하고 있다.

Temporal Policy가 실제로 바꾼 것은 문제의 기하학적 구조이다. 동작 생성을 "무정보 사전 분포에서 목표 분포로의 원거리 전송"에서 "최근 상태 이력에서 미래 동작 블록으로의 단거리, 시간 결합 전송"으로 재구성한다. 전문가 시연의 매끄러움 덕분에 소스와 타깃 사이에는 강한 양의 상관관계가 존재하며, 이는 전송 경로를 더 직선적으로 만들고 벡터 필드를 더 단순하게 만든다. 이러한 재구성은 추론 지연 시간을 줄일 뿐만 아니라, 단일 샘플링 단계만으로도 유효한 동작을 생성할 수 있게 한다. 이는 노이즈 초기화 방법이 32 NFE 미만에서는 달성할 수 없는 성능이다.

## 방법 분해

### 문제 정식화
- 상태 공간 𝒮와 동작 공간 𝒜가 동형(𝒮 ≅ 𝒜 ≅ ℝ^D)이어야 한다. 즉, 상태와 동작이 동일한 표현(예: 관절 위치 또는 데카르트 포즈)을 공유해야 한다.
- 시점 t에서 소스는 상태 이력 𝐱₀ = s_{t-H+1:t}로 정의되고, 타깃은 미래 동작 블록 𝐱₁ = s_{t-H+1+d:t+d}로 정의된다. 여기서 d는 시간 오프셋(1 ≤ d ≤ H)이다. 시퀀스 중첩(d < H)은 동작 블록 간의 불연속성을 줄이는 데 사용된다.

### 확률적 보간 프레임워크
- 보간 경로(수식 1): 𝐱_λ = (1−λ)𝐱₀ + λ𝐱₁ + ε(1−λ)𝐰_λ, 여기서 λ ∈ [0,1], ε ≥ 0은 노이즈 스케일, 𝐰_λ는 표준 위너 과정이다. 선형 보간 방식은 직선 벡터 필드를 장려하기 위한 것이다.
- SDE 형태(수식 2): d𝐱_λ = [(𝐱₁−𝐱₀) − ε𝐰_λ]dλ + ε(1−λ)d𝐰_λ, 드리프트 타깃은 u_λ = (𝐱₁−𝐱₀) − ε𝐰_λ이다.
- 훈련 손실(수식 3): ℒ(θ) = 𝔼[||b_θ − (𝐱₁−𝐱₀−ε√λ z)||²₂], 제곱 손실 회귀를 통해 드리프트 b_θ(𝐱_λ, 𝐱₀, λ, c)를 학습한다.

### 네트워크 아키텍처
- 1D U-Net 백본 네트워크로, 동작 블록의 시간 차원에서 작동한다.
- 시각적 관측은 ResNet-18로 인코딩되고, Spatial Softmax가 2D 특징점으로 투영한다.
- 특징과 보간 시간 λ의 사인 임베딩을 연결하여 조건 벡터 c를 형성하고, FiLM 레이어를 통해 U-Net 특징 맵을 변조한다. 저자는 이 공식이 아키텍처에 구애받지 않는다고 강조한다.

### 추론 전략
- 해석적 점수 복원(수식 4, 5): 점수 ∇_𝐱 log p_λ(𝐱|𝐱₀)는 드리프트 u_λ와 보간 계수 α_λ = 1−λ, β_λ = λ, γ_λ = ε(1−λ)로부터 해석적으로 복원할 수 있으며, 재훈련 없이 노이즈 스케줄을 조정할 수 있다.
- 추론 SDE(수식 6)는 결정적 샘플링(g_λ = 0, 단일 경로, 적은 단계)과 확률적 샘플링(g_λ > 0, 노이즈 주입으로 다중 모드 탐색)을 모두 지원한다.
- 롤링 호라이즌 제어를 채택하여, 동작 블록의 처음 K단계(K < H)만 실행한 후 네트워크를 다시 쿼리한다.

## 핵심 혁신

1. **시간 결합 전송 문제의 새로운 정식화**: 동작 생성을 "노이즈에서 동작으로"의 독립 결합에서 "이력에서 미래로"의 시간 결합으로 재구성한다. 이 정식화는 로봇 제어에서 상태가 알려져 있다는 사전 정보를 활용하여 수학적으로 전송 비용을 낮추고(J_temporal < J_indep), 벡터 필드 기하학을 단순화한다. 이는 기존 플로우 매칭 프레임워크를 로봇 응용에 근본적으로 재배치한 것이다.

2. **해석적 점수 복원 및 추론 시 노이즈 스케줄 조정**: 확률적 보간의 특성을 활용하여 재훈련 없이 추론 시 결정적/확률적 샘플링 패러다임을 전환할 수 있다. 이 설계는 훈련과 추론의 노이즈 정책을 분리하여 배포 시 유연성에 대한 이론적 기반을 제공한다.

3. **컴팩트 아키텍처의 효율성**: Temporal Policy는 1,700만 개의 파라미터(기준 모델은 2억 5,500만 개)로 동등하거나 더 우수한 성능을 달성하며, 단일 샘플링 단계만으로도 유효한 동작을 생성할 수 있다. 이는 전송 문제의 단순화가 더 큰 네트워크로 사전 선택의 비효율성을 보완하는 대신, 모델 용량 요구 사항과 계산 비용의 감소로 직접 이어진다는 것을 시사한다.

## 실험 및 결과

### 시뮬레이션 벤치마크(Robomimic)
- 다섯 가지 작업(Lift, Can, Square, Transport, Tool Hang), proficient-human(ph) 및 multi-human(mh) 데이터셋 사용.
- 기준 모델은 Diffusion Policy 및 CFM(모두 노이즈 초기화).
- 훈련 구성: 배치 크기 128, 1500 에포크, 단일 NVIDIA A100 GPU; 추론은 RTX 4080에서 측정.

| 작업 | Diffusion Policy (Max/Avg) | CFM (Max/Avg) | Temporal Policy (Max/Avg) |
|---|---|---|---|
| Lift ph | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 |
| Can mh | 0.99 / 0.96 | 0.99 / 0.95 | 1.00 / 0.98 |
| Square ph | 0.98 / 0.91 | 0.97 / 0.91 | 0.99 / 0.96 |
| Transport mh | 0.82 / 0.73 | 0.67 / 0.54 | 0.85 / 0.76 |
| Tool Hang ph | 0.87 / 0.71 | 0.79 / 0.70 | 0.81 / 0.69 |

### 추론 효율성
- NFE: Diffusion Policy 100, CFM 10, Temporal Policy 10.
- 추론 지연 시간: Diffusion Policy 615.6ms, CFM 63.5ms, Temporal Policy 19.1ms.
- 파라미터 수: 기준 모델 2억 5,500만 개, Temporal Policy 1,700만 개.

### 전송 지표(Square ph, 50 에피소드 평균)
| 모델 | Transport | Straightness |
|---|---|---|
| Diffusion Policy | 189.99 | 20.61 |
| CFM | 10.00 | 1.08 |
| Temporal Policy | 1.21 | 1.02 |

Straightness 비율(수식 8) ≈ 1은 직선 이동을 의미한다: Temporal Policy는 1.02, Diffusion Policy는 20.61, CFM은 1.08.

### 소거 및 실제 세계
- NFE 소거: 표준 확산은 32 NFE 미만에서 유효한 동작을 생성할 수 없다; Temporal Policy는 단일 샘플링 단계만으로도 상대적으로 높은 성공률을 달성한다.
- SDE 노이즈 스케줄(Tool Hang ph): 결정적 ODE(ε = 0.0)는 2~4단계 내에 높은 성공률을 달성; 완전 확률적(ε = 1.0)은 8~16단계가 필요.
- 실제 세계(mug-hanging): 20회 시도에서 전체 성공률 50%(10/20), 그리핑 단계 성공률 95%(19/20); 주요 실패 모드는 정렬 단계에서 엔드 이펙터의 체계적인 언더슈트.

## 경계 및 한계

- 점-대-분포 공식은 초기화 품질에 민감하다: 소스 상태의 상당한 노이즈는 생성 궤적에 편향을 초래할 수 있으며, 논문은 이 민감성의 임계값을 명시적으로 정량화하지 않았다.
- 이력 초기화가 주로 표면적 다중 모드성을 제거하는지, 그리고 시연에서 관찰된 모든 유효한 행동 범위를 보존하는지 여부를 탐구하지 않았다.
- 실제 세계 실험은 단일 작업(mug-hanging)만 검증했으며, 성공률 50%는 정렬 단계에 체계적인 결함이 있음을 시사하지만, 논문은 이 결함이 전송 공식 자체에서 비롯된 것인지 엔지니어링 구현 세부 사항에서 비롯된 것인지 명확히 하지 않았다.
- 상태-동작 동형 요구 사항(𝒮 ≅ 𝒜)은 힘/토크 제어와 같은 비유클리드 표현에 대한 직접적인 적용 가능성을 제한한다.

## 엔지니어링 시사점

- **재현 시 우선 확인 사항**: 상태와 동작 표현이 엄격히 동형(관절 위치 또는 데카르트 포즈)인지 확인해야 한다. 그렇지 않으면 수식 1의 보간 경로가 기하학적으로 의미가 없다. 실제 세계 실험에서 상태-동작 결합은 엔드 관절 위치와 그리퍼 속도로 구성되며, 중첩 d = 2, 관측 창 2, 16단계 예측 후 8단계 실행, 결정적 샘플링 10개의 오일러 단계를 사용한다. 이러한 하이퍼파라미터는 재현의 핵심 출발점이다.
- **가장 쉽게 빠지는 함정**: 모델 용량 선택. 저자는 2억 5,500만 개의 파라미터 모델이 Temporal Policy에서 과적합을 유발하므로 1,700만 개의 컴팩트 아키텍처를 사용해야 한다는 것을 발견했다. Diffusion Policy의 하이퍼파라미터 구성을 그대로 사용하면 과적합으로 인해 성능이 저하될 수 있다.
- **추론 전략**: 결정적 ODE(ε = 0.0)는 효율성 측면에서 최적의 선택(2~4단계)이며, 확률적 샘플링(ε = 1.0)은 다중 모드를 탐색할 수 있지만 8~16단계가 필요하다. 하위 작업이 고주파 제어를 필요로 한다면 결정적 샘플링을 우선하고, 작업에 상당한 다중 모드 동작이 존재한다면 지연 시간과 탐색 능력 사이의 균형을 고려해야 한다.
- **데이터 효율성**: Temporal Policy는 모든 데이터 규모에서 Diffusion Policy보다 지속적으로 우수하며(Square ph 작업), 데이터가 부족한 로봇 시나리오에서 더 매력적이다. 하위 팀은 시연 데이터가 제한적인 경우 이 방법을 우선적으로 채택하는 것을 고려할 수 있다.
