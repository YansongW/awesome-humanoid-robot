---
$id: ent_paper_futurertc_real_time_robot_execution_anti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking'
  zh: 'FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking'
  ko: 'FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking'
summary:
  en: Real-time deployment of Vision-Language-Action (VLA) policies necessitates asynchronous execution, wherein subsequent
    action chunks are computed concurrently with the execution of the current chunk, leading to prediction-execution misalignment
    and manifesting as inter-chunk discontinuities. Existing methods either superficially smooth chunk boundaries, require
    costly policy optimization, or.
  zh: FutureRTC 是一个即插即用的异步 VLA 策略适配框架，通过预测执行时刻的视觉潜在特征与本体感受状态，缓解异步执行中的预测-执行错位。核心贡献在于将观测预测从像素空间转移到预训练 VLA 的潜在空间，并以动作序列作为显式运动先验驱动特征传输与残差合成，同时引入策略一致性损失确保预测上下文被冻结策略忠实消费。
  ko: Real-time deployment of Vision-Language-Action (VLA) policies necessitates asynchronous execution, wherein subsequent
    action chunks are computed concurrently with the execution of the current chunk, leading to prediction-execution misalignment
    and manifesting as inter-chunk discontinuities. Existing methods either superficially smooth chunk boundaries, require
    costly policy optimization, or.
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
- futurertc
- real
- time
- robot
- execution
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
  title: 'arXiv:2607.24008 FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunki'
  url: https://arxiv.org/abs/2607.24008
  date: '2026-07-27'
  accessed_at: '2026-08-05'
---

## 概述

FutureRTC 是一个即插即用的异步 VLA 策略适配框架，通过预测执行时刻的视觉潜在特征与本体感受状态，缓解异步执行中的预测-执行错位。核心贡献在于将观测预测从像素空间转移到预训练 VLA 的潜在空间，并以动作序列作为显式运动先验驱动特征传输与残差合成，同时引入策略一致性损失确保预测上下文被冻结策略忠实消费。

## 它改变了什么

异步 VLA 部署的核心矛盾在于：策略生成动作块需要时间，而环境在等待期间持续演化。现有推理时方法（TE、BID、RTC）只做表面平滑或仅前向预测状态，忽略了视觉场景随机器人配置一同演化这一事实；训练时方法（T-RTC、REMAC）虽更彻底但需重训或微调策略，代价高昂。VLASH 首次意识到状态预测的必要性，但仍依赖过时视觉观测——这恰恰是错位的主要来源。

FutureRTC 真正改变的是问题定义：不再试图让策略适应延迟，而是直接预测"执行时刻"的完整上下文（视觉+状态），使策略仿佛在零延迟条件下运行。这一思路将异步部署问题转化为一个上下文预测问题，且预测发生在潜在空间而非像素空间，使得计算开销可控（额外 3.04 ms），同时预测结果与 VLA 策略天然兼容。它证明了一个关键事实：在机器人是环境变化主要来源的操作场景中，基于动作先验的潜在空间预测足以恢复绝大部分同步执行性能。

## 方法拆解

### 总体架构
适配器 φ(·) 从过时对 (z_1, a_{1:2}) 预测执行时上下文 (ẑ_3, ŝ_3)，其中 z 为预训练 VLA 视觉编码器输出的潜在特征。VLA 策略直接消费预测的潜在表示，绕过原始视觉编码器。

### 状态校正模块（SCM）
- 前向积分过时状态：s̃_{t+K} = s_{t+K-d} ⊕ Σ_{i=t+K-d}^{t+K-1} a_i
- MLP 预测补偿残差：s̃_Δ = φ_SCM(s̃_{t+K}, d/d_max)
- 最终状态：ŝ_{t+K} = s̃_{t+K} ⊕ s̃_Δ，旋转部分用相对旋转合成
- 损失：L_state = ||(s_{t+K} ⊖ s̃_{t+K}) − s̃_Δ||₂²

