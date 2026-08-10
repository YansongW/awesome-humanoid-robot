---
$id: ent_paper_zhang_4d_vla_spatiotemporal_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration'
  zh: 4D-VLA
  ko: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration'
summary:
  en: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (4D-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, HUAWEI Noah''s Ark Lab, and published at NIPS25.'
  zh: 4D-VLA 是复旦大学与华为诺亚方舟实验室联合提出的 2025 年大型视觉-语言-动作模型，发表于 NIPS25。其核心贡献在于通过引入深度与时间信息，解决机器人数据预训练中的坐标系统混乱与状态混乱问题，并显著提升操作成功率。
  ko: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (4D-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, HUAWEI Noah''s Ark Lab, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 4d_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.22242v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (867 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (arXiv)'
  url: https://arxiv.org/abs/2506.22242
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 4D-VLA source
  url: https://doi.org/10.48550/arXiv.2506.22242
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有方法通常仅依赖简单观测作为输入来建模动作分布，但输入信息不完整导致条件动作分布分散，表现为坐标系统混乱与状态混乱，严重阻碍预训练效率。4D-VLA 通过将 4D 信息（深度与时间）整合到视觉特征中，利用序列 RGB-D 输入对齐机器人坐标系与场景坐标系，从而赋予模型强大的时空推理能力，同时保持低训练开销。此外，模型引入记忆库采样策略，从历史图像中提取信息帧以提升效率与效果。实验表明，4D-VLA 在模拟与真实场景中均显著超越 OpenVLA，并在新提出的多视角基准 MV-Bench 上展现出更强的空间感知与泛化能力。

## 核心内容
### 方法概述
4D-VLA 的核心思路是将 4D 信息（深度与时间）作为输入，以缓解预训练中的两类混乱：
- **坐标系统混乱**：不同数据集中的机器人坐标系与场景坐标系不一致，导致模型难以对齐动作与观测。
- **状态混乱**：观测信息不完整（如缺乏深度或时序上下文），使得同一动作对应多种可能状态。

### 架构设计
- **输入处理**：采用序列 RGB-D 图像作为输入，通过深度信息增强视觉特征，并利用时间维度捕捉动态变化。
- **对齐机制**：模型自动学习将机器人坐标系与场景坐标系对齐，无需显式标定，从而减少训练开销。
- **记忆库采样**：一种帧采样策略，从历史图像中筛选信息量最大的帧，避免冗余数据，提升训练效率。

### 实验设置与结果
- **基准对比**：在模拟与真实机器人操作任务中，4D-VLA 的成功率相比 OpenVLA 显著提升（具体数字未在正文中给出，但强调“显著增加”）。
- **新基准 MV-Bench**：为评估空间感知与视角泛化能力，作者提出多视角仿真基准 MV-Bench。4D-VLA 在此基准上持续优于现有方法，证明其更强的空间理解与适应性。

### 结论
4D-VLA 通过引入 4D 信息与记忆库采样，有效解决了机器人数据预训练中的输入不完整问题，在多个场景下实现了性能突破，尤其在新视角泛化方面表现突出。

## Overview
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution-an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## Overview
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution—an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## Content
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution—an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## 参考
- http://arxiv.org/abs/2506.22242v2

## 개요
기존 방법들은 일반적으로 단순 관측만을 입력으로 사용하여 동작 분포를 모델링하지만, 입력 정보의 불완전성으로 인해 조건부 동작 분포가 분산되어 좌표계 혼란과 상태 혼란으로 나타나며, 이는 사전 학습 효율을 심각하게 저해합니다. 4D-VLA는 4D 정보(깊이와 시간)를 시각적 특징에 통합하고, 시퀀스 RGB-D 입력을 활용하여 로봇 좌표계와 장면 좌표계를 정렬함으로써 모델에 강력한 시공간 추론 능력을 부여하면서도 낮은 훈련 비용을 유지합니다. 또한, 모델은 메모리 뱅크 샘플링 전략을 도입하여 과거 이미지에서 정보성 높은 프레임을 추출함으로써 효율성과 효과를 향상시킵니다. 실험 결과, 4D-VLA는 시뮬레이션과 실제 환경 모두에서 OpenVLA를 크게 능가하며, 새로 제안된 다중 시점 벤치마크 MV-Bench에서 더 강력한 공간 인식과 일반화 능력을 보여줍니다.

## 핵심 내용
### 방법 개요
4D-VLA의 핵심 아이디어는 4D 정보(깊이와 시간)를 입력으로 사용하여 사전 학습 중 발생하는 두 가지 혼란을 완화하는 것입니다:
- **좌표계 혼란**: 서로 다른 데이터셋에서 로봇 좌표계와 장면 좌표계가 일치하지 않아 모델이 동작과 관측을 정렬하기 어렵게 만듭니다.
- **상태 혼란**: 관측 정보가 불완전하여(예: 깊이 또는 시간적 맥락 부족) 동일한 동작이 여러 가능한 상태에 대응하게 됩니다.

### 아키텍처 설계
- **입력 처리**: 시퀀스 RGB-D 이미지를 입력으로 사용하며, 깊이 정보를 통해 시각적 특징을 강화하고 시간 차원을 활용하여 동적 변화를 포착합니다.
- **정렬 메커니즘**: 모델은 명시적 캘리브레이션 없이 로봇 좌표계와 장면 좌표계를 자동으로 정렬하는 방법을 학습하여 훈련 비용을 줄입니다.
- **메모리 뱅크 샘플링**: 과거 이미지에서 정보량이 가장 큰 프레임을 선별하는 프레임 샘플링 전략으로, 중복 데이터를 피하고 훈련 효율을 높입니다.

### 실험 설정 및 결과
- **벤치마크 비교**: 시뮬레이션 및 실제 로봇 조작 작업에서 4D-VLA의 성공률은 OpenVLA 대비 크게 향상되었습니다(구체적인 수치는 본문에 제시되지 않았지만 "현저한 증가"가 강조됨).
- **새 벤치마크 MV-Bench**: 공간 인식과 시점 일반화 능력을 평가하기 위해 저자들은 다중 시점 시뮬레이션 벤치마크 MV-Bench를 제안했습니다. 4D-VLA는 이 벤치마크에서 지속적으로 기존 방법을 능가하여 더 강력한 공간 이해와 적응성을 입증합니다.

### 결론
4D-VLA는 4D 정보와 메모리 뱅크 샘플링을 도입하여 로봇 데이터 사전 학습에서의 입력 불완전성 문제를 효과적으로 해결했으며, 여러 환경에서 성능 돌파구를 마련했고 특히 새로운 시점 일반화에서 두드러진 성과를 보여줍니다.
