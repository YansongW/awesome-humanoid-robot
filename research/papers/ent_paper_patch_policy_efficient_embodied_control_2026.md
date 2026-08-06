---
$id: ent_paper_patch_policy_efficient_embodied_control_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations'
  zh: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations'
  ko: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations'
summary:
  en: Pretrained dense visual features from Vision Transformers (ViTs) are powerful yet have been underutilized in robot learning.
    Modern robot policies either compress each observation into a single global token, or rely on visual backbones trained
    from scratch, sacrificing both fine-grained spatial detail and the benefits of large-scale visual pre-training. While
    there exist policies that do operate.
  zh: Patch Policy 提出了一种直接消费预训练 ViT 密集 patch 特征（而非全局池化或 CLS token）的模块化 Transformer 策略架构，由 NYU、Meta-FAIR 与 AMI Labs 联合完成。其核心贡献在于证明：在不引入十亿参数
    VLM 骨干的前提下，仅靠冻结的密集视觉表征配合块因果注意力，即可在模拟与真实世界操控任务上超越全局表征基线与微调 VLA 模型，同时将参数量与推理延迟降低数个数量级。
  ko: Pretrained dense visual features from Vision Transformers (ViTs) are powerful yet have been underutilized in robot learning.
    Modern robot policies either compress each observation into a single global token, or rely on visual backbones trained
    from scratch, sacrificing both fine-grained spatial detail and the benefits of large-scale visual pre-training. While
    there exist policies that do operate.
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
- patch
- policy
- efficient
- embodied
- control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.18236 Patch Policy: Efficient Embodied Control via Dense Visual Representations'
  url: https://arxiv.org/abs/2607.18236
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

Patch Policy 提出了一种直接消费预训练 ViT 密集 patch 特征（而非全局池化或 CLS token）的模块化 Transformer 策略架构，由 NYU、Meta-FAIR 与 AMI Labs 联合完成。其核心贡献在于证明：在不引入十亿参数 VLM 骨干的前提下，仅靠冻结的密集视觉表征配合块因果注意力，即可在模拟与真实世界操控任务上超越全局表征基线与微调 VLA 模型，同时将参数量与推理延迟降低数个数量级。

## 它改变了什么

机器人学习社区长期面临一个两难：要么使用 CLS token 或平均池化这类全局表征，牺牲细粒度空间信息；要么引入 OpenVLA 这类十亿参数 VLM，继承其全部推理与训练成本。Patch Policy 真正改变的是这个权衡的默认假设——它用实验证明，视觉运动策略的核心需求是"密集但冻结"的特征，而非"全局但可微调"的表征，更非"庞大但通用"的生成式骨干。这一判断将视觉预训练与策略学习的耦合方式从"端到端微调"或"全局压缩"两个极端中解放出来，指向一条参数效率与空间保真度兼得的中间路径。

该工作还改变了社区对"patch 特征必须配合大模型使用"的隐性认知。通过将策略学习建模为对 T×P 时空 token 序列的序列建模，并引入块因果注意力掩码，它让 3 千万可训练参数即可驾驭 1 万+ 的 patch token 流，而无需任何全局池化或降维操作。这实质上把视觉表征的利用问题从"如何压缩"重新定义为"如何组织注意力"。

## 方法拆解

### 观测主干（Observation Trunk）
- 输入图像 o_t ∈ R^{C×H×W} 经冻结 ViT 编码器分割为 patches，输出形状 P×D 的密集特征（P=patch 数，D=嵌入维度）。
- 对上下文窗口 T，特征序列形状为 T×P×D；目标条件设置下，目标图像经同编码器编码后与观测拼接为 T×P×2D，或目标向量 g ∈ R^G 逐 token 拼接为 T×P×(D+G)。
- 关键设计：P=1 时退化为全局池化特征，天然兼容基于状态的环境，保证架构通用性。

### 策略学习（Policy Learning）
- 将 T×P 时空张量展平为长度 T×P 的序列，添加可学习 1D 位置嵌入（按展平索引）。
- 应用**块因果注意力掩码（block-causal attention mask）**：帧内 patch 完全双向注意力，帧间严格因果。该设计允许模型整合每帧空间上下文，同时防止未来帧信息泄漏。
- 动作头在每帧最后一个 patch token 处输出动作块（action chunk）；公式与动作头架构无关，评估了 VQ-BeT（混合分类-回归）与 Diffusion Policy（去噪）两种头。

