---
$id: ent_paper_chainvla_chaining_vision_language_action_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ChainVLA: Chaining Vision-Language-Action Queries through a Unified Execution State for Long-Horizon Manipulation'
  zh: 'ChainVLA: Chaining Vision-Language-Action Queries through a Unified Execution State for Long-Horizon Manipulation'
  ko: 'ChainVLA: Chaining Vision-Language-Action Queries through a Unified Execution State for Long-Horizon Manipulation'
summary:
  en: Humans perform long-horizon manipulation by retaining knowledge of what earlier actions have established while continuously
    adapting the motion underway. By contrast, action-chunked vision-language-action (VLA) policies repeatedly replan from
    the current input at each query. Existing methods preserve either long-term task evidence through memory or short-term
    motion through action reuse and.
  zh: ChainVLA 是一个 1.2B 参数的视觉-语言-动作（VLA）策略，通过联合且可修订的执行状态 s_k = (g_k, u_k) 链式连接连续查询，解决长时程操作中跨查询的任务进度与运动延续问题。其核心贡献在于将循环工作状态（Progress
    Context）与运动尾部（Motion Tail）统一在一个查询转移框架中，在 RMBench 上达到 62.8% 平均成功率（远超基线），在 LIBERO 上达到 98.8% 平均成功率（超越所有对比方法）。
  ko: Humans perform long-horizon manipulation by retaining knowledge of what earlier actions have established while continuously
    adapting the motion underway. By contrast, action-chunked vision-language-action (VLA) policies repeatedly replan from
    the current input at each query. Existing methods preserve either long-term task evidence through memory or short-term
    motion through action reuse and.
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
- chainvla
- chaining
- vision
- language
- action
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
  title: 'arXiv:2608.02326 ChainVLA: Chaining Vision-Language-Action Queries through a Unified Execution St'
  url: https://arxiv.org/abs/2608.02326
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---

## 概述

ChainVLA 是一个 1.2B 参数的视觉-语言-动作（VLA）策略，通过联合且可修订的执行状态 s_k = (g_k, u_k) 链式连接连续查询，解决长时程操作中跨查询的任务进度与运动延续问题。其核心贡献在于将循环工作状态（Progress Context）与运动尾部（Motion Tail）统一在一个查询转移框架中，在 RMBench 上达到 62.8% 平均成功率（远超基线），在 LIBERO 上达到 98.8% 平均成功率（超越所有对比方法）。

## 它改变了什么

现有 action-chunked VLA 策略在每次查询时都从当前输入重新规划，存在两类信息缺失：任务级上，早期任务证据可能已不在当前视野中（如 Put Back Block 任务中相同观测和指令可能对应不同历史，需要不同决策）；运动级上，重新规划丢弃了前一次预测的未执行延续，导致新预测前缀与它所替代的运动不一致。memory-augmented 策略保留长期任务证据但不保留未执行动作延续，基于 Temporal Ensemble 的方法保留短期运动但无法保留更早任务证据——两条路线互补但割裂。

ChainVLA 真正改变的是将这两类信息统一到一个可修订的执行状态中，并强调运动连续性有助于保留任务进度推断所需的观测流，因此两个组件是顺序作用而非独立作用。它不再把跨查询交接视为后处理技巧，而是作为训练与部署共享的一等公民——训练时按 episode 顺序展开同一执行状态转移，携带的后缀在条件化下一查询前被 detach，确保模型学会主动利用而非被动拼接跨查询信息。

## 方法拆解

### 执行状态定义
- 状态 s_k = (g_k, u_k)，其中 g_k = Fuse(L_k, Z_k^e) 为 Progress Context（循环工作状态实时 token 与检索事件证据的融合），u_k 为 Motion Tail（前一次预测的未执行后缀）
- 查询转移公式：s_{k+1} = F_θ(s_k, x_k)，x_k = (o_k, r_k, ℓ) 为观测、本体感受和语言指令
- 严格前缀递减时域：1 ≤ h_exec < H，预测 H 步执行前 h_exec 步后再次查询（H=30, h_exec=24）

