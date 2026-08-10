---
$id: ent_paper_representation_aligned_tactile_grounding_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation
  zh: Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation
  ko: Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation
summary:
  en: Tactile-enhanced vision-language-action (VLA) policies have been introduced for contact-rich manipulation, where critical
    interaction states are often hidden from vision. Future tactile prediction is a promising way to use touch because it
    turns tactile outcomes into supervision for action-induced contact dynamics. Yet VLA policies contain representations
    with different roles, from perceptual.
  zh: 本文提出表征对齐触觉接地（Representation-Aligned Tactile Grounding）方法，用于接触丰富机器人操作。作者通过诊断实验发现未来触觉可预测性沿VLA动作通路呈非单调趋势，中间动作专家表征最优，据此设计Latent
    Tactile Predictor（LTP）分支，在训练时将未来触觉预测施加于该特定内部表征，显著提升多任务成功率。核心贡献在于将未来触觉预测从通用辅助损失重新定义为表征对齐问题，并给出具体施加位置与轻量实现。
  ko: Tactile-enhanced vision-language-action (VLA) policies have been introduced for contact-rich manipulation, where critical
    interaction states are often hidden from vision. Future tactile prediction is a promising way to use touch because it
    turns tactile outcomes into supervision for action-induced contact dynamics. Yet VLA policies contain representations
    with different roles, from perceptual.
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
- representation
- aligned
- tactile
- grounding
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
  title: arXiv:2607.14609 Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation
  url: https://arxiv.org/abs/2607.14609
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

本文提出表征对齐触觉接地（Representation-Aligned Tactile Grounding）方法，用于接触丰富机器人操作。作者通过诊断实验发现未来触觉可预测性沿VLA动作通路呈非单调趋势，中间动作专家表征最优，据此设计Latent Tactile Predictor（LTP）分支，在训练时将未来触觉预测施加于该特定内部表征，显著提升多任务成功率。核心贡献在于将未来触觉预测从通用辅助损失重新定义为表征对齐问题，并给出具体施加位置与轻量实现。

## 它改变了什么

现有触觉增强VLA方法大多将触觉仅作为输入信号，未显式要求策略建模自身动作如何改变未来接触状态。未来触觉预测虽被用作辅助损失或世界建模目标，但未研究该监督应施加于策略的哪个内部表征——这是本文真正改变的痛点。作者将未来触觉预测表述为“表征对齐问题”：VLM侧特征过于感知导向，最终动作特征已专门用于运动解码，中间动作专家表征最可能包含未来接触信息。这一判断改变了未来触觉预测的定位——它不应作为可任意添加的通用辅助损失，而应施加于与动作条件接触动力学对齐的特定内部表征。对工程实践而言，这意味着触觉接地不是“加一个损失”那么简单，选错施加位置可能不仅无益反而有害。

## 方法拆解

### 诊断阶段
- 冻结基础VLA策略，对轨迹段提取VLM侧输出 \(h_t^{\mathrm{vlm}}\) 和动作专家各层特征 \(\{h_t^{\ell}\}_{\ell=1}^{L}\)
- 为每个候选表征训练独立轻量线性探针 \(g_h\) 预测原始未来触觉序列 \(r_{t+1:t+H}\)，损失为 \(\mathcal{L}_{\mathrm{probe}}=\|\hat{r}_{t+1:t+H}-r_{t+1:t+H}\|_2^2\)
- 策略在诊断期间不更新；对基于流的动作专家，在归一化动作生成时间 \(T \in \{0.25, 0.5, 0.75, 1.0\}\) 重复探针
- 诊断结果：未来触觉可预测性沿动作通路呈非单调趋势，VLM侧误差高，进入动作专家后下降，中间层最小，接近最终动作状态时再次上升；该模式在无触觉输入、有触觉输入、更大VLA骨干（\(\pi_0\)）下均一致

