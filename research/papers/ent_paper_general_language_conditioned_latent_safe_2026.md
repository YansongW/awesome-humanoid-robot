---
$id: ent_paper_general_language_conditioned_latent_safe_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards General Language-Conditioned Latent Safety Filters
  zh: Towards General Language-Conditioned Latent Safety Filters
  ko: Towards General Language-Conditioned Latent Safety Filters
summary:
  en: Robot policies are becoming increasingly general, with vision-language-action (VLA) models enabling a single policy
    to execute diverse tasks specified in natural language. Safe deployment, however, requires adapting not only to new tasks
    but also to varying safety requirements across users, environments, and applications. Existing safety filters remain largely
    constraint-specific and thus must be.
  zh: 本文提出语言条件化安全过滤（language-conditioned safety filtering）框架，将 Hamilton–Jacobi 可达性安全 critic 与 actor 条件化于自然语言指定的约束，使单个学习到的安全过滤器能在运行时适应不同部署场景的安全需求。作者在
    RoboSuite 仿真环境中验证了该方法在三种操作任务上的有效性，并系统评估了当前视觉-语言模型（VLM）作为失败函数与弱标注器的可靠性边界。
  ko: Robot policies are becoming increasingly general, with vision-language-action (VLA) models enabling a single policy
    to execute diverse tasks specified in natural language. Safe deployment, however, requires adapting not only to new tasks
    but also to varying safety requirements across users, environments, and applications. Existing safety filters remain largely
    constraint-specific and thus must be.
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
- general
- language
- conditioned
- latent
- safe
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
  title: arXiv:2608.00315 Towards General Language-Conditioned Latent Safety Filters
  url: https://arxiv.org/abs/2608.00315
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

本文提出语言条件化安全过滤（language-conditioned safety filtering）框架，将 Hamilton–Jacobi 可达性安全 critic 与 actor 条件化于自然语言指定的约束，使单个学习到的安全过滤器能在运行时适应不同部署场景的安全需求。作者在 RoboSuite 仿真环境中验证了该方法在三种操作任务上的有效性，并系统评估了当前视觉-语言模型（VLM）作为失败函数与弱标注器的可靠性边界。

## 它改变了什么

现有安全过滤器大多与特定约束绑定，当安全需求变化时需要重新设计或重新学习，这与机器人策略（尤其是 VLA 模型）日益通用化的发展趋势形成尖锐矛盾。作者敏锐地指出，VLA 策略通过行为克隆训练，在演示中缺乏危险场景时无法学习隐式安全，且显式语言指定的约束对生成动作的影响很小——这意味着单纯依赖策略本身无法保证安全。本文真正改变了安全过滤器的设计范式：不再为每个约束单独训练过滤器，而是将语言作为条件变量嵌入安全 critic 的输入表示，使单个过滤器能够表达多种约束并泛化到未见约束。这一转变将安全过滤从“约束特定”的工程实践推向“通用安全基础模型”的研究方向，与 VLA 策略的通用化进程对齐。

## 方法拆解

### 语言条件化 HJ 安全 critic
- 学习约束条件化的 HJ critic Qθ(zt, at)，其中 zt = ϕ(ot, c) ∈ Z 同时编码观测和语言约束。
- 诱导值函数 Vθ(zt) = max_{a∈A} Qθ(zt, a)，训练损失与公式 (1) 相同：L(θ) := E[(Qθ(st, at) − yt)²]，其中 yt := (1−γ)h(st) + γ min{h(st), max_{a∈A} Qθ(st+1, a)}。
- 动作空间连续，使用 SAC 训练 HJ critic 和近似动作最大化器的随机 actor。

### 运行时安全过滤
- 每步评估名义动作：仅当 Qθ(zt, a_nom_t) ≥ ε 时执行，否则切换到 HJ actor 策略。
- 从 actor 策略采样多个候选动作，并额外采样名义动作的高斯扰动，选择最接近名义动作且满足 Qθ(zt, at) ≥ ε 的动作。
- 采样数量：Stack Blocks 采样 100 个 actor 动作和 100 个扰动名义动作；Safe Grab/Safe Wipe 采样 100 个扰动名义动作。

