---
$id: ent_paper_s_squared_vla_decoupling_semantic_spatia_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving'
  zh: 'S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving'
  ko: 'S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving'
summary:
  en: Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving,
    yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical
    gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action
    (VLA) architectures.
  zh: S²-VLA 是一种面向自动驾驶的双流视觉-语言-动作（VLA）架构，由研究团队提出，旨在显式解耦语义推理与空间几何感知，以缓解现有 VLM 在低层连续控制中的语义-物理鸿沟。其核心贡献在于通过多尺度语义流与任务驱动空间流的并行设计，结合双流规划适配器，在仅使用单目前视相机的情况下，于
    NAVSIM 基准上达到 PDMS 87.1，超越多数融合 LiDAR 的基线方法。
  ko: Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving,
    yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical
    gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action
    (VLA) architectures.
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
- s
- squared
- vla
- decoupling
- semantic
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.13926 S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action'
  url: https://arxiv.org/abs/2607.13926
  date: '2026-07-15'
  accessed_at: '2026-08-05'
---

## 概述

S²-VLA 是一种面向自动驾驶的双流视觉-语言-动作（VLA）架构，由研究团队提出，旨在显式解耦语义推理与空间几何感知，以缓解现有 VLM 在低层连续控制中的语义-物理鸿沟。其核心贡献在于通过多尺度语义流与任务驱动空间流的并行设计，结合双流规划适配器，在仅使用单目前视相机的情况下，于 NAVSIM 基准上达到 PDMS 87.1，超越多数融合 LiDAR 的基线方法。

## 它改变了什么

现有 VLA 方法将感知与控制统一为单一策略，导致语义与空间信息在深度网络中纠缠并逐步坍缩。这种坍缩并非简单的信息丢失，而是不可逆地破坏了安全关键导航所需的细粒度几何先验——例如车道边界、可行驶区域与障碍物距离。作者敏锐地指出，问题的根源在于离散语言 token 与连续轨迹之间的固有失配，以及单流架构将高层语义表征直接映射到低层控制时，跨模态对齐发生在重度压缩的 embedding 上，从而产生系统性偏置。

S²-VLA 真正改变的是“语义与空间必须共享同一表征空间”这一隐含假设。它通过物理上分离两个信息流，让语义流专注于意图理解与高层推理，空间流专注于几何重建与密集预测，最后在规划阶段才进行受控融合。这种设计不仅缓解了表征坍缩，还使得辅助感知任务（如 BEV 地图重建与智能体检测）能够以显式监督的方式注入空间先验，而非依赖隐式学习。

## 方法拆解

### 双流架构总览
S²-VLA 将输入（导航命令 C_nav、自车运动历史 T_hist、前视图像 I）分别送入语义流与空间流，最终通过双流规划适配器融合生成轨迹。

### 语义流（Multi-Scale Semantic Stream）
- 骨干：InternVL3-2B（InternViT 视觉编码器 + Qwen2.5 语言模型）。
- 注入 N_act=64 个可学习动作查询 Q_act，与文本和视觉 token 联合编码。
- 稀疏多尺度采样：仅从层 L={3,8,13,18,23,24} 提取隐藏状态，形成多尺度特征集 {(V_sem^(l), V_act^(l))}。
- 自车历史经 MLP 编码为 E_ego∈ℝ^(1×d_vlm)，在每层与动作中心特征拼接形成统一状态记忆 E_mem。

### 空间流（Task-Driven Spatial Stream）
- 动态分辨率：将高分辨率图像划分为 N_patch=9 个 patch（8 局部 + 1 全局），每个 patch 引入 N_vis=64 个视觉查询。
- 编码后视觉查询重组为 V_vis∈ℝ^(B×(N_patch×N_vis)×C)，添加 tile 级位置嵌入后经 Transformer 编码器。
- **Map Head**：1D token 序列重塑为 2D 网格 V_2D∈ℝ^(d×24×24)，经上采样输出 BEV 语义地图 M_hat_sem∈ℝ^(C×128×256)，覆盖 X∈[0,32]m、Y∈[−32,32]m，由加权交叉熵 L_map 监督。
- **Agent Head**：DETR 范式，N_agent=30 个查询，匈牙利匹配，损失为 L_agent=λ_reg·L_L1 + λ_cls·L_BCE。
- 中间表征 V 经线性投影形成 V_spatial，作为规划适配器的空间约束。

