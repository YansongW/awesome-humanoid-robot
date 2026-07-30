---
$id: ent_paper_training_vision_language_actio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision
  zh: Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision
  ko: Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision
summary:
  en: 'arXiv:2606.30552v2 Announce Type: replace Abstract: Cross-embodiment transfer in vision-language-action (VLA) models
    remains challenging because low-level state and action spaces differ fundamentally across robot platforms. We observe
    that the high-level cognitive process underlying manipulation, including scene perception, object identification, task
    planning, and sub-task decomposition, is largely shared across embodiments. Based on this observation, we present ZR-0,
    a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment
    representations within the vision-language model (VLM). ZR-0 adopts a dual-stream architecture: a pre-trained VLM (System
    2) generates structured ECoT reasoning during training, while a Diffusion Transformer-based action expert (System 1) produces
    continuous action chunks via flow matching. The two components are coupled through cross-attention, with an attention
    mask that restricts the action expert to input prompt features only, enabling ECoT generation to be entirely skipped at
    inference without any performance loss. ZR-0 is pre-trained on ProcCorpus-60M, a large-scale dataset comprising approximately
    60 million frames (approximately 1,000 hours) from over 400K trajectories, with dense ECoT annotations covering 96.8%
    of all frames. We evaluate ZR-0 on three simulation benchmarks spanning single-arm (LIBERO), bimanual (RoboTwin 2.0),
    and humanoid (RoboCasa GR-1 Tabletop) embodiments, as well as real-world experiments on the xArm platform, demonstrating
    strong performance across all settings. Code and model checkpoints are available at https://github.com/RUCKBReasoning/ZR-0.'
  zh: ZR-0 是一个 26 亿参数的端到端视觉-语言-动作模型，由中国人民大学等机构提出。其核心贡献在于利用密集的具身思维链（ECoT）监督来对齐不同机器人平台间的跨本体表征，并采用双流架构在推理时跳过 ECoT 生成而不损失性能。模型在包含约
    6000 万帧的 ProcCorpus-60M 数据集上预训练，在单臂、双臂和类人机器人仿真基准以及真实 xArm 平台上均表现优异。
  ko: 'arXiv:2606.30552v2 Announce Type: replace Abstract: Cross-embodiment transfer in vision-language-action (VLA) models
    remains challenging because low-level state and action spaces differ fundamentally across robot platforms. We observe
    that the high-level cognitive process underlying manipulation, including scene perception, object identification, task
    planning, and sub-task decomposition, is largely shared across embodiments. Based on this observation, we present ZR-0,
    a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment
    representations within the vision-language model (VLM). ZR-0 adopts a dual-stream architecture: a pre-trained VLM (System
    2) generates structured ECoT reasoning during training, while a Diffusion Transformer-based action expert (System 1) produces
    continuous action chunks via flow matching. The two components are coupled through cross-attention, with an attention
    mask that restricts the action expert to input prompt features only, enabling ECoT generation to be entirely skipped at
    inference without any performance loss. ZR-0 is pre-trained on ProcCorpus-60M, a large-scale dataset comprising approximately
    60 million frames (approximately 1,000 hours) from over 400K trajectories, with dense ECoT annotations covering 96.8%
    of all frames. We evaluate ZR-0 on three simulation benchmarks spanning single-arm (LIBERO), bimanual (RoboTwin 2.0),
    and humanoid (RoboCasa GR-1 Tabletop) embodiments, as well as real-world experiments on the xArm platform, demonstrating
    strong performance across all settings. Code and model checkpoints are available at https://github.com/RUCKBReasoning/ZR-0.'
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
- training_vision_language_actio
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30552v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision (arXiv)
  url: https://arxiv.org/abs/2606.30552
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
ZR-0 针对视觉-语言-动作模型在跨本体迁移中因底层状态和动作空间差异而面临的挑战，提出利用高层认知过程（如场景感知、物体识别、任务规划）的共享性来解决问题。模型采用双流架构：预训练的视觉-语言模型（System 2）在训练时生成结构化的 ECoT 推理，而基于 Diffusion Transformer 的动作专家（System 1）通过流匹配产生连续动作块。两者通过交叉注意力耦合，并借助注意力掩码确保推理时 ECoT 生成可被完全跳过。ZR-0 在包含约 6000 万帧、96.8% 帧具有密集 ECoT 标注的 ProcCorpus-60M 数据集上预训练，并在 LIBERO、RoboTwin 2.0、RoboCasa GR-1 Tabletop 三个仿真基准及 xArm 真实平台上验证了其强大性能。

