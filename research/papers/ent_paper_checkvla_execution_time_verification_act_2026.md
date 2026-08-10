---
$id: ent_paper_checkvla_execution_time_verification_act_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation'
  zh: 'CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation'
  ko: 'CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation'
summary:
  en: 'Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks,
    issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations
    should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate
    the error: commit-time policy.'
  zh: CheckVLA 提出了一种面向长时程移动操作的开环分块执行验证框架，在动作块执行期间通过动作条件世界模型滚动预测与校准风险触发，实现延迟一致的“后缀重写”修复。核心贡献在于将验证触发与修复机制解耦设计，通过共形校准控制误报率，并利用风险自适应引导权重在扰动发生后及时纠正动作而不伤害原本成功的轨迹。在
    RoboCasa365 基准上，该方法将扰动成功率提升至 47.6%，同时保持 4.8% 的情节级误报率。
  ko: 'Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks,
    issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations
    should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate
    the error: commit-time policy.'
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
- checkvla
- execution
- time
- verification
- act
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. 深读+数字白名单复核通过 2026-08-10（补网）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.26789 CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Lo'
  url: https://arxiv.org/abs/2607.26789
  date: '2026-07-29'
  accessed_at: '2026-08-05'
---

## 概述

CheckVLA 提出了一种面向长时程移动操作的开环分块执行验证框架，在动作块执行期间通过动作条件世界模型滚动预测与校准风险触发，实现延迟一致的“后缀重写”修复。核心贡献在于将验证触发与修复机制解耦设计，通过共形校准控制误报率，并利用风险自适应引导权重在扰动发生后及时纠正动作而不伤害原本成功的轨迹。在 RoboCasa365 基准上，该方法将扰动成功率提升至 47.6%，同时保持 4.8% 的情节级误报率。

## 它改变了什么

开环分块执行（open-loop action chunking）是当前 VLA 策略部署的主流范式，但其根本缺陷在于块内反馈缺失——策略在块边界提交 H 步动作后，对块内发生的物理扰动（如物体滑动、碰撞偏移）完全失明，偏差只能累积到下一个块边界才被发现，此时往往已无法挽回。现有解决方案要么在提交时估计不确定性（无法利用派发后观测），要么用纯观测异常检测（缺乏动作条件参考，无法区分预期效果与异常偏差），要么做固定周期重规划（浪费调用预算且同样延迟感知不足）。CheckVLA 真正改变的是：把“验证”从策略置信度中剥离出来，变成一个独立的、动作条件化的、可校准的监控通道，并配套一个延迟感知的修复机制，使得系统能在扰动发生后 3 个控制步内（覆盖中位推理延迟 286ms）触发重规划并部署新动作块。这相当于在开环执行中重新引入了闭环反馈，且不牺牲策略本身的训练范式。

## 方法拆解

### 整体架构
CheckVLA 由四个耦合组件构成：动作条件滚动预测、校准风险触发、延迟感知后缀重写、情节上下文记忆。

### 动作条件滚动预测
- 使用冻结的 V-JEPA 2-AC 编码器 φ 提取观测特征 z_{t'} = φ(o_{t'})，世界模型 Ψ 仅预测未来 k 步（k ≪ H，H=50）：
  ẑ_{t'+i+1} = Ψ(z_{t'}, ẑ_{t'+1:t'+i}, ā_{t':t'+i}, ŝ_{t':t'+i})
- 每次新观测到达时重新锚定（re-anchor）预测，跨块边界的预测仅在下一块提交后生成
- 训练两阶段：先教师强制（teacher forcing）最小化 Huber 损失，再用自身 rollout 替换预测上下文以匹配在线自回归使用；全程在特征空间进行，无像素解码

