---
$id: ent_paper_fm_vla_force_memory_vision_language_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation'
  zh: 'FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation'
  ko: 'FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation'
summary:
  en: Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented
    VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries. Vision-based memory approaches
    address this by conditioning on sampled past image frames, but they are computationally expensive and fundamentally limited
    when temporal.
  zh: FM-VLA 是首个将力（wrench）流作为轻量级长时程记忆用于视觉-语言-动作（VLA）模型的系统，由作者团队提出，旨在解决接触丰富操作中依赖单帧观测的马尔可夫假设失效问题。其核心贡献在于通过冻结的 Force-VAE 将长程腕部力/力矩历史压缩为
    8 个记忆 token，并与短程关节状态历史结合，在三个双臂接触任务上将平均成功率从基线的 27.8% 提升至 83.3%，同时推理延迟仅增加 3.3 ms。
  ko: Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented
    VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries. Vision-based memory approaches
    address this by conditioning on sampled past image frames, but they are computationally expensive and fundamentally limited
    when temporal.
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
- fm
- vla
- force
- memory
- vision
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
  title: 'arXiv:2607.18231 FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Man'
  url: https://arxiv.org/abs/2607.18231
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

FM-VLA 是首个将力（wrench）流作为轻量级长时程记忆用于视觉-语言-动作（VLA）模型的系统，由作者团队提出，旨在解决接触丰富操作中依赖单帧观测的马尔可夫假设失效问题。其核心贡献在于通过冻结的 Force-VAE 将长程腕部力/力矩历史压缩为 8 个记忆 token，并与短程关节状态历史结合，在三个双臂接触任务上将平均成功率从基线的 27.8% 提升至 83.3%，同时推理延迟仅增加 3.3 ms。

## 它改变了什么

现有 VLA 模型将决策视为从当前状态到动作的无记忆映射，这在按钮按压、擦碗等视觉变化细微但力信号携带关键计数信息的任务中系统性失效。此前引入力信号的尝试（如 TA-VLA）仅将力作为短期上下文，无法累积“已按几次”这类长时程状态；而视觉记忆方案（如 π-MEM）在视觉位移可忽略时失效，且存储历史帧导致推理延迟显著增加（+39.1 ms 至 +129.3 ms）。

FM-VLA 真正改变的是“记忆的模态选择”与“记忆的压缩方式”。它证明了力信号不仅是瞬时的反馈信号，更是一种天然适合长时程压缩的本体感受流——6 维力/力矩的时序模式比高维视觉帧更易编码为紧凑的潜在表示。通过将力历史压缩为固定 8 个 token，它绕开了视觉记忆的 token 膨胀问题，同时保留了任务关键的非马尔可夫信息，这是对 VLA 架构中“记忆从哪来、以何种形式存在”这一根本问题的重新回答。

## 方法拆解

### 问题形式化
策略建模为 π(a_t | o_t, l, h_t)，其中历史 h_t 由两个互补流组成：
- **长时程 wrench 历史**：{f_τ}_{τ=1}^{t}，f_τ ∈ R⁶（3 轴力 + 3 轴力矩，腕装六轴 F/T 传感器，100 Hz 降采样至 30 Hz）
- **短窗口关节状态历史**：{s_τ}_{τ=t-W+1}^{t}，s_τ ∈ R¹⁶（7-DoF 双臂 + 两个 1-DoF 夹爪）

### 力历史预处理
- **因果一阶 EMA 平滑**：f̃_τ = 0.3·f_τ + 0.7·f̃_{τ-1}，去除传感器噪声同时保留接触起始与峰值特征
- **随机噪声预填充**：训练时在历史前添加均匀采样至多 1000 帧（≈10 s）的低幅高斯噪声（σ=0.05），防止模型利用序列长度泄露时间进度；推理时禁用

