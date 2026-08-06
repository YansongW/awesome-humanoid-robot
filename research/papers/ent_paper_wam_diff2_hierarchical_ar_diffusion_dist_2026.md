---
$id: ent_paper_wam_diff2_hierarchical_ar_diffusion_dist_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA'
  zh: 'WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA'
  ko: 'WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA'
summary:
  en: Vision-Language-Action (VLA) models have emerged as a prominent paradigm for end-to-end autonomous driving; however,
    their efficient deployment is severely constrained by high computational latency and exposure bias arising from sequential
    autoregressive decoding. Conversely, while specialized diffusion policies enable low-latency, parallel execution, training
    them from scratch typically yields.
  zh: WAM-Diff2 提出一种三阶段层次化蒸馏方法，将预训练的自回归（AR）视觉-语言-动作（VLA）模型转化为并行离散扩散模型，在保持多任务认知能力的同时实现高吞吐量解码。该方法通过渐进式块因果注意力适应、块级蒸馏和跨尺度教师蒸馏，解决了因果到双向注意力模式转换的架构挑战，并在
    NAVSIM、Bench2Drive 等基准上验证了精度与效率的权衡。
  ko: Vision-Language-Action (VLA) models have emerged as a prominent paradigm for end-to-end autonomous driving; however,
    their efficient deployment is severely constrained by high computational latency and exposure bias arising from sequential
    autoregressive decoding. Conversely, while specialized diffusion policies enable low-latency, parallel execution, training
    them from scratch typically yields.
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
- wam
- diff2
- hierarchical
- ar
- diffusion
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
  title: 'arXiv:2608.01035 WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autono'
  url: https://arxiv.org/abs/2608.01035
  date: '2026-08-02'
  accessed_at: '2026-08-05'
---

## 概述

WAM-Diff2 提出一种三阶段层次化蒸馏方法，将预训练的自回归（AR）视觉-语言-动作（VLA）模型转化为并行离散扩散模型，在保持多任务认知能力的同时实现高吞吐量解码。该方法通过渐进式块因果注意力适应、块级蒸馏和跨尺度教师蒸馏，解决了因果到双向注意力模式转换的架构挑战，并在 NAVSIM、Bench2Drive 等基准上验证了精度与效率的权衡。

## 它改变了什么

这项工作真正改变的是端到端自动驾驶模型“认知能力”与“执行效率”之间的固有取舍。以往，AR 模型（如 Qwen3-VL 基座）虽具备强大的场景推理和语言交互能力，但其顺序解码方式在车端实时场景下是结构性瓶颈，且存在暴露偏差；而专门的扩散策略模型虽能并行生成，却往往退化为单任务专用架构，丢失了通用视觉-语言理解。WAM-Diff2 的贡献在于，它不是从零训练一个新模型，而是提供了一条“转化”路径：将已经过大规模预训练的 AR 通用模型，通过蒸馏“重塑”为并行扩散模型。这改变了领域内“通用性”与“实时性”不可兼得的认知，使得多任务 VLA 模型在部署时无需牺牲推理速度。

## 方法拆解

方法的核心是三阶段层次化蒸馏，旨在平滑地跨越 AR 与扩散模型之间的架构鸿沟。

### 阶段一：渐进式块级适应（Progressive Block-wise Adaptation）
- 设计**块因果注意力**（Block-Causal Attention），将严格因果掩码放宽为块内双向、块间因果的掩码。
- 通过课程式扩展解码块大小 B（B = 1 → 32）逐步放宽约束，确保注意力模式转变期间的数学稳定性。
- 采用渐进式引导初始化：θ_B^(0) ← θ_{B/2}^SFT，其中 θ_1 = θ_AR，即每个更大块的学生模型由前一个较小块的模型权重初始化，而非从头训练。

### 阶段二：块级蒸馏（Block-wise Distillation）
- 使用稳定的、小块的扩散教师模型（如 B=4），通过对称 **Jensen-Shannon 散度（JSD）** 损失，在并行解码的中间噪声状态上对学生模型进行蒸馏。
- 蒸馏顺序为 4 → 8 → 16 → 32，逐步提升学生模型的并行解码能力，同时消除 AR 解码的暴露偏差。

