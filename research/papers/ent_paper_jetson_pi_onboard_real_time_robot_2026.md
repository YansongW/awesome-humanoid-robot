---
$id: ent_paper_jetson_pi_onboard_real_time_robot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference'
  zh: 'Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference'
  ko: 'Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference'
summary:
  en: Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying
    VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational
    complexity, which leads to substantial inference latency and low control frequency. Asynchronous inference can partially
    mask this latency by parallelizing action.
  zh: 本文提出 Jetson-PI，一个面向 Jetson Orin/Thor 等低功耗机载设备的实时 VLA 控制框架。核心贡献是 Foresight-Aligned Asynchronous Correction（前瞻对齐异步校正）与
    Confidence-based Scheduling Optimization（基于置信度的调度优化），配合基于 llama.cpp 的系统级加速，将 π₀.₅ 在 Orin 上的控制频率从 0.7 Hz 提升至 6.06 Hz（8.66×），并在
    LIBERO 基准上超越现有异步方法。
  ko: Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying
    VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational
    complexity, which leads to substantial inference latency and low control frequency. Asynchronous inference can partially
    mask this latency by parallelizing action.
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
- jetson
- pi
- onboard
- real
- time
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
  title: 'arXiv:2607.12659 Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchr'
  url: https://arxiv.org/abs/2607.12659
  date: '2026-07-14'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Jetson-PI，一个面向 Jetson Orin/Thor 等低功耗机载设备的实时 VLA 控制框架。核心贡献是 Foresight-Aligned Asynchronous Correction（前瞻对齐异步校正）与 Confidence-based Scheduling Optimization（基于置信度的调度优化），配合基于 llama.cpp 的系统级加速，将 π₀.₅ 在 Orin 上的控制频率从 0.7 Hz 提升至 6.06 Hz（8.66×），并在 LIBERO 基准上超越现有异步方法。

## 它改变了什么

VLA 模型在高端 GPU 上表现优异，但部署到 Jetson Orin 这类机载设备时，推理延迟高达 1.4 秒（π₀.₅），控制频率仅 0.7 Hz，导致机器人对环境变化反应迟钝。异步推理虽能隐藏部分延迟，却引入感知-执行错位：动作专家基于过时的视觉上下文生成动作，而环境已发生变化。现有方法如 VLASH 仅预测未来机器人状态（qₜ₊Δ），无法反映环境变化；RTC 等也未解决根本错位问题。

Jetson-PI 真正改变了异步 VLA 推理的范式：不再试图让 VLM 跟上动作节奏，而是训练一个轻量级模块预测未来 VLM 状态，使动作专家能基于未来环境生成动作。同时，它重新定义了 VLM 与动作专家的角色——VLM 从每步必调用的组件变为按需调用的观察者，通过置信度调度器动态决定何时刷新环境上下文。这解决了异步推理中反应时间与精度不可兼得的矛盾，使机载 VLA 部署从实验室演示走向实用。

## 方法拆解

### 1. Foresight-Aligned Asynchronous Correction（前瞻对齐异步校正）
- 训练 40M 参数（VLA 的 1%）的未来校正模块，输入为 t 时刻压缩的 VLM 最终层输出（经 Q-Former 压缩至 T′=4 token）与已提交动作序列（a_t 至 a_{t+Δ-1}）。
- 动作序列经 MLP+Transformer 处理取最后 token，与压缩 VLM 输出拼接后经两个 Transformer 块，分叉为校正头（预测 t+Δ 时刻压缩 VLM 状态 ĥₜ₊Δ）与置信度头（输出标量 ĉ）。
- 损失函数：L_predict = ‖ĥₜ₊Δ − hₜ₊Δ‖₂，L_total = L_predict + λ‖ĉ + L_predict‖₂。训练时随机采样 Δ，使模块适应不同推理延迟。

### 2. 两阶段 Correction-aware 训练
- 阶段 1：使用 t+Δ 时刻 ground-truth VLM 状态训练压缩器和动作专家（动作损失），使其学会从未来隐藏状态提取有用信息。
- 阶段 2：固定阶段 1 参数，训练未来校正模块预测 t+Δ 时刻压缩 VLM 状态，同时输出置信度。批量大小 32，学习率 3e-4，AdamW，阶段 1/2 分别训练 30,000/25,000 步。