### 观测预测模块（OPM）
- 对每个已承诺动作构造物理特征向量：u_i = [a_i, Σ_{j≤i} a_j, a_i − a_{i−1}, Σ_{j≤i} |a_j|, i/d]
- 轨迹特征矩阵 U 输入时间自注意力，产生动作条件运动先验 c_motion
- 融合 c_motion、过时潜在 z_{t+K−d}、相机嵌入 e_cam、位置嵌入 e_pos、校正状态 ŝ_{t+K} 形成条件特征 F
- 级联线性+卷积层将 F 投影为 2D 流位移 Δp 和传输门 α ∈ [0,1]
- 可微双线性采样做空间扭曲，门控组合：z_trans = (1−α)·z_{t+K−d} + α·W(z_{t+K−d}, p − Δp)
- 门控残差分支预测合成特征 r 和合成门 β：{r, β} = Linear(Conv(F, z_trans − z_{t+K−d}, z_0))
- 最终潜在：ẑ_{t+K} = z_trans + β·r
- 损失：L_obs = ||z_{t+K} − ẑ_{t+K}||₂²

### 策略一致性损失
L_policy = ||π_θ(z_{t+K}, s_{t+K}) − π_θ(ẑ_{t+K}, ŝ_{t+K})||₂²，使用单步流近似避免多步流匹配开销。总目标：L_total = L_state + L_obs + λ·L_policy，λ = 10，π_θ 冻结。

### 关键设计决策
- 潜在空间预测而非像素重建：确保计算开销可控且与策略表示兼容
- 空间传输建模而非从头合成：已承诺动作作为显式运动先验，静态区域保持原表示（α→0），运动区域依赖扭曲特征（α→1）
- 训练时均匀采样延迟 d ~ U[1, d_max]：单一模型覆盖全延迟范围，无需按延迟分别训练

## 关键创新

1. **潜在空间观测预测**：首次将异步 VLA 的视觉补偿从像素空间转移到预训练编码器的潜在空间。这不仅将额外推理延迟控制在 3.04 ms（由表内数值 35.4→38.44 计算），更重要的是预测结果与 VLA 策略的输入分布天然对齐，避免了像素重建误差被策略放大。

2. **动作驱动的双分支预测架构**：将视觉变化分解为"空间传输"（运动先验驱动的可微扭曲）与"残差合成"（门控残差分支）两部分，分别由传输门 α 和合成门 β 控制。这一分解符合操作场景的物理直觉——大部分视觉变化由机器人自身运动引起，可被动作序列精确预测；剩余动态（如物体滑动）由残差分支捕获。

3. **策略一致性损失**：不仅要求预测上下文在特征空间接近真实值，还要求冻结策略从预测对生成的块与从真实对生成的块对齐。这一损失直接优化最终目标（策略输出），而非中间表示，是消融中 d=20 时成功率从 67.5% 提升至 69.4% 的关键。

## 实验与结果

### LIBERO 基准（π_0.5 骨干）
| 方法 | d=5 | d=10 | d=15 | d=20 |
|------|-----|------|------|------|
| Naive Async. | 89.5 | 82.7 | 76.3 | 68.3 |
| RTC | 89.9 | 83.2 | 77.5 | 73.7 |
| VLASH | 88.0 | 83.4 | 79.5 | 74.5 |
| REMAC | 90.8 | 85.4 | 78.5 | 73.9 |
| **FutureRTC** | **94.2** | **92.4** | **91.0** | **88.5** |

### LIBERO 基准（SmolVLA-450M 骨干）
| 方法 | d=5 | d=10 | d=15 | d=20 |
|------|-----|------|------|------|
| Naive Async. | 70.3 | 64.5 | 61.3 | 56.2 |
| VLASH | 69.3 | 65.8 | 64.7 | 61.9 |
| REMAC | 70.9 | 66.5 | 62.2 | 59.7 |
| **FutureRTC** | **75.8** | **73.3** | **71.6** | **69.4** |

### 消融（SmolVLA-450M 平均成功率）
| 配置 | d=5 | d=10 | d=15 | d=20 |
|------|-----|------|------|------|
| Baseline | 26.1 | 8.4 | 2.5 | 0.7 |
| +SCM | 45.9 | 18.1 | 10.4 | 5.8 |
| +OPM | 74.1 | 70.4 | 70.0 | 67.5 |
| +L_policy | 75.8 | 73.3 | 71.6 | 69.4 |

