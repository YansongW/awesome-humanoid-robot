---
$id: ent_paper_gigaworld_0_world_models_data_engine_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GigaWorld-0: World Models as Data Engine to Empower Embodied AI'
  zh: 'GigaWorld-0: World Models as Data Engine to Empower Embodied AI'
  ko: 'GigaWorld-0: World Models as Data Engine to Empower Embodied AI'
summary:
  en: 'World models are emerging as a foundational paradigm for scalable, data-efficient embodied AI. In this work, we present
    GigaWorld-0, a unified world model framework designed explicitly as a data engine for Vision-Language-Action (VLA) learning.
    GigaWorld-0 integrates two synergistic components: GigaWorld-0-Video, which leverages large-scale video generation to
    produce diverse, texture-rich, and.'
  zh: GigaWorld-0 是一个面向具身智能的统一世界模型框架，由视频生成（GigaWorld-0-Video）与 3D 资产生成（GigaWorld-0-3D）两大组件构成，旨在作为 VLA 模型的数据引擎，以合成数据替代昂贵且受限的真实世界采集。其核心贡献在于将可控视频生成、物理可微系统辨识与可执行运动规划整合为一条可扩展的数据生产管线，并配套了质量评估与加速推理机制。
  ko: 'World models are emerging as a foundational paradigm for scalable, data-efficient embodied AI. In this work, we present
    GigaWorld-0, a unified world model framework designed explicitly as a data engine for Vision-Language-Action (VLA) learning.
    GigaWorld-0 integrates two synergistic components: GigaWorld-0-Video, which leverages large-scale video generation to
    produce diverse, texture-rich, and.'
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
- gigaworld
- '0'
- world
- models
- data
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P115. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2511.19861 GigaWorld-0: World Models as Data Engine to Empower Embodied AI'
  url: https://arxiv.org/abs/2511.19861
  date: '2025-11-25'
  accessed_at: '2026-08-05'
---

## 概述

GigaWorld-0 是一个面向具身智能的统一世界模型框架，由视频生成（GigaWorld-0-Video）与 3D 资产生成（GigaWorld-0-3D）两大组件构成，旨在作为 VLA 模型的数据引擎，以合成数据替代昂贵且受限的真实世界采集。其核心贡献在于将可控视频生成、物理可微系统辨识与可执行运动规划整合为一条可扩展的数据生产管线，并配套了质量评估与加速推理机制。

## 它改变了什么

它改变了什么：问题与动机。传统具身数据获取的瓶颈并非单纯的成本问题，而是真实世界数据在视点、纹理、光照和物理交互上的多样性天花板——这直接限制了 VLA 模型从“看见”到“行动”的泛化能力。GigaWorld-0 的实质改变在于，它不再把世界模型当作一个被动的预测器，而是将其重构为一个主动的、可编程的数据生产工具，使得“生成数据”这一行为本身具备了与真实采集同等的训练价值。它试图回答一个更根本的问题：当数据可以按需合成时，具身智能的训练范式是否可以从“收集”转向“设计”。

这一转变的深层动机在于，现有视频生成模型（如 Cosmos、Wan）虽然能产出高保真画面，但在物理合理性、多视点一致性和动作语义可控性上存在系统性缺陷，导致其生成内容无法直接用于策略学习。GigaWorld-0 通过引入 3D 物理模拟与可微系统辨识，将生成过程从“像素层面的逼真”推进到“物理层面的可信”，这是对现有数据引擎范式的关键修正。

## 方法拆解

方法拆解：怎么做的。

### 视频生成分支（GigaWorld-0-Video）
- **基础模型（Dreamer）**：采用 flow-matching 公式 `dz_t/dt = v_θ(z_t, t, c)`，使用 3D-VAE 压缩原始视频，时空压缩比为 4,8,8（时间、高度、宽度），产生 16 通道潜变量。随后应用 1×2×2 patchification 进一步压缩，并用 3D-RoPE 编码位置信息。
- **MoE 架构**：在 FFN 块中集成 4 个路由专家（N_r=4），每 token 激活 2 个专家（K_r=2），采用 DeepSeek-V3 的互补平衡损失，平衡因子 α=0.01。与 DeepSeek-V2 不同，不包含共享专家。
- **可控生成**：通过三个后训练适配模块实现细粒度控制——AppearanceTransfer（外观编辑）、ViewTransfer（视点迁移）、MimicTransfer（人-机动作迁移）。其中 ViewTransfer 采用双重重投影策略，利用 MoGe 估计深度，将视点 A 的图像扭曲到视点 B，并用 SAM2 掩码机械臂以保证背景一致性；MimicTransfer 则通过 IK 将人手末端位姿映射到机械臂关节角，在 SAPIEN 模拟器中渲染条件视频。