### 3. Confidence-based Scheduling Optimization（基于置信度的调度优化）
- 当 ĉ > θ（θ < 0.0）时跳过 VLM，动作专家直接基于预测的未来状态生成动作；当 ĉ ≤ θ 时调用 VLM 刷新环境上下文，更新 KV buffer 和隐藏状态 buffer。
- 动作块大小 H=20，L=H−Δ，动作专家推理时间估计 Δ_ae = ⌈Δ/3⌉。

### 4. 系统级加速（基于 llama.cpp）
- **计算图复用**：语言指令 padding 到固定长度保证 token 长度恒定，复用首次推理的 CUDA graph。
- **GPU 驻留中间缓冲**：ViT→LLM→动作专家的中间结果保留在 GPU 内存，避免写回 CPU。
- **Flow matching 展开**：将 10 步去噪迭代融合为统一计算图，减少图调用次数。

### 5. 为何不并行化 VLM 与动作专家
- Roofline 分析：矩阵乘法执行时间 = max(M*K*N/compute throughput, 2*(M*K+K*N)/bandwidth)。
- 在 RTX 4090 上 VLM 计算受限、动作专家带宽受限，并行可充分利用资源；在机载设备上两者均带宽受限（Orin 平衡计算强度 1953/2685，Thor 3736），并行导致带宽争用。

## 关键创新

1. **未来状态预测而非未来图像/KV 缓存校正**：直接预测压缩的 VLM 最终层输出，避免重建高维图像或逐层校正 KV cache 的计算开销。40M 参数（VLA 的 1%）的模块即可捕捉环境变化，这是异步 VLA 推理中首次以如此轻量的方式解决感知-执行错位。

2. **置信度驱动的自适应调度**：将 VLM 从每步必调用变为按需调用，通过置信度阈值 θ 动态平衡反应时间与精度。这改变了 VLM 与动作专家的协作模式——VLM 成为环境观察者而非动作生成者，动作专家成为实时决策者。在 Orin 上反应时间降低 2.11×，控制频率提升至 1.48 Hz。

3. **面向机载设备的系统级优化组合**：计算图复用、GPU 驻留中间缓冲、flow matching 展开三项优化正交于量化/剪枝，不改变模型计算。在 Orin 上实现 8.66× 控制频率提升（0.7→6.06 Hz），相比 vla.cpp 提升 5.41×。这是首个在 Jetson 级设备上达到实用控制频率的 VLA 部署方案。

## 实验与结果

### LIBERO 基准（π₀.₅，跨 Δ=1 至 9 平均成功率）
| 方法 | SPATIAL | OBJECT | GOAL | LIBERO-10 |
|------|---------|--------|------|-----------|
| VLASH | 74.4 | 86.1 | 84.2 | 81.3 |
| RTC | 92.6 | 96.6 | 94.1 | 86.4 |
| Ours | 97.0 | 98.0 | 96.5 | 92.2 |
| +Sched | 97.4 | 98.6 | 96.8 | 92.5 |

- Δ=9 时（跨四数据集平均）：相比 VLASH 提升 45.6%，相比 RTC 提升 7.0%。
- 总体：相比 VLASH 平均提升 14.8%，相比 RTC 平均提升 3.9%。

### 延迟与控制频率（Jetson Orin，π₀.₅）
| 方法 | Total (ms) | Reaction Time (ms) | Control Frequency (Hz) |
|------|------------|--------------------|------------------------|
| Naive PI05 | 1420.8 | 1420.8 | 0.70 |
| +Schedule opt. | 1420.8 | 674.9 | 1.48 |
| +Graph reuse | 476.1 | 227.0 | 4.41 |
| +Intermediate Buffer & Unroll | 412.9 | 165.1 | 6.06 |

- 调度优化：Orin 反应时间降低 2.11×，Thor 降低 1.87×。
- 图复用：Orin 反应时间降低 2.96×。
- GPU 驻留中间缓冲与 flow matching 展开：动作专家加速 1.50×（Orin）和 1.59×（Thor）。
- 总体控制频率提升：Orin 8.66×、Thor 3.48×（相比 naive PyTorch）；相比 vla.cpp 提升 5.41×。