### Latent Tactile Predictor (LTP)
- 在时间 \(t\)，策略接收当前图像 \(I_t\)、语言指令 \(l\)、当前触觉观测 \(r_t\)，预测动作块 \(\hat{a}_{t+1:t+H}\)
- 执行后观测未来触觉序列 \(r_{t+1:t+H}\)，仅训练时用作触觉接地目标
- 未来触觉序列编码为潜在触觉序列：\(z_{t+1:t+H}=E_{\mathrm{tac}}(r_{t+1:t+H})\)
- LTP使用可学习触觉查询 \(Q=\{q_1,\ldots,q_H\}\) 从中间动作专家表征 \(h_t^{\mathrm{mid}}\) 预测未来触觉潜在序列：\(\hat{z}_{t+1:t+H}=P_{\theta}(Q, h_t^{\mathrm{mid}})\)
- 训练损失：\(\mathcal{L}_{\mathrm{tac}}=\|\hat{z}_{t+1:t+H}-\mathrm{sg}(z_{t+1:t+H})\|_2^2\)，\(\mathrm{sg}(\cdot)\) 对触觉目标停止梯度
- 总目标：\(\mathcal{L}=\mathcal{L}_{\mathrm{act}}+\lambda_{\mathrm{tac}}\mathcal{L}_{\mathrm{tac}}\)

### 关键设计决策
- 直接预测原始触觉信号不适合接地：触觉信号高维、传感器相关、含测量噪声、校准偏差和局部接触伪影，原始预测损失可能强调传感伪影而非控制相关接触动力学
- 预测紧凑潜在空间使目标聚焦于接触相关结构
- LTP分支仅训练时使用，推理时移除，不改变推理通路，无推理时开销

## 关键创新

1. **表征对齐的诊断框架**：首次系统研究未来触觉预测应施加于策略哪个内部表征，而非默认加在最终输出或VLM侧。诊断探针方法可复用于其他模态（如力、力矩）与其他VLA骨干，具有方法论价值。
2. **非单调可预测性发现**：未来触觉可预测性沿动作通路呈非单调趋势，中间层最优——这挑战了“越深越好”或“输出端最相关”的直觉，为表征工程提供了新依据。
3. **轻量LTP设计**：可学习查询+停止梯度的潜在预测头，训练时接地、推理时零开销，且通过潜在空间规避原始触觉的传感伪影问题。该设计将触觉接地从“辅助损失”提升为“表征对齐约束”，且不改变推理通路。

## 实验与结果

实验在真实世界单臂设置（ARX R5机器人+PaXini触觉传感器）上，五个接触丰富任务各50个演示、20次试验评估。

**SmolVLA主结果**：VLM级预测平均成功率58%，最终动作状态预测62%，中间动作专家表征接地74%。输入级触觉条件化和外部触觉表征学习优于VLA基线但低于表征对齐接地。

**\(\pi_0\) 骨干结果**：标准 \(\pi_0\) 平均成功率40%，触觉条件化提升至54%，VLM侧预测58%，最终动作预测59%，表征对齐接地73%。

**消融——多层接地（SmolVLA，所有任务）**：

| 变体 | Plug | USB | Wipe | Deformable | Bulb | Avg |
|------|------|-----|------|------------|------|-----|
| None（有触觉输入无预测） | 30 | 20 | 45 | 50 | 60 | 41 |
| Multi-A（所有动作专家层） | 20 | 20 | 45 | 45 | 60 | 38 |
| Multi-B（每两层，0/2/4/…） | 30 | 25 | 55 | 55 | 70 | 48 |
| Multi-C（中间层4–11） | 50 | 30 | 60 | 70 | 90 | 60 |
| Ours（单中间层） | 80 | 40 | 70 | 80 | 100 | 74 |

**消融——潜在预测**：将紧凑触觉潜在替换为直接原始触觉预测，Plug Insertion成功率从80%降至55%。

结果含义：表征对齐接地显著优于输入级触觉条件化与外部表征学习；多层接地中，覆盖中间层（Multi-C）优于全层或稀疏层，但单中间层（Ours）最佳——说明“对齐到正确位置”比“覆盖更多层”更重要；潜在预测优于原始触觉预测，验证了潜在空间设计的必要性。

## 边界与局限

论文未明确列出局限性章节，但隐含局限包括：实验仅在单一真实世界单臂设置上评估；每个任务仅50个演示；评估仅20次试验每任务。未做之事：未研究其他VLA骨干（除SmolVLA和 \(\pi_0\)）；未研究其他触觉传感器类型；未研究推理时使用预测分支；未研究多任务联合训练或跨任务泛化；未研究长期部署或分布外场景。诊断结论基于特定架构（SmolVLA与 \(\pi_0\)），对其他架构（如基于Transformer的扩散策略）是否成立论文未明确。