### 关键结果解读
- 从 d=5 到 d=20，FutureRTC 在 π_0.5 上成功率仅下降 5.7%，在 SmolVLA 上下降 6.4%，而 Naive Async. 分别下降 21.2% 和 14.1%（由表内数值计算）
- OPM 是性能主力（+SCM 到 +OPM 在 d=20 时提升 61.7 个百分点），SCM 单独效果有限但为 OPM 提供必要状态条件
- Kinetix 上从 d=0 到 d=4 成功率仅下降 3.0%，但小延迟下略落后于针对基准微调的训练时方法
- 真实世界三个双臂任务中一致获得最高成功率、最少执行步数和时间

## 边界与局限

- 观测预测模块在高度动态场景（由独立外部智能体主导）中可能表现不佳——论文未明确给出此类场景的定量评估
- 仅实例化于流匹配 VLA 策略（π_0.5 和 SmolVLA-450M），未扩展到自回归策略或离散扩散策略；省略 DiscreteRTC 对比因其无法在基于流的骨干上实例化
- 未评估 d > 20 的更长延迟场景
- Kinetix 小延迟 d = {0, 1} 下略落后于针对基准任务微调或重训练的训练时方法，尽管保持策略冻结
- 真实世界实验为定性演示（视频对比），未报告定量成功率数字
- 训练时对比方法（除 VLASH 外）由作者自行复现而非使用官方权重，可能存在复现偏差

## 工程启示

- **先核对动作块拼接约定**：当条件上下文对应执行时刻时，必须从第一个动作执行 A[0:K-1]；若继续沿用异步补偿的 A[d:d+K-1] 拼接，成功率会从 94.2% 暴跌至 39.0%（由表内数值计算）。这是最容易踩坑的工程细节。
- **SCM 单独使用价值有限**：消融显示 +SCM 在 SmolVLA 上 d=20 时仅从 0.7% 提升至 5.8%，必须与 OPM 配合才能发挥效果。若只做状态预测，不如直接采用 VLASH。
- **训练成本可控**：批大小 128、200k 迭代、RTX 4090 单卡即可收敛；适配器仅增加 5.19 M 参数和 3.04 ms 推理延迟。训练时均匀采样延迟 d ~ U[1, d_max] 意味着单一模型覆盖全延迟范围，无需按部署环境重新训练。
- **策略一致性损失的 λ 需调参**：论文使用 λ = 10，但该超参数对策略架构敏感，复现时建议在 [1, 50] 范围扫描。
- **真实世界部署预算**：端到端延迟约 170 ms（对应 d ≈ 5），其中 VLA 前向约 99 ms、LAN 通信约 40 ms、数据处理约 30 ms。若需降低延迟，优先优化通信与数据处理而非适配器本身。

## Overview
Real-time deployment of Vision-Language-Action (VLA) policies necessitates asynchronous execution, wherein subsequent action chunks are computed concurrently with the execution of the current chunk, leading to prediction-execution misalignment and manifesting as inter-chunk discontinuities. Existing methods either superficially smooth chunk boundaries, require costly policy optimization, or exclusively forward-predict proprioceptive states yet neglect critical visual observations. In this paper, we propose \textbf{FutureRTC}, a plug-and-play adaptation framework that predicts execution-time observations and states for asynchronous VLA control without modifying the underlying policy. Specifically, FutureRTC features a state correction module to compensate for the discrepancy between rolled-forward and actual execution-time proprioceptive states and an observation prediction module that forecasts execution-time visual representations by leveraging robot motion as an explicit physical prior through motion-aware feature transport and reconstruction. Furthermore, we introduce a policy consistency loss to align the action chunks generated from predicted contexts with those produced under the expected execution-time inputs of the VLA policy. Extensive experiments across simulated and real-world environments demonstrate that FutureRTC achieves superior robustness to inference delays, resulting in smoother trajectories, faster execution, and consistently higher task success rates.

## 参考
- https://arxiv.org/abs/2607.24008

## 개요

