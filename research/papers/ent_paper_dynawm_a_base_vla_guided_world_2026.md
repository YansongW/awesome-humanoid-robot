---
$id: ent_paper_dynawm_a_base_vla_guided_world_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
  zh: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
  ko: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
summary:
  en: 'arXiv:2607.02604v1 Announce Type: cross Abstract: Although vision-language-action (VLA) models have received widespread
    attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward
    or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may
    degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose
    DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA
    checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk
    produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from
    multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These
    feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object
    manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object
    manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the
    DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images.
    For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA,
    X-VLA, {\pi}0, and {\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06,
    35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%,
    while reducing success by 45.44% if action conditioning is removed.'
  zh: DynaWM 是一种基于基础 VLA 引导的世界基础模型，专为动态移动物体操作设计。它通过 Mamba-3 动作编码器、V-JEPA 2.1 视觉编码器和本体状态编码器，联合条件化流匹配 DiT 以生成运动感知动作轨迹。在 DynaGrasp-32
    基准上，DynaWM 在微调和粗调基础 VLA 检查点上分别实现了最高 45.31% 和 44.06% 的性能提升。
  ko: 'arXiv:2607.02604v1 Announce Type: cross Abstract: Although vision-language-action (VLA) models have received widespread
    attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward
    or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may
    degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose
    DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA
    checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk
    produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from
    multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These
    feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object
    manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object
    manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the
    DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images.
    For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA,
    X-VLA, {\pi}0, and {\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06,
    35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%,
    while reducing success by 45.44% if action conditioning is removed.'
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
- robotics
- dynawm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02604v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1082 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.02604
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
DynaWM 由研究团队提出，旨在解决现有 VLA 模型在操作动态移动物体时因不当微调导致性能下降的问题。该模型采用模块化架构，通过 Mamba-3 动作编码器将基础 VLA 的动作块编码为动作条件表示，结合 V-JEPA 2.1 视觉编码器提取多视角观测特征，以及本体状态编码器处理机械臂状态，共同引导流匹配 DiT 生成运动感知轨迹。为系统评估，团队构建了包含 32 个场景、1600 条演示轨迹和约 153 万张图像的 DynaGrasp-1600 数据集，以及覆盖速度变化、轨迹变化和多物体操作等六类任务的 DynaGrasp-32 基准。

## 核心内容
### 方法架构
DynaWM 的核心创新在于其基础 VLA 引导机制，避免直接微调预训练模型。具体组件包括：
- **Mamba-3 动作编码器**：将基础 VLA 输出的动作块编码为动作条件表示，保留运动意图。
- **V-JEPA 2.1 视觉编码器**：从多视角观测历史中提取视觉特征，增强对动态环境的理解。
- **本体状态编码器**：编码机械臂的本体状态（如关节角度、末端执行器位置）。
- **流匹配 DiT**：以上述三种表示作为条件，通过扩散过程生成运动感知的动作轨迹，专为移动物体操作优化。

### 实验设置
- **基准与数据集**：构建 DynaGrasp-32 基准，包含六类任务（速度变化、轨迹变化、多物体操作等）；DynaGrasp-1600 数据集含 32 个场景、1600 条演示轨迹、约 153 万张图像。
- **基础 VLA 检查点**：测试了四种微调检查点（SmolVLA、X-VLA、π0、π0.5）和四种粗调检查点（对应模型）。
- **评估指标**：任务成功率。

### 关键结果
- **微调检查点**：DynaWM 在 SmolVLA、X-VLA、π0、π0.5 上分别提升 7.19%、45.31%、1.88%、10.94%。
- **粗调检查点**：性能分别提升 35.13%、44.06%、35.69%、26.13%。
- **消融实验**：
  - 移除视觉编码（V-JEPA 2.1）导致成功率下降 27.50%。
  - 移除动作条件（Mamba-3 编码）导致成功率下降 45.44%，表明动作条件对动态操作至关重要。

### 结论
DynaWM 通过基础 VLA 引导的模块化设计，在不破坏预训练模型性能的前提下，显著提升了动态移动物体操作的成功率。其动作条件表示和视觉编码的协同作用被消融实验证实为关键因素。

## Overview
Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, π0, and π0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

## 参考
- http://arxiv.org/abs/2607.02604v1

## 개요
DynaWM은 연구팀이 제안한 모델로, 기존 VLA 모델이 동적 이동 물체를 조작할 때 부적절한 미세 조정으로 인해 성능이 저하되는 문제를 해결하기 위해 설계되었습니다. 이 모델은 모듈식 아키텍처를 채택하여, Mamba-3 동작 인코더가 기본 VLA의 동작 블록을 동작 조건 표현으로 인코딩하고, V-JEPA 2.1 비전 인코더가 다중 시점 관측 특징을 추출하며, 본체 상태 인코더가 로봇 팔 상태를 처리하여, 이들이 함께 플로우 매칭 DiT가 운동 인식 궤적을 생성하도록 유도합니다. 체계적인 평가를 위해 연구팀은 32개 장면, 1600개 시연 궤적, 약 153만 장의 이미지를 포함하는 DynaGrasp-1600 데이터셋과 속도 변화, 궤적 변화, 다중 물체 조작 등 여섯 가지 작업 유형을 포함하는 DynaGrasp-32 벤치마크를 구축했습니다.

## 핵심 내용
### 방법 아키텍처
DynaWM의 핵심 혁신은 사전 훈련된 모델을 직접 미세 조정하지 않는 기본 VLA 유도 메커니즘에 있습니다. 구체적인 구성 요소는 다음과 같습니다:
- **Mamba-3 동작 인코더**: 기본 VLA가 출력한 동작 블록을 동작 조건 표현으로 인코딩하여 운동 의도를 보존합니다.
- **V-JEPA 2.1 비전 인코더**: 다중 시점 관측 기록에서 시각적 특징을 추출하여 동적 환경에 대한 이해를 강화합니다.
- **본체 상태 인코더**: 로봇 팔의 본체 상태(예: 관절 각도, 엔드 이펙터 위치)를 인코딩합니다.
- **플로우 매칭 DiT**: 위 세 가지 표현을 조건으로 사용하여 확산 과정을 통해 운동 인식 동작 궤적을 생성하며, 이동 물체 조작에 특화되어 있습니다.

### 실험 설정
- **벤치마크 및 데이터셋**: DynaGrasp-32 벤치마크를 구축하여 여섯 가지 작업 유형(속도 변화, 궤적 변화, 다중 물체 조작 등)을 포함합니다. DynaGrasp-1600 데이터셋은 32개 장면, 1600개 시연 궤적, 약 153만 장의 이미지를 포함합니다.
- **기본 VLA 체크포인트**: 네 가지 미세 조정 체크포인트(SmolVLA, X-VLA, π0, π0.5)와 네 가지 거친 조정 체크포인트(해당 모델)를 테스트했습니다.
- **평가 지표**: 작업 성공률.

### 주요 결과
- **미세 조정 체크포인트**: DynaWM은 SmolVLA, X-VLA, π0, π0.5에서 각각 7.19%, 45.31%, 1.88%, 10.94% 향상되었습니다.
- **거친 조정 체크포인트**: 성능이 각각 35.13%, 44.06%, 35.69%, 26.13% 향상되었습니다.
- **절제 실험**:
  - 비전 인코딩(V-JEPA 2.1) 제거 시 성공률이 27.50% 하락했습니다.
  - 동작 조건(Mamba-3 인코딩) 제거 시 성공률이 45.44% 하락하여, 동작 조건이 동적 조작에 필수적임을 보여줍니다.

### 결론
DynaWM은 기본 VLA 유도 모듈식 설계를 통해 사전 훈련된 모델의 성능을 손상시키지 않으면서 동적 이동 물체 조작의 성공률을 크게 향상시킵니다. 동작 조건 표현과 비전 인코딩의 시너지 효과는 절제 실험을 통해 핵심 요인으로 확인되었습니다.
