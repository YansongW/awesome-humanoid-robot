---
$id: ent_paper_comprehensive_survey_world_models_embodi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Comprehensive Survey on World Models for Embodied AI
  zh: A Comprehensive Survey on World Models for Embodied AI
  ko: A Comprehensive Survey on World Models for Embodied AI
summary:
  en: Embodied AI requires agents that perceive, act, and anticipate how actions reshape future world states. World models
    serve as internal simulators that capture environment dynamics, enabling forward and counterfactual rollouts to support
    perception, prediction, and decision making. This survey presents a unified framework for world models in embodied AI.
    Specifically, we formalize the problem.
  zh: 这篇综述为具身智能中的世界模型提出了一套统一分类框架，围绕功能耦合度、时间建模方式和空间表示形式三个核心轴组织文献。作者系统梳理了从模型架构、训练范式到数据资源与评估指标的完整技术栈，并给出了跨操作、导航、自动驾驶等任务的定量性能对比。
  ko: Embodied AI requires agents that perceive, act, and anticipate how actions reshape future world states. World models
    serve as internal simulators that capture environment dynamics, enabling forward and counterfactual rollouts to support
    perception, prediction, and decision making. This survey presents a unified framework for world models in embodied AI.
    Specifically, we formalize the problem.
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
- comprehensive
- survey
- world
- models
- embodi
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P072. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: arXiv:2510.16732 A Comprehensive Survey on World Models for Embodied AI
  url: https://arxiv.org/abs/2510.16732
  date: '2025-10-19'
  accessed_at: '2026-08-05'
---

## 概述

这篇综述为具身智能中的世界模型提出了一套统一分类框架，围绕功能耦合度、时间建模方式和空间表示形式三个核心轴组织文献。作者系统梳理了从模型架构、训练范式到数据资源与评估指标的完整技术栈，并给出了跨操作、导航、自动驾驶等任务的定量性能对比。

## 它改变了什么

世界模型领域此前最大的问题不是方法不够多，而是缺乏一个能让不同子社区（强化学习、自动驾驶、视频预测）对话的共同语言。功能导向的分类法（如按理解与预测划分）和应用驱动的分类法（如聚焦自动驾驶）各自为政，导致同一类技术在不同论文里被冠以不同名称，术语混乱直接阻碍了方法迁移和基准对比。

这篇综述真正改变的是把“世界模型”从一种具体技术（如Dreamer系列）提升为一个可分析的研究范式。通过引入决策耦合vs通用目的、顺序模拟vs全局差异预测、以及四种空间表示（全局潜向量、Token序列、空间潜网格、分解渲染）这三个正交轴，它让研究者能清晰定位任意方法的design space位置，并理解不同选择背后的权衡——比如自回归设计紧凑但误差累积，全局预测一致性更好但计算重且闭环交互弱。

## 方法拆解

### 统一数学框架
作者将环境交互建模为POMDP，定义潜状态z_t的学习目标：
- 动态先验：p_θ(z_t | z_{t-1}, a_{t-1})
- 滤波后验：q_ϕ(z_t | z_{t-1}, a_{t-1}, o_t)
- 重建：p_θ(o_t | z_t)

优化目标为ELBO，分解为重建项与KL正则项：
L(θ, ϕ) = Σ_t E_{q_ϕ(z_t)}[log p_θ(o_t | z_t)] - D_KL(q_ϕ ∥ p_θ)

### 三种时间建模策略
- **顺序模拟与推理**：逐帧滚动预测，代表为RSSM、Dreamer系列、TransDreamer（用TSSM替代循环核心）、Mamba类SSM（GLAM）
- **全局差异预测**：并行预测未来序列或BEV/体素图，减少误差累积，如JEPA类方法（V-JEPA 2）
- **混合设计**：如Epona用Transformer建模时空、DiT生成轨迹与视觉；NWM用条件DiT实现零样本规划

### 四种空间表示
- **全局潜向量**：紧凑、计算高效，但丢弃细粒度时空细节
- **Token特征序列**：支持因果推理与LLM复用，如MWM用掩码自编码器解耦视觉token与RSSM
- **空间潜网格**：BEV或体素网格引入几何先验，保留局部性，支持流式展开
- **分解渲染表示**：NeRF/3DGS基元+可微渲染，视角一致且支持对象级组合，但动态场景扩展性差

### 关键架构决策
- 逆动力学建模（IDM）将世界模型分解为可控/不可控组件（Iso-Dream）
- 显式推理注入：NavCoT分解导航为想象-过滤-预测，ECoT用基础模型生成推理标签训练VLA

