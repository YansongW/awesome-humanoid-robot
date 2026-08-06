---
$id: ent_paper_latency_tolerant_cloud_edge_collaborativ_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latency-Tolerant Cloud-Edge Collaborative Vision-Language-Action Models via Emergent Representational Specialization
  zh: Latency-Tolerant Cloud-Edge Collaborative Vision-Language-Action Models via Emergent Representational Specialization
  ko: Latency-Tolerant Cloud-Edge Collaborative Vision-Language-Action Models via Emergent Representational Specialization
summary:
  en: 'Deploying billion-parameter Vision-Language-Action (VLA) policies on mobile robots creates a systems conflict: semantic
    reasoning benefits from cloud GPUs, whereas closed-loop control must respond locally despite network delay and jitter.
    Existing hierarchical and asynchronous policies improve throughput, but their slow-path representations can still arrive
    stale or require explicit scheduling.'
  zh: 本文提出 CloudEdgeVLA，一种延迟容忍的云-边协同视觉-语言-动作（VLA）模型，通过将时间错位重构为表示学习问题，使云端骨干编码延迟观测为缓慢变化的任务特征，边缘动作头融合最新云特征与实时本地视觉。核心贡献在于引入配对帧双路径训练与视觉增强动作头，在不阻塞等待云响应的前提下，将均匀延迟
    40 步时的任务成功率从基线最高 6.4% 提升至 63.8–78.0%。
  ko: 'Deploying billion-parameter Vision-Language-Action (VLA) policies on mobile robots creates a systems conflict: semantic
    reasoning benefits from cloud GPUs, whereas closed-loop control must respond locally despite network delay and jitter.
    Existing hierarchical and asynchronous policies improve throughput, but their slow-path representations can still arrive
    stale or require explicit scheduling.'
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
- latency
- tolerant
- cloud
- edge
- collaborativ
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
  title: arXiv:2608.00569 Latency-Tolerant Cloud-Edge Collaborative Vision-Language-Action Models via Emer
  url: https://arxiv.org/abs/2608.00569
  date: '2026-08-01'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 CloudEdgeVLA，一种延迟容忍的云-边协同视觉-语言-动作（VLA）模型，通过将时间错位重构为表示学习问题，使云端骨干编码延迟观测为缓慢变化的任务特征，边缘动作头融合最新云特征与实时本地视觉。核心贡献在于引入配对帧双路径训练与视觉增强动作头，在不阻塞等待云响应的前提下，将均匀延迟 40 步时的任务成功率从基线最高 6.4% 提升至 63.8–78.0%。

## 它改变了什么

现有分层异步策略虽提升吞吐量，但慢路径表示过期到达时仍需显式调度或延迟提示，本质上是将时间错位当作推理调度问题处理。本文真正改变的是问题定义：将延迟鲁棒性视为表示学习目标，而非系统调度约束。这意味着云端骨干被训练为主动丢弃瞬态状态信息、保留任务级不变特征，边缘头则学会用实时视觉补偿残余漂移，从而消除对时钟对齐、频率同步或阻塞等待的依赖。

这一转变的深层意义在于，它把“网络延迟”从系统缺陷转化为训练信号，使模型在部署时天然容忍抖动，而非依赖运行时补偿机制。对实际机器人系统而言，这改变了设计权衡：云端可以自由选择计算批次或异步推理，边缘无需为同步牺牲控制频率，系统架构从“尽力同步”转向“异步即默认”。

## 方法拆解

### 系统架构三组件
- **云端 VLA 骨干 f_θ**：7B 参数视觉-语言模型，处理观测与语言指令，输出规划表示 h = f_θ(o, ℓ) ∈ R^{L×D}，其中 L = T × A（动作块长度 × 动作维度），D 为隐藏维度。使用 LoRA 适配，仅在云端运行。
- **边缘视觉编码器 v_ψ**：SigLIP-Base，本地提取实时特征 z_t = v_ψ(o_t) ∈ R^{D_v}，训练期间冻结。
- **边缘动作头 g_ϕ**：对规划特征沿动作维度轴均值池化，将视觉特征投影至同一潜在空间，拼接后经残差 MLP 预测动作块 â_t = g_ϕ(h_{t-k}, z_t) ∈ R^{T×A}。

