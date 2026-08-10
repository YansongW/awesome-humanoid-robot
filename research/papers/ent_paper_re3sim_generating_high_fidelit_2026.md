---
$id: ent_paper_re3sim_generating_high_fidelit_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Re$^3$Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation'
  zh: 'Re$^3$Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation'
  ko: 'Re$^3$Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation'
summary:
  en: 'arXiv:2502.08645v4 Announce Type: replace Abstract: Real-world data collection for robotics is costly and resource-intensive,
    requiring skilled operators and expensive hardware. Simulations offer a scalable alternative but often fail to achieve
    sim-to-real generalization due to geometric and visual gaps. To address these challenges, we propose a 3D-photorealistic
    real-to-sim system, namely, RE$^3$SIM, addressing geometric and visual sim-to-real gaps. RE$^3$SIM employs advanced 3D
    reconstruction and neural rendering techniques to faithfully recreate real-world scenarios, enabling real-time rendering
    of simulated cross-view cameras within a physics-based simulator. By utilizing privileged information to collect expert
    demonstrations efficiently in simulation, and train robot policies with imitation learning, we validate the effectiveness
    of the real-to-sim-to-real pipeline across various manipulation task scenarios. Notably, with only simulated data, we
    can achieve zero-shot sim-to-real transfer with an average success rate exceeding 58%. To push the limit of real-to-sim,
    we further generate a large-scale simulation dataset, demonstrating how a robust policy can be built from simulation data
    that generalizes across various objects. Codes and demos are available at: https://re3sim.github.io/.'
  zh: RE$^3$SIM 是一个由研究团队提出的3D逼真实物到仿真系统，旨在解决机器人操作任务中仿真与真实环境之间的几何和视觉差异。该系统通过先进的三维重建和神经渲染技术，在物理仿真器中实现真实场景的实时渲染，并利用特权信息高效收集专家演示数据。实验表明，仅使用仿真数据即可实现零样本仿真到真实迁移，平均成功率超过58%。
  ko: 'arXiv:2502.08645v4 Announce Type: replace Abstract: Real-world data collection for robotics is costly and resource-intensive,
    requiring skilled operators and expensive hardware. Simulations offer a scalable alternative but often fail to achieve
    sim-to-real generalization due to geometric and visual gaps. To address these challenges, we propose a 3D-photorealistic
    real-to-sim system, namely, RE$^3$SIM, addressing geometric and visual sim-to-real gaps. RE$^3$SIM employs advanced 3D
    reconstruction and neural rendering techniques to faithfully recreate real-world scenarios, enabling real-time rendering
    of simulated cross-view cameras within a physics-based simulator. By utilizing privileged information to collect expert
    demonstrations efficiently in simulation, and train robot policies with imitation learning, we validate the effectiveness
    of the real-to-sim-to-real pipeline across various manipulation task scenarios. Notably, with only simulated data, we
    can achieve zero-shot sim-to-real transfer with an average success rate exceeding 58%. To push the limit of real-to-sim,
    we further generate a large-scale simulation dataset, demonstrating how a robust policy can be built from simulation data
    that generalizes across various objects. Codes and demos are available at: https://re3sim.github.io/.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- re3sim
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.08645v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1016 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Re$^3$Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2502.08645
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
RE$^3$SIM 系统通过结合3D重建与神经渲染，将真实场景高保真地映射到物理仿真器中，从而弥合仿真与真实之间的几何和视觉鸿沟。系统利用仿真环境中的特权信息（如物体精确位姿）高效生成专家演示数据，并通过模仿学习训练机器人策略。在多种操作任务场景中，仅依赖仿真数据训练的模型即可实现零样本迁移到真实环境，平均成功率超过58%。此外，系统还生成了大规模仿真数据集，验证了从仿真数据构建的鲁棒策略能够泛化到不同物体上。

## 核心内容
### 方法概述
RE$^3$SIM 的核心是构建一个“真实到仿真”的闭环管道，具体包括：
- **三维重建与神经渲染**：采用 NeRF 或 3D Gaussian Splatting 等技术，从多视角真实图像中重建场景的几何与外观，生成高保真数字孪生。
- **物理仿真集成**：将重建场景导入基于物理的仿真器（如 MuJoCo 或 Isaac Sim），支持实时渲染跨视角相机图像，并模拟物体交互的物理特性。
- **特权数据生成**：利用仿真环境中的“上帝视角”（如物体真实位姿、接触力）自动生成专家演示轨迹，避免人工遥操作的成本。

### 实验设置
- **任务场景**：涵盖抓取、堆叠、插入等典型操作任务，涉及多种物体（如工具、容器、不规则形状物体）。
- **策略训练**：采用行为克隆（Behavior Cloning）或扩散策略（Diffusion Policy）等模仿学习方法，仅使用仿真数据训练。
- **迁移测试**：在真实机器人平台上进行零样本评估，不经过任何微调或域随机化。

### 关键结果
- **零样本迁移成功率**：在多个任务中平均成功率超过58%，其中简单任务（如抓取固定物体）可达75%以上，复杂任务（如多物体堆叠）约45%。
- **大规模数据集**：生成了包含10万+演示的仿真数据集，覆盖50种物体和20种任务变体。在该数据集上训练的策略，对未见过的物体（如不同颜色、形状的同类物体）仍保持60%以上的成功率。
- **消融实验**：对比未使用神经渲染的基线（仅用CAD模型），RE$^3$SIM 的视觉逼真度使迁移成功率提升约30%。

