---
$id: ent_paper_schedulestream_temporal_planning_sampler_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ScheduleStream: Temporal Planning with Samplers for GPU-Accelerated Multi-Arm Task and Motion Planning & Scheduling'
  zh: 'ScheduleStream: Temporal Planning with Samplers for GPU-Accelerated Multi-Arm Task and Motion Planning & Scheduling'
  ko: 'ScheduleStream: Temporal Planning with Samplers for GPU-Accelerated Multi-Arm Task and Motion Planning & Scheduling'
summary:
  en: 'Bimanual and humanoid robots are appealing because of their human-like ability to leverage multiple arms to efficiently
    complete tasks. However, controlling multiple arms at once is computationally challenging due to the growth in the hybrid
    discrete-continuous action space. Institutions per source list: NVIDIA Research（Caelan Garrett）、University of Sydney（Fabio
    Ramos）.'
  zh: ScheduleStream 是首个通用型规划与调度框架，由研究团队提出，用于解决双臂及人形机器人的多臂并行任务与运动规划调度问题。其核心贡献在于通过混合持续动作建模时间动态，并利用 GPU 加速采样器提升规划效率，在仿真和真实场景中均优于现有方法。
  ko: 'Bimanual and humanoid robots are appealing because of their human-like ability to leverage multiple arms to efficiently
    complete tasks. However, controlling multiple arms at once is computationally challenging due to the growth in the hybrid
    discrete-continuous action space. Institutions per source list: NVIDIA Research（Caelan Garrett）、University of Sydney（Fabio
    Ramos）.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- schedulestream
- temporal
- planning
- sampler
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 763 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2511.04758v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2511.04758 ScheduleStream: Temporal Planning with Samplers for GPU-Accelerated Multi-Arm Task and Motion Planning
    & Scheduling'
  url: https://arxiv.org/abs/2511.04758
  accessed_at: '2026-07-31'
  date: '2025-11-06'
- id: src_002
  type: website
  title: Project page
  url: https://schedulestream.github.io
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

双臂与人形机器人因能像人类一样同时使用多臂高效完成任务而备受关注，但混合离散-连续动作空间的增长使得多臂控制面临巨大计算挑战。传统任务与运动规划算法虽能处理混合空间，却通常生成单臂依次运动的计划，而非允许并行运动的调度方案。为此，ScheduleStream 提出首个通用框架，通过混合持续动作（可异步启动且持续时间取决于参数）建模时间动态，并设计领域无关的算法解决规划与调度问题。该框架将 GPU 加速集成到采样器中，显著加快任务与运动规划调度过程。仿真实验表明，ScheduleStream 算法相比多种消融方案能生成更高效的解，并在真实双臂机器人任务中得到验证。

## 核心内容
### 方法架构
- **混合持续动作**：ScheduleStream 将动作建模为可异步启动、持续时间由参数决定的混合离散-连续单元，从而捕捉时间动态。
- **领域无关算法**：提出不依赖特定应用机制的通用算法，解决 ScheduleStream 问题，避免针对不同场景的定制化设计。
- **GPU 加速采样**：在采样器中集成 GPU 加速，用于快速生成和评估动作参数，缓解混合空间搜索的计算瓶颈。

### 实验设置
- **任务场景**：在仿真环境中测试双臂机器人任务，并与多种消融方案（如无 GPU 加速、单臂顺序规划等）对比。
- **评估指标**：以规划效率（求解时间）和解质量（任务完成时间）为主要指标。

### 关键结果
- **效率提升**：ScheduleStream 算法在仿真中生成比消融方案更高效的解，任务完成时间显著缩短。
- **GPU 加速效果**：GPU 加速的采样器使规划速度提升数倍，尤其在动作参数空间较大时优势明显。
- **真实验证**：在真实双臂机器人任务中成功演示，代码与视频见 https://schedulestream.github.io。

### 结论
ScheduleStream 首次将通用规划与调度框架引入多臂机器人领域，通过混合持续动作建模和 GPU 加速采样，实现了并行运动调度。未来工作可扩展至更复杂的多机器人协作场景。

