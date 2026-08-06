---
$id: ent_paper_cosfly_vla_spatially_aware_vision_langua_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking'
  zh: 'CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking'
  ko: 'CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking'
summary:
  en: Dynamic target tracking is essential for Unmanned Aerial Vehicles (UAVs) operating in complex urban environments, where
    both the target and the camera viewpoint change continuously. Existing Vision-Language-Action (VLA) policies can track
    visible targets effectively, but their performance often degrades when buildings, vegetation, or roadside objects block
    the line of sight. During sustained.
  zh: CosFly-VLA 是一个面向无人机目标跟踪的空间感知视觉-语言-动作模型，由 0.8B 参数规模实现，通过联合预测目标可见性、当前目标框和 8 步 4-DoF 航点增量动作块，在部分可观测条件下实现闭环目标恢复。核心贡献在于提出渐进式训练配方——空间接地持续预训练（CPT）、三阶段课程
    SFT、思维链（CoT）训练和闭环强化学习（EG-FPO），在遮挡分级评估中显著超越通用 VLA 基线和检测-ReID-控制流水线。
  ko: Dynamic target tracking is essential for Unmanned Aerial Vehicles (UAVs) operating in complex urban environments, where
    both the target and the camera viewpoint change continuously. Existing Vision-Language-Action (VLA) policies can track
    visible targets effectively, but their performance often degrades when buildings, vegetation, or roadside objects block
    the line of sight. During sustained.
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
- cosfly
- vla
- spatially
- aware
- vision
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
  title: 'arXiv:2607.15004 CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking'
  url: https://arxiv.org/abs/2607.15004
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

CosFly-VLA 是一个面向无人机目标跟踪的空间感知视觉-语言-动作模型，由 0.8B 参数规模实现，通过联合预测目标可见性、当前目标框和 8 步 4-DoF 航点增量动作块，在部分可观测条件下实现闭环目标恢复。核心贡献在于提出渐进式训练配方——空间接地持续预训练（CPT）、三阶段课程 SFT、思维链（CoT）训练和闭环强化学习（EG-FPO），在遮挡分级评估中显著超越通用 VLA 基线和检测-ReID-控制流水线。

## 它改变了什么

这篇工作真正改变的是对无人机跟踪问题的建模方式：它不再把跟踪拆成"检测+ReID+控制"的串联流水线，也不把 VLA 当作单纯的感知-动作映射器，而是将问题重新定义为部分可观测马尔可夫决策过程下的闭环目标恢复。作者明确指出，默认窗口构建器过滤掉 4/5 和 5/5 不可见输入窗口会让数据集看起来更干净，但恰恰移除了与重新捕获目标最相关的片段——这个观察直击当前 VLA 评估协议的软肋。

另一个关键转变在于训练范式的认知：静态结构化输出的改进（如更低的 ADE）并不自动意味着最优在策略行为，因为执行动作会改变后续观测与状态分布。这一判断直接催生了闭环 RL 阶段的设计——策略必须在自身动作诱导的观测分布上优化，而非在固定数据集上蒸馏。对行业而言，这暗示着"更大模型+更多数据"的路线在部分可观测控制任务上存在天花板，需要显式引入闭环反馈机制。

## 方法拆解

### 架构设计
- 骨干：Qwen3.5 作为视觉-语言骨干，LoRA 微调（r=16，α=32，dropout 0.05）
- 连接器：0.8B 配置使用 2 层/8 头 Transformer 连接器，meta-query 池化含 16 个动作查询、16 个 bbox 查询、1 个可见性查询
- 动作专家：12 层 DiT（Diffusion Transformer），adaLN 调制 + 每块交叉注意力，输出 8×4 动作块（Δx, Δy, Δz, Δψ），每维归一化尺度 (5, 5, 2, 30)
- 辅助头：bbox 和可见性头为 2 层 MLP（GELU + LayerNorm）

