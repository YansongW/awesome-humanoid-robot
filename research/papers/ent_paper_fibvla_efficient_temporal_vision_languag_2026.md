---
$id: ent_paper_fibvla_efficient_temporal_vision_languag_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FibVLA: An Efficient Temporal Vision-Language-Action Model with Fibonacci Sampling'
  zh: 'FibVLA: An Efficient Temporal Vision-Language-Action Model with Fibonacci Sampling'
  ko: 'FibVLA: An Efficient Temporal Vision-Language-Action Model with Fibonacci Sampling'
summary:
  en: Vision-language-action models (VLAs), which leverage the cognition of multimodal information to infer physical-world
    actions, provide a generalized solution for embodied AI applications. Conventional VLAs usually concentrate on current
    digital cognition. While some efforts are made to enhance VLAs' reasoning capabilities by capturing temporal information,
    encoding the long-context history causes.
  zh: FibVLA 是一个面向长时程具身操作任务的时序视觉-语言-动作模型，由研究团队提出，核心贡献在于用斐波那契采样策略替代固定频率或密集历史帧输入，在不增加 token 开销的前提下提升模型对任务上下文与细粒度运动的联合建模能力。该模型在
    LIBERO、MIKASA-Robo、SimplerEnv 及真实机械臂平台上均取得领先成功率，同时推理延迟显著低于同类时序 VLA 基线。
  ko: Vision-language-action models (VLAs), which leverage the cognition of multimodal information to infer physical-world
    actions, provide a generalized solution for embodied AI applications. Conventional VLAs usually concentrate on current
    digital cognition. While some efforts are made to enhance VLAs' reasoning capabilities by capturing temporal information,
    encoding the long-context history causes.
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
- fibvla
- efficient
- temporal
- vision
- languag
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
  title: 'arXiv:2607.29596 FibVLA: An Efficient Temporal Vision-Language-Action Model with Fibonacci Sampli'
  url: https://arxiv.org/abs/2607.29596
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

FibVLA 是一个面向长时程具身操作任务的时序视觉-语言-动作模型，由研究团队提出，核心贡献在于用斐波那契采样策略替代固定频率或密集历史帧输入，在不增加 token 开销的前提下提升模型对任务上下文与细粒度运动的联合建模能力。该模型在 LIBERO、MIKASA-Robo、SimplerEnv 及真实机械臂平台上均取得领先成功率，同时推理延迟显著低于同类时序 VLA 基线。

## 它改变了什么

现有 VLA 模型在处理长时程任务时普遍存在“时间短视”问题——它们要么只依赖最近几帧观测，要么试图把全部历史帧塞进视觉编码器，前者丢失了子任务进展等低频上下文，后者则引发 token 爆炸，直接拖垮实时控制。此前的时间建模方案，如预测未来子目标或稀疏表示学习，要么引入额外训练复杂度，要么依赖离线预处理，难以在部署时灵活适配不同控制频率。

FibVLA 真正改变的是“历史信息如何被采样、编码和复用”这一底层逻辑。它不再把历史帧当作静态输入拼接，而是通过斐波那契递推的采样间隔，让历史特征 token 在推理时可以被显式复用，从而把“看更多历史”的成本从线性增长降为对数增长。这等于在时间维度上做了一次类似“注意力稀疏化”的改造，但用的是更简单的整数序列约束，而非学习式掩码。

## 方法拆解

### 对数后见采样（Logarithmic Hindsight Sampling）
- 采样点定义为 k_i = ⌊q_min · r^i⌋，其中 q_min 为最小采样间隔，r > 1 为增长率。
- 施加递归稀疏约束 k_i ≥ k_{i-1} + k_{i-2}（∀i > 2），消除离散化导致的索引碰撞，保证序列严格单调并消除冗余。
- 增长率可根据控制频率灵活调整，平衡长期覆盖与关键状态转换捕捉精度。

### 通道时序编码（Channel-wise Temporal Encoding, CTE）
- 通过帧差分 D(·,i) = |I(·,t−k_i) − I(·,t−k_{i+1})| 计算运动差异。
- 用预定义阈值 ξ 生成二值运动掩码 Ψ(·,i)。
- 递归生成时序编码帧 H(·,i)：运动处设为 τ（最大强度持续时间），非运动处衰减 H(·,i+1) − δ（δ为衰减参数），形成“视觉轨迹”。
- 将视觉历史分为 Near、Mid、Far 三个时间范围，分别映射到 PaliGemma 视觉编码器（SigLip）的 R、G、B 通道，形成后见特征；当前 RGB 帧作为语义锚点与后见特征合并输入。

