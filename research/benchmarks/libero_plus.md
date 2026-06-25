---
$id: "ent_benchmark_libero_plus"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "benchmark"

names:
  en: "LIBERO-Plus"
  zh: "LIBERO-Plus"
  ko: "LIBERO-Plus"

summary:
  en: "A robustness benchmark for Vision-Language-Action models that extends LIBERO with 10,030 tasks across seven perturbation dimensions including camera viewpoint, robot initial state, language, lighting, background, noise, and object layout."
  zh: "一个针对视觉-语言-动作模型的鲁棒性基准，扩展自 LIBERO，涵盖 10,030 项任务，覆盖相机视角、机器人初始状态、语言、光照、背景、噪声与物体布局七种扰动维度。"
  ko: "LIBERO를 확장한 VLA 모델 견고성 벤치마크로, 칔대 시점, 로봇 초기 상태, 언어, 조명, 배경, 노이즈, 객체 배치 등 7가지 섭동 차원에 걸쳐 10,030개 작업을 포함함."

domains:
  - "07_ai_models_algorithms"
  - "10_evaluation_benchmarks"

layers:
  - "intelligence"
  - "validation_markets"

functional_roles:
  - "knowledge"
  - "intelligence"

tags:
  - "vla"
  - "robustness"
  - "benchmark"
  - "tabletop"
  - "perturbation"
  - "generalization"
  - "evaluation"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Benchmark scope and leaderboard retrieved from arXiv paper and GitHub repository."

sources:
  - id: "src_libero_plus_paper"
    type: "paper"
    title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
    url: "https://arxiv.org/abs/2510.13626"
    date: "2025-10-17"
    accessed_at: "2026-06-22"
  - id: "src_libero_plus_repo"
    type: "website"
    title: "LIBERO-Plus GitHub Repository"
    url: "https://github.com/sylvestf/LIBERO-plus"
    date: "2025-10-17"
    accessed_at: "2026-06-22"

related_entities:
  - id: "ent_benchmark_libero"
    relationship: "is_version_of"
    description:
      en: "LIBERO-Plus extends the original LIBERO benchmark with systematic perturbations."
      zh: "LIBERO-Plus 在原始 LIBERO 基准基础上增加了系统性扰动。"
      ko: "LIBERO-Plus는 원본 LIBERO 벤치마크에 체계적 섭동을 추가하여 확장함."
  - id: "ent_paper_roboomni_2025"
    relationship: "serves"
    description:
      en: "LIBERO-Plus evaluates models such as RoboOmni in the broader LIBERO ecosystem."
      zh: "LIBERO-Plus 在更广泛的 LIBERO 生态中评估 RoboOmni 等模型。"
      ko: "LIBERO-Plus는 더 넓은 LIBERO 생태계에서 RoboOmni와 같은 모델을 평가함."
---

# LIBERO-Plus

## Overview

LIBERO-Plus is a robustness-focused extension of the LIBERO benchmark. It systematically exposes vulnerabilities in VLA models by evaluating them under controlled perturbations across seven dimensions.

## Seven Perturbation Dimensions

1. **Objects Layout**: confounding objects and target object displacement
2. **Camera Viewpoints**: position, orientation, and field-of-view changes
3. **Robot Initial States**: manipulator initial pose variations
4. **Language Instructions**: LLM-based instruction rewriting
5. **Light Conditions**: intensity, direction, color, and shadow variations
6. **Background Textures**: scene and surface appearance changes
7. **Sensor Noise**: photometric distortions and image degradation

## Key Findings

- VLA models show extreme sensitivity to camera viewpoints and robot initial states, with performance dropping from ~95% to below 30% under modest perturbations.
- Models often ignore language instructions, behaving more like Vision-Action models.
- Combined perturbations reveal complex interaction effects beyond independent factors.

## Leaderboard Highlights

| Model | Average |
|-------|---------|
| OpenVLA | 15.6% |
| π0 | 53.6% |
| π0-Fast | 61.6% |
| OpenVLA-OFT+ (mix-SFT on LIBERO-plus) | **79.6%** |

## Relevance to Humanoid Robotics

Robustness evaluation is critical for humanoid deployment in unstructured human environments. LIBERO-Plus provides a methodology for stress-testing perception-language grounding under visual and linguistic variation, though its tasks are still tabletop arm manipulation rather than whole-body locomotion.
