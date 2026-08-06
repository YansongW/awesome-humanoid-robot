---
$id: ent_paper_spatial_attention_adapting_execution_hor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Spatial Attention: Adapting Execution Horizons for Diffusion Policies via Observation Sensitivity'
  zh: 'Spatial Attention: Adapting Execution Horizons for Diffusion Policies via Observation Sensitivity'
  ko: 'Spatial Attention: Adapting Execution Horizons for Diffusion Policies via Observation Sensitivity'
summary:
  en: Sampling action chunks via generative models has become a widely adopted methodology for robotic learning from demonstration.
    However, existing methods often struggle to balance responsiveness and computational cost because they execute each action
    chunk for a fixed execution horizon. In this paper, we adaptively adjust the execution horizon of sampled action chunks,
    balancing responsiveness and.
  zh: 本文提出 Spatial Attention（SA）准则，用于为扩散策略自适应调整动作块执行时域（execution horizon）。作者通过理论推导证明，在固定采样预算下，最优重采样率正比于 Spatial Attention
    的 (2γ+1) 次根，并训练辅助分数网络与序列 Transformer 预测该指标。在 Robomimic 基准、扰动环境及真实机器人上，SA 一致提升成功率，同时维持平均执行时域。
  ko: Sampling action chunks via generative models has become a widely adopted methodology for robotic learning from demonstration.
    However, existing methods often struggle to balance responsiveness and computational cost because they execute each action
    chunk for a fixed execution horizon. In this paper, we adaptively adjust the execution horizon of sampled action chunks,
    balancing responsiveness and.
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
- spatial
- attention
- adapting
- execution
- hor
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
  title: 'arXiv:2607.04739 Spatial Attention: Adapting Execution Horizons for Diffusion Policies via Observ'
  url: https://arxiv.org/abs/2607.04739
  date: '2026-07-06'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Spatial Attention（SA）准则，用于为扩散策略自适应调整动作块执行时域（execution horizon）。作者通过理论推导证明，在固定采样预算下，最优重采样率正比于 Spatial Attention 的 (2γ+1) 次根，并训练辅助分数网络与序列 Transformer 预测该指标。在 Robomimic 基准、扰动环境及真实机器人上，SA 一致提升成功率，同时维持平均执行时域。

## 它改变了什么

扩散策略的固定动作块长度是长期被忽视的隐性假设：策略一旦生成动作块，在块内对观测变化完全“失明”。现有工作要么固定块长，要么用启发式规则（如固定间隔）重规划，缺乏理论依据。本文真正改变的是将“何时重新规划”从工程调参问题转化为可优化的统计决策问题——通过最小化扰动下累积似然下降，给出闭式最优解，使重采样时机与观测敏感度严格挂钩。

这一转变的深层意义在于：它把执行时域从超参数变为策略本身的函数。夹爪接近物体时，观测微小变化即导致动作分布显著偏移，此时缩短块长；远离物体时，观测变化不敏感，可延长块长以节省计算。这打破了“块长固定”与“响应性”之间的零和权衡，且不改变底层策略架构，可作为即插即用模块。

## 方法拆解

### 问题形式化
- 设策略 π(a_t|o_t) 生成动作块 {a_t, ..., a_{t+T_H-1}}，执行时域 T_a ≤ T_H。
- 扰动使观测从 o_t 变为 o'_t，导致动作分布偏移。目标：在固定采样预算 N 下，选择重采样时刻以最小化累积似然下降 Σ_t D_KL(π(·|o_t) || π(·|o'_t))。

### Spatial Attention 定义
- 对观测 o 的每个空间位置 s，定义 SA(s) = ||∂log π(a|o) / ∂o_s||²，衡量动作分布对局部观测变化的敏感度。
- 全局 Spatial Attention 为空间聚合：SA(o) = Σ_s SA(s)。

### 最优重采样率推导
- 假设扰动方差随 elapsed time 按幂律增长（式 4：σ²(t) ∝ t^{2γ}）。
- 推导得：在固定预算下，最优重采样率 r*(t) ∝ SA(o_t)^{1/(2γ+1)}。
- 即：Spatial Attention 越大，重采样越频繁，执行时域越短。

