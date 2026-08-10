---
$id: ent_paper_luo_being_h0_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos'
  zh: Being-H0
  ko: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos'
summary:
  en: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Being-H0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Renmin University of China, BeingBeyond.'
  zh: Being-H0 是北京大学、中国人民大学与 BeingBeyond 于 2025 年提出的灵巧视觉-语言-动作模型（VLA），通过大规模人类视频预训练解决机器人操作中的数据瓶颈。其核心贡献在于物理指令调优范式与部件级运动标记化方法，实现了毫米级重建精度，并在真实机器人操作中展现出优异的指令跟随与泛化能力。
  ko: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Being-H0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Renmin University of China, BeingBeyond.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- being_h0
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.15597v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (786 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (arXiv)'
  url: https://arxiv.org/abs/2507.15597
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Being-H0 source
  url: https://doi.org/10.48550/arXiv.2507.15597
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型因依赖合成数据或遥操作演示，在复杂灵巧操作与跨场景泛化上表现不佳。Being-H0 创新性地将人类手部作为基础操作器，利用网络视频中丰富的灵巧性与可扩展性进行预训练。该模型通过物理指令调优三阶段流程（大规模人类视频预训练、物理空间对齐实现 3D 推理、后训练适配机器人任务），结合部件级运动标记化方法（毫米级重建精度），并构建了融合动捕、VR 与 RGB 视频的百万级运动指令数据集。实验表明，该模型在手部运动生成与指令跟随上表现优异，且随模型与数据规模提升而扩展，物理指令调优在真实机器人操作中带来预期增益。

## 核心内容
### 方法架构
- **物理指令调优**：三阶段训练范式
  - 阶段一：从大规模人类视频进行 VLA 预训练
  - 阶段二：物理空间对齐，实现 3D 推理能力
  - 阶段三：后训练适配，针对机器人任务进行微调
- **部件级运动标记化**：将手部运动分解为部件级 token，实现毫米级重建精度，用于建模精确手部轨迹以支持动作学习

### 数据构建
- 开发综合数据整理流水线，整合异构数据源：
  - 运动捕捉数据
  - VR 交互数据
  - RGB 视频数据
- 最终形成包含数百万运动指令实例的大规模数据集

### 实验设置与关键结果
- **手部运动生成**：在指令跟随任务中表现优异
- **模型扩展性**：随模型参数与数据规模增加，性能持续提升
- **真实机器人操作**：应用物理指令调优后，在真实操作任务中观察到预期增益
- **关键数字**：部件级运动标记化实现毫米级重建精度；数据集包含数百万运动指令实例

### 结论
Being-H0 通过利用人类视频的灵巧性与可扩展性，结合物理指令调优范式，有效解决了 VLA 模型的数据瓶颈问题，在复杂灵巧操作与跨场景泛化上取得突破。

## Overview
We introduce Being-H0, a dexterous Vision-Language-Action model (VLA) trained on large-scale human videos. Existing VLAs struggle with complex manipulation tasks requiring high dexterity and generalize poorly to novel scenarios and tasks, primarily due to their reliance on synthetic data with significant sim-to-real gaps or teleoperated demonstrations lacking scale and diversity. To address this data bottleneck, we propose leveraging human hands as a foundation manipulator, capitalizing on the rich dexterity and scalability present in web data. Our approach centers on physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, physical space alignment for 3D reasoning, and post-training adaptation for robotic tasks. Additionally, we introduce a part-level motion tokenization method which achieves millimeter-level reconstruction accuracy to model precise hand trajectories for action learning. To support our proposed paradigm, we further develop a comprehensive data curation pipeline that integrates heterogeneous sources -- including motion capture, VR, and RGB-only videos -- into a large-scale dataset with millions of motion-based instructional instances. We empirically show the excellence of Being-H0 in hand motion generation and instruction following, and it also scales well with model and data sizes. Importantly, we observe the expected gains of Being-H0 in real-world robotic manipulation as physical instruction tuning is applied. More details are available at https://beingbeyond.github.io/Being-H0.

## 参考
- http://arxiv.org/abs/2507.15597v1

## 개요
기존 VLA 모델은 합성 데이터나 원격 조작 데모에 의존하여 복잡한 정교한 조작과 교차 장면 일반화에서 성능이 저조하다. Being-H0는 혁신적으로 인간의 손을 기본 조작기로 활용하여, 네트워크 비디오에서 풍부한 정교함과 확장성을 이용해 사전 학습을 수행한다. 이 모델은 물리적 명령 튜닝 3단계 프로세스(대규모 인간 비디오 사전 학습, 물리적 공간 정렬을 통한 3D 추론, 후속 훈련을 통한 로봇 작업 적응)를 통해, 부품 수준 운동 토큰화 방법(밀리미터 수준 재구성 정밀도)을 결합하고, 모션 캡처, VR 및 RGB 비디오를 통합한 백만 규모 운동 명령 데이터 세트를 구축한다. 실험 결과, 이 모델은 손 운동 생성과 명령 따르기에서 우수한 성능을 보이며, 모델 및 데이터 규모 증가에 따라 확장되고, 물리적 명령 튜닝은 실제 로봇 조작에서 기대되는 이득을 가져온다.

## 핵심 내용
### 방법 아키텍처
- **물리적 명령 튜닝**: 3단계 훈련 패러다임
  - 1단계: 대규모 인간 비디오에서 VLA 사전 학습
  - 2단계: 물리적 공간 정렬을 통한 3D 추론 능력 구현
  - 3단계: 후속 훈련 적응, 로봇 작업에 대한 미세 조정
- **부품 수준 운동 토큰화**: 손 운동을 부품 수준 토큰으로 분해하여 밀리미터 수준 재구성 정밀도를 달성하고, 정확한 손 궤적 모델링을 통해 동작 학습 지원

### 데이터 구축
- 이종 데이터 소스를 통합하는 종합 데이터 정리 파이프라인 개발:
  - 모션 캡처 데이터
  - VR 상호작용 데이터
  - RGB 비디오 데이터
- 최종적으로 수백만 개의 운동 명령 인스턴스를 포함하는 대규모 데이터 세트 형성

### 실험 설정 및 주요 결과
- **손 운동 생성**: 명령 따르기 작업에서 우수한 성능
- **모델 확장성**: 모델 매개변수 및 데이터 규모 증가에 따라 성능 지속 향상
- **실제 로봇 조작**: 물리적 명령 튜닝 적용 후, 실제 조작 작업에서 기대되는 이득 관찰
- **주요 수치**: 부품 수준 운동 토큰화가 밀리미터 수준 재구성 정밀도 달성; 데이터 세트에 수백만 개의 운동 명령 인스턴스 포함

### 결론
Being-H0는 인간 비디오의 정교함과 확장성을 활용하고 물리적 명령 튜닝 패러다임을 결합하여 VLA 모델의 데이터 병목 문제를 효과적으로 해결하고, 복잡한 정교한 조작과 교차 장면 일반화에서 돌파구를 마련한다.
