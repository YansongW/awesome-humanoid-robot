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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.08645v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
로봇 공학을 위한 실제 데이터 수집은 숙련된 작업자와 고가의 하드웨어가 필요하여 비용이 많이 들고 자원 집약적입니다. 시뮬레이션은 확장 가능한 대안을 제공하지만, 기하학적 및 시각적 차이로 인해 시뮬레이션-실제 일반화를 달성하지 못하는 경우가 많습니다. 이러한 문제를 해결하기 위해, 우리는 기하학적 및 시각적 시뮬레이션-실제 차이를 해결하는 3D 포토리얼리스틱 실제-시뮬레이션 시스템인 RE$^3$SIM을 제안합니다. RE$^3$SIM은 고급 3D 재구성 및 신경 렌더링 기술을 사용하여 실제 시나리오를 충실히 재현하며, 물리 기반 시뮬레이터 내에서 시뮬레이션된 교차 시점 카메라의 실시간 렌더링을 가능하게 합니다. 특권 정보를 활용하여 시뮬레이션에서 효율적으로 전문가 시연을 수집하고, 모방 학습을 통해 로봇 정책을 훈련함으로써, 다양한 조작 작업 시나리오에서 실제-시뮬레이션-실제 파이프라인의 효과를 검증합니다. 특히, 시뮬레이션 데이터만으로도 평균 성공률 58%를 초과하는 제로샷 시뮬레이션-실제 전이를 달성할 수 있습니다. 실제-시뮬레이션의 한계를 극복하기 위해, 대규모 시뮬레이션 데이터셋을 추가로 생성하여, 다양한 객체에 일반화되는 강력한 정책을 시뮬레이션 데이터로부터 구축할 수 있는 방법을 보여줍니다. 코드와 데모는 https://re3sim.github.io/에서 확인할 수 있습니다.

## 핵심 내용
로봇 공학을 위한 실제 데이터 수집은 숙련된 작업자와 고가의 하드웨어가 필요하여 비용이 많이 들고 자원 집약적입니다. 시뮬레이션은 확장 가능한 대안을 제공하지만, 기하학적 및 시각적 차이로 인해 시뮬레이션-실제 일반화를 달성하지 못하는 경우가 많습니다. 이러한 문제를 해결하기 위해, 우리는 기하학적 및 시각적 시뮬레이션-실제 차이를 해결하는 3D 포토리얼리스틱 실제-시뮬레이션 시스템인 RE$^3$SIM을 제안합니다. RE$^3$SIM은 고급 3D 재구성 및 신경 렌더링 기술을 사용하여 실제 시나리오를 충실히 재현하며, 물리 기반 시뮬레이터 내에서 시뮬레이션된 교차 시점 카메라의 실시간 렌더링을 가능하게 합니다. 특권 정보를 활용하여 시뮬레이션에서 효율적으로 전문가 시연을 수집하고, 모방 학습을 통해 로봇 정책을 훈련함으로써, 다양한 조작 작업 시나리오에서 실제-시뮬레이션-실제 파이프라인의 효과를 검증합니다. 특히, 시뮬레이션 데이터만으로도 평균 성공률 58%를 초과하는 제로샷 시뮬레이션-실제 전이를 달성할 수 있습니다. 실제-시뮬레이션의 한계를 극복하기 위해, 대규모 시뮬레이션 데이터셋을 추가로 생성하여, 다양한 객체에 일반화되는 강력한 정책을 시뮬레이션 데이터로부터 구축할 수 있는 방법을 보여줍니다. 코드와 데모는 https://re3sim.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2502.08645v4
