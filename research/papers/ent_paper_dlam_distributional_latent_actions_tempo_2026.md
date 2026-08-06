---
$id: ent_paper_dlam_distributional_latent_actions_tempo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DLAM: Distributional Latent Actions with Temporal Constraints'
  zh: 'DLAM: Distributional Latent Actions with Temporal Constraints'
  ko: 'DLAM: Distributional Latent Actions with Temporal Constraints'
summary:
  en: Vision-language-action (VLA) models remain constrained by scarce action-labeled robot data, whereas action-free videos
    offer abundant observations of physical change. Latent action models can extract such priors, but reconstruction-trained
    codes may predict future observations without the structure required for joint generation with robot actions. Existing
    structured methods add temporal.
  zh: DLAM 将潜在动作模型（LAM）中每个转移的确定性点估计升级为对角高斯分布，使时间一致性约束同时监督均值和逐维方差。该方法在无动作视频上预训练，再冻结编码器迁移到 π0 策略，在 MetaWorld、LIBERO 和真实机器人任务上显著超越确定性基线。核心贡献在于用分布化表示和归一化组合操作，缓解了递归组合中残差误差的累积问题。
  ko: Vision-language-action (VLA) models remain constrained by scarce action-labeled robot data, whereas action-free videos
    offer abundant observations of physical change. Latent action models can extract such priors, but reconstruction-trained
    codes may predict future observations without the structure required for joint generation with robot actions. Existing
    structured methods add temporal.
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
- dlam
- distributional
- latent
- actions
- tempo
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
  title: 'arXiv:2607.27138 DLAM: Distributional Latent Actions with Temporal Constraints'
  url: https://arxiv.org/abs/2607.27138
  date: '2026-07-29'
  accessed_at: '2026-08-05'
---

## 概述

DLAM 将潜在动作模型（LAM）中每个转移的确定性点估计升级为对角高斯分布，使时间一致性约束同时监督均值和逐维方差。该方法在无动作视频上预训练，再冻结编码器迁移到 π0 策略，在 MetaWorld、LIBERO 和真实机器人任务上显著超越确定性基线。核心贡献在于用分布化表示和归一化组合操作，缓解了递归组合中残差误差的累积问题。

## 它改变了什么

潜在动作模型（LAM）的核心矛盾在于：从无动作视频中学习到的潜在转移表示，既要能预测未来观测，又要能支撑下游机器人动作生成。此前结构化方法（如 AC-LAM、ALAM、RotVLA）虽然引入了时间约束，但每个转移仍是确定性点。问题在于，当这些转移在长时程上递归组合时，局部推断的残差误差会逐级传播放大——这不是简单的精度问题，而是表示结构本身的缺陷：确定性点无法表达"这个转移有多确定"，导致组合时所有误差都被等权叠加。

DLAM 真正改变的是将"转移"从点估计变为分布估计。这个转变不是锦上添花，而是从根本上改变了时间约束的作用方式：约束不再只监督均值轨迹，还监督方差如何随组合变化。这使得模型在组合多个转移时，能够通过方差传播来隐式地控制误差累积——不确定的转移在组合时贡献更少的确定性信息。更重要的是，这种分布化并不增加下游推理成本，因为预训练后只取均值，方差纯粹作为训练信号存在。

## 方法拆解

### 分布化转移表示
每个转移 token 的条件后验为对角高斯：
\[ q_{i,\kappa}^{j} = \mathcal{N}(\boldsymbol{\mu}_{i,\kappa}^{j}, \operatorname{diag}((\boldsymbol{\sigma}_{i,\kappa}^{j})^{2})) \]
其中 \(\kappa\) 索引 token 槽位，\(d\) 为 token 宽度。关系编码器 \(E_{\phi}\) 处理两帧并输出均值和对数方差，对数方差经裁剪后转换为标准差。

### 重建路径仅用均值
源条件解码器 \(D_{\omega}\) 从源帧和堆叠转移均值重建目标帧，不使用后验采样。这是关键设计：方差不参与重建，因此不会被"校准不确定性"的目标带偏，而是纯粹作为时间约束的训练信号。

