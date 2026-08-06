---
$id: ent_paper_reflex_real_time_vla_control_through_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reflex: Real-Time VLA Control through Streaming Inference'
  zh: 'Reflex: Real-Time VLA Control through Streaming Inference'
  ko: 'Reflex: Real-Time VLA Control through Streaming Inference'
summary:
  en: 'Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising
    nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching,
    forcing a choice between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse. We present \textbf{Reflex},
    a framework that enables.'
  zh: Reflex 是一套面向流匹配类视觉-语言-动作（VLA）模型的实时推理系统，通过时间步不变性洞察、分区注意力缓存与异步流水线协同设计，将 Pi0.5 在 LIBERO 上的推理延迟从 135.2ms 降至 52.4ms（2.58×
    加速），并实现 50Hz 稳定流式控制。核心贡献在于将流匹配去噪循环与 KV 缓存机制从根本性冲突中解耦，同时保持与全批量注意力在数学上的精确等价。
  ko: 'Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising
    nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching,
    forcing a choice between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse. We present \textbf{Reflex},
    a framework that enables.'
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
- reflex
- real
- time
- vla
- control
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
  title: 'arXiv:2607.14695 Reflex: Real-Time VLA Control through Streaming Inference'
  url: https://arxiv.org/abs/2607.14695
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

Reflex 是一套面向流匹配类视觉-语言-动作（VLA）模型的实时推理系统，通过时间步不变性洞察、分区注意力缓存与异步流水线协同设计，将 Pi0.5 在 LIBERO 上的推理延迟从 135.2ms 降至 52.4ms（2.58× 加速），并实现 50Hz 稳定流式控制。核心贡献在于将流匹配去噪循环与 KV 缓存机制从根本性冲突中解耦，同时保持与全批量注意力在数学上的精确等价。

## 它改变了什么

流匹配 VLA 模型在机器人控制中的落地困境，本质上是生成式架构的迭代去噪特性与实时控制回路对延迟的硬约束之间的结构性矛盾。此前所有工作都默认必须在这两者间做非此即彼的取舍：要么接受 O(N²) 的逐帧全量重计算换取数学正确性，要么采用数学上不正确的缓存复用换取速度。Reflex 真正改变的是打破了这个二选一的框架——它证明了在特定架构约束下，缓存复用可以做到与全量重计算完全等价，从而将问题从"如何近似"转变为"如何精确且高效"。

这一转变的深层意义在于，它重新定义了 VLA 实时化的瓶颈所在。过去研究者聚焦于减少单次推理的计算量，而 Reflex 指出真正的延迟杀手是同步阻塞导致的执行暂停，以及去噪循环中因时间步注入导致的缓存失效。通过将感知编码器与去噪循环在时间步维度上解耦，并据此设计分区注意力机制，Reflex 将系统性问题转化为可工程化的缓存管理问题，使得 50Hz 控制频率不再是理论目标而是可复现的工程现实。

## 方法拆解

### 核心前提：时间步不变性
Reflex 的整个方法建立在感知编码器不接收去噪时间步这一架构事实之上（∂Enc/∂t_k = 0）。这意味着视觉观察的编码结果在整个去噪循环中保持不变，其 KV 缓存可以被安全地复用，无需随迭代步数更新。

### 分区注意力（Partitioned Attention）
将注意力上下文按语义划分为三个区域，各自采用不同的缓存策略：
- **Static Prefix**：系统指令 token，计算一次后永久固定于 KV 缓存，不参与任何更新。
- **Sliding History**：最近 N 帧视觉观察的 FIFO 队列，新帧到达时淘汰最旧帧，保持恒定内存占用。LIBERO 上 N=10 帧（约 300ms 历史）为最优操作点。
- **Dynamic Suffix**：瞬态流状态 x^(k) 与时间步嵌入，每个去噪周期结束后重置。

注意力计算形式化为：
Attn(x^(k)) = Softmax(Q^(k)[K_pin; K_slide(t); K_dyn(k)]^T/√d) × [V_pin; V_slide(t); V_dyn(k)]

该公式在固定输入与固定观测窗口下，与全批量注意力产生逐位相同的输出（MSE 恰好为 0.00），同时将缓存更新复杂度降为 O(1)。

