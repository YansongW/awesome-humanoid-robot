---
$id: ent_paper_think_5_hz_act_20_hz_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving'
  zh: 'Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving'
  ko: 'Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving'
summary:
  en: Large language models bring instruction following and scene reasoning to end-to-end driving, but their inference latency
    collides with the control rate a vehicle requires. Existing closed-loop agents hide this gap by invoking the model on
    alternate simulation ticks and replaying the previous command in between, so half of all control outputs ignore the newest
    observations. We present a fast-slow.
  zh: 本文提出一种异步快慢双系统闭环驾驶架构：冻结的 7B 视觉-语言骨干作为慢系统低频消化导航指令与视觉历史，轻量 337M 动作专家作为快系统在每个仿真 tick 通过单次前向传播回归航点。核心贡献在于利用骨干逐层键值缓存作为常驻场景表示，使快系统在消费级硬件上以
    20 Hz 全控制率运行，同时通过陈旧性增强训练吸收缓存滞后，显著提升闭环驾驶完成率与路线偏离指标。
  ko: Large language models bring instruction following and scene reasoning to end-to-end driving, but their inference latency
    collides with the control rate a vehicle requires. Existing closed-loop agents hide this gap by invoking the model on
    alternate simulation ticks and replaying the previous command in between, so half of all control outputs ignore the newest
    observations. We present a fast-slow.
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
- think
- '5'
- hz
- act
- '20'
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
  title: 'arXiv:2607.15621 Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Infer'
  url: https://arxiv.org/abs/2607.15621
  date: '2026-07-17'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一种异步快慢双系统闭环驾驶架构：冻结的 7B 视觉-语言骨干作为慢系统低频消化导航指令与视觉历史，轻量 337M 动作专家作为快系统在每个仿真 tick 通过单次前向传播回归航点。核心贡献在于利用骨干逐层键值缓存作为常驻场景表示，使快系统在消费级硬件上以 20 Hz 全控制率运行，同时通过陈旧性增强训练吸收缓存滞后，显著提升闭环驾驶完成率与路线偏离指标。

## 它改变了什么

现有闭环 VLA 智能体（如 LMDrive）的延迟问题被普遍视为根本性瓶颈，通常通过隔 tick 调用模型、中间重放上一条命令来掩盖，导致一半控制输出忽略最新观测。本文改变了这一认知框架：将延迟问题重新定义为架构性而非根本性——指令理解与时序场景聚合变化缓慢，而当前帧到轨迹的映射必须快速但计算量轻。这一判断将问题从“如何加速大模型”转向“如何设计计算分工”，使 7B 模型在消费级 GPU 上以全控制率参与闭环成为可能。

此前 fast-slow 设计（DriveVLM、π₀、DriveVLA-W0）要么仅交换轨迹、要么仅在同步开环基准上评估，未证明 fast-slow VLA 能在消费级硬件上以全控制率吸收缓存陈旧性并改善驾驶结果。本文首次在 CARLA 闭环中验证了这一架构假设，将控制率从 10 Hz 提升至 20 Hz，同时将路线完成率从 37.0 提升至 94.0，并证明缓存陈旧性可通过训练分布内采样被有效吸收。

## 方法拆解

### 整体架构
- **慢系统**：冻结的 7B 视觉-语言骨干，低频（每 K=4 tick，0.2 s）消化导航指令与视觉历史，暴露逐层键值缓存作为场景常驻表示。
- **快系统**：轻量动作专家，每个仿真 tick（50 ms）通过单次前向传播回归 5 个航点。

### 动作专家设计
- 32 层 transformer，隐藏宽度 d_ae=512，与骨干层一一对应。
- 每层通过矩形投影 W^ℓ_{q,k,v} ∈ R^{4096×512} 将自身 token 投影到骨干的 32 头、128 维注意力几何中，拼接骨干同层缓存键值后执行单次注意力操作，输出投影回 d_ae 并接 SwiGLU 前馈块。
- **关键属性**：骨干从不关注专家 token，因此缓存无论专家是否运行都相同——这是允许缓存的关键设计决策。
- 专家 token 携带可学习位置嵌入、无旋转编码；骨干键保留其缓存时的旋转相位，使仅追加缓存精确。