### 循环工作状态（Recurrent Working State）
- W_k = (L_k, B_k)，L_k 为实时 token，B_k 为早期实时 token 的有界 FIFO 缓存（8 当前 + 24 先前，三槽）
- 更新公式：
  - η_k = MLP[φ_r(r_k), Pool(P_k), Pool(U_k), τ_k]
  - L̃_k = CrossAttn(Q_W + η_k, X_k)
  - L_k = LN(L̃_k + m_{k-1}^{live} · CrossAttn(L̃_k, L_{k-1}))
  - W̄_k = Pool([L_k, B_{k-1}, P_k, U_k])
- 八个学习查询关注当前多模态令牌并循环更新实时令牌，实时令牌直接进入进度上下文

### 稀疏事件记忆（Sparse Event Memory）
- C_k = {(κ_i, E_i, b_i)}，事件体 E_i = [V_i, S_i, T_i]（64 视觉 + 8 阶段 + 8 时间令牌），容量 16，最旧非锚点被逐出
- 写入规则：第一个有效查询保留为锚点；有阶段标注按任务阶段转换触发，无标注用固定三查询间隔
- 检索评分：ρ_{k,i} = cos(LN(q_k^e), LN(κ_i + Emb_age(clip(k − b_i))))，读取锚点和两个最高分非锚点记录

### Motion Tail 两条模型侧路径
1. 动作空间归一化后经学习投影编码为 tail tokens U_{k+1} 供工作状态使用
2. 对齐的轨迹初始化动作生成：Ã_{k+1}^{(0)} | u_{k+1} ~ N(μ_{k+1}, σ_u²I)，μ_{k+1} = I(u_{k+1})

### 解码与训练
- 解码器为 conditional-flow DiT backbone，从最新观测、Progress Context 和 tail tokens 重新生成每个水平位置，不复制或冻结任何位置——携带状态是可修订先验而非固定计划
- 解码后控制器线性混合重叠步骤（执行侧交接），与两条模型侧路径分离
- 训练目标：标准 conditional-flow 动作目标 + 阶段监督（有标注时）+ 重叠一致性正则化（权重 0.2，前一次预测被 detach）
- 训练时按 episode 顺序展开，携带后缀 detach 后才条件化下一查询；episode 开始时 tail 路径被掩码

## 关键创新

1. **统一执行状态的双通道设计**：将长期任务证据（Progress Context）与短期运动延续（Motion Tail）统一在一个查询转移公式中，而非像现有方法那样割裂处理。关键创新在于两个组件顺序作用——运动连续性帮助保留任务进度推断所需的观测流，这解释了为何 w/o Motion Tail 时成功率暴跌至 11.2%（Full 为 62.8%）。

2. **可修订先验而非固定计划**：解码器从最新观测和进度上下文重新生成每个水平位置，携带的尾部只是初始化先验（加性噪声扰动），而非复制或冻结。这与 Temporal Ensemble 的硬性平均不同，允许新预测在保持运动连续性的同时响应最新观测变化。

3. **训练与部署共享同一状态转移**：训练时按 episode 顺序展开执行状态转移，携带后缀 detach 后条件化下一查询，且以 0.5 概率使用前驱的分离预测尾部。这使得模型在训练时就学会主动利用跨查询信息，而非仅在部署时做后处理拼接——消融显示 FIFO History + Temporal Ensemble 替代方案仅达 35.6%，低于 Full 27.2 个百分点。

## 实验与结果

### RMBench 主结果（成功率 %，100 episodes/任务）
| 方法 | Obs. | Rearr. | Put B. | Swap B. | Swap T. | Avg. |
|------|------|--------|--------|---------|---------|------|
| DP | 1 | 0 | 0 | 11 | 20 | 6.4 |
| ACT | 1 | 29 | 0 | 2 | 2 | 6.8 |
| π_0.5 (2.6B+0.3B) | 9 | 13 | 11 | 24 | 15 | 14.4 |
| MemoryVLA (7B+0.3B) | 0 | 22 | 50 | 17 | 9 | 19.6 |
| Mem-0 (8B+2B) | 4 | 89 | 90 | 67 | 14 | 52.8 |
| **ChainVLA (1.2B)** | **11** | **93** | **96** | **74** | **40** | **62.8** |