### 工程化缓存管理
- **Incremental Prefill**：每步仅编码最新观察帧，而非重新处理全部历史。
- **Manual Cache Merging**：进入去噪循环前，将静态前缀与滑动历史预合并为单一连续内存缓冲区，消除逐次 torch.cat 开销。
- **静态环形缓冲区**：初始化时预分配整体张量 B ∈ ℝ^{L×N_max×H×D}，通过自定义指针算术循环索引，实现零动态分配与 O(1) 内存访问。

### 数值稳定性：AdaRMSNorm
流匹配模型在长时间流式推理中，因连续暴露于高方差初始化噪声，标准 BF16 混合精度会频繁产生 NaN/Inf。AdaRMSNorm 将 RMS 统计量计算强制在 FP32 执行，并通过门控 MLP 引入时间步与本体感受状态的自适应缩放：
AdaRMSNorm(x,c) = x/RMS(x) ⊙ γ(c)，其中 γ(c) = 1 + MLP(c)，c = [t_k, s_t]

### 异步流水线与延迟补偿
- **双线程架构**：线程 A（视觉）连续编码观察并推送 KV 对；线程 B（策略）作为消费者查询最新缓存生成动作块。
- **Future-Conditional State Prediction**：用系统最后命令的目标动作替代过时传感器状态（ŝ_{t+Δ} ≈ a_t^cmd），作为轻量级延迟补偿启发式。
- **Adaptive Overlap Scheduling**：基于实时推理延迟测量动态调整前瞻 K，确保动作块无缝衔接。

### 算子融合
将 QKV 投影融合为单一打包核（W_QKV = [W_Q; W_K; W_V]），合并 SwiGLU 块中的 Gate 与 Up 投影，每层减少 50% 核启动，单流推理获得 15–20% 墙钟加速。

## 关键创新

**1. 时间步不变性作为缓存复用的理论基石**：此前所有 KV 缓存复用方案都因流匹配模型的时间步注入而失效，Reflex 首次明确指出感知编码器在功能上独立于去噪循环，并据此设计了严格的分区注意力机制。这一洞察不仅具有工程价值，更提供了理论保证——在满足时间步不变性与 FIFO 驱逐条件下，输出与全批量注意力完全等价（Proposition A.1），而非近似。

**2. 将数值稳定性问题纳入系统设计**：长时间流式推理中的混合精度退化是一个此前未被充分认识的问题。Reflex 通过 AdaRMSNorm 将 RMS 统计量强制 FP32 计算，同时保持门控 MLP 在 BF16 运行，在几乎不增加延迟（+0.4ms）的前提下将最大稳定步数从 120–220 提升至超过 2000，且完全消除 NaN/Inf 事件。这是将数值鲁棒性作为一等公民纳入推理系统设计的罕见案例。

**3. 异步执行与延迟补偿的协同设计**：Reflex 不仅消除计算与执行之间的阻塞间隙，还通过 Future-Conditional State Prediction 主动补偿因异步引入的观测延迟。在四延迟步场景下，该启发式比移除预测器提升 +11pp 成功率，比纯异步基线提升 +22pp，证明了延迟补偿在动态环境中的关键作用。

## 实验与结果

### 推理延迟与加速
Pi0.5 在 LIBERO 上从 135.2ms 降至 52.4ms（2.58× 加速），Pi0 实现 2.73× 加速。RTX 3090 上加速比略降至 2.47×，归因于 Ampere 架构注意力操作相对成本更高。

### 分区注意力精确性
与全批量注意力 oracle 的 MSE 恰好为 0.00，而 Naive Caching 的 MSE 高达 1.42，对应成功率从 85.4% 暴跌至 12.5%。

### 反应延迟与 stall 率
| 模型 | 指标 | LIBERO-Spatial | LIBERO-Object | LIBERO-Goal | LIBERO-Long | LIBERO Avg | Kinetix |
|---|---|---|---|---|---|---|---|
| Pi0.5 | 反应延迟 (ms) | 78.5 (-47%) | 82.3 (-46%) | 85.1 (-46%) | 84.2 (-50%) | 82.5 (-47%) | 86.8 (-50%) |
| Pi0.5 | stall 率 | 0% | 0% | 0% | 0% | 0% | 0% |
| Pi0 | 反应延迟 (ms) | 98.2 (-50%) | 101.5 (-50%) | 104.6 (-50%) | 105.2 (-54%) | 102.4 (-51%) | 112.6 (-50%) |
| Pi0 | stall 率 | 0% | 0% | 0% | 0% | 0% | 0% |