### 实现架构
- **SA 估计**：训练辅助分数网络（NCSN，10 个噪声级别），通过 Bayes 规则从分数函数比值估计 SA。
- **视觉编码**：使用 VAE（潜变量维度 32）将视觉观测映射到潜空间，在潜空间计算 SA。
- **未来预测**：序列到序列 Transformer（4 层，8 头，隐藏维度 256）预测未来 SA 轨迹，用于提前规划重采样时刻。
- **执行规则**：设定阈值 C_att，当预测 SA 超过阈值时触发重采样，否则继续执行当前块。

### 关键设计决策
- 选择 VAE 潜空间而非原始像素空间计算 SA，因潜空间更平滑且计算高效。
- 使用预测模型而非实时计算 SA，因推理时计算完整 SA 成本过高（预测模型运行约 100 Hz）。
- γ 设为 1.0，C_att 按任务调整以匹配平均执行时域在 T_avg ± 0.5 范围内。

## 关键创新

1. **理论驱动的自适应时域**：首次将执行时域选择建模为累积似然下降最小化问题，得到闭式最优解（重采样率 ∝ SA^{1/(2γ+1)}）。此前方法均为启发式或固定策略，缺乏最优性保证。

2. **观测敏感度的可计算代理**：通过分数网络 + Bayes 规则，将难以直接计算的 SA 转化为可训练的回归目标。VAE 潜空间的使用使 SA 在推理时可高效估计，且对视觉噪声鲁棒。

3. **预测式重规划**：用 Transformer 预测未来 SA 轨迹，使策略能“提前”缩短时域，而非被动响应。这比纯反应式方法更优，因为扩散采样本身有延迟，预测可补偿该延迟。

## 实验与结果

### 模拟实验（Robomimic）
- 基线：3 step-CP、1 step-CP（CP 为一致性策略蒸馏），对比加 SA 版本。
- 关键结果（成功率）：

| 方法 | Lift | Can | Square | Tool Hang |
|---|---|---|---|---|
| 3 step-CP | 0.60 ± 0.071 | 0.66 ± 0.053 | 0.68 ± 0.050 | 0.70 ± 0.038 |
| 3 step-CP+SA | 0.63 ± 0.060 | 0.80 ± 0.044 | 0.73 ± 0.050 | 0.72 ± 0.047 |
| 1 step-CP | 0.64 ± 0.092 | 0.56 ± 0.103 | 0.63 ± 0.074 | 0.68 ± 0.041 |
| 1 step-CP+SA | 0.67 ± 0.085 | 0.72 ± 0.102 | 0.68 ± 0.078 | 0.68 ± 0.048 |

- SA 在 Can 任务提升最显著（3 step：0.66→0.80；1 step：0.56→0.72），因该任务需精确对准，观测敏感度高。

### 真实机器人实验
- 7-DoF Franka Research 3，双 RealSense D435i，RTX 4090。
- 基线 DDIM（T_a=8）vs DDIM+SA（T̄_a ∈ [7.5, 8.5]）：

| 方法 | 成功率 | 平均 T_a |
|---|---|---|
| DDIM | 0.42 | 8 |
| DDIM+SA | 0.92 | 8.3 |

- SA 将成功率从 0.42 提升至 0.92（由表内数值 0.42→0.92 计算），平均时域仅从 8 增至 8.3，几乎不牺牲效率。
- 定性观察：DDIM 因块长过长无法响应立方体运动而失败；SA 在夹爪接近时缩短时域，成功跟踪目标。

## 边界与局限

- **扰动模型假设**：零均值高斯噪声且方差按时间幂律增长（式 4）可能不适用于真实世界非高斯、非平稳扰动。
- **VAE 潜空间代理**：潜空间敏感度不等同于原始观测空间敏感度，编码器可能丢失任务相关细节。
- **需离线训练辅助模型**：SA 分数网络与预测 Transformer 需额外训练（各约 2 小时/1 小时），增加部署成本。
- **不适用流式策略**：框架要求离散动作块，无法用于连续生成动作的策略（如 [5, 9, 12]）。
- **未覆盖多任务/元学习**：策略固定，不支持部署时新任务适应或在线微调。
- **超参数 γ 与 C_att 需人工调整**：论文未探索自动选择方法。
- **未在 VLA 大规模数据上验证**：论文未明确。

## 工程启示

