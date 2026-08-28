---
$id: ent_paper_unified_structural_hydrodynami_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
  zh: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
  ko: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
summary:
  en: 'arXiv:2603.07939v2 Announce Type: replace Abstract: Underwater robots are widely deployed for ocean exploration and
    manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers
    motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated
    and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic
    parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic
    modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the
    proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through
    trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated
    mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording.
    We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification
    of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories,
    initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated
    on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally,
    eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body
    behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic
    modeling framework across underwater underactuated and soft robotic systems.'
  zh: 本文提出一种基于轨迹驱动的全局优化框架，用于水下欠驱动机构与软体机器人的统一结构-水动力学建模。该方法受CMA-ES启发，通过仿真与实验运动轨迹匹配，同时识别弹性、阻尼及分布式水动力学参数，仅需单段视频即可实现高保真复现。在连杆欠驱动机构与章鱼仿生软体臂上验证，末端位置误差低于5%，并成功扩展至八臂游泳章鱼机器人。
  ko: 'arXiv:2603.07939v2 Announce Type: replace Abstract: Underwater robots are widely deployed for ocean exploration and
    manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers
    motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated
    and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic
    parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic
    modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the
    proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through
    trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated
    mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording.
    We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification
    of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories,
    initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated
    on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally,
    eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body
    behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic
    modeling framework across underwater underactuated and soft robotic systems.'
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
- unified_structural_hydrodynami
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.07939v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (709 chars, DeepSeek). [2026-08-28] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
  url: https://arxiv.org/abs/2603.07939
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述

本文提出一种统一的结构-水动力学建模框架，用于水下欠驱动机构与软体机器人的 real-to-sim 迁移。作者通过 MuJoCo 平台，结合 CMA-ES 优化算法辨识每个连杆的五个流体系数（c₀ 至 c₄），实现从三连杆刚性机构到八臂章鱼启发软体机器人的参数迁移。核心贡献在于单一框架内同时估计多个流体动力学参数，避免了顺序辨识的误差累积。

## 它改变了什么

水下机器人的仿真保真度长期受限于流体动力学参数的难辨识性。传统做法要么依赖 CFD 求解器的高计算成本，要么采用顺序辨识策略——先标定惯性参数再标定流体参数，这种逐步逼近的方式在参数强耦合时容易产生误差漂移，且难以扩展到高自由度的软体结构。本文真正改变的是将流体参数辨识从“分步走”变为“一步到位”，并且证明了从简化刚性机构上辨识出的参数可以直接迁移到结构差异巨大的软体臂上，这为软体机器人的仿真工作流提供了一个可复用的范式。

更关键的是，作者没有停留在单臂验证，而是将单臂辨识参数直接应用于完整八臂机器人，并暴露了中央身体平台未标定导致的位移偏差。这种“诚实”的失败报告比完美结果更有工程价值——它明确了该方法的适用边界，即参数迁移的有效性取决于结构相似性和流体相互作用的可分解性。

## 方法拆解

### 参数分类与辨识框架
- **直接指定参数**：流体粘度按实验条件设定；电机速度与力范围采用执行器规格；刚性连杆启用碰撞检测。
- **优化辨识参数**：每个连杆优化五个流体系数（c₀ 至 c₄），描述连杆与流体的相互作用；同时辨识关节阻尼和摩擦损失参数，确保数值积分稳定。

### 优化流程
1. 采集真实轨迹数据（Real-world Trajectory Extraction）。
2. 在 MuJoCo 中构建仿真模型，以轨迹驱动方式运行。
3. 定义误差度量：时间对齐条件下，仿真与真实关键点位置的欧氏距离，在整个轨迹上取平均。
4. 使用 CMA-ES 优化器（对应论文 Section II-C）最小化轨迹误差，迭代更新流体系数与关节阻尼参数。
5. 将辨识参数整合到最终 MuJoCo 标定仿真系统，用于后续验证。

### 实验机构与软体臂结构
- **三连杆机构**：每连杆长 30 mm，相邻连杆重叠半径 5 mm，整体有效长度约 80 mm。轨迹误差相对于该特征长度归一化。
- **软体臂**：八个串联段，锥形形态，宽度沿长度递减；运动呈方向依赖特性，整体保持 2:1 速度比（逆时针运动持续时间是顺时针的两倍）。
- **全机器人**：中央身体平台加八条相同软臂，采用同步驱动策略，单臂辨识参数直接应用于全部八条臂。

## 关键创新

1. **单一框架多参数联合辨识**：与顺序辨识不同，CMA-ES 在统一目标函数下同时优化流体系数与关节阻尼，避免了参数耦合导致的失真。这是对传统标定流程的实质性简化，且计算效率高（MuJoCo 的低资源需求使迭代可行）。

2. **跨结构参数迁移**：从刚性三连杆机构辨识的参数，直接用于八段软体臂和完整八臂机器人，且软体臂实验表现出“清晰的一一对应关系”。这证明流体动力学参数在相似几何尺度下具有可迁移性，为软体机器人省去了逐结构标定的成本。

3. **误差归一化与物理意义绑定**：将轨迹误差相对于系统特征长度（80 mm）归一化，使性能指标具有跨机构可比性。所有初始条件下整体平均误差保持在系统总长度的 5% 以下，这一阈值可作为后续工作的验收标准。

