---
$id: ent_paper_scaling_behavior_foundation_model_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scaling Behavior Foundation Model for Humanoid Robots
  zh: Scaling Behavior Foundation Model for Humanoid Robots
  ko: Scaling Behavior Foundation Model for Humanoid Robots
summary:
  en: Humanoid control requires natural whole-body coordination, precise real-time responses to control signals, and robust
    generalization across diverse environmental contexts, making it a cornerstone for generalist embodied agents. Behavior
    Foundation Models (BFMs) have recently emerged as a promising solution to address these challenges by leveraging large-scale
    behavioral data to achieve superior.
  zh: 本文提出一套面向人形机器人的可扩展行为基础模型（BFM）训练体系，通过协调全局运动跟踪学习范式、在线策略数据与参考动作的协同缩放、以及 Humanoid Transformer 架构三大组件，系统研究了 BFM 的缩放行为。作者在
    Unitree G1 平台上验证了该方法，相比现有控制器在全局跟踪误差上降低 82%（由表内数值 0.5674→0.0798 计算），并揭示了同质与异质数据缩放、模型容量与潜在空间结构化之间的关键规律。
  ko: Humanoid control requires natural whole-body coordination, precise real-time responses to control signals, and robust
    generalization across diverse environmental contexts, making it a cornerstone for generalist embodied agents. Behavior
    Foundation Models (BFMs) have recently emerged as a promising solution to address these challenges by leveraging large-scale
    behavioral data to achieve superior.
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
- scaling
- behavior
- foundation
- model
- humano
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
  title: arXiv:2607.15163 Scaling Behavior Foundation Model for Humanoid Robots
  url: https://arxiv.org/abs/2607.15163
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一套面向人形机器人的可扩展行为基础模型（BFM）训练体系，通过协调全局运动跟踪学习范式、在线策略数据与参考动作的协同缩放、以及 Humanoid Transformer 架构三大组件，系统研究了 BFM 的缩放行为。作者在 Unitree G1 平台上验证了该方法，相比现有控制器在全局跟踪误差上降低 82%（由表内数值 0.5674→0.0798 计算），并揭示了同质与异质数据缩放、模型容量与潜在空间结构化之间的关键规律。

## 它改变了什么

人形机器人全身控制长期困于任务特定奖励工程，每个新行为都要重新设计奖励函数，这从根本上限制了跨场景泛化。本文真正改变的是将“缩放”这一 LLM 领域的核心方法论引入人形控制，并给出了可操作的配方——不是零散的技巧堆砌，而是把学习范式、数据构成、模型架构三者作为统一系统来协调。此前 SONIC 等工作的扩展研究只是初步结论，本文则通过行为覆盖分析（K-Means 占用率）将数据缩放拆解为同质（XXS→S，占用率 0.9365→0.9365）与异质（S→L，占用率 0.9365→0.9995）两种机制，证明单纯增加动作量收益甚微，行为覆盖扩展才是性能跃升的关键。

另一个重要改变在于对“全局坐标系运动跟踪”的坚持。现有方法多采用局部姿态跟踪或解耦根运动与姿态跟踪，导致前进与原地踏步不可区分、误差逐帧传播。本文以全局框架下整体全身轨迹复现为统一代理任务，配合八种控制模式掩码（从 Root 单连杆到 Whole-Body 14 连杆），使单一策略天然支持部署时的全局与局部控制切换，无需修改机器人原始感官输入。这为 BFM 预训练与下游任务适配之间提供了更干净的接口抽象。

## 方法拆解

### 问题形式化与学习范式
- 将人形控制建模为 MDP，行为定义为本体感觉状态与动作的轨迹，排除目标状态（视为外部规范）。
- 采用运动跟踪作为统一代理任务，要求复现全局坐标系下整体全身轨迹，而非仅局部姿态。

### 状态与架构设计
- 非对称 actor-critic：Actor 状态为 (根角速度, 投影重力, 关节位置, 关节速度)；Critic 使用特权信息（根高度、连杆位姿、速度等），均在航向坐标系表达。
- 控制接口：从掩码集 ℳ = {𝒎₀, …, 𝒎₇} 随机采样逐连杆掩码，指定八种控制模式（Root、Bimanual、Root-and-Hand、End-Effector、Root-and-End-Effector、Upper-Body、Root-and-Upper-Body、Whole-Body），激活连杆数从 1 到 14。

