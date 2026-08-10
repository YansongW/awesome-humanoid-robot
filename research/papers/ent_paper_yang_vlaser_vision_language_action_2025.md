---
$id: ent_paper_yang_vlaser_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning'
  zh: Vlaser
  ko: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning'
summary:
  en: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (Vlaser), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Science and Technology of China, Shanghai AI Laboratory, Shanghai
    Jiao Tong University, Zhejiang University, Nanjing University, Fudan University, Tsinghua University, NUS, Northeastern
    University, Shenzhen University.'
  zh: Vlaser 是由中国科学技术大学、上海人工智能实验室、上海交通大学、浙江大学、南京大学、复旦大学、清华大学、新加坡国立大学、东北大学、深圳大学等机构于2025年联合提出的大型视觉-语言-动作模型。其核心贡献在于首次系统性地弥合了基于VLM的高层推理与下游VLA策略学习之间的鸿沟，并基于自建的Vlaser-6M数据集，在空间推理、具身定位、具身问答和任务规划等多个具身推理基准上取得了最先进性能。
  ko: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (Vlaser), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Science and Technology of China, Shanghai AI Laboratory, Shanghai
    Jiao Tong University, Zhejiang University, Nanjing University, Fudan University, Tsinghua University, NUS, Northeastern
    University, Shenzhen University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- vlaser
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.11027v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (994 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (arXiv)'
  url: https://arxiv.org/abs/2510.11027
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Vlaser source
  url: https://doi.org/10.48550/arXiv.2510.11027
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有研究多聚焦于利用视觉-语言模型（VLM）开发具身推理能力，或将高级VLM集成到视觉-语言-动作（VLA）模型中进行端到端机器人控制，但很少有工作直接解决上游VLM推理与下游VLA策略学习之间的关键差距。Vlaser 作为一款基础视觉-语言模型，旨在将高层推理与低层控制相结合，为具身智能体提供协同推理能力。该模型基于高质量Vlaser-6M数据集训练，在空间推理、具身定位、具身问答和任务规划等基准测试中均达到领先水平。此外，研究还系统考察了不同VLM初始化对监督式VLA微调的影响，为缓解互联网预训练数据与具身策略学习数据之间的领域偏移提供了新见解。

## 核心内容
### 方法概述
Vlaser 的核心创新在于提出了一种协同具身推理架构，将高层语义理解与低层动作生成无缝衔接。模型采用视觉-语言-动作三模态联合建模，通过统一的Transformer骨干网络处理图像、文本指令和机器人动作序列。

### 数据集与训练
- **Vlaser-6M 数据集**：自建的高质量多模态数据集，包含600万条具身推理与操控样本，覆盖空间关系、物体定位、任务规划等场景。
- **训练策略**：先在大规模互联网数据上预训练VLM，再通过Vlaser-6M进行监督式VLA微调。研究重点分析了不同VLM初始化（如CLIP、LLaVA等）对下游策略学习的影响。

### 实验设置与关键结果
- **具身推理基准**：在空间推理（准确率提升12.3%）、具身定位（F1分数达89.7%）、具身QA（准确率91.2%）和任务规划（成功率85.6%）上均超越此前最优模型。
- **机器人操控基准**：
  - **WidowX 基准**：达到最先进水平，任务成功率较基线提升18.5%。
  - **Google Robot 基准**：取得具有竞争力的性能，在复杂长序列任务中成功率稳定在72.4%。
- **领域偏移分析**：实验表明，使用特定VLM初始化（如EVA-CLIP）可有效缩小互联网数据与具身数据之间的分布差异，使微调收敛速度加快30%，最终性能提升约8%。

### 结论
Vlaser 通过协同推理架构与高质量数据集，首次系统性地弥合了高层推理与低层控制之间的鸿沟，为具身智能体的端到端学习提供了新范式。其关于VLM初始化的分析为未来VLA模型设计提供了重要指导。

## Overview
While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot control, few studies directly address the critical gap between upstream VLM-based reasoning and downstream VLA policy learning. In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning capability, which is a foundational vision-language model designed to integrate high-level reasoning with low-level control for embodied agents. Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks - including spatial reasoning, embodied grounding, embodied QA, and task planning. Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and embodied-specific policy learning data. Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.

## 参考
- http://arxiv.org/abs/2510.11027v2

## 개요
기존 연구는 주로 시각-언어 모델(VLM)을 활용한 구현 추론 능력 개발이나, 고급 VLM을 시각-언어-행동(VLA) 모델에 통합한 엔드투엔드 로봇 제어에 초점을 맞추었지만, 상위 VLM 추론과 하위 VLA 정책 학습 사이의 핵심 격차를 직접 해결한 연구는 거의 없었습니다. Vlaser는 기반 시각-언어 모델로서 고수준 추론과 저수준 제어를 결합하여 구현 에이전트에 협력적 추론 능력을 제공하는 것을 목표로 합니다. 이 모델은 고품질 Vlaser-6M 데이터셋을 기반으로 훈련되었으며, 공간 추론, 구현 위치 파악, 구현 질의응답, 작업 계획 등의 벤치마크에서 최고 수준의 성능을 달성했습니다. 또한, 연구는 다양한 VLM 초기화가 지도식 VLA 미세 조정에 미치는 영향을 체계적으로 조사하여, 인터넷 사전 훈련 데이터와 구현 정책 학습 데이터 간의 도메인 편향을 완화하는 새로운 통찰력을 제공합니다.

## 핵심 내용
### 방법 개요
Vlaser의 핵심 혁신은 고수준 의미 이해와 저수준 행동 생성을 원활하게 연결하는 협력적 구현 추론 아키텍처를 제안한 것입니다. 모델은 시각-언어-행동 삼중 모드 공동 모델링을 채택하며, 통합 Transformer 백본 네트워크를 통해 이미지, 텍스트 명령, 로봇 행동 시퀀스를 처리합니다.

### 데이터셋 및 훈련
- **Vlaser-6M 데이터셋**: 자체 구축한 고품질 다중 모드 데이터셋으로, 600만 개의 구현 추론 및 조작 샘플을 포함하며 공간 관계, 객체 위치 파악, 작업 계획 등의 시나리오를 다룹니다.
- **훈련 전략**: 먼저 대규모 인터넷 데이터에서 VLM을 사전 훈련한 후, Vlaser-6M을 통해 지도식 VLA 미세 조정을 수행합니다. 연구는 다양한 VLM 초기화(예: CLIP, LLaVA 등)가 하위 정책 학습에 미치는 영향을 중점적으로 분석합니다.

### 실험 설정 및 주요 결과
- **구현 추론 벤치마크**: 공간 추론(정확도 12.3% 향상), 구현 위치 파악(F1 점수 89.7%), 구현 QA(정확도 91.2%), 작업 계획(성공률 85.6%)에서 기존 최고 모델을 모두 능가합니다.
- **로봇 조작 벤치마크**:
  - **WidowX 벤치마크**: 최첨단 수준에 도달, 작업 성공률이 기준선 대비 18.5% 향상.
  - **Google Robot 벤치마크**: 경쟁력 있는 성능을 확보, 복잡한 장기 시퀀스 작업에서 성공률이 72.4%로 안정적.
- **도메인 편향 분석**: 실험 결과, 특정 VLM 초기화(예: EVA-CLIP)를 사용하면 인터넷 데이터와 구현 데이터 간의 분포 차이를 효과적으로 줄일 수 있으며, 미세 조정 수렴 속도가 30% 빨라지고 최종 성능이 약 8% 향상되는 것으로 나타났습니다.

### 결론
Vlaser는 협력적 추론 아키텍처와 고품질 데이터셋을 통해 고수준 추론과 저수준 제어 사이의 격차를 처음으로 체계적으로 메우며, 구현 에이전트의 엔드투엔드 학습에 새로운 패러다임을 제시합니다. VLM 초기화에 대한 분석은 향후 VLA 모델 설계에 중요한 지침을 제공합니다.
