---
$id: ent_paper_trustvla_mechanism_guided_inference_time_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors'
  zh: 'TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors'
  ko: 'TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors'
summary:
  en: Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can
    behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure
    becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks like
    or how to recover behavior without.
  zh: TrustVLA 是一种针对视觉-语言-动作（VLA）模型后门攻击的推理时防御框架，由作者团队提出。它基于对 BadVLA 和 INFUSE 两种攻击内部机制的观察，利用 Dirichlet 证据框架监控逐 token、逐层的认知不确定性，实现无需重训练的检测、定位与局部修复。核心贡献在于将后门防御从经验性输入扰动或参数修复，转向机制引导的因果干预。
  ko: Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can
    behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure
    becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks like
    or how to recover behavior without.
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
- trustvla
- mechanism
- guided
- inference
- time
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
  title: 'arXiv:2607.12571 TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action'
  url: https://arxiv.org/abs/2607.12571
  date: '2026-07-14'
  accessed_at: '2026-08-05'
---

## 概述

TrustVLA 是一种针对视觉-语言-动作（VLA）模型后门攻击的推理时防御框架，由作者团队提出。它基于对 BadVLA 和 INFUSE 两种攻击内部机制的观察，利用 Dirichlet 证据框架监控逐 token、逐层的认知不确定性，实现无需重训练的检测、定位与局部修复。核心贡献在于将后门防御从经验性输入扰动或参数修复，转向机制引导的因果干预。

## 它改变了什么

现有 VLA 防御面临一个根本困境：输入级扰动（JPEG、高斯噪声）不加区分地破坏整个观测，参数级修复（ΔW Auditing、Fine-Pruning）则往往以牺牲干净能力为代价，且两者都无法回答"哪个像素区域导致了不安全动作"这一关键问题。作者识别出被投毒 VLA 内部一个重复出现的机制——紧凑因果足迹，即触发区域在深层注意力中被提升、同时压缩空间不确定性分布。这一发现将防御问题从"如何过滤异常输入"转变为"如何在表示层面定位并因果验证异常来源"。

TrustVLA 真正改变的是防御的粒度与可解释性：它不再把后门视为需要整体清洗的污染，而是视为可在单个观测内定位、掩码并修复的局部因果结构。这使得干净帧仅需支付轻量检测成本，只有被标记的高风险帧才触发完整的定位与修复流程，在保持干净性能的同时显著降低防御开销。

## 方法拆解

TrustVLA 的推理时防御流程分为三个阶段，全部基于冻结的 VLA 检查点，不引入额外训练。

### 证据参数化与不确定性监控
- 对第 l 层隐藏状态 h^(l)，通过语言模型头投影得到逐类证据：e_k^(l) = exp((W_out h^(l))_k)
- Dirichlet 浓度参数：α̃_k^(l) = e_k^(l) + 1，总浓度质量 S^(l) = Σ_{k=1}^{V} α̃_k^(l)
- 认知不确定性：EU^(l) = V / (S^(l) + V)，其中 V 为词表大小

### 三维机制特征
- 机制特征向量 ψ(X) = [r_collapse(X), r_evidence(X), r_early(X)]
- 三个族由五个原始统计量实例化：
  - r_collapse：低序列级均值/最小 EU，捕获空间不确定性坍缩
  - r_evidence：log-max-evidence 和 log-late-evidence，捕获浅到中层证据稳定化
  - r_early：层 0 图像 token EU 标准差，捕获异常早期层离散
- 标量机制分数 R(X) = r_collapse(X) + r_evidence(X) + r_early(X)，三个标准化分量等权聚合，避免学习权重（学习权重需要被威胁模型排除的触发示例）

### 检测阈值校准
- 阈值 τ_cal 从干净验证 rollout 冻结：X 被标记当且仅当 R(X) > τ_cal
- 不使用触发示例、触发器坐标或投毒验证样本设置阈值

### 紧凑因果足迹定位
- 紧凑性：|S| ≤ B，其中 B = 16 图像 token（LIBERO 实验中约占视觉 token 网格的 6%）
- 可定位性：S 由决策层注意力排名相对全局排名提升的 token 播种
- 候选池生成：C_0 = Top_{j, K_cand} {I_deep(j) / (I_all(j) + ε)}，其中 I_all(j) 和 I_deep(j) 分别计算所有层和决策层的平均接收注意力
- 默认 K_cand = 8，缩放闭包/消融诊断 K_cand = 12