### 每帧专家输入
- 10 个 token：1 个状态 token（嵌入先前预测航点、先前控制三元组、当前速度、目标点）、当前帧 4 个视觉 token（由与骨干相同的 Q-Former 管线产生）、5 个可学习航点查询，由两层头在 L1 监督下解码为 5 个 (x,y) 航点。

### 陈旧性增强训练
- 部署时缓存落后当前帧最多 K 个 tick。训练时对每个样本采样 δ ~ U{0,…,δ_max}，掩蔽帧 j 的专家块可见的骨干前缀使其止于帧 j−δ（当 j<δ 时仅见指令文本）。
- 状态 token 在高斯噪声和随机 dropout 下用教师强制的先前航点训练。
- 所有帧通过逐块注意力掩蔽并行监督。

### 异步部署
- 骨干缓存作为可变状态维护。每 K=4 tick 通过增量前向传播追加当前帧 4 个 token，成本与历史长度无关。
- 仅在指令变化、通知到达、episode 结束或缓存达训练窗口上限时从头重建。
- 每个 tick 专家按原样读取缓存，测试时陈旧性上界为 K−1 个 tick，保持在训练分布内。
- 黄金测试确认增量与整体预填充的航点差异低于 4 mm（fp16 噪声底）。

## 关键创新

1. **缓存不变性设计**：骨干从不关注专家 token，使缓存与专家运行状态解耦。这一设计允许快系统任意频率读取缓存而不触发骨干重算，是异步部署的架构基础，此前 fast-slow 设计未明确利用此属性。

2. **陈旧性增强训练**：将部署时的缓存滞后显式建模为训练分布的一部分，通过随机掩蔽骨干前缀模拟 δ 个 tick 的滞后。这使得快系统在测试时面对陈旧缓存仍能保持性能，是闭环中 20 Hz 控制率得以实现的关键训练策略。

3. **增量缓存维护**：利用旋转相位使仅追加缓存精确，每 K=4 tick 的增量前向传播成本与历史长度无关（闭环内中位数 10.7 ms）。这打破了传统 transformer 推理延迟随上下文线性增长的瓶颈，使长历史场景聚合成为可能。

## 实验与结果

### 开环航点精度（表 1，同步 δ=0 协议）
| 配置 | L1 | 训练参数 |
|---|---|---|
| 骨干动作头（冻结） | 0.123 | — |
| 动作专家，仅 δ=0 | 0.037 | 337M |
| 动作专家，随机 δ（本文） | 0.031 | 337M |

### 闭环驾驶（表 2，LangAuto-Short town05，32 路线）
| 配置 | 控制率 | DS | RC | IS |
|---|---|---|---|---|
| LMDrive（重放 tick） | 10 Hz | 28.8 ± 0.8 | 37.0 ± 0.4 | 0.80 ± 0.04 |
| FastSlow-LMDrive，帧跳过 | 10 Hz | 34.0 | 82.1 | 0.45 |
| FastSlow-LMDrive（本文） | 20 Hz | 32.9 ± 0.7 | 94.0 ± 2.6 | 0.37 ± 0.02 |

### 每公里违规（两次运行均值）
- 基线：25.0 次路线偏离、2.9 次超时；本文：4.3 次偏离、0.08 次超时。
- 每公里车辆碰撞从 3.2 升至 11.2；布局碰撞从 10.3 降至 2.2；偏离车道从 7.9 降至 1.1。

### 延迟（表 3，40 帧历史，RTX 3090 Ti，中位数）
| 组件 | Legacy | 本文 |
|---|---|---|
| 感知 + Q-Former | 26.9 每步 | 24.8 每 tick（29.2） |
| 骨干全量重算 | 61.6 每步 | 无 |
| 增量追加 | — | 21.1 每 K=4 tick（10.7） |
| 动作专家 | — | 7.5 每 tick（9.3） |
| 总模型计算 | 88.6 | 32.4 每 tick；5.3 每 K=4 tick 摊销 |

### 零样本城镇迁移（表 4，单次运行）
- town01：LMDrive DS=20.5、RC=40.5、IS=0.56；本文 DS=23.2、RC=84.3、IS=0.26。
- town02：LMDrive DS=11.6、RC=30.7、IS=0.38；本文 DS=28.3、RC=94.4、IS=0.29。
- town02 上驾驶分数为基线 2.4 倍、完成率为 3.1 倍。

