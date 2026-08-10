---
$id: ent_paper_motion_primitive_discovery_humanoid_robo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Motion Primitive Discovery in a Humanoid Robot via Self-Organising Maps for Phase Recognition
  zh: Motion Primitive Discovery in a Humanoid Robot via Self-Organising Maps for Phase Recognition
  ko: Motion Primitive Discovery in a Humanoid Robot via Self-Organising Maps for Phase Recognition
summary:
  en: Understanding the computational basis of action recognition is a central challenge in social cognition as well as in
    human-robot interaction. Inspired by the Mirror Neuron System (MNS), we propose a two-level architecture for motor primitive
    discovery and online phase recognition applied to the NICO humanoid robot. At the first level, two Self-Organising Maps
    (SOMs) learn topographic.
  zh: 本文提出一种受镜像神经元系统启发的双层架构，在 NICO 人形机器人上通过自组织映射（SOM）发现运动基元，并用回声状态网络（ESN）实现在线相位识别。核心贡献在于验证了本体感觉信号的拓扑表示足以支撑高精度相位识别，且额外上下文信息（动作、距离、接触）的增益随储备池容量增大而递减。
  ko: Understanding the computational basis of action recognition is a central challenge in social cognition as well as in
    human-robot interaction. Inspired by the Mirror Neuron System (MNS), we propose a two-level architecture for motor primitive
    discovery and online phase recognition applied to the NICO humanoid robot. At the first level, two Self-Organising Maps
    (SOMs) learn topographic.
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
- motion
- primitive
- discovery
- humanoid
- robo
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
  title: arXiv:2607.18737 Motion Primitive Discovery in a Humanoid Robot via Self-Organising Maps for Phas
  url: https://arxiv.org/abs/2607.18737
  date: '2026-07-21'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一种受镜像神经元系统启发的双层架构，在 NICO 人形机器人上通过自组织映射（SOM）发现运动基元，并用回声状态网络（ESN）实现在线相位识别。核心贡献在于验证了本体感觉信号的拓扑表示足以支撑高精度相位识别，且额外上下文信息（动作、距离、接触）的增益随储备池容量增大而递减。

## 它改变了什么

动作识别研究长期被端到端训练的循环或 Transformer 架构主导，这类方法将“基元发现”与“序列建模”捆绑在隐空间中，难以解释动作理解的两个层次：基本运动基元的库及其组成的目标导向序列。本文的动机不是提出又一个更高精度的分类器，而是追问一个更根本的问题：机器人当前运动相位结构在多大程度上仅由学习到的运动基元的时序动态决定，需要多少额外上下文才能实现准确的在线相位识别。

这项工作真正改变的是评估视角——它把“表示是否充分”从“模型是否更优”中剥离出来。作者明确不声称超越直接运动学 ESN 或现代序列模型，而是测试 SOM 这一神经科学启发的拓扑表示是否具备足够的判别力。这种“充分性检验”而非“性能竞赛”的定位，在当下追求 SOTA 的研究环境中是一种有意的反潮流，它试图为具身智能中的表示学习提供可解释的中间层。

## 方法拆解

### 数据采集与特征选择
- 基于物理的 Unity 仿真环境，NICO 执行 7 种动作（Pick, Eat, Place, Push, Tap, Point, Wave），每种动作在 14 个物理多样的物体上执行，共 4,200 个试次，过滤后 1,284,794 帧，60Hz 记录。
- 三阶段特征选择：按功能排除 51 列保留 57 个候选；计算帧间 Pearson 相关系数得到相似矩阵 R ∈ [0,1]^{57×57}；转换为距离矩阵 d_ij = 1 − r_ij 后用 Ward 链接层次聚类，在 τ = 0.7 处切割，得到 22 个非冗余特征。