### 因果验证与恢复
- 反事实分数下降：Δ(S) = R(X) − R(M_S(X))
- 最终支持 S* = ParetoElbow{(|S|, Δ(S)) : S ∈ H(C_0)}，保持面积-下降前沿并最大化下降增益减面积成本，平局偏向紧凑支持
- 恢复：X_def = Inpaint(X_original, S*)，局部均值、零和模糊掩码作为恢复消融
- 注意力仅用于播种紧凑候选，不作为因果解释；区域仅在掩码降低机制分数时被接受

## 关键创新

**机制引导而非经验防御**：TrustVLA 首次将后门防御建立在可验证的内部机制假设上——紧凑因果足迹。通过命题 1（认知同质化）和命题 2（深层排名提升）的形式化，防御不再依赖启发式规则，而是针对攻击的表示级签名进行检测与定位。这一转变使得防御具有可解释性：每个防御动作都能追溯到具体的机制证据。

**无需重训练与触发样本的推理时干预**：整个流程仅需少量干净校准集（实验中 5-40 样本即可达到高准确率），不接触触发示例或投毒验证样本。这在实际部署中至关重要，因为最终用户无法审计 VLA 的投毒流水线，也不应假设防御者拥有攻击样本。等权聚合机制分数避免了学习权重，从而排除了对触发示例的依赖。

**因果闭包与 Pareto 最优支持选择**：定位阶段不是简单地选择注意力最高的 token，而是通过反事实掩码验证分数下降，并在面积-下降前沿上做 Pareto 选择。这一设计区分了"注意力相关"与"因果必要"——只有掩码后确实降低机制分数的区域才被接受为支持，避免了注意力误导导致的过度掩码。

## 实验与结果

实验覆盖 LIBERO 四个套件（Spatial/Object/Goal/LIBERO-10）上的 OpenVLA 评估，以及 π_0.5 在 LIBERO 风格和 REAL 物理机器人上的迁移验证。主行要求配对 500 集干净/触发日志，每单元 10 任务、每任务 50 rollout。

**表 1 关键结果（VLA-ASR，越低越好）**：

| 攻击 | 防御 | Spatial | Object | Goal | LIBERO-10 | 平均 |
|---|---|---|---|---|---|---|
| BadVLA | 无防御 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| BadVLA | TrustVLA | 0.6 | 8.5 | 9.4 | 9.5 | 7.0% |
| BadVLA | JPEG q=20 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| BadVLA | Gaussian ε=0.08 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| BadVLA | ΔW Auditing r=20% | 100.0 | 100.0 | 100.0 | 99.6 | 99.9% |
| INFUSE | 无防御 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| INFUSE | TrustVLA | 0.0 | 0.6 | 1.7 | 6.3 | 2.2% |
| INFUSE | JPEG q=20 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| INFUSE | Gaussian ε=0.08 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| INFUSE | ΔW Auditing r=20% | 20.9 | 37.3 | 98.9 | 83.2 | 60.1% |

**检测可靠性（表 2）**：BadVLA 总计 FAR=0/2000=0.0、DR=1989/2000=99.5；INFUSE 总计 FAR=0/2000=0.0、DR=2000/2000=100.0。

**π_0.5 迁移（表 3）**：TrustVLA 在 LIBERO-10 上残余 VLA-ASR 为 24.06，相比无防御的 100 显著降低；REAL 物理机器人（表 4）Strawberries 任务 ASR 从 94.12 降至 11.76，Blocks 任务从 96.43 降至 14.29。

**运行时开销（表 12）**：干净帧检测开销约 6-21 ms/动作查询，触发帧定位+修复约 15-50 ms，定位入口率在 0.0%-7.5% 之间。

**消融（表 13）**：仅注意力定位平均恢复 SR(w)=74.0，仅最大下降 81.0，仅 Pareto 79.8，Pareto+2D 闭包 81.8；完整因果闭包在 LIBERO-10 上从 57.0 提升至 83.5。