### 双流规划适配器
- 初始化 M=8 个规划 token P^(0)∈ℝ^(M×d)。
- 阶段 1（语义对齐）：规划 token 与多尺度语义特征 V_sem 和状态记忆 E_mem 执行并行交叉注意力，门控参数 g∈ℝ^d 调制融合：P_fuse=P^(l−1)+Linear([tanh(g)⊙P_raw; P_ego; P_sa])。
- 阶段 2（空间细化）：注入 V_spatial，P_vis=P_fuse+MHCA₃(P_fuse, V_spatial, V_spatial)，再经 FFN。
- 轨迹解码：MLP 预测 Ŷ∈ℝ^(M×3)，损失为 L_plan=L_L1 + λ_smooth·Σ SmoothL1(a, j)。
- 总损失：L_total=λ_plan·L_plan + λ_agent·L_agent + λ_map·L_map。

## 关键创新

1. **显式双流解耦**：不同于现有 VLA 的单流纠缠设计，S²-VLA 在架构层面强制分离语义与空间处理路径。这一设计直接针对空间表征坍缩问题，使得几何先验可以在独立流中被显式监督和保留，而非在深度抽象中被动丢失。

2. **任务驱动的空间流**：空间流不仅提取视觉特征，还通过 Map Head 和 Agent Head 输出结构化的 BEV 语义地图与智能体预测。这种“以任务为监督”的空间特征提取方式，确保了注入规划器的 V_spatial 是经过任务验证的几何信息，而非通用的视觉 embedding。

3. **门控融合机制**：规划适配器中的可学习门控参数 g 允许模型自适应地权衡语义与空间特征的贡献。这一机制避免了简单拼接带来的特征冗余，使得高层意图与低层几何能够在规划阶段动态协调，而非静态叠加。

## 实验与结果

实验在 NAVSIM 基准上进行，采用 PDMS 综合指标（由 NC、DAC、TTC、Comf、EP 五项计算）。关键结果如下：

| 方法 | NC | DAC | EP | TTC | Comf | PDMS |
|------|-----|-----|-----|-----|------|------|
| UniAD | 97.8 | 91.9 | 78.8 | 92.9 | 100 | 83.4 |
| PARA-Drive | 97.9 | 92.4 | 79.3 | 93.0 | 99.8 | 84.0 |
| DiffusionDrive | 98.2 | 96.2 | 82.2 | 94.7 | 100 | 88.1 |
| InternVL3-2B | 97.6 | 93.1 | 79.1 | 92.7 | 100 | 84.1 |
| ReCogDrive* | 98.1 | 94.7 | 80.9 | 94.2 | 100 | 86.5 |
| **S²-VLA** | **98.4** | **94.9** | **81.6** | **94.6** | **100** | **87.1** |

- S²-VLA 仅用单目相机即超越融合 LiDAR 的 ARTEMIS（87.0）与 DRAMA（86.9）。
- 相比相同骨干的朴素 VLM 基线（InternVL3-2B，PDMS 84.1），S²-VLA 提升 3.0 点（由表内数值 84.1→87.1 计算）。
- 消融实验显示：加入语义特征提升 PDMS +1.5（84.1→85.6），添加空间流再 +0.6（85.6→86.2），加入辅助感知任务最终 +0.9（86.2→87.1）。
- DiffusionDrive 的 PDMS 88.1 略高，主要优势在 DAC（96.2 vs 94.9），但其依赖迭代式扩散解码器与显式 LiDAR 点云。

## 边界与局限

作者明确承认空间特征的密集提取与双流融合带来非平凡的计算开销，未来需开发更稀疏的特征表征机制。此外，双流架构与训练范式正交，作者排除了基线中的闭环强化学习后训练（如 GRPO），以确保网络设计公平比较，但这也意味着当前结果未反映后训练可能带来的增益。论文未明确讨论在极端天气、传感器故障或高动态场景下的鲁棒性表现，也未提供推理延迟的具体数字。

## 工程启示

复现时需优先核对以下关键配置：稀疏采样层 L={3,8,13,18,23,24} 的选择直接影响多尺度语义特征的丰富度；N_patch=9 的动态分辨率策略对空间流的 BEV 重建质量至关重要；门控参数 g 的初始化与训练稳定性需仔细调优。最容易踩坑的地方在于三阶段训练流程——第一阶段 SFT 使用 ReCogDrive VQA 数据（3 epochs），第二、三阶段在 NAVSIM 上各 4 epochs，若阶段间未正确冻结相应模块（如第二阶段冻结 VLM 骨干并应用 LoRA，第三阶段冻结感知与意图组件），会导致特征分布偏移。损失权重 λ_plan=1.0、λ_agent=0.1、λ_map=0.5、λ_smooth=0.5 需严格保持，其中 λ_smooth 对轨迹平滑性影响显著，过大会导致规划过于保守。对于下游团队，若需部署到实车，建议先验证 BEV 地图输出（128×256）与真实世界坐标的对齐精度，因为该模块是空间流的核心监督信号，其误差会直接传导至规划轨迹。

