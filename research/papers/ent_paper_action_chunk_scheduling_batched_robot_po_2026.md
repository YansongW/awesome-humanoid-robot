---
$id: ent_paper_action_chunk_scheduling_batched_robot_po_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Action Chunk Scheduling for Batched Robot Policy Serving
  zh: Action Chunk Scheduling for Batched Robot Policy Serving
  ko: Action Chunk Scheduling for Batched Robot Policy Serving
summary:
  en: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots.
    However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute
    is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots
    from a remote GPU and formulate it as a.
  zh: Armory 是一个面向多机器人共享云端 GPU 推理的批处理调度系统，由 Georgia Tech 团队提出。它将批量策略服务形式化为闭环马尔可夫决策过程（MDP），并实现了一个基于前瞻（Lookahead）的调度器，在异构车队中按任务紧迫性动态分配
    GPU 批次，而非简单追求最大批处理量。核心贡献在于首次将“饥饿率”和“下游执行成本”纳入调度目标，并通过模拟与真实 10 臂实验验证了其在动态任务场景下的吞吐量优势。
  ko: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots.
    However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute
    is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots
    from a remote GPU and formulate it as a.
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
- action
- chunk
- scheduling
- batched
- robot
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
  title: arXiv:2608.00337 Action Chunk Scheduling for Batched Robot Policy Serving
  url: https://arxiv.org/abs/2608.00337
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

Armory 是一个面向多机器人共享云端 GPU 推理的批处理调度系统，由 Georgia Tech 团队提出。它将批量策略服务形式化为闭环马尔可夫决策过程（MDP），并实现了一个基于前瞻（Lookahead）的调度器，在异构车队中按任务紧迫性动态分配 GPU 批次，而非简单追求最大批处理量。核心贡献在于首次将“饥饿率”和“下游执行成本”纳入调度目标，并通过模拟与真实 10 臂实验验证了其在动态任务场景下的吞吐量优势。

## 它改变了什么

现有机器人策略服务系统（如 Kairos、ROSA）要么假设单机器人，要么在批处理时忽略延迟对闭环行为的反馈效应。它们把 GPU 利用率当作首要优化目标，默认“批次越大越好”，却未意识到：推理延迟随批次大小非线性增长（L40S 上 batch 5 需 211 ms vs batch 1 需 73 ms），被排除在批次外的机器人会因动作过期而“饥饿”，进而产生抖动或停滞。这本质上是把静态批处理调度问题错当成了吞吐量优化问题，而非闭环控制问题。

Armory 真正改变的是调度目标函数：它不再最大化 GPU 吞吐，而是最大化“单位时间内被执行的有效机器人动作数”，并显式建模动作块队列、执行周期和网络延迟对饥饿的影响。这使得调度器可以在“多批几个机器人摊薄成本”与“让急迫任务先跑”之间做有原则的权衡，而非依赖启发式。对异构车队（如动态转盘分拣与静态分拣混跑）而言，这是从“一刀切”到“按需分配”的范式转变。

## 方法拆解

### 问题建模
将批量策略服务建模为 MDP，状态 \( s_k = (t_k, i_j, \hat{i}_j, \mathcal{Q}_j) \)：
- \( t_k \)：调度周期开始时间
- \( i_j \)：机器人 j 最新执行的动作索引
- \( \hat{i}_j \)：服务器收到的最新动作索引
- \( \mathcal{Q}_j \)：动作块队列（每个块 \( c = (i_{\text{start}}, h_j, t_{\text{arr}}) \)）

### 转移与奖励
- 推理完成时间：\( t_{k+1} = t_k + \tilde{d}_{\text{infer}}(|B_k|) \)，其中 \( \tilde{d}_{\text{infer}} \) 是批次大小的延迟函数（启动时 profiling 获得）
- 新动作块：\( c_{\text{new}}^j = (\hat{i}_j, h_j, t_{k+1} + \tilde{d}_{\text{action},j}) \)
- 每周期奖励：\( R(s_k, B_k) = \frac{1}{f_c} \sum_{j=1}^{N} w_j \Delta i_j(s_k, B_k) \)，\( w_j \) 为任务权重，\( \Delta i_j \) 为该周期内机器人 j 实际执行的动作数

### Lookahead 调度器
精确规划不可行，采用有限深度前瞻：
1. 枚举未来 L 个周期的所有潜在批次组合（大小 1 到 \( B_{\text{max}} \)）
2. 对每个候选调度 S，模拟前滚并计算得分 \( \text{Score}(S) = \sum_{\ell=0}^{L-1} \frac{R(s_\ell, B_\ell)}{d_{\text{infer}}(|B_\ell|)} \)
3. 选择得分最高的调度的第一个批次执行