## 核心内容
### 方法概述
ZR-0 的核心思想是利用高层认知过程的跨本体共享性，通过密集的 Embodied Chain-of-Thought (ECoT) 监督来对齐不同机器人平台的表征。ECoT 包含场景感知、物体识别、任务规划和子任务分解等结构化推理步骤。

### 双流架构
- **System 2（视觉-语言模型）**：采用预训练的 VLM，在训练阶段生成结构化的 ECoT 推理文本。
- **System 1（动作专家）**：基于 Diffusion Transformer，通过流匹配（flow matching）生成连续的 action chunks。
- **耦合机制**：两个系统通过交叉注意力（cross-attention）连接，并设计了一个注意力掩码，限制动作专家仅能访问输入提示特征，从而在推理时完全跳过 ECoT 生成而不影响性能。

### 数据集与训练
- **ProcCorpus-60M**：包含约 6000 万帧（约 1000 小时），来自超过 40 万条轨迹，其中 96.8% 的帧具有密集的 ECoT 标注。
- 模型参数量为 26 亿，采用端到端预训练方式。

### 实验设置与结果
- **仿真基准**：
  - 单臂操作：LIBERO
  - 双臂操作：RoboTwin 2.0
  - 类人机器人：RoboCasa GR-1 Tabletop
- **真实实验**：在 xArm 平台上进行。
- **性能**：ZR-0 在所有设置下均展现出强劲性能，具体数字未在摘要中列出，但表明其跨本体迁移能力显著。

### 结论
ZR-0 通过密集 ECoT 监督和双流架构，有效解决了 VLA 模型跨本体迁移的难题，在多个仿真和真实场景中验证了其有效性。代码和模型检查点已开源。

## Overview
Cross-embodiment transfer in vision-language-action (VLA) models remains challenging because low-level state and action spaces differ fundamentally across robot platforms. We observe that the high-level cognitive process underlying manipulation, including scene perception, object identification, task planning, and sub-task decomposition, is largely shared across embodiments. Based on this observation, we present ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment representations within the vision-language model (VLM). ZR-0 adopts a dual-stream architecture: a pre-trained VLM (System 2) generates structured ECoT reasoning during training, while a Diffusion Transformer-based action expert (System 1) produces continuous action chunks via flow matching. The two components are coupled through cross-attention, with an attention mask that restricts the action expert to input prompt features only, enabling ECoT generation to be entirely skipped at inference without any performance loss. ZR-0 is pre-trained on ProcCorpus-60M, a large-scale dataset comprising approximately 60 million frames (approximately 1,000 hours) from over 400K trajectories, with dense ECoT annotations covering 96.8% of all frames. We evaluate ZR-0 on three simulation benchmarks spanning single-arm (LIBERO), bimanual (RoboTwin 2.0), and humanoid (RoboCasa GR-1 Tabletop) embodiments, as well as real-world experiments on the xArm platform, demonstrating strong performance across all settings. Code and model checkpoints are available at https://github.com/RUCKBReasoning/ZR-0.

