---
$id: ent_paper_generalizable_vla_finetuning_representat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment
  zh: Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment
  ko: Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment
summary:
  en: Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the
    standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained
    representations that support visual and semantic generalization. Co-training on web image-text data, a common remedy,
    does not prevent this; it applies language.
  zh: Anchor-Align 是一套面向视觉-语言-动作（VLA）模型微调的通用配方，由作者团队提出，核心是在标准行为克隆（BC）之外同时施加两个辅助目标：逐层蒸馏冻结预训练 VLM 隐藏状态的“锚定”损失，以及用程序化生成的运动方向标签监督语言头与动作头一致的“对齐”损失。该方法在
    LIBERO-PRO、LIBERO-Plus、CALVIN 及真实 xArm7 机器人上显著提升分布外泛化与长时程控制，并首次直接量化了联合训练 VLA 中语言-动作错位的程度及其与任务成功的相关性。
  ko: Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the
    standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained
    representations that support visual and semantic generalization. Co-training on web image-text data, a common remedy,
    does not prevent this; it applies language.
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
- generalizable
- vla
- finetuning
- representat
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
  title: arXiv:2607.13429 Generalizable VLA Finetuning via Representation Anchoring and Language-Action Al
  url: https://arxiv.org/abs/2607.13429
  date: '2026-07-15'
  accessed_at: '2026-08-05'
---

## 概述

Anchor-Align 是一套面向视觉-语言-动作（VLA）模型微调的通用配方，由作者团队提出，核心是在标准行为克隆（BC）之外同时施加两个辅助目标：逐层蒸馏冻结预训练 VLM 隐藏状态的“锚定”损失，以及用程序化生成的运动方向标签监督语言头与动作头一致的“对齐”损失。该方法在 LIBERO-PRO、LIBERO-Plus、CALVIN 及真实 xArm7 机器人上显著提升分布外泛化与长时程控制，并首次直接量化了联合训练 VLA 中语言-动作错位的程度及其与任务成功的相关性。

## 它改变了什么

这项工作的真正价值在于把 VLA 微调从“纯动作优化”重新定义为“表征保持过程”。此前社区默认两条路线：要么用标准 BC 只优化动作头，结果预训练 VLM 的语义表征被逐步覆盖（CKA 降至 0.34，GQA 精度损失 94%）；要么引入联合训练（co-training）用通用 VQA 数据同时监督语言头，结果语言与动作头在共享骨干上从未被要求一致，导致两者预测相互矛盾——例如动作头预测向右时语言头可能说“左”。作者用数据证明联合训练不仅没解决灾难性遗忘（LIBERO-PRO 位置交换得分 0.0%），还引入了新的错位问题。

作者改变的关键认知是：保留预训练表征与学习动作并非零和博弈。他们用“锚定”把骨干的几何结构钉在预训练状态，用“对齐”迫使动作相关信息路由到语言头与动作头都能访问的共享表示中。这比单纯加正则化或数据增强更本质——它直接干预了表征的语义内容，而非仅约束其数值稳定性。此外，论文提供的语言-动作对齐诊断工具（逐帧比较两头的方向预测）是第一个能直接量化 VLA 内部一致性的方法，为后续调试提供了可操作的指标。

## 方法拆解

### 总体损失
总目标为三部分加权求和：
L_total = L_action + λ_anchor · L_anchor + λ_align · L_align
其中 BC 损失按动作头架构选择：回归头用 L1，流匹配头用 L2（作用于预测速度）。

### Vision-Language Anchoring（锚定）
- 维护一个冻结的预训练 VLM 副本（anchor），与可训练骨干并行处理相同输入批次。
- 在每个解码器层 u，对视觉与文本 token 的隐藏状态施加平方 Frobenius 范数蒸馏：
  L_anchor^(u) = ‖H^S_u[m] − H^A_u[m]‖_F²
- 总锚定损失为所有层平均：L_anchor = (1/|D|) Σ_{u∈D} L_anchor^(u)
- 关键设计：anchor 的语言建模头替换为 nn.Identity()，仅需中间隐藏状态，额外显存 0.7 GB；权重 λ_anchor = 0.1。