## 实验与结果

实验覆盖四种配置（纯被动两种、主动-被动两种），关键结果如下：

| Case | P1 | P2 | P3 |
|------|-----|-----|-----|
| Purely Passive Case 1 | 0.87 | 1.53 | 2.79 |
| Purely Passive Case 2 | 1.35 | 1.76 | 2.54 |
| Active-Passive Case 1 | 1.62 | 2.78 | 2.55 |
| Active-Passive Case 2 | 1.14 | 1.97 | 1.68 |

- 所有四种初始条件下，整体平均误差保持在系统总长度的 5% 以下（由表内数值与 80 mm 特征长度计算，最大 2.79 mm 对应 3.5%（由表内数值 1.68→1.62 计算））。
- 主动-被动配置中，远端关键点 P2 和 P3 的幅值调制与实验观测紧密匹配；纯被动配置中，重力驱动的振荡衰减行为被准确捕捉。
- 软体臂实验中，仿真与真实运动在相同时间条件下高度一致，存在清晰的一一对应关系。
- 全机器人实验中，仿真位移略短于真实机器人，归因于中央身体平台未进行流体参数标定。

## 边界与局限

论文未明确列出所有局限，但实验暴露了关键边界：**中央身体平台未进行流体动力学参数辨识**，导致全机器人仿真位移偏短——平台贡献的附加质量和流体阻力未建模，误差随时间累积。这意味着参数迁移的有效性仅限于臂结构，不适用于几何差异大的部件。此外，所有实验均在静水条件下进行，**未在流水条件下验证**，因此框架对来流扰动的鲁棒性未知。软体臂的 2:1 速度比特性是否在更高驱动频率下保持，论文未明确。

## 工程启示

复现时首先核对三连杆机构的几何参数（30 mm 连杆长度、5 mm 重叠半径、80 mm 有效长度）与 MuJoCo 模型的一致性，这是误差归一化的基准。最容易踩坑的是关节阻尼参数的初始化——CMA-ES 对流体系数敏感，但阻尼参数若初始值不当会导致数值积分发散，建议先固定阻尼、单独优化流体系数，再联合优化。参数迁移到软体臂时，务必确认几何尺度与三连杆机构相近，否则需重新辨识。对于全机器人场景，不要直接沿用单臂参数到中央平台——必须对平台单独标定，否则位移偏差会随时间累积。最后，所有轨迹误差计算需严格时间对齐，否则欧氏距离会被相位差污染，建议在采集时同步触发仿真时钟。

## 参考
- http://arxiv.org/abs/2603.07939v2

## 개요
수중 로봇은 해양 탐사와 작업에 널리 사용되며, 부족구동 메커니즘은 액추에이터 수를 줄여 모터 누출 위험을 낮추고 기계적 유연성을 도입하지만, 모델링 과정에서 고차원 구조와 수력학적 매개변수 식별의 어려움이 있습니다. 본 논문은 CMA-ES에서 영감을 받은 궤적 기반 전역 최적화 프레임워크를 제안하며, 시뮬레이션과 실험 운동 궤적의 일치를 통해 결합된 탄성, 감쇠 및 분산 수력학적 매개변수를 동시에 식별합니다. 이 방법은 단일 비디오 세그먼트만으로 수중 부족구동 메커니즘과 유연 소프트 시스템을 고충실도로 재현할 수 있습니다. 링크 부족구동 메커니즘에서 검증되었으며, 끝단 위치 정규화 오차가 5% 미만이고, 비대칭 문어 생체모방 소프트 암에서도 유효성을 확인했습니다. 마지막으로, 식별된 8개의 암을 조립하여 수영하는 문어 로봇을 구성했으며, 통합 매개변수 세트는 추가 조정 없이도 사실적인 전신 동작을 구현합니다.

## 핵심 내용
### 방법
- 수중 다물체 시스템의 통합 구조-수력학적 모델링을 위한 **궤적 기반 전역 최적화 프레임워크**를 제안합니다.
- **Covariance Matrix Adaptation Evolution Strategy (CMA-ES)** 에서 영감을 받아, 시뮬레이션과 실험 운동 궤적의 일치를 통해 결합된 탄성, 감쇠 및 분산 수력학적 매개변수를 동시에 식별합니다.
- **단일 비디오 기록**만으로 고충실도 재현이 가능하며, 부족구동 메커니즘과 유연 소프트 시스템에 적용 가능합니다.

### 실험 설정 및 검증
- **링크 부족구동 메커니즘**: 링크별로 검증하여 분산 수력학적 계수를 정확히 식별했으며, 다양한 궤적, 초기 조건 및 능동-수동 및 완전 수동 구성에서 **끝단 위치 정규화 오차가 5% 미만**입니다.
- **비대칭 문어 생체모방 소프트 암**: 프레임워크의 유연 소프트 시스템에 대한 유효성을 추가로 검증합니다.
- **8개 암 수영 문어 로봇**: 식별된 8개의 암을 조립하여 **통합 매개변수 세트는 추가 조정 없이** 사실적인 전신 동작을 구현합니다.

### 결론
- 결과는 이 프레임워크가 **확장성과 전이성**을 가지며, 수중 부족구동 메커니즘과 소프트 로봇 시스템에 적용될 수 있음을 보여줍니다.