## Overview
Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. While Vision-Language-Action (VLA) architectures attempt to bridge this gap by unifying perception and control into a single policy, this entanglement creates a new bottleneck. Standard VLAs experience a severe spatial representation collapse, which irreversibly degrades the fine-grained spatial and geometric priors essential for safe, boundary-aware navigation. To address this limitation, we propose the S-squared-VLA, which explicitly decouples the semantic and spatial streams in Vision-Language-Action models. The semantic stream leverages hierarchical bridging to extract multi-scale VLM features for robust intent reasoning. In parallel, an independent spatial stream bypasses the autoregressive language bottleneck, directly preserving uncompressed spatial features from the visual encoder. By integrating auxiliary perception supervision, this stream explicitly equips the model with rich spatial and geometric priors. Finally, a dual-stream planning adapter fuses high-level semantic intent with precise spatial constraints via cascaded attention mechanisms. Evaluations on the NAVSIM closed-loop benchmark show that S-squared-VLA achieves a Predictive Driver Model Score (PDMS) of 87.1, establishing a new state-of-the-art for VLA models under a purely supervised fine-tuning (SFT) setting. By mitigating the spatial representation collapse of traditional VLMs, our framework significantly outperforms baselines, achieving the highest No Collision (NC) rate of 98.4 among all evaluated methods.

## 参考
- https://arxiv.org/abs/2607.13926

## 개요

S²-VLA는 자율주행을 위한 이중 스트림 비전-언어-행동(VLA) 아키텍처로, 연구팀이 제안했으며 의미론적 추론과 공간 기하학적 인식을 명시적으로 분리하여 기존 VLM이 저수준 연속 제어에서 겪는 의미-물리적 간극을 완화하는 것을 목표로 한다. 핵심 기여는 다중 스케일 의미 스트림과 작업 주도 공간 스트림의 병렬 설계와 이중 스트림 계획 어댑터를 결합하여, 단일 전방 카메라만 사용하면서 NAVSIM 벤치마크에서 PDMS 87.1을 달성하여 LiDAR를 융합한 대부분의 기준 방법을 능가한다는 점이다.

## 그것이 바꾼 것

기존 VLA 방법은 인식과 제어를 단일 정책으로 통합하여 의미 정보와 공간 정보가 심층 네트워크에서 얽히고 점차 붕괴되도록 만든다. 이러한 붕괴는 단순한 정보 손실이 아니라, 안전에 중요한 내비게이션에 필요한 미세한 기하학적 사전 지식(예: 차선 경계, 주행 가능 영역, 장애물 거리)을 비가역적으로 파괴한다. 저자는 문제의 근원이 이산 언어 토큰과 연속 궤적 간의 고유한 불일치, 그리고 단일 스트림 아키텍처가 고수준 의미 표현을 저수준 제어에 직접 매핑할 때 교차 모달 정렬이 심하게 압축된 임베딩에서 발생하여 체계적 편향을 초래한다는 점을 날카롭게 지적한다.

S²-VLA가 실제로 바꾼 것은 "의미와 공간이 동일한 표현 공간을 공유해야 한다"는 암묵적 가정이다. 두 정보 스트림을 물리적으로 분리하여 의미 스트림은 의도 이해와 고수준 추론에 집중하고, 공간 스트림은 기하학적 재구성과 밀집 예측에 집중하며, 마지막으로 계획 단계에서만 통제된 융합을 수행한다. 이러한 설계는 표현 붕괴를 완화할 뿐만 아니라 BEV 지도 재구성 및 에이전트 감지와 같은 보조 인식 작업이 암묵적 학습에 의존하지 않고 명시적 감독으로 공간 사전 지식을 주입할 수 있게 한다.

## 방법 분해

### 이중 스트림 아키텍처 개요
S²-VLA는 입력(내비게이션 명령 C_nav, 자차 운동 이력 T_hist, 전방 이미지 I)을 각각 의미 스트림과 공간 스트림에 전달하고, 최종적으로 이중 스트림 계획 어댑터를 통해 융합하여 궤적을 생성한다.