### Force-VAE 编码器（Perceiver-IO 架构）
1. 输入力帧经分位数归一化（q₀₁/q₉₉），输入 MLP 投影至 384 维，叠加 32 波段傅里叶位置编码（f_max=1500）
2. 编码器：2 层交叉注意力（1 头，头维 64）将特征提取至 K=8 个可学习潜查询 token，穿插 10 层自注意力（8 头，头维 32，dropout 0.1）
3. 每潜 token 经线性头输出后验参数 (μₖ, log σₖ²) ∈ R⁹⁶，采样 zₖ = μₖ + σₖ ⊙ εₖ
4. 解码器：2 层交叉注意力，时间步特定傅里叶编码查询关注潜 token，重建序列 F̂ ∈ R^{T×6}

### 短状态历史投影器
避免第二个 VAE，取最近 10 帧关节状态（步长 3 数据集帧，覆盖 ≈0.9 s），10×16 张量展平后经单个零初始化线性层投影为 1 个状态历史 token。

### 记忆 token 注入
- 力编码器仅取后验均值 μ_f（无重参数化噪声），经零初始化线性层从 d_z=96 投影至动作专家隐藏维度 d_h
- 序列布局：`[30 个噪声动作 token] ∥ [8 个 wrench 记忆 token] ∥ [1 个状态窗口 token]`
- 后置位置保持噪声动作 token 在基础策略预训练时的 RoPE 位置不变

### 两阶段训练
- **Stage 1（Force-VAE 预训练）**：掩码 ELBO 目标 L_VAE = (1/(Σ_τ m_τ·6)) Σ_τ m_τ ||f_τ - f̂_τ||² + 1×10⁻³·(1/(8·96)) Σ_{k,j} max(D_KL^(k,j), 0.5)，使用逆频率任务采样；100000 步，批大小 512，峰值 LR 3×10⁻⁴
- **Stage 2（VLA 微调）**：冻结力编码器并切换 eval 模式，仅用 μ_f；遵循 π₀.₅ 的 rectified-flow 方案，预测速度 ε - a₀；联合微调 VLM、动作专家、短状态投影器、wrench 潜在投影器；50000 步，全局批大小 32，峰值 LR 5×10⁻⁵，每视角图像 dropout p=0.4

## 关键创新

1. **力作为长时程记忆的首次系统性应用**：此前力信号仅用于短期动作调节，FM-VLA 证明 6 维力/力矩流经 VAE 压缩后可稳定携带“按钮已按次数”“碗已擦几圈”等跨数十秒的任务状态，这是对 VLA 记忆模态选择的根本性拓展。

2. **冻结 VAE + 零初始化投影的注入范式**：力编码器在 Stage 1 预训练后完全冻结，仅通过零初始化线性层接入动作专家。这避免了端到端训练中力表征被动作预测目标破坏，同时零初始化保证初始训练时记忆 token 不干扰 π₀.₅ 预训练的行为分布，实现稳定微调。

3. **极低推理开销的记忆机制**：8 个力记忆 token + 1 个状态 token 仅增加 3.3 ms 延迟（60.7→64.0 ms），相比视觉记忆 π-MEM 的 +39.1 ms（K=5）和 +129.3 ms（K=16）有数量级优势，使长时程记忆首次可部署于实时机器人控制回路。

## 实验与结果

**任务套件**（AgiBot G1 双臂人形，每任务 18 次试验）：
- 任务 1（Find a Block Under Two Cups）：200 演示，需记住哪个杯子已检查
- 任务 2（Push Buttons）：350 演示，按 N∈{1,2,3} 次后停止，视觉位移可忽略
- 任务 3（Wipe Dishes）：200 演示，擦碗 N∈{1,2,3} 圈，视觉变化极小

**主要结果（成功率 %）**：