### Language-Action Alignment（对齐）
- 取最后一个指令 token 的最后一层隐藏状态 h_pre ∈ R^d（d=896），经可学习投影 W_proj ∈ R^{d×d} 与冻结的预训练语言头 W_lm ∈ R^{|V|×d} 得到词汇表 logits，与程序化方向标签计算交叉熵。
- 标签生成三步（无需人工标注）：
  1. 平均分块：v̄ = (1/K) Σ_{k=1}^{K} A_{:,k,1:3} ∈ R^{B×3}
  2. 过滤：移除 ‖v̄_i‖₂ < τ 的近静止样本（τ = 0.15）
  3. 离散化：选择主导平移轴 j* = argmax_{j∈{x,y,z}} |v̄_{i,j}|，按符号映射到 {up, down, left, right, forward, backward}
- 对齐头仅增加 803,712 个参数（bfloat16 下 1.5 MB）；λ_align = 0.02。

### 对照实验设计
- Shuffle：固定置换方向标签映射（如 left→forward），保持损失表面不变但破坏语义。
- Scatter：将方向词替换为嵌入空间中相互远离的无意义词（如 purple、math）。
- 两者均用于证明对齐增益来自语义一致性而非额外监督信号本身。

### 训练配置
- 骨干：Prismatic-Qwen2.5-0.5B，LoRA 秩 r=64，缩放 α=128，应用于所有层。
- 输入：512 个视觉补丁（每张图像 DINOv2+SigLIP 特征拼接后 256 补丁）+ 文本 + 本体感觉状态。
- 10,000 梯度步，batch size 32，学习率 2×10⁻⁴，每 2,500 步保存检查点。

## 关键创新

1. **逐层锚定而非仅输出层对齐**：现有方法多在最终表示或输出层做约束，Anchor-Align 在全部 24 个 transformer 层施加蒸馏，直接保住中间层的视觉-语言几何结构。这解释了为何 CKA 能维持 0.91（标准 BC 仅 0.34），且 GQA 精度保留 70% 而标准 BC 损失 94%。

2. **程序化语言标签实现语言-动作对齐**：无需人工标注或外部 VQA 数据，仅从动作轨迹的平移分量自动生成六方向标签。这使语言头与动作头首次在同一机器人观测上被监督一致，将对齐率从 16.8% 提升至 78.4%，且 per-rollout 对齐与成功的 Pearson r 从 −0.03 转为 +0.51——证明对齐不是成功的副产品，而是因果驱动因素。

3. **诊断工具与训练目标统一**：将对齐损失框架扩展为诊断指标，可逐帧比较语言头与动作头的方向预测一致性。这是首个能直接量化 VLA 内部错位的方法，并揭示了 SOTA 模型（ChatVLA 20.9%、MolmoAct 15.5%、Magma 17.2%）的方向轴对齐分数远低于随机水平的两倍，说明错位是普遍问题而非个别案例。

## 实验与结果

### 仿真基准
| 任务 | Anchor-Align VLA | VLA-Adapter | OpenVLA-OFT | Co-training + KI |
|------|-----------------|-------------|-------------|------------------|
| LIBERO-PRO Mean | 71.9% | 61.0% | 56.5% | 43.8% |
| LIBERO-PRO Pos. Swap | 22.6% | 2.3% | 0.0% | 0.0% |
| LIBERO-Plus Mean | 90.3% | 85.1% | 74.1% | 57.1% |
| CALVIN 5/5 | 77.9% | 73.1% | 66.5% | — |

位置交换是最严苛的 OOD 测试：Anchor-Align 从基线的 2.3% 提升至 22.6%，而所有对照（含联合训练）均为 0.0%。LIBERO-Plus 各轴增益最大处为背景纹理 +8.9、传感器噪声 +7.4、机器人初始状态 +6.5（由表内数值计算）。

### 消融与对照
| 配置 | LIBERO-PRO | LIBERO-Plus |
|------|-----------|-------------|
| VLA-Adapter（标准 BC） | 61.0 | 85.1 |
| 仅对齐 | 65.9 | 88.6 |
| 仅锚定 | 68.1 | 87.3 |
| Anchor-Align（完整） | 71.9 | 90.3 |
| Shuffle（对照） | 61.4 | 84.9 |
| Scatter（对照） | 63.3 | 85.7 |

Shuffle 与 Scatter 几乎不提升性能，证明增益来自语义正确的标签而非额外监督本身。

### 真实世界（xArm7）
- VLA-Adapter 设置：平均成功率从 28.3% 提升至 54.2%。
- StarVLA 设置：平均成功率从 36.7% 提升至 60.0%；语义扰动测试中，Anchor-Align 在 100% 试验中选择正确目标（基线 90% 选错）。
- 失败模式分析：语义错误从 7 降至 0，错误物体接近从 10 降至 1。

