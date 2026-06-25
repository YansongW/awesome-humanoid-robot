---
$id: "ent_benchmark_humanoid_foundation_model"
$schema: "../../../../../data/schema/v1/entry_schema.json"
$version: 1

type: "benchmark"

names:
  en: "Humanoid Foundation Model Benchmark"
  zh: "人形机器人基础模型基准"
  ko: "휴리노이드 파울데이션 모델 벤치마크"

summary:
  en: "An independent, publicly accessible benchmark that rates and compares AI foundation models for humanoid robots across ten capability dimensions, including locomotion, manipulation, reasoning, and sim-to-real transfer."
  zh: "一个独立、公开可访问的基准，从十个能力维度对人形机器人 AI 基础模型进行评级和比较，包括移动、操作、推理和仿真到现实迁移。"
  ko: "휴리노이드 로봇을 위한 AI 파울데이션 모델을 이동, 조작, 추론, 시뮬레이션-투-리얼 전이 등 10가지 역량 차원에서 평가하고 비교하는 독립적이고 공개적으로 접근 가능한 벤치마크."

domains:
  - "10_evaluation_benchmarks"
  - "11_applications_markets"

layers:
  - "validation_markets"

functional_roles:
  - "knowledge"
  - "market"

tags:
  - "benchmark"
  - "foundation_model"
  - "humanoid"
  - "vla"
  - "comparison"
  - "sim_to_real"

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "AI-extracted from the benchmark launch page and model directory page; methodology and model counts are consistent with the source. Individual model scores are not independently verified."

sources:
  - id: "src_humanoid_foundation_model_benchmark_2026"
    type: "website"
    title: "Humanoid Foundation Models – humanoid.guide"
    url: "https://humanoid.guide/foundation-models/"
    date: "2026-04-14"
    accessed_at: "2026-06-25"
  - id: "src_humanoid_foundation_model_benchmark_launch_2026"
    type: "press_release"
    title: "Humanoid Foundation Model Benchmark Launch"
    url: "https://humanoid.guide/humanoid-foundation-model-benchmark-launch/"
    date: "2026-04-14"
    accessed_at: "2026-06-25"

related_entities:
  - id: "ent_paper_openvla_2024"
    relationship: "cites"
    description:
      en: "The benchmark directory lists and rates OpenVLA among the evaluated VLA models."
      zh: "该基准目录将 OpenVLA 列为参评的 VLA 模型之一并进行评级。"
      ko: "해당 벤치마크 디렉토리는 OpenVLA를 평가된 VLA 모델 중 하나로 나열하고 등급을 매김."
  - id: "ent_paper_pi0_2024"
    relationship: "cites"
    description:
      en: "The benchmark directory lists and rates π0 among the evaluated VLA models."
      zh: "该基准目录将 π0 列为参评的 VLA 模型之一并进行评级。"
      ko: "해당 벤치마크 디렉토리는 π0를 평가된 VLA 모델 중 하나로 나열하고 등급을 매김."
---

# Humanoid Foundation Model Benchmark

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像一份公开的“AI 模型高考排行榜”——从走路、用手、语言理解到仿真到现实迁移等多个科目，给人形机器人用的大模型打分排名。

> **自然语言逻辑**：人形机器人基础模型基准是一个独立、公开的平台，从移动、全身控制、双手协调、灵巧操作、推理、长程规划等十个维度评估和比较面向人形机器人的基础模型；它帮助研究者和从业者判断哪些模型已具备部署潜力，并暴露当前能力短板。

## Overview

The Humanoid Foundation Model Benchmark, launched by humanoid.guide on 14 April 2026, is an independent, free, and publicly accessible comparison platform for AI foundation models designed to control humanoid robots. It evaluates 40+ models from organizations such as NVIDIA, Google DeepMind, Tesla, Physical Intelligence, Figure AI, and Unitree.

## Evaluation Framework

Models are scored on a five-point scale across ten capability dimensions:

1. Locomotion
2. Whole-body control
3. Bimanual coordination
4. Dexterous manipulation
5. Navigation
6. Reasoning
7. Sim-to-real transfer
8. Cross-embodiment generalization
9. Real-time inference
10. Long-horizon planning

Models are categorized as VLA models, world models, or reward models. Filters allow users to narrow results by open weights, on-device inference, omni-body vs. humanoid-only support, and other features.

## Relevance to the VLA Workstream

The benchmark provides a structured, cross-model view of the VLA landscape specifically for humanoid embodiments. It helps identify which open or closed VLAs are considered deployment-ready for humanoid tasks and surfaces capability gaps such as long-horizon planning and sim-to-real transfer.
