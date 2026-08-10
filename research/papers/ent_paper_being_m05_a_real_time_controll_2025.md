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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.07863v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (732 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2508.07863v1

## 개요
기존 비전-언어-모션 모델은 제어 가능성 측면에서 다섯 가지 주요 병목 현상이 있습니다: 다양한 인간 명령에 응답하기 어렵고, 자세 초기화 능력이 제한적이며, 긴 시퀀스 생성 품질이 낮고, 보지 못한 장면을 처리하지 못하며, 신체 부위별 세밀한 제어가 부족합니다. Being-M0.5는 HuMo100M 데이터셋과 부위 인식 잔차 양자화 기술을 도입하여 최초로 실시간 제어 가능한 모션 생성을 구현했습니다. 이 모델은 여러 벤치마크에서 선도적인 성능을 보여주며, 효율성 분석을 통해 실시간 처리 능력을 검증하여 실제 배포를 위한 핵심 설계 통찰력을 제공합니다.

## 핵심 내용
### 핵심 문제
기존 VLMM은 제어 가능성에서 다섯 가지 주요 결함이 있습니다:
- 사용자의 다양한 명령에 충분히 응답하지 못함
- 자세 초기화 능력이 제한됨
- 긴 시퀀스 생성 품질이 낮음
- 보지 못한 장면에 대한 일반화 부족
- 신체 각 부위의 독립적 제어 부재

### 데이터셋: HuMo100M
- 규모: 500만 개 이상의 자체 수집 모션 시퀀스를 포함하며, 총 1억 개의 멀티태스크 명령 인스턴스로 구성
- 특징: 세부 부위 수준 주석을 제공하여 기존 데이터셋의 세밀한 제어 측면 공백을 메움
- 용도: 모델 훈련 및 멀티태스크 학습 지원

### 방법 혁신
- **부위 인식 잔차 양자화**: 잔차 인코딩을 통해 머리, 팔, 몸통 등 독립적인 신체 부위의 정밀한 제어를 구현하는 새로운 모션 토큰화 기술
- 모델 아키텍처는 실시간 추론을 지원하며, 생성 과정에서 지정된 부위의 모션 파라미터를 동적으로 조정 가능

### 실험 및 성능
- 여러 모션 생성 벤치마크에서 SOTA 성능 달성
- 효율성 분석 확인: 모델은 실시간 처리 능력을 갖추어 실제 애플리케이션의 지연 시간 요구 사항을 충족
- 절제 실험을 통해 부위 인식 양자화가 제어 정밀도를 크게 향상시킴을 검증

### 결론 및 의의
Being-M0.5와 HuMo100M은 함께 모션 생성 기술을 실험실에서 실제 배포로 이끌며, 로봇, 애니메이션, 인간-컴퓨터 상호작용 등 분야에 제어 가능하고 실시간적인 솔루션을 제공합니다. 프로젝트 페이지: https://beingbeyond.github.io/Being-M0.5
