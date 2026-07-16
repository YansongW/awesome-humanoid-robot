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
  zh: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution (DeeR-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, BNRist, ByteDance, and
    published at NIPS 2024.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.02359v1.
sources:
- id: src_001
  type: website
  title: DeeR-VLA source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
MLLMs have demonstrated remarkable comprehension and reasoning capabilities with complex language and visual data. These advances have spurred the vision of establishing a generalist robotic MLLM proficient in understanding complex human instructions and accomplishing various embodied tasks. However, developing MLLMs for real-world robots is challenging due to the typically limited computation and memory capacities available on robotic platforms. In contrast, the inference of MLLMs involves storing billions of parameters and performing tremendous computation, imposing significant hardware demands. In our paper, we propose a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model (DeeR-VLA, or simply DeeR) that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Additionally, we develop novel algorithms that establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (i.e., power consumption), as well as peak computational consumption (i.e., latency) and GPU memory usage. These enhancements ensure that DeeR operates efficiently under varying resource constraints while maintaining competitive performance. On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. Code and checkpoints are available at https://github.com/yueyang130/DeeR-VLA.

## 核心内容
MLLMs have demonstrated remarkable comprehension and reasoning capabilities with complex language and visual data. These advances have spurred the vision of establishing a generalist robotic MLLM proficient in understanding complex human instructions and accomplishing various embodied tasks. However, developing MLLMs for real-world robots is challenging due to the typically limited computation and memory capacities available on robotic platforms. In contrast, the inference of MLLMs involves storing billions of parameters and performing tremendous computation, imposing significant hardware demands. In our paper, we propose a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model (DeeR-VLA, or simply DeeR) that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Additionally, we develop novel algorithms that establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (i.e., power consumption), as well as peak computational consumption (i.e., latency) and GPU memory usage. These enhancements ensure that DeeR operates efficiently under varying resource constraints while maintaining competitive performance. On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. Code and checkpoints are available at https://github.com/yueyang130/DeeR-VLA.

## 参考
- http://arxiv.org/abs/2411.02359v1

## Overview
MLLMs have demonstrated remarkable comprehension and reasoning capabilities with complex language and visual data. These advances have spurred the vision of establishing a generalist robotic MLLM proficient in understanding complex human instructions and accomplishing various embodied tasks. However, developing MLLMs for real-world robots is challenging due to the typically limited computation and memory capacities available on robotic platforms. In contrast, the inference of MLLMs involves storing billions of parameters and performing tremendous computation, imposing significant hardware demands. In our paper, we propose a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model (DeeR-VLA, or simply DeeR) that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Additionally, we develop novel algorithms that establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (i.e., power consumption), as well as peak computational consumption (i.e., latency) and GPU memory usage. These enhancements ensure that DeeR operates efficiently under varying resource constraints while maintaining competitive performance. On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. Code and checkpoints are available at https://github.com/yueyang130/DeeR-VLA.

## Content
MLLMs have demonstrated remarkable comprehension and reasoning capabilities with complex language and visual data. These advances have spurred the vision of establishing a generalist robotic MLLM proficient in understanding complex human instructions and accomplishing various embodied tasks. However, developing MLLMs for real-world robots is challenging due to the typically limited computation and memory capacities available on robotic platforms. In contrast, the inference of MLLMs involves storing billions of parameters and performing tremendous computation, imposing significant hardware demands. In our paper, we propose a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model (DeeR-VLA, or simply DeeR) that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Additionally, we develop novel algorithms that establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (i.e., power consumption), as well as peak computational consumption (i.e., latency) and GPU memory usage. These enhancements ensure that DeeR operates efficiently under varying resource constraints while maintaining competitive performance. On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. Code and checkpoints are available at https://github.com/yueyang130/DeeR-VLA.

## 개요
MLLM은 복잡한 언어 및 시각 데이터에 대해 뛰어난 이해와 추론 능력을 보여주었습니다. 이러한 발전은 복잡한 인간 명령을 이해하고 다양한 구현 작업을 수행하는 데 능숙한 범용 로봇 MLLM을 구축하려는 비전을 촉진했습니다. 그러나 실제 로봇을 위한 MLLM을 개발하는 것은 로봇 플랫폼에서 일반적으로 제한된 계산 및 메모리 용량으로 인해 어렵습니다. 반면, MLLM의 추론은 수십억 개의 매개변수를 저장하고 막대한 계산을 수행해야 하므로 상당한 하드웨어 요구 사항이 발생합니다. 본 논문에서는 각 상황에 따라 활성화된 MLLM의 크기를 자동으로 조정하는 로봇 시각-언어-행동 모델을 위한 동적 조기 종료 프레임워크(DeeR-VLA, 간단히 DeeR)를 제안합니다. 이 접근 방식은 MLLM의 다중 종료 아키텍처를 활용하여 특정 상황에 적절한 크기의 모델이 활성화되면 처리를 종료하여 추가적인 중복 계산을 방지합니다. 또한 평균 계산 비용(즉, 전력 소비), 최대 계산 소비(즉, 지연 시간) 및 GPU 메모리 사용량과 같은 사전 정의된 요구 사항에 따라 DeeR의 조기 종료 기준을 설정하는 새로운 알고리즘을 개발합니다. 이러한 개선 사항은 DeeR이 경쟁력 있는 성능을 유지하면서 다양한 리소스 제약 조건에서 효율적으로 작동하도록 보장합니다. CALVIN 로봇 조작 벤치마크에서 DeeR은 성능 저하 없이 LLM의 계산 비용을 5.2-6.5배, LLM의 GPU 메모리를 2-6배 크게 줄였습니다. 코드와 체크포인트는 https://github.com/yueyang130/DeeR-VLA에서 확인할 수 있습니다.

## 핵심 내용
MLLM은 복잡한 언어 및 시각 데이터에 대해 뛰어난 이해와 추론 능력을 보여주었습니다. 이러한 발전은 복잡한 인간 명령을 이해하고 다양한 구현 작업을 수행하는 데 능숙한 범용 로봇 MLLM을 구축하려는 비전을 촉진했습니다. 그러나 실제 로봇을 위한 MLLM을 개발하는 것은 로봇 플랫폼에서 일반적으로 제한된 계산 및 메모리 용량으로 인해 어렵습니다. 반면, MLLM의 추론은 수십억 개의 매개변수를 저장하고 막대한 계산을 수행해야 하므로 상당한 하드웨어 요구 사항이 발생합니다. 본 논문에서는 각 상황에 따라 활성화된 MLLM의 크기를 자동으로 조정하는 로봇 시각-언어-행동 모델을 위한 동적 조기 종료 프레임워크(DeeR-VLA, 간단히 DeeR)를 제안합니다. 이 접근 방식은 MLLM의 다중 종료 아키텍처를 활용하여 특정 상황에 적절한 크기의 모델이 활성화되면 처리를 종료하여 추가적인 중복 계산을 방지합니다. 또한 평균 계산 비용(즉, 전력 소비), 최대 계산 소비(즉, 지연 시간) 및 GPU 메모리 사용량과 같은 사전 정의된 요구 사항에 따라 DeeR의 조기 종료 기준을 설정하는 새로운 알고리즘을 개발합니다. 이러한 개선 사항은 DeeR이 경쟁력 있는 성능을 유지하면서 다양한 리소스 제약 조건에서 효율적으로 작동하도록 보장합니다. CALVIN 로봇 조작 벤치마크에서 DeeR은 성능 저하 없이 LLM의 계산 비용을 5.2-6.5배, LLM의 GPU 메모리를 2-6배 크게 줄였습니다. 코드와 체크포인트는 https://github.com/yueyang130/DeeR-VLA에서 확인할 수 있습니다.
