---
$id: ent_paper_being_m05_a_real_time_controll_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model'
  zh: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model'
  ko: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model'
summary:
  en: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model is a 2025 work on human motion analysis and synthesis
    for humanoid robots.'
  zh: Being-M0.5 是 2025 年提出的首个实时可控视觉-语言-运动模型，由 BeingBeyond 团队基于自建的最大规模人体运动数据集 HuMo100M 开发。其核心贡献在于通过创新的部位感知残差量化技术，实现了对生成运动中单个身体部位的精细控制，并在多项运动生成基准上达到最优性能。
  ko: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model is a 2025 work on human motion analysis and synthesis
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- being_m05
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.07863v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model (arXiv)'
  url: https://arxiv.org/abs/2508.07863
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model project page'
  url: https://beingbeyond.github.io/Being-M0.5/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-运动模型在可控性方面存在五大瓶颈：难以响应多样的人类指令、姿态初始化能力有限、长序列生成效果差、无法处理未见场景、缺乏对身体部位的细粒度控制。Being-M0.5 通过引入 HuMo100M 数据集和部位感知残差量化技术，首次实现了实时可控的运动生成。该模型在多个基准测试中展现出领先性能，并通过效率分析验证了其实时处理能力，为实际部署提供了关键设计见解。

## 核心内容
### 核心问题
现有 VLMM 在可控性上存在五大缺陷：
- 无法充分响应用户的多样化指令
- 姿态初始化能力受限
- 长序列生成质量差
- 对未见场景泛化不足
- 缺乏对身体各部位的独立控制

### 数据集：HuMo100M
- 规模：包含超过 500 万条自采集运动序列，总计 1 亿条多任务指令实例
- 特色：提供详细的部位级标注，填补了现有数据集在细粒度控制方面的空白
- 用途：支撑模型训练与多任务学习

### 方法创新
- **部位感知残差量化**：一种新型运动标记化技术，通过残差编码实现对头部、手臂、躯干等独立身体部位的精确控制
- 模型架构支持实时推理，在生成过程中可动态调整指定部位的运动参数

### 实验与性能
- 在多个运动生成基准上达到 SOTA 性能
- 效率分析证实：模型具备实时处理能力，满足实际应用延迟要求
- 消融实验验证了部位感知量化对控制精度的显著提升

### 结论与意义
Being-M0.5 与 HuMo100M 共同推动了运动生成技术从实验室走向实际部署，为机器人、动画、人机交互等领域提供了可控、实时的解决方案。项目页面：https://beingbeyond.github.io/Being-M0.5

## Overview
Human motion generation has emerged as a critical technology with transformative potential for real-world applications. However, existing vision-language-motion models (VLMMs) face significant limitations that hinder their practical deployment. We identify controllability as a main bottleneck, manifesting in five key aspects: inadequate response to diverse human commands, limited pose initialization capabilities, poor performance on long-term sequences, insufficient handling of unseen scenarios, and lack of fine-grained control over individual body parts. To overcome these limitations, we present Being-M0.5, the first real-time, controllable VLMM that achieves state-of-the-art performance across multiple motion generation tasks. Our approach is built upon HuMo100M, the largest and most comprehensive human motion dataset to date, comprising over 5 million self-collected motion sequences, 100 million multi-task instructional instances, and detailed part-level annotations that address a critical gap in existing datasets. We introduce a novel part-aware residual quantization technique for motion tokenization that enables precise, granular control over individual body parts during generation. Extensive experimental validation demonstrates Being-M0.5's superior performance across diverse motion benchmarks, while comprehensive efficiency analysis confirms its real-time capabilities. Our contributions include design insights and detailed computational analysis to guide future development of practical motion generators. We believe that HuMo100M and Being-M0.5 represent significant advances that will accelerate the adoption of motion generation technologies in real-world applications. The project page is available at https://beingbeyond.github.io/Being-M0.5.

