---
$id: ent_paper_fang_corevla_a_dual_stage_end_to_en_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine'
  zh: CoReVLA
  ko: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine'
summary:
  en: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (CoReVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by College of Transportation, Tongji
    University.'
  zh: CoReVLA 是同济大学交通运输学院于 2025 年提出的双阶段端到端自动驾驶框架，专为长尾安全关键场景设计。其核心贡献在于通过“收集-优化”双阶段流程，结合驾驶接管数据与 Direct Preference Optimization
    (DPO) 算法，持续提升模型在罕见危险场景下的表现。在 Bench2Drive 基准上，CoReVLA 的驾驶得分达 72.18，成功率 50%，分别超越现有最优方法 7.96 分和 15%。
  ko: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (CoReVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by College of Transportation, Tongji
    University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- corevla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15968v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (832 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (arXiv)'
  url: https://arxiv.org/abs/2509.15968
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoReVLA source
  url: https://doi.org/10.48550/arXiv.2509.15968
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
CoReVLA 是一个面向长尾场景的持续学习端到端自动驾驶框架，由同济大学提出。该框架首先在开源驾驶问答数据集上联合微调，使模型获得基础驾驶场景理解能力；随后在 CAVE 仿真平台中部署，通过实时交互收集驾驶员接管数据——每次接管都标记了模型无法可靠处理的长尾场景。最后，利用 Direct Preference Optimization (DPO) 从人类偏好中直接学习，避免手动设计奖励带来的奖励破解问题。实验表明，CoReVLA 在 Bench2Drive 基准的长尾安全关键场景下，驾驶得分和成功率均显著超越现有方法，并能通过历史接管经验持续改进类似故障场景的表现。

## 核心内容
### 方法架构
CoReVLA 采用双阶段“收集-优化”流程：
- **第一阶段（基础理解）**：在混合开源驾驶问答数据集上联合微调大视觉-语言-动作模型，使其掌握驾驶场景的基础推理能力。
- **第二阶段（长尾优化）**：
  1. 在 CAVE 仿真平台中部署模型，实时记录驾驶员接管事件。
  2. 每次接管对应一个模型无法可靠处理的长尾场景。
  3. 使用 Direct Preference Optimization (DPO) 从人类偏好中直接学习，避免手动设计奖励函数导致的奖励破解问题。

### 实验设置与关键结果
- **基准测试**：在 Bench2Drive 基准上进行开环与闭环实验。
- **关键指标**：
  - 驾驶得分 (DS)：72.18
  - 成功率 (SR)：50%
  - 在长尾安全关键场景下，DS 超越现有最优方法 7.96 分，SR 提升 15%。
- **持续学习能力**：案例研究显示，模型能利用历史接管经验，在类似故障场景中持续改进性能。

### 结论
CoReVLA 通过双阶段流程有效解决了长尾场景数据稀缺与学习效率低下的问题，在安全关键场景下显著优于现有方法。所有代码和预处理数据集已开源。

## Overview
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All codea and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## Overview
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All code and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## Content
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All code and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## 参考
- http://arxiv.org/abs/2509.15968v1

## 개요
CoReVLA는 통지대학교에서 제안한 장기 꼬리(long-tail) 시나리오를 위한 지속 학습 기반 엔드투엔드 자율주행 프레임워크입니다. 이 프레임워크는 먼저 오픈소스 주행 질의응답 데이터셋에서 공동 미세 조정을 통해 모델이 기본 주행 시나리오 이해 능력을 획득하게 합니다. 이후 CAVE 시뮬레이션 플랫폼에 배포하여 실시간 상호작용을 통해 운전자 개입 데이터를 수집합니다—각 개입은 모델이 안정적으로 처리하지 못하는 장기 꼬리 시나리오를 표시합니다. 마지막으로 Direct Preference Optimization (DPO)을 사용하여 인간 선호도에서 직접 학습함으로써 수동 보상 설계로 인한 보상 해킹 문제를 방지합니다. 실험 결과, CoReVLA는 Bench2Drive 벤치마크의 장기 꼬리 안전 핵심 시나리오에서 주행 점수와 성공률 모두 기존 방법을 크게 능가하며, 과거 개입 경험을 통해 유사한 고장 시나리오의 성능을 지속적으로 개선할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
CoReVLA는 2단계 "수집-최적화" 프로세스를 채택합니다:
- **1단계 (기본 이해)**: 혼합 오픈소스 주행 질의응답 데이터셋에서 대형 비전-언어-행동 모델을 공동 미세 조정하여 주행 시나리오의 기본 추론 능력을 습득하게 합니다.
- **2단계 (장기 꼬리 최적화)**:
  1. CAVE 시뮬레이션 플랫폼에 모델을 배포하고 운전자 개입 이벤트를 실시간으로 기록합니다.
  2. 각 개입은 모델이 안정적으로 처리하지 못하는 장기 꼬리 시나리오에 해당합니다.
  3. Direct Preference Optimization (DPO)을 사용하여 인간 선호도에서 직접 학습함으로써 수동 보상 함수 설계로 인한 보상 해킹 문제를 방지합니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: Bench2Drive 벤치마크에서 오픈 루프 및 폐쇄 루프 실험을 수행합니다.
- **주요 지표**:
  - 주행 점수 (DS): 72.18
  - 성공률 (SR): 50%
  - 장기 꼬리 안전 핵심 시나리오에서 DS는 기존 최적 방법보다 7.96점, SR은 15% 향상되었습니다.
- **지속 학습 능력**: 사례 연구에 따르면 모델은 과거 개입 경험을 활용하여 유사한 고장 시나리오에서 성능을 지속적으로 개선할 수 있습니다.

### 결론
CoReVLA는 2단계 프로세스를 통해 장기 꼬리 시나리오의 데이터 부족과 학습 효율성 저하 문제를 효과적으로 해결하며, 안전 핵심 시나리오에서 기존 방법보다 크게 우수합니다. 모든 코드와 전처리된 데이터셋은 오픈소스로 공개되었습니다.