### 奖励与训练稳定性
- 加权和包含全局根高度（权重 0.5，σ_height=0.3）、全局身体位置（权重 1.0，σ_pos=0.3）、全局身体旋转（权重 1.0，σ_rot=0.4）、线速度（权重 1.0，σ_lin=1.0）、角速度（权重 1.0，σ_ang=3.14）、动作率惩罚（-0.1）、关节限制惩罚（-10.0）、生存奖励（1.0）。
- 早停：任何连杆偏离参考运动超过 0.5 米即终止，并从终止点附近参考状态重新初始化（RSI）。
- 自适应采样：初始权重 w₀=1，每 T_eval=200 轮评估，失败轨迹权重除以 β^T_eval（β=0.999），成功乘以 β^T_eval，裁剪至 [0.03, 1.0]。

### Humanoid Transformer
- 输入为有限时间窗口，经模态特定 tokenizer 编码；本体感觉与动作 token 交错形成上下文序列，加可学习查询 token（被掩码，只能被其他 token 注意到）。
- 目标状态经时间偏移拼接后通过交叉注意力注入；每层更新规则：Z=Z+SelfAttn(RoPE(RMSNorm(Z)))、Z=Z+CrossAttn(RMSNorm(Z), RMSNorm(Z_g))、Z=Z+FFN(RMSNorm(Z))。
- 潜在空间通过 RMSNorm 投影到单位超球面（移除乘法缩放因子），无辅助目标，仅由运动跟踪目标塑造。

### 数据与缩放
- 训练数据聚合 1.02 亿帧（50 FPS）来自 8 个开源数据集，重定向采用两阶段流程（形状系数对齐 + 逐帧 IK）。
- 在线策略缩放：宽度（GPU 数）与深度（rollout 长度）均在 32、48、64 三水平变化，保持每 GPU 环境数 8192 不变。
- 参考动作缩放：五个嵌套子集 XXS（16,159,416 帧）、XS（32,230,197 帧）、S（48,321,234 帧）、M（71,130,505 帧）、L（101,979,598 帧）。

## 关键创新

**1. 行为覆盖的量化与双机制缩放分析**：用 K-Means 聚类（从 L 分区采样 200,000 特征，2,000 簇）定义占用率，将数据缩放拆解为同质（XXS→S，占用率 0.9365→0.9365）与异质（S→L，占用率 0.9365→0.9995）。这是首次将“数据多样性”从“数据量”中解耦并量化，证明异质缩放才是性能提升主因——Ours 测试集上 S→L 带来显著提升，而 XXS→S 仅边际改进。

**2. 全局坐标系运动跟踪 + 八种控制模式掩码**：不同于现有方法解耦根运动与姿态跟踪，本文以全局框架下整体全身轨迹复现为统一目标，并通过预定义掩码集（而非伯努利独立激活）指定控制粒度。这使单一策略同时支持全局与局部控制，局部模式通过首帧校准对齐控制信号方向，避免修改原始感官输入，可解释为参考强制机制。

**3. 无辅助目标的超球面潜在空间结构化**：通过 RMSNorm 将目标嵌入投影到单位超球面，仅靠运动跟踪目标即涌现局部性（时间邻近命令映射到邻近表示）、全局组织（不同行为意图占据可区分区域）、鲁棒性（噪声水平 20 时成功率仅从 0.9836 降至 0.9400）。这为 BFM 的潜在空间可解释性提供了无需额外正则化目标的简洁方案。

## 实验与结果

### 基准对比（全身控制，3M 参数 BFM）
| 方法 | BONES Succ | BONES G-MPKPE | Ours Succ | Ours G-MPKPE |
|---|---|---|---|---|
| GMT | 0.4407 | 0.5674 | 0.0855 | 1.8693 |
| TWIST | 0.4226 | 0.6212 | 0.0831 | 2.2744 |
| SONIC† | 0.9239 | 0.1740 | 0.5937 | 0.5035 |
| BFM-Bym | 0.9644 | 0.1005 | 0.9709 | 0.1224 |
| BFM-Local | 0.7286 | 0.2281 | 0.2553 | 0.4731 |
| BFM-Global | 0.9677 | 0.0798 | 0.9776 | 0.0915 |

全局模式下 G-MPKPE 较 GMT 降低 82%（由表内数值 0.5674→0.0798 计算）。† 标注随机采样的 BONES 测试集可能与 SONIC 训练集重叠。