- **复现优先核对**：先确认 γ=1.0、C_att 按任务调整至 T_avg ± 0.5 的匹配逻辑，这是成功率提升的关键敏感点。C_att 过松则退化为固定块长，过紧则频繁重采样导致计算浪费。
- **最大踩坑点**：SA 分数网络训练需与策略的观测预处理完全一致（含 VAE 编码），任何归一化或数据增强不一致都会导致 SA 估计偏差。建议先冻结策略，单独验证 SA 预测与真实敏感度的相关性。
- **下游团队集成**：SA 模块可独立于策略推理，通过 TCP 通信（真实实验已验证）插入现有系统。预测模型 100 Hz 运行频率远高于扩散采样（1-100 步），不会成为瓶颈。
- **迁移到新任务**：若新任务观测敏感度分布与 Robomimic 差异大，需重新调 C_att；可先用少量轨迹估计 SA 分布范围，再设定阈值。
- **计算预算**：SA 辅助训练约 3 小时/任务（A100），推理额外开销约 10 ms（预测模型），对实时性要求高的场景需评估是否可接受。

## Overview
Sampling action chunks via generative models has become a widely adopted methodology for robotic learning from demonstration. However, existing methods often struggle to balance responsiveness and computational cost because they execute each action chunk for a fixed execution horizon. In this paper, we adaptively adjust the execution horizon of sampled action chunks, balancing responsiveness and computational efficiency. We introduce Spatial Attention -- defined as the expected squared norm of the gradient of the action log-likelihood with respect to the observation -- which indicates the sensitivity of the policy's action distribution to variations in the observation. We show that, under a fixed budget of chunk samplings, the execution horizon that minimizes the cumulative likelihood drop induced by disturbances decreases as Spatial Attention increases. By forecasting future Spatial Attention values alongside the action chunk, our framework dynamically assigns shorter execution horizons to phases with high Spatial Attention, and longer horizons to phases with low Spatial Attention. Experiments on standard and perturbed tasks, in both simulation and on a real robot, show that our method significantly improves success rates over fixed-horizon baselines while maintaining the average execution horizon.

## 参考
- https://arxiv.org/abs/2607.04739

## 개요

본 논문은 확산 정책(diffusion policy)의 실행 시간 영역(execution horizon)을 적응형으로 조정하기 위한 Spatial Attention(SA) 기준을 제안한다. 저자들은 고정 샘플링 예산 하에서 최적 재샘플링 비율이 Spatial Attention의 (2γ+1) 제곱근에 비례한다는 것을 이론적으로 증명하고, 보조 스코어 네트워크와 시퀀스 Transformer를 훈련하여 해당 지표를 예측한다. Robomimic 벤치마크, 교란 환경 및 실제 로봇에서 SA는 평균 실행 시간 영역을 유지하면서 일관되게 성공률을 향상시킨다.

## 그것이 바꾸는 것

확산 정책의 고정 동작 블록 길이는 오랫동안 간과된 암묵적 가정이다. 정책이 동작 블록을 생성하면 블록 내에서 관측 변화에 완전히 "눈이 멀게" 된다. 기존 연구는 블록 길이를 고정하거나 휴리스틱 규칙(예: 고정 간격)으로 재계획을 수행하여 이론적 근거가 부족했다. 본 논문이 실제로 바꾸는 것은 "언제 재계획할지"를 엔지니어링 파라미터 튜닝 문제에서 최적화 가능한 통계적 의사결정 문제로 전환한 것이다—교란 하에서 누적 우도 감소를 최소화하여 폐쇄형 최적해를 제공하고, 재샘플링 시점을 관측 민감도와 엄격하게 연계한다.

이 전환의 심층적 의미는 실행 시간 영역을 하이퍼파라미터에서 정책 자체의 함수로 만든다는 것이다. 그리퍼가 물체에 접근할 때 관측의 미세한 변화가 동작 분포의 유의미한 이동을 초래하므로 블록 길이를 줄이고, 물체에서 멀어지면 관측 변화에 둔감하므로 블록 길이를 늘려 계산을 절약할 수 있다. 이는 "블록 길이 고정"과 "반응성" 사이의 제로섬 트레이드오프를 깨뜨리며, 기본 정책 아키텍처를 변경하지 않으므로 플러그 앤 플레이 모듈로 사용할 수 있다.

## 방법 분해