### 归一化组合
对等间隔三元组 \((O_a, O_b, O_c)\)：
- 组合均值：\(\overline{\boldsymbol{\mu}}_{a}^{c} = \frac{\boldsymbol{\mu}_{a}^{b} + \boldsymbol{\mu}_{b}^{c}}{\sqrt{2}}\)
- 组合方差：\((\overline{\boldsymbol{\sigma}}_{a}^{c})^{2} = \frac{(\boldsymbol{\sigma}_{a}^{b})^{2} + (\boldsymbol{\sigma}_{b}^{c})^{2}}{2} + \rho \, \boldsymbol{\sigma}_{a}^{b} \odot \boldsymbol{\sigma}_{b}^{c}\)

\(1/\sqrt{2}\) 因子保证输入为独立标准高斯时组合后仍为单位方差。\(\rho\) 为共享相关系数，通过 \(\rho = \rho_{\max} \tanh(r)\) 学习，固定界 \(0 < \rho_{\max} < 1\) 确保 \(|\rho| < 1\)。

### 反转操作与损失
反转操作 \(\mathcal{R}\) 取反均值、保持方差，应用两次恢复原后验。完整预训练目标：
\[ \mathcal{L}_{\mathrm{DLAM}} = \sum_{s \in \mathcal{S}} \lambda_{s} \mathcal{L}_{s}, \quad \mathcal{S} = \{\mathrm{rec}, \mathrm{prior}, \mathrm{comp}, \mathrm{rev}\} \]
损失权重：\(\lambda_{\mathrm{rec}} = 1\)，\(\lambda_{\mathrm{prior}} = 0.005\)，\(\lambda_{\mathrm{comp}} = \lambda_{\mathrm{rev}} = 0.05\)，\(\lambda_{\ell} = 0.1\)。

### 下游转移
预训练后丢弃重建解码器、冻结转移编码器，仅用后验均值 \(\boldsymbol{\mu}_{h}^{m}\) 作为下游潜在目标。联合流匹配损失同时生成动作流和每视角潜在流，推理时仅执行动作流。

## 关键创新

1. **分布化转移 + 归一化组合**：将时间约束从确定性点扩展到对角高斯，组合操作在保持单位方差的同时引入共享相关系数。这是首个在潜在动作模型中同时约束均值和方差的方案，直接针对递归组合误差累积问题。

2. **方差作为训练信号而非不确定性估计**：由于重建路径仅用均值，方差不会被校准目标污染，可以纯粹服务于时间一致性约束。这个设计决策避免了"方差既要预测未来又要表达不确定性"的目标冲突。

3. **零下游开销的迁移**：预训练后只取均值，不预测方差、不需要潜在到动作解码器、不更换 VLA 骨干。这意味着分布化带来的收益完全在预训练阶段兑现，下游推理成本与确定性基线相同。

## 实验与结果

### MetaWorld MT50（表 1）
| 方法 | Easy | Med | Hard | V-Hard | Avg. |
|------|------|-----|------|--------|------|
| π0 + DLAM | 90.3 | 84.8 | 84.0 | 91.3 | 87.6 |
| π0 + ALAM | 89.3 | 83.6 | 85.0 | 82.0 | 85.0 |
| π0 | 71.8 | 48.2 | 41.7 | 30.0 | 47.9 |
| π0.5 | 68.2 | 37.3 | 41.7 | 28.0 | 43.8 |

DLAM 在 Avg. 上较 ALAM 提升 2.6 个百分点（由表内数值 87.6→85.0 计算），较 π0 提升 39.7 个百分点（由表内数值 87.6→47.9 计算）。

### LIBERO（表 2）
| 方法 | Spatial | Object | Goal | Long | Avg. |
|------|---------|--------|------|------|------|
| π0 + DLAM | 99.6 | 99.8 | 99.6 | 97.1 | 99.0 |
| π0 + ALAM | 99.2 | 99.6 | 99.0 | 94.4 | 98.1 |
| π0 | — | — | — | — | 94.1 |
| π0.5 | — | — | — | — | 96.9 |

DLAM 在 Long 上较 ALAM 提升 2.7 个百分点（由表内数值 97.1→94.4 计算）。

