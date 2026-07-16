---
$id: rel_ent_robot_system_openloong_uses_ent_method_whole_body_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_openloong
  name:
    en: OpenLoong (Qinglong) Open-Source Humanoid Robot
    zh: OpenLoong / 青龙开源人形机器人
target:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: OpenLoong's OpenLoong-Dyn-Control framework implements whole-body control (WBC) with walking, jumping
    and blind obstacle-stepping examples validated on a physical prototype.
  zh: OpenLoong 的 OpenLoong-Dyn-Control 框架实现全身控制（WBC），提供行走/跳跃/盲踩障碍示例并已在实物样机验证。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/openloong-qinglong.md 确认 WBC 框架与实物样机验证。
sources:
- id: src_001
  type: website
  title: OpenLoong-Dyn-Control GitHub Repository
  url: https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md
  accessed_at: '2026-07-01'
---
