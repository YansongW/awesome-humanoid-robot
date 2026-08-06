---
$id: ent_paper_imbench_benchmark_intuitive_robotic_mani_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IMBench: A Benchmark for Intuitive Robotic Manipulation'
  zh: 'IMBench: A Benchmark for Intuitive Robotic Manipulation'
  ko: 'IMBench: A Benchmark for Intuitive Robotic Manipulation'
summary:
  en: 'Humans combine reasoning and motor control to solve complex manipulation tasks under diverse constraints. They build
    an understanding of the physical world that helps them convert reasoning into actions and quickly adapt to new scenes,
    tasks, and rules. We refer to this capability as intuitive manipulation. Existing benchmarks fail to capture this integration:
    they evaluate physical reasoning in.'
  zh: IMBench 是一个面向“直觉操作”的仿真基准，由研究团队构建，包含 35 个基于 robosuite 的任务，旨在将物理推理、动作提议与低级执行作为集成能力进行端到端评估。核心贡献在于揭示了当前视觉-语言-动作模型（VLA）与基础模型在物理约束提取与闭环执行上的显著短板，并提供了分阶段（理解、规划、执行）的细粒度诊断工具。
  ko: 'Humans combine reasoning and motor control to solve complex manipulation tasks under diverse constraints. They build
    an understanding of the physical world that helps them convert reasoning into actions and quickly adapt to new scenes,
    tasks, and rules. We refer to this capability as intuitive manipulation. Existing benchmarks fail to capture this integration:
    they evaluate physical reasoning in.'
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
- imbench
- benchmark
- intuitive
- robotic
- mani
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
  title: 'arXiv:2607.15641 IMBench: A Benchmark for Intuitive Robotic Manipulation'
  url: https://arxiv.org/abs/2607.15641
  date: '2026-07-17'
  accessed_at: '2026-08-05'
---

## 概述

IMBench 是一个面向“直觉操作”的仿真基准，由研究团队构建，包含 35 个基于 robosuite 的任务，旨在将物理推理、动作提议与低级执行作为集成能力进行端到端评估。核心贡献在于揭示了当前视觉-语言-动作模型（VLA）与基础模型在物理约束提取与闭环执行上的显著短板，并提供了分阶段（理解、规划、执行）的细粒度诊断工具。

## 它改变了什么

现有机器人操作基准存在一个根本性割裂：物理推理基准（如 PhysBench）止步于“想”，操作基准（如 LIBERO）只考核“做”，而真实世界的灵巧操作恰恰要求两者无缝耦合。IMBench 真正改变的是评估范式——它不再问“策略能否完成动作序列”，而是问“系统能否从观测中推断出隐藏的物理约束，并将该推断转化为可执行且鲁棒的动作”。这一转向将评估焦点从感知-运动映射的统计拟合，拉回到对物理世界因果结构的主动建模与利用。

作者敏锐地指出，当前 VLA 模型在物体身份和场景布局上泛化良好，但一旦任务结构本身需要物理推理（如薄板需先滑动再抓取），性能便急剧下降。IMBench 通过设计“推理瓶颈”任务，迫使系统显式处理不可行性、几何、动力学、因果性、隐藏状态与稳定性等物理事实，从而定位了现有模型能力图谱中缺失的关键轴——这比单纯追求更高成功率更有诊断价值。

## 方法拆解

IMBench 的构建遵循“能力分解、任务隔离、流程贯通”的原则，其方法拆解如下：

### 任务设计与分类
- 35 个任务分为七类（P1-P7）加杂项，每类针对一种物理直觉：
  - **P1 几何与受限抓取**（9 任务）：如 edge-slide 要求先滑动薄板至悬垂再抓取，测试可供性推理。
  - **P2 动力学与轨迹预测**（7 任务）：如 pendulum-grasp 需在摆锤角速度为零时抓取，探测前向模拟能力。
  - **P3 因果与间接动作**（6 任务）：如 domino-single 要求通过级联位移目标板且夹爪不得触碰，测试因果链构建。
  - **P4 工具使用**（2 任务）、**P5 隐藏状态**（2 任务）、**P6 反应式重规划**（3 任务）、**P7 稳定性与平衡**（4 任务）。