## 边界与局限

TrustVLA 的恢复能力以紧凑因果足迹假设为条件，该假设是所评估视觉触发攻击的可证伪工作假设，而非普遍不变量。语义或非视觉触发器、全局滤波器风格触发器、以及模仿证据同时抑制定位的自适应攻击者仍在鲁棒性声明之外。对于与任务对象不可分的语义触发器，预期行为是保守检测后 fail-safe 停止，而非保证恢复。

Lipschitz 假设仅适用于连续表示和预离散化动作输出，不保证离散动作 token 在 argmax 或采样后的不变性；小 logit 扰动仍可能翻转决策边界附近的 token，因此表 1 的成功率应视为经验证据而非紧致认证结果。论文未在所有 VLA 架构上验证，理论分析抽象为 token 级隐藏状态，不表征所有架构。自适应攻击者若同时满足四个约束（保持干净证据轨迹、避免深层排名提升、保持干净 SR、保持触发效能），则 TrustVLA 的机制解释将被削弱。

## 工程启示

复现 TrustVLA 时，首先核对干净校准集的规模与质量——表 9 显示 5 样本校准 FAR 高达 0.172，40 样本降至 0.025，建议至少使用 20 样本以保证检测可靠性。最容易踩坑的是注意力定位与因果验证的混淆：注意力仅用于播种候选，绝不能直接作为掩码依据，必须通过反事实分数下降验证（表 13 显示仅注意力定位平均恢复仅 74.0，显著低于完整方法）。

部署时注意运行时模式：干净帧仅支付检测成本（约 6-21 ms），候选搜索、反事实掩码和修复仅在门触发后运行。若下游任务存在杂乱场景中的多物体容纳（如 LIBERO-10 任务 8、9），面积预算 B=16 可能余量最小，需考虑增大 B 或接受更高的残余 VLA-ASR。对于 π_0.5 等使用流匹配动作头的架构，需通过语言模型头投影预动作视觉-语言隐藏状态以获取可比较的证据轨迹，这一跨架构实例化是迁移可行性的关键前提。

## Overview
Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks like or how to recover behavior without retraining. We study this gap through two independently proposed VLA attacks from groups with distinct injection strategies, BadVLA and INFUSE; the latter persists after downstream clean adaptation. Across the evaluated poisoned models, we identify a recurring internal mechanism: a \emph{compact causal footprint}, namely a small visual support that is attention-seeded, spatially compact, and \emph{causal} in a precise sense -- masking it returns a clean-calibrated evidence-evolution score to the normal operating region. This footprint motivates TrustVLA, a mechanism-guided inference-time defense that adapts the Dirichlet evidence framework from trusted classification to monitor per-token, per-layer epistemic uncertainty in VLA policies. With only a small clean calibration set, TrustVLA (i)~detects abnormal evidence evolution, (ii)~localizes the compact support by counterfactual mechanism-score drop, and (iii)~recovers the observation by localized inpainting. Across OpenVLA/LIBERO and $π_{0.5}$ transfer evaluations, TrustVLA reduces attack success while preserving clean-task performance, providing a retraining-free, mechanism-guided defense for visual-triggered VLA backdoors.

## 参考
- https://arxiv.org/abs/2607.12571

## 개요

TrustVLA는 시각-언어-행동(VLA) 모델에 대한 백도어 공격을 위한 추론 시점 방어 프레임워크로, 저자 팀이 제안했습니다. 이는 BadVLA와 INFUSE 두 가지 공격의 내부 메커니즘 관찰에 기반하여, Dirichlet 증거 프레임워크를 활용해 토큰별, 레이어별 인지 불확실성을 모니터링함으로써 재학습 없이 탐지, 위치 파악, 국소 복구를 구현합니다. 핵심 기여는 백도어 방어를 경험적 입력 교란 또는 파라미터 수리에서 메커니즘 기반 인과 개입으로 전환한 것입니다.

## 무엇을 바꾸었는가

