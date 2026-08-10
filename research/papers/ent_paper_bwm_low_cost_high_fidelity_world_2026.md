---
$id: ent_paper_bwm_low_cost_high_fidelity_world_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning'
  zh: 'BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning'
  ko: 'BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning'
summary:
  en: Reliable robot learning requires a world simulator that can predict action consequences before execution on physical
    hardware, including risky and failure-prone outcomes. Existing physics simulators require substantial asset construction
    and calibration and still face a sim-to-real gap, while video generators often lack precise control over their responses
    to fine-grained robot actions. In this.
  zh: BWM 是一个面向特定机器人领域的低成本高保真世界模拟器，由 Boundless 团队开发。它通过领域特定的后训练方式适配预训练视频扩散模型，将模型容量聚焦于目标机器人和环境，实现了高保真的动作条件未来观测预测。核心贡献在于提出了一个完整的数据管线、双路径动作注入架构和模拟器接口，在模拟保真度、数据引擎和策略评估器三个功能角色上均取得了领先性能。
  ko: Reliable robot learning requires a world simulator that can predict action consequences before execution on physical
    hardware, including risky and failure-prone outcomes. Existing physics simulators require substantial asset construction
    and calibration and still face a sim-to-real gap, while video generators often lack precise control over their responses
    to fine-grained robot actions. In this.
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
- bwm
- low
- cost
- high
- fidelity
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
  title: 'arXiv:2607.29302 BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning'
  url: https://arxiv.org/abs/2607.29302
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

BWM 是一个面向特定机器人领域的低成本高保真世界模拟器，由 Boundless 团队开发。它通过领域特定的后训练方式适配预训练视频扩散模型，将模型容量聚焦于目标机器人和环境，实现了高保真的动作条件未来观测预测。核心贡献在于提出了一个完整的数据管线、双路径动作注入架构和模拟器接口，在模拟保真度、数据引擎和策略评估器三个功能角色上均取得了领先性能。

## 它改变了什么

机器人学习长期面临一个根本性困境：物理模拟器需要大量资产构建和校准，且 sim-to-real 差距难以消除；而视频生成器虽然能生成逼真图像，却缺乏对细粒度机器人动作响应的精确控制。现有动作条件世界模型通常对大规模机器人数据集进行后训练来适配预训练视频生成骨干，但通用机器人后训练面临相机视角、embodiment 和动作空间的多样性，导致模型容量和训练需求急剧膨胀，难以同时实现高保真预测和实时模拟。

BWM 真正改变的是这条技术路线的选择：它放弃了通用多 embodiment 的雄心，转而采用领域特定的机器人后训练策略。这个决策看似保守，实则务实——保留通用视频先验的同时，将模型容量全部聚焦于目标机器人和环境，从而在可控成本下实现了超越通用方案的高保真预测。它同时改变了世界模拟器的功能定位，不再仅仅是生成视频，而是同时充当数据引擎（为模仿学习生成训练轨迹）和策略评估器（对候选策略进行闭环排名），将世界模型从研究工具提升为工程基础设施。

## 方法拆解

### 数据管线
- **轨迹重放**：在 RoboTwin 模拟器中收集操作轨迹后，重新运行原始规划器生成的轨迹并以目标分辨率渲染观测。重放不引入新行为，仅沿原始轨迹收集更高分辨率观测，保证重渲染帧与原始 EEF 动作保持时间同步。
- **重叠片段采样**：使用重叠滑动窗口提取时间对齐的训练片段。相比非重叠分割，重叠窗口保留原本会被固定片段边界分割的转换，并在不同时间上下文下暴露它们，更好地匹配自回归推理中使用的滑动上下文窗口。
- **初始观测增强**：推理时模拟器重放不可用，使用 SeedVR-2 在 rollout 前恢复初始环境观测。

### 模型架构
BWM 将世界模拟形式化为观测空间中的动作条件预测：给定初始环境观测 x₀、动态历史 h_t = (x_{t-H+1}, …, x_t) 和候选动作块 a_{t+1:t+K}，参数化下一个 K 个观测的分布 p_θ(x_{t+1:t+K} | x₀, h_t, a_{t+1:t+K})。

动作接口通过两条互补路径注入同一动作块：
- **帧级路径**：独立编码每个动作并提供 token 给交叉注意力，保留精细时间控制。
- **潜变量级路径**：时间聚合和投影动作序列以与压缩视频潜变量对齐，将结果表示添加到时间步嵌入以调制 AdaLN。