### LIBERO 主结果（成功率 %，50 episodes/任务）
| 方法 | Spatial | Object | Goal | Long | Avg. |
|------|---------|--------|------|------|------|
| OpenVLA (7B) | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |
| GR00T-N1 (2.2B) | 94.4 | 97.6 | 93.0 | 90.6 | 93.9 |
| π_0 (3.3B) | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| MemoryVLA (7B+0.3B) | 98.4 | 98.4 | 96.4 | 93.4 | 96.7 |
| CronusVLA (7B) | 97.3 | 99.6 | 96.9 | 94.0 | 97.0 |
| X-VLA (0.9B) | 98.2 | 98.6 | 97.8 | 97.6 | 98.1 |
| **ChainVLA (1.2B)** | **98.4** | **99.4** | **99.2** | **98.2** | **98.8** |

### 关键消融（RMBench 成功率 %）
| 条件 | Avg. |
|------|------|
| w/o Progress Ctx. | 3.0 |
| w/o Motion Tail | 11.2 |
| w/o Both | 1.6 |
| FIFO Hist. + TE | 35.6 |
| **ChainVLA (Full)** | **62.8** |

### 边界诊断（80 对匹配场景，Full vs w/o Motion Tail 池化降低）
| 指标 | 降低幅度 |
|------|----------|
| CD_p（位置命令不连续性） | 56.6% |
| CD_R（方向命令不连续性） | 40.4% |
| B2（边界二阶差分） | 57.4% |
| RMSE_3（三步重叠 RMSE） | 43.1% |

后解码平滑控制对比显示：Put Back Block 上 w/o Motion Tail 成功率 0（CD_p 5.90），Linear Cont. 成功率 0（CD_p 2.09），Temporal Ens. 成功率 0（CD_p 3.57），Full 成功率 96（CD_p 2.69）——说明仅靠后处理平滑无法恢复链式状态的能力。

## 边界与局限

- 所有结果来自固定速率仿真（RMBench 和 LIBERO），边界诊断描述命令流而非物理轨迹；未在硬件上评估，未改变控制速率，报告余量不应视为异步或实时部署的预测
- 每个内部训练条件使用单一随机种子（42），未报告种子变异性或显著性检验，成功率和边界均值应视为点估计
- 每个消融同时从训练和部署中撤回路径，衡量组装系统对该路径的依赖而非隔离内部机制；边界测量建立关联关系而非组件级因果关系
- 未使用单独的规划器或世界模型来分解子目标或想象潜在状态；未将 Motion Tail 用作符号计划或潜在目标；未在 LIBERO 上做消融分析（因接近上限）
- 所有四个诊断仅局部于接缝，不评分整剧集轨迹质量、累积状态偏差或固定频率物理平滑度；外部基线比较行未在本文协议下重新运行，可能在骨干、演示数、优化预算和成功标准上不同
- 固定设计选择（视界 30、前缀 24、记忆容量 16、写入置信度 0.55、重叠权重 0.2）均固定一次未搜索，无法报告其敏感性

## 工程启示

复现时先核对四个关键超参：视界 H=30 与执行前缀 h_exec=24 的比例（留 6 步尾部）、事件记忆容量 16、重叠一致性权重 0.2、无阶段标注时的三查询写入间隔。最容易踩坑的是训练与部署的状态转移一致性——训练时必须以 episode 顺序展开查询，携带后缀 detach 后才条件化下一查询，且 episode 开始时 tail 路径必须被掩码，否则会出现训练-部署分布偏移。

第二个坑是阶段标注的处理：有标注时 ground-truth 转换监督阶段估计和训练时写入目标，但标签从不进入动作解码器；无标注时用固定三查询间隔。如果下游任务没有阶段标签，建议先验证三查询间隔是否合理，因为写入频率直接影响事件记忆的检索质量。