### 渐进式训练配方
1. **空间接地 CPT**：全参数（含 ViT）持续预训练，目的不仅是增加数据，而是让冻结的 Qwen3.5 骨干暴露于目标缺失时仍有信息量的航拍几何线索
2. **三阶段课程 SFT**：从空间接地 CPT 骨干开始，批大小 128，峰值学习率 1×10⁻⁴
3. **CoT 训练**：批大小 64，峰值学习率 5×10⁻⁵，注入恢复导向的推理能力
4. **闭环 RL（CosFly-RFT）**：批大小 32，峰值学习率 1×10⁻⁵，仅更新动作头

### 闭环 RL 关键设计（EG-FPO）
- 从 SFT+CoT 检查点热启动，冻结骨干、bbox 头和可见性头
- 每条路径从固定方差高斯代理采样 K 条在策略轨迹：a ∼ 𝒩(μθ(s), diag(σ²))
- 组相对优势：Âi = (Ri − μ𝒢)/(σ𝒢 + ε)，每组增加一条专家回放轨迹作为高回报锚点
- 策略比率用固定方差高斯代理计算：ρi,t(θ) = exp(log πθ(ai,t|si,t) − log πθ_old(ai,t|si,t))
- 目标函数：ℒEG-FPO(θ) = −𝔼i,t[min(ρi,tÂi, clip(ρi,t, 1−δ, 1+δ)Âi)]，δ=0.2
- 奖励：rt = −wd·|dt−d*|/d* + wiou·IoU(b̂t, bt^GT) + rt^coll + rt^succ，其中 d*=28 m，wd=1.0，wiou=0.5

### 数据与 rollout
- RL split：550 条路径跨 11 张地图（440 训练 + 110 测试），外加 20 条校准路径，产生 104,250 帧
- 闭环评估：一个决策步跨 5 个模拟帧（2.5 s），图像尺寸 640×360
- 更新后策略热重载入 rollout 服务器，下一迭代用更新策略收集数据

## 关键创新

**1. 遮挡分级的评估协议**：将窗口按不可见帧数分为 Easy（0 不可见）、Medium（1 不可见）、Hard（2 不可见），并保留 3 个以上不可见帧的窗口用于闭环评估。这打破了传统评估中"过滤困难样本"的惯例，使得 Hard 场景下的恢复能力成为可量化的核心指标。

**2. 专家引导的流策略优化（EG-FPO）**：将 flow-matching 动作生成、PPO 式似然比裁剪和 GRPO 式组相对优势归一化三者结合。关键创新在于用固定方差高斯代理计算可解析的 log 概率，不替换底层 flow-matching 解码器，同时每组加入专家回放轨迹作为高回报锚点，防止所有在线 rollout 失败时组优势崩溃。

**3. 空间接地 CPT 的独特定位**：CPT 不是简单的预训练数据扩充，而是让骨干在目标缺失时仍能提取有信息量的航拍几何线索。消融显示 CPT 对 unseen-test 的跨地图泛化增益最大（unseen-test 整体 ADE 降低 9.2%，Hard ADE 降低 13.4%），这验证了"空间接地"比"数据量"更关键。

## 实验与结果

### 开放环评估（Town10HD）
| 方法 | Seen-test ADE | Unseen-test ADE | Seen-test Hard ADE | Unseen-test Hard ADE |
|---|---|---|---|---|
| OpenVLA | 1.0887 | 0.9160 | 1.3542 | 1.1671 |
| CosFly-VLA-0.8B (SFT) | 0.8247 | 0.6364 | 0.9599 | 0.8039 |
| CosFly-VLA-0.8B (SFT+CoT) | 0.7175 | 0.5931 | 0.7218 | 0.7096 |

相对 OpenVLA，SFT+CoT 变体在 seen-test 整体 ADE 降低 34.1%（1.0887→0.7175），unseen-test 降低 35.3%（0.9160→0.5931）；Hard ADE 在 seen-test 降低 46.7%、unseen-test 降低 39.2%。最佳 bbox 接地：0.659/0.635 IoU 和 9.4/11.4 px 中心误差（seen-test/unseen-test）。