| 方法 | 任务 1 | 任务 2 | 任务 3 | 平均 |
|------|--------|--------|--------|------|
| π₀.₅（无历史） | 72.2 | 11.1 | 0.0 | 27.8 |
| TA-VLA（短期力） | 50.0 | 11.1 | 5.6 | 22.2 |
| π-MEM（视觉记忆） | 77.8 | 33.3 | 50.0 | 53.7 |
| FM-VLA（VAE，ours） | 100.0 | 72.2 | 77.8 | 83.3 |

**关键消融**：
- 仅力历史（无状态窗口）：平均 25.9%，任务 2 降至 0.0%——力历史单独不足以完成任务，需与短状态配合
- 仅状态历史：平均 40.7%，任务 1 达 100.0%——关节状态可推断杯子检查进度，但无法感知按钮按压次数
- 架构消融：GRU 编码器平均 33.3%，Q-Former 平均 57.4%，VAE 平均 83.3%——VAE 的显式信息瓶颈（8 token）优于 GRU 的单 token 压缩和 Q-Former 的端到端学习

**推理延迟（RTX 4090）**：

| 方法 | 延迟 (ms) | Δ vs. base |
|------|-----------|------------|
| π₀.₅ | 60.7 ± 0.3 | — |
| π-MEM (K=5) | 99.8 ± 0.4 | +39.1 |
| π-MEM (K=16) | 190.0 ± 1.0 | +129.3 |
| FM-VLA | 64.0 ± 0.4 | +3.3 |

**容量消融**（Wipe Dishes）：VAE 潜 token 数在 {4, 8, 16, 32} 上测试，8 个 token 达峰值；16/32 个 token 性能下降，归因于基础策略预训练时最多观察 50 个 token，额外力 token 超出分布范围。

## 边界与局限

- 当前 VAE 潜空间引入固定 8 token 瓶颈，对于需记忆数百个接触事件的超长时程任务（如整桌多碗擦拭），可能需要分层或自适应压缩机制，论文未明确。
- VAE 仅在演示数据集（共 750 个演示）的力数据上训练，未在大规模机器人数据集上预训练多样力/力矩记录，泛化性受限。
- 实验仅在单一平台（AgiBot G1）和三个任务上验证，未涉及更复杂的接触操作（如装配、插拔）或非双臂场景。
- 力传感器为腕装六轴，未探索指尖触觉或全身力感知；任务 2 中 FM-VLA 仍有 27.8% 失败率，说明计数误差在极端情况下仍存在。
- 论文未明确报告训练时间、显存占用或对传感器噪声/漂移的鲁棒性分析。

## 工程启示

- **先核对力信号质量**：EMA 平滑（α=0.3）和分位数归一化（q₀₁/q₉₉）是预处理关键，若传感器噪声大或基线漂移，需先调整这两个超参数；训练时噪声预填充（σ=0.05，最大 1000 帧）必须启用，否则模型会利用序列长度作弊。
- **冻结 VAE 是稳定微调的核心**：Stage 2 中力编码器必须切换 eval 模式并仅用后验均值，任何重参数化噪声都会破坏动作专家训练；零初始化投影器保证初始梯度不干扰 π₀.₅ 预训练行为，这是复现 83.3% 成功率的关键设计。
- **最容易踩坑的是 token 数量**：VAE 潜 token 数固定为 8，不要随意增加——基础策略预训练时动作专家最多观察 50 个 token，超过此限制会因分布偏移导致性能骤降（16/32 token 时任务 3 成功率下降）。
- **短状态窗口不可省略**：仅力历史在任务 2 上完全失败（0.0%），必须配合 10 帧关节状态窗口（步长 3，覆盖 0.9 s）；状态窗口的零初始化线性投影是轻量且有效的设计，无需额外 VAE。
- **推理部署友好**：64.0 ms 延迟（含 8 个力 token + 1 个状态 token）满足实时控制需求；若下游任务需更高控制频率，可考虑将力流降采样率从 30 Hz 进一步降低，但需重新验证计数精度。

