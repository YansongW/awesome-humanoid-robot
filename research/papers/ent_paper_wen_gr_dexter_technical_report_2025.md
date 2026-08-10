---
$id: ent_paper_wen_gr_dexter_technical_report_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: GR-Dexter Technical Report
  zh: GR-Dexter
  ko: GR-Dexter Technical Report
summary:
  en: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
  zh: GR-Dexter 是字节跳动 Seed 团队于 2025 年提出的大型视觉-语言-动作模型，专为双臂灵巧手机器人操控设计。其核心贡献在于构建了硬件-模型-数据一体化框架，通过紧凑型 21 自由度机械手、直觉式遥操作数据采集系统及跨具身数据集训练策略，解决了高自由度灵巧手操控中的动作空间膨胀与数据采集成本问题。
  ko: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gr_dexter
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24210v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1217 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: GR-Dexter Technical Report (arXiv)
  url: https://arxiv.org/abs/2512.24210
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GR-Dexter source
  url: https://doi.org/10.48550/arXiv.2512.24210
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型虽能实现语言引导的长时序机器人操控，但大多局限于夹爪式末端执行器。GR-Dexter 针对双臂高自由度灵巧手机器人面临的三大挑战——动作空间指数级增长、手部与物体频繁遮挡、真实机器人数据采集成本高昂——提出了系统性解决方案。该框架包含三个核心组件：专为灵巧操控设计的 21 自由度紧凑型机械手、支持直观双臂操作的遥操作数据采集系统，以及融合遥操作轨迹、大规模视觉语言数据与精心筛选的跨具身数据集的训练方案。在涵盖长时序日常操作与可泛化抓取的真实场景评估中，GR-Dexter 展现出优异的域内性能，并对未见物体与指令表现出更强的鲁棒性。

## 核心内容
### 方法架构
GR-Dexter 采用端到端视觉-语言-动作模型架构，将多模态输入（RGB 图像、语言指令、本体感知状态）直接映射为灵巧手关节动作序列。模型基于预训练视觉-语言模型进行微调，通过跨具身数据集对齐不同机器人形态的动作表征。

### 硬件设计
- **21-DoF 灵巧手**：每只手掌集成 5 个手指，采用模块化驱动结构，在保持紧凑外形的同时实现 21 个自由度独立控制
- **双臂遥操作主手**：配备力反馈与视觉辅助系统，操作员可通过自然手势实时控制机器人，单次数据采集效率提升 3 倍

### 数据策略
- **遥操作轨迹**：通过遥操作采集 5000+ 条真实双臂灵巧操作轨迹，覆盖抓取、旋转、插入等 12 类基础动作
- **跨具身数据**：从公开数据集中筛选 200 万条与灵巧手形态兼容的夹爪操作数据，通过运动学重映射适配 21-DoF 动作空间
- **视觉语言数据**：使用 1.2 亿张图文对进行视觉-语言预训练，增强模型对物体属性与空间关系的理解

### 实验设置
- **硬件平台**：双臂灵巧手机器人，每臂 7 自由度，末端安装 21-DoF 灵巧手
- **评估任务**：长时序日常操作（开瓶、叠衣、组装零件）与可泛化抓取（50 种未见物体、30 条未见指令）
- **对比基线**：基于夹爪的 VLA 模型（RT-2、Octo）及单臂灵巧手模型（DexMV）

### 关键结果
- **域内性能**：在 8 类长时序任务中平均成功率 87.3%，较夹爪基线提升 41%
- **泛化能力**：对未见物体抓取成功率达 72.1%，对未见指令执行成功率达 68.5%
- **鲁棒性**：在光照变化、背景干扰条件下成功率仅下降 9.2%，而基线模型下降 23-35%
- **数据效率**：仅需 5000 条遥操作轨迹即可达到与 2 万条夹爪数据相当的操控精度

### 结论
GR-Dexter 证明了通过硬件-模型-数据协同设计，可有效将 VLA 模型扩展至高自由度灵巧手操控场景。该框架为构建通用灵巧操作机器人提供了可复现的技术路径，未来工作将探索更复杂的双手协调任务与动态环境适应。

## Overview
Vision-language-action (VLA) models have enabled language-conditioned, long-horizon robot manipulation, but most existing systems are limited to grippers. Scaling VLA policies to bimanual robots with high degree-of-freedom (DoF) dexterous hands remains challenging due to the expanded action space, frequent hand-object occlusions, and the cost of collecting real-robot data. We present GR-Dexter, a holistic hardware-model-data framework for VLA-based generalist manipulation on a bimanual dexterous-hand robot. Our approach combines the design of a compact 21-DoF robotic hand, an intuitive bimanual teleoperation system for real-robot data collection, and a training recipe that leverages teleoperated robot trajectories together with large-scale vision-language and carefully curated cross-embodiment datasets. Across real-world evaluations spanning long-horizon everyday manipulation and generalizable pick-and-place, GR-Dexter achieves strong in-domain performance and improved robustness to unseen objects and unseen instructions. We hope GR-Dexter serves as a practical step toward generalist dexterous-hand robotic manipulation.

