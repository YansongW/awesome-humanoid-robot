---
$id: ent_paper_robottt_context_scaling_robot_policies_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboTTT: Context Scaling for Robot Policies'
  zh: 'RoboTTT: Context Scaling for Robot Policies'
  ko: 'RoboTTT: Context Scaling for Robot Policies'
summary:
  en: 'Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training
    Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders
    of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new
    robot capabilities: one-shot.'
  zh: RoboTTT 将测试时训练（TTT）的快速权重机制集成到预训练机器人基础模型 GR00T N1.7 中，使视觉-运动上下文长度扩展至 8K 时间步（约 5 分钟），比现有最先进策略高出三个数量级且不增加推理延迟。核心贡献在于首次证明上下文长度可作为机器人策略的独立扩展轴，并在长时程多阶段组装任务上显著超越单步与短上下文基线。
  ko: 'Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training
    Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders
    of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new
    robot capabilities: one-shot.'
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
- robottt
- context
- scaling
- robot
- policies
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
  title: 'arXiv:2607.15275 RoboTTT: Context Scaling for Robot Policies'
  url: https://arxiv.org/abs/2607.15275
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

RoboTTT 将测试时训练（TTT）的快速权重机制集成到预训练机器人基础模型 GR00T N1.7 中，使视觉-运动上下文长度扩展至 8K 时间步（约 5 分钟），比现有最先进策略高出三个数量级且不增加推理延迟。核心贡献在于首次证明上下文长度可作为机器人策略的独立扩展轴，并在长时程多阶段组装任务上显著超越单步与短上下文基线。

## 它改变了什么

机器人基础模型长期受限于单步或短历史上下文，这直接制约了从人类视频演示进行一次性模仿、从部署历史即时改进以及多阶段长时程任务的闭环性能。此前虽有 test-time training 工作，但均通过收集额外数据微调整个模型，而非在推理时动态更新参数。RoboTTT 真正改变了“上下文”在机器人策略中的角色——将历史压缩进快速权重空间，使策略在推理时持续学习，而非仅依赖固定权重的前向传播。这一转变将上下文长度从数百步量级提升至 8K 步，且不牺牲推理速度，为机器人策略开辟了类似 LLM 的上下文扩展路径。

## 方法拆解

### 快速权重更新机制
- 每个 TTT 层包含一个两层 MLP 快速模型，通过梯度下降更新：  
  `W_t ← W_{t-1} − η ∇_W L_FW(f_{W_{t-1}}(K_t), V_t)`，其中 `L_FW(v̂, v) = ‖v̂ − v‖²`，η 为可学习学习率（基础值 0.1）。
- 应用步骤为“先更新后应用”：`O_t = f_{W_t}(Q_t)`，训练与推理均执行此操作。

### 架构集成
- 在 GR00T N1.7 的 DiT 动作头 16 层中每层添加一个 TTT 层（每层约 10M 参数，总计 690M）。
- 输入序列为 `[R_1, Φ_1, q_1, Ã_1, …, R_T, Φ_T, q_T, Ã_T]`，其中 Φ_t 为 VLM 输出 token，q_t 为本体感觉 token，Ã_t 为加噪动作 token，R_t 为 N=16 个可学习寄存器 token。
- 关键设计：VL token Φ 不直接通过 TTT 层（计算效率考虑），由寄存器 token 跨时间携带 VL 信息。

### 训练稳定性设计
- **tanh 门控**：`O = tanh(α) ⊙ O_TTT + O_attn`，α 初始化为 0.001 以保留预训练能力。
- **序列动作强制**：为每个动作块独立采样噪声水平，避免全序列共享噪声导致训练不稳定。
- **截断 BPTT**：梯度仅在段内流动，快速权重跨段传递，GPU 内存由段长而非总序列长度决定。

### 上下文学习解耦
- 通过掩码选定时间步的流匹配损失，使这些步仅更新快速权重、不提供模仿目标，实现纯上下文学习。
- 视频演示模仿：人类视频序列仅更新快速权重，动作损失在配对机器人轨迹上计算。
- DAgger 蒸馏：快速权重在完整交互历史（含次优动作）上更新，但损失仅掩码到人类纠正，形成“失败为上下文、纠正为目标”的不对称蒸馏。