### 校准风险触发
- 计算标准化差异 d̃_t = (d_t - μ_d^(ℓ)) / max(σ_d^(ℓ), ε)，时间因果风险头 R 在窗口 x_{t-w+1:t} 上聚合每步元组 x_τ = (d̃_τ, ℓ(τ)/k, h_τ/H, Δ_sw,τ)
- 风险头输出 r_t = R(x_{t-w+1:t}, m(ρ_t)) ∈ [0,1]，训练数据包含名义成功、自然失败、物理扰动三类轨迹，对 [τ_on, τ_on+Δ] 内 softmax 池化风险施加二元交叉熵
- 共形校准：在名义成功影子模式轨迹上拟合每步风险统计 (μ_{r,t}, σ_{r,t})，校准分数 κ^(i) = sup_t (r_t^(i) - μ_{r,t})/σ̃_{r,t}，阈值 δ_t = μ_{r,t} + q̂_α σ̃_{r,t}，q̂_α 为 ⌈(n+1)(1-α)⌉ 阶统计量，α=0.05

### 延迟感知后缀重写
- 触发时刻 t* 后，策略推理需 d_lat=3 个控制步（覆盖中位延迟 286ms，控制周期 100ms），旧块步骤 20-22 继续执行形成“不可逆前缀”
- 新块从 h=d_lat 部署，硬约束前缀位置匹配已执行动作（Eqs. 9-10）
- 引导权重 W_{h,m} = w_0(e_{t*})exp(-λ_m(h - d_lat))，其中 w_0(e) = w_min + (1-w_min)exp(-βe)，e 为标准化超限，超限越大允许修正越强
- 引导混合：v = (1-W) ⊙ v_θ + W ⊙ v_ref，v_ref 为旧块参考速度

### 解耦动作专家与情节记忆
- 移动和操作专家各有独立 QKV 投影、前馈网络和去噪头，仅通过共享 VLM 前缀令牌的联合自注意力交互；stop-gradient 隔离 VLM 主干
- 事件驱动关键帧库 B_t 跨块和修复持久化，非学习两阶段过滤器写入；策略通过门控交叉注意力融合完整库，风险头仅读取紧凑摘要 m(ρ_t)

## 关键创新

1. **动作条件验证（Action-Conditioned Verification）**：世界模型基于已提交动作预测未来观测特征，将预测-观测差异作为风险信号。相比纯观测预测器（召回 48.6%）和动作洗牌对照（召回 37.9%），动作条件化将及时召回提升至 77.9%，证明“知道策略打算做什么”是区分预期效果与异常偏差的关键。这是首次将动作条件世界模型用于执行时验证而非规划。

2. **共形校准的时变阈值（Conformal Calibration with Time-Varying Threshold）**：在名义成功轨迹上拟合每步风险统计，用分割共形校准（split conformal）计算有限样本分位数，提供轨迹边际保证 Pr(∃t: r_t > δ_t | 名义成功) ≤ α。这解决了验证器阈值调参的“最后一公里”问题——恒定阈值将 FWER 从 4.8% 升至 7.1%，而校准阈值在 4.8% 的误报率下保持 77.9% 的召回。

3. **风险自适应引导权重（Risk-Adaptive Guidance Weight）**：将标准化超限映射到参考保留强度，超限越大保留权重越小（单调递减），编码为 w_0(e) = w_min + (1-w_min)exp(-βe)。相比固定权重（W=0.5）和打乱超限对照，自适应机制将救援率从 12.8% 提升至 16.9%，伤害率从 3.7% 降至 2.8%，且在不同超限区间均接近逐区间最优权重包络线（差距 ≤1.5 个百分点）。

## 实验与结果

### 主结果（RoboCasa365，3 种子均值）

| 方法 | A-S | C-S | C-U | 平均 |
|---|---|---|---|---|
| π_0.5（已发表） | 39.6 | 7.1 | 1.2 | 16.9 |
| Qwen-RobotManip | 68.6 | 20.1 | 14.9 | 35.9 |
| CheckVLA | 63.7 | 30.9 | 10.2 | 36.1 |

CheckVLA 平均成功率 36.1%，比复现 π_0.5 高 19.2 个百分点，在 C-S 上排名第一（30.9%），C-U 上排名第二。

### 触发比较（目标 FWER α=0.05）

| 检测器 | FWER(%) | 及时召回(%) | 扰动成功(%) |
|---|---|---|---|
| 策略特征探针（最强策略侧基线） | 5.1 | 68.6 | 43.7 |
| 仅观测世界预测器 | 5.3 | 48.6 | 35.2 |
| 动作洗牌世界模型 | 5.1 | 37.9 | 31.0 |
| 完整动作条件验证器 | 4.8 | 77.9 | 47.6 |