## Overview
Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries. Vision-based memory approaches address this by conditioning on sampled past image frames, but they are computationally expensive and fundamentally limited when temporal events are visually ambiguous, e.g., pushing a button multiple times with small movements. We propose FM-VLA, a VLA model with force-based memory, enabling temporal context reasoning for non-Markovian, contact-rich manipulation. We encode force histories into compact force memory tokens with a variational autoencoder (VAE) pretrained with force time series reconstruction. By projecting force latent representations and short state history as additional conditioning tokens to the action expert module, we enable VLAs to leverage accumulated contact event history to guide manipulation. We evaluate FM-VLA on three memory-dependent tasks, including finding a hidden block, pressing a button, and wiping a dish for a specific number of times. Our lightweight force memory achieves over 80% success rate with minimal inference overhead, significantly outperforming baseline approaches. Project page: https://qft-333.github.io/FM-VLA-Page/

## 参考
- https://arxiv.org/abs/2607.18231

## 개요

FM-VLA는 힘(토크) 흐름을 경량 장기 기억으로 활용하는 최초의 비전-언어-행동(VLA) 모델 시스템으로, 저자 팀이 제안했으며 접촉이 많은 조작 작업에서 단일 프레임 관측에 의존하는 마르코프 가정이 실패하는 문제를 해결하는 것을 목표로 합니다. 핵심 기여는 동결된 Force-VAE를 통해 장기 손목 힘/토크 이력을 8개의 메모리 토큰으로 압축하고, 단기 관절 상태 이력과 결합하여 세 가지 이중 팔 접촉 작업에서 평균 성공률을 기준선의 27.8%에서 83.3%로 끌어올리면서 추론 지연 시간은 단 3.3ms만 증가시킨 것입니다.

## 무엇을 바꾸었는가

기존 VLA 모델은 결정을 현재 상태에서 행동으로의 무기억 매핑으로 간주합니다. 이는 버튼 누르기, 접시 닦기 등 시각적 변화는 미세하지만 힘 신호가 핵심 카운팅 정보를 담고 있는 작업에서 체계적으로 실패합니다. 이전에 힘 신호를 도입하려는 시도(예: TA-VLA)는 힘을 단기 컨텍스트로만 사용하여 "몇 번 눌렀는지"와 같은 장기 상태를 누적할 수 없었습니다. 반면 시각적 메모리 방식(예: π-MEM)은 시각적 변위가 무시할 수준일 때 실패하고, 이력 프레임을 저장하여 추론 지연 시간이 크게 증가했습니다(+39.1ms ~ +129.3ms).

FM-VLA가 실제로 바꾼 것은 "메모리의 양식 선택"과 "메모리의 압축 방식"입니다. 이는 힘 신호가 단순한 즉각적 피드백 신호일 뿐만 아니라 장기 압축에 자연스럽게 적합한 고유 수용성 흐름임을 증명했습니다. 6차원 힘/토크의 시계열 패턴은 고차원 시각 프레임보다 컴팩트한 잠재 표현으로 인코딩하기 쉽습니다. 힘 이력을 고정된 8개 토큰으로 압축함으로써 시각적 메모리의 토큰 팽창 문제를 우회하면서 작업에 중요한 비마르코프 정보를 보존합니다. 이는 VLA 아키텍처에서 "메모리가 어디서 오고 어떤 형태로 존재하는가"라는 근본적인 질문에 대한 재답변입니다.

## 방법 분해

### 문제 정식화
정책은 π(a_t | o_t, l, h_t)로 모델링되며, 이력 h_t는 두 개의 상호 보완적인 흐름으로 구성됩니다:
- **장기 토크 이력**: {f_τ}_{τ=1}^{t}, f_τ ∈ R⁶ (3축 힘 + 3축 토크, 손목 장착 6축 F/T 센서, 100Hz에서 30Hz로 다운샘플링)
- **단기 창 관절 상태 이력**: {s_τ}_{τ=t-W+1}^{t}, s_τ ∈ R¹⁶ (7-DoF 이중 팔 + 두 개의 1-DoF 그리퍼)