训练目标采用未来仅流匹配目标：
L_future = E[w(τ)‖v^fut_θ(z̃_τ, a, τ) − v^fut_τ‖²₂]

历史潜变量接收低水平扰动：z̃^hist = (1 − σ_h)z^hist + σ_h ε^hist，初始环境潜变量 z⁰ 保持干净。自回归推理时，每个去噪步骤用干净的初始环境潜变量和固定扰动历史替换条件前缀，解码后仅将 x_{t+1:t+K} 追加到 rollout。

### 模拟器接口
- **数据引擎**：模型接收对齐的观测和动作上下文，离线生成未来观测块，每个生成块与产生它的动作序列保持配对，使生成的轨迹可增强模仿学习数据。
- **策略评估器**：使用固定策略且不进行策略更新的闭环协议，任务特定成功标准将每个生成轨迹转换为结果分数，聚合分数对候选策略模型进行排名。

## 关键创新

1. **领域特定后训练路线**：不同于通用机器人后训练追求多 embodiment 支持，BWM 明确选择聚焦目标机器人和环境的领域特定路线。这一设计决策大幅降低了模型容量和训练需求，使得在有限计算资源下（929 GPU 小时）即可达到超越通用方案的高保真预测，是低成本与高性能之间的关键平衡点。

2. **双路径动作注入机制**：帧级交叉注意力路径和潜变量级 AdaLN 路径互补工作——前者提供逐帧精细时间控制，后者在潜变量时间分辨率上调节去噪过程。这种设计解决了单一注入方式难以同时满足时间精度和全局一致性的问题，是动作条件视频生成中少见的架构创新。

3. **统一模拟器接口设计**：将世界模型同时封装为数据引擎和策略评估器，形成闭环协议。数据引擎生成的轨迹与动作序列保持配对，可直接增强模仿学习；策略评估器提供固定策略的闭环排名能力。这种功能整合使世界模型从被动生成工具转变为主动的机器人学习基础设施。

## 实验与结果

### 模拟保真度
BWM 在 WorldArena 的 16 个生成指标上排名第一，EWMScore 为 63.51，超过最高分闭源视频生成器 Wan 2.6 达 1.65，超过最高分开源通用视频生成器 CogVideoX 达 5.61。在动作条件世界模拟器中，比最强基线 Ctrl-World 提高 3.81，轨迹精度提高 16.70。

| 指标 | BWM | 对比基线 | 差值 |
|------|-----|---------|------|
| EWMScore | 63.51 | Ctrl-World 59.70（由表内数值计算） | +3.81 |
| 轨迹精度 | 64.36 | Ctrl-World 47.66（由表内数值计算） | +16.70 |
| JEPA 相似度 | 98.88 | 最佳 | — |
| 深度精度 | 97.56 | 最佳 | — |

### 模拟数据引擎
BWM 生成数据训练的策略平均成功率达 94.50%，比真实数据训练高 23.00，比最强替代世界模拟器 WoW 高 36.50。

| 数据来源 | 平均成功率 | adjust bottle | click bell |
|---------|-----------|---------------|------------|
| BWM 生成 | 94.50% | 98.00% | 91.00% |
| 真实数据 | 71.50% | 77.00% | 66.00% |
| WoW 生成 | 58.00% | 45.00% | 71.00% |
| π₀.₅ 零样本 | 3.50% | 2.00% | 5.00% |

### 模拟策略评估器
BWM 达到 Pearson 相关系数 r = 0.978，在最强基线 Ctrl-World 的 0.008 以内，是仅有的两个相关系数高于 0.97 的评估世界模拟器之一。

| 评估器 | Pearson r |
|--------|-----------|
| Ctrl-World | 0.986 |
| BWM | 0.978 |
| WoW | 0.959 |
| RoboScape | 0.863 |
| IRASim | 0.658 |
| Cosmos-Predict 2.5 (action) | 0.483 |

### 物理机器人
物理机器人数据引擎实验中，BWM 生成数据训练的策略达到 71.00% 平均成功率，而最强评估世界模拟器基线为 53.33%。物理机器人策略评估器的 Pearson 相关系数 r 为 0.908。物理机器人保真度评估中，动作跟随在两个视角均不可用，腕部视角轨迹精度也不可用。

## 边界与局限