## 개요
비전-언어-행동(VLA) 모델에서의 교차 체화 전이(Cross-embodiment transfer)는 로봇 플랫폼 간 저수준 상태 및 행동 공간이 근본적으로 다르기 때문에 여전히 어려운 과제입니다. 우리는 조작의 기저에 있는 고수준 인지 과정(장면 인식, 객체 식별, 작업 계획, 하위 작업 분해 포함)이 체화 간에 대부분 공유된다는 점을 관찰했습니다. 이러한 관찰을 바탕으로, 우리는 밀집된 체화 사고 사슬(ECoT) 감독을 사용하여 비전-언어 모델(VLM) 내에서 교차 체화 표현을 정렬하는 26억 개의 매개변수를 가진 종단 간 VLA 모델인 ZR-0을 제시합니다. ZR-0은 이중 스트림 아키텍처를 채택합니다. 사전 훈련된 VLM(System 2)은 훈련 중 구조화된 ECoT 추론을 생성하고, Diffusion Transformer 기반 행동 전문가(System 1)는 흐름 매칭을 통해 연속적인 행동 청크를 생성합니다. 두 구성 요소는 교차 주의를 통해 결합되며, 행동 전문가가 입력 프롬프트 특징만 사용하도록 제한하는 주의 마스크를 사용하여 추론 시 ECoT 생성을 완전히 건너뛸 수 있어 성능 손실이 없습니다. ZR-0은 약 6천만 프레임(약 1,000시간)과 40만 개 이상의 궤적으로 구성된 대규모 데이터셋인 ProcCorpus-60M에서 사전 훈련되었으며, 모든 프레임의 96.8%에 밀집된 ECoT 주석이 포함되어 있습니다. 우리는 단일 암(LIBERO), 양팔(RoboTwin 2.0), 휴머노이드(RoboCasa GR-1 Tabletop) 체화를 포함한 세 가지 시뮬레이션 벤치마크와 xArm 플랫폼에서의 실제 실험을 통해 ZR-0을 평가하여 모든 설정에서 강력한 성능을 입증했습니다. 코드와 모델 체크포인트는 https://github.com/RUCKBReasoning/ZR-0에서 확인할 수 있습니다.

## 핵심 내용
비전-언어-행동(VLA) 모델에서의 교차 체화 전이는 로봇 플랫폼 간 저수준 상태 및 행동 공간이 근본적으로 다르기 때문에 여전히 어려운 과제입니다. 우리는 조작의 기저에 있는 고수준 인지 과정(장면 인식, 객체 식별, 작업 계획, 하위 작업 분해 포함)이 체화 간에 대부분 공유된다는 점을 관찰했습니다. 이러한 관찰을 바탕으로, 우리는 밀집된 체화 사고 사슬(ECoT) 감독을 사용하여 비전-언어 모델(VLM) 내에서 교차 체화 표현을 정렬하는 26억 개의 매개변수를 가진 종단 간 VLA 모델인 ZR-0을 제시합니다. ZR-0은 이중 스트림 아키텍처를 채택합니다. 사전 훈련된 VLM(System 2)은 훈련 중 구조화된 ECoT 추론을 생성하고, Diffusion Transformer 기반 행동 전문가(System 1)는 흐름 매칭을 통해 연속적인 행동 청크를 생성합니다. 두 구성 요소는 교차 주의를 통해 결합되며, 행동 전문가가 입력 프롬프트 특징만 사용하도록 제한하는 주의 마스크를 사용하여 추론 시 ECoT 생성을 완전히 건너뛸 수 있어 성능 손실이 없습니다. ZR-0은 약 6천만 프레임(약 1,000시간)과 40만 개 이상의 궤적으로 구성된 대규모 데이터셋인 ProcCorpus-60M에서 사전 훈련되었으며, 모든 프레임의 96.8%에 밀집된 ECoT 주석이 포함되어 있습니다. 우리는 단일 암(LIBERO), 양팔(RoboTwin 2.0), 휴머노이드(RoboCasa GR-1 Tabletop) 체화를 포함한 세 가지 시뮬레이션 벤치마크와 xArm 플랫폼에서의 실제 실험을 통해 ZR-0을 평가하여 모든 설정에서 강력한 성능을 입증했습니다. 코드와 모델 체크포인트는 https://github.com/RUCKBReasoning/ZR-0에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2606.30552v2