### 힘 이력 전처리
- **인과적 1차 EMA 평활화**: f̃_τ = 0.3·f_τ + 0.7·f̃_{τ-1}, 센서 노이즈를 제거하면서 접촉 시작 및 피크 특징을 보존
- **무작위 노이즈 사전 채움**: 훈련 중 이력 앞에 최대 1000프레임(≈10초)의 저진폭 가우시안 노이즈(σ=0.05)를 균일하게 샘플링하여 추가, 모델이 시퀀스 길이로 시간 진행을 유출하는 것을 방지; 추론 시 비활성화

### Force-VAE 인코더(Perceiver-IO 아키텍처)
1. 입력 힘 프레임은 분위수 정규화(q₀₁/q₉₉)를 거쳐 MLP로 384차원에 투영되고, 32밴드 푸리에 위치 인코딩(f_max=1500)이 추가됨
2. 인코더: 2계층 교차 어텐션(1헤드, 헤드 차원 64)이 특징을 K=8개의 학습 가능한 잠재 쿼리 토큰으로 추출하고, 10계층 자기 어텐션(8헤드, 헤드 차원 32, dropout 0.1)이穿插됨
3. 각 잠재 토큰은 선형 헤드를 통해 사후 파라미터 (μₖ, log σₖ²) ∈ R⁹⁶를 출력하고, zₖ = μₖ + σₖ ⊙ εₖ를 샘플링
4. 디코더: 2계층 교차 어텐션, 시간 단계별 푸리에 인코딩 쿼리가 잠재 토큰에 주목하여 시퀀스 F̂ ∈ R^{T×6}를 재구성

### 단기 상태 이력 프로젝터
두 번째 VAE를 피하고, 최근 10프레임의 관절 상태(스텝 3 데이터셋 프레임, ≈0.9초 커버)를 취하여 10×16 텐서를 펼친 후 단일 제로 초기화 선형 레이어로 1개의 상태 이력 토큰에 투영합니다.

### 메모리 토큰 주입
- 힘 인코더는 사후 평균 μ_f만 사용(재파라미터화 노이즈 없음), 제로 초기화 선형 레이어를 통해 d_z=96에서 행동 전문가 은닉 차원 d_h로 투영
- 시퀀스 레이아웃: `[30개의 노이즈 행동 토큰] ∥ [8개의 토크 메모리 토큰] ∥ [1개의 상태 창 토큰]`
- 후치 위치는 기본 정책 사전 훈련 시 노이즈 행동 토큰의 RoPE 위치를 변경하지 않도록 유지

### 2단계 훈련
- **1단계(Force-VAE 사전 훈련)**: 마스크 ELBO 목표 L_VAE = (1/(Σ_τ m_τ·6)) Σ_τ m_τ ||f_τ - f̂_τ||² + 1×10⁻³·(1/(8·96)) Σ_{k,j} max(D_KL^(k,j), 0.5), 역빈도 작업 샘플링 사용; 100000스텝, 배치 크기 512, 피크 LR 3×10⁻⁴
- **2단계(VLA 미세 조정)**: 힘 인코더를 동결하고 eval 모드로 전환, μ_f만 사용; π₀.₅의 rectified-flow 방식을 따르며 속도 ε - a₀를 예측; VLM, 행동 전문가, 단기 상태 프로젝터, 토크 잠재 프로젝터를 공동 미세 조정; 50000스텝, 전역 배치 크기 32, 피크 LR 5×10⁻⁵, 뷰별 이미지 dropout p=0.4

## 핵심 혁신

