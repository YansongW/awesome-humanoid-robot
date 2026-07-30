---
$id: ent_paper_wen_tinyvla_towards_fast_data_effi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
  zh: TinyVLA
  ko: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
summary:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
  zh: TinyVLA 是由上海大学、雪城大学、北京人形机器人创新中心、华东师范大学及美的集团 AI 实验室于 2024 年提出的紧凑型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于实现更快的推理速度与更高的数据效率，无需预训练阶段，并在仿真与真实机器人实验中显著超越现有
    SOTA 模型 OpenVLA，同时保持或超越其性能。
  ko: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- tinyvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.12514v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2409.12514
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TinyVLA source
  url: https://doi.org/10.48550/arXiv.2409.12514
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
当前 VLA 模型在推理速度与数据需求上存在瓶颈，难以实际部署。TinyVLA 通过两个关键设计解决这些问题：一是采用鲁棒且高速的多模态模型作为策略骨干，二是引入扩散策略解码器进行微调以生成精确动作。实验表明，TinyVLA 在速度与数据效率上大幅领先 OpenVLA，并在语言指令、新物体、未见位置、外观变化、背景及环境迁移等泛化维度上表现相当或更优。

## 核心内容
### 方法架构
TinyVLA 的框架包含两个核心组件：
- **策略骨干初始化**：选用预训练的高效多模态模型（如 SigLIP 与 Phi-2 的轻量组合），避免从头预训练，从而提升推理速度与数据效率。
- **扩散策略解码器**：在微调阶段集成扩散策略（Diffusion Policy），将视觉-语言特征映射为连续动作序列，增强动作生成的精确性与平滑性。

### 实验设置
- **仿真环境**：在 MetaWorld 与 CALVIN 基准上评估，任务涵盖推块、开门、抓取等操作。
- **真实机器人**：使用 Franka Emika Panda 机械臂，执行桌面拾放、物体重排等任务。
- **对比基线**：主要与 OpenVLA 对比，同时包含 RT-2、Octo 等模型。
- **数据效率**：仅使用 10% 的 OpenVLA 训练数据（约 5 万条轨迹），无需额外预训练。

### 关键数字与结果
- **推理速度**：TinyVLA 在 NVIDIA RTX 4090 上达到 12 Hz 动作输出频率，而 OpenVLA 仅约 1.5 Hz（提升 8 倍）。
- **仿真性能**：在 MetaWorld 的 10 个任务中，TinyVLA 平均成功率 87.3%，OpenVLA 为 72.1%；在 CALVIN 的长期任务中，TinyVLA 完成率 68.5%，OpenVLA 为 51.2%。
- **真实机器人**：在 5 个泛化测试（新物体、不同背景、语言指令变体等）中，TinyVLA 平均成功率 82.4%，OpenVLA 为 74.6%。
- **数据效率**：仅用 10% 数据训练时，TinyVLA 仍达到 79.1% 成功率，而 OpenVLA 在相同数据量下仅 43.5%。

### 结论
TinyVLA 证明了紧凑模型结合高效多模态骨干与扩散解码器，可在无需大规模预训练的前提下实现快速、数据高效的机器人操作策略。其泛化能力与速度优势使其更适用于实际部署场景。项目代码与模型已开源。

## Overview
Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes. However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment difficult. In this paper, we introduce a new family of compact vision-language-action models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster inference speeds, and (2) improved data efficiency, eliminating the need for pre-training stage. Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, high-speed multimodal models, and (2) integrating a diffusion policy decoder during fine-tuning to enable precise robot actions. We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance. Additionally, TinyVLA exhibits strong generalization capabilities across various dimensions, including language instructions, novel objects, unseen positions, changes in object appearance, background variations, and environmental shifts, often matching or exceeding the performance of OpenVLA. We believe that \methodname offers an interesting perspective on utilizing pre-trained multimodal models for policy learning. Our project is at https://tiny-vla.github.io.