## 关键创新

1. **三维分类轴取代二维谱系**：此前综述多按“功能”或“应用”单轴划分，本文引入时间建模与空间表示两个正交维度，使方法定位更精确。例如，同样是占用预测，OccWorld（顺序模拟+空间网格）与COME（全局差异+空间网格）在误差累积特性上有本质差异，单看功能无法区分。

2. **将评估指标分层为像素级/状态级/任务级**：明确指出现有FID、FVD等像素指标无法反映物理一致性，并系统整理了mIoU、ADE/FDE、成功率、碰撞率等状态与任务级指标。这为后续研究提供了选择评估协议的决策树，而非简单罗列。

3. **跨任务定量对比表**：首次在同一张表中对比DMC（连续控制）、RLBench（操作）、nuScenes（规划）、Occ3D（占用预测）四个基准上的代表性方法，揭示了不同任务对世界模型架构偏好的差异——例如IDM在RLBench上表现突出，而占用输入在4D预测中显著优于纯相机。

## 实验与结果

综述汇总了四个基准的定量结果（论文未提供实验设置细节，以下为表格数据）：

**nuScenes视频生成（FID↓/FVD↓）**：

| 方法 | FID | FVD |
|------|-----|-----|
| DrivePhysica | 4.0 | 38.1 |
| MiLA | 4.1 | 14.9 |
| Vista | 6.9 | 89.4 |
| DriveDreamer | 52.6 | 452.0 |

DrivePhysica在视觉保真度最优，MiLA时间一致性最强，两者均采用显式物理或分解渲染。

**Occ3D 4D占用预测（mIoU%，Avg）**：

| 方法 | 输入 | Avg mIoU |
|------|------|----------|
| DTT-O | 真值占用 | 30.85 |
| COME-O | 真值占用+GT ego | 34.23 |
| COME-S | 相机（自监督） | 19.11 |
| OccWorld-S | 相机（自监督） | 0.26 |

占用输入显著优于纯相机；GT ego轨迹提供额外增益。

**DMC（Episode Return↑）**：

| 方法 | 步数 | Cheetah Run | Walker Walk |
|------|------|-------------|-------------|
| PlaNet | 5M | 496 | 945 |
| Dreamer | 5M | 895 | 962 |
| HRSSM | 500k | - | - |

近期模型在更少步数达到更高回报，但任务子集不一致妨碍公平对比。

**RLBench（成功率%）**：

| 方法 | 平均成功率 |
|------|-----------|
| VidMan | 67 |
| TesserAct | 63 |
| ManiGaussian | 45 |

VidMan（IDM）在广任务集上最优，揭示逆动力学建模为有前景方向。

**nuScenes规划（L2↓/碰撞率↓）**：

| 方法 | Avg L2 | Avg碰撞率 |
|------|--------|-----------|
| UniAD+DriveWorld | 0.69 | 0.19 |
| SSR | 0.75 | 0.15 |
| OccWorld-S | 1.83 | 2.02 |

SSR在无额外监督下实现最佳碰撞率；基于相机的方法已超越使用特权占用的模型。

## 边界与局限

论文未设专门局限章节，但引言明确列出开放挑战：统一数据集稀缺（现有基准如DMC、RLBench、nuScenes各自为政，跨域迁移困难）；评估指标偏像素保真度而忽略物理一致性；模型性能与实时控制所需计算效率的权衡未解决；长时程时间一致性受误差累积制约。

具体到表格数据，DMC对比中任务子集不一致（如TransDreamer仅报告4个任务），RLBench各方法片段预算从25到250不等、分辨率从128到512，这些实现差异使同类比较复杂化。分解渲染方法（NeRF/3DGS）在动态场景中的扩展性未得到充分验证，论文仅指出该方向“扩展性差”但未给出量化分析。

## 工程启示

复现或选型时，先核对三件事：**输入模态**（真值占用vs相机预测对结果影响巨大，如Occ3D上COME-S与COME-O的Avg mIoU差距达15个百分点）、**评估协议**（DMC的Episode Return定义、nuScenes的UniAD协议、RLBench的成功率判定标准各不相同）、**计算预算**（VidMan用125个片段达到67%成功率，而DreMa用250个片段仅25%，但前者分辨率224、后者128，直接对比需谨慎）。