기존 VLA 방어는 근본적인 딜레마에 직면해 있습니다: 입력 수준 교란(JPEG, 가우시안 노이즈)은 관측 전체를 무차별적으로 손상시키고, 파라미터 수준 수리(ΔW Auditing, Fine-Pruning)는 종종 깨끗한 성능을 희생하는 대가를 치르며, 둘 다 "어떤 픽셀 영역이 안전하지 않은 행동을 유발했는가"라는 핵심 질문에 답할 수 없습니다. 저자들은 중독된 VLA 내부에서 반복적으로 나타나는 메커니즘, 즉 **컴팩트 인과 발자국**(트리거 영역이 깊은 레이어 어텐션에서 강조되면서 동시에 공간 불확실성 분포를 압축하는 현상)을 식별했습니다. 이 발견은 방어 문제를 "이상 입력을 어떻게 필터링할 것인가"에서 "표현 수준에서 이상 원인을 어떻게 위치 파악하고 인과적으로 검증할 것인가"로 전환합니다.

TrustVLA가 실제로 바꾸는 것은 방어의 세분성과 해석 가능성입니다: 백도어를 전체적으로 세척해야 할 오염이 아니라, 단일 관측 내에서 위치 파악, 마스킹, 복구가 가능한 국소 인과 구조로 간주합니다. 이를 통해 깨끗한 프레임은 가벼운 탐지 비용만 지불하고, 표시된 고위험 프레임만 전체 위치 파악 및 복구 프로세스를 트리거하여 깨끗한 성능을 유지하면서 방어 오버헤드를 크게 줄입니다.

## 방법 분해

TrustVLA의 추론 시점 방어 프로세스는 세 단계로 구성되며, 모두 동결된 VLA 체크포인트를 기반으로 추가 학습 없이 진행됩니다.

### 증거 파라미터화 및 불확실성 모니터링
- l번째 레이어 은닉 상태 h^(l)에 대해 언어 모델 헤드 투영을 통해 클래스별 증거를 얻습니다: e_k^(l) = exp((W_out h^(l))_k)
- Dirichlet 농도 파라미터: α̃_k^(l) = e_k^(l) + 1, 총 농도 질량 S^(l) = Σ_{k=1}^{V} α̃_k^(l)
- 인지 불확실성: EU^(l) = V / (S^(l) + V), 여기서 V는 어휘 크기

### 3차원 메커니즘 특징
- 메커니즘 특징 벡터 ψ(X) = [r_collapse(X), r_evidence(X), r_early(X)]
- 세 가지 패밀리는 다섯 가지 원시 통계량으로 인스턴스화됩니다:
  - r_collapse: 낮은 시퀀스 수준 평균/최소 EU, 공간 불확실성 붕괴 포착
  - r_evidence: log-max-evidence 및 log-late-evidence, 얕은 레이어에서 중간 레이어로의 증거 안정화 포착
  - r_early: 레이어 0 이미지 토큰 EU 표준편차, 비정상적인 초기 레이어 이산성 포착
- 스칼라 메커니즘 점수 R(X) = r_collapse(X) + r_evidence(X) + r_early(X), 세 개의 표준화된 구성 요소가 동일 가중치로 집계되어 학습 가중치를 피합니다(학습 가중치는 위협 모델에서 제외된 트리거 예제가 필요함)

### 탐지 임계값 보정
- 임계값 τ_cal은 깨끗한 검증 롤아웃에서 동결됩니다: X는 R(X) > τ_cal일 때만 표시됨
- 트리거 예제, 트리거 좌표 또는 중독 검증 샘플을 사용하지 않고 임계값 설정

### 컴팩트 인과 발자국 위치 파악
- 컴팩트성: |S| ≤ B, 여기서 B = 16 이미지 토큰(LIBERO 실험에서 시각 토큰 그리드의 약 6% 차지)
- 위치 파악 가능성: S는 결정 레이어 어텐션 순위가 전체 순위에 비해 상승한 토큰으로 시드됨
- 후보 풀 생성: C_0 = Top_{j, K_cand} {I_deep(j) / (I_all(j) + ε)}, 여기서 I_all(j)와 I_deep(j)는 각각 모든 레이어와 결정 레이어의 평균 수신 어텐션을 계산
- 기본 K_cand = 8, 스케일링 폐포/소거 진단 K_cand = 12

