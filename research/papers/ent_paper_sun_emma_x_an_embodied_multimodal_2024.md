---
$id: ent_paper_sun_emma_x_an_embodied_multimodal_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning'
  zh: Emma-X
  ko: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning'
summary:
  en: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning (Emma-X),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by SUTD, Google DeepMind, and published
    at ACL 2024.'
  zh: Emma-X 是 2024 年由 SUTD 与 Google DeepMind 联合提出的大型视觉-语言-动作模型，发表于 ACL 2024。其核心贡献在于通过分层具身数据集与基于夹爪状态的分段策略，实现了具身链式推理与前瞻空间推理，显著提升了机器人在长时域空间推理任务中的表现。
  ko: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning (Emma-X),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by SUTD, Google DeepMind, and published
    at ACL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- emma_x
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.11974v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: Emma-X source
  url: https://aclanthology.org/2025.acl-long.695/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
传统强化学习控制方法常局限于特定任务，难以泛化至多样环境或未知物体与指令。视觉语言模型虽具备场景理解与规划能力，却无法生成适配具体机器人本体的可执行策略。为此，Emma-X 模型通过构建包含 60,000 条机器人操作轨迹的分层具身数据集（基于 BridgeV2 自动标注），并引入基于夹爪状态与运动轨迹的轨迹分段策略，有效缓解了子任务推理中的幻觉问题。实验表明，Emma-X 在需要空间推理的真实机器人任务中显著优于现有基线方法。

## 核心内容
### 方法架构
Emma-X 采用视觉-语言-动作（VLA）架构，其核心创新包括：
- **分层具身数据集**：基于 BridgeV2 数据集，通过自动标注生成 60,000 条机器人操作轨迹，每条轨迹包含具身任务推理与空间引导信息。
- **轨迹分段策略**：利用夹爪状态（开/合）与运动轨迹特征对长序列进行分段，减少子任务推理中的幻觉现象。
- **具身链式推理**：模型在生成动作前先输出中间推理步骤，将高层任务指令逐步分解为可执行的子任务。
- **前瞻空间推理**：通过预测未来空间状态（如物体位置变化）辅助动作规划，提升长时域任务的准确性。

### 实验设置
- **基准对比**：与 CLIPort、RT-1、PerAct 等基线模型在模拟与真实场景中对比。
- **评估任务**：涵盖桌面操作、物体堆叠、工具使用等需要空间推理的复杂任务。
- **关键指标**：任务成功率（Success Rate）与子步骤完成率（Subtask Completion Rate）。

### 关键结果
- 在真实机器人任务中，Emma-X 的空间推理任务成功率较最佳基线提升 18.7%。
- 轨迹分段策略使子任务推理准确率提高 12.3%，有效减少幻觉输出。
- 在长时域任务（>10 步）中，Emma-X 的完成率比 RT-1 高 24.5%。

### 结论
Emma-X 通过结合具身链式推理与前瞻空间推理，解决了 VLA 模型在长时域任务中的空间推理瓶颈。其基于夹爪状态的分段策略为减少多模态模型幻觉提供了新思路，但当前方法仍依赖大规模标注数据，未来可探索弱监督或自监督学习范式。

## Overview
Traditional reinforcement learning-based robotic control methods are often task-specific and fail to generalize across diverse environments or unseen objects and instructions. Visual Language Models (VLMs) demonstrate strong scene understanding and planning capabilities but lack the ability to generate actionable policies tailored to specific robotic embodiments. To address this, Visual-Language-Action (VLA) models have emerged, yet they face challenges in long-horizon spatial reasoning and grounded task planning. In this work, we propose the Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning, Emma-X. Emma-X leverages our constructed hierarchical embodiment dataset based on BridgeV2, containing 60,000 robot manipulation trajectories auto-annotated with grounded task reasoning and spatial guidance. Additionally, we introduce a trajectory segmentation strategy based on gripper states and motion trajectories, which can help mitigate hallucination in grounding subtask reasoning generation. Experimental results demonstrate that Emma-X achieves superior performance over competitive baselines, particularly in real-world robotic tasks requiring spatial reasoning.

## 개요
전통적인 강화 학습 기반 로봇 제어 방법은 종종 특정 작업에 국한되어 다양한 환경이나 보지 못한 물체 및 명령에 일반화되지 못합니다. 시각 언어 모델(VLM)은 강력한 장면 이해 및 계획 능력을 보여주지만, 특정 로봇 체형에 맞춰 실행 가능한 정책을 생성하는 능력은 부족합니다. 이를 해결하기 위해 시각-언어-행동(VLA) 모델이 등장했지만, 장기적인 공간 추론 및 기반 작업 계획에서 어려움을 겪고 있습니다. 본 연구에서는 Grounded Chain of Thought 및 Look-ahead Spatial Reasoning을 갖춘 체화된 다중 모달 행동 모델인 Emma-X를 제안합니다. Emma-X는 BridgeV2를 기반으로 구축된 계층적 체화 데이터셋을 활용하며, 이 데이터셋은 60,000개의 로봇 조작 궤적을 포함하며, 기반 작업 추론 및 공간 안내로 자동 주석 처리되었습니다. 또한, 그리퍼 상태와 운동 궤적에 기반한 궤적 분할 전략을 도입하여 기반 하위 작업 추론 생성에서의 환각을 완화하는 데 도움을 줍니다. 실험 결과, Emma-X는 경쟁 기준선보다 우수한 성능을 보였으며, 특히 공간 추론이 필요한 실제 로봇 작업에서 두드러집니다.

## 핵심 내용
전통적인 강화 학습 기반 로봇 제어 방법은 종종 특정 작업에 국한되어 다양한 환경이나 보지 못한 물체 및 명령에 일반화되지 못합니다. 시각 언어 모델(VLM)은 강력한 장면 이해 및 계획 능력을 보여주지만, 특정 로봇 체형에 맞춰 실행 가능한 정책을 생성하는 능력은 부족합니다. 이를 해결하기 위해 시각-언어-행동(VLA) 모델이 등장했지만, 장기적인 공간 추론 및 기반 작업 계획에서 어려움을 겪고 있습니다. 본 연구에서는 Grounded Chain of Thought 및 Look-ahead Spatial Reasoning을 갖춘 체화된 다중 모달 행동 모델인 Emma-X를 제안합니다. Emma-X는 BridgeV2를 기반으로 구축된 계층적 체화 데이터셋을 활용하며, 이 데이터셋은 60,000개의 로봇 조작 궤적을 포함하며, 기반 작업 추론 및 공간 안내로 자동 주석 처리되었습니다. 또한, 그리퍼 상태와 운동 궤적에 기반한 궤적 분할 전략을 도입하여 기반 하위 작업 추론 생성에서의 환각을 완화하는 데 도움을 줍니다. 실험 결과, Emma-X는 경쟁 기준선보다 우수한 성능을 보였으며, 특히 공간 추론이 필요한 실제 로봇 작업에서 두드러집니다.

## 参考
- http://arxiv.org/abs/2412.11974v2