### 关键设计决策
- **L=1 足够**：作者发现单步前瞻已能实现异构感知，更深搜索（L=2,3）反而略微增加饥饿率（见实验）
- **保守调度**：GPU 空闲且有请求时立即调度，不等待凑满批次
- **推式通信**：机器人发送观测后才执行动作，避免拉式架构中的过期观测
- **进程隔离**：网络处理、调度、GPU 推理分离为独立进程，通过共享内存通信，CPU 工作不阻塞 GPU

## 关键创新

1. **闭环调度公式化**：首次将“饥饿率”作为显式优化目标纳入批处理调度，而非仅关注 GPU 利用率。这使调度器能感知动作块队列的消耗速度，对动态任务（短执行周期）和静态任务（长执行周期）做差异化处理。

2. **前瞻搜索替代贪心启发式**：EDF 只关注“谁最急”，RR 只关注“公平”，两者都未建模当前批次选择对未来状态的影响。Lookahead 通过模拟前滚，显式评估“这次多批一个机器人”对后续周期饥饿率的代价，从而在摊销与延迟之间找到平衡点。

3. **权重机制实现异构感知**：通过任务权重 \( w_j \)（如快速机器人 \( w_j=5 \)），调度器可在不牺牲慢速任务吞吐的前提下，将快速层吞吐提升 4 倍（vs RR）和 2 倍（vs EDF）。这是对“统一处理”假设的直接挑战，证明优先级调度在真实机器人车队中的价值。

## 实验与结果

### 模拟实验（LIBERO 基准）
- 配置：\( \pi_{0.5} \) 模型，\( H=10 \), \( f_c=20 \)，快速机器人 \( H_{\text{max}}=6 \)，慢速 \( H_{\text{max}}=10 \)，车队规模 2–10，3 个种子
- 关键结果（one-fast 配置，N=10）：

| 调度器 | 快速层吞吐 | 慢速层吞吐 | 系统饥饿率 |
|--------|-----------|-----------|-----------|
| RR     | 低        | 9.04      | 12.90%    |
| EDF    | 中        | 8.81      | 13.37%    |
| LA@5   | 高（约 2×EDF） | 10.04 | 15.18%    |

### 真实世界（10 个 AgileX PiPER 手臂）
- 配置：\( H=20 \), \( f_c=30 \)，快速 \( H_{\text{max}}=10 \)，慢速 \( H_{\text{max}}=20 \)，动态转盘分拣 vs 静态分拣
- one-fast 设置：LA@5 将快速层吞吐提升至 8.33 件/分（EDF 为 3.67，RR 为 2.00），系统总吞吐 98.67 vs EDF 83.00（提升约 18%）

### 批处理大小消融
- all-fast 场景，cap=10 时：EDF/RR 平均批次 4.7 机器人/调用，Lookahead 平均 3.3、中位数 3
- naive 调度器随 cap 增长过度批处理导致饥饿率上升，Lookahead 对 cap 不敏感

### 网络鲁棒性
- 中位延迟 50 ms 时扫描抖动 σ，三种调度器性能几乎平坦
- 中位延迟从 25 ms 扫到 500 ms，50–100 ms 内性能保持高，超过后所有调度器以相同方式退化

## 边界与局限

- **推理模型假设简单**：仅考虑单 GPU 上的批处理，未实现连续批处理、PagedAttention、分块预填充等优化，也未做分布式推理。这些技术可能改变延迟-批次大小曲线，进而影响调度策略的最优性。
- **L=1 的局限**：虽然作者发现单步前瞻足够，但更深搜索（L=2,3）在部分配置下略微增加饥饿率，这与直觉相反，可能特定于其搜索实现和奖励函数。
- **异步策略混淆**：使用 naive async 作为动作 chunking 策略，其本身可能产生抖动运动。Lookahead 偏向从 chunk 起始执行，无意中减少了这种抖动，若改用 RTC 或 VLASH 等更复杂策略，结果可能不同。
- **网络延迟补偿上限**：调度策略无法补偿原始传输延迟，超过 50 ms 后所有调度器以相同方式退化，仅作为更强的饥饿信号。
- **样本量有限**：真实世界仅 1 分钟 rollout、3 个种子，指标可能有噪声。

## 工程启示