### 인과 검증 및 복구
- 반사실 점수 하락: Δ(S) = R(X) − R(M_S(X))
- 최종 지지 집합 S* = ParetoElbow{(|S|, Δ(S)) : S ∈ H(C_0)}, 면적-하락 프론티어를 유지하고 하락 이득에서 면적 비용을 뺀 값을 최대화하며, 동률일 경우 컴팩트 지지 집합을 선호
- 복구: X_def = Inpaint(X_original, S*), 국소 평균, 제로, 블러 마스크가 복구 소거로 사용됨
- 어텐션은 컴팩트 후보 시드에만 사용되며 인과 설명으로 사용되지 않음; 영역은 마스킹이 메커니즘 점수를 낮출 때만 수용됨

## 핵심 혁신

**메커니즘 기반而非경험적 방어**: TrustVLA는 백도어 방어를 검증 가능한 내부 메커니즘 가설, 즉 컴팩트 인과 발자국에 처음으로 기반을 둡니다. 명제 1(인지 동질화)과 명제 2(깊은 레이어 순위 상승)의 형식화를 통해 방어는 더 이상 휴리스틱 규칙에 의존하지 않고 공격의 표현 수준 서명을 탐지하고 위치 파악합니다. 이러한 전환은 방어에 해석 가능성을 부여합니다: 모든 방어 조치는 구체적인 메커니즘 증거로 추적될 수 있습니다.

**재학습 및 트리거 샘플 없는 추론 시점 개입**: 전체 프로세스는 소량의 깨끗한 보정 집합만 필요하며(실험에서 5-40개 샘플로 높은 정확도 달성), 트리거 예제나 중독 검증 샘플에 접촉하지 않습니다. 이는 최종 사용자가 VLA의 중독 파이프라인을 감사할 수 없고 방어자가 공격 샘플을 보유하고 있다고 가정해서는 안 되기 때문에 실제 배포에서 중요합니다. 동일 가중치 집계 메커니즘 점수는 학습 가중치를 피하여 트리거 예제에 대한 의존성을 배제합니다.

**인과 폐포 및 Pareto 최적 지지 집합 선택**: 위치 파악 단계는 단순히 어텐션이 가장 높은 토큰을 선택하는 것이 아니라, 반사실 마스킹을 통해 점수 하락을 검증하고 면적-하락 프론티어에서 Pareto 선택을 수행합니다. 이 설계는 "어텐션 관련성"과 "인과 필수성"을 구분합니다 — 마스킹 후 실제로 메커니즘 점수를 낮추는 영역만 지지 집합으로 수용되어 어텐션 오도로 인한 과도한 마스킹을 방지합니다.

## 실험 및 결과

실험은 LIBERO 네 가지 스위트(Spatial/Object/Goal/LIBERO-10)에서의 OpenVLA 평가와 π_0.5의 LIBERO 스타일 및 REAL 물리 로봇 전이 검증을 포함합니다. 메인 라인은 500개 에피소드의 깨끗한/트리거 로그 쌍, 유닛당 10개 작업, 작업당 50개 롤아웃을 요구합니다.

**표 1 핵심 결과(VLA-ASR, 낮을수록 좋음)**:

| 공격 | 방어 | Spatial | Object | Goal | LIBERO-10 | 평균 |
|---|---|---|---|---|---|---|
| BadVLA | 방어 없음 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| BadVLA | TrustVLA | 0.6 | 8.5 | 9.4 | 9.5 | 7.0% |
| BadVLA | JPEG q=20 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| BadVLA | Gaussian ε=0.08 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| BadVLA | ΔW Auditing r=20% | 100.0 | 100.0 | 100.0 | 99.6 | 99.9% |
| INFUSE | 방어 없음 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| INFUSE | TrustVLA | 0.0 | 0.6 | 1.7 | 6.3 | 2.2% |
| INFUSE | JPEG q=20 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| INFUSE | Gaussian ε=0.08 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| INFUSE | ΔW Auditing r=20% | 20.9 | 37.3 | 98.9 | 83.2 | 60.1% |

**탐지 신뢰성(표 2)**: BadVLA 총 FAR=0/2000=0.0, DR=1989/2000=99.5; INFUSE 총 FAR=0/2000=0.0, DR=2000/2000=100.0.