完整验证器比探针提高及时召回 9.3 点、扰动成功率 3.9 点；动作条件化将召回从 77.9% 降至 37.9%（动作洗牌）和 48.6%（仅观测）。

### 修复规则对比（d_lat=3）

| 规则 | 救援率(%) | 伤害率(%) | 成功率(%) |
|---|---|---|---|
| 等待边界 | 7.4 | 4.8 | 34.0 |
| 无约束丢弃前缀 | 10.1 | 8.9 | 39.8 |
| RTC 前缀保持 | 13.7 | 4.1 | 45.6 |
| 固定引导 W | 12.8 | 3.7 | 46.0 |
| 自适应 W(e) | 16.9 | 2.8 | 47.6 |

### 消融与敏感性
- 无滚动重锚定：召回降至 62.8%；瞬时分数（无时间聚合）：召回 66.1%
- 无良性负样本：FWER 升至 6.2%，良性伤害从 1.2% 升至 4.7%
- 记忆消融：完整设计将子目标回归从 1.34 降至 0.18，FWER 从 5.6% 降至 4.8%
- 部署成本：新增 88.4M 参数、16.9 GFLOPs/步，墙钟因子 1.18×，监控 p95 16.4ms 低于控制周期
- 留出自然执行：成功率从 61.4%（开环）升至 68.9%，伤害 2.7%

## 边界与局限

- 结论仅限于 RoboCasa365 模拟器及所述任务、场景和扰动分布，不建立硬件安全性；作者明确未做真实机器人实验
- 共形校准仅控制可交换名义成功情节上不必要首次干预的概率，不保证扰动下的召回、修复后安全、重复干预或分布偏移覆盖
- “不可逆性”指测试修复集下恢复窗口的关闭，非物理不可能性；若可部署后缀过少或不存在可行替换，即使正确警告也无法恢复
- 动作绑定审计不分离动作令牌与名义本体感受 rollout 两条路径的信息贡献
- 观测刷新策略侧信号变体是离线上限，不可部署（p95 延迟超控制周期）；未提及跨模拟器泛化、多扰动并发处理
- 表 2 与已发表结果比较是描述性而非配对比较，因公开系统在预训练数据之外存在差异

## 工程启示

- **先核对动作条件化是否成立**：验证器性能高度依赖世界模型对“已提交动作”的预测质量。复现时先跑动作洗牌对照（表 S3），若动作条件化增益不明显，说明世界模型没有真正利用动作信息，需检查预测上下文是否包含完整动作序列及本体感受
- **共形校准的坑**：所有风险统计必须在计算分位数前固定，校准集与名义成功影子模式轨迹不相交；每检查点独立校准，超参数在验证数据上选择一次后锁定。校准规模从 100 到 400 片段，FWER 从 5.4% 降至 4.8%，建议至少 300 片段
- **延迟调度是修复成败的关键**：d_lat=3 对应中位推理延迟 286ms，但 p95 为 338ms，需扫描至 d_lat=10 验证鲁棒性。硬前缀约束（Eqs. 9-10）必须严格实现，否则切换跳跃（switch jump）会引入部署不连续性
- **良性负样本不可省略**：无良性负样本时 FWER 升至 6.2%，良性伤害翻倍至 4.7%。风险头训练数据必须包含名义成功轨迹和良性偏差，否则验证器会对无害外观变化反应过度
- **监控器与策略解耦**：冻结 V-JEPA 2-AC 编码器 + 独立风险头，监控 p95 16.4ms 低于控制周期，与执行重叠。若监控延迟超一个控制周期，需考虑异步调度或降低预测频率 k
- **记忆库的写入过滤是性能瓶颈**：事件驱动关键帧库将子目标回归从 1.34 降至 0.18，但需注意两阶段过滤器（延迟确认的关节空间位移局部最小值 + 相似性/时间接近拒绝）的参数敏感性；策略读取完整库而风险头仅读紧凑摘要，两者必须独立训练

