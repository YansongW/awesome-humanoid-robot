---
$id: ent_benchmark_libero_plus
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: benchmark
names:
  en: LIBERO-Plus
  zh: LIBERO-Plus
  ko: LIBERO-Plus
summary:
  en: A robustness benchmark for Vision-Language-Action models that extends LIBERO with 10,030 tasks across seven perturbation
    dimensions including camera viewpoint, robot initial state, language, lighting, background, noise, and object layout.
  zh: 一个针对视觉-语言-动作模型的鲁棒性基准，扩展自 LIBERO，涵盖 10,030 项任务，覆盖相机视角、机器人初始状态、语言、光照、背景、噪声与物体布局七种扰动维度。
  ko: LIBERO를 확장한 VLA 모델 견고성 벤치마크로, 칔대 시점, 로봇 초기 상태, 언어, 조명, 배경, 노이즈, 객체 배치 등 7가지 섭동 차원에 걸쳐 10,030개 작업을 포함함.
domains:
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- robustness
- benchmark
- tabletop
- perturbation
- generalization
- evaluation
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: high
  notes: Benchmark scope and leaderboard retrieved from arXiv paper and GitHub repository. Body backfilled from entity metadata
    by scripts/backfill_critical_entities.py.
sources:
- id: src_libero_plus_paper
  type: paper
  title: 'LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models'
  url: https://arxiv.org/abs/2510.13626
  date: '2025-10-17'
  accessed_at: '2026-06-22'
- id: src_libero_plus_repo
  type: website
  title: LIBERO-Plus GitHub Repository
  url: https://github.com/sylvestf/LIBERO-plus
  date: '2025-10-17'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_benchmark_libero
  relationship: is_version_of
  description:
    en: LIBERO-Plus extends the original LIBERO benchmark with systematic perturbations.
    zh: LIBERO-Plus 在原始 LIBERO 基准基础上增加了系统性扰动。
    ko: LIBERO-Plus는 원본 LIBERO 벤치마크에 체계적 섭동을 추가하여 확장함.
- id: ent_paper_roboomni_2025
  relationship: serves
  description:
    en: LIBERO-Plus evaluates models such as RoboOmni in the broader LIBERO ecosystem.
    zh: LIBERO-Plus 在更广泛的 LIBERO 生态中评估 RoboOmni 等模型。
    ko: LIBERO-Plus는 더 넓은 LIBERO 생태계에서 RoboOmni와 같은 모델을 평가함.
theoretical_depth:
- system
---
## 概述
一个针对视觉-语言-动作模型的鲁棒性基准，扩展自 LIBERO，涵盖 10,030 项任务，覆盖相机视角、机器人初始状态、语言、光照、背景、噪声与物体布局七种扰动维度。

## 核心内容
### LIBERO-Plus的定义与定位
LIBERO-Plus属于 **评测基准** 类型，英文名称为 *LIBERO-Plus*。
一个针对视觉-语言-动作模型的鲁棒性基准，扩展自 LIBERO，涵盖 10,030 项任务，覆盖相机视角、机器人初始状态、语言、光照、背景、噪声与物体布局七种扰动维度。

### LIBERO-Plus的关键信息
以下整理了关于LIBERO-Plus的详细说明，供中英文读者参考。

## 抽象

> **生活实例**：它就像自动驾驶汽车的极端天气路测——不仅要在晴天跑，还要在雨雾、黑夜、眩光、拥堵和不同道路标线下反复测试，才能发现系统脆弱点。

> **自然语言逻辑**：LIBERO-Plus 是针对视觉-语言-动作模型鲁棒性的基准，从相机视角、机器人初始状态、语言指令、光照、背景、噪声和物体布局七个维度系统扰动任务；它揭示了 VLA 模型在面对真实环境变化时有多脆弱，为改进泛化能力提供依据。

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

## 参考
- [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus GitHub Repository](https://github.com/sylvestf/LIBERO-plus)

## 개요
시각-언어-행동 모델을 위한 강건성 벤치마크로, LIBERO에서 확장되어 10,030개의 작업을 포함하며, 카메라 시점, 로봇 초기 상태, 언어, 조명, 배경, 노이즈 및 물체 배치의 7가지 교란 차원을 다룹니다.

## 핵심 내용
### LIBERO-Plus의 정의와 위치
LIBERO-Plus는 **평가 벤치마크** 유형에 속하며, 영문 명칭은 *LIBERO-Plus*입니다.
시각-언어-행동 모델을 위한 강건성 벤치마크로, LIBERO에서 확장되어 10,030개의 작업을 포함하며, 카메라 시점, 로봇 초기 상태, 언어, 조명, 배경, 노이즈 및 물체 배치의 7가지 교란 차원을 다룹니다.

### LIBERO-Plus의 주요 정보
다음은 LIBERO-Plus에 대한 상세 설명을 중·영문 독자를 위해 정리한 내용입니다.

## 초록

> **생활 속 예시**: 이는 자율주행 자동차의 극한 기후 도로 테스트와 같습니다. 맑은 날뿐만 아니라 비, 안개, 어둠, 눈부심, 혼잡 및 다양한 도로 표시 아래에서 반복적으로 테스트해야 시스템의 취약점을 발견할 수 있습니다.

> **자연어 논리**: LIBERO-Plus는 시각-언어-행동 모델의 강건성을 위한 벤치마크로, 카메라 시점, 로봇 초기 상태, 언어 명령, 조명, 배경, 노이즈 및 물체 배치의 7가지 차원에서 작업을 체계적으로 교란합니다. 이는 VLA 모델이 실제 환경 변화에 얼마나 취약한지를 밝혀내며, 일반화 능력 개선을 위한 근거를 제공합니다.
