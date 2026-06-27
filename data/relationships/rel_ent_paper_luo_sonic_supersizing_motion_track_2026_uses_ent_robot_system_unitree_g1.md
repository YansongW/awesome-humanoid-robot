---
$id: rel_ent_paper_luo_sonic_supersizing_motion_track_2026_uses_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_luo_sonic_supersizing_motion_track_2026
  name:
    en: 'SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control'
    zh: SONIC：通过超大规模运动跟踪实现自然人形全身控制
    ko: 'SONIC: 자연스러운 휴머노이드 전신 제어를 위한 모션 트래킹 초대규모 확장'
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: Deploys the trained policy on the 29-actuated-joint Unitree G1 humanoid and
    reports sim-to-real results.
  zh: 在具有 29 个驱动关节的 Unitree G1 人形机器人上部署训练策略并报告仿真到现实的迁移结果。
  ko: 29개 구동 관절을 가진 Unitree G1 휴머노이드에 학습된 정책을 배포하고 시뮬레이션-실제 전이 결과를 보고한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Components listed in metadata
    include ''Unitree G1 humanoid (29 actuated joints)''; abstract notes real-world
    deployment and robust sim-to-real transfer.'
sources:
- id: src_001
  type: paper
  title: 'SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control'
  url: https://arxiv.org/abs/2511.07820
  date: '2026'
  accessed_at: '2026-06-26'
---