## Overview
Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks, issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate the error: commit-time policy confidence cannot react to a deviation that occurs after dispatch, and observation-only anomaly scores lack an action-conditioned reference for separating expected effects from unexplained changes. We propose CheckVLA, which verifies execution with a separately trained, frozen action-conditioned world model. A conformally calibrated risk threshold bounds the episode-level probability of an unnecessary first intervention and determines when to intervene, its exceedance controls how strongly the rewritten suffix retains the superseded chunk, latency-aware hard prefixing restricts replacement to actions that remain deployable, and an event-driven keyframe bank preserves evidence of prior progress across repairs. On RoboCasa365, under a common training recipe and a matched invocation budget, CheckVLA attains a 36.1% average success rate against 27.6% for periodic replanning (+8.5 points). At a matched 5% episode-level false-alarm target, action conditioning raises timely recall to 77.9%, against 48.6% for an observation-only control and 37.9% for an action-shuffled control. These simulation results support action-conditioned verification as a way to restore feedback during chunked execution while keeping the repair consistent with inference latency.

## 参考
- https://arxiv.org/abs/2607.26789

## 개요

CheckVLA는 장시간 이동 조작을 위한 개루프 청크 실행 검증 프레임워크를 제안하며, 액션 청크 실행 중 액션 조건부 월드 모델의 롤링 예측과 보정된 위험 트리거를 통해 지연 일관된 '접미사 재작성' 수리를 구현합니다. 핵심 기여는 검증 트리거와 수리 메커니즘을 분리 설계하고, 공형 보정(conformal calibration)으로 오탐률을 제어하며, 위험 적응형 유도 가중치를 통해 교란 발생 후 적시에 동작을 수정하면서도 원래 성공한 궤적을 해치지 않는 것입니다. RoboCasa365 벤치마크에서 이 방법은 교란 성공률을 47.6%로 끌어올리면서 에피소드 수준 오탐률 4.8%를 유지합니다.

## 무엇을 바꾸는가

개루프 액션 청킹(open-loop action chunking)은 현재 VLA 정책 배포의 주류 패러다임이지만, 근본적 결함은 청크 내 피드백 부재입니다. 정책이 청크 경계에서 H步 동작을 제출한 후, 청크 내에서 발생하는 물리적 교란(예: 물체 미끄러짐, 충돌 변위)에 완전히 눈이 멀어, 편차는 다음 청크 경계에 도달할 때까지 누적되며 그때는 이미 되돌릴 수 없는 경우가 많습니다. 기존 해결책은 제출 시 불확실성을 추정하거나(발송 후 관측을 활용할 수 없음), 순수 관측 이상 탐지(액션 조건부 참조가 없어 기대 효과와 이상 편차를 구분할 수 없음), 또는 고정 주기 재계획(호출 예산 낭비 및 지연 인식 부족)에 의존합니다. CheckVLA가 실제로 바꾸는 것은 '검증'을 정책 신뢰도에서 분리하여 독립적이고 액션 조건부이며 보정 가능한 모니터링 채널로 만들고, 지연 인식 수리 메커니즘을 결합하여 시스템이 교란 발생 후 3개 제어 스텝 내(중앙값 추론 지연 286ms 포함) 재계획을 트리거하고 새 액션 청크를 배포할 수 있게 하는 것입니다. 이는 개루프 실행에 폐루프 피드백을 다시 도입하면서도 정책 자체의 훈련 패러다임을 희생하지 않는 것과 같습니다.

## 방법 분해

### 전체 아키텍처
CheckVLA는 네 가지 결합 구성 요소로 이루어집니다: 액션 조건부 롤링 예측, 보정된 위험 트리거, 지연 인식 접미사 재작성, 에피소드 컨텍스트 메모리.

### 액션 조건부 롤링 예측
- 동결된 V-JEPA 2-AC 인코더 φ를 사용하여 관측 특징 z_{t'} = φ(o_{t'})를 추출하고, 월드 모델 Ψ는 미래 k步만 예측합니다(k ≪ H, H=50):
  ẑ_{t'+i+1} = Ψ(z_{t'}, ẑ_{t'+1:t'+i}, ā_{t':t'+i}, ŝ_{t':t'+i})
