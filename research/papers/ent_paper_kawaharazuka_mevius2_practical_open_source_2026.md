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
  zh: Kawaharazuka等人提出了MEVIUS2，一种与Spot尺寸相当的开源四足机器人，主要由可通过电子商务采购的钣金焊接和机加工铝制部件构成，并验证其在崎岖地形运动和LiDAR/HDR相机感知方面的能力。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.22031v1.
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
Various quadruped robots have been developed to date, and thanks to reinforcement learning, they are now capable of traversing diverse types of rough terrain. In parallel, there is a growing trend of releasing these robot designs as open-source, enabling researchers to freely build and modify robots themselves. However, most existing open-source quadruped robots have been designed with 3D printing in mind, resulting in structurally fragile systems that do not scale well in size, leading to the construction of relatively small robots. Although a few open-source quadruped robots constructed with metal components exist, they still tend to be small in size and lack multimodal sensors for perception, making them less practical. In this study, we developed MEVIUS2, an open-source quadruped robot with a size comparable to Boston Dynamics' Spot, whose structural components can all be ordered through e-commerce services. By leveraging sheet metal welding and metal machining, we achieved a large, highly durable body structure while reducing the number of individual parts. Furthermore, by integrating sensors such as LiDARs and a high dynamic range camera, the robot is capable of detailed perception of its surroundings, making it more practical than previous open-source quadruped robots. We experimentally validated that MEVIUS2 can traverse various types of rough terrain and demonstrated its environmental perception capabilities. All hardware, software, and training environments can be obtained from Supplementary Materials or https://github.com/haraduka/mevius2.

## 核心内容
Various quadruped robots have been developed to date, and thanks to reinforcement learning, they are now capable of traversing diverse types of rough terrain. In parallel, there is a growing trend of releasing these robot designs as open-source, enabling researchers to freely build and modify robots themselves. However, most existing open-source quadruped robots have been designed with 3D printing in mind, resulting in structurally fragile systems that do not scale well in size, leading to the construction of relatively small robots. Although a few open-source quadruped robots constructed with metal components exist, they still tend to be small in size and lack multimodal sensors for perception, making them less practical. In this study, we developed MEVIUS2, an open-source quadruped robot with a size comparable to Boston Dynamics' Spot, whose structural components can all be ordered through e-commerce services. By leveraging sheet metal welding and metal machining, we achieved a large, highly durable body structure while reducing the number of individual parts. Furthermore, by integrating sensors such as LiDARs and a high dynamic range camera, the robot is capable of detailed perception of its surroundings, making it more practical than previous open-source quadruped robots. We experimentally validated that MEVIUS2 can traverse various types of rough terrain and demonstrated its environmental perception capabilities. All hardware, software, and training environments can be obtained from Supplementary Materials or https://github.com/haraduka/mevius2.

## 参考
- http://arxiv.org/abs/2603.22031v1