- **先核对延迟-批次曲线**：Armory 的有效性高度依赖 \( \tilde{d}_{\text{infer}}(|B|) \) 的准确性。部署前务必在目标 GPU 上 profiling 每个批次大小的延迟（如 L40S 上 batch 1 为 73 ms，batch 5 为 211 ms），若曲线平坦（如 H100），调度收益会缩小。
- **权重设置是关键超参**：\( w_j \) 直接控制优先级倾斜程度。模拟中 half-fast 配置下 LA@5 导致慢速层吞吐崩溃（20.83 vs RR 35.88），说明激进权重可能适得其反。建议从 \( w_j=1 \) 开始，逐步增加并监控慢速层饥饿率。
- **批次上限 b 的选择**：仿真中 b=3 是 naive 调度器最强配置，但 Lookahead 对 b 不敏感。实际部署时可将 b 设大（如 5），依赖调度器自行决定实际批次大小，而非手动限制。
- **网络延迟是硬约束**：若单向延迟超过 50 ms，调度策略无法补偿，应优先考虑边缘计算或模型压缩，而非优化调度。
- **最容易踩坑**：直接复用 naive async 作为动作执行策略会引入抖动，且与调度器行为耦合。建议在评估调度器时，同时评估动作 chunking 策略（如从 chunk 起始执行 vs 从中间执行）的影响。

## Overview
Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots from a remote GPU and formulate it as a scheduling problem. We build Armory, a serving system validated on fleets of both simulated and real robots. Our experiments show that naive scheduling heuristics perform well when all robots are the same, but fall short when robots consume action chunks at different rates, uncovering a mismatch between conventional batching methods and the closed-loop requirements of robot policy execution. To address this, we propose a scheduling algorithm that accounts for this heterogeneity and improves overall system throughput by up to $18\%$ in real-world experiments. Additional details are available at https://gatech-rl2.github.io/actionchunkscheduling.

## 参考
- https://arxiv.org/abs/2608.00337

## 개요

Armory는 Georgia Tech 팀이 제안한 다중 로봇 공유 클라우드 GPU 추론을 위한 배치 스케줄링 시스템입니다. 이 시스템은 배치 정책 서비스를 폐루프 마르코프 결정 과정(MDP)으로 공식화하고, 선견(Lookahead) 기반 스케줄러를 구현하여 이기종 로봇 군집에서 작업 긴급성에 따라 GPU 배치를 동적으로 할당하며, 단순히 최대 배치 처리량만 추구하지 않습니다. 핵심 기여는 처음으로 '기아율'과 '다운스트림 실행 비용'을 스케줄링 목표에 포함시킨 것이며, 시뮬레이션과 실제 10-암 실험을 통해 동적 작업 시나리오에서의 처리량 우위를 검증했습니다.

## 무엇을 바꾸었는가

기존 로봇 정책 서비스 시스템(예: Kairos, ROSA)은 단일 로봇을 가정하거나, 배치 처리 시 지연이 폐루프 동작에 미치는 피드백 효과를 무시합니다. 이들은 GPU 활용률을 최우선 최적화 목표로 삼고 '배치가 클수록 좋다'고 기본 가정하지만, 추론 지연이 배치 크기에 따라 비선형적으로 증가한다는 점(L40S에서 batch 5는 211ms, batch 1은 73ms)을 인식하지 못합니다. 배치에서 제외된 로봇은 동작이 만료되어 '기아' 상태가 되고, 이로 인해 떨림이나 정체가 발생합니다. 이는 본질적으로 정적 배치 스케줄링 문제를 처리량 최적화 문제로 오인한 것이지, 폐루프 제어 문제로 보지 않은 것입니다.

Armory가 실제로 바꾼 것은 스케줄링 목표 함수입니다. 더 이상 GPU 처리량을 최대화하지 않고 '단위 시간당 실행되는 유효 로봇 동작 수'를 최대화하며, 동작 청크 큐, 실행 주기, 네트워크 지연이 기아에 미치는 영향을 명시적으로 모델링합니다. 이를 통해 스케줄러는 '여러 로봇을 배치하여 비용을 분산'하는 것과 '긴급한 작업을 먼저 실행'하는 것 사이에서 휴리스틱에 의존하지 않고 원칙적인 절충을 할 수 있습니다. 이기종 로봇 군집(예: 동적 턴테이블 분류와 정적 분류 혼합)에게 이는 '일괄 적용'에서 '수요 기반 할당'으로의 패러다임 전환입니다.

## 방법 분석

### 문제 모델링
배치 정책 서비스를 MDP로 모델링하며, 상태 \( s_k = (t_k, i_j, \hat{i}_j, \mathcal{Q}_j) \):
- \( t_k \): 스케줄링 주기 시작 시간
- \( i_j \): 로봇 j가 가장 최근에 실행한 동작 인덱스
- \( \hat{i}_j \): 서버가 수신한 가장 최근 동작 인덱스
- \( \mathcal{Q}_j \): 동작 청크 큐 (각 청크 \( c = (i_{\text{start}}, h_j, t_{\text{arr}}) \))

