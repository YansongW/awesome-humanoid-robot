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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22134v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (923 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.22134v1

## 개요
DualVLA는 범용 VLA 모델이 미세 조정 후 동작 성능이 저하되는 문제를 해결하기 위해, 추론과 동작을 부분적으로 분리하는 아키텍처를 제안합니다. 이 방법은 먼저 이중 계층 데이터 정리를 통해 중복된 임베디드 추론을 제거하여 동작 학습에 부정적인 영향을 방지하고, 이후 이중 교사 적응형 증류 전략을 설계하여 서로 다른 데이터 도메인에 서로 다른 감독 신호를 할당하면서 추론 능력을 유지합니다. 범용 VLA 평가의 공백을 메우기 위해 연구팀은 VLA Score도 제안하여 VLA 능력을 추론, 의도, 동작, 정렬의 네 가지 차원으로 분리하여 세밀하게 평가합니다. 실험 결과, DualVLA는 SimplerEnv에서 평균 성공률 61.0을 달성했고, 여덟 개의 멀티모달 벤치마크에서 평균 점수 65.4를 기록하여 정밀한 동작 실행과 멀티모달 이해 사이의 더 강한 균형을 실현했습니다.

## 핵심 내용
### 방법 개요
DualVLA의 핵심 혁신은 추론과 동작을 부분적으로 분리하여 범용 VLA 모델이 미세 조정 후 동작 성능이 저하되는 문제를 해결하는 것입니다. 구체적인 방법은 다음과 같습니다:
- **이중 계층 데이터 정리**: 먼저 중복된 임베디드 추론 데이터를 제거하여 동작 학습에 부정적인 영향을 방지합니다.
- **이중 교사 적응형 증류**: 서로 다른 데이터 도메인에 서로 다른 감독 신호를 할당하면서 추론 능력을 유지합니다.

### 아키텍처 설계
DualVLA는 시각-언어-동작(VLA) 아키텍처를 채택하여 추론과 동작을 부분적으로 분리함으로써 정밀한 동작 실행과 멀티모달 이해 사이의 균형을 실현합니다. 모델은 로봇 시연 데이터에서 훈련되어 신뢰할 수 있는 조작 기술을 획득한 후, 혼합 주석이 달린 로봇 데이터와 멀티모달 데이터를 결합하여 더 넓은 추론 능력을 회복합니다.

### 실험 설정
- **벤치마크 테스트**: SimplerEnv와 여덟 개의 멀티모달 벤치마크에서 평가를 수행합니다.
- **평가 지표**: VLA Score는 VLA 능력을 추론, 의도, 동작, 정렬의 네 가지 차원으로 분리하여 세밀하게 평가합니다.

### 주요 결과
- **SimplerEnv**: 평균 성공률 61.0을 달성했습니다.
- **멀티모달 벤치마크**: 여덟 개의 경쟁력 있는 멀티모달 벤치마크에서 평균 점수 65.4를 기록했습니다.
- **성능 비교**: DualVLA는 동작 실행 정밀도와 멀티모달 이해 사이에서 더 강한 균형을 실현하여 미세 조정 전 기본 모델보다 우수합니다.

### 결론
DualVLA는 추론과 동작을 부분적으로 분리함으로써 범용 VLA 모델의 동작 저하 문제를 효과적으로 해결하고 여러 벤치마크에서 우수한 성능을 달성했습니다. 프로젝트 웹사이트에서 더 많은 세부 정보를 확인할 수 있습니다: https://costaliya.github.io/DualVLA/.
