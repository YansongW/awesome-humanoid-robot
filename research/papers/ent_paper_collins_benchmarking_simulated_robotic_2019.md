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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1911.01557v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (596 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1911.01557v2

## Overview
This benchmark assists researchers in reproducing real-world manipulation outcomes within simulated environments by providing a real-world motion capture dataset and standardized protocols. It encompasses 23 kinematic and dynamic metrics to evaluate the success of simulation environments and reveal their shortcomings. The authors have applied the benchmark to two simulation environments, PyBullet and V-Rep, and have made all testing materials publicly available, including protocols and datasets.

## Content
### Core Contributions
- Introduces the first simulation manipulation benchmark based on real-world motion capture data, enabling evaluation of simulation environments without physical hardware.
- Provides 23 kinematic and dynamic metrics to quantify the gap between simulation and real environments (sim2real gap).
- Standardized protocols require users to complete specified manipulation tasks and reproduce the real results from the recorded dataset.

### Experimental Setup
- Test environments: Two mainstream physics simulation engines, PyBullet and V-Rep.
- Dataset: Real-world motion capture data, including complete trajectories of manipulation tasks.
- Evaluation metrics: 23 metrics covering kinematic (e.g., joint angles, end-effector trajectories) and dynamic (e.g., forces, torques) characteristics.

### Key Results
- Neither simulation environment fully reproduced the real data results, indicating a significant sim2real gap.
- The benchmark successfully identified specific deficiencies in each environment, such as PyBullet performing poorly in contact dynamics and V-Rep showing deviations in joint friction modeling.

### Resource Access
All benchmark materials (protocols, datasets, evaluation code) are open-sourced and available at: https://research.csiro.au/robotics/manipulation-benchmark/

## 개요
이 벤치마크는 실제 세계 모션 캡처 데이터셋과 표준화된 프로토콜을 제공하여 연구자들이 시뮬레이션 환경에서 실제 조작 결과를 재현할 수 있도록 돕습니다. 여기에는 시뮬레이션 환경의 성공 정도를 평가하고 결함을 드러내는 23가지 운동학 및 동역학 지표가 포함됩니다. 저자들은 이 벤치마크를 PyBullet과 V-Rep 두 시뮬레이션 환경에 적용했으며, 프로토콜과 데이터셋을 포함한 모든 테스트 자료를 공개했습니다.

## 핵심 내용
### 핵심 기여
- 실제 세계 모션 캡처 데이터를 기반으로 한 최초의 시뮬레이션 조작 벤치마크를 제안하여, 물리적 하드웨어 없이도 시뮬레이션 환경을 평가할 수 있음
- 시뮬레이션과 실제 환경 간의 차이(sim2real gap)를 정량화하는 23가지 운동학 및 동역학 지표 제공
- 표준화된 프로토콜은 사용자가 지정된 조작 작업을 완료하고, 기록된 데이터셋의 실제 결과를 재현하도록 요구함

### 실험 설정
- 테스트 환경: PyBullet과 V-Rep 두 주요 물리 시뮬레이션 엔진
- 데이터셋: 조작 작업의 전체 궤적을 포함한 실제 세계 모션 캡처 데이터
- 평가 지표: 23가지 지표는 운동학(예: 관절 각도, 말단 효과기 궤적) 및 동역학(예: 힘, 토크) 특성을 포함

### 주요 결과
- 두 시뮬레이션 환경 모두 실제 데이터 결과를 완전히 재현하지 못했으며, 상당한 sim2real 차이가 존재함
- 벤치마크는 각 환경의 구체적인 결함을 성공적으로 식별했으며, 예를 들어 PyBullet은 접촉 동역학에서 성능이 낮고, V-Rep은 관절 마찰 모델링에서 편차를 보임

### 자료 획득
모든 벤치마크 테스트 자료(프로토콜, 데이터셋, 평가 코드)는 오픈소스로 공개되어 있으며, 다음에서 확인할 수 있습니다: https://research.csiro.au/robotics/manipulation-benchmark/
