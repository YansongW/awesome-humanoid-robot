---
$id: ent_paper_reducing_temporal_redundancy_efficient_v_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference
  zh: Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference
  ko: Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference
summary:
  en: 'Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference
    latency limits real time deployment. We identify two primary sources of temporal redundancy in existing VLA pipelines:
    repeated visual encoding of highly similar consecutive frames and multi step iterative sampling in diffusion based policies.
    To address this, we propose a system.'
  zh: 本文提出一种系统级VLA推理加速框架，从感知与动作生成两端同时削减时间冗余：视觉编码器采用基于余弦相似度的token复用（更新比例r=0.4），动作侧将10步流匹配求解器压缩为2步低秩近似（锚定v0与v7）。在LIBERO与RoboTwin
    2.0基准上，π0.5+Ours达到93.8%平均成功率（基线94.4%），端到端延迟从286.9ms降至121.2ms（2.37×加速），FPS从3.5提升至8.2。
  ko: 'Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference
    latency limits real time deployment. We identify two primary sources of temporal redundancy in existing VLA pipelines:
    repeated visual encoding of highly similar consecutive frames and multi step iterative sampling in diffusion based policies.
    To address this, we propose a system.'
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
- reducing
- temporal
- redundancy
- efficient
- v
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: arXiv:2607.12287 Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference
  url: https://arxiv.org/abs/2607.12287
  date: '2026-07-14'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一种系统级VLA推理加速框架，从感知与动作生成两端同时削减时间冗余：视觉编码器采用基于余弦相似度的token复用（更新比例r=0.4），动作侧将10步流匹配求解器压缩为2步低秩近似（锚定v0与v7）。在LIBERO与RoboTwin 2.0基准上，π0.5+Ours达到93.8%平均成功率（基线94.4%），端到端延迟从286.9ms降至121.2ms（2.37×加速），FPS从3.5提升至8.2。

## 它改变了什么

现有VLA加速工作几乎都犯同一个错误：只盯着视觉编码器或LLM的token稀疏化，却对动作生成（Action Expert）这个真正的延迟大头视而不见。从Table II看，π0.5基线中Action Expert耗时212.6ms，占总延迟的72.5%，而ViT仅占13.7%。ToMe、ToFu、V2Drop这些方法把ViT和LLM压到70%左右，但Action Expert纹丝不动，最终总延迟只降了10%上下，FPS从3.4提到3.8——这种优化对实时闭环控制毫无意义。本文真正改变的是把优化重心从"看得快"转向"动得快"：通过压缩流匹配求解器步数，把Action Expert从212.6ms砍到40.9ms（降81%），同时用token复用保住视觉侧精度不崩。这个视角转换才是系统级加速的关键，也是之前所有方法都没做到的事。

## 方法拆解

### 感知侧：奇偶分块token复用
- 将视觉token按奇偶索引分块，奇数块全量前向并缓存key投影作为参考
- 偶数块计算当前token与缓存key的余弦相似度，选择相似度最低的top-ρN个token更新（ρ为更新比例）
- token索引选择仅在第一层执行，后续层复用该索引，避免重复计算
- 更新token重新计算Q/K/V，复用token直接继承缓存KV对；注意力仅对更新token计算，残差后所有token经MLP处理保证全量前向

### 动作侧：2步压缩求解器
- 分析flow matching速度场的奇异值谱，发现能量集中在前两个主成分，速度演化呈低维结构
- 选择v0和v7作为锚定速度：v0代表早期全局方向，v7代表中期轨迹细化
- 速度近似：v_t ≈ a_t v_0 + b_t v_7 + ε_t，最终状态x_T ≈ x_0 + α v_0 + β v_7 + b
- 轻量适配器g_φ直接预测系数(α, β, b) = g_φ(v_0)，训练目标为min_φ E[‖x_T^(2) − x_T^(10)‖_2^2]
- 不改变骨干架构，仅替换求解器步数

### 关键设计决策
- r=0.4的token更新比例：Table VII显示r从1.0降到0.4时成功率仅从94.4%降至93.8%（-0.6%），但r=0.5时骤降至92.6%（-1.8%），说明0.4是精度-效率的临界点
- 锚定v0和v7而非v0和v5：v7更接近轨迹末端，能更好捕捉细化方向，减少末端误差累积

## 关键创新

1. **首次将加速矛头对准Action Expert**：此前所有方法（ToMe、ToFu、V2Drop、SnapKV、SparseVLM）都只优化ViT和LLM，Action Expert耗时占比超70%却无人问津。本文通过低秩速度近似将求解器从10步压到2步，Action Expert耗时降81%，这是2.37×加速的主要来源。

