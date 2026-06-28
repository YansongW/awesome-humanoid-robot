---
$id: ent_paper_kawaharazuka_mevius2_practical_open_source_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MEVIUS2: Practical Open-Source Quadruped Robot with Sheet Metal Welding and
    Multimodal Perception'
  zh: MEVIUS2：具有钣金焊接和多模态感知的实用开源四足机器人
  ko: 'MEVIUS2: 판금 용접 및 다중 모달 지각을 갖춘 실용적인 오픈소스 사족 로봇'
summary:
  en: Kawaharazuka et al. present MEVIUS2, a Spot-sized open-source quadruped robot
    built primarily with sheet-metal-welded and machined aluminum components that
    can all be procured through e-commerce, and validate its rough-terrain locomotion
    and LiDAR/HDR-camera perception capabilities.
  zh: Kawaharazuka等人提出了MEVIUS2，一种与Spot尺寸相当的开源四足机器人，主要由可通过电子商务采购的钣金焊接和机加工铝制部件构成，并验证其在崎岖地形运动和LiDAR/HDR相机感知方面的能力。
  ko: Kawaharazuka 등은 전자상거래를 통해 조달 가능한 판금 용접 및 가공 알루미늄 부품으로 주로 제작된 Spot 크기의 오픈소스 사족
    로봇 MEVIUS2를 제시하고 거친 지형 이동 및 LiDAR/HDR 카메라 지각 능력을 검증하였다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided abstract and metadata; full paper not independently
    reviewed. Component list, institutional affiliations, and cited comparisons require
    human verification before promotion to verified.; approved by autonomous review
    workflow.
sources:
- id: src_001
  type: paper
  title: 'MEVIUS2: Practical Open-Source Quadruped Robot with Sheet Metal Welding
    and Multimodal Perception'
  url: https://arxiv.org/abs/2603.22031
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

MEVIUS2 is an open-source quadruped robot developed by Kawaharazuka, Yoneda, Inoue, Suzuki, Oda, and Okada from The University of Tokyo. The platform is designed to be comparable in size to Boston Dynamics' Spot, with the key distinction that all structural and electronic components can be ordered through e-commerce services. The body structure primarily uses A7075 aluminum alloy and A5052 sheet metal, joined by sheet metal welding and machining, yielding a large, durable frame while reducing part count relative to conventional designs.

The robot is actuated by Robstride03 motors and powered by 24V/12V LiPo batteries with CAN-USB interfaces. For perception, MEVIUS2 integrates dual Livox Mid-360 LiDARs and a Tier IV C1 HDR camera, all processed on an NVIDIA Jetson. Locomotion is trained end-to-end with reinforcement learning in IsaacGym, validated in MuJoCo, and then deployed on the real robot. The authors experimentally demonstrate traversal over various rough terrains and showcase environmental perception capabilities. All hardware designs, software, and training environments are released open-source via GitHub and supplementary materials.

## Key Contributions

- Spot-sized, fully open-source quadruped robot constructed primarily from metal.
- Use of sheet metal welding to reduce part count and enable a large, durable structure.
- Integration of multimodal perception with dual LiDARs and an HDR RGB camera.
- End-to-end e-commerce procurement of structural and electronic components.
- Open release of hardware, software, and RL training environments.

## Relevance to Humanoid Robotics

Although MEVIUS2 is a quadruped platform, its fabrication and integration approach is directly transferable to humanoid robotics. The use of sheet metal welding and aluminum machining to build a large, low-cost, durable structure from commercially available parts addresses the same mass-production and scalability challenges faced by humanoid robots. The paper demonstrates that a complete legged robot can be sourced through standard e-commerce supply chains, which is relevant to humanoid manufacturing and supply-chain design.

Furthermore, the tight integration of multimodal perception—including LiDAR and HDR cameras—on a legged platform mirrors the sensing requirements for humanoid robots operating in unstructured environments. The reinforcement-learning-based locomotion pipeline (IsaacGym training, MuJoCo validation, real-robot transfer) is also broadly applicable to bipedal and humanoid locomotion development.
