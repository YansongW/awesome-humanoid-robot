---
$id: ent_paper_zeng_diagnose_correct_and_learn_fro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
  zh: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
  ko: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
summary:
  en: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (Diagnose Correct and Learn from Manipulation
    Failures via Visual Symbols), is a 2025 large vision-language-action model for robotic manipulation, introduced by Beihang
    University, Shanghai Innovation Institute, Southern University of Science and Technology, Shanghai Jiao Tong University.
  zh: ViFailback 是由北京航空航天大学、上海创新研究院、南方科技大学和上海交通大学于2025年提出的大型视觉-语言-动作模型，用于机器人操作中的故障诊断与纠正。其核心贡献在于利用显式视觉符号提升标注效率，并发布了包含58,126个VQA对和5,202条真实操作轨迹的ViFailback数据集，以及用于评估VLM故障诊断能力的ViFailback-Bench基准。
  ko: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (Diagnose Correct and Learn from Manipulation
    Failures via Visual Symbols), is a 2025 large vision-language-action model for robotic manipulation, introduced by Beihang
    University, Shanghai Innovation Institute, Southern University of Science and Technology, Shanghai Jiao Tong University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diagnose_correct_and_learn_fro
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02787v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1330 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (arXiv)
  url: https://arxiv.org/abs/2512.02787
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols source
  url: https://doi.org/10.48550/arXiv.2512.02787
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ViFailback 框架旨在解决现有VLA模型在故障诊断和从失败中学习方面的局限性，同时克服模拟生成故障数据集在真实世界泛化不足的问题。该框架通过显式视觉符号增强标注效率，并构建了大规模真实世界数据集ViFailback，包含58,126个VQA对和5,202条操作轨迹。基于此数据集，团队建立了ViFailback-Bench基准，包含11个细粒度VQA任务，分为封闭式评估的ViFailback-Bench Lite和开放式评估的ViFailback-Bench Hard。为验证框架有效性，团队开发了ViFailback-8B VLM，在基准上取得显著性能提升，并能生成用于纠正动作的视觉符号。最终，通过将ViFailback-8B与VLA模型集成，真实机器人实验展示了其辅助VLA模型从失败中恢复的能力。

## 核心内容
### 方法
ViFailback 框架的核心创新在于使用显式视觉符号（如箭头、高亮框等）来标注操作失败的关键位置和纠正方向，从而大幅提升数据标注效率。该框架包含三个主要组件：
- **ViFailback 数据集**：包含58,126个VQA对，对应5,202条真实世界操作轨迹。每个VQA对包含一个关于操作失败的问题（如“为什么抓取失败？”）以及对应的文本和视觉纠正指导。
- **ViFailback-Bench 基准**：包含11个细粒度VQA任务，分为两类：
  - **ViFailback-Bench Lite**：封闭式评估，提供预设答案选项。
  - **ViFailback-Bench Hard**：开放式评估，要求模型生成自由文本回答。
- **ViFailback-8B VLM**：基于8B参数规模的VLM，在ViFailback数据集上微调，能够同时输出故障诊断文本和纠正动作的视觉符号。

### 实验设置
- **数据集规模**：58,126个VQA对，5,202条真实操作轨迹。
- **基准任务**：11个细粒度VQA任务，涵盖故障类型识别、纠正动作预测等。
- **模型对比**：ViFailback-8B 与多个基线VLM（如LLaVA、BLIP-2等）在ViFailback-Bench上进行对比。

### 关键结果
- **ViFailback-Bench 性能**：ViFailback-8B 在ViFailback-Bench Lite和ViFailback-Bench Hard上均取得显著整体性能提升，具体数字需参考原论文。
- **视觉符号生成**：ViFailback-8B 能够生成准确的视觉符号（如箭头指向正确抓取位置），用于指导机器人纠正动作。
- **真实机器人实验**：将ViFailback-8B与VLA模型集成后，机器人成功从多种操作失败（如抓取偏移、物体滑落）中恢复，成功率提升明显。

### 结论
ViFailback 通过显式视觉符号和高质量真实世界数据集，有效提升了VLA模型的故障诊断和纠正能力。ViFailback-8B 在基准测试和真实机器人实验中均表现出色，为机器人从失败中学习提供了实用框架。项目网站提供更多细节和演示。

## Overview
Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic manipulation, yet they remain limited in failure diagnosis and learning from failures. Additionally, existing failure datasets are mostly generated programmatically in simulation, which limits their generalization to the real world. In light of these, we introduce ViFailback, a framework designed to diagnose robotic manipulation failures and provide both textual and visual correction guidance. Our framework utilizes explicit visual symbols to enhance annotation efficiency. We further release the ViFailback dataset, a large-scale collection of 58,126 Visual Question Answering (VQA) pairs along with their corresponding 5,202 real-world manipulation trajectories. Based on the dataset, we establish ViFailback-Bench, a benchmark of 11 fine-grained VQA tasks designed to assess the failure diagnosis and correction abilities of Vision-Language Models (VLMs), featuring ViFailback-Bench Lite for closed-ended and ViFailback-Bench Hard for open-ended evaluation. To demonstrate the effectiveness of our framework, we built the ViFailback-8B VLM, which not only achieves significant overall performance improvement on ViFailback-Bench but also generates visual symbols for corrective action guidance. Finally, by integrating ViFailback-8B with a VLA model, we conduct real-world robotic experiments demonstrating its ability to assist the VLA model in recovering from failures. Project Website: https://x1nyuzhou.github.io/vifailback.github.io/

