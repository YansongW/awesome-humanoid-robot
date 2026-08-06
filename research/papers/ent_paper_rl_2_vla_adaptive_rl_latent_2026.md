---
$id: ent_paper_rl_2_vla_adaptive_rl_latent_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models'
  zh: 'RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models'
  ko: 'RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models'
summary:
  en: Despite the impressive visuomotor capabilities enabled by Vision-Language-Action (VLA) models, their performance often
    degrades on challenging and out-of-domain tasks. Recent test-time steering and scaling methods improve performance without
    extensive data collection and retraining, but action samples often remain concentrated around similar behaviors and therefore
    inherit correlated failure.
  zh: RL²-VLA 提出一种自适应推理时转向框架，通过轻量级离线 RL 策略在 VLA 潜在空间上生成多样化动作候选，并利用失败检测器仅在基础策略可能失败时触发组合式转向。核心贡献在于将“何时转向”与“如何转向”解耦，用共形预测校准的
    SAFE 检测器实现按需干预，在 SIMPLER、PolaRiS 及真实机器人上显著提升 OOD 鲁棒性。
  ko: Despite the impressive visuomotor capabilities enabled by Vision-Language-Action (VLA) models, their performance often
    degrades on challenging and out-of-domain tasks. Recent test-time steering and scaling methods improve performance without
    extensive data collection and retraining, but action samples often remain concentrated around similar behaviors and therefore
    inherit correlated failure.
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
- rl
- '2'
- vla
- adaptive
- rl
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
  title: 'arXiv:2607.26991 RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for'
  url: https://arxiv.org/abs/2607.26991
  date: '2026-07-29'
  accessed_at: '2026-08-05'
---

## 概述

RL²-VLA 提出一种自适应推理时转向框架，通过轻量级离线 RL 策略在 VLA 潜在空间上生成多样化动作候选，并利用失败检测器仅在基础策略可能失败时触发组合式转向。核心贡献在于将“何时转向”与“如何转向”解耦，用共形预测校准的 SAFE 检测器实现按需干预，在 SIMPLER、PolaRiS 及真实机器人上显著提升 OOD 鲁棒性。

## 它改变了什么

现有测试时缩放方法（如 Repeated/Rephrase）生成的动作样本高度同质，继承基础 VLA 的相同失败模式；而可微转向方法受限于预训练 VLM 的物理基础缺陷。更关键的是，所有方法在每个时间步施加相同干预强度，不区分当前状态基础策略是否可能成功——这在分布内任务上反而引入不必要的扰动，降低已准确的动作质量。

RL² 真正改变了“干预策略”的粒度：它把转向从“全局固定”变为“状态自适应”。通过轻量级失败检测器（SAFE）实时判断基础 VLA 是否处于失败风险，仅在必要时激活组合转向，否则回退到原始策略。这避免了“一刀切”干预的副作用，使得同一套框架既能提升 OOD 鲁棒性（+17.3%），又不牺牲分布内性能。

## 方法拆解

### 1. 潜在空间 RL 策略训练（如何转向）
- 在 VLA 内部特征（如 π₀ 的 1024 维嵌入）上训练轻量级流匹配策略，而非原始观测。
- 使用 QAM（Q-learning with Adjoint Matching）替代反向传播：通过伴随状态 g̃_t 从终端动作反推时间相关引导信号，匹配损失为：
  L_AM = E ∫₀¹ ||2(f_θ - f_β)/σ_t + σ_t g̃_t||² dt，其中 σ_t = √(2(1-t)/t)。
- 策略收敛到 π(a|s) ∝ π_β(a|s)exp(τQ(s,a))，逆温度 τ 控制探索-利用平衡（π₀ 用 0.1，π₀.₅ 用 0.02）。

### 2. 组合式转向（Compositional Steering）
- 速度场加权组合：v_comp ← w·v_VLA + (1-w)·v_RL，权重 w 从高斯分布（μ=0.5，σ=0.25）采样并裁剪到 [0,1]。
- 对自回归 VLA（如 OpenVLA），先拟合 VLA 与 RL 样本等量混合的高斯分布，再从拟合分布采样更大批次。
- 设计理由：VLA 提供大规模但固有缺陷的行为先验，离线 RL 诱导超越主导演示模式的多样性，两者互补。