### 真实世界叠衣服任务（XR-1 模型，Jetson Orin，动作执行 15 Hz）
| 方法 | Picking | Folding | Placing |
|------|---------|---------|---------|
| RTX 4090 (Baseline) | 10/10 | 7/10 | 10/10 |
| Jetson Orin (Naive Async) | 6/10 | 0/10 | 5/10 |
| Jetson-PI (Ours) | 10/10 | 8/10 | 9/10 |

结果表明 Jetson-PI 在机载设备上接近 RTX 4090 水平，而 naive async 在折叠任务上完全失败（0/10）。

## 边界与局限

- 机载平台在计算和带宽上相对 GPU 集群存在根本性限制；随着模型参数量和 batch size 扩大，Jetson-PI 的性能提升可能无法完全弥合与高端 GPU 部署的差距。
- 方法聚焦于不改变模型计算的系统级优化，未与量化、剪枝等技术结合验证。
- 未来校正模块依赖训练时随机采样 Δ 的分布，若实际推理延迟超出训练分布范围，预测精度可能退化（论文未明确具体范围）。
- 真实世界实验仅在单一机器人平台（PrimeBot X2-W）和单一任务（叠衣服）上验证，泛化性未充分证明。
- 置信度阈值 θ 的选取（示例为 -0.2）未给出系统调优方法，可能依赖经验。

## 工程启示

- **先核对硬件带宽**：Jetson-PI 的核心假设是机载设备上 VLM 与动作专家均带宽受限。复现前先用 roofline 模型（平衡计算强度 = TOPS/Bandwidth × 1000）确认目标设备是否满足此条件，否则并行化可能更优。
- **训练数据与 Δ 分布匹配**：未来校正模块训练时随机采样 Δ，但实际部署时 Δ 由硬件和功率模式决定。建议在训练集中覆盖目标设备的典型 Δ 范围，并验证 Δ_ae = ⌈Δ/3⌉ 的估计是否适用于你的动作专家架构。
- **系统级优化顺序敏感**：调度优化（+Schedule opt.）不改变总延迟但降低反应时间；图复用和 GPU 驻留缓冲是延迟降低的主要来源。复现时先实现图复用（需固定 token 长度），再考虑 flow matching 展开，后者首次推理有额外开销。
- **置信度阈值 θ 需调参**：θ 控制 VLM 调用频率，过小则反应时间长，过大则精度下降。建议在验证集上扫描 θ（如 -0.5 至 0.0），观察成功率与反应时间的权衡曲线。
- **最易踩坑**：语言指令 padding 到固定长度是图复用的前提，若指令长度波动大，CUDA graph 复用会失效。另外，GPU 驻留中间缓冲需精确计算 ViT→LLM→动作专家的中间张量大小，预留不足会导致内存溢出。

## Overview
Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency. Asynchronous inference can partially mask this latency by parallelizing action execution and subsequent inference, but it introduces two critical issues: perception-execution misalignment and long reaction time. In this paper, we propose Jetson-PI, a method for efficient VLA deployment on onboard devices via Foresight-Aligned Asynchronous Correction. To address misalignment, we train a lightweight future correction module that predicts future environment representation conditioned on committed actions, enabling the action expert to directly predict actions from the future time step. To reduce reaction time, we introduce confidence-based scheduling optimization that adaptively balances VLM and action expert invocations, complemented by system-level accelerations including CUDA graph reuse, GPU-resident intermediate buffering, and flow unrolling. Extensive experiments demonstrate that Jetson-PI achieves 8.66x and 5.41x improvements in control frequency compared with naive PyTorch and vla.cpp on NVIDIA Jetson Orin, while outperforming VLASH by 14.8\% in average success rate on the LIBERO benchmark. The code of our asynchronous algorithm is available on https://github.com/PKU-SEC-Lab/Jetson-PI, and our efficient llama.cpp-based inference engine is available on https://github.com/PKU-SEC-Lab/Jetson-PI-Edge.

## 参考
- https://arxiv.org/abs/2607.12659

## 개요

본 논문은 Jetson Orin/Thor 등 저전력 온보드 장치를 위한 실시간 VLA 제어 프레임워크인 Jetson-PI를 제안한다. 핵심 기여는 Foresight-Aligned Asynchronous Correction(전향 정렬 비동기 보정)과 Confidence-based Scheduling Optimization(신뢰도 기반 스케줄링 최적화)이며, llama.cpp 기반 시스템 수준 가속을 결합하여 Orin에서 π₀.₅의 제어 주파수를 0.7 Hz에서 6.06 Hz(8.66배)로 향상시키고 LIBERO 벤치마크에서 기존 비동기 방식을 능가한다.