### 阶段三：模型级跨尺度蒸馏（Cross-scale Distillation）
- 利用 8B 扩散教师模型向 2B 学生模型转移知识，同样通过 JSD 损失匹配预测分布。
- 关键发现：共享相同扩散范式的模型具有高度对齐的 token 预测模式，用 top-K 重叠率 ρ_K 量化（如 ρ1 为 84.8%），这为跨尺度蒸馏提供了可行性基础。

### 架构与系统优化
- 基于 Qwen3-VL 框架，8B 教师集成 SigLIP2-SO-400M 视觉编码器（27 块，4096 隐藏维度）和 36 个 Transformer 块；2B 学生使用 SigLIP2-Large 编码器（24 块，2048 隐藏维度）和 28 个 Transformer 块。
- 所有模态（语言 token、2D 边界框、未来路径点）通过统一文本分词器处理，完全移除任务特定投影头。
- 系统级优化：使用 FlashInfer 定制注意力内核加速块因果注意力模式，使用 CUDA Graphs 封装整个执行图以消除 CPU 启动开销。

## 关键创新

1.  **块因果注意力机制**：这是连接 AR 与扩散模型的桥梁。它不是简单的掩码替换，而是通过课程式扩展块大小（B=1→32）和渐进式权重初始化，在数学上保证了注意力模式剧变时的训练稳定性。这一设计使得从 AR 到扩散的转化不再是“推倒重来”，而是“平滑迁移”。
2.  **层次化蒸馏策略**：将蒸馏分解为“块级”和“模型级”两个维度。块级蒸馏解决的是解码并行度提升带来的优化目标不一致问题；模型级蒸馏则解决参数规模缩小带来的能力差距问题。这种解耦使得每一步优化目标清晰，且可独立验证。
3.  **JSD 损失的选择**：作者对比了前向 KL、反向 KL 和 JSD，发现 JSD 在模式寻求（mode-seeking）和广泛语义覆盖之间取得最佳平衡。这避免了前向 KL 导致的“平均化”模糊输出和反向 KL 导致的“模式崩溃”，对于多任务 VLA 模型至关重要。

## 实验与结果

实验在统一多任务协议下进行，覆盖驾驶 VQA、视觉接地和运动规划。

| 模型配置 | DriveBench | LingoQA | COCO mAP | NAVSIM V1 PDMS | NAVSIM V2 EPDMS | Decode TPS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ours-2B (B=1, AR) | 51.23 | 68.40 | 39.20 | 88.14 / 91.50* | 88.32 | 44.5 |
| Ours-2B (B=32) | 48.80 | 65.80 | 36.30 | 87.44 / 91.05* | 87.50 | 124.8 / 673.4 |

- **效率**：从 AR 到扩散（B=32）产生 **2.8×** 解码加速，结合 FlashInfer 和 CUDA Graphs 系统级优化后达到 **15.1×** 加速（由表内数值 44.5 → 673.4 计算）。
- **精度**：在 NAVSIM v1/v2 上，B=32 的 PDMS/EPDMS 与 AR 基线几乎持平（Δ ≤ 0.5 点）。在 Bench2Drive 闭环评估中，B=32 的 Success 率从 51.96 降至 49.55，但 Comfort 指标从 21.40 提升至 23.15。
- **消融**：表 4 显示，直接 AR 到扩散适应（无蒸馏）导致 PDMS 从 88.1 降至 84.1，而完整的块级+模型级蒸馏可恢复至 88.3。表 7 显示，使用 AR 教师（PDMS 79.9）远不如使用扩散教师（PDMS 88.3），验证了跨尺度蒸馏必须基于相同扩散范式。

## 边界与局限

作者明确承认，依赖离散 tokenization 可能引入空间量化伪影，偶尔损害高精度轨迹规划的平滑性。此外，并行扩散学生的下游能力受限于初始自回归教师的基线语义推理能力，即蒸馏无法超越教师的上限。论文未明确说明在极端动态场景（如突发障碍物）下的闭环表现，也未涉及多模态输入（如激光雷达）的扩展性。阶段三（跨尺度蒸馏）和阶段一（AR 预训练）均被作者标注为“非强制”或“可选”，这意味着其必要性可能依赖于具体任务和资源约束。

## 工程启示