## 关键创新

1. **上下文长度作为新扩展轴**：首次系统证明扩展预训练上下文长度（至 8K 步）能稳定提升闭环性能，且仅在充分扩展后涌现长上下文条件能力，为机器人基础模型提供了类似 LLM 的 scaling 方向。
2. **快速权重实现测试时学习**：将 TTT 机制嵌入预训练策略，使模型在推理时通过梯度下降持续更新参数，而非静态前向传播，这是对现有 test-time training 范式的本质区别。
3. **上下文学习解耦与 DAgger 蒸馏**：通过掩码机制实现“纯上下文”与“模仿目标”的分离，并利用失败-纠正不对称性将人类干预高效蒸馏进快速权重，显著提升从次优数据中学习的能力。

## 实验与结果

### 主要结果（任务完成分数）
| 方法 | Pup Go Car | Circuit | Gear Bot | 平均 |
|------|------------|---------|----------|------|
| RoboTTT | 9/20 | 13/20 | 2/10 | 79% |
| GR00T N1.7 | 3/20 | 3/20 | 0/10 | 42% |
| GR00T N1.7 Hist. | 0/20 | 8/20 | 0/10 | 56% |
| GDN | 3/20 | 8/20 | 0/10 | 56% |

RoboTTT 平均 79%，比单步基线高 87%（由 42%→79% 计算），比最佳基线 GDN 高 41%（由 56%→79% 计算）。Gear Bot 任务中仅 RoboTTT 实现完全成功（2/10）。

### 上下文长度缩放
- 8K 上下文达 71.5%，比 1K 预训练（43.9%）高 63%（由 43.9%→71.5% 计算），比短上下文基线 GR00T N1.7 Hist.（45.6%）高 57%（由 45.6%→71.5% 计算）。

### 消融与鲁棒性
- TTT 线性变体比 MLP 快速模型差 27%；添加动作 token 带来 23% 相对改进；添加寄存器 token 带来 18% 相对改进。
- 扰动鲁棒性：屋顶扰动 RoboTTT 15/20 vs GR00T N1.7 10/20；轮胎扰动 RoboTTT 18/20 vs GR00T N1.7 11/20。
- DAgger 蒸馏：标准 DAgger 平均提升 9%（序列模型上 13%），DAgger 蒸馏平均提升 33%（RoboTTT 36%，GDN 29%）。

## 边界与局限

- 在 1K 上下文以下，RoboTTT 仍具竞争力但不如长上下文变体，作者归因于 rollout 水平超过训练上下文（1K 步约半分钟，短于最短任务片段），推理时快速权重更新远超训练所见窗口。
- 作者未声称短上下文下优于基线，仅强调充分扩展后的一致优势。
- 未在其他骨干架构上实例化（尽管声称兼容性广泛）；未解决 GDN 在长上下文下无缩放趋势的问题，仅提出假设性解释。
- 未进行超出 8K 时间步的实验，未探索饱和点；扩展训练上下文长度会增加训练成本。

## 工程启示

- **复现核对**：先确认预训练阶段仅微调新增序列建模层（TTT/GDN），冻结 GR00T N1.7 其他组件；后训练阶段再微调全部参数。预训练使用 WSD 调度（峰值学习率 2×10⁻⁵），后训练使用余弦调度（峰值学习率 5×10⁻⁵）。
- **最易踩坑**：序列动作强制（每个动作块独立采样噪声）是训练稳定的关键，若全序列共享噪声水平会导致训练发散；tanh 门控初始值 0.001 必须严格保持，否则破坏预训练能力。
- **资源规划**：预训练 30K 步需 16 块 GB200 GPU，4K 以上上下文时批大小降至每设备 1（全局 16）；后训练 20K 步用 8 块 GPU，上下文固定 1K。推理需 RTX 5090 级 GPU 维持 30 Hz 控制频率。
- **下游团队**：若任务时长超过 1 分钟，务必使用 8K 预训练上下文而非 1K；一次性模仿需配对人类视频与机器人轨迹，视频序列仅更新快速权重；DAgger 蒸馏时确保失败轨迹与人类纠正配对，不对称掩码是核心。