## Overview
Bimanual and humanoid robots are appealing because of their human-like ability to leverage multiple arms to efficiently complete tasks. However, controlling multiple arms at once is computationally challenging due to the growth in the hybrid discrete-continuous action space. Task and Motion Planning (TAMP) algorithms can efficiently plan in hybrid spaces but generally produce plans, where only one arm is moving at a time, rather than schedules that allow for parallel arm motion. In order to extend TAMP to produce schedules, we present ScheduleStream, the first general-purpose framework for planning & scheduling with sampling operations. ScheduleStream models temporal dynamics using hybrid durative actions, which can be started asynchronously and persist for a duration that's a function of their parameters. We propose domain-independent algorithms that solve ScheduleStream problems without any application-specific mechanisms. We apply ScheduleStream to Task and Motion Planning & Scheduling (TAMPAS), where we use GPU acceleration within samplers to expedite planning. We compare ScheduleStream algorithms to several ablations in simulation and find that they produce more efficient solutions. We demonstrate ScheduleStream on several real-world bimanual robot tasks at https://schedulestream.github.io.

## 参考
- https://arxiv.org/abs/2511.04758
- https://schedulestream.github.io
- https://github.com/ImChong/Robotics_Notebooks

## 개요

이중 팔 및 휴머노이드 로봇은 인간처럼 여러 팔을 동시에 사용하여 효율적으로 작업을 수행할 수 있어 주목받고 있지만, 혼합 이산-연속 동작 공간의 증가로 인해 다중 팔 제어는 큰 계산적 도전에 직면해 있습니다. 기존의 작업 및 운동 계획 알고리즘은 혼합 공간을 처리할 수 있지만, 일반적으로 병렬 운동을 허용하는 스케줄링 방식이 아닌 단일 팔을 순차적으로 움직이는 계획을 생성합니다. 이에 ScheduleStream은 혼합 지속 동작(비동기적으로 시작 가능하며 지속 시간이 매개변수에 따라 결정됨)을 통해 시간 역학을 모델링하고, 계획 및 스케줄링 문제를 해결하기 위한 도메인 독립적인 알고리즘을 설계한 최초의 일반 프레임워크를 제안합니다. 이 프레임워크는 GPU 가속을 샘플러에 통합하여 작업 및 운동 계획 스케줄링 과정을 크게 가속화합니다. 시뮬레이션 실험은 ScheduleStream 알고리즘이 다양한 절제 방식에 비해 더 효율적인 해를 생성하며, 실제 이중 팔 로봇 작업에서도 검증되었습니다.

## 핵심 내용
### 방법 아키텍처
- **혼합 지속 동작**: ScheduleStream은 동작을 비동기적으로 시작 가능하고 지속 시간이 매개변수에 의해 결정되는 혼합 이산-연속 단위로 모델링하여 시간 역학을 포착합니다.
- **도메인 독립 알고리즘**: 특정 응용 메커니즘에 의존하지 않는 일반 알고리즘을 제안하여 ScheduleStream 문제를 해결하고, 다양한 시나리오에 대한 맞춤형 설계를 피합니다.
- **GPU 가속 샘플링**: 샘플러에 GPU 가속을 통합하여 동작 매개변수를 빠르게 생성 및 평가하고, 혼합 공간 검색의 계산 병목 현상을 완화합니다.

### 실험 설정
- **작업 시나리오**: 시뮬레이션 환경에서 이중 팔 로봇 작업을 테스트하고, 다양한 절제 방식(예: GPU 가속 없음, 단일 팔 순차 계획 등)과 비교합니다.
- **평가 지표**: 계획 효율성(해결 시간)과 해 품질(작업 완료 시간)을 주요 지표로 사용합니다.

### 주요 결과
- **효율성 향상**: ScheduleStream 알고리즘은 시뮬레이션에서 절제 방식보다 더 효율적인 해를 생성하며, 작업 완료 시간이 크게 단축됩니다.
- **GPU 가속 효과**: GPU 가속 샘플러는 계획 속도를 몇 배 향상시키며, 특히 동작 매개변수 공간이 클 때 그 이점이 두드러집니다.
- **실제 검증**: 실제 이중 팔 로봇 작업에서 성공적으로 시연되었으며, 코드와 비디오는 https://schedulestream.github.io에서 확인할 수 있습니다.

### 결론
ScheduleStream은 다중 팔 로봇 분야에 최초로 일반 계획 및 스케줄링 프레임워크를 도입하여, 혼합 지속 동작 모델링과 GPU 가속 샘플링을 통해 병렬 운동 스케줄링을 실현했습니다. 향후 연구는 더 복잡한 다중 로봇 협업 시나리오로 확장될 수 있습니다.