### 3D 资产生成分支（GigaWorld-0-3D）
- **前景生成（FG）**：基于 Trellis 进行图像到 3D 转换，支持网格与 3DGS 双表示。预处理阶段使用 Aesthetic-Checker 和 GPT-4o 驱动的 ImageSegChecker 评估分割可靠性，后处理阶段通过 MeshGeoChecker 从四个正交视点验证几何完整性。
- **背景重建（BG）**：采用 3DGRUT（每个高斯关联 7 个代表点）支持非针孔相机，通过稀疏视点输入→初始重建→视点细化→密集重建→泊松表面重建的流程生成水密网格。
- **物理属性建模（Phys）**：机械臂采用基于 PINN 的可微物理框架，三阶段流程：随机采样物理参数生成模拟 rollouts → 训练代理模型最小化预测与模拟的 MSE → 梯度下降优化物理参数。操作对象则基于 Qwen3-VL 多模态专家推断质量、摩擦系数等属性。
- **动作生成（Act）**：两层级管线，使用 MimicGen 框架将种子轨迹扩展到新物体姿态和场景布局，复杂场景则用遥操作演示作为强化学习冷启动数据。

### 训练与推理优化
- 训练框架 GigaTrain 支持 DeepSpeed ZeRO（Stages 0–3）与 FSDP2，训练分辨率 480×768，序列长度 61 帧，使用 NATTEN 稀疏注意力算子与 FP8 精度。
- 推理加速：采用 DMD2 去噪步蒸馏将采样从数十步降至单步，结合 FP8 精度实现超过 50× 加速。

## 关键创新

关键创新：

1. **物理感知的视频生成控制**：不同于现有视频模型仅控制外观或相机轨迹，GigaWorld-0 通过 ViewTransfer 和 MimicTransfer 将机械臂的运动学约束（关节角、末端位姿）直接注入生成过程，使得生成视频中的动作序列在物理上可执行。这是从“看起来像操作”到“实际上能操作”的关键跨越。

2. **可微系统辨识与 3D 生成的闭环**：将 PINN 驱动的物理参数辨识与 3DGS 重建结合，使得生成的 3D 资产不仅外观逼真，还具备正确的质量、摩擦和弹性属性，可直接用于物理模拟器。这解决了 Trellis 等 3D 生成模型缺乏物理合理性的根本缺陷。

3. **轻量级控制分支设计**：在 MoE 架构下放弃 ControlNet（因其复制 MoE 层会显著增加参数），改用通道拼接+MLP 压缩的方式注入多模态条件，在保持模型规模的同时实现细粒度控制。这一设计决策对大规模视频生成模型的可控适配具有直接参考价值。

## 实验与结果

实验与结果：对照设置、关键数字、结果的含义。

### PBench Robot Set 评估
| 模型 | 参数 | 质量分数 | 领域分数 | 总体分数 |
|---|---|---|---|---|
| Cosmos-Predict2 | 14B | 97.4 | 84.0 | 79.88 |
| Wan2.2 | 14B | 95.9 | 83.2 | 78.85 |
| Wan2.2 | 5B | 95.4 | 80.1 | 77.15 |
| Cosmos-Predict2.5 | 2B | 93.8 | 84.7 | 79.95 |
| GigaWorld-0-Video-Dreamer | 2B(Act.) | 97.6 | 88.2 | 82.07 |

GigaWorld-0 以 2B 激活参数超越 14B 模型，总体分数 82.07 领先第二名约 2.1 分（由表内数值 82.07−79.95 计算），尤其在领域分数（88.2）上优势明显，表明其生成内容更贴合具身操作任务需求。

