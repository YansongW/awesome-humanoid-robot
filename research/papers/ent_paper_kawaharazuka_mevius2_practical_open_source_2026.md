---
$id: ent_paper_kawaharazuka_mevius2_practical_open_source_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MEVIUS2: Practical Open-Source Quadruped Robot with Sheet Metal Welding and Multimodal Perception'
  zh: MEVIUS2：具有钣金焊接和多模态感知的实用开源四足机器人
  ko: 'MEVIUS2: 판금 용접 및 다중 모달 지각을 갖춘 실용적인 오픈소스 사족 로봇'
summary:
  en: Kawaharazuka et al. present MEVIUS2, a Spot-sized open-source quadruped robot built primarily with sheet-metal-welded
    and machined aluminum components that can all be procured through e-commerce, and validate its rough-terrain locomotion
    and LiDAR/HDR-camera perception capabilities.
  zh: Kawaharazuka 等人提出了 MEVIUS2，一款尺寸与 Boston Dynamics Spot 相当的开源四足机器人。其结构主要采用钣金焊接和机加工铝材，所有部件均可通过电商平台采购。核心贡献在于实现了大型、高耐久性的机器人本体，并集成了
    LiDAR 与高动态范围相机，具备粗糙地形行走与多模态感知能力。
  ko: Kawaharazuka 등은 전자상거래를 통해 조달 가능한 판금 용접 및 가공 알루미늄 부품으로 주로 제작된 Spot 크기의 오픈소스 사족 로봇 MEVIUS2를 제시하고 거친 지형 이동 및 LiDAR/HDR
    카메라 지각 능력을 검증하였다.
domains:
- 03_manufacturing_processes
- 02_components
- 05_mass_production
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- process
- system
tags:
- quadruped_robot
- open_source_hardware
- sheet_metal_welding
- aluminum_machining
- multimodal_perception
- lidar
- hdr_camera
- reinforcement_learning
- e_commerce_procurement
- isaacgym
- mujoco
- rough_terrain_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.22031v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (611 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MEVIUS2: Practical Open-Source Quadruped Robot with Sheet Metal Welding and Multimodal Perception'
  url: https://arxiv.org/abs/2603.22031
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
现有开源四足机器人多依赖 3D 打印，导致结构脆弱且难以放大尺寸，通常体型较小。少数金属构件机器人也缺乏多模态传感器，实用性不足。MEVIUS2 通过钣金焊接与金属加工技术，在减少零件数量的同时实现了大型且坚固的机身，其尺寸与 Spot 相当。该机器人集成了 LiDAR 和高动态范围相机，能够详细感知周围环境。实验验证了其在多种粗糙地形上的行走能力及环境感知能力，所有硬件、软件和训练环境均已开源。

## 核心内容
### 背景与动机
- 现有开源四足机器人多采用 3D 打印，结构脆弱，难以放大尺寸，导致体型普遍较小。
- 少数金属构件机器人仍存在体型小、缺乏多模态传感器的问题，实用性受限。

### MEVIUS2 设计
- **结构**：主要采用钣金焊接与机加工铝材，所有结构部件均可通过电商平台订购。该设计在减少零件数量的同时，实现了与 Boston Dynamics Spot 相当的大型、高耐久性机身。
- **感知**：集成了 LiDAR 与高动态范围（HDR）相机，能够对周围环境进行详细感知，提升了实用性。

### 实验验证
- 实验验证了 MEVIUS2 在多种粗糙地形上的行走能力。
- 同时展示了其环境感知能力。

### 开源信息
- 所有硬件、软件和训练环境均可从补充材料或 GitHub 仓库（https://github.com/haraduka/mevius2）获取。

## Overview
Various quadruped robots have been developed to date, and thanks to reinforcement learning, they are now capable of traversing diverse types of rough terrain. In parallel, there is a growing trend of releasing these robot designs as open-source, enabling researchers to freely build and modify robots themselves. However, most existing open-source quadruped robots have been designed with 3D printing in mind, resulting in structurally fragile systems that do not scale well in size, leading to the construction of relatively small robots. Although a few open-source quadruped robots constructed with metal components exist, they still tend to be small in size and lack multimodal sensors for perception, making them less practical. In this study, we developed MEVIUS2, an open-source quadruped robot with a size comparable to Boston Dynamics' Spot, whose structural components can all be ordered through e-commerce services. By leveraging sheet metal welding and metal machining, we achieved a large, highly durable body structure while reducing the number of individual parts. Furthermore, by integrating sensors such as LiDARs and a high dynamic range camera, the robot is capable of detailed perception of its surroundings, making it more practical than previous open-source quadruped robots. We experimentally validated that MEVIUS2 can traverse various types of rough terrain and demonstrated its environmental perception capabilities. All hardware, software, and training environments can be obtained from Supplementary Materials or https://github.com/haraduka/mevius2.

## 参考
- http://arxiv.org/abs/2603.22031v1

## 개요
기존 오픈소스 사족 보행 로봇은 대부분 3D 프린팅에 의존하여 구조가 취약하고 크기를 확장하기 어려워 일반적으로 체구가 작습니다. 소수의 금속 부품 로봇도 다중 모달 센서가 부족하여 실용성이 충분하지 않습니다. MEVIUS2는 판금 용접과 금속 가공 기술을 통해 부품 수를 줄이면서도 Spot과 비슷한 크기의 대형이면서 견고한 본체를 구현했습니다. 이 로봇은 LiDAR와 고동적 범위 카메라를 통합하여 주변 환경을 상세히 인식할 수 있습니다. 실험을 통해 다양한 거친 지형에서의 보행 능력과 환경 인식 능력을 검증했으며, 모든 하드웨어, 소프트웨어 및 훈련 환경이 오픈소스로 공개되었습니다.

## 핵심 내용
### 배경 및 동기
- 기존 오픈소스 사족 보행 로봇은 대부분 3D 프린팅을 사용하여 구조가 취약하고 크기를 확장하기 어려워 체구가 일반적으로 작습니다.
- 소수의 금속 부품 로봇도 여전히 체구가 작고 다중 모달 센서가 부족하여 실용성이 제한적입니다.

### MEVIUS2 설계
- **구조**: 주로 판금 용접과 기계 가공 알루미늄을 사용하며, 모든 구조 부품은 전자상거래 플랫폼에서 주문할 수 있습니다. 이 설계는 부품 수를 줄이면서 Boston Dynamics Spot과 비슷한 대형이면서 고내구성의 본체를 구현합니다.
- **인식**: LiDAR와 고동적 범위(HDR) 카메라를 통합하여 주변 환경을 상세히 인식할 수 있어 실용성을 높였습니다.

### 실험 검증
- 실험을 통해 MEVIUS2가 다양한 거친 지형에서 보행할 수 있는 능력을 검증했습니다.
- 동시에 환경 인식 능력도 입증했습니다.

### 오픈소스 정보
- 모든 하드웨어, 소프트웨어 및 훈련 환경은 보충 자료 또는 GitHub 저장소(https://github.com/haraduka/mevius2)에서 확인할 수 있습니다.