### 闭环评估（CARLA）
| 方法 | Seen-test SR | Seen-test ADE | Unseen-test SR | Unseen-test ADE |
|---|---|---|---|---|
| OpenVLA | 57% | 9.0 | 80% | 6.9 |
| CosFly-VLA-0.8B (SFT) | 70% | 8.9 | 79% | 8.8 |
| CosFly-VLA-0.8B (RL) | 74% | 8.1 | 82% | 6.3 |

相对 OpenVLA，RL 变体 seen-test SR 提升 17 个百分点（57%→74%，相对增加 29.8%），unseen-test 提升 2 点（80%→82%，相对增加 2.5%）；rollout ADE seen-test 降低 10.0%（9.0→8.1）、unseen-test 降低 8.7%（6.9→6.3）；stand-off 距离误差分别降低 20.6% 和 18.2%。

### 训练配方消融
| 配方 | Seen-test ADE | Unseen-test ADE |
|---|---|---|
| SFT only | 0.8924 | 0.7087 |
| +课程学习 | 0.8295 | 0.7007 |
| +空间接地 CPT | 0.8247 | 0.6364 |
| +CoT 监督 | 0.7175 | 0.5931 |

课程学习使 seen-test 整体 ADE 相对 SFT only 降低 7.0%；空间接地 CPT 对应 unseen-test 整体 ADE 降低 9.2%、Hard ADE 降低 13.4%；CoT 阶段在 seen-test Hard 上边际增益最大（ADE 降低 24.8%）。从 SFT-only 到最终 +CoT 变体，整体 ADE seen-test 降低 19.6%、unseen-test 降低 16.3%，Hard ADE 分别降低 30.9% 和 23.0%。

## 边界与局限

作者明确承认的边界包括：训练数据仅来自 Town10HD 行人场景，未覆盖车辆、无人机、动物等其他目标类型；评估使用真值状态历史而非预测状态反馈，对预测框历史反馈的鲁棒性未验证；RL 阶段使用单一奖励公式和固定 11 地图划分，奖励设计与地图多样性可扩展；0.8B 配置使用 2 层/8 头连接器，扩展到更大骨干需使用更浅连接器以适配内存预算；所有闭环评估仅在 CARLA 模拟中进行，未测试真实部署。此外，目标行为相对简单（多数接近恒定速度、室外场景），室外到室内过渡、密集人群、突然意图变化、对抗性运动等挑战性案例未充分表示。定量比较使用 0.8B 模型和聚合 split 级指标，未建立到 2B/9B 配置的一对一扩展，也未量化多种子方差。

## 工程启示

复现或采用此方法时，最需要先核对的是**闭环 RL 的 rollout 基础设施**：550 条路径跨 11 张地图（440 训练 + 110 测试）加 20 条校准路径，产生 104,250 帧，这个数据规模对单节点八卡 A800 是可承受的，但 rollout 收集器与训练机之间的 JSON 传输、热重载机制是工程瓶颈。最容易踩坑的地方在于**组相对优势的稳定性**——如果一组内所有在线 rollout 都失败，优势估计会崩溃，因此每组必须加入专家回放轨迹作为高回报锚点；实践中对负优势异常值使用双重裁剪，并使用仅在线 KL 早停（排除专家步骤，因为大专家比率预期将策略拉向锚点）。

另一个关键决策是**从 SFT 检查点直接热启动 RL**，而非先做 BC v0.1 诊断实验——作者发现 BC 诊断虽改善 bbox IoU 但导致碰撞回归。这意味着如果你计划复现，不要跳过 SFT+CoT 阶段直接做 RL，否则策略会陷入次优。推理时使用确定性均值动作、8 个 flow 积分步，单卡 A100-80GB 可达到 10 Hz 控制频率；闭环评估中一个决策步跨 5 个模拟帧（2.5 s），图像尺寸 640×360，d*=28 m——这些参数需严格对齐才能复现论文中的 SR 和 ADE 数字。

