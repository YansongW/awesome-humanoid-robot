---
$id: ent_paper_chen_fast_in_slow_a_dual_system_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning'
  zh: Fast-in-Slow
  ko: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning'
summary:
  en: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (Fast-in-Slow), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Chinese University of Hong Kong, State Key Laboratory
    of Multimedia Information Processing, School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial
    Intelligence (BAAI), and published at NIPS25.'
  zh: Fast-in-Slow (FiS) 是由香港中文大学、北京大学等机构联合提出的2025年大型视觉-语言-动作模型，旨在解决机器人操作中的泛化策略与执行效率矛盾。其核心创新在于将快速执行模块（System 1）嵌入基于VLM的慢速推理系统（System
    2）中，通过部分参数共享实现统一双系统架构，在仿真和真实任务中分别取得8%和11%的平均成功率提升，控制频率达117.7 Hz。
  ko: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (Fast-in-Slow), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Chinese University of Hong Kong, State Key Laboratory
    of Multimedia Information Processing, School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial
    Intelligence (BAAI), and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fast_in_slow
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01953v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1025 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (arXiv)'
  url: https://arxiv.org/abs/2506.01953
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Fast-in-Slow (FiS) 借鉴卡尼曼双系统理论，提出一种统一的双系统视觉-语言-动作模型。现有方法将基于VLM的System 2（负责高层推理）与独立的System 1（负责实时控制）分离，导致System 1无法充分利用VLM的预训练知识。FiS通过将System 1执行模块嵌入System 2内部并共享部分参数，既实现了高频执行，又促进了推理与执行组件的协同。该模型为两个系统设计了异构模态输入和异步运行频率，并采用双感知协同训练策略，使System 1获得动作生成能力的同时保留System 2的上下文推理表征。

## 核心内容
### 方法架构
- **双系统设计**：FiS-VLA 将快速执行模块（System 1）嵌入基于VLM的慢速推理系统（System 2）内部，通过部分参数共享实现统一架构。System 2 负责高层语义推理与任务规划，System 1 负责实时动作生成。
- **异构模态输入**：两个系统采用不同的输入模态——System 2 处理全局视觉与语言指令，System 1 接收局部感知信息与高频传感器数据，以适应各自的功能需求。
- **异步运行频率**：System 2 以较低频率（如5-10 Hz）进行推理，System 1 以较高频率（117.7 Hz）执行动作，动作块大小设为8。

### 训练策略
- **双感知协同训练**：提出一种联合训练方法，使System 1在获得动作生成能力的同时，不破坏System 2的上下文推理表征。该策略通过共享参数梯度传播，确保两个系统在训练过程中相互促进而非干扰。

### 实验设置与结果
- **仿真环境**：在多个标准机器人操作基准上测试，FiS-VLA 平均成功率较先前最优方法提升8%。
- **真实世界任务**：在真实机器人平台上进行多类操作任务（如抓取、放置、组装），平均成功率提升11%。
- **控制频率**：在动作块大小为8的条件下，达到117.7 Hz的控制频率，满足实时操作需求。
- **消融实验**：验证了参数共享策略、异构模态输入和异步频率设计对性能的贡献，每个组件均带来显著提升。

### 结论
FiS-VLA 通过统一双系统架构，有效解决了机器人操作中泛化策略与执行效率的矛盾，在仿真和真实场景中均取得领先性能，同时保持高频实时控制能力。项目页面：fast-in-slow.github.io。

## Overview
Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation. While recent foundation policies benefit from the common-sense reasoning capabilities of internet-scale pretrained vision-language models (VLMs), they often suffer from low execution frequency. To mitigate this dilemma, dual-system approaches, inspired by Kahneman's theory, have been proposed to leverage a VLM-based System 2 model handling high-level reasoning and a separate System 1 action model ensuring real-time control. However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2. In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing parameters. This innovative paradigm not only enables high-frequency execution in System 1 but also facilitates coordination between the reasoning and execution components within a single foundation model of System 2. Given their fundamentally distinct roles within FiS-VLA, we design the two systems to incorporate heterogeneous modality inputs alongside asynchronous operating frequencies, enabling both fast and precise manipulation. To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's contextual reasoning representation. For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in real-world tasks in terms of average success rate, while achieving a 117.7 Hz control frequency with action chunk set to eight. Project web page: fast-in-slow.github.io.