### 3. 自适应触发（何时转向）
- SAFE 检测器：LSTM 接收 VLA 内部特征序列 e_{0:t}，输出失败分数 s_t ∈ [0,1]，用二元交叉熵训练。
- 共形预测校准：对每个任务分别校准时变阈值带 C_α = {[lower_t, upper_t]}，upper_t = μ_t + h_t，保证新成功 rollout 满足 s_t < upper_t 的概率至少 1-α。
- α 选择启发式：在验证集上扫描候选 α 值，用平衡准确率 BalAcc = ½(TPR + TNR) 选择最优；若并列，则根据 RL 策略相对 VLA 的独立表现打破平局（RL 更优时选更大 α 以允许更频繁干预）。

### 4. 动作验证
- 验证器（CoVer 或 RoboMonkey）为每个候选动作打分 r_t^n = V_θ(o_t, â_t^n, l_t)，选择最高分样本 â_t*。

## 关键创新

1. **状态自适应的转向时机**：首次将失败检测（SAFE）与测试时缩放结合，用共形预测提供统计保证的触发阈值。相比“Always 转向”或“CoVer 触发”，SAFE 在 PolaRiS 上平均成功率提升 +3.5%（由表内 42.7 vs 39.8 计算），且成功/失败分数更易分离（ROC-AUC 最高 90.4%）。

2. **潜在空间 RL 而非观测空间**：在 VLA 内部特征（1024 维）上训练 RL 策略，而非用小型 ResNet 编码器。消融显示潜在空间带来 +38.8% 提升（OpenVLA 上无潜在空间 RL 仅 0.5% 成功率），因为 VLA 特征已编码丰富的语义与物理先验。

3. **组合式速度场加权**：不同于直接替换或拼接动作，通过速度加权（w 从高斯采样）实现软组合，既保留 VLA 的大规模先验，又注入 RL 的多样性。缩放实验显示样本数 1→40 时 RL² 性能提升 +18.7%，优于 Rephrase 的饱和曲线。

## 实验与结果

| 设置 | 基线 | RL² 自适应 | 提升 |
|---|---|---|---|
| SIMPLER 域内（OpenVLA） | Repeated 最强 | 任务级最高 | +19.4%（平均 +7.5%） |
| SIMPLER OOD 语言（π₀） | Rephrase 最强 | 任务级最高 | +14.7%（平均 +10.1%） |
| PolaRiS OOD 语言（π₀.₅） | Rephrase 最强 | 平均成功率 | +10.9%（Move Latte Cup +17.3%） |
| SIMPLER OOD 环境（π₀） | Rephrase 最强 | 平均 | +8.5%（Spoon on Towel - Google +14.6%） |
| 真实机器人（PiperX） | Rephrase 最强 | 平均成功率 | +17.5% |

- 消融：自适应 vs 非自适应平均 +8.9%（任务级 +16.7%）；RL vs BC +4.5%；SAFE vs CoVer +3.5%。
- 缩放定律：失败元组下 RL² 组合转向表现出最强缩放行为（NRMSE 显著更低），成功元组下多数方法比 Rephrase 差，验证了“仅在失败时转向”的必要性。
- 时间开销：SAFE 推理恒为 1ms（H100），QAM 为 9-25ms，远低于 π₀ 的 219-698ms，适合实时部署。

## 边界与局限

- 未与大型 VLM 的可微引导方法（如 ConRFT、Policy Decorator）比较，这些方法可能在不同规模下表现不同。
- α 选择启发式需要为每个新任务重新执行一次验证集扫描，增加部署成本；论文未明确扫描的完整 α 范围。
- 失败检测器依赖在线 rollout 收集训练数据（每任务 100 个 rollout），未利用大规模离线数据集，可能限制跨任务泛化。
- 真实世界实验仅评估 π₀，未覆盖 π₀.₅ 或 OpenVLA；工具箱任务存在动作高度限制，可能低估方法在更复杂操作上的表现。
- 假设存在稳健的验证器（CoVer/RoboMonkey），未联合训练 RL 策略与验证器，验证器误差可能成为瓶颈。

## 工程启示