### 潜在空间鲁棒性（噪声水平 0→20）
| 测试集 | Succ (0→20) | G-MPKPE (0→20) |
|---|---|---|
| BONES | 0.9717→0.9646 | 0.0835→0.1067 |
| Ours | 0.9836→0.9400 | 0.0856→0.1387 |

### 架构缩放
- Humanoid Transformer S（0.41M）到 XL（9.91M）：中等规模 M（3.00M）已达与显著更大 MLP（11.86M）相当或更好性能，进一步增大仅递减收益。
- 增加模型容量导致不同控制模式的潜在表示收敛（图 11），但并非所有模式一致提升，部分模式在适中规模即早期饱和。

### 在线策略缩放
- 最大配置（64 GPU、rollout 64）在几乎所有实验取得最佳性能；单独扩展宽度或深度并不总产生一致改进，需两者平衡。

## 边界与局限

论文未明确列出除以下外的其他局限。作者承认统一控制接口是否是最合适抽象尚不清楚，以及这些模式应如何与未来高层策略集成。行为覆盖的量化度量本质上依赖用于构建共享聚类空间的参考运动选择，没有有限数据集能穷尽所有可能行为，稀有和长尾行为模式不可避免缺失。扩展研究相对 LLM 仍有限：人形控制缺乏成熟大规模预训练基础设施，且实际部署约束（需维持 50 Hz 以上推理频率并预留高层集成预算）限制参数量无限增长。作者未回答如何实现细粒度行为覆盖，而是提出策展有限训练集以实现数据效率与行为覆盖平衡这一更有意义的问题。

## 工程启示

复现时最先核对三件事：**数据分区的行为覆盖**——用论文的 K-Means 流程（200,000 特征、2,000 簇）验证自己的训练集占用率是否达到 0.9995 级别，若低于 0.98 则性能提升将主要受限于数据多样性而非模型容量；**在线策略的宽度-深度平衡**——单独增加 GPU 数或 rollout 长度都可能无效甚至有害，建议先在 32/48/64 三水平网格搜索找到平衡点，再投入大规模训练；**早停阈值 0.5 米与 RSI 的配合**——这是训练稳定性的关键，若去掉 RSI，失败轨迹的梯度噪声会显著拖慢收敛。

最容易踩坑的地方：一是控制模式掩码的采样方式，不要用伯努利独立激活（概率 0.5），必须用论文的八种代表性模式，否则策略会偏向某些链路组合；二是 RMSNorm 投影必须移除乘法缩放因子以得到单位超球面，否则潜在空间结构化性质（局部性、全局组织）会退化；三是评估时全局与局部模式的误差计算方式不同——局部模式去除水平平移偏移和航向差异（L-MPKPE），全局模式保留（G-MPKPE），混淆两者会导致对控制器性能的误判。部署到真实机器人时，高层推理需 TensorRT 加速维持 50 Hz，底层 Unitree SDK2 运行 200 Hz，两者间通过 Wi-Fi TCP 传输并按时间戳缓冲，延迟抖动会直接影响全局跟踪精度。

## Overview
Humanoid control requires natural whole-body coordination, precise real-time responses to control signals, and robust generalization across diverse environmental contexts, making it a cornerstone for generalist embodied agents. Behavior Foundation Models (BFMs) have recently emerged as a promising solution to address these challenges by leveraging large-scale behavioral data to achieve superior expressiveness, versatility and generalization. However, despite growing interest in scaling BFMs to further improve their capabilities, it remains unclear how key factors, including the learning paradigm, behavioral data and model architecture should be coordinated to enable effective scaling. In this work, we revisit the scaling recipe for BFMs and demonstrate that substantial performance gains can be achieved through the coordination of three core components: 1) the learning paradigm of motion tracking that reformulates diverse humanoid control problems as the reproduction of integrated whole-body behaviors in the global frame; 2) the strategic synergy between on-policy rollout quantity and reference motion diversity; and 3) the expressive and scalable model architecture termed Humanoid Transformer that facilitates the natural emergence of structured behavioral representations. Through extensive experiments in both simulation and real-world deployment, we demonstrate that our approach yields significant improvements in control fidelity and task generalization, reducing Mean Per-Keypoint Position Error (MPKPE) on the test set by over 10% in local mode and 82% in global mode compared with existing humanoid controllers. These results establish BFM as a principled and effective foundation for scalable and general-purpose humanoid control.

## 参考
- https://arxiv.org/abs/2607.15163

## 개요