### 训练与推理
- 训练：前向传递 patch token 序列，逐帧计算损失。
- 推理：提取当前观测 patch 特征，追加至长度 T 的滚动窗口，策略预测动作块并以递减时域控制执行。
- 冻结骨干允许预计算视觉嵌入，显著加速训练。

## 关键创新

1. **块因果注意力掩码的引入**：这是对"如何组织密集 token 注意力"的明确回答。相比 full attention（允许未来帧泄漏）与 token-causal（破坏帧内上下文），块因果在帧内保持双向、帧间保持因果，在 Diffusion Policy 上 Cube 任务从 0.11（token-causal）恢复至 1.24（block-causal），证明该掩码对时空建模的关键性。

2. **冻结骨干 + 密集特征的解耦**：不微调视觉编码器，直接消费预训练 patch 特征。这一设计使训练成本降至 6.5 GPU-hours（1xL40S），对比 OpenVLA-OFT 的 16 GPU-hours 与 ACT 的 24 GPU-hours，同时保留 DINOv2/WebSSL 等大规模预训练的表征收益。

3. **参数效率的极致化**：以 51.55M 总参数（VQ-BeT + DINOv2）超越 7.61B 的 OpenVLA-OFT，推理延迟 10.99 ms 对比 61.71 ms。这证明密集特征的价值不在于模型规模，而在于特征本身的保真度与策略架构的适配性。

## 实验与结果

### 模拟环境（Table 1，100 轨迹/种子）
| 方法 | Push-T | LIBERO Goal | BlockPush | Cube |
|---|---|---|---|---|
| WebSSL Patch + VQ-BeT (Ours) | 0.68 ± 0.03 | 0.94 ± 0.01 | 1.68 ± 0.15 | 1.68 ± 0.03 |
| WebSSL Patch + DP (Ours) | 0.80 ± 0.01 | 0.98 ± 0.00 | 1.65 ± 0.08 | 1.73 ± 0.02 |
| WebSSL Avg Pool + DP | 0.79 ± 0.02 | 0.98 ± 0.01 | 1.34 ± 0.02 | 0.21 ± 0.03 |
| OpenVLA-OFT | 0.59 ± 0.02 | 0.95 | 1.43 ± 0.17 | 1.50 ± 0.09 |
| ResNet-18 Patch + ACT | 0.64 ± 0.03 | 0.93 ± 0.02 | 0.15 ± 0.01 | 0.69 ± 0.11 |

### 真实世界（Table 2，20 次试验，DINOv2 Patch + VQ-BeT）
| 任务 | 阶段 | Ours | DINOv2 CLS | ACT | OpenVLA-OFT |
|---|---|---|---|---|---|
| Cable Insertion | Fully inserted | 0.70 | 0.60 | 0.35 | 0.30 |
| Pen Collection | Third pen placed | 0.85 | 0.65 | 0.65 | 0.60 |
| Tool Hanging | Tool placed | 0.90 | 0.70 | 0.85 | 0.65 |

### 计算资源（Table 3，H200）
| 方法 | 总参数 | 可训练参数 | 推理延迟 |
|---|---|---|---|
| Ours - VQ-BeT (DINOv2) | 51.55M | 29.49M | 10.99 ms |
| Ours - DP (WebSSL) | 303.66M | 9.35M | 451.68 ms |
| OpenVLA-OFT | 7.61B | 177.90M | 61.71 ms |
| ACT | 83.85M | 83.85M | 8.63 ms |

### 关键结论
- 相比最优全局池化基线，相对改进 40%（由表内数值 1.73→0.21 计算）；超越 OpenVLA-OFT 18%（由表内数值 1.73→1.50 计算），参数仅约 0.7%。
- 表征消融（Table 7/8）：WebSSL 与 DINOv2 表现最佳，SigLIP2 全面垫底（Push-T 0.51 vs DINOv2 0.69）。
- 零样本泛化（Table 5/6）：真实世界拾取 87% vs CAP 79%；EgoGym 关闭任务 92.44% vs 86.50%。

## 边界与局限

- 仅评估冻结视觉骨干，未探索端到端微调对专门视觉领域（如透明物体、高反光表面）的增益。
- 密集 token 增加序列长度与训练时间，FlashAttention 等优化未纳入当前实现。
- 仅作为行为克隆策略验证，未扩展到强化学习；静态专家演示的性能上限未被突破。
- 视觉表征选择对结果影响显著（SigLIP2 全面失败），论文未明确给出表征选择的理论判据，仅提供经验结论。
- 真实世界实验仅用 DINOv2 (ViT-S)，未验证 WebSSL 在真实场景的迁移性。

## 工程启示

