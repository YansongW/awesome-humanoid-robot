---
$id: ent_paper_deva_decoupled_video_action_model_physic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeVA: Decoupled Video-Action Model with physical guidance for robot policy learning'
  zh: 'DeVA: Decoupled Video-Action Model with physical guidance for robot policy learning'
  ko: 'DeVA: Decoupled Video-Action Model with physical guidance for robot policy learning'
summary:
  en: Generalizable robot manipulation requires policies that can anticipate how visual scenes evolve while executing language
    instructions. While recent Vision-Language-Action models benefit from large-scale pretraining, their predominantly static
    pretraining objectives provide limited supervision for physical dynamics and temporal causality, leaving control-relevant
    knowledge to be learned from.
  zh: DeVA 提出一种解耦的视频-动作策略学习架构，将视觉动态建模与动作预测分配给独立专家，并通过多级特征交互与物理显著引导（affordance 与相对深度）提升机器人操作策略的样本效率与泛化能力。该方法在 RoboCasa、LIBERO、LIBERO-Plus
    及真实双臂平台上均显著超越现有 VLA/VAM 基线。
  ko: Generalizable robot manipulation requires policies that can anticipate how visual scenes evolve while executing language
    instructions. While recent Vision-Language-Action models benefit from large-scale pretraining, their predominantly static
    pretraining objectives provide limited supervision for physical dynamics and temporal causality, leaving control-relevant
    knowledge to be learned from.
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
- deva
- decoupled
- video
- action
- model
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
  title: 'arXiv:2607.24159 DeVA: Decoupled Video-Action Model with physical guidance for robot policy learn'
  url: https://arxiv.org/abs/2607.24159
  date: '2026-07-27'
  accessed_at: '2026-08-05'
---

## 概述

DeVA 提出一种解耦的视频-动作策略学习架构，将视觉动态建模与动作预测分配给独立专家，并通过多级特征交互与物理显著引导（affordance 与相对深度）提升机器人操作策略的样本效率与泛化能力。该方法在 RoboCasa、LIBERO、LIBERO-Plus 及真实双臂平台上均显著超越现有 VLA/VAM 基线。

## 它改变了什么

现有 VLA 模型依赖静态图文预训练，对物理动态与时间因果性监督不足，控制知识需从下游演示中重新学习，导致对任务特定数据量要求极高。而 VAM 虽引入视频预训练，但统一公式（shared backbone）迫使视觉生成与控制预测共享单一特征空间，限制了模态特定特征学习；早期或双 DiT 架构仅从选定骨干层与固定去噪阶段提取特征，未充分利用视频骨干中分布的各层互补抽象。DeVA 真正改变的是将“视频理解”与“动作生成”从架构层面解耦，并首次将场景几何（相对深度）与交互区域（affordance）作为显式物理引导注入动作预测，而非仅依赖隐式视频-动作目标。这使控制相关特征不再需要完全从下游演示中隐式涌现，而是通过预训练视频骨干的多级表示与物理先验直接引导，显著降低了对任务特定演示数量的依赖。

## 方法拆解

### 解耦双专家架构
- **视频专家**：初始化自 Cosmos-Predict2（潜在视频扩散 transformer，约 1.96B 参数），负责未来视觉动态建模，使用标准 EDM 去噪目标。
- **动作专家**：基于 GR00T-N1.5 动作头的 action-DiT 架构（约 564M 参数），以中间视频表示、T5 语言嵌入和物理引导为条件，无独立视觉编码器，使用 flow-matching 目标训练。

### 多级特征交互
- 从视频骨干早到晚阶段**均匀采样 8 层**，通过层间交叉注意力路由到动作专家对应层。
- 12 个可学习桥接 token（维度 1024）通过自注意力聚合视频上下文并引入动作流。

### 物理显著引导
- 两个轻量 DPT 风格解码器（affordance 与相对深度，共约 36.3M 参数，占训练参数 1.4%）附加到视频骨干，从不相交中间块（affordance 用块 {6,13,20,27}，深度用 {3,10,17,24}）采样特征。
- Affordance 定义为图像平面上末端执行器位置的条件概率，语言特征通过 FiLM 层融入；仿真中用高斯核（σ=1.0）从真实接触位置构造目标，真实数据用现成模型生成伪标签。
- 深度用离线视频深度预测模型（Video Depth Anything）估计，预测反转并归一化到 [0,1]。
- 从解码器最终时空块提取特征，投影到视频特征空间分辨率并展平，沿通道维度与多级视频表示拼接，作为额外键值提供给动作交叉注意力层。