본 논문은 인간형 로봇을 위한 확장 가능한 행동 기반 모델(BFM) 훈련 체계를 제안한다. 전역 운동 추적 학습 패러다임, 온라인 정책 데이터와 참조 동작의 협조적 스케일링, 그리고 Humanoid Transformer 아키텍처의 세 가지 핵심 구성 요소를 조율하여 BFM의 스케일링 동작을 체계적으로 연구한다. 저자는 Unitree G1 플랫폼에서 이 방법을 검증했으며, 기존 컨트롤러 대비 전역 추적 오차를 82% 감소시켰고(표 내 수치 0.5674→0.0798로 계산), 동질적·이질적 데이터 스케일링, 모델 용량, 잠재 공간 구조화 간의 핵심 규칙을 밝혀냈다.

## 무엇을 바꾸었는가

인간형 로봇의 전신 제어는 오랫동안 작업별 보상 엔지니어링에 얽매여 있었으며, 새로운 행동마다 보상 함수를 재설계해야 했기 때문에 교차 시나리오 일반화가 근본적으로 제한되었다. 본 논문이 실제로 바꾼 것은 LLM 분야의 핵심 방법론인 "스케일링"을 인간형 제어에 도입하고 실행 가능한 레시피를 제시한 것이다. 이는 단편적인 기법의 나열이 아니라 학습 패러다임, 데이터 구성, 모델 아키텍처를 하나의 통합 시스템으로 조율한 것이다. 이전 SONIC 등의 확장 연구는 예비적 결론에 그쳤지만, 본 논문은 행동 커버리지 분석(K-Means 점유율)을 통해 데이터 스케일링을 동질적(XXS→S, 점유율 0.9365→0.9365)과 이질적(S→L, 점유율 0.9365→0.9995) 두 메커니즘으로 분해하여, 단순히 동작량을 늘리는 것만으로는 이득이 미미하며 행동 커버리지 확장이 성능 도약의 핵심임을 증명했다.

또 다른 중요한 변화는 "전역 좌표계 운동 추적"에 대한 고수이다. 기존 방법들은 대부분 국소 자세 추적 또는 루트 운동과 자세 추적의 분리를 사용하여, 전진과 제자리 걷기를 구분하지 못하고 오차가 프레임마다 전파되는 문제가 있었다. 본 논문은 전역 프레임워크에서 전체 전신 궤적 재현을 통합 대리 작업으로 삼고, 8가지 제어 모드 마스크(Root 단일 링크부터 Whole-Body 14링크까지)를 함께 사용하여 단일 정책이 배포 시 전역·국소 제어 전환을 자연스럽게 지원하도록 했다. 로봇의 원시 감각 입력을 수정할 필요가 없다. 이는 BFM 사전 훈련과 하위 작업 적응 사이에 더 깔끔한 인터페이스 추상화를 제공한다.

## 방법 분해

### 문제 형식화와 학습 패러다임
- 인간형 제어를 MDP로 모델링하고, 행동을 고유수용감각 상태와 동작의 궤적으로 정의하며, 목표 상태는 외부 사양으로 간주하여 제외한다.
- 운동 추적을 통합 대리 작업으로 채택하며, 국소 자세가 아닌 전역 좌표계에서의 전체 전신 궤적 재현을 요구한다.

### 상태와 아키텍처 설계
- 비대칭 actor-critic: Actor 상태는 (루트 각속도, 투영 중력, 관절 위치, 관절 속도)이고, Critic은 특권 정보(루트 높이, 링크 포즈, 속도 등)를 사용하며, 모두 항로 좌표계에서 표현된다.
- 제어 인터페이스: 마스크 집합 ℳ = {𝒎₀, …, 𝒎₇}에서 링크별 마스크를 무작위 샘플링하여 8가지 제어 모드(Root, Bimanual, Root-and-Hand, End-Effector, Root-and-End-Effector, Upper-Body, Root-and-Upper-Body, Whole-Body)를 지정하며, 활성 링크 수는 1에서 14까지이다.

### 보상과 훈련 안정성
- 가중 합에는 전역 루트 높이(가중치 0.5, σ_height=0.3), 전역 신체 위치(가중치 1.0, σ_pos=0.3), 전역 신체 회전(가중치 1.0, σ_rot=0.4), 선속도(가중치 1.0, σ_lin=1.0), 각속도(가중치 1.0, σ_ang=3.14), 동작률 패널티(-0.1), 관절 제한 패널티(-10.0), 생존 보상(1.0)이 포함된다.
- 조기 종료: 어떤 링크든 참조 운동에서 0.5미터 이상 벗어나면 종료하고, 종료 지점 근처의 참조 상태에서 재초기화한다(RSI).
- 적응형 샘플링: 초기 가중치 w₀=1, 매 T_eval=200 라운드마다 평가하며, 실패 궤적의 가중치는 β^T_eval(β=0.999)로 나누고, 성공 시 β^T_eval을 곱하며, [0.03, 1.0] 범위로 클리핑한다.