## Overview
Dynamic target tracking is essential for Unmanned Aerial Vehicles (UAVs) operating in complex urban environments, where both the target and the camera viewpoint change continuously. Existing Vision-Language-Action (VLA) policies can track visible targets effectively, but their performance often degrades when buildings, vegetation, or roadside objects block the line of sight. During sustained occlusion, a policy may lose the target state, execute actions toward an incorrect region, and amplify this error through subsequent observations until re-acquisition becomes impossible. To this end, we present CosFly-VLA, a spatially aware VLA model that jointly grounds the target, estimates its visibility, and generates continuous flight actions through a structured prediction interface. To train this policy, we use a large-scale recipe over diverse data sources. Spatially Grounded Continued Pretraining (CPT) on a 500k mixed pool injects UAV-view depth, distance, and 3-D spatial reasoning. A three-stage Curriculum-based Supervised Fine-Tuning (SFT) process then specializes the tracker through multi-head warm-up followed by two-stage curriculum learning over natural and hard / long-occlusion data. Chain-of-Thought (CoT) training subsequently teaches recovery-oriented reasoning traces before structured answers. Finally, a closed-loop Reinforcement Learning (RL) stage optimizes tracking behavior with a multi-component reward covering stand-off tracking, grounding quality, collision avoidance, and task success. Relative to OpenVLA, CosFly-VLA-0.8B reduces open-loop Average Displacement Error (ADE) by 34.1% on seen-test and 35.3% on unseen-test. Closed-loop optimization improves Success Rate (SR) by 29.8% and 2.5%, respectively. These results demonstrate progress from visible-frame imitation toward spatially grounded action-closed-loop control, evaluated under a shared oracle state history.

## 参考
- https://arxiv.org/abs/2607.15004

## 개요

CosFly-VLA는 드론 목표 추적을 위한 공간 인식 비전-언어-행동 모델로, 0.8B 파라미터 규모로 구현되었으며 목표 가시성, 현재 목표 박스, 8단계 4-DoF 웨이포인트 증분 행동 블록을 공동 예측하여 부분 관측 조건에서 폐루프 목표 복구를 구현합니다. 핵심 기여는 점진적 훈련 레시피(공간 접지 지속 사전훈련(CPT), 3단계 커리큘럼 SFT, 사고 사슬(CoT) 훈련, 폐루프 강화학습(EG-FPO))를 제안한 것이며, 폐색 등급 평가에서 일반 VLA 베이스라인과 탐지-ReID-제어 파이프라인을 크게 능가합니다.

## 무엇을 바꾸었는가

이 연구가 진정으로 바꾼 것은 드론 추적 문제의 모델링 방식입니다: 더 이상 추적을 "탐지+ReID+제어"의 직렬 파이프라인으로 분해하지 않으며, VLA를 단순한 지각-행동 매퍼로 취급하지 않고, 문제를 부분 관측 마르코프 결정 프로세스 하의 폐루프 목표 복구로 재정의합니다. 저자들은 기본 창 구성기가 4/5 및 5/5 비가시 입력 창을 필터링하면 데이터셋이 더 깨끗해 보이지만, 정확히 목표 재포착과 가장 관련된 세그먼트를 제거한다고 명시합니다 — 이 관찰은 현재 VLA 평가 프로토콜의 약점을 정확히 겨냥합니다.