### 两种输入表示
- **特权 oracle**：zt = st 为完整系统状态，含机器人状态、物体位姿和安全约束的显式编码。
- **视觉-语言（VL）**：使用 π0.5 的 VLM 编码器，联合处理视觉观测、语言输入和本体感觉，通过共享 transformer 产生 token 序列 Ht ∈ R^{T×D}（D = 2048），均值池化聚合：zt = (1/T) Σ H_t^(i)。
- 选择联合对齐表示而非简单拼接，理由是显式对齐模态可改善下游机器人学习。

### 失败函数定义
- Safe Grab/Safe Wipe：h(st, c) = d_min(st, c) − d_thresh，d_min 为指定障碍物与机械臂最小距离。
- Stack Blocks：h(st, c) = r − d_cube(st, c)，d_cube 为末端执行器到正确目标方块距离。
- VL 设置中定义 h(zt) = h(st, c)，因当前 VLM 尚不足以可靠作为失败函数。

## 关键创新

1. **语言条件化 HJ 安全过滤**：首次将 Hamilton–Jacobi 可达性安全框架直接条件化于自然语言约束，而非约束图像或形式化规格。这使得单个离线学习的过滤器能在运行时适应当前指令，无需为每个新约束重新规划或重新训练。
2. **VLM 作为通用失败函数的系统评估**：构建了 5,000 条安全关键操作轨迹数据集（88.6% 含安全违规），对 11 个 VLM 进行单状态分类、成对偏好、短窗口检测和操作推理探针四类评估，首次量化了当前 VLM 作为安全失败检测器的能力边界——最强模型 Gemini Robotics-ER 1.6 总体准确率 0.758，但失败检测准确率仅 0.564。
3. **采样近似二次规划**：通过从 actor 和扰动名义动作中采样候选并选择最小偏差动作，缓解硬切换导致的抖动，在八个评估设置中的六个达到相等或更高成功率。

## 实验与结果

### 表 1：主结果（50 个场景评估）

| 方法 | Safe Grab SR/CR/IR | Safe Wipe SR/CR/IR | Stack Blocks-3 SR/OC/IR | Stack Blocks-4 SR/OC/IR |
|---|---|---|---|---|
| Nominal | 100.00/76.00/– | 62.00/84.00/– | 0.00/0.00/– | 0.00/0.00/– |
| GT Single | 62.00/48.00/17.71 | 14.94/18.00/20.40 | 28.00/80.00/16.16 | 18.00/92.00/28.30 |
| GT General | 60.00/46.00/8.80 | 8.56/48.00/19.42 | 48.00/82.00/18.59 | 14.00/94.00/32.71 |
| VL Single | 54.00/56.00/18.56 | 6.36/58.00/17.90 | 34.00/74.00/39.55 | 2.00/50.00/72.35 |
| VL General | 40.00/46.00/18.38 | 6.42/72.00/12.54 | 52.00/80.00/31.57 | 0.00/64.00/68.81 |

### 表 2：OOD 泛化（General 过滤器）

| 变体 | SR | CR | OC |
|---|---|---|---|
| Safe Grab OOD | 60.00 | 52.00 | – |
| Safe Wipe OOD | 70.00 | 56.00 | – |
| Stack Blocks-3 Color-Only | 42.00 | – | 82.00 |
| Stack Blocks-4 Color-Only | 0.00 | – | 44.00 |
| Geom-Color | 28.00 | – | 72.00 |
| Geom-Wrong-Prompt | 22.00 | – | 64.00 |
| Geom-Single-Color | 32.00 | – | 62.00 |

### 表 3：VLM 单状态失败分类（250 失败 + 250 非失败）

| 模型 | Acc | Acc_fail | Acc_nonfail |
|---|---|---|---|
| Gemini Robotics-ER 1.6 | 0.758 | 0.564 | 0.952 |
| GPT-5.5 | 0.720 | 0.528 | 0.912 |
| GPT-5.4-mini | 0.664 | 0.552 | 0.776 |
| Qwen3-VL-32B | 0.640 | 0.332 | 0.948 |

### 表 4：池化消融

| 池化 | Safe Grab SR/CR | Safe Wipe SR/CR | Stack Blocks-3 SR/OC |
|---|---|---|---|
| Mean | 74.00/26.00 | 56.00/38.00 | 52.00/80.00 |
| Attention | 84.00/26.00 | 68.00/64.00 | 46.00/88.00 |

### 表 5：推理延迟（ms）