### 两阶段训练
- **Stage 1**：预热视频专家和物理解码器 10K 步，联合学习未来视觉动态、affordance 和深度，损失 L_v = L_video + λ_aff L_aff + λ_depth L_depth（λ_aff=λ_depth=1.0）。
- **Stage 2**：引入动作专家并联合优化，物理解码器冻结但继续监督视频特征并提供引导，总损失 L = L_v + L_act。
- 优化：FusedAdamW，峰值学习率 1×10⁻⁴，warmup 1,000 步，线性衰减至 3×10⁻⁵（30k 步）后降至 6×10⁻⁶，梯度裁剪 1.0，批大小 8/GPU（全局 64），FSDP 全分片（8 GPU），bfloat16。

## 关键创新

1. **架构级解耦**：将视觉生成与动作预测分配给独立 transformer 专家，各自保留独立参数与 token 表示，避免共享单一特征空间导致的模态特定特征损失。这是对统一公式 VAM 的根本性修正。
2. **物理显著引导**：首次将 affordance（交互区域）与相对深度（场景几何）作为显式中间监督与推理时条件注入动作预测。这不仅提供稠密物理先验，还通过 FiLM 层与通道拼接实现任务条件化引导，使模型聚焦于视频中与动作最相关的信息。
3. **多级特征交互与去噪步条件化**：从视频骨干均匀采样 8 层中间表示进行交叉注意力，而非仅用最终层或固定去噪步；消融显示多步条件化（53.2%）显著优于最终步（49.6%），且冻结视频骨干导致性能骤降（22.4%），证明联合适应视频表示比简单特征提取更关键。

## 实验与结果

### 仿真基准
- **RoboCasa**（24 任务，每任务 50 演示，3,600 次 rollout）：DeVA 成功率 72.0%，同数据预算下提升最高 22.0 点（由表内 50.0→72.0 计算）。对比 UVA（50.0）、Cosmos-Policy（67.1）、GR00T-N1.5 + HAMLET（66.4）。
- **LIBERO**（4 套件 40 任务）：DeVA 平均 99.0%，超越 Cosmos-Policy（98.5）、DiT4DiT（98.6）、CogVLA（97.4）。
- **LIBERO-Plus**（10,030 变体）：DeVA 平均 80.8%，超过最强基线 OpenVLA-OFT（69.6）11.2 点（由表内 69.6→80.8 计算）；从标准 LIBERO 99.0% 下降 18.2 点（由表内 99.0→80.8 计算）。

### 真实世界（14-DoF 双臂平台，3 任务）
| 方法 | Handover Marker | Lift Pot | Pick Up Bottles | 平均 |
|------|-----------------|----------|-----------------|------|
| GR00T-N1.6 | 0.88 | 0.45 | 0.10 | 0.48 |
| π0.5 | 0.70 | 0.55 | 0.75 | 0.67 |
| Cosmos-Policy | 0.45 | 0.23 | 0.35 | 0.34 |
| **DeVA** | **0.90** | **0.68** | **0.65** | **0.74** |

### 消融（约 55K 步检查点）
| 变体 | 成功率 |
|------|--------|
| 仅动作模型 | 19.8% |
| 目标图像预测 | 25.8% |
| 未来视频预测 | 36.8% |
| 解耦架构 + 多级特征迁移 | 66.0% |
| + affordance + 相对深度 | **72.0%** |

特征交互机制消融：直接自注意力 66.79% > 直接交叉注意力 66.50% > 特定层交叉注意力 63.75% > 聚合注意力后交叉注意力 62.75%。去噪步条件化：多步 53.2% > 最终步 49.6% > 冻结骨干 22.4%。

## 边界与局限

论文未明确探索通过潜在空间预测与加速采样提升推理效率；未在真实世界使用额外合成轨迹；未报告 LIBERO-Plus 中七种扰动维度的逐维度分解结果（仅提及 "Robot Init" 与 "Camera View" 示例）。继承预训练视频骨干的计算成本使训练比仅动作策略学习更昂贵，联合去噪视频与动作流引入额外推理开销。额外变换层会降低性能，表明过度处理可能削弱预训练视频骨干已编码的信息。深度目标不需要度量精度或跨视图精确尺度一致性，对轻微跨视图不一致和时间漂移鲁棒；affordance 监督对伪标签中的中等噪声和定位误差容忍，但真实数据伪标签质量依赖现成模型。

## 工程启示