## Overview
Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new robot capabilities: one-shot in-context imitation from human video demonstrations, on-the-fly policy improvement, robustness to perturbations, and stronger performance on multi-stage, long-horizon tasks. We also observe, for the first time, steady gains in closed-loop performance as pretraining context length scales. At its core, RoboTTT integrates Test-Time Training into robot foundation models such as Vision-Language-Action policies, yielding a sequence model whose recurrent state consists of fast weights, parameters updated by gradient descent during both training and inference, compressing histories into weight space and retrieving contextual information for long-context conditioning. To scale training context length, the recipe combines sequence action forcing with truncated backpropagation through time. On challenging real-robot manipulation tasks, RoboTTT improves overall performance by 87% over the single-step context baseline and fully completes a five-minute, ten-stage assembly task, which no baseline ever does. RoboTTT trained with 8K-timestep context outperforms the same model pretrained with 1K timesteps by 62%, suggesting context length as a new scaling axis for robot foundation models. Videos are available at https://research.nvidia.com/labs/gear/robottt/

## 参考
- https://arxiv.org/abs/2607.15275

## 개요

RoboTTT는 테스트 시점 훈련(TTT)의 빠른 가중치 메커니즘을 사전 훈련된 로봇 기반 모델 GR00T N1.7에 통합하여, 시각-운동 컨텍스트 길이를 8K 타임스텝(약 5분)으로 확장합니다. 이는 기존 최첨단 정책보다 세 자릿수 이상 높은 수치이며 추론 지연 시간은 증가하지 않습니다. 핵심 기여는 컨텍스트 길이가 로봇 정책의 독립적인 확장 축이 될 수 있음을 처음으로 증명하고, 장기 다단계 조립 작업에서 단일 스텝 및 짧은 컨텍스트 기준선을 크게 능가한다는 점입니다.

## 무엇을 바꾸는가

로봇 기반 모델은 오랫동안 단일 스텝 또는 짧은 히스토리 컨텍스트에 제한되어 왔으며, 이는 인간 비디오 시연으로부터의 일회성 모방, 배포 히스토리로부터의 즉각적인 개선, 다단계 장기 작업의 폐루프 성능을 직접적으로 제약했습니다. 이전에도 테스트 시점 훈련 작업이 있었지만, 모두 추가 데이터를 수집하여 전체 모델을 미세 조정하는 방식이었고 추론 시 매개변수를 동적으로 업데이트하지는 않았습니다. RoboTTT는 로봇 정책에서 '컨텍스트'의 역할을 진정으로 바꿉니다. 즉, 히스토리를 빠른 가중치 공간으로 압축하여 정책이 추론 시 지속적으로 학습하도록 하며, 고정 가중치의 순방향 전파에만 의존하지 않습니다. 이러한 전환은 컨텍스트 길이를 수백 스텝 수준에서 8K 스텝으로 끌어올리면서도 추론 속도를 희생하지 않아, 로봇 정책에 LLM과 유사한 컨텍스트 확장 경로를 열어줍니다.

## 방법 분석

### 빠른 가중치 업데이트 메커니즘
- 각 TTT 레이어는 2계층 MLP 빠른 모델을 포함하며, 경사 하강법으로 업데이트됩니다:  
  `W_t ← W_{t-1} − η ∇_W L_FW(f_{W_{t-1}}(K_t), V_t)`, 여기서 `L_FW(v̂, v) = ‖v̂ − v‖²`, η는 학습 가능한 학습률(기본값 0.1)입니다.
- 적용 단계는 '먼저 업데이트 후 적용'입니다: `O_t = f_{W_t}(Q_t)`, 훈련과 추론 모두에서 이 작업을 수행합니다.

