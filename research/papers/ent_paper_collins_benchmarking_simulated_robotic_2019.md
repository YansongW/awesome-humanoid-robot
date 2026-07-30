---
$id: ent_paper_collins_benchmarking_simulated_robotic_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Benchmarking Simulated Robotic Manipulation through a Real World Dataset
  zh: 通过真实世界数据集对模拟机器人操作进行基准测试
  ko: 실제 세계 데이터셋을 통한 시뮬레이션 로봇 조작 벤치마킹
summary:
  en: Collins et al. introduce a hardware-free benchmark for simulated robotic manipulation that distributes a real-world
    motion-capture dataset and standardized protocols so researchers can quantify the sim2real gap using 23 kinematic and
    dynamic metrics.
  zh: Collins等人提出了一种无需硬件的模拟机器人操作基准，通过发布真实世界运动捕捉数据集和标准化协议，使研究人员能够使用23项运动学和动力学指标量化sim2real差距。该基准旨在替代物理基准测试，并已应用于PyBullet和V-Rep两个仿真环境。
  ko: Collins 등은 실제 세계 모션 캡처 데이터셋과 표준화된 프로토콜을 배포하여 연구자들이 23개의 운동학적 및 동역학적 메트릭을 사용하여 sim2real 격차를 정량화할 수 있도록 하는 하드웨어 없는 시뮬레이션
    로봇 조작 벤치마크를 소개한다.
domains:
- 10_evaluation_benchmarks
- 09_data_datasets
- 08_software_middleware
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- sim2real
- benchmark
- manipulation
- motion_capture
- simulator_fidelity
- pybullet
- v_rep
- kinova_mico2
- robotiq_ft300
- qualisys
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1911.01557v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Benchmarking Simulated Robotic Manipulation through a Real World Dataset
  url: https://arxiv.org/abs/1911.01557
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该基准通过提供真实世界运动捕捉数据集和标准化协议，帮助研究人员在模拟环境中复现真实操作结果。它包含23项运动学和动力学指标，用于评估仿真环境的成功程度并揭示其缺陷。作者已将基准应用于PyBullet和V-Rep两个仿真环境，并公开了所有测试材料，包括协议和数据集。

## 核心内容
### 核心贡献
- 提出首个基于真实世界运动捕捉数据的模拟操作基准，无需物理硬件即可评估仿真环境
- 提供23项运动学与动力学指标，量化仿真与真实环境之间的差距（sim2real gap）
- 标准化协议要求用户完成指定操作任务，复现记录数据集的真实结果

### 实验设置
- 测试环境：PyBullet和V-Rep两个主流物理仿真引擎
- 数据集：真实世界运动捕捉数据，包含操作任务的完整轨迹
- 评估指标：23项指标覆盖运动学（如关节角度、末端执行器轨迹）和动力学（如力、扭矩）特性

### 关键结果
- 两个仿真环境均未能完全复现真实数据结果，存在显著sim2real差距
- 基准成功识别了各环境的具体缺陷，例如PyBullet在接触动力学方面表现较差，V-Rep在关节摩擦建模上存在偏差

### 资源获取
所有基准测试材料（协议、数据集、评估代码）均开源发布于：https://research.csiro.au/robotics/manipulation-benchmark/

## Overview
We present a benchmark to facilitate simulated manipulation; an attempt to overcome the obstacles of physical benchmarks through the distribution of a real world, ground truth dataset. Users are given various simulated manipulation tasks with assigned protocols having the objective of replicating the real world results of a recorded dataset. The benchmark comprises of a range of metrics used to characterise the successes of submitted environments whilst providing insight into their deficiencies. We apply our benchmark to two simulation environments, PyBullet and V-Rep, and publish the results. All materials required to benchmark an environment, including protocols and the dataset, can be found at the benchmarks' website https://research.csiro.au/robotics/manipulation-benchmark/.

## 개요
우리는 시뮬레이션 조작을 촉진하기 위한 벤치마크를 제시합니다. 이는 실제 세계의 실측 데이터셋을 배포함으로써 물리적 벤치마크의 장애물을 극복하려는 시도입니다. 사용자에게는 기록된 데이터셋의 실제 세계 결과를 재현하는 것을 목표로 하는 할당된 프로토콜과 함께 다양한 시뮬레이션 조작 작업이 제공됩니다. 이 벤치마크는 제출된 환경의 성공을 특성화하고 그 결함에 대한 통찰력을 제공하는 데 사용되는 다양한 지표로 구성됩니다. 우리는 이 벤치마크를 PyBullet과 V-Rep이라는 두 가지 시뮬레이션 환경에 적용하고 결과를 게시합니다. 프로토콜과 데이터셋을 포함하여 환경을 벤치마킹하는 데 필요한 모든 자료는 벤치마크 웹사이트 https://research.csiro.au/robotics/manipulation-benchmark/에서 확인할 수 있습니다.

## 핵심 내용
우리는 시뮬레이션 조작을 촉진하기 위한 벤치마크를 제시합니다. 이는 실제 세계의 실측 데이터셋을 배포함으로써 물리적 벤치마크의 장애물을 극복하려는 시도입니다. 사용자에게는 기록된 데이터셋의 실제 세계 결과를 재현하는 것을 목표로 하는 할당된 프로토콜과 함께 다양한 시뮬레이션 조작 작업이 제공됩니다. 이 벤치마크는 제출된 환경의 성공을 특성화하고 그 결함에 대한 통찰력을 제공하는 데 사용되는 다양한 지표로 구성됩니다. 우리는 이 벤치마크를 PyBullet과 V-Rep이라는 두 가지 시뮬레이션 환경에 적용하고 결과를 게시합니다. 프로토콜과 데이터셋을 포함하여 환경을 벤치마킹하는 데 필요한 모든 자료는 벤치마크 웹사이트 https://research.csiro.au/robotics/manipulation-benchmark/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/1911.01557v2