### 전이와 보상
- 추론 완료 시간: \( t_{k+1} = t_k + \tilde{d}_{\text{infer}}(|B_k|) \), 여기서 \( \tilde{d}_{\text{infer}} \)는 배치 크기의 지연 함수(시작 시 프로파일링으로 획득)
- 새 동작 청크: \( c_{\text{new}}^j = (\hat{i}_j, h_j, t_{k+1} + \tilde{d}_{\text{action},j}) \)
- 주기별 보상: \( R(s_k, B_k) = \frac{1}{f_c} \sum_{j=1}^{N} w_j \Delta i_j(s_k, B_k) \), \( w_j \)는 작업 가중치, \( \Delta i_j \)는 해당 주기 내 로봇 j가 실제로 실행한 동작 수

### Lookahead 스케줄러
정확한 계획은 불가능하므로 유한 깊이 선견을 채택:
1. 향후 L개 주기의 모든 잠재적 배치 조합(크기 1부터 \( B_{\text{max}} \)까지)을 열거
2. 각 후보 스케줄 S에 대해 시뮬레이션 전진 실행 후 점수 계산 \( \text{Score}(S) = \sum_{\ell=0}^{L-1} \frac{R(s_\ell, B_\ell)}{d_{\text{infer}}(|B_\ell|)} \)
3. 가장 높은 점수를 얻은 스케줄의 첫 번째 배치를 실행

### 핵심 설계 결정
- **L=1로 충분**: 저자는 단일 단계 선견만으로 이기종 인식이 가능하며, 더 깊은 탐색(L=2,3)은 오히려 기아율을 약간 증가시킨다고 발견(실험 참조)
- **보수적 스케줄링**: GPU가 유휴 상태이고 요청이 있을 때 즉시 스케줄링하며, 배치를 채우기 위해 대기하지 않음
- **푸시 통신**: 로봇이 관측을 전송한 후에만 동작을 실행하여 풀 아키텍처의 만료된 관측을 방지
- **프로세스 격리**: 네트워크 처리, 스케줄링, GPU 추론을 별도의 프로세스로 분리하고 공유 메모리로 통신하여 CPU 작업이 GPU를 차단하지 않음

## 핵심 혁신

1. **폐루프 스케줄링 공식화**: 처음으로 '기아율'을 명시적 최적화 목표로 배치 스케줄링에 포함시켰으며, GPU 활용률만 고려하지 않습니다. 이를 통해 스케줄러가 동작 청크 큐의 소비 속도를 인식하고, 동적 작업(짧은 실행 주기)과 정적 작업(긴 실행 주기)을 차별화할 수 있습니다.

2. **선견 탐색으로 탐욕 휴리스틱 대체**: EDF는 '누가 가장 긴급한가'만, RR은 '공정성'만 고려하며, 둘 다 현재 배치 선택이 미래 상태에 미치는 영향을 모델링하지 않습니다. Lookahead는 시뮬레이션 전진 실행을 통해 '이번에 로봇 하나를 더 배치하는 것'이 후속 주기 기아율에 미치는 비용을 명시적으로 평가하여, 분산과 지연 사이의 균형점을 찾습니다.

3. **가중치 메커니즘으로 이기종 인식 구현**: 작업 가중치 \( w_j \)(예: 빠른 로봇 \( w_j=5 \))를 통해 스케줄러는 느린 작업의 처리량을 희생하지 않으면서 빠른 계층의 처리량을 4배(RR 대비) 및 2배(EDF 대비) 향상시킬 수 있습니다. 이는 '균일 처리' 가정에 대한 직접적인 도전이며, 실제 로봇 군집에서 우선순위 스케줄링의 가치를 증명합니다.

## 실험과 결과

### 시뮬레이션 실험 (LIBERO 벤치마크)
- 구성: \( \pi_{0.5} \) 모델, \( H=10 \), \( f_c=20 \), 빠른 로봇 \( H_{\text{max}}=6 \), 느린 로봇 \( H_{\text{max}}=10 \), 로봇 군집 규모 2–10, 3개 시드
- 주요 결과 (one-fast 구성, N=10):

| 스케줄러 | 빠른 계층 처리량 | 느린 계층 처리량 | 시스템 기아율 |
|--------|-----------|-----------|-----------|
| RR     | 낮음        | 9.04      | 12.90%    |
| EDF    | 중간        | 8.81      | 13.37%    |
| LA@5   | 높음 (약 2×EDF) | 10.04 | 15.18%    |