### 문제 정식화
- 정책 π(a_t|o_t)이 동작 블록 {a_t, ..., a_{t+T_H-1}}을 생성하고, 실행 시간 영역 T_a ≤ T_H이다.
- 교란으로 관측이 o_t에서 o'_t로 변하여 동작 분포가 이동한다. 목표: 고정 샘플링 예산 N 하에서 누적 우도 감소 Σ_t D_KL(π(·|o_t) || π(·|o'_t))를 최소화하는 재샘플링 시점을 선택한다.

### Spatial Attention 정의
- 관측 o의 각 공간 위치 s에 대해 SA(s) = ||∂log π(a|o) / ∂o_s||²로 정의하며, 이는 동작 분포의 국소 관측 변화에 대한 민감도를 측정한다.
- 전역 Spatial Attention은 공간 집계: SA(o) = Σ_s SA(s)이다.

### 최적 재샘플링 비율 유도
- 교란 분산이 경과 시간에 따라 멱법칙으로 증가한다고 가정한다(식 4: σ²(t) ∝ t^{2γ}).
- 유도 결과: 고정 예산 하에서 최적 재샘플링 비율 r*(t) ∝ SA(o_t)^{1/(2γ+1)}이다.
- 즉, Spatial Attention이 클수록 재샘플링이 빈번해지고 실행 시간 영역이 짧아진다.

### 구현 아키텍처
- **SA 추정**: 보조 스코어 네트워크(NCSN, 10개 노이즈 레벨)를 훈련하고, Bayes 규칙을 통해 스코어 함수 비율에서 SA를 추정한다.
- **시각 인코딩**: VAE(잠재 변수 차원 32)를 사용하여 시각 관측을 잠재 공간에 매핑하고, 잠재 공간에서 SA를 계산한다.
- **미래 예측**: 시퀀스-투-시퀀스 Transformer(4층, 8헤드, 은닉 차원 256)가 미래 SA 궤적을 예측하여 재샘플링 시점을 사전에 계획한다.
- **실행 규칙**: 임계값 C_att를 설정하고, 예측 SA가 임계값을 초과하면 재샘플링을 트리거하고, 그렇지 않으면 현재 블록을 계속 실행한다.

### 핵심 설계 결정
- 원본 픽셀 공간 대신 VAE 잠재 공간에서 SA를 계산하는 이유는 잠재 공간이 더 매끄럽고 계산 효율적이기 때문이다.
- 실시간 SA 계산 대신 예측 모델을 사용하는 이유는 추론 시 전체 SA 계산 비용이 너무 높기 때문이다(예측 모델은 약 100 Hz로 실행).
- γ는 1.0으로 설정하고, C_att는 평균 실행 시간 영역이 T_avg ± 0.5 범위 내에 있도록 작업별로 조정한다.

## 핵심 혁신

1. **이론 기반 적응형 시간 영역**: 실행 시간 영역 선택을 누적 우도 감소 최소화 문제로 모델링하여 폐쇄형 최적해(재샘플링 비율 ∝ SA^{1/(2γ+1)})를 처음으로 도출했다. 기존 방법은 모두 휴리스틱 또는 고정 전략으로 최적성 보장이 없었다.

2. **관측 민감도의 계산 가능한 대리 지표**: 스코어 네트워크 + Bayes 규칙을 통해 직접 계산이 어려운 SA를 훈련 가능한 회귀 목표로 변환한다. VAE 잠재 공간 사용으로 SA를 추론 시 효율적으로 추정할 수 있고 시각적 노이즈에 강건하다.

3. **예측 기반 재계획**: Transformer로 미래 SA 궤적을 예측하여 정책이 수동적으로 반응하는 대신 "사전에" 시간 영역을 줄일 수 있다. 이는 확산 샘플링 자체에 지연이 있으므로 예측이 해당 지연을 보상할 수 있어 순수 반응형 방법보다 우수하다.

## 실험 및 결과

### 시뮬레이션 실험(Robomimic)
- 기준선: 3 step-CP, 1 step-CP(CP는 일관성 정책 증류), SA 적용 버전과 비교.
- 주요 결과(성공률):

| 방법 | Lift | Can | Square | Tool Hang |
|---|---|---|---|---|
| 3 step-CP | 0.60 ± 0.071 | 0.66 ± 0.053 | 0.68 ± 0.050 | 0.70 ± 0.038 |
| 3 step-CP+SA | 0.63 ± 0.060 | 0.80 ± 0.044 | 0.73 ± 0.050 | 0.72 ± 0.047 |
| 1 step-CP | 0.64 ± 0.092 | 0.56 ± 0.103 | 0.63 ± 0.074 | 0.68 ± 0.041 |
| 1 step-CP+SA | 0.67 ± 0.085 | 0.72 ± 0.102 | 0.68 ± 0.078 | 0.68 ± 0.048 |