### 配对帧双路径训练
1. **配对帧提取**：训练样本提供 W=21 个连续观测窗口，当前帧 o_t 与延迟帧 o_{t-d}，其中 d ~ Uniform(1, W-1)。
2. **双前向传播**：两帧均通过云骨干，h_fresh 与 h_stale 均接收梯度（h_stale 不从计算图分离）。
3. **视觉增强预测**：两组规划特征与相同实时视觉特征 z_t 融合。
4. **双路径损失**：L = (1-λ)‖â_fresh - a_t‖₁ + λ‖â_stale - a_t‖₁，其中 λ 从 0 课程式增至 λ_max。
5. **课程学习**：前 n_warmup 步内 λ 递增，使骨干先学习强表示再被要求延迟不变。

### 部署协议
边缘捕获 o_t → 异步非阻塞发送至云 → 云返回 h 时更新 h_received → 边缘计算 z_t → 预测 â_t = g_ϕ(h_received, z_t) → 执行。机器人从不阻塞等待云。

### 涌现表示特化
跨随机延迟 d，仅与瞬时状态相关的特征对动作预测不可靠，而任务身份、目标与粗略进度更稳定。训练目标鼓励（但不保证）对时间位移的不变性，边缘特征 z_t 保留状态敏感信息。

## 关键创新

1. **延迟鲁棒性作为表示学习目标**：首次将时间错位从调度问题转为训练信号，使云端骨干自发特化为任务级不变表示，边缘头学会用实时视觉补偿残余漂移。这一设计消除了对显式延迟提示、时钟同步或阻塞等待的依赖，是架构层面的范式转变。

2. **配对帧双路径损失与课程学习**：同时监督新鲜与延迟路径，且延迟路径不分离梯度，迫使骨干在保持任务表示的同时承受延迟压力。课程式 λ 递增避免早期训练不稳定，使模型先建立强表示再学习延迟不变性，这是训练动态上的关键创新。

3. **视觉增强动作头**：将冻结的轻量级视觉编码器与云特征融合，使边缘头能利用实时状态信息补偿过期规划特征。消融显示，添加视觉编码器将成功率从 31.6% 提升至 95.1%（63.5 点增益），证明实时视觉是延迟补偿的核心机制。

## 实验与结果

### LIBERO 基准（均匀延迟，成功率 %）
| 条件 | OpenVLA | OpenVLA-OFT | UniVLA | VLASH | Ours |
|------|---------|-------------|--------|-------|------|
| d_max=0 | 56.2–84.6 | 93.4–98.6 | 93.2–96.6 | 93.5–99.6 | 91.7–97.9 |
| d_max=10 | 1.2–6.8 | 3.6–26.2 | 27.4–48.2 | 45.6–62.8 | 83.2–94.4 |
| d_max=20 | 0.0–0.2 | 0.0–4.0 | 0.4–21.8 | 5.0–28.2 | 78.1–92.1 |
| d_max=40 | 0.0 | 0.0 | 0.0–3.0 | 0.0–6.4 | 63.8–78.0 |

d_max=40 时，CloudEdgeVLA 保留 63.8–78.0% 成功率，VLASH 最高 6.4%，单路径基线最高 3.0%。Long 套件损失最大（下降 27.9 点），Goal 最稳定（下降 18.5 点）。

### 消融（d_max=10 聚合成功率）
| 配置 | 成功率 |
|------|--------|
| 无视觉编码器 | 31.6% |
| SigLIP-Base（默认） | 95.1% |
| SigLIP-SO400M | 95.8% |
| 仅 L_fresh | 54.8% |
| 仅 L_stale | 89.2% |
| L_fresh + L_stale | 95.1% |