- 每个任务包含 Setup、Goal、Intuition、Canonical Plan 四要素，并明确标注“推理瓶颈”类型。

### 数据收集与过滤
- 遥操作使用 Xbox 控制器（6-DoF 增量命令，EMA 滤波 α=0.8，步进钳位 ±0.15），对比 Meta Quest 后因成功率更高（58.7% vs 11.2%）而选用。
- 三阶段过滤管线：人类 1-5 分评分（仅保留 ≥4 分）→ VLM 代理异常检测（含 FFmpeg 视觉故障检测，Sobel 梯度 <0.3 且 MAD 分数 >10.0）→ 最终人工审查。
- 发布数据集含 6,000 遥操作轨迹 + 8,000 脚本轨迹 = 14,000 条。

### 评估协议
- **Q1/Q2 高层推理**：五个推理器（GPT-5.5、GPT-5.4-mini、Gemma-4、Claude Haiku-4.5、Claude-Sonnet-4.6）使用共享 CoT 提示，分两阶段输出：约束理解（结构化探针）与高层计划（子目标序列，人类验证）。
- **Q3 闭环执行**：GPT-5.5 作为代理，采用 ReAct 框架，每步选择 8 个运动原语之一（MoveEEF、CloseGripper 等），滚动帧历史 H=12，ReAct 循环最多 K=24 步。
- **端到端策略**：Diffusion Policy（DP）从零训练，π0.5 与 GR00T N1.5 在零样本和微调（LoRA Rank 64, α=128）下评估，每任务 20 种子 × 5 次 rollout。

## 关键创新

1. **“推理瓶颈”任务设计原则**：不同于随机化场景或增加物体数量，IMBench 系统性地在任务中注入必须从观测推断的隐藏事实（如 T25 mass-sort 中视觉相同但质量不同的立方体）。这一设计迫使评估对象显式进行物理推理，而非依赖表面特征匹配，是基准能区分“理解”与“记忆”的关键。

2. **三阶段解耦评估协议**：将“约束理解（Q1）→ 计划生成（Q2）→ 闭环执行（Q3）”分离测量，使得能力瓶颈可精确定位。例如 slide-catch 任务中，模型理解得分高达 88-95%，但计划阶段多数完全失败，这直接揭示了“知道该做什么”与“知道怎么做”之间的鸿沟，是现有基准无法提供的诊断粒度。

3. **特权信息对照实验**：在 Stage 3 中引入 IMBAgent-obj（提供特权物体中心姿态），平均成功率从 11.3% 升至 18.8%。这一设计量化了“感知缺失”与“推理/执行缺陷”各自的贡献，为后续研究方向提供了数据支撑——例如 domino-select 从 50% 到 100% 的提升表明，部分失败源于视觉感知而非规划能力。

## 实验与结果

实验覆盖推理、规划、执行与端到端策略四个层面，关键结果如下：

**表 1：高层推理与执行（成功率 %）**

| 阶段 | Gemma 4 | Claude-Haiku 4.5 | Claude Sonnet 4.6 | GPT-5.4-Mini | GPT-5.5 |
|------|---------|------------------|-------------------|--------------|---------|
| Q1 约束理解（Mean） | 57.8（由表内数值 70.0→29.6 计算）±32.0 | 63.6（由表内数值 31.1→51.0 计算）±32.8 | 74.5±31.2 | 64.8（由表内数值 86.0→30.6 计算）±31.6 | 74.1±33.0 |
| Q2 计划正确（Mean） | 45.3（由表内数值 33.5→18.5 计算）±34.3 | 55.7（由表内数值 57.8→90.0 计算）±33.9 | 64.1（由表内数值 86.0→30.6 计算）±34.6 | 50.0±34.4 | 69.5±35.7 |
| Q3 执行（IMBAgent） | - | - | - | - | 11.3 |
| Q3 执行（IMBAgent-obj） | - | - | - | - | 18.8 |

**表 2：端到端策略成功率（Mean）**

| 策略 | π0.5 ZS | π0.5 FT | GR00T 1.5 ZS | GR00T 1.5 FT | DP Full-training |
|------|---------|---------|--------------|--------------|------------------|
| Mean | 0.01 | 0.15 | 0.00 | 0.02 | 0.24 |

