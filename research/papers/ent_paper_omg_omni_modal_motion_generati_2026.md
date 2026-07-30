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
    Generation for Generalist Humanoid Control. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py'
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

## 개요
휴머노이드 전신 제어는 최근 몇 년간 큰 진전을 이루었지만, 기존 접근 방식은 과도한 보상 엔지니어링이 필요한 소수의 스킬 정책이나 새로운 입력 양식으로 확장하기 어려운 모션 트래커에 국한되어 있습니다. 우리는 범용 휴머노이드 제어의 핵심이 생물학적 운동 시스템의 계층적 구조를 반영하여, 반응형 모션 추적 소뇌 위에 다양한 조건화 양식으로 추론할 수 있는 확장 가능한 두뇌, 즉 모듈을 구축하는 것이라고 주장합니다. 이 비전을 실현하는 데는 두 가지 과제가 있습니다: 범용 제어를 달성하기 위한 방대한 양의 고품질 데이터 확보, 그리고 생성기에 구성 가능하고 확장 가능한 다중 모달 입력을 조건화할 수 있는 능력을 부여하는 것입니다. 우리는 이러한 과제를 정밀한 데이터 큐레이션, 필터링 및 레이블링 파이프라인과 언어, 오디오 및 인간 참조 동작을 조건화하는 확산 기반 모션 생성 백본을 통해 해결하는 OMG를 제시합니다. 광범위한 실험을 통해 OMG는 최첨단 성능, 모델 확장 동작 및 새로운 분포와 양식에 대한 효율적인 적응을 보여주는 전모달 전신 제어기로 검증되었으며, 이는 휴머노이드 로봇을 위한 기초 모델을 향한 구체적인 발걸음을 의미합니다.

## 핵심 내용
휴머노이드 전신 제어는 최근 몇 년간 큰 진전을 이루었지만, 기존 접근 방식은 과도한 보상 엔지니어링이 필요한 소수의 스킬 정책이나 새로운 입력 양식으로 확장하기 어려운 모션 트래커에 국한되어 있습니다. 우리는 범용 휴머노이드 제어의 핵심이 생물학적 운동 시스템의 계층적 구조를 반영하여, 반응형 모션 추적 소뇌 위에 다양한 조건화 양식으로 추론할 수 있는 확장 가능한 두뇌, 즉 모듈을 구축하는 것이라고 주장합니다. 이 비전을 실현하는 데는 두 가지 과제가 있습니다: 범용 제어를 달성하기 위한 방대한 양의 고품질 데이터 확보, 그리고 생성기에 구성 가능하고 확장 가능한 다중 모달 입력을 조건화할 수 있는 능력을 부여하는 것입니다. 우리는 이러한 과제를 정밀한 데이터 큐레이션, 필터링 및 레이블링 파이프라인과 언어, 오디오 및 인간 참조 동작을 조건화하는 확산 기반 모션 생성 백본을 통해 해결하는 OMG를 제시합니다. 광범위한 실험을 통해 OMG는 최첨단 성능, 모델 확장 동작 및 새로운 분포와 양식에 대한 효율적인 적응을 보여주는 전모달 전신 제어기로 검증되었으며, 이는 휴머노이드 로봇을 위한 기초 모델을 향한 구체적인 발걸음을 의미합니다.

## 参考
- Semantic Scholar search: OMG: Omni-Modal Motion Generation for Generalist Humanoid Control