复现时先核对三处：**数据归一化**（真实 YAM 数据用 1st/99th 百分位，仿真用 min-max，动作掩码 (6,−1,6,−1) 表示 delta 与绝对维度混合）；**视频骨干初始化**（必须使用 Cosmos-Predict2 预训练 480p/16-fps 检查点，冻结骨干会导致性能从 49.6% 骤降至 22.4%）；**两阶段训练切换**（Stage 1 预热 10K 步后必须冻结物理解码器，但继续监督视频特征）。最容易踩坑的是多视角平铺布局：RoboCasa 三视图用 2×2 网格（第四 tile 留空），LIBERO 两视图水平平铺，真实数据三视图水平平铺，布局差异对性能影响可忽略但需保持一致。训练约 55K 步（仿真）或 40K 步（真实），8 GPU FSDP 下批大小 8/GPU，若显存不足优先降分辨率而非批大小。消融显示直接自注意力（66.79%）优于交叉注意力变体，若需简化可优先尝试直接自注意力方案。

## Overview
Generalizable robot manipulation requires policies that can anticipate how visual scenes evolve while executing language instructions. While recent Vision-Language-Action models benefit from large-scale pretraining, their predominantly static pretraining objectives provide limited supervision for physical dynamics and temporal causality, leaving control-relevant knowledge to be learned from downstream robot demonstrations. Video generative models offer a promising foundation by encoding rich spatiotemporal priors through future predictions. However, existing Video-Action Models either couple video and action prediction in a shared backbone, making policy adaptation harder to optimize, or under-utilize video information when guiding the action branch. In this work, we introduce DeVA, a Decoupled Video-Action model with specialized video and action experts, multi-level feature transfer, and physically salient guidance. DeVA transfers representations from multiple video layers to the action expert, enabling rich information exchange while making policy learning more tractable. It further supervises intermediate video features and the action stream with physically salient guidance (affordance/depth). Experiments on both simulation benchmarks and real-world deployment demonstrate strong performance with limited data, faster convergence than a unified architecture, and clear performance gains from physical guidance.

## 参考
- https://arxiv.org/abs/2607.24159

## 개요

DeVA는 비디오-액션 정책 학습을 위한 분리형 아키텍처를 제안하며, 시각적 동역학 모델링과 액션 예측을 독립적인 전문가(Expert)에게 할당하고, 다중 레벨 특징 상호작용과 물리적 현저성 가이드(affordance 및 상대 깊이)를 통해 로봇 조작 정책의 샘플 효율성과 일반화 능력을 향상시킵니다. 이 방법은 RoboCasa, LIBERO, LIBERO-Plus 및 실제 이중 팔 플랫폼에서 기존 VLA/VAM 기준선을 크게 능가합니다.

## 무엇을 바꾸었는가

기존 VLA 모델은 정적 이미지-텍스트 사전 학습에 의존하여 물리적 동역학과 시간적 인과성에 대한 감독이 부족하며, 제어 지식은 하위 작업 데모에서 다시 학습해야 하므로 작업별 데이터 요구량이 매우 높습니다. 반면 VAM은 비디오 사전 학습을 도입했지만, 통합 공식(shared backbone)은 시각적 생성과 제어 예측이 단일 특징 공간을 공유하도록 강제하여 모달리티별 특징 학습을 제한합니다. 초기 또는 이중 DiT 아키텍처는 선택된 백본 레이어와 고정된 디노이징 단계에서만 특징을 추출하여 비디오 백본에 분포된 다양한 레벨의 상호 보완적 추상화를 충분히 활용하지 못합니다. DeVA가 진정으로 바꾼 것은 "비디오 이해"와 "액션 생성"을 아키텍처 수준에서 분리하고, 처음으로 장면 기하학(상대 깊이)과 상호작용 영역(affordance)을 명시적 물리적 가이드로 액션 예측에 주입한다는 점입니다. 이는 암시적 비디오-액션 목표에만 의존하지 않습니다. 이를 통해 제어 관련 특징이 더 이상 하위 작업 데모에서 완전히 암시적으로 도출될 필요 없이, 사전 학습된 비디오 백본의 다중 레벨 표현과 물리적 사전 지식을 통해 직접 유도되어 작업별 데모 수에 대한 의존도를 크게 낮춥니다.

## 방법 분석

### 분리형 이중 전문가 아키텍처
- **비디오 전문가**: Cosmos-Predict2(잠재 비디오 확산 트랜스포머, 약 1.96B 파라미터)에서 초기화되며, 미래 시각적 동역학 모델링을 담당하고 표준 EDM 디노이징 목표를 사용합니다.
- **액션 전문가**: GR00T-N1.5 액션 헤드 기반의 action-DiT 아키텍처(약 564M 파라미터)로, 중간 비디오 표현, T5 언어 임베딩 및 물리적 가이드를 조건으로 사용하며, 독립적인 시각 인코더 없이 flow-matching 목표로 학습됩니다.