**关键发现**：
- GPT-5.5 约束理解约 74%，规划约 70%，但执行仅 11.3%——推理到执行的转化是最大瓶颈。
- 零样本 VLA 性能极低（≤0.02 mean），微调后 π0.5 提升至 0.15，但仍远低于 DP 的 0.24。
- 所有策略均未解决 cup-inversion、shape-stack、packing 等需精确对齐或工具使用的任务。
- OOD 泛化测试中，DP 在 slip-recovery 上 ID 0.44 → OOD 0.56（+0.12），而 π0.5 在 balance-medium 上从 0.71 暴跌至 0.12（-0.59），表明不同方法对分布偏移的鲁棒性差异显著。

## 边界与局限

- **仿真局限**：仅评估 Franka 配平行夹爪和吸盘，排除灵巧手、移动平台与人形机器人；任务为低到中视野，不考虑可变形物体。
- **模态缺失**：虽发布力-力矩和触觉信号，但评估基线均未使用这些模态，其原则性集成仍是开放方向。
- **代理单一**：Stage 3 仅评估 GPT-5.5（因成本约 $1800），未覆盖其他 VLM 的执行能力。
- **任务描述固定**：未测试语言指令变化对性能的影响。
- **遥操作偏差**：操作员均为 STEM 背景男性研究生（N=10），数据多样性受限；VR 遥操作成功率显著低于 Xbox 控制器（11.2% vs 58.7%），可能影响任务难度评估。

## 工程启示

- **复现优先级**：先核对数据过滤管线中的 VLM 异常检测阈值（Sobel 梯度 <0.3、MAD 分数 >10.0），这是保证演示质量的关键，也是最易因环境差异产生偏差的环节。
- **训练配置陷阱**：π0.5 与 GR00T 的 LoRA 配置（Rank 64, α=128）及学习率（3×10⁻⁴）需严格对齐；DP 训练 50k 步、批大小 32，若计算资源受限可先验证 5k 步检查点是否达到论文报告水平的 80%。
- **评估协议注意**：Stage 3 的 ReAct 循环中，滚动帧历史 H=12 每额外批次增加约 1,800 输入 token，API 成本随任务数线性增长——16 任务约 $1800，大规模评估前需预算规划。
- **下游团队选型**：若任务涉及物理推理（如平衡、工具使用），DP 的从零训练表现优于微调 VLA；但若需零样本泛化，π0.5 仍是更稳妥选择。对于需要精确对齐的任务（如 packing），当前所有方法均失败，建议优先探索特权状态或触觉反馈的融合。
- **最易踩坑**：遥操作数据质量过滤中，人类标注的 1-5 分标准主观性较强，建议先在小批量数据上校准标注者一致性（如 Cohen's Kappa），再扩展至全量。

## Overview
Humans combine reasoning and motor control to solve complex manipulation tasks under diverse constraints. They build an understanding of the physical world that helps them convert reasoning into actions and quickly adapt to new scenes, tasks, and rules. We refer to this capability as intuitive manipulation. Existing benchmarks fail to capture this integration: they evaluate physical reasoning in isolation from execution, or measure policy performance without requiring explicit reasoning. We introduce IMBENCH, a benchmark designed to evaluate intuitive manipulation as an integrated capability spanning perception, physical reasoning, action generation, and iterative execution. Our tasks require models to infer task-relevant physical structure and generate feasible action sequences under explicit constraints, including contact-rich manipulation, tool use, and multi-stage dependencies. We introduce a benchmark of 35 tasks, 14K filtered trajectories, and scalable tools for generating diverse scenarios. Experiments reveal a consistent gap: vision language models show partial physical reasoning ability but fail to produce executable plans, while state-of-the-art vision-language-action models struggle to satisfy task constraints and generalize across scenarios. These results identify intuitive manipulation as a missing axis in current foundation models and generalist robot policies, and position IMBENCH as a step toward evaluating and enabling more integrated, adaptive physical intelligence.

## 参考
- https://arxiv.org/abs/2607.15641

## 개요