### 双 SOM 拓扑映射
- A-SOM（13 维）：TCP 速度（3）、手臂关节速度（6）、手掌方向四元数（4），35×35 网格。
- H-SOM（9 维）：孔径及速度（2）、拇指和中指位置（3）、手指关节速度（4），18×18 网格。
- 加窗：W=30 帧（0.5s），步幅 S=15 帧（50% 重叠），每窗口用均值表示，相位标签取自中心帧，每动作 8,789 个窗口共 61,523 个。
- Kohonen 更新：w_i(t+1) = w_i(t) + α(t) h_{i*i}(t)[x̂(t) − w_i(t)]，高斯邻域随时间收缩。

### ESN 相位识别
- 输入为 A-SOM 和 H-SOM 的 BMU 权重向量拼接：u(t) = [b^A(t), b^H(t)] ∈ R^{22}。
- 储备池：N=300 随机连接神经元，状态更新 x̃(t) = tanh(W_res x(t−1) + W_in u(t))，x(t) = (1−α)x(t−1) + α x̃(t)，泄漏率 α=0.50，谱半径 ρ=0.99。
- 读出层：单次教师强制遍历收集状态，前 W=5 步热身排除，岭回归 W_out = (X^T X + λI)^{-1} X^T Y，λ=10^{-4}。
- 四种上下文配置累积扩展：ctx-no（22D）→ ctx-act（+动作 one-hot，29D）→ ctx-dst（+归一化手掌–物体距离，30D）→ ctx-all（+接触标志，31D）。
- 目标为 27 个相位的 one-hot 编码，推理时 φ̂(t) = arg max_k [W_out^T x(t)]_k。

### 关键设计决策
- 双图设计反映手臂运动与手部塑形在动作执行中的互补信息。
- H-SOM 中死神经元（51.5% 活跃率）被视为隔离动作岛之间的硬边界，而非容量浪费。
- 相关性在原始帧上计算，避免窗口大小影响协方差结构。

## 关键创新

1. **本体感觉的拓扑表示作为基元库**：不同于直接使用原始运动学特征或端到端学习隐表示，本文用双 SOM 将 22 维本体感觉特征映射到地形化网格，使运动基元以空间邻域关系呈现。A-SOM 中 preshape 平滑过渡到 move-to-grasp、H-SOM 中 Point/Tap/Wave/Push 形成 100% 纯净孤立簇，这种可解释的拓扑组织是端到端模型难以提供的。

2. **基元发现与相位识别的显式解耦**：SOM 负责无监督基元发现，ESN 负责时序积分与相位识别，两者通过 BMU 权重向量衔接。这种模块化设计允许独立分析“表示充分性”与“时序建模能力”，是首个在类人机器人上验证该双层架构的工作。

3. **上下文增益的容量依赖性发现**：通过 9 种超参数配置 × 4 种上下文输入的 36 次运行，揭示上下文信息（动作、距离、接触）的增益随储备池容量增大而单调递减——N=30 时全上下文贡献 +4.1 pp，N=1,000 时仅 +0.60 pp。这表明大容量储备池能从纯基元序列中提取更多相位信息，为资源分配提供定量依据。

## 实验与结果

### 主要结果
| 配置 | ctx-no | ctx-act | ctx-dst | ctx-all |
|------|--------|---------|---------|---------|
| R5（N=300, ρ=0.99, α=0.50） | 93.9% | 94.6% | 94.6% | 94.9% |
| R8（N=500, ρ=0.89, α=0.20） | 95.8% | 96.3% | 96.3% | 96.7% |
| R9（N=1,000, ρ=0.90, α=0.10） | 96.7% | 96.9% | 96.9% | 97.3% |

### 关键发现
- 储备池容量是主导因素：准确率随 N 单调增加，N=30 时 ctx-no 仅 73.6%，N=1,000 时达 96.7%。
- 固定 N=300 时改变其他超参数，准确率变化最多 0.5 pp，说明容量比泄漏率、谱半径更关键。
- 上下文增益随容量递减：N=30 时全上下文贡献 +4.1 pp，N=1,000 时仅 +0.60 pp（由表内数值 77.7−73.6 与 97.3−96.7 计算）。
- 单试次分析：Eat 动作 ctx-no 达 98.4%（63/64 步），唯一错误在 t=18（首个 move-to-grasp 步）；ctx-all 达 100%，动作 one-hot 与距离信号提供提前一步检测相位转换的能力。
- 神经元级歧义：A-SOM BMU (7,18) 含 35% move-to-grasp、23% preshape、18% closing，无主导相位，ESN 通过时间积分与双流整合解决。