2. **低秩速度近似的理论依据**：发现flow matching速度场奇异值谱能量集中在前两个主成分，这为2步压缩提供了数学基础——不是盲目砍步数，而是利用速度场的低维结构做有损压缩。锚定v0和v7分别捕捉全局方向和局部细化，比均匀采样步数更聪明。

3. **系统级而非组件级优化**：token复用（感知侧）与求解器压缩（动作侧）独立设计但联合部署，消融实验（Table III）显示两者叠加后总延迟从293.2ms降至111.6ms（2.63×），而单独使用分别只能降到282.9ms和123.9ms。这种"1+1>2"的系统效应是组件级方法无法达到的。

## 实验与结果

### LIBERO基准（Table I）
| 方法 | Mean SR (%) | Steps | Avg Time (ms) | FPS | TFLOPs |
|------|------------|-------|---------------|-----|--------|
| π0 | 92.3 | 10 | 276.4 | 3.6 | 4.48 |
| π0.5 | 94.4 | 10 | 286.9 | 3.5 | 4.48 |
| OpenVLA | 76.5 | 8 | 629.6 | 1.6 | 8.82 |
| X-VLA | 94.1 | 10 | 256.8 | 3.9 | – |
| Efficient VLA | 91.6 | 10 | 144.1 | 6.9 | 1.48 |
| π0+Ours | 91.0 | 2 | 156.2 | 6.4 | 2.86 |
| π0.5+Ours | 93.8 | 2 | 121.2 | 8.2 | 1.23 |

### 推理时间分解（Table II，LIBERO）
| 方法 | SR (%) | ViT (ms) | LLM (ms) | Action (ms) | Total (ms) | FPS |
|------|--------|----------|----------|-------------|------------|-----|
| π0.5 | 94.4 | 40.1 | 42.5 | 212.6 | 293.2 | 3.4 |
| ToMe | 75.3 | 31.8 | 32.8 | 202.3 | 266.9 | 3.7 |
| SnapKV | 89.8 | 27.2 | 26.1 | 196.3 | 249.6 | 4.0 |
| SparseVLM | 92.2 | 30.2 | 31.1 | 199.6 | 260.9 | 3.8 |
| Ours | 93.8 | 38.6 | 42.3 | 40.9 | 121.8 | 8.2 |

### RoboTwin 2.0（Table II）
| 方法 | SR (%) | Action (ms) | Total (ms) | FPS |
|------|--------|-------------|------------|-----|
| π0 | 82.2 | 226.85 | 298.46 | 3.35 |
| ToMe | 66.1 | 200.60 | 268.97 | 3.72 |
| SnapKV | 78.3 | 188.30 | 252.87 | 3.95 |
| Ours | 81.5 | 43.1 | 125.4 | 8.0 |

### 真实机器人（Table IV，六任务均值）
| 方法 | SR (%) | SR@30s (%) |
|------|--------|------------|
| π0.5 | 97.2 | 77.1 |
| Ours | 95.4 | 82.3 |

关键发现：Ours在SR@30s上反超基线（82.3% vs 77.1%），说明虽然单次成功率略降（-1.8%），但更高推理频率（8.2 vs 3.5 FPS）让机器人有更多机会在30秒窗口内完成任务——这是"快而稳"胜过"慢而准"的直接证据。

## 边界与局限

- 压缩策略仅在短视界操作任务上验证（LIBERO和RoboTwin均为单步或短序列操作），对长视界规划或高度动态环境（如移动操作、人机交互）的有效性未验证
- token复用假设相邻帧视觉内容高度相似（余弦相似度>0.98），在快速运动或场景突变时该假设可能失效，Table VII中r=0.5时成功率骤降1.8%暗示存在精度悬崖
- 真实机器人评估仅6个任务且均为桌面操作，未覆盖力控、灵巧操作等复杂场景
- 未提及对多模态输入（深度图、触觉）或不同动作空间（力控、阻抗控制）的扩展
- 适配器g_φ的训练数据量、学习率、批量大小等关键超参数未披露，复现门槛较高

## 工程启示

1. **先核对Action Expert耗时占比**：如果你的VLA管线中动作生成占总延迟比例低于50%，本文的求解器压缩收益会大打折扣。建议先做profiling，确认瓶颈位置再决定是否采用此方案。

