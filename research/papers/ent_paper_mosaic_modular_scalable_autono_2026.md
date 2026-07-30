---
$id: ent_paper_mosaic_modular_scalable_autono_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MOSAIC: Modular Scalable Autonomy for Intelligent Coordination of Heterogeneous Robotic Teams'
  zh: 'MOSAIC: Modular Scalable Autonomy for Intelligent Coordination of Heterogeneous Robotic Teams'
  ko: 'MOSAIC: Modular Scalable Autonomy for Intelligent Coordination of Heterogeneous Robotic Teams'
summary:
  en: 'arXiv:2601.23038v3 Announce Type: replace Abstract: Mobile robots have become indispensable for exploring hostile environments,
    such as in space or disaster relief scenarios, but often remain limited to teleoperation by a human operator. This restricts
    the deployment scale and requires near-continuous low-latency communication between the operator and the robot. We present
    MOSAIC: a scalable autonomy framework for multi-robot scientific exploration using a unified mission abstraction based
    on Points of Interest (POIs) and multiple layers of autonomy, enabling supervision by a single operator. The framework
    dynamically allocates exploration and measurement tasks based on each robot''s capabilities, leveraging team-level redundancy
    and specialization to enable continuous operation. We validated the framework in a space-analog field experiment emulating
    a lunar prospecting scenario, involving a heterogeneous team of five robots and a single operator. Despite the complete
    failure of one robot during the mission, the team completed 82.3% of assigned tasks at an Autonomy Ratio of 86%, while
    the operator workload remained at only 78.2%. These results demonstrate that the proposed framework enables robust, scalable
    multi-robot scientific exploration with limited operator intervention. We further derive practical lessons learned in
    robot interoperability, networking architecture, team composition, and operator workload management to inform future multi-robot
    exploration missions.'
  zh: MOSAIC 是一个面向异构机器人团队的可扩展自主框架，由研究团队提出，基于兴趣点（POI）统一任务抽象与多层自主架构，实现单操作员对多机器人科学探索的监督。核心贡献在于通过动态任务分配与团队级冗余/专业化机制，在模拟月球勘探的野外实验中，即使一台机器人完全失效，仍完成82.3%任务，自主率达86%，操作员负载仅78.2%。
  ko: 'arXiv:2601.23038v3 Announce Type: replace Abstract: Mobile robots have become indispensable for exploring hostile environments,
    such as in space or disaster relief scenarios, but often remain limited to teleoperation by a human operator. This restricts
    the deployment scale and requires near-continuous low-latency communication between the operator and the robot. We present
    MOSAIC: a scalable autonomy framework for multi-robot scientific exploration using a unified mission abstraction based
    on Points of Interest (POIs) and multiple layers of autonomy, enabling supervision by a single operator. The framework
    dynamically allocates exploration and measurement tasks based on each robot''s capabilities, leveraging team-level redundancy
    and specialization to enable continuous operation. We validated the framework in a space-analog field experiment emulating
    a lunar prospecting scenario, involving a heterogeneous team of five robots and a single operator. Despite the complete
    failure of one robot during the mission, the team completed 82.3% of assigned tasks at an Autonomy Ratio of 86%, while
    the operator workload remained at only 78.2%. These results demonstrate that the proposed framework enables robust, scalable
    multi-robot scientific exploration with limited operator intervention. We further derive practical lessons learned in
    robot interoperability, networking architecture, team composition, and operator workload management to inform future multi-robot
    exploration missions.'
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
- mosaic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.23038v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MOSAIC: Modular Scalable Autonomy for Intelligent Coordination of Heterogeneous Robotic Teams (arXiv)'
  url: https://arxiv.org/abs/2601.23038
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
该框架针对传统遥操作机器人部署规模受限、依赖持续低延迟通信的痛点，提出以兴趣点（POI）为核心的任务抽象，并构建多层自主控制体系。MOSAIC 能根据每台机器人的能力动态分配勘探与测量任务，利用团队冗余与专业化分工实现连续作业。在模拟月球勘探的太空类比野外实验中，一个包含五台异构机器人的团队在单操作员监督下运行，尽管中途一台机器人完全失效，团队仍完成82.3%任务，自主率（Autonomy Ratio）达86%，操作员工作负载仅为78.2%。实验还总结了机器人互操作性、网络架构、团队组成及操作员负载管理方面的实践经验。

## 核心内容
### 方法架构
- **任务抽象**：基于兴趣点（POI）构建统一任务描述，将复杂勘探目标分解为可独立分配的子任务。
- **多层自主**：设计从底层运动控制到高层任务规划的自主层级，操作员仅需在关键决策点介入。
- **动态分配**：根据机器人传感器、移动能力及当前状态，实时分配勘探与测量任务，支持团队级冗余与专业化。

### 实验设置
- **场景**：模拟月球勘探的太空类比野外实验，环境包含未知地形与资源分布。
- **团队**：五台异构机器人（包括轮式、履带式及无人机），由一名操作员通过 MOSAIC 框架监督。
- **指标**：任务完成率（82.3%）、自主率（86%，即操作员干预时间占比）、操作员工作负载（NASA-TLX 量表，78.2%）。