同步基线在所有任务上均为 100% stall 率。

### 真实机器人部署（AgileX PiPer，每任务 20 集）
| 任务 | Sync 成功率 | Async-Naive 成功率 | Reflex 成功率 | Reflex 延迟 |
|---|---|---|---|---|
| Pick-Place | 65±8%（由表内数值 122.8→112.4 计算） | 62±8% | 76±7% | 101ms |
| Articulated | 52±9% | 48±11%（由表内数值 112.4→100.0 计算） | 66±9% | 104ms |
| Dynamic Recovery | 38±8% | 32±8% | 55±9% | 110ms |

### 任务成功率（LIBERO）
| 模型 | Spatial | Object | Goal | Long |
|---|---|---|---|---|
| Pi0.5 | 83.2% (+0.8) | 80.4% (+0.8) | 82.0% (+0.8) | 72.4% (+3.6) |
| Pi0 | 85.4% (+0.8) | 82.6% (+0.8) | 84.2% (+0.8) | 75.0% (+4.0) |

Naive Cache 基线成功率仅 8.4–15.4%。Kinetix 上 Pi0.5 提升 +7.4%，Pi0 提升 +6.7%。

### 消融与稳定性
- 分区注意力将推理延迟从 135.2ms 降至 61.5ms；异步执行与未来条件重叠调度将反应延迟从 151.9ms 降至 82.5ms。
- 上下文窗口 K=10 为最优平衡点（2.58× 加速与近最大精度）；K=1 加速最高但精度显著下降，K=50 时加速低于 1×。
- 流稳定性：BF16 基线最大稳定步数 120–220（频繁 NaN/Inf）；BF16+FP32 norm-only 为 700–1200（罕见 NaN/Inf，+0.8ms）；BF16+AdaRMSNorm 超过 2000（无 NaN/Inf，+0.4ms）。
- 算子融合：FlashNorm 减少 2.7ms，FusedAdaLN 额外节省 1.5ms，合计减少动作专家前向传播延迟 18%。

## 边界与局限

Reflex 的等价性声明严格限定于分区注意力本身，不覆盖异步调度、未来状态预测与混合精度数值行为——这些组件仅通过经验评估验证。方法仅适用于感知编码器时间步不变的 VLA 架构，统一 DiT 风格架构（时间步条件进入视觉编码器）不在当前范围内。未来状态预测器是轻量级启发式而非学习动力学模型，其假设低级控制器准确跟踪命令动作；在 AgileX PiPer 上 100ms 前瞻内观察到 <3cm 末端执行器偏差，但更大延迟或更复杂动力学下该假设可能失效。真实机器人实验旨在验证部署可行性而非完整的 sim-to-real 研究，流稳定性分析是经验性失败分析而非形式化证明。论文未明确讨论数据隐私或安全方面的新关切。

## 工程启示

复现 Reflex 时，首先核对目标 VLA 架构是否满足时间步不变性——这是整个方法成立的前提，若感知编码器接收时间步条件则分区注意力直接失效。其次，严格遵循混合精度护栏：RMS 统计量必须在 FP32 计算，门控 MLP 保持 BF16，任何精度混用都可能导致长时间流式推理中的 NaN/Inf 崩溃。最容易踩坑的是缓存管理：静态前缀与滑动历史的预合并必须在进入去噪循环前完成，动态后缀需在预分配张量中管理并每周期重置，否则 torch.cat 开销会侵蚀大部分加速收益。上下文窗口 K 的选取需基于实际推理延迟动态调整，K=10 在 LIBERO 上最优，但不同任务与硬件可能需要重新标定。对于下游团队，建议优先在 RTX 4090 上验证 2.58× 加速与 0% stall 率，再迁移至其他硬件——RTX 3090 上加速比降至 2.47× 表明架构差异会影响收益。真实部署时，未来状态预测器的延迟补偿效果高度依赖低级控制器的跟踪精度，需在目标平台上实测末端执行器偏差。