## 参考
- http://arxiv.org/abs/2512.02787v3

## 개요
ViFailback 프레임워크는 기존 VLA 모델의 고장 진단 및 실패로부터 학습하는 데 있어 한계를 해결하고, 동시에 시뮬레이션으로 생성된 고장 데이터셋이 실제 세계에서 일반화가 부족한 문제를 극복하는 것을 목표로 합니다. 이 프레임워크는 명시적 시각 기호를 통해 주석 효율을 향상시키고, 58,126개의 VQA 쌍과 5,202개의 조작 궤적을 포함하는 대규모 실제 세계 데이터셋 ViFailback을 구축했습니다. 이 데이터셋을 기반으로 팀은 11개의 세분화된 VQA 작업으로 구성된 ViFailback-Bench 벤치마크를 설립했으며, 폐쇄형 평가를 위한 ViFailback-Bench Lite와 개방형 평가를 위한 ViFailback-Bench Hard로 나뉩니다. 프레임워크의 유효성을 검증하기 위해 팀은 ViFailback-8B VLM을 개발하여 벤치마크에서 상당한 성능 향상을 달성했고, 교정 동작을 위한 시각 기호를 생성할 수 있습니다. 마지막으로, ViFailback-8B를 VLA 모델과 통합함으로써 실제 로봇 실험을 통해 VLA 모델이 실패로부터 복구하도록 돕는 능력을 입증했습니다.

## 핵심 내용
### 방법
ViFailback 프레임워크의 핵심 혁신은 화살표, 강조 상자 등과 같은 명시적 시각 기호를 사용하여 조작 실패의 핵심 위치와 교정 방향을 주석 처리함으로써 데이터 주석 효율을 크게 향상시키는 것입니다. 이 프레임워크는 세 가지 주요 구성 요소를 포함합니다:
- **ViFailback 데이터셋**: 5,202개의 실제 세계 조작 궤적에 해당하는 58,126개의 VQA 쌍을 포함합니다. 각 VQA 쌍은 조작 실패에 대한 질문(예: "왜 그립이 실패했는가?")과 해당 텍스트 및 시각적 교정 지침을 포함합니다.
- **ViFailback-Bench 벤치마크**: 11개의 세분화된 VQA 작업을 포함하며, 두 가지 범주로 나뉩니다:
  - **ViFailback-Bench Lite**: 폐쇄형 평가로, 사전 정의된 답변 옵션을 제공합니다.
  - **ViFailback-Bench Hard**: 개방형 평가로, 모델이 자유 형식 텍스트 응답을 생성하도록 요구합니다.
- **ViFailback-8B VLM**: 8B 매개변수 규모의 VLM을 기반으로 ViFailback 데이터셋에서 미세 조정되어, 고장 진단 텍스트와 교정 동작을 위한 시각 기호를 동시에 출력할 수 있습니다.

### 실험 설정
- **데이터셋 규모**: 58,126개의 VQA 쌍, 5,202개의 실제 조작 궤적.
- **벤치마크 작업**: 고장 유형 식별, 교정 동작 예측 등을 포함한 11개의 세분화된 VQA 작업.
- **모델 비교**: ViFailback-8B는 여러 기준 VLM(예: LLaVA, BLIP-2 등)과 ViFailback-Bench에서 비교됩니다.

### 주요 결과
- **ViFailback-Bench 성능**: ViFailback-8B는 ViFailback-Bench Lite와 ViFailback-Bench Hard 모두에서 상당한 전체 성능 향상을 달성했으며, 구체적인 수치는 원본 논문을 참조해야 합니다.
- **시각 기호 생성**: ViFailback-8B는 로봇의 교정 동작을 안내하기 위한 정확한 시각 기호(예: 올바른 그립 위치를 가리키는 화살표)를 생성할 수 있습니다.
- **실제 로봇 실험**: ViFailback-8B를 VLA 모델과 통합한 후, 로봇은 그립 오프셋, 물체 미끄러짐 등 다양한 조작 실패로부터 성공적으로 복구했으며, 성공률이 크게 향상되었습니다.

### 결론
ViFailback은 명시적 시각 기호와 고품질 실제 세계 데이터셋을 통해 VLA 모델의 고장 진단 및 교정 능력을 효과적으로 향상시킵니다. ViFailback-8B는 벤치마크 테스트와 실제 로봇 실험 모두에서 뛰어난 성능을 보여주며, 로봇이 실패로부터 학습할 수 있는 실용적인 프레임워크를 제공합니다. 프로젝트 웹사이트에서 더 많은 세부 정보와 데모를 확인할 수 있습니다.
