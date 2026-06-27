---
$id: rel_ent_paper_wei_hmc_learning_heterogeneous_met_2025_evaluates_on_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_wei_hmc_learning_heterogeneous_met_2025
  name:
    en: 'HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation'
    zh: HMC：面向接触密集型移动操作任务的异构元控制学习
    ko: 'HMC: 접촉이 풍부한 로코 매니퓰레이션을 위한 이종 메타 제어 학습'
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 humanoid robot
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: HMC is validated on a real Unitree G1 humanoid across contact-rich loco-manipulation
    tasks.
  zh: HMC 在真实的 Unitree G1 人形机器人上验证了接触密集型移动操作任务。
  ko: HMC는 접촉이 풍부한 로코 매니퓰레이션 작업에서 실제 Unitree G1 휴머노이드로 검증되었다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Key contribution 4: ''Real-world
    validation on a Unitree G1 humanoid across contact-rich tasks such as wiping,
    bottle lifting, and drawer opening.'''
sources:
- id: src_001
  type: paper
  title: 'HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation'
  url: https://arxiv.org/abs/2511.14756
  date: '2025'
  accessed_at: '2026-06-26'
---