1. **힘을 장기 메모리로 체계적으로 적용한 최초 사례**: 이전에는 힘 신호가 단기 행동 조절에만 사용되었지만, FM-VLA는 6차원 힘/토크 흐름이 VAE 압축을 거쳐 "버튼을 몇 번 눌렀는지", "접시를 몇 바퀴 닦았는지"와 같은 수십 초에 걸친 작업 상태를 안정적으로 전달할 수 있음을 증명했습니다. 이는 VLA 메모리 양식 선택의 근본적인 확장입니다.

2. **동결 VAE + 제로 초기화 투영의 주입 패러다임**: 힘 인코더는 1단계 사전 훈련 후 완전히 동결되며, 제로 초기화 선형 레이어를 통해서만 행동 전문가에 연결됩니다. 이는 종단 간 훈련에서 힘 표현이 행동 예측 목표에 의해 손상되는 것을 방지하고, 제로 초기화는 초기 훈련 시 메모리 토큰이 π₀.₅ 사전 훈련의 행동 분포를 방해하지 않도록 보장하여 안정적인 미세 조정을 구현합니다.

3. **매우 낮은 추론 오버헤드의 메모리 메커니즘**: 8개의 힘 메모리 토큰 + 1개의 상태 토큰은 단 3.3ms의 지연 시간만 추가합니다(60.7→64.0ms). 이는 시각적 메모리 π-MEM의 +39.1ms(K=5) 및 +129.3ms(K=16)와 비교하여 규모의 차이가 있으며, 장기 메모리를 실시간 로봇 제어 루프에 처음으로 배포 가능하게 합니다.

## 실험 및 결과

**작업 세트**(AgiBot G1 이중 팔 휴머노이드, 작업당 18회 시도):
- 작업 1(Find a Block Under Two Cups): 200개 데모, 어느 컵을 확인했는지 기억해야 함
- 작업 2(Push Buttons): 350개 데모, N∈{1,2,3}번 누른 후 정지, 시각적 변위 무시 가능
- 작업 3(Wipe Dishes): 200개 데모, 접시를 N∈{1,2,3}바퀴 닦음, 시각적 변화 극히 미미

**주요 결과(성공률 %)**:

| 방법 | 작업 1 | 작업 2 | 작업 3 | 평균 |
|------|--------|--------|--------|------|
| π₀.₅(이력 없음) | 72.2 | 11.1 | 0.0 | 27.8 |
| TA-VLA(단기 힘) | 50.0 | 11.1 | 5.6 | 22.2 |
| π-MEM(시각적 메모리) | 77.8 | 33.3 | 50.0 | 53.7 |
| FM-VLA(VAE, ours) | 100.0 | 72.2 | 77.8 | 83.3 |

**핵심 소거**:
- 힘 이력만(상태 창 없음): 평균 25.9%, 작업 2는 0.0%로 하락 — 힘 이력만으로는 작업을 완료할 수 없으며 단기 상태와의 결합이 필요
- 상태 이력만: 평균 40.7%, 작업 1은 100.0% 달성 — 관절 상태로 컵 확인 진행 상황을 추론할 수 있지만 버튼 누름 횟수는 감지 불가
- 아키텍처 소거: GRU 인코더 평균 33.3%, Q-Former 평균 57.4%, VAE 평균 83.3% — VAE의 명시적 정보 병목(8토큰)이 GRU의 단일 토큰 압축 및 Q-Former의 종단 간 학습보다 우수

**추론 지연 시간(RTX 4090)**:

| 방법 | 지연 시간 (ms) | Δ vs. base |
|------|-----------|------------|
| π₀.₅ | 60.7 ± 0.3 | — |
| π-MEM (K=5) | 99.8 ± 0.4 | +39.1 |
| π-MEM (K=16) | 190.0 ± 1.0 | +129.3 |
| FM-VLA | 64.0 ± 0.4 | +3.3 |

**용량 소거**(Wipe Dishes): VAE 잠재 토큰 수를 {4, 8, 16, 32}에서 테스트했으며, 8개 토큰에서 최고 성능 도달; 16/32개 토큰에서는 성능이 하락했으며, 이는 기본 정책 사전 훈련 시 최대 50개 토큰만 관찰할 수 있고 추가 힘 토큰이 분포 범위를 벗어나기 때문입니다.