2. **token复用比例r=0.4是安全线**：Table VII显示r从0.4降到0.5时成功率骤降1.2%（93.8%→92.6%），说明存在精度悬崖。复现时建议从r=0.4起步，逐步下调并监控成功率，不要盲目追求更低r值。

3. **锚定速度选择需重新验证**：本文选择v0和v7基于π0.5的速度场奇异值谱分析，换用不同骨干（如OpenVLA、RT-2）时主成分分布可能变化，需要重新做SVD分析确定锚点，不能直接照搬。

4. **训练适配器g_φ时注意轨迹对齐**：训练目标是最小化2步与10步轨迹的MSE，但不同任务的动作尺度差异大（如抓取vs放置），建议按任务归一化动作空间后再训练，否则适配器可能偏向大尺度动作任务。

5. **真实部署时关注SR@30s而非单次SR**：本文真实实验显示Ours单次SR略降但SR@30s反超（82.3% vs 77.1%），说明高推理频率补偿了精度损失。评估时应以"单位时间内成功次数"为核心指标，而非单次成功率。

## Overview
Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference latency limits real time deployment. We identify two primary sources of temporal redundancy in existing VLA pipelines: repeated visual encoding of highly similar consecutive frames and multi step iterative sampling in diffusion based policies. To address this, we propose a system level acceleration strategy that reduces computation in both perception and action generation. On the perception side, we incrementally update only tokens corresponding to dynamic scene regions instead of re-encoding entire frames. On the policy side, we compress diffusion sampling into a compact 2-step schedule through efficiency oriented training while preserving action precision. Experiments on Libero, RobotWin, and Real Robot Platforms demonstrate over 2 times speedup while maintaining high performance, achieving up to 98% success rate on general manipulation benchmarks. Our codes will be released on Github.

## 参考
- https://arxiv.org/abs/2607.12287

## 개요

본 논문은 시스템 수준의 VLA 추론 가속 프레임워크를 제안하며, 인식과 행동 생성 양쪽에서 시간 중복을 동시에 줄인다: 시각 인코더는 코사인 유사도 기반 토큰 재사용(업데이트 비율 r=0.4)을 채택하고, 행동 측은 10단계 플로우 매칭 솔버를 2단계 저랭크 근사(앵커 v0 및 v7)로 압축한다. LIBERO 및 RoboTwin 2.0 벤치마크에서 π0.5+Ours는 93.8% 평균 성공률(기준 94.4%)을 달성하고, 엔드투엔드 지연 시간은 286.9ms에서 121.2ms(2.37배 가속)로 감소하며, FPS는 3.5에서 8.2로 향상된다.

## 그것이 바꾸는 것

기존 VLA 가속 연구는 거의 모두 동일한 실수를 범한다: 시각 인코더나 LLM의 토큰 희소화에만 집중하고, 실제 지연 시간의 핵심인 행동 생성(Action Expert)은 무시한다. Table II에서 π0.5 기준에서 Action Expert는 212.6ms로 전체 지연 시간의 72.5%를 차지하는 반면, ViT는 13.7%에 불과하다. ToMe, ToFu, V2Drop과 같은 방법들은 ViT와 LLM을 약 70%까지 압축하지만 Action Expert는 그대로이며, 최종 지연 시간은 약 10%만 감소하고 FPS는 3.4에서 3.8로 향상된다—이러한 최적화는 실시간 폐쇄 루프 제어에 의미가 없다. 본 논문이 실제로 바꾸는 것은 최적화의 초점을 "빠르게 보기"에서 "빠르게 움직이기"로 전환한 것이다: 플로우 매칭 솔버 단계를 압축하여 Action Expert를 212.6ms에서 40.9ms로 줄이고(81% 감소), 동시에 토큰 재사용으로 시각 측 정밀도를 유지한다. 이러한 관점 전환이 시스템 수준 가속의 핵심이며, 이전 모든 방법이 달성하지 못한 부분이다.

## 방법 분석

### 인식 측: 홀짝 분할 토큰 재사용
- 시각 토큰을 홀짝 인덱스로 분할하고, 홀수 블록은 전체 순방향을 수행하며 키 투영을 캐시하여 참조로 사용
- 짝수 블록은 현재 토큰과 캐시된 키의 코사인 유사도를 계산하고, 유사도가 가장 낮은 top-ρN 토큰을 선택하여 업데이트(ρ는 업데이트 비율)
- 토큰 인덱스 선택은 첫 번째 레이어에서만 수행되며, 후속 레이어는 해당 인덱스를 재사용하여 중복 계산 방지
- 업데이트 토큰은 Q/K/V를 다시 계산하고, 재사용 토큰은 캐시된 KV 쌍을 직접 상속; 어텐션은 업데이트 토큰에 대해서만 계산되며, 잔차 후 모든 토큰은 MLP를 거쳐 전체 순방향 보장