FutureRTC는 플러그 앤 플레이 방식의 비동기 VLA 정책 적응 프레임워크로, 실행 시점의 시각적 잠재 특징과 고유수용감각 상태를 예측하여 비동기 실행에서 발생하는 예측-실행 불일치를 완화합니다. 핵심 기여는 관측 예측을 픽셀 공간에서 사전 학습된 VLA의 잠재 공간으로 이동시키고, 동작 시퀀스를 명시적 운동 사전으로 사용하여 특징 전송과 잔차 합성을 구동하며, 정책 일관성 손실을 도입하여 예측된 컨텍스트가 고정된 정책에 의해 충실히 소비되도록 보장하는 것입니다.

## 무엇을 변화시키는가

비동기 VLA 배포의 핵심 모순은 정책이 동작 블록을 생성하는 데 시간이 걸리는 반면, 환경은 대기 시간 동안 계속 진화한다는 점입니다. 기존 추론 시점 방법(TE, BID, RTC)은 표면적 평활화나 전방 상태 예측만 수행할 뿐, 시각적 장면이 로봇 구성과 함께 진화한다는 사실을 무시합니다. 학습 시점 방법(T-RTC, REMAC)은 더 철저하지만 정책 재학습이나 미세 조정이 필요하여 비용이 높습니다. VLASH는 상태 예측의 필요성을 처음으로 인식했지만 여전히 오래된 시각적 관측에 의존합니다—이것이 바로 불일치의 주요 원인입니다.

FutureRTC가 진정으로 바꾸는 것은 문제 정의입니다. 더 이상 정책이 지연에 적응하도록 만들지 않고, "실행 시점"의 완전한 컨텍스트(시각+상태)를 직접 예측하여 정책이 제로 지연 조건에서 작동하는 것처럼 만듭니다. 이 접근 방식은 비동기 배포 문제를 컨텍스트 예측 문제로 전환하며, 예측이 픽셀 공간이 아닌 잠재 공간에서 이루어지므로 계산 오버헤드가 제어 가능하고(추가 3.04 ms), 예측 결과가 VLA 정책과 자연스럽게 호환됩니다. 이는 로봇이 환경 변화의 주요 원인인 조작 시나리오에서 동작 사전 기반 잠재 공간 예측만으로도 동기 실행 성능의 대부분을 회복할 수 있음을 증명합니다.

## 방법 분해

### 전체 아키텍처
어댑터 φ(·)는 오래된 쌍 (z_1, a_{1:2})에서 실행 시점 컨텍스트 (ẑ_3, ŝ_3)를 예측하며, 여기서 z는 사전 학습된 VLA 시각 인코더가 출력하는 잠재 특징입니다. VLA 정책은 예측된 잠재 표현을 직접 소비하여 원본 시각 인코더를 우회합니다.

### 상태 보정 모듈(SCM)
- 오래된 상태 전방 적분: s̃_{t+K} = s_{t+K-d} ⊕ Σ_{i=t+K-d}^{t+K-1} a_i
- MLP가 보상 잔차 예측: s̃_Δ = φ_SCM(s̃_{t+K}, d/d_max)
- 최종 상태: ŝ_{t+K} = s̃_{t+K} ⊕ s̃_Δ, 회전 부분은 상대 회전 합성 사용
- 손실: L_state = ||(s_{t+K} ⊖ s̃_{t+K}) − s̃_Δ||₂²

### 관측 예측 모듈(OPM)
- 각 약속된 동작에 대해 물리적 특징 벡터 구성: u_i = [a_i, Σ_{j≤i} a_j, a_i − a_{i−1}, Σ_{j≤i} |a_j|, i/d]
- 궤적 특징 행렬 U를 시간 자기 주의에 입력하여 동작 조건 운동 사전 c_motion 생성
- c_motion, 오래된 잠재 z_{t+K−d}, 카메라 임베딩 e_cam, 위치 임베딩 e_pos, 보정 상태 ŝ_{t+K}를 융합하여 조건 특징 F 형성
- 캐스케이드 선형+컨볼루션 레이어가 F를 2D 흐름 변위 Δp와 전송 게이트 α ∈ [0,1]로 투영
- 미분 가능한 이중선형 샘플링으로 공간 왜곡 수행, 게이트 결합: z_trans = (1−α)·z_{t+K−d} + α·W(z_{t+K−d}, p − Δp)
- 게이트 잔차 분기가 합성 특징 r과 합성 게이트 β 예측: {r, β} = Linear(Conv(F, z_trans − z_{t+K−d}, z_0))
- 최종 잠재: ẑ_{t+K} = z_trans + β·r
- 손실: L_obs = ||z_{t+K} − ẑ_{t+K}||₂²

