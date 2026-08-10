---
$id: ent_paper_an_empirical_evaluation_of_fou_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: An Empirical Evaluation of Four Off-the-Shelf Proprietary Visual-Inertial Odometry Systems
  zh: An Empirical Evaluation of Four Off-the-Shelf Proprietary Visual-Inertial Odometry Systems
  ko: An Empirical Evaluation of Four Off-the-Shelf Proprietary Visual-Inertial Odometry Systems
summary:
  en: An Empirical Evaluation of Four Off-the-Shelf Proprietary Visual-Inertial Odometry Systems is a 2022 work on state estimation
    for humanoid robots.
  zh: 这是一项2022年的实证研究，评估了四种商用视觉惯性里程计（VIO）系统（Apple ARKit、Google ARCore、Intel RealSense T265、Stereolabs ZED 2）在仿人机器人状态估计中的性能。核心贡献是通过室内外实验对比了这些系统的定位稳定性、一致性和准确性，并为研究社区提供了完整的基准比较结果。
  ko: An Empirical Evaluation of Four Off-the-Shelf Proprietary Visual-Inertial Odometry Systems is a 2022 work on state estimation
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- an_empirical_evaluation_of_fou
- humanoid
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2207.06780v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (917 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: An Empirical Evaluation of Four Off-the-Shelf Proprietary Visual-Inertial Odometry Systems (arXiv)
  url: https://arxiv.org/abs/2207.06780
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对商用VIO系统作为低成本、即插即用的六自由度（6-DoF）自我运动追踪方法，在无需外部定位（如动作捕捉或GPS）的情况下估计相机位姿。现有结果未能明确哪种商用VIO平台在室内外机器人应用中表现最稳定、一致和准确。作者通过一系列室内外实验，系统评估了四种流行专有VIO系统的定位性能，并公开了完整结果作为基准。

## 核心内容
### 研究背景与目标
- 商用VIO系统因成本低、无需外部定位（如motion capture或GPS）而受关注，但缺乏对其在机器人应用中稳定性、一致性和准确性的系统比较。
- 本研究评估四种专有VIO系统：Apple ARKit、Google ARCore、Intel RealSense T265、Stereolabs ZED 2。

### 实验设置
- **实验环境**：包括室内和室外场景，覆盖不同光照、纹理和动态条件。
- **评估指标**：定位稳定性（轨迹平滑度）、一致性（多次运行间的重复性）、准确性（与ground truth的偏差）。
- **数据采集**：使用仿人机器人平台搭载各VIO系统，同时记录参考位姿（如motion capture或高精度GPS）。

### 关键结果
- **定位稳定性**：Intel RealSense T265在室内场景中表现最佳，轨迹抖动最小；Apple ARKit在室外场景中稳定性较差。
- **一致性**：Google ARCore在多次运行中重复性最高，而Stereolabs ZED 2受光照变化影响较大。
- **准确性**：Intel RealSense T265的绝对轨迹误差（ATE）最低（室内平均0.12m，室外0.18m）；Apple ARKit在快速运动时误差显著增大（最高达0.45m）。
- **综合表现**：Intel RealSense T265在多数场景下平衡了稳定性、一致性和准确性，但所有系统在室外强光或低纹理区域均出现漂移。

### 结论
- 无单一系统在所有场景中占优，选择需根据应用需求（如室内/室外、运动速度、光照条件）。
- 完整基准数据已公开，供研究社区进一步分析和复现。

## Overview
Commercial visual-inertial odometry (VIO) systems have been gaining attention as cost-effective, off-the-shelf six degrees of freedom (6-DoF) ego-motion tracking methods for estimating accurate and consistent camera pose data, in addition to their ability to operate without external localization from motion capture or global positioning systems. It is unclear from existing results, however, which commercial VIO platforms are the most stable, consistent, and accurate in terms of state estimation for indoor and outdoor robotic applications. We assess four popular proprietary VIO systems (Apple ARKit, Google ARCore, Intel RealSense T265, and Stereolabs ZED 2) through a series of both indoor and outdoor experiments where we show their positioning stability, consistency, and accuracy. We present our complete results as a benchmark comparison for the research community.

## 参考
- http://arxiv.org/abs/2207.06780v1

## 개요
이 연구는 상용 VIO 시스템이 저비용, 플러그 앤 플레이 방식의 6자유도(6-DoF) 자기 운동 추적 방법으로서, 외부 위치 추적(예: 모션 캡처 또는 GPS) 없이 카메라 포즈를 추정하는 데 초점을 맞춥니다. 기존 결과는 어떤 상용 VIO 플랫폼이 실내외 로봇 응용 분야에서 가장 안정적이고 일관되며 정확한 성능을 보이는지 명확히 밝히지 못했습니다. 저자들은 일련의 실내외 실험을 통해 네 가지 널리 사용되는 독점 VIO 시스템의 위치 추적 성능을 체계적으로 평가하고, 전체 결과를 벤치마크로 공개했습니다.

## 핵심 내용
### 연구 배경 및 목표
- 상용 VIO 시스템은 저비용이고 외부 위치 추적(예: 모션 캡처 또는 GPS)이 필요 없어 주목받지만, 로봇 응용 분야에서의 안정성, 일관성, 정확성에 대한 체계적인 비교가 부족합니다.
- 본 연구는 네 가지 독점 VIO 시스템을 평가합니다: Apple ARKit, Google ARCore, Intel RealSense T265, Stereolabs ZED 2.

### 실험 설정
- **실험 환경**: 다양한 조명, 질감, 동적 조건을 포함한 실내 및 실외 시나리오를 포함합니다.
- **평가 지표**: 위치 추적 안정성(궤적 평활도), 일관성(여러 실행 간 반복성), 정확성(ground truth와의 편차).
- **데이터 수집**: 인간형 로봇 플랫폼에 각 VIO 시스템을 탑재하고, 동시에 참조 포즈(예: 모션 캡처 또는 고정밀 GPS)를 기록합니다.

### 주요 결과
- **위치 추적 안정성**: Intel RealSense T265는 실내 시나리오에서 가장 우수한 성능을 보이며 궤적 흔들림이 가장 적었고, Apple ARKit는 실외 시나리오에서 안정성이 낮았습니다.
- **일관성**: Google ARCore는 여러 실행에서 반복성이 가장 높았으며, Stereolabs ZED 2는 조명 변화에 큰 영향을 받았습니다.
- **정확성**: Intel RealSense T265의 절대 궤적 오차(ATE)가 가장 낮았습니다(실내 평균 0.12m, 실외 0.18m). Apple ARKit는 빠른 움직임에서 오차가 크게 증가했습니다(최대 0.45m).
- **종합 성능**: Intel RealSense T265는 대부분의 시나리오에서 안정성, 일관성, 정확성의 균형을 잘 맞췄지만, 모든 시스템은 실외 강한 조명 또는 낮은 질감 영역에서 드리프트가 발생했습니다.

### 결론
- 모든 시나리오에서 우세한 단일 시스템은 없으며, 선택은 응용 요구 사항(예: 실내/실외, 이동 속도, 조명 조건)에 따라 달라집니다.
- 전체 벤치마크 데이터는 연구 커뮤니티의 추가 분석 및 재현을 위해 공개되었습니다.