또 다른 핵심 전환은 훈련 패러다임에 대한 인식입니다: 정적 구조화 출력의 개선(예: 더 낮은 ADE)이 자동으로 최적의 인-폴리시 행동을 의미하지 않습니다. 실행된 행동이 후속 관측과 상태 분포를 변경하기 때문입니다. 이 판단은 폐루프 RL 단계의 설계를 직접 촉발했습니다 — 정책은 고정 데이터셋에서 증류하는 것이 아니라 자체 행동이 유도한 관측 분포에서 최적화되어야 합니다. 업계 관점에서 이는 "더 큰 모델+더 많은 데이터" 경로가 부분 관측 제어 작업에서 한계가 있으며, 명시적 폐루프 피드백 메커니즘의 도입이 필요함을 시사합니다.

## 방법 분해

### 아키텍처 설계
- 백본: Qwen3.5를 비전-언어 백본으로 사용, LoRA 미세조정(r=16, α=32, dropout 0.05)
- 커넥터: 0.8B 구성은 2레이어/8헤드 Transformer 커넥터 사용, meta-query 풀링에 16개 행동 쿼리, 16개 bbox 쿼리, 1개 가시성 쿼리 포함
- 행동 전문가: 12레이어 DiT(Diffusion Transformer), adaLN 변조 + 블록별 교차 주의, 8×4 행동 블록 출력(Δx, Δy, Δz, Δψ), 각 차원 정규화 스케일 (5, 5, 2, 30)
- 보조 헤드: bbox 및 가시성 헤드는 2레이어 MLP(GELU + LayerNorm)

### 점진적 훈련 레시피
1. **공간 접지 CPT**: 전체 파라미터(ViT 포함) 지속 사전훈련, 목적은 단순히 데이터 증가가 아니라 동결된 Qwen3.5 백본이 목표 부재 시에도 정보가 있는 항공 기하학적 단서에 노출되도록 하는 것
2. **3단계 커리큘럼 SFT**: 공간 접지 CPT 백본에서 시작, 배치 크기 128, 피크 학습률 1×10⁻⁴
3. **CoT 훈련**: 배치 크기 64, 피크 학습률 5×10⁻⁵, 복구 지향 추론 능력 주입
4. **폐루프 RL(CosFly-RFT)**: 배치 크기 32, 피크 학습률 1×10⁻⁵, 행동 헤드만 업데이트

### 폐루프 RL 핵심 설계(EG-FPO)
- SFT+CoT 체크포인트에서 핫 스타트, 백본, bbox 헤드, 가시성 헤드 동결
- 각 경로는 고정 분산 가우시안 프록시에서 K개의 인-폴리시 궤적 샘플링: a ∼ 𝒩(μθ(s), diag(σ²))
- 그룹 상대 이점: Âi = (Ri − μ𝒢)/(σ𝒢 + ε), 각 그룹에 전문가 리플레이 궤적을 고보상 앵커로 추가
- 정책 비율은 고정 분산 가우시안 프록시로 계산: ρi,t(θ) = exp(log πθ(ai,t|si,t) − log πθ_old(ai,t|si,t))
- 목적 함수: ℒEG-FPO(θ) = −𝔼i,t[min(ρi,tÂi, clip(ρi,t, 1−δ, 1+δ)Âi)], δ=0.2
- 보상: rt = −wd·|dt−d*|/d* + wiou·IoU(b̂t, bt^GT) + rt^coll + rt^succ, 여기서 d*=28 m, wd=1.0, wiou=0.5

### 데이터 및 롤아웃
- RL 분할: 11개 맵에 걸친 550개 경로(440 훈련 + 110 테스트), 추가로 20개 보정 경로, 총 104,250 프레임 생성
- 폐루프 평가: 하나의 결정 단계가 5개 시뮬레이션 프레임(2.5초)에 걸침, 이미지 크기 640×360
- 업데이트된 정책을 롤아웃 서버에 핫 리로드, 다음 반복에서는 업데이트된 정책으로 데이터 수집

## 핵심 혁신