### 训练成本
| 指标 | Standard BC | Co-training + KI | Anchor-Align |
|------|-------------|------------------|--------------|
| 墙钟时间（s/it） | 1.28 | 2.50 | 1.64 |
| 额外 GPU 内存 | — | +5 GB | +0.7 GB |
| 外部数据需求 | 无 | 25K VQA | 无 |

Anchor-Align 开销比联合训练少 3.4×，无需外部数据，额外显存少 7×。

## 边界与局限

作者明确承认的局限包括：对齐标签仅覆盖六个粗略运动方向，无法表达完整动作谱系（如旋转、精细操作）；锚定损失对所有层等权施加，可能非最优；未探索与大规模动作预训练 VLA（如 π₀ 或 OpenVLA）的交互；真实世界评估仅限单臂 xArm7 与少量任务，未覆盖双臂或移动操作。此外，方法需要冻结 VLM 副本，训练期间骨干内存占用翻倍——这对资源受限团队是实际门槛。论文未明确讨论锚定与对齐在视觉-语言-动作联合预训练（而非微调）阶段的适用性，也未分析标签噪声（如近静止样本过滤阈值 τ 的敏感性）对对齐质量的影响。

## 工程启示

复现时最先核对三件事：一是冻结 anchor 的显存占用（0.7 GB）是否在你的训练环境中可接受，尤其当骨干规模超过 0.5B 时；二是对齐标签生成中的 τ=0.15 阈值——它直接决定过滤掉多少近静止样本，若你的任务包含大量缓慢移动（如精密装配），此阈值需重新标定；三是确认语言头确实冻结（W_lm 不更新），否则对齐梯度会破坏预训练词汇几何结构，导致 CKA 分析失效。

最容易踩坑的地方是 LoRA 的周期性合并：论文提到训练中需合并权重，若跳过此步，锚定蒸馏的逐层隐藏状态可能因 LoRA 与基座权重分离而失真。另外，对齐头仅 1.5 MB 参数，但其梯度流经骨干 LoRA——若 LoRA 秩或缩放因子设置不当（如 α 过小），对齐信号可能被 BC 损失淹没。建议先跑 LIBERO-PRO 位置交换作为快速验证：若该轴成功率低于 20%，优先检查锚定权重 λ_anchor 是否被动作损失主导，而非调整对齐标签。对于下游团队，若目标是部署到双臂或移动平台，需自行扩展方向标签空间（如加入 roll/pitch/yaw），并重新评估 τ 与 K 窗口参数。

## Overview
Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained representations that support visual and semantic generalization. Co-training on web image-text data, a common remedy, does not prevent this; it applies language and action losses to separate observations, leaving VLAs with language-action misalignment that standard manipulation benchmarks do not expose. We propose Anchor-Align, which augments BC with two objectives: Vision-Language Anchoring distills layer-wise representations from a frozen VLM copy to prevent this drift, while Language-Action Alignment converts each action target into a discrete motion-direction label and jointly trains language and action prediction on the same robot observation. On a physical xArm7 robot, across two widely used VLA architectures, Anchor-Align improves real-robot success on both (28% to 54% and 37% to 60%). At scale in simulation, we demonstrate consistent improvements on OOD perturbations, perceptual robustness, and long-horizon control across LIBERO-PRO, LIBERO-Plus, and CALVIN, respectively, suggesting that preserving pretrained representations and effective action learning are not fundamentally at odds. Project page: anchoralignvla.github.io

## 参考
- https://arxiv.org/abs/2607.13429

## 개요

Anchor-Align은 VLA(비전-언어-동작) 모델 미세 조정을 위한 범용 레시피로, 저자 팀이 제안했으며, 핵심은 표준 행동 복제(BC) 외에 두 가지 보조 목표를 동시에 적용하는 것입니다: 동결된 사전 훈련 VLM의 은닉 상태를 계층별로 증류하는 "앵커링" 손실, 그리고 프로그램 방식으로 생성된 동작 방향 레이블로 언어 헤드와 동작 헤드의 일치를 감독하는 "정렬" 손실입니다. 이 방법은 LIBERO-PRO, LIBERO-Plus, CALVIN 및 실제 xArm7 로봇에서 분포 외 일반화와 장기 제어를 크게 향상시켰으며, 공동 훈련된 VLA에서 언어-동작 불일치의 정도와 작업 성공과의 상관관계를 최초로 직접 정량화했습니다.