### 다중 레벨 특징 상호작용
- 비디오 백본의 초기부터 후기 단계까지 **균일하게 8개 레이어를 샘플링**하여 레이어 간 교차 어텐션을 통해 액션 전문가의 해당 레이어로 라우팅합니다.
- 12개의 학습 가능한 브리징 토큰(차원 1024)이 자기 어텐션을 통해 비디오 컨텍스트를 집계하고 액션 스트림에 도입합니다.

### 물리적 현저성 가이드
- 두 개의 경량 DPT 스타일 디코더(affordance 및 상대 깊이, 총 약 36.3M 파라미터, 학습 파라미터의 1.4%)가 비디오 백본에 부착되며, 서로 다른 중간 블록(affordance는 블록 {6,13,20,27}, 깊이는 {3,10,17,24})에서 특징을 샘플링합니다.
- Affordance는 이미지 평면에서 엔드 이펙터 위치의 조건부 확률로 정의되며, 언어 특징은 FiLM 레이어를 통해 통합됩니다. 시뮬레이션에서는 가우시안 커널(σ=1.0)을 사용하여 실제 접촉 위치에서 목표를 구성하고, 실제 데이터는 기성 모델로 의사 레이블을 생성합니다.
- 깊이는 오프라인 비디오 깊이 예측 모델(Video Depth Anything)로 추정되며, 예측값을 반전시켜 [0,1]로 정규화합니다.
- 디코더의 최종 시공간 블록에서 특징을 추출하여 비디오 특징 공간 해상도로 투영하고 평탄화한 후, 채널 차원을 따라 다중 레벨 비디오 표현과 연결하여 액션 교차 어텐션 레이어에 추가 키-값으로 제공합니다.

### 2단계 학습
- **Stage 1**: 비디오 전문가와 물리 디코더를 10K 스텝 동안 워밍업하며, 미래 시각적 동역학, affordance 및 깊이를 공동 학습합니다. 손실 L_v = L_video + λ_aff L_aff + λ_depth L_depth (λ_aff=λ_depth=1.0).
- **Stage 2**: 액션 전문가를 도입하고 공동 최적화하며, 물리 디코더는 동결되지만 비디오 특징을 계속 감독하고 가이드를 제공합니다. 총 손실 L = L_v + L_act.
- 최적화: FusedAdamW, 피크 학습률 1×10⁻⁴, 워밍업 1,000 스텝, 3×10⁻⁵(30k 스텝)까지 선형 감소 후 6×10⁻⁶으로 감소, 그래디언트 클리핑 1.0, 배치 크기 8/GPU(전역 64), FSDP 전체 샤딩(8 GPU), bfloat16.

## 핵심 혁신

1. **아키텍처 수준 분리**: 시각적 생성과 액션 예측을 독립적인 트랜스포머 전문가에게 할당하여 각각 독립적인 파라미터와 토큰 표현을 유지함으로써, 단일 특징 공간 공유로 인한 모달리티별 특징 손실을 방지합니다. 이는 통합 공식 VAM에 대한 근본적인 수정입니다.
2. **물리적 현저성 가이드**: 처음으로 affordance(상호작용 영역)와 상대 깊이(장면 기하학)를 명시적 중간 감독 및 추론 시 조건으로 액션 예측에 주입합니다. 이는 조밀한 물리적 사전 지식을 제공할 뿐만 아니라, FiLM 레이어와 채널 연결을 통해 작업 조건화 가이드를 구현하여 모델이 비디오에서 액션과 가장 관련된 정보에 집중하도록 합니다.
3. **다중 레벨 특징 상호작용 및 디노이징 스텝 조건화**: 비디오 백본에서 최종 레이어나 고정 디노이징 스텝 대신 8개 레이어의 중간 표현을 균일하게 샘플링하여 교차 어텐션을 수행합니다. 절제 실험은 다중 스텝 조건화(53.2%)가 최종 스텝(49.6%)보다 크게 우수하며, 비디오 백본 동결 시 성능이 급락(22.4%)하여 단순 특징 추출보다 비디오 표현의 공동 적응이 더 중요함을 입증합니다.

## 실험 및 결과

### 시뮬레이션 벤치마크
- **RoboCasa**(24개 작업, 작업당 50개 데모, 3,600회 롤아웃): DeVA 성공률 72.0%, 동일 데이터 예산에서 최대 22.0포인트 향상(표 내 50.0→72.0 계산). UVA(50.0), Cosmos-Policy(67.1), GR00T-N1.5 + HAMLET(66.4)와 비교.
- **LIBERO**(4개 스위트 40개 작업): DeVA 평균 99.0%, Cosmos-Policy(98.5), DiT4DiT(98.6), CogVLA(97.4) 능가.
- **LIBERO-Plus**(10,030개 변형): DeVA 평균 80.8%, 최강 기준선 OpenVLA-OFT(69.6)보다 11.2포인트 높음(표 내 69.6→80.8 계산); 표준 LIBERO 99.0%에서 18.2포인트 하락(표 내 99.0→80.8 계산).