## Overview
Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching, forcing a choice between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse. We present \textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that perception encoders are functionally independent of the denoising loop. Reflex partitions the attention context into static, sliding, and dynamic regions, enabling $O(1)$ incremental cache updates while preserving full-batch-equivalent attention outputs for fixed inputs. To ensure stability under continuous high-frequency inference, we introduce \textit{AdaRMSNorm}, an adaptive normalization layer that prevents BFloat16 numerical collapse by gating on flow phase. We further maximize throughput through an \textit{async pipeline} that decouples visual encoding from action generation, combined with \textit{operator fusion} that reduces kernel overhead. On LIBERO and Kinetix benchmarks, Reflex achieves a 2.58$\times$ inference speedup and 50Hz stable streaming, reducing reaction latency by up to 54\% and enabling efficient deployment without performance degradation.

## 参考
- https://arxiv.org/abs/2607.14695

## 개요

Reflex는 스트리밍 매칭 기반 비전-언어-행동(VLA) 모델을 위한 실시간 추론 시스템으로, 시간 단계 불변성 통찰, 분할 어텐션 캐시, 비동기 파이프라인 협력 설계를 통해 Pi0.5의 LIBERO 추론 지연 시간을 135.2ms에서 52.4ms(2.58배 가속)로 줄이고 50Hz 안정적 스트리밍 제어를 구현합니다. 핵심 기여는 스트리밍 매칭 디노이징 루프와 KV 캐시 메커니즘을 근본적 충돌에서 분리하면서도 전체 배치 어텐션과 수학적으로 정확히 동등함을 유지하는 데 있습니다.

## 무엇을 바꾸었는가

스트리밍 매칭 VLA 모델의 로봇 제어 적용困境은 본질적으로 생성형 아키텍처의 반복적 디노이징 특성과 실시간 제어 루프의 지연 시간 하드 제약 사이의 구조적 모순입니다. 이전 모든 작업은 이 둘 사이에서 이분법적 선택을 강요받았습니다: 수학적 정확성을 위해 O(N²)의 프레임별 전체 재계산을 수용하거나, 속도를 위해 수학적으로 부정확한 캐시 재사용을 채택하는 방식이었습니다. Reflex가 실제로 바꾼 것은 이 이분법적 프레임워크를 깨뜨린 것입니다—특정 아키텍처 제약 하에서 캐시 재사용이 전체 재계산과 완전히 동등할 수 있음을 증명하여, 문제를 "어떻게 근사할 것인가"에서 "어떻게 정확하면서도 효율적으로 할 것인가"로 전환했습니다.

이 전환의 심층적 의미는 VLA 실시간화의 병목 지점을 재정의했다는 점입니다. 과거 연구자들은 단일 추론의 계산량을 줄이는 데 집중했지만, Reflex는 진정한 지연 시간의 주범이 동기적 블로킹으로 인한 실행 중단과 디노이징 루프 내 시간 단계 주입으로 인한 캐시 무효화임을 지적합니다. 인식 인코더와 디노이징 루프를 시간 단계 차원에서 분리하고 이를 기반으로 분할 어텐션 메커니즘을 설계함으로써, Reflex는 시스템적 문제를 엔지니어링 가능한 캐시 관리 문제로 전환하여 50Hz 제어 주파수를 이론적 목표가 아닌 재현 가능한 엔지니어링 현실로 만들었습니다.

## 방법 분석

### 핵심 전제: 시간 단계 불변성
Reflex의 전체 방법은 인식 인코더가 디노이징 시간 단계를 수신하지 않는다는 아키텍처 사실(∂Enc/∂t_k = 0)에 기반합니다. 이는 시각적 관찰의 인코딩 결과가 전체 디노이징 루프 동안 일정하게 유지되며, 해당 KV 캐시가 반복 단계에 따라 업데이트될 필요 없이 안전하게 재사용될 수 있음을 의미합니다.

