---
$id: ent_paper_yue_deer_vla_dynamic_inference_of_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution'
  zh: DeeR-VLA
  ko: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution'
summary:
  en: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution (DeeR-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, BNRist, ByteDance, and
    published at NIPS 2024.'
  zh: DeeR-VLA 是清华大学、BNRist 与字节跳动联合提出的动态推理框架，旨在解决多模态大语言模型在机器人平台上计算与内存资源受限的问题。其核心贡献在于通过多出口架构实现模型规模的自动调整，在 CALVIN 基准上实现 LLM
    计算成本降低 5.2-6.5 倍、GPU 内存减少 2-6 倍且不牺牲性能。
  ko: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution (DeeR-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, BNRist, ByteDance, and
    published at NIPS 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deer_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.02359v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (711 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: DeeR-VLA source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
DeeR-VLA 针对机器人执行场景中 MLLM 推理时参数规模庞大、硬件需求高的问题，提出动态早退机制。该框架在 MLLM 中嵌入多出口结构，使模型能根据当前任务复杂度自动选择合适大小的激活参数，避免冗余计算。同时，研究团队开发了基于平均计算成本、峰值计算消耗及 GPU 内存使用等预设条件的早退判定算法，确保在不同资源约束下保持高效运行。实验表明，该方法在 CALVIN 基准上显著降低计算与内存开销，且性能未受影响。

## 核心内容
### 方法概述
- **动态早退框架**：DeeR-VLA 在 MLLM 中引入多出口架构，允许模型在推理过程中根据任务复杂度提前终止计算，仅激活必要规模的参数。
- **早退判定算法**：基于预设条件（如平均计算成本、峰值计算消耗、GPU 内存使用）设计终止准则，确保在资源约束下动态调整模型规模。

### 实验设置
- **基准测试**：在 CALVIN 机器人操作基准上进行评估，该基准包含多种复杂指令与操作任务。
- **对比基线**：与标准 MLLM 推理方法对比，重点衡量计算成本与 GPU 内存消耗。

### 关键结果
- **计算成本**：LLM 部分计算量降低 5.2-6.5 倍。
- **GPU 内存**：LLM 部分内存占用减少 2-6 倍。
- **性能保持**：在 CALVIN 基准上，DeeR-VLA 的操控成功率与完整 MLLM 推理持平，未出现性能下降。

### 结论
DeeR-VLA 通过动态早退机制有效缓解了 MLLM 在机器人平台上的资源瓶颈，为资源受限场景下的多模态大模型部署提供了可行方案。代码与模型权重已开源。

## Overview
MLLMs have demonstrated remarkable comprehension and reasoning capabilities with complex language and visual data. These advances have spurred the vision of establishing a generalist robotic MLLM proficient in understanding complex human instructions and accomplishing various embodied tasks. However, developing MLLMs for real-world robots is challenging due to the typically limited computation and memory capacities available on robotic platforms. In contrast, the inference of MLLMs involves storing billions of parameters and performing tremendous computation, imposing significant hardware demands. In our paper, we propose a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model (DeeR-VLA, or simply DeeR) that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Additionally, we develop novel algorithms that establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (i.e., power consumption), as well as peak computational consumption (i.e., latency) and GPU memory usage. These enhancements ensure that DeeR operates efficiently under varying resource constraints while maintaining competitive performance. On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. Code and checkpoints are available at https://github.com/yueyang130/DeeR-VLA.

## 参考
- http://arxiv.org/abs/2411.02359v1

## 개요
DeeR-VLA는 로봇 실행 시나리오에서 MLLM 추론 시 매개변수 규모가 크고 하드웨어 요구 사항이 높은 문제를 해결하기 위해 동적 조기 종료 메커니즘을 제안합니다. 이 프레임워크는 MLLM에 다중 출력 구조를 내장하여 모델이 현재 작업 복잡도에 따라 적절한 크기의 활성 매개변수를 자동으로 선택하고 불필요한 계산을 방지합니다. 동시에 연구팀은 평균 계산 비용, 최대 계산 소비, GPU 메모리 사용량 등의 사전 설정 조건을 기반으로 한 조기 종료 판단 알고리즘을 개발하여 다양한 리소스 제약 조건에서 효율적인 실행을 보장합니다. 실험 결과, 이 방법은 CALVIN 벤치마크에서 계산 및 메모리 오버헤드를 크게 줄이면서 성능 저하가 없음을 보여줍니다.

## 핵심 내용
### 방법 개요
- **동적 조기 종료 프레임워크**: DeeR-VLA는 MLLM에 다중 출력 아키텍처를 도입하여 모델이 추론 과정에서 작업 복잡도에 따라 계산을 조기에 종료하고 필요한 규모의 매개변수만 활성화할 수 있도록 합니다.
- **조기 종료 판단 알고리즘**: 평균 계산 비용, 최대 계산 소비, GPU 메모리 사용량 등의 사전 설정 조건을 기반으로 종료 기준을 설계하여 리소스 제약 하에서 모델 규모를 동적으로 조정합니다.

### 실험 설정
- **벤치마크 테스트**: 다양한 복잡한 지시 및 조작 작업을 포함하는 CALVIN 로봇 조작 벤치마크에서 평가를 수행합니다.
- **비교 기준선**: 표준 MLLM 추론 방법과 비교하여 계산 비용과 GPU 메모리 소비를 중점적으로 측정합니다.

### 주요 결과
- **계산 비용**: LLM 부분의 계산량이 5.2-6.5배 감소합니다.
- **GPU 메모리**: LLM 부분의 메모리 점유율이 2-6배 감소합니다.
- **성능 유지**: CALVIN 벤치마크에서 DeeR-VLA의 조작 성공률이 완전한 MLLM 추론과 동일하며 성능 저하가 없습니다.

### 결론
DeeR-VLA는 동적 조기 종료 메커니즘을 통해 로봇 플랫폼에서 MLLM의 리소스 병목 현상을 효과적으로 완화하며, 리소스 제약 시나리오에서의 다중 모달 대형 모델 배포를 위한 실현 가능한 솔루션을 제공합니다. 코드와 모델 가중치는 오픈소스로 공개되었습니다.