最容易踩坑的是**跨表对比**：不同论文的“平均分”因任务难度差异不可直接比较（如RLBench的Close Jar成功率88%与Stack Blocks 48%差距悬殊），综述中已标注“仅为粗略指标”。工程上建议优先复现IDM类方法（VidMan、Iso-Dream），因其在操作任务上表现稳定且架构简单；若做自动驾驶规划，SSR这类无额外监督的方法性价比最高，而占用预测任务中DTT的分解token设计值得借鉴。

## Overview
Embodied AI requires agents that perceive, act, and anticipate how actions reshape future world states. World models serve as internal simulators that capture environment dynamics, enabling forward and counterfactual rollouts to support perception, prediction, and decision making. This survey presents a unified framework for world models in embodied AI. Specifically, we formalize the problem setting and learning objectives, and propose a three-axis taxonomy encompassing: (1) Functionality, Decision-Coupled vs. General-Purpose; (2) Temporal Modeling, Sequential Simulation and Inference vs. Global Difference Prediction; (3) Spatial Representation, Global Latent Vector, Token Feature Sequence, Spatial Latent Grid, and Decomposed Rendering Representation. We systematize data resources and metrics across robotics, autonomous driving, and general video settings, covering pixel prediction quality, state-level understanding, and task performance. Furthermore, we offer a quantitative comparison of state-of-the-art models and distill key open challenges, including the scarcity of unified datasets and the need for evaluation metrics that assess physical consistency over pixel fidelity, the trade-off between model performance and the computational efficiency required for real-time control, and the core modeling difficulty of achieving long-horizon temporal consistency while mitigating error accumulation. Finally, we maintain a curated bibliography at https://github.com/Li-Zn-H/AwesomeWorldModels.

## 参考
- https://arxiv.org/abs/2510.16732

## 개요

이 리뷰 논문은 구현 지능(Embodied AI) 분야의 세계 모델(World Model)에 대한 통합 분류 프레임워크를 제안하며, 기능 결합도, 시간 모델링 방식, 공간 표현 형식이라는 세 가지 핵심 축을 중심으로 문헌을 체계화합니다. 저자들은 모델 아키텍처, 훈련 패러다임부터 데이터 자원과 평가 지표에 이르는 전체 기술 스택을 체계적으로 정리하고, 조작, 내비게이션, 자율주행 등 다양한 태스크에 걸친 정량적 성능 비교를 제시합니다.

## 무엇을 바꾸었는가

세계 모델 분야의 가장 큰 문제는 방법이 부족하다기보다, 서로 다른 하위 커뮤니티(강화학습, 자율주행, 비디오 예측)가 공유할 공통 언어가 부재하다는 점이었습니다. 기능 중심 분류법(예: 이해와 예측으로 구분)과 애플리케이션 중심 분류법(예: 자율주행에 초점)이 각자 제각각 운영되면서, 동일한 유형의 기술이 논문마다 다른 이름으로 불리게 되었고, 이러한 용어 혼란은 방법 전이와 벤치마크 비교를 직접적으로 방해했습니다.

이 리뷰가 실제로 바꾼 것은 '세계 모델'을 특정 기술(예: Dreamer 시리즈)에서 분석 가능한 연구 패러다임으로 승격시킨 점입니다. 의사결정 결합 vs 범용 목적, 순차 시뮬레이션 vs 전역 차이 예측, 그리고 네 가지 공간 표현(전역 잠재 벡터, 토큰 시퀀스, 공간 잠재 그리드, 분해 렌더링)이라는 세 가지 직교 축을 도입함으로써, 연구자들이 임의의 방법이 설계 공간에서 차지하는 위치를 명확히 파악하고 각 선택 뒤에 숨은 트레이드오프를 이해할 수 있게 했습니다. 예를 들어 자기회귀 설계는 컴팩트하지만 오류가 누적되고, 전역 예측은 일관성이 더 좋지만 계산량이 많고 폐쇄 루프 상호작용이 약합니다.

## 방법 분해

### 통합 수학 프레임워크
저자들은 환경 상호작용을 POMDP로 모델링하고, 잠재 상태 z_t의 학습 목표를 다음과 같이 정의합니다:
- 동적 사전 분포: p_θ(z_t | z_{t-1}, a_{t-1})
- 필터링 사후 분포: q_ϕ(z_t | z_{t-1}, a_{t-1}, o_t)
- 재구성: p_θ(o_t | z_t)

최적화 목표는 ELBO이며, 재구성 항과 KL 정규화 항으로 분해됩니다:
L(θ, ϕ) = Σ_t E_{q_ϕ(z_t)}[log p_θ(o_t | z_t)] - D_KL(q_ϕ ∥ p_θ)

