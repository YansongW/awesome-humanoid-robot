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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30552v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1135 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.30552v2

## 개요
ZR-0은 시각-언어-행동 모델이 교차 본체 전이에서 하위 상태 및 행동 공간의 차이로 인해 직면하는 문제를 해결하기 위해, 고수준 인지 과정(예: 장면 인식, 객체 인식, 작업 계획)의 공유성을 활용하는 것을 제안합니다. 모델은 이중 스트림 아키텍처를 채택합니다: 사전 훈련된 시각-언어 모델(System 2)은 훈련 중 구조화된 ECoT 추론을 생성하고, Diffusion Transformer 기반의 행동 전문가(System 1)는 흐름 매칭을 통해 연속적인 행동 청크를 생성합니다. 두 시스템은 교차 주의를 통해 결합되며, 주의 마스크를 통해 추론 시 ECoT 생성을 완전히 건너뛸 수 있습니다. ZR-0은 약 6000만 프레임을 포함하고 96.8%의 프레임에 밀집된 ECoT 주석이 있는 ProcCorpus-60M 데이터셋에서 사전 훈련되었으며, LIBERO, RoboTwin 2.0, RoboCasa GR-1 Tabletop의 세 가지 시뮬레이션 벤치마크와 xArm 실제 플랫폼에서 강력한 성능을 검증했습니다.

## 핵심 내용
### 방법 개요
ZR-0의 핵심 아이디어는 고수준 인지 과정의 교차 본체 공유성을 활용하여, 밀집된 Embodied Chain-of-Thought (ECoT) 감독을 통해 서로 다른 로봇 플랫폼의 표현을 정렬하는 것입니다. ECoT는 장면 인식, 객체 인식, 작업 계획 및 하위 작업 분해와 같은 구조화된 추론 단계를 포함합니다.

### 이중 스트림 아키텍처
- **System 2 (시각-언어 모델)**: 사전 훈련된 VLM을 사용하며, 훈련 단계에서 구조화된 ECoT 추론 텍스트를 생성합니다.
- **System 1 (행동 전문가)**: Diffusion Transformer 기반으로, 흐름 매칭을 통해 연속적인 행동 청크를 생성합니다.
- **결합 메커니즘**: 두 시스템은 교차 주의로 연결되며, 행동 전문가가 입력 프롬프트 특징에만 접근할 수 있도록 제한하는 주의 마스크를 설계하여, 추론 시 ECoT 생성을 완전히 건너뛰어도 성능에 영향을 주지 않습니다.

### 데이터셋 및 훈련
- **ProcCorpus-60M**: 약 6000만 프레임(약 1000시간)을 포함하며, 40만 개 이상의 궤적에서 수집되었고, 96.8%의 프레임에 밀집된 ECoT 주석이 있습니다.
- 모델 파라미터 수는 26억 개이며, 종단 간 사전 훈련 방식을 채택합니다.

### 실험 설정 및 결과
- **시뮬레이션 벤치마크**:
  - 단일 팔 조작: LIBERO
  - 이중 팔 조작: RoboTwin 2.0
  - 인간형 로봇: RoboCasa GR-1 Tabletop
- **실제 실험**: xArm 플랫폼에서 수행.
- **성능**: ZR-0은 모든 설정에서 강력한 성능을 보여주며, 구체적인 수치는 요약에 나열되지 않았지만 교차 본체 전이 능력이 뛰어남을 나타냅니다.

### 결론
ZR-0은 밀집된 ECoT 감독과 이중 스트림 아키텍처를 통해 VLA 모델의 교차 본체 전이 문제를 효과적으로 해결하며, 여러 시뮬레이션 및 실제 시나리오에서 그 유효성을 검증했습니다. 코드와 모델 체크포인트는 오픈소스로 공개되었습니다.