### 结果含义
93.86% 的纯基元序列相位识别准确率表明，SOM 拓扑表示确实充分捕捉了运动相位结构。上下文增益虽小但一致，且随容量递减，说明大储备池能从基元序列中提取更多时序信息，而小储备池更依赖外部上下文补偿。

## 边界与局限

- 模型仅在 NICO 自身动作上训练和评估，未涉及跨具身观察——扩展到其他机器人或人类演示需要处理视角、尺度和具身差异的镜像机制，论文未明确给出解决方案。
- 识别而非预测：当前 ESN 输出当前相位，不生成未来输入；作者将基元预测和闭环想象运动生成列为未来工作。
- 手部控制采用低维协同控制器（4 个标量参数驱动 13 个手指关节），H-SOM 的 18×18 网格和 51.5% 活跃率可能依赖这一简化；真实高维手部自由度下拓扑结构可能不同。
- 仿真环境基于 Unity 物理引擎，未在实体 NICO 上验证；仿真与实体的域差异可能影响 SOM 拓扑和 ESN 泛化。

## 工程启示

- 复现时先核对特征选择细节：22 个特征中 A-SOM 的 13 维包含 TCP 速度、手臂关节速度、手掌方向四元数，H-SOM 的 9 维包含孔径、手指位置与速度；相关性计算必须在原始帧上进行，否则窗口大小会污染协方差结构。
- 最容易踩坑的是 H-SOM 网格大小：18×18 是基于协同控制器产生约六种手部姿态的低维假设，若更换手部控制策略需重新网格搜索；死神经元不应视为浪费，它们是动作岛之间的硬边界。
- ESN 训练时务必重置每试次储备池状态并排除前 W=5 步热身期；岭回归 λ=10^{-4} 是默认值，但 R8 中 λ=10^{-7} 配合 N=500 也有效，建议按容量调整。
- 上下文增益随容量递减的规律意味着：若下游任务对延迟敏感需用小储备池，应优先加入动作 one-hot 和距离信号；若可用大储备池（N≥1,000），纯基元序列已足够，额外上下文收益有限。
- 单试次分析显示相位转换边界（如 t=18 的 move-to-grasp 起始）是最易出错点，可考虑在训练时对相位边界附近样本加权。

## Overview
Understanding the computational basis of action recognition is a central challenge in social cognition as well as in human-robot interaction. Inspired by the Mirror Neuron System (MNS), we propose a two-level architecture for motor primitive discovery and online phase recognition applied to the NICO humanoid robot. At the first level, two Self-Organising Maps (SOMs) learn topographic representations of arm kinematics (A-SOM) and hand kinematics (H-SOM) from simulated trials covering seven motor actions. The maps are trained on non-redundant features identified through hierarchical correlation analysis of motion trajectories. The results show that the two SOMs encode complementary aspects of motor behaviour. At the second level, an Echo State Network (ESN) evaluates whether temporal trajectories of SOM activations, represented by consecutive best-matching units, are sufficient for online recognition of the currently executed movement phase. The results show that SOM-based trajectories preserve the dominant phase-discriminative structure of the movement, while contextual information provides only a secondary refinement. Our contribution is the integration of established SOM and ESN methods within an MNS-inspired architecture for motor primitive representation and online phase recognition. The results are compatible with the computational hypothesis that self-organised motor representations, when temporally integrated, can support accurate online recognition of ongoing movement phases.

## 参考
- https://arxiv.org/abs/2607.18737

## 개요