### 重建质量与真实世界
跨 \(3k\)–\(5k\) 跨度，DLAM 直接重建 PSNR 29.14 dB，累积重建 22.40 dB，较 ALAM 分别提升 3.45 dB 和 1.17 dB。LPIPS 降低 45.6%（直接）和 26.1%（累积）。真实世界 4 任务平均成功率：π0 + DLAM 73.8%，π0 + ALAM 63.8%，π0.5 53.8%，π0 40.0%。

### 受控消融（表 3）
| 变体 | PSNR | SSIM | LPIPS | \(R_{\mathrm{comp}}^{\mu}\) | \(R_{\mathrm{rev}}^{\mu}\) | Avg. Success |
|------|------|------|-------|--------------------------|--------------------------|--------------|
| No temporal relations | 21.236 | 0.7894 | 0.1755 | 1.2071 | 1.0314 | 76.6% |
| Matched mean-only | 22.109 | 0.8057 | 0.1644 | 1.1808 | 1.0371 | 82.1% |
| Learned variance (ρ=0) | 22.084 | 0.8067 | 0.1637 | 1.1777 | 1.0341 | 85.3% |
| Full DLAM | 22.400 | 0.8086 | 0.1623 | 1.1662 | 1.0010 | 87.6% |

归一化均值约束将成功率从 76.6% 提升至 82.1%，学习方差（ρ=0）再提升至 85.3%，完整 DLAM 较无时间关系变体提升 11.0 个百分点。

## 边界与局限

DLAM 仅对等间隔三元组施加局部约束，长时程泛化仍是开放问题——时间一致性诊断只反映所评估跨度上的行为，不构成任意时域的通用保证。方差目标可能允许近似常数解，且由于下游仅用均值，方差始终只是辅助训练信号而非校准不确定性。共享相关系数 \(\rho\) 跨样本、token 槽位和潜在维度共享，可能遗漏上下文相关或维度相关的依赖关系。均值探针不测试超出监督跨度的相关感知方差组合。论文未明确在非等间隔时间步或非机器人操作场景下的表现。

## 工程启示

复现时先核对三个关键点：一是归一化组合中的 \(1/\sqrt{2}\) 因子是否在实现中正确应用，这直接影响组合后方差是否保持单位尺度；二是对数方差裁剪边界 \(\ell_{\min}, \ell_{\max}\) 的具体取值，论文未明确，这会影响训练稳定性；三是共享相关系数 \(\rho\) 的初始化与 \(\rho_{\max}\) 取值，论文未明确，建议从较小值开始。最容易踩坑的地方是下游转移时"仅用均值"——如果误将方差也传入策略，会改变训练分布且无收益。预训练硬件为 64 块 AMD MI308X GPU，训练 57 个 epoch，策略转移学习率 \(5 \times 10^{-5}\)，这些配置对复现成功率有直接影响。对于下游团队，DLAM 的价值在于预训练成本一次投入、下游零额外开销，适合作为 VLA 基座的通用预训练模块。

## Overview
Vision-language-action (VLA) models remain constrained by scarce action-labeled robot data, whereas action-free videos offer abundant observations of physical change. Latent action models can extract such priors, but reconstruction-trained codes may predict future observations without the structure required for joint generation with robot actions. Existing structured methods add temporal constraints but retain deterministic transition points, so residual errors in locally inferred transitions may propagate and compound under recursive composition. We introduce DLAM, a distributional latent-action model that represents each transition as a diagonal Gaussian. Reconstruction conditioned on the reference frame grounds the mean in observed visual change, while normalized composition and reversal over equal-gap triplets constrain both the mean and dimension-wise variance. Variance composition uses a lightweight shared-correlation coefficient to account for dependence between adjacent transitions that share an intermediate frame, whereas reversal negates the mean and preserves the variance. For downstream policy learning, we freeze the encoder and train a flow-matching policy to jointly generate mean transition sequences and robot actions. On held-out transitions, DLAM learns more temporally consistent latent dynamics than existing latent-action baselines and achieves stronger direct and cumulative reconstruction on held-out videos. Under the same controlled $π_0$ transfer protocol, it also improves policy performance on MetaWorld MT50, LIBERO, and real-world manipulation tasks. Controlled ablations show that normalized mean constraints account for most of the reconstruction gain, while learned variance and correlation-aware composition provide complementary improvements in downstream control.

## 参考
- https://arxiv.org/abs/2607.27138

## 개요

