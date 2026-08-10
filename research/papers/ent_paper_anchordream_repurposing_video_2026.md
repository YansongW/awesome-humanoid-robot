---
$id: ent_paper_anchordream_repurposing_video_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
  zh: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
  ko: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
summary:
  en: 'arXiv:2512.11797v2 Announce Type: replace Abstract: The collection of large-scale and diverse robot demonstrations
    remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited
    diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing
    methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies
    that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model
    that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process
    on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments
    consistent with the robot''s kinematics. Starting from only a handful of human teleoperation demonstrations, our method
    scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show
    that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in
    simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative
    world models in robot motion provides a practical path toward scaling imitation learning.'
  zh: AnchorDream 是一种具身感知世界模型，由研究团队提出，用于将预训练的视频扩散模型重新用于机器人数据合成。其核心贡献在于通过将扩散过程锚定在机器人运动渲染上，生成与机器人运动学一致的高质量、多样化数据集，从而显著提升下游模仿学习策略的性能。
  ko: 'arXiv:2512.11797v2 Announce Type: replace Abstract: The collection of large-scale and diverse robot demonstrations
    remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited
    diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing
    methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies
    that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model
    that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process
    on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments
    consistent with the robot''s kinematics. Starting from only a handful of human teleoperation demonstrations, our method
    scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show
    that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in
    simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative
    world models in robot motion provides a practical path toward scaling imitation learning.'
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
- anchordream
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11797v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (865 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis (arXiv)'
  url: https://arxiv.org/abs/2512.11797
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
AnchorDream 解决了机器人模仿学习中数据采集成本高、模拟器多样性有限且存在 sim-to-real 差距的问题。该方法利用预训练的视频扩散模型，通过条件化扩散过程于机器人运动渲染，避免了生成不合理的运动，同时合成与机器人运动学一致的对象和环境。仅需少量人类遥操作演示，AnchorDream 就能将其扩展为大规模、多样化、高质量的数据集，无需显式环境建模。实验表明，生成的数据在模拟器基准测试中带来 36.4% 的相对性能提升，在真实世界研究中性能几乎翻倍。

## 核心内容
### 方法概述
AnchorDream 是一种具身感知世界模型，旨在重新利用预训练的视频扩散模型进行机器人数据合成。其核心思想是将扩散过程条件化于机器人运动渲染，从而锚定具身性，防止生成不合理的运动，同时合成与机器人运动学一致的对象和环境。

### 架构与流程
- **运动渲染条件化**：AnchorDream 将机器人运动渲染作为条件输入到扩散模型中，确保生成的视频帧与机器人的实际运动轨迹一致。
- **数据扩展**：从少量人类遥操作演示开始，该方法通过扩散过程生成大量多样化、高质量的数据集，无需显式环境建模。
- **无环境建模**：与现有方法不同，AnchorDream 不依赖显式的环境模型，而是通过扩散模型隐式学习环境与对象的分布。

### 实验设置与结果
- **模拟器基准测试**：在模拟器环境中，使用 AnchorDream 生成的数据训练的策略实现了 36.4% 的相对性能提升。
- **真实世界研究**：在真实机器人实验中，性能几乎翻倍，表明生成的数据在真实场景中具有高度实用性。
- **一致性改进**：实验显示，生成的数据在多个下游任务中均带来一致的策略学习改进，验证了方法的泛化能力。

### 结论
AnchorDream 通过将生成式世界模型锚定在机器人运动上，提供了一种实用的路径来扩展模仿学习。该方法不仅解决了数据稀缺问题，还显著提升了策略性能，为机器人数据合成领域提供了新的方向。

## Overview
The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

## 参考
- http://arxiv.org/abs/2512.11797v2

## 개요
AnchorDream은 로봇 모방 학습에서 데이터 수집 비용이 높고, 시뮬레이터의 다양성이 제한적이며 sim-to-real 격차가 존재하는 문제를 해결합니다. 이 방법은 사전 훈련된 비디오 확산 모델을 활용하여, 확산 과정을 로봇 운동 렌더링에 조건화함으로써 비현실적인 운동 생성을 방지하고, 로봇 운동학과 일치하는 객체와 환경을 합성합니다. 소량의 인간 원격 조작 데모만으로도 AnchorDream은 이를 대규모, 다양하고 고품질의 데이터셋으로 확장할 수 있으며, 명시적 환경 모델링이 필요 없습니다. 실험 결과, 생성된 데이터는 시뮬레이터 벤치마크에서 36.4%의 상대적 성능 향상을 가져왔고, 실제 세계 연구에서는 성능이 거의 두 배로 향상되었습니다.

## 핵심 내용
### 방법 개요
AnchorDream은 로봇 데이터 합성을 위해 사전 훈련된 비디오 확산 모델을 재활용하는 것을 목표로 하는 구현 인식 세계 모델입니다. 핵심 아이디어는 확산 과정을 로봇 운동 렌더링에 조건화하여 구현성을 고정하고, 비현실적인 운동 생성을 방지하면서 로봇 운동학과 일치하는 객체와 환경을 합성하는 것입니다.

### 아키텍처 및 흐름
- **운동 렌더링 조건화**: AnchorDream은 로봇 운동 렌더링을 확산 모델의 조건 입력으로 사용하여, 생성된 비디오 프레임이 로봇의 실제 운동 궤적과 일치하도록 보장합니다.
- **데이터 확장**: 소량의 인간 원격 조작 데모에서 시작하여, 이 방법은 확산 과정을 통해 대규모의 다양하고 고품질의 데이터셋을 생성하며, 명시적 환경 모델링이 필요 없습니다.
- **환경 모델링 없음**: 기존 방법과 달리 AnchorDream은 명시적 환경 모델에 의존하지 않고, 확산 모델을 통해 환경과 객체의 분포를 암시적으로 학습합니다.

### 실험 설정 및 결과
- **시뮬레이터 벤치마크**: 시뮬레이터 환경에서 AnchorDream으로 생성된 데이터로 훈련된 정책은 36.4%의 상대적 성능 향상을 달성했습니다.
- **실제 세계 연구**: 실제 로봇 실험에서 성능이 거의 두 배로 향상되어, 생성된 데이터가 실제 시나리오에서 높은 실용성을 가짐을 보여줍니다.
- **일관성 개선**: 실험 결과, 생성된 데이터는 여러 하위 작업에서 일관된 정책 학습 개선을 가져와 방법의 일반화 능력을 검증했습니다.

### 결론
AnchorDream은 생성적 세계 모델을 로봇 운동에 고정함으로써 모방 학습을 확장하는 실용적인 경로를 제공합니다. 이 방법은 데이터 부족 문제를 해결할 뿐만 아니라 정책 성능을 크게 향상시켜, 로봇 데이터 합성 분야에 새로운 방향을 제시합니다.