- **先核对视觉表征**：WebSSL 与 DINOv2 是当前最优选择，SigLIP2 在操控任务上系统性失败，复现时优先采用前两者。
- **注意力掩码是核心超参数**：block-causal 是默认选择；token-causal 在 Diffusion Policy 上会导致 Cube 性能崩溃（0.11），务必避免。
- **模型大小存在阈值效应**：Push-T 上 Diffusion Policy 从 25.30M（覆盖 0.56）增至 40.43M（覆盖 0.83）时性能跃升，小模型可能无法利用密集特征，需按任务调整 N、heads、d_emb。
- **预计算嵌入是训练加速关键**：冻结骨干允许离线提取 patch 特征，训练成本可降至 6.5 GPU-hours，工程上应优先实现该缓存机制。
- **推理延迟需区分动作分块**：论文报告的 10.99 ms 为单次前向传递，未含 receding horizon 的时间加速；实际部署时该技术可正交叠加。

## Overview
Pretrained dense visual features from Vision Transformers (ViTs) are powerful yet have been underutilized in robot learning. Modern robot policies either compress each observation into a single global token, or rely on visual backbones trained from scratch, sacrificing both fine-grained spatial detail and the benefits of large-scale visual pre-training. While there exist policies that do operate on dense patch features like large vision-language-action models (VLAs), they tend to be heavy and slow, inheriting the full cost of a billion-parameter vision-language model (VLM) backbone. We close this gap with Patch Policy, a minimal architectural extension that enables transformer-based policies to consume dense pre-trained patch tokens directly without the computational overhead of a full VLM. At its core is a block-causal attention mask that preserves the temporal causality of standard policies while letting the model attend over many patch tokens per observation, alongside other state information. Patch Policy is lightweight, fast, and highly effective. Across four simulated and three real-world environment suites, our method achieves a 40% relative improvement over policies using state-of-the-art global-pooled representations. Furthermore, it surpasses fine-tuned OpenVLA-OFT by 18% while using roughly 0.7% of the parameters. We believe Patch Policy provides a pipeline for the robotics community to readily leverage continuing progress in visual representation learning, without sacrificing the training efficiency or inference speed required for high-frequency, reactive control. Videos can be viewed at https://patch-policy.github.io

## 参考
- https://arxiv.org/abs/2607.18236

## 개요

Patch Policy는 사전 학습된 ViT의 밀집 패치 특징(전역 풀링 또는 CLS 토큰이 아닌)을 직접 소비하는 모듈식 Transformer 정책 아키텍처를 제안하며, NYU, Meta-FAIR 및 AMI Labs가 공동으로 완성했습니다. 핵심 기여는 수십억 파라미터 VLM 백본을 도입하지 않고도, 동결된 밀집 시각 표현과 블록 인과 어텐션만으로 시뮬레이션 및 실제 세계 조작 작업에서 전역 표현 기준선과 미세 조정된 VLA 모델을 능가하면서 파라미터 수와 추론 지연 시간을 수 자릿수 줄일 수 있음을 증명한 것입니다.

## 무엇을 바꾸었는가

로봇 학습 커뮤니티는 오랫동안 딜레마에 직면해 왔습니다: CLS 토큰이나 평균 풀링과 같은 전역 표현을 사용하여 미세한 공간 정보를 희생하거나, OpenVLA와 같은 수십억 파라미터 VLM을 도입하여 모든 추론 및 훈련 비용을 상속받는 것입니다. Patch Policy가 실제로 바꾼 것은 이 트레이드오프의 기본 가정입니다. 실험을 통해 시각-운동 정책의 핵심 요구 사항은 "밀집하지만 동결된" 특징이지, "전역적이지만 미세 조정 가능한" 표현도, "거대하지만 범용적인" 생성 백본도 아님을 증명했습니다. 이 판단은 시각 사전 학습과 정책 학습의 결합 방식을 "엔드투엔드 미세 조정" 또는 "전역 압축"이라는 두 극단에서 해방시켜, 파라미터 효율성과 공간 충실도를 모두 갖춘 중간 경로를 가리킵니다.

이 작업은 또한 "패치 특징은 대형 모델과 함께 사용해야 한다"는 커뮤니티의 암묵적 인식을 바꾸었습니다. 정책 학습을 T×P 시공간 토큰 시퀀스의 시퀀스 모델링으로 모델링하고 블록 인과 어텐션 마스크를 도입함으로써, 3천만 개의 훈련 가능한 파라미터로 1만 개 이상의 패치 토큰 스트림을 처리할 수 있으며 전역 풀링이나 차원 축소 작업이 필요 없습니다. 이는 본질적으로 시각 표현 활용 문제를 "어떻게 압축할 것인가"에서 "어떻게 어텐션을 구성할 것인가"로 재정의합니다.