### 陈旧性增强消融（同步 δ=0 协议下逐 epoch 验证 L1）
- 随机 δ 专家 vs δ=0 孪生：0.060 vs 0.067，0.049 vs 0.056，0.037 vs 0.045，收敛时 0.031 vs 0.037。

## 边界与局限

- 本研究为仿真研究，仅在单一城镇（town05）的短路线上训练，长路线上的危险协商不迁移；每公里车辆碰撞随完成率上升而增加（由表内数值 3.2→11.2 计算）。
- 低层控制器继承了为较慢基线调优的增益，未重新调参，可能限制 20 Hz 控制率的潜在收益。
- 主要对比为每配置两次运行，帧跳过消融和迁移行为单次运行，观测到运行间散布最高 1.6 DS。
- 驾驶系统需要远超仿真基准的安全验证，本文结果不应被解读为道路就绪的证据。
- 未做之事：未将骨干与世界模型预训练结合以丰富缓存编码内容；未使用 fast-slow 分歧作为免训练的安全监督触发；未在长路线训练片段上训练（作者指出这是自然下一步）。

## 工程启示

- **复现优先核对**：训练时骨干、感知编码器、Q-Former、原始头全部冻结，从公开 LMDrive 检查点初始化；batch size 4 时峰值低于 28 GB GPU 内存，单张 48 GB GPU 可训练。推理时单张 RTX 3090 Ti 即可闭环，墙钟速率约 17 Hz。
- **最易踩坑点**：陈旧性增强训练中 δ 的采样范围需与部署时 K 值匹配（本文 K=4，δ_max 对应 4 个 tick）；若部署时缓存滞后超出训练分布，专家性能可能显著退化。黄金等价测试（航点差异 < 4 mm）应作为缓存维护正确性的常规验证。
- **下游团队指导**：若需迁移到新场景，注意长路线上的惩罚因子塌缩（本文 town03 上惩罚因子 0.04 导致驾驶分数 2.96 低于基线 5.98），建议在长路线训练片段上微调；低层 PID 参数需针对 20 Hz 控制率重新调优，直接沿用慢基线参数可能掩盖架构收益。

## Overview
Large language models bring instruction following and scene reasoning to end-to-end driving, but their inference latency collides with the control rate a vehicle requires. Existing closed-loop agents hide this gap by invoking the model on alternate simulation ticks and replaying the previous command in between, so half of all control outputs ignore the newest observations. We present a fast-slow architecture that removes this compromise. A frozen 7B vision-language backbone acts as the slow system, digesting navigation instructions and visual history at low frequency while exposing its per-layer key-value cache as a standing representation of the scene. A lightweight action expert acts as the fast system, attending to this cache and to the current camera frame at every simulation tick to regress waypoints in a single forward pass. Since the cache lags behind the world at deployment, we train the expert under randomized staleness, aligning training with asynchronous execution. On LangAuto-Short routes in CARLA, our system produces fresh control at every 50 ms simulation tick and lifts route completion from 37.0 to 94.0 over the frame-skipping baseline. A frame-skip ablation with the same expert separates the two factors at work: the expert raises the driving score on its own, while per-tick freshness raises completion from 82.1 to 94.0 and cuts red-light violations by a third. Trained on a single town, the expert transfers zero-shot to two unseen towns, holding 84-94% route completion where the baseline reaches 31-41%. It reduces open-loop waypoint error by nearly a factor of four compared to the backbone's own action head, at a per-tick model cost of 32 ms that is independent of history length on a single consumer GPU.

## 参考
- https://arxiv.org/abs/2607.15621

## 개요