第三个坑是消融实验的解读：每个消融同时撤回路径输入、训练项和部署处理，因此 w/o Motion Tail 的 11.2% 不是单一机制的孤立效果，而是整个尾部路径（含训练正则化）的系统依赖。如果只想复现核心能力，优先保证 Progress Context（w/o 后仅 3.0%）和 Motion Tail（w/o 后 11.2%）两条路径都完整实现，FIFO History + Temporal Ensemble 替代方案（35.6%）不足以替代链式状态。

## Overview
Humans perform long-horizon manipulation by retaining knowledge of what earlier actions have established while continuously adapting the motion underway. By contrast, action-chunked vision-language-action (VLA) policies repeatedly replan from the current input at each query. Existing methods preserve either long-term task evidence through memory or short-term motion through action reuse and ensembling, leaving the cross-query handoff incomplete. We introduce ChainVLA, a 1.2B-parameter VLA policy that chains successive queries through a joint and revisable execution state. Progress Context combines a recurrent Working State with sparse event memory to carry observation-derived task progress, while Motion Tail feeds the preceding prediction's unexecuted continuation into state construction and action generation. Together, the two components condition a decoder that regenerates each action horizon under the latest observation, allowing the carried state to guide the next prediction without fixing it. ChainVLA reaches 62.8% average success on RMBench and 98.8% across four LIBERO suites, while removing Motion Tail or Progress Context reduces RMBench success to 11.2% and 3.0%, respectively. These asymmetric ablations are consistent with motion continuity helping preserve the observation stream from which task progress is inferred.

## 参考
- https://arxiv.org/abs/2608.02326

## 개요

ChainVLA는 1.2B 파라미터의 비전-언어-행동(VLA) 정책으로, 결합 가능하고 수정 가능한 실행 상태 s_k = (g_k, u_k)를 통해 연속 쿼리를 체인 방식으로 연결하여 장기간 조작에서 쿼리 간 작업 진행 상황과 운동 연속성 문제를 해결합니다. 핵심 기여는 순환 작업 상태(Progress Context)와 운동 꼬리(Motion Tail)를 하나의 쿼리 전이 프레임워크로 통합한 것으로, RMBench에서 62.8% 평균 성공률(기준선 크게 초과), LIBERO에서 98.8% 평균 성공률(모든 비교 방법 능가)을 달성했습니다.

## 무엇을 바꾸었는가

기존 action-chunked VLA 정책은 각 쿼리 시 현재 입력에서 재계획하며 두 가지 정보 부족 문제가 있습니다: 작업 수준에서 초기 작업 증거가 현재 시야에 없을 수 있고(예: Put Back Block 작업에서 동일한 관측과 명령이 다른 이력을 가리켜 다른 결정이 필요할 수 있음), 운동 수준에서 재계획은 이전 예측의 실행되지 않은 연속 부분을 버려 새 예측의 접두사가 대체하는 운동과 일치하지 않게 됩니다. memory-augmented 정책은 장기 작업 증거를 유지하지만 실행되지 않은 행동 연속 부분은 유지하지 않으며, Temporal Ensemble 기반 방법은 단기 운동을 유지하지만 더 이른 작업 증거는 유지할 수 없습니다—두 접근 방식은 상호 보완적이지만 분리되어 있습니다.

ChainVLA가 실제로 바꾼 것은 이 두 가지 정보를 수정 가능한 실행 상태로 통합하고, 운동 연속성이 작업 진행 추론에 필요한 관측 흐름을 보존하는 데 도움이 되므로 두 구성 요소가 독립적으로 작동하는 것이 아니라 순차적으로 작동한다는 점을 강조한 것입니다. 더 이상 쿼리 간 인계를 후처리 기법으로 취급하지 않고 훈련과 배포가 공유하는 일급 시민으로 취급합니다—훈련 시 에피소드 순서로 동일한 실행 상태 전이를 전개하고, 휴대된 접미사는 다음 쿼리를 조건화하기 전에 detach되어 모델이 수동적 이어붙이기가 아닌 능동적 활용을 학습하도록 보장합니다.