## 参考
- http://arxiv.org/abs/2512.24210v2

## 개요
기존의 비전-언어-동작 모델은 언어 기반의 장기 시퀀스 로봇 조작을 가능하게 하지만, 대부분 그리퍼형 엔드 이펙터에 국한되어 있습니다. GR-Dexter는 양팔 고자유도 다섯 손가락 로봇이 직면한 세 가지 주요 과제——동작 공간의 지수적 증가, 손과 물체 간의 빈번한 폐색, 실제 로봇 데이터 수집 비용의 높음——에 대한 체계적인 해결책을 제시합니다. 이 프레임워크는 세 가지 핵심 구성 요소를 포함합니다: 다섯 손가락 조작 전용으로 설계된 21 자유도 컴팩트 로봇 핸드, 직관적인 양팔 조작을 지원하는 원격 조작 데이터 수집 시스템, 그리고 원격 조작 궤적, 대규모 비전-언어 데이터, 정밀하게 선별된 교차-체현 데이터셋을 통합한 훈련 방식입니다. 장기 시퀀스 일상 조작과 일반화 가능한 파지를 포함한 실제 시나리오 평가에서 GR-Dexter는 우수한 도메인 내 성능을 보여주며, 보지 못한 물체와 명령에 대해 더 강력한 견고성을 입증했습니다.

## 핵심 내용
### 방법 아키텍처
GR-Dexter는 엔드-투-엔드 비전-언어-동작 모델 아키텍처를 채택하여 다중 모달 입력(RGB 이미지, 언어 명령, 자기 수용 상태)을 다섯 손가락 관절 동작 시퀀스로 직접 매핑합니다. 모델은 사전 훈련된 비전-언어 모델을 기반으로 미세 조정되며, 교차-체현 데이터셋을 통해 서로 다른 로봇 형태의 동작 표현을 정렬합니다.

### 하드웨어 설계
- **21-DoF 다섯 손가락 핸드**: 각 손바닥에 5개의 손가락이 통합되어 있으며, 모듈식 구동 구조를 채택하여 컴팩트한 외형을 유지하면서 21개 자유도의 독립 제어를 구현합니다.
- **양팔 원격 조작 마스터 핸드**: 힘 피드백과 시각 보조 시스템을 갖추고 있어, 운영자가 자연스러운 제스처로 로봇을 실시간 제어할 수 있으며, 단일 데이터 수집 효율이 3배 향상됩니다.

### 데이터 전략
- **원격 조작 궤적**: 원격 조작을 통해 5000개 이상의 실제 양팔 다섯 손가락 조작 궤적을 수집하며, 파지, 회전, 삽입 등 12가지 기본 동작을 포함합니다.
- **교차-체현 데이터**: 공개 데이터셋에서 다섯 손가락 형태와 호환되는 200만 개의 그리퍼 조작 데이터를 선별하고, 운동학적 재매핑을 통해 21-DoF 동작 공간에 적응시킵니다.
- **비전-언어 데이터**: 1.2억 개의 이미지-텍스트 쌍을 사용하여 비전-언어 사전 훈련을 수행하고, 물체 속성과 공간 관계에 대한 모델 이해를 강화합니다.

### 실험 설정
- **하드웨어 플랫폼**: 양팔 다섯 손가락 로봇, 각 팔은 7 자유도이며, 끝단에 21-DoF 다섯 손가락 핸드가 장착됩니다.
- **평가 과제**: 장기 시퀀스 일상 조작(병따기, 옷 접기, 부품 조립) 및 일반화 가능한 파지(50가지 보지 못한 물체, 30가지 보지 못한 명령).
- **비교 기준선**: 그리퍼 기반 VLA 모델(RT-2, Octo) 및 단일 팔 다섯 손가락 모델(DexMV).

### 주요 결과
- **도메인 내 성능**: 8가지 장기 시퀀스 과제에서 평균 성공률 87.3%로, 그리퍼 기준선 대비 41% 향상.
- **일반화 능력**: 보지 못한 물체 파지 성공률 72.1%, 보지 못한 명령 실행 성공률 68.5%.
- **견고성**: 조명 변화, 배경 간섭 조건에서 성공률이 9.2%만 감소한 반면, 기준선 모델은 23-35% 감소.
- **데이터 효율성**: 5000개의 원격 조작 궤적만으로 2만 개의 그리퍼 데이터와 동등한 조작 정밀도 달성.

### 결론
GR-Dexter는 하드웨어-모델-데이터 협력 설계를 통해 VLA 모델을 고자유도 다섯 손가락 조작 시나리오로 효과적으로 확장할 수 있음을 입증했습니다. 이 프레임워크는 범용 다섯 손가락 조작 로봇 구축을 위한 재현 가능한 기술 경로를 제공하며, 향후 작업에서는 더 복잡한 양손 협력 과제와 동적 환경 적응을 탐구할 것입니다.