- SA는 Can 작업에서 가장 큰 향상을 보였다(3 step: 0.66→0.80; 1 step: 0.56→0.72). 이는 해당 작업이 정밀한 정렬을 요구하고 관측 민감도가 높기 때문이다.

### 실제 로봇 실험
- 7-DoF Franka Research 3, 듀얼 RealSense D435i, RTX 4090.
- 기준선 DDIM(T_a=8) vs DDIM+SA(T̄_a ∈ [7.5, 8.5]):

| 방법 | 성공률 | 평균 T_a |
|---|---|---|
| DDIM | 0.42 | 8 |
| DDIM+SA | 0.92 | 8.3 |

- SA는 성공률을 0.42에서 0.92로 향상시켰고(표 내 수치 0.42→0.92로 계산), 평균 시간 영역은 8에서 8.3으로만 증가하여 효율성을 거의 희생하지 않았다.
- 정성적 관찰: DDIM은 블록 길이가 너무 길어 큐브 움직임에 반응하지 못해 실패했고, SA는 그리퍼가 접근할 때 시간 영역을 줄여 목표를 성공적으로 추적했다.

## 경계 및 한계

- **교란 모델 가정**: 평균이 0인 가우시안 노이즈와 분산의 시간 멱법칙 증가(식 4)는 실제 세계의 비가우시안, 비정상 교란에는 적용되지 않을 수 있다.
- **VAE 잠재 공간 대리 지표**: 잠재 공간 민감도는 원본 관측 공간 민감도와 동일하지 않으며, 인코더가 작업 관련 세부 정보를 손실할 수 있다.
- **오프라인 보조 모델 훈련 필요**: SA 스코어 네트워크와 예측 Transformer는 추가 훈련(각각 약 2시간/1시간)이 필요하여 배포 비용이 증가한다.
- **스트리밍 정책에 부적합**: 프레임워크가 이산 동작 블록을 요구하므로 연속적으로 동작을 생성하는 정책(예: [5, 9, 12])에는 사용할 수 없다.
- **다중 작업/메타러닝 미포함**: 정책이 고정되어 배포 시 새로운 작업 적응이나 온라인 미세 조정을 지원하지 않는다.
- **하이퍼파라미터 γ 및 C_att 수동 조정 필요**: 논문은 자동 선택 방법을 탐구하지 않았다.
- **VLA 대규모 데이터에서 검증되지 않음**: 논문에서 명시되지 않았다.

## 엔지니어링 시사점

- **재현 시 우선 확인 사항**: γ=1.0, C_att를 작업별로 T_avg ± 0.5에 맞추는 매칭 로직을 먼저 확인하라. 이것이 성공률 향상의 핵심 민감 지점이다. C_att가 너무 느슨하면 고정 블록 길이로 퇴화하고, 너무 조이면 빈번한 재샘플링으로 계산 낭비가 발생한다.
- **최대 함정**: SA 스코어 네트워크 훈련은 정책의 관측 전처리(VAE 인코딩 포함)와 완전히 일치해야 한다. 정규화나 데이터 증강의 불일치는 SA 추정 편향을 초래한다. 정책을 먼저 동결하고 SA 예측과 실제 민감도의 상관관계를 별도로 검증할 것을 권장한다.
- **하위 팀 통합**: SA 모듈은 정책 추론과 독립적으로 TCP 통신(실제 실험에서 검증됨)을 통해 기존 시스템에 삽입할 수 있다. 예측 모델의 100 Hz 실행 빈도는 확산 샘플링(1-100 스텝)보다 훨씬 높아 병목이 되지 않는다.
- **새 작업으로 전이**: 새 작업의 관측 민감도 분포가 Robomimic과 크게 다르면 C_att를 다시 조정해야 한다. 먼저 소량의 궤적으로 SA 분포 범위를 추정한 다음 임계값을 설정할 수 있다.
- **계산 예산**: SA 보조 훈련은 작업당 약 3시간(A100)이 소요되고, 추론 추가 오버헤드는 약 10 ms(예측 모델)이므로 실시간 요구사항이 높은 시나리오에서는 수용 가능 여부를 평가해야 한다.