### 분할 어텐션(Partitioned Attention)
어텐션 컨텍스트를 의미적으로 세 영역으로 나누고 각각 다른 캐시 전략을 적용합니다:
- **Static Prefix**: 시스템 명령 토큰으로, 한 번 계산 후 KV 캐시에 영구 고정되며 어떤 업데이트에도 참여하지 않습니다.
- **Sliding History**: 최근 N프레임 시각적 관찰의 FIFO 큐로, 새 프레임 도착 시 가장 오래된 프레임을 제거하여 일정한 메모리 사용량을 유지합니다. LIBERO에서 N=10프레임(약 300ms 히스토리)이 최적 운영 지점입니다.
- **Dynamic Suffix**: 일시적 스트리밍 상태 x^(k)와 시간 단계 임베딩으로, 각 디노이징 주기 종료 후 리셋됩니다.

어텐션 계산은 다음과 같이 형식화됩니다:
Attn(x^(k)) = Softmax(Q^(k)[K_pin; K_slide(t); K_dyn(k)]^T/√d) × [V_pin; V_slide(t); V_dyn(k)]

이 공식은 고정 입력과 고정 관찰 창에서 전체 배치 어텐션과 비트 단위로 동일한 출력을 생성하며(MSE 정확히 0.00), 캐시 업데이트 복잡도를 O(1)로 낮춥니다.

### 엔지니어링 캐시 관리
- **Incremental Prefill**: 각 단계에서 전체 히스토리를 재처리하지 않고 최신 관찰 프레임만 인코딩합니다.
- **Manual Cache Merging**: 디노이징 루프 진입 전에 정적 접두사와 슬라이딩 히스토리를 단일 연속 메모리 버퍼로 사전 병합하여 매번 torch.cat 오버헤드를 제거합니다.
- **정적 링 버퍼**: 초기화 시 전체 텐서 B ∈ ℝ^{L×N_max×H×D}를 사전 할당하고 사용자 정의 포인터 산술 순환 인덱싱을 통해 제로 동적 할당과 O(1) 메모리 접근을 구현합니다.

### 수치 안정성: AdaRMSNorm
스트리밍 매칭 모델은 장시간 스트리밍 추론에서 높은 분산 초기화 노이즈에 연속적으로 노출되어 표준 BF16 혼합 정밀도가 빈번하게 NaN/Inf를 생성합니다. AdaRMSNorm은 RMS 통계 계산을 FP32에서 강제 수행하고 게이트 MLP를 통해 시간 단계와 고유수용성 상태의 적응형 스케일링을 도입합니다:
AdaRMSNorm(x,c) = x/RMS(x) ⊙ γ(c), 여기서 γ(c) = 1 + MLP(c), c = [t_k, s_t]

### 비동기 파이프라인 및 지연 보상
- **이중 스레드 아키텍처**: 스레드 A(시각)는 관찰을 연속적으로 인코딩하고 KV 쌍을 푸시합니다; 스레드 B(정책)는 소비자로서 최신 캐시를 쿼리하여 행동 블록을 생성합니다.
- **Future-Conditional State Prediction**: 오래된 센서 상태(ŝ_{t+Δ} ≈ a_t^cmd)를 시스템의 마지막 명령의 목표 행동으로 대체하여 경량 지연 보상 휴리스틱으로 사용합니다.
- **Adaptive Overlap Scheduling**: 실시간 추론 지연 측정을 기반으로 선견지향 K를 동적으로 조정하여 행동 블록이 끊김 없이 이어지도록 보장합니다.

### 연산자 융합
QKV 프로젝션을 단일 패킹 커널(W_QKV = [W_Q; W_K; W_V])로 융합하고 SwiGLU 블록의 Gate와 Up 프로젝션을 병합하여 레이어당 커널 시작을 50% 줄이고 단일 스트림 추론에서 15–20% 벽시계 가속을 얻습니다.

## 핵심 혁신

**1. 시간 단계 불변성을 캐시 재사용의 이론적 기반으로**: 이전 모든 KV 캐시 재사용 방식은 스트리밍 매칭 모델의 시간 단계 주입으로 인해 실패했지만, Reflex는 인식 인코더가 기능적으로 디노이징 루프와 독립적임을 처음으로 명확히 지적하고 이를 기반으로 엄격한 분할 어텐션 메커니즘을 설계했습니다. 이 통찰은 엔지니어링 가치뿐만 아니라 이론적 보장을 제공합니다—시간 단계 불변성과 FIFO 퇴출 조건을 충족할 때 출력이 전체 배치 어텐션과 완전히 동등하며(Proposition A.1), 근사가 아닙니다.