- 새 관측이 도착할 때마다 예측을 다시 앵커링(re-anchor)하며, 청크 경계를 넘는 예측은 다음 청크 제출 후에만 생성됩니다
- 훈련은 두 단계로 진행됩니다: 먼저 교사 강제(teacher forcing)로 Huber 손실을 최소화하고, 이후 자체 롤아웃으로 예측 컨텍스트를 대체하여 온라인 자기회귀 사용과 일치시킵니다. 전체 과정은 특징 공간에서 이루어지며 픽셀 디코딩이 없습니다

### 보정된 위험 트리거
- 표준화된 차이 d̃_t = (d_t - μ_d^(ℓ)) / max(σ_d^(ℓ), ε)를 계산하고, 시간 인과 위험 헤드 R은 창 x_{t-w+1:t}에서 각 스텝 튜플 x_τ = (d̃_τ, ℓ(τ)/k, h_τ/H, Δ_sw,τ)를 집계합니다
- 위험 헤드 출력 r_t = R(x_{t-w+1:t}, m(ρ_t)) ∈ [0,1]이며, 훈련 데이터는 명목 성공, 자연 실패, 물리적 교란 세 가지 궤적 유형을 포함하고, [τ_on, τ_on+Δ] 내 softmax 풀링 위험에 이진 교차 엔트로피를 적용합니다
- 공형 보정: 명목 성공 섀도우 모드 궤적에서 스텝별 위험 통계 (μ_{r,t}, σ_{r,t})를 적합하고, 보정 점수 κ^(i) = sup_t (r_t^(i) - μ_{r,t})/σ̃_{r,t}, 임계값 δ_t = μ_{r,t} + q̂_α σ̃_{r,t}, q̂_α는 ⌈(n+1)(1-α)⌉ 번째 순서 통계량, α=0.05입니다

### 지연 인식 접미사 재작성
- 트리거 시점 t* 이후, 정책 추론은 d_lat=3 제어 스텝(중앙값 지연 286ms, 제어 주기 100ms)이 필요하며, 이전 청크의 스텝 20-22가 계속 실행되어 '되돌릴 수 없는 접두사'를 형성합니다
- 새 청크는 h=d_lat에서 배포되며, 하드 제약 조건으로 접두사 위치가 이미 실행된 동작과 일치해야 합니다(Eqs. 9-10)
- 유도 가중치 W_{h,m} = w_0(e_{t*})exp(-λ_m(h - d_lat)), 여기서 w_0(e) = w_min + (1-w_min)exp(-βe), e는 표준화된 초과량이며, 초과량이 클수록 더 강한 수정이 허용됩니다
- 유도 혼합: v = (1-W) ⊙ v_θ + W ⊙ v_ref, v_ref는 이전 청크의 참조 속도입니다

### 분리된 액션 전문가와 에피소드 메모리
- 이동 및 조작 전문가는 각각 독립적인 QKV 투영, 피드포워드 네트워크, 디노이징 헤드를 가지며, 공유 VLM 접두사 토큰의 결합 자기 주의를 통해서만 상호작용합니다. stop-gradient로 VLM 백본을 격리합니다
- 이벤트 기반 키프레임 라이브러리 B_t는 청크와 수리를 넘어 지속되며, 비학습 2단계 필터로 기록됩니다. 정책은 게이트 교차 주의로 전체 라이브러리를 융합하고, 위험 헤드는 압축 요약 m(ρ_t)만 읽습니다

## 핵심 혁신

1. **액션 조건부 검증(Action-Conditioned Verification)**: 월드 모델이 제출된 액션을 기반으로 미래 관측 특징을 예측하고, 예측-관측 차이를 위험 신호로 사용합니다. 순수 관측 예측기(재현율 48.6%) 및 액션 셔플 대조(재현율 37.9%)와 비교하여, 액션 조건화는 적시 재현율을 77.9%로 끌어올립니다. 이는 '정책이 무엇을 하려는지 아는 것'이 기대 효과와 이상 편차를 구분하는 핵심임을 증명합니다. 실행 중 검증에 액션 조건부 월드 모델을 사용한 것은 이번이 처음입니다(계획이 아닌).

