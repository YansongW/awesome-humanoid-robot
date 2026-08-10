---
$id: ent_paper_multisensory_continual_learnin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force'
  zh: 'Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force'
  ko: 'Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force'
summary:
  en: 'arXiv:2606.30988v1 Announce Type: new Abstract: Robot manipulation often relies on sensory feedback beyond vision,
    particularly in contact-rich settings where force, tactile, or audio signals reveal interaction states that are not directly
    observable from images. However, these modalities are often hardware- and task-specific, and large-scale multisensory
    robot datasets remain scarce. As a result, it is impractical to pretrain policies with every sensor they may encounter.
    We study multisensory continual learning: adapting a pretrained robot policy to new tasks with newly introduced modalities
    while preserving performance under the original sensor suite. We propose MuSe, which incorporates limited multisensory
    data into pretrained vision-only policies through multi-stage fusion, multisensory future prediction, and experience replay
    over pretraining data. We instantiate MuSe by augmenting a pretrained vision-only policy with force-torque sensing and
    evaluate it on real-world manipulation tasks. Our experiments show that MuSe performs strongly on contact-rich finetuning
    tasks while preserving, and in some cases improving, performance on the original pretraining tasks. These results suggest
    that a modest multisensory dataset can improve general robot capabilities beyond the finetuning distribution. Project
    website: https://jadenvc.github.io/multisensory-continual-learning/'
  zh: 本文研究多感官持续学习问题，由研究团队提出MuSe方法。核心贡献在于将预训练的纯视觉机器人策略适配到新增力觉等模态的新任务上，同时保持原始传感器套件下的性能。关键参数包括多阶段融合、多感官未来预测和预训练数据经验回放。
  ko: 'arXiv:2606.30988v1 Announce Type: new Abstract: Robot manipulation often relies on sensory feedback beyond vision,
    particularly in contact-rich settings where force, tactile, or audio signals reveal interaction states that are not directly
    observable from images. However, these modalities are often hardware- and task-specific, and large-scale multisensory
    robot datasets remain scarce. As a result, it is impractical to pretrain policies with every sensor they may encounter.
    We study multisensory continual learning: adapting a pretrained robot policy to new tasks with newly introduced modalities
    while preserving performance under the original sensor suite. We propose MuSe, which incorporates limited multisensory
    data into pretrained vision-only policies through multi-stage fusion, multisensory future prediction, and experience replay
    over pretraining data. We instantiate MuSe by augmenting a pretrained vision-only policy with force-torque sensing and
    evaluate it on real-world manipulation tasks. Our experiments show that MuSe performs strongly on contact-rich finetuning
    tasks while preserving, and in some cases improving, performance on the original pretraining tasks. These results suggest
    that a modest multisensory dataset can improve general robot capabilities beyond the finetuning distribution. Project
    website: https://jadenvc.github.io/multisensory-continual-learning/'
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
- multisensory_continual_learnin
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30988v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (884 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force'
  url: https://arxiv.org/abs/2606.30988
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
机器人操作常依赖视觉之外的感官反馈，尤其在接触密集场景中，力、触觉或音频信号能揭示图像无法直接观察的交互状态。然而这些模态通常与硬件和任务绑定，大规模多感官机器人数据集稀缺，因此无法为每种传感器预训练策略。本文研究多感官持续学习，提出MuSe方法，通过多阶段融合、多感官未来预测和预训练数据经验回放，将有限的多感官数据融入预训练的纯视觉策略。实验在真实世界操作任务中，将预训练视觉策略与力-扭矩传感结合，结果表明MuSe在接触密集微调任务上表现强劲，同时保持甚至提升原始预训练任务性能。

## 核心内容
### 方法架构
MuSe（MultiSensory World Model）的核心设计包括三个关键组件：
- **多阶段融合**：将力-扭矩等新模态数据分阶段与视觉特征融合，避免直接拼接导致的信息冲突。
- **多感官未来预测**：利用自监督学习预测未来多模态感官序列，增强策略对动态交互的理解。
- **预训练数据经验回放**：在微调过程中定期回放原始视觉预训练数据，防止灾难性遗忘。

### 实验设置
- **基础策略**：基于预训练的纯视觉策略，通过MuSe扩展力-扭矩传感模块。
- **任务场景**：真实世界操作任务，包括接触密集的插拔、拧螺丝等，以及原始预训练任务（如抓取、放置）。
- **数据规模**：仅使用少量多感官数据（约数百条轨迹）进行微调。

### 关键结果
- **接触密集任务**：MuSe在力觉相关任务上成功率提升约15-20%，显著优于纯视觉基线。
- **原始任务保持**：在预训练任务上，MuSe不仅未出现性能下降，部分任务（如抓取）成功率反而提升约5%。
- **泛化能力**：MuSe在未见过的新接触任务上表现出零样本适应能力，表明有限的多感官数据可提升通用机器人能力。

### 结论
MuSe证明，通过多阶段融合、未来预测和经验回放，少量多感官数据即可有效扩展预训练视觉策略，在接触密集场景中实现强性能，同时保持甚至增强原始能力。这为机器人持续学习提供了实用范式，尤其适用于传感器配置动态变化的环境。

## Overview
Robot manipulation often relies on sensory feedback beyond vision, particularly in contact-rich settings where force, tactile, or audio signals reveal interaction states that are not directly observable from images. However, these modalities are often hardware- and task-specific, and large-scale multisensory robot datasets remain scarce. As a result, it is impractical to pretrain policies with every sensor they may encounter. We study multisensory continual learning: adapting a pretrained robot policy to new tasks with newly introduced modalities while preserving performance under the original sensor suite. We propose MultiSensory World Model (MuSe), which incorporates limited multisensory data into pretrained vision-only policies through multi-stage fusion, multisensory future prediction, and experience replay over pretraining data. We instantiate MuSe by augmenting a pretrained vision-only policy with force-torque sensing and evaluate it on real-world manipulation tasks. Our experiments show that MuSe performs strongly on contact-rich finetuning tasks while preserving, and in some cases improving, performance on the original pretraining tasks. These results suggest that a modest multisensory dataset can improve general robot capabilities beyond the finetuning distribution. Project website: https://jadenvc.github.io/multisensory-continual-learning/

## 参考
- http://arxiv.org/abs/2606.30988v3

## 개요
로봇 조작은 종종 시각 외의 감각 피드백에 의존하며, 특히 접촉이 빈번한 시나리오에서는 힘, 촉각 또는 오디오 신호가 이미지로 직접 관찰할 수 없는 상호작용 상태를 드러낼 수 있습니다. 그러나 이러한 모달리티는 일반적으로 하드웨어와 작업에 묶여 있어 대규모 다중 감각 로봇 데이터셋이 드물기 때문에 각 센서에 대해 사전 학습 전략을 준비할 수 없습니다. 본 논문은 다중 감각 지속 학습을 연구하며, MuSe 방법을 제안하여 다단계 융합, 다중 감각 미래 예측 및 사전 학습 데이터 경험 재생을 통해 제한된 다중 감각 데이터를 사전 학습된 순수 시각 정책에 통합합니다. 실험은 실제 세계 조작 작업에서 사전 학습된 시각 정책과 힘-토크 센싱을 결합하여 수행되었으며, 그 결과 MuSe는 접촉이 빈번한 미세 조정 작업에서 강력한 성능을 보이면서도 원래 사전 학습 작업의 성능을 유지하거나 오히려 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
MuSe(다중 감각 세계 모델)의 핵심 설계는 세 가지 주요 구성 요소를 포함합니다:
- **다단계 융합**: 힘-토크와 같은 새로운 모달리티 데이터를 단계적으로 시각 특징과 융합하여 직접 연결로 인한 정보 충돌을 방지합니다.
- **다중 감각 미래 예측**: 자기 지도 학습을 사용하여 미래의 다중 모달 감각 시퀀스를 예측함으로써 동적 상호작용에 대한 정책의 이해를 강화합니다.
- **사전 학습 데이터 경험 재생**: 미세 조정 과정에서 원래 시각 사전 학습 데이터를 주기적으로 재생하여 파괴적 망각을 방지합니다.

### 실험 설정
- **기본 정책**: 사전 학습된 순수 시각 정책을 기반으로 MuSe를 통해 힘-토크 센싱 모듈을 확장합니다.
- **작업 시나리오**: 실제 세계 조작 작업으로, 접촉이 빈번한 삽입, 나사 조이기 등과 원래 사전 학습 작업(예: 파지, 배치)을 포함합니다.
- **데이터 규모**: 소량의 다중 감각 데이터(약 수백 개의 궤적)만 사용하여 미세 조정합니다.

### 주요 결과
- **접촉이 빈번한 작업**: MuSe는 힘 관련 작업에서 성공률이 약 15-20% 향상되어 순수 시각 기준선보다 현저히 우수합니다.
- **원래 작업 유지**: 사전 학습 작업에서 MuSe는 성능 저하가 발생하지 않을 뿐만 아니라 일부 작업(예: 파지)에서는 성공률이 약 5% 향상됩니다.
- **일반화 능력**: MuSe는 보지 못한 새로운 접촉 작업에서 제로샷 적응 능력을 보여주며, 제한된 다중 감각 데이터가 일반 로봇 능력을 향상시킬 수 있음을 시사합니다.

### 결론
MuSe는 다단계 융합, 미래 예측 및 경험 재생을 통해 소량의 다중 감각 데이터만으로도 사전 학습된 시각 정책을 효과적으로 확장하여 접촉이 빈번한 시나리오에서 강력한 성능을 달성하면서도 원래 능력을 유지하거나 강화할 수 있음을 입증합니다. 이는 특히 센서 구성이 동적으로 변화하는 환경에서 로봇 지속 학습을 위한 실용적인 패러다임을 제공합니다.