DLAM은 잠재 행동 모델(LAM)의 각 전이에 대한 결정론적 점 추정을 대각 가우시안 분포로 업그레이드하여, 시간 일관성 제약이 평균과 차원별 분산을 동시에 감독하도록 합니다. 이 방법은 행동 없는 비디오에서 사전 학습한 후, 인코더를 동결하여 π0 정책으로 전이하며, MetaWorld, LIBERO 및 실제 로봇 작업에서 결정론적 기준선을 크게 능가합니다. 핵심 기여는 분포화 표현과 정규화된 조합 연산을 통해 재귀적 조합에서 잔차 오류 누적 문제를 완화하는 데 있습니다.

## 무엇을 바꾸었는가

잠재 행동 모델(LAM)의 핵심 모순은 행동 없는 비디오에서 학습된 잠재 전이 표현이 미래 관측을 예측할 수 있어야 할 뿐만 아니라, 하위 로봇 행동 생성을 지원해야 한다는 점입니다. 이전의 구조화된 방법(AC-LAM, ALAM, RotVLA 등)은 시간 제약을 도입했지만, 각 전이는 여전히 결정론적 점이었습니다. 문제는 이러한 전이가 장시간에 걸쳐 재귀적으로 조합될 때, 국소 추론의 잔차 오류가 단계적으로 전파되고 증폭된다는 것입니다. 이는 단순한 정밀도 문제가 아니라 표현 구조 자체의 결함입니다. 결정론적 점은 "이 전이가 얼마나 확실한지"를 표현할 수 없어, 조합 시 모든 오류가 동등하게 가중되어 중첩됩니다.

DLAM이 진정으로 바꾼 것은 "전이"를 점 추정에서 분포 추정으로 전환한 것입니다. 이 전환은 단순한 개선이 아니라 시간 제약이 작동하는 방식을 근본적으로 바꿉니다. 제약이 더 이상 평균 궤적만 감독하는 것이 아니라 분산이 조합에 따라 어떻게 변하는지도 감독합니다. 이를 통해 모델은 여러 전이를 조합할 때 분산 전파를 통해 오류 누적을 암시적으로 제어할 수 있습니다. 불확실한 전이는 조합 시 더 적은 결정적 정보를 기여합니다. 더 중요한 것은, 이러한 분포화가 하위 추론 비용을 증가시키지 않는다는 점입니다. 사전 학습 후에는 평균만 사용하고 분산은 순수하게 훈련 신호로만 존재하기 때문입니다.

## 방법 분해

### 분포화 전이 표현
각 전이 토큰의 조건부 사후는 대각 가우시안입니다:
\[ q_{i,\kappa}^{j} = \mathcal{N}(\boldsymbol{\mu}_{i,\kappa}^{j}, \operatorname{diag}((\boldsymbol{\sigma}_{i,\kappa}^{j})^{2})) \]
여기서 \(\kappa\)는 토큰 슬롯을 인덱싱하고, \(d\)는 토큰 너비입니다. 관계 인코더 \(E_{\phi}\)는 두 프레임을 처리하여 평균과 로그 분산을 출력하며, 로그 분산은 클리핑 후 표준 편차로 변환됩니다.

### 재구성 경로는 평균만 사용
소스 조건 디코더 \(D_{\omega}\)는 소스 프레임과 쌓인 전이 평균에서 대상 프레임을 재구성하며, 사후 샘플링을 사용하지 않습니다. 이는 핵심 설계입니다. 분산은 재구성에 참여하지 않으므로 "불확실성 보정" 목표에 치우치지 않고, 순수하게 시간 제약의 훈련 신호로만 작용합니다.

### 정규화된 조합
등간격 삼중항 \((O_a, O_b, O_c)\)에 대해:
- 조합 평균: \(\overline{\boldsymbol{\mu}}_{a}^{c} = \frac{\boldsymbol{\mu}_{a}^{b} + \boldsymbol{\mu}_{b}^{c}}{\sqrt{2}}\)
- 조합 분산: \((\overline{\boldsymbol{\sigma}}_{a}^{c})^{2} = \frac{(\boldsymbol{\sigma}_{a}^{b})^{2} + (\boldsymbol{\sigma}_{b}^{c})^{2}}{2} + \rho \, \boldsymbol{\sigma}_{a}^{b} \odot \boldsymbol{\sigma}_{b}^{c}\)