2. **시변 임계값을 갖는 공형 보정(Conformal Calibration with Time-Varying Threshold)**: 명목 성공 궤적에서 스텝별 위험 통계를 적합하고, 분할 공형 보정(split conformal)으로 유한 표본 분위수를 계산하여 궤적 주변 보장 Pr(∃t: r_t > δ_t | 명목 성공) ≤ α를 제공합니다. 이는 검증기 임계값 튜닝의 '마지막 마일' 문제를 해결합니다. 고정 임계값은 FWER를 4.8%에서 7.1%로 올리지만, 보정된 임계값은 4.8%의 오탐률에서 77.9%의 재현율을 유지합니다.

3. **위험 적응형 유도 가중치(Risk-Adaptive Guidance Weight)**: 표준화된 초과량을 참조 보존 강도에 매핑하며, 초과량이 클수록 보존 가중치가 작아집니다(단조 감소). w_0(e) = w_min + (1-w_min)exp(-βe)로 인코딩됩니다. 고정 가중치(W=0.5) 및 셔플된 초과량 대조와 비교하여, 적응 메커니즘은 구조율을 12.8%에서 16.9%로 높이고 손상률을 3.7%에서 2.8%로 낮추며, 다양한 초과량 구간에서 구간별 최적 가중치 포락선에 근접합니다(차이 ≤1.5% 포인트).

## 실험 및 결과

### 주요 결과(RoboCasa365, 3개 시드 평균)

| 방법 | A-S | C-S | C-U | 평균 |
|---|---|---|---|---|
| π_0.5(발표) | 39.6 | 7.1 | 1.2 | 16.9 |
| Qwen-RobotManip | 68.6 | 20.1 | 14.9 | 35.9 |
| CheckVLA | 63.7 | 30.9 | 10.2 | 36.1 |

CheckVLA 평균 성공률 36.1%로, 재현된 π_0.5보다 19.2% 포인트 높으며, C-S에서 1위(30.9%), C-U에서 2위를 기록했습니다.

### 트리거 비교(목표 FWER α=0.05)

| 감지기 | FWER(%) | 적시 재현율(%) | 교란 성공률(%) |
|---|---|---|---|
| 정책 특징 프로브(가장 강한 정책 측 기준선) | 5.1 | 68.6 | 43.7 |
| 관측 전용 월드 예측기 | 5.3 | 48.6 | 35.2 |
| 액션 셔플 월드 모델 | 5.1 | 37.9 | 31.0 |
| 전체 액션 조건부 검증기 | 4.8 | 77.9 | 47.6 |

전체 검증기는 프로브보다 적시 재현율 9.3% 포인트, 교란 성공률 3.9% 포인트 향상시켰습니다. 액션 조건화는 재현율을 77.9%에서 37.9%(액션 셔플) 및 48.6%(관측 전용)로 낮췄습니다.

### 수리 규칙 비교(d_lat=3)

| 규칙 | 구조율(%) | 손상률(%) | 성공률(%) |
|---|---|---|---|
| 경계 대기 | 7.4 | 4.8 | 34.0 |
| 제약 없는 접두사 폐기 | 10.1 | 8.9 | 39.8 |
| RTC 접두사 유지 | 13.7 | 4.1 | 45.6 |
| 고정 유도 W | 12.8 | 3.7 | 46.0 |
| 적응형 W(e) | 16.9 | 2.8 | 47.6 |

### 소거 및 민감도
- 롤링 재앵커링 없음: 재현율 62.8%로 하락; 순간 점수(시간 집계 없음): 재현율 66.1%
- 양성 부정 샘플 없음: FWER 6.2%로 상승, 양성 손상 1.2%에서 4.7%로 상승
- 메모리 소거: 전체 설계가 하위 목표 회귀를 1.34에서 0.18로 낮추고, FWER를 5.6%에서 4.8%로 낮춤
- 배포 비용: 추가 88.4M 파라미터, 16.9 GFLOPs/스텝, 벽시계 계수 1.18×, 모니터링 p95 16.4ms로 제어 주기 미만
- 홀드아웃 자연 실행: 성공률 61.4%(개루프)에서 68.9%로 상승, 손상 2.7%

## 경계 및 한계