IMBench는 "직관적 조작"을 위한 시뮬레이션 벤치마크로, 연구팀이 구축했으며 robosuite 기반의 35개 태스크를 포함한다. 물리 추론, 동작 제안, 저수준 실행을 통합된 능력으로 평가하는 종단 간(end-to-end) 평가를 목표로 한다. 핵심 기여는 현재 비전-언어-동작 모델(VLA)과 기초 모델이 물리적 제약 추출과 폐루프 실행에서 현저한 한계를 보인다는 점을 밝히고, 단계별(이해, 계획, 실행) 세분화된 진단 도구를 제공한 것이다.

## 무엇을 바꾸었는가

기존 로봇 조작 벤치마크에는 근본적인 단절이 존재한다: 물리 추론 벤치마크(예: PhysBench)는 "생각"에서 멈추고, 조작 벤치마크(예: LIBERO)는 "실행"만 평가하며, 실제 세계의 정교한 조작은 이 둘의 원활한 결합을 요구한다. IMBench가 진정으로 바꾼 것은 평가 패러다임이다—더 이상 "정책이 동작 시퀀스를 완료할 수 있는가"를 묻지 않고, "시스템이 관측에서 숨겨진 물리적 제약을 추론하고, 그 추론을 실행 가능하고 강건한 동작으로 변환할 수 있는가"를 묻는다. 이러한 전환은 평가의 초점을 지각-운동 매핑의 통계적 피팅에서 물리적 세계의 인과 구조에 대한 능동적 모델링과 활용으로 되돌린다.

저자들은 현재 VLA 모델이 객체 정체성과 장면 레이아웃에서는 일반화가 잘 되지만, 태스크 구조 자체가 물리 추론을 요구할 때(예: 얇은 판을 먼저 밀어야 잡을 수 있는 경우) 성능이 급격히 저하된다는 점을 예리하게 지적한다. IMBench는 "추론 병목" 태스크를 설계하여 시스템이 실행 불가능성, 기하학, 동역학, 인과성, 숨겨진 상태, 안정성과 같은 물리적 사실을 명시적으로 처리하도록 강제함으로써, 기존 모델 능력 지도에서 누락된 핵심 축을 위치시킨다—이는 단순히 더 높은 성공률을 추구하는 것보다 진단적 가치가 더 크다.

## 방법 분석

IMBench의 구축은 "능력 분해, 태스크 격리, 프로세스 연계" 원칙을 따르며, 방법 분석은 다음과 같다:

### 태스크 설계 및 분류
- 35개 태스크는 7개 범주(P1-P7)와 기타 항목으로 나뉘며, 각 범주는 하나의 물리적 직관을 대상으로 한다:
  - **P1 기하학 및 제한적 파지** (9개 태스크): edge-slide는 얇은 판을 먼저 밀어 돌출부에 올린 후 잡아야 하며, 어포던스 추론을 테스트한다.
  - **P2 동역학 및 궤적 예측** (7개 태스크): pendulum-grasp는 진자의 각속도가 0일 때 잡아야 하며, 전방 시뮬레이션 능력을 탐지한다.
  - **P3 인과 및 간접 동작** (6개 태스크): domino-single은 연쇄 변위를 통해 목표 판을 이동시키되 그리퍼가 닿지 않아야 하며, 인과 체인 구축을 테스트한다.
  - **P4 도구 사용** (2개 태스크), **P5 숨겨진 상태** (2개 태스크), **P6 반응적 재계획** (3개 태스크), **P7 안정성 및 균형** (4개 태스크).
- 각 태스크는 Setup, Goal, Intuition, Canonical Plan의 네 가지 요소를 포함하며, "추론 병목" 유형을 명시적으로 표시한다.

### 데이터 수집 및 필터링
- 원격 조작은 Xbox 컨트롤러(6-DoF 증분 명령, EMA 필터 α=0.8, 스텝 클램프 ±0.15)를 사용하며, Meta Quest와 비교 후 성공률이 더 높아(58.7% vs 11.2%) 선택되었다.
- 3단계 필터링 파이프라인: 인간 1-5점 평가(≥4점만 유지) → VLM 에이전트 이상 탐지(FFmpeg 시각적 오류 탐지 포함, Sobel 그래디언트 <0.3 및 MAD 점수 >10.0) → 최종 인간 검토.
- 공개 데이터셋은 6,000개의 원격 조작 궤적 + 8,000개의 스크립트 궤적 = 14,000개를 포함한다.