### 아키텍처 통합
- GR00T N1.7의 DiT 액션 헤드 16개 레이어 각각에 TTT 레이어를 추가합니다(각 레이어 약 10M 매개변수, 총 690M).
- 입력 시퀀스는 `[R_1, Φ_1, q_1, Ã_1, …, R_T, Φ_T, q_T, Ã_T]`이며, 여기서 Φ_t는 VLM 출력 토큰, q_t는 고유 감각 토큰, Ã_t는 노이즈가 추가된 액션 토큰, R_t는 N=16개의 학습 가능한 레지스터 토큰입니다.
- 핵심 설계: VL 토큰 Φ는 TTT 레이어를 직접 통과하지 않으며(계산 효율성 고려), 레지스터 토큰이 시간에 걸쳐 VL 정보를 전달합니다.

### 훈련 안정성 설계
- **tanh 게이팅**: `O = tanh(α) ⊙ O_TTT + O_attn`, α는 0.001로 초기화되어 사전 훈련 능력을 보존합니다.
- **시퀀스 액션 강제**: 각 액션 블록에 대해 독립적으로 노이즈 수준을 샘플링하여, 전체 시퀀스가 노이즈를 공유하여 훈련이 불안정해지는 것을 방지합니다.
- **절단된 BPTT**: 경사는 세그먼트 내에서만 흐르고, 빠른 가중치는 세그먼트 간에 전달되며, GPU 메모리는 총 시퀀스 길이가 아닌 세그먼트 길이에 의해 결정됩니다.

### 컨텍스트 학습 분리
- 선택된 타임스텝의 흐름 매칭 손실을 마스킹하여, 해당 스텝은 빠른 가중치만 업데이트하고 모방 목표는 제공하지 않아 순수 컨텍스트 학습을 구현합니다.
- 비디오 시연 모방: 인간 비디오 시퀀스는 빠른 가중치만 업데이트하고, 액션 손실은 짝지어진 로봇 궤적에서 계산됩니다.
- DAgger 증류: 빠른 가중치는 전체 상호작용 히스토리(차선 액션 포함)에서 업데이트되지만, 손실은 인간 교정에만 마스킹되어 '실패는 컨텍스트, 교정은 목표'라는 비대칭 증류를 형성합니다.

## 핵심 혁신

1. **컨텍스트 길이를 새로운 확장 축으로**: 처음으로 사전 훈련된 컨텍스트 길이(8K 스텝까지)를 확장하면 폐루프 성능이 안정적으로 향상되고, 충분히 확장된 후에만 장기 컨텍스트 조건 능력이 출현함을 체계적으로 증명하여 로봇 기반 모델에 LLM과 유사한 스케일링 방향을 제공합니다.
2. **빠른 가중치로 테스트 시점 학습 구현**: TTT 메커니즘을 사전 훈련된 정책에 내장하여 모델이 추론 시 경사 하강법으로 매개변수를 지속적으로 업데이트하도록 하며, 정적 순방향 전파가 아닌 방식으로 기존 테스트 시점 훈련 패러다임과 본질적으로 구별됩니다.
3. **컨텍스트 학습 분리 및 DAgger 증류**: 마스킹 메커니즘을 통해 '순수 컨텍스트'와 '모방 목표'를 분리하고, 실패-교정 비대칭성을 활용하여 인간 개입을 빠른 가중치로 효율적으로 증류하여 차선 데이터에서 학습하는 능력을 크게 향상시킵니다.

## 실험 및 결과

### 주요 결과(작업 완료 점수)
| 방법 | Pup Go Car | Circuit | Gear Bot | 평균 |
|------|------------|---------|----------|------|
| RoboTTT | 9/20 | 13/20 | 2/10 | 79% |
| GR00T N1.7 | 3/20 | 3/20 | 0/10 | 42% |
| GR00T N1.7 Hist. | 0/20 | 8/20 | 0/10 | 56% |
| GDN | 3/20 | 8/20 | 0/10 | 56% |

RoboTTT 평균 79%로, 단일 스텝 기준선보다 87% 높고(42%→79% 계산), 최고 기준선 GDN보다 41% 높습니다(56%→79% 계산). Gear Bot 작업에서는 RoboTTT만 완전 성공을 달성했습니다(2/10).