## 개요
인간 동작 생성(Human motion generation)은 실제 애플리케이션에 혁신적인 잠재력을 지닌 핵심 기술로 부상했습니다. 그러나 기존의 비전-언어-동작 모델(VLMM)은 실제 배포를 저해하는 상당한 한계에 직면해 있습니다. 우리는 제어 가능성(controllability)을 주요 병목 현상으로 식별하며, 이는 다섯 가지 핵심 측면에서 나타납니다: 다양한 인간 명령에 대한 부적절한 대응, 제한된 포즈 초기화 능력, 장기 시퀀스에 대한 낮은 성능, 보지 못한 시나리오 처리 부족, 개별 신체 부위에 대한 세밀한 제어 부족입니다. 이러한 한계를 극복하기 위해 우리는 Being-M0.5를 제시합니다. 이는 최초의 실시간 제어 가능한 VLMM으로, 여러 동작 생성 작업에서 최첨단 성능을 달성합니다. 우리의 접근 방식은 현재까지 가장 크고 포괄적인 인간 동작 데이터셋인 HuMo100M을 기반으로 구축되었으며, 500만 개 이상의 자체 수집 동작 시퀀스, 1억 개의 멀티태스크 명령 인스턴스, 기존 데이터셋의 중요한 격차를 해소하는 상세한 부위별 주석을 포함합니다. 우리는 동작 토큰화를 위한 새로운 부위 인식 잔차 양자화(part-aware residual quantization) 기술을 도입하여 생성 중 개별 신체 부위에 대한 정밀하고 세분화된 제어를 가능하게 합니다. 광범위한 실험 검증을 통해 다양한 동작 벤치마크에서 Being-M0.5의 우수한 성능을 입증했으며, 포괄적인 효율성 분석을 통해 실시간 기능을 확인했습니다. 우리의 기여에는 실용적인 동작 생성기의 미래 개발을 안내하기 위한 설계 통찰력과 상세한 계산 분석이 포함됩니다. 우리는 HuMo100M과 Being-M0.5가 실제 애플리케이션에서 동작 생성 기술의 채택을 가속화할 중요한 진전을 나타낸다고 믿습니다. 프로젝트 페이지는 https://beingbeyond.github.io/Being-M0.5에서 확인할 수 있습니다.

## 핵심 내용
인간 동작 생성은 실제 애플리케이션에 혁신적인 잠재력을 지닌 핵심 기술로 부상했습니다. 그러나 기존의 비전-언어-동작 모델(VLMM)은 실제 배포를 저해하는 상당한 한계에 직면해 있습니다. 우리는 제어 가능성을 주요 병목 현상으로 식별하며, 이는 다섯 가지 핵심 측면에서 나타납니다: 다양한 인간 명령에 대한 부적절한 대응, 제한된 포즈 초기화 능력, 장기 시퀀스에 대한 낮은 성능, 보지 못한 시나리오 처리 부족, 개별 신체 부위에 대한 세밀한 제어 부족입니다. 이러한 한계를 극복하기 위해 우리는 Being-M0.5를 제시합니다. 이는 최초의 실시간 제어 가능한 VLMM으로, 여러 동작 생성 작업에서 최첨단 성능을 달성합니다. 우리의 접근 방식은 현재까지 가장 크고 포괄적인 인간 동작 데이터셋인 HuMo100M을 기반으로 구축되었으며, 500만 개 이상의 자체 수집 동작 시퀀스, 1억 개의 멀티태스크 명령 인스턴스, 기존 데이터셋의 중요한 격차를 해소하는 상세한 부위별 주석을 포함합니다. 우리는 동작 토큰화를 위한 새로운 부위 인식 잔차 양자화 기술을 도입하여 생성 중 개별 신체 부위에 대한 정밀하고 세분화된 제어를 가능하게 합니다. 광범위한 실험 검증을 통해 다양한 동작 벤치마크에서 Being-M0.5의 우수한 성능을 입증했으며, 포괄적인 효율성 분석을 통해 실시간 기능을 확인했습니다. 우리의 기여에는 실용적인 동작 생성기의 미래 개발을 안내하기 위한 설계 통찰력과 상세한 계산 분석이 포함됩니다. 우리는 HuMo100M과 Being-M0.5가 실제 애플리케이션에서 동작 생성 기술의 채택을 가속화할 중요한 진전을 나타낸다고 믿습니다. 프로젝트 페이지는 https://beingbeyond.github.io/Being-M0.5에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2508.07863v1