- **先核对验证器质量**：RL² 依赖验证器选择最优动作，若验证器本身在 OOD 上不可靠（如 CoVer 在 PolaRiS 上触发效果差于 SAFE），整体收益会大打折扣。建议先评估验证器的 ROC-AUC 是否高于 80%。
- **潜在空间维度决定训练成本**：QAM 训练时间主要由 VLA 嵌入维度决定（π₀ 的 1024 维需 4.5 小时，OpenVLA 的 4096 维需 48 小时）。复现时优先选择低维潜在空间的 VLA（如 π₀），或考虑降维。
- **最容易踩坑：α 选择与阈值校准**：共形预测的阈值带需按任务分别校准，且 α 选择启发式依赖 RL 策略与 VLA 的相对表现。若 RL 策略训练不充分（如逆温度 τ 过大导致探索不足），启发式可能选错 α，导致过度或不足干预。
- **组合权重 w 的采样分布**：高斯 μ=0.5、σ=0.25 是经验值，对自回归 VLA（OpenVLA）需改用高斯扰动策略（拟合混合分布再采样）。切换 VLA 架构时必须重新验证此超参数。
- **推理时延预算**：SAFE（1ms）和 QAM（<25ms）开销可忽略，但验证器 CoVer 在 batch size 128 时需 145ms（RTX 5090），若动作批次过大可能成为瓶颈。建议控制候选样本数在 40 以内（缩放实验显示 40 样本时收益已饱和）。

## Overview
Despite the impressive visuomotor capabilities enabled by Vision-Language-Action (VLA) models, their performance often degrades on challenging and out-of-domain tasks. Recent test-time steering and scaling methods improve performance without extensive data collection and retraining, but action samples often remain concentrated around similar behaviors and therefore inherit correlated failure modes. Moreover, existing methods apply the same intervention strategy at every timestep, regardless of whether the base policy is already likely to succeed. To address these limitations, we introduce $RL^2$, an adaptive inference-time steering framework that leverages Reinforcement Learning on VLA Latents. First, we train a lightweight offline RL policy conditioned on expressive latents extracted from the VLA action expert and compose its flow velocity with that of the frozen VLA during inference. This compositional steering strategy combines the behavioral priors of large-scale imitation learning with the action diversity induced by offline RL beyond dominant demonstration modes. We further discover that inference-time steering follows fundamentally different scaling laws under success and failure states, revealing that action diversity is most beneficial when the base VLA is likely to fail, but can unnecessarily perturb already-accurate actions when success is likely. Building on this insight, $RL^2$ activates compositional steering only when failure is predicted. Across the SIMPLER and PolaRiS benchmarks, $RL^2$ improves success rates by up to +17.3% in out-of-domain settings, while ablations and scaling studies demonstrate the importance of latent representations and RL training. Finally, real-world experiments demonstrate that these gains transfer beyond simulation, establishing $RL^2$ as a practical and modular steering framework for VLA deployment.

## 参考
- https://arxiv.org/abs/2607.26991

## 개요

RL²-VLA는 경량 오프라인 RL 정책을 VLA 잠재 공간에 적용하여 다양한 행동 후보를 생성하고, 실패 감지기를 활용하여 기본 정책이 실패할 가능성이 있을 때만 구성적 스티어링을 트리거하는 적응형 추론 시점 스티어링 프레임워크를 제안합니다. 핵심 기여는 "언제 스티어링할지"와 "어떻게 스티어링할지"를 분리하고, 공형 예측으로 보정된 SAFE 감지기를 통해 온디맨드 개입을 구현하여 SIMPLER, PolaRiS 및 실제 로봇에서 OOD 견고성을 크게 향상시키는 것입니다.

## 무엇을 바꾸었는가

기존 테스트 시점 스케일링 방법(예: Repeated/Rephrase)은 생성된 행동 샘플이 매우 동질적이며 기본 VLA의 동일한 실패 패턴을 계승합니다. 반면 미분 가능한 스티어링 방법은 사전 훈련된 VLM의 물리적 기반 결함에 제한됩니다. 더 중요한 것은 모든 방법이 매 시간 스텝마다 동일한 개입 강도를 적용하여 현재 상태에서 기본 정책이 성공할 가능성이 있는지 구분하지 않는다는 점입니다. 이는 분포 내 작업에서 오히려 불필요한 교란을 도입하여 이미 정확한 행동 품질을 저하시킵니다.

RL²는 실제로 "개입 정책"의 세분성을 변경합니다. 스티어링을 "전역 고정"에서 "상태 적응형"으로 전환합니다. 경량 실패 감지기(SAFE)를 통해 기본 VLA가 실패 위험에 있는지 실시간으로 판단하고, 필요한 경우에만 구성적 스티어링을 활성화하며, 그렇지 않으면 원래 정책으로 폴백합니다. 이는 "일괄 적용" 개입의 부작용을 피하여 동일한 프레임워크가 OOD 견고성(+17.3%)을 향상시키면서도 분포 내 성능을 희생하지 않도록 합니다.

## 방법 분해