## 경계 및 한계

- 현재 VAE 잠재 공간은 고정 8토큰 병목을 도입하며, 수백 개의 접촉 이벤트를 기억해야 하는 초장기 작업(예: 전체 테이블의 여러 접시 닦기)에는 계층적 또는 적응형 압축 메커니즘이 필요할 수 있지만 논문에서는 명확히 다루지 않았습니다.
- VAE는 데모 데이터셋(총 750개 데모)의 힘 데이터에서만 훈련되었으며, 대규모 로봇 데이터셋에서 다양한 힘/토크 기록으로 사전 훈련되지 않아 일반화 성능이 제한적입니다.
- 실험은 단일 플랫폼(AgiBot G1)과 세 가지 작업에서만 검증되었으며, 더 복잡한 접촉 조작(예: 조립, 삽입/분리)이나 비이중 팔 시나리오는 다루지 않았습니다.
- 힘 센서는 손목 장착 6축이며, 손끝 촉각이나 전신 힘 감지는 탐구되지 않았습니다. 작업 2에서 FM-VLA는 여전히 27.8%의 실패율을 보여 극단적인 경우 카운팅 오류가 여전히 존재함을 시사합니다.
- 논문은 훈련 시간, GPU 메모리 사용량 또는 센서 노이즈/드리프트에 대한 강건성 분석을 명확히 보고하지 않았습니다.

## 엔지니어링 시사점

- **먼저 힘 신호 품질을 확인하세요**: EMA 평활화(α=0.3)와 분위수 정규화(q₀₁/q₉₉)는 전처리의 핵심입니다. 센서 노이즈가 크거나 기준선 드리프트가 있다면 이 두 하이퍼파라미터를 먼저 조정해야 합니다. 훈련 중 노이즈 사전 채움(σ=0.05, 최대 1000프레임)은 반드시 활성화해야 합니다. 그렇지 않으면 모델이 시퀀스 길이를 이용해 부정행위를 합니다.
- **VAE 동결은 안정적인 미세 조정의 핵심입니다**: 2단계에서 힘 인코더는 반드시 eval 모드로 전환하고 사후 평균만 사용해야 합니다. 어떤 재파라미터화 노이즈도 행동 전문가 훈련을 방해합니다. 제로 초기화 프로젝터는 초기 그래디언트가 π₀.₅ 사전 훈련 행동을 방해하지 않도록 보장하며, 이는 83.3% 성공률을 재현하는 핵심 설계입니다.
- **가장 쉽게 함정에 빠지는 부분은 토큰 수입니다**: VAE 잠재 토큰 수는 8로 고정되어 있으며 임의로 늘리지 마세요. 기본 정책 사전 훈련 시 행동 전문가는 최대 50개 토큰만 관찰할 수 있으며, 이 제한을 초과하면 분포 이동으로 인해 성능이 급락합니다(16/32토큰에서 작업 3 성공률 하락).
- **단기 상태 창은 생략할 수 없습니다**: 힘 이력만으로는 작업 2에서 완전히 실패하며(0.0%), 10프레임 관절 상태 창(스텝 3, 0.9초 커버)과 반드시 결합해야 합니다. 상태 창의 제로 초기화 선형 투영은 가볍고 효과적인 설계로 추가 VAE가 필요 없습니다.
- **추론 배포에 친화적입니다**: 64.0ms 지연 시간(8개 힘 토큰 + 1개 상태 토큰 포함)은 실시간 제어 요구를 충족합니다. 하류 작업에서 더 높은 제어 주파수가 필요하다면 힘 흐름 다운샘플링 비율을 30Hz에서 더 낮출 수 있지만, 카운팅 정확도를 다시 검증해야 합니다.