## 工程启示

复现时先核对三点：一是触觉编码器 \(E_{\mathrm{tac}}\) 的预训练方式与潜在维度——这直接影响接地目标质量；二是中间动作专家表征 \(h_t^{\mathrm{mid}}\) 的层选择——诊断阶段必须在自己模型上重跑探针，不能直接照搬论文层号，因为不同骨干的“中间层”语义不同；三是 \(\lambda_{\mathrm{tac}}\) 的敏感性——论文用 \(\lambda=1\)，但若动作损失尺度不同需重新调节。最容易踩坑的地方：直接预测原始触觉信号会显著掉点（Plug从80%降至55%），务必使用潜在空间；多层接地并非越多越好（Multi-A全层反而低于None），应聚焦中间层；LTP分支推理时必须移除，否则改变推理通路。对下游团队，建议在接入新任务时先跑诊断探针确认中间层可预测性，再决定是否启用LTP——若探针误差高，接地收益可能有限。

## Overview
Tactile-enhanced vision-language-action (VLA) policies have been introduced for contact-rich manipulation, where critical interaction states are often hidden from vision. Future tactile prediction is a promising way to use touch because it turns tactile outcomes into supervision for action-induced contact dynamics. Yet VLA policies contain representations with different roles, from perceptual encoding to motor prediction, making it unclear where this supervision should be applied. We study this as a representation-alignment problem. Through a linear probe analysis, we find that future tactile states are most predictable from intermediate action-expert features, rather than from vision-language features or final action states. Motivated by this observation, we introduce a lightweight Latent Tactile Predictor (LTP), which predicts compact future tactile embeddings from the identified intermediate representation. By avoiding direct prediction of noisy raw tactile signals, LTP provides an action-outcome grounding signal that aligns intermediate action representations with future contact consequences. Experiments on real-world contact-rich manipulation tasks show that representation-aligned tactile grounding outperforms less aligned or multi-interface tactile prediction, highlighting the importance of where tactile supervision is applied.

## 参考
- https://arxiv.org/abs/2607.14609

## 개요

본 논문은 접촉이 풍부한 로봇 조작을 위한 표현 정렬 촉각 접지(Representation-Aligned Tactile Grounding) 방법을 제안한다. 저자들은 진단 실험을 통해 미래 촉각 예측 가능성이 VLA 동작 경로를 따라 비단조적 추세를 보이며, 중간 동작 전문가 표현이 최적임을 발견하고, 이를 바탕으로 Latent Tactile Predictor(LTP) 분기를 설계하여 훈련 시 해당 특정 내부 표현에 미래 촉각 예측을 적용함으로써 다중 작업 성공률을 크게 향상시킨다. 핵심 기여는 미래 촉각 예측을 일반적인 보조 손실에서 표현 정렬 문제로 재정의하고, 구체적인 적용 위치와 경량 구현을 제시한 것이다.

## 무엇을 바꾸었는가

기존 촉각 강화 VLA 방법은 대부분 촉각을 입력 신호로만 사용하며, 정책이 자체 동작이 미래 접촉 상태를 어떻게 변화시키는지 명시적으로 모델링하도록 요구하지 않았다. 미래 촉각 예측이 보조 손실 또는 세계 모델링 목표로 사용되긴 했지만, 이 감독이 정책의 어떤 내부 표현에 적용되어야 하는지 연구되지 않았다——이것이 본 논문이 실제로 바꾼 핵심痛点이다. 저자들은 미래 촉각 예측을 "표현 정렬 문제"로 표현한다: VLM 측 특징은 지각 중심적이고, 최종 동작 특징은 운동 디코딩에 전용되며, 중간 동작 전문가 표현이 미래 접촉 정보를 가장 포함할 가능성이 높다. 이 판단은 미래 촉각 예측의 위치를 바꾼다——그것은 임의로 추가할 수 있는 일반적인 보조 손실이 아니라, 동작 조건 접촉 역학과 정렬된 특정 내부 표현에 적용되어야 한다. 공학 실무 측면에서 이는 촉각 접지가 "손실 하나 추가"만큼 단순하지 않으며, 적용 위치를 잘못 선택하면 이로울 뿐만 아니라 오히려 해로울 수 있음을 의미한다.