对于复现或应用该方法的团队，以下几点值得优先核对：
1.  **初始化至关重要**：阶段一的渐进式初始化（θ_B^(0) ← θ_{B/2}^SFT）是稳定训练的关键。若跳过此步骤直接进行大块训练，很可能遭遇注意力模式剧变导致的训练发散。
2.  **JSD 损失是优选**：在蒸馏目标选择上，JSD 明显优于前向/反向 KL。若下游任务对输出多样性有要求，应避免使用反向 KL。
3.  **系统优化需分平台验证**：FlashInfer 和 CUDA Graphs 的加速效果（15.1×）是在 CUDA 平台上评估的，而模型质量结果在 Ascend 910C 上获得。若部署在非 CUDA 平台，需重新评估系统级优化收益。
4.  **精度与效率的权衡点**：B=8 到 B=16 是精度下降的拐点（LingoQA 从 68.00 降至 66.00），但吞吐量提升显著。若场景对语言推理要求高，建议选择 B≤8；若以规划为主，B=32 可接受。

## Overview
Vision-Language-Action (VLA) models have emerged as a prominent paradigm for end-to-end autonomous driving; however, their efficient deployment is severely constrained by high computational latency and exposure bias arising from sequential autoregressive decoding. Conversely, while specialized diffusion policies enable low-latency, parallel execution, training them from scratch typically yields narrow, single-task architectures that lack holistic visual-linguistic reasoning. Successfully transforming pre-trained autoregressive generalists into parallel diffusion models could combine multi-task cognitive intelligence with execution efficiency, yet this transition presents a formidable architectural challenge due to mismatched attention patterns (causal versus bidirectional) and divergent optimization objectives. To bridge this divide, we introduce WAM-Diff2, a multi-task discrete diffusion VLA framework powered by a three-stage hierarchical distillation strategy. By structuring the architectural shift through progressive block-wise adaptation, block-wise distillation, and model-wise cross-scale distillation, WAM-Diff2 preserves the underlying semantic foundations of the base model while accelerating inference. Extensive evaluations across driving understanding, perception, and planning benchmarks demonstrate that WAM-Diff2 effectively mitigates exposure bias and achieves performance parity with autoregressive baselines. Crucially, the autoregressive-to-diffusion transition yields a 2.8x decoding speedup, which scales to an ultimate 15.1x acceleration when combined with system-level optimizations including FlashInfer and CUDA Graphs.

## 参考
- https://arxiv.org/abs/2608.01035

## 개요

WAM-Diff2는 사전 학습된 자기회귀(AR) 비전-언어-행동(VLA) 모델을 병렬 이산 확산 모델로 변환하는 3단계 계층적 증류 방법을 제안하며, 다중 작업 인지 능력을 유지하면서 높은 처리량 디코딩을 달성합니다. 이 방법은 점진적 블록 인과 어텐션 적응, 블록 수준 증류, 교차 스케일 교사 증류를 통해 인과-양방향 어텐션 패턴 전환의 아키텍처적 과제를 해결하고, NAVSIM, Bench2Drive 등의 벤치마크에서 정밀도와 효율성의 균형을 검증합니다.

## 무엇을 바꾸는가

이 작업이 실제로 바꾸는 것은 엔드투엔드 자율주행 모델의 '인지 능력'과 '실행 효율성' 사이의 고유한 트레이드오프입니다. 기존에는 AR 모델(예: Qwen3-VL 기반)이 강력한 장면 추론 및 언어 상호작용 능력을 갖추고 있지만, 순차 디코딩 방식은 차량 내 실시간 환경에서 구조적 병목이며 노출 편향이 존재합니다. 반면 전용 확산 정책 모델은 병렬 생성이 가능하지만 종종 단일 작업 전용 아키텍처로 퇴화하여 일반적인 비전-언어 이해를 잃습니다. WAM-Diff2의 기여는 처음부터 새 모델을 훈련하는 것이 아니라 '변환' 경로를 제공한다는 점입니다: 대규모 사전 학습된 AR 범용 모델을 증류를 통해 병렬 확산 모델로 '재구성'합니다. 이는 '범용성'과 '실시간성'이 양립할 수 없다는 분야의 인식을 바꾸어, 다중 작업 VLA 모델이 배포 시 추론 속도를 희생할 필요가 없게 합니다.