## 무엇을 바꾸었는가

이 작업의 진정한 가치는 VLA 미세 조정을 "순수 동작 최적화"에서 "표현 유지 과정"으로 재정의한 것입니다. 기존 커뮤니티는 두 가지 경로를 기본으로 삼았습니다: 표준 BC로 동작 헤드만 최적화하면 사전 훈련된 VLM의 의미 표현이 점진적으로 덮어써지거나(CKA 0.34로 하락, GQA 정확도 94% 손실), 공동 훈련(co-training)으로 일반 VQA 데이터를 사용해 언어 헤드를 동시에 감독하면 언어 헤드와 동작 헤드가 공유 백본에서 일치하도록 요구된 적이 없어 두 헤드의 예측이 서로 모순됩니다—예를 들어 동작 헤드가 오른쪽을 예측할 때 언어 헤드는 "왼쪽"이라고 말할 수 있습니다. 저자들은 데이터를 통해 공동 훈련이 파괴적 망각을 해결하지 못했을 뿐만 아니라(LIBERO-PRO 위치 교체 점수 0.0%), 새로운 불일치 문제를 도입했음을 증명했습니다.

저자들이 바꾼 핵심 인식은 사전 훈련 표현 유지와 동작 학습이 제로섬 게임이 아니라는 것입니다. 그들은 "앵커링"으로 백본의 기하학적 구조를 사전 훈련 상태에 고정하고, "정렬"로 동작 관련 정보가 언어 헤드와 동작 헤드 모두가 접근할 수 있는 공유 표현으로 라우팅되도록 강제합니다. 이는 단순히 정규화나 데이터 증강을 추가하는 것보다 더 본질적입니다—표현의 의미적 내용에 직접 개입하며, 수치적 안정성만 제약하지 않습니다. 또한, 논문에서 제공하는 언어-동작 정렬 진단 도구(두 헤드의 방향 예측을 프레임별로 비교)는 VLA 내부 일관성을 직접 정량화할 수 있는 첫 번째 방법으로, 이후 디버깅을 위한 실행 가능한 지표를 제공합니다.

## 방법 분해

### 전체 손실
총 목표는 세 부분의 가중 합입니다:
L_total = L_action + λ_anchor · L_anchor + λ_align · L_align
여기서 BC 손실은 동작 헤드 아키텍처에 따라 선택됩니다: 회귀 헤드는 L1, 플로우 매칭 헤드는 L2(예측 속도에 적용).

### Vision-Language Anchoring(앵커링)
- 동결된 사전 훈련 VLM 복사본(anchor)을 유지하며, 훈련 가능한 백본과 병렬로 동일한 입력 배치를 처리합니다.
- 각 디코더 레이어 u에서 시각 및 텍스트 토큰의 은닉 상태에 제곱 Frobenius 노름 증류를 적용합니다:
  L_anchor^(u) = ‖H^S_u[m] − H^A_u[m]‖_F²
- 총 앵커링 손실은 모든 레이어의 평균입니다: L_anchor = (1/|D|) Σ_{u∈D} L_anchor^(u)
- 핵심 설계: anchor의 언어 모델링 헤드를 nn.Identity()로 교체하여 중간 은닉 상태만 필요로 하며, 추가 GPU 메모리는 0.7 GB입니다; 가중치 λ_anchor = 0.1.

### Language-Action Alignment(정렬)
- 마지막 명령 토큰의 마지막 레이어 은닉 상태 h_pre ∈ R^d(d=896)를 가져와, 학습 가능한 투영 W_proj ∈ R^{d×d}와 동결된 사전 훈련 언어 헤드 W_lm ∈ R^{|V|×d}를 통해 어휘 로짓을 얻고, 프로그램 방식의 방향 레이블과 교차 엔트로피를 계산합니다.
- 레이블 생성 3단계(수동 주석 불필요):
  1. 평균 블록: v̄ = (1/K) Σ_{k=1}^{K} A_{:,k,1:3} ∈ R^{B×3}
  2. 필터링: ‖v̄_i‖₂ < τ인 근정지 샘플 제거(τ = 0.15)
  3. 이산화: 지배적 이동 축 j* = argmax_{j∈{x,y,z}} |v̄_{i,j}| 선택, 부호에 따라 {up, down, left, right, forward, backward}로 매핑
- 정렬 헤드는 803,712개의 파라미터만 추가합니다(bfloat16에서 1.5 MB); λ_align = 0.02.