### 데이터와 스케일링
- 훈련 데이터는 8개 오픈소스 데이터셋에서 수집한 1.02억 프레임(50 FPS)을 집계하며, 리타겟팅은 2단계 프로세스(형상 계수 정렬 + 프레임별 IK)를 사용한다.
- 온라인 정책 스케일링: 너비(GPU 수)와 깊이(rollout 길이) 모두 32, 48, 64 세 수준에서 변화시키며, GPU당 환경 수 8192는 유지한다.
- 참조 동작 스케일링: 5개의 중첩 하위 집합 XXS(16,159,416프레임), XS(32,230,197프레임), S(48,321,234프레임), M(71,130,505프레임), L(101,979,598프레임).

## 핵심 혁신

**1. 행동 커버리지의 정량화와 이중 메커니즘 스케일링 분석**: K-Means 클러스터링(L 파티션에서 200,000개 특징, 2,000개 클러스터 샘플링)으로 점유율을 정의하고, 데이터 스케일링을 동질적(XXS→S, 점유율 0.9365→0.9365)과 이질적(S→L, 점유율 0.9365→0.9995)으로 분해한다. 이는 "데이터 다양성"을 "데이터 양"에서 처음으로 분리하여 정량화한 것으로, 이질적 스케일링이 성능 향상의 주요 원인임을 증명한다. Ours 테스트 세트에서 S→L은 뚜렷한 향상을 가져오지만 XXS→S는 미미한 개선에 그친다.

**2. 전역 좌표계 운동 추적 + 8가지 제어 모드 마스크**: 기존 방법이 루트 운동과 자세 추적을 분리하는 것과 달리, 본 논문은 전역 프레임워크에서 전체 전신 궤적 재현을 통합 목표로 삼고, 사전 정의된 마스크 집합(베르누이 독립 활성화가 아닌)으로 제어 세분성을 지정한다. 이로써 단일 정책이 전역·국소 제어를 동시에 지원하며, 국소 모드는 첫 프레임 보정을 통해 제어 신호 방향을 정렬하므로 원시 감각 입력을 수정할 필요가 없고, 참조 강제 메커니즘으로 해석할 수 있다.

**3. 보조 목표 없는 초구면 잠재 공간 구조화**: RMSNorm으로 목표 임베딩을 단위 초구면에 투영하여, 운동 추적 목표만으로도 국소성(시간적으로 인접한 명령이 인접한 표현에 매핑), 전역 조직화(서로 다른 행동 의도가 구분 가능한 영역을 점유), 견고성(노이즈 수준 20에서 성공률이 0.9836에서 0.9400으로만 감소)이 자연스럽게 나타난다. 이는 추가 정규화 목표 없이 BFM의 잠재 공간 해석 가능성을 위한 간결한 해법을 제공한다.

## 실험과 결과

### 기준 비교(전신 제어, 3M 파라미터 BFM)
| 방법 | BONES Succ | BONES G-MPKPE | Ours Succ | Ours G-MPKPE |
|---|---|---|---|---|
| GMT | 0.4407 | 0.5674 | 0.0855 | 1.8693 |
| TWIST | 0.4226 | 0.6212 | 0.0831 | 2.2744 |
| SONIC† | 0.9239 | 0.1740 | 0.5937 | 0.5035 |
| BFM-Bym | 0.9644 | 0.1005 | 0.9709 | 0.1224 |
| BFM-Local | 0.7286 | 0.2281 | 0.2553 | 0.4731 |
| BFM-Global | 0.9677 | 0.0798 | 0.9776 | 0.0915 |

전역 모드에서 G-MPKPE가 GMT 대비 82% 감소(표 내 수치 0.5674→0.0798로 계산). † 무작위 샘플링된 BONES 테스트 세트가 SONIC 훈련 세트와 겹칠 수 있음을 표시.

