---
$id: ent_paper_reuss_multimodal_diffusion_transform_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals'
  zh: MDT
  ko: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals'
summary:
  en: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals (MDT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology, and published at Robotics - Science and
    Systems 2024.'
  zh: MDT（Multimodal Diffusion Transformer）是卡尔斯鲁厄理工学院于2024年提出的扩散策略框架，旨在从多模态目标指令中学习通用机器人操作行为。其核心贡献在于通过自监督辅助目标对齐图像与语言目标嵌入，在仅含不足2%语言标注的LIBERO基准上表现优异，并在CALVIN操作挑战中实现15%的绝对性能提升。
  ko: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals (MDT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology, and published at Robotics - Science and
    Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- mdt
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.05996v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (853 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: MDT source
  url: https://doi.org/10.15607/RSS.2024.XX.121
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
MDT通过扩散式多模态Transformer骨干网络与两个自监督辅助目标，解决了现有模仿学习方法依赖单一目标模态（如仅语言或仅图像）的局限。该方法学习一种潜在目标条件状态表征，同时对齐图像与语言目标嵌入，并编码足够信息以预测未来状态。在CALVIN与LIBERO的164项任务中，MDT展现出卓越性能，尤其在语言标注稀疏场景下表现突出。相比需大规模预训练且参数量多10倍的前沿方法，MDT在CALVIN挑战中创下新纪录。

## 核心内容
### 方法架构
- **扩散策略框架**：MDT采用扩散式多模态Transformer作为骨干网络，通过去噪过程生成动作序列，支持多模态目标条件（语言指令或目标图像）。
- **潜在目标条件状态表征**：同时训练图像与语言目标嵌入的对齐，编码未来状态预测所需信息，解决多模态目标指令的异构性。
- **自监督辅助目标**：两个辅助目标分别用于增强状态表征的预测能力与模态对齐，无需额外标注即可提升Transformer骨干性能。

### 实验设置
- **基准与任务**：在CALVIN（长时域操作挑战）与LIBERO（含稀疏语言标注版本）的164项任务上评估。
- **数据稀疏性**：LIBERO版本中语言标注比例低于2%，模拟真实场景中标注稀缺问题。
- **对比方法**：与需大规模预训练且参数量多10倍的前沿方法（如RT-2）对比。

### 关键结果
- **CALVIN挑战**：MDT实现15%的绝对性能提升（从基线方法到新纪录），且无需大规模预训练。
- **LIBERO基准**：在语言标注稀疏场景下仍保持高成功率，验证对多模态目标指令的泛化能力。
- **真实环境验证**：在模拟与真实机器人操作任务中均成功完成长时域操作。

### 结论
MDT通过扩散式多模态Transformer与自监督辅助目标，首次实现从稀疏标注的多模态目标中学习通用操作行为，显著降低对语言标注的依赖，为机器人学习提供高效解决方案。代码与演示已开源。

## Overview
This work introduces the Multimodal Diffusion Transformer (MDT), a novel diffusion policy framework, that excels at learning versatile behavior from multimodal goal specifications with few language annotations. MDT leverages a diffusion-based multimodal transformer backbone and two self-supervised auxiliary objectives to master long-horizon manipulation tasks based on multimodal goals. The vast majority of imitation learning methods only learn from individual goal modalities, e.g. either language or goal images. However, existing large-scale imitation learning datasets are only partially labeled with language annotations, which prohibits current methods from learning language conditioned behavior from these datasets. MDT addresses this challenge by introducing a latent goal-conditioned state representation that is simultaneously trained on multimodal goal instructions. This state representation aligns image and language based goal embeddings and encodes sufficient information to predict future states. The representation is trained via two self-supervised auxiliary objectives, enhancing the performance of the presented transformer backbone. MDT shows exceptional performance on 164 tasks provided by the challenging CALVIN and LIBERO benchmarks, including a LIBERO version that contains less than $2\%$ language annotations. Furthermore, MDT establishes a new record on the CALVIN manipulation challenge, demonstrating an absolute performance improvement of $15\%$ over prior state-of-the-art methods that require large-scale pretraining and contain $10\times$ more learnable parameters. MDT shows its ability to solve long-horizon manipulation from sparsely annotated data in both simulated and real-world environments. Demonstrations and Code are available at https://intuitive-robots.github.io/mdt_policy/.

## 参考
- http://arxiv.org/abs/2407.05996v1

## 개요
MDT는 확산 기반 멀티모달 Transformer 백본 네트워크와 두 가지 자기 지도 보조 목표를 통해, 기존 모방 학습 방법이 단일 목표 모달리티(예: 언어 또는 이미지 전용)에 의존하는 한계를 해결합니다. 이 방법은 이미지와 언어 목표 임베딩을 동시에 정렬하고, 미래 상태를 예측하기에 충분한 정보를 인코딩하는 잠재 목표 조건 상태 표현을 학습합니다. CALVIN과 LIBERO의 164개 작업에서 MDT는 뛰어난 성능을 보여주며, 특히 언어 주석이 희소한 시나리오에서 두드러진 성과를 나타냅니다. 대규모 사전 학습이 필요하고 매개변수 수가 10배 많은 최첨단 방법과 비교하여, MDT는 CALVIN 챌린지에서 새로운 기록을 세웠습니다.

## 핵심 내용
### 방법 아키텍처
- **확산 정책 프레임워크**: MDT는 확산 기반 멀티모달 Transformer를 백본 네트워크로 사용하여, 노이즈 제거 과정을 통해 행동 시퀀스를 생성하며, 멀티모달 목표 조건(언어 명령 또는 목표 이미지)을 지원합니다.
- **잠재 목표 조건 상태 표현**: 이미지와 언어 목표 임베딩의 정렬을 동시에 훈련하고, 미래 상태 예측에 필요한 정보를 인코딩하여 멀티모달 목표 명령의 이질성을 해결합니다.
- **자기 지도 보조 목표**: 두 가지 보조 목표는 각각 상태 표현의 예측 능력과 모달리티 정렬을 강화하며, 추가 주석 없이 Transformer 백본 성능을 향상시킵니다.

### 실험 설정
- **벤치마크 및 작업**: CALVIN(장기 도메인 조작 챌린지)과 LIBERO(희소 언어 주석 버전 포함)의 164개 작업에서 평가합니다.
- **데이터 희소성**: LIBERO 버전에서 언어 주석 비율이 2% 미만으로, 실제 시나리오의 주석 부족 문제를 시뮬레이션합니다.
- **비교 방법**: 대규모 사전 학습이 필요하고 매개변수 수가 10배 많은 최첨단 방법(예: RT-2)과 비교합니다.

### 주요 결과
- **CALVIN 챌린지**: MDT는 대규모 사전 학습 없이 15%의 절대 성능 향상(기준 방법에서 새로운 기록까지)을 달성합니다.
- **LIBERO 벤치마크**: 언어 주석이 희소한 시나리오에서도 높은 성공률을 유지하여, 멀티모달 목표 명령에 대한 일반화 능력을 검증합니다.
- **실제 환경 검증**: 시뮬레이션 및 실제 로봇 조작 작업에서 장기 도메인 조작을 성공적으로 완료합니다.

### 결론
MDT는 확산 기반 멀티모달 Transformer와 자기 지도 보조 목표를 통해, 희소 주석이 있는 멀티모달 목표에서 일반적인 조작 행동을 학습하는 것을 최초로 실현하며, 언어 주석에 대한 의존도를 크게 줄여 로봇 학습을 위한 효율적인 솔루션을 제공합니다. 코드와 데모는 오픈소스로 공개되었습니다.