**1. 폐색 등급 평가 프로토콜**: 창을 비가시 프레임 수에 따라 Easy(0 비가시), Medium(1 비가시), Hard(2 비가시)로 분류하고, 3개 이상의 비가시 프레임이 있는 창은 폐루프 평가에 유지합니다. 이는 전통적 평가에서 "어려운 샘플 필터링" 관례를 깨며, Hard 시나리오에서의 복구 능력을 정량화 가능한 핵심 지표로 만듭니다.

**2. 전문가 유도 흐름 정책 최적화(EG-FPO)**: flow-matching 행동 생성, PPO식 우도비 클리핑, GRPO식 그룹 상대 이점 정규화를 결합합니다. 핵심 혁신은 고정 분산 가우시안 프록시로 해석 가능한 로그 확률을 계산하고, 기본 flow-matching 디코더를 교체하지 않으면서 각 그룹에 전문가 리플레이 궤적을 고보상 앵커로 추가하여 모든 온라인 롤아웃이 실패할 때 그룹 이점 붕괴를 방지하는 것입니다.

**3. 공간 접지 CPT의 독특한 위치**: CPT는 단순한 사전훈련 데이터 확장이 아니라, 백본이 목표 부재 시에도 정보가 있는 항공 기하학적 단서를 추출할 수 있게 합니다. 절제 실험은 CPT가 unseen-test의 교차 맵 일반화 이득이 가장 크다는 것을 보여줍니다(unseen-test 전체 ADE 9.2% 감소, Hard ADE 13.4% 감소). 이는 "공간 접지"가 "데이터 양"보다 더 중요함을 검증합니다.

## 실험 및 결과

### 개방 루프 평가(Town10HD)
| 방법 | Seen-test ADE | Unseen-test ADE | Seen-test Hard ADE | Unseen-test Hard ADE |
|---|---|---|---|---|
| OpenVLA | 1.0887 | 0.9160 | 1.3542 | 1.1671 |
| CosFly-VLA-0.8B (SFT) | 0.8247 | 0.6364 | 0.9599 | 0.8039 |
| CosFly-VLA-0.8B (SFT+CoT) | 0.7175 | 0.5931 | 0.7218 | 0.7096 |

OpenVLA 대비 SFT+CoT 변형은 seen-test 전체 ADE 34.1% 감소(1.0887→0.7175), unseen-test 35.3% 감소(0.9160→0.5931); Hard ADE는 seen-test 46.7%, unseen-test 39.2% 감소. 최적 bbox 접지: 0.659/0.635 IoU 및 9.4/11.4 px 중심 오차(seen-test/unseen-test).

### 폐루프 평가(CARLA)
| 방법 | Seen-test SR | Seen-test ADE | Unseen-test SR | Unseen-test ADE |
|---|---|---|---|---|
| OpenVLA | 57% | 9.0 | 80% | 6.9 |
| CosFly-VLA-0.8B (SFT) | 70% | 8.9 | 79% | 8.8 |
| CosFly-VLA-0.8B (RL) | 74% | 8.1 | 82% | 6.3 |

OpenVLA 대비 RL 변형은 seen-test SR 17%포인트 향상(57%→74%, 상대 증가 29.8%), unseen-test 2%포인트 향상(80%→82%, 상대 증가 2.5%); 롤아웃 ADE seen-test 10.0% 감소(9.0→8.1), unseen-test 8.7% 감소(6.9→6.3); stand-off 거리 오차는 각각 20.6% 및 18.2% 감소.

### 훈련 레시피 절제
| 레시피 | Seen-test ADE | Unseen-test ADE |
|---|---|---|
| SFT only | 0.8924 | 0.7087 |
| +커리큘럼 학습 | 0.8295 | 0.7007 |
| +공간 접지 CPT | 0.8247 | 0.6364 |
| +CoT 감독 | 0.7175 | 0.5931 |