### 정책 일관성 손실
L_policy = ||π_θ(z_{t+K}, s_{t+K}) − π_θ(ẑ_{t+K}, ŝ_{t+K})||₂², 다단계 흐름 매칭 오버헤드를 피하기 위해 단일 단계 흐름 근사 사용. 총 목적 함수: L_total = L_state + L_obs + λ·L_policy, λ = 10, π_θ는 고정.

### 핵심 설계 결정
- 픽셀 재구성이 아닌 잠재 공간 예측: 계산 오버헤드를 제어하고 정책 표현과 호환되도록 보장
- 처음부터 합성이 아닌 공간 전송 모델링: 약속된 동작이 명시적 운동 사전 역할을 하며, 정적 영역은 원래 표현 유지(α→0), 운동 영역은 왜곡된 특징에 의존(α→1)
- 학습 시 지연 d ~ U[1, d_max] 균일 샘플링: 단일 모델이 전체 지연 범위를 커버하므로 지연별 별도 학습 불필요

## 핵심 혁신

1. **잠재 공간 관측 예측**: 비동기 VLA의 시각적 보상을 픽셀 공간에서 사전 학습된 인코더의 잠재 공간으로 처음 이동시켰습니다. 이는 추가 추론 지연을 3.04 ms로 제어할 뿐만 아니라(표 내 수치 35.4→38.44에서 계산), 예측 결과가 VLA 정책의 입력 분포와 자연스럽게 정렬되어 픽셀 재구성 오류가 정책에 의해 증폭되는 것을 방지합니다.

2. **동작 기반 이중 분기 예측 아키텍처**: 시각적 변화를 "공간 전송"(운동 사전 기반 미분 가능 왜곡)과 "잔차 합성"(게이트 잔차 분기)의 두 부분으로 분해하며, 각각 전송 게이트 α와 합성 게이트 β로 제어됩니다. 이 분해는 조작 시나리오의 물리적 직관과 일치합니다—대부분의 시각적 변화는 로봇 자체 운동에 의해 발생하며 동작 시퀀스로 정확히 예측할 수 있고, 나머지 동역학(예: 물체 미끄러짐)은 잔차 분기가 포착합니다.

3. **정책 일관성 손실**: 예측된 컨텍스트가 특징 공간에서 실제 값에 가까울 뿐만 아니라, 고정된 정책이 예측 쌍에서 생성한 블록이 실제 쌍에서 생성한 블록과 정렬되도록 요구합니다. 이 손실은 중간 표현이 아닌 최종 목표(정책 출력)를 직접 최적화하며, d=20에서 성공률을 67.5%에서 69.4%로 향상시키는 소거 실험의 핵심 요소입니다.

## 실험 및 결과

### LIBERO 벤치마크(π_0.5 백본)
| 방법 | d=5 | d=10 | d=15 | d=20 |
|------|-----|------|------|------|
| Naive Async. | 89.5 | 82.7 | 76.3 | 68.3 |
| RTC | 89.9 | 83.2 | 77.5 | 73.7 |
| VLASH | 88.0 | 83.4 | 79.5 | 74.5 |
| REMAC | 90.8 | 85.4 | 78.5 | 73.9 |
| **FutureRTC** | **94.2** | **92.4** | **91.0** | **88.5** |

### LIBERO 벤치마크(SmolVLA-450M 백본)
| 방법 | d=5 | d=10 | d=15 | d=20 |
|------|-----|------|------|------|
| Naive Async. | 70.3 | 64.5 | 61.3 | 56.2 |
| VLASH | 69.3 | 65.8 | 64.7 | 61.9 |
| REMAC | 70.9 | 66.5 | 62.2 | 59.7 |
| **FutureRTC** | **75.8** | **73.3** | **71.6** | **69.4** |

### 소거 실험(SmolVLA-450M 평균 성공률)
| 구성 | d=5 | d=10 | d=15 | d=20 |
|------|-----|------|------|------|
| Baseline | 26.1 | 8.4 | 2.5 | 0.7 |
| +SCM | 45.9 | 18.1 | 10.4 | 5.8 |
| +OPM | 74.1 | 70.4 | 70.0 | 67.5 |
| +L_policy | 75.8 | 73.3 | 71.6 | 69.4 |