\(1/\sqrt{2}\) 인자는 입력이 독립 표준 가우시안일 때 조합 후에도 단위 분산을 유지하도록 보장합니다. \(\rho\)는 공유 상관 계수로, \(\rho = \rho_{\max} \tanh(r)\)로 학습되며, 고정 경계 \(0 < \rho_{\max} < 1\)는 \(|\rho| < 1\)을 보장합니다.

### 반전 연산과 손실
반전 연산 \(\mathcal{R}\)은 평균을 반전시키고 분산을 유지하며, 두 번 적용하면 원래 사후로 복원됩니다. 전체 사전 학습 목표:
\[ \mathcal{L}_{\mathrm{DLAM}} = \sum_{s \in \mathcal{S}} \lambda_{s} \mathcal{L}_{s}, \quad \mathcal{S} = \{\mathrm{rec}, \mathrm{prior}, \mathrm{comp}, \mathrm{rev}\} \]
손실 가중치: \(\lambda_{\mathrm{rec}} = 1\), \(\lambda_{\mathrm{prior}} = 0.005\), \(\lambda_{\mathrm{comp}} = \lambda_{\mathrm{rev}} = 0.05\), \(\lambda_{\ell} = 0.1\).

### 하위 전이
사전 학습 후 재구성 디코더를 폐기하고 전이 인코더를 동결하며, 사후 평균 \(\boldsymbol{\mu}_{h}^{m}\)만 하위 잠재 목표로 사용합니다. 결합 흐름 매칭 손실은 행동 흐름과 각 시점의 잠재 흐름을 동시에 생성하며, 추론 시에는 행동 흐름만 실행합니다.

## 핵심 혁신

1. **분포화 전이 + 정규화된 조합**: 시간 제약을 결정론적 점에서 대각 가우시안으로 확장하고, 조합 연산이 단위 분산을 유지하면서 공유 상관 계수를 도입합니다. 이는 잠재 행동 모델에서 평균과 분산을 동시에 제약하는 최초의 방법으로, 재귀적 조합 오류 누적 문제를 직접적으로 해결합니다.

2. **불확실성 추정이 아닌 훈련 신호로서의 분산**: 재구성 경로가 평균만 사용하므로 분산은 보정 목표에 오염되지 않고 순수하게 시간 일관성 제약에 기여할 수 있습니다. 이 설계 결정은 "분산이 미래 예측과 불확실성 표현을 동시에 담당해야 하는" 목표 충돌을 피합니다.

3. **하위 오버헤드가 없는 전이**: 사전 학습 후 평균만 사용하며, 분산을 예측하지 않고, 잠재-행동 디코더를 교체하지 않으며, VLA 백본을 변경하지 않습니다. 이는 분포화의 이점이 전적으로 사전 학습 단계에서 실현되며, 하위 추론 비용은 결정론적 기준선과 동일함을 의미합니다.

## 실험 및 결과

### MetaWorld MT50 (표 1)
| 방법 | Easy | Med | Hard | V-Hard | Avg. |
|------|------|-----|------|--------|------|
| π0 + DLAM | 90.3 | 84.8 | 84.0 | 91.3 | 87.6 |
| π0 + ALAM | 89.3 | 83.6 | 85.0 | 82.0 | 85.0 |
| π0 | 71.8 | 48.2 | 41.7 | 30.0 | 47.9 |
| π0.5 | 68.2 | 37.3 | 41.7 | 28.0 | 43.8 |

DLAM은 Avg.에서 ALAM 대비 2.6% 포인트(표 내 값 87.6→85.0으로 계산), π0 대비 39.7% 포인트(표 내 값 87.6→47.9로 계산) 향상되었습니다.

### LIBERO (표 2)
| 방법 | Spatial | Object | Goal | Long | Avg. |
|------|---------|--------|------|------|------|
| π0 + DLAM | 99.6 | 99.8 | 99.6 | 97.1 | 99.0 |
| π0 + ALAM | 99.2 | 99.6 | 99.0 | 94.4 | 98.1 |
| π0 | — | — | — | — | 94.1 |
| π0.5 | — | — | — | — | 96.9 |