### DreamGen Bench 评估（GR1-Env 子集）
| 方法 | 参数 | Qwen-IF | GPT-IF | PA |
|---|---|---|---|---|
| Cosmos-Predict2 | 14B | 0.966 | 0.552 | 0.586 |
| Wan2.2 | 14B | 0.900 | 0.760 | 0.549 |
| Wan2.2 | 5B | 0.790 | 0.340 | 0.531 |
| Cosmos-Predict2.5 | 2B | 0.930 | 0.480 | 0.534 |
| GigaWorld-0-Video-Dreamer | 2B(Act.) | 0.966 | 0.586 | 0.529 |

在 GR1-Env 上，GigaWorld-0 的 Qwen-IF 分数与 Cosmos-Predict2 并列最高（0.966），GPT-IF 分数（0.586）优于 Cosmos-Predict2（0.552），但 PA 分数（0.529）略低于 Cosmos-Predict2（0.586）。这表明其在指令跟随上表现优异，但在物理合理性上仍有提升空间。

### 训练效率（8×H20 GPUs，batch size 32）
| 配置 | 时间 (s/step) | 内存 (MB) |
|---|---|---|
| DeepSpeed-Zero2 + FP8 + 稀疏注意力 | 25.44 | 76937 |
| FSDP-2 + FP8 + 稀疏注意力 | 25.38 | 73131 |
| DeepSpeed-Zero2 + 激活检查点 + FP8 + 稀疏注意力 + MoE | 33.27 | 84699 |
| FSDP-2 + 激活检查点 + FP8 + 稀疏注意力 + MoE | 33.38 | 73997 |

FP8 与稀疏注意力组合将训练速度从 32.84 s/step 提升至 25.38 s/step（由表内数值 32.84→25.38 计算），但引入 MoE 后需激活检查点，速度回落至 33.38 s/step，内存控制在 73997 MB。

## 边界与局限

边界与局限：作者未在本文中提供下游任务（如衣物折叠、餐桌清理）的定量成功率，仅指出可在 GigaBrain-0 论文中查阅。生成视频仍可能包含幻觉或伪影，可能损害下游策略学习，因此引入质量评估管线作为补救而非根治。对于可变形物体，PhysTwin 采用逐场景优化，而作者探索的前馈方法尚未完成。GigaWorld-0 目前仅作为数据引擎使用，未部署为交互式策略环境用于基于模型的强化学习，也未实现世界模型作为主动策略共同设计者的能力。真实世界经验与合成生成之间的闭环（机器人 rollout 持续改进世界模型）同样未在本文中实现。

## 工程启示

工程启示：对复现、选型、下游团队的具体指导。

1. **先核对训练配置**：MoE 架构下必须启用激活检查点，否则在 8×H20 上会 OOM（DeepSpeed-Zero0 配置直接 OOM）。FSDP2 在内存控制上优于 DeepSpeed-Zero2（73997 MB vs 84699 MB），但两者速度接近，建议优先选择 FSDP2。

2. **注意力算子选择**：NATTEN 相比 SageAttention 有更优加速效果，但需要微调以避免性能退化。若直接替换默认算子，可能引入训练不稳定问题。

3. **数据质量评估不可跳过**：生成视频的幻觉和伪影会直接损害策略学习，建议在数据生产管线中集成四维质量评估（几何一致性、多视点一致性、文本对齐、物理合理性），并设置综合分数阈值决定数据用途。

4. **物理属性辨识的坑**：机械臂的 PINN 三阶段流程中，代理模型的训练质量直接决定后续梯度下降的收敛性。建议先在小规模轨迹上验证代理模型 MSE 是否足够低，再扩展到大规模数据。

5. **视点迁移的复现要点**：ViewTransfer 依赖 MoGe 的尺度估计和 SAM2 的臂部掩码，这两个前置模型的精度直接影响生成质量。建议在目标场景上先验证 MoGe 的深度估计是否准确，否则扭曲过程会产生严重伪影。