## 무엇을 변화시키는가

VLA 모델은 고성능 GPU에서 우수한 성능을 보이지만, Jetson Orin과 같은 온보드 장치에 배포할 경우 추론 지연 시간이 1.4초(π₀.₅)에 달하고 제어 주파수가 0.7 Hz에 불과하여 로봇이 환경 변화에 둔감하게 반응한다. 비동기 추론은 일부 지연 시간을 숨길 수 있지만 인지-실행 불일치를 초래한다: 동작 전문가가 과거 시각적 맥락을 기반으로 동작을 생성하는 동안 환경은 이미 변화한 상태다. VLASH와 같은 기존 방법은 미래 로봇 상태(qₜ₊Δ)만 예측할 뿐 환경 변화를 반영하지 못하며, RTC 등도 근본적인 불일치 문제를 해결하지 못한다.

Jetson-PI는 비동기 VLA 추론의 패러다임을 실질적으로 변화시킨다: VLM이 동작 리듬을 따라잡도록 하는 대신, 경량 모듈을 훈련하여 미래 VLM 상태를 예측함으로써 동작 전문가가 미래 환경을 기반으로 동작을 생성할 수 있게 한다. 동시에 VLM과 동작 전문가의 역할을 재정의한다 — VLM은 매 단계 호출되는 구성 요소에서 필요 시 호출되는 관찰자로 전환되며, 신뢰도 스케줄러가 환경 맥락을 새로 고칠 시점을 동적으로 결정한다. 이는 비동기 추론에서 반응 시간과 정밀도를 동시에 얻을 수 없던 모순을 해결하여 온보드 VLA 배포를 실험실 데모에서 실용적 수준으로 끌어올린다.

## 방법 분석

### 1. Foresight-Aligned Asynchronous Correction(전향 정렬 비동기 보정)
- 4천만 파라미터(VLA의 1%) 규모의 미래 보정 모듈을 훈련하며, 입력은 t 시점의 압축된 VLM 최종 레이어 출력(Q-Former로 T′=4 토큰으로 압축)과 제출된 동작 시퀀스(a_t ~ a_{t+Δ-1})이다.
- 동작 시퀀스는 MLP+Transformer를 거쳐 마지막 토큰을 취하고, 압축된 VLM 출력과 결합된 후 두 개의 Transformer 블록을 통과하여 보정 헤드(t+Δ 시점의 압축 VLM 상태 ĥₜ₊Δ 예측)와 신뢰도 헤드(스칼라 ĉ 출력)로 분기된다.
- 손실 함수: L_predict = ‖ĥₜ₊Δ − hₜ₊Δ‖₂, L_total = L_predict + λ‖ĉ + L_predict‖₂. 훈련 중 Δ를 무작위 샘플링하여 모듈이 다양한 추론 지연 시간에 적응하도록 한다.

### 2. 2단계 Correction-aware 훈련
- 1단계: t+Δ 시점의 ground-truth VLM 상태를 사용하여 압축기와 동작 전문가를 훈련(동작 손실)하여 미래 은닉 상태에서 유용한 정보를 추출하는 방법을 학습시킨다.
- 2단계: 1단계 파라미터를 고정하고, 미래 보정 모듈을 훈련하여 t+Δ 시점의 압축 VLM 상태를 예측하면서 신뢰도를 출력한다. 배치 크기 32, 학습률 3e-4, AdamW, 1/2단계 각각 30,000/25,000 스텝 훈련.

### 3. Confidence-based Scheduling Optimization(신뢰도 기반 스케줄링 최적화)
- ĉ > θ(θ < 0.0)일 때 VLM을 건너뛰고 동작 전문가가 예측된 미래 상태를 기반으로 직접 동작을 생성한다; ĉ ≤ θ일 때 VLM을 호출하여 환경 맥락을 새로 고치고 KV 버퍼와 은닉 상태 버퍼를 업데이트한다.
- 동작 블록 크기 H=20, L=H−Δ, 동작 전문가 추론 시간 추정 Δ_ae = ⌈Δ/3⌉.

