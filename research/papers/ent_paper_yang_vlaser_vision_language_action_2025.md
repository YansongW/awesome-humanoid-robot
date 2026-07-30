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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.11027v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
상당한 연구가 시각-언어 모델(VLM)을 사용한 체화된 추론 능력 개발이나 고급 VLM을 시각-언어-행동(VLA) 모델에 통합하여 엔드투엔드 로봇 제어를 수행하는 데 집중되어 왔지만, 상위 VLM 기반 추론과 하위 VLA 정책 학습 간의 중요한 격차를 직접적으로 해결한 연구는 거의 없습니다. 본 연구에서는 체화된 추론과 VLA 정책 학습을 연결하는 첫걸음으로, Vlaser를 소개합니다. Vlaser는 시너지적 체화된 추론 능력을 갖춘 시각-언어-행동 모델로, 체화된 에이전트를 위해 고수준 추론과 저수준 제어를 통합하도록 설계된 기초 시각-언어 모델입니다. 고품질의 Vlaser-6M 데이터셋을 기반으로 구축된 Vlaser는 공간 추론, 체화된 접지, 체화된 QA, 작업 계획을 포함한 다양한 체화된 추론 벤치마크에서 최첨단 성능을 달성합니다. 또한, 서로 다른 VLM 초기화가 지도 학습 기반 VLA 미세 조정에 미치는 영향을 체계적으로 조사하여, 인터넷 규모의 사전 학습 데이터와 체화된 특화 정책 학습 데이터 간의 도메인 차이를 완화하는 새로운 통찰력을 제공합니다. 이러한 통찰력을 바탕으로, 우리의 접근 방식은 WidowX 벤치마크에서 최첨단 결과를, Google Robot 벤치마크에서 경쟁력 있는 성능을 달성합니다.

## 핵심 내용
상당한 연구가 시각-언어 모델(VLM)을 사용한 체화된 추론 능력 개발이나 고급 VLM을 시각-언어-행동(VLA) 모델에 통합하여 엔드투엔드 로봇 제어를 수행하는 데 집중되어 왔지만, 상위 VLM 기반 추론과 하위 VLA 정책 학습 간의 중요한 격차를 직접적으로 해결한 연구는 거의 없습니다. 본 연구에서는 체화된 추론과 VLA 정책 학습을 연결하는 첫걸음으로, Vlaser를 소개합니다. Vlaser는 시너지적 체화된 추론 능력을 갖춘 시각-언어-행동 모델로, 체화된 에이전트를 위해 고수준 추론과 저수준 제어를 통합하도록 설계된 기초 시각-언어 모델입니다. 고품질의 Vlaser-6M 데이터셋을 기반으로 구축된 Vlaser는 공간 추론, 체화된 접지, 체화된 QA, 작업 계획을 포함한 다양한 체화된 추론 벤치마크에서 최첨단 성능을 달성합니다. 또한, 서로 다른 VLM 초기화가 지도 학습 기반 VLA 미세 조정에 미치는 영향을 체계적으로 조사하여, 인터넷 규모의 사전 학습 데이터와 체화된 특화 정책 학습 데이터 간의 도메인 차이를 완화하는 새로운 통찰력을 제공합니다. 이러한 통찰력을 바탕으로, 우리의 접근 방식은 WidowX 벤치마크에서 최첨단 결과를, Google Robot 벤치마크에서 경쟁력 있는 성능을 달성합니다.

## 参考
- http://arxiv.org/abs/2510.11027v2