본 논문은 비동기식 빠른-느린 이중 시스템 폐루프 주행 아키텍처를 제안한다: 동결된 7B 비전-언어 백본이 느린 시스템으로서 저주파수로 내비게이션 명령과 시각적 이력을 소화하고, 경량 337M 액션 전문가가 빠른 시스템으로서 각 시뮬레이션 틱마다 단일 순방향 전파를 통해 웨이포인트를 회귀한다. 핵심 기여는 백본의 계층별 키-값 캐시를 상주 장면 표현으로 활용하여, 빠른 시스템이 소비자급 하드웨어에서 20 Hz 전체 제어율로 작동하도록 하면서, 오래됨(staleness) 증강 훈련을 통해 캐시 지연을 흡수하여 폐루프 주행 완료율과 경로 이탈 지표를 크게 개선한다는 점이다.

## 무엇을 바꾸었는가

기존 폐루프 VLA 에이전트(예: LMDrive)의 지연 문제는 일반적으로 근본적인 병목으로 간주되며, 일반적으로 틱을 건너뛰어 모델을 호출하거나 중간에 이전 명령을 재생하여 은폐하는데, 이는 제어 출력의 절반이 최신 관측을 무시하게 만든다. 본 논문은 이러한 인식 프레임워크를 변경한다: 지연 문제를 근본적이 아닌 아키텍처적 문제로 재정의한다—명령 이해와 시계열 장면 집계는 느리게 변화하는 반면, 현재 프레임에서 궤적으로의 매핑은 빠르지만 계산량이 가벼워야 한다. 이 판단은 문제를 "대형 모델을 어떻게 가속화할 것인가"에서 "계산 분업을 어떻게 설계할 것인가"로 전환하여, 7B 모델이 소비자급 GPU에서 전체 제어율로 폐루프에 참여할 수 있게 한다.

이전 fast-slow 설계(DriveVLM, π₀, DriveVLA-W0)는 궤적만 교환하거나 동기식 오픈루프 벤치마크에서만 평가되었으며, fast-slow VLA가 소비자급 하드웨어에서 전체 제어율로 캐시 오래됨을 흡수하고 주행 결과를 개선할 수 있음을 입증하지 못했다. 본 논문은 CARLA 폐루프에서 처음으로 이 아키텍처 가설을 검증하여 제어율을 10 Hz에서 20 Hz로 높이고 경로 완료율을 37.0에서 94.0으로 향상시켰으며, 캐시 오래됨이 훈련 분포 내 샘플링을 통해 효과적으로 흡수될 수 있음을 증명했다.

## 방법 분해

### 전체 아키텍처
- **느린 시스템**: 동결된 7B 비전-언어 백본, 저주파수(매 K=4 틱, 0.2초)로 내비게이션 명령과 시각적 이력을 소화하며, 계층별 키-값 캐시를 장면 상주 표현으로 노출한다.
- **빠른 시스템**: 경량 액션 전문가, 각 시뮬레이션 틱(50ms)마다 단일 순방향 전파로 5개의 웨이포인트를 회귀한다.

### 액션 전문가 설계
- 32개 레이어 트랜스포머, 은닉 너비 d_ae=512, 백본 레이어와 일대일 대응.
- 각 레이어는 직사각형 투영 W^ℓ_{q,k,v} ∈ R^{4096×512}을 통해 자체 토큰을 백본의 32개 헤드, 128차원 어텐션 기하 구조로 투영하고, 백본 동일 레이어의 캐시 키-값을 연결한 후 단일 어텐션 연산을 수행하며, 출력을 d_ae로 투영하고 SwiGLU 피드포워드 블록을 연결한다.
- **핵심 속성**: 백본은 전문가 토큰에 주목하지 않으므로, 캐시는 전문가 실행 여부와 관계없이 동일하다—이것이 캐시를 허용하는 핵심 설계 결정이다.
- 전문가 토큰은 학습 가능한 위치 임베딩을 가지며 회전 인코딩이 없다; 백본 키는 캐시 시점의 회전 위상을 유지하여, 추가 전용 캐시가 정확하다.

### 프레임별 전문가 입력
- 10개 토큰: 1개 상태 토큰(이전 예측 웨이포인트, 이전 제어 삼중항, 현재 속도, 목표 지점 임베딩), 현재 프레임의 4개 비전 토큰(백본과 동일한 Q-Former 파이프라인으로 생성), 5개 학습 가능한 웨이포인트 쿼리, 2개 레이어 헤드가 L1 감독 하에 5개의 (x,y) 웨이포인트로 디코딩.