6. **下游团队选型**：若任务对物理合理性要求高（如接触丰富的操作），建议优先使用 3D 分支生成的资产；若任务更看重视觉多样性和指令跟随，视频分支的生成结果已足够。两者结合使用时，需注意 3DGS 与网格表示的切换成本。

## Overview
World models are emerging as a foundational paradigm for scalable, data-efficient embodied AI. In this work, we present GigaWorld-0, a unified world model framework designed explicitly as a data engine for Vision-Language-Action (VLA) learning. GigaWorld-0 integrates two synergistic components: GigaWorld-0-Video, which leverages large-scale video generation to produce diverse, texture-rich, and temporally coherent embodied sequences under fine-grained control of appearance, camera viewpoint, and action semantics; and GigaWorld-0-3D, which combines 3D generative modeling, 3D Gaussian Splatting reconstruction, physically differentiable system identification, and executable motion planning to ensure geometric consistency and physical realism. Their joint optimization enables the scalable synthesis of embodied interaction data that is visually compelling, spatially coherent, physically plausible, and instruction-aligned. Training at scale is made feasible through our efficient GigaTrain framework, which exploits FP8-precision and sparse attention to drastically reduce memory and compute requirements. We conduct comprehensive evaluations showing that GigaWorld-0 generates high-quality, diverse, and controllable data across multiple dimensions. Critically, VLA model (e.g., GigaBrain-0) trained on GigaWorld-0-generated data achieve strong real-world performance, significantly improving generalization and task success on physical robots without any real-world interaction during training.

## 参考
- https://arxiv.org/abs/2511.19861

## 개요

GigaWorld-0은 임베디드 지능을 위한 통합 세계 모델 프레임워크로, 비디오 생성(GigaWorld-0-Video)과 3D 자산 생성(GigaWorld-0-3D)의 두 가지 주요 구성 요소로 이루어져 있습니다. VLA 모델의 데이터 엔진 역할을 하여, 합성 데이터로 비용이 높고 제한적인 실제 세계 수집을 대체하는 것을 목표로 합니다. 핵심 기여는 제어 가능한 비디오 생성, 물리적 미분 가능한 시스템 식별, 실행 가능한 모션 플래닝을 확장 가능한 데이터 생산 파이프라인으로 통합하고, 품질 평가 및 추론 가속화 메커니즘을 함께 제공한다는 점입니다.

## 무엇을 바꾸었는가

무엇을 바꾸었는가: 문제와 동기. 전통적인 임베디드 데이터 획득의 병목은 단순한 비용 문제가 아니라, 실제 세계 데이터가 시점, 텍스처, 조명, 물리적 상호작용에서 가지는 다양성의 한계입니다. 이는 VLA 모델이 "보는 것"에서 "행동하는 것"으로 일반화되는 능력을 직접적으로 제한합니다. GigaWorld-0의 실질적인 변화는 세계 모델을 수동적인 예측기로 보지 않고, 능동적이고 프로그래밍 가능한 데이터 생산 도구로 재구성하여 "데이터 생성"이라는 행위 자체가 실제 수집과 동등한 훈련 가치를 갖게 한다는 점입니다. 이는 더 근본적인 질문에 답하려고 시도합니다: 데이터를 필요에 따라 합성할 수 있을 때, 임베디드 지능의 훈련 패러다임이 "수집"에서 "설계"로 전환될 수 있는가?

이 전환의 깊은 동기는 기존 비디오 생성 모델(Cosmos, Wan 등)이 고충실도 화면을 생성할 수 있지만, 물리적 합리성, 다중 시점 일관성, 동작 의미론의 제어 가능성에서 체계적 결함이 있어 생성 콘텐츠를 정책 학습에 직접 사용할 수 없다는 점에 있습니다. GigaWorld-0은 3D 물리 시뮬레이션과 미분 가능한 시스템 식별을 도입하여 생성 과정을 "픽셀 수준의 사실성"에서 "물리 수준의 신뢰성"으로 끌어올리며, 이는 기존 데이터 엔진 패러다임에 대한 핵심 수정입니다.

## 방법 분해

방법 분해: 어떻게 했는가.

