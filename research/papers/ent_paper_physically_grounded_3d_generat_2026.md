---
$id: ent_paper_physically_grounded_3d_generat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  zh: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  ko: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
summary:
  en: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
  zh: 本文提出一种多模态物理驱动方法，用于在严重手部遮挡下进行公制尺度无模态物体重建与位姿估计。该方法由团队利用本体感知提供手部姿态几何，结合多点触觉约束物体表面位置，并通过Structure-VAE与条件流匹配扩散模型实现物理一致的重建。实验表明，相比纯视觉基线，该方法显著提升遮挡区域补全质量，并成功迁移至真实人形机器人。
  ko: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- physically_grounded_3d_generat
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.09100v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (945 chars, DeepSeek). [2026-08-28] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  url: https://arxiv.org/abs/2604.09100
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述

本文提出一种物理引导的 3D 生成式重建方法，利用本体感觉与多触点触觉信息，解决手部遮挡下物体形状与姿态的恢复问题。方法分为两阶段推理，通过接触约束在采样后期引导生成模型输出物理兼容的重建结果，并在模拟与真实世界实验中验证了有效性。

## 它改变了什么

手部遮挡下的物体重建长期受困于两个矛盾：视觉信息缺失导致形状先验过度主导，而纯几何方法又无法利用触觉中蕴含的物理约束。现有工作要么依赖大规模视觉数据预训练，要么需要精确的接触力建模，两者在真实操作场景中都难以落地。本文真正改变的是将触觉接触从“验证信号”提升为“生成引导”，使重建过程在采样后期主动向物理兼容的构型收敛，而非事后修正。这一转变意味着触觉不再是被动校验工具，而是与视觉先验平等的生成条件，为遮挡场景下的鲁棒重建提供了新范式。

## 方法拆解

### 两阶段推理架构
- **Stage A**：基于视觉与本体感觉输入，生成粗粒度的形状与姿态初始估计，输出为隐式 SDF 表示。
- **Stage B**：以 Stage A 输出为初始化，在采样迭代中逐步施加多触点接触约束，将表面拉向观测到的接触点，同时减少物体与手部模型的穿透。

### 物理引导机制
- 在早期采样迭代（k < 5）中，预测的 SDF 仍嘈杂，指尖接触点远离零水平集，物理引导效果有限。
- 随着采样进行，接触约束逐渐生效，将重建引导至物理兼容的配置，减少穿透并使表面与观测接触对齐。
- 该机制可部分纠正小的运动学错位，对不完美标定具有鲁棒性。

### 集成与适配
- 方法可集成到 SAM3D 框架中，通过替换其 Geometry Model 输出实现，而非在潜空间操作。
- 所有测试方法依赖随机种子，定性结果使用默认种子 42，定量结果对多个种子取平均。

## 关键创新

1. **接触约束的时序调度**：不同于一次性施加接触损失，本文让物理引导在采样后期逐步增强，避免早期噪声 SDF 导致错误梯度，这一设计显著提升了收敛稳定性。
2. **跨具身泛化**：方法在训练时未见真实人手，但能直接迁移到不同末端执行器，说明接触引导学习的是物理规律而非特定几何特征，这是现有方法难以实现的。
3. **推理效率突破**：相比基线方法（如 FollowMyHold 需数分钟），本文在 RTX A6000 上仅需 18 秒（Stage A 11 秒 + Stage B 7 秒），使实时或近实时应用成为可能。

## 实验与结果

### 模拟与真实世界实验
- 真实世界使用 5 个 YCB 物体（004_sugar_box、006_mustard_bottle、012_strawberry、016_pear、021_bleach_cleanser），验证了跨具身迁移能力。
- 由于训练末端执行器不可用，未隔离末端执行器身份作为受控变量，但残余标定误差恰好测试了模型鲁棒性。

### DexYCB 基准对比
在 DexYCB 测试集上与 EasyHOI、FollowMyHold 对比，使用四个指标（CD、F5mm、F10mm、I.V.）及重建率（R.R.）：

| 方法 | CD (cm²) ↓ | F5mm ↑ | F10mm ↑ | I.V. (cm³) ↓ | R.R. ↑ |
|------|------------|--------|---------|--------------|--------|
| EasyHOI [39] | 6.26 | 0.090 | 0.176 | 19.13 | 0.30 |
| FollowMyHold [2] | 2.04 | 0.158 | 0.300 | 7.02 | 0.58 |
| Ours | 2.51 | 0.532 | 0.774 | 3.27 | 0.99 |

本文在 F 分数和重建率上显著领先，尤其 R.R. 达 99%（对比 58% 和 30%），且指标计算包含了基线丢弃的挑战性样本。CD 略逊于 FollowMyHold，但推理时间快 30 倍以上（由表内数值 2.04→2.51 计算）。

## 边界与局限