### 행동 측: 2단계 압축 솔버
- 플로우 매칭 속도장의 특이값 스펙트럼을 분석하여 에너지가 처음 두 주성분에 집중되고 속도 진화가 저차원 구조를 가짐을 발견
- v0 및 v7을 앵커 속도로 선택: v0는 초기 전역 방향, v7은 중기 궤적 세분화를 나타냄
- 속도 근사: v_t ≈ a_t v_0 + b_t v_7 + ε_t, 최종 상태 x_T ≈ x_0 + α v_0 + β v_7 + b
- 경량 어댑터 g_φ가 계수 (α, β, b) = g_φ(v_0)를 직접 예측하며, 훈련 목표는 min_φ E[‖x_T^(2) − x_T^(10)‖_2^2]
- 백본 아키텍처는 변경하지 않고 솔버 단계만 교체

### 핵심 설계 결정
- r=0.4의 토큰 업데이트 비율: Table VII는 r이 1.0에서 0.4로 감소할 때 성공률이 94.4%에서 93.8%(-0.6%)로만 감소하지만, r=0.5에서는 92.6%(-1.8%)로 급락하여 0.4가 정밀도-효율의 임계점임을 시사
- v0 및 v7 앵커링( v0 및 v5 대신): v7은 궤적 끝에 더 가까워 세분화 방향을 더 잘 포착하고 끝단 오류 누적을 줄임

## 핵심 혁신

1. **최초로 Action Expert에 가속 초점을 맞춤**: 이전 모든 방법(ToMe, ToFu, V2Drop, SnapKV, SparseVLM)은 ViT와 LLM만 최적화했으며, Action Expert는 70% 이상의 지연 시간을 차지하지만 주목받지 못했다. 본 논문은 저랭크 속도 근사를 통해 솔버를 10단계에서 2단계로 압축하여 Action Expert 지연 시간을 81% 줄였으며, 이것이 2.37배 가속의 주요 원천이다.

2. **저랭크 속도 근사의 이론적 근거**: 플로우 매칭 속도장의 특이값 스펙트럼 에너지가 처음 두 주성분에 집중됨을 발견하여, 이는 2단계 압축의 수학적 기반을 제공한다—맹목적으로 단계를 줄이는 것이 아니라 속도장의 저차원 구조를 활용한 손실 압축이다. v0 및 v7 앵커링은 각각 전역 방향과 국소 세분화를 포착하며, 균일 샘플링 단계보다 더 지능적이다.

3. **구성 요소 수준이 아닌 시스템 수준 최적화**: 토큰 재사용(인식 측)과 솔버 압축(행동 측)은 독립적으로 설계되었지만 함께 배포되며, 소거 실험(Table III)은 두 가지를 결합하면 총 지연 시간이 293.2ms에서 111.6ms(2.63배)로 감소하는 반면, 단독 사용 시 각각 282.9ms 및 123.9ms로만 감소함을 보여준다. 이러한 "1+1>2" 시스템 효과는 구성 요소 수준 방법으로는 달성할 수 없다.

## 실험 및 결과

### LIBERO 벤치마크(Table I)
| 방법 | Mean SR (%) | Steps | Avg Time (ms) | FPS | TFLOPs |
|------|------------|-------|---------------|-----|--------|
| π0 | 92.3 | 10 | 276.4 | 3.6 | 4.48 |
| π0.5 | 94.4 | 10 | 286.9 | 3.5 | 4.48 |
| OpenVLA | 76.5 | 8 | 629.6 | 1.6 | 8.82 |
| X-VLA | 94.1 | 10 | 256.8 | 3.9 | – |
| Efficient VLA | 91.6 | 10 | 144.1 | 6.9 | 1.48 |
| π0+Ours | 91.0 | 2 | 156.2 | 6.4 | 2.86 |
| π0.5+Ours | 93.8 | 2 | 121.2 | 8.2 | 1.23 |

