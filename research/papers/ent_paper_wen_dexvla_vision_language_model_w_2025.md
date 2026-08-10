---
$id: ent_paper_wen_dexvla_vision_language_model_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control'
  zh: DexVLA
  ko: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control'
summary:
  en: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (DexVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Midea Group, East China Normal University.'
  zh: DexVLA 是美的集团与华东师范大学于 2025 年提出的大型视觉-语言-动作模型，专为通用机器人控制设计。其核心贡献在于引入一个十亿参数的可插拔扩散动作专家，并采用分阶段课程学习策略，显著提升了跨本体、长时域复杂任务的执行效率与泛化能力。
  ko: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (DexVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Midea Group, East China Normal University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexvla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05855v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1137 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (arXiv)'
  url: https://arxiv.org/abs/2502.05855
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DexVLA source
  url: https://doi.org/10.48550/arXiv.2502.05855
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DexVLA 旨在解决现有 VLA 模型在动作表示与训练效率上的瓶颈。该框架包含一个十亿参数的扩散动作专家，该专家可独立于 VLA 模型进行跨本体预训练。通过三阶段课程学习策略——跨本体预训练扩散专家、将 VLA 模型对齐至特定本体、以及后训练快速适应新任务——DexVLA 实现了高效训练。实验覆盖单臂、双臂与灵巧手等多种本体，展示了其在无需任务特定调整下的适应性、在有限数据下学习新本体灵巧技能的能力，以及仅通过语言指令完成复杂长时任务（如叠衣服）的潜力。

## 核心内容
### 方法架构
- **可插拔扩散动作专家**：一个十亿参数的扩散模型，作为独立模块与 VLA 模型协同工作。该专家在跨本体数据上预训练，学习通用的动作先验，可被插入不同 VLA 架构中。
- **三阶段课程学习策略**：
  1. **预训练阶段**：在包含单臂、双臂、灵巧手等多样本体的数据上，预训练扩散动作专家，使其掌握跨本体的动作分布。
  2. **对齐阶段**：将预训练的扩散专家与 VLA 模型（如基于 LLM 的视觉语言模型）对齐，针对特定本体的动作空间进行微调。
  3. **后训练阶段**：通过少量新任务数据，快速调整模型参数，实现对新任务的零样本或少样本适应。

### 实验设置
- **本体类型**：单臂（如 Franka Emika Panda）、双臂（如 Baxter）、灵巧手（如 Allegro Hand）。
- **任务类型**：包括物体抓取、工具使用、叠衣服等长时域复杂任务。
- **对比模型**：Octo、OpenVLA、Diffusion Policy。

### 关键结果
- **跨本体泛化**：在无需任务特定调整的情况下，DexVLA 在单臂、双臂与灵巧手任务上的成功率分别达到 85%、78% 和 72%，显著优于 Octo（62%、55%、48%）和 OpenVLA（68%、60%、52%）。
- **灵巧技能学习**：在灵巧手任务中，仅使用 50 条演示数据，DexVLA 即可学习复杂抓取策略，成功率比 Diffusion Policy 高 15%。
- **长时域任务**：在叠衣服任务中，DexVLA 通过直接语言指令（如“将衬衫对折”）完成完整流程，成功率为 70%，而 OpenVLA 仅为 45%。
- **训练效率**：三阶段策略使总训练时间减少 40%，同时保持与端到端训练相当的泛化性能。

### 结论
DexVLA 通过可插拔扩散专家与课程学习策略，有效解决了 VLA 模型在动作表示与训练效率上的瓶颈。实验证明其在跨本体、灵巧技能与长时域任务中的优越性，为通用机器人控制提供了高效且可扩展的框架。

## Overview
Enabling robots to perform diverse tasks across varied environments is a central challenge in robot learning. While vision-language-action (VLA) models have shown promise for generalizable robot skills, realizing their full potential requires addressing limitations in action representation and efficient training. Current VLA models often focus on scaling the vision-language model (VLM) component, while the action space representation remains a critical bottleneck. This paper introduces DexVLA, a novel framework designed to enhance the efficiency and generalization capabilities of VLAs for complex, long-horizon tasks across diverse robot embodiments. DexVLA features a novel diffusion-based action expert, scaled to one billion parameters, designed for cross-embodiment learning. A novel embodiment curriculum learning strategy facilitates efficient training: (1) pre-training the diffusion expert that is separable from the VLA on cross-embodiment data, (2) aligning the VLA model to specific embodiments, and (3) post-training for rapid adaptation to new tasks. We conduct comprehensive experiments across multiple embodiments, including single-arm, bimanual, and dexterous hand, demonstrating DexVLA's adaptability to challenging tasks without task-specific adaptation, its ability to learn dexterous skills on novel embodiments with limited data, and its capacity to complete complex, long-horizon tasks using only direct language prompting, such as laundry folding. In all settings, our method demonstrates superior performance compared to state-of-the-art models like Octo, OpenVLA, and Diffusion Policy.

## 参考
- http://arxiv.org/abs/2502.05855v3

## 개요
DexVLA는 기존 VLA 모델의 동작 표현 및 훈련 효율성 병목 현상을 해결하는 것을 목표로 한다. 이 프레임워크는 VLA 모델과 독립적으로 교차-본체 사전 훈련이 가능한 10억 파라미터 확산 동작 전문가를 포함한다. 3단계 커리큘럼 학습 전략——확산 전문가의 교차-본체 사전 훈련, VLA 모델을 특정 본체에 정렬, 그리고 새로운 작업에 대한 사후 훈련을 통한 빠른 적응——을 통해 DexVLA는 효율적인 훈련을 달성한다. 실험은 단일 팔, 이중 팔, 및 손재주 손과 같은 다양한 본체를 포괄하며, 작업별 조정 없이 적응성, 제한된 데이터로 새로운 본체의 손재주 기술 학습 능력, 그리고 언어 명령만으로 복잡한 장기 작업(예: 옷 접기)을 수행할 수 있는 잠재력을 보여준다.

## 핵심 내용
### 방법 아키텍처
- **플러그형 확산 동작 전문가**: VLA 모델과 협력하여 독립 모듈로 작동하는 10억 파라미터 확산 모델. 이 전문가는 교차-본체 데이터에서 사전 훈련되어 일반적인 동작 사전을 학습하며, 다양한 VLA 아키텍처에 삽입될 수 있다.
- **3단계 커리큘럼 학습 전략**:
  1. **사전 훈련 단계**: 단일 팔, 이중 팔, 손재주 손 등 다양한 본체를 포함한 데이터에서 확산 동작 전문가를 사전 훈련하여 교차-본체 동작 분포를 습득하게 한다.
  2. **정렬 단계**: 사전 훈련된 확산 전문가를 VLA 모델(예: LLM 기반 시각-언어 모델)과 정렬하고, 특정 본체의 동작 공간에 맞춰 미세 조정한다.
  3. **사후 훈련 단계**: 소량의 새로운 작업 데이터를 통해 모델 파라미터를 빠르게 조정하여 새로운 작업에 대한 제로샷 또는 퓨샷 적응을 실현한다.

### 실험 설정
- **본체 유형**: 단일 팔(예: Franka Emika Panda), 이중 팔(예: Baxter), 손재주 손(예: Allegro Hand).
- **작업 유형**: 물체 잡기, 도구 사용, 옷 접기 등 장기적 복잡 작업 포함.
- **비교 모델**: Octo, OpenVLA, Diffusion Policy.

### 주요 결과
- **교차-본체 일반화**: 작업별 조정 없이 DexVLA는 단일 팔, 이중 팔, 및 손재주 손 작업에서 각각 85%, 78%, 72%의 성공률을 달성하며, Octo(62%, 55%, 48%) 및 OpenVLA(68%, 60%, 52%)보다 크게 우수하다.
- **손재주 기술 학습**: 손재주 손 작업에서 50개의 데모 데이터만 사용하여 DexVLA는 복잡한 잡기 전략을 학습할 수 있으며, 성공률이 Diffusion Policy보다 15% 높다.
- **장기 작업**: 옷 접기 작업에서 DexVLA는 직접적인 언어 명령(예: "셔츠를 반으로 접어")을 통해 전체 프로세스를 완료하며 성공률이 70%인 반면, OpenVLA는 45%에 불과하다.
- **훈련 효율성**: 3단계 전략은 총 훈련 시간을 40% 줄이면서도 엔드투엔드 훈련과 동등한 일반화 성능을 유지한다.

### 결론
DexVLA는 플러그형 확산 전문가와 커리큘럼 학습 전략을 통해 VLA 모델의 동작 표현 및 훈련 효율성 병목 현상을 효과적으로 해결한다. 실험은 교차-본체, 손재주 기술, 및 장기 작업에서의 우수성을 입증하며, 범용 로봇 제어를 위한 효율적이고 확장 가능한 프레임워크를 제공한다.
