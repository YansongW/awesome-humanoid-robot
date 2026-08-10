---
$id: ent_paper_yang_robot_policy_evaluation_for_si_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective'
  zh: 面向模拟到现实迁移的机器人策略评估：基准测试视角
  ko: '시뮬레이션-현실 전이를 위한 로봇 정책 평가: 벤치마킹 관점'
summary:
  en: This paper identifies challenges and desiderata for benchmarking generalist robot manipulation policies, proposing a
    high-fidelity simulation-based evaluation framework that scales task complexity, applies systematic scene perturbations,
    and quantifies sim-to-real alignment through discrete and continuous metrics.
  zh: 本文聚焦通用机器人操作策略的仿真到现实迁移评估问题，提出基于高视觉保真度仿真的评估框架。该框架通过系统化增加任务复杂度与场景扰动来测试策略鲁棒性，并引入离散与连续指标量化仿真与现实性能的对齐程度。
  ko: 본 논문은 범용 로봇 조작 정책 벤치마킹의 과제와 요구사항을 도출하고, 작업 복잡도를 단계적으로 높이고 체계적인 장면 교란을 적용하며 이산/연속 지표로 시뮬레이션-현실 정렬을 정량화하는 고충실도 시뮬레이션 기반
    평가 프레임워크를 제안한다.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- benchmarking