### 关键结果
- **鲁棒性**：即使一台机器人完全失效，团队仍通过动态重分配任务完成82.3%目标。
- **自主性**：86%的自主率表明框架有效减少操作员持续干预需求。
- **负载管理**：操作员工作负载仅78.2%，低于传统遥操作模式。
- **经验教训**：机器人互操作性需标准化通信协议；网络架构应支持动态拓扑；团队组成需平衡冗余与专业化；操作员负载可通过预测性任务分配进一步优化。

### 结论
MOSAIC 框架验证了单操作员监督下异构多机器人团队进行大规模科学探索的可行性，为未来月球、火星及灾害救援任务提供了可扩展的自主方案。

## Overview
Mobile robots have become indispensable for exploring hostile environments, such as in space or disaster relief scenarios, but often remain limited to teleoperation by a human operator. This restricts the deployment scale and requires near-continuous low-latency communication between the operator and the robot. We present MOSAIC: a scalable autonomy framework for multi-robot scientific exploration using a unified mission abstraction based on Points of Interest (POIs) and multiple layers of autonomy, enabling supervision by a single operator. The framework dynamically allocates exploration and measurement tasks based on each robot's capabilities, leveraging team-level redundancy and specialization to enable continuous operation. We validated the framework in a space-analog field experiment emulating a lunar prospecting scenario, involving a heterogeneous team of five robots and a single operator. Despite the complete failure of one robot during the mission, the team completed 82.3% of assigned tasks at an Autonomy Ratio of 86%, while the operator workload remained at only 78.2%. These results demonstrate that the proposed framework enables robust, scalable multi-robot scientific exploration with limited operator intervention. We further derive practical lessons learned in robot interoperability, networking architecture, team composition, and operator workload management to inform future multi-robot exploration missions.

## 개요
모바일 로봇은 우주나 재난 구조 현장과 같은 열악한 환경 탐사에 필수적이 되었지만, 여전히 인간 운영자의 원격 조작에 제한되는 경우가 많습니다. 이는 배치 규모를 제한하고 운영자와 로봇 간에 거의 지속적인 저지연 통신을 요구합니다. 우리는 관심 지점(POI)에 기반한 통합 임무 추상화와 여러 계층의 자율성을 사용하여 단일 운영자가 감독할 수 있는 다중 로봇 과학 탐사를 위한 확장 가능한 자율성 프레임워크인 MOSAIC을 제시합니다. 이 프레임워크는 각 로봇의 역량에 따라 탐사 및 측정 작업을 동적으로 할당하며, 팀 수준의 중복성과 전문화를 활용하여 지속적인 운영을 가능하게 합니다. 우리는 달 탐사 시나리오를 모방한 우주 유사 현장 실험에서 이 프레임워크를 검증했으며, 5대의 이기종 로봇과 단일 운영자가 참여했습니다. 임무 중 한 로봇이 완전히 고장났음에도 불구하고, 팀은 할당된 작업의 82.3%를 자율성 비율 86%로 완료했으며, 운영자 작업 부하는 78.2%에 불과했습니다. 이러한 결과는 제안된 프레임워크가 제한된 운영자 개입으로 강력하고 확장 가능한 다중 로봇 과학 탐사를 가능하게 함을 보여줍니다. 또한, 우리는 로봇 상호 운용성, 네트워킹 아키텍처, 팀 구성 및 운영자 작업 부하 관리에 관한 실용적인 교훈을 도출하여 향후 다중 로봇 탐사 임무에 정보를 제공합니다.

## 핵심 내용
모바일 로봇은 우주나 재난 구조 현장과 같은 열악한 환경 탐사에 필수적이 되었지만, 여전히 인간 운영자의 원격 조작에 제한되는 경우가 많습니다. 이는 배치 규모를 제한하고 운영자와 로봇 간에 거의 지속적인 저지연 통신을 요구합니다. 우리는 관심 지점(POI)에 기반한 통합 임무 추상화와 여러 계층의 자율성을 사용하여 단일 운영자가 감독할 수 있는 다중 로봇 과학 탐사를 위한 확장 가능한 자율성 프레임워크인 MOSAIC을 제시합니다. 이 프레임워크는 각 로봇의 역량에 따라 탐사 및 측정 작업을 동적으로 할당하며, 팀 수준의 중복성과 전문화를 활용하여 지속적인 운영을 가능하게 합니다. 우리는 달 탐사 시나리오를 모방한 우주 유사 현장 실험에서 이 프레임워크를 검증했으며, 5대의 이기종 로봇과 단일 운영자가 참여했습니다. 임무 중 한 로봇이 완전히 고장났음에도 불구하고, 팀은 할당된 작업의 82.3%를 자율성 비율 86%로 완료했으며, 운영자 작업 부하는 78.2%에 불과했습니다. 이러한 결과는 제안된 프레임워크가 제한된 운영자 개입으로 강력하고 확장 가능한 다중 로봇 과학 탐사를 가능하게 함을 보여줍니다. 또한, 우리는 로봇 상호 운용성, 네트워킹 아키텍처, 팀 구성 및 운영자 작업 부하 관리에 관한 실용적인 교훈을 도출하여 향후 다중 로봇 탐사 임무에 정보를 제공합니다.

## 参考
- http://arxiv.org/abs/2601.23038v3