### 真实机器人（静态/动态，10 次试验）
| RTT | VLASH | CE-VLA |
|-----|-------|--------|
| 0ms | 100/90 | 100/90 |
| 400ms | 60/30 | 90/90 |
| 1000ms | 0/0 | 80/70 |

### 离线诊断（d=20）
CloudEdgeVLA 将骨干漂移从 0.391 降至 0.160（减少 59.2%），κ 从 1.082 降至 0.295（减少 72.7%），动作漂移从 0.423 降至 0.047，演示 MAE 从 0.421 降至 0.048。归一化延迟 AUC 为 90.8%（VLASH 为 32.4%）。

## 边界与局限

- 鲁棒性仅对测试的延迟分布建立，不暗示对无界延迟或云断连的容忍；长时间断连可能使任务级上下文失效。
- 配对帧训练需两次骨干前向传播，训练成本翻倍；冻结 RGB 编码器可能缺失深度、力或接触线索。
- 真实机器人结果是单一平台（RTX 5080 边缘 + RTX 4090 云端）的小规模试点，每单元仅 10 次试验，差异为描述性证据而非统计功效验证。
- 离线诊断中，每个任务仅一个回合和八个采样时间步，共十个任务级样本，不能替代闭环成功率；附录 E 显示当前边缘视觉对陈旧云特征的直接修复能力极弱（边缘救援比例 0.03%），优势主要由更稳定的骨干与动作头衰减残余漂移主导。

## 工程启示

复现时先核对三点：一是配对帧窗口 W=21 与延迟采样分布 d ~ Uniform(1, W-1) 是否一致，这直接影响骨干特化程度；二是课程学习 λ 的递增步数 n_warmup，过短会导致骨干未充分学习即被延迟压力破坏，过长则延迟鲁棒性不足；三是边缘视觉编码器必须冻结，否则会破坏与云特征的潜在空间对齐。

最容易踩坑的是评估协议：延迟 d 以环境步数衡量，其墙钟时长取决于控制频率与网络流水线，不能直接换算为毫秒；基线为点估计而 CloudEdgeVLA 报告均值±标准差，比较时需注意方差。工程上，部署时无需任何时钟同步或阻塞等待，但需确保边缘视觉编码器推理延迟低于控制周期，否则实时特征本身也会过期。若下游任务涉及深度或力反馈，需扩展视觉编码器输入模态，当前冻结 RGB 编码器不覆盖这些线索。

## Overview
Deploying billion-parameter Vision-Language-Action (VLA) policies on mobile robots creates a systems conflict: semantic reasoning benefits from cloud GPUs, whereas closed-loop control must respond locally despite network delay and jitter. Existing hierarchical and asynchronous policies improve throughput, but their slow-path representations can still arrive stale or require explicit scheduling and delay cues. We introduce CloudEdgeVLA, a cloud-edge policy that treats temporal misalignment as a representation-learning problem. A cloud VLA encodes delayed observations into slowly varying task features, while a lightweight edge head combines the latest available cloud feature with current local vision. During training, current and randomly delayed frames are paired with the same current action target in fresh and stale paths. This objective encourages the cloud representation to preserve task-level information while the edge path supplies state-sensitive corrections. Across four LIBERO suites, CloudEdgeVLA retains 63.8--78.0% success with a 40-step uniform-delay window, whereas VLASH reaches at most 6.4% and the evaluated single-path baselines at most 3.0%. By removing blocking synchronization from the control loop, the design offers a practical route to scalable VLA deployment in which cloud models can grow while edge computation remains lightweight and responsive.

## 参考
- https://arxiv.org/abs/2608.00569

## 개요