| 组件 | Safe Grab | Safe Wipe | Stack Blocks |
|---|---|---|---|
| Encoding | 42.43 | 42.30 | 42.75 |
| Direct switching | 43.29 | 43.13 | 43.62 |
| Minimum-deviation | 219.36 | 225.55 | 221.72 |

关键发现：Ground Truth General 过滤器在 Safe Grab 上达到与 Single 竞争的性能（SR 60.00 vs 62.00，CR 46.00 vs 48.00），证明语言条件化可替代约束特定训练；但 VL 变体碰撞率仍高（Safe Grab CR 46.00，Safe Wipe CR 72.00）。OOD 泛化显示 Safe Grab CR 从 26% 升至 52%（由表内数值 26.00→52.00 计算），Stack Blocks-4 OC 从 64% 降至 44%（由表内数值 64.00→44.00 计算）。最小偏差选择延迟约 220 ms，超出 20 Hz 控制率 50 ms 预算 4 倍以上。

## 边界与局限

- General 安全过滤器不保证满足语言指定约束，OOD 约束下性能进一步下降。
- 过滤器仍限于特定类型安全约束（避开障碍物或接近物体），跨约束类型泛化未验证。
- 当前 VLM 原始预测不足以定义在线安全过滤器的失败集，VL 设置中 h(zt) 仍使用特权状态定义。
- 最小偏差选择延迟约 220 ms，无法在物理硬件上实时运行；模拟器会等待过滤器，因此任务性能不受影响。
- 注意力池化内存成本巨大：10⁵ 转换的 replay buffer 从约 0.8 GB 增至约 740 GB。
- 未将自然语言规格翻译为形式化规格与本文方法结合；未训练跨约束类型泛化的过滤器；未在物理硬件上部署。
- 论文未明确：VLM 评估中 11 个模型的具体版本日期与训练数据分布。

## 工程启示

- **复现优先核对**：训练超参数差异显著——GT 路径使用批大小 512、回放缓冲区 10⁶、epoch 数 10000；VL 路径使用批大小 64、回放缓冲区 10⁵、epoch 数 1000。若复现 VL 结果，务必区分这两条路径的配置。
- **最容易踩坑**：均值池化压缩 VLM token 序列会丢弃空间特征，注意力池化虽改善部分指标但内存爆炸（约 740 GB）。建议先在小规模验证注意力池化的收益是否值得内存代价。
- **VLM 作为失败函数不可靠**：最强模型 Gemini 仅检测到 56.4% 的失败，且多数模型存在严重类别偏差（如 RoboBrain2.5 非失败准确率 1.000 但失败准确率仅 0.016）。若下游团队计划用 VLM 做安全监督，需先评估其失败检测准确率而非总体准确率。
- **采样策略优于直接执行 actor 动作**：Sampling 在八个评估设置中的六个达到相等或更高 SR，最大差距在 VL 观察下 Stack Blocks-3（52% vs 33%）。工程实现时建议保留采样机制。
- **OOD 泛化需谨慎**：Safe Grab OOD 碰撞率翻倍（由表内数值 26.00→52.00 计算），Stack Blocks-4 OOD 顺序正确率大幅下降（由表内数值 64.00→44.00 计算）。部署到新场景前必须重新评估过滤器性能。

## Overview
Robot policies are becoming increasingly general, with vision-language-action (VLA) models enabling a single policy to execute diverse tasks specified in natural language. Safe deployment, however, requires adapting not only to new tasks but also to varying safety requirements across users, environments, and applications. Existing safety filters remain largely constraint-specific and thus must be redesigned or relearned when safety requirements change. In this paper, we investigate language-conditioned safety filtering, in which a Hamilton-Jacobi safety actor and critic are conditioned on language-specified constraints. We evaluate this formulation across pick-and-place, table-wiping, and block-stacking tasks in the vision-based setting, examining its ability to enforce language-specified constraints and transfer to unseen constraint instances within the evaluated constraint families. Our experiments provide evidence that language-conditioned safety filters reduce constraint violations and exhibit partial transfer to unseen constraint instances.

## 参考
- https://arxiv.org/abs/2608.00315

## 개요