### 평가 프로토콜
- **Q1/Q2 고수준 추론**: 5개의 추론기(GPT-5.5, GPT-5.4-mini, Gemma-4, Claude Haiku-4.5, Claude-Sonnet-4.6)가 공유 CoT 프롬프트를 사용하며, 두 단계로 출력한다: 제약 이해(구조화된 프로브) 및 고수준 계획(하위 목표 시퀀스, 인간 검증).
- **Q3 폐루프 실행**: GPT-5.5가 에이전트로 사용되며, ReAct 프레임워크를 채택하고, 각 단계에서 8개의 운동 원시 동작 중 하나(MoveEEF, CloseGripper 등)를 선택하며, 롤링 프레임 히스토리 H=12, ReAct 루프 최대 K=24단계.
- **종단 간 정책**: Diffusion Policy(DP)는 처음부터 훈련되고, π0.5와 GR00T N1.5는 제로샷 및 미세 조정(LoRA Rank 64, α=128)으로 평가되며, 각 태스크당 20개 시드 × 5회 롤아웃.

## 핵심 혁신

1. **"추론 병목" 태스크 설계 원칙**: 무작위 장면이나 객체 수 증가와 달리, IMBench는 관측에서 추론해야 하는 숨겨진 사실(예: T25 mass-sort의 시각적으로 동일하지만 질량이 다른 큐브)을 체계적으로 태스크에 주입한다. 이 설계는 평가 대상이 표면적 특징 매칭에 의존하지 않고 명시적으로 물리 추론을 수행하도록 강제하며, 벤치마크가 "이해"와 "기억"을 구분할 수 있는 핵심이다.

2. **3단계 분리 평가 프로토콜**: "제약 이해(Q1) → 계획 생성(Q2) → 폐루프 실행(Q3)"을 분리 측정하여 능력 병목을 정밀하게 위치시킬 수 있다. 예를 들어 slide-catch 태스크에서 모델의 이해 점수는 88-95%에 달하지만, 계획 단계에서는 대부분 완전히 실패하며, 이는 "무엇을 해야 하는지 아는 것"과 "어떻게 하는지 아는 것" 사이의 간극을 직접적으로 드러낸다—기존 벤치마크가 제공할 수 없는 진단적 세분성이다.

3. **특권 정보 대조 실험**: Stage 3에서 IMBAgent-obj(특권 객체 중심 자세 제공)를 도입하여 평균 성공률이 11.3%에서 18.8%로 상승했다. 이 설계는 "지각 결함"과 "추론/실행 결함"의 각각의 기여도를 정량화하며, 후속 연구 방향에 데이터 기반을 제공한다—예를 들어 domino-select가 50%에서 100%로 향상된 것은 일부 실패가 계획 능력이 아닌 시각적 지각에서 비롯됨을 시사한다.

## 실험 및 결과

실험은 추론, 계획, 실행, 종단 간 정책의 네 가지 수준을 다루며, 핵심 결과는 다음과 같다:

**표 1: 고수준 추론 및 실행 (성공률 %)**

| 단계 | Gemma 4 | Claude-Haiku 4.5 | Claude Sonnet 4.6 | GPT-5.4-Mini | GPT-5.5 |
|------|---------|------------------|-------------------|--------------|---------|
| Q1 제약 이해 (Mean) | 57.8 (표 내 값 70.0→29.6으로 계산) ±32.0 | 63.6 (표 내 값 31.1→51.0으로 계산) ±32.8 | 74.5±31.2 | 64.8 (표 내 값 86.0→30.6으로 계산) ±31.6 | 74.1±33.0 |
| Q2 계획 정확도 (Mean) | 45.3 (표 내 값 33.5→18.5로 계산) ±34.3 | 55.7 (표 내 값 57.8→90.0으로 계산) ±33.9 | 64.1 (표 내 값 86.0→30.6으로 계산) ±34.6 | 50.0±34.4 | 69.5±35.7 |
| Q3 실행 (IMBAgent) | - | - | - | - | 11.3 |
| Q3 실행 (IMBAgent-obj) | - | - | - | - | 18.8 |

**표 2: 종단 간 정책 성공률 (Mean)**