### 4. 시스템 수준 가속(llama.cpp 기반)
- **계산 그래프 재사용**: 언어 명령을 고정 길이로 패딩하여 토큰 길이를 일정하게 유지하고, 첫 추론의 CUDA 그래프를 재사용한다.
- **GPU 상주 중간 버퍼**: ViT→LLM→동작 전문가의 중간 결과를 GPU 메모리에 유지하여 CPU로의 쓰기 저장을 방지한다.
- **Flow matching 언롤링**: 10단계 노이즈 제거 반복을 단일 계산 그래프로 융합하여 그래프 호출 횟수를 줄인다.

### 5. VLM과 동작 전문가를 병렬화하지 않는 이유
- Roofline 분석: 행렬 곱셈 실행 시간 = max(M*K*N/연산 처리량, 2*(M*K+K*N)/대역폭).
- RTX 4090에서는 VLM이 연산 제한적이고 동작 전문가가 대역폭 제한적이므로 병렬화가 자원을 최대한 활용할 수 있다; 온보드 장치에서는 둘 다 대역폭 제한적이며(Orin 균형 연산 강도 1953/2685, Thor 3736), 병렬화는 대역폭 경합을 초래한다.

## 핵심 혁신

1. **미래 이미지/KV 캐시 보정이 아닌 미래 상태 예측**: 압축된 VLM 최종 레이어 출력을 직접 예측하여 고차원 이미지 재구성이나 레이어별 KV 캐시 보정의 계산 오버헤드를 피한다. 4천만 파라미터(VLA의 1%) 모듈만으로 환경 변화를 포착할 수 있으며, 이는 비동기 VLA 추론에서 인지-실행 불일치를 이렇게 경량화된 방식으로 해결한 첫 사례다.

2. **신뢰도 기반 적응형 스케줄링**: VLM을 매 단계 필수 호출에서 필요 시 호출로 전환하고, 신뢰도 임계값 θ로 반응 시간과 정밀도를 동적으로 균형 있게 조절한다. 이는 VLM과 동작 전문가의 협업 방식을 변화시킨다 — VLM은 환경 관찰자가 되고 동작 전문가는 실시간 의사 결정자가 된다. Orin에서 반응 시간이 2.11배 감소하고 제어 주파수가 1.48 Hz로 향상된다.

3. **온보드 장치를 위한 시스템 수준 최적화 조합**: 계산 그래프 재사용, GPU 상주 중간 버퍼, flow matching 언롤링의 세 가지 최적화는 양자화/가지치기와 직교하며 모델 계산을 변경하지 않는다. Orin에서 8.66배 제어 주파수 향상(0.7→6.06 Hz)을 달성하고, vla.cpp 대비 5.41배 향상된다. 이는 Jetson급 장치에서 실용적 제어 주파수에 도달한 최초의 VLA 배포 방안이다.

## 실험 및 결과

### LIBERO 벤치마크(π₀.₅, Δ=1~9 평균 성공률)
| 방법 | SPATIAL | OBJECT | GOAL | LIBERO-10 |
|------|---------|--------|------|-----------|
| VLASH | 74.4 | 86.1 | 84.2 | 81.3 |
| RTC | 92.6 | 96.6 | 94.1 | 86.4 |
| Ours | 97.0 | 98.0 | 96.5 | 92.2 |
| +Sched | 97.4 | 98.6 | 96.8 | 92.5 |

- Δ=9일 때(4개 데이터셋 평균): VLASH 대비 45.6% 향상, RTC 대비 7.0% 향상.
- 전체: VLASH 대비 평균 14.8% 향상, RTC 대비 평균 3.9% 향상.

### 지연 시간 및 제어 주파수(Jetson Orin, π₀.₅)
| 방법 | Total (ms) | Reaction Time (ms) | Control Frequency (Hz) |
|------|------------|--------------------|------------------------|
| Naive PI05 | 1420.8 | 1420.8 | 0.70 |
| +Schedule opt. | 1420.8 | 674.9 | 1.48 |
| +Graph reuse | 476.1 | 227.0 | 4.41 |
| +Intermediate Buffer & Unroll | 412.9 | 165.1 | 6.06 |

- 스케줄링 최적화: Orin 반응 시간 2.11배 감소, Thor 1.87배 감소.
- 그래프 재사용: Orin 반응 시간 2.96배 감소.
- GPU 상주 중간 버퍼 및 flow matching 언롤링: 동작 전문가 1.50배(Orin) 및 1.59배(Thor) 가속.
- 전체 제어 주파수 향상: Orin 8.66배, Thor 3.48배(naive PyTorch 대비); vla.cpp 대비 5.41배 향상.