- 物理机器人保真度评估存在明显盲区：动作跟随在两个视角均不可用，腕部视角轨迹精度也不可用，这意味着对物理机器人场景的动作响应精度验证是不完整的。
- 论文未明确 BWM 在物理机器人保真度表 5 中的具体数值，仅说明该表为文本表格，无法进行定量对比。
- 领域特定后训练路线意味着模型泛化能力受限，对新的 embodiment、相机视角或任务场景需要重新训练，论文未明确跨领域迁移的具体成本。
- 物理机器人模型覆盖更少任务，使用更短的训练计划，可能影响其在更广泛任务上的表现。
- 初始观测增强依赖 SeedVR-2，当推理时模拟器重放不可用时，rollout 质量受限于该增强模型的能力。

## 工程启示

复现 BWM 时，首先核对数据管线的三个关键环节：轨迹重放必须保持原始执行顺序和时间戳不变，重叠片段采样的窗口参数（H = 8，K = 72）直接影响训练上下文匹配，初始观测增强的 SeedVR-2 版本选择会影响 rollout 起点质量。最容易踩坑的地方是动作归一化——使用训练数据第 1 和第 99 百分位数作为边界，裁剪值映射到 [ℓ_a, u_a]，如果数据分布偏移，归一化边界需要重新计算。

训练配置方面，BWM 从 Wan2.2-TI2V-5B 初始化，在四个节点各八块 NVIDIA A800 GPU 上训练，每 GPU 批大小为 1，梯度累积四步，有效批大小为 128。WorldArena 提交模型训练 12,000 个优化步骤约需 929 GPU 小时。动作接口前置 P = 3 个边界动作并以 G = 4 分组动作，使 token 与时间压缩的视频潜变量对齐，这个设计细节对动作时间对齐至关重要。

对于下游团队，BWM 作为数据引擎的价值已充分验证——生成数据训练的策略在模拟中比真实数据高 23.00，在物理机器人上比最强基线高 17.67（由表内数值 71.00% 与 53.33% 计算）。但作为策略评估器使用时需注意，模拟评估的 Pearson 相关系数 0.978 与物理机器人评估的 0.908 存在差距，跨 sim-to-real 的评估置信度需要额外验证。

## Overview
Reliable robot learning requires a world simulator that can predict action consequences before execution on physical hardware, including risky and failure-prone outcomes. Existing physics simulators require substantial asset construction and calibration and still face a sim-to-real gap, while video generators often lack precise control over their responses to fine-grained robot actions. In this paper, we present the Boundless World Model (BWM), an open-source, low-cost, high-fidelity world simulator for robot manipulation. BWM is an action-conditioned world model that combines initial-environment guidance, dynamic visual history, and temporally aligned robot-action conditioning for stateful autoregressive prediction of future observations. We construct action-aligned training clips through trajectory replay, overlapping clip sampling, and initial-observation enhancement. BWM serves as a data engine that augments imitation-learning data with action-aligned rollouts, and as a policy evaluator for closed-loop assessment, risk anticipation, and policy ranking. Experiments on the WorldArena benchmark and physical robots demonstrate improved simulator fidelity and functional utility across the data-engine and policy-evaluator settings. BWM ranks first overall in the WorldArena Challenge across Track 1 and its two Track 2 applications. We release the BWM open-source ecosystem, including model checkpoints, training and inference code, and interfaces for data generation and policy evaluation.

## 参考
- https://arxiv.org/abs/2607.29302

## 개요

BWM은 Boundless 팀이 개발한 특정 로봇 도메인을 위한 저비용 고충실도 세계 시뮬레이터입니다. 사전 학습된 비디오 확산 모델을 도메인 특화된 후속 학습 방식으로 적응시켜, 모델 용량을 대상 로봇과 환경에 집중함으로써 고충실도의 행동 조건부 미래 관측 예측을 구현합니다. 핵심 기여는 완전한 데이터 파이프라인, 이중 경로 행동 주입 아키텍처, 그리고 시뮬레이터 인터페이스를 제안하여 시뮬레이션 충실도, 데이터 엔진, 정책 평가자라는 세 가지 기능적 역할에서 모두 선도적인 성능을 달성한 것입니다.

## 무엇을 바꾸었는가