### 비디오 생성 브랜치 (GigaWorld-0-Video)
- **기반 모델 (Dreamer)**: flow-matching 공식 `dz_t/dt = v_θ(z_t, t, c)`을 채택하고, 3D-VAE로 원본 비디오를 압축하며, 시공간 압축 비율은 4,8,8(시간, 높이, 너비)로 16채널 잠재 변수를 생성합니다. 이후 1×2×2 patchification을 적용하여 추가 압축하고, 3D-RoPE로 위치 정보를 인코딩합니다.
- **MoE 아키텍처**: FFN 블록에 4개의 라우팅 전문가(N_r=4)를 통합하고, 토큰당 2개의 전문가(K_r=2)를 활성화하며, DeepSeek-V3의 상호 보완 균형 손실을 사용하고 균형 계수 α=0.01입니다. DeepSeek-V2와 달리 공유 전문가는 포함하지 않습니다.
- **제어 가능한 생성**: 세 가지 사후 훈련 적응 모듈을 통해 세밀한 제어를 구현합니다 — AppearanceTransfer(외관 편집), ViewTransfer(시점 이동), MimicTransfer(인간-로봇 동작 이동). ViewTransfer는 이중 재투영 전략을 채택하고, MoGe로 깊이를 추정하여 시점 A의 이미지를 시점 B로 왜곡하며, SAM2로 로봇 팔을 마스킹하여 배경 일관성을 보장합니다. MimicTransfer는 IK를 통해 인간 손의 말단 자세를 로봇 팔의 관절 각도로 매핑하고, SAPIEN 시뮬레이터에서 조건부 비디오를 렌더링합니다.

### 3D 자산 생성 브랜치 (GigaWorld-0-3D)
- **전경 생성 (FG)**: Trellis 기반 이미지-3D 변환으로, 메시와 3DGS 이중 표현을 지원합니다. 전처리 단계에서는 Aesthetic-Checker와 GPT-4o 기반 ImageSegChecker로 분할 신뢰성을 평가하고, 후처리 단계에서는 MeshGeoChecker로 네 개의 직교 시점에서 기하학적 완전성을 검증합니다.
- **배경 재구성 (BG)**: 3DGRUT(각 가우시안에 7개의 대표점 연결)을 채택하여 비-핀홀 카메라를 지원하며, 희소 시점 입력 → 초기 재구성 → 시점 세분화 → 밀집 재구성 → 푸아송 표면 재구성의 흐름으로 수밀 메시를 생성합니다.
- **물리 속성 모델링 (Phys)**: 로봇 팔은 PINN 기반 미분 가능한 물리 프레임워크를 사용하며, 3단계 프로세스: 물리 파라미터를 무작위 샘플링하여 시뮬레이션 롤아웃 생성 → 예측과 시뮬레이션의 MSE를 최소화하는 대리 모델 훈련 → 경사 하강법으로 물리 파라미터 최적화. 조작 대상은 Qwen3-VL 다중 모달 전문가를 기반으로 질량, 마찰 계수 등의 속성을 추론합니다.
- **동작 생성 (Act)**: 두 계층 파이프라인으로, MimicGen 프레임워크를 사용하여 시드 궤적을 새로운 객체 자세와 장면 레이아웃으로 확장하고, 복잡한 장면은 원격 조작 데모를 강화 학습 콜드 스타트 데이터로 사용합니다.

### 훈련 및 추론 최적화
- 훈련 프레임워크 GigaTrain은 DeepSpeed ZeRO(Stages 0–3)와 FSDP2를 지원하며, 훈련 해상도는 480×768, 시퀀스 길이는 61프레임, NATTEN 희소 어텐션 연산자와 FP8 정밀도를 사용합니다.
- 추론 가속화: DMD2 디노이징 스텝 증류로 샘플링을 수십 스텝에서 단일 스텝으로 줄이고, FP8 정밀도를 결합하여 50배 이상의 가속을 달성합니다.

## 핵심 혁신

핵심 혁신:

1. **물리 인식 비디오 생성 제어**: 기존 비디오 모델이 외관이나 카메라 궤적만 제어하는 것과 달리, GigaWorld-0은 ViewTransfer와 MimicTransfer를 통해 로봇 팔의 운동학적 제약(관절 각도, 말단 자세)을 생성 과정에 직접 주입하여, 생성된 비디오의 동작 시퀀스가 물리적으로 실행 가능하도록 합니다. 이는 "조작처럼 보이는 것"에서 "실제로 조작할 수 있는 것"으로의 핵심 도약입니다.