DLAM은 Long에서 ALAM 대비 2.7% 포인트(표 내 값 97.1→94.4로 계산) 향상되었습니다.

### 재구성 품질 및 실제 세계
\(3k\)–\(5k\) 범위에 걸쳐 DLAM 직접 재구성 PSNR 29.14 dB, 누적 재구성 22.40 dB로 ALAM 대비 각각 3.45 dB 및 1.17 dB 향상되었습니다. LPIPS는 45.6%(직접) 및 26.1%(누적) 감소했습니다. 실제 세계 4개 작업 평균 성공률: π0 + DLAM 73.8%, π0 + ALAM 63.8%, π0.5 53.8%, π0 40.0%.

### 통제된 절제 연구 (표 3)
| 변형 | PSNR | SSIM | LPIPS | \(R_{\mathrm{comp}}^{\mu}\) | \(R_{\mathrm{rev}}^{\mu}\) | Avg. Success |
|------|------|------|-------|--------------------------|--------------------------|--------------|
| 시간 관계 없음 | 21.236 | 0.7894 | 0.1755 | 1.2071 | 1.0314 | 76.6% |
| 평균만 일치 | 22.109 | 0.8057 | 0.1644 | 1.1808 | 1.0371 | 82.1% |
| 학습된 분산 (ρ=0) | 22.084 | 0.8067 | 0.1637 | 1.1777 | 1.0341 | 85.3% |
| 전체 DLAM | 22.400 | 0.8086 | 0.1623 | 1.1662 | 1.0010 | 87.6% |

정규화된 평균 제약은 성공률을 76.6%에서 82.1%로 향상시키고, 학습된 분산(ρ=0)은 85.3%로 추가 향상시키며, 전체 DLAM은 시간 관계 없는 변형 대비 11.0% 포인트 향상되었습니다.

## 경계 및 한계

DLAM은 등간격 삼중항에만 국소 제약을 적용하므로, 장시간 일반화는 여전히 열린 문제입니다. 시간 일관성 진단은 평가된 범위에서의 행동만 반영하며, 임의 시간 영역에 대한 일반적 보장을 구성하지 않습니다. 분산 목표는 근사 상수 해를 허용할 수 있으며, 하위에서 평균만 사용하므로 분산은 항상 보조 훈련 신호일 뿐 보정된 불확실성이 아닙니다. 공유 상관 계수 \(\rho\)는 샘플, 토큰 슬롯 및 잠재 차원에 걸쳐 공유되므로, 맥락 관련 또는 차원 관련 의존성을 놓칠 수 있습니다. 평균 프로브는 감독 범위를 초과하는 상관 인식 분산 조합을 테스트하지 않습니다. 논문은 비등간격 시간 단계 또는 비로봇 조작 시나리오에서의 성능을 명시하지 않았습니다.

## 공학적 시사점

재현 시 세 가지 핵심 사항을 먼저 확인하십시오: 첫째, 정규화된 조합의 \(1/\sqrt{2}\) 인자가 구현에서 올바르게 적용되었는지 — 이는 조합 후 분산이 단위 스케일을 유지하는지에 직접 영향을 줍니다. 둘째, 로그 분산 클리핑 경계 \(\ell_{\min}, \ell_{\max}\)의 구체적인 값 — 논문에 명시되지 않았으며, 이는 훈련 안정성에 영향을 줍니다. 셋째, 공유 상관 계수 \(\rho\)의 초기화 및 \(\rho_{\max}\) 값 — 논문에 명시되지 않았으며, 작은 값에서 시작하는 것이 좋습니다. 가장 함정에 빠지기 쉬운 부분은 하위 전이 시 "평균만 사용"하는 것입니다. 실수로 분산도 정책에 전달하면 훈련 분포가 변경되고 이점이 없습니다. 사전 학습 하드웨어는 64개의 AMD MI308X GPU, 훈련 57 에폭, 정책 전이 학습률 \(5 \times 10^{-5}\)로, 이러한 구성은 재현 성공률에 직접적인 영향을 미칩니다. 하위 팀의 경우, DLAM의 가치는 사전 학습 비용이 일회성으로 투입되고 하위에서 추가 오버헤드가 없다는 점에 있으며, VLA 기반의 범용 사전 학습 모듈로 적합합니다.