- 결론은 RoboCasa365 시뮬레이터 및 설명된 작업, 시나리오, 교란 분포에만 국한되며 하드웨어 안전성을 확립하지 않습니다. 저자는 실제 로봇 실험을 수행하지 않았음을 명시했습니다
- 공형 보정은 교환 가능한 명목 성공 에피소드에서 불필요한 첫 개입의 확률만 제어하며, 교란 하 재현율, 수리 후 안전성, 반복 개입 또는 분포 이동 커버리지를 보장하지 않습니다
- '되돌릴 수 없음'은 테스트 수리 세트에서 복구 창이 닫히는 것을 의미하며 물리적 불가능성을 의미하지 않습니다. 배포 가능한 접미사가 너무 적거나 실행 가능한 대체가 없으면 올바른 경고에도 복구할 수 없습니다
- 액션 바인딩 감사는 액션 토큰과 명목 본체감각 롤아웃 두 경로의 정보 기여를 분리하지 않습니다
- 관측 새로고침 전략 측 신호 변형은 오프라인 상한이며 배포할 수 없습니다(p95 지연이 제어 주기를 초과). 시뮬레이터 간 일반화, 다중 교란 동시 처리에 대한 언급은 없습니다
- 표 2와 발표된 결과의 비교는 설명적이며 쌍별 비교가 아닙니다. 공개 시스템이 사전 훈련 데이터 외부에서 차이가 있기 때문입니다

## 엔지니어링 시사점

- **액션 조건화가 성립하는지 먼저 확인하세요**: 검증기 성능은 월드 모델의 '제출된 액션' 예측 품질에 크게 의존합니다. 재현 시 먼저 액션 셔플 대조(표 S3)를 실행하고, 액션 조건화 이득이 명확하지 않으면 월드 모델이 액션 정보를 실제로 활용하지 않는 것이므로 예측 컨텍스트에 전체 액션 시퀀스와 본체감각이 포함되어 있는지 확인하세요
- **공형 보정의 함정**: 모든 위험 통계는 분위수 계산 전에 고정되어야 하며, 보정 세트는 명목 성공 섀도우 모드 궤적과 교차하지 않아야 합니다. 각 체크포인트는 독립적으로 보정하고, 하이퍼파라미터는 검증 데이터에서 한 번 선택한 후 잠급니다. 보정 규모를 100에서 400개 세그먼트로 늘리면 FWER가 5.4%에서 4.8%로 감소하므로 최소 300개 세그먼트를 권장합니다
- **지연 스케줄링은 수리 성공의 핵심입니다**: d_lat=3은 중앙값 추론 지연 286ms에 해당하지만 p95는 338ms이므로 d_lat=10까지 스캔하여 견고성을 검증해야 합니다. 하드 접두사 제약(Eqs. 9-10)은 엄격히 구현해야 하며, 그렇지 않으면 스위치 점프가 배포 불연속성을 도입합니다
- **양성 부정 샘플은 생략할 수 없습니다**: 양성 부정 샘플이 없으면 FWER가 6.2%로 상승하고 양성 손상이 4.7%로 두 배가 됩니다. 위험 헤드 훈련 데이터에는 명목 성공 궤적과 양성 편차가 반드시 포함되어야 하며, 그렇지 않으면 검증기가 무해한 외관 변화에 과민 반응합니다
- **모니터와 정책 분리**: 동결된 V-JEPA 2-AC 인코더 + 독립 위험 헤드로, 모니터링 p95 16.4ms가 제어 주기보다 낮아 실행과 중첩됩니다. 모니터링 지연이 제어 주기를 초과하면 비동기 스케줄링 또는 예측 빈도 k 감소를 고려하세요
- **메모리 라이브러리 쓰기 필터는 성능 병목입니다**: 이벤트 기반 키프레임 라이브러리는 하위 목표 회귀를 1.34에서 0.18로 낮추지만, 2단계 필터(지연 확인된 관절 공간 변위 로컬 최소값 + 유사성/시간 근접 거부)의 파라미터 민감성에 주의해야 합니다. 정책은 전체 라이브러리를 읽고 위험 헤드는 압축 요약만 읽으므로 둘은 독립적으로 훈련해야 합니다