### 세 가지 시간 모델링 전략
- **순차 시뮬레이션 및 추론**: 프레임 단위 롤링 예측. 대표적으로 RSSM, Dreamer 시리즈, TransDreamer(순환 코어를 TSSM으로 대체), Mamba 계열 SSM(GLAM) 등이 있습니다.
- **전역 차이 예측**: 미래 시퀀스 또는 BEV/복셀 맵을 병렬 예측하여 오류 누적을 줄입니다. 예: JEPA 계열 방법(V-JEPA 2).
- **혼합 설계**: Epona는 Transformer로 시공간을 모델링하고 DiT로 궤적과 비주얼을 생성합니다. NWM은 조건부 DiT로 제로샷 플래닝을 구현합니다.

### 네 가지 공간 표현
- **전역 잠재 벡터**: 컴팩트하고 계산 효율적이지만, 세밀한 시공간 디테일을 버립니다.
- **토큰 특징 시퀀스**: 인과 추론과 LLM 재사용을 지원합니다. 예: MWM은 마스크 오토인코더로 비주얼 토큰과 RSSM을 분리합니다.
- **공간 잠재 그리드**: BEV 또는 복셀 그리드가 기하학적 사전 정보를 도입하고, 지역성을 유지하며 스트리밍 전개를 지원합니다.
- **분해 렌더링 표현**: NeRF/3DGS 프리미티브 + 미분 가능 렌더링. 시점 일관성을 제공하고 객체 수준 구성을 지원하지만, 동적 장면 확장성은 떨어집니다.

### 핵심 아키텍처 결정
- 역동역학 모델링(IDM)은 세계 모델을 제어 가능/불가능 구성 요소로 분해합니다(Iso-Dream).
- 명시적 추론 주입: NavCoT는 내비게이션을 상상-필터링-예측으로 분해하고, ECoT는 기초 모델로 추론 라벨을 생성하여 VLA를 훈련합니다.

## 핵심 혁신

1. **2차원 계보를 3차원 분류 축으로 대체**: 기존 리뷰는 대부분 '기능' 또는 '애플리케이션' 단일 축으로 나누었지만, 본 논문은 시간 모델링과 공간 표현이라는 두 개의 직교 차원을 도입하여 방법 위치 파악을 더 정밀하게 만듭니다. 예를 들어 동일한 점유 예측이라도 OccWorld(순차 시뮬레이션 + 공간 그리드)와 COME(전역 차이 + 공간 그리드)은 오류 누적 특성에서 본질적 차이가 있으며, 기능만으로는 구분할 수 없습니다.

2. **평가 지표를 픽셀 수준/상태 수준/태스크 수준으로 계층화**: 기존 FID, FVD 같은 픽셀 지표가 물리적 일관성을 반영하지 못한다는 점을 명확히 지적하고, mIoU, ADE/FDE, 성공률, 충돌률 등 상태 및 태스크 수준 지표를 체계적으로 정리했습니다. 이는 단순 나열이 아닌, 후속 연구를 위한 평가 프로토콜 선택 의사결정 트리를 제공합니다.

3. **태스크 간 정량 비교 테이블**: DMC(연속 제어), RLBench(조작), nuScenes(플래닝), Occ3D(점유 예측) 네 가지 벤치마크의 대표 방법을 최초로 단일 테이블에서 비교하여, 태스크별 세계 모델 아키텍처 선호도 차이를 밝혔습니다. 예를 들어 IDM은 RLBench에서 두드러지고, 점유 입력은 4D 예측에서 순수 카메라보다 크게 우수합니다.

## 실험 및 결과

리뷰는 네 가지 벤치마크의 정량 결과를 종합했습니다(논문은 실험 설정 세부사항을 제공하지 않으며, 아래는 테이블 데이터입니다):

**nuScenes 비디오 생성(FID↓/FVD↓)**:

| 방법 | FID | FVD |
|------|-----|-----|
| DrivePhysica | 4.0 | 38.1 |
| MiLA | 4.1 | 14.9 |
| Vista | 6.9 | 89.4 |
| DriveDreamer | 52.6 | 452.0 |

DrivePhysica는 시각적 충실도가 가장 우수하고, MiLA는 시간적 일관성이 가장 강합니다. 둘 다 명시적 물리 또는 분해 렌더링을 사용합니다.

**Occ3D 4D 점유 예측(mIoU%, Avg)**:

| 방법 | 입력 | Avg mIoU |
|------|------|----------|
| DTT-O | GT 점유 | 30.85 |
| COME-O | GT 점유+GT ego | 34.23 |
| COME-S | 카메라(자기지도) | 19.11 |
| OccWorld-S | 카메라(자기지도) | 0.26 |

점유 입력은 순수 카메라보다 크게 우수하며, GT ego 궤적은 추가 이득을 제공합니다.

**DMC(Episode Return↑)**:

| 방법 | 스텝 수 | Cheetah Run | Walker Walk |
|------|------|-------------|-------------|
| PlaNet | 5M | 496 | 945 |
| Dreamer | 5M | 895 | 962 |
| HRSSM | 500k | - | - |

최신 모델은 더 적은 스텝으로 더 높은 리턴을 달성하지만, 태스크 하위 집합이 일관되지 않아 공정한 비교가 어렵습니다.

**RLBench(성공률%)**:

| 방법 | 평균 성공률 |
|------|-----------|
| VidMan | 67 |
| TesserAct | 63 |
| ManiGaussian | 45 |

VidMan(IDM)이 광범위한 태스크 집합에서 최고 성능을 보이며, 역동역학 모델링이 유망한 방향임을 시사합니다.

**nuScenes 플래닝(L2↓/충돌률↓)**:

| 방법 | Avg L2 | Avg 충돌률 |
|------|--------|-----------|
| UniAD+DriveWorld | 0.69 | 0.19 |
| SSR | 0.75 | 0.15 |
| OccWorld-S | 1.83 | 2.02 |

SSR은 추가 감독 없이 최고 충돌률을 달성하며, 카메라 기반 방법은 특권 점유를 사용하는 모델을 이미 능가했습니다.

## 경계와 한계

논문은 별도의 한계 섹션을 두지 않았지만, 서론에서 공개된 도전 과제를 명확히 제시합니다: 통합 데이터셋 부족(기존 DMC, RLBench, nuScenes 등 벤치마크가 각자 운영되어 교차 도메인 전이가 어려움), 픽셀 충실도에 치우친 평가 지표로 물리적 일관성 무시, 모델 성능과 실시간 제어에 필요한 계산 효율성 간 트레이드오프 미해결, 장기 시간 일관성이 오류 누적에 의해 제약됨.

구체적으로 테이블 데이터에서 DMC 비교는 태스크 하위 집합이 일관되지 않고(예: TransDreamer는 4개 태스크만 보고), RLBench 각 방법의 에피소드 예산은 25~250, 해상도는 128~512로 다양하여 구현 차이가 동일 유형 비교를 복잡하게 만듭니다. 분해 렌더링 방법(NeRF/3DGS)의 동적 장면 확장성은 충분히 검증되지 않았으며, 논문은 해당 방향이 '확장성이 낮다'고만 지적하고 정량적 분석은 제공하지 않습니다.

## 엔지니어링 시사점

재현 또는 방법 선택 시 세 가지를 먼저 확인해야 합니다: **입력 모달리티**(GT 점유 vs 카메라 예측은 결과에 큰 영향을 미칩니다. Occ3D에서 COME-S와 COME-O의 Avg mIoU 차이는 15% 포인트에 달합니다), **평가 프로토콜**(DMC의 Episode Return 정의, nuScenes의 UniAD 프로토콜, RLBench의 성공률 판정 기준이 각각 다릅니다), **계산 예산**(VidMan은 125개 에피소드로 67% 성공률을 달성하는 반면, DreMa는 250개 에피소드로 25%에 불과하지만 전자는 해상도 224, 후자는 128이므로 직접 비교에 주의가 필요합니다).

가장 함정에 빠지기 쉬운 것은 **테이블 간 비교**입니다: 서로 다른 논문의 '평균 점수'는 태스크 난이도 차이로 직접 비교할 수 없습니다(예: RLBench의 Close Jar 성공률 88%와 Stack Blocks 48%는 큰 차이). 리뷰에서도 '대략적인 지표일 뿐'이라고 명시했습니다. 엔지니어링 관점에서는 IDM 계열 방법(VidMan, Iso-Dream)을 우선 재현하는 것이 좋습니다. 조작 태스크에서 성능이 안정적이고 아키텍처가 단순하기 때문입니다. 자율주행 플래닝을 한다면 SSR처럼 추가 감독이 없는 방법이 가장 비용 효율적이며, 점유 예측 태스크에서는 DTT의 분해 토큰 설계가 참고할 만합니다.