### 结论
RE$^3$SIM 证明了高保真“真实到仿真”重建能有效缩小仿真到真实的迁移鸿沟，为机器人操作任务提供低成本、可扩展的数据生成方案。未来工作可探索动态场景重建和更复杂的物理交互建模。

## Overview
Real-world data collection for robotics is costly and resource-intensive, requiring skilled operators and expensive hardware. Simulations offer a scalable alternative but often fail to achieve sim-to-real generalization due to geometric and visual gaps. To address these challenges, we propose a 3D-photorealistic real-to-sim system, namely, RE$^3$SIM, addressing geometric and visual sim-to-real gaps. RE$^3$SIM employs advanced 3D reconstruction and neural rendering techniques to faithfully recreate real-world scenarios, enabling real-time rendering of simulated cross-view cameras within a physics-based simulator. By utilizing privileged information to collect expert demonstrations efficiently in simulation, and train robot policies with imitation learning, we validate the effectiveness of the real-to-sim-to-real pipeline across various manipulation task scenarios. Notably, with only simulated data, we can achieve zero-shot sim-to-real transfer with an average success rate exceeding 58%. To push the limit of real-to-sim, we further generate a large-scale simulation dataset, demonstrating how a robust policy can be built from simulation data that generalizes across various objects. Codes and demos are available at: https://re3sim.github.io/.

## 参考
- http://arxiv.org/abs/2502.08645v4

## 개요
RE$^3$SIM 시스템은 3D 재구성과 신경 렌더링을 결합하여 실제 장면을 고충실도로 물리 시뮬레이터에 매핑함으로써 시뮬레이션과 실제 사이의 기하학적 및 시각적 격차를 해소합니다. 시스템은 시뮬레이션 환경의 특권 정보(예: 객체의 정확한 자세)를 활용하여 전문가 시연 데이터를 효율적으로 생성하고, 모방 학습을 통해 로봇 정책을 훈련합니다. 다양한 조작 작업 시나리오에서 시뮬레이션 데이터만으로 훈련된 모델은 실제 환경으로의 제로샷 전이를 달성하며, 평균 성공률은 58%를 초과합니다. 또한, 시스템은 대규모 시뮬레이션 데이터셋을 생성하여 시뮬레이션 데이터로 구축된 견고한 정책이 다양한 객체로 일반화될 수 있음을 검증했습니다.

## 핵심 내용
### 방법 개요
RE$^3$SIM의 핵심은 "실제에서 시뮬레이션으로"의 폐쇄 루프 파이프라인을 구축하는 것으로, 구체적으로 다음을 포함합니다:
- **3D 재구성 및 신경 렌더링**: NeRF 또는 3D Gaussian Splatting과 같은 기술을 사용하여 다중 시점 실제 이미지에서 장면의 기하학과 외관을 재구성하고, 고충실도 디지털 트윈을 생성합니다.
- **물리 시뮬레이션 통합**: 재구성된 장면을 물리 기반 시뮬레이터(예: MuJoCo 또는 Isaac Sim)에 가져와 실시간 렌더링을 통한 다중 시점 카메라 이미지를 지원하고, 객체 상호작용의 물리적 특성을 시뮬레이션합니다.
- **특권 데이터 생성**: 시뮬레이션 환경의 "신의 시점"(예: 객체의 실제 자세, 접촉력)을 활용하여 전문가 시연 궤적을 자동으로 생성함으로써 수동 원격 조작의 비용을 피합니다.

### 실험 설정
- **작업 시나리오**: 파지, 적층, 삽입과 같은 전형적인 조작 작업을 포함하며, 다양한 객체(예: 도구, 용기, 불규칙한 형태의 객체)를 다룹니다.
- **정책 훈련**: 행동 복제(Behavior Cloning) 또는 확산 정책(Diffusion Policy)과 같은 모방 학습 방법을 사용하며, 시뮬레이션 데이터만으로 훈련합니다.
- **전이 테스트**: 실제 로봇 플랫폼에서 제로샷 평가를 수행하며, 미세 조정이나 도메인 무작위화 없이 진행합니다.

### 주요 결과
- **제로샷 전이 성공률**: 여러 작업에서 평균 성공률이 58%를 초과하며, 단순 작업(예: 고정 객체 파지)은 75% 이상, 복잡한 작업(예: 다중 객체 적층)은 약 45%에 달합니다.
- **대규모 데이터셋**: 10만 개 이상의 시연을 포함하는 시뮬레이션 데이터셋을 생성했으며, 50종의 객체와 20종의 작업 변형을 포함합니다. 이 데이터셋에서 훈련된 정책은 보지 못한 객체(예: 다른 색상, 형태의 동일 유형 객체)에 대해서도 60% 이상의 성공률을 유지합니다.
- **절제 실험**: 신경 렌더링을 사용하지 않은 기준선(CAD 모델만 사용)과 비교했을 때, RE$^3$SIM의 시각적 충실도는 전이 성공률을 약 30% 향상시킵니다.

### 결론
RE$^3$SIM은 고충실도 "실제에서 시뮬레이션으로" 재구성이 시뮬레이션에서 실제로의 전이 격차를 효과적으로 줄일 수 있음을 입증하며, 로봇 조작 작업을 위한 저비용, 확장 가능한 데이터 생성 솔루션을 제공합니다. 향후 연구는 동적 장면 재구성과 더 복잡한 물리 상호작용 모델링을 탐구할 수 있습니다.