### 斐波那契递归推理（Fibonacci Recurrent Inference）
- 当 k_i = k_{i-1} + k_{i-2} 时，采样策略与斐波那契序列的加法递归性质完美对齐，允许历史特征 token 在下一动作块推理时被复用。
- 设置动作块长度 L = k_{i-2}，使历史帧与下一时刻采样点精确对齐（等式 (t+k_{i-2})−k_i = t−k_{i-1}）。
- 证明该策略是在稀疏采样约束下最大化历史信息复用的唯一解析解（证明见附录H）。
- 采样深度增加时，相邻采样间隔之比收敛于黄金比例，自然维持对数采样分布。

### 动作专家
- 采用流匹配生成动作分布而非判别式动作序列。

## 关键创新

1. **斐波那契约束下的 token 复用**：这是最核心的机制创新。通过将采样间隔设计为满足二阶递推的整数序列，并让动作块长度绑定到斐波那契项，历史帧的视觉特征 token 可以在下一动作块推理时被直接复用，无需重新编码。这相当于在时间维度上实现了“缓存”，且论文证明这是稀疏约束下的唯一最优解。

2. **通道级时间编码（CTE）**：把三个不同时间范围的历史帧差分结果编码进 RGB 三个通道，而非拼接多个帧。这不仅避免了 token 数量膨胀，还让视觉编码器天然地感知到“运动轨迹”的时空分布——高频帧对应细粒度运动，低频帧对应任务上下文，二者在特征空间中形成不同聚类，CTE 恰好利用了这一非均匀性。

3. **无需重训练视觉编码器**：FibVLA 声称无需对大规模视觉编码器进行重训练即可提升性能，这意味着它可以作为即插即用的时间建模模块，叠加在现有 PaliGemma 等骨干之上，降低了迁移成本。

## 实验与结果

实验覆盖三个仿真基准（LIBERO、MIKASA-Robo、SimplerEnv）和真实机械臂平台，基线包括 OpenVLA、π₀、CogACT、TraceVLA、HiF-VLA 等 12 种方法。关键结果如下：

| 基准 | FibVLA | 第二好基线 | 提升幅度 |
|------|--------|-----------|---------|
| LIBERO Avg SR | 96.8% | π₀ 94.2% | 2.6 个百分点 |
| LIBERO-Long | 95.2% | CogACT 88.8% | 7.21%（由表内数值 95.2→88.8 计算） |
| SimplerEnv-Fractal Overall | 72.1% | CogACT 68.1% | 5.87%（由表内数值 72.1→68.1 计算） |
| SimplerEnv-Bridge Avg | 67.3% | CogACT 51.3% | 3.12%（由表内数值 67.3→51.3 计算） |
| MIKASA-Robo Avg | 46.5% | π₀ 33.0% | 40.9%（由表内数值 46.5→33.0 计算） |
| 真实世界平均得分 | 85.7 | π₀ 74.3（由表内数值 85.7−11.4 计算） | 11.4 分 |

消融实验显示，去掉采样策略（w/o Sampling）在 LIBERO-Long 上从 95.2% 降至 88.4%，去掉 CTE（w/o CTE）降至 91.2%，说明两者均贡献显著。效率方面，在统一 10 帧历史窗口下，FibVLA 推理时间 177 ms，低于 TraceVLA 的 196 ms（降低 9.69%，由表内数值 177→196 计算）和 HiF-VLA 的 243 ms（降低 27.16%，由表内数值 177→243 计算），同时成功率最高。

## 边界与局限

论文未在正文中明确列出局限性章节。从事实要点推断，真实世界实验环境被刻意简化（白色背景板、黑色桌布、常见家用物品），未在更复杂、非受控的真实场景中验证；真实世界评估仅选取 7 个代表性任务，未覆盖全部 15 个任务。此外，斐波那契递归推理的最优性证明依赖严格不等式约束，若实际部署中采样间隔因离散化偏离严格递推，token 复用效率可能下降。论文未明确提供 GPU 型号、训练轮数等硬件配置细节。

## 工程启示