### 1. 잠재 공간 RL 정책 훈련 (어떻게 스티어링할지)
- 원시 관측이 아닌 VLA 내부 특징(예: π₀의 1024차원 임베딩)에서 경량 플로우 매칭 정책을 훈련합니다.
- 역전파 대신 QAM(Q-learning with Adjoint Matching)을 사용합니다. 수반 상태 g̃_t를 통해 터미널 행동에서 시간 의존적 안내 신호를 역산하며, 매칭 손실은 다음과 같습니다:
  L_AM = E ∫₀¹ ||2(f_θ - f_β)/σ_t + σ_t g̃_t||² dt, 여기서 σ_t = √(2(1-t)/t)입니다.
- 정책은 π(a|s) ∝ π_β(a|s)exp(τQ(s,a))로 수렴하며, 역온도 τ가 탐험-활용 균형을 제어합니다(π₀는 0.1, π₀.₅는 0.02).

### 2. 구성적 스티어링 (Compositional Steering)
- 속도장 가중 결합: v_comp ← w·v_VLA + (1-w)·v_RL, 가중치 w는 가우시안 분포(μ=0.5, σ=0.25)에서 샘플링하여 [0,1]로 클리핑합니다.
- 자기회귀 VLA(예: OpenVLA)의 경우, 먼저 VLA와 RL 샘플을 동일 비율로 혼합한 가우시안 분포를 피팅한 후, 피팅된 분포에서 더 큰 배치를 샘플링합니다.
- 설계 근거: VLA는 대규모이지만 고유한 결함이 있는 행동 사전을 제공하고, 오프라인 RL은 주류 데모 패턴을 넘어서는 다양성을 유도하여 서로 보완합니다.

### 3. 적응형 트리거 (언제 스티어링할지)
- SAFE 감지기: LSTM이 VLA 내부 특징 시퀀스 e_{0:t}를 수신하고 실패 점수 s_t ∈ [0,1]을 출력하며, 이진 교차 엔트로피로 훈련됩니다.
- 공형 예측 보정: 각 작업에 대해 시간 변화 임계값 밴드 C_α = {[lower_t, upper_t]}를 개별적으로 보정하며, upper_t = μ_t + h_t로 새로운 성공 rollout이 s_t < upper_t를 만족할 확률이 최소 1-α가 되도록 보장합니다.
- α 선택 휴리스틱: 검증 세트에서 후보 α 값을 스캔하고 균형 정확도 BalAcc = ½(TPR + TNR)로 최적 값을 선택합니다. 동률인 경우 RL 정책의 VLA 대비 독립 성능으로 결정합니다(RL이 더 우수하면 더 큰 α를 선택하여 더 빈번한 개입 허용).

### 4. 행동 검증
- 검증기(CoVer 또는 RoboMonkey)가 각 후보 행동에 점수 r_t^n = V_θ(o_t, â_t^n, l_t)를 부여하고 최고 점수 샘플 â_t*를 선택합니다.

## 핵심 혁신

1. **상태 적응형 스티어링 타이밍**: 실패 감지(SAFE)를 테스트 시점 스케일링과 처음으로 결합하고, 공형 예측으로 통계적 보장이 있는 트리거 임계값을 제공합니다. "항상 스티어링" 또는 "CoVer 트리거"와 비교하여 SAFE는 PolaRiS에서 평균 성공률 +3.5% 향상(표 내 42.7 vs 39.8 계산)을 보이며, 성공/실패 점수 분리가 더 용이합니다(ROC-AUC 최대 90.4%).

2. **관측 공간이 아닌 잠재 공간 RL**: 소형 ResNet 인코더 대신 VLA 내부 특징(1024차원)에서 RL 정책을 훈련합니다. 절제 실험에서 잠재 공간이 +38.8% 향상을 가져옵니다(OpenVLA에서 잠재 공간 RL 없이는 성공률 0.5%에 불과). VLA 특징이 풍부한 의미론적 및 물리적 사전을 이미 인코딩하기 때문입니다.

3. **구성적 속도장 가중**: 직접 교체나 행동 연결 대신 속도 가중(w를 가우시안에서 샘플링)으로 소프트 결합을 구현하여 VLA의 대규모 사전을 보존하면서 RL의 다양성을 주입합니다. 스케일링 실험에서 샘플 수 1→40일 때 RL² 성능이 +18.7% 향상되어 Rephrase의 포화 곡선보다 우수합니다.

## 실험 및 결과

