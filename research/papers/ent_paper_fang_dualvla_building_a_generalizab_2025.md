---
$id: ent_paper_fang_dualvla_building_a_generalizab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action'
  zh: DualVLA
  ko: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action'
summary:
  en: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (DualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by MoE Key Laboratory of Brain-inspired Intelligent
    Perception and Cognition, University of Science and Technology of China, State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, CUHK.'
  zh: DualVLA 是由中国科学技术大学、北京大学和香港中文大学联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于通过部分解耦推理与动作，解决了通用 VLA 模型在微调后动作性能退化的问题，并提出了 VLA
    Score 评估框架。实验表明，DualVLA 在 SimplerEnv 中平均成功率达 61.0，在八个多模态基准上平均得分 65.4。
  ko: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (DualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by MoE Key Laboratory of Brain-inspired Intelligent
    Perception and Cognition, University of Science and Technology of China, State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, CUHK.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dualvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22134v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (arXiv)'
  url: https://arxiv.org/abs/2511.22134
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DualVLA source
  url: https://doi.org/10.48550/arXiv.2511.22134
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DualVLA 针对通用 VLA 模型在微调后动作性能退化的问题，提出了一种部分解耦推理与动作的架构。该方法首先通过双层数据剪枝去除冗余的具身推理，防止其对动作学习产生负面影响；随后设计双教师自适应蒸馏策略，为不同数据域分配不同的监督信号，同时保持推理能力。为填补通用 VLA 评估的空白，研究团队还提出了 VLA Score，将 VLA 能力解耦为推理、意图、动作和对齐四个维度进行细粒度评估。实验结果显示，DualVLA 在 SimplerEnv 中平均成功率达 61.0，在八个多模态基准上平均得分 65.4，实现了精确动作执行与多模态理解之间的更强平衡。

## 核心内容
### 方法概述
DualVLA 的核心创新在于部分解耦推理与动作，以解决通用 VLA 模型在微调后动作性能退化的问题。具体方法包括：
- **双层数据剪枝**：首先去除冗余的具身推理数据，防止其对动作学习产生负面影响。
- **双教师自适应蒸馏**：为不同数据域分配不同的监督信号，同时保持推理能力。

### 架构设计
DualVLA 采用视觉-语言-动作（VLA）架构，通过部分解耦推理与动作，实现精确动作执行与多模态理解之间的平衡。模型在机器人演示数据上训练，获得可靠的操作技能，随后结合混合标注的机器人数据和多模态数据，恢复更广泛的推理能力。

### 实验设置
- **基准测试**：在 SimplerEnv 和八个多模态基准上进行评估。
- **评估指标**：VLA Score 将 VLA 能力解耦为推理、意图、动作和对齐四个维度，进行细粒度评估。

### 关键结果
- **SimplerEnv**：平均成功率达 61.0。
- **多模态基准**：在八个竞争性多模态基准上平均得分 65.4。
- **性能对比**：DualVLA 在动作执行精度和多模态理解之间实现了更强的平衡，优于微调前的基础模型。

### 结论
DualVLA 通过部分解耦推理与动作，有效解决了通用 VLA 模型的动作退化问题，并在多个基准上取得了优异性能。项目网站提供更多细节：https://costaliya.github.io/DualVLA/。

## Overview
To build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, a common strategy is to first train a specialist VLA on robot demonstrations to acquire reliable manipulation skills, and then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, we observe that the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon we refer to as action degeneration. To address this issue, we propose DualVLA, which enhances action performance through carefully designed post-training while still preserving reasoning capability. We first introduce a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. To further strengthen action generation, we design a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability. To fill the evaluation gap for generalist VLAs, we also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding. Project Website: https://costaliya.github.io/DualVLA/.

## 개요
강력한 추론 능력을 갖춘 일반화 가능한 Vision-Language-Action (VLA) 모델을 구축하기 위한 일반적인 전략은 먼저 로봇 시연 데이터를 통해 전문가 VLA를 학습시켜 신뢰할 수 있는 조작 기술을 습득한 후, 혼합된 주석 처리된 로봇 데이터와 멀티모달 데이터를 함께 통합하여 더 넓은 추론 능력을 복원하는 것입니다. 그러나 우리는 결과적으로 얻어진 추론 VLA가 미세 조정 전의 전문가 모델에 비해 종종 저하된 행동 성능을 보인다는 점을 관찰했으며, 이를 행동 퇴화(action degeneration) 현상이라고 부릅니다. 이 문제를 해결하기 위해 우리는 DualVLA를 제안합니다. DualVLA는 추론 능력을 유지하면서도 신중하게 설계된 사후 학습(post-training)을 통해 행동 성능을 향상시킵니다. 먼저, 중복된 체화된 추론(embodied reasoning)을 제거하여 행동 학습에 부정적인 영향을 미치지 않도록 하는 이중 계층 데이터 정리(dual-layer data pruning) 방법을 도입합니다. 행동 생성을 더욱 강화하기 위해, 우리는 추론 능력을 유지하면서도 서로 다른 데이터 도메인에 다른 감독 신호를 할당하는 이중 교사 적응형 증류(dual-teacher adaptive distillation) 전략을 설계합니다. 일반주의 VLA에 대한 평가 격차를 해소하기 위해, 우리는 VLA Score도 제안합니다. 이는 VLA 능력을 추론, 의도, 행동 및 정렬 차원으로 분리하여 더 세분화된 평가를 가능하게 합니다. 실험 결과, DualVLA는 SimplerEnv에서 평균 성공률 61.0을 달성하고, 8개의 경쟁력 있는 멀티모달 벤치마크에서 평균 점수 65.4를 기록하여 정밀한 행동 실행과 멀티모달 이해 간의 더 강력한 균형을 보여줍니다. 프로젝트 웹사이트: https://costaliya.github.io/DualVLA/.

## 핵심 내용
강력한 추론 능력을 갖춘 일반화 가능한 Vision-Language-Action (VLA) 모델을 구축하기 위한 일반적인 전략은 먼저 로봇 시연 데이터를 통해 전문가 VLA를 학습시켜 신뢰할 수 있는 조작 기술을 습득한 후, 혼합된 주석 처리된 로봇 데이터와 멀티모달 데이터를 함께 통합하여 더 넓은 추론 능력을 복원하는 것입니다. 그러나 우리는 결과적으로 얻어진 추론 VLA가 미세 조정 전의 전문가 모델에 비해 종종 저하된 행동 성능을 보인다는 점을 관찰했으며, 이를 행동 퇴화(action degeneration) 현상이라고 부릅니다. 이 문제를 해결하기 위해 우리는 DualVLA를 제안합니다. DualVLA는 추론 능력을 유지하면서도 신중하게 설계된 사후 학습(post-training)을 통해 행동 성능을 향상시킵니다. 먼저, 중복된 체화된 추론(embodied reasoning)을 제거하여 행동 학습에 부정적인 영향을 미치지 않도록 하는 이중 계층 데이터 정리(dual-layer data pruning) 방법을 도입합니다. 행동 생성을 더욱 강화하기 위해, 우리는 추론 능력을 유지하면서도 서로 다른 데이터 도메인에 다른 감독 신호를 할당하는 이중 교사 적응형 증류(dual-teacher adaptive distillation) 전략을 설계합니다. 일반주의 VLA에 대한 평가 격차를 해소하기 위해, 우리는 VLA Score도 제안합니다. 이는 VLA 능력을 추론, 의도, 행동 및 정렬 차원으로 분리하여 더 세분화된 평가를 가능하게 합니다. 실험 결과, DualVLA는 SimplerEnv에서 평균 성공률 61.0을 달성하고, 8개의 경쟁력 있는 멀티모달 벤치마크에서 평균 점수 65.4를 기록하여 정밀한 행동 실행과 멀티모달 이해 간의 더 강력한 균형을 보여줍니다. 프로젝트 웹사이트: https://costaliya.github.io/DualVLA/.

## 参考
- http://arxiv.org/abs/2511.22134v1