### 실제 세계 (10개 AgileX PiPER 암)
- 구성: \( H=20 \), \( f_c=30 \), 빠른 \( H_{\text{max}}=10 \), 느린 \( H_{\text{max}}=20 \), 동적 턴테이블 분류 vs 정적 분류
- one-fast 설정: LA@5는 빠른 계층 처리량을 8.33개/분으로 향상(EDF는 3.67, RR은 2.00), 시스템 총 처리량 98.67 vs EDF 83.00(약 18% 향상)

### 배치 크기 절제 실험
- all-fast 시나리오, cap=10일 때: EDF/RR 평균 배치 4.7 로봇/호출, Lookahead 평균 3.3, 중앙값 3
- naive 스케줄러는 cap이 증가함에 따라 과도한 배치로 기아율이 상승하지만, Lookahead는 cap에 둔감

### 네트워크 견고성
- 중앙 지연 50ms에서 지터 σ를 스캔할 때, 세 스케줄러 성능은 거의 평탄
- 중앙 지연을 25ms에서 500ms로 스캔할 때, 50–100ms 내에서 성능이 높게 유지되며, 그 이후 모든 스케줄러가 동일한 방식으로 저하

## 경계와 한계

- **추론 모델 가정 단순**: 단일 GPU에서의 배치만 고려하며, 연속 배치, PagedAttention, 청크 프리필 등의 최적화나 분산 추론을 구현하지 않았습니다. 이러한 기술은 지연-배치 크기 곡선을 변경하여 스케줄링 전략의 최적성에 영향을 줄 수 있습니다.
- **L=1의 한계**: 저자는 단일 단계 선견이 충분하다고 발견했지만, 더 깊은 탐색(L=2,3)은 일부 구성에서 기아율을 약간 증가시키며, 이는 직관에 반하며 특정 탐색 구현과 보상 함수에 국한될 수 있습니다.
- **비동기 정책 혼동**: naive async를 동작 청킹 전략으로 사용하며, 이 자체가 떨림 동작을 생성할 수 있습니다. Lookahead는 청크 시작부터 실행하는 것을 선호하여 이러한 떨림을 의도치 않게 줄이지만, RTC나 VLASH 같은 더 복잡한 전략을 사용하면 결과가 달라질 수 있습니다.
- **네트워크 지연 보상 상한**: 스케줄링 전략은 원시 전송 지연을 보상할 수 없으며, 50ms를 초과하면 모든 스케줄러가 동일한 방식으로 저하되어 더 강한 기아 신호로만 작용합니다.
- **표본 크기 제한**: 실제 세계는 1분 rollout, 3개 시드뿐이며, 지표에 노이즈가 있을 수 있습니다.

## 공학적 시사점

- **지연-배치 곡선 먼저 확인**: Armory의 효과성은 \( \tilde{d}_{\text{infer}}(|B|) \)의 정확성에 크게 의존합니다. 배포 전에 반드시 대상 GPU에서 각 배치 크기의 지연을 프로파일링하세요(예: L40S에서 batch 1은 73ms, batch 5는 211ms). 곡선이 평탄하면(예: H100) 스케줄링 이점이 줄어듭니다.
- **가중치 설정이 핵심 하이퍼파라미터**: \( w_j \)는 우선순위 기울기 정도를 직접 제어합니다. 시뮬레이션에서 half-fast 구성에서 LA@5는 느린 계층 처리량을 붕괴시켰으며(20.83 vs RR 35.88), 이는 공격적인 가중치가 역효과를 낼 수 있음을 시사합니다. \( w_j=1 \)에서 시작하여 점진적으로 증가시키고 느린 계층 기아율을 모니터링하는 것을 권장합니다.
- **배치 상한 b 선택**: 시뮬레이션에서 b=3은 naive 스케줄러의 가장 강력한 구성이지만, Lookahead는 b에 둔감합니다. 실제 배포 시 b를 크게(예: 5) 설정하고 수동 제한 대신 스케줄러가 실제 배치 크기를 결정하도록 하는 것이 좋습니다.
- **네트워크 지연은 하드 제약**: 단방향 지연이 50ms를 초과하면 스케줄링 전략으로 보상할 수 없으며, 스케줄링 최적화보다 엣지 컴퓨팅이나 모델 압축을 우선 고려해야 합니다.
- **가장 흔한 함정**: naive async를 동작 실행 전략으로 직접 재사용하면 떨림이 발생하고 스케줄러 동작과 결합됩니다. 스케줄러를 평가할 때 동작 청킹 전략(예: 청크 시작부터 실행 vs 중간부터 실행)의 영향도 함께 평가하는 것을 권장합니다.