**2. 수치 안정성 문제를 시스템 설계에 통합**: 장시간 스트리밍 추론에서의 혼합 정밀도 저하는 이전에 충분히 인식되지 못한 문제였습니다. Reflex는 AdaRMSNorm을 통해 RMS 통계를 FP32에서 강제 계산하면서 게이트 MLP를 BF16으로 유지하여 지연 시간을 거의 증가시키지 않고(+0.4ms) 최대 안정 단계 수를 120–220에서 2000 이상으로 높이고 NaN/Inf 이벤트를 완전히 제거했습니다. 이는 수치적 견고성을 일등 시민으로 추론 시스템 설계에 통합한 드문 사례입니다.

**3. 비동기 실행과 지연 보상의 협력 설계**: Reflex는 계산과 실행 사이의 블로킹 간격을 제거할 뿐만 아니라 Future-Conditional State Prediction을 통해 비동기로 인한 관찰 지연을 능동적으로 보상합니다. 4지연 단계 시나리오에서 이 휴리스틱은 예측기 제거 대비 +11pp 성공률 향상, 순수 비동기 베이스라인 대비 +22pp 향상을 보여주며 동적 환경에서 지연 보상의 핵심 역할을 입증합니다.

## 실험 및 결과

### 추론 지연 및 가속
Pi0.5는 LIBERO에서 135.2ms에서 52.4ms(2.58배 가속)로 감소했고, Pi0는 2.73배 가속을 달성했습니다. RTX 3090에서는 가속비가 2.47배로 약간 감소했으며, 이는 Ampere 아키텍처에서 어텐션 연산의 상대적 비용이 더 높기 때문입니다.

### 분할 어텐션 정확성
전체 배치 어텐션 오라클과의 MSE가 정확히 0.00인 반면, Naive Caching의 MSE는 1.42로 높아 성공률이 85.4%에서 12.5%로 급락했습니다.

### 반응 지연 및 stall 비율
| 모델 | 지표 | LIBERO-Spatial | LIBERO-Object | LIBERO-Goal | LIBERO-Long | LIBERO 평균 | Kinetix |
|---|---|---|---|---|---|---|---|
| Pi0.5 | 반응 지연 (ms) | 78.5 (-47%) | 82.3 (-46%) | 85.1 (-46%) | 84.2 (-50%) | 82.5 (-47%) | 86.8 (-50%) |
| Pi0.5 | stall 비율 | 0% | 0% | 0% | 0% | 0% | 0% |
| Pi0 | 반응 지연 (ms) | 98.2 (-50%) | 101.5 (-50%) | 104.6 (-50%) | 105.2 (-54%) | 102.4 (-51%) | 112.6 (-50%) |
| Pi0 | stall 비율 | 0% | 0% | 0% | 0% | 0% | 0% |

동기 베이스라인은 모든 작업에서 100% stall 비율을 보였습니다.

### 실제 로봇 배포(AgileX PiPer, 작업당 20회)
| 작업 | Sync 성공률 | Async-Naive 성공률 | Reflex 성공률 | Reflex 지연 |
|---|---|---|---|---|
| Pick-Place | 65±8%(표 내 수치 122.8→112.4로 계산) | 62±8% | 76±7% | 101ms |
| Articulated | 52±9% | 48±11%(표 내 수치 112.4→100.0으로 계산) | 66±9% | 104ms |
| Dynamic Recovery | 38±8% | 32±8% | 55±9% | 110ms |

### 작업 성공률(LIBERO)
| 모델 | Spatial | Object | Goal | Long |
|---|---|---|---|---|
| Pi0.5 | 83.2% (+0.8) | 80.4% (+0.8) | 82.0% (+0.8) | 72.4% (+3.6) |
| Pi0 | 85.4% (+0.8) | 82.6% (+0.8) | 84.2% (+0.8) | 75.0% (+4.0) |

Naive Cache 베이스라인 성공률은 8.4–15.4%에 불과했습니다. Kinetix에서 Pi0.5는 +7.4%, Pi0는 +6.7% 향상되었습니다.