커리큘럼 학습은 seen-test 전체 ADE를 SFT only 대비 7.0% 감소; 공간 접지 CPT는 unseen-test 전체 ADE 9.2%, Hard ADE 13.4% 감소; CoT 단계는 seen-test Hard에서 한계 이득이 가장 큼(ADE 24.8% 감소). SFT-only에서 최종 +CoT 변형까지 전체 ADE는 seen-test 19.6%, unseen-test 16.3% 감소, Hard ADE는 각각 30.9% 및 23.0% 감소.

## 경계 및 한계

저자들이 명시적으로 인정한 경계는 다음과 같습니다: 훈련 데이터는 Town10HD 보행자 시나리오에서만 나왔으며, 차량, 드론, 동물 등 다른 목표 유형을 포함하지 않음; 평가는 예측 상태 피드백이 아닌 실제 상태 기록을 사용하므로 예측 박스 기록 피드백에 대한 견고성은 검증되지 않음; RL 단계는 단일 보상 공식과 고정 11개 맵 분할을 사용하므로 보상 설계와 맵 다양성 확장이 필요; 0.8B 구성은 2레이어/8헤드 커넥터를 사용하며, 더 큰 백본으로 확장하려면 메모리 예산에 맞게 더 얕은 커넥터를 사용해야 함; 모든 폐루프 평가는 CARLA 시뮬레이션에서만 수행되었으며 실제 배포는 테스트되지 않음. 또한 목표 행동이 상대적으로 단순하고(대부분 거의 일정한 속도, 실외 시나리오), 실외에서 실내로의 전환, 밀집 군중, 갑작스러운 의도 변화, 적대적 움직임 등의 도전적 사례가 충분히 표현되지 않았습니다. 정량적 비교는 0.8B 모델과 집계 분할 수준 지표를 사용했으며, 2B/9B 구성으로의 일대일 확장이 확립되지 않았고 다중 시드 분산도 정량화되지 않았습니다.

## 엔지니어링 시사점

이 방법을 재현하거나 채택할 때 가장 먼저 확인해야 할 것은 **폐루프 RL의 롤아웃 인프라**입니다: 11개 맵에 걸친 550개 경로(440 훈련 + 110 테스트)에 20개 보정 경로를 더해 104,250 프레임이 생성되는데, 이 데이터 규모는 단일 노드 8xA800에서 감당 가능하지만 롤아웃 수집기와 훈련 머신 간의 JSON 전송, 핫 리로드 메커니즘이 엔지니어링 병목입니다. 가장 함정에 빠지기 쉬운 곳은 **그룹 상대 이점의 안정성**입니다 — 그룹 내 모든 온라인 롤아웃이 실패하면 이점 추정이 붕괴되므로, 각 그룹에 전문가 리플레이 궤적을 고보상 앵커로 포함해야 합니다; 실제로는 음의 이점 이상값에 이중 클리핑을 사용하고, 온라인 전용 KL 조기 종료를 사용합니다(전문가 단계 제외, 큰 전문가 비율이 정책을 앵커로 끌어당길 것으로 예상되기 때문).

또 다른 핵심 결정은 **SFT 체크포인트에서 직접 RL을 핫 스타트**하는 것이며, 먼저 BC v0.1 진단 실험을 수행하지 않는 것입니다 — 저자들은 BC 진단이 bbox IoU를 개선하지만 충돌 회귀를 초래한다는 것을 발견했습니다. 이는 재현을 계획한다면 SFT+CoT 단계를 건너뛰고 직접 RL을 수행하지 말아야 함을 의미합니다. 그렇지 않으면 정책이 차선에 빠집니다. 추론 시 결정적 평균 행동, 8개 flow 적분 단계를 사용하며, 단일 A100-80GB에서 10Hz 제어 주파수 달성 가능; 폐루프 평가에서 하나의 결정 단계는 5개 시뮬레이션 프레임(2.5초)에 걸치고, 이미지 크기는 640×360, d*=28 m — 이러한 파라미터는 논문의 SR 및 ADE 수치를 재현하려면 엄격히 정렬해야 합니다.