| 설정 | 기준선 | RL² 적응형 | 향상 |
|---|---|---|---|
| SIMPLER 도메인 내(OpenVLA) | Repeated 최강 | 작업 수준 최고 | +19.4%(평균 +7.5%) |
| SIMPLER OOD 언어(π₀) | Rephrase 최강 | 작업 수준 최고 | +14.7%(평균 +10.1%) |
| PolaRiS OOD 언어(π₀.₅) | Rephrase 최강 | 평균 성공률 | +10.9%(Move Latte Cup +17.3%) |
| SIMPLER OOD 환경(π₀) | Rephrase 최강 | 평균 | +8.5%(Spoon on Towel - Google +14.6%) |
| 실제 로봇(PiperX) | Rephrase 최강 | 평균 성공률 | +17.5% |

- 절제: 적응형 vs 비적응형 평균 +8.9%(작업 수준 +16.7%); RL vs BC +4.5%; SAFE vs CoVer +3.5%.
- 스케일링 법칙: 실패 튜플에서 RL² 구성적 스티어링이 가장 강한 스케일링 동작을 보이며(NRMSE가 현저히 낮음), 성공 튜플에서는 대부분의 방법이 Rephrase보다 나빠 "실패 시에만 스티어링"의 필요성을 검증합니다.
- 시간 오버헤드: SAFE 추론은 항상 1ms(H100), QAM은 9-25ms로 π₀의 219-698ms보다 훨씬 낮아 실시간 배포에 적합합니다.

## 경계 및 한계

- 대형 VLM의 미분 가능한 안내 방법(예: ConRFT, Policy Decorator)과 비교하지 않았으며, 이러한 방법은 다른 규모에서 다르게 동작할 수 있습니다.
- α 선택 휴리스틱은 각 새 작업에 대해 검증 세트 스캔을 다시 실행해야 하므로 배포 비용이 증가합니다. 논문은 스캔의 전체 α 범위를 명시하지 않았습니다.
- 실패 감지기는 온라인 rollout 수집 훈련 데이터(작업당 100개 rollout)에 의존하며 대규모 오프라인 데이터 세트를 활용하지 않아 교차 작업 일반화를 제한할 수 있습니다.
- 실제 세계 실험은 π₀만 평가하고 π₀.₅ 또는 OpenVLA를 다루지 않습니다. 도구 상자 작업은 행동 제약이 높아 더 복잡한 조작에서 방법의 성능을 과소평가할 수 있습니다.
- 견고한 검증기(CoVer/RoboMonkey)가 존재한다고 가정하며 RL 정책과 검증기를 공동 훈련하지 않아 검증기 오류가 병목이 될 수 있습니다.

## 엔지니어링 시사점

- **검증기 품질 먼저 확인**: RL²는 검증기에 의존하여 최적 행동을 선택하므로, 검증기 자체가 OOD에서 신뢰할 수 없으면(예: PolaRiS에서 CoVer 트리거가 SAFE보다 나쁨) 전체 이점이 크게 감소합니다. 검증기의 ROC-AUC가 80% 이상인지 먼저 평가하는 것이 좋습니다.
- **잠재 공간 차원이 훈련 비용 결정**: QAM 훈련 시간은 주로 VLA 임베딩 차원에 의해 결정됩니다(π₀의 1024차원은 4.5시간, OpenVLA의 4096차원은 48시간 필요). 재현 시 저차원 잠재 공간의 VLA(예: π₀)를 우선 선택하거나 차원 축소를 고려하세요.
- **가장 쉽게 실수하는 부분: α 선택 및 임계값 보정**: 공형 예측의 임계값 밴드는 작업별로 개별 보정해야 하며, α 선택 휴리스틱은 RL 정책과 VLA의 상대적 성능에 의존합니다. RL 정책 훈련이 불충분하면(예: 역온도 τ가 너무 커 탐험이 부족) 휴리스틱이 잘못된 α를 선택하여 과도하거나 부족한 개입을 초래할 수 있습니다.
- **결합 가중치 w의 샘플링 분포**: 가우시안 μ=0.5, σ=0.25는 경험적 값이며, 자기회귀 VLA(OpenVLA)의 경우 가우시안 교란 전략(혼합 분포 피팅 후 재샘플링)으로 변경해야 합니다. VLA 아키텍처를 전환할 때 이 하이퍼파라미터를 반드시 재검증하세요.
- **추론 지연 예산**: SAFE(1ms) 및 QAM(<25ms) 오버헤드는 무시할 수 있지만, 검증기 CoVer는 배치 크기 128에서 145ms(RTX 5090)가 필요하므로 행동 배치가 너무 크면 병목이 될 수 있습니다. 후보 샘플 수를 40 이하로 제어하는 것이 좋습니다(스케일링 실험에서 40 샘플에서 이점이 이미 포화됨).