로봇 학습은 오랫동안 근본적인 딜레마에 직면해 왔습니다. 물리 시뮬레이터는 많은 자산 구축과 보정이 필요하고 sim-to-real 격차를 제거하기 어려운 반면, 비디오 생성기는 사실적인 이미지를 생성할 수 있지만 세밀한 로봇 행동 응답에 대한 정밀한 제어가 부족합니다. 기존의 행동 조건부 세계 모델은 일반적으로 대규모 로봇 데이터셋에 대한 후속 학습을 통해 사전 학습된 비디오 생성 백본을 적응시키지만, 일반 로봇 후속 학습은 카메라 시점, embodiment, 행동 공간의 다양성으로 인해 모델 용량과 학습 요구 사항이 급격히 증가하여 고충실도 예측과 실시간 시뮬레이션을 동시에 달성하기 어렵습니다.

BWM이 진정으로 바꾼 것은 이 기술 경로의 선택입니다. 범용 다중 embodiment에 대한 야망을 포기하고 대신 도메인 특화된 로봇 후속 학습 전략을 채택했습니다. 이 결정은 보수적으로 보일 수 있지만 실용적입니다. 일반 비디오 사전 지식을 유지하면서 모델 용량을 대상 로봇과 환경에 집중하여 통제 가능한 비용으로 일반 솔루션을 능가하는 고충실도 예측을 달성합니다. 또한 세계 시뮬레이터의 기능적 위치를 변경하여 단순히 비디오를 생성하는 것에 그치지 않고 데이터 엔진(모방 학습을 위한 학습 궤적 생성)과 정책 평가자(후보 정책에 대한 폐쇄 루프 순위 지정)를 동시에 수행함으로써 세계 모델을 연구 도구에서 엔지니어링 인프라로 승격시킵니다.

## 방법 분석

### 데이터 파이프라인
- **궤적 재생**: RoboTwin 시뮬레이터에서 조작 궤적을 수집한 후, 원래 플래너가 생성한 궤적을 재실행하고 대상 해상도로 관측을 렌더링합니다. 재생은 새로운 행동을 도입하지 않고 원래 궤적을 따라 더 높은 해상도의 관측만 수집하여, 재렌더링된 프레임이 원래 EEF 행동과 시간적으로 동기화되도록 보장합니다.
- **중첩 세그먼트 샘플링**: 중첩 슬라이딩 윈도우를 사용하여 시간 정렬된 학습 세그먼트를 추출합니다. 비중첩 분할과 비교하여 중첩 윈도우는 고정된 세그먼트 경계로 분할되었을 변환을 보존하고 다양한 시간 컨텍스트에서 노출시켜, 자기회귀 추론에서 사용되는 슬라이딩 컨텍스트 윈도우와 더 잘 일치합니다.
- **초기 관측 증강**: 추론 시 시뮬레이터 재생을 사용할 수 없으므로, SeedVR-2를 사용하여 rollout 전에 초기 환경 관측을 복원합니다.

### 모델 아키텍처
BWM은 세계 시뮬레이션을 관측 공간에서의 행동 조건부 예측으로 형식화합니다. 초기 환경 관측 x₀, 동적 히스토리 h_t = (x_{t-H+1}, …, x_t), 후보 행동 블록 a_{t+1:t+K}가 주어졌을 때, 다음 K개의 관측 분포 p_θ(x_{t+1:t+K} | x₀, h_t, a_{t+1:t+K})를 파라미터화합니다.

행동 인터페이스는 두 가지 상보적 경로를 통해 동일한 행동 블록을 주입합니다:
- **프레임 수준 경로**: 각 행동을 독립적으로 인코딩하고 교차 주의에 토큰을 제공하여 세밀한 시간 제어를 보존합니다.
- **잠재 변수 수준 경로**: 시간적으로 행동 시퀀스를 집계하고 투영하여 압축된 비디오 잠재 변수와 정렬하고, 결과 표현을 시간 단계 임베딩에 추가하여 AdaLN을 변조합니다.

학습 목표는 미래 전용 흐름 매칭 목표를 채택합니다:
L_future = E[w(τ)‖v^fut_θ(z̃_τ, a, τ) − v^fut_τ‖²₂]

히스토리 잠재 변수는 낮은 수준의 섭동을 받습니다: z̃^hist = (1 − σ_h)z^hist + σ_h ε^hist, 초기 환경 잠재 변수 z⁰는 깨끗하게 유지됩니다. 자기회귀 추론 시 각 노이즈 제거 단계에서 깨끗한 초기 환경 잠재 변수와 고정 섭동 히스토리로 조건부 접두사를 대체하고, 디코딩 후 x_{t+1:t+K}만 rollout에 추가합니다.