### 실제 세계 옷 접기 작업(XR-1 모델, Jetson Orin, 동작 실행 15 Hz)
| 방법 | 집기 | 접기 | 놓기 |
|------|---------|---------|---------|
| RTX 4090 (Baseline) | 10/10 | 7/10 | 10/10 |
| Jetson Orin (Naive Async) | 6/10 | 0/10 | 5/10 |
| Jetson-PI (Ours) | 10/10 | 8/10 | 9/10 |

결과는 Jetson-PI가 온보드 장치에서 RTX 4090 수준에 근접함을 보여주며, naive async는 접기 작업에서 완전히 실패(0/10)함을 보여준다.

## 경계 및 한계

- 온보드 플랫폼은 계산 및 대역폭 측면에서 GPU 클러스터 대비 근본적인 제약이 있다; 모델 파라미터 수와 배치 크기가 커질수록 Jetson-PI의 성능 향상이 고성능 GPU 배포와의 격차를 완전히 메우지 못할 수 있다.
- 이 방법은 모델 계산을 변경하지 않는 시스템 수준 최적화에 초점을 맞추며, 양자화, 가지치기 등의 기술과 결합하여 검증되지 않았다.
- 미래 보정 모듈은 훈련 중 무작위 샘플링된 Δ 분포에 의존하며, 실제 추론 지연 시간이 훈련 분포 범위를 벗어나면 예측 정밀도가 저하될 수 있다(논문은 구체적인 범위를 명시하지 않음).
- 실제 세계 실험은 단일 로봇 플랫폼(PrimeBot X2-W)과 단일 작업(옷 접기)에서만 검증되어 일반화 가능성이 충분히 입증되지 않았다.
- 신뢰도 임계값 θ의 선택(예시는 -0.2)에 대한 체계적인 튜닝 방법이 제시되지 않아 경험에 의존할 수 있다.

## 엔지니어링 시사점

- **먼저 하드웨어 대역폭을 확인하라**: Jetson-PI의 핵심 가정은 온보드 장치에서 VLM과 동작 전문가가 모두 대역폭 제한적이라는 것이다. 재현 전에 roofline 모델(균형 연산 강도 = TOPS/Bandwidth × 1000)로 대상 장치가 이 조건을 충족하는지 확인하라, 그렇지 않으면 병렬화가 더 나을 수 있다.
- **훈련 데이터와 Δ 분포를 일치시켜라**: 미래 보정 모듈 훈련 시 Δ를 무작위 샘플링하지만, 실제 배포 시 Δ는 하드웨어와 전력 모드에 의해 결정된다. 훈련 세트에 대상 장치의 일반적인 Δ 범위를 포함하고, Δ_ae = ⌈Δ/3⌉ 추정이 동작 전문가 아키텍처에 적용되는지 검증하라.
- **시스템 수준 최적화 순서가 중요하다**: 스케줄링 최적화(+Schedule opt.)는 총 지연 시간을 변경하지 않지만 반응 시간을 줄인다; 그래프 재사용과 GPU 상주 버퍼가 지연 시간 감소의 주요 원천이다. 재현 시 먼저 그래프 재사용(토큰 길이 고정 필요)을 구현한 다음 flow matching 언롤링을 고려하라, 후자는 첫 추론에 추가 오버헤드가 있다.
- **신뢰도 임계값 θ는 튜닝이 필요하다**: θ는 VLM 호출 빈도를 제어하며, 너무 작으면 반응 시간이 길어지고 너무 크면 정밀도가 저하된다. 검증 세트에서 θ를 스캔(예: -0.5 ~ 0.0)하여 성공률과 반응 시간의 트레이드오프 곡선을 관찰하라.
- **가장 흔한 함정**: 언어 명령을 고정 길이로 패딩하는 것은 그래프 재사용의 전제 조건이며, 명령 길이 변동이 크면 CUDA 그래프 재사용이 실패한다. 또한 GPU 상주 중간 버퍼는 ViT→LLM→동작 전문가의 중간 텐서 크기를 정확히 계산해야 하며, 여유 공간이 부족하면 메모리 오버플로가 발생한다.
