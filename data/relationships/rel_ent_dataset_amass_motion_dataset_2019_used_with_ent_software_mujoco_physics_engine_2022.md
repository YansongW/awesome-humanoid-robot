---
$id: rel_ent_dataset_amass_motion_dataset_2019_used_with_ent_software_mujoco_physics_engine_2022
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_dataset_amass_motion_dataset_2019
  name:
    en: AMASS Motion Dataset
    zh: AMASS 动作数据集
    ko: AMASS 모션 데이터셋
target:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
    ko: MuJoCo 물리 엔진
domains:
  source:
  - 04_data_collection
  - 07_ai_models_algorithms
  target:
  - 08_software_middleware
  - 07_ai_models_algorithms
description:
  en: AMASS motions are used to seed MuJoCo simulations for humanoid tracking.
  zh: AMASS动作用于在MuJoCo仿真中初始化人形跟踪。
  ko: AMASS 동작은 MuJoCo 시뮬레이션에서 휨로봇 추적을 위한 시드를 만드는 데 사용됩니다.
verification:
  confidence: medium
  notes: bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review
  status: partially_verified
  sources: []
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-02T00:21:22.207515+00:00'
sources:
- type: website
  url: ''
  description: Workflow relationship curated from public project pages and literature.
  id: curated_workflow_relationship
---