**π_0.5 전이(표 3)**: TrustVLA는 LIBERO-10에서 잔여 VLA-ASR이 24.06으로, 방어 없는 100에 비해 크게 감소; REAL 물리 로봇(표 4) Strawberries 작업 ASR이 94.12에서 11.76으로, Blocks 작업이 96.43에서 14.29로 감소.

**런타임 오버헤드(표 12)**: 깨끗한 프레임 탐지 오버헤드는 약 6-21 ms/행동 쿼리, 트리거 프레임 위치 파악+복구는 약 15-50 ms, 위치 파악 진입률은 0.0%-7.5% 사이.

**소거(표 13)**: 어텐션 전용 위치 파악 평균 복구 SR(w)=74.0, 최대 하락 전용 81.0, Pareto 전용 79.8, Pareto+2D 폐포 81.8; 완전한 인과 폐포는 LIBERO-10에서 57.0에서 83.5로 향상.

## 경계 및 한계

TrustVLA의 복구 능력은 컴팩트 인과 발자국 가설을 조건으로 하며, 이는 평가된 시각 트리거 공격에 대한 반증 가능한 작업 가설이지 보편적 불변량이 아닙니다. 의미론적 또는 비시각적 트리거, 전역 필터 스타일 트리거, 그리고 증거를 모방하면서 동시에 위치 파악을 억제하는 적응형 공격자는 여전히 견고성 주장 범위 밖에 있습니다. 작업 객체와 분리할 수 없는 의미론적 트리거의 경우, 기대되는 동작은 보수적 탐지 후 fail-safe 중지이지 복구 보장이 아닙니다.

Lipschitz 가정은 연속 표현 및 사전 이산화된 행동 출력에만 적용되며, argmax 또는 샘플링 후 이산 행동 토큰의 불변성을 보장하지 않습니다; 작은 logit 교란도 결정 경계 근처의 토큰을 뒤집을 수 있으므로 표 1의 성공률은 경험적 증거로 간주해야 하며 엄격한 인증 결과가 아닙니다. 논문은 모든 VLA 아키텍처에서 검증되지 않았으며, 이론적 분석은 토큰 수준 은닉 상태로 추상화되어 모든 아키텍처를 특성화하지 않습니다. 적응형 공격자가 네 가지 제약(깨끗한 증거 궤적 유지, 깊은 레이어 순위 상승 회피, 깨끗한 SR 유지, 트리거 효능 유지)을 동시에 충족하면 TrustVLA의 메커니즘 해석은 약화됩니다.

## 엔지니어링 시사점

TrustVLA를 재현할 때 먼저 깨끗한 보정 집합의 규모와 품질을 확인하십시오 — 표 9는 5개 샘플 보정 FAR이 0.172까지 높지만 40개 샘플에서는 0.025로 감소함을 보여주며, 탐지 신뢰성을 위해 최소 20개 샘플을 권장합니다. 가장 흔한 함정은 어텐션 위치 파악과 인과 검증의 혼동입니다: 어텐션은 후보 시드에만 사용되며 절대 마스크 근거로 직접 사용해서는 안 되며, 반드시 반사실 점수 하락을 통해 검증해야 합니다(표 13은 어텐션 전용 위치 파악 평균 복구가 74.0에 불과하여 완전한 방법보다 크게 낮음을 보여줍니다).

배포 시 런타임 패턴에 주의하십시오: 깨끗한 프레임은 탐지 비용만 지불하며(약 6-21 ms), 후보 검색, 반사실 마스킹 및 복구는 게이트가 트리거된 후에만 실행됩니다. 하위 작업에 혼잡한 장면의 다중 객체 수용(예: LIBERO-10 작업 8, 9)이 있는 경우 면적 예산 B=16의 여유가 최소일 수 있으므로 B를 늘리거나 더 높은 잔여 VLA-ASR을 수용하는 것을 고려해야 합니다. π_0.5와 같이 흐름 매칭 행동 헤드를 사용하는 아키텍처의 경우, 언어 모델 헤드 투영을 통해 사전 행동 시각-언어 은닉 상태를 투영하여 비교 가능한 증거 궤적을 얻어야 하며, 이 교차 아키텍처 인스턴스화가 전이 가능성의 핵심 전제 조건입니다.