复现或采用 FibVLA 时，首先核对采样序列是否严格满足 k_i ≥ k_{i-1} + k_{i-2} 约束——这是 token 复用机制成立的前提，任何离散化碰撞都会破坏递归对齐。其次，动作块长度 L 必须动态绑定到 k_{i-2}，而非固定值，否则历史帧与下一时刻采样点无法精确对齐。最容易踩坑的地方在于 CTE 的阈值 ξ 和衰减参数 δ：LIBERO 环境（10 Hz）与真实世界（30 Hz）的帧间位移差异很大，前者产生拉长轨迹，后者更紧凑，直接套用同一组参数会导致运动掩码失真。建议按控制频率分别标定这两个参数。效率对比时注意统一历史窗口大小（论文用 10 帧），否则推理时间差异不具可比性。最后，FibVLA 声称无需重训练视觉编码器，但骨干网络仍为 PaliGemma 3B，下游团队若更换视觉编码器，需重新验证 CTE 的通道映射是否仍然有效。

## Overview
Vision-language-action models (VLAs), which leverage the cognition of multimodal information to infer physical-world actions, provide a generalized solution for embodied AI applications. Conventional VLAs usually concentrate on current digital cognition. While some efforts are made to enhance VLAs' reasoning capabilities by capturing temporal information, encoding the long-context history causes an efficiency-decreasing issue. To reconcile the conflict between capturing temporal information and maintaining inference efficiency in VLAs, this paper introduces FibVLA, an efficient framework featuring temporal perception of long-context history. Specifically, we leverage logarithmic hindsight sampling to both proprioceptive states and visual frames to capture long-term temporal dependencies with minimal redundancy. For the action expert, we introduce the flow matching to produce action distributions, and the Fibonacci recurrent inference strategy to generate long-range planning steps based on real-time closed-loop feedback. Experiments demonstrate that FibVLA significantly improves action smoothness and success rates without retraining large-scale visual encoders. Efficiency analysis demonstrates superior real-time responsiveness compared to video-based baselines in real-world evaluations.

## 参考
- https://arxiv.org/abs/2607.29596

## 개요

FibVLA는 장기 호라이즌 조작 작업을 위한 시간적 비전-언어-행동 모델로, 연구팀이 제안했으며, 핵심 기여는 고정 주파수 또는 밀집된 과거 프레임 입력 대신 피보나치 샘플링 전략을 사용하여 토큰 오버헤드를 늘리지 않으면서 작업 컨텍스트와 세밀한 움직임의 공동 모델링 능력을 향상시키는 데 있습니다. 이 모델은 LIBERO, MIKASA-Robo, SimplerEnv 및 실제 로봇 팔 플랫폼에서 선도적인 성공률을 달성했으며, 추론 지연 시간은 유사한 시간적 VLA 기준선보다 현저히 낮습니다.

## 무엇을 바꾸었는가

기존 VLA 모델은 장기 호라이즌 작업을 처리할 때 일반적으로 "시간적 근시안" 문제를 가지고 있습니다. 즉, 최근 몇 프레임의 관측에만 의존하거나 모든 과거 프레임을 비전 인코더에 집어넣으려고 합니다. 전자는 하위 작업 진행 상황과 같은 저주파 컨텍스트를 잃고, 후자는 토큰 폭발을 유발하여 실시간 제어를 직접 무너뜨립니다. 이전의 시간 모델링 접근 방식(예: 미래 하위 목표 예측 또는 희소 표현 학습)은 추가 훈련 복잡성을 도입하거나 오프라인 전처리에 의존하여 배포 시 다양한 제어 주파수에 유연하게 적응하기 어렵습니다.

FibVLA가 실제로 바꾼 것은 "과거 정보가 어떻게 샘플링, 인코딩 및 재사용되는가"라는 기본 논리입니다. 더 이상 과거 프레임을 정적 입력으로 연결하지 않고, 피보나치 점화식 기반의 샘플링 간격을 통해 추론 시 과거 특징 토큰을 명시적으로 재사용할 수 있게 하여 "더 많은 과거를 보는" 비용을 선형 증가에서 로그 증가로 줄입니다. 이는 시간 차원에서 "어텐션 희소화"와 유사한 개조를 수행한 것이지만, 학습된 마스크 대신 더 간단한 정수 시퀀스 제약을 사용합니다.

## 방법 분해