### 대조 실험 설계
- Shuffle: 방향 레이블 매핑을 고정 순열로 교체(예: left→forward), 손실 표면은 유지하되 의미를 파괴.
- Scatter: 방향 단어를 임베딩 공간에서 서로 멀리 떨어진 무의미한 단어(예: purple, math)로 대체.
- 둘 다 정렬 이득이 추가 감독 신호 자체가 아닌 의미적 일관성에서 비롯됨을 증명하는 데 사용됩니다.

### 훈련 구성
- 백본: Prismatic-Qwen2.5-0.5B, LoRA 랭크 r=64, 스케일 α=128, 모든 레이어에 적용.
- 입력: 512개의 시각 패치(각 이미지의 DINOv2+SigLIP 특징을 연결한 후 256 패치) + 텍스트 + 고유수용감 상태.
- 10,000 그래디언트 스텝, 배치 크기 32, 학습률 2×10⁻⁴, 2,500 스텝마다 체크포인트 저장.

## 핵심 혁신

1. **출력 레이어 정렬이 아닌 계층별 앵커링**: 기존 방법은 최종 표현이나 출력 레이어에서 제약을 가하는 경우가 많지만, Anchor-Align은 전체 24개 트랜스포머 레이어에 증류를 적용하여 중간 레이어의 시각-언어 기하학적 구조를 직접 보존합니다. 이는 CKA가 0.91을 유지할 수 있는 이유를 설명합니다(표준 BC는 0.34에 불과), GQA 정확도는 70% 보존되는 반면 표준 BC는 94% 손실됩니다.

2. **프로그램 방식 언어 레이블로 언어-동작 정렬 구현**: 수동 주석이나 외부 VQA 데이터 없이 동작 궤적의 병진 성분에서 6방향 레이블을 자동 생성합니다. 이를 통해 언어 헤드와 동작 헤드가 처음으로 동일한 로봇 관측에서 일관되게 감독되며, 정렬률이 16.8%에서 78.4%로 향상되고, 롤아웃당 정렬과 성공의 Pearson r이 −0.03에서 +0.51로 전환됩니다—정렬이 성공의 부산물이 아니라 인과적 동인임을 증명합니다.

3. **진단 도구와 훈련 목표의 통합**: 정렬 손실 프레임워크를 진단 지표로 확장하여 언어 헤드와 동작 헤드의 방향 예측 일관성을 프레임별로 비교할 수 있습니다. 이는 VLA 내부 불일치를 직접 정량화할 수 있는 최초의 방법이며, SOTA 모델(ChatVLA 20.9%, MolmoAct 15.5%, Magma 17.2%)의 방향 축 정렬 점수가 무작위 수준의 두 배보다 훨씬 낮음을 밝혀내어, 불일치가 개별 사례가 아닌 보편적 문제임을 보여줍니다.

## 실험 및 결과

### 시뮬레이션 벤치마크
| 작업 | Anchor-Align VLA | VLA-Adapter | OpenVLA-OFT | Co-training + KI |
|------|-----------------|-------------|-------------|------------------|
| LIBERO-PRO 평균 | 71.9% | 61.0% | 56.5% | 43.8% |
| LIBERO-PRO 위치 교체 | 22.6% | 2.3% | 0.0% | 0.0% |
| LIBERO-Plus 평균 | 90.3% | 85.1% | 74.1% | 57.1% |
| CALVIN 5/5 | 77.9% | 73.1% | 66.5% | — |

위치 교체는 가장 엄격한 OOD 테스트입니다: Anchor-Align은 기준선 2.3%에서 22.6%로 향상된 반면, 모든 대조군(공동 훈련 포함)은 0.0%입니다. LIBERO-Plus의 축별 최대 이득은 배경 텍스처 +8.9, 센서 노이즈 +7.4, 로봇 초기 상태 +6.5입니다(표 내 수치로 계산).

### 소거 및 대조
| 구성 | LIBERO-PRO | LIBERO-Plus |
|------|-----------|-------------|
| VLA-Adapter(표준 BC) | 61.0 | 85.1 |
| 정렬만 | 65.9 | 88.6 |
| 앵커링만 | 68.1 | 87.3 |
| Anchor-Align(전체) | 71.9 | 90.3 |
| Shuffle(대조) | 61.4 | 84.9 |
| Scatter(대조) | 63.3 | 85.7 |