## 방법 분해

### 실행 상태 정의
- 상태 s_k = (g_k, u_k), 여기서 g_k = Fuse(L_k, Z_k^e)는 Progress Context(순환 작업 상태 실시간 토큰과 검색된 이벤트 증거의 융합), u_k는 Motion Tail(이전 예측의 실행되지 않은 접미사)
- 쿼리 전이 공식: s_{k+1} = F_θ(s_k, x_k), x_k = (o_k, r_k, ℓ)는 관측, 고유수용감각, 언어 명령
- 엄격한 접두사 감소 시간 영역: 1 ≤ h_exec < H, H 단계 예측 후 h_exec 단계 실행 후 다시 쿼리(H=30, h_exec=24)

### 순환 작업 상태(Recurrent Working State)
- W_k = (L_k, B_k), L_k는 실시간 토큰, B_k는 초기 실시간 토큰의 유계 FIFO 캐시(현재 8개 + 이전 24개, 3슬롯)
- 업데이트 공식:
  - η_k = MLP[φ_r(r_k), Pool(P_k), Pool(U_k), τ_k]
  - L̃_k = CrossAttn(Q_W + η_k, X_k)
  - L_k = LN(L̃_k + m_{k-1}^{live} · CrossAttn(L̃_k, L_{k-1}))
  - W̄_k = Pool([L_k, B_{k-1}, P_k, U_k])
- 8개의 학습 쿼리가 현재 다중 모달 토큰에 주목하고 실시간 토큰을 순환 업데이트하며, 실시간 토큰은 직접 진행 컨텍스트로 들어갑니다

### 희소 이벤트 메모리(Sparse Event Memory)
- C_k = {(κ_i, E_i, b_i)}, 이벤트 본체 `E_i = [V_i, S_i, T_i]`（64 시각 + 8 단계 + 8 시간 토큰）, 용량 16, 가장 오래된 비앵커가 축출됨
- 쓰기 규칙: 첫 번째 유효 쿼리는 앵커로 유지됨; 단계 레이블이 있으면 작업 단계 전환에 따라 트리거, 레이블이 없으면 고정 3쿼리 간격 사용
- 검색 점수: ρ_{k,i} = cos(LN(q_k^e), LN(κ_i + Emb_age(clip(k − b_i)))), 앵커와 가장 높은 점수의 비앵커 레코드 2개 읽기

### Motion Tail의 두 가지 모델 측 경로
1. 동작 공간 정규화 후 학습된 투영으로 tail 토큰 U_{k+1}로 인코딩되어 작업 상태에 사용
2. 정렬된 궤적 초기화 동작 생성: Ã_{k+1}^{(0)} | u_{k+1} ~ N(μ_{k+1}, σ_u²I), μ_{k+1} = I(u_{k+1})

### 디코딩 및 훈련
- 디코더는 conditional-flow DiT 백본으로, 최신 관측, Progress Context 및 tail 토큰에서 각 수평 위치를 재생성하며 어떤 위치도 복사하거나 고정하지 않음—휴대 상태는 고정 계획이 아닌 수정 가능한 사전
- 디코딩 후 컨트롤러가 겹치는 단계를 선형 혼합(실행 측 인계), 두 모델 측 경로와 분리
- 훈련 목표: 표준 conditional-flow 동작 목표 + 단계 감독(레이블이 있을 때) + 겹침 일관성 정규화(가중치 0.2, 이전 예측은 detach됨)
- 훈련 시 에피소드 순서로 전개, 휴대 접미사는 detach 후에만 다음 쿼리를 조건화; 에피소드 시작 시 tail 경로는 마스킹됨

## 핵심 혁신

1. **통합 실행 상태의 이중 채널 설계**: 장기 작업 증거(Progress Context)와 단기 운동 연속성(Motion Tail)을 기존 방법처럼 분리 처리하지 않고 하나의 쿼리 전이 공식으로 통합. 핵심 혁신은 두 구성 요소가 순차적으로 작동한다는 점—운동 연속성이 작업 진행 추론에 필요한 관측 흐름을 보존하는 데 도움이 되며, 이는 w/o Motion Tail 시 성공률이 11.2%로 급락하는 이유(Full은 62.8%)를 설명합니다.