### 의미 스트림(Multi-Scale Semantic Stream)
- 백본: InternVL3-2B(InternViT 비전 인코더 + Qwen2.5 언어 모델).
- N_act=64개의 학습 가능한 행동 쿼리 Q_act를 주입하여 텍스트 및 비전 토큰과 공동 인코딩.
- 희소 다중 스케일 샘플링: 레이어 L={3,8,13,18,23,24}에서만 은닉 상태를 추출하여 다중 스케일 특징 집합 {(V_sem^(l), V_act^(l))}을 형성.
- 자차 이력은 MLP를 통해 E_ego∈ℝ^(1×d_vlm)로 인코딩되고, 각 레이어에서 행동 중심 특징과 연결되어 통합 상태 메모리 E_mem을 형성.

### 공간 스트림(Task-Driven Spatial Stream)
- 동적 해상도: 고해상도 이미지를 N_patch=9개의 패치(8개 로컬 + 1개 글로벌)로 분할하고, 각 패치에 N_vis=64개의 비전 쿼리를 도입.
- 인코딩된 비전 쿼리는 V_vis∈ℝ^(B×(N_patch×N_vis)×C)로 재구성되고, 타일 수준 위치 임베딩이 추가된 후 Transformer 인코더를 통과.
- **Map Head**: 1D 토큰 시퀀스를 2D 그리드 V_2D∈ℝ^(d×24×24)로 재구성하고, 업샘플링을 통해 BEV 의미 지도 M_hat_sem∈ℝ^(C×128×256)을 출력하며, X∈[0,32]m, Y∈[−32,32]m 범위를 커버하고 가중 교차 엔트로피 L_map으로 감독.
- **Agent Head**: DETR 패러다임, N_agent=30개 쿼리, 헝가리안 매칭, 손실은 L_agent=λ_reg·L_L1 + λ_cls·L_BCE.
- 중간 표현 V는 선형 투영을 통해 V_spatial을 형성하여 계획 어댑터의 공간 제약으로 사용.

### 이중 스트림 계획 어댑터
- M=8개의 계획 토큰 P^(0)∈ℝ^(M×d)을 초기화.
- 단계 1(의미 정렬): 계획 토큰은 다중 스케일 의미 특징 V_sem 및 상태 메모리 E_mem과 병렬 교차 주의를 수행하고, 게이트 파라미터 g∈ℝ^d가 융합을 변조: P_fuse=P^(l−1)+Linear([tanh(g)⊙P_raw; P_ego; P_sa]).
- 단계 2(공간 정제): V_spatial을 주입하고, P_vis=P_fuse+MHCA₃(P_fuse, V_spatial, V_spatial), 이후 FFN 통과.
- 궤적 디코딩: MLP가 Ŷ∈ℝ^(M×3)을 예측하고, 손실은 L_plan=L_L1 + λ_smooth·Σ SmoothL1(a, j).
- 총 손실: L_total=λ_plan·L_plan + λ_agent·L_agent + λ_map·L_map.

## 핵심 혁신

1. **명시적 이중 스트림 분리**: 기존 VLA의 단일 스트림 얽힘 설계와 달리, S²-VLA는 아키텍처 수준에서 의미와 공간 처리 경로를 강제로 분리한다. 이 설계는 공간 표현 붕괴 문제를 직접 겨냥하여 기하학적 사전 지식이 깊은 추상화에서 수동적으로 손실되지 않고 독립 스트림에서 명시적으로 감독되고 보존될 수 있게 한다.

2. **작업 주도 공간 스트림**: 공간 스트림은 비전 특징을 추출할 뿐만 아니라 Map Head와 Agent Head를 통해 구조화된 BEV 의미 지도와 에이전트 예측을 출력한다. 이러한 "작업을 감독으로 하는" 공간 특징 추출 방식은 계획기에 주입되는 V_spatial이 일반적인 비전 임베딩이 아닌 작업 검증된 기하학적 정보임을 보장한다.

3. **게이트 융합 메커니즘**: 계획 어댑터의 학습 가능한 게이트 파라미터 g는 모델이 의미와 공간 특징의 기여도를 적응적으로 균형 조정할 수 있게 한다. 이 메커니즘은 단순 연결로 인한 특징 중복을 피하고, 고수준 의도와 저수준 기하학이 계획 단계에서 정적으로 중첩되는 것이 아니라 동적으로 조정될 수 있게 한다.