Shuffle과 Scatter는 성능을 거의 향상시키지 않아, 이득이 추가 감독 자체가 아닌 의미적으로 올바른 레이블에서 비롯됨을 증명합니다.

### 실제 세계(xArm7)
- VLA-Adapter 설정: 평균 성공률이 28.3%에서 54.2%로 향상.
- StarVLA 설정: 평균 성공률이 36.7%에서 60.0%로 향상; 의미적 교란 테스트에서 Anchor-Align은 100% 시행에서 올바른 대상을 선택(기준선은 90% 오선택).
- 실패 모드 분석: 의미 오류가 7에서 0으로 감소, 잘못된 객체 접근이 10에서 1로 감소.

### 훈련 비용
| 지표 | Standard BC | Co-training + KI | Anchor-Align |
|------|-------------|------------------|--------------|
| 벽시계 시간(s/it) | 1.28 | 2.50 | 1.64 |
| 추가 GPU 메모리 | — | +5 GB | +0.7 GB |
| 외부 데이터 요구 | 없음 | 25K VQA | 없음 |

Anchor-Align의 오버헤드는 공동 훈련보다 3.4× 적고, 외부 데이터가 필요 없으며, 추가 메모리는 7× 적습니다.

## 경계 및 한계

저자들이 명시적으로 인정한 한계는 다음과 같습니다: 정렬 레이블은 6개의 대략적인 이동 방향만 포함하여 전체 동작 스펙트럼(회전, 정밀 조작 등)을 표현할 수 없음; 앵커링 손실이 모든 레이어에 동일한 가중치로 적용되어 최적이 아닐 수 있음; 대규모 동작 사전 훈련 VLA(예: π₀ 또는 OpenVLA)와의 상호작용을 탐구하지 않음; 실제 세계 평가가 단일 암 xArm7과 소수의 작업으로 제한되어 양팔 또는 이동 조작을 포함하지 않음. 또한, 이 방법은 동결된 VLM 복사본이 필요하여 훈련 중 백본 메모리 사용량이 두 배가 됩니다—이는 자원이 제한된 팀에게 실질적인 장벽입니다. 논문은 앵커링과 정렬이 미세 조정이 아닌 비전-언어-동작 공동 사전 훈련 단계에서의 적용 가능성을 명시적으로 논의하지 않았으며, 레이블 노이즈(예: 근정지 샘플 필터링 임계값 τ의 민감도)가 정렬 품질에 미치는 영향도 분석하지 않았습니다.

## 엔지니어링 시사점

재현 시 가장 먼저 확인할 세 가지: 첫째, 동결된 anchor의 메모리 사용량(0.7 GB)이 훈련 환경에서 허용 가능한지, 특히 백본 규모가 0.5B를 초과할 때; 둘째, 정렬 레이블 생성의 τ=0.15 임계값—이는 필터링할 근정지 샘플 수를 직접 결정하며, 작업에 느린 이동(예: 정밀 조립)이 많이 포함된 경우 이 임계값을 재보정해야 함; 셋째, 언어 헤드가 실제로 동결되었는지 확인(W_lm이 업데이트되지 않음), 그렇지 않으면 정렬 그래디언트가 사전 훈련 어휘 기하학적 구조를 파괴하여 CKA 분석이 무효화됩니다.

가장 쉽게 실수하는 부분은 LoRA의 주기적 병합입니다: 논문은 훈련 중 가중치 병합이 필요하다고 언급하며, 이 단계를 건너뛰면 앵커링 증류의 계층별 은닉 상태가 LoRA와 베이스 가중치 분리로 인해 왜곡될 수 있습니다. 또한, 정렬 헤드는 1.5 MB 파라미터에 불과하지만 그 그래디언트는 백본 LoRA를 통과합니다—LoRA 랭크나 스케일 팩터가 부적절하게 설정된 경우(예: α가 너무 작음), 정렬 신호가 BC 손실에 묻힐 수 있습니다. 먼저 LIBERO-PRO 위치 교체를 빠른 검증으로 실행하는 것이 좋습니다: 해당 축 성공률이 20% 미만이면 정렬 레이블을 조정하는 대신 앵커링 가중치 λ_anchor가 동작 손실에 압도되지 않았는지 우선 확인하세요. 하류 팀의 경우, 양팔 또는 이동 플랫폼에 배포하려면 방향 레이블 공간을 직접 확장하고(예: roll/pitch/yaw 추가), τ와 K 창 파라미터를 재평가해야 합니다.