본 논문은 거울 신경계 시스템에서 영감을 받은 이중 계층 아키텍처를 제안하며, NICO 휴머노이드 로봇에서 자기조직화 지도(SOM)를 통해 운동 기본요소를 발견하고, 에코 상태 네트워크(ESN)로 온라인 위상 인식을 구현한다. 핵심 기여는 고유수용감각 신호의 위상적 표현이 고정밀 위상 인식을 지원하기에 충분하다는 것을 검증하고, 추가 컨텍스트 정보(동작, 거리, 접촉)의 이득이 저장소 용량이 증가함에 따라 감소한다는 점이다.

## 그것이 바꾸는 것

동작 인식 연구는 오랫동안 엔드투엔드 훈련 순환 또는 트랜스포머 아키텍처가 지배해 왔으며, 이러한 방법은 '기본요소 발견'과 '시퀀스 모델링'을 잠재 공간에 결합하여 동작 이해의 두 계층, 즉 기본 운동 기본요소의 라이브러리와 그 구성의 목표 지향 시퀀스를 설명하기 어렵다. 본 논문의 동기는 또 다른 더 높은 정확도의 분류기를 제안하는 것이 아니라, 더 근본적인 질문을 추구한다: 로봇의 현재 운동 위상 구조가 학습된 운동 기본요소의 시간적 역학에 의해 어느 정도 결정되는지, 정확한 온라인 위상 인식을 위해 얼마나 많은 추가 컨텍스트가 필요한지.

이 작업이 실제로 바꾸는 것은 평가 관점이다—'표현이 충분한지'를 '모델이 더 우수한지'에서 분리한다. 저자는 직접 운동학 ESN이나 현대 시퀀스 모델을 능가한다고 명시적으로 주장하지 않고, 신경과학에서 영감을 받은 SOM의 위상적 표현이 충분한 판별력을 갖는지 테스트한다. '성능 경쟁'이 아닌 '충분성 검증'이라는 이러한 포지셔닝은 SOTA를 추구하는 현재 연구 환경에서 의도적인 반조류이며, 구현 지능의 표현 학습에 해석 가능한 중간 계층을 제공하려 한다.

## 방법 분해

### 데이터 수집 및 특징 선택
- 물리 기반 Unity 시뮬레이션 환경에서 NICO가 7가지 동작(Pick, Eat, Place, Push, Tap, Point, Wave)을 수행하며, 각 동작은 14개의 물리적으로 다양한 물체에 대해 수행되어 총 4,200회 시행, 필터링 후 1,284,794프레임, 60Hz 기록.
- 3단계 특징 선택: 기능별로 51개 열을 제외하고 57개 후보 유지; 프레임 간 Pearson 상관 계수를 계산하여 유사 행렬 R ∈ [0,1]^{57×57} 획득; 거리 행렬 d_ij = 1 − r_ij로 변환 후 Ward 연결 계층적 클러스터링, τ = 0.7에서 절단하여 22개의 비중복 특징 획득.

### 이중 SOM 위상 매핑
- A-SOM(13차원): TCP 속도(3), 팔 관절 속도(6), 손바닥 방향 쿼터니언(4), 35×35 그리드.
- H-SOM(9차원): 개구부 및 속도(2), 엄지와 중지 위치(3), 손가락 관절 속도(4), 18×18 그리드.
- 윈도우 처리: W=30프레임(0.5초), 스텝 S=15프레임(50% 중첩), 각 윈도우는 평균으로 표현, 위상 레이블은 중심 프레임에서 가져오며, 각 동작당 8,789개 윈도우 총 61,523개.
- Kohonen 업데이트: w_i(t+1) = w_i(t) + α(t) h_{i*i}(t)[x̂(t) − w_i(t)], 가우시안 이웃은 시간에 따라 수축.