### 오래됨 증강 훈련
- 배포 시 캐시는 현재 프레임보다 최대 K 틱 지연된다. 훈련 시 각 샘플에 대해 δ ~ U{0,…,δ_max}를 샘플링하고, 프레임 j의 전문가 블록이 볼 수 있는 백본 접두사를 프레임 j−δ에서 멈추도록 마스킹한다(j<δ일 때는 명령 텍스트만 볼 수 있음).
- 상태 토큰은 가우시안 노이즈와 무작위 드롭아웃 하에서 교사 강제(teacher forcing)로 이전 웨이포인트를 사용하여 훈련된다.
- 모든 프레임은 블록별 어텐션 마스킹을 통해 병렬로 감독된다.

### 비동기 배포
- 백본 캐시는 가변 상태로 유지된다. 매 K=4 틱마다 증분 순방향 전파를 통해 현재 프레임의 4개 토큰을 추가하며, 비용은 이력 길이와 무관하다.
- 명령 변경, 알림 도착, 에피소드 종료 또는 캐시가 훈련 창 상한에 도달할 때만 처음부터 재구축한다.
- 각 틱마다 전문가는 캐시를 그대로 읽으며, 테스트 시 오래됨 상한은 K−1 틱으로 훈련 분포 내에 유지된다.
- 골든 테스트는 증분과 전체 프리필의 웨이포인트 차이가 4mm 미만임을 확인한다(fp16 노이즈 바닥).

## 핵심 혁신

1. **캐시 불변성 설계**: 백본은 전문가 토큰에 주목하지 않으므로 캐시가 전문가 실행 상태와 분리된다. 이 설계는 빠른 시스템이 백본 재계산을 유발하지 않고 임의 주파수로 캐시를 읽을 수 있게 하며, 비동기 배포의 아키텍처 기반이다. 이전 fast-slow 설계는 이 속성을 명시적으로 활용하지 않았다.

2. **오래됨 증강 훈련**: 배포 시 캐시 지연을 훈련 분포의 일부로 명시적으로 모델링하고, 무작위 백본 접두사 마스킹을 통해 δ 틱의 지연을 시뮬레이션한다. 이는 빠른 시스템이 테스트 시 오래된 캐시를 마주해도 성능을 유지할 수 있게 하며, 폐루프에서 20 Hz 제어율을 가능하게 하는 핵심 훈련 전략이다.

3. **증분 캐시 유지**: 회전 위상을 활용하여 추가 전용 캐시가 정확하며, 매 K=4 틱의 증분 순방향 전파 비용은 이력 길이와 무관하다(폐루프 내 중앙값 10.7ms). 이는 기존 트랜스포머 추론 지연이 컨텍스트 길이에 따라 선형적으로 증가하는 병목을 깨고, 긴 이력 장면 집계를 가능하게 한다.

## 실험 및 결과

### 오픈루프 웨이포인트 정확도(표 1, 동기 δ=0 프로토콜)
| 구성 | L1 | 훈련 파라미터 |
|---|---|---|
| 백본 액션 헤드(동결) | 0.123 | — |
| 액션 전문가, δ=0만 | 0.037 | 337M |
| 액션 전문가, 무작위 δ(본 논문) | 0.031 | 337M |

### 폐루프 주행(표 2, LangAuto-Short town05, 32개 경로)
| 구성 | 제어율 | DS | RC | IS |
|---|---|---|---|---|
| LMDrive(틱 재생) | 10 Hz | 28.8 ± 0.8 | 37.0 ± 0.4 | 0.80 ± 0.04 |
| FastSlow-LMDrive, 프레임 스킵 | 10 Hz | 34.0 | 82.1 | 0.45 |
| FastSlow-LMDrive(본 논문) | 20 Hz | 32.9 ± 0.7 | 94.0 ± 2.6 | 0.37 ± 0.02 |

### 킬로미터당 위반(두 번 실행 평균)
- 기준선: 25.0회 경로 이탈, 2.9회 시간 초과; 본 논문: 4.3회 이탈, 0.08회 시간 초과.
- 킬로미터당 차량 충돌이 3.2에서 11.2로 증가; 레이아웃 충돌이 10.3에서 2.2로 감소; 차선 이탈이 7.9에서 1.1로 감소.