## 방법 분석

방법의 핵심은 3단계 계층적 증류로, AR과 확산 모델 간의 아키텍처 격차를 부드럽게 넘기 위한 것입니다.

### 1단계: 점진적 블록 수준 적응
- **블록 인과 어텐션**을 설계하여 엄격한 인과 마스크를 블록 내 양방향, 블록 간 인과 마스크로 완화합니다.
- 커리큘럼 방식으로 디코딩 블록 크기 B(B = 1 → 32)를 확장하여 제약을 점진적으로 완화하고, 어텐션 패턴 전환 중 수학적 안정성을 보장합니다.
- 점진적 초기화를 채택: θ_B^(0) ← θ_{B/2}^SFT, 여기서 θ_1 = θ_AR, 즉 더 큰 블록의 학생 모델은 처음부터 훈련하는 대신 이전 더 작은 블록의 모델 가중치로 초기화됩니다.

### 2단계: 블록 수준 증류
- 안정적인 작은 블록 확산 교사 모델(예: B=4)을 사용하여 대칭 **젠슨-섀넌 발산(JSD)** 손실을 통해 병렬 디코딩의 중간 노이즈 상태에서 학생 모델을 증류합니다.
- 증류 순서는 4 → 8 → 16 → 32로, 학생 모델의 병렬 디코딩 능력을 점진적으로 향상시키면서 AR 디코딩의 노출 편향을 제거합니다.

### 3단계: 모델 수준 교차 스케일 증류
- 8B 확산 교사 모델을 사용하여 2B 학생 모델로 지식을 전이하며, 마찬가지로 JSD 손실로 예측 분포를 정합합니다.
- 핵심 발견: 동일한 확산 패러다임을 공유하는 모델은 높은 정렬된 토큰 예측 패턴을 가지며, top-K 중첩률 ρ_K로 정량화됩니다(예: ρ1 = 84.8%). 이는 교차 스케일 증류의 타당성 기반을 제공합니다.

### 아키텍처 및 시스템 최적화
- Qwen3-VL 프레임워크 기반, 8B 교사는 SigLIP2-SO-400M 비전 인코더(27개 블록, 4096 히든 차원)와 36개 Transformer 블록을 통합; 2B 학생은 SigLIP2-Large 인코더(24개 블록, 2048 히든 차원)와 28개 Transformer 블록을 사용합니다.
- 모든 모달리티(언어 토큰, 2D 경계 상자, 미래 경로점)는 통합 텍스트 토크나이저로 처리되며, 작업별 프로젝션 헤드는 완전히 제거됩니다.
- 시스템 수준 최적화: FlashInfer 맞춤형 어텐션 커널로 블록 인과 어텐션 패턴을 가속화하고, CUDA Graphs로 전체 실행 그래프를 캡슐화하여 CPU 시작 오버헤드를 제거합니다.

## 핵심 혁신

1.  **블록 인과 어텐션 메커니즘**: AR과 확산 모델을 연결하는 다리입니다. 단순한 마스크 교체가 아니라 커리큘럼 방식의 블록 크기 확장(B=1→32)과 점진적 가중치 초기화를 통해 어텐션 패턴의 급격한 변화 시 훈련 안정성을 수학적으로 보장합니다. 이 설계는 AR에서 확산으로의 변환을 '처음부터 다시'가 아니라 '부드러운 전이'로 만듭니다.
2.  **계층적 증류 전략**: 증류를 '블록 수준'과 '모델 수준'의 두 차원으로 분해합니다. 블록 수준 증류는 디코딩 병렬성 증가로 인한 최적화 목표 불일치 문제를 해결하고, 모델 수준 증류는 파라미터 규모 축소로 인한 능력 격차를 해결합니다. 이러한 분리는 각 단계의 최적화 목표를 명확하게 하고 독립적으로 검증 가능하게 합니다.
3.  **JSD 손실 선택**: 저자는 순방향 KL, 역방향 KL, JSD를 비교했으며, JSD가 모드 탐색과 광범위한 의미론적 커버리지 사이에서 최상의 균형을 이룬다는 것을 발견했습니다. 이는 순방향 KL의 '평균화'로 인한 모호한 출력과 역방향 KL의 '모드 붕괴'를 피하며, 다중 작업 VLA 모델에 매우 중요합니다.