### ESN 위상 인식
- 입력은 A-SOM과 H-SOM의 BMU 가중치 벡터 연결: u(t) = [b^A(t), b^H(t)] ∈ R^{22}.
- 저장소: N=300 무작위 연결 뉴런, 상태 업데이트 x̃(t) = tanh(W_res x(t−1) + W_in u(t)), x(t) = (1−α)x(t−1) + α x̃(t), 누수율 α=0.50, 스펙트럼 반경 ρ=0.99.
- 읽기 계층: 단일 교사 강제 순회로 상태 수집, 처음 W=5단계 워밍업 제외, 릿지 회귀 W_out = (X^T X + λI)^{-1} X^T Y, λ=10^{-4}.
- 4가지 컨텍스트 구성 누적 확장: ctx-no(22D) → ctx-act(+동작 one-hot, 29D) → ctx-dst(+정규화 손바닥–물체 거리, 30D) → ctx-all(+접촉 플래그, 31D).
- 목표는 27개 위상의 one-hot 인코딩, 추론 시 φ̂(t) = arg max_k [W_out^T x(t)]_k.

### 핵심 설계 결정
- 이중 맵 설계는 동작 실행에서 팔 운동과 손 모양의 상보적 정보를 반영.
- H-SOM의 죽은 뉴런(51.5% 활성율)은 용량 낭비가 아닌 동작 섬 사이의 경계로 간주.
- 상관 관계는 원본 프레임에서 계산되어 윈도우 크기가 공분산 구조를 오염시키지 않도록 함.

## 핵심 혁신

1. **고유수용감각의 위상적 표현을 기본요소 라이브러리로**: 원시 운동학적 특징을 직접 사용하거나 엔드투엔드로 잠재 표현을 학습하는 대신, 이중 SOM으로 22차원 고유수용감각 특징을 지형적 그리드에 매핑하여 운동 기본요소가 공간적 이웃 관계로 나타나게 한다. A-SOM에서 preshape가 move-to-grasp로 부드럽게 전이되고, H-SOM에서 Point/Tap/Wave/Push가 100% 순수 고립 클러스터를 형성하는 이러한 해석 가능한 위상 조직은 엔드투엔드 모델이 제공하기 어렵다.

2. **기본요소 발견과 위상 인식의 명시적 분리**: SOM은 비지도 기본요소 발견을 담당하고, ESN은 시간적 통합과 위상 인식을 담당하며, 둘은 BMU 가중치 벡터로 연결된다. 이러한 모듈식 설계는 '표현 충분성'과 '시간적 모델링 능력'을 독립적으로 분석할 수 있게 하며, 휴머노이드 로봇에서 이 이중 계층 아키텍처를 검증한 최초의 작업이다.

3. **컨텍스트 이득의 용량 의존성 발견**: 9가지 하이퍼파라미터 구성 × 4가지 컨텍스트 입력의 36회 실행을 통해 컨텍스트 정보(동작, 거리, 접촉)의 이득이 저장소 용량이 증가함에 따라 단조 감소함을 밝혀냈다—N=30에서 전체 컨텍스트 기여 +4.1 pp, N=1,000에서 +0.60 pp에 불과. 이는 대용량 저장소가 순수 기본요소 시퀀스에서 더 많은 위상 정보를 추출할 수 있음을 시사하며, 자원 할당에 정량적 근거를 제공한다.

## 실험 및 결과

### 주요 결과
| 구성 | ctx-no | ctx-act | ctx-dst | ctx-all |
|------|--------|---------|---------|---------|
| R5(N=300, ρ=0.99, α=0.50) | 93.9% | 94.6% | 94.6% | 94.9% |
| R8(N=500, ρ=0.89, α=0.20) | 95.8% | 96.3% | 96.3% | 96.7% |
| R9(N=1,000, ρ=0.90, α=0.10) | 96.7% | 96.9% | 96.9% | 97.3% |

### 핵심 발견
- 저장소 용량이 지배적 요인: 정확도는 N에 따라 단조 증가, N=30에서 ctx-no는 73.6%에 불과, N=1,000에서 96.7% 도달.
- N=300 고정 시 다른 하이퍼파라미터 변경 시 정확도 변화는 최대 0.5 pp로, 용량이 누수율, 스펙트럼 반경보다 더 중요함을 시사.
- 컨텍스트 이득은 용량에 따라 감소: N=30에서 전체 컨텍스트 기여 +4.1 pp, N=1,000에서 +0.60 pp에 불과(표 내 77.7−73.6 및 97.3−96.7 계산).
- 단일 시행 분석: Eat 동작 ctx-no에서 98.4%(63/64단계), 유일한 오류는 t=18(첫 move-to-grasp 단계); ctx-all에서 100% 달성, 동작 one-hot과 거리 신호가 위상 전환을 한 단계 앞서 감지하는 능력 제공.
- 뉴런 수준 모호성: A-SOM BMU (7,18)은 35% move-to-grasp, 23% preshape, 18% closing을 포함하며 지배적 위상이 없고, ESN이 시간적 통합과 이중 스트림 통합으로 해결.

