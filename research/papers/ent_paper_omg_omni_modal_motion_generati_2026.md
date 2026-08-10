---
$id: ent_paper_omg_omni_modal_motion_generati_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OMG: Omni-Modal Motion Generation for Generalist Humanoid Control'
  zh: OMG｜用于通用人形控制的全模态运动生成
  ko: 'OMG: Omni-Modal Motion Generation for Generalist Humanoid Control'
summary:
  en: 'Humanoid whole-body control has made significant progress in recent years, yet existing approaches remain limited to
    few-skill policies with heavy reward engineering, or motion trackers that are difficult to extend to new input modalities.
    We argue that the key to general-purpose humanoid control is to build a scalable brain, a module capable of reasoning
    with diverse conditioning modalities, atop a reactive motion tracking cerebellum, mirroring the hierarchical structure
    of biological motor systems. Two challenges arise in realizing this vision: acquiring a vast amount of high-quality data
    to achieve general purpose control, and equipping the generator with the capability to condition on compositional, extensible
    multi-modal inputs. We present OMG, which addresses these challenges with a'
  zh: OMG 是一种面向通用人形机器人控制的全身运动生成框架，由研究团队提出。其核心贡献在于通过精心设计的数据处理流程和基于扩散模型的运动生成骨干网络，实现了对语言、音频和人体参考动作等多种输入模态的兼容，并展现出优异的模型扩展性和对新分布与模态的高效适应能力。
  ko: OMG 先从本体状态与关节序列恢复场景、目标或运动表征，再用扩散策略/流匹配、VLM 语义规划/路由、全身控制器/WBC/MPC生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generative_motion
- language_control
- motion_generation
- omg
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: OMG: Omni-Modal Motion
    Generation for Generalist Humanoid Control. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (677 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: OMG project page
  url: https://tsinghua-mars-lab.github.io/OMG/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
现有的人形机器人全身控制方法要么局限于少数技能策略并依赖繁重的奖励工程，要么是难以扩展至新输入模态的运动追踪器。OMG 借鉴生物运动系统的层级结构，将可扩展的“大脑”模块（负责处理多种条件模态的推理）置于反应式运动追踪“小脑”之上。为解决通用控制所需的海量高质量数据获取以及生成器对组合式、可扩展多模态输入的适应能力这两大挑战，OMG 采用了细致的数据整理、过滤与标注流程，并构建了基于扩散模型的运动生成骨干网络。实验表明，OMG 作为全模态全身控制器，在性能、模型缩放行为以及高效适应新分布与模态方面均达到了当前最优水平。

## 核心内容
### 方法概述
OMG 的核心架构包含两个关键组件：
- **数据处理流程**：通过精心设计的数据整理、过滤与标注流水线，解决了通用控制所需海量高质量数据的获取难题。
- **运动生成骨干网络**：采用基于扩散模型的生成架构，能够以语言、音频和人体参考动作作为条件输入，生成全身运动。

### 实验设置与关键结果
- **性能表现**：在多项实验中，OMG 作为全模态全身控制器展现出当前最优（state-of-the-art）的性能。
- **模型缩放行为**：验证了模型具备良好的缩放特性，即随着模型规模增大，性能持续提升。
- **适应能力**：能够高效适应新的数据分布和输入模态，展现出强大的泛化能力。

### 结论
OMG 标志着向人形机器人基础模型迈出了具体的一步，通过模仿生物运动系统的层级结构，成功构建了可扩展的“大脑-小脑”控制框架，为通用人形机器人控制提供了新的解决方案。

## Overview
Humanoid whole-body control has made significant progress in recent years, yet existing approaches remain limited to few-skill policies with heavy reward engineering, or motion trackers that are difficult to extend to new input modalities. We argue that the key to general-purpose humanoid control is to build a scalable brain, a module capable of reasoning with diverse conditioning modalities, atop a reactive motion tracking cerebellum, mirroring the hierarchical structure of biological motor systems. Two challenges arise in realizing this vision: acquiring a vast amount of high-quality data to achieve general purpose control, and equipping the generator with the capability to condition on compositional, extensible multi-modal inputs. We present OMG, which addresses these challenges with a meticulous data curation, filtering and labeling pipeline, as well as a diffusion-based motion generation backbone that conditions on language, audio, and human reference motions. Extensive experiments validate OMG as an omni-modal whole-body controller exhibiting state-of-the-art performance, model scaling behavior and efficient adaptation to new distributions and modalities, marking a concrete step toward foundation models for humanoid robots.

## 参考
- Semantic Scholar search: OMG: Omni-Modal Motion Generation for Generalist Humanoid Control

## 개요
기존의 휴머노이드 로봇 전신 제어 방법은 제한된 스킬 정책에 국한되거나 복잡한 보상 엔지니어링에 의존하거나, 새로운 입력 모달리티로 확장하기 어려운 모션 트래커에 머물러 있습니다. OMG는 생물학적 운동 시스템의 계층 구조를 차용하여, 다양한 조건 모달리티를 처리하는 확장 가능한 '뇌' 모듈을 반응형 모션 추적 '소뇌' 위에 배치합니다. 일반 제어에 필요한 대규모 고품질 데이터 확보와 생성기의 조합적이고 확장 가능한 다중 모달 입력 적응 능력이라는 두 가지 과제를 해결하기 위해, OMG는 세심한 데이터 정리, 필터링 및 주석 처리 프로세스를 채택하고 확산 모델 기반의 모션 생성 백본 네트워크를 구축했습니다. 실험 결과, OMG는 전 모달리티 전신 제어기로서 성능, 모델 스케일링 동작, 새로운 분포 및 모달리티에 대한 효율적 적응 측면에서 최신 수준(state-of-the-art)을 달성했습니다.

## 핵심 내용
### 방법 개요
OMG의 핵심 아키텍처는 두 가지 주요 구성 요소를 포함합니다:
- **데이터 처리 프로세스**: 정교하게 설계된 데이터 정리, 필터링 및 주석 처리 파이프라인을 통해 일반 제어에 필요한 대규모 고품질 데이터 확보 문제를 해결합니다.
- **모션 생성 백본 네트워크**: 확산 모델 기반의 생성 아키텍처를 채택하여 언어, 오디오 및 인간 참조 동작을 조건 입력으로 사용하여 전신 모션을 생성할 수 있습니다.

### 실험 설정 및 주요 결과
- **성능表現**: 여러 실험에서 OMG는 전 모달리티 전신 제어기로서 최신 수준(state-of-the-art)의 성능을 보여줍니다.
- **모델 스케일링 동작**: 모델 크기가 증가함에 따라 성능이 지속적으로 향상되는 우수한 스케일링 특성을 검증했습니다.
- **적응 능력**: 새로운 데이터 분포와 입력 모달리티에 효율적으로 적응하며 강력한 일반화 능력을 입증했습니다.

### 결론
OMG는 휴머노이드 로봇 기반 모델을 향한 구체적인 한 걸음을 나타내며, 생물학적 운동 시스템의 계층 구조를 모방하여 확장 가능한 '뇌-소뇌' 제어 프레임워크를 성공적으로 구축함으로써 일반 휴머노이드 로봇 제어를 위한 새로운 솔루션을 제공합니다.