| 정책 | π0.5 ZS | π0.5 FT | GR00T 1.5 ZS | GR00T 1.5 FT | DP Full-training |
|------|---------|---------|--------------|--------------|------------------|
| Mean | 0.01 | 0.15 | 0.00 | 0.02 | 0.24 |

**핵심 발견**:
- GPT-5.5의 제약 이해는 약 74%, 계획은 약 70%이지만, 실행은 11.3%에 불과—추론에서 실행으로의 전환이 가장 큰 병목이다.
- 제로샷 VLA 성능은 매우 낮으며(≤0.02 mean), 미세 조정 후 π0.5는 0.15로 향상되지만 여전히 DP의 0.24에 크게 미치지 못한다.
- 모든 정책은 cup-inversion, shape-stack, packing과 같이 정밀한 정렬이나 도구 사용이 필요한 태스크를 해결하지 못했다.
- OOD 일반화 테스트에서 DP는 slip-recovery에서 ID 0.44 → OOD 0.56(+0.12)로 향상된 반면, π0.5는 balance-medium에서 0.71에서 0.12로 급락(-0.59)하여, 분포 이동에 대한 강건성에서 방법 간 차이가 크다는 것을 보여준다.

## 경계 및 한계

- **시뮬레이션 한계**: Franka 로봇에 평행 그리퍼와 흡착 패드만 평가하며, 정교한 손, 이동 플랫폼, 휴머노이드 로봇은 제외한다; 태스크는 저~중 시야 범위이며, 변형 가능한 객체는 고려하지 않는다.
- **모달리티 부재**: 힘-토크 및 촉각 신호가 공개되었지만, 평가 기준선은 이러한 모달리티를 사용하지 않았으며, 원칙적 통합은 여전히 열린 방향이다.
- **단일 에이전트**: Stage 3는 비용(약 $1800) 때문에 GPT-5.5만 평가하며, 다른 VLM의 실행 능력을 다루지 않는다.
- **고정된 태스크 설명**: 언어 명령 변화가 성능에 미치는 영향을 테스트하지 않았다.
- **원격 조작 편향**: 운영자는 모두 STEM 배경의 남성 대학원생(N=10)이며, 데이터 다양성이 제한적이다; VR 원격 조작 성공률은 Xbox 컨트롤러보다 현저히 낮아(11.2% vs 58.7%), 태스크 난이도 평가에 영향을 줄 수 있다.

## 공학적 시사점

- **재현 우선순위**: 데이터 필터링 파이프라인의 VLM 이상 탐지 임계값(Sobel 그래디언트 <0.3, MAD 점수 >10.0)을 먼저 확인하라. 이는 데모 품질을 보장하는 핵심이며, 환경 차이로 인해 편향이 발생하기 가장 쉬운 단계이다.
- **훈련 구성 함정**: π0.5와 GR00T의 LoRA 구성(Rank 64, α=128) 및 학습률(3×10⁻⁴)을 엄격히 일치시켜야 한다; DP는 50k 스텝, 배치 크기 32로 훈련하며, 계산 자원이 제한된 경우 5k 스텝 체크포인트가 논문 보고 수준의 80%에 도달하는지 먼저 검증할 수 있다.
- **평가 프로토콜 주의**: Stage 3의 ReAct 루프에서 롤링 프레임 히스토리 H=12는 추가 배치마다 약 1,800 입력 토큰을 증가시키며, API 비용은 태스크 수에 따라 선형적으로 증가한다—16개 태스크는 약 $1800이므로, 대규모 평가 전에 예산 계획이 필요하다.
- **하류 팀 선택**: 태스크가 물리 추론(예: 균형, 도구 사용)을 포함하는 경우, DP의 처음부터 훈련이 미세 조정 VLA보다 우수하다; 그러나 제로샷 일반화가 필요한 경우 π0.5가 더 안정적인 선택이다. 정밀한 정렬이 필요한 태스크(예: packing)의 경우 현재 모든 방법이 실패하므로, 특권 상태 또는 촉각 피드백 융합을 우선적으로 탐색할 것을 권장한다.
- **가장 흔한 함정**: 원격 조작 데이터 품질 필터링에서 인간 주석의 1-5점 기준은 주관성이 강하므로, 소규모 데이터에서 먼저 주석자 일치도(예: Cohen's Kappa)를 보정한 후 전체로 확장하는 것이 좋다.