### 결과 의미
93.86%의 순수 기본요소 시퀀스 위상 인식 정확도는 SOM 위상 표현이 운동 위상 구조를 충분히 포착함을 시사한다. 컨텍스트 이득은 작지만 일관되며 용량에 따라 감소하므로, 대용량 저장소는 기본요소 시퀀스에서 더 많은 시간적 정보를 추출할 수 있고, 소용량 저장소는 외부 컨텍스트 보상에 더 의존함을 나타낸다.

## 경계 및 한계

- 모델은 NICO 자체 동작에서만 훈련 및 평가되었으며, 교차 구현 관찰은 다루지 않음—다른 로봇이나 인간 시연으로 확장하려면 시점, 스케일, 구현 차이의 거울 메커니즘 처리가 필요하며, 논문은 명확한 해결책을 제시하지 않음.
- 인식이지 예측이 아님: 현재 ESN은 현재 위상을 출력하며 미래 입력을 생성하지 않음; 저자는 기본요소 예측과 폐루프 상상 운동 생성을 향후 작업으로 언급.
- 손 제어는 저차원 협동 제어기(4개 스칼라 파라미터가 13개 손가락 관절 구동)를 사용하며, H-SOM의 18×18 그리드와 51.5% 활성율은 이 단순화에 의존할 수 있음; 실제 고차원 손 자유도에서는 위상 구조가 다를 수 있음.
- 시뮬레이션 환경은 Unity 물리 엔진 기반이며, 실제 NICO에서 검증되지 않음; 시뮬레이션과 실물의 도메인 차이가 SOM 위상과 ESN 일반화에 영향을 줄 수 있음.

## 공학적 시사점

- 재현 시 특징 선택 세부사항을 먼저 확인: 22개 특징 중 A-SOM의 13차원은 TCP 속도, 팔 관절 속도, 손바닥 방향 쿼터니언을 포함하고, H-SOM의 9차원은 개구부, 손가락 위치와 속도를 포함; 상관 관계 계산은 반드시 원본 프레임에서 수행해야 하며, 그렇지 않으면 윈도우 크기가 공분산 구조를 오염시킴.
- 가장 함정에 빠지기 쉬운 것은 H-SOM 그리드 크기: 18×18은 협동 제어기가 약 6가지 손姿态을 생성한다는 저차원 가정에 기반하며, 손 제어 전략을 변경하면 그리드 탐색을 다시 해야 함; 죽은 뉴런은 낭비로 간주하지 말 것—동작 섬 사이의 경계이다.
- ESN 훈련 시 반드시 각 시행의 저장소 상태를 재설정하고 처음 W=5단계 워밍업을 제외할 것; 릿지 회귀 λ=10^{-4}는 기본값이지만, R8에서 λ=10^{-7}과 N=500 조합도 유효하므로 용량에 따라 조정 권장.
- 컨텍스트 이득이 용량에 따라 감소하는 규칙은: 다운스트림 작업이 지연에 민감하여 소용량 저장소를 사용해야 한다면 동작 one-hot과 거리 신호를 우선 추가할 것; 대용량 저장소(N≥1,000)를 사용할 수 있다면 순수 기본요소 시퀀스로 충분하며 추가 컨텍스트 이득은 제한적.
- 단일 시행 분석은 위상 전환 경계(예: t=18의 move-to-grasp 시작)가 가장 오류가 발생하기 쉬운 지점임을 보여주며, 훈련 시 위상 경계 근처 샘플에 가중치를 부여하는 것을 고려할 수 있음.