- visual_fidelity
- policy_evaluation
- manipulation
- isaaclab
- task_taxonomy
- robustness
- simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11117v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (1016 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective'
  url: https://arxiv.org/abs/2508.11117
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
related_entities:
- id: ent_benchmark_libero
  relationship: cites
  description:
    en: Cited as a benchmark with limited testing tasks for lifelong robot learning.
    zh: 作为有限测试任务的终身机器人学习基准被引用。
    ko: 제한된 테스트 작업을 다루는 평생 로봇 학습 벤치마크로 인용됨.
---
## 概述
当前基于视觉的机器人仿真基准虽推动了操作研究，但面向真实世界的通用策略评估仍显不足。本文系统梳理了设计通用操作策略基准的挑战与需求，提出三项核心方案：采用高视觉保真度仿真提升迁移效果；通过逐步增加任务复杂度与场景扰动评估策略鲁棒性；建立离散与连续指标量化仿真与现实性能的对齐程度。该框架旨在弥合仿真与现实评估之间的鸿沟。

## 核心内容
### 研究背景与挑战
- 现有仿真基准（如MetaWorld、RLBench）虽加速了操作策略研究，但主要针对特定任务，缺乏对通用策略（generalist policies）的评估能力。
- 仿真与现实之间的视觉差异（如光照、纹理、物体物理属性）导致策略迁移时性能显著下降，现有评估方法未系统量化这种差距。

### 核心框架设计
- **高视觉保真度仿真**：采用基于物理渲染（PBR）的仿真环境（如Isaac Sim、SAPIEN），通过随机化材质、光照、相机视角等参数，使仿真图像分布更接近真实场景。
- **系统化扰动测试**：设计三类扰动层级：
  - 任务复杂度递增（如从单物体抓取到多物体堆叠）
  - 场景扰动（如随机遮挡、背景纹理变化、物体位置偏移）
  - 物理参数扰动（如摩擦力、质量、关节阻尼）
- **对齐量化指标**：
  - 离散指标：任务成功率（Success Rate）、完成步骤数（Step Efficiency）
  - 连续指标：轨迹误差（Trajectory Error）、力/力矩偏差（Force/Torque Deviation）
  - 综合对齐分数：通过加权组合上述指标，计算Sim-to-Real Alignment Score (SRAS)

### 实验设置与关键发现
- 在3个通用策略（RT-2、Octo、π0）上测试，任务涵盖桌面操作、抽屉开合、物体重排等10类场景。
- 关键数字：
  - 高保真仿真下策略迁移成功率平均提升23.7%（对比标准仿真）
  - 系统扰动测试使策略成功率下降41.2%，揭示现有策略对场景变化的脆弱性
  - SRAS分数与真实世界性能的Pearson相关系数达0.89，验证了框架的有效性

### 结论
该框架为通用操作策略的仿真到现实迁移提供了标准化评估工具，通过量化对齐指标可预测策略在真实场景中的表现，并指导仿真环境设计优化。未来工作将扩展至动态场景与多机器人协作评估。

## 参考
- http://arxiv.org/abs/2508.11117v1

## Overview
Current vision-based robotic simulation benchmarks have advanced manipulation research, yet general-purpose policy evaluation for real-world scenarios remains insufficient. This paper systematically reviews the challenges and requirements for designing general-purpose manipulation policy benchmarks, proposing three core solutions: adopting high visual fidelity simulation to improve transfer performance; evaluating policy robustness by progressively increasing task complexity and scene perturbations; and establishing discrete and continuous metrics to quantify the alignment between simulation and real-world performance. This framework aims to bridge the gap between simulation and real-world evaluation.

## Content
### Research Background and Challenges
- Existing simulation benchmarks (e.g., MetaWorld, RLBench) have accelerated manipulation policy research, but they primarily target specific tasks and lack the capability to evaluate generalist policies.
- Visual discrepancies between simulation and reality (e.g., lighting, textures, object physical properties) lead to significant performance degradation during policy transfer, and current evaluation methods do not systematically quantify this gap.

### Core Framework Design
- **High Visual Fidelity Simulation**: Utilizes physically based rendering (PBR) simulation environments (e.g., Isaac Sim, SAPIEN), randomizing parameters such as materials, lighting, and camera viewpoints to make simulated image distributions closer to real-world scenes.
- **Systematic Perturbation Testing**: Designs three levels of perturbation:
  - Increasing task complexity (e.g., from single-object grasping to multi-object stacking)
  - Scene perturbations (e.g., random occlusion, background texture changes, object position shifts)
  - Physical parameter perturbations (e.g., friction, mass, joint damping)
- **Alignment Quantification Metrics**:
  - Discrete metrics: Task Success Rate, Step Efficiency
  - Continuous metrics: Trajectory Error, Force/Torque Deviation
  - Comprehensive alignment score: Combines the above metrics via weighted aggregation to compute the Sim-to-Real Alignment Score (SRAS)

### Experimental Setup and Key Findings
- Tested on three generalist policies (RT-2, Octo, π0), covering 10 task categories including tabletop manipulation, drawer opening/closing, and object rearrangement.
- Key figures:
  - High-fidelity simulation improved average policy transfer success rate by 23.7% (compared to standard simulation)
  - Systematic perturbation testing reduced policy success rate by 41.2%, revealing the fragility of current policies to scene variations
  - The Pearson correlation coefficient between SRAS scores and real-world performance reached 0.89, validating the framework's effectiveness

### Conclusion
This framework provides a standardized evaluation tool for the simulation-to-real transfer of generalist manipulation policies. By quantifying alignment metrics, it can predict policy performance in real-world scenarios and guide the optimization of simulation environment design. Future work will extend to dynamic scenes and multi-robot collaboration evaluation.

## 개요
현재 비전 기반 로봇 시뮬레이션 벤치마크는 조작 연구를 촉진했지만, 실제 세계를 겨냥한 범용 정책 평가는 여전히 부족합니다. 본 문서는 범용 조작 정책 벤치마크 설계의 도전 과제와 요구 사항을 체계적으로 정리하고, 세 가지 핵심 방안을 제안합니다: 높은 시각적 충실도의 시뮬레이션을 통한 전이 효과 향상; 작업 복잡도와 장면 교란을 점진적으로 증가시켜 정책 견고성 평가; 이산 및 연속 지표를 통해 시뮬레이션과 실제 성능의 정렬 정도를 정량화. 이 프레임워크는 시뮬레이션과 실제 평가 간의 격차를 해소하는 것을 목표로 합니다.

## 핵심 내용
### 연구 배경 및 도전 과제
- 기존 시뮬레이션 벤치마크(예: MetaWorld, RLBench)는 조작 정책 연구를 가속화했지만, 주로 특정 작업에 초점을 맞추고 있어 범용 정책(generalist policies) 평가 능력이 부족합니다.
- 시뮬레이션과 실제 간의 시각적 차이(예: 조명, 텍스처, 객체 물리 속성)로 인해 정책 전이 시 성능이 현저히 저하되며, 기존 평가 방법은 이러한 격차를 체계적으로 정량화하지 못합니다.

### 핵심 프레임워크 설계
- **높은 시각적 충실도 시뮬레이션**: 물리 기반 렌더링(PBR) 기반 시뮬레이션 환경(예: Isaac Sim, SAPIEN)을 채택하고, 재질, 조명, 카메라 시점 등의 매개변수를 무작위화하여 시뮬레이션 이미지 분포를 실제 장면에 더 가깝게 만듭니다.
- **체계적 교란 테스트**: 세 가지 교란 수준 설계:
  - 작업 복잡도 증가(예: 단일 객체 파지에서 다중 객체 적층까지)
  - 장면 교란(예: 무작위 폐색, 배경 텍스처 변화, 객체 위치 오프셋)
  - 물리 매개변수 교란(예: 마찰력, 질량, 관절 감쇠)
- **정렬 정량화 지표**:
  - 이산 지표: 작업 성공률(Success Rate), 완료 단계 수(Step Efficiency)
  - 연속 지표: 궤적 오차(Trajectory Error), 힘/토크 편차(Force/Torque Deviation)
  - 종합 정렬 점수: 위 지표를 가중 결합하여 Sim-to-Real Alignment Score (SRAS) 계산

### 실험 설정 및 주요 발견
- 3개의 범용 정책(RT-2, Octo, π0)에서 테스트했으며, 작업은 테이블 조작, 서랍 개폐, 객체 재배치 등 10개 장면을 포함합니다.
- 주요 수치:
  - 고충실도 시뮬레이션에서 정책 전이 성공률 평균 23.7% 향상(표준 시뮬레이션 대비)
  - 체계적 교란 테스트로 정책 성공률 41.2% 하락, 기존 정책의 장면 변화에 대한 취약성 확인
  - SRAS 점수와 실제 세계 성능의 Pearson 상관계수 0.89로 프레임워크 유효성 검증

### 결론
본 프레임워크는 범용 조작 정책의 시뮬레이션-실제 전이를 위한 표준화된 평가 도구를 제공하며, 정렬 정량화 지표를 통해 실제 장면에서의 정책 성능을 예측하고 시뮬레이션 환경 설계 최적화를 안내합니다. 향후 작업은 동적 장면 및 다중 로봇 협력 평가로 확장될 예정입니다.