본 논문은 CloudEdgeVLA를 제안한다. 이는 지연 허용적인 클라우드-엣지 협업 비전-언어-행동(VLA) 모델로, 시간적 불일치를 표현 학습 문제로 재구성하여 클라우드 백본이 지연된 관측을 느리게 변화하는 작업 특성으로 인코딩하고, 엣지 행동 헤드가 최신 클라우드 특성과 실시간 로컬 비전을 융합하도록 한다. 핵심 기여는 페어링 프레임 이중 경로 훈련과 비전 강화 행동 헤드를 도입하여, 클라우드 응답을 차단하지 않으면서 균일 지연 40스텝에서 작업 성공률을 베이스라인 최고 6.4%에서 63.8–78.0%로 향상시킨 것이다.

## 그것이 바꾸는 것

기존 계층적 비동기 전략은 처리량을 높이지만, 느린 경로의 표현이 지연되어 도착할 때 여전히 명시적 스케줄링이나 지연 프롬프트가 필요하며, 본질적으로 시간적 불일치를 추론 스케줄링 문제로 취급한다. 본 논문이 진정으로 바꾸는 것은 문제 정의이다: 지연 강건성을 시스템 스케줄링 제약이 아닌 표현 학습 목표로 간주한다. 이는 클라우드 백본이 훈련되어 일시적 상태 정보를 능동적으로 버리고 작업 수준 불변 특성을 유지하며, 엣지 헤드는 실시간 비전으로 잔여 드리프트를 보상하는 법을 학습하여 클록 정렬, 주파수 동기화 또는 차단 대기에 대한 의존성을 제거함을 의미한다.

이 전환의 심층적 의미는 "네트워크 지연"을 시스템 결함에서 훈련 신호로 전환하여, 모델이 배포 시 런타임 보상 메커니즘에 의존하지 않고 자연스럽게 지터를 허용한다는 점이다. 실제 로봇 시스템의 경우, 이는 설계 트레이드오프를 바꾼다: 클라우드는 계산 배치나 비동기 추론을 자유롭게 선택할 수 있고, 엣지는 동기화를 위해 제어 주파수를 희생할 필요가 없으며, 시스템 아키텍처는 "최선의 동기화"에서 "비동기 기본값"으로 전환된다.

## 방법 분해

### 시스템 아키텍처 세 가지 구성 요소
- **클라우드 VLA 백본 f_θ**: 7B 파라미터 비전-언어 모델로, 관측과 언어 명령을 처리하고 계획 표현 h = f_θ(o, ℓ) ∈ R^{L×D}를 출력한다. 여기서 L = T × A(행동 블록 길이 × 행동 차원), D는 은닉 차원이다. LoRA 어댑테이션을 사용하며 클라우드에서만 실행된다.
- **엣지 비전 인코더 v_ψ**: SigLIP-Base로, 로컬에서 실시간 특성 z_t = v_ψ(o_t) ∈ R^{D_v}를 추출하며 훈련 중 동결된다.
- **엣지 행동 헤드 g_ϕ**: 계획 특성을 행동 차원 축을 따라 평균 풀링하고, 비전 특성을 동일한 잠재 공간에 투영한 후, 연결 후 잔차 MLP를 통해 행동 블록 â_t = g_ϕ(h_{t-k}, z_t) ∈ R^{T×A}를 예측한다.

### 페어링 프레임 이중 경로 훈련
1. **페어링 프레임 추출**: 훈련 샘플은 W=21개의 연속 관측 창을 제공하며, 현재 프레임 o_t와 지연 프레임 o_{t-d}를 포함하고, d ~ Uniform(1, W-1)이다.
2. **이중 순전파**: 두 프레임 모두 클라우드 백본을 통과하며, h_fresh와 h_stale 모두 그래디언트를 받는다(h_stale은 계산 그래프에서 분리되지 않음).
3. **비전 강화 예측**: 두 계획 특성 세트가 동일한 실시간 비전 특성 z_t와 융합된다.
4. **이중 경로 손실**: L = (1-λ)‖â_fresh - a_t‖₁ + λ‖â_stale - a_t‖₁, 여기서 λ는 0에서 λ_max로 커리큘럼 방식으로 증가한다.
5. **커리큘럼 학습**: 처음 n_warmup 스텝 동안 λ가 증가하여, 백본이 강한 표현을 먼저 학습한 후 지연 불변성을 요구받는다.