## 실험 및 결과

실험은 통합 다중 작업 프로토콜 하에서 수행되며, 주행 VQA, 시각적 접지, 운동 계획을 포함합니다.

| 모델 구성 | DriveBench | LingoQA | COCO mAP | NAVSIM V1 PDMS | NAVSIM V2 EPDMS | Decode TPS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ours-2B (B=1, AR) | 51.23 | 68.40 | 39.20 | 88.14 / 91.50* | 88.32 | 44.5 |
| Ours-2B (B=32) | 48.80 | 65.80 | 36.30 | 87.44 / 91.05* | 87.50 | 124.8 / 673.4 |

- **효율성**: AR에서 확산(B=32)으로 **2.8×** 디코딩 가속, FlashInfer 및 CUDA Graphs 시스템 수준 최적화 결합 시 **15.1×** 가속(표 내 값 44.5 → 673.4 계산).
- **정밀도**: NAVSIM v1/v2에서 B=32의 PDMS/EPDMS는 AR 기준선과 거의 동일(Δ ≤ 0.5 포인트). Bench2Drive 폐루프 평가에서 B=32의 Success율은 51.96에서 49.55로 감소했지만, Comfort 지표는 21.40에서 23.15로 향상.
- **절제**: 표 4는 직접 AR-확산 적응(증류 없음)이 PDMS를 88.1에서 84.1로 낮추는 반면, 완전한 블록+모델 수준 증류는 88.3으로 회복함을 보여줍니다. 표 7은 AR 교사(PDMS 79.9)가 확산 교사(PDMS 88.3)보다 훨씬 못하며, 교차 스케일 증류가 동일한 확산 패러다임에 기반해야 함을 검증합니다.

## 경계 및 한계

저자는 이산 토큰화에 의존하면 공간 양자화 아티팩트가 도입되어 고정밀 궤적 계획의 부드러움을 가끔 손상시킬 수 있음을 명시적으로 인정합니다. 또한 병렬 확산 학생의 하위 능력은 초기 자기회귀 교사의 기준선 의미론적 추론 능력에 의해 제한되며, 즉 증류는 교사의 상한을 초과할 수 없습니다. 논문은 극단적 동적 시나리오(예: 돌발 장애물)에서의 폐루프 성능을 명확히 설명하지 않으며, 다중 모달 입력(예: 라이다)으로의 확장성도 다루지 않습니다. 3단계(교차 스케일 증류)와 1단계(AR 사전 학습)는 모두 저자에 의해 '비필수' 또는 '선택적'으로 표시되어, 그 필요성이 특정 작업 및 리소스 제약에 의존할 수 있음을 의미합니다.

## 엔지니어링 시사점

이 방법을 재현하거나 적용하려는 팀에게 다음 사항을 우선적으로 확인하는 것이 좋습니다:
1.  **초기화가 매우 중요**: 1단계의 점진적 초기화(θ_B^(0) ← θ_{B/2}^SFT)는 안정적인 훈련의 핵심입니다. 이 단계를 건너뛰고 직접 큰 블록 훈련을 하면 어텐션 패턴 급변으로 인한 훈련 발산이 발생할 가능성이 높습니다.
2.  **JSD 손실이 우선**: 증류 목표 선택에서 JSD는 순방향/역방향 KL보다 명확히 우수합니다. 하위 작업이 출력 다양성을 요구하는 경우 역방향 KL을 피해야 합니다.
3.  **시스템 최적화는 플랫폼별 검증 필요**: FlashInfer 및 CUDA Graphs의 가속 효과(15.1×)는 CUDA 플랫폼에서 평가된 반면, 모델 품질 결과는 Ascend 910C에서 얻어졌습니다. 비-CUDA 플랫폼에 배포하는 경우 시스템 수준 최적화 이점을 재평가해야 합니다.
4.  **정밀도-효율성 트레이드오프 지점**: B=8에서 B=16은 정밀도 하락의 변곡점(LingoQA가 68.00에서 66.00으로 감소)이지만 처리량 향상은 상당합니다. 언어 추론 요구가 높은 시나리오에서는 B≤8을 권장하고, 계획 중심이라면 B=32가 허용 가능합니다.
