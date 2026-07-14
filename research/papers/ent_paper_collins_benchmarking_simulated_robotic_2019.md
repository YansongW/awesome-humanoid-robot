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
  zh: Collins 等人提出了一种无需硬件的模拟机器人操作基准，通过分发真实世界的动作捕捉数据集和标准化协议，使研究人员能够使用23种运动学和动力学指标来量化仿真到现实的差距。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1911.01557v2.
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
We present a benchmark to facilitate simulated manipulation; an attempt to overcome the obstacles of physical benchmarks through the distribution of a real world, ground truth dataset. Users are given various simulated manipulation tasks with assigned protocols having the objective of replicating the real world results of a recorded dataset. The benchmark comprises of a range of metrics used to characterise the successes of submitted environments whilst providing insight into their deficiencies. We apply our benchmark to two simulation environments, PyBullet and V-Rep, and publish the results. All materials required to benchmark an environment, including protocols and the dataset, can be found at the benchmarks' website https://research.csiro.au/robotics/manipulation-benchmark/.

## 核心内容
We present a benchmark to facilitate simulated manipulation; an attempt to overcome the obstacles of physical benchmarks through the distribution of a real world, ground truth dataset. Users are given various simulated manipulation tasks with assigned protocols having the objective of replicating the real world results of a recorded dataset. The benchmark comprises of a range of metrics used to characterise the successes of submitted environments whilst providing insight into their deficiencies. We apply our benchmark to two simulation environments, PyBullet and V-Rep, and publish the results. All materials required to benchmark an environment, including protocols and the dataset, can be found at the benchmarks' website https://research.csiro.au/robotics/manipulation-benchmark/.

## 参考
- http://arxiv.org/abs/1911.01557v2