## 방법 분해

### 진단 단계
- 기본 VLA 정책을 동결하고, 궤적 세그먼트에서 VLM 측 출력 \(h_t^{\mathrm{vlm}}\) 및 동작 전문가 각 계층 특징 \(\{h_t^{\ell}\}_{\ell=1}^{L}\)을 추출한다
- 각 후보 표현에 대해 독립적인 경량 선형 프로브 \(g_h\)를 훈련하여 원시 미래 촉각 시퀀스 \(r_{t+1:t+H}\)를 예측하며, 손실은 \(\mathcal{L}_{\mathrm{probe}}=\|\hat{r}_{t+1:t+H}-r_{t+1:t+H}\|_2^2\)이다
- 정책은 진단 중 업데이트되지 않는다; 플로우 기반 동작 전문가의 경우 정규화된 동작 생성 시간 \(T \in \{0.25, 0.5, 0.75, 1.0\}\)에서 프로브를 반복한다
- 진단 결과: 미래 촉각 예측 가능성은 동작 경로를 따라 비단조적 추세를 보이며, VLM 측 오류가 높고, 동작 전문가 진입 후 감소하며, 중간 계층에서 최소이고, 최종 동작 상태에 가까워질수록 다시 상승한다; 이 패턴은 촉각 입력 없음, 촉각 입력 있음, 더 큰 VLA 백본(\(\pi_0\))에서 모두 일관된다

### 핵심 설계 결정
- 원시 촉각 신호를 직접 예측하는 것은 접지에 부적합하다: 촉각 신호는 고차원, 센서 의존적이며, 측정 노이즈, 캘리브레이션 편향 및 국소 접촉 아티팩트를 포함하므로, 원시 예측 손실은 제어 관련 접촉 역학보다 센싱 아티팩트를 강조할 수 있다
- 컴팩트 잠재 공간을 예측하면 목표가 접촉 관련 구조에 집중된다
- LTP 분기는 훈련 시에만 사용되고, 추론 시 제거되며, 추론 경로를 변경하지 않고 추론 오버헤드가 없다

## 핵심 혁신

1. **표현 정렬 진단 프레임워크**: 미래 촉각 예측이 정책의 어떤 내부 표현에 적용되어야 하는지 처음으로 체계적으로 연구하며, 최종 출력이나 VLM 측에 기본적으로 추가하지 않는다. 진단 프로브 방법은 다른 모달리티(예: 힘, 토크) 및 다른 VLA 백본에 재사용 가능하며 방법론적 가치가 있다.
2. **비단조적 예측 가능성 발견**: 미래 촉각 예측 가능성은 동작 경로를 따라 비단조적 추세를 보이며, 중간 계층이 최적이다——이는 "깊을수록 좋다" 또는 "출력 끝이 가장 관련 있다"는 직관에 도전하며 표현 엔지니어링에 새로운 근거를 제공한다.
3. **경량 LTP 설계**: 학습 가능한 쿼리 + 정지 그래디언트 잠재 예측 헤드로, 훈련 시 접지되고 추론 시 제로 오버헤드이며, 잠재 공간을 통해 원시 촉각의 센싱 아티팩트 문제를 회피한다. 이 설계는 촉각 접지를 "보조 손실"에서 "표현 정렬 제약"으로 승격시키고 추론 경로를 변경하지 않는다.

## 실험 및 결과

실험은 실제 세계 단일 암 설정(ARX R5 로봇 + PaXini 촉각 센서)에서 수행되었으며, 다섯 가지 접촉이 풍부한 작업 각각 50개 데모, 20회 시험 평가를 사용한다.

**SmolVLA 주요 결과**: VLM 수준 예측 평균 성공률 58%, 최종 동작 상태 예측 62%, 중간 동작 전문가 표현 접지 74%. 입력 수준 촉각 조건화 및 외부 촉각 표현 학습은 VLA 기준선보다 우수하지만 표현 정렬 접지보다는 낮다.