2. **고정 계획이 아닌 수정 가능한 사전**: 디코더는 최신 관측과 진행 컨텍스트에서 각 수평 위치를 재생성하며, 휴대된 꼬리는 복사나 고정이 아닌 초기화 사전(가산 노이즈 섭동)일 뿐입니다. 이는 Temporal Ensemble의 경직된 평균과 달리 새 예측이 운동 연속성을 유지하면서 최신 관측 변화에 대응할 수 있게 합니다.

3. **훈련과 배포가 동일한 상태 전이 공유**: 훈련 시 에피소드 순서로 실행 상태 전이를 전개하고, 휴대 접미사는 detach 후 다음 쿼리를 조건화하며, 0.5 확률로 전임자의 분리 예측 꼬리를 사용합니다. 이는 모델이 배포 시에만 후처리 이어붙이기를 하는 것이 아니라 훈련 단계에서부터 쿼리 간 정보를 능동적으로 활용하도록 학습하게 합니다—소거 실험에서 FIFO History + Temporal Ensemble 대안은 35.6%에 불과해 Full보다 27.2% 포인트 낮습니다.

## 실험 및 결과

### RMBench 주요 결과(성공률 %, 100 episodes/작업)
| 방법 | Obs. | Rearr. | Put B. | Swap B. | Swap T. | Avg. |
|------|------|--------|--------|---------|---------|------|
| DP | 1 | 0 | 0 | 11 | 20 | 6.4 |
| ACT | 1 | 29 | 0 | 2 | 2 | 6.8 |
| π_0.5 (2.6B+0.3B) | 9 | 13 | 11 | 24 | 15 | 14.4 |
| MemoryVLA (7B+0.3B) | 0 | 22 | 50 | 17 | 9 | 19.6 |
| Mem-0 (8B+2B) | 4 | 89 | 90 | 67 | 14 | 52.8 |
| **ChainVLA (1.2B)** | **11** | **93** | **96** | **74** | **40** | **62.8** |

### LIBERO 주요 결과(성공률 %, 50 episodes/작업)
| 방법 | Spatial | Object | Goal | Long | Avg. |
|------|---------|--------|------|------|------|
| OpenVLA (7B) | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |
| GR00T-N1 (2.2B) | 94.4 | 97.6 | 93.0 | 90.6 | 93.9 |
| π_0 (3.3B) | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| MemoryVLA (7B+0.3B) | 98.4 | 98.4 | 96.4 | 93.4 | 96.7 |
| CronusVLA (7B) | 97.3 | 99.6 | 96.9 | 94.0 | 97.0 |
| X-VLA (0.9B) | 98.2 | 98.6 | 97.8 | 97.6 | 98.1 |
| **ChainVLA (1.2B)** | **98.4** | **99.4** | **99.2** | **98.2** | **98.8** |

### 핵심 소거(RMBench 성공률 %)
| 조건 | Avg. |
|------|------|
| w/o Progress Ctx. | 3.0 |
| w/o Motion Tail | 11.2 |
| w/o Both | 1.6 |
| FIFO Hist. + TE | 35.6 |
| **ChainVLA (Full)** | **62.8** |

### 경계 진단(80쌍 매칭 시나리오, Full vs w/o Motion Tail 풀링 감소)
| 지표 | 감소 폭 |
|------|----------|
| CD_p(위치 명령 불연속성) | 56.6% |
| CD_R(방향 명령 불연속성) | 40.4% |
| B2(경계 2차 차분) | 57.4% |
| RMSE_3(3단계 겹침 RMSE) | 43.1% |

후디코딩 평활 제어 비교: Put Back Block에서 w/o Motion Tail 성공률 0(CD_p 5.90), Linear Cont. 성공률 0(CD_p 2.09), Temporal Ens. 성공률 0(CD_p 3.57), Full 성공률 96(CD_p 2.69)—후처리 평활만으로는 체인 상태의 능력을 복원할 수 없음을 보여줍니다.