본 논문은 언어 조건화 안전 필터링(language-conditioned safety filtering) 프레임워크를 제안한다. Hamilton–Jacobi 도달 가능성 안전 critic과 actor를 자연어로 지정된 제약 조건에 조건화하여, 단일 학습된 안전 필터가 실행 시 다양한 배포 시나리오의 안전 요구사항에 적응할 수 있게 한다. 저자는 RoboSuite 시뮬레이션 환경에서 세 가지 조작 작업에 대한 방법의 효과를 검증하고, 현재 비전-언어 모델(VLM)이 실패 함수 및 약한 라벨러로서 가지는 신뢰성 경계를 체계적으로 평가한다.

## 무엇을 바꾸었는가

기존 안전 필터는 대부분 특정 제약 조건에 묶여 있어 안전 요구사항이 변경되면 재설계 또는 재학습이 필요하며, 이는 로봇 정책(특히 VLA 모델)의 보편화 추세와 심각한 모순을 이룬다. 저자는 VLA 정책이 행동 복제로 훈련되어 위험 시나리오가 없는 시연에서는 암묵적 안전을 학습할 수 없고, 명시적 언어 지정 제약이 생성된 행동에 미치는 영향이 매우 작다는 점을 예리하게 지적한다. 즉, 정책 자체만으로는 안전을 보장할 수 없다. 본 논문은 안전 필터의 설계 패러다임을 실질적으로 변화시킨다. 더 이상 제약 조건별로 필터를 개별 훈련하지 않고, 언어를 조건 변수로 안전 critic의 입력 표현에 내장하여 단일 필터가 여러 제약 조건을 표현하고 보지 못한 제약 조건으로 일반화할 수 있게 한다. 이러한 전환은 안전 필터링을 "제약 특정" 엔지니어링 관행에서 "범용 안전 기반 모델" 연구 방향으로 끌어올리며, VLA 정책의 일반화 과정과 정렬된다.

## 방법 분석

### 언어 조건화 HJ 안전 critic
- 제약 조건에 조건화된 HJ critic Qθ(zt, at)를 학습하며, 여기서 zt = ϕ(ot, c) ∈ Z는 관측과 언어 제약을 동시에 인코딩한다.
- 유도 가치 함수 Vθ(zt) = max_{a∈A} Qθ(zt, a)를 사용하며, 훈련 손실은 수식 (1)과 동일하다: L(θ) := E[(Qθ(st, at) − yt)²], 여기서 yt := (1−γ)h(st) + γ min{h(st), max_{a∈A} Qθ(st+1, a)}.
- 행동 공간이 연속적이므로 SAC를 사용하여 HJ critic과 근사 행동 최대화를 위한 확률적 actor를 훈련한다.

### 실행 시 안전 필터링
- 각 단계에서 명목 행동을 평가한다: Qθ(zt, a_nom_t) ≥ ε인 경우에만 실행하고, 그렇지 않으면 HJ actor 정책으로 전환한다.
- actor 정책에서 여러 후보 행동을 샘플링하고, 추가로 명목 행동의 가우시안 섭동을 샘플링하여 명목 행동에 가장 가깝고 Qθ(zt, at) ≥ ε을 만족하는 행동을 선택한다.
- 샘플링 수: Stack Blocks는 actor 행동 100개와 섭동 명목 행동 100개를 샘플링하고, Safe Grab/Safe Wipe는 섭동 명목 행동 100개를 샘플링한다.

### 두 가지 입력 표현
- **특권 오라클**: zt = st는 전체 시스템 상태로, 로봇 상태, 물체 자세 및 안전 제약의 명시적 인코딩을 포함한다.
- **시각-언어(VL)**: π0.5의 VLM 인코더를 사용하여 시각 관측, 언어 입력 및 고유 감각을 공동 처리하고, 공유 트랜스포머를 통해 토큰 시퀀스 Ht ∈ R^{T×D}(D = 2048)를 생성한 후 평균 풀링으로 집계한다: zt = (1/T) Σ H_t^(i).
- 단순 연결 대신 공동 정렬 표현을 선택한 이유는 명시적 모달리티 정렬이 하위 로봇 학습을 개선할 수 있기 때문이다.

### 실패 함수 정의
- Safe Grab/Safe Wipe: h(st, c) = d_min(st, c) − d_thresh, 여기서 d_min은 지정된 장애물과 로봇 팔 사이의 최소 거리이다.
- Stack Blocks: h(st, c) = r − d_cube(st, c), 여기서 d_cube는 엔드 이펙터에서 올바른 목표 큐브까지의 거리이다.
- VL 설정에서는 현재 VLM이 실패 함수로 신뢰할 수 없으므로 h(zt) = h(st, c)로 정의한다.