## 방법 분석

### 관측 백본 (Observation Trunk)
- 입력 이미지 o_t ∈ R^{C×H×W}는 동결된 ViT 인코더에 의해 패치로 분할되며, P×D 형태의 밀집 특징을 출력합니다 (P=패치 수, D=임베딩 차원).
- 컨텍스트 창 T에 대해 특징 시퀀스 형태는 T×P×D입니다. 목표 조건 설정에서는 목표 이미지가 동일한 인코더로 인코딩된 후 관측과 연결되어 T×P×2D가 되거나, 목표 벡터 g ∈ R^G가 토큰별로 연결되어 T×P×(D+G)가 됩니다.
- 핵심 설계: P=1일 때 전역 풀링 특징으로 축소되어 상태 기반 환경과 자연스럽게 호환되며 아키텍처의 범용성을 보장합니다.

### 정책 학습 (Policy Learning)
- T×P 시공간 텐서를 길이 T×P의 시퀀스로 평탄화하고, 학습 가능한 1D 위치 임베딩(평탄화 인덱스 기준)을 추가합니다.
- **블록 인과 어텐션 마스크(block-causal attention mask)** 적용: 프레임 내 패치는 완전 양방향 어텐션, 프레임 간은 엄격한 인과 관계. 이 설계는 각 프레임의 공간 컨텍스트를 통합하면서 미래 프레임 정보 누출을 방지합니다.
- 액션 헤드는 각 프레임의 마지막 패치 토큰에서 액션 청크(action chunk)를 출력합니다. 공식은 액션 헤드 아키텍처와 무관하며, VQ-BeT(혼합 분류-회귀)와 Diffusion Policy(노이즈 제거) 두 가지 헤드를 평가했습니다.

### 훈련 및 추론
- 훈련: 패치 토큰 시퀀스를 순방향 전달하고 프레임별로 손실을 계산합니다.
- 추론: 현재 관측 패치 특징을 추출하여 길이 T의 롤링 창에 추가하고, 정책이 액션 청크를 예측하며 감소하는 시간 영역 제어로 실행합니다.
- 동결된 백본은 시각 임베딩을 사전 계산할 수 있게 하여 훈련을 크게 가속화합니다.

## 핵심 혁신

1. **블록 인과 어텐션 마스크 도입**: 이는 "밀집 토큰 어텐션을 어떻게 구성할 것인가"에 대한 명확한 답변입니다. full attention(미래 프레임 누출 허용) 및 token-causal(프레임 내 컨텍스트 파괴)과 비교하여, 블록 인과는 프레임 내 양방향, 프레임 간 인과를 유지하며 Diffusion Policy의 Cube 작업에서 0.11(token-causal)에서 1.24(block-causal)로 회복되어 이 마스크가 시공간 모델링에 결정적임을 증명합니다.

2. **동결 백본 + 밀집 특징의 분리**: 시각 인코더를 미세 조정하지 않고 사전 학습된 패치 특징을 직접 소비합니다. 이 설계는 훈련 비용을 6.5 GPU-hours(1xL40S)로 낮추며, OpenVLA-OFT의 16 GPU-hours 및 ACT의 24 GPU-hours와 비교되면서 DINOv2/WebSSL과 같은 대규모 사전 학습의 표현 이점을 유지합니다.

3. **파라미터 효율성의 극대화**: 51.55M 총 파라미터(VQ-BeT + DINOv2)로 7.61B의 OpenVLA-OFT를 능가하며, 추론 지연 시간은 10.99 ms 대 61.71 ms입니다. 이는 밀집 특징의 가치가 모델 규모가 아니라 특징 자체의 충실도와 정책 아키텍처의 적합성에 있음을 증명합니다.

## 실험 및 결과

### 시뮬레이션 환경 (Table 1, 100 궤적/시드)
| 방법 | Push-T | LIBERO Goal | BlockPush | Cube |
|---|---|---|---|---|
| WebSSL Patch + VQ-BeT (Ours) | 0.68 ± 0.03 | 0.94 ± 0.01 | 1.68 ± 0.15 | 1.68 ± 0.03 |
| WebSSL Patch + DP (Ours) | 0.80 ± 0.01 | 0.98 ± 0.00 | 1.65 ± 0.08 | 1.73 ± 0.02 |
| WebSSL Avg Pool + DP | 0.79 ± 0.02 | 0.98 ± 0.01 | 1.34 ± 0.02 | 0.21 ± 0.03 |
| OpenVLA-OFT | 0.59 ± 0.02 | 0.95 | 1.43 ± 0.17 | 1.50 ± 0.09 |
| ResNet-18 Patch + ACT | 0.64 ± 0.03 | 0.93 ± 0.02 | 0.15 ± 0.01 | 0.69 ± 0.11 |