## 경계 및 한계

- 모든 결과는 고정 속도 시뮬레이션(RMBench 및 LIBERO)에서 나왔으며, 경계 진단은 명령 흐름을 설명하지 물리적 궤적을 설명하지 않음; 하드웨어에서 평가되지 않았고 제어 속도를 변경하지 않았으며, 보고된 여유는 비동기 또는 실시간 배포의 예측으로 간주해서는 안 됨
- 각 내부 훈련 조건은 단일 랜덤 시드(42)를 사용하며, 시드 변동성이나 유의성 검정이 보고되지 않아 성공률과 경계 평균은 점 추정으로 간주해야 함
- 각 소거는 훈련과 배포에서 동시에 경로를 철회하여 조립된 시스템의 해당 경로 의존성을 측정하지 내부 메커니즘을 격리하지 않음; 경계 측정은 상관 관계를 설정하지 구성 요소 수준 인과 관계를 설정하지 않음
- 별도의 플래너나 세계 모델을 사용하여 하위 목표를 분해하거나 잠재 상태를 상상하지 않음; Motion Tail을 기호 계획이나 잠재 목표로 사용하지 않음; LIBERO에서 소거 분석을 수행하지 않음(상한에 근접)
- 네 가지 진단 모두 이음새에만 국한되며 전체 에피소드 궤적 품질, 누적 상태 편차 또는 고정 주파수 물리적 평활도를 평가하지 않음; 외부 기준선 비교 행은 본 논문 프로토콜 하에서 재실행되지 않았으며 백본, 데모 수, 최적화 예산 및 성공 기준이 다를 수 있음
- 고정 설계 선택(시야 30, 접두사 24, 메모리 용량 16, 쓰기 신뢰도 0.55, 겹침 가중치 0.2)은 모두 한 번 고정되어 검색되지 않았으며 민감도를 보고할 수 없음

## 공학적 시사점

재현 시 네 가지 핵심 하이퍼파라미터를 먼저 확인하세요: 시야 H=30과 실행 접두사 h_exec=24의 비율(6단계 꼬리 유지), 이벤트 메모리 용량 16, 겹침 일관성 가중치 0.2, 단계 레이블이 없을 때의 3쿼리 쓰기 간격. 가장 함정에 빠지기 쉬운 것은 훈련과 배포의 상태 전이 일관성—훈련 시 반드시 에피소드 순서로 쿼리를 전개하고, 휴대 접미사는 detach 후에만 다음 쿼리를 조건화하며, 에피소드 시작 시 tail 경로는 반드시 마스킹해야 합니다. 그렇지 않으면 훈련-배포 분포 이동이 발생합니다.

두 번째 함정은 단계 레이블 처리입니다: 레이블이 있으면 ground-truth 전환이 단계 추정과 훈련 시 쓰기 대상을 감독하지만 레이블은 절대 동작 디코더에 들어가지 않습니다; 레이블이 없으면 고정 3쿼리 간격을 사용합니다. 다운스트림 작업에 단계 레이블이 없으면 3쿼리 간격이 합리적인지 먼저 검증하는 것이 좋습니다. 쓰기 빈도는 이벤트 메모리의 검색 품질에 직접 영향을 미치기 때문입니다.

세 번째 함정은 소거 실험 해석입니다: 각 소거는 경로 입력, 훈련 항목 및 배포 처리를 동시에 철회하므로 w/o Motion Tail의 11.2%는 단일 메커니즘의 고립 효과가 아니라 전체 꼬리 경로(훈련 정규화 포함)의 시스템 의존성입니다. 핵심 능력만 재현하려면 Progress Context(w/o 후 3.0%에 불과)와 Motion Tail(w/o 후 11.2%) 두 경로를 모두 완전히 구현하는 것을 우선시하고, FIFO History + Temporal Ensemble 대안(35.6%)은 체인 상태를 대체하기에 충분하지 않습니다.