### 배포 프로토콜
엣지가 o_t를 캡처 → 클라우드로 비동기 비차단 전송 → 클라우드가 h를 반환할 때 h_received 업데이트 → 엣지가 z_t 계산 → â_t = g_ϕ(h_received, z_t) 예측 → 실행. 로봇은 클라우드를 기다리기 위해 차단하지 않는다.

### 창발적 표현 특화
무작위 지연 d에 걸쳐, 일시적 상태와만 관련된 특성은 행동 예측에 불신뢰한 반면, 작업 정체성, 목표 및 대략적 진행 상황은 더 안정적이다. 훈련 목표는 시간 이동에 대한 불변성을 장려하지만(보장하지는 않음), 엣지 특성 z_t는 상태 민감 정보를 유지한다.

## 핵심 혁신

1. **지연 강건성을 표현 학습 목표로 전환**: 처음으로 시간적 불일치를 스케줄링 문제에서 훈련 신호로 전환하여, 클라우드 백본이 자발적으로 작업 수준 불변 표현으로 특화되고 엣지 헤드는 실시간 비전으로 잔여 드리프트를 보상하는 법을 학습한다. 이 설계는 명시적 지연 프롬프트, 클록 동기화 또는 차단 대기에 대한 의존성을 제거하며, 아키텍처 수준의 패러다임 전환이다.

2. **페어링 프레임 이중 경로 손실과 커리큘럼 학습**: 신선한 경로와 지연된 경로를 동시에 감독하고, 지연된 경로는 그래디언트를 분리하지 않아 백본이 작업 표현을 유지하면서 지연 압력을 견디도록 강제한다. 커리큘럼 방식의 λ 증가는 초기 훈련 불안정을 피하고, 모델이 강한 표현을 먼저 구축한 후 지연 불변성을 학습하게 하며, 이는 훈련 역학의 핵심 혁신이다.

3. **비전 강화 행동 헤드**: 동결된 경량 비전 인코더를 클라우드 특성과 융합하여, 엣지 헤드가 실시간 상태 정보를 활용해 만료된 계획 특성을 보상할 수 있게 한다. 절제 실험에서 비전 인코더 추가가 성공률을 31.6%에서 95.1%로 향상시켰으며(63.5포인트 이득), 실시간 비전이 지연 보상의 핵심 메커니즘임을 증명한다.

## 실험 및 결과

### LIBERO 벤치마크(균일 지연, 성공률 %)
| 조건 | OpenVLA | OpenVLA-OFT | UniVLA | VLASH | Ours |
|------|---------|-------------|--------|-------|------|
| d_max=0 | 56.2–84.6 | 93.4–98.6 | 93.2–96.6 | 93.5–99.6 | 91.7–97.9 |
| d_max=10 | 1.2–6.8 | 3.6–26.2 | 27.4–48.2 | 45.6–62.8 | 83.2–94.4 |
| d_max=20 | 0.0–0.2 | 0.0–4.0 | 0.4–21.8 | 5.0–28.2 | 78.1–92.1 |
| d_max=40 | 0.0 | 0.0 | 0.0–3.0 | 0.0–6.4 | 63.8–78.0 |

d_max=40에서 CloudEdgeVLA는 63.8–78.0% 성공률을 유지하며, VLASH는 최고 6.4%, 단일 경로 베이스라인은 최고 3.0%이다. Long 스위트가 가장 큰 손실(27.9포인트 하락), Goal이 가장 안정적(18.5포인트 하락)이다.