## 핵심 혁신

1. **언어 조건화 HJ 안전 필터링**: Hamilton–Jacobi 도달 가능성 안전 프레임워크를 제약 이미지나 형식 사양이 아닌 자연어 제약에 직접 조건화한 최초의 시도이다. 이를 통해 단일 오프라인 학습 필터가 실행 시 현재 지시에 적응할 수 있으며, 새 제약 조건마다 재계획이나 재훈련이 필요 없다.
2. **VLM의 범용 실패 함수로서의 체계적 평가**: 안전 위반이 포함된 88.6%의 안전 중요 조작 궤적 데이터셋 5,000개를 구축하고, 11개 VLM에 대해 단일 상태 분류, 쌍별 선호, 짧은 창 탐지 및 조작 추론 프로브의 네 가지 평가를 수행하여 현재 VLM이 안전 실패 탐지기로서 가지는 능력 경계를 처음으로 정량화했다. 가장 강력한 모델인 Gemini Robotics-ER 1.6의 전체 정확도는 0.758이지만 실패 탐지 정확도는 0.564에 불과하다.
3. **샘플링 기반 근사 이차 계획**: actor 및 섭동 명목 행동에서 후보를 샘플링하고 최소 편차 행동을 선택하여 하드 전환으로 인한 떨림을 완화하며, 8개 평가 설정 중 6개에서 동일하거나 더 높은 성공률을 달성했다.

## 실험 및 결과

### 표 1: 주요 결과(50개 시나리오 평가)

| 방법 | Safe Grab SR/CR/IR | Safe Wipe SR/CR/IR | Stack Blocks-3 SR/OC/IR | Stack Blocks-4 SR/OC/IR |
|---|---|---|---|---|
| Nominal | 100.00/76.00/– | 62.00/84.00/– | 0.00/0.00/– | 0.00/0.00/– |
| GT Single | 62.00/48.00/17.71 | 14.94/18.00/20.40 | 28.00/80.00/16.16 | 18.00/92.00/28.30 |
| GT General | 60.00/46.00/8.80 | 8.56/48.00/19.42 | 48.00/82.00/18.59 | 14.00/94.00/32.71 |
| VL Single | 54.00/56.00/18.56 | 6.36/58.00/17.90 | 34.00/74.00/39.55 | 2.00/50.00/72.35 |
| VL General | 40.00/46.00/18.38 | 6.42/72.00/12.54 | 52.00/80.00/31.57 | 0.00/64.00/68.81 |

### 표 2: OOD 일반화(General 필터)

| 변형 | SR | CR | OC |
|---|---|---|---|
| Safe Grab OOD | 60.00 | 52.00 | – |
| Safe Wipe OOD | 70.00 | 56.00 | – |
| Stack Blocks-3 Color-Only | 42.00 | – | 82.00 |
| Stack Blocks-4 Color-Only | 0.00 | – | 44.00 |
| Geom-Color | 28.00 | – | 72.00 |
| Geom-Wrong-Prompt | 22.00 | – | 64.00 |
| Geom-Single-Color | 32.00 | – | 62.00 |

### 표 3: VLM 단일 상태 실패 분류(실패 250 + 비실패 250)

| 모델 | Acc | Acc_fail | Acc_nonfail |
|---|---|---|---|
| Gemini Robotics-ER 1.6 | 0.758 | 0.564 | 0.952 |
| GPT-5.5 | 0.720 | 0.528 | 0.912 |
| GPT-5.4-mini | 0.664 | 0.552 | 0.776 |
| Qwen3-VL-32B | 0.640 | 0.332 | 0.948 |

### 표 4: 풀링 절제

| 풀링 | Safe Grab SR/CR | Safe Wipe SR/CR | Stack Blocks-3 SR/OC |
|---|---|---|---|
| Mean | 74.00/26.00 | 56.00/38.00 | 52.00/80.00 |
| Attention | 84.00/26.00 | 68.00/64.00 | 46.00/88.00 |

### 표 5: 추론 지연 시간(ms)

| 구성 요소 | Safe Grab | Safe Wipe | Stack Blocks |
|---|---|---|---|
| Encoding | 42.43 | 42.30 | 42.75 |
| Direct switching | 43.29 | 43.13 | 43.62 |
| Minimum-deviation | 219.36 | 225.55 | 221.72 |