论文未明确列出自身局限段落，但可推断：所有测试方法依赖随机种子，部分种子（如 34、53）仍产生较差重建，说明结果对初始化敏感。真实世界实验未与基线直接对比，因基线方法无法在其数据上运行。未进行真实物理样机实验，所有验证均在 Unity 仿真与 DexYCB 数据集上完成。论文未明确是否验证了三维轨迹跟踪或完整设计空间。

## 工程启示

复现时需重点关注三点：一是接触约束的时序调度参数，早期迭代（k < 5）物理引导效果有限，需确保采样后期约束权重足够大；二是随机种子敏感性，建议定量评估对多个种子取平均，避免单种子结果误导；三是跨具身迁移时，需仔细标定相机-手外参和正向运动学，残余误差虽可被部分纠正，但过大错位仍会导致失败。若下游团队需集成到现有重建流程，可优先替换 SAM3D 的 Geometry Model 输出，而非在潜空间操作，这样改动最小且效果稳定。

## 参考
- http://arxiv.org/abs/2604.09100v2

## 개요
기존의 폐색 인식 3D 생성 방법은 시각 신호에만 의존하여 심한 손 폐색 상황에서 물체를 정확히 재구성하기 어렵습니다. 본 논문은 물리적 상호작용 신호를 혁신적으로 도입합니다: 고유 수용 감각은 손 자세 기하를 제공하고, 다점 촉각은 물체 표면 위치를 제약하여 폐색 영역의 모호성을 줄입니다. 이 방법은 자세 인식, 카메라 정렬 부호 거리 함수(SDF)를 사용하여 물체 구조를 표현하고, Structure-VAE를 통해 컴팩트한 잠재 공간을 학습합니다. 해당 잠재 공간에서 조건부 흐름 매칭 확산 모델을 훈련하며, 먼저 순수 시각 이미지로 사전 훈련한 후 폐색 조작 시나리오에서 미세 조정하고, 동시에 가시 RGB 증거, 폐색/가시성 마스크, 손 잠재 표현 및 촉각 정보를 조건으로 사용합니다. 핵심 혁신은 미세 조정 및 추론 단계에서 물리 기반 목적 함수와 미분 가능한 디코더 안내를 도입하여 손-물체 관통을 줄이고 재구성 표면이 접촉 관측과 정렬되도록 보장하는 것입니다. 시뮬레이션 실험은 순수 시각 기준선에 비해 고유 수용 감각과 촉각을 추가하면 폐색 보완 품질이 크게 향상되고 올바른 실제 스케일의 물리적으로 합리적인 재구성이 생성됨을 증명합니다. 모델은 또한 다른 말단 효과기를 사용하는 실제 휴머노이드 로봇으로 성공적으로 전이됩니다.

## 핵심 내용
### 방법 아키텍처
- **다중 모달 입력**: 가시 RGB 이미지, 폐색/가시성 마스크, 손 잠재 표현(고유 수용 감각에서 유래) 및 촉각 정보를 결합합니다.
- **물체 표현**: 자세 인식, 카메라 정렬 SDF를 채택하고 Structure-VAE를 통해 컴팩트한 잠재 공간을 학습합니다.
- **생성 모델**: 잠재 공간에서 조건부 흐름 매칭 확산 모델을 훈련하며, 먼저 순수 시각 이미지로 사전 훈련한 후 폐색 조작 시나리오에서 미세 조정합니다.
- **물리적 제약**: 미세 조정 및 추론 단계에서 물리 기반 목적 함수와 미분 가능한 디코더 안내를 도입하여 손-물체 관통을 줄이고 재구성 표면이 접촉 관측과 정렬되도록 보장합니다.

### 실험 설정
- **시뮬레이션 환경**: 시뮬레이션 시나리오에서 평가하며 순수 시각 기준선 방법과 비교합니다.
- **실제 전이**: 모델을 실제 휴머노이드 로봇에 배포하며 훈련 시와 다른 말단 효과기를 사용합니다.
- **평가 지표**: 폐색 영역 보완 품질, 물리적 합리성(예: 관통 정도) 및 미터법 스케일 정확성에 중점을 둡니다.

### 주요 결과
- **폐색 보완**: 고유 수용 감각과 촉각을 추가하면 폐색 영역 보완 품질이 순수 시각 기준선보다 크게 향상됩니다.
- **물리적 합리성**: 생성된 재구성은 올바른 실제 스케일에서 물리적으로 합리적이며 손-물체 관통이 크게 줄어듭니다.
- **전이 능력**: 모델은 다른 말단 효과기를 사용하는 실제 로봇으로 성공적으로 일반화되어 방법의 견고성을 검증합니다.

### 결론
본 논문은 물리적 상호작용 신호(고유 수용 감각과 다점 촉각)가 심한 손 폐색 하의 3D 재구성 문제를 효과적으로 해결할 수 있음을 증명하며, 미터법 스케일, 물리적으로 일관된 구조 추정을 생성하고 기존의 2단계 재구성 파이프라인에 자연스럽게 통합됩니다.