### 컨텍스트 길이 스케일링
- 8K 컨텍스트는 71.5%로, 1K 사전 훈련(43.9%)보다 63% 높고(43.9%→71.5% 계산), 짧은 컨텍스트 기준선 GR00T N1.7 Hist.(45.6%)보다 57% 높습니다(45.6%→71.5% 계산).

### 절제 및 견고성
- TTT 선형 변형은 MLP 빠른 모델보다 27% 낮음; 액션 토큰 추가는 23% 상대적 개선; 레지스터 토큰 추가는 18% 상대적 개선.
- 교란 견고성: 지붕 교란 RoboTTT 15/20 vs GR00T N1.7 10/20; 타이어 교란 RoboTTT 18/20 vs GR00T N1.7 11/20.
- DAgger 증류: 표준 DAgger 평균 9% 향상(시퀀스 모델에서 13%), DAgger 증류 평균 33% 향상(RoboTTT 36%, GDN 29%).

## 경계 및 한계

- 1K 컨텍스트 미만에서는 RoboTTT가 여전히 경쟁력이 있지만 장기 컨텍스트 변형보다는 낮으며, 저자는 롤아웃 수준이 훈련 컨텍스트(1K 스텝 약 30초, 최단 작업 세그먼트보다 짧음)를 초과하고, 추론 시 빠른 가중치 업데이트가 훈련에서 본 창을 훨씬 초과하기 때문이라고 설명합니다.
- 저자는 짧은 컨텍스트에서 기준선보다 우수하다고 주장하지 않으며, 충분히 확장된 후의 일관된 우위만 강조합니다.
- 다른 백본 아키텍처에서는 인스턴스화되지 않았습니다(광범위한 호환성 주장에도 불구하고); GDN이 장기 컨텍스트에서 스케일링 추세가 없는 문제를 해결하지 못했으며, 가설적 설명만 제시합니다.
- 8K 타임스텝을 초과하는 실험은 수행되지 않았고, 포화 지점을 탐색하지 않았습니다; 훈련 컨텍스트 길이를 확장하면 훈련 비용이 증가합니다.

## 엔지니어링 시사점

- **재현 확인**: 먼저 사전 훈련 단계에서 새로 추가된 시퀀스 모델링 레이어(TTT/GDN)만 미세 조정하고 GR00T N1.7의 다른 구성 요소는 동결하는지 확인; 후훈련 단계에서 전체 매개변수를 미세 조정합니다. 사전 훈련은 WSD 스케줄(피크 학습률 2×10⁻⁵), 후훈련은 코사인 스케줄(피크 학습률 5×10⁻⁵)을 사용합니다.
- **가장 흔한 함정**: 시퀀스 액션 강제(각 액션 블록에 대해 독립적으로 노이즈 샘플링)가 훈련 안정성의 핵심이며, 전체 시퀀스가 노이즈 수준을 공유하면 훈련이 발산합니다; tanh 게이팅 초기값 0.001은 엄격히 유지해야 하며, 그렇지 않으면 사전 훈련 능력이 손상됩니다.
- **리소스 계획**: 사전 훈련 30K 스텝에는 16개의 GB200 GPU가 필요하며, 4K 이상의 컨텍스트에서는 배치 크기가 장치당 1(전역 16)로 감소합니다; 후훈련 20K 스텝은 8개 GPU, 컨텍스트는 1K로 고정됩니다. 추론에는 RTX 5090급 GPU가 필요하여 30Hz 제어 주파수를 유지합니다.
- **하위 팀**: 작업 시간이 1분을 초과하면 반드시 1K가 아닌 8K 사전 훈련 컨텍스트를 사용하세요; 일회성 모방은 인간 비디오와 로봇 궤적의 짝지음이 필요하며, 비디오 시퀀스는 빠른 가중치만 업데이트합니다; DAgger 증류 시 실패 궤적과 인간 교정이 짝지어져 있는지 확인하고, 비대칭 마스킹이 핵심입니다.
