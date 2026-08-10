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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.23038v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (892 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2601.23038v3

## 개요
이 프레임워크는 기존 원격 조작 로봇의 배포 규모 제한과 지속적인 저지연 통신 의존성이라는 문제점을 해결하기 위해, 관심 지점(POI)을 핵심으로 하는 작업 추상화를 제안하고 다층 자율 제어 체계를 구축한다. MOSAIC은 각 로봇의 능력에 따라 탐사 및 측정 작업을 동적으로 할당하며, 팀의 중복성과 전문화된 분업을 활용하여 연속 작업을 구현한다. 달 탐사를 모사한 우주 유사 야외 실험에서, 이종 로봇 5대로 구성된 팀이 단일 운영자의 감독 하에 운영되었고, 중간에 한 대의 로봇이 완전히 고장났음에도 팀은 82.3%의 작업을 완료했으며, 자율 비율(Autonomy Ratio)은 86%, 운영자 작업 부하는 78.2%에 불과했다. 실험은 또한 로봇 상호 운용성, 네트워크 아키텍처, 팀 구성 및 운영자 부하 관리에 관한 실질적인 경험을 정리했다.

## 핵심 내용
### 방법 아키텍처
- **작업 추상화**: 관심 지점(POI)을 기반으로 통합 작업 설명을 구축하고, 복잡한 탐사 목표를 독립적으로 할당 가능한 하위 작업으로 분해한다.
- **다층 자율성**: 하위 수준의 운동 제어부터 상위 수준의 작업 계획까지 자율 계층을 설계하여, 운영자는 핵심 의사 결정 지점에서만 개입하면 된다.
- **동적 할당**: 로봇의 센서, 이동 능력 및 현재 상태에 따라 탐사 및 측정 작업을 실시간으로 할당하며, 팀 수준의 중복성과 전문화를 지원한다.

### 실험 설정
- **시나리오**: 달 탐사를 모사한 우주 유사 야외 실험으로, 환경에는 미지의 지형과 자원 분포가 포함된다.
- **팀**: 이종 로봇 5대(바퀴형, 궤도형, 드론 포함)로 구성되며, 한 명의 운영자가 MOSAIC 프레임워크를 통해 감독한다.
- **지표**: 작업 완료율(82.3%), 자율 비율(86%, 즉 운영자 개입 시간 비율), 운영자 작업 부하(NASA-TLX 척도, 78.2%).

### 주요 결과
- **견고성**: 한 대의 로봇이 완전히 고장났음에도 팀은 동적 재할당을 통해 82.3%의 목표를 완료했다.
- **자율성**: 86%의 자율 비율은 프레임워크가 운영자의 지속적인 개입 필요성을 효과적으로 줄였음을 보여준다.
- **부하 관리**: 운영자 작업 부하는 78.2%로, 전통적인 원격 조작 방식보다 낮다.
- **교훈**: 로봇 상호 운용성은 표준화된 통신 프로토콜이 필요하며, 네트워크 아키텍처는 동적 토폴로지를 지원해야 하고, 팀 구성은 중복성과 전문화의 균형을 유지해야 하며, 운영자 부하는 예측적 작업 할당을 통해 더욱 최적화할 수 있다.

### 결론
MOSAIC 프레임워크는 단일 운영자 감독 하에 이종 다중 로봇 팀이 대규모 과학 탐사를 수행할 수 있는 가능성을 검증했으며, 향후 달, 화성 및 재난 구조 임무를 위한 확장 가능한 자율 솔루션을 제공한다.