주요 발견: Ground Truth General 필터는 Safe Grab에서 Single과 경쟁력 있는 성능을 달성하여(SR 60.00 vs 62.00, CR 46.00 vs 48.00) 언어 조건화가 제약 특정 훈련을 대체할 수 있음을 증명한다. 그러나 VL 변형의 충돌률은 여전히 높다(Safe Grab CR 46.00, Safe Wipe CR 72.00). OOD 일반화는 Safe Grab CR이 26%에서 52%로 상승하고(표 내 수치 26.00→52.00으로 계산), Stack Blocks-4 OC가 64%에서 44%로 하락함을 보여준다(표 내 수치 64.00→44.00으로 계산). 최소 편차 선택 지연 시간은 약 220ms로, 20Hz 제어율의 50ms 예산을 4배 이상 초과한다.

## 경계 및 한계

- General 안전 필터는 언어 지정 제약 조건을 충족함을 보장하지 않으며, OOD 제약 조건에서는 성능이 더욱 저하된다.
- 필터는 여전히 특정 유형의 안전 제약(장애물 회피 또는 물체 접근)으로 제한되며, 제약 유형 간 일반화는 검증되지 않았다.
- 현재 VLM의 원시 예측은 온라인 안전 필터의 실패 집합을 정의하기에 충분하지 않으며, VL 설정에서 h(zt)는 여전히 특권 상태로 정의된다.
- 최소 편차 선택 지연 시간은 약 220ms로 물리적 하드웨어에서 실시간 실행이 불가능하다. 시뮬레이터는 필터를 기다리므로 작업 성능에는 영향을 미치지 않는다.
- 어텐션 풀링의 메모리 비용이 크다: 10⁵ 전환의 리플레이 버퍼가 약 0.8GB에서 약 740GB로 증가한다.
- 자연어 사양을 형식 사양으로 변환하는 것과 본 방법을 결합하지 않았으며, 제약 유형 간 일반화 필터를 훈련하지 않았고, 물리적 하드웨어에 배포하지 않았다.
- 논문에서 명시하지 않은 사항: VLM 평가에서 11개 모델의 구체적 버전 날짜와 훈련 데이터 분포.

## 공학적 시사점

- **재현 시 우선 확인 사항**: 훈련 하이퍼파라미터 차이가 크다. GT 경로는 배치 크기 512, 리플레이 버퍼 10⁶, epoch 수 10000을 사용하고, VL 경로는 배치 크기 64, 리플레이 버퍼 10⁵, epoch 수 1000을 사용한다. VL 결과를 재현하려면 이 두 경로의 구성을 반드시 구분해야 한다.
- **가장 쉽게 빠지는 함정**: 평균 풀링은 VLM 토큰 시퀀스를 압축하여 공간 특징을 잃어버리며, 어텐션 풀링은 일부 지표를 개선하지만 메모리가 폭발한다(약 740GB). 어텐션 풀링의 이점이 메모리 비용을 정당화하는지 소규모로 먼저 검증할 것을 권장한다.
- **VLM은 실패 함수로 신뢰할 수 없다**: 가장 강력한 모델인 Gemini도 실패의 56.4%만 탐지하며, 대부분의 모델은 심각한 클래스 편향을 보인다(예: RoboBrain2.5의 비실패 정확도는 1.000이지만 실패 정확도는 0.016에 불과). 하위 팀이 VLM을 안전 감독에 사용하려면 전체 정확도가 아닌 실패 탐지 정확도를 먼저 평가해야 한다.
- **샘플링 전략이 actor 행동 직접 실행보다 우수하다**: 샘플링은 8개 평가 설정 중 6개에서 동일하거나 더 높은 SR을 달성했으며, 가장 큰 차이는 VL 관측 하의 Stack Blocks-3에서 나타났다(52% vs 33%). 엔지니어링 구현 시 샘플링 메커니즘을 유지할 것을 권장한다.
- **OOD 일반화는 주의가 필요하다**: Safe Grab OOD 충돌률이 두 배로 증가하고(표 내 수치 26.00→52.00으로 계산), Stack Blocks-4 OOD 순서 정확도가 크게 하락한다(표 내 수치 64.00→44.00으로 계산). 새 시나리오에 배포하기 전에 필터 성능을 반드시 재평가해야 한다.