### 로그 후견 샘플링 (Logarithmic Hindsight Sampling)
- 샘플링 포인트는 k_i = ⌊q_min · r^i⌋로 정의되며, 여기서 q_min은 최소 샘플링 간격, r > 1은 성장률입니다.
- 재귀적 희소 제약 k_i ≥ k_{i-1} + k_{i-2} (∀i > 2)를 적용하여 이산화로 인한 인덱스 충돌을 제거하고, 시퀀스가 엄격히 단조롭고 중복이 없도록 보장합니다.
- 성장률은 제어 주파수에 따라 유연하게 조정되어 장기 커버리지와 핵심 상태 전환 캡처 정밀도의 균형을 맞출 수 있습니다.

### 채널별 시간 인코딩 (Channel-wise Temporal Encoding, CTE)
- 프레임 차분 D(·,i) = |I(·,t−k_i) − I(·,t−k_{i+1})|을 통해 움직임 차이를 계산합니다.
- 사전 정의된 임계값 ξ를 사용하여 이진 움직임 마스크 Ψ(·,i)를 생성합니다.
- 재귀적으로 시간 인코딩 프레임 H(·,i)를 생성합니다: 움직임 위치에서는 τ(최대 강도 지속 시간)로 설정하고, 비움직임 위치에서는 H(·,i+1) − δ(감쇠 매개변수)로 감쇠하여 "시각적 궤적"을 형성합니다.
- 시각적 과거를 Near, Mid, Far 세 가지 시간 범위로 나누어 각각 PaliGemma 비전 인코더(SigLip)의 R, G, B 채널에 매핑하여 후견 특징을 형성합니다. 현재 RGB 프레임은 의미론적 앵커로 후견 특징과 병합되어 입력됩니다.

### 피보나치 재귀 추론 (Fibonacci Recurrent Inference)
- k_i = k_{i-1} + k_{i-2}일 때, 샘플링 전략은 피보나치 수열의 덧셈 재귀 속성과 완벽하게 정렬되어 다음 동작 블록 추론 시 과거 특징 토큰을 재사용할 수 있습니다.
- 동작 블록 길이 L = k_{i-2}로 설정하여 과거 프레임과 다음 시점의 샘플링 포인트가 정확히 정렬되도록 합니다(등식 (t+k_{i-2})−k_i = t−k_{i-1}).
- 이 전략이 희소 샘플링 제약 하에서 과거 정보 재사용을 최대화하는 유일한 해석적 해임을 증명합니다(증명은 부록 H 참조).
- 샘플링 깊이가 증가함에 따라 인접 샘플링 간격의 비율은 황금비로 수렴하여 자연스럽게 로그 샘플링 분포를 유지합니다.

### 동작 전문가
- 판별적 동작 시퀀스 대신 흐름 매칭을 사용하여 동작 분포를 생성합니다.

## 핵심 혁신

1. **피보나치 제약 하의 토큰 재사용**: 이것이 가장 핵심적인 메커니즘 혁신입니다. 샘플링 간격을 2차 점화식을 만족하는 정수 시퀀스로 설계하고 동작 블록 길이를 피보나치 항에 바인딩함으로써, 과거 프레임의 시각적 특징 토큰은 다음 동작 블록 추론 시 재인코딩 없이 직접 재사용될 수 있습니다. 이는 시간 차원에서 "캐시"를 구현한 것과 같으며, 논문은 이것이 희소 제약 하에서 유일한 최적 해임을 증명합니다.

2. **채널 수준 시간 인코딩 (CTE)**: 여러 프레임을 연결하는 대신 세 가지 다른 시간 범위의 과거 프레임 차분 결과를 RGB 세 채널에 인코딩합니다. 이는 토큰 수 팽창을 방지할 뿐만 아니라 비전 인코더가 "움직임 궤적"의 시공간 분포를 자연스럽게 인식하게 합니다. 고주파 프레임은 세밀한 움직임에 해당하고 저주파 프레임은 작업 컨텍스트에 해당하며, 둘은 특징 공간에서 서로 다른 클러스터를 형성하고 CTE는 바로 이 비균일성을 활용합니다.

3. **비전 인코더 재훈련 불필요**: FibVLA는 대규모 비전 인코더를 재훈련하지 않고도 성능을 향상시킬 수 있다고 주장합니다. 이는 기존 PaliGemma와 같은 백본 위에 플러그 앤 플레이 방식의 시간 모델링 모듈로 추가될 수 있어 전이 비용을 낮춥니다.

## 실험 및 결과