### 실제 환경(14-DoF 이중 팔 플랫폼, 3개 작업)
| 방법 | Handover Marker | Lift Pot | Pick Up Bottles | 평균 |
|------|-----------------|----------|-----------------|------|
| GR00T-N1.6 | 0.88 | 0.45 | 0.10 | 0.48 |
| π0.5 | 0.70 | 0.55 | 0.75 | 0.67 |
| Cosmos-Policy | 0.45 | 0.23 | 0.35 | 0.34 |
| **DeVA** | **0.90** | **0.68** | **0.65** | **0.74** |

### 절제 실험(약 55K 스텝 체크포인트)
| 변형 | 성공률 |
|------|--------|
| 액션 모델만 | 19.8% |
| 목표 이미지 예측 | 25.8% |
| 미래 비디오 예측 | 36.8% |
| 분리 아키텍처 + 다중 레벨 특징 전이 | 66.0% |
| + affordance + 상대 깊이 | **72.0%** |

특징 상호작용 메커니즘 절제: 직접 자기 어텐션 66.79% > 직접 교차 어텐션 66.50% > 특정 레이어 교차 어텐션 63.75% > 집계 어텐션 후 교차 어텐션 62.75%. 디노이징 스텝 조건화: 다중 스텝 53.2% > 최종 스텝 49.6% > 백본 동결 22.4%.

## 경계 및 한계

논문은 잠재 공간 예측과 가속 샘플링을 통한 추론 효율성 향상을 명시적으로 탐구하지 않았습니다. 실제 환경에서 추가 합성 궤적을 사용하지 않았으며, LIBERO-Plus의 7가지 교란 차원에 대한 차원별 분해 결과를 보고하지 않았습니다("Robot Init" 및 "Camera View" 예시만 언급). 사전 학습된 비디오 백본의 계산 비용을 계승하여 학습이 액션 전용 정책 학습보다 더 비싸며, 비디오와 액션 스트림의 공동 디노이징은 추가 추론 오버헤드를 발생시킵니다. 추가 변환 레이어는 성능을 저하시킬 수 있으며, 이는 과도한 처리가 사전 학습된 비디오 백본에 이미 인코딩된 정보를 약화시킬 수 있음을 시사합니다. 깊이 목표는 측정 정밀도나 뷰 간 정확한 스케일 일관성을 요구하지 않으며, 약간의 뷰 간 불일치와 시간적 드리프트에 강건합니다. Affordance 감독은 의사 레이블의 중간 수준 노이즈와 위치 오류에 대해 관대하지만, 실제 데이터의 의사 레이블 품질은 기성 모델에 의존합니다.

## 엔지니어링 시사점

재현 시 세 가지를 먼저 확인하세요: **데이터 정규화**(실제 YAM 데이터는 1st/99th 백분위수, 시뮬레이션은 min-max, 액션 마스크 (6,−1,6,−1)는 델타와 절대 차원의 혼합을 나타냄); **비디오 백본 초기화**(반드시 Cosmos-Predict2 사전 학습 480p/16-fps 체크포인트를 사용해야 하며, 백본 동결 시 성능이 49.6%에서 22.4%로 급락); **2단계 학습 전환**(Stage 1 워밍업 10K 스텝 후 반드시 물리 디코더를 동결하되 비디오 특징을 계속 감독). 가장 쉽게 실수하는 부분은 다중 뷰 타일 레이아웃입니다: RoboCasa 3뷰는 2×2 그리드(네 번째 타일은 비움), LIBERO 2뷰는 수평 타일, 실제 데이터 3뷰는 수평 타일이며, 레이아웃 차이가 성능에 미치는 영향은 무시할 수 있지만 일관성을 유지해야 합니다. 학습은 약 55K 스텝(시뮬레이션) 또는 40K 스텝(실제)이며, 8 GPU FSDP에서 배치 크기 8/GPU, GPU 메모리가 부족하면 배치 크기보다 해상도를 먼저 낮추세요. 절제 실험은 직접 자기 어텐션(66.79%)이 교차 어텐션 변형보다 우수함을 보여주며, 단순화가 필요하면 직접 자기 어텐션 방식을 우선 시도할 수 있습니다.