### 소거 및 안정성
- 분할 어텐션은 추론 지연을 135.2ms에서 61.5ms로 줄였습니다; 비동기 실행과 미래 조건부 중첩 스케줄링은 반응 지연을 151.9ms에서 82.5ms로 줄였습니다.
- 컨텍스트 창 K=10이 최적 균형점(2.58배 가속과 거의 최대 정밀도)입니다; K=1은 가속이 가장 높지만 정밀도가 크게 떨어지고, K=50에서는 가속이 1배 미만입니다.
- 스트리밍 안정성: BF16 베이스라인 최대 안정 단계 수 120–220(빈번한 NaN/Inf); BF16+FP32 norm-only는 700–1200(드문 NaN/Inf, +0.8ms); BF16+AdaRMSNorm은 2000 초과(NaN/Inf 없음, +0.4ms).
- 연산자 융합: FlashNorm은 2.7ms 감소, FusedAdaLN은 추가로 1.5ms 절약, 합계 행동 전문가 순방향 전파 지연 18% 감소.

## 경계 및 한계

Reflex의 동등성 주장은 분할 어텐션 자체에 엄격히 국한되며, 비동기 스케줄링, 미래 상태 예측, 혼합 정밀도 수치 동작은 포함하지 않습니다—이러한 구성 요소는 경험적 평가로만 검증되었습니다. 이 방법은 인식 인코더가 시간 단계 불변인 VLA 아키텍처에만 적용 가능하며, 통합 DiT 스타일 아키텍처(시간 단계 조건이 시각 인코더에 들어가는 경우)는 현재 범위에 포함되지 않습니다. 미래 상태 예측기는 학습된 동역학 모델이 아닌 경량 휴리스틱이며, 저수준 제어기가 명령 행동을 정확히 추적한다고 가정합니다; AgileX PiPer에서 100ms 선견지향 내에서 <3cm 엔드 이펙터 편차가 관찰되었지만, 더 큰 지연이나 더 복잡한 동역학에서는 이 가정이 실패할 수 있습니다. 실제 로봇 실험은 배포 가능성 검증을 목적으로 하며 완전한 sim-to-real 연구가 아닙니다. 스트리밍 안정성 분석은 형식적 증명이 아닌 경험적 실패 분석입니다. 논문은 데이터 프라이버시나 안전 측면의 새로운 우려를 명시적으로 논의하지 않았습니다.

## 엔지니어링 시사점

Reflex를 재현할 때 먼저 대상 VLA 아키텍처가 시간 단계 불변성을 충족하는지 확인하십시오—이것이 전체 방법이 성립하는 전제이며, 인식 인코더가 시간 단계 조건을 수신하면 분할 어텐션이 직접 실패합니다. 둘째, 혼합 정밀도 가드레일을 엄격히 준수하십시오: RMS 통계는 FP32에서 계산해야 하고 게이트 MLP는 BF16을 유지해야 하며, 정밀도 혼용은 장시간 스트리밍 추론에서 NaN/Inf 붕괴를 초래할 수 있습니다. 가장 함정에 빠지기 쉬운 부분은 캐시 관리입니다: 정적 접두사와 슬라이딩 히스토리의 사전 병합은 디노이징 루프 진입 전에 완료되어야 하며, 동적 접미사는 사전 할당 텐서에서 관리되고 매 주기 리셋되어야 합니다. 그렇지 않으면 torch.cat 오버헤드가 대부분의 가속 이점을 잠식합니다. 컨텍스트 창 K의 선택은 실제 추론 지연을 기반으로 동적으로 조정해야 하며, K=10이 LIBERO에서 최적이지만 다른 작업과 하드웨어에서는 재보정이 필요할 수 있습니다. 하류 팀에게는 RTX 4090에서 2.58배 가속과 0% stall 비율을 먼저 검증한 후 다른 하드웨어로 이전할 것을 권장합니다—RTX 3090에서 가속비가 2.47배로 감소한 것은 아키텍처 차이가 이점에 영향을 미친다는 것을 보여줍니다. 실제 배포 시 미래 상태 예측기의 지연 보상 효과는 저수준 제어기의 추적 정밀도에 크게 의존하므로, 대상 플랫폼에서 엔드 이펙터 편차를 실측해야 합니다.