실험은 세 가지 시뮬레이션 벤치마크(LIBERO, MIKASA-Robo, SimplerEnv)와 실제 로봇 팔 플랫폼을 포함하며, 기준선에는 OpenVLA, π₀, CogACT, TraceVLA, HiF-VLA 등 12가지 방법이 포함됩니다. 주요 결과는 다음과 같습니다:

| 벤치마크 | FibVLA | 두 번째로 좋은 기준선 | 향상 폭 |
|------|--------|-----------|---------|
| LIBERO Avg SR | 96.8% | π₀ 94.2% | 2.6 퍼센트 포인트 |
| LIBERO-Long | 95.2% | CogACT 88.8% | 7.21% (표 내 값 95.2→88.8로 계산) |
| SimplerEnv-Fractal Overall | 72.1% | CogACT 68.1% | 5.87% (표 내 값 72.1→68.1로 계산) |
| SimplerEnv-Bridge Avg | 67.3% | CogACT 51.3% | 3.12% (표 내 값 67.3→51.3으로 계산) |
| MIKASA-Robo Avg | 46.5% | π₀ 33.0% | 40.9% (표 내 값 46.5→33.0으로 계산) |
| 실제 세계 평균 점수 | 85.7 | π₀ 74.3 (표 내 값 85.7−11.4로 계산) | 11.4점 |

절제 실험에 따르면 샘플링 전략 제거(w/o Sampling)는 LIBERO-Long에서 95.2%에서 88.4%로 감소하고, CTE 제거(w/o CTE)는 91.2%로 감소하여 둘 다 상당한 기여를 했음을 보여줍니다. 효율성 측면에서 통일된 10프레임 과거 창에서 FibVLA 추론 시간은 177ms로 TraceVLA의 196ms(9.69% 감소, 표 내 값 177→196으로 계산) 및 HiF-VLA의 243ms(27.16% 감소, 표 내 값 177→243으로 계산)보다 낮았으며, 동시에 성공률이 가장 높았습니다.

## 경계 및 한계

논문은 본문에 한계 섹션을 명시적으로 나열하지 않았습니다. 사실적 요점에서 추론하면 실제 세계 실험 환경은 의도적으로 단순화되었으며(흰색 배경판, 검은색 테이블보, 일반적인 가정용품), 더 복잡하고 통제되지 않은 실제 시나리오에서는 검증되지 않았습니다. 실제 세계 평가는 7개의 대표 작업만 선택했으며 전체 15개 작업을 다루지 않았습니다. 또한 피보나치 재귀 추론의 최적성 증명은 엄격한 부등식 제약에 의존하므로, 실제 배포에서 샘플링 간격이 이산화로 인해 엄격한 점화식에서 벗어나면 토큰 재사용 효율이 저하될 수 있습니다. 논문은 GPU 모델, 훈련 에폭 수 등의 하드웨어 구성 세부 사항을 명시적으로 제공하지 않았습니다.

## 엔지니어링 시사점

FibVLA를 재현하거나 채택할 때 먼저 샘플링 시퀀스가 k_i ≥ k_{i-1} + k_{i-2} 제약을 엄격히 충족하는지 확인하십시오. 이는 토큰 재사용 메커니즘이 성립하는 전제 조건이며, 이산화 충돌은 재귀 정렬을 깨뜨릴 수 있습니다. 둘째, 동작 블록 길이 L은 고정 값이 아닌 k_{i-2}에 동적으로 바인딩되어야 합니다. 그렇지 않으면 과거 프레임과 다음 시점의 샘플링 포인트가 정확히 정렬되지 않습니다. 가장 함정에 빠지기 쉬운 부분은 CTE의 임계값 ξ와 감쇠 매개변수 δ입니다. LIBERO 환경(10Hz)과 실제 세계(30Hz)의 프레임 간 변위 차이가 크며, 전자는 늘어난 궤적을 생성하고 후자는 더 컴팩트하므로 동일한 매개변수 세트를 직접 적용하면 움직임 마스크가 왜곡됩니다. 제어 주파수에 따라 두 매개변수를 각각 보정하는 것이 좋습니다. 효율성 비교 시 과거 창 크기를 통일해야 합니다(논문은 10프레임 사용). 그렇지 않으면 추론 시간 차이가 비교 가능하지 않습니다. 마지막으로 FibVLA는 비전 인코더 재훈련이 필요 없다고 주장하지만 백본은 여전히 PaliGemma 3B이므로, 하류 팀이 비전 인코더를 교체하는 경우 CTE의 채널 매핑이 여전히 유효한지 재검증해야 합니다.