### 추론 시간 분해(Table II, LIBERO)
| 방법 | SR (%) | ViT (ms) | LLM (ms) | Action (ms) | Total (ms) | FPS |
|------|--------|----------|----------|-------------|------------|-----|
| π0.5 | 94.4 | 40.1 | 42.5 | 212.6 | 293.2 | 3.4 |
| ToMe | 75.3 | 31.8 | 32.8 | 202.3 | 266.9 | 3.7 |
| SnapKV | 89.8 | 27.2 | 26.1 | 196.3 | 249.6 | 4.0 |
| SparseVLM | 92.2 | 30.2 | 31.1 | 199.6 | 260.9 | 3.8 |
| Ours | 93.8 | 38.6 | 42.3 | 40.9 | 121.8 | 8.2 |

### 실제 로봇(Table IV, 6개 작업 평균)
| 방법 | SR (%) | SR@30s (%) |
|------|--------|------------|
| π0.5 | 97.2 | 77.1 |
| Ours | 95.4 | 82.3 |

핵심 발견: Ours는 SR@30s에서 기준을 역전한다(82.3% vs 77.1%). 이는 단일 성공률이 약간 감소했지만(-1.8%), 더 높은 추론 빈도(8.2 vs 3.5 FPS)로 로봇이 30초 창 내에서 작업을 완료할 더 많은 기회를 얻는다는 것을 의미한다—"빠르고 안정적인 것"이 "느리고 정확한 것"보다 우월하다는 직접적인 증거이다.

## 경계 및 한계

- 압축 전략은 짧은 시야 작업( LIBERO 및 RoboTwin 모두 단일 단계 또는 짧은 시퀀스 작업)에서만 검증되었으며, 긴 시야 계획 또는 고도로 동적인 환경(예: 이동 조작, 인간-로봇 상호작용)에서의 효과는 검증되지 않음
- 토큰 재사용은 인접 프레임의 시각적 내용이 매우 유사하다고 가정(코사인 유사도 > 0.98)하며, 빠른 움직임이나 장면 급변 시 이 가정이 무너질 수 있음. Table VII에서 r=0.5일 때 성공률이 1.8% 급락하는 것은 정밀도 절벽이 존재함을 시사
- 실제 로봇 평가는 6개 작업에 불과하며 모두 테이블 조작으로, 힘 제어, 손재주 조작 등 복잡한 시나리오를 포함하지 않음
- 다중 모달 입력(깊이 맵, 촉각) 또는 다양한 동작 공간(힘 제어, 임피던스 제어)으로의 확장은 언급되지 않음
- 어댑터 g_φ의 훈련 데이터 양, 학습률, 배치 크기 등 핵심 하이퍼파라미터가 공개되지 않아 재현 장벽이 높음

## 공학적 시사점

1. **먼저 Action Expert 지연 시간 비중을 확인**: VLA 파이프라인에서 행동 생성이 총 지연 시간의 50% 미만을 차지한다면, 본 논문의 솔버 압축 이점은 크게 줄어든다. 프로파일링을 먼저 수행하여 병목 지점을 확인한 후 이 방식을 채택할지 결정하는 것이 좋다.

2. **토큰 재사용 비율 r=0.4는 안전선**: Table VII는 r이 0.4에서 0.5로 감소할 때 성공률이 1.2% 급락(93.8%→92.6%)함을 보여 정밀도 절벽이 존재함을 시사한다. 재현 시 r=0.4에서 시작하여 점진적으로 낮추고 성공률을 모니터링하며, 무조건적으로 더 낮은 r 값을 추구하지 말 것.

3. **앵커 속도 선택은 재검증 필요**: 본 논문은 π0.5의 속도장 특이값 스펙트럼 분석을 기반으로 v0 및 v7을 선택했다. 다른 백본(예: OpenVLA, RT-2)을 사용하면 주성분 분포가 달라질 수 있으므로, 앵커를 결정하기 위해 SVD 분석을 다시 수행해야 하며 직접 복사할 수 없다.

4. **어댑터 g_φ 훈련 시 궤적 정렬 주의**: 훈련 목표는 2단계와 10단계 궤적의 MSE를 최소화하는 것이지만, 작업별 동작 스케일 차이가 크다(예: 파지 vs 배치). 작업별로 동작 공간을 정규화한 후 훈련하는 것이 좋으며, 그렇지 않으면 어댑터가 대규모 동작 작업에 편향될 수 있다.

5. **실제 배포 시 단일 SR보다 SR@30s에 주목**: 본 논문의 실제 실험은 Ours의 단일 SR이 약간 감소하지만 SR@30s가 역전함(82.3% vs 77.1%)을 보여주며, 높은 추론 빈도가 정밀도 손실을 보상함을 시사한다. 평가 시 "단위 시간당 성공 횟수"를 핵심 지표로 삼아야 하며, 단일 성공률이 아니다.