2. **미분 가능한 시스템 식별과 3D 생성의 폐루프**: PINN 기반 물리 파라미터 식별과 3DGS 재구성을 결합하여, 생성된 3D 자산이 외관이 사실적일 뿐만 아니라 올바른 질량, 마찰, 탄성 속성을 가지며 물리 시뮬레이터에 직접 사용할 수 있습니다. 이는 Trellis와 같은 3D 생성 모델이 물리적 합리성이 부족한 근본적 결함을 해결합니다.

3. **경량 제어 브랜치 설계**: MoE 아키텍처에서 ControlNet을 포기하고(MoE 레이어를 복제하면 파라미터가 크게 증가하기 때문), 채널 연결+MLP 압축 방식으로 다중 모달 조건을 주입하여 모델 규모를 유지하면서 세밀한 제어를 구현합니다. 이 설계 결정은 대규모 비디오 생성 모델의 제어 가능한 적응에 직접적인 참조 가치가 있습니다.

## 실험 및 결과

실험 및 결과: 대조 설정, 핵심 수치, 결과의 의미.

### PBench Robot Set 평가
| 모델 | 파라미터 | 품질 점수 | 도메인 점수 | 종합 점수 |
|---|---|---|---|---|
| Cosmos-Predict2 | 14B | 97.4 | 84.0 | 79.88 |
| Wan2.2 | 14B | 95.9 | 83.2 | 78.85 |
| Wan2.2 | 5B | 95.4 | 80.1 | 77.15 |
| Cosmos-Predict2.5 | 2B | 93.8 | 84.7 | 79.95 |
| GigaWorld-0-Video-Dreamer | 2B(Act.) | 97.6 | 88.2 | 82.07 |

GigaWorld-0은 2B 활성 파라미터로 14B 모델을 능가하며, 종합 점수 82.07로 2위보다 약 2.1점 높습니다(표 내 수치 82.07−79.95로 계산). 특히 도메인 점수(88.2)에서 뚜렷한 우위를 보여, 생성 콘텐츠가 임베디드 조작 작업 요구에 더 부합함을 나타냅니다.

### DreamGen Bench 평가 (GR1-Env 하위 집합)
| 방법 | 파라미터 | Qwen-IF | GPT-IF | PA |
|---|---|---|---|---|
| Cosmos-Predict2 | 14B | 0.966 | 0.552 | 0.586 |
| Wan2.2 | 14B | 0.900 | 0.760 | 0.549 |
| Wan2.2 | 5B | 0.790 | 0.340 | 0.531 |
| Cosmos-Predict2.5 | 2B | 0.930 | 0.480 | 0.534 |
| GigaWorld-0-Video-Dreamer | 2B(Act.) | 0.966 | 0.586 | 0.529 |

GR1-Env에서 GigaWorld-0의 Qwen-IF 점수는 Cosmos-Predict2와 공동 최고(0.966)이며, GPT-IF 점수(0.586)는 Cosmos-Predict2(0.552)보다 우수하지만, PA 점수(0.529)는 Cosmos-Predict2(0.586)보다 약간 낮습니다. 이는 명령 따르기에서 우수한 성능을 보이지만 물리적 합리성에서는 여전히 개선 여지가 있음을 나타냅니다.

### 훈련 효율성 (8×H20 GPUs, batch size 32)
| 구성 | 시간 (s/step) | 메모리 (MB) |
|---|---|---|
| DeepSpeed-Zero2 + FP8 + 희소 어텐션 | 25.44 | 76937 |
| FSDP-2 + FP8 + 희소 어텐션 | 25.38 | 73131 |
| DeepSpeed-Zero2 + 활성화 체크포인트 + FP8 + 희소 어텐션 + MoE | 33.27 | 84699 |
| FSDP-2 + 활성화 체크포인트 + FP8 + 희소 어텐션 + MoE | 33.38 | 73997 |