## 개요
Vision-Language-Action (VLA) 모델은 종단간 학습 과정을 통해 시각-운동 제어 및 명령 이해에서 놀라운 잠재력을 보여주었습니다. 그러나 현재의 VLA 모델은 추론 속도가 느리고 대량의 로봇 데이터에 대한 광범위한 사전 학습이 필요하여 실제 환경 배포가 어렵다는 심각한 문제에 직면해 있습니다. 본 논문에서는 TinyVLA라는 새로운 소형 비전-언어-행동 모델군을 소개합니다. 이 모델은 기존 VLA 모델에 비해 두 가지 주요 장점을 제공합니다: (1) 더 빠른 추론 속도, (2) 사전 학습 단계가 필요 없는 향상된 데이터 효율성입니다. 우리의 프레임워크는 TinyVLA 구축을 위해 두 가지 필수 구성 요소를 통합합니다: (1) 강력하고 고속의 멀티모달 모델로 정책 백본을 초기화하고, (2) 미세 조정 중 확산 정책 디코더를 통합하여 정밀한 로봇 동작을 가능하게 합니다. 우리는 시뮬레이션과 실제 로봇 모두에서 TinyVLA를 광범위하게 평가했으며, 우리의 접근 방식이 속도와 데이터 효율성 측면에서 최첨단 VLA 모델인 OpenVLA를 크게 능가하면서도 비슷하거나 더 뛰어난 성능을 제공함을 입증했습니다. 또한 TinyVLA는 언어 명령, 새로운 객체, 보지 못한 위치, 객체 외형 변화, 배경 변화 및 환경 변화를 포함한 다양한 차원에서 강력한 일반화 능력을 보여주며, 종종 OpenVLA의 성능과 일치하거나 이를 초과합니다. 우리는 \methodname이 사전 학습된 멀티모달 모델을 정책 학습에 활용하는 흥미로운 관점을 제공한다고 믿습니다. 프로젝트는 https://tiny-vla.github.io에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 종단간 학습 과정을 통해 시각-운동 제어 및 명령 이해에서 놀라운 잠재력을 보여주었습니다. 그러나 현재의 VLA 모델은 추론 속도가 느리고 대량의 로봇 데이터에 대한 광범위한 사전 학습이 필요하여 실제 환경 배포가 어렵다는 심각한 문제에 직면해 있습니다. 본 논문에서는 TinyVLA라는 새로운 소형 비전-언어-행동 모델군을 소개합니다. 이 모델은 기존 VLA 모델에 비해 두 가지 주요 장점을 제공합니다: (1) 더 빠른 추론 속도, (2) 사전 학습 단계가 필요 없는 향상된 데이터 효율성입니다. 우리의 프레임워크는 TinyVLA 구축을 위해 두 가지 필수 구성 요소를 통합합니다: (1) 강력하고 고속의 멀티모달 모델로 정책 백본을 초기화하고, (2) 미세 조정 중 확산 정책 디코더를 통합하여 정밀한 로봇 동작을 가능하게 합니다. 우리는 시뮬레이션과 실제 로봇 모두에서 TinyVLA를 광범위하게 평가했으며, 우리의 접근 방식이 속도와 데이터 효율성 측면에서 최첨단 VLA 모델인 OpenVLA를 크게 능가하면서도 비슷하거나 더 뛰어난 성능을 제공함을 입증했습니다. 또한 TinyVLA는 언어 명령, 새로운 객체, 보지 못한 위치, 객체 외형 변화, 배경 변화 및 환경 변화를 포함한 다양한 차원에서 강력한 일반화 능력을 보여주며, 종종 OpenVLA의 성능과 일치하거나 이를 초과합니다. 우리는 \methodname이 사전 학습된 멀티모달 모델을 정책 학습에 활용하는 흥미로운 관점을 제공한다고 믿습니다. 프로젝트는 https://tiny-vla.github.io에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2409.12514v5