### 실제 세계 (Table 2, 20회 시도, DINOv2 Patch + VQ-BeT)
| 작업 | 단계 | Ours | DINOv2 CLS | ACT | OpenVLA-OFT |
|---|---|---|---|---|---|
| Cable Insertion | 완전 삽입 | 0.70 | 0.60 | 0.35 | 0.30 |
| Pen Collection | 세 번째 펜 배치 | 0.85 | 0.65 | 0.65 | 0.60 |
| Tool Hanging | 도구 배치 | 0.90 | 0.70 | 0.85 | 0.65 |

### 계산 자원 (Table 3, H200)
| 방법 | 총 파라미터 | 훈련 가능 파라미터 | 추론 지연 시간 |
|---|---|---|---|
| Ours - VQ-BeT (DINOv2) | 51.55M | 29.49M | 10.99 ms |
| Ours - DP (WebSSL) | 303.66M | 9.35M | 451.68 ms |
| OpenVLA-OFT | 7.61B | 177.90M | 61.71 ms |
| ACT | 83.85M | 83.85M | 8.63 ms |

### 핵심 결론
- 최적 전역 풀링 기준선 대비 상대적 개선 40%(표 내 값 1.73→0.21로 계산); OpenVLA-OFT 대비 18% 능가(표 내 값 1.73→1.50으로 계산), 파라미터는 약 0.7%에 불과.
- 표현 소거 실험(Table 7/8): WebSSL과 DINOv2가 최고 성능, SigLIP2는 전반적으로 최하위(Push-T 0.51 vs DINOv2 0.69).
- 제로샷 일반화(Table 5/6): 실제 세계 픽업 87% vs CAP 79%; EgoGym 폐쇄 작업 92.44% vs 86.50%.

## 경계 및 한계

- 동결된 시각 백본만 평가했으며, 투명 물체나 고반사 표면과 같은 전문 시각 영역에 대한 엔드투엔드 미세 조정의 이점을 탐구하지 않았습니다.
- 밀집 토큰은 시퀀스 길이와 훈련 시간을 증가시키며, FlashAttention과 같은 최적화는 현재 구현에 포함되지 않았습니다.
- 행동 클로닝 정책으로만 검증되었으며 강화 학습으로 확장되지 않았습니다. 정적 전문가 시연의 성능 상한은 돌파되지 않았습니다.
- 시각 표현 선택이 결과에 큰 영향을 미치며(SigLIP2 전면 실패), 논문은 표현 선택에 대한 이론적 기준을 명시하지 않고 경험적 결론만 제공합니다.
- 실제 세계 실험은 DINOv2 (ViT-S)만 사용했으며, WebSSL의 실제 시나리오 전이성을 검증하지 않았습니다.

## 공학적 시사점

- **시각 표현 먼저 확인**: WebSSL과 DINOv2가 현재 최적 선택이며, SigLIP2는 조작 작업에서 체계적으로 실패하므로 재현 시 전자를 우선 사용하세요.
- **어텐션 마스크는 핵심 하이퍼파라미터**: block-causal이 기본 선택입니다. token-causal은 Diffusion Policy에서 Cube 성능 붕괴(0.11)를 초래하므로 반드시 피해야 합니다.
- **모델 크기에는 임계 효과가 존재**: Push-T에서 Diffusion Policy가 25.30M(커버리지 0.56)에서 40.43M(커버리지 0.83)으로 증가할 때 성능이 급등하며, 작은 모델은 밀집 특징을 활용하지 못할 수 있으므로 작업에 따라 N, heads, d_emb를 조정해야 합니다.
- **사전 계산 임베딩은 훈련 가속의 핵심**: 동결된 백본은 패치 특징을 오프라인으로 추출할 수 있게 하여 훈련 비용을 6.5 GPU-hours로 낮출 수 있으며, 공학적으로 이 캐싱 메커니즘을 우선 구현해야 합니다.
- **추론 지연 시간은 액션 청크를 구분해야 함**: 논문에서 보고된 10.99 ms는 단일 순방향 전달이며, receding horizon의 시간 가속은 포함하지 않습니다. 실제 배포 시 이 기술은 직교적으로 추가할 수 있습니다.