### 핵심 결과 해석
- d=5에서 d=20까지 FutureRTC는 π_0.5에서 성공률이 5.7%만 하락하고 SmolVLA에서는 6.4% 하락하는 반면, Naive Async.는 각각 21.2%와 14.1% 하락합니다(표 내 수치에서 계산)
- OPM이 성능의 주력입니다(+SCM에서 +OPM으로 d=20에서 61.7% 포인트 향상), SCM 단독 효과는 제한적이지만 OPM에 필요한 상태 조건을 제공합니다
- Kinetix에서 d=0에서 d=4까지 성공률이 3.0%만 하락하지만, 작은 지연에서는 벤치마크에 미세 조정된 학습 시점 방법보다 약간 뒤처집니다
- 실제 세계 세 가지 이중 팔 작업에서 일관되게 최고 성공률, 최소 실행 단계 수 및 시간을 달성했습니다

## 경계 및 한계

- 관측 예측 모듈은 고도로 동적인 시나리오(독립적인 외부 에이전트가 지배하는)에서 성능이 저하될 수 있습니다—논문은 이러한 시나리오에 대한 정량적 평가를 명시적으로 제공하지 않습니다
- 흐름 매칭 VLA 정책(π_0.5 및 SmolVLA-450M)에만 인스턴스화되었으며, 자기회귀 정책이나 이산 확산 정책으로 확장되지 않았습니다. DiscreteRTC 비교는 흐름 기반 백본에서 인스턴스화할 수 없어 생략되었습니다
- d > 20의 더 긴 지연 시나리오는 평가되지 않았습니다
- Kinetix의 작은 지연 d = {0, 1}에서는 정책을 고정한 상태에서 벤치마크 작업에 미세 조정되거나 재학습된 학습 시점 방법보다 약간 뒤처집니다
- 실제 세계 실험은 정성적 시연(비디오 비교)이며 정량적 성공률 수치를 보고하지 않습니다
- 학습 시점 비교 방법(VLASH 제외)은 저자가 공식 가중치 대신 직접 재현한 것으로 재현 편향이 있을 수 있습니다

## 엔지니어링 시사점

- **동작 블록 연결 규칙을 먼저 확인하세요**: 조건 컨텍스트가 실행 시점에 해당할 때, 첫 번째 동작부터 A[0:K-1]을 실행해야 합니다. 비동기 보상의 A[d:d+K-1] 연결을 계속 사용하면 성공률이 94.2%에서 39.0%로 급락합니다(표 내 수치에서 계산). 이것이 가장 쉽게 함정에 빠지는 엔지니어링 세부 사항입니다.
- **SCM 단독 사용 가치는 제한적입니다**: 소거 실험에서 +SCM은 SmolVLA에서 d=20일 때 0.7%에서 5.8%로만 향상되며, OPM과 함께 사용해야 효과를 발휘합니다. 상태 예측만 한다면 VLASH를 직접 사용하는 것이 낫습니다.
- **학습 비용이 제어 가능합니다**: 배치 크기 128, 200k 반복, RTX 4090 단일 GPU로 수렴 가능합니다. 어댑터는 5.19M 파라미터와 3.04ms 추론 지연만 추가합니다. 학습 시 지연 d ~ U[1, d_max] 균일 샘플링은 단일 모델이 전체 지연 범위를 커버하므로 배포 환경별 재학습이 필요 없습니다.
- **정책 일관성 손실의 λ는 튜닝이 필요합니다**: 논문은 λ = 10을 사용하지만, 이 하이퍼파라미터는 정책 아키텍처에 민감하므로 재현 시 [1, 50] 범위에서 스캔하는 것이 좋습니다.
- **실제 세계 배포 예산**: 종단 간 지연은 약 170ms(d ≈ 5에 해당)이며, VLA 순방향 약 99ms, LAN 통신 약 40ms, 데이터 처리 약 30ms입니다. 지연을 줄여야 한다면 어댑터 자체보다 통신과 데이터 처리를 우선 최적화하세요.