### 절제 실험(d_max=10 집계 성공률)
| 구성 | 성공률 |
|------|--------|
| 비전 인코더 없음 | 31.6% |
| SigLIP-Base(기본값) | 95.1% |
| SigLIP-SO400M | 95.8% |
| L_fresh만 | 54.8% |
| L_stale만 | 89.2% |
| L_fresh + L_stale | 95.1% |

### 실제 로봇(정적/동적, 10회 시행)
| RTT | VLASH | CE-VLA |
|-----|-------|--------|
| 0ms | 100/90 | 100/90 |
| 400ms | 60/30 | 90/90 |
| 1000ms | 0/0 | 80/70 |

### 오프라인 진단(d=20)
CloudEdgeVLA는 백본 드리프트를 0.391에서 0.160으로(59.2% 감소), κ를 1.082에서 0.295로(72.7% 감소), 행동 드리프트를 0.423에서 0.047로, 데모 MAE를 0.421에서 0.048로 줄였다. 정규화된 지연 AUC는 90.8%(VLASH는 32.4%)이다.

## 경계 및 한계

- 강건성은 테스트된 지연 분포에 대해서만 확립되며, 무한 지연이나 클라우드 연결 끊김에 대한 허용을 암시하지 않는다; 장기간 연결 끊김은 작업 수준 컨텍스트를 무효화할 수 있다.
- 페어링 프레임 훈련은 두 번의 백본 순전파가 필요하여 훈련 비용이 두 배가 된다; 동결된 RGB 인코더는 깊이, 힘 또는 접촉 신호를 놓칠 수 있다.
- 실제 로봇 결과는 단일 플랫폼(RTX 5080 엣지 + RTX 4090 클라우드)의 소규모 파일럿으로, 각 유닛당 10회 시행이며, 차이는 통계적 검증이 아닌 기술적 증거이다.
- 오프라인 진단에서 각 작업당 하나의 에피소드와 8개의 샘플링 시간 스텝, 총 10개의 작업 수준 샘플로, 폐루프 성공률을 대체할 수 없다; 부록 E는 현재 엣지 비전이 만료된 클라우드 특성을 직접 복구하는 능력이 극히 약함(엣지 구조 비율 0.03%)을 보여주며, 이점은 주로 더 안정적인 백본과 행동 헤드가 잔여 드리프트를 감쇠시키는 데서 비롯된다.

## 공학적 시사점

재현 시 세 가지를 먼저 확인하라: 첫째, 페어링 프레임 창 W=21과 지연 샘플링 분포 d ~ Uniform(1, W-1)이 일치하는지, 이는 백본 특화 정도에 직접 영향을 미친다; 둘째, 커리큘럼 학습 λ의 증가 스텝 수 n_warmup, 너무 짧으면 백본이 충분히 학습되기 전에 지연 압력으로 파괴되고, 너무 길면 지연 강건성이 부족하다; 셋째, 엣지 비전 인코더는 반드시 동결되어야 하며, 그렇지 않으면 클라우드 특성과의 잠재 공간 정렬이 깨진다.

가장 쉽게 실수하는 부분은 평가 프로토콜이다: 지연 d는 환경 스텝 수로 측정되며, 그 벽시계 시간은 제어 주파수와 네트워크 파이프라인에 따라 달라져 밀리초로 직접 환산할 수 없다; 베이스라인은 점 추정이고 CloudEdgeVLA는 평균±표준편차를 보고하므로 비교 시 분산을 주의해야 한다. 공학적으로 배포 시 클록 동기화나 차단 대기가 필요 없지만, 엣지 비전 인코더 추론 지연이 제어 주기보다 짧아야 하며, 그렇지 않으면 실시간 특성 자체도 만료된다. 하류 작업이 깊이 또는 힘 피드백을 포함하면 비전 인코더 입력 모달리티를 확장해야 하며, 현재 동결된 RGB 인코더는 이러한 신호를 다루지 않는다.