## 参考
- http://arxiv.org/abs/2506.01953v1

## 개요
Fast-in-Slow (FiS)는 카너먼의 이중 시스템 이론을 차용하여 통합된 이중 시스템 비전-언어-행동 모델을 제안한다. 기존 방법은 고수준 추론을 담당하는 VLM 기반 System 2와 실시간 제어를 담당하는 독립적인 System 1을 분리하여, System 1이 VLM의 사전 학습 지식을 충분히 활용하지 못하는 문제가 있었다. FiS는 System 1 실행 모듈을 System 2 내부에 내장하고 일부 파라미터를 공유함으로써, 고주파 실행을 달성하면서도 추론과 실행 구성 요소 간의 협력을 촉진한다. 이 모델은 두 시스템을 위해 이질적 모달리티 입력과 비동기 실행 주파수를 설계하고, 이중 인식 협력 훈련 전략을 채택하여 System 1이 행동 생성 능력을 획득하는 동시에 System 2의 맥락 추론 표현을 보존한다.

## 핵심 내용
### 방법 아키텍처
- **이중 시스템 설계**: FiS-VLA는 빠른 실행 모듈(System 1)을 VLM 기반의 느린 추론 시스템(System 2) 내부에 내장하고, 부분 파라미터 공유를 통해 통합 아키텍처를 구현한다. System 2는 고수준 의미 추론과 작업 계획을 담당하고, System 1은 실시간 행동 생성을 담당한다.
- **이질적 모달리티 입력**: 두 시스템은 서로 다른 입력 모달리티를 사용한다—System 2는 전역 시각 및 언어 명령을 처리하고, System 1은 국소 인식 정보와 고주파 센서 데이터를 수신하여 각자의 기능적 요구에 적응한다.
- **비동기 실행 주파수**: System 2는 낮은 주파수(예: 5-10 Hz)로 추론하고, System 1은 높은 주파수(117.7 Hz)로 행동을 실행하며, 행동 블록 크기는 8로 설정된다.

### 훈련 전략
- **이중 인식 협력 훈련**: System 1이 행동 생성 능력을 획득하면서도 System 2의 맥락 추론 표현을 손상시키지 않는 공동 훈련 방법을 제안한다. 이 전략은 공유 파라미터의 그래디언트 전파를 통해 두 시스템이 훈련 과정에서 서로 방해하지 않고 상호 촉진하도록 보장한다.

### 실험 설정 및 결과
- **시뮬레이션 환경**: 여러 표준 로봇 조작 벤치마크에서 테스트한 결과, FiS-VLA의 평균 성공률이 이전 최고 방법보다 8% 향상되었다.
- **실세계 작업**: 실제 로봇 플랫폼에서 다양한 조작 작업(예: 파지, 배치, 조립)을 수행하여 평균 성공률이 11% 향상되었다.
- **제어 주파수**: 행동 블록 크기가 8인 조건에서 117.7 Hz의 제어 주파수를 달성하여 실시간 조작 요구를 충족한다.
- **절제 실험**: 파라미터 공유 전략, 이질적 모달리티 입력, 비동기 주파수 설계가 성능에 기여하는 바를 검증했으며, 각 구성 요소가 유의미한 향상을 가져왔다.

### 결론
FiS-VLA는 통합된 이중 시스템 아키텍처를 통해 로봇 조작에서 일반화 정책과 실행 효율성 간의 모순을 효과적으로 해결하며, 시뮬레이션과 실제 시나리오 모두에서 선도적인 성능을 달성하면서 고주파 실시간 제어 능력을 유지한다. 프로젝트 페이지: fast-in-slow.github.io.