### 잠재 공간 견고성(노이즈 수준 0→20)
| 테스트 세트 | Succ (0→20) | G-MPKPE (0→20) |
|---|---|---|
| BONES | 0.9717→0.9646 | 0.0835→0.1067 |
| Ours | 0.9836→0.9400 | 0.0856→0.1387 |

### 아키텍처 스케일링
- Humanoid Transformer S(0.41M)부터 XL(9.91M)까지: 중간 규모 M(3.00M)이 훨씬 더 큰 MLP(11.86M)와 동등하거나 더 나은 성능에 도달하며, 더 키우면 수익이 체감한다.
- 모델 용량 증가는 서로 다른 제어 모드의 잠재 표현을 수렴시키지만(그림 11), 모든 모드가 일관되게 향상되지는 않으며 일부 모드는 적정 규모에서 조기 포화된다.

### 온라인 정책 스케일링
- 최대 구성(64 GPU, rollout 64)이 거의 모든 실험에서 최고 성능을 달성한다. 너비나 깊이만 단독으로 확장하면 항상 일관된 개선이 나타나지 않으며, 둘의 균형이 필요하다.

## 경계와 한계

논문은 아래 외에 다른 한계를 명시적으로 나열하지 않았다. 저자는 통합 제어 인터페이스가 가장 적절한 추상화인지 여전히 불분명하며, 이러한 모드가 미래의 고수준 정책과 어떻게 통합되어야 하는지도 불분명함을 인정한다. 행동 커버리지의 정량적 측정은 본질적으로 공유 클러스터 공간을 구축하는 데 사용되는 참조 운동 선택에 의존하며, 유한한 데이터셋이 모든 가능한 행동을 완전히 포함할 수는 없고 희귀하고 긴꼬리 행동 패턴은 불가피하게 누락된다. 확장 연구는 LLM에 비해 여전히 제한적이다. 인간형 제어는 성숙한 대규모 사전 훈련 인프라가 부족하고, 실제 배포 제약(50Hz 이상의 추론 빈도 유지 및 고수준 통합 예산 확보 필요)이 파라미터 수의 무한 증가를 제한한다. 저자는 세밀한 행동 커버리지를 어떻게 달성할지에 답하지 않고, 유한한 훈련 세트를 큐레이션하여 데이터 효율성과 행동 커버리지의 균형을 맞추는 더 의미 있는 문제를 제기한다.

## 공학적 시사점

재현 시 가장 먼저 확인할 세 가지: **데이터 파티션의 행동 커버리지** — 논문의 K-Means 프로세스(200,000개 특징, 2,000개 클러스터)로 자체 훈련 세트의 점유율이 0.9995 수준인지 검증하고, 0.98 미만이면 성능 향상이 모델 용량보다 데이터 다양성에 의해 제한될 것이다. **온라인 정책의 너비-깊이 균형** — GPU 수나 rollout 길이만 단독으로 늘리면 무효하거나 오히려 해로울 수 있으므로, 먼저 32/48/64 세 수준의 그리드 탐색으로 균형점을 찾은 후 대규모 훈련에 투자할 것. **조기 종료 임계값 0.5미터와 RSI의 조합** — 이는 훈련 안정성의 핵심이며, RSI를 제거하면 실패 궤적의 그래디언트 노이즈가 수렴을 크게 지연시킨다.

가장 쉽게 실수하는 지점: 첫째, 제어 모드 마스크의 샘플링 방식 — 베르누이 독립 활성화(확률 0.5)를 사용하지 말고 논문의 8가지 대표 모드를 사용해야 한다. 그렇지 않으면 정책이 특정 링크 조합에 편향된다. 둘째, RMSNorm 투영에서 단위 초구면을 얻기 위해 곱셈 스케일링 인자를 제거해야 하며, 그렇지 않으면 잠재 공간 구조화 특성(국소성, 전역 조직화)이 퇴화한다. 셋째, 평가 시 전역·국소 모드의 오차 계산 방식이 다르다 — 국소 모드는 수평 이동 오프셋과 항로 차이를 제거하고(L-MPKPE), 전역 모드는 유지한다(G-MPKPE). 둘을 혼동하면 컨트롤러 성능을 잘못 판단하게 된다. 실제 로봇 배포 시 고수준 추론은 TensorRT 가속으로 50Hz를 유지하고, 저수준 Unitree SDK2는 200Hz로 실행하며, 둘 사이는 Wi-Fi TCP로 전송하고 타임스탬프 기준 버퍼링을 사용한다. 지연 지터는 전역 추적 정밀도에 직접 영향을 미친다.