### 시뮬레이터 인터페이스
- **데이터 엔진**: 모델은 정렬된 관측과 행동 컨텍스트를 받아 오프라인으로 미래 관측 블록을 생성하며, 각 생성 블록은 이를 생성한 행동 시퀀스와 쌍을 유지하여 생성된 궤적이 모방 학습 데이터를 증강할 수 있게 합니다.
- **정책 평가자**: 정책 업데이트 없이 고정 정책을 사용하는 폐쇄 루프 프로토콜로, 작업별 성공 기준이 각 생성 궤적을 결과 점수로 변환하고, 집계된 점수로 후보 정책 모델의 순위를 매깁니다.

## 핵심 혁신

1. **도메인 특화 후속 학습 경로**: 다중 embodiment 지원을 추구하는 일반 로봇 후속 학습과 달리, BWM은 대상 로봇과 환경에 초점을 맞춘 도메인 특화 경로를 명확히 선택합니다. 이 설계 결정은 모델 용량과 학습 요구 사항을 크게 줄여 제한된 계산 자원(929 GPU 시간)으로 일반 솔루션을 능가하는 고충실도 예측을 달성할 수 있게 하며, 저비용과 고성능 사이의 핵심 균형점입니다.

2. **이중 경로 행동 주입 메커니즘**: 프레임 수준 교차 주의 경로와 잠재 변수 수준 AdaLN 경로가 상호 보완적으로 작동합니다. 전자는 프레임별 세밀한 시간 제어를 제공하고, 후자는 잠재 변수 시간 해상도에서 노이즈 제거 과정을 조절합니다. 이 설계는 단일 주입 방식으로 시간 정밀도와 전역 일관성을 동시에 충족하기 어려운 문제를 해결하며, 행동 조건부 비디오 생성에서 드문 아키텍처 혁신입니다.

3. **통합 시뮬레이터 인터페이스 설계**: 세계 모델을 데이터 엔진과 정책 평가자로 동시에 캡슐화하여 폐쇄 루프 프로토콜을 형성합니다. 데이터 엔진이 생성한 궤적은 행동 시퀀스와 쌍을 유지하여 모방 학습을 직접 증강할 수 있고, 정책 평가자는 고정 정책에 대한 폐쇄 루프 순위 지정 기능을 제공합니다. 이러한 기능 통합은 세계 모델을 수동적 생성 도구에서 능동적 로봇 학습 인프라로 변환합니다.

## 실험 및 결과

### 시뮬레이션 충실도
BWM은 WorldArena의 16개 생성 지표에서 1위를 차지했으며, EWMScore 63.51로 최고 점수 폐쇄 소스 비디오 생성기 Wan 2.6을 1.65 초과, 최고 점수 오픈 소스 일반 비디오 생성기 CogVideoX를 5.61 초과했습니다. 행동 조건부 세계 시뮬레이터 중에서는 가장 강력한 기준선 Ctrl-World보다 3.81 높고, 궤적 정밀도는 16.70 높습니다.

| 지표 | BWM | 비교 기준선 | 차이 |
|------|-----|---------|------|
| EWMScore | 63.51 | Ctrl-World 59.70 (표 내 값으로 계산) | +3.81 |
| 궤적 정밀도 | 64.36 | Ctrl-World 47.66 (표 내 값으로 계산) | +16.70 |
| JEPA 유사도 | 98.88 | 최고 | — |
| 깊이 정밀도 | 97.56 | 최고 | — |

### 시뮬레이션 데이터 엔진
BWM 생성 데이터로 학습된 정책의 평균 성공률은 94.50%로, 실제 데이터 학습보다 23.00 높고, 가장 강력한 대체 세계 시뮬레이터 WoW보다 36.50 높습니다.

| 데이터 소스 | 평균 성공률 | adjust bottle | click bell |
|---------|-----------|---------------|------------|
| BWM 생성 | 94.50% | 98.00% | 91.00% |
| 실제 데이터 | 71.50% | 77.00% | 66.00% |
| WoW 생성 | 58.00% | 45.00% | 71.00% |
| π₀.₅ 제로샷 | 3.50% | 2.00% | 5.00% |

### 시뮬레이션 정책 평가자
BWM은 Pearson 상관 계수 r = 0.978을 달성하여 가장 강력한 기준선 Ctrl-World의 0.008 이내이며, 상관 계수가 0.97보다 높은 유일한 두 평가 세계 시뮬레이터 중 하나입니다.