**\(\pi_0\) 백본 결과**: 표준 \(\pi_0\) 평균 성공률 40%, 촉각 조건화 54%로 향상, VLM 측 예측 58%, 최종 동작 예측 59%, 표현 정렬 접지 73%.

**절제——다중 계층 접지(SmolVLA, 모든 작업)**:

| 변형 | Plug | USB | Wipe | Deformable | Bulb | Avg |
|------|------|-----|------|------------|------|-----|
| None(촉각 입력 있음, 예측 없음) | 30 | 20 | 45 | 50 | 60 | 41 |
| Multi-A(모든 동작 전문가 계층) | 20 | 20 | 45 | 45 | 60 | 38 |
| Multi-B(매 두 계층, 0/2/4/…) | 30 | 25 | 55 | 55 | 70 | 48 |
| Multi-C(중간 계층 4–11) | 50 | 30 | 60 | 70 | 90 | 60 |
| Ours(단일 중간 계층) | 80 | 40 | 70 | 80 | 100 | 74 |

**절제——잠재 예측**: 컴팩트 촉각 잠재를 직접 원시 촉각 예측으로 대체하면 Plug Insertion 성공률이 80%에서 55%로 감소한다.

결과 의미: 표현 정렬 접지는 입력 수준 촉각 조건화 및 외부 표현 학습보다 크게 우수하다; 다중 계층 접지에서 중간 계층 커버(Multi-C)가 전체 계층 또는 희소 계층보다 우수하지만, 단일 중간 계층(Ours)이 최적이다——"더 많은 계층을 커버하는 것"보다 "올바른 위치에 정렬하는 것"이 더 중요함을 시사한다; 잠재 예측이 원시 촉각 예측보다 우수하여 잠재 공간 설계의 필요성을 검증한다.

## 경계 및 한계

논문은 한계 섹션을 명시적으로 나열하지 않았지만, 암시적 한계는 다음과 같다: 실험은 단일 실제 세계 단일 암 설정에서만 평가되었다; 각 작업당 50개 데모만 사용; 작업당 20회 시험만 평가. 수행되지 않은 것: 다른 VLA 백본(SmolVLA 및 \(\pi_0\) 제외) 연구 없음; 다른 촉각 센서 유형 연구 없음; 추론 시 예측 분기 사용 연구 없음; 다중 작업 공동 훈련 또는 교차 작업 일반화 연구 없음; 장기 배포 또는 분포 외 시나리오 연구 없음. 진단 결론은 특정 아키텍처(SmolVLA 및 \(\pi_0\))에 기반하며, 다른 아키텍처(예: Transformer 기반 확산 정책)에 대해서도 성립하는지 논문은 명시하지 않았다.

## 공학적 시사점

재현 시 먼저 세 가지를 확인하라: 첫째, 촉각 인코더 \(E_{\mathrm{tac}}\)의 사전 훈련 방식과 잠재 차원——이것은 접지 목표 품질에 직접 영향을 미친다; 둘째, 중간 동작 전문가 표현 \(h_t^{\mathrm{mid}}\)의 계층 선택——진단 단계는 반드시 자체 모델에서 프로브를 다시 실행해야 하며, 논문의 계층 번호를 직접 복사해서는 안 된다. 다른 백본의 "중간 계층" 의미가 다르기 때문이다; 셋째, \(\lambda_{\mathrm{tac}}\)의 민감도——논문은 \(\lambda=1\)을 사용하지만, 동작 손실 규모가 다르면 재조정이 필요하다. 가장 함정에 빠지기 쉬운 곳: 원시 촉각 신호를 직접 예측하면 성능이 크게 떨어지며(Plug 80%에서 55%로), 반드시 잠재 공간을 사용해야 한다; 다중 계층 접지는 많을수록 좋지 않으며(Multi-A 전체 계층은 오히려 None보다 낮음), 중간 계층에 집중해야 한다; LTP 분기는 추론 시 반드시 제거해야 하며, 그렇지 않으면 추론 경로가 변경된다. 하류 팀에게는 새 작업을 통합할 때 먼저 진단 프로브를 실행하여 중간 계층 예측 가능성을 확인한 후 LTP 활성화 여부를 결정할 것을 권장한다——프로브 오류가 높으면 접지 이점이 제한적일 수 있다.