## 실험 및 결과

실험은 NAVSIM 벤치마크에서 수행되었으며, PDMS 종합 지표(NC, DAC, TTC, Comf, EP 다섯 항목으로 계산)를 사용한다. 주요 결과는 다음과 같다:

| 방법 | NC | DAC | EP | TTC | Comf | PDMS |
|------|-----|-----|-----|-----|------|------|
| UniAD | 97.8 | 91.9 | 78.8 | 92.9 | 100 | 83.4 |
| PARA-Drive | 97.9 | 92.4 | 79.3 | 93.0 | 99.8 | 84.0 |
| DiffusionDrive | 98.2 | 96.2 | 82.2 | 94.7 | 100 | 88.1 |
| InternVL3-2B | 97.6 | 93.1 | 79.1 | 92.7 | 100 | 84.1 |
| ReCogDrive* | 98.1 | 94.7 | 80.9 | 94.2 | 100 | 86.5 |
| **S²-VLA** | **98.4** | **94.9** | **81.6** | **94.6** | **100** | **87.1** |

- S²-VLA는 단일 카메라만으로 LiDAR를 융합한 ARTEMIS(87.0) 및 DRAMA(86.9)를 능가한다.
- 동일 백본의 단순 VLM 기준(InternVL3-2B, PDMS 84.1)과 비교하여 S²-VLA는 3.0포인트 향상(표 내 수치 84.1→87.1로 계산).
- 절제 실험: 의미 특징 추가 시 PDMS +1.5(84.1→85.6), 공간 스트림 추가 시 +0.6(85.6→86.2), 보조 인식 작업 추가 시 최종 +0.9(86.2→87.1).
- DiffusionDrive의 PDMS 88.1은 약간 높으며, 주요 우위는 DAC(96.2 vs 94.9)에 있지만 반복적 확산 디코더와 명시적 LiDAR 포인트 클라우드에 의존한다.

## 경계 및 한계

저자는 공간 특징의 밀집 추출과 이중 스트림 융합이 사소하지 않은 계산 오버헤드를 초래하며, 향후 더 희소한 특징 표현 메커니즘을 개발해야 한다고 명시적으로 인정한다. 또한 이중 스트림 아키텍처는 훈련 패러다임과 직교하므로, 저자는 네트워크 설계의 공정한 비교를 위해 기준선의 폐루프 강화 학습 후훈련(예: GRPO)을 배제했지만, 이는 현재 결과가 후훈련으로 인한 이득을 반영하지 않음을 의미한다. 논문은 극한 기상, 센서 고장 또는 고동적 시나리오에서의 견고성 성능을 명시적으로 논의하지 않았으며, 추론 지연 시간의 구체적인 수치도 제공하지 않는다.

## 엔지니어링 시사점

재현 시 다음 핵심 구성을 우선적으로 확인해야 한다: 희소 샘플링 레이어 L={3,8,13,18,23,24}의 선택은 다중 스케일 의미 특징의 풍부함에 직접 영향을 미친다; N_patch=9의 동적 해상도 전략은 공간 스트림의 BEV 재구성 품질에 중요하다; 게이트 파라미터 g의 초기화와 훈련 안정성은 세심한 튜닝이 필요하다. 가장 함정에 빠지기 쉬운 부분은 3단계 훈련 프로세스이다 — 첫 번째 단계 SFT는 ReCogDrive VQA 데이터(3 epochs)를 사용하고, 두 번째와 세 번째 단계는 NAVSIM에서 각각 4 epochs를 수행하며, 단계 간에 해당 모듈을 올바르게 동결하지 않으면(예: 두 번째 단계에서 VLM 백본 동결 및 LoRA 적용, 세 번째 단계에서 인식 및 의도 구성 요소 동결) 특징 분포 이동이 발생한다. 손실 가중치 λ_plan=1.0, λ_agent=0.1, λ_map=0.5, λ_smooth=0.5는 엄격히 유지해야 하며, 특히 λ_smooth는 궤적 평활성에 큰 영향을 미치므로 너무 크면 계획이 지나치게 보수적으로 변한다. 하류 팀의 경우 실차 배포가 필요하다면 BEV 지도 출력(128×256)과 실제 세계 좌표 간의 정렬 정확도를 먼저 검증하는 것이 좋다. 이 모듈은 공간 스트림의 핵심 감독 신호이며, 그 오류는 계획 궤적으로 직접 전파되기 때문이다.