### 지연(표 3, 40프레임 이력, RTX 3090 Ti, 중앙값)
| 구성 요소 | 기존 | 본 논문 |
|---|---|---|
| 인식 + Q-Former | 26.9 매 단계 | 24.8 매 틱(29.2) |
| 백본 전체 재계산 | 61.6 매 단계 | 없음 |
| 증분 추가 | — | 21.1 매 K=4 틱(10.7) |
| 액션 전문가 | — | 7.5 매 틱(9.3) |
| 총 모델 계산 | 88.6 | 32.4 매 틱; 5.3 매 K=4 틱 상각 |

### 제로샷 도시 전이(표 4, 단일 실행)
- town01: LMDrive DS=20.5, RC=40.5, IS=0.56; 본 논문 DS=23.2, RC=84.3, IS=0.26.
- town02: LMDrive DS=11.6, RC=30.7, IS=0.38; 본 논문 DS=28.3, RC=94.4, IS=0.29.
- town02에서 주행 점수는 기준선의 2.4배, 완료율은 3.1배.

### 오래됨 증강 소거(동기 δ=0 프로토콜에서 에폭별 L1 검증)
- 무작위 δ 전문가 vs δ=0 쌍둥이: 0.060 vs 0.067, 0.049 vs 0.056, 0.037 vs 0.045, 수렴 시 0.031 vs 0.037.

## 경계 및 한계

- 본 연구는 시뮬레이션 연구로, 단일 도시(town05)의 짧은 경로에서만 훈련되었으며, 긴 경로에서의 위험 협상은 전이되지 않는다; 킬로미터당 차량 충돌은 완료율 상승에 따라 증가한다(표 내 수치 3.2→11.2로 계산).
- 저수준 제어기는 더 느린 기준선에 맞춰 조정된 게인을 상속받았으며 재조정되지 않아, 20 Hz 제어율의 잠재적 이점을 제한할 수 있다.
- 주요 비교는 구성당 두 번 실행이며, 프레임 스킵 소거와 전이 동작은 단일 실행으로, 실행 간 분산이 최대 1.6 DS로 관찰되었다.
- 주행 시스템은 시뮬레이션 벤치마크를 훨씬 넘는 안전 검증이 필요하며, 본 결과는 도로 준비 완료의 증거로 해석되어서는 안 된다.
- 하지 않은 일: 백본과 세계 모델 사전 훈련을 결합하여 캐시 인코딩 내용을 풍부하게 하지 않음; fast-slow 분기를 훈련 없는 안전 감독 트리거로 사용하지 않음; 긴 경로 훈련 세그먼트에서 훈련하지 않음(저자는 이를 자연스러운 다음 단계로 지적).

## 공학적 시사점

- **재현 우선 확인 사항**: 훈련 시 백본, 인식 인코더, Q-Former, 원본 헤드가 모두 동결되며 공개 LMDrive 체크포인트에서 초기화; 배치 크기 4에서 최대 28GB GPU 메모리 미만, 단일 48GB GPU로 훈련 가능. 추론 시 단일 RTX 3090 Ti로 폐루프가 가능하며, 벽시계 속도 약 17 Hz.
- **가장 쉽게 실수하는 지점**: 오래됨 증강 훈련에서 δ 샘플링 범위는 배포 시 K 값과 일치해야 한다(본 논문 K=4, δ_max는 4틱에 해당); 배포 시 캐시 지연이 훈련 분포를 초과하면 전문가 성능이 크게 저하될 수 있다. 골든 등가 테스트(웨이포인트 차이 < 4mm)는 캐시 유지 정확성의 일상적 검증으로 수행되어야 한다.
- **하위 팀 지침**: 새 장면으로 전이할 경우 긴 경로에서의 페널티 인자 붕괴에 주의하라(본 논문 town03에서 페널티 인자 0.04로 주행 점수 2.96이 기준선 5.98보다 낮음), 긴 경로 훈련 세그먼트에서 미세 조정을 권장; 저수준 PID 파라미터는 20 Hz 제어율에 맞춰 재조정해야 하며, 느린 기준선 파라미터를 그대로 사용하면 아키텍처 이점이 가려질 수 있다.