| 평가자 | Pearson r |
|--------|-----------|
| Ctrl-World | 0.986 |
| BWM | 0.978 |
| WoW | 0.959 |
| RoboScape | 0.863 |
| IRASim | 0.658 |
| Cosmos-Predict 2.5 (action) | 0.483 |

### 물리 로봇
물리 로봇 데이터 엔진 실험에서 BWM 생성 데이터로 학습된 정책은 71.00% 평균 성공률을 달성한 반면, 가장 강력한 평가 세계 시뮬레이터 기준선은 53.33%였습니다. 물리 로봇 정책 평가자의 Pearson 상관 계수 r은 0.908입니다. 물리 로봇 충실도 평가에서 행동 추종은 두 시점 모두에서 사용할 수 없었고, 손목 시점 궤적 정밀도도 사용할 수 없었습니다.

## 경계 및 한계

- 물리 로봇 충실도 평가에는 명백한 사각지대가 있습니다. 행동 추종이 두 시점 모두에서 사용할 수 없고 손목 시점 궤적 정밀도도 사용할 수 없어, 물리 로봇 시나리오에 대한 행동 응답 정밀도 검증이 불완전합니다.
- 논문은 BWM의 물리 로봇 충실도 표 5의 구체적인 수치를 명시하지 않았으며, 해당 표가 텍스트 표임을 언급할 뿐 정량적 비교가 불가능합니다.
- 도메인 특화 후속 학습 경로는 모델 일반화 능력이 제한되어 새로운 embodiment, 카메라 시점 또는 작업 시나리오에 대해 재학습이 필요하며, 논문은 교차 도메인 전이의 구체적인 비용을 명시하지 않았습니다.
- 물리 로봇 모델은 더 적은 작업을 다루고 더 짧은 학습 계획을 사용하여 더 넓은 작업 범위에서의 성능에 영향을 미칠 수 있습니다.
- 초기 관측 증강은 SeedVR-2에 의존하며, 추론 시 시뮬레이터 재생을 사용할 수 없을 때 rollout 품질이 해당 증강 모델의 능력에 제한됩니다.

## 엔지니어링 시사점

BWM을 재현할 때 먼저 데이터 파이프라인의 세 가지 핵심 단계를 확인해야 합니다. 궤적 재생은 원래 실행 순서와 타임스탬프를 변경하지 않고 유지해야 하며, 중첩 세그먼트 샘플링의 윈도우 파라미터(H = 8, K = 72)는 학습 컨텍스트 일치에 직접적인 영향을 미치고, 초기 관측 증강의 SeedVR-2 버전 선택은 rollout 시작점 품질에 영향을 미칩니다. 가장 함정에 빠지기 쉬운 부분은 행동 정규화입니다. 학습 데이터의 제1 및 제99 백분위수를 경계로 사용하여 값을 [ℓ_a, u_a]에 매핑하며, 데이터 분포가 이동하면 정규화 경계를 다시 계산해야 합니다.

학습 구성 측면에서 BWM은 Wan2.2-TI2V-5B에서 초기화되고, 4개 노드 각각 8개의 NVIDIA A800 GPU에서 학습되며, GPU당 배치 크기는 1, 그래디언트 누적 4단계, 유효 배치 크기는 128입니다. WorldArena 제출 모델은 12,000개의 최적화 단계 학습에 약 929 GPU 시간이 필요합니다. 행동 인터페이스는 P = 3개의 경계 행동을 앞에 두고 G = 4로 행동을 그룹화하여 토큰이 시간 압축된 비디오 잠재 변수와 정렬되도록 하며, 이 설계 세부 사항은 행동 시간 정렬에 중요합니다.

하류 팀의 경우 BWM의 데이터 엔진으로서의 가치는 충분히 검증되었습니다. 생성 데이터로 학습된 정책은 시뮬레이션에서 실제 데이터보다 23.00 높고, 물리 로봇에서는 가장 강력한 기준선보다 17.67 높습니다(표 내 값 71.00%와 53.33%로 계산). 그러나 정책 평가자로 사용할 때는 시뮬레이션 평가의 Pearson 상관 계수 0.978과 물리 로봇 평가의 0.908 사이에 차이가 있으므로, sim-to-real 간 평가 신뢰도에 대한 추가 검증이 필요합니다.