FP8과 희소 어텐션의 조합은 훈련 속도를 32.84 s/step에서 25.38 s/step으로 향상시키지만(표 내 수치 32.84→25.38로 계산), MoE 도입 후 활성화 체크포인트가 필요해 속도는 33.38 s/step으로 돌아가고 메모리는 73997 MB로 제어됩니다.

## 경계와 한계

경계와 한계: 저자는 본 논문에서 하위 작업(예: 옷 접기, 테이블 정리)의 정량적 성공률을 제공하지 않았으며, GigaBrain-0 논문에서 확인할 수 있다고만 언급했습니다. 생성된 비디오는 여전히 환각이나 아티팩트를 포함할 수 있어 하위 정책 학습을 손상시킬 수 있으므로, 품질 평가 파이프라인을 근본적 해결이 아닌 보완책으로 도입했습니다. 변형 가능한 객체의 경우 PhysTwin은 장면별 최적화를 채택하지만, 저자가 탐구한 피드포워드 방법은 아직 완성되지 않았습니다. GigaWorld-0은 현재 데이터 엔진으로만 사용되며, 모델 기반 강화 학습을 위한 상호작용 정책 환경으로 배포되지 않았고, 세계 모델이 능동적 정책 공동 설계자 역할을 하는 능력도 구현되지 않았습니다. 실제 세계 경험과 합성 생성 간의 폐루프(로봇 롤아웃이 세계 모델을 지속적으로 개선)도 본 논문에서 구현되지 않았습니다.

## 엔지니어링 시사점

엔지니어링 시사점: 재현, 선택, 하위 팀에 대한 구체적 지침.

1. **훈련 구성 먼저 확인**: MoE 아키텍처에서는 활성화 체크포인트를 반드시 활성화해야 하며, 그렇지 않으면 8×H20에서 OOM이 발생합니다(DeepSpeed-Zero0 구성은 직접 OOM). FSDP2는 메모리 제어에서 DeepSpeed-Zero2보다 우수하지만(73997 MB vs 84699 MB), 속도는 비슷하므로 FSDP2를 우선 선택하는 것이 좋습니다.

2. **어텐션 연산자 선택**: NATTEN은 SageAttention보다 더 나은 가속 효과를 제공하지만, 성능 저하를 피하기 위해 미세 조정이 필요합니다. 기본 연산자를 직접 교체하면 훈련 불안정 문제가 발생할 수 있습니다.

3. **데이터 품질 평가는 건너뛸 수 없음**: 생성된 비디오의 환각과 아티팩트는 정책 학습을 직접 손상시키므로, 데이터 생산 파이프라인에 4차원 품질 평가(기하학적 일관성, 다중 시점 일관성, 텍스트 정렬, 물리적 합리성)를 통합하고 종합 점수 임계값을 설정하여 데이터 용도를 결정하는 것이 좋습니다.

4. **물리 속성 식별의 함정**: 로봇 팔의 PINN 3단계 프로세스에서 대리 모델의 훈련 품질이 이후 경사 하강법의 수렴성을 직접 결정합니다. 먼저 소규모 궤적에서 대리 모델 MSE가 충분히 낮은지 검증한 후 대규모 데이터로 확장하는 것이 좋습니다.

5. **시점 이동 재현의 핵심 포인트**: ViewTransfer는 MoGe의 스케일 추정과 SAM2의 팔 마스크에 의존하며, 이 두 전제 모델의 정확도가 생성 품질에 직접 영향을 미칩니다. 대상 장면에서 먼저 MoGe의 깊이 추정이 정확한지 검증하는 것이 좋습니다. 그렇지 않으면 왜곡 과정에서 심각한 아티팩트가 발생합니다.

6. **하위 팀 선택**: 작업이 물리적 합리성을 높게 요구하는 경우(예: 접촉이 많은 조작), 3D 브랜치에서 생성된 자산을 우선 사용하는 것이 좋습니다. 작업이 시각적 다양성과 명령 따르기를 더 중시하는 경우, 비디오 브랜치의 생성 결과로 충분합니다. 둘을 결합할 때는 3DGS와 메시 표현 간의 전환 비용에 주의해야 합니다.
